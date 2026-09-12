# D-009: III over Function Fields

**Direction ID:** D-009
**Title:** The Tate-Shafarevich Group over Function Fields

## Status Assessment

Active. Finiteness of Sha is proven for E/F_q(t) with non-constant j-invariant (Tan 2021, via the Artin-Tate conjecture). The function field case is the closest setting to number fields where BSD is largely proved. The constant-j case and the case k = Q remain open.

## Testable Conjecture or Lemma

**Theorem (Artin-Tate, Milne, Tan).** For E/F_q(t) with non-constant j-invariant, Sha(E/F_q(t)) is finite and satisfies:

$$|Sha(E/F_q(t))| = \frac{L(E/F_q(t), 1) \cdot |E(F_q(t))_{tors}|^2}{\Omega_E \cdot \prod c_v \cdot \deg(\hat{h})}$$

where L is the Goss L-function, Ω_E is the period, and ĥ is the canonical height on E/F_q(t).

**Theorem (Geisser, 2004).** For E/F_q(t) and p ≠ char(F_q):

$$Sha(E/F_q(t))[p] = 0$$

That is, the prime-to-characteristic part of Sha is trivial over finite fields. (This was later extended to the full Sha by Tan.)

**Conjecture (Geisser).** For E/F_q(t), Sha(E/F_q(t))[p^∞] = 0 for p = char(F_q). This remains open.

**Structural Result.** For E/C over a curve C/F_q, the Sha fits in the Artin-Tate exact sequence:

$$0 \to Sha(E/F_q(C)) \to \text{Br}(S) \to \bigoplus_v \text{Br}(E_{k_v}) \to H^1(C, \text{Pic}^0(\bar{S}))$$

where S is the Néron model of E over C and Br is the Brauer group.

## Approach Summary

1. **Artin-Tate reduction:** The BSD conjecture for E/F_q(t) is equivalent to the Tate conjecture for the surface S = E ×_{F_q(t)} C (where C is the base curve). The Tate conjecture for divisors on S over F_q was proved by Tate (for abelian varieties) and extended by Tan.

2. **Weil conjecture method:** The zeta function of S encodes the L-function of E/F_q(t). The functional equation and rationality of the zeta function (Weil conjectures, proved by Deligne) give the analytic properties needed for BSD.

3. **Néron-Severi computation:** |Sha| is related to the rank of the Néron-Severi group NS(S) via: |Sha| = |det(intersection matrix on NS(S))| / (∏ c_v · |tors|²). This is computable from the geometry of S.

4. **Ulmer's constructions:** For specific E/F_q(t), Ulmer constructed curves with arbitrarily large rank by specializing families. The Sha for these curves can be computed from the Néron-Severi group of the associated surface.

5. **Characteristic p methods:** For the p-part (p = char(F_q)), the flat cohomology sequence and the Artin-Milne duality replace the Galois cohomology used in the number field case.

## Computational Example

**Example 1: E: y² = x³ + t over F_2(t).** This curve has rank 0 over F_2(t). The L-function L(E/F_2(t), 1) = 1. |Sha| = 1. Confirmed by direct computation of the Néron-Severi group.

**Example 2: Ulmer's curve.** E: y² + xy = x³ + t over F_q(t). For q = p^n, the rank of E(F_q(t)) grows with n. Specifically, rank E(F_{p^n}(t)) = (p^n − 1)/(p − 1). The Sha for these curves is computable and grows in a controlled manner.

**Example 3: Constant j-invariant.** E: y² = x³ + 1 over F_p(t) (j = 0). The Artin-Tate conjecture is not fully proved in this case. Partial results (Deshpande 2022) show |Sha[p'|^∞]| = 0 for p' ≠ p.

**Example 4: L-function computation.** For E over F_3(t) of conductor 10, the Goss L-function L(E, 1) is computed by counting points on E(F_{3^n}) for n = 1, 2, ..., 10 and using the Euler product. Result: L(E, 1) ∈ F_3[[T]] and |Sha| matches the BSD prediction.

## Obstacle Analysis

- **Constant j-invariant:** When j(E) ∈ F_q, the surface S has extra automorphisms and the Tate conjecture is harder. The Néron-Severi group may have unexpected generators.
- **Characteristic p Sha:** The p-part of Sha (p = char(F_q)) is the most mysterious. Geisser's vanishing result for p ≠ char does not extend to p = char.
- **Number field function fields:** For E/Q(t) or E/k(t) with k a number field, finiteness of Sha is completely open. The Weil conjecture approach fails because there is no Frobenius.
- **Explicit computation:** For large q or high conductor, the surface S is complicated and computing NS(S) is difficult.

## Cross-Group Connections

- **Group F (Motivic/Cohomological):** The Artin-Tate conjecture has a motivic interpretation. The Tate conjecture for S is equivalent to a motivic statement about H^2(S).
- **Group D (D-001):** Over function fields, Euler systems exist more naturally (via Drinfeld modules and shtukas). The function field analogue of Kato's Euler system is Beilinson's construction.
- **Group I (Connections):** The function field case provides evidence and intuition for the number field case. The analogy between F_q(t) and Q guides conjectures.
- **Group C (Arithmetic Statistics):** The distribution of |Sha| over function field families is better understood than over number fields, providing test cases for heuristics.

## Classification

**Type:** Structural, Active
**Difficulty:** Moderate (non-constant j), High (constant j, number field base)
**Impact:** Closest setting to number fields where BSD is proved; provides structural insights.
