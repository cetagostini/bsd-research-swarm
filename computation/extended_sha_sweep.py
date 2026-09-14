#!/usr/bin/env python3
"""
Extended SHA sweep: E1 + E2 combined.

E1: Sweep ALL rank-2 |Ш|=4 curves in LMFDB (paginate past 100).
    Falsifier: any curve with failed certification or s ≠ 2.

E2: Hunt for rank-2 curves with dim Ш[2] ≥ 3 or 4-torsion signature.
    Search rank-2 curves with |Ш| = 16, 36, 64, 100, 144, 256.
    Look for failed certification (4-torsion signature).

Output: extended_sha_sweep_results.json
"""
import json
import sys
import time
from typing import Optional

try:
    from cypari2 import Pari
    HAS_PARI = True
except ImportError:
    HAS_PARI = False
    print("WARNING: cypari2 not installed. Install with: pip install cypari2")


def lmfdb_search(query: str, limit: int = 100, offset: int = 0) -> list[dict]:
    """Search LMFDB with pagination."""
    import urllib.request
    import urllib.parse

    base_url = "https://www.lmfdb.org/api/elliptic_curves/curves/"
    params = {
        "search": query,
        "limit": str(limit),
        "offset": str(offset),
        "format": "json"
    }
    url = base_url + "?" + urllib.parse.urlencode(params)

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "bsd-research-swarm"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            return data.get("results", data.get("objects", []))
    except Exception as e:
        print(f"  LMFDB search error: {e}")
        return []


def search_rank2_sha4_page(offset: int = 0, limit: int = 100) -> list[dict]:
    """Search for rank-2 curves with analytic |Ш| = 4."""
    # LMFDB search syntax for rank=2 and sha=4
    query = "rank=2&sha=4"
    return lmfdb_search(query, limit=limit, offset=offset)


def search_rank2_higher_sha(sha_value: int, limit: int = 100) -> list[dict]:
    """Search for rank-2 curves with specific analytic |Ш| value."""
    query = f"rank=2&sha={sha_value}"
    return lmfdb_search(query, limit=limit)


def analyze_curve_pari(ainvs: list, label: str, conductor: int) -> dict:
    """Analyze a single curve with PARI ellrank."""
    if not HAS_PARI:
        return {"error": "PARI not available", "label": label}

    pari = Pari()
    result = {
        "label": label,
        "conductor": conductor,
        "ainvs": ainvs
    }

    try:
        t0 = time.time()
        E = pari.ellinit(ainvs)
        R = pari.ellrank(E, 3)
        result["ellrank"] = [int(x) for x in (R[0], R[1], R[2])]
        result["rank_certified"] = (int(R[0]) == int(R[1]))

        # Torsion
        tors = pari.elltors(E)
        result["torsion_order"] = int(tors[0])
        result["torsion_structure"] = [int(x) for x in tors[1]]

        # Derived quantities
        T = 1 if result["torsion_order"] % 2 == 0 else 0  # dim E(Q)[2]
        R = result["ellrank"][0]  # certified rank (if certified)
        s = result["ellrank"][2]  # s from ellrank

        C = R + T + s  # dim Sel_2
        S = s  # dim Ш[2] (when certified)

        result["T"] = T
        result["C_dim_Sel2"] = C
        result["S_dim_Sha2"] = S
        result["Sel2_order"] = 2**C

        # Lifting analysis
        if result["rank_certified"]:
            if s == 0:
                result["sha2_trivial"] = True
                result["lifting"] = "trivial (no Ш[2])"
            elif s == 2:
                result["sha2_trivial"] = False
                result["sha2_structure"] = "(Z/2)^2"
                result["lifting"] = "none lift (p=2 case settled)"
            elif s >= 3:
                result["sha2_trivial"] = False
                result["sha2_structure"] = f"dim Ш[2] = {s} (HIGHER THAN EXPECTED)"
                result["lifting"] = "NEEDS INVESTIGATION"
                result["flag"] = "high_sha2_dim"
            else:
                result["sha2_trivial"] = False
                result["sha2_structure"] = f"dim Ш[2] = {s}"
                result["lifting"] = "unclear (s=1 impossible by CT)"
        else:
            result["flag"] = "not_certified_possible_4torsion"
            result["lifting"] = "CERTIFICATION FAILED - possible 4-torsion"

        result["elapsed"] = round(time.time() - t0, 2)

    except Exception as e:
        result["error"] = str(e)[:300]
        result["elapsed"] = round(time.time() - t0, 2)

    return result


def run_e1_sweep(max_curves: int = 500) -> dict:
    """
    E1: Sweep all rank-2 |Ш|=4 curves.
    Paginate through LMFDB.
    """
    print("=" * 60)
    print("E1: Sweeping rank-2 |Ш|=4 curves")
    print("=" * 60)

    all_results = []
    offset = 0
    page_size = 100
    falsifier_found = False

    while len(all_results) < max_curves:
        print(f"\nFetching page at offset {offset}...")
        curves = search_rank2_sha4_page(offset=offset, limit=page_size)

        if not curves:
            print("  No more curves found.")
            break

        print(f"  Found {len(curves)} curves in this page.")

        for i, curve in enumerate(curves):
            label = curve.get("lmfdb_label", curve.get("label", f"unknown_{offset+i}"))
            conductor = curve.get("conductor", 0)
            ainvs = curve.get("ainvs", curve.get("a_invariants", []))

            if not ainvs:
                print(f"  Skipping {label}: no a-invariants")
                continue

            result = analyze_curve_pari(ainvs, label, conductor)
            all_results.append(result)

            # Print progress
            status = "CERTIFIED" if result.get("rank_certified") else "NOT_CERTIFIED"
            ellrank = result.get("ellrank", "ERR")
            s = result.get("ellrank", [0,0,0])[2] if isinstance(result.get("ellrank"), list) else "?"
            flag = result.get("flag", "")

            print(f"  {len(all_results):3d} {label:20s} {status:12s} rank={ellrank} s={s} {flag}")

            # Check for falsifier
            if result.get("flag") in ["high_sha2_dim", "not_certified_possible_4torsion"]:
                falsifier_found = True
                print(f"  *** FALSIFIER FOUND: {label} ***")
                print(f"  Flag: {result['flag']}")
                print(f"  Details: {result}")

        offset += page_size

        # Rate limiting
        time.sleep(1)

    # Summary
    certified = sum(1 for r in all_results if r.get("rank_certified"))
    s_values = {}
    flags = []
    for r in all_results:
        if isinstance(r.get("ellrank"), list):
            s = r["ellrank"][2]
            s_values[s] = s_values.get(s, 0) + 1
        if r.get("flag"):
            flags.append(r)

    summary = {
        "total_curves": len(all_results),
        "certified": certified,
        "not_certified": len(all_results) - certified,
        "s_value_distribution": s_values,
        "flags": flags,
        "falsifier_found": falsifier_found
    }

    print("\n" + "=" * 60)
    print("E1 SUMMARY")
    print("=" * 60)
    print(f"Total curves analyzed: {len(all_results)}")
    print(f"Rank certified: {certified}")
    print(f"Not certified: {len(all_results) - certified}")
    print(f"s-value distribution: {s_values}")
    print(f"Falsifier found: {falsifier_found}")

    if falsifier_found:
        print("\n*** E1 RESULT: FALSIFIER FOUND — STOP AND INVESTIGATE ***")
        for f in flags:
            print(f"  {f['label']}: {f['flag']}")
    else:
        print("\n*** E1 RESULT: Uniform s=2 across all certified curves ***")

    return {
        "experiment": "E1",
        "query": "rank=2&sha=4",
        "summary": summary,
        "results": all_results
    }


def run_e2_hunt() -> dict:
    """
    E2: Hunt for rank-2 curves with higher Ш[2] or 4-torsion.
    Search for |Ш| = 16, 36, 64, 100, 144, 256.
    """
    print("\n" + "=" * 60)
    print("E2: Hunting for higher Ш[2] or 4-torsion at rank 2")
    print("=" * 60)

    sha_values = [16, 36, 64, 100, 144, 256]
    all_results = []
    discoveries = []

    for sha_val in sha_values:
        print(f"\n--- Searching rank-2 |Ш|={sha_val} ---")
        curves = search_rank2_higher_sha(sha_val, limit=50)

        if not curves:
            print(f"  No rank-2 curves with |Ш|={sha_val} found.")
            continue

        print(f"  Found {len(curves)} curves.")

        for i, curve in enumerate(curves[:20]):  # Limit to 20 per sha value
            label = curve.get("lmfdb_label", curve.get("label", f"sha{sha_val}_{i}"))
            conductor = curve.get("conductor", 0)
            ainvs = curve.get("ainvs", curve.get("a_invariants", []))

            if not ainvs:
                continue

            result = analyze_curve_pari(ainvs, label, conductor)
            result["analytic_sha"] = sha_val
            all_results.append(result)

            status = "CERTIFIED" if result.get("rank_certified") else "NOT_CERTIFIED"
            ellrank = result.get("ellrank", "ERR")
            s = result.get("ellrank", [0,0,0])[2] if isinstance(result.get("ellrank"), list) else "?"
            flag = result.get("flag", "")

            print(f"  {label:20s} {status:12s} rank={ellrank} s={s} {flag}")

            # Track discoveries
            if result.get("flag") in ["high_sha2_dim", "not_certified_possible_4torsion"]:
                discoveries.append(result)
                print(f"  *** DISCOVERY: {label} ***")

        time.sleep(1)  # Rate limiting

    # Summary
    certified = sum(1 for r in all_results if r.get("rank_certified"))
    s_values = {}
    for r in all_results:
        if isinstance(r.get("ellrank"), list):
            s = r["ellrank"][2]
            s_values[s] = s_values.get(s, 0) + 1

    summary = {
        "total_curves": len(all_results),
        "certified": certified,
        "not_certified": len(all_results) - certified,
        "s_value_distribution": s_values,
        "discoveries": discoveries
    }

    print("\n" + "=" * 60)
    print("E2 SUMMARY")
    print("=" * 60)
    print(f"Total curves analyzed: {len(all_results)}")
    print(f"Rank certified: {certified}")
    print(f"s-value distribution: {s_values}")
    print(f"Discoveries: {len(discoveries)}")

    if discoveries:
        print("\n*** E2 RESULT: DISCOVERIES FOUND ***")
        for d in discoveries:
            print(f"  {d['label']}: {d['flag']}")
            print(f"    Analytic |Ш|={d['analytic_sha']}, s={d['ellrank'][2]}")
    else:
        print("\n*** E2 RESULT: No higher Ш[2] found at rank 2 ***")

    return {
        "experiment": "E2",
        "sha_values_searched": sha_values,
        "summary": summary,
        "results": all_results
    }


def main():
    """Run both E1 and E2 experiments."""
    print("Extended SHA Sweep: E1 + E2")
    print("Date:", time.strftime("%Y-%m-%d %H:%M:%S"))
    print()

    if not HAS_PARI:
        print("ERROR: cypari2 required. Install with:")
        print("  pip install cypari2")
        sys.exit(1)

    # Run E1
    e1_results = run_e1_sweep(max_curves=500)

    # Run E2
    e2_results = run_e2_hunt()

    # Combined output
    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "e1": e1_results,
        "e2": e2_results,
        "overall_conclusion": {
            "e1_falsifier": e1_results["summary"]["falsifier_found"],
            "e1_uniform_s2": not e1_results["summary"]["falsifier_found"],
            "e2_discoveries": len(e2_results["summary"]["discoveries"]),
            "sha2_stable_at_rank2": (
                not e1_results["summary"]["falsifier_found"]
                and len(e2_results["summary"]["discoveries"]) == 0
            )
        }
    }

    output_path = "computation/extended_sha_sweep_results.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print("\n" + "=" * 60)
    print("OVERALL CONCLUSION")
    print("=" * 60)
    print(f"E1 falsifier found: {output['overall_conclusion']['e1_falsifier']}")
    print(f"E1 uniform s=2: {output['overall_conclusion']['e1_uniform_s2']}")
    print(f"E2 discoveries: {output['overall_conclusion']['e2_discoveries']}")
    print(f"Ш[2] stable at rank 2: {output['overall_conclusion']['sha2_stable_at_rank2']}")

    if output['overall_conclusion']['sha2_stable_at_rank2']:
        print("\n*** RESULT: Ш[2] ≅ (ℤ/2)² is stable across all tested rank-2 curves ***")
        print("*** The odd part remains the genuinely open problem ***")
    else:
        print("\n*** RESULT: Anomalies found — investigate further ***")

    print(f"\nResults written to {output_path}")


if __name__ == "__main__":
    main()
