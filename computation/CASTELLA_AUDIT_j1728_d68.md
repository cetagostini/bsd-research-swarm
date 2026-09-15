# Castella Theorem B Audit: E: y² = x³ + 68x at p=5

## Curve Identification

- **Label**: j1728_d68 (LMFDB: 9248g2)
- **Equation**: y² = x³ + 68x
- **Conductor**: 9248 = 2⁵ × 17²
- **CM**: By Q(i) (j-invariant 1728)
- **Rank**: 2 (certified by PARI)
- **Generators**: P₁ = (2, 12), P₂ = (18, 84)
- **Regulator**: 1.85677888241069065664
- **Torsion**: Z/2Z

**NOT** the d=2 quadratic twist of 194040.cu1 (N1). N1 has ainvs [0,0,0,-1825528908,-30021416896912], conductor 1,552,320, and numerical BSD quotient 64.

## p=5 Properties

- **Reduction**: Good (v₅(Δ) = 0)
- **Splitting**: 5 splits in Q(i) (5 ≡ 1 mod 4)
- **Frobenius trace**: a₅ = -4
- **Ordinary**: Yes (a₅ ≡ 1 mod 5 ≠ 0)
- **Root number**: w₅ = 1

## Castella Theorem B Hypotheses (arXiv:2204.09608v3)

### H1: CM by imaginary quadratic field K
✅ E has CM by K = Q(i), j(E) = 1728.

### H2: p is a good ordinary split prime
✅ p = 5 is:
- Good reduction (v₅(Δ) = 0)
- Split in Q(i) (5 = (2+i)(2-i))
- Ordinary (a₅ = -4, v₅(a₅) = 0)

### H3: E(Q) has rank r = 2
✅ PARI certifies rank 2 with explicit generators.

### H4: Kato cotorsion
**⚠️ NEEDS VERIFICATION**

Kato's theorem (2004) gives that the Selmer group Sel_p(E/Q) is cotorsion over the Iwasawa algebra Λ for:
- p odd prime
- E has good ordinary reduction at p
- E has good reduction outside p (or more generally, certain conditions)

For p = 5:
- E has good reduction at 5 ✓
- E has bad reduction at 2 (additive, v₂(N) = 5)
- Kato's result requires checking that the p-adic Galois representation is "geometrically ordinary"

**Status**: This is typically verified by checking that E has good ordinary reduction at p AND the p-adic L-function is well-defined. For CM curves, this follows from the CM theory.

### H5: κ_p ≠ 0 (Generalized Kato class)
**⚠️ NEEDS COMPUTATION**

Castella's Theorem B (arXiv:2204.09608v3) states:
- If κ_p ≠ 0, then dim_{Q_p} Sel(Q, V_p E) = 2.
- **Converse** (Theorem B, converse direction): If dim Sel(Q, V_p E) = 2, then κ_p ≠ 0 iff the restriction map to H¹(Q_p, V_p E) is nonzero.

**CRITICAL PREREQUISITE** (per Mr. Genius): The converse assumes dim Sel = 2 as a hypothesis. Using the converse to *prove* κ_p ≠ 0 requires first independently establishing dim Sel = 2 — typically via a p-adic L-function order bound and an applicable Iwasawa theorem. Assuming one to prove the other is circular.

The class κ_p is constructed from:
1. The generalized Kato class in H¹(Q, V_p E)
2. Via diagonal cycles with auxiliary Hecke characters satisfying Castella's conditions (1.5) and Theorem A
3. Classical `lfun`, ordinary cyclotomic `ellpadicL`, and Katz/triple-product objects are NOT interchangeable

**To prove κ_p ≠ 0**, we need EITHER:
- (A) Direct computation of κ_p (requires the specific generalized-Kato construction, not generic p-adic L-functions)
- (B) Independent proof that dim Sel = 2 (via Iwasawa theory + p-adic L-function order bound), then check restriction map

### H6: Sha[p^∞] finite
**FOLLOWS from H1-H5**: If κ_p ≠ 0, then by Castella Theorem B:
- dim Sel(Q, V_p E) = 2
- Sha(E/Q)[p^∞] is finite

**NOTE**: Theorem C explicitly assumes Sha[p^∞] finite; it cannot be quoted to establish that assumption.

## BSD Verification (Numerical Only)

| Component | Value |
|-----------|-------|
| L''(E,1) | 9.59069697518261352068 |
| ellbsd(E) | 2.58261688185801444142 |
| Reg(E) | 1.85677888241069065664 |
| BSD quotient | 1.000000 |

**BSD formula**: L''(E,1)/2! = ellbsd(E) × Reg(E) × |Sha|

Verified: 9.5907 / (2 × 2.5826 × 1.8568) = 1.000 ✓

**This is a numerical BSD quotient, NOT a proven |Sha| = 1.** Generator saturation and the conjectural status of BSD still matter. With an index-I subgroup instead of a full basis, its regulator is I² times the full regulator.

## Published Examples — NOT Novelty Controls

Per Mr. Genius: nonzero generalized Kato classes at rank 2 already have published examples.

**Castella–Hsieh (arXiv:1809.09066v4), §6, pp.25–26** explicitly constructs such examples and explains why the computed theta-element order gives fixed-prime Sha finiteness. The table includes **389a1 at p=11**, with anticyclotomic theta series beginning `10*T² + 69*T³ + ...` modulo `(11²,T^11)`.

**Implication**: "The first proven κ_p≠0 at rank 2" is NOT an available novelty claim. Fixed odd-primary finiteness is NOT uniformly unknown at rank 2. These published examples should be controls, not claimed discoveries.

Total Sha finiteness and a general rank≥2 theorem are different questions.

## Unsafe Assertions Retracted (per Mr. Genius)

### 1. Wrong curve in inertia argument
The claim that v_389(Δ) = 0 for 194040.cu1 was incorrect. 194040.cu1's conductor is 194040; its discriminant factors as 2¹¹·3⁸·5·7⁸·11. The valuation-1 transvection at 389 belongs to **389a1**, not this curve.

### 2. Kato alone insufficient for rank-2 finiteness
Kato does not by itself give rank-two finiteness at all non-exceptional primes. Large image supplies divisibility/cotorsion hypotheses; an upper bound closing the Selmer-corank chain is still needed. See [Kim's guide](https://arxiv.org/abs/2404.05186), Theorems 2.6/2.9 and Proposition 2.7.

### 3. Kolyvagin finiteness ≠ exact |Sha| order
Even after establishing analytic rank zero for the d=2 twist, the descent dimensions plus finiteness allow (Z/2)² × (Z/2^a)² with a≥2. The numerical BSD ratio 64 suggests a=2; proving the exact order requires additional arithmetic, not merely the finiteness theorem.

## Remaining Work

### Option A: Direct κ_p computation
1. Compute the specific generalized Kato class (NOT generic p-adic L-function)
2. Use Castella–Hsieh's construction with diagonal cycles and Hecke characters
3. Verify against the published 389a1 at p=11 example first

**Difficulty**: Requires implementing Castella's specific construction. PARI's `ellpadicL` is NOT the right object — it computes the cyclotomic p-adic L-function, not the anticyclotomic generalized Kato class.

### Option B: Selmer dimension via Iwasawa theory
1. Compute the characteristic ideal of the Selmer group over Z_p-extension
2. Use an applicable Iwasawa theorem to bound dim Sel = 2
3. THEN apply Castella's converse (restriction map criterion)

**Difficulty**: Requires Iwasawa-theoretic machinery and separately justified Selmer upper bound.

### Option C: Restriction map computation
1. FIRST independently establish dim Sel = 2 (via Option B or other means)
2. THEN compute restriction map on P₁, P₂
3. Check nonzero on at least one generator → proves κ_p ≠ 0 by converse

**Difficulty**: Requires Option B as prerequisite. Cannot assume dim Sel = 2 to prove κ_p ≠ 0.

## Recommendation

**Keep one CM curve E:y²=x³+68x at p=5 and produce an auditable list of theorem hypotheses and the exact remaining numerical/cohomological object.**

Choose either direct generalized-class nonvanishing or a separately justified Selmer upper bound; do not assume one to prove the other. Use the published non-CM examples (389a1 at p=11) to validate any applicable implementation, while respecting that their multiplicative-reduction hypotheses do not automatically extend to CM curves.

Specify the function, requested/achieved precision and resource failure before choosing replacement software. Installing Sage alone does not supply an implementation of the missing generalized-Kato construction.

## Status

**BLOCKED ON**: Either (a) implementation of Castella's specific generalized Kato construction (not generic p-adic L-functions), or (b) independent Selmer upper bound via Iwasawa theory.

**NEXT**: Produce auditable theorem-hypothesis checklist for E:y²=x³+68x at p=5, with each hypothesis either verified, verifiable (with specified method), or open.

---

*Generated by Mr. Implementation, 2026-09-15*
*Commit: 4079a76*
*Updated: address Mr. Genius review concerns [9], [10], [12]*
