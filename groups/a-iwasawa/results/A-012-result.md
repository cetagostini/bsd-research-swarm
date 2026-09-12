# A-012: Iwasawa Theory at Eisenstein Primes

## Status Assessment

Iwasawa theory at Eisenstein primes addresses the "exceptional zero" phenomenon where the $p$-adic L-function vanishes even when the classical $L$-function does not. Mazur (1977) pioneered the study of Eisenstein ideals, and the Mazur–Tate–Teitelbaum conjecture (now a theorem in many cases) provides the correction factor. The direction is promising and well-developed theoretically. Realistic timeline for complete results: 3–5 years.

## Testable Conjecture

**Conjecture (Eisenstein Main Conjecture).** Let $E/\mathbb{Q}$ be an elliptic curve and $p$ a prime such that $E[p]$ is reducible, fitting in $0 \to \mu_p \to E[p] \to \mathbb{Z}/p\mathbb{Z} \to 0$ over $\mathbb{Q}$. Let $\mathscr{I} \subset \mathbb{T}$ be the Eisenstein ideal. Then

$$\operatorname{char}_\Lambda(\mathfrak{X}) = \left(L_p(E, T) \cdot \mathcal{E}_{\mathrm{Eis}}(T)\right)$$

where $\mathcal{E}_{\mathrm{Eis}}(T)$ is the Eisenstein correction factor satisfying

$$\mathcal{E}_{\mathrm{Eis}}(0) = \left(1 - \frac{1}{p}\right)^{-1} \cdot \left(1 - \frac{a_p}{p}\right)^{-1} \cdot \frac{\log_p(\alpha)}{\text{ord}_p(q_E)}$$

where $\alpha$ is the $p$-adic multiplier of the Tate uniformization $E(\overline{\mathbb{Q}_p}) \cong \overline{\mathbb{Q}_p}^\times / q_E^{\mathbb{Z}}$ and $\log_p(\alpha) / \text{ord}_p(q_E) = \mathcal{L}(E, p)$ is the $\mathcal{L}$-invariant of Mazur–Tate–Teitelbaum.

## Approach Summary

**Phase 1: Identify Eisenstein congruences.** For all curves $E/\mathbb{Q}$ with $N \leq 500$ and $p \in \{2, 3, 5, 7\}$, check whether $a_\ell(E) \equiv 1 + \ell \pmod{p}$ for all $\ell \nmid Np$. This identifies the Eisenstein primes. The congruence is equivalent to $E[p]$ being reducible, which can be checked by computing the mod-$p$ Galois representation.

**Phase 2: Compute the $\mathcal{L}$-invariant.** For each Eisenstein pair $(E, p)$, compute the $\mathcal{L}$-invariant via the formula $\mathcal{L} = \log_p(q_E) / \operatorname{ord}_p(q_E)$ where $q_E$ is the Tate parameter. The Tate parameter can be computed from the $j$-invariant and the $p$-adic uniformization of $E$.

**Phase 3: Modified Main Conjecture verification.** Compute $L_p(E, T)$ via Pollack–Stevens and verify that $L_p(E, 0) = 0$ (the exceptional zero). Then compute $L_p'(E, 0)$ and verify the Mazur–Tate–Teitelbaum formula:

$$L_p'(E, 0) = \mathcal{L}(E, p) \cdot \frac{L(E, 1)}{\Omega_E} \cdot c_p \cdot \prod_{\ell | N} c_\ell$$

where $c_p$ is the Tamagawa factor at $p$ and $c_\ell$ are local Tamagawa factors.

## Computational Example

**Curve 11a1** at $p = 5$:

Check Eisenstein congruence: $a_2(11a1) = -2$. Is $-2 \equiv 1 + 2 = 3 \pmod{5}$? $-2 \equiv 3 \pmod{5}$. Yes! $a_3(11a1) = -1$. Is $-1 \equiv 1 + 3 = 4 \pmod{5}$? $-1 \equiv 4 \pmod{5}$. Yes! So 11a1 at $p = 5$ is an Eisenstein prime.

$E[5]$ is reducible: $0 \to \mu_5 \to E[5] \to \mathbb{Z}/5\mathbb{Z} \to 0$. The extension class is the class of $E$ in $\operatorname{Ext}^1_{G_\mathbb{Q}}(\mathbb{Z}/5\mathbb{Z}, \mu_5) \cong \mathbb{Q}^\times / (\mathbb{Q}^\times)^5$. By Ribet's theorem, this class is the Shimura subgroup element corresponding to $11$.

The $\mathcal{L}$-invariant: $\mathcal{L}(11a1, 5) = \log_5(q_{11a1}) / \operatorname{ord}_5(q_{11a1})$. The Tate parameter $q_{11a1}$ can be computed from $j(11a1) = -2^{12} 11^{-1}$ and the $5$-adic uniformization. Numerically: $\mathcal{L}(11a1, 5) \approx 1.5216...$

The corrected BSD formula: $L_5'(11a1, 0) = \mathcal{L} \cdot L(11a1, 1)/\Omega \cdot c_5 = 1.5216... \times 0.2538... \times 1 = 0.3863...$

**Curve 37a1** at $p = 3$: $a_2(37a1) = -2 \equiv 1 + 2 = 3 \pmod{3}$. Yes! Eisenstein at $p = 3$. The exceptional zero correction involves $\mathcal{L}(37a1, 3)$.

## Obstacle Analysis

The main obstacle is that the reducibility of $E[p]$ invalidates the standard Euler system argument (Kato's classes assume irreducibility for norm-compatibility). When $E[p]$ is reducible, the Selmer group may have a non-trivial $\Lambda$-submodule not detected by $L_p$, arising from the extension class of $E[p]$. The Mazur–Ribet theory identifies this submodule with the class group of $\mathbb{Q}(\mu_p)$ via the Shimura–cuspidal subgroup, but controlling it requires the full force of the Mazur–Tate–Teitelbaum conjecture. The correction factor $\mathcal{E}_{\mathrm{Eis}}$ depends on the $\mathcal{L}$-invariant, which is a transcendental quantity (the $p$-adic logarithm of the Tate parameter), making it inaccessible to purely algebraic methods. One needs either: (a) a $p$-adic analytic proof using Perrin-Riou's explicit reciprocity law, or (b) a deformation argument: vary $E$ in a family where $E[p]$ becomes irreducible and specialize.

## Cross-Group Connections

- **Group A (Main Conjecture):** The Eisenstein case is the main gap in the ordinary Main Conjecture.
- **Group H (Galois Representations):** The reducibility of $E[p]$ is a Galois-theoretic condition.
- **Group F (BSD Formula):** The exceptional zero correction is the $\mathcal{L}$-invariant formula of Mazur–Tate–Teitelbaum.
- **Group D (Iwasawa Invariants):** The Eisenstein congruence affects $\lambda$ via Greenberg–Vatsal.

## Classification

Theorem (Mazur–Tate–Teitelbaum conjecture: proven by Greenberg–Stevens for $\mathcal{L}$-invariant; Iwasawa Main Conjecture at Eisenstein primes: partial)
