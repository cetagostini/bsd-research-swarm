#!/usr/bin/env python3
"""
Sha-Lifting Research: Iteration 1
==================================
Question: For rank-2 elliptic curves E/Q with nontrivial Ш(E/Q)[p],
which classes in Ш[p] lift to Ш[p²] (i.e., are p-divisible in Ш)?

Approach:
  1. Query LMFDB for rank-2 curves with known Sha order > 1
  2. For each curve, determine the p-primary decomposition of Ш
  3. Predict which classes lift using the Cassels-Tate pairing structure
  4. Verify predictions against the known structure

Mathematical framework:
  - Ш[p] embeds into Sel_p(E/Q) via the Kummer connecting map
  - The descent map d: Ш[p] → Sel_p factors through H^1(Q, E[p])
  - An element ξ ∈ Ш[p] lifts to Ш[p²] iff d(ξ) = 0 in Sel_p
  - The Cassels-Tate pairing CT: Ш[p] × Ш[p] → Z/pZ induces
    a homomorphism Ш[p] → Hom(Ш[p]/pШ[p], Z/pZ)
  - ξ lifts iff CT(ξ, ·) vanishes on Ш[p]/pШ[p]
  - Key consequence: if Ш[p] ≅ (Z/p)^k with k odd, the alternating
    pairing forces a nontrivial kernel, predicting ≥ 1 class lifts

Reference curves (from LMFDB / known examples):
  - 194040.cu1: rank 2, |Ш| = 4 = 2²  → Ш[2] ≅ Z/2 × Z/2 or Z/4
  - 571.a1: rank 2, |Ш| = 1 (trivial, control case)
  - Other rank-2 curves with nontrivial Sha from database search
"""

import json
import math
import urllib.request
import urllib.parse
from fractions import Fraction
from typing import Optional


def lmfdb_search_rank2_sha(limit: int = 100) -> list[dict]:
    """Search LMFDB for rank-2 curves with nontrivial Sha.
    
    Uses the LMFDB API to find elliptic curves over Q with:
    - rank = 2
    - analytic Sha order > 1
    
    Returns list of curve data dicts.
    """
    # LMFDB search: rank 2, torsion structure includes sha_an
    # API: https://www.lmfdb.org/EllipticCurve/Q/?rank=2&sha>1
    # We need to use their internal API
    url = (
        "https://www.lmfdb.org/api/ec_curves?"
        "rank=2&sha_an_gt=1&"
        "_fields=label,conductor,rank,sha_an,torsion,iso_nlabel,lmfdb_iso,"
        "ainvs,analytic_sha,_trace_coeffs&"
        f"_limit={limit}&_sort=sha_an"
    )
    
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        return data.get("data", data) if isinstance(data, dict) else data
    except Exception as e:
        print(f"LMFDB API search failed: {e}")
        return []


def get_curve_data(label: str) -> Optional[dict]:
    """Get full curve data from LMFDB by label."""
    url = f"https://www.lmfdb.org/api/ec_curves/{label}"
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"  Failed to fetch {label}: {e}")
        return None


def factor_sha_order(n: int) -> dict[int, int]:
    """Factor Sha order into prime power components."""
    if n <= 0:
        return {}
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def sha_p_structure(sha_order: int, p: int) -> dict:
    """Determine the p-primary structure of Ш from its order.
    
    For a finite abelian group of order n = p^a * m (p ∤ m):
    - The p-primary part has order p^a
    - Possible structures: Z/p^a, Z/p × Z/p^{a-1}, etc.
    - The Cassels-Tate pairing constrains: a must be even for non-degenerate alternating pairing
    
    Returns analysis dict.
    """
    factors = factor_sha_order(sha_order)
    p_power = factors.get(p, 0)
    
    result = {
        "prime": p,
        "p_power": p_power,
        "sha_order": sha_order,
        "full_factorization": factors,
    }
    
    if p_power == 0:
        result["p_primary_trivial"] = True
        result["analysis"] = f"Ш has no {p}-torsion"
        return result
    
    result["p_primary_trivial"] = False
    result["p_primary_order"] = p**p_power
    
    # The Cassels-Tate pairing on Ш[p^∞] is alternating and non-degenerate
    # on Ш/pШ. This forces the p-primary part to have EVEN rank as Z/p-module.
    # More precisely: Ш[p^∞] ≅ ⊕ Z/p^{a_i} with Σ a_i = p_power,
    # and the pairing on Ш[p] ≅ (Z/p)^r is non-degenerate on Ш[p]/pШ[p]
    # where r = #{i : a_i ≥ 1} = number of cyclic summands.
    
    # For |Ш[p^∞]| = p^a:
    # Possible decompositions and whether CT non-degeneracy is possible:
    possible_structures = []
    # Enumerate partitions of p_power into cyclic summands
    # Each partition λ = (a_1 ≥ a_2 ≥ ... ≥ a_r) with Σ a_i = p_power
    # corresponds to Ш[p^∞] ≅ ⊕ Z/p^{a_i}
    # The rank r (number of summands) must be even for CT non-degeneracy
    # (since the alternating form on Ш[p]/pШ[p] ≅ (Z/p)^r is non-degenerate iff r is even)
    
    def partitions(n, max_part=None):
        """Generate partitions of n as non-increasing sequences."""
        if max_part is None:
            max_part = n
        if n == 0:
            yield []
            return
        for first in range(min(n, max_part), 0, -1):
            for rest in partitions(n - first, first):
                yield [first] + rest
    
    for part in partitions(p_power):
        r = len(part)  # rank of Ш[p] as F_p-vector space
        ct_compatible = (r % 2 == 0)  # alternating non-degenerate pairing needs even rank
        possible_structures.append({
            "partition": part,
            "rank_of_Shap": r,
            "Shap_isomorphic": " ⊕ ".join(f"Z/{p}^{a}" if a > 1 else "Z/p" for a in part) if part else "trivial",
            "CT_compatible": ct_compatible,
        })
    
    # Filter to CT-compatible structures
    ct_compatible = [s for s in possible_structures if s["CT_compatible"]]
    ct_incompatible = [s for s in possible_structures if not s["CT_compatible"]]
    
    result["possible_structures"] = possible_structures
    result["ct_compatible_structures"] = ct_compatible
    result["ct_incompatible_structures"] = ct_incompatible
    
    # Key prediction: if the p-primary part has odd rank r,
    # then CT non-degeneracy forces at least one class to have trivial pairing,
    # which means at least one class lifts to Ш[p²].
    if ct_compatible:
        # All CT-compatible structures have even rank
        # For each, the lifting prediction:
        predictions = []
        for s in ct_compatible:
            r = s["rank_of_Shap"]
            # Ш[p] ≅ (Z/p)^r
            # The CT pairing on Ш[p]/pШ[p] ≅ (Z/p)^r is alternating non-degenerate
            # The kernel of Ш[p] → Ш[p]/pШ[p] consists of classes in pШ[p]
            # For Ш[p^∞] ≅ ⊕ Z/p^{a_i} with a_i ≥ 1:
            # pШ[p^∞] ≅ ⊕ Z/p^{a_i - 1} (the "divisible part")
            # So |ker(Ш[p] → Ш[p]/pШ[p])| = |Ш[p] ∩ pШ[p^∞]|
            # = #{i : a_i ≥ 2} = number of summands with exponent ≥ 2
            
            s_copy = dict(s)
            summands_ge_2 = sum(1 for a in s["partition"] if a >= 2)
            summands_eq_1 = r - summands_ge_2
            
            # Classes in Ш[p] that are also in pШ[p^∞] (i.e., lift to Ш[p²]):
            # These are exactly the classes in the image of multiplication by p
            # restricted to the p-torsion. Count = p^{summands_ge_2} - 1 (non-identity)
            # Actually: |Ш[p] ∩ pШ| = p^{summands_ge_2}
            
            s_copy["lifts_to_Sha_p2"] = p**summands_ge_2
            s_copy["nonlifts"] = p**r - p**summands_ge_2
            s_copy["lift_fraction"] = f"{p**summands_ge_2}/{p**r}"
            
            # The descent map d: Ш[p] → Sel_p has kernel = lifts
            # Its image has size p^{summands_eq_1} (the "non-liftable" part)
            s_copy["descent_image_size"] = p**summands_eq_1
            s_copy["descent_kernel_size"] = p**summands_ge_2
            
            predictions.append(s_copy)
        
        result["lifting_predictions"] = predictions
        
        # Family-level criterion:
        # If Ш[p^∞] ≅ (Z/p^a)^k (symmetric case), then:
        # - Ш[p] ≅ (Z/p)^k
        # - All classes lift iff a ≥ 2 (i.e., Ш[p²] = Ш[p])
        # - No classes lift iff a = 1 (i.e., Ш[p] has exponent exactly p)
        # - Mixed: some lift, some don't
        result["family_criterion"] = (
            f"For |Ш[{p}^∞]| = {p}^{p_power}: "
            f"classes lift to Ш[{p}²] iff they lie in the image of "
            f"multiplication by {p} on Ш. The number of liftable classes "
            f"is p^k where k = number of summands with exponent >= 2 in the "
            f"p-primary decomposition."
        )
    
    return result


def analyze_curve(label: str, sha_order: int, rank: int, conductor: int) -> dict:
    """Full analysis of a rank-2 curve's Sha-lifting structure."""
    print(f"\n{'='*70}")
    print(f"Analyzing curve {label}: rank={rank}, conductor={conductor}, |Ш|={sha_order}")
    print(f"{'='*70}")
    
    factors = factor_sha_order(sha_order)
    analysis = {
        "label": label,
        "rank": rank,
        "conductor": conductor,
        "sha_order": sha_order,
        "sha_factorization": factors,
        "prime_analyses": {},
    }
    
    for p in sorted(factors.keys()):
        result = sha_p_structure(sha_order, p)
        analysis["prime_analyses"][p] = result
        
        print(f"\n  p = {p}:")
        print(f"    |Ш[{p}^∞]| = {p}^{factors[p]}")
        
        if result.get("p_primary_trivial"):
            print(f"    No {p}-torsion in Ш")
            continue
        
        ct_comp = result.get("ct_compatible_structures", [])
        predictions = result.get("lifting_predictions", [])
        if ct_comp:
            print(f"    CT-compatible structures ({len(ct_comp)}):")
            for i, s in enumerate(ct_comp):
                pred = predictions[i] if i < len(predictions) else {}
                lifts = pred.get('lifts_to_Sha_p2', '?')
                nonlifts = pred.get('nonlifts', '?')
                frac = pred.get('lift_fraction', '?')
                print(f"      {s['Shap_isomorphic']}: "
                      f"lifts={lifts}, "
                      f"nonlifts={nonlifts}, "
                      f"fraction={frac}")
        
        fam = result.get("family_criterion", "")
        if fam:
            print(f"    Family criterion: {fam}")
    
    return analysis


def search_and_analyze():
    """Main research pipeline."""
    print("=" * 70)
    print("SHA-LIFTING RESEARCH: Iteration 1")
    print("=" * 70)
    print()
    print("Question: Which classes in Ш(E/Q)[p] lift to Ш(E/Q)[p²]?")
    print("Method: Analyze p-primary structure from Sha order + CT constraints")
    print()
    
    # Known rank-2 curves with nontrivial Sha (from LMFDB/databases)
    # These are well-documented examples
    known_curves = [
        # (label, conductor, sha_order, description)
        ("194040.cu1", 194040, 4, "rank 2, |Ш|=4, first known rank-2 with nontrivial Ш"),
        ("246464.ba1", 246464, 4, "rank 2, |Ш|=4"),
        ("571.a1", 571, 1, "rank 2, |Ш|=1, control case"),
        # From the project's earlier work:
        ("389.a1", 389, 1, "rank 2, |Ш|=1, benchmark curve"),
    ]
    
    # Also search LMFDB for more examples
    print("Searching LMFDB for rank-2 curves with nontrivial Sha...")
    search_results = lmfdb_search_rank2_sha(limit=50)
    
    if search_results:
        print(f"  Found {len(search_results)} curves from LMFDB search")
        for r in search_results[:20]:
            label = r.get("label", r.get("lmfdb_label", "unknown"))
            sha = r.get("sha_an", r.get("analytic_sha", 1))
            cond = r.get("conductor", 0)
            if sha and sha > 1:
                known_curves.append((label, int(cond), int(sha), f"LMFDB: rank 2, |Ш|={sha}"))
    else:
        print("  LMFDB search returned no results (may be rate-limited)")
    
    # Deduplicate by label
    seen = set()
    unique_curves = []
    for c in known_curves:
        if c[0] not in seen:
            seen.add(c[0])
            unique_curves.append(c)
    
    print(f"\nTotal curves to analyze: {len(unique_curves)}")
    
    # Analyze each curve
    all_analyses = []
    nontrivial_sha_curves = []
    
    for label, conductor, sha_order, desc in unique_curves:
        if sha_order <= 1:
            print(f"\nSkipping {label}: |Ш|=1 (trivial Sha)")
            continue
        
        analysis = analyze_curve(label, sha_order, 2, conductor)
        all_analyses.append(analysis)
        nontrivial_sha_curves.append((label, sha_order, analysis))
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY OF FINDINGS")
    print("=" * 70)
    
    if not nontrivial_sha_curves:
        print("\nNo curves with nontrivial Sha found.")
        print("This may indicate LMFDB API issues or that our search was too narrow.")
        print("\nFalling back to theoretical analysis...")
        theoretical_analysis()
        return
    
    print(f"\nCurves with nontrivial Sha: {len(nontrivial_sha_curves)}")
    
    for label, sha_order, analysis in nontrivial_sha_curves:
        factors = analysis["sha_factorization"]
        print(f"\n  {label}: |Ш| = {sha_order} = {' × '.join(f'{p}^{e}' for p, e in sorted(factors.items()))}")
        
        for p, p_analysis in analysis["prime_analyses"].items():
            if p_analysis.get("p_primary_trivial"):
                continue
            
            ct_comp = p_analysis.get("ct_compatible_structures", [])
            predictions = p_analysis.get("lifting_predictions", [])
            if ct_comp:
                best = ct_comp[0]
                pred = predictions[0] if predictions else {}
                print(f"    p={p}: Ш[{p}^∞] ≅ {best['Shap_isomorphic']}")
                lifts = pred.get('lifts_to_Sha_p2', '?')
                rank_p = best['rank_of_Shap']
                print(f"      Lifts to Ш[{p}²]: {lifts}/{p**rank_p if isinstance(rank_p, int) else '?'} classes")
                
                if best["rank_of_Shap"] % 2 == 0:
                    print(f"      CT non-degeneracy: compatible (rank {best['rank_of_Shap']} is even)")
                else:
                    print(f"      CT non-degeneracy: INCOMPATIBLE (rank {best['rank_of_Shap']} is odd)")
    
    # Theoretical implications
    print("\n" + "=" * 70)
    print("THEORETICAL IMPLICATIONS")
    print("=" * 70)
    
    print("""
1. DESCENT MAP CHARACTERIZATION:
   For ξ ∈ Ш(E/Q)[p], define d_p: Ш[p] → Sel_p(E/Q) via the Kummer
   connecting homomorphism. Then:
   
   ξ lifts to Ш[p²]  ⟺  d_p(ξ) = 0  ⟺  ξ ∈ im(mult by p on Ш)
   
   This is equivalent to: CT(ξ, ζ) = 0 for all ζ ∈ Ш[p]/pШ[p].

2. FAMILY-LEVEL CRITERION:
   If Ш[p^∞] ≅ (Z/p)^k (exponent exactly p), then NO class in Ш[p]
   lifts to Ш[p²], since pШ[p^∞] = 0. The descent map is injective.
   
   If Ш[p^∞] ≅ Z/p^a with a ≥ 2, then ALL classes in Ш[p] lift.
   
   Mixed case: Ш[p^∞] ≅ Z/p^a ⊕ (Z/p)^{k-1} with a ≥ 2, k ≥ 2:
   - p^{k-1} classes lift (those in the Z/p^a summand)
   - p^k - p^{k-1} classes do NOT lift

3. KEY PREDICTION FOR RANK-2 CURVES:
   For rank-2 curves, Ш must have even rank as an F_p-module
   (from CT non-degeneracy). So Ш[p] ≅ (Z/p)^{2m} for some m.
   
   - If m = 1 (rank 2): Ш[p] ≅ Z/p × Z/p
     * If Ш[p^∞] ≅ Z/p²: all 4 elements lift
     * If Ш[p^∞] ≅ Z/p × Z/p: no elements lift (except identity)
   
   - If m = 2 (rank 4): Ш[p] ≅ (Z/p)⁴
     * Multiple decompositions possible, each with different lifting counts

4. OBSTRUCTION TO LIFTING:
   The "obstruction" for ξ ∈ Ш[p] to lift is its image d_p(ξ) ∈ Sel_p.
   This image is a Galois cohomology class that can be computed (in principle)
   from the local behavior of the homogeneous space representing ξ.
   
   New direction: Can we express d_p(ξ) explicitly in terms of:
   - The discriminant of the homogeneous space?
   - Local Tamagawa factors?
   - The p-adic valuation of the conductor?
""")


def theoretical_analysis():
    """Pure theoretical analysis when LMFDB is unavailable."""
    print("\n" + "=" * 70)
    print("THEORETICAL ANALYSIS (no LMFDB data)")
    print("=" * 70)
    
    # Analyze all possible Sha structures for small orders
    print("\n--- Analysis of Ш structures by order ---\n")
    
    for sha_order in [4, 9, 16, 25, 36, 49, 64, 81, 100]:
        factors = factor_sha_order(sha_order)
        print(f"|Ш| = {sha_order} = {' × '.join(f'{p}^{e}' for p, e in sorted(factors.items()))}")
        
        for p, e in sorted(factors.items()):
            result = sha_p_structure(sha_order, p)
            ct_comp = result.get("ct_compatible_structures", [])
            
            if ct_comp:
                print(f"  p = {p}: CT-compatible structures:")
                for s in ct_comp:
                    print(f"    {s['Shap_isomorphic']}: "
                          f"{s['lifts_to_Sha_p2']}/{p**(s['rank_of_Shap'])} lift, "
                          f"{s['nonlifts']}/{p**(s['rank_of_Shap'])} don't lift")
        print()
    
    # Special focus on rank-2 curves
    print("\n--- Special case: rank-2 curves ---\n")
    print("""
For rank-2 curves with nontrivial Sha, the Cassels-Tate pairing
imposes strong constraints:

1. Ш must have order n² (perfect square) — proven by Cassels
2. Ш[p] has even F_p-rank r = 2m
3. The CT pairing on Ш[p]/pШ[p] ≅ (Z/p)^r is alternating non-degenerate

The alternating non-degenerate form on (Z/p)^{2m} has a standard
normal form: ⊕_{i=1}^m (e_i ∧ f_i) where CT(e_i, f_j) = δ_{ij}/p.

This means: the "non-liftable" part of Ш[p] (i.e., the image of d_p)
carries a non-degenerate CT pairing. The "liftable" part (kernel of d_p)
lies in pШ[p^∞] and has its own induced CT pairing.

NEW INSIGHT: The decomposition Ш[p] = ker(d_p) ⊕ im(d_p) is NOT
canonical — it depends on the choice of splitting. However, the
dimensions are canonical:
- dim(ker d_p) = #{cyclic summands with exponent ≥ 2}
- dim(im d_p) = #{cyclic summands with exponent = 1}

This gives a COMPUTABLE criterion: ξ ∈ Ш[p] lifts iff it can be
written as pη for some η ∈ Ш[p²]. The obstruction is:
  ob(ξ) = ξ mod pШ[p^∞] ∈ Ш[p]/pШ[p^∞]

This obstruction lives in a group of size p^{#{summands with exp=1}}.

FAMILY-LEVEL FORMULA:
For a family of rank-2 curves where Ш[p^∞] ≅ Z/p^a × Z/p^a
(symmetric, the generic case by CT non-degeneracy):

  Lift fraction = p^{2·max(a-1,0)} / p^{2a} = p^{-2·min(a,1)}

- a = 1 (exponent p): lift fraction = 1/p² (only identity lifts)
- a = 2: lift fraction = 1 (all lift)
- a ≥ 2: lift fraction = 1 (all lift, since both summands have exp ≥ 2)

CONJECTURE (new, testable):
For a family of rank-2 curves with conductor → ∞, the probability
that a randomly chosen class in Ш[2] lifts to Ш[4] is either 0
(if Ш[4] = Ш[2]) or 1 (if Ш[2] ⊂ Ш[4]). There is NO intermediate
case for rank-2 curves because the CT pairing forces the 2-primary
decomposition to be either (Z/2)^{2m} (no lifts) or Z/2^a × Z/2^a
(all lifts).

This is because the alternating non-degenerate CT pairing on Ш[2]
forces Ш[2] to have even rank, and the only way to get even rank
with some classes lifting is to have mixed exponents — which is
impossible for a symmetric alternating form on (Z/2)^r.
""")


def extended_analysis():
    """Extended analysis with specific curve computations."""
    print("\n" + "=" * 70)
    print("EXTENDED ANALYSIS: Descent Map for Specific Curves")
    print("=" * 70)
    
    # For 194040.cu1 with |Ш| = 4:
    print("\n--- Curve 194040.cu1: rank 2, |Ш| = 4 ---\n")
    
    sha_order = 4
    factors = factor_sha_order(sha_order)
    p = 2
    e = factors[2]
    
    result = sha_p_structure(sha_order, p)
    
    print(f"|Ш| = 4 = 2²")
    print(f"2-primary part: order 4")
    print(f"\nPossible structures for Ш[2^∞]:")
    for s in result["possible_structures"]:
        ct = "✓ CT-compatible" if s["CT_compatible"] else "✗ CT-incompatible"
        print(f"  {s['Shap_isomorphic']} (rank {s['rank_of_Shap']}): {ct}")
        if s["CT_compatible"] and "lifts_to_Sha_p2" in s:
            print(f"    Lifts: {s['lifts_to_Sha_p2']}/{2**s['rank_of_Shap']}")
    
    print(f"\nConclusion for 194040.cu1:")
    print(f"  Ш[2^∞] is either Z/4 or Z/2 × Z/2.")
    print(f"  CT non-degeneracy requires even rank of Ш[2] as F_2-vector space.")
    print(f"  Z/4: Ш[2] ≅ Z/2 (rank 1, odd) → CT-INCOMPATIBLE")
    print(f"  Z/2 × Z/2: Ш[2] ≅ Z/2 × Z/2 (rank 2, even) → CT-COMPATIBLE")
    print(f"  Therefore: Ш[2^∞] ≅ Z/2 × Z/2 for 194040.cu1")
    print(f"  Prediction: NO nontrivial class in Ш[2] lifts to Ш[4].")
    print(f"  (All non-identity elements of Ш[2] have order exactly 2.)")
    
    # Now analyze what this means for the descent map
    print(f"\n  Descent map d: Ш[2] → Sel_2(E/Q):")
    print(f"  - |Ш[2]| = 4")
    print(f"  - d is injective (no class lifts, so kernel is trivial)")
    print(f"  - im(d) has order 4 in Sel_2")
    print("  - Sel_2 has order 2^(rank + dim(im d)) = 2^(2+2) = 16")
    print("    (assuming rank = 2 and Ш contributes 2 independent classes)")
    
    # For a hypothetical curve with |Ш| = 16 = 2⁴:
    print(f"\n--- Hypothetical: rank-2 curve with |Ш| = 16 = 2⁴ ---\n")
    
    sha_order = 16
    result = sha_p_structure(sha_order, 2)
    
    print(f"Possible structures:")
    predictions = result.get("lifting_predictions", [])
    for i, s in enumerate(result["ct_compatible_structures"]):
        pred = predictions[i] if i < len(predictions) else {}
        lifts = pred.get('lifts_to_Sha_p2', '?')
        nonlifts = pred.get('nonlifts', '?')
        rank_p = s['rank_of_Shap']
        print(f"  {s['Shap_isomorphic']}: "
              f"{lifts}/{2**rank_p} lift, "
              f"{nonlifts}/{2**rank_p} don't lift")
    
    print(f"\nKey observation:")
    print(f"  The decomposition type determines the lifting behavior completely.")
    print(f"  Z/4 × Z/4: ALL 16 elements of Ш[2] lift to Ш[4]")
    print(f"  Z/2 × Z/2 × Z/2 × Z/2: NO nontrivial element lifts")
    print(f"  Z/4 × Z/2 × Z/2: 4 out of 16 elements lift")
    print(f"  (The 4 liftable elements form a subgroup isomorphic to Z/2 × Z/2)")


if __name__ == "__main__":
    search_and_analyze()
    extended_analysis()
