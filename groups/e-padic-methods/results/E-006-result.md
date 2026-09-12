# E-006 · Coleman's p-adic L-functions via Overconvergent Modular Symbols

## Direction ID and Title
E-006: Construction of p-adic L-functions for finite-slope eigenforms using Coleman's theory of overconvergent modular forms and Pollack–Stevens algorithmic modular symbols.

## Status Assessment
**Active.** The algorithmic construction of Pollack–Stevens (2011) is available for finite-slope forms. The theory extends beyond the ordinary case (Hida theory) to arbitrary finite slope $\alpha < k-1$. Numerical verification is ongoing; precision management remains a practical challenge.

## Testable Conjecture or Lemma

**Theorem (Pollack–Stevens, 2011).** Let $f = f_p(X) \in S_k^\dagger(\Gamma_0(Np))$ be a p-stabilised overconvergent eigenform of finite slope $\alpha$ (i.e., $U_p f = a_p f$ with $|a_p|_p = p^{(k-1)/2 - \alpha}$ where $0 \leq \alpha < k-1$). There exists a p-adic distribution $\mu_f$ on $\mathbb{Z}_p^\times$ such that for all critical integers $j$ with $1 \leq j \leq k-1$:

$$\int_{\mathbb{Z}_p^\times} x^j \, d\mu_f = \mathcal{E}(f, j) \cdot \frac{L(f, j)}{(2\pi i)^{j-1} / (j-1)!}$$

where $\mathcal{E}(f, j) = (1 - p^{j-1}/\alpha)(1 - p^{j}/\beta)$ with $\alpha\beta = p^{k-1}$, $\alpha + \beta = a_p$.

**Conjecture (Measure vs. Distribution).** The distribution $\mu_f$ is a measure (i.e., has bounded denominators) if and only if the Fourier coefficients $a_n(f)$ satisfy $|a_n|_p \leq C$ for a constant $C$ independent of $n$. For ordinary forms this is automatic; for finite slope it depends on the growth of $p$-adic valuations.

## Approach Summary

1. **Overconvergent modular forms:** The space $S_k^\dagger(\Gamma_0(Np))$ of overconvergent modular forms consists of sections of $\omega^k$ on the ordinary locus of the modular curve, extended to a strict neighborhood of the ordinary locus. The $U_p$-operator acts compactly on this space.

2. **Coleman's control theorem:** The natural inclusion $S_k(\Gamma_0(Np)) \hookrightarrow S_k^\dagger(\Gamma_0(Np))$ has finite-cokernel: every finite-slope overconvergent eigenform is classical (Coleman, 1997). This means the distribution $\mu_f$ interpolates genuine classical L-values.

3. **Pollack–Stevens algorithm:** 
   - Start with the classical modular symbol $\{f\}: \Delta_0 \to \mathbb{Q}_p$ (a function on divisors on $\mathbb{P}^1(\mathbb{Q})$).
   - Lift to an overconvergent modular symbol $\{f\}^\dagger$ by solving a system of linear equations in the $U_p$-eigenspace.
   - The distribution $\mu_f$ is the image of $\{f\}^\dagger$ under the Manin map $\mathbb{P}^1(\mathbb{Q}) \to \mathcal{D}(\mathbb{Z}_p^\times)$ (distributions on $\mathbb{Z}_p^\times$).

4. **Precision management:** The $U_p$-operator on overconvergent symbols is a compact operator on a p-adic Banach space. Its eigenvalues cluster; computing the eigenvector corresponding to $a_p$ requires inverting $(U_p - a_p)$, which loses precision proportional to $\text{ord}_p(a_p - \text{other eigenvalues})$.

## Computational Example

**Setup.** Consider the elliptic curve $E = 17a1$ ($y^2 + xy + y = x^3 - x^2 - x - 14$, conductor 17).

**At $p = 2$:** $a_2 = -2$ (supersingular: $|a_2|_2 = 1/2 > 2^{-1/2}$, so the slope is $\alpha = 1$, not ordinary).

The p-stabilised eigenform $f_2 \in S_2^\dagger(\Gamma_0(34))$ has $U_2$-eigenvalue $a_2 = -2$. The Hecke polynomial at $2$ is $X^2 + 2X + 2$, with roots $\alpha = -1 + i$, $\beta = -1 - i$ in $\overline{\mathbb{Q}_2}$. Since $|a_2|_2 = 1/2$, this is the "large" root; the slope is $\alpha = 1$.

**Pollack–Stevens computation:**
1. Compute the classical modular symbol $\{f\}: \text{Div}^0(\mathbb{P}^1(\mathbb{Q})) \to \mathbb{Q}$.
2. Lift to overconvergent symbol: solve $(U_2 - a_2)\{f\}^\dagger = \{f\}$ in the Banach space of overconvergent symbols.
3. The distribution $\mu_f$ on $\mathbb{Z}_2^\times$ satisfies $\int x^1 d\mu_f = \mathcal{E}(f, 1) \cdot L(f, 1) / \Omega_f$.
4. Since this is a weight-2 form attached to an elliptic curve: $L(f, 1) = L(E, 1) = 0$ (rank 1 curve!), so the central value vanishes classically. The p-adic L-function $L_p(E, s)$ has a zero at $s = 1$ of order equal to the rank.

**At $p = 3$:** $a_3 = 2$, ordinary (since $|a_3|_3 = |2|_3 = 1 < 3^{1/2}$). This falls under Hida theory (slope 0), and Pollack–Stevens recovers the ordinary p-adic L-function.

**At $p = 5$:** $a_5 = -2$, ordinary ($|a_5|_5 = 1$). Again slope 0, recovered by Hida theory.

**Supersingular example with $a_p = 0$:** $E = 11a1$, $p = 3$: $a_3 = 0$, supersingular with slope $1/2$. The Hecke polynomial is $X^2 + 3$, roots $\pm\sqrt{-3}$. Pollack's plus/minus p-adic L-functions $L_p^\pm(E, s)$ are constructed via the ± eigenspaces of the $U_3$-operator on overconvergent symbols.

## Obstacle Analysis

1. **Precision loss:** The operator $(U_p - a_p)^{-1}$ on overconvergent symbols loses p-adic precision proportional to the number of near-eigenvalues. For high-slope forms, precision degrades rapidly.

2. **Convergence:** The iterative construction of $\mu_f$ (lifting the classical symbol to an overconvergent one) converges only in the finite-slope case. For slope zero, convergence is guaranteed by Hida's theory. For higher slopes, convergence depends on the spectral gap between $a_p$ and other $U_p$-eigenvalues.

3. **Extension to weight 1:** Coleman's control theorem fails for weight 1 forms. Constructing p-adic L-functions for weight-1 eigenforms requires different techniques (e.g., Bellaïche–Chenevier's eigenvarieties).

4. **Supersingular case:** When $a_p = 0$ (pure slope $(k-1)/2$), the $U_p$-eigenvalue is zero, and the construction requires Pollack's plus/minus decomposition, which is not canonical.

## Cross-Group Connections

- **Group A (Classical BSD):** The overconvergent p-adic L-function interpolates classical L-values; its central value encodes rank and Sha.
- **E-001 (Two-variable):** The overconvergent construction can be extended to families (eigenvarieties), giving a higher-dimensional analogue of the two-variable L-function.
- **E-009 (Supersingular BSD):** The overconvergent construction is the primary tool for defining $L_p(E, s)$ at supersingular primes.
- **E-008 (Exceptional zeros):** The overconvergent framework provides a unified treatment of exceptional zeros for all reduction types.

## Classification
**Overconvergent methods.** Algorithmic p-adic analysis extending Hida theory to all finite slopes.
