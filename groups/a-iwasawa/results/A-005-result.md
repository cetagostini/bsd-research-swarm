# A-005: Anticylotomic Iwasawa Theory

## Status Assessment

Anticylotomic Iwasawa theory is one of the most successful directions in the field. The Main Conjecture is proven in the analytic rank $\leq 1$ case by Chida–Hsieh (2018) and Castella (2019), and $\mu = 0$ is proven by Brooks (2021). The remaining challenge is the generic rank case ($\operatorname{ord}_{s=1} L(E^{(K)}, s) \geq 2$), which requires new Euler system input. Realistic timeline for the higher-rank case: 5–8 years.

## Testable Conjecture

**Conjecture (Anticylotomic Main Conjecture, full rank).** Let $E/\mathbb{Q}$, $K$ an imaginary quadratic field satisfying the Heegner hypothesis, $p \nmid 2ND_K$ splitting in $K$. Let $K_\infty^-/K$ be the anticylotomic $\mathbb{Z}_p$-extension with layers $K_n^-$. Then

$$\operatorname{char}_{\Lambda^-}\left(\operatorname{Sel}^-(E/K_\infty^-)^\vee\right) = \left(\mathscr{L}_p^-(E/K)\right)$$

where $\mathscr{L}_p^-(E/K) \in \Lambda^- = \mathbb{Z}_p[[T^-]]$ is the Bertolini–Darmon anticylotomic $p$-adic L-function, and

$$\lambda^- = \operatorname{ord}_{s=1} L(E^{(K)}/\mathbb{Q}, s)$$

where $E^{(K)}$ is the quadratic twist of $E$ by $K$, and $\mu^- = 0$.

## Approach Summary

**Phase 1: Heegner point computation in towers.** For curves with $N \leq 200$ and imaginary quadratic $K$ with $|D_K| \leq 100$, compute Heegner points $y_n \in E(K_n^-)$ at layers $n = 0, 1, \ldots, 10$ of the anticylotomic tower using Magma's Heegner point machinery. Verify the norm-compatibility $N_{m/n}(y_m) = a_p^{m-n} \cdot y_n$ (up to finite error).

**Phase 2: Stark–Heegner points.** For primes $p$ where the Heegner hypothesis fails (primes dividing $N$ do not split in $K$), compute Stark–Heegner points via rigid analytic methods (Bertolini–Darmon). These are $p$-adic points on $E(\mathbb{Q}_p)$ that play the role of Heegner points in the non-split case.

**Phase 3: Higher-rank Euler system.** The key theoretical advance needed is an Euler system of rank $> 1$ in the anticylotomic direction. The Beilinson–Flach elements for $E \times E^{(K)}$ provide classes in $H^1(K_n^-, T_p E)$ that are norm-compatible in the anticylotomic tower. If these elements can be shown to generate a rank-$r$ submodule (where $r = \operatorname{ord}_{s=1} L(E^{(K)}, s)$), the Rubin–Kolyvagin machine would give the Main Conjecture.

## Computational Example

**Curve 37a1** ($y^2 + y = x^3 - x$, rank 1 over $\mathbb{Q}$) with $K = \mathbb{Q}(\sqrt{-3})$, $p = 5$:

$D_K = -3$. Check: $37 \nmid D_K$, $5$ splits in $K$ (since $5 \equiv 2 \pmod{3}$, $\left(\frac{5}{3}\right) = -1$... $5$ is actually inert in $\mathbb{Q}(\sqrt{-3})$. Choose $p = 7$: $7 \equiv 1 \pmod{3}$, so $7$ splits. The Heegner hypothesis: $37$ splits in $K$? $\left(\frac{37}{3}\right) = \left(\frac{1}{3}\right) = 1$. Yes.

The anticylotomic tower $K_n^-$ has $[K_n^- : K] = 7^n$ (for the $\mathbb{Z}_7$-part). At layer $n = 0$: $y_0 \in E(K)$ is a Heegner point with $\hat{h}(y_0) \sim L'(E^{(-3)}, 1)$. The twist $E^{(-3)}: y^2 + y = x^3 + 3x^2 + 3x$ has rank $\leq 1$. If $L(E^{(-3)}, 1) = 0$, then $\lambda^- \geq 1$ and the Main Conjecture predicts $\lambda^- = 1$.

## Obstacle Analysis

The main obstacle for the higher-rank case is that Heegner points form a rank-1 Euler system: the Heegner point $y_n$ generates a cyclic submodule of $E(K_n^-) \otimes \mathbb{Z}_p$. When $\operatorname{ord}_{s=1} L(E^{(K)}, s) \geq 2$, the Selmer group has $\mathbb{Z}_p$-corank $\geq 2$, and a single Heegner point cannot control it. The Beilinson–Flach elements offer a higher-rank input, but their norm-compatibility in the anticylotomic direction is only known under the non-critical slope condition ($a_p(E) \neq a_p(E^{(K)})$), which fails when the two curves are congruent mod $p$. A potential workaround is to use congruence arguments: if the Main Conjecture is known for a curve $E'$ congruent to $E$ mod $p$ with $\operatorname{ord}_{s=1} L(E'^{(K)}, s) = 1$, then the Eisenstein congruence transfers the result to $E$.

## Cross-Group Connections

- **Group B (Heegner Points):** Direct computation of the anticylotomic Euler system.
- **Group A (Imaginary Quadratic Fields):** The anticylotomic direction is one component of the two-variable theory.
- **Group C (Euler Systems):** Beilinson–Flach elements as higher-rank input.
- **Group F (BSD Formula):** The anticylotomic Main Conjecture controls BSD for quadratic twists.

## Classification

Theorem (rank $\leq 1$ case; Conjecture for rank $\geq 2$)
