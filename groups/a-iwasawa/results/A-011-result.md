# A-011: Two-Variable $p$-adic L-functions for Imaginary Quadratic Base

## Status Assessment

The two-variable $p$-adic L-function for $E/K$ (imaginary quadratic $K$) is the analytic cornerstone of the Bertolini–Darmon program. Construction is complete only in the CM case (Rubin's elliptic units) and partial in the non-CM case (Hsieh for the anticylotomic direction, Castella–Hsieh for progress toward the full two-variable object via Hida families). The direction is largely speculative for non-CM curves. Realistic timeline: 10–15 years.

## Testable Conjecture

**Conjecture (Two-Variable $p$-adic L-function).** Let $K$ be an imaginary quadratic field with $p = \mathfrak{p}\bar{\mathfrak{p}}$ split, $E/\mathbb{Q}$ with good ordinary reduction at $p$ satisfying the Heegner hypothesis for $K$. There exists a unique element

$$\mathscr{L}_p(E/K) \in \Lambda(G_\infty) = \mathbb{Z}_p[[S, T]]$$

such that for every ring class character $\psi$ of $K$ of conductor $\mathfrak{f}$ coprime to $p$ and every integer $j \geq 0$ of appropriate parity,

$$\mathscr{L}_p(E/K)(\psi, j) = \mathcal{E}_p(\psi, j) \cdot \frac{L(E/K, \psi, j+1)}{\Omega_E^{\pm} \cdot \langle f, f \rangle_K}$$

where the specialization at $(\psi, j)$ corresponds to evaluating at $(S, T) = (\psi(\mathfrak{p}) - 1, \psi(\mathfrak{p})^{j} \cdot [\gamma]^j - 1)$ for a topological generator $\gamma$ of the cyclotomic $\Gamma$, and $\mathcal{E}_p$ is the Euler factor

$$\mathcal{E}_p(\psi, j) = \left(1 - \frac{a_p \psi(\mathfrak{p})}{p^{j+1}}\right)\left(1 - \frac{\overline{\psi(\mathfrak{p})}}{a_p p^j}\right)$$

## Approach Summary

**Phase 1: One-variable specializations.** Verify the two-variable interpolation by computing the one-variable specializations separately:
- **Cyclotomic direction** ($S = 0$): $L_p(E/K, T) \in \mathbb{Z}_p[[T]]$ is the cyclotomic $p$-adic L-function of $E/K$, computable via Pollack–Stevens for the base-changed form $f_K$.
- **Anticylotomic direction** ($T = 0$): $\mathscr{L}_p^-(E/K, S) \in \mathbb{Z}_p[[S]]$ is the Bertolini–Darmon / Chida–Hsieh anticylotomic $p$-adic L-function, computable via Heegner point integration.

**Phase 2: Double $p$-adic integration.** The Bertolini–Darmon construction of $\mathscr{L}_p(E/K)$ uses $p$-adic integration on the product $X_p \times \mathbb{Z}_p^\times$ where $X_p$ is the $p$-adic upper half-plane. The integrand is the $p$-adic avatar of the Rankin–Selberg kernel. Implement this double integral in SageMath for specific $(E, K, p)$ and verify the interpolation formula.

**Phase 3: Hida family approach.** An alternative construction via Hida families: let $\mathbf{f}$ be the Hida family through $f$ (the newform of $E$), and let $\mathbf{g}$ be the Hida family through a CM form associated to $K$. The Rankin–Selberg convolution $\mathbf{f} \times \mathbf{g}$ gives a two-variable $p$-adic L-function in $\mathbb{Z}_p[[S, T]]$ where $S$ parametrizes the anticylotomic family and $T$ the cyclotomic family. Castella–Hsieh (2020) made progress on this approach.

## Computational Example

**$E = 11a1$, $K = \mathbb{Q}(\sqrt{-7})$, $p = 5$:**

$D_K = -7$. Check: $5$ splits in $K$? $\left(\frac{5}{7}\right) = \left(\frac{-2}{7}\right) = (-1)^{(7^2-1)/8} = (-1)^6 = 1$. Yes, $5$ splits. Heegner hypothesis: $11$ splits in $K$? $\left(\frac{11}{7}\right) = \left(\frac{4}{7}\right) = 1$. Yes.

The two-variable $p$-adic L-function $\mathscr{L}_5(11a1/\mathbb{Q}(\sqrt{-7})) \in \mathbb{Z}_5[[S, T]]$:

At $(S, T) = (0, 0)$: $\mathscr{L}_5(0, 0) = \mathcal{E}_5(\mathbf{1}, 0) \cdot L(11a1/\mathbb{Q}(\sqrt{-7}), 1) / (\Omega \cdot \langle f, f \rangle_K)$. The $L$-value $L(11a1/\mathbb{Q}(\sqrt{-7}), 1) = L(11a1, 1) \cdot L(11a1 \times \chi_{-7}, 1)$ by factorization of the Dedekind zeta function.

At $(S, T) = (\zeta_5 - 1, 0)$ for the anticylotomic character of conductor $5$: $\mathscr{L}_5(\zeta_5 - 1, 0) = \mathscr{L}_p^-(11a1/\mathbb{Q}(\sqrt{-7}), \zeta_5 - 1)$, the anticylotomic $p$-adic L-function at a finite-order character.

## Obstacle Analysis

The fundamental difficulty is constructing a single $p$-adic analytic object that simultaneously interpolates in two independent directions. In the cyclotomic direction, the modular symbol $\{a/p^n\}_f$ provides the building block. In the anticylotomic direction, Heegner points $y_n \in E(K_n^-)$ provide the building block. Combining them requires a "two-variable modular symbol" or a "double $p$-adic integral" that converges in both variables simultaneously. The convergence issue is technical: the anticylotomic integral converges on a smaller domain than the cyclotomic one, and extending the domain requires careful analysis of the $p$-adic measures involved. The Shimura–Waldspurger period for $L(E \times \chi_K, s)$ adds another layer of complexity.

## Cross-Group Connections

- **Group A (Imaginary Quadratic Fields):** The two-variable $p$-adic L-function is the analytic input for the two-variable Main Conjecture.
- **Group A (Anticylotomic Iwasawa):** The anticylotomic specialization is the Chida–Hsieh $p$-adic L-function.
- **Group D (p-adic L-functions):** The cyclotomic specialization is the Mazur–Swinnerton-Dyer $p$-adic L-function.
- **Group G (Automorphic Forms):** The Hida family construction requires automorphic input.

## Classification

Speculation (proven in CM case; non-CM case: largely open)
