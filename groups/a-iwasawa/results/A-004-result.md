# A-004: Iwasawa Theory for Imaginary Quadratic Fields

## Status Assessment

Iwasawa theory over imaginary quadratic fields is in active development. For CM curves, Rubin's Euler system gives the anticylotomic Main Conjecture unconditionally. For non-CM curves base-changed to $K$, the two-variable Main Conjecture is open but significant progress has been made by Brooks–Shimizu (2022) in the cyclotomic direction. The realistic timeline for the full two-variable Main Conjecture (non-CM case) is 8–15 years.

## Testable Conjecture

**Conjecture (Two-Variable Main Conjecture).** Let $K$ be an imaginary quadratic field with $p = \mathfrak{p}\bar{\mathfrak{p}}$ split, $E/\mathbb{Q}$ a non-CM elliptic curve with good ordinary reduction at $p$ satisfying the Heegner hypothesis for $K$. Let $G_\infty = \operatorname{Gal}(K_\infty/K) \cong \mathbb{Z}_p^2$ and $\Lambda(G_\infty) \cong \mathbb{Z}_p[[S, T]]$. Then

$$\operatorname{char}_{\Lambda(G_\infty)}\left(\operatorname{Sel}_{p^\infty}(E/K_\infty)^\vee / (\cdots)_{\mathrm{div}}\right) = \left(\mathscr{L}_p(E/K)\right)$$

where $\mathscr{L}_p(E/K) \in \mathbb{Z}_p[[S, T]]$ satisfies: for every ring class character $\psi$ of $K$ of conductor coprime to $p$,

$$\mathscr{L}_p(E/K)(\psi, 0) = \mathcal{E}_p(\psi) \cdot \frac{L(E/K, \psi, 1)}{\Omega_E^+ \cdot \Omega_K}$$

where $\mathcal{E}_p(\psi) = \left(1 - \frac{a_p \psi(\mathfrak{p})}{p}\right)\left(1 - \frac{\psi(\bar{\mathfrak{p}})}{a_p}\right)$.

## Approach Summary

**Phase 1: Anticylotomic direction.** Using the Chida–Hsieh (2018) construction of the anticylotomic $p$-adic L-function $\mathscr{L}_p^-(E/K) \in \Lambda^-$, verify computationally for curves with $N \leq 200$ and imaginary quadratic $K$ with $|D_K| \leq 100$. Compute Heegner points at layers of the anticylotomic tower and verify the Gross–Zagier formula at each layer.

**Phase 2: Cyclotomic direction over $K$.** Base-change $E$ to $K$ and study $\operatorname{Sel}_{p^\infty}(E/K_\infty^{\mathrm{cyc}})$. The Main Conjecture for $E/K$ over the cyclotomic tower follows from the Skinner–Urban result applied to $E/K$, provided $E/K$ satisfies their hypotheses. This gives the "vertical" variable of the two-variable conjecture.

**Phase 3: Patching the two variables.** Construct the two-variable $p$-adic L-function by interpolating $\mathscr{L}_p^-$ (anticylotomic) with the cyclotomic $p$-adic L-function of $E/K$. The key difficulty is showing compatibility: the specialization of $\mathscr{L}_p(E/K)$ to the anticylotomic line recovers $\mathscr{L}_p^-$, and to the cyclotomic line recovers $L_p(E/K, T)$.

## Computational Example

**Curve 11a1 over $K = \mathbb{Q}(\sqrt{-7})$** at $p = 5$:

$D_K = -7$, $p = 5$ splits in $K$ (since $5 \equiv 2 \pmod{7}$ and $\left(\frac{5}{7}\right) = -1$... actually $5$ is inert in $\mathbb{Q}(\sqrt{-7})$. Let us choose $K = \mathbb{Q}(\sqrt{-3})$ instead, where $p = 5$ splits as $\mathfrak{p}\bar{\mathfrak{p}}$.

The Heegner hypothesis: $11$ must split in $K$. $11 \equiv 2 \pmod{3}$, $\left(\frac{11}{3}\right) = -1$, so $11$ is inert. Choose $K = \mathbb{Q}(\sqrt{-11})$: $D_K = -11$. Then $5$ splits ($\left(\frac{5}{11}\right) = 1$ since $5^5 \equiv 1 \pmod{11}$). The Heegner hypothesis fails since $11 | D_K$. Choose $K = \mathbb{Q}(\sqrt{-23})$: $\left(\frac{5}{23}\right) = 1$, $\left(\frac{11}{23}\right) = 1$. Both $5$ and $11$ split. The ring class field tower has layers $H_0, H_1, \ldots$ with $[H_n : K] = 23 \cdot 5^{2n}$ (for the $\mathbb{Z}_5$-part).

Heegner point $y_n \in E(H_n)$ at layer $n$ of the anticylotomic tower: $\hat{h}(y_n) \sim L'(E^{(-23)}/\mathbb{Q}, 1) \cdot 5^n$ by Gross–Zagier.

## Obstacle Analysis

The main obstacle is the lack of a two-variable Euler system. Kato's Euler system lives over $\mathbb{Q}$ and gives control only in the cyclotomic direction. Heegner points give control in the anticylotomic direction but are rank-1 objects. Combining them into a single two-variable system requires either: (a) Beilinson–Flach elements for the Rankin–Selberg convolution $E \times \chi_K$, which give classes in both directions simultaneously, or (b) a direct construction of the two-variable $p$-adic L-function via $p$-adic integration on the product of two $p$-adic Lie groups. Strategy (a) is being pursued by Kings–Loeffler–Zerbes but requires the non-critical slope condition.

## Cross-Group Connections

- **Group B (Heegner Points):** The anticylotomic Euler system comes from Heegner points.
- **Group A (Anticylotomic Iwasawa):** The anticylotomic direction is the most developed part.
- **Group E (Two-variable p-adic L-functions):** The analytic construction of $\mathscr{L}_p(E/K)$.
- **Group F (BSD over number fields):** The two-variable Main Conjecture controls BSD for $E$ over all ring class fields of $K$.

## Classification

Theorem (CM case: Rubin; non-CM case: Conjecture)
