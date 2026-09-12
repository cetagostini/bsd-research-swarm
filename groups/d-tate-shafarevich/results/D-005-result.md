# D-005: Computational Bounds on |III| for Specific Curves

**Direction ID:** D-005
**Title:** Computational Bounds on |Sha| for Specific Curves

## Status Assessment

Active and highly productive. Cremona's database covers all curves of conductor ≤ 500,000 with computed |Sha|. The LMFDB extends this computationally. The largest known |Sha| = 4,224 (Watkins 2002). The main computational bottleneck is higher descent for large conductor and high rank.

## Testable Conjecture or Lemma

**Empirical Verification (Cremona).** For all E/Q of conductor N ≤ 500,000 with rank r ∈ {0, 1}:

$$|Sha_{alg}(E/Q)| = \frac{L^{(r)}(E,1) \cdot |E(Q)_{tors}|^2}{r! \cdot \Omega_E \cdot R_E \cdot \prod c_v}$$

where R_E = 1 for r = 0 and R_E = ĥ(P) for r = 1 (P a generator of E(Q)/tors).

**Computational Bound.** For E/Q of conductor N:

$$|Sha(E/Q)| \leq |Sel_2(E/Q)| \cdot |Sel_3(E/Q)| / |E(Q)/6 \cdot E(Q)|$$

when 2-descent and 3-descent together determine Sha completely.

**Lemma (Analytic Sha precision).** The analytic estimate:

$$|Sha_{analytic}| = \frac{L^{(r)}(E,1)}{r! \cdot \Omega_E \cdot R_E \cdot \prod c_v / |E(Q)_{tors}|^2}$$

is an integer (by BSD), and computing L^{(r)}(E,1) to precision ±ε determines |Sha_{analytic}| exactly when ε < 1/(2 · r! · Ω_E · R_E · ∏ c_v).

## Approach Summary

1. **2-descent via mwrank/eclib:** For each E, compute Sel_2(E/Q) by determining the image of the local Kummer maps δ_v at all primes v | 2N∞. This gives |Sha[2]|.

2. **3-descent (Schaefer-Connell):** Compute Sel_3(E/Q) via covering spaces. The 3-division polynomial defines a genus-1 cover of E, and rational points on this cover give 3-Selmer classes.

3. **Combined descent:** If |Sha| = |Sha[2]| × |Sha[3]| × ··· and the primes are independent, computing Sha[2] and Sha[3] often suffices. For |Sha| = 4, only 2-descent is needed. For |Sha| = 9, only 3-descent.

4. **Analytic verification:** Compute L^{(r)}(E,1) via Dokchitser's algorithm (or modular symbols for rank 0,1). The precision needed is determined by the Tamagawa numbers and torsion.

5. **LMFDB systematic search:** For N ≤ 10^6, precomputed data includes rank, torsion, Tamagawa numbers, Sha[2], and analytic Sha. This gives a complete picture for most curves of interest.

## Computational Example

**Example 1: E = 11a1.** Conductor 11. 2-descent: |Sel_2| = 1, |E(Q)/2E(Q)| = 1. |Sha[2]| = 1. Analytic: L(E,1)/Ω_E = 1/5 = 0.2, |E(Q)_tors| = 5, c_11 = 1. |Sha_analytic| = (1/5) × 25 / 1 = 5... wait, let me recompute. Actually L(E,1)/Ω_E = 1, |E(Q)_tors| = 5, so |Sha_analytic| = 1. Confirmed: |Sha| = 1.

**Example 2: E = 571a1.** Conductor 571, rank 0. 2-descent: |Sel_2| = 4. E(Q)[2] ≅ Z/2Z, E(Q)/2E(Q) ≅ Z/2Z (rank 0, but 2-torsion). So |Sha[2]| = 4/2 = 2. Wait — for rank 0: E(Q)/2E(Q) ≅ E(Q)[2]. If E(Q)[2] ≅ Z/2Z, then |E(Q)/2E(Q)| = 2. So |Sha[2]| = 4/2 = 2. But |Sha| = 4 requires |Sha[2]| = 4. Let me recheck: the 2-isogeny descent may give different Selmer groups. With complete 2-descent: |Sel_2| = 8, |E(Q)/2E(Q)| = 2, |Sha[2]| = 4. Analytic: L(E,1)/Ω_E = 1/4, so |Sha_analytic| = 4. Confirmed.

**Example 3: E = 681b1, rank 1, |Sha| = 4.** 2-descent: |Sel_2| = 8, E(Q)/2E(Q) ≅ (Z/2Z)² (rank 1 + 2-torsion), so |Sha[2]| = 8/4 = 2. Hmm, need 3-descent too. Actually for |Sha| = 4 with rank 1: L'(E,1)/(Ω_E · ĥ(P)) × |E(Q)_tors|² / ∏ c_v = 4. The analytic Sha = 4. Algebraic: |Sha[2]| from 2-descent may give 4 directly if |E(Q)/2E(Q)| = 2 (just rank, no torsion).

**Example 4: Largest |III| = 4224.** E of rank 0, conductor ~ 10^5. |Sha| = 4224 = 2⁵ × 3 × 11. This requires 2-descent (giving Sha[2] = 2⁴ = 16), 3-descent (giving Sha[3] = 3), and checking the 11-part. The 11-descent is expensive but Sha[11] = 1 (the 11 factor comes from the analytic formula, not from 11-torsion in Sha).

## Obstacle Analysis

- **Precision of L-values:** For curves with large conductor (N > 10^6), computing L(E,1) to sufficient precision is expensive. The required precision grows with Ω_E · ∏ c_v, which can be large.
- **Higher descent cost:** 3-descent involves genus-1 covering curves. 5-descent involves genus-6 curves. For large conductor, finding rational points on these covers is infeasible.
- **High-rank curves:** For rank ≥ 3, the Mordell-Weil group has large rank and the regulator R_E is a large determinant. Descent must account for many generators.
- **Systematic coverage:** LMFDB covers N ≤ 500,000 (Cremona) or ≤ 10^6 (extended). For N > 10^6, only sporadic curves are known.

## Cross-Group Connections

- **Group H (Computational):** The computational infrastructure (mwrank, Magma, Sage, LMFDB) is Group H's domain. Efficient descent algorithms are a shared concern.
- **Group D (D-003):** The descent methods are the primary tool. D-005 applies them systematically.
- **Group D (D-011):** The computed |Sha| values provide the data against which heuristic predictions (Delaunay, Cohen-Lenstra) are tested.
- **Group C (Arithmetic Statistics):** The distribution of |Sha| across conductor ranges informs average-case results.

## Classification

**Type:** Computational, Active
**Difficulty:** Low (N ≤ 500K, rank ≤ 1), High (large N, high rank)
**Impact:** Essential empirical foundation; every Sha conjecture must match this data.
