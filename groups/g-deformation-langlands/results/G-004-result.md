# G-004: Modularity Lifting for Higher-Dimensional Representations

## Status Assessment
Active research. The GL₂ case over totally real fields is well-established. The GLₙ case over CM fields is known under residual automorphy hypotheses (Allen et al. 2018). Removing residual automorphy is the main open problem.

## Testable Conjecture

**Conjecture (Higher-Dimensional Modularity).** Let $F$ be a CM field, $n \geq 3$, and $\rho: G_F \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ continuous. Suppose:
1. $\bar\rho|_{G_{F(\zeta_\ell)}}$ is automorphic of regular weight,
2. $\rho|_{G_{F_v}}$ is crystalline with regular HT weights for $v | \ell$,
3. $\rho$ satisfies the Taylor-Wiles condition at auxiliary primes.

Then $\rho$ is automorphic: there exists a regular algebraic conjugate-self-dual cuspidal automorphic representation $\pi$ of $\mathrm{GL}_n(\mathbb{A}_F)$ with $\rho \cong r_\lambda(\pi)$.

**Lemma (Defect Control).** The defect $\delta = \mathrm{pd}_{R_\infty}(M_\infty) - \dim R_\infty$ satisfies $\delta \leq \dim H^2(G_{F,\Sigma}, \mathrm{ad}^0\bar\rho)$.

## Approach Summary
1. Use the Calegari-Geraghty method: patch in the derived category to handle $n \geq 3$.
2. Apply potential automorphy (Thorne 2015) to ensure residual automorphy over a solvable CM extension.
3. Use derived Hecke algebras: $H^*(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho)$ acts on completed cohomology $\widetilde{H}^*$.
4. Show $t$-exactness of the completed cohomology functor under Taylor-Wiles conditions.
5. Read off automorphy from the patched $R_\infty \cong \mathbb{T}_\infty$ isomorphism.

## Computational Example
Take $F = \mathbb{Q}(\mu_7)$ (CM field), $n = 3$, $\ell = 11$. Let $\bar\rho: G_F \to \mathrm{GL}_3(\mathbb{F}_{11})$ be the residual representation attached to a cuspidal automorphic representation $\pi$ of $\mathrm{GL}_3(\mathbb{A}_F)$ of weight $(2, 3, 4)$. The adjoint representation $\mathrm{ad}\,\bar\rho$ has dimension 8, and $\dim H^2(G_{F,\Sigma}, \mathrm{ad}^0\bar\rho) = 1$ (computed via Tate's Euler characteristic formula). The defect $\delta \leq 1$, so the patched module $M_\infty$ may not be free over $\mathbb{S}_\infty$, but the derived Hecke algebra method handles this.

## Obstacle Analysis
- **Primary**: For $n \geq 3$, $R_{\bar\rho}^{\Sigma, \mathbf{v}}$ may not be a complete intersection; the patched module has nontrivial higher homology.
- **Secondary**: The "defect" $\delta$ grows with $n$ and requires new ideas to control for large $n$.
- **Tertiary**: Removing the residual automorphy hypothesis requires new techniques beyond current methods.

## Cross-Group Connections
- **G-001**: Taylor-Wiles patching provides the framework for $R = \mathbb{T}$.
- **G-010**: Potential automorphy feeds residual automorphy hypotheses.
- **G-006**: Symmetric power functoriality requires higher-dimensional modularity.
- **G-003**: Local deformation ring smoothness is a prerequisite.

## Classification
Core techniques — the engine connecting Galois representations to automorphic forms.
