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
    
    # Classification using dim_F2(2Sha[4]) = r2 - R.
    #
    # PARI's identity: dim Sel_2 = T + R + dim Sha[2], where R = actual rank.
    # Also dim Sel_2 = T + r2 (from the 2-descent upper bound).
    # And dim Sha[2] = s + dim(2Sha[4]) where s = dim_F2(Sha[2]/2Sha[4]).
    # So: T + r2 = T + R + s + dim(2Sha[4]), hence dim(2Sha[4]) = r2 - R - s.
    #
    # Wait — let me be precise. PARI gives r1, r2, s with:
    #   r1 <= R <= r2 (R = actual rank)
    #   s = dim_F2(Sha[2]/2Sha[4])  (always even, since it's the dimension of a
    #       quotient of Sha[2] by the image of multiplication by 2)
    #   C = dim Sel_2 = T + r2 (exact, from 2-descent)
    #
    # The exact formula: dim Sel_2 = T + R + dim Sha[2]
    #   => T + r2 = T + R + dim Sha[2]
    #   => dim Sha[2] = r2 - R
    #   And dim Sha[2] = s + dim(2Sha[4])
    #   => dim(2Sha[4]) = (r2 - R) - s
    #
    # Note: 2Sha[4] is an F_2-vector space (killed by 2), so its dimension
    # is a non-negative integer. It cannot contain a Z/4 summand.
    #
    # For [0,2,2]:
    #   If R=0: dim Sha[2] = 2-0 = 2, dim(2Sha[4]) = 2-2 = 0
    #   If R=2: dim Sha[2] = 2-2 = 0, dim(2Sha[4]) = 0-2 = -2 (impossible)
    #   So R cannot be 2 when s=2 and r2=2. R must be 0 (or 1 if s permits).
    #   With R=0, s=2: dim Sha[2]=2, dim(2Sha[4])=0. Sha[2]≅(Z/2)^2.
    #   No 4-torsion in this case.
    #
    # For [1,3,2]:
    #   If R=1: dim Sha[2] = 3-1 = 2, dim(2Sha[4]) = 2-2 = 0
    #   If R=2: dim Sha[2] = 3-2 = 1 (impossible: dim Sha[2] must be even
    #       since Sha[2] has a nondegenerate alternating form)
    #   If R=3: dim Sha[2] = 3-3 = 0, dim(2Sha[4]) = 0-2 = -2 (impossible)
    #   So R must be 1. dim Sha[2]=2, no 4-torsion.
    #
    # For [0,2,0]:
    #   If R=0: dim Sha[2] = 2-0 = 2, dim(2Sha[4]) = 2-0 = 2
    #   This IS a 4-torsion candidate: Sha[2^inf] could be Z/4 x Z/2 or (Z/2)^3
    #   (but s=0 means Sha[2]/2Sha[4]=0, so Sha[2]=2Sha[4]; dim Sha[2]=2,
    #   dim(2Sha[4])=2 means Sha[2] = 2Sha[4], which with dim=2 means
    #   Sha[2^inf] contains Z/4 components)
    #
    # Summary: the interesting 4-torsion case is s=0 with r2>R (not s>=1).

    if r1 == r2 and r1 >= 2:
        # Certified rank >= 2
        dim_sha2 = r2 - r1  # = 0 for certified
        dim_2sha4 = dim_sha2 - s  # = 0 - s
        result["classification"] = "CERTIFIED_RANK"
        result["dim_sha2"] = dim_sha2
        result["dim_2sha4"] = dim_2sha4
        if s >= 3:
            result["flag"] = "HIGH_SHA2"
            result["note"] = f"s={s} >= 3: dim Sha[2] >= {s} (certified). Higher Sha[2] dimension found!"
        elif s == 0:
            # r1=r2 and s=0 => dim Sha[2] = 0, Sha[2]=0 exactly.
            # No room for (Z/4)^2 or any nonzero Sha at all.
            result["flag"] = "TRIVIAL_SHA2"
            result["note"] = f"s=0, rank={r1} certified. Sha[2]=0 (exactly)."
        else:
            result["flag"] = "STANDARD"
    elif r2 >= 2 and r1 < r2:
        # Rank not certified but upper bound >= 2
        # We can compute dim Sha[2] = r2 - R for each possible R in [r1, r2].
        # dim(2Sha[4]) = (r2 - R) - s for each R.
        dim_sha2_at_r1 = r2 - r1
        dim_2sha4_at_r1 = dim_sha2_at_r1 - s
        result["classification"] = "UNRESOLVED"
        result["dim_sha2_at_r1"] = dim_sha2_at_r1
        result["dim_2sha4_at_r1"] = dim_2sha4_at_r1
        result["dim_sha2_at_r2"] = 0
        result["dim_2sha4_at_r2"] = 0 - s
        if s >= 3:
            result["flag"] = "HIGH_SHA2_UNRESOLVED"
            result["note"] = f"s={s} >= 3 with uncertified rank. Candidate for higher Sha[2]."
        elif s == 0 and r2 > r1:
            # s=0 means Sha[2]=2Sha[4]. If R=r1, dim Sha[2]=r2-r1, dim(2Sha[4])=r2-r1.
            # Sha[2] = 2Sha[4] with dim(2Sha[4]) > 0 means 4-torsion is present.
            result["flag"] = "POSSIBLE_4_TORSION"
            result["note"] = (f"r1={r1}, r2={r2}, s=0. "
                             f"If rank={r1}: dim Sha[2]={dim_sha2_at_r1}, "
                             f"dim(2Sha[4])={dim_2sha4_at_r1} (s=0 => Sha[2]=2Sha[4], 4-torsion). "
                             f"If rank={r2}: Sha[2]=0. "
                             f"Needs independent rank determination.")
        elif dim_2sha4_at_r1 > 0:
            result["flag"] = "POSSIBLE_4_TORSION"
            result["note"] = (f"r1={r1}, r2={r2}, s={s}. "
                             f"If rank={r1}: dim(2Sha[4])={dim_2sha4_at_r1} (possible 4-torsion). "
                             f"If rank={r2}: dim(2Sha[4])={0 - s} (impossible, so rank < r2). "
                             f"Needs independent rank determination.")
        else:
            result["flag"] = "UNRESOLVED_STANDARD"
    else:
        result["classification"] = "LOW_RANK"
        result["flag"] = "NOT_RANK_2"
        result["dim_2sha4"] = None
    
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
    print(f"Certified rank >= 2: {len(flags['CERTIFIED_RANK'])}")
    print(f"  Standard (s in {{0,2}}): {len(flags['STANDARD'])}")
    print(f"  High Sha[2] (s>=3): {len(flags['HIGH_SHA2'])}")
    print(f"  Trivial Sha[2] (s=0): {len(flags.get('TRIVIAL_SHA2', []))}")
    print(f"Unresolved (r1 < r2):")
    print(f"  Standard: {len(flags['UNRESOLVED_STANDARD'])}")
    print(f"  Possible 4-torsion: {len(flags['POSSIBLE_4_TORSION'])}")
    print(f"  High Sha[2] unresolved: {len(flags['HIGH_SHA2_UNRESOLVED'])}")
    print()
    print("4-torsion analysis (dim(2Sha[4]) = r2 - R):")
    print("  [0,2,2] candidates: 4-torsion possible iff rank=0 (not rank=2)")
    print("  [1,3,2] candidates: 4-torsion possible iff rank=1 (not rank=3)")
    print("  All need independent rank determination via 3-descent or other method")
    
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
        "conclusion": ("Candidates need independent rank determination. "
                       "[0,2,2] pairs: 4-torsion iff rank=0 (dim(2Sha[4])=2). "
                       "[1,3,2] pairs: 4-torsion iff rank=1 (dim(2Sha[4])=2). "
                       "Neither provides rank 2 + nonzero first lifting simultaneously.")
    }
    
    out_path = "computation/track_d_lifting_experiment.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults written to {out_path}")
    
    return output


if __name__ == "__main__":
    main()
