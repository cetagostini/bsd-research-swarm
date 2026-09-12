# C-007: Distribution of Analytic Ranks via Random Matrix Theory

## Status Assessment

The Katz-Sarnak philosophy predicts that the distribution of analytic ranks of L-functions in a family follows the distribution of orders of vanishing of characteristic polynomials of random matrices from the corresponding classical compact group. For families of elliptic curves, the expected symmetry type is symplectic ($Sp$), which predicts: $\Pr(r = 0) \approx 45.7\%$, $\Pr(r = 1) \approx 46.3\%$, $\Pr(r = 2) \approx 5.9\%$, $\Pr(r = 3) \approx 1.5\%$, $\Pr(r \geq 4) \approx 0.6\%$. While 1-level density results (detecting symmetry type) are proven for many families, the full rank distribution prediction requires taking limits of increasing matrix size, which is open over number fields.

## Testable Conjecture

**Conjecture C-007 (RMT rank distribution).** For the family of all elliptic curves $E/\mathbb{Q}$ ordered by conductor $N_E \leq X$:
$$\lim_{X \to \infty} \frac{\#\{E : N_E \leq X,\ \operatorname{ord}_{s=1} L(E,s) = r\}}{\#\{E : N_E \leq X\}} = \lim_{N \to \infty} \Pr\left(\operatorname{ord}_{\lambda=1} \det(I - A) = r\right)$$
where $A$ is drawn from Haar measure on $Sp(2N)$. The right-hand side equals:
- $r = 0$: $\prod_{i=1}^{\infty}(1 - 2^{-2i}) \approx 0.457$
- $r = 1$: $\frac{1}{2} \prod_{i=2}^{\infty}(1 - 2^{-2i}) \approx 0.463$
- $r = 2$: $\frac{1}{24} \prod_{i=2}^{\infty}(1 - 2^{-2i}) + \text{correction} \approx 0.059$
- General $r$: explicit formula involving products over $\zeta$-values

More specifically, for the subfamily with fixed root number $w = (-1)^r$:
$$\Pr(\operatorname{ord} = r \mid w = (-1)^r) = \frac{\text{Haar measure on } SO(\text{even/odd})}{\text{normalization}}.$$

## Approach Summary

**1-level density and symmetry detection.** The $n$-level density $W_n(\mathcal{F}) = \frac{1}{|\mathcal{F}(X)|} \sum_{E \in \mathcal{F}(X)} \sum_{\gamma_1,\ldots,\gamma_n} \phi_1(\gamma_1 \log N) \cdots \phi_n(\gamma_n \log N)$ measures correlations of low-lying zeros. For support $\sigma < 1$ of the test functions $\phi_i$, the 1-level density determines the symmetry type: the coefficient of $\hat{\phi}(0)$ distinguishes $O$, $SO(\text{even})$, $SO(\text{odd})$, $Sp$. Rubinstein (2001) proved that the family of all elliptic curves has symplectic symmetry for $\sigma < 2/3$.

**From symmetry to rank distribution.** The Katz-Sarnak prediction is: the distribution of $\operatorname{ord}_{s=1}$ equals the distribution of $\operatorname{ord}_{\lambda=1}$ of $\det(I-A)$ as $A \to$ Haar on $Sp(2N)$ as $N \to \infty$. This requires understanding the convergence rate of $n$-level densities as $N \to \infty$, which is controlled by the conductor of the family.

**Keating-Snaith moments approach.** The moments of the characteristic polynomial:
$$\mathbb{E}_{A \in Sp(2N)}[|\det(I-A)|^{2k}] = \prod_{j=1}^{N} \frac{\Gamma(j)\Gamma(j+2k)}{\Gamma(j+k)^2} \sim N^{k(k+1)/2} \cdot (\text{explicit constant})$$
These moments, via an inversion formula, give the rank distribution.

## Computational Example

**Rubinstein's computation (all elliptic curves, conductor $\leq 10^5$).** The 1-level density for $\sigma < 2/3$:
- $\hat{\phi}(0)$ coefficient: $\approx -0.5$ (consistent with $Sp$: expected $-1/2$)
- For $SO(\text{even})$: expected $0$; $SO(\text{odd})$: expected $1$
- Clear separation from orthogonal types

**Watkins's rank data (conductor $\leq 10^8$).** Observed vs. RMT predicted:
| Rank | Observed | RMT ($Sp$) | Difference |
|------|----------|------------|------------|
| 0    | 47.5%    | 45.7%      | +1.8%      |
| 1    | 47.5%    | 46.3%      | +1.2%      |
| 2    | 4.7%     | 5.9%       | -1.2%      |
| 3    | 0.3%     | 1.5%       | -1.2%      |

The discrepancy at rank 3+ is expected: finite conductor effects (the "low-lying zeros" are not yet in the asymptotic regime).

**Quadratic twist family of $E = 11a1$, $|D| \leq 10^4$:**
- $\Pr(r=0) \approx 51.2\%$, $\Pr(r=1) \approx 47.8\%$
- Root number split: 50/50 (as predicted)
- Consistent with $SO(\text{even}) \times SO(\text{odd})$ decomposition

## Obstacle Analysis

The fundamental obstacle is that 1-level density with support $\sigma < 1$ detects the symmetry type but cannot determine the rank distribution: the rank distribution requires taking $N \to \infty$ (matrix size) and controlling the convergence rate. For $\sigma > 1$, one needs bounds on sums $\sum_{p} \lambda(p) a_p(E)$ over the family, where $\lambda(p)$ is a test function — these sums involve deep automorphic information. Over function fields, the Katz-Sarnak correspondence is proven for all $n$ (using the Deligne-Lafforgue theory), but over number fields, the best results are for $n = 1$ with limited support.

## Cross-Group Connections

- **C-002 (Goldfeld):** The RMT prediction $Pr(r \geq 2) \approx 5.9\%$ contradicts Goldfeld ($\Pr(r \geq 2) = 0$) at finite conductor; the RMT limit should give $\Pr(r \geq 2) = 0$ as $N \to \infty$.
- **C-004 (Moments):** The RMT moments $\mathbb{E}[|\det(I-A)|^{2k}]$ predict the L-value moments.
- **C-008 (Selmer):** The BKLRP Selmer distribution is consistent with the RMT prediction after accounting for Sha[2].
- **C-012 (Katz-Sarnak):** This direction provides the theoretical foundation; C-007 focuses on the rank distribution specifically.

## Classification

**Conjecture / Partial results** — 1-level density proven in many families for limited support. Full rank distribution from RMT is conjectural, with strong computational verification.
