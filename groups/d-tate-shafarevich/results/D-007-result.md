# D-007: Structure Constants — III[p^n] and p^∞-Selmer Groups

**Direction ID:** D-007
**Title:** Structure Constants of III[p^n] and Control via p^∞-Selmer Groups

## Status Assessment

Active. The Iwasawa-theoretic framework provides the most detailed information about Sha[p^∞] via the invariants µ, λ, ν. The structure theorem for Λ-modules gives the decomposition of the dual Selmer group. The main unresolved issue is the µ-invariant (conjecturally zero) and the supersingular case.

## Testable Conjecture or Lemma

**Conjecture (Finiteness).** Sha(E/Q)[p^∞] ≅ ⊕_{i=1}^{t} Z/p^{n_i}Z for some n_1 ≤ n_2 ≤ ··· ≤ n_t.

**Structure Theorem.** The Pontryagin dual X_∞ = Sel_{p^∞}(E/Q_∞)^∨ is a finitely generated torsion Λ-module (Λ = Z_p[[T]]). By the structure theorem:

$$X_\infty \sim_{\Lambda} \bigoplus_{i=1}^{s} \Lambda/(f_i(T)^{e_i})$$

up to pseudo-isomorphism, where f_i are distinguished polynomials. The characteristic ideal is char_Λ(X_∞) = ∏ f_i^{e_i}.

**Iwasawa Invariants.** For n sufficiently large:

$$|Sel_{p^n}(E/Q)| = p^{\mu p^n + \lambda n + \nu}$$

where µ = ∑ e_i · deg(f_i^0-term) (the µ-invariant), λ = ∑ e_i · deg(f_i) (the λ-invariant), and ν is a correction term.

**Greenberg's µ-vanishing.** For E/Q ordinary at p with p ∤ N · |E(Q)_tors|, the µ-invariant of Sel_{p^∞}(E/Q_∞) vanishes.

**Recovery of Sha.** Under the control theorem:

$$0 \to \text{ker}_n \to Sel_{p^n}(E/Q) \to Sel_{p^\infty}(E/Q_\infty)^{\Gamma_n} \to \text{coker}_n \to 0$$

where |ker_n| and |coker_n| are bounded independently of n. Then:

$$|Sha[p^n]| = \frac{|Sel_{p^n}(E/Q)|}{|E(Q)/p^n \cdot E(Q)|} \cdot \frac{1}{|\text{error}_n|}$$

## Approach Summary

1. **Λ-module theory:** Study X_∞ via its pseudo-isomorphism class. The elementary divisors of X_∞ determine the growth pattern of |Sel_{p^n}|.

2. **Control theorem (Greenberg):** For E ordinary at p, the natural map Sel_{p^n}(E/Q) → Sel_{p^∞}(E/Q_∞)^{Γ_n} has kernel and cokernel bounded by local terms at p. Specifically, |ker| ≤ |E(Q_p)[p^n]| and |coker| ≤ |Ẽ(Q_p)[p^n]| for the reduced curve Ẽ.

3. **Characteristic ideal computation:** From the main conjecture (Skinner-Urban), char_Λ(X_∞) = (L_p(E)). The p-adic L-function's µ and λ invariants determine those of X_∞.

4. **Structure extraction:** Given char_Λ(X_∞) = (T^λ + ···) (assuming µ = 0), the Λ-module structure of X_∞ determines the finite quotients X_∞/ω_n X_∞ which approximate Sha[p^n] via the control theorem.

5. **Ochi's formula:** For many E/Q, the Pontryagin dual of Sel_{p^∞}(E/Q) decomposes as Z_p^r ⊕ M with M finite and |M| = |Sha[p^∞]| · |E(Q)_tors/p^∞|.

## Computational Example

**Example 1: E = 11a1, p = 5.** Ordinary at 5. λ = 0 (L_5(E,1) is a unit), µ = 0. So Sel_{5^∞}(E/Q_∞)^∨ is finite. The control theorem gives |Sha[5^∞]| = 0.

**Example 2: E = 571a1, p = 2.** Analytic rank 0, |Sha| = 4. The 2-adic L-function has λ = 2 (matching |Sha[2]| = 4 = 2²). The Λ-module X_∞ has char = (T² + ···) with µ = 0. The structure: X_∞ ≅ Λ/(f(T)) with f a distinguished polynomial of degree 2.

**Example 3: Growth pattern.** For E with |Sha[p]| = p² and |Sha[p²]| = p⁴, the sequence k_n = 1, 2, 2, 2, ... stabilizes at n = 2. This means Sha[p^∞] ≅ (Z/pZ)² and the p²-Selmer group captures the full p^∞-information.

**Example 4: Iwasawa invariants from LMFDB.** For E = 681b1 (rank 1, |Sha| = 4) at p = 3: L_3(E, s) has a zero of order 1 at s = 1 (matching rank 1). λ = 1, µ = 0. The 3-part of Sha is trivial, consistent with |Sha| = 4 = 2².

## Obstacle Analysis

- **µ-invariant:** The conjecture µ = 0 is open for general E/Q. Without it, the Iwasawa invariants do not determine |Sha[p^∞]| exactly. Greenberg's result requires p ∤ N · |E(Q)_tors|.
- **Supersingular primes:** For a_p ≡ 0 (mod p), the cyclotomic Selmer group is not cotorsion over Λ. The ±-Selmer groups are cotorsion but the relationship between X_∞^± and Sha[p^∞] is indirect.
- **Pseudo-null ambiguity:** The structure theorem is only up to pseudo-isomorphism. Pseudo-null Λ-modules (those with codimension ≥ 2 support) can modify the finite part of X_∞ without changing the characteristic ideal.
- **Control theorem error terms:** The kernel and cokernel of the control map depend on the p-adic valuation of |E(Q_p)[p^n]|, which varies with n. For E with rational p-torsion, the error terms are non-trivial.

## Cross-Group Connections

- **Group A (Iwasawa):** The Λ-module theory and characteristic ideals are Group A's primary focus. D-007 applies their structural results to Sha.
- **Group E (p-adic Methods):** The p-adic L-function's invariants (µ, λ) directly determine the Selmer group's invariants via the main conjecture.
- **Group D (D-010):** D-010 focuses on the Iwasawa framework for Sha specifically. D-007 and D-010 are closely related.
- **Group D (D-003):** Descent computes |Sel_{p^n}| for small n. The Iwasawa theory extrapolates to all n.

## Classification

**Type:** Structural / Iwasawa-theoretic, Active
**Difficulty:** High (supersingular, pseudo-null issues), Moderate (ordinary, µ = 0)
**Impact:** Provides the most detailed information about the p-primary structure of Sha.
