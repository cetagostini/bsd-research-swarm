# G-005: The Langlands-Weissman Approach to L-Values

## Status Assessment
Active research. The theoretical framework is developed (Weissman 2023). Explicit L-value formulas are known in low rank (Waldspurger, Gross-Zagier). The general framework for GLₙ and its covers remains incomplete.

## Testable Conjecture

**Conjecture (Central L-Value Formula).** Let $\pi$ be a tempered cuspidal automorphic representation of $\mathrm{GL}_2(\mathbb{A}_F)$ with $\pi_\infty$ discrete series. Then:

$$L^*(1/2, \pi) = \frac{|\alpha(P_\pi)|^2}{\langle \phi, \phi \rangle} \cdot \prod_v \alpha_v$$

where $P_\pi = \int_{Z(\mathbb{A})\backslash \mathrm{GL}_2(F)} \phi(g) \, dg$ is the period integral, $\phi$ is a test vector, and $\alpha_v$ are explicit local factors.

**Lemma (Waldspurger's Formula).** For $\mathrm{GL}_2$ with a quadratic character $\chi$, $L(1/2, \pi \times \chi) = c \cdot |P_\chi(\phi)|^2$ for an explicit constant $c$ depending only on $\pi$ and the choice of test vector.

## Approach Summary
1. Use Brylinski-Deligne central extensions of reductive groups by $K_2$.
2. Develop the Langlands-Weissman L-group formalism for non-connected L-groups.
3. Express L-values via Rankin-Selberg integral representations.
4. Use the Ichino-Ikeda / Gan-Gross-Prasad conjectures to relate periods to L-values.
5. Apply the relative trace formula to compare period integrals with spectral data.

## Computational Example
Take $\pi$ the automorphic representation of $\mathrm{GL}_2(\mathbb{A}_\mathbb{Q})$ attached to the elliptic curve $E: y^2 = x^3 - x$ (conductor 32) and $\chi = \chi_{-4}$ the Kronecker character. The central value $L(1/2, \pi \times \chi) \approx 0.6555$ (computed via Dokchitser). Waldspurger's formula gives $L(1/2, \pi \times \chi) = \frac{|P_\chi(\phi_0)|^2}{\langle \phi_0, \phi_0 \rangle} \cdot \Omega$ where $\phi_0$ is the newform and $\Omega$ is an explicit product of local integrals.

## Obstacle Analysis
- **Primary**: Metaplectic L-groups have disconnected dual groups; Arthur's endoscopic classification does not directly apply.
- **Secondary**: Extension from tempered to non-tempered representations requires handling Eisenstein cohomology.
- **Tertiary**: The relative trace formula comparison is technically difficult beyond low-rank cases.

## Cross-Group Connections
- **G-006**: The Langlands-Weissman framework is a specific instance of functoriality.
- **G-010**: Potential automorphy gives analytic continuation needed for L-value formulas.
- **G-001**: The adjoint L-value enters the Taylor-Wiles numerical criterion.
- **G-011**: p-adic interpolation of L-values connects to eigenvariety geometry.

## Classification
New framework — potentially unifying approach to central L-values.
