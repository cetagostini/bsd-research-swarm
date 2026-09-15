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

**Isogeny fact (2026-09-15, verified):** y²=x³+68x is **2-isogenous to y²=x³−17x (LMFDB 9248g1), which is curve E₂ (D=17) in Coates–Liang–Sujatha** (arXiv:1005.4206, Thm 1.3). They prove Ш(E₂/ℚ)[p^∞]=0 at every good split prime p ≡ 1 (mod 4), p < 30,000, unconditionally (Rubin's main conjecture for ℚ(i)); the only exceptions are (E₁,29), (E₁,277), (E₄,577), (E₅,17) — (E₂, 5) is not among them. **Hence Ш[5^∞] = 0 for the d68 isogeny class is already a theorem of CLS 2010; p=5 is not an open case.** Banwait (arXiv:2609.08431, Sep 2026) settles the four CLS-inconclusive pairs with a cyclotomic unit-condition criterion + Lean 4 formalisation.

**Consequence:** the Castella Theorem B route for E:y²=x³+68x at p=5 would reprove an already-proven statement, not produce new finiteness. The curve is not a genuine target for the program unless the goal is (a) an independent proof/control of the CLS machinery at an anomalous prime, or (b) an explicit construction of κ₅ (which is not in the literature for any CM curve — that construction is still new even though the finiteness conclusion is already known). The p=5 case has a₅=−4 ⟹ #Ẽ(𝔽₅)=10 ≡ 0 (mod 5), i.e. p=5 is anomalous for this curve, so it sits outside the unit-condition/regulator-unit workflow; that is the only reason it was a "candidate" — it is a genuinely harder case of an already-settled question.

## p=5 Properties

- **Reduction**: Good (v₅(Δ) = 0)
- **Splitting**: 5 splits in Q(i) (5 ≡ 1 mod 4)
- **Frobenius trace**: a₅ = -4
- **Ordinary**: Yes (a₅ ≡ 1 mod 5 ≠ 0)
- **Root number**: w₅ = 1
- **ANOMALOUS**: a₅ = −4 ⟹ #Ẽ(𝔽₅) = 10 ≡ 0 (mod 5). Excluded from the CLS criterion and Banwait's Theorem A unit-condition test; this is the reason p=5 was never ruled out by the routine criterion — but CLS Theorem 1.3's exception list does not contain (E₂, 5), so Ш[5^∞]=0 is already proven for the class.

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
The claim that v_389(Δ) = 0 for 194040.cu1 was incorrect — but the correction must be stated precisely: 389 does not divide 194040.cu1's discriminant at all (its discriminant factors as 2¹¹·3⁸·5·7⁸·11), so v_389(Δ) = 0 is *trivially true* for 194040.cu1 and carries no transvection information. The valuation-1 (multiplicative reduction) transvection at 389 belongs to **389a1** (discriminant 389, v_389(Δ_min) = 1), not to 194040.cu1.

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
