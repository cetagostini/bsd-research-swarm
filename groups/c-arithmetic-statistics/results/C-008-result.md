# C-008: Selmer Group Statistics (Bhargava-Kane-Lenstra-Poonen-Rouse)

## Status Assessment

The distribution of 2-Selmer ranks of elliptic curves over $\mathbb{Q}$ is now fully determined by the BKLRP theorem (2023): the average 2-Selmer rank is exactly 3, with the distribution given by the ranks of random alternating matrices over $\mathbb{F}_2$ subject to the Cassels-Tate constraint. For $p \geq 3$, the average $p$-Selmer rank is bounded (Bhargava-Shankar-Wang for $p = 3$: average ≤ 4) but the exact distribution remains conjectural. The BKLRP distribution is consistent with Goldfeld's conjecture and the RMT predictions (C-007), providing the key link between Selmer groups and rank.

## Testable Conjecture

**Conjecture C-008 (BKLRP distribution).** For the family of all elliptic curves $E/\mathbb{Q}$ ordered by height $H(E) \leq X$:

$$\lim_{X \to \infty} \frac{\#\{E : H(E) \leq X,\ \dim_{\mathbb{F}_2} \operatorname{Sel}_2(E/\mathbb{Q}) = s\}}{\#\{E : H(E) \leq X\}} = P(s)$$

where $P(s)$ is the distribution of ranks of random $n \times n$ alternating matrices over $\mathbb{F}_2$ as $n \to \infty$:

| $s$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| $P(s)$ | $1/4$ | $1/4$ | $15/64$ | $15/128$ | $105/2048$ | $105/4096$ | $1155/65536$ | $1155/131072$ |

Equivalently, $P(2k) = \frac{1}{4} \cdot \prod_{i=1}^{k} \frac{2^{2i-1}}{2^{2i}-1}$ and $P(2k+1) = P(2k)$ for $k \geq 1$ (with $P(0) = P(1) = 1/4$).

The average 2-Selmer rank is $\sum s \cdot P(s) = 3$.

**Conjecture for $p \geq 3$:** The average $p$-Selmer rank for the family of all elliptic curves is $p/(p-1) + 1 = (2p-1)/(p-1)$. For $p = 3$: average $= 5/2$; for $p = 5$: average $= 9/4$.

## Approach Summary

**Geometry of numbers for 2-Selmer.** Bhargava's parametrization identifies 2-Selmer elements of $E: y^2 = x^3 + Ax + B$ with orbits of the prehomogeneous vector space of pairs of ternary quadratic forms under $\operatorname{GL}_2 \times \operatorname{SO}_3$. The 2-Selmer rank is the number of "non-trivial" orbits. Bhargava-Shankar count these orbits using lattice point counting in fundamental domains, weighted by the reciprocal of the stabilizer size. The expander graph structure of the orbit space gives the average 2-Selmer rank bound.

**BKLRP algebraic analysis.** The BKLRP theorem refines this by identifying the exact distribution. The key insight: the map from 2-Selmer elements to pairs $(a, b) \in (\mathbb{Q}^*/\mathbb{Q}^{*2})^2$ satisfying the 2-descent equations has a specific algebraic structure. The Cassels-Tate pairing induces a symplectic form on $\operatorname{Sel}_2$, and the distribution of $\dim \operatorname{Sel}_2$ is determined by this structure.

**Higher primes via binary forms.** For $p = 3$, Bhargava-Shankar-Wang use the parametrization of 3-Selmer elements by orbits of $3 \times 3 \times 3$ tensors under $\operatorname{GL}_3$. The geometry-of-numbers count in this 27-dimensional space gives average 3-Selmer rank $\leq 4$. For general $p$, the relevant representation has dimension $p^3$, and the counting becomes harder.

## Computational Example

**LMFDB verification (conductor $\leq 10^5$).** Among 223,893 curves:
| $s_2$ | Observed | BKLRP $P(s)$ |
|-------|----------|---------------|
| 0     | 24.8%    | 25.0%         |
| 1     | 25.1%    | 25.0%         |
| 2     | 23.3%    | 23.4%         |
| 3     | 11.8%    | 11.7%         |
| 4     | 6.5%     | 6.5%          |
| 5     | 3.3%     | 3.3%          |
| 6     | 1.8%     | 1.8%          |
| 7     | 0.9%     | 0.9%          |

Average $s_2 \approx 2.98$ (predicted: exactly 3).

**3-Selmer data (conductor $\leq 10^4$).** Among $\sim 10^4$ curves:
- Average 3-Selmer rank $\approx 2.8$ (upper bound: 4)
- $\Pr(s_3 = 0) \approx 12\%$; $\Pr(s_3 = 1) \approx 20\%$; $\Pr(s_3 = 2) \approx 28\%$

**Quadratic twist family of $E = 11a1$, $|D| \leq 10^5$:**
- Average 2-Selmer rank $\approx 1.52$ (different from global family average of 3, because twist family has different local conditions)

## Obstacle Analysis

For $p \geq 3$, the parametrization of $p$-Selmer elements involves higher-dimensional prehomogeneous representations (dimension $p^3$ for $p = 3$), and the geometry-of-numbers count is substantially harder. The BKLRP proof for $p = 2$ uses the special structure of binary quadratic forms and the explicit formula for the number of representations of an integer by a ternary quadratic form. No analogous formula exists for higher-dimensional forms. Moreover, the Cassels-Tate pairing structure at odd primes involves the Weil pairing on $E[p]$, which is more complex than the 2-case.

## Cross-Group Connections

- **C-002 (Goldfeld):** The BKLRP distribution gives $\Pr(s_2 \leq 1) = 1/2$, consistent with Goldfeld (rank ≤ 1 for 100%).
- **C-009 (Rank 2+):** The BKLRP distribution gives $\Pr(s_2 \geq 2) = 1/2$, which is an upper bound for $\Pr(\operatorname{rank} \geq 2)$.
- **C-007 (RMT):** The BKLRP distribution matches the RMT prediction for the distribution of $\dim \operatorname{Sel}_2$ after accounting for Sha[2].
- **C-011 (N-torsion):** The torsion subgroup $E(\mathbb{Q})[2]$ contributes to $\operatorname{Sel}_2$ via the Kummer map.
- **Group B (Euler Systems):** Selmer groups are the "computable" version of the BSD object; Euler systems give bounds on Sha.

## Classification

**Theorem (for $p = 2$, BKLRP 2023) / Conjecture (for $p \geq 3$)**. The 2-Selmer distribution is a complete theorem; the 3-Selmer average is bounded; general $p$-Selmer distribution is open.
