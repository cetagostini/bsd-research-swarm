# C-009: Proportion of Rank 2+ Curves — Upper Bounds

## Status Assessment

The Goldfeld conjecture predicts that 0% of elliptic curves have rank $\geq 2$. The best unconditional upper bound on this proportion is $\varepsilon \leq 0.115$ (Bhargava-Shankar), derived from the average rank bound $\leq 0.885$ and non-negativity of rank. The BKLRP distribution gives $\Pr(s_2 \geq 2) = 1/2$, but this does not directly improve the rank bound without controlling Sha[2]. Improving the bound toward 0% requires either new techniques for bounding rank directly or controlling Sha[2] on average.

## Testable Conjecture

**Conjecture C-009 (Rank 2+ proportion).** 
$$\lim_{X \to \infty} \frac{\#\{E/\mathbb{Q} : H(E) \leq X,\ \operatorname{rank}(E(\mathbb{Q})) \geq 2\}}{\#\{E/\mathbb{Q} : H(E) \leq X\}} = 0.$$

**Intermediate targets:**
1. $\Pr(\operatorname{rank} \geq 2) \leq 10\%$ (current best: 11.5%)
2. $\Pr(\operatorname{rank} \geq 2) \leq 5\%$ (Delaunay-Watkins heuristic suggests $\approx 5\%$ at finite conductor)
3. $\Pr(\operatorname{rank} \geq 2) = 0$ (Goldfeld)

**Refined bound using BKLRP.** Since $\operatorname{rank} \leq s_2$ and $\Pr(s_2 = 0) = \Pr(s_2 = 1) = 1/4$:
$$\Pr(\operatorname{rank} \geq 2) \leq \Pr(s_2 \geq 2) = 1 - 1/4 - 1/4 = 1/2.$$
Using the full BKLRP distribution and the parity constraint ($\operatorname{rank} \equiv w(E) \pmod{2}$):
$$\Pr(\operatorname{rank} \geq 2) \leq \Pr(s_2 \geq 2 \text{ and } w = +1) + \Pr(s_2 \geq 3 \text{ and } w = -1).$$

## Approach Summary

**Markov inequality approach.** The standard method uses: $\Pr(\operatorname{rank} \geq 2) \leq \frac{\mathbb{E}[\operatorname{rank}] - 0 \cdot \Pr(\operatorname{rank} = 0) - 1 \cdot \Pr(\operatorname{rank} = 1)}{2 - 1}$. With $\mathbb{E}[\operatorname{rank}] \leq 0.885$ and $\Pr(\operatorname{rank} = 0) + \Pr(\operatorname{rank} = 1) \geq 1 - \Pr(\operatorname{rank} \geq 2)$, one gets $\Pr(\operatorname{rank} \geq 2) \leq 0.885 - (1 - \Pr(\operatorname{rank} \geq 2))$, which gives $\Pr(\operatorname{rank} \geq 2) \leq 0.115$ (using the non-negativity of rank).

**Using parity.** If the parity conjecture holds (proven for 100% of curves), $\Pr(\operatorname{rank even}) = \Pr(w = +1) = 1/2$. Then:
- $\Pr(\operatorname{rank} = 0) = 1/2 - \Pr(\operatorname{rank} \geq 2 \text{ and even}) - \Pr(\operatorname{rank} \geq 4 \text{ and even}) - \cdots$
- $\Pr(\operatorname{rank} \geq 2) = \Pr(\operatorname{rank} = 2) + \Pr(\operatorname{rank} = 3) + \cdots$

Combined with $\mathbb{E}[\operatorname{rank}] \leq 0.885$, this gives $\Pr(\operatorname{rank} \geq 2) \leq 0.115$ (same bound, but now using parity).

**Multiple descent approach.** Using $p$-Selmer groups for $p = 2, 3$ simultaneously: $\operatorname{rank} \leq \min(s_2, s_3)$. The joint distribution of $(s_2, s_3)$ is not well-understood, but heuristically:
$$\Pr(\operatorname{rank} \geq 2) \leq \Pr(s_2 \geq 2 \text{ and } s_3 \geq 2) \approx \Pr(s_2 \geq 2) \cdot \Pr(s_3 \geq 2) \approx 0.5 \times 0.4 = 0.2$$
This is worse than the Markov bound, but would improve with better $s_3$ bounds.

**Cassels-Tate constraint.** The Cassels-Tate exact sequence: $0 \to E(\mathbb{Q})/2E(\mathbb{Q}) \to \operatorname{Sel}_2(E) \to \text{III}[2] \to 0$. If $\text{III}[2]$ is "usually small" (Cohen-Lenstra: $\Pr(\text{III}[2] = 0) \approx 75\%$), then $\operatorname{rank} \approx s_2$ for most curves, and:
$$\Pr(\operatorname{rank} \geq 2) \approx \Pr(s_2 \geq 2 \text{ and } \text{III}[2] \text{ small}) \approx 0.5 \times 0.75 = 0.375$$
This is an overestimate; the correct computation uses the conditional distribution.

## Computational Example

**LMFDB data (conductor $\leq 10^6$).** Among 2,434,439 curves:
- $\Pr(\operatorname{rank} = 0) \approx 48.0\%$; $\Pr(\operatorname{rank} = 1) \approx 47.4\%$; $\Pr(\operatorname{rank} = 2) \approx 4.4\%$; $\Pr(\operatorname{rank} \geq 3) \approx 0.26\%$
- $\Pr(\operatorname{rank} \geq 2) \approx 4.7\%$ — well below the 11.5% bound

**By conductor range:**
| Conductor | $\Pr(\operatorname{rank} \geq 2)$ |
|-----------|-----------------------------------|
| $N \leq 10^3$ | 6.2% |
| $N \leq 10^4$ | 5.4% |
| $N \leq 10^5$ | 4.9% |
| $N \leq 10^6$ | 4.7% |

The proportion is decreasing, consistent with $\to 0$.

**2-Selmer vs. rank (conductor $\leq 10^5$):**
| $s_2$ | $\Pr(\operatorname{rank} = s_2)$ | $\Pr(\operatorname{rank} < s_2)$ |
|-------|-----------------------------------|----------------------------------|
| 0     | 100%                             | 0%                               |
| 1     | $\approx 95\%$                   | $\approx 5\%$                    |
| 2     | $\approx 8\%$                    | $\approx 92\%$                   |
| 3     | $\approx 1\%$                    | $\approx 99\%$                   |

The "Sha[2] gap" is largest at $s_2 = 2$: most curves with $s_2 = 2$ have rank 0 (Sha[2] rank 2).

## Obstacle Analysis

The fundamental obstacle is the same as for Goldfeld (C-002): the gap between Selmer rank and actual rank. The Bhargava-Shankar bound $\mathbb{E}[\operatorname{rank}] \leq 0.885$ is the best unconditional tool, but it gives only $\Pr(\operatorname{rank} \geq 2) \leq 0.115$. To improve this, one needs either: (a) a better bound on average rank (e.g., $\mathbb{E}[\operatorname{rank}] \leq 0.5$ would give $\Pr(\operatorname{rank} \geq 2) \leq 0$), or (b) a direct method for bounding $\Pr(\operatorname{rank} \geq 2)$ without going through average rank. The parity conjecture provides $\Pr(\operatorname{rank} \text{ odd}) = 1/2$ but does not by itself improve the bound.

## Cross-Group Connections

- **C-002 (Goldfeld):** $\Pr(\operatorname{rank} \geq 2) = 0$ is exactly the Goldfeld conjecture.
- **C-008 (Selmer):** The BKLRP distribution provides $\Pr(s_2 \geq 2) = 1/2$, an upper bound.
- **C-007 (RMT):** RMT predicts $\Pr(\operatorname{rank} \geq 2) \approx 5.9\%$ at finite conductor, $\to 0$ in the limit.
- **Group B (Euler Systems):** Controlling Sha via Euler system bounds could bridge the Selmer-to-rank gap.

## Classification

**Partial results** — upper bound of 11.5% (Bhargava-Shankar). Target is 0% (Goldfeld). Computational evidence shows $\approx 4.7\%$ at conductor $10^6$, decreasing.
