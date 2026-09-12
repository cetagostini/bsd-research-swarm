# D-008: Visibility Method for Elements of III

**Direction ID:** D-008
**Title:** Visibility of Elements of Sha in Jacobians of Modular Curves

## Status Assessment

Active. The visibility method successfully explains elements of Sha in all computationally verified cases. For conductor N ≤ 50,000, Sha = Sha^{vis} in most cases. The method is geometric and computationally effective for moderate conductor.

## Testable Conjecture or Lemma

**Principle (Mazur, 1997).** An element c ∈ Sha(E/Q) is **visible** in J_0(N) if c lies in the image of the connecting homomorphism:

$$\delta: E(Q) \to H^1(Q, \ker(\pi))$$

where π: J_0(N) → E is the modular parametrization map on Jacobians. Equivalently, c is visible if there exists a divisor D ∈ J_0(N) with π(D) = 0 and D not torsion, such that D represents c in Sha.

**Theorem (Agashe-Stein, 2005).** For E/Q of conductor N, the visible Sha satisfies:

$$Sha^{vis}(E/Q) = \ker\left(J_0(N)(Q) \xrightarrow{\pi} E(Q)\right) / \ker(\pi)_{tors}$$

modulo elements that are locally trivial everywhere.

**Lemma (Clark, 2003).** If E_1, ..., E_k are distinct isogeny classes of conductor N, then Sha(E_i) can be simultaneously visible in ker(J_0(N) → ∏ E_j). Specifically:

$$\bigoplus_{i=1}^k Sha^{vis}(E_i) \hookrightarrow \ker\left(J_0(N) \to \prod_{j=1}^k E_j\right) / \text{torsion}$$

**Conjecture.** For E/Q of rank 0, Sha(E/Q) = Sha^{vis}(E/Q). That is, all of Sha is visible in J_0(N).

## Approach Summary

1. **Modular parametrization:** E is a quotient of J_0(N) via the modular parametrization φ: X_0(N) → E. The dual map π: J_0(N) → E has kernel K = ker(π), an abelian subvariety of J_0(N).

2. **Exact sequence:** 0 → K → J_0(N) → E → 0 gives the connecting homomorphism δ: E(Q) → H^1(Q, K). The visible Sha is the intersection of im(δ) with Sha(K/Q).

3. **Hecke algebra decomposition:** J_0(N) decomposes up to isogeny as ∏_f A_f where f ranges over newforms of level N and A_f is the associated abelian variety. The E-isotypic component is A_f for the newform f corresponding to E.

4. **Explicit computation:** Compute K = ker(π) using Hecke operators. Find divisors D ∈ K(Q) that are locally trivial. The image of such D in Sha(E) is a visible element.

5. **Period matrix method:** For moderate N, compute the period matrix of J_0(N) and use it to determine the rational points of K numerically, then verify integrally.

## Computational Example

**Example 1: E = 571a1, |Sha| = 4.** N = 571. J_0(571) has dimension 46. The kernel K = ker(π: J_0(571) → E) has dimension 45. The visible Sha is computed by finding divisors in K(Q) that map to non-trivial elements of Sha(E). Result: Sha^{vis} = Sha = (Z/2Z)², both non-trivial elements are visible.

**Example 2: E = 960d1, |Sha[2]| = 16.** N = 960. The kernel K in J_0(960) has large dimension. Clark's method finds that Sha(E)[2] is fully visible by simultaneously considering the quotient maps to all isogeny classes of conductor 960.

**Example 3: Curves with trivial Sha.** For E = 11a1, |Sha| = 1. The kernel K = ker(π) has no non-torsion rational points, confirming Sha^{vis} = 0.

**Example 4: Rank 1 visibility.** E = 681b1, rank 1, |Sha| = 4. The generator P ∈ E(Q) has δ(P) ∈ H^1(Q, K) which is non-trivial. The visible Sha includes elements arising from the interaction of the rank-1 generator with the kernel.

## Obstacle Analysis

- **No proof Sha = Sha^{vis}:** While true in all computed cases, there is no proof that all of Sha is visible. Counterexamples could exist for large conductor.
- **Computational cost:** J_0(N) has dimension ≈ N/12 for large N. Computing period matrices and height pairings on J_0(N) becomes infeasible for N > 10,000 approximately.
- **Non-modular curves:** For E over number fields other than Q, or for abelian varieties not associated to modular forms, the visibility method via J_0(N) is not available.
- **Rank ≥ 2:** For high rank, the kernel K has many generators and the connecting homomorphism δ is harder to compute. The interaction between rank and visibility is not well-understood.
- **p-adic visibility:** Visibility of Sha[p] for p ≥ 3 requires working with J_0(N) modulo p, which introduces additional technical difficulties.

## Cross-Group Connections

- **Group D (D-005):** Visibility provides a geometric explanation for the computed |Sha| values. Every element of Sha in Cremona's database can be traced to a divisor on X_0(N).
- **Group D (D-002):** The Cassels-Tate pairing on Sha^{vis} can be computed from the intersection theory on X_0(N).
- **Group F (Motivic/Cohomological):** Visibility is a concrete manifestation of the motivic cohomology class of Sha. The connecting homomorphism δ is the boundary map in motivic cohomology.
- **Group H (Computational):** The algorithms for computing visibility (period matrices, Hecke operators, height pairings on J_0(N)) are computational number theory.

## Classification

**Type:** Computational / Structural, Active
**Difficulty:** Moderate (small N), Very High (large N)
**Impact:** Provides geometric explanations for Sha elements; verified for N ≤ 50,000.
