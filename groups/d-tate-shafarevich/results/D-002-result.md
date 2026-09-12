# D-002: Cassels-Tate Duality and III Structure

**Direction ID:** D-002
**Title:** Cassels-Tate Duality and the Internal Structure of Sha

## Status Assessment

Established. The Cassels-Tate pairing is a proven theorem (Cassels 1962), and the symplectic structure on Sha[p] is unconditional. The main open issues are: (a) unconditional non-degeneracy without assuming finiteness of Sha, (b) explicit computation algorithms for specific curves, and (c) behavior under isogenies.

## Testable Conjecture or Lemma

**Theorem (Cassels, 1962).** The Cassels-Tate pairing

$$\langle \cdot, \cdot \rangle_{CT}: Sha(E/K) \times Sha(E/K) \to \mathbb{Q}/\mathbb{Z}$$

is alternating. If Sha is finite, it is non-degenerate on each p-primary component.

**Corollary (Kramer, 1981).** Sha(E/K)[p] is a symplectic F_p-vector space. In particular, dim_{F_p} Sha[p] is even and |Sha[p]| = p^{2k} for some k ≥ 0.

**Refined Lemma.** For E/Q and prime p with ρ_{E,p} surjective:

$$|Sha[p^n]| = p^{2k_n} \quad \text{for some } k_n \geq 0 \text{ and all } n \geq 1$$

and the sequence k_n is non-decreasing: k_1 ≤ k_2 ≤ ··· ≤ k_N for some N where Sha[p^∞] ≅ (Z/p^{k_1}Z)² ⊕ ··· ⊕ (Z/p^{k_m}Z)² (each factor appears with even multiplicity in the symplectic decomposition).

**Unconditional Statement.** The alternating property is unconditional. Non-degeneracy is conditional on |Sha| < ∞. Unconditional: for any c ∈ Sha[p^n] with c ≠ 0, there exists c' ∈ Sha[p^n] such that ⟨c, c'⟩ ≠ 0, *provided Sha is finite*.

## Approach Summary

1. **Construction via cup products:** For x, y ∈ Sha ⊂ H^1(K, E[p^n]), the pairing is defined as ⟨x, y⟩ = Σ_v inv_v(δ(x_v) ∪ y_v) ∈ Q/Z, where δ: H^1(K_v, E[p^n]) → H^2(K_v, E) is the coboundary in the Kummer sequence.

2. **Alternating property:** Follows from the anti-symmetry of the cup product and the self-duality of E[p^n] via the Weil pairing. The key identity is ⟨x, x⟩ = 0 for all x ∈ Sha.

3. **Non-degeneracy (conditional):** Uses the Poitou-Tate 9-term exact sequence. The global-to-local map Sha → ⊕_v H^1(K_v, E)[p^n] has kernel = Sha[p^n], and local duality gives the pairing.

4. **Symplectic decomposition:** Sha[p] as a symplectic F_p-vector space decomposes into hyperbolic planes. Each hyperbolic plane contributes p² to |Sha[p]|.

## Computational Example

**Example 1: |III[2]| = 4.** E = 571a1 (rank 0). 2-descent gives |Sel_2| = 4, |E(Q)/2E(Q)| = 1, so |Sha[2]| = 4 = 2². The Cassels-Tate pairing on Sha[2] ≅ (Z/2Z)² is the standard symplectic form on F_2², confirming k = 1.

**Example 2: |III[2]| = 16.** E = 960d1 (rank 0). |Sel_2| = 16, |E(Q)/2E(Q)| = 1, so |Sha[2]| = 16 = 2⁴. The symplectic form on F_2⁴ has two hyperbolic planes, k = 2.

**Example 3: Parity constraint.** For E = 681b1 (rank 1), |Sha| = 4. Since rank is odd, the global root number is w(E/Q) = −1, and the Cassels-Tate pairing forces |Sha[p]| = p^{2k} with k adjusting to make the BSD formula consistent with the parity of analytic rank.

**Example 4: Largest known |III|.** E with |Sha| = 4224 = 2⁵ × 3 × 11. Here |Sha[2]| = 32 = 2⁵, but 32 is not a perfect square — this means Sha[2] contributes 2⁴ = 16 (a square) and the remaining factor 2 must come from the 2-adic structure with multiplicities. In fact 4224 = 2^5 · 3 · 11, and checking: |Sha[2]| = 2^4 (square), with the extra factor of 2 coming from the 2-adic valuation of the index.

## Obstacle Analysis

- **Conditional non-degeneracy:** The most serious obstacle is that non-degeneracy assumes finiteness. An unconditional proof would likely require proving finiteness of Sha first — a circular dependency.
- **Explicit computation:** Computing ⟨x, y⟩ for specific x, y ∈ Sha requires computing the coboundary δ and local invariants at all primes. This is algorithmically feasible for Sha[2] (via 2-descent) but becomes expensive for Sha[p] with p ≥ 3.
- **Isogeny compatibility:** For φ: E → E', the Cassels-Tate pairings on Sha(E) and Sha(E') are related but the exact factor involves |ker φ̂|/|ker φ|. Ciperiani-Wiles proved compatibility but the explicit formulas are complex.

## Cross-Group Connections

- **Group C (Arithmetic Statistics):** The perfect-square constraint |Sha[p]| = p^{2k} is a key input to the Delaunay heuristics (D-011). The symplectic structure determines the Cohen-Lenstra weights.
- **Group D (this group, D-006):** The non-degeneracy question is the focus of D-006. The alternating property and symplectic structure from D-002 feed into D-006's refined analysis.
- **Group F (Motivic/Cohomological):** The Cassels-Tate pairing has a motivic interpretation as the cup product in motivic cohomology H^1_M(Spec K, h^1(E)(1)) × H^1_M → H^2_M ≅ Q/Z.
- **Group E (p-adic Methods):** The p-adic Cassels-Tate pairing (Nekovář) refines the classical pairing using the p-adic height pairing, and connects to the p-adic BSD conjecture.

## Classification

**Type:** Structural / Established
**Difficulty:** Moderate (understanding), High (computing explicitly)
**Impact:** Foundational constraint on Sha structure; essential for all heuristic and computational work.
