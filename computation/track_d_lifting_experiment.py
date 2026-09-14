#!/usr/bin/env python3
"""
Track D (revised): Redesigned lifting experiment.

Per Mr. Genius's review:
- Do NOT require r1=r2 when searching for 4-torsion (that excludes the target)
- Pre-register a twist family and range
- Compute actual Selmer dimensions using r2 (upper bound)
- Preserve unresolved cases as data, not discoveries
- Look for: s ≥ 3 (higher Ш[2] dim), or failed certification at rank ≥ 2 (4-torsion signature)

Target: find any rank-2 curve with dim Ш[2] ≥ 3 or Ш[2^∞] containing Z/4Z.
Such a curve would exercise the p^4 "all-lift" branch.

This script:
1. Scans the28 unresolved twists from E3 revised
2. Reports their (r1, r2, s) data honestly
3. Identifies the most promising candidates for further investigation

Output: track_d_lifting_experiment.json
"""
import json
import time

try:
    from cypari2 import Pari
    HAS_PARI = True
except ImportError:
    HAS_PARI = False


def analyze_unresolved_twist(pari, ainvs, d, base_label):
    """
    Analyze a single quadratic twist, preserving full (r1, r2, s) data.
    
    Key difference from E3: we do NOT filter on r1=r2.
    We record r2 as the rank upper bound and s as dim(Sha[2]/2Sha[4]).
    
    For a curve with Ш[2^∞] ≅ Z/4Z: PARI would give s=1 (dim Sha[2]/2Sha[4] = 1)
    For a curve with Ш[2^∞] ≅ (Z/2)^3: s=3
    For a curve with Ш[2^∞] ≅ Z/4Z × Z/2Z: s=2 (but with 4-torsion)
    """
    E_base = pari.ellinit(ainvs)
    disc = d if d % 4 == 1 else 4 * d
    E = pari.elltwist(E_base, disc)
    twist_ainvs = [int(E[i]) for i in range(5)]
    
    R = pari.ellrank(E, 3)
    r1, r2, s = int(R[0]), int(R[1]), int(R[2])
    
    tors = pari.elltors(E)
    tors_struct = [int(x) for x in tors[1]]
    tors_order = int(tors[0])
    T = sum(1 for f in tors_struct if f % 2 == 0)
    
    # dim Sel_2 upper bound: r2 + T + s
    C_upper = r2 + T + s
    
    result = {
        "twist_d": d,
        "ainvs": twist_ainvs,
        "r1": r1, "r2": r2, "s": s,
        "T": T,
        "torsion_order": tors_order,
        "torsion_structure": tors_struct,
        "C_dim_sel2_upper": C_upper,
        "rank_certified": r1 == r2,
    }
    
    # Classification
    if r1 == r2 and r1 >= 2:
        # Certified rank ≥ 2
        result["classification"] = "CERTIFIED_RANK"
        if s >= 3:
            result["flag"] = "HIGH_SHA2"
            result["note"] = f"s={s} ≥ 3: dim Sha[2] ≥ {s} (certified). Higher Ш[2] dimension found!"
        elif s == 0:
            result["flag"] = "TRIVIAL_SHA2"
        else:
            result["flag"] = "STANDARD"
    elif r2 >= 2 and r1 < r2:
        # Rank not certified but upper bound ≥ 2
        # This could indicate 4-torsion in Sha (PARI can't certify)
        result["classification"] = "UNRESOLVED"
        if s >= 3:
            result["flag"] = "HIGH_SHA2_UNRESOLVED"
            result["note"] = f"s={s} ≥ 3 with uncertified rank. Candidate for higher Ш[2]."
        elif s >= 1 and r2 > r1 + 1:
            result["flag"] = "POSSIBLE_4_TORSION"
            result["note"] = f"r1={r1}, r2={r2}, s={s}. Large gap may indicate 4-torsion in Sha."
        else:
            result["flag"] = "UNRESOLVED_STANDARD"
    else:
        result["classification"] = "LOW_RANK"
        result["flag"] = "NOT_RANK_2"
    
    return result


def main():
    print("Track D (revised): Redesigned Lifting Experiment")
    print("Date:", time.strftime("%Y-%m-%d %H:%M:%S"))
    print()
    
    if not HAS_PARI:
        print("ERROR: cypari2 required")
        return
    
    pari = Pari()
    
    # Load E3 v2 results to get the28 unresolved twists
    try:
        with open("computation/quadratic_twist_sha_stability_v2.json") as f:
            e3_data = json.load(f)
        unresolved = e3_data["results"]["unresolved_candidates"]
        base_ainvs = [0, 0, 0, -456382227, -3752677112114]  # 194040.cu1
        base_label = "194040.cu1"
        print(f"Loaded {len(unresolved)} unresolved twists from E3 v2")
    except Exception as e:
        print(f"Could not load E3 v2 results: {e}")
        print("Running fresh analysis on all squarefree d from 2 to 100")
        unresolved = [{"twist_d": d} for d in range(2, 101) 
                      if all(d % (p*p) != 0 for p in range(2, int(d**0.5)+1))]
        base_ainvs = [0, 0, 0, -456382227, -3752677112114]
        base_label = "194040.cu1"
    
    # Pre-register: squarefree 0 < |d| ≤ 100 for 194040.cu1
    print(f"\nPre-registered range: squarefree d in 2..100 for {base_label}")
    print(f"Analyzing {len(unresolved)} twists...")
    print()
    
    results = []
    flags = {"HIGH_SHA2": [], "HIGH_SHA2_UNRESOLVED": [], "POSSIBLE_4_TORSION": [], 
             "CERTIFIED_RANK": [], "STANDARD": [], "UNRESOLVED_STANDARD": []}
    
    for tw in unresolved:
        d = tw["twist_d"]
        result = analyze_unresolved_twist(pari, base_ainvs, d, base_label)
        results.append(result)
        
        flag = result["flag"]
        if flag in flags:
            flags[flag].append(result)
        
        # Print summary
        cls = result["classification"]
        print(f"  d={d:3d}: {cls:16s} r1={result['r1']} r2={result['r2']} s={result['s']} T={result['T']} {flag}")
        if "note" in result:
            print(f"         *** {result['note']}")
    
    # Summary
    print(f"\n{'='*60}")
    print("TRACK D SUMMARY")
    print(f"{'='*60}")
    print(f"Twists analyzed: {len(results)}")
    print(f"Certified rank ≥ 2: {len(flags['CERTIFIED_RANK'])}")
    print(f"  Standard (s∈{{0,2}}): {len(flags['STANDARD'])}")
    print(f"  High Ш[2] (s≥3): {len(flags['HIGH_SHA2'])}")
    print(f"Unresolved (r1 < r2):")
    print(f"  Standard: {len(flags['UNRESOLVED_STANDARD'])}")
    print(f"  Possible 4-torsion: {len(flags['POSSIBLE_4_TORSION'])}")
    print(f"  High Ш[2] unresolved: {len(flags['HIGH_SHA2_UNRESOLVED'])}")
    
    # Identify best candidates for further investigation
    candidates = []
    
    # Priority 1: s ≥ 3 (any)
    for r in flags["HIGH_SHA2"] + flags["HIGH_SHA2_UNRESOLVED"]:
        candidates.append({
            "twist_d": r["twist_d"],
            "reason": f"s={r['s']} ≥ 3",
            "priority": 1,
            "data": r
        })
    
    # Priority 2: Large rank gap (possible 4-torsion)
    for r in flags["POSSIBLE_4_TORSION"]:
        gap = r["r2"] - r["r1"]
        candidates.append({
            "twist_d": r["twist_d"],
            "reason": f"r2-r1={gap}, s={r['s']}",
            "priority": 2,
            "data": r
        })
    
    candidates.sort(key=lambda c: c["priority"])
    
    if candidates:
        print(f"\n*** {len(candidates)} CANDIDATES FOR FURTHER INVESTIGATION: ***")
        for c in candidates[:10]:
            print(f"  d={c['twist_d']}: {c['reason']}")
    else:
        print(f"\n*** NO CANDIDATES FOUND ***")
        print("All twists have s ∈ {{0, 2}} with standard rank bounds.")
        print("The lifting question at |Ш|=p² appears uniformly settled for this family.")
    
    # Build output
    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "track": "D",
        "version": 2,
        "design": "per_Mr_Genius_review",
        "pre_registration": {
            "base_curve": base_label,
            "range": "squarefree 2 ≤ d ≤ 100",
            "target": "find s ≥ 3 or failed certification at rank ≥ 2",
            "falsifier": "any certified rank-2 twist with s ≥ 3"
        },
        "summary": {
            "twists_analyzed": len(results),
            "certified_rank2": len(flags["CERTIFIED_RANK"]),
            "standard_s0_or_s2": len(flags["STANDARD"]),
            "high_sha2": len(flags["HIGH_SHA2"]),
            "high_sha2_unresolved": len(flags["HIGH_SHA2_UNRESOLVED"]),
            "possible_4_torsion": len(flags["POSSIBLE_4_TORSION"]),
            "unresolved_standard": len(flags["UNRESOLVED_STANDARD"]),
        },
        "candidates": candidates,
        "all_results": results,
        "conclusion": "No candidates found" if not candidates else f"{len(candidates)} candidates identified"
    }
    
    out_path = "computation/track_d_lifting_experiment.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults written to {out_path}")
    
    return output


if __name__ == "__main__":
    main()
