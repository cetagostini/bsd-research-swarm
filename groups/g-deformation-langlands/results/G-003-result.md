# G-003: Fontaine-Laffaille Modules and Local Deformation Rings

## Status Assessment
Largely resolved for GL₂ and ℓ ≥ 5 (Kisin 2006). Active research for ℓ = 2, 3 and GLₙ with n ≥ 3. The Emerton-Gee stack-theoretic framework provides a systematic approach.

## Testable Conjecture

**Conjecture (Crystalline Smoothness).** For $\bar\rho: G_{\mathbb{Q}_\ell} \to \mathrm{GL}_n(\overline{\mathbb{F}}_\ell)$ in the Fontaine-Laffaille range ($\ell > k$ where $k$ is the maximal Hodge-Tate weight), the framed crystalline deformation ring $R_\ell^{\square, \mathrm{cr}, \mathbf{v}}$ is formally smooth over $\mathcal{O}$ of dimension $n^2 + \binom{n}{2}$.

**Lemma (Tangent Space Formula).** The tangent space of $\mathcal{D}_{\bar\rho}^{\square, \mathrm{cr}, \mathbf{v}}$ has $\mathcal{O}$-dimension equal to $n^2 + \dim_{\mathbb{F}_\ell} H^0(G_{\mathbb{Q}_\ell}, \mathrm{ad}\,\bar\rho) - \dim_{\mathbb{F}_\ell} H^0(G_{\mathbb{Q}_\ell}, \mathrm{ad}\,\bar\rho(1))$.

## Approach Summary
1. Use Fontaine-Laffaille theory to classify crystalline representations with HT weights in $[0, \ell-2]$.
2. Compute $H^1(G_{\mathbb{Q}_\ell}, \mathrm{ad}\,\bar\rho)$ via local Tate duality.
3. Show the framed deformation functor is smooth by verifying the obstruction space $H^2(G_{\mathbb{Q}_\ell}, \mathrm{ad}\,\bar\rho) = 0$.
4. For $v \neq \ell$, use Böckle's result that local deformation rings are formally smooth of dimension $n^2$.
5. Beyond the FL range, use Kisin's $(\varphi, \hat{G})$-modules.

## Computational Example
Take $n = 2$, $\ell = 7$, $\mathbf{v} = (0, 4)$ (i.e., $k = 5 < 7$). Let $\bar\rho: G_{\mathbb{Q}_7} \to \mathrm{GL}_2(\mathbb{F}_7)$ be the residual representation attached to a weight-5 modular form of level 1. The crystalline deformation ring $R_7^{\square, \mathrm{cr}, (0,4)}$ is formally smooth of dimension $4 + \binom{2}{2} = 5$ over $\mathcal{O}$. The tangent space has dimension 5, matching the expected dimension. The Fontaine-Laffaille module is a 2-dimensional $\mathbb{F}_7$-vector space with filtration jumps at positions 0 and 4.

## Obstacle Analysis
- **Primary**: Outside the Fontaine-Laffaille range ($\ell \leq k$), Breuil modules introduce complications; the ring need not be smooth.
- **Secondary**: For $\ell = 2, 3$, the Galois cohomology $H^2(G_{\mathbb{Q}_\ell}, \mathrm{ad}\,\bar\rho)$ can be nonzero, giving obstructions.
- **Tertiary**: For $n \geq 3$, the local rings can have embedded primes and non-reduced structure.

## Cross-Group Connections
- **G-001**: Smooth local deformation rings are essential input to Taylor-Wiles patching.
- **G-009**: The Breuil-Mézard conjecture governs the geometry of local deformation rings.
- **G-008**: Local deformation conditions enter the global deformation functor.
- **G-011**: p-adic Langlands uses the geometry of crystalline deformation spaces.

## Classification
Local analysis — foundational input to the global patching method.
