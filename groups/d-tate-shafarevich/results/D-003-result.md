# D-003: Descent Methods for Bounding |III|

**Direction ID:** D-003
**Title:** Descent Methods for Bounding |Sha| via Selmer Groups

## Status Assessment

Active. Descent is the primary practical method for computing |Sha[p]|. Complete 2-descent is fully algorithmic (Cassels, Cremona). Complete 3-descent and 5-descent are implemented (Schaefer-Connell, Fisher). Higher p-descent remains difficult. The main theoretical contribution is the exact sequence relating Sel_p to Sha[p].

## Testable Conjecture or Lemma

**Proposition.** For E/Q and prime p, there is an exact sequence

$$0 \to E(Q)/p \cdot E(Q) \to Sel_p(E/Q) \to Sha(E/Q)[p] \to 0$$

Hence $|Sha[p]| = |Sel_p(E/Q)| / |E(Q)/p \cdot E(Q)|$.

**Descent Bound.** For the p^n-Selmer group:

$$|Sha[p^n]| = \frac{|Sel_{p^n}(E/Q)|}{|E(Q)/p^n \cdot E(Q)|}$$

**Refined Bound (2-descent).** Let s = #{v | 2N : local image δ_v(E(Q_v)/2) has codimension > 0 in H^1(Q_v, E[2])}. Then:

$$|Sel_2(E/Q)| \leq 2^{r+1+s}$$

where r = rank E(Q), and |Sha[2]| ≤ 2^{s-1} when r = 0 (from Zywina's effective bound).

**Lemma (Descent via isogenies).** If φ: E → E' is a p-isogeny defined over Q, then the φ-Selmer group Sel_φ(E/Q) fits in 0 → E'(Q)/φ(E(Q)) → Sel_φ(E/Q) → Sha(E/Q)[φ] → 0, and |Sel_φ| is computed by local conditions at primes dividing pN∞.

## Approach Summary

1. **2-descent (complete):** The Kummer map δ: E(Q)/2 → H^1(Q, E[2]) factors through the Selmer conditions at all places. For E: y² = f(x) with f cubic, E[2] = {roots of f} ∪ {0}, and H^1(Q, E[2]) is computed via the connecting homomorphism to Q*/(Q*)² × Q*/(Q*)². The images δ_v at each prime v are computed from the Hilbert symbol.

2. **2-isogeny descent:** When E has a rational 2-torsion point, use the 2-isogeny φ: E → E' and compute Sel_φ and Sel_φ̂ separately. This is Birch-Swinnerton-Dyer's original method.

3. **p-descent for p ≥ 3:** The covering space approach (Schaefer-Connell): the p-descent uses unramified covers of E defined by the p-division polynomial. The Selmer group is computed by finding rational points on these covers locally at each prime.

4. **Iterated descent:** The p^n-Selmer group for n ≥ 2 requires computing the image of Sel_{p^{n+1}} → Sel_{p^n} via the connecting homomorphism. This is done by a recursive tower of covering curves.

5. **Nekovář's Selmer complex:** Provides unconditional bounds on Sha by replacing the Selmer group with a complex in the derived category. The Euler characteristic of this complex gives bounds on |Sha| without assuming finiteness.

## Computational Example

**Example 1: 2-descent on 571a1.** E: y² + y = x³ − x² − 93x − 324. The 2-division polynomial has one rational root, so E(Q)[2] ≅ Z/2Z. The 2-isogeny descent gives |Sel_φ| = 2, |Sel_φ̂| = 2, so |Sel_2| = 4. Since E(Q) = {0} (rank 0), |Sha[2]| = 4.

**Example 2: Complete 2-descent on 681b1.** E of rank 1 with |Sha| = 4. Complete 2-descent: E[2] splits completely over Q (three rational 2-torsion points). |Sel_2| = 8, |E(Q)/2E(Q)| = 2 (rank 1), so |Sha[2]| = 4.

**Example 3: 3-descent on a rank-0 curve.** E = 19a1: y² + y = x³ + x² + x. |Sel_3| = 1, |E(Q)/3E(Q)| = 1, so |Sha[3]| = 1. Combined with 2-descent giving |Sha[2]| = 1, we get |Sha| = 1.

**Example 4: 2-descent bound.** For E = 960d1 (rank 0), s = 5 (five primes where the local image is proper), so |Sha[2]| ≤ 2⁴ = 16. Actual: |Sha[2]| = 16 = 2⁴, confirming the bound is sharp.

## Obstacle Analysis

- **Computational cost of p-descent for p ≥ 5:** The covering curves have genus (p−1)(p−2)/2, so for p = 5 one handles genus 6 curves. Finding rational points on such curves is expensive.
- **Wild ramification at p = 2:** The local Kummer map at 2 involves the 2-adic logarithm, which has convergence issues. The explicit computation of δ_2 requires careful treatment of the formal group.
- **Large conductor:** For E of conductor N >> 10^6, even 2-descent becomes slow because the local conditions at bad primes require computing over Q_p for large p.
- **Incomplete Sha determination:** Descent gives |Sha[p]| for one p at a time. To determine |Sha| completely, one must compute |Sha[p]| for all p dividing |Sha_{analytic}|, which may require descents at multiple primes.
- **Indeterminacy for rank ≥ 2:** When rank ≥ 2, the quotient Sel_p / E(Q)/p may not stabilize after one descent. Higher descents (p², p³, ...) are needed to determine the p-adic structure of Sha.

## Cross-Group Connections

- **Group H (Computational):** The algorithms for descent are implemented in mwrank, Magma, and Sage. Group H's work on efficient implementations directly supports D-003.
- **Group D (D-006):** The Cassels-Tate pairing can be computed from descent data. The 2-descent gives the pairing on Sha[2] via the local Hilbert symbol.
- **Group D (D-005):** Descent is the primary tool for computing |Sha| for specific curves, feeding into the database of known Sha values.
- **Group B (Euler Systems):** Kolyvagin's descent via Euler systems is a different kind of descent — it uses cohomology classes from the Euler system rather than the Kummer map. The two approaches are complementary.

## Classification

**Type:** Computational / Theoretical, Active
**Difficulty:** Low (2-descent), Moderate (3-descent), High (p ≥ 5 descent)
**Impact:** Primary practical method for computing Sha; essential for verifying BSD on specific curves.
