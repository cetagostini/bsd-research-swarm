# G-001: Taylor-Wiles Method Extensions for Higher-Rank Selmer Groups

## Status Assessment
Active research. GL₂ over totally real fields is essentially complete (Kisin 2009). The GLₙ case requires derived methods and is known for regular weight under mild hypotheses (Calegari-Geraghty 2016). Passage to irregular weight and general coefficient fields remains open.

## Testable Conjecture

**Conjecture (Higher-Rank Selmer Control).** Let $F$ be a CM field, $n \geq 3$, and $\bar\rho: G_F \to \mathrm{GL}_n(\overline{\mathbb{F}}_\ell)$ absolutely irreducible. Assume $\bar\rho$ is automorphic of regular weight. Then:

$$\mathrm{corank}_{\mathcal{O}}\, \mathrm{Sel}_\Sigma(F, \mathrm{ad}\,\bar\rho(1)) = \mathrm{ord}_{s=1} L(\mathrm{ad}\,\bar\rho, s)$$

provided the global deformation ring $R_\infty$ is a complete intersection (i.e., the "defect" $\delta = \mathrm{pd}_{R_\infty}(M_\infty) - \dim R_\infty = 0$).

**Lemma (Patched Module Freeness).** Under the Calegari-Geraghty patching with derived Hecke algebras, if $H^2(G_{F,\Sigma}, \mathrm{ad}^0\bar\rho) = 0$, then $M_\infty$ is free over $\mathbb{S}_\infty$, and the classical Taylor-Wiles numerical criterion applies.

## Approach Summary
1. Choose Taylor-Wiles primes $Q = \{q_1, \ldots, q_N\}$ with $q_i \equiv 1 \pmod{\ell^M}$ and $\bar\rho(\mathrm{Frob}_{q_i})$ having distinct eigenvalues.
2. Construct the patched deformation ring $R_\infty^{\square_Q} \cong \mathcal{O}[[S_\infty, T_\infty]]$ via Kisin's framing.
3. Patch the homology of arithmetic groups (using perfectoid methods or classical Borel-Serre).
4. Use derived Hecke algebras to handle the case where $M_\infty$ is not free over $\mathbb{S}_\infty$.
5. Apply Poitou-Tate duality to relate the Selmer group to the adjoint L-value.

## Computational Example
Consider $\bar\rho: G_{\mathbb{Q}} \to \mathrm{GL}_3(\mathbb{F}_7)$ the residual representation attached to a Siegel modular form of genus 2 and level $N = 1$. The adjoint L-function $L(\mathrm{ad}\,\bar\rho, s)$ has order of vanishing 1 at $s = 1$ (verified numerically via Dokchitser's algorithm). The Selmer group $\mathrm{Sel}(\mathbb{Q}, \mathrm{ad}\,\bar\rho(1))$ should have $\mathbb{F}_7$-corank 1. The Taylor-Wiles primes must satisfy $q \equiv 1 \pmod{7^M}$ with $\bar\rho(\mathrm{Frob}_q)$ having eigenvalues in distinct $\mathbb{F}_7^\times$-cosets.

## Obstacle Analysis
- **Primary**: For $n \geq 3$, $H^2(G_{F,\Sigma}, \mathrm{ad}^0\bar\rho)$ can be nonzero, obstructing freeness of $M_\infty$ over $\mathbb{S}_\infty$.
- **Secondary**: The derived Hecke algebra produces a perfect complex rather than a single module; extracting the Selmer group requires controlling cohomological amplitude.
- **Tertiary**: Irregular weight cases lack the Fontaine-Laffaille theory needed for smooth local deformation rings.

## Cross-Group Connections
- **G-008**: Selmer group structure is the deformation-theoretic dual of this direction.
- **G-003**: Local deformation ring smoothness (Fontaine-Laffaille) feeds the global patching.
- **G-011**: p-adic Langlands provides refined patching for p-adic families.
- **G-004**: Higher-dimensional modularity lifting relies on the patched $R = \mathbb{T}$ isomorphism.

## Classification
Foundational — enables all modularity lifting results in this group.
