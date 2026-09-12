# D-010: The p-part of III and Iwasawa Theory

**Direction ID:** D-010
**Title:** The p-part of Sha in the Iwasawa-theoretic Framework

## Status Assessment

Active. The Iwasawa main conjecture for E/Q ordinary at p is proved (Skinner-Urban 2014), giving char_Λ(X_∞) = (L_p(E)). The p-part of Sha is recoverable from the Iwasawa invariants via the control theorem. The main gaps: µ = 0 conjecture, supersingular primes, and rank ≥ 2 extraction.

## Testable Conjecture or Lemma

**Theorem (Control Theorem, Greenberg 1989).** For E/Q ordinary at p, the natural map

$$Sel_{p^n}(E/Q) \to Sel_{p^\infty}(E/Q_\infty)^{\Gamma_n}$$

has kernel and cokernel bounded independently of n. Specifically:

$$|\text{ker}| \leq |E(Q_p)[p^\infty]| \quad \text{and} \quad |\text{coker}| \leq |\tilde{E}(\mathbb{F}_p)[p^\infty]|$$

where Ẽ is the reduced curve modulo p.

**Theorem (Kato, 2004).** char_Λ(X_∞) divides (L_p(E)) in Λ = Z_p[[T]].

**Theorem (Skinner-Urban, 2014).** For E/Q ordinary at p with analytic rank ≤ 1 and a_p not divisible by p:

$$char_\Lambda(X_\infty) = (L_p(E))$$

**Conjecture (µ = 0).** For E/Q and all primes p, the µ-invariant of X_∞ = Sel_{p^∞}(E/Q_∞)^∨ vanishes:

$$\mu(X_\infty) = 0$$

**Recovery Formula.** Under the main conjecture with µ = 0:

$$v_p(|Sha[p^\infty]|) = v_p(L_p^{(r)}(E, 1)) - v_p(r!) - v_p(\mathcal{L}_p(E)) - \sum_v v_p(c_v) + 2 \cdot v_p(|E(Q)_{tors}|)$$

## Approach Summary

1. **Iwasawa algebra Λ = Z_p[[T]]:** T corresponds to γ − 1 for a topological generator γ of Γ = Gal(Q_∞/Q). The module X_∞ is finitely generated and torsion over Λ.

2. **Structure theorem:** X_∞ is pseudo-isomorphic to ⊕ Λ/(p^{µ_i}) ⊕ ⊕ Λ/(f_i^{e_i}) where f_i are distinguished polynomials. The µ-invariant is ∑ µ_i and the λ-invariant is ∑ e_i · deg(f_i).

3. **Control theorem application:** For each n, |Sel_{p^n}| ≈ p^{µp^n + λn + ν} (up to bounded error). If µ = 0, then |Sel_{p^n}| grows polynomially in p^n, and Sha[p^n] stabilizes.

4. **Characteristic ideal → Sha:** Given char_Λ(X_∞) = (L_p(E)) with L_p(E) = T^λ + ··· (µ = 0), the finite module X_∞/(T) determines the "generic" fiber of the Selmer group, and Sha[p^∞] is the correction between this and the actual Sel_{p^∞}(E/Q).

5. **Supersingular ±-theory:** For a_p ≡ 0 (mod p), define Sel_{p^∞}^±(E/Q_∞) using Kobayashi's ±-local conditions at p. These are cotorsion over Λ with invariants µ^±, λ^±. The main conjecture (Wan 2014) relates char(Sel^±) to Pollack's ±-L-functions.

## Computational Example

**Example 1: E = 11a1, p = 5.** L_5(E, T) is a unit in Λ (λ = 0, µ = 0). So X_∞ is finite, and the control theorem gives |Sha[5^∞]| = 0. The 5-adic BSD: L_5(E, 1) is a 5-adic unit, consistent.

**Example 2: E = 571a1, p = 2.** The 2-adic L-function has λ = 2 (matching |Sha[2]| = 4). Computing L_2(E, T) = T² + aT + b with b ≡ 0 (mod 4). The Λ-module X_∞ ≅ Λ/(T² + aT + b). The 2-part of Sha is recovered from X_∞/(T) ≅ Z/4Z (or (Z/2Z)² depending on the structure).

**Example 3: Growth of Sel_{p^n}.** For E with |Sha[p]| = p² and |Sha[p²]| = p² (stabilized), the λ-invariant is 2. The Selmer group grows as |Sel_{p^n}| = p^{2n} · |E(Q)/p^n| for n ≥ 1, confirming the Iwasawa prediction with µ = 0.

**Example 4: Supersingular verification.** E = 43a1 at p = 3 (a_3 = 0). The ±-L-functions L_3^±(E, T) are computed. λ^+ + λ^− = 2 (the expected total λ). The ±-Sha contributions combine to give |Sha[3^∞]|.

## Obstacle Analysis

- **µ = 0 unproven:** For general E/Q, µ = 0 is a conjecture. Greenberg proved it for ordinary E with p ∤ N · |E(Q)_tors|. The general case would follow from the main conjecture plus a vanishing result for the µ-invariant of the p-adic L-function.
- **Supersingular case:** The cyclotomic Selmer group is not cotorsion. The ±-theory is a substitute but introduces two sets of invariants (µ^±, λ^±) whose relationship to the actual Sha is indirect.
- **Rank ≥ 2:** Even with char_Λ(X_∞) = (L_p(E)), extracting |Sha[p^∞]| requires computing the p-adic regulator ℒ_p(E) as a determinant of p-adic heights on E(Q). For rank ≥ 2, this is computationally intensive.
- **Pseudo-null ambiguity:** The structure theorem is up to pseudo-isomorphism. A pseudo-null submodule of X_∞ (with char = Λ) does not affect char_Λ but can modify the finite part of X_∞ that determines Sha.

## Cross-Group Connections

- **Group A (Iwasawa):** The Λ-module theory is Group A's domain. The main conjecture (proved by Group A's methods) determines Sha.
- **Group E (p-adic Methods):** The p-adic L-function L_p(E) is constructed by Group E's methods. The µ, λ invariants of L_p determine those of X_∞.
- **Group D (D-007):** The structure constants of Sha[p^n] are the finite-level manifestation of the Iwasawa invariants.
- **Group D (D-004):** The p-adic BSD conjecture is the precise statement connecting L_p(E) to Sha[p^∞]. D-010 provides the Iwasawa-theoretic framework.

## Classification

**Type:** Core / Iwasawa-theoretic, Active
**Difficulty:** High (µ = 0, supersingular), Moderate (ordinary, rank ≤ 1)
**Impact:** Deepest structural information about the p-primary part of Sha.
