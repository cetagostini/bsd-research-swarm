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
    
    # Classification using the PARI identities.
    #
    # PARI defines (from ellrank docs):
    #   r2 = C - T - s    where C = dim Sel_2, T = dim E(Q)[2], s = dim(Sha[2]/2Sha[4])
    #
    # Kummer exact sequence gives:
    #   C = T + R + S     where R = actual Mordell-Weil rank, S = dim Sha[2]
    #
    # Combining:
    #   T + r2 + s = T + R + S    (since C = T + r2 + s from PARI's definition)
    #   => S = r2 + s - R         (dim Sha[2])
    #   And S = s + d             where d = dim(2Sha[4])
    #   => d = r2 - R             (dim(2Sha[4]))
    #
    # Note: d = r2 - R does NOT depend on s. It only depends on r2 and R.
    # 2Sha[4] is an F_2-vector space (killed by 2); it cannot contain a Z/4 summand.
    #
    # PARI says s is "conjecturally even" — the nondegenerate quotient Sha[2]/2Sha[4]
    # has even dimension (alternating form), but the full Sha[2] need not.
    # We cannot assume nondegeneracy on all of Sha[2] to force parity on S.
    #
    # The 4-torsion criterion: dim(2Sha[4]) = r2 - R > 0, i.e. R < r2.
    # Nonzero lifting is possible when r2 > R (regardless of s).
    #
    # Verified: 194040.cu1 (r1=r2=2, s=2, T=1):
    #   C = 1+2+2 = 5, S = 2+2-2 = 2, d = 2-2 = 0. Correct.

    if r1 == r2:
        # Certified rank: R = r1 = r2 exactly.
        dim_sha2 = r2 + s - r1   # = s (since r1=r2)
        dim_2sha4 = r2 - r1      # = 0 (since r1=r2)
        result["dim_sha2"] = dim_sha2
        result["dim_2sha4"] = dim_2sha4
        if r1 >= 2:
            result["classification"] = "CERTIFIED_RANK"
            if s >= 3:
                result["flag"] = "HIGH_SHA2"
                result["note"] = f"s={s} >= 3: dim Sha[2] = {dim_sha2} (certified). Higher Sha[2] dimension found!"
            elif s == 0:
                # r1=r2 and s=0 => dim Sha[2] = 0, Sha[2]=0 exactly.
                result["flag"] = "TRIVIAL_SHA2"
                result["note"] = f"s=0, rank={r1} certified. Sha[2]=0 (exactly)."
            else:
                result["flag"] = "STANDARD"
        else:
            result["classification"] = "CERTIFIED_LOW_RANK"
            result["flag"] = "NOT_RANK_2"
    elif r2 >= 2 and r1 < r2:
        # Rank not certified: R in [r1, r2].
        # For each possible R:
        #   dim Sha[2] = r2 + s - R
        #   dim(2Sha[4]) = r2 - R
        # 4-torsion requires R < r2 (i.e. dim(2Sha[4]) > 0).
        dim_sha2_at_r1 = r2 + s - r1
        dim_2sha4_at_r1 = r2 - r1
        dim_sha2_at_r2 = s          # r2 + s - r2 = s
        dim_2sha4_at_r2 = 0         # r2 - r2 = 0
        result["classification"] = "UNRESOLVED"
        result["dim_sha2_at_r1"] = dim_sha2_at_r1
        result["dim_2sha4_at_r1"] = dim_2sha4_at_r1
        result["dim_sha2_at_r2"] = dim_sha2_at_r2
        result["dim_2sha4_at_r2"] = dim_2sha4_at_r2
        # For intermediate R values (if r2 - r1 > 1)
        result["possible_ranks"] = list(range(r1, r2 + 1))
        result["dim_2sha4_table"] = {R: r2 - R for R in range(r1, r2 + 1)}

        if s >= 3:
            result["flag"] = "HIGH_SHA2_UNRESOLVED"
            result["note"] = (f"s={s} >= 3 with uncertified rank. "
                             f"dim Sha[2] in [{dim_sha2_at_r2}, {dim_sha2_at_r1}] depending on rank. "
                             f"Candidate for higher Sha[2].")
        elif dim_2sha4_at_r1 > 0:
            # At rank r1, dim(2Sha[4]) = r2 - r1 > 0 => possible 4-torsion.
            # At rank r2, dim(2Sha[4]) = 0 => no 4-torsion.
            # Note: nonzero lifting is possible for ANY s when r2 > R.
            result["flag"] = "POSSIBLE_4_TORSION"
            result["note"] = (f"r1={r1}, r2={r2}, s={s}. "
                             f"4-torsion possible iff R < r2: "
                             f"dim(2Sha[4]) table by R: {result['dim_2sha4_table']}. "
                             f"Needs independent rank determination.")
        else:
            result["flag"] = "UNRESOLVED_STANDARD"
    else:
        result["classification"] = "LOW_RANK"
        result["flag"] = "NOT_RANK_2"
        result["dim_sha2"] = None
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
    print("Identity (PARI): C = T + r2 + s, S = r2 + s - R, d = r2 - R")
    print("4-torsion criterion: dim(2Sha[4]) = r2 - R > 0, i.e. R < r2.")
    print("Nonzero lifting is possible for ANY s when r2 > R.")
    print("All candidates need independent rank determination.")
    
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
                       "dim(2Sha[4]) = r2 - R (does not depend on s). "
                       "4-torsion criterion: R < r2. "
                       "Nonzero lifting is possible for any s when r2 > R.")
    }
    
    out_path = "computation/track_d_lifting_experiment.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults written to {out_path}")
    
    return output


def test_base_curve_identity():
    """Regression test: verify PARI identity on 194040.cu1 (d=1, untwisted).

    Per Mr. Genius: r1=r2=2, s=2, T=1, C=5.
    Expected: dim_sha2=2, dim_2sha4=0.
    """
    if not HAS_PARI:
        print("SKIPPED: PARI not available")
        return True

    pari = Pari()
    base_ainvs = [0, 0, 0, -456382227, -3752677112114]  # 194040.cu1
    result = analyze_unresolved_twist(pari, base_ainvs, 1, "194040.cu1")

    assert result["r1"] == 2, f"r1 should be 2, got {result['r1']}"
    assert result["r2"] == 2, f"r2 should be 2, got {result['r2']}"
    assert result["s"] == 2, f"s should be 2, got {result['s']}"
    assert result["T"] == 1, f"T should be 1, got {result['T']}"
    assert result["rank_certified"] is True, "Rank should be certified"

    # C = T + r2 + s = 1 + 2 + 2 = 5
    C = result["T"] + result["r2"] + result["s"]
    assert C == 5, f"C should be 5, got {C}"

    # dim Sha[2] = r2 + s - R = 2 + 2 - 2 = 2
    assert result["dim_sha2"] == 2, f"dim_sha2 should be 2, got {result['dim_sha2']}"
    # dim(2Sha[4]) = r2 - R = 2 - 2 = 0
    assert result["dim_2sha4"] == 0, f"dim_2sha4 should be 0, got {result['dim_2sha4']}"

    print("PASSED: test_base_curve_identity")
    return True


def run_tests():
    """Run Track D tests."""
    print("=" * 40)
    print("Running Track D tests")
    print("=" * 40)
    results = []
    results.append(("base_curve_identity", test_base_curve_identity()))
    print(f"\n{'='*40}")
    all_pass = all(r[1] for r in results)
    print(f"Results: {sum(1 for _, v in results if v)}/{len(results)} passed")
    if not all_pass:
        print("FAILURES detected!")
    return all_pass


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        success = run_tests()
        sys.exit(0 if success else 1)
    else:
        main()
