# C-006: Average Tamagawa Numbers in Families

## Status Assessment

The Tamagawa product $\prod_{p \mid N_E} c_p(E)$ appears in the BSD formula as a multiplicative factor linking the central L-value to the arithmetic invariants. Computing its average over families of elliptic curves is essential for converting average L-value results (C-004) into average information about $|\text{III}| \cdot R$. While specific families (e.g., quadratic twists) have been partially analyzed, a systematic computation of the average Tamagawa product for the family of all elliptic curves ordered by conductor is not yet available.

## Testable Conjecture

**Conjecture C-006 (Average Tamagawa product).** For the family of all elliptic curves $E/\mathbb{Q}$ ordered by conductor $N_E \leq X$:
$$\lim_{X \to \infty} \frac{1}{|\mathcal{F}(X)|} \sum_{E \in \mathcal{F}(X)} \prod_{p \mid N_E} c_p(E) = C_{\text{Tam}}$$
where $C_{\text{Tam}} = \prod_p \left(1 + \frac{\mathbb{E}[c_p \cdot \mathbf{1}_{p \mid N_E}] - \Pr(p \mid N_E)}{\Pr(p \mid N_E)}\right)$ is an explicit Euler product.

More precisely, for each prime $p$:
- $\Pr(p \mid N_E,\ c_p = 1) = \frac{1}{p} + O(p^{-2})$ (multiplicative, non-split)
- $\Pr(p \mid N_E,\ c_p = 2) = \frac{1}{p} + O(p^{-2})$ (multiplicative, split)  
- $\Pr(p \mid N_E,\ c_p \geq 3) = O(p^{-2})$ (additive reduction)
- $\mathbb{E}[c_p \mid p \mid N_E] = 2 + O(1/p)$

The expected Euler product converges: $C_{\text{Tam}} \approx 2.15$.

## Approach Summary

**Local sieve at each prime.** The Tamagawa number $c_p$ depends on the Kodaira-Néron reduction type at $p$. For each prime $p$, one can enumerate the possible reduction types and compute $c_p$ for each:
- Split multiplicative: $c_p = |v_p(j)|$
- Non-split multiplicative: $c_p = 1$ or $2$ depending on $v_p(j)$ parity
- Additive: $c_p \in \{1, 2, 3, 4\}$ (Kodaira types $II, III, IV, I_0^*, \ldots$)

The density of each reduction type among curves of conductor $N_E \leq X$ with $p \mid N_E$ can be computed by counting points on the moduli stack of Weierstrass models with prescribed local data. This is a multi-parameter sieve problem.

**Average over quadratic twists.** For the family of quadratic twists $E^{(D)}$ of a fixed curve $E$, the Tamagawa numbers change at primes $p \mid D$ depending on the Legendre symbol $(D/p)$. The average $\sum_{|D| \leq X} \prod_{p \mid N_{E^{(D)}}} c_p(E^{(D)})$ can be computed using multiplicative function theory: $c_p(E^{(D)})$ depends on $D \pmod{p^2}$ (for bad primes of $E$) and on $D \pmod{p}$ (for primes of additive reduction becoming good).

**Connection to moments via BSD.** From the BSD formula for rank 0 curves:
$$\frac{L(E,1)}{\Omega_E} = \frac{|\text{III}| \cdot \prod c_p}{|E_{\text{tors}}|^2}$$
The average of $L(E,1)/\Omega_E$ (first moment, C-004) divided by the average of $|\text{III}|/|E_{\text{tors}}|^2$ (Cohen-Lenstra prediction, C-003) gives the average Tamagawa product.

## Computational Example

**LMFDB data (conductor $\leq 10^5$).** Among 223,893 curves:
- Average $\prod c_p \approx 2.18$ (close to predicted $C_{\text{Tam}} \approx 2.15$)
- $\Pr(\prod c_p = 1) \approx 0.42$
- $\Pr(\prod c_p = 2) \approx 0.24$
- $\Pr(\prod c_p = 4) \approx 0.12$
- $\Pr(\prod c_p \geq 6) \approx 0.22$

**By conductor.** For $N \leq 10^3$: avg $\prod c_p \approx 2.05$; for $N \leq 10^5$: $\approx 2.18$. The convergence to the limit is slow.

**Specific primes.** For $p = 2$:
- Among curves with $2 \mid N_E$: $\mathbb{E}[c_2] \approx 2.8$ (higher due to additive reduction types at 2)
- For $p = 3$: $\mathbb{E}[c_3 \mid 3 \mid N_E] \approx 2.1$

**Quadratic twist family of $E = 37a1$.** For $|D| \leq 10^5$:
- Average $\prod c_p(E^{(D)}) \approx 3.4$ (higher because twist introduces new bad primes)

## Obstacle Analysis

The main difficulty is that Tamagawa numbers at different primes are not independent: the conductor $N_E$ constrains which primes can have bad reduction, creating global dependencies. At each prime $p$, the distribution of $c_p$ depends on the Kodaira-Néron type, which involves solving a system of congruences on the coefficients $a_i$ of the Weierstrass model. For additive reduction, the Kodaira type is determined by the valuation of the discriminant $\Delta$ and the $c_4, c_6$ invariants, creating a complex local picture. A full Euler product computation requires handling all reduction types simultaneously.

## Cross-Group Connections

- **C-004 (Moments):** The average Tamagawa product converts average L-values into average $|\text{III}| \cdot R$ information.
- **C-003 (Cohen-Lenstra):** Combined with average $|\text{III}|$ predictions, gives average $R$ (regulator) information.
- **C-001 (Average rank):** For twist families, the average Tamagawa product constrains the average $|\text{III}| \cdot R$.
- **Group D (Tate-Shafarevich):** Local reduction data and Tamagawa numbers are the "local ingredients" of BSD.

## Classification

**Experiment / Partial results** — computational data available for specific families, theoretical framework (local sieve) partially developed. The Euler product prediction is conjectural.
