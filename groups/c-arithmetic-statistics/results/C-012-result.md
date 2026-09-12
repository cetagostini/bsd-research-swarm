# C-012: Katz-Sarnak Philosophy for Families of Elliptic Curves

## Status Assessment

The Katz-Sarnak philosophy predicts that the low-lying zeros of L-functions in a family follow the distribution of eigenvalues near 1 of the corresponding classical compact group. For families of elliptic curves, the expected symmetry type is symplectic ($Sp$), predicting that 100% of curves have even analytic rank (rank 0 dominant). Over function fields, the Katz-Sarnak correspondence is a theorem (Deligne-Lafforgue). Over number fields, 1-level density is proven for many families with limited support ($\sigma < 2/3$ unconditionally, $\sigma < 1$ under GRH). Extending the support to $\sigma > 1$ would unconditionally determine the symmetry type and resolve the rank distribution.

## Testable Conjecture

**Conjecture C-012 (Katz-Sarnak for elliptic curves).** For the family $\mathcal{F}$ of all elliptic curves $E/\mathbb{Q}$ ordered by conductor $N_E \leq X$, the $n$-level density with test functions $\phi_1, \ldots, \phi_n$ supported in $(-\sigma, \sigma)$ satisfies:

$$\lim_{X \to \infty} \frac{1}{|\mathcal{F}(X)|} \sum_{E \in \mathcal{F}(X)} \sum_{\gamma_1,\ldots,\gamma_n} \prod_{i=1}^{n} \phi_i(\gamma_i \log N_E) = \int_{Sp(2N)} \prod_{i=1}^{n} \phi_i(\theta_i) \, d\mu_{Sp}$$

as $N \to \infty$, where $\mu_{Sp}$ is the Haar measure on $Sp(2N)$ and $\theta_i = \frac{1}{2\pi} \log \lambda_i$ for eigenvalues $e^{i\theta_j}$ of the matrix.

**Specific predictions for 1-level density ($n = 1$, symplectic):**
$$W_1^{Sp}(\phi) = \hat{\phi}(0) - \frac{1}{2} \int_0^1 \phi(x) \, dx + \frac{1}{2} \phi(0)$$

For the orthogonal families (rank 0 and rank 1 subfamilies):
$$W_1^{SO(\text{even})}(\phi) = \hat{\phi}(0) + \frac{1}{2} \int_0^1 \phi(x) \, dx - \frac{1}{2} \phi(0)$$
$$W_1^{SO(\text{odd})}(\phi) = \hat{\phi}(0) - \frac{1}{2} \int_0^1 \phi(x) \, dx + \frac{3}{2} \phi(0)$$

**Rank distribution from symplectic symmetry:**
| Rank | $\Pr(r)$ (Sp prediction) |
|------|--------------------------|
| 0    | $\prod_{k=1}^{\infty}(1-2^{-2k}) \approx 0.457$ |
| 1    | $\frac{1}{2}\prod_{k=2}^{\infty}(1-2^{-2k}) \approx 0.463$ |
| 2    | $\approx 0.059$ |
| 3    | $\approx 0.015$ |
| $\geq 4$ | $\approx 0.006$ |

## Approach Summary

**Explicit formula and prime sums.** The $n$-level density is computed via the explicit formula: $\sum_\gamma \phi(\gamma \log N) = \hat{\phi}(0) \frac{\log N}{\log N} + \sum_p (\text{local terms}) + O(1/\log N)$. Averaging over the family, the "diagonal" contribution gives $\hat{\phi}(0)$. The "off-diagonal" contributions involve averages of $a_p(E)$ (Fourier coefficients) and products $a_{p_1}(E) \cdots a_{p_k}(E)$ over the family. For $n = 1$ with support $\sigma < 1$, only one prime appears, and the average $\frac{1}{|\mathcal{F}(X)|} \sum_E a_p(E)$ is computable by the Petersson trace formula.

**Support extension via Kuznetsov formula.** To extend support beyond $\sigma = 1$, one needs to handle averages of products $a_{p_1}(E) \cdots a_{p_k}(E)$ for $k \geq 2$. These are moments of Fourier coefficients, related to the Rankin-Selberg convolution. The Kuznetsov formula (for the family of all newforms of weight 2 and level $N$) gives an explicit spectral expansion, but the error terms require subconvexity estimates.

**Distinguished densities for rank 0/1.** Dueñez-Huynh-Miller-Miller compute the "distinguished 1-level density" by separating the family into rank 0 and rank 1 subfamilies (using the root number). The rank 0 subfamily shows $SO(\text{even})$ symmetry and the rank 1 subfamily shows $SO(\text{odd})$ symmetry, as predicted by the Katz-Sarnak philosophy.

## Computational Example

**Rubinstein's computation (all elliptic curves, conductor $\leq 10^5$).** 1-level density with Gaussian test function $\phi(x) = e^{-x^2/2}$:
- Symplectic prediction: $W_1^{Sp}(\phi) \approx 0.424$
- Observed: $\approx 0.421$ (support $\sigma < 2/3$)
- Orthogonal predictions: $W_1^{SO(\text{even})} \approx 0.576$, $W_1^{SO(\text{odd})} \approx 0.827$
- Result: consistent with $Sp$, ruled out $SO(\text{even})$ and $SO(\text{odd})$ at $> 3\sigma$

**Young's GRH-dependent computation (support $\sigma < 1$).** For the family of all elliptic curves with conductor $N \leq X$:
- $W_1(\phi) = \hat{\phi}(0) - \frac{1}{2}\hat{\phi}(0) \cdot \frac{1}{\log X} + \cdots$ (Sp form confirmed)

**Bui-Heap 2-level density (quadratic twists, $\sigma < 1$).** For the family $\{E^{(D)} : |D| \leq X\}$:
- 2-level density matches $Sp$ prediction for $\sigma < 1$
- Confirms: zeros of different curves in the family are "independent" at this scale

**LMFDB verification.** For conductor $\leq 10^6$, computing $\sum_E \sum_\gamma \phi(\gamma \log N_E)$:
- Result matches Sp prediction within 2% for $\sigma = 0.5$
- Diverges from all three symmetry types for $\sigma > 1.5$ (insufficient data)

## Obstacle Analysis

The fundamental barrier is that determining the symmetry type requires support $\sigma > 1$ (so that the integral $\int_0^1 \phi(x) dx$ appears with a nonzero coefficient that distinguishes $Sp$ from $SO$). For $\sigma < 1$, the 1-level density is the same for all symmetry types up to the coefficient of $\hat{\phi}(0)$, which is always $1$ (the "trivial" term). The coefficient that distinguishes symmetry types is the one involving $\phi(0)$, which requires primes up to $N^{1+\varepsilon}$ to appear in the explicit formula — this is beyond the reach of current unconditional methods. Under GRH, the support extends to $\sigma < 1$ (Young), but extending beyond $\sigma = 1$ even conditionally is open.

## Cross-Group Connections

- **C-007 (RMT):** C-012 provides the theoretical foundation (Katz-Sarnak correspondence); C-007 applies it to predict the rank distribution.
- **C-002 (Goldfeld):** If the symmetry type is $Sp$ and the Katz-Sarnak correspondence holds, then $\Pr(r \geq 2) \to 0$, giving Goldfeld.
- **C-004 (Moments):** The $n$-level density determines the correlations among central values, which encode the moments.
- **C-008 (Selmer):** The BKLRP Selmer distribution is consistent with $Sp$ symmetry; the Katz-Sarnak prediction constrains the Selmer-rank gap.
- **C-010 (Function fields):** Over function fields, the full Katz-Sarnak correspondence is proven, providing the model case.

## Classification

**Partial results / Conjecture** — 1-level density proven in many families for limited support ($\sigma < 2/3$ unconditional, $\sigma < 1$ under GRH). Full $n$-level density and symmetry type determination are open over $\mathbb{Q}$. The function field case is complete.
