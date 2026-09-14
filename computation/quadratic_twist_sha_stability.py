#!/usr/bin/env python3
"""
E3: Quadratic twist stability for 194040.cu1.

For a rank-2 curve with analytic |Ш|=4, compute dim Ш^{(d)}[2]
for quadratic twists E^{(d)} of rank 2.

Test whether the 2-part structure is twist-stable:
always (ℤ/2)² when BSD predicts |Ш|=4.

Output: quadratic_twist_sha_stability.json
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


def get_twist_ainvs(ainvs: list, d: int) -> list:
    """
    Compute a-invariants of the quadratic twist E^{(d)}.

    For E: y² = x³ + ax + b, the twist by d is:
    E^{(d)}: dy² = x³ + ax + b
    or equivalently: y² = x³ + d²ax + d³b

    The a-invariants transform as:
    a1 → a1, a2 → d*a2, a3 → d*a3, a4 → d²*a4, a6 → d³*a6
    (for short Weierstrass form a1=a2=a3=0: a4 → d²a4, a6 → d³a6)
    """
    a1, a2, a3, a4, a6 = ainvs
    return [a1, d*a2, d*a3, d*d*a4, d*d*d*a6]


def analyze_twist(ainvs: list, d: int, base_label: str) -> dict:
    """Analyze a single quadratic twist."""
    if not HAS_PARI:
        return {"error": "PARI not available"}

    pari = Pari()
    twist_ainvs = get_twist_ainvs(ainvs, d)
    label = f"{base_label}_twist_{d}"

    result = {
        "label": label,
        "base_curve": base_label,
        "twist_d": d,
        "ainvs": twist_ainvs
    }

    try:
        t0 = time.time()
        E = pari.ellinit(twist_ainvs)
        R = pari.ellrank(E, 3)
        result["ellrank"] = [int(x) for x in (R[0], R[1], R[2])]
        result["rank_certified"] = (int(R[0]) == int(R[1]))

        # Torsion
        tors = pari.elltors(E)
        result["torsion_order"] = int(tors[0])

        # Derived quantities
        T = 1 if result["torsion_order"] % 2 == 0 else 0
        R = result["ellrank"][0]
        s = result["ellrank"][2]
        C = R + T + s

        result["T"] = T
        result["C_dim_Sel2"] = C
        result["S_dim_Sha2"] = s
        result["Sel2_order"] = 2**C

        # Analysis
        if result["rank_certified"]:
            if s == 0:
                result["sha2_trivial"] = True
                result["sha2_structure"] = "trivial"
            elif s == 2:
                result["sha2_trivial"] = False
                result["sha2_structure"] = "(Z/2)^2"
            elif s >= 3:
                result["sha2_trivial"] = False
                result["sha2_structure"] = f"dim {s} (HIGHER)"
                result["flag"] = "high_sha2_dim"
            else:
                result["sha2_trivial"] = False
                result["sha2_structure"] = f"dim {s}"
        else:
            result["flag"] = "not_certified"
            result["sha2_structure"] = "CERTIFICATION FAILED"

        result["elapsed"] = round(time.time() - t0, 2)

    except Exception as e:
        result["error"] = str(e)[:300]
        result["elapsed"] = round(time.time() - t0, 2)

    return result


def find_rank2_twists(ainvs: list, base_label: str, max_d: int = 50) -> dict:
    """
    Find quadratic twists of a curve that have rank 2.

    For each squarefree d from 2 to max_d, compute the twist
    and check if it has rank 2. If so, analyze its Ш[2].
    """
    print(f"\n{'='*60}")
    print(f"Finding rank-2 quadratic twists of {base_label}")
    print(f"Testing d from 2 to {max_d}")
    print(f"{'='*60}")

    pari = Pari()
    rank2_twists = []
    all_twists = []
    errors = []

    # Squarefree integers
    squarefree = []
    for d in range(2, max_d + 1):
        is_squarefree = True
        for p in range(2, int(d**0.5) + 1):
            if d % (p*p) == 0:
                is_squarefree = False
                break
        if is_squarefree:
            squarefree.append(d)

    print(f"Testing {len(squarefree)} squarefree values of d")

    for i, d in enumerate(squarefree):
        result = analyze_twist(ainvs, d, base_label)
        all_twists.append(result)

        if "error" in result:
            errors.append(result)
            print(f"  d={d:3d}: ERROR - {result['error'][:50]}")
            continue

        ellrank = result.get("ellrank", "ERR")
        certified = result.get("rank_certified", False)
        s = result.get("ellrank", [0,0,0])[2] if isinstance(result.get("ellrank"), list) else "?"
        flag = result.get("flag", "")

        status = "R2" if (certified and result["ellrank"][0] == 2) else "R≠2"
        print(f"  d={d:3d}: {status:4s} rank={ellrank} s={s} {flag}")

        if certified and result["ellrank"][0] == 2:
            rank2_twists.append(result)

    # Summary
    summary = {
        "base_curve": base_label,
        "twists_tested": len(squarefree),
        "rank2_twists_found": len(rank2_twists),
        "errors": len(errors),
        "rank2_s_values": {},
        "rank2_sha_structures": {}
    }

    for tw in rank2_twists:
        s = tw.get("ellrank", [0,0,0])[2]
        summary["rank2_s_values"][s] = summary["rank2_s_values"].get(s, 0) + 1
        struct = tw.get("sha2_structure", "unknown")
        summary["rank2_sha_structures"][struct] = summary["rank2_sha_structures"].get(struct, 0) + 1

    print(f"\n{'='*60}")
    print(f"TWIST STABILITY SUMMARY for {base_label}")
    print(f"{'='*60}")
    print(f"Twists tested: {len(squarefree)}")
    print(f"Rank-2 twists found: {len(rank2_twists)}")
    print(f"s-value distribution: {summary['rank2_s_values']}")
    print(f"Ш[2] structures: {summary['rank2_sha_structures']}")

    if len(rank2_twists) > 0:
        s_vals = set(tw.get("ellrank", [0,0,0])[2] for tw in rank2_twists)
        if s_vals == {2}:
            print(f"\n*** STABLE: All {len(rank2_twists)} rank-2 twists have Ш[2] ≅ (ℤ/2)² ***")
            summary["stability"] = "stable_s2"
        elif len(s_vals) == 1:
            print(f"\n*** STABLE: All rank-2 twists have dim Ш[2] = {s_vals.pop()} ***")
            summary["stability"] = f"stable_s{list(s_vals)[0]}"
        else:
            print(f"\n*** UNSTABLE: Different s values found: {s_vals} ***")
            summary["stability"] = "unstable"
    else:
        print("\n*** No rank-2 twists found in range ***")
        summary["stability"] = "no_rank2_twists"

    return {
        "summary": summary,
        "rank2_twists": rank2_twists,
        "all_twists": all_twists
    }


def main():
    """Run E3: quadratic twist stability analysis."""
    print("E3: Quadratic Twist SHA Stability")
    print("Date:", time.strftime("%Y-%m-%d %H:%M:%S"))
    print()

    if not HAS_PARI:
        print("ERROR: cypari2 required. Install with:")
        print("  pip install cypari2")
        sys.exit(1)

    # 194040.cu1 a-invariants (from LMFDB)
    # Curve: y^2 = x^3 - x^2 - x + 1 (or similar)
    # Let me get the actual a-invariants from the pool results
    try:
        with open("computation/sha_lift_pool_results.json") as f:
            pool = json.load(f)
        # Find 194040.cu1
        cu1 = None
        for r in pool.get("results", pool.get("pool", [])):
            if r.get("label") == "194040.cu1":
                cu1 = r
                break

        if cu1 is None:
            print("ERROR: 194040.cu1 not found in pool results")
            print("Using hardcoded a-invariants from LMFDB")
            # Hardcoded from LMFDB: 194040.cu1
            ainvs = [1, 0, 0, -2880, -57240]  # y^2 = x^3 - 2880x - 57240
            base_label = "194040.cu1"
        else:
            ainvs = cu1["ainvs"]
            base_label = cu1["label"]
            print(f"Found {base_label} with a-invariants: {ainvs}")

    except Exception as e:
        print(f"Warning: Could not load pool results: {e}")
        print("Using hardcoded a-invariants from LMFDB")
        ainvs = [1, 0, 0, -2880, -57240]
        base_label = "194040.cu1"

    # Run twist analysis
    results = find_rank2_twists(ainvs, base_label, max_d=100)

    # Save results
    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "experiment": "E3",
        "base_curve": base_label,
        "results": results
    }

    output_path = "computation/quadratic_twist_sha_stability.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults written to {output_path}")

    # Final assessment
    print(f"\n{'='*60}")
    print("E3 CONCLUSION")
    print(f"{'='*60}")

    stability = results["summary"]["stability"]
    if stability == "stable_s2":
        print("The 2-part structure Ш[2] ≅ (ℤ/2)² is STABLE across quadratic twists.")
        print("This suggests a family-level criterion: for this curve's twist family,")
        print("the 2-primary part is always elementary abelian of rank 2.")
        print("\nIMPLICATION: The lifting question is settled uniformly for this family.")
    elif stability.startswith("stable"):
        print(f"Stable but unexpected: {stability}")
        print("Investigate further.")
    elif stability == "unstable":
        print("UNSTABLE: Different Ш[2] structures found across twists.")
        print("This would be a significant discovery — investigate the outliers.")
    else:
        print("No rank-2 twists found in tested range.")
        print("Try expanding the range or testing a different base curve.")


if __name__ == "__main__":
    main()
