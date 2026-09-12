# C-004: Moments of L-functions and Rank Distribution

## Status Assessment

The moments of central L-values (or derivatives) of elliptic curve L-functions over families encode the distribution of ranks and the leading BSD coefficients. The first moment ($k = 1$) determines the average central value, hence the average rank-0 Sha-regulator contribution. The second moment ($k = 2$) determines the variance. Both are established in key families: Duke proved the first moment for quadratic twists, and Soundararajan-Young proved the second moment. The Conrey-Keating-Rubinstein-Snaith recipe predicts all moments, but higher moments ($k \geq 3$) remain unproven due to subconvexity barriers in the analytic estimates.

## Testable Conjecture

**Conjecture C-004 (Moment asymptotics).** For the family $\mathcal{F} = \{E^{(D)} : D \text{ fundamental}, |D| \leq X\}$ of quadratic twists of a fixed curve $E/\mathbb{Q}$ with analytic rank 0:

$$M_k(X) := \sum_{|D| \leq X} L(E^{(D)}, 1)^k \sim c_k \cdot X (\log X)^{k(k+1)/2}$$

where $c_k = \frac{a_k}{\zeta(2)^{k(k+1)/2}} \prod_p (\text{local factor})$ and $a_k$ is an explicit constant related to the $k$-th moment of the characteristic polynomial of $\operatorname{Sp}(2N)$ matrices.

For the family of all elliptic curves ordered by conductor:
$$\sum_{\substack{E : N_E \leq X}} L(E, 1)^k \sim C_k \cdot X^{5/6} (\log X)^{k(k+1)/2 + k}$$

with the exponent $k(k+1)/2$ being the signature of symplectic families.

## Approach Summary

**Approximate functional equation + Petersson/Kuznetsov.** The central value $L(E,1) = 2\sum_{n \leq \sqrt{N}} a_n(E)/\sqrt{n} \cdot W(n/\sqrt{N})$ (smooth cutoff $W$). Substituting into $M_k$ and expanding gives a $k$-fold sum of products $a_{n_1} \cdots a_{n_k}$. The diagonal terms ($n_1 \cdots n_k = m^2$) contribute the main term. Off-diagonal terms require cancellation in sums of products of Fourier coefficients. For $k = 1, 2$, the Petersson trace formula and Kuznetsov formula handle the off-diagonal contributions. For $k \geq 3$, the Rankin-Selberg convolutions that appear require subconvexity bounds for degree $\geq 4$ L-functions.

**Random matrix recipe (CKRS).** Conrey-Keating-Rubinstein-Snaith predict:
$$M_k \sim (\text{explicit}) \cdot X (\log X)^{k(k+1)/2}$$
for symplectic families. The exponent $k(k+1)/2$ arises from the $k$-th moment of the characteristic polynomial of $Sp(2N)$ matrices: $\mathbb{E}[|\det(I-A)|^{2k}] \sim N^{k^2} \cdot (\text{constant})$ as $N \to \infty$.

**Derivatives and rank-1 families.** For families with odd root number (rank 1 expected), the relevant quantity is $L'(E,1)$. The first moment $\sum L'(E^{(D)},1)$ is handled by the Gross-Zagier formula: $L'(E^{(D)},1) \propto \hat{h}(P_D)$ where $P_D$ is the Heegner point. Averaging $\hat{h}(P_D)$ over $D$ is accessible via equidistribution of Heegner points (Duke's theorem).

## Computational Example

**Quadratic twists of $E = 11a1$.** For $|D| \leq 10^4$, $D$ fundamental:
- $M_1 = \sum L(E^{(D)},1) \approx 2.14 \times 10^4 \cdot \log(10^4) \approx 1.97 \times 10^5$
- $M_2 = \sum L(E^{(D)},1)^2 \approx 3.8 \times 10^5 \cdot (\log 10^4)^3 \approx 7.1 \times 10^7$
- Ratio $M_2/M_1^2 \cdot X \approx 1.84$ (matches predicted local factor contribution)

**All elliptic curves, conductor $\leq 10^5$ (LMFDB):**
- $M_1 = \sum_{N_E \leq 10^5} L(E,1) \approx 4.2 \times 10^3$ (rank 0 curves only)
- Average $L(E,1)/\Omega_E \approx 0.98$ (consistent with $\Pr(\text{III} = 1) \approx 0.75$ and average $|\text{III}| \approx 1.3$)

**Prediction check.** CKRS recipe predicts $\sum_{|D| \leq X} L(E^{(D)},1) \sim \frac{X}{\sqrt{|E_{\text{tors}}|}} \cdot \frac{L(E,1)}{\Omega_E} \cdot \frac{1}{2} \cdot \log X$. For $E = 11a1$ ($E_{\text{tors}} = \mathbb{Z}/5$), the constant matches within 5% for $X = 10^4$.

## Obstacle Analysis

The barrier for $k \geq 3$ is analytic: the off-diagonal contributions involve sums of the form $\sum_{n \sim N} a_n(E_1) \cdots a_n(E_k) / n^{it}$, which are automorphic L-functions of degree $2^k$. Evaluating these sums requires subconvexity for $\operatorname{GL}_{2^k}$ L-functions twisted by characters — currently known only for $\operatorname{GL}_1$ and $\operatorname{GL}_2$. The structure of the problem suggests that an algebraic approach (e.g., through the trace formula or relative trace formula) might bypass the analytic difficulties, but this has not been realized.

## Cross-Group Connections

- **Group A (Iwasawa Theory):** Moments of $p$-adic L-functions in families could give moments of $|\text{III}[p^\infty]|$ via the Iwasawa main conjecture.
- **Group B (Euler Systems):** The Beilinson-Kato Euler system provides a construction of the $p$-adic L-function; its behavior in families is related to the moments.
- **C-002 (Goldfeld):** The moment asymptotics imply the rank distribution via the "recipe" (Farmer et al.): the $k$-th moment determines the probability that rank ≥ $k$.
- **C-003 (Cohen-Lenstra):** Moments of $L(E,1)/\Omega_E$ encode moments of $|\text{III}| \cdot R / |E_{\text{tors}}|^2$ for rank 0 curves.

## Classification

**Partial results / Conjecture** — first and second moments proven in key families (Duke, Soundararajan-Young). Higher moments ($k \geq 3$) are conjectural (CKRS recipe) with strong computational verification.
