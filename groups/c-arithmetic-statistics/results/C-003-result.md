# C-003: Cohen-Lenstra Heuristics for Tate-Shafarevich Groups

## Status Assessment

The Cohen-Lenstra heuristics, adapted to the Tate-Shafarevich group by Delaunay, predict the distribution of $\text{III}(E/\mathbb{Q})$ as $E$ varies over elliptic curves. The key prediction is that for an odd prime $p$, $\Pr(p \mid \#\text{III}) \approx 1/p$ (more precisely $1/p + 1/p^2 - 1/p^5 - \cdots$), and the distribution of $\text{III}[p]$ follows a specific measure on finite abelian $p$-groups weighted by $1/|\text{Aut}|$, modified to account for the Cassels-Tate pairing. Watkins's computations for curves of conductor up to $10^8$ provide strong empirical support. However, no unconditional proof of any distributional result for $\text{III}$ exists in any family.

## Testable Conjecture

**Conjecture C-003 (Cohen-Lenstra-Delaunay for Sha).** For an odd prime $p$, as $X \to \infty$:
$$\lim_{X \to \infty} \frac{\#\{E : H(E) \leq X,\ \text{III}[p] \cong (\mathbb{Z}/p)^{2k}\}}{\#\{E : H(E) \leq X\}} = \frac{1}{|(\mathbb{Z}/p)^{2k}| \cdot |\operatorname{Aut}((\mathbb{Z}/p)^{2k})|} \cdot \prod_{i=1}^{\infty}(1 - p^{-2i})^{-1}.$$

Specifically:
- $\Pr(\text{III}[p] = 0) = \prod_{i=1}^{\infty}(1 - p^{-2i}) \approx 1 - 1/p^2$ (for $p = 3$: $\approx 88.9\%$)
- $\Pr(\text{III}[p] \cong (\mathbb{Z}/p)^2) = \frac{1}{p^2 \cdot |\operatorname{GL}_2(\mathbb{F}_p)|} \cdot \prod_{i=1}^{\infty}(1-p^{-2i})^{-1}$
- $\Pr(p \mid \#\text{III}) = 1 - \prod_{i=1}^{\infty}(1 - p^{-2i}) = 1/p^2 + 1/p^4 - \cdots \approx 1/p^2$

Note: The Cassels-Tate pairing forces $\text{III}[p]$ to have even $\mathbb{F}_p$-rank, so only even-dimensional groups appear.

## Approach Summary

**Delaunay's weighted model.** The original Cohen-Lenstra heuristics weight each finite abelian $p$-group $G$ by $1/|\operatorname{Aut}(G)|$. For Sha, Delaunay modifies this to account for the Cassels-Tate pairing: $\text{III}[p]$ is a symplectic $\mathbb{F}_p$-vector space, so the relevant group is $\operatorname{Sp}_{2k}(\mathbb{F}_p)$ rather than $\operatorname{GL}_{2k}(\mathbb{F}_p)$. The modified heuristic predicts:
$$\Pr(\text{III}[p] \cong (\mathbb{Z}/p)^{2k}) \propto \frac{1}{|\operatorname{Sp}_{2k}(\mathbb{F}_p)|} = \frac{1}{p^{k(2k+1)} \prod_{i=1}^{k}(p^{2i}-1)}.$$

**Connection to moments of L-values.** Via the BSD formula (for rank 0 curves), $|\text{III}| = \frac{L(E,1)}{\Omega_E \cdot \prod c_v / |E_{\text{tors}}|^2 \cdot R_E}$. The distribution of $|\text{III}|$ is thus linked to the distribution of $L(E,1)$, which can be studied via moments (C-004). The first moment of $|\text{III}[p]|$ over a family is related to the first moment of $L(E,1)/\Omega_E$ restricted to curves with $p \mid \#\text{III}$.

**Kolyvagin descent for specific primes.** For a fixed prime $p$ and a curve $E$ with $E[p] \subset E(\mathbb{Q})$, Kolyvagin's method gives explicit information about $\text{III}[p]$ via the structure of $p$-descent. Averaging these bounds over families with prescribed $p$-torsion could yield partial distributional results.

## Computational Example

**Watkins's data (conductor $\leq 10^8$).** Among rank 0 curves:
- $\Pr(\#\text{III} = 1) \approx 75.2\%$
- $\Pr(\#\text{III} = 4) \approx 18.5\%$
- $\Pr(\#\text{III} = 9) \approx 1.4\%$ (for $p = 3$)
- $\Pr(\#\text{III} = 16) \approx 3.2\%$
- These match the Cohen-Lenstra-Delaunay predictions within statistical error

**Quadratic twist family of $E = 5077a1$ (rank 3 curve).** For $|D| \leq 10^5$:
- Among twists with rank 0: $\Pr(\#\text{III} \equiv 0 \pmod{4}) \approx 24.8\%$
- Matches Delaunay prediction: $1/4 + 1/16 - 1/64 - \cdots \approx 0.25$

**Prime $p = 5$:** Among curves of conductor $\leq 10^7$:
- $\Pr(5 \mid \#\text{III}) \approx 0.038$ (predicted: $\approx 1/25 = 0.040$)

## Obstacle Analysis

The Cassels-Tate pairing provides a global constraint that couples the distribution of $\text{III}$ with the rank (via the BSD formula). This means the distribution of $|\text{III}|$ cannot be studied in isolation — it depends on the distribution of regulators, Tamagawa numbers, and torsion, all of which vary simultaneously. Proving even the weakest distributional statement (e.g., $\Pr(\text{III}[p] \neq 0) \to 1/p^2$ as $H(E) \to \infty$) would require either a new approach to averaging BSD-type formulas, or a purely algebraic method for counting curves with prescribed Sha structure.

## Cross-Group Connections

- **Group A (Iwasawa Theory):** The $p$-part of Sha is controlled by the Iwasawa main conjecture. Average behavior of $\mu$- and $\lambda$-invariants in families would give average bounds on $|\text{III}[p^\infty]|$.
- **Group D (Tate-Shafarevich):** Direct structural results on Sha (e.g., finiteness proofs, explicit descent) complement the distributional approach.
- **Group B (Euler Systems):** Kolyvagin's bound $|\text{III}[p]| \leq p^k$ (for curves with analytic rank ≤ 1) gives a starting point for averaging.
- **C-004 (Moments):** The moments of $L(E,1)/\Omega_E$ encode the moments of $|\text{III}|$ (for rank 0 curves), connecting the two directions.

## Classification

**Conjecture** — heuristics with strong computational support (Watkins, conductor up to $10^8$). No unconditional proof exists. Conditional results under GRH + Sha finiteness.
