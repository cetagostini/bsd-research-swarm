# B-004: Rubin's Euler System for CM Elliptic Curves

## Direction ID and Title
B-004 — Rubin's Euler System for CM Elliptic Curves

## Status Assessment
Rubin's Euler system of elliptic units for CM elliptic curves is the most complete instance of the Euler system method. For $E/\mathbb{Q}$ with CM by an order in an imaginary quadratic field $K$ and $p$ split in $K$, the Euler system bound yields $\operatorname{rk}_p \operatorname{Sel}(E/K) \leq \operatorname{ord}_{s=1} L(E/K,s)$ unconditionally. Combined with the Gross-Zagier formula for CM twists and the fact that $r \leq 1$ cases are settled, this proves weak BSD for analytic rank $\leq 1$ for CM curves. The full BSD formula (including the leading term) follows from the Iwasawa main conjecture for CM fields, proved by Rubin.

## Testable Conjecture or Lemma

**Theorem B-004 (Rubin).** Let $E/\mathbb{Q}$ have CM by $\mathcal{O}_K$ for an imaginary quadratic field $K$, and let $p$ be a prime of good ordinary reduction splitting in $K$ as $p = \mathfrak{p}\bar{\mathfrak{p}}$. Let $\{c_m\}$ be the Euler system of elliptic units with $c_m \in E(K(m)) \otimes \mathbb{Q}$ for squarefree $m$ composed of primes splitting in $K$. Then:

(a) **Selmer bound:** $\dim_{\mathbb{F}_p} \operatorname{Sel}(E/K)[p] \leq \operatorname{ord}_{s=1} L(E/K, s)$.

(b) **Characteristic ideal equality (IMC):** $\operatorname{char}_\Lambda\left(\operatorname{Sel}(E/K_\infty)^\vee\right) = \left(\mathcal{L}_p^{\mathrm{Katz}}\right)$ where $\mathcal{L}_p^{\mathrm{Katz}}$ is the Katz $p$-adic L-function and $K_\infty = K(E[p^\infty])$.

(c) **Leading term formula:** Specializing (b) at the augmentation ideal yields:
$$v_p\left(\frac{L^{(r)}(E/K, 1)}{r! \cdot \Omega_E}\right) = v_p\left(\frac{|\operatorname{III}(E/K)[p^\infty]| \cdot \prod c_v^{(p)}}{|E(K)_{\mathrm{tors}}|_p^2}\right)$$

## Approach Summary

The Euler system of elliptic units arises from Siegel units $g_a \in \mathcal{O}(Y_1(N))^\times$ for $a \in (\mathbb{Z}/N\mathbb{Z})^\times$. Under the CM period map $\psi: E \to \mathbb{C}^\times/q^\mathbb{Z}$ (the Weierstrass parametrization), these units map to points $c_m = \psi(g_a(m)) \in E(K(m)) \otimes \mathbb{Q}$. The norm compatibility $\operatorname{Tr}_{K(m\ell)/K(m)}(c_{m\ell}) = P_\ell(\operatorname{Frob}_\mathfrak{l}^{-1}) c_m$ follows from the Hecke equivariance of Siegel units.

Rubin's method proceeds by defining the "Euler system ideal" $\mathcal{Z} = \operatorname{char}_\Lambda(\text{image of } \{c_m\} \text{ in } H^1_\Sigma(K, T \otimes \Lambda))$ and proving the bounding inequality $\mathcal{Z} \subseteq \operatorname{char}_\Lambda(\operatorname{Sel}(T/K_\infty)^\vee)$ via the Bockstein homomorphism and global duality. The equality $\mathcal{Z} = \operatorname{char}_\Lambda(\operatorname{Sel}^\vee)$ in the CM case uses the fact that the elliptic units generate the maximal "Euler-module" submodule of the local cohomology at $\mathfrak{p}$.

The supersingular case ($p$ inert or ramified in $K$) requires Kobayashi's $\pm$-Selmer groups and a modified Euler system with $\pm$-norm relations, using the theory of plus/minus logarithms on $E(\mathbb{Q}_p)$.

## Computational Example

- **$E = $ 27a1**: $y^2 + y = x^3 - 7$, CM by $\mathbb{Z}[\omega]$ ($K = \mathbb{Q}(\sqrt{-3})$). For $p = 7$ (split in $K$): compute the Euler system class $c_1$ and verify $v_7(L(E/K, 1)/\Omega_E) = v_7(|\operatorname{III}| \cdot \prod c_v / |E_{\mathrm{tors}}|^2)$. Here $r = 0$, so $L(E/K,1) \neq 0$.
- **$E = $ 32a1**: $y^2 = x^3 + 4x$, CM by $\mathbb{Z}[i]$ ($K = \mathbb{Q}(i)$). $p = 5$ (split as $(2+i)(2-i)$). Test the Selmer bound: $\operatorname{rk}(E(\mathbb{Q})) = 0$, so $\operatorname{Sel}(E/K)[5]$ should be trivial.
- **$E = $ 49a1**: $y^2 + xy = x^3 - x^2 - 2x - 1$, CM by $\mathbb{Z}[(1+\sqrt{-7})/2]$ ($K = \mathbb{Q}(\sqrt{-7})$). $p = 2$ (split: $2 = \frac{1+\sqrt{-7}}{2} \cdot \frac{1-\sqrt{-7}}{2}$). $r = 0$: verify $L(E/K,1)/\Omega_E = |\operatorname{III}| \cdot \prod c_v / |E_{\mathrm{tors}}|^2$.

## Obstacle Analysis

For rank $\geq 2$ CM curves, the lower bound $\operatorname{rk}(E(K)) \geq \operatorname{ord}_{s=1} L(E/K, s)$ requires constructing global points of infinite order, which the Euler system alone cannot provide. The Euler system gives the correct upper bound, but equality demands the existence of $r$ independent points in $E(K) \otimes \mathbb{Q}$. For $r = 1$, the point comes from Heegner/Kolyvagin; for $r \geq 2$, no general construction is known. The supersingular case additionally requires the Kobayashi $\pm$-theory, and the Euler system in this setting has weaker norm relations (only $\pm$-compatible, not fully compatible).

## Cross-Group Connections
- **Group A (BSD Formula)**: The characteristic ideal equality (c) is the $p$-part of BSD for CM curves.
- **Group D (Heegner Points)**: For $r = 1$, the non-trivial Heegner point provides the lower bound.
- **Group F (Iwasawa Theory)**: Rubin's IMC is a foundational result in Iwasawa theory.

## Classification
Theorem (Selmer bound and IMC for CM curves); Partial Result (full BSD for rank $\geq 2$)
