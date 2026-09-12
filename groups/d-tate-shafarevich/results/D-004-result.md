# D-004: p-adic Methods for III

**Direction ID:** D-004
**Title:** p-adic Methods for Controlling Sha

## Status Assessment

Active. The p-adic L-function and Iwasawa-theoretic approach to Sha is one of the most powerful tools available. The Iwasawa main conjecture is proved for ordinary primes (Skinner-Urban 2014). The main gaps are: (a) supersingular primes, (b) extracting exact |Sha[p^∞]| from the main conjecture (requires µ = 0), and (c) rank ≥ 2.

## Testable Conjecture or Lemma

**Conjecture (p-adic BSD, Mazur-Tate-Teitelbaum).** For E/Q ordinary at p of analytic rank r:

$$L_p^{(r)}(E, 1) = \left(1 - \frac{a_p}{p} + \frac{1}{p}\right)^{\epsilon} \cdot \frac{|Sha[p^\infty]| \cdot \mathcal{L}_p(E) \cdot \prod c_v^{(p)}}{|E(Q)_{tors}|^2}$$

where ε = 1 if L(E,1) ≠ 0 and ε = 0 otherwise, and ℒ_p(E) is the p-adic regulator (determinant of p-adic heights).

**Theorem (Kato divisibility).** char_Λ(Sel_{p^∞}(E/Q_∞)^∨) divides (L_p(E)) in Λ = Z_p[[T]].

**Theorem (Skinner-Urban, 2014).** For E/Q ordinary at p with analytic rank ≤ 1:

$$\text{char}_\Lambda(Sel_{p^\infty}(E/Q_\infty)^\vee) = (L_p(E))$$

**Bound.** The control theorem gives:

$$|Sha(E/Q)[p^n]| \leq \frac{|Sel_{p^n}(E/Q)|}{|E(Q)/p^n \cdot E(Q)|}$$

and for n sufficiently large: |Sel_{p^n}| = p^{µp^n + λn + ν} for Iwasawa invariants µ, λ, ν.

## Approach Summary

1. **Construction of L_p(E):** Via modular symbols. The p-adic L-function interpolates L(E, χ, 1) for Dirichlet characters χ of p-power conductor. For E ordinary at p, the construction uses the ordinary projection of modular symbols (Mazur-Swinnerton-Dyer, Amice-Vélu, Vishik).

2. **Kato's Euler system → Iwasawa:** Kato's classes z_f^(p) ∈ H^1(Q, T_p(E)) map to the Selmer group. The regulator map sends z_f^(p) to L_p(E) via Perrin-Riou's big exponential map. The divisibility char | (L_p) follows.

3. **Skinner-Urban's converse:** Uses the Eisenstein ideal and the Hida family to prove the reverse divisibility. The key input is the non-vanishing of a certain Hecke eigenvalue modulo p.

4. **Extracting |Sha[p^∞]|:** From the main conjecture, the characteristic ideal determines the structure of Sel_{p^∞}^∨ as a Λ-module. The p-adic valuation of |Sha[p^∞]| is read off from the Iwasawa invariants, provided µ = 0.

5. **Supersingular case (Pollack ±):** For a_p ≡ 0 (mod p), define L_p^+(E) and L_p^−(E) by interpolating L-values with modified Euler factors. The ±-Selmer groups Sel_p^± are cotorsion over Λ and satisfy their own main conjecture.

## Computational Example

**Example 1: p-adic L-value for 11a1 at p = 5.** E: y² + y = x³ − x² − 10x − 20, ordinary at 5 (a_5 = −2). L_5(E, 1) ≈ 2 × (unit in Z_5). Since L(E,1)/Ω_E = 1/1 = 1 and c_v = 1, we get |Sha[5^∞]| = 0, confirming Sha has no 5-part.

**Example 2: p = 2 for 571a1.** E has |Sha| = 4, so Sha[2^∞] ≅ (Z/2Z)². The 2-adic L-function L_2(E, s) has ord_{s=1} L_2 = 0 (analytic rank 0). The p-adic BSD predicts v_2(L_2(E,1)) = v_2(|Sha[4]|) + corrections. Computing: L_2(E,1) has 2-adic valuation 2, consistent with |Sha[2^∞]| = 4.

**Example 3: Supersingular case.** E = 11a1 at p = 3: a_3 = 1, not supersingular. E = 43a1 at p = 3: a_3 = 0, supersingular. The ±-L-functions L_3^±(E) must be used. Pollack's computation gives L_3^+(E, 1) and L_3^−(E, 1) as 3-adic numbers whose valuations determine |Sha[3^∞]|.

## Obstacle Analysis

- **µ-invariant:** Conjecturally µ = 0 for all E/Q and all p. Proven for p not dividing N · |E(Q)_tors| by Greenberg (for ordinary E). The general case remains open. If µ > 0, the main conjecture does not determine |Sha[p^∞]| exactly.
- **Supersingular primes:** The standard Selmer group is not cotorsion over Λ. The ±-theory works but has complications: the ±-Selmer groups depend on a choice of sign, and the relationship between them and the actual Sha is indirect.
- **Rank ≥ 2:** Even with the full main conjecture, extracting |Sha[p^∞]| for rank ≥ 2 requires computing the p-adic regulator ℒ_p(E), which is a determinant of p-adic heights on a rank ≥ 2 Mordell-Weil group. These heights are hard to compute to sufficient p-adic precision.
- **Explicit computation:** Computing L_p(E, s) to high p-adic precision requires many modular symbols. For large conductor, this is computationally expensive.

## Cross-Group Connections

- **Group A (Iwasawa):** The Iwasawa main conjecture is the bridge between L_p(E) and Sha. Group A's work on the main conjecture directly determines the p-part of Sha.
- **Group E (p-adic Methods):** D-004 and Group E overlap significantly. The p-adic L-function construction, Perrin-Riou's regulator, and the Coleman map are shared tools.
- **Group D (D-010):** The Iwasawa-theoretic framework for Sha[p^∞] is the subject of D-010. D-004 focuses on the L-function side; D-010 focuses on the Selmer group side.
- **Group D (D-001):** Kato's Euler system is the source of the divisibility char | (L_p). The Euler system method (D-001) and the p-adic method (D-004) are two sides of the same coin.

## Classification

**Type:** Core, Active
**Difficulty:** High (supersingular, rank ≥ 2), Moderate (ordinary, rank ≤ 1)
**Impact:** Deepest known approach to the p-part of BSD; proved for ordinary primes of analytic rank ≤ 1.
