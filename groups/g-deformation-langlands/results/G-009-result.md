# G-009: The Breuil-Mézard Conjecture and Local-Global Compatibility

## Status Assessment
Active research. Known for GL₂(ℚ_p) (Kisin 2010). Partial results for GL₂ over unramified extensions (Helm 2014). The Emerton-Gee stack provides a conceptual framework but explicit computations for n ≥ 3 are ongoing.

## Testable Conjecture

**Conjecture (Breuil-Mézard Formula).** For $\bar\rho: G_{\mathbb{Q}_p} \to \mathrm{GL}_n(\overline{\mathbb{F}}_p)$ and a crystalline type $\mathbf{v}$, the Hilbert-Samuel multiplicity satisfies:

$$e(R_v^{\square, \mathbf{v}} / \varpi) = \sum_{\sigma \in \mathrm{Irr}(\mathrm{GL}_n(\mathbb{F}_p))} n_\sigma(\bar\rho|_{G_{\mathbb{Q}_p}}, \mathbf{v}) \cdot e_\sigma$$

where $e_\sigma$ is the multiplicity of $\sigma$ in the mod-$p$ Lusztig datum and $n_\sigma$ is a combinatorial coefficient determined by $\bar\rho$.

**Lemma (Component Multiplicity).** The irreducible components of $\mathrm{Spec}(R_v^{\square, \mathbf{v}})$ are in bijection with the representations $\sigma$ appearing with $n_\sigma > 0$ in the formula above, and each component has multiplicity $e_\sigma$.

## Approach Summary
1. Use Kisin's theory of $(\varphi, \hat{G})$-modules to study local deformation rings.
2. Relate to the mod-$\ell$ local Langlands correspondence (Vignéras, Breuil).
3. Use the Emerton-Gee stack $\mathscr{X}$ of mod-$p$ representations.
4. Compute special fibers of local Shtuka spaces (Harris-Taylor, Scholze).
5. Verify computationally for GL₂ and GL₃ (Le-Le Hung-Levin-Morra 2020).

## Computational Example
Take $n = 2$, $p = 5$, $\bar\rho: G_{\mathbb{Q}_5} \to \mathrm{GL}_2(\mathbb{F}_5)$ with $\bar\rho \sim \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. The crystalline type $\mathbf{v} = (0, 1)$. The framed deformation ring $R_5^{\square, (0,1)}$ modulo $\varpi = 5$ has Hilbert-Samuel multiplicity $e = 2$. The irreducible representations of $\mathrm{GL}_2(\mathbb{F}_5)$ are: trivial (1-dim), Steinberg (1-dim), principal series (4-dim), cuspidal (4-dim). The Breuil-Mézard formula gives $e = 1 \cdot e_{\mathrm{triv}} + 1 \cdot e_{\mathrm{St}}$ with $e_{\mathrm{triv}} = e_{\mathrm{St}} = 1$.

## Obstacle Analysis
- **Primary**: For $n \geq 3$, the combinatorics of the mod-$p$ local Langlands correspondence are not fully understood.
- **Secondary**: Special fibers of local Shtuka spaces are difficult to compute explicitly.
- **Tertiary**: The connection to deformation rings requires understanding geometry beyond the reduced structure.

## Cross-Group Connections
- **G-003**: Local deformation ring geometry is the input to Breuil-Mézard.
- **G-001**: The Breuil-Mézard formula enters Taylor-Wiles patching as the local factor.
- **G-008**: Local deformation conditions are governed by Breuil-Mézard data.
- **G-011**: p-adic Langlands uses the geometry of crystalline deformation spaces.

## Classification
Local analysis — connects local geometry to global arithmetic.
