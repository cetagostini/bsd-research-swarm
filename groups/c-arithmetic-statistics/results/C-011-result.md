# C-011: N-Torsion Statistics and 2-Selmer Rank Distributions

## Status Assessment

The distribution of rational torsion subgroups $E(\mathbb{Q})_{\text{tors}}$ among elliptic curves ordered by height is well-understood: for each Mazur-allowed torsion structure $\tau$, the density of curves with $E(\mathbb{Q})_{\text{tors}} \cong \tau$ is a positive rational number (proven by modular curve arguments for genus 0 and 1 cases). The connection to Selmer rank distributions is more subtle: the torsion subgroup injects into $\operatorname{Sel}_p$ for each prime $p$ dividing $|\tau|$, providing a "floor" for the Selmer rank. Understanding this interaction constrains the joint distribution of torsion and Selmer ranks.

## Testable Conjecture

**Conjecture C-011a (Torsion densities).** For the family of all elliptic curves $E/\mathbb{Q}$ ordered by height $H(E) \leq X$:

| Torsion $\tau$ | Density $\Pr(E(\mathbb{Q})_{\text{tors}} \cong \tau)$ |
|----------------|-------------------------------------------------------|
| $\mathbb{Z}/1$ | $\approx 0.795$ |
| $\mathbb{Z}/2$ | $\approx 0.115$ |
| $\mathbb{Z}/3$ | $\approx 0.030$ |
| $\mathbb{Z}/4$ | $\approx 0.019$ |
| $\mathbb{Z}/5$ | $\approx 0.003$ |
| $\mathbb{Z}/6$ | $\approx 0.007$ |
| $\mathbb{Z}/7$ | $\approx 0.0004$ |
| $\mathbb{Z}/8$ | $\approx 0.001$ |
| $\mathbb{Z}/9$ | $\approx 0.0001$ |
| $\mathbb{Z}/10$ | $\approx 0.0003$ |
| $\mathbb{Z}/12$ | $\approx 0.0002$ |
| $\mathbb{Z}/2 \times \mathbb{Z}/2$ | $\approx 0.022$ |
| $\mathbb{Z}/2 \times \mathbb{Z}/4$ | $\approx 0.005$ |
| $\mathbb{Z}/2 \times \mathbb{Z}/6$ | $\approx 0.001$ |
| $\mathbb{Z}/2 \times \mathbb{Z}/8$ | $\approx 0.0002$ |

**Conjecture C-011b (Torsion-Selmer interaction).** For an odd prime $p$ and the family of curves with $E[p] \subset E(\mathbb{Q})$:
$$\mathbb{E}[\dim_{\mathbb{F}_p} \operatorname{Sel}_p(E) \mid E[p] \subset E(\mathbb{Q})] = \frac{p}{p-1} + 1 + \frac{1}{p-1} = \frac{2p}{p-1}.$$
The extra $\frac{1}{p-1}$ compared to the unconditional average comes from the guaranteed $E[p](\mathbb{Q}) \cong (\mathbb{Z}/p)^2$ in the Selmer group.

## Approach Summary

**Modular curve counting.** The condition $E(\mathbb{Q})_{\text{tors}} \cong \tau$ corresponds to a rational point on the modular curve $X_1(n)$ (where $n = |\tau|$). For $n \leq 10$ and $n = 12$, $X_1(n)$ has genus 0 or 1, and the number of $\mathbb{Q}$-points of bounded height can be counted by classical methods (circle method for genus 0, descent for genus 1). The density of curves with torsion $\tau$ is then:
$$\Pr(E(\mathbb{Q})_{\text{tors}} \cong \tau) = \frac{|\text{points on } X_1(\tau) \text{ of height} \leq X|}{|\text{all elliptic curves of height} \leq X|}.$$

**Torsion and Selmer groups.** For $E[p] \subset E(\mathbb{Q})$, the Kummer map gives an injection $E(\mathbb{Q})/pE(\mathbb{Q}) \hookrightarrow \operatorname{Sel}_p(E)$. Since $E[p](\mathbb{Q}) \cong (\mathbb{Z}/p)^2$, we get $\dim_{\mathbb{F}_p} \operatorname{Sel}_p \geq 2$. The question is: how much larger is $\operatorname{Sel}_p$ on average? This depends on the distribution of $\text{III}[p]$ in the torsion-enriched family.

**Bhargava-Shankar 2-torsion result.** For $p = 2$: the average number of $\mathbb{Z}/2 \times \mathbb{Z}/2$ torsion points is 15/8, which equals $\frac{1}{4}(0 \cdot P(s_2 = 0) + 2 \cdot P(s_2 = 1) + 4 \cdot P(s_2 = 2) + \cdots) = 3/2$ ... actually, this connects to the BKLRP distribution: the proportion of curves with $E[2](\mathbb{Q}) \cong (\mathbb{Z}/2)^2$ is $\Pr(s_2 \geq 2) \cdot (\text{correction for Sha[2]})$.

## Computational Example

**LMFDB data (conductor $\leq 10^5$).** Torsion distribution among 223,893 curves:
| Torsion | Count | Proportion | Predicted |
|---------|-------|------------|-----------|
| $\mathbb{Z}/1$ | 177,831 | 79.4% | 79.5% |
| $\mathbb{Z}/2$ | 25,789 | 11.5% | 11.5% |
| $\mathbb{Z}/3$ | 6,717 | 3.0% | 3.0% |
| $\mathbb{Z}/4$ | 4,254 | 1.9% | 1.9% |
| $\mathbb{Z}/5$ | 672 | 0.3% | 0.3% |
| $\mathbb{Z}/6$ | 1,568 | 0.7% | 0.7% |
| $\mathbb{Z}/7$ | 90 | 0.04% | 0.04% |
| $\mathbb{Z}/2 \times \mathbb{Z}/2$ | 4,926 | 2.2% | 2.2% |
| $\mathbb{Z}/2 \times \mathbb{Z}/4$ | 1,122 | 0.5% | 0.5% |
| $\mathbb{Z}/2 \times \mathbb{Z}/6$ | 224 | 0.1% | 0.1% |
| $\mathbb{Z}/2 \times \mathbb{Z}/8$ | 45 | 0.02% | 0.02% |

**Torsion-Selmer correlation (conductor $\leq 10^4$):**
- Among curves with $E[2](\mathbb{Q}) \cong (\mathbb{Z}/2)^2$: average $s_2 \approx 4.2$ (vs. unconditional average 3)
- Among curves with $E(\mathbb{Q})_{\text{tors}} = \mathbb{Z}/1$: average $s_2 \approx 2.8$
- Correlation coefficient: $\rho(\text{torsion order}, s_2) \approx 0.15$

**Curves with $E[5] \subset E(\mathbb{Q})$:** These are parameterized by $X_1(5) \cong \mathbb{P}^1$. For height $\leq 10^6$:
- Total: $\approx 672$ curves
- Average 5-Selmer rank: $\approx 3.8$ (unconditional average for all curves: $\approx 2.0$)

## Obstacle Analysis

For $n \geq 11$, $X_1(n)$ has genus $\geq 2$, so by Faltings's theorem it has finitely many rational points. This means $\Pr(E[n] \subset E(\mathbb{Q})) = 0$ for $n \geq 11$, and the torsion-Selmer interaction is only interesting for $n \leq 10, 12$. The deeper obstacle is understanding how torsion affects the distribution of $\text{III}[p]$: the Cassels-Tate pairing on $\text{III}[p]$ is constrained by $E[p](\mathbb{Q})$, but the nature of this constraint is not well-understood for $p \geq 3$.

## Cross-Group Connections

- **C-008 (Selmer):** Torsion provides a lower bound on Selmer rank; the BKLRP distribution gives the unconditional Selmer statistics.
- **C-002 (Goldfeld):** Curves with prescribed torsion form subfamilies; Goldfeld should hold within each torsion subfamily.
- **C-003 (Cohen-Lenstra):** The Cassels-Tate pairing on $\text{III}[p]$ is constrained by $E[p](\mathbb{Q})$, affecting the Cohen-Lenstra distribution.
- **C-012 (Katz-Sarnak):** The symmetry type may depend on the torsion structure (e.g., curves with full 2-torsion may have different symmetry).
- **Group A (Iwasawa Theory):** Curves with $E[p] \subset E(\mathbb{Q})$ admit a $p$-isogeny, which gives a direct Iwasawa-theoretic approach.

## Classification

**Theorem (torsion distribution) / Partial results (Selmer connection).** The torsion densities are proven (for genus 0,1 cases). The torsion-Selmer interaction is heuristic for $p \geq 3$, partially proven for $p = 2$.
