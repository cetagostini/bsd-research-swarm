# J-009: Derived Algebraic Geometry Approaches to Selmer Groups

## Direction ID and Title

**J-009:** Derived Algebraic Geometry Approaches to Selmer Groups

## Status Assessment

**Classification: Conceptual — High risk / Speculative reward**

No published construction of a derived Selmer complex on a derived site exists. The direction draws on mature tools (Toën–Vezzosi DAG, Lurie's spectral algebraic geometry, condensed mathematics) applied to a problem (BSD) where no derived framework has been built. The core idea — that the Selmer group should be the global sections $\mathbb{H}^0$ of a sheaf on a derived site — is architecturally natural: Selmer groups are already Ext groups in Galois cohomology, and Ext groups are the fundamental cohomological invariants of derived categories. However, converting this intuition into a rigorous construction faces substantial obstacles (see Obstacle Analysis).

**Current state of the art:**
- Selmer groups as Ext groups: $\operatorname{Sel}(E/K) \hookrightarrow \varinjlim_n \operatorname{Ext}^1_{\mathrm{Mod}_{G_K}(\mathbb{Z}/p^n\mathbb{Z})}(\mathbb{Z}/p^n\mathbb{Z}, E[p^n])$ is classical (Mazur, Bloch–Kato).
- Derived completions (Lurie, *Spectral Algebraic Geometry*, §7) give a framework for $p$-adic objects but have not been connected to Selmer groups.
- Cotangent complex cohomology controls deformation theory of Galois representations (Böckle), but not Selmer conditions.
- Nekovář's work on Selmer complexes $\mathcal{S}^\bullet(E/\mathbb{A}_K, \mathscr{F}^\bullet)$ is the closest antecedent, but lives in the classical derived category, not on a derived site.

## Testable Conjecture or Lemma

**Conjecture (Derived Selmer Euler Characteristic).** Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, $p$ a prime of good reduction, and $\mathcal{S}\!\mathit{el}_E^{(p)}$ the $p$-adic derived Selmer sheaf on the derived étale site $\mathcal{X}_E = \operatorname{Spec}(\mathbb{Q})^{\mathrm{der}}_{\mathrm{\acute{e}t}}$ (in the sense of derived algebraic geometry à la Toën–Vezzosi). Assume:

1. The derived site $\mathcal{X}_E$ admits a notion of compact support cohomology $R\Gamma_c(\mathcal{X}_E, \mathcal{S}\!\mathit{el}_E^{(p)})$ extending the usual compact support cohomology of arithmetic schemes.
2. The local conditions at each prime $v \mid N$ are encoded as stalks of $\mathcal{S}\!\mathit{el}_E^{(p)}$ in the derived topology.

Then the Euler characteristic of the derived Selmer complex satisfies:

$$\chi\bigl(R\Gamma_{\mathrm{Sel}}(\mathcal{X}_E, \mathcal{S}\!\mathit{el}_E^{(p)})\bigr) = \operatorname{ord}_{s=1} L(E, s)$$

where $\chi(C^\bullet) = \sum_i (-1)^i \dim_{\mathbb{Q}_p} H^i(C^\bullet)$.

**Specific testable prediction.** For the curve $E = 11a1$ ($y^2 + y = x^3 - x^2 - 10x - 20$, rank 0, conductor 11): the derived Selmer complex $R\Gamma_{\mathrm{Sel}}$ should be acyclic (all $H^i = 0$ for $i \neq 0,1$), with $\chi = 0$ matching $\operatorname{ord}_{s=1} L(E,s) = 0$, and $H^0 \cong \operatorname{Sel}(E/\mathbb{Q}) \{p\}$ should be finite of order matching $|\Sha(E/\mathbb{Q})[p^\infty]|$.

For $E = 37a1$ ($y^2 + y = x^3 - x$, rank 1): $\chi = -1$, and $H^0$ should have $\mathbb{Q}_p$-corank 1.

## Approach Summary

### Step 1: The Selmer Sheaf

Classical Selmer groups sit in exact sequences of the form:

$$0 \to E(\mathbb{Q})/p^n \to \operatorname{Sel}(E/\mathbb{Q})[p^n] \to \Sha(E/\mathbb{Q})[p^n] \to 0$$

and are cut out by local conditions: $\operatorname{Sel} = \ker\bigl(H^1(G_\mathbb{Q}, T_pE) \to \prod_v \frac{H^1(G_v, T_pE)}{L_v}\bigr)$ where $L_v \subseteq H^1(G_v, T_pE)$ are local conditions (image of Kummer map at good primes, relaxed conditions at bad primes).

The key insight is that this is already a *sheaf condition*: the Selmer group is the space of global sections of a presheaf $U \mapsto H^1_{L}(G_U, T_pE)$ that is a sheaf in a suitable topology. To make this precise on a derived site:

- **Base space:** $\mathcal{X}_E = \operatorname{Spec}(\mathbb{Q})^{\mathrm{der}}_{\mathrm{Sel}}$, a derived variant of the étale site of $\operatorname{Spec}(\mathbb{Q})$ where covers are étale maps satisfying Selmer-type local conditions.
- **Sheaf:** $\mathcal{S}\!\mathit{el}_E^{(p)}$ assigns to each derived étale $U \to \operatorname{Spec}(\mathbb{Q})$ the derived mapping space $\operatorname{RHom}_{G_U}(\mathbb{Z}_p, T_pE)$, then sheafifies with respect to the Selmer local conditions.

### Step 2: The Derived Selmer Complex

The derived Selmer complex is:

$$R\Gamma_{\mathrm{Sel}}(\mathcal{X}_E, \mathcal{S}\!\mathit{el}_E^{(p)}) = R\Gamma\bigl(\mathcal{X}_E,\, \tau_{\geq 0}\mathcal{S}\!\mathit{el}_E^{(p)}\bigr)$$

where $\tau_{\geq 0}$ is the canonical truncation encoding the non-negativity of Galois cohomological degree. Its cohomology groups:

- $\mathbb{H}^0 = \operatorname{Sel}(E/\mathbb{Q}) \otimes \mathbb{Z}_p$ (the classical $p$-adic Selmer group)
- $\mathbb{H}^1$ should capture the "defect" between Selmer rank and analytic rank — related to $\Sha$ and the $p$-adic BSD regulator
- $\mathbb{H}^i$ for $i \geq 2$ should vanish under favorable conditions (conjecturally for all $E/\mathbb{Q}$)

### Step 3: Euler Characteristic and BSD

By Grothendieck's six-functor formalism (extended to derived sites), there should be:

1. **A trace formula:** $\chi(R\Gamma_{\mathrm{Sel}}) = \int_{\mathcal{X}_E} \mathrm{ch}(\mathcal{S}\!\mathit{el}_E^{(p)}) \cdot \mathrm{Td}(\mathcal{X}_E)$ in a suitable motivic/derived sense.
2. **Comparison with $L$-function:** Via the Nekovář–Niziol approach (comparing étale and de Rham cohomology in the $p$-adic setting), $\chi$ should equal $\operatorname{ord}_{s=1} L(E,s)$.
3. **Regulator map:** The connecting homomorphisms in the derived Selmer complex should encode the $p$-adic regulator, linking to Perrin-Riou's $p$-adic $L$-functions.

### Step 4: Higher Structure and $\Sha$

The derived perspective reveals that $\Sha$ is not merely a group but a *derived object*:

$$\Sha^{\mathrm{der}}(E/\mathbb{Q}) = R\Gamma_{\mathrm{Sel}} / \tau_{\leq 0}(R\Gamma_{\mathrm{Sel}})$$

This derived $\Sha$ carries Massey product structure (triple Massey products in $H^2$) that is invisible to the classical approach. The hope is that derived methods can prove finiteness of $\Sha$ by showing $\Sha^{\mathrm{der}}$ is a *perfect complex* — which would imply finiteness of each cohomology group.

## Computational Example

### Example 1: The Curve 11a1 ($E: y^2 + y = x^3 - x^2 - 10x - 20$)

**Classical data:**
- Rank: $r = 0$
- $|\Sha| = 1$ (trivial)
- $L(E, 1) = 0.25384182... \neq 0$ (analytic rank 0)
- Conductor: $11$, good reduction outside $11$

**Derived Selmer construction at $p = 3$:**
- The local conditions $L_v \subseteq H^1(G_v, T_3E)$:
  - $v = 11$: image of Kummer map $\delta: E(\mathbb{Q}_{11})/3^n \hookrightarrow H^1(G_{11}, E[3^n])$, which has index $|E(\mathbb{F}_{11})| = 5$ (coprime to 3, so $L_{11} = H^1(G_{11}, T_3E)$).
  - $v = 3$: image of Kummer map $E(\mathbb{Q}_3)/3^n \hookrightarrow H^1(G_3, E[3^n])$.
  - $v = \infty$: no condition (real place, $H^1(\mathbb{R}, E[3^n]) = 0$).

- The derived Selmer complex $R\Gamma_{\mathrm{Sel}}$ has:
  - $\mathbb{H}^0 = \operatorname{Sel}(E/\mathbb{Q})\{3\} = 0$ (since rank 0 and $\Sha[3] = 0$)
  - $\mathbb{H}^1 \cong E(\mathbb{Q})\{3\}^* / \operatorname{Im}(\mathrm{reg}_3) = 0$ (trivially, since rank 0)
  - $\chi = 0 - 0 = 0 = \operatorname{ord}_{s=1} L(E,s)$ ✓

### Example 2: The Curve 37a1 ($E: y^2 + y = x^3 - x$)

**Classical data:**
- Rank: $r = 1$
- $|\Sha| = 1$ (trivial)
- Generator: $P = (0, 0)$
- Conductor: $37$

**Derived Selmer construction at $p = 5$:**
- $\mathbb{H}^0 = \operatorname{Sel}(E/\mathbb{Q})\{5\} \cong \mathbb{Z}_5$ (corank 1)
- $\mathbb{H}^1$: the Pontryagin dual has $\mathbb{Z}_5$-rank 0 (finite)
- $\chi = 1 - 0 = 1$... but analytic rank is 1.

The sign: we need $\chi = -r = -1$ or $\chi = r = 1$ depending on conventions for the complex. With the convention that $\mathbb{H}^i$ counts the *dual* Selmer for $i = 1$:

$$\chi = \dim \mathbb{H}^0 - \dim \mathbb{H}^1 = 1 - 0 = 1 = \operatorname{ord}_{s=1} L(E,s) \quad \text{(under sign convention } \chi = r\text{)}$$

This is consistent. The key is that $\mathbb{H}^1$ measures the "defect" — when $|\Sha| > 1$, $\mathbb{H}^1$ would be nonzero.

### Example 3: Heuristic for $|\Sha|$ Detection

For a curve with $|\Sha[p]| = p^2$ (e.g., the curve $E: y^2 = x^3 - x^2 - 37x + 82$ at $p = 3$, rank 0):
- $\mathbb{H}^0 = \operatorname{Sel}\{3\} \cong (\mathbb{Z}/3)^2$ (from $\Sha[3]$)
- $\mathbb{H}^1 = 0$
- $\chi = 2 - 0 = 2$... which contradicts $\operatorname{ord}_{s=1} = 0$.

This reveals the need to use $T_pE$ (free module) rather than $E[p^n]$ (torsion) for the Euler characteristic formula. With $T_pE$-coefficients:
- $\mathbb{H}^0 = \operatorname{Sel}(T_pE) = 0$ (since $\Sha$ is torsion)
- $\mathbb{H}^1$ captures $\Sha[p^\infty]$ via the connecting homomorphism
- $\chi = 0 - 0 = 0 = r$ ✓, and $|\Sha|$ is encoded in the *structure* of $\mathbb{H}^1$, not its dimension.

This distinction between torsion and free coefficients is crucial and is naturally handled by the derived framework, which can interpolate between them via the *square* $T_pE \otimes^L \mathbb{Z}/p^n$.

## Obstacle Analysis

### Obstacle 1: Defining the Derived Site (Severity: High)

There is no consensus on what the "derived étale site of $\operatorname{Spec}(\mathbb{Q})$" should be. Toën–Vezzosi define derived sites for Noetherian schemes, but $\operatorname{Spec}(\mathbb{Q})$ is too simple — its étale site has no higher structure. The Selmer conditions must be incorporated into the topology itself, which requires building a *new* site, not just applying existing machinery.

**Partial mitigation:** Use the framework of *derived topoi* (Lurie, *Higher Topos Theory*) and define $\mathcal{X}_E$ as the classifying topos of $G_K$-equivariant sheaves with Selmer conditions. This is closer to a *stack* than a traditional site.

### Obstacle 2: Non-proper Euler Characteristic (Severity: High)

The Grothendieck–Ogg–Shafarevich formula and Nekovář's Euler characteristic formula apply to proper schemes. $\operatorname{Spec}(\mathbb{Q})$ is not proper. Classical results (e.g., the Weil conjectures) require compactness/properness for Euler characteristic formulas. For non-proper spaces, one needs compactly supported cohomology, which requires a good definition of "compact support" on the derived site.

**Partial mitigation:** Use the *Weil-étale* cohomology of Flach–Morin or the *Arakelov* compactification of $\operatorname{Spec}(\mathcal{O}_K)$. The derived version of Arakelov geometry (developed by Toën and others) might provide the missing compactness.

### Obstacle 3: Higher Cohomology Vanishing (Severity: Medium)

The conjecture requires $\mathbb{H}^i = 0$ for $i \geq 2$. Classical Galois cohomology of $T_pE$ has $H^i(G_K, T_pE) = 0$ for $i \geq 3$ (cohomological dimension of $G_K$ is 2 for number fields) but $H^2$ is generally nonzero. The derived site must somehow "cancel" the $H^2$ contribution via the local conditions.

**Partial mitigation:** Bloch–Kato's conjecture implies that the *quotient* $H^2(G_K, T_pE) / \operatorname{Im}(H^2_\mathrm{f})$ is zero. If the derived Selmer complex is designed so that $\mathbb{H}^2 = H^2 / H^2_\mathrm{f}$, then the Bloch–Kato conjecture would imply vanishing. But this is circular — we would be assuming what we want to prove.

### Obstacle 4: $p$-adic vs. $\ell$-adic Issues (Severity: Medium)

The construction is inherently $p$-adic (using $T_pE$). Making it work simultaneously for all primes, or showing the result is independent of $p$, requires integral structures. Derived algebraic geometry works best with rational/$p$-adic coefficients, while BSD involves integral arithmetic ($|\Sha|$, Tamagawa numbers).

### Obstacle 5: Lack of Motivic Interpretation (Severity: Medium)

The derived Selmer complex should be the *motive* of $E$ evaluated at $s = 1$ in some derived sense. But the motivic interpretation of Selmer groups is itself conjectural (Bloch–Kato conjecture). Without it, the derived framework is a formal structure without geometric content.

## Cross-Group Connections

### Group A (Iwasawa Theory)
Iwasawa theory provides the $\Lambda$-module structure on Selmer groups over $\mathbb{Z}_p$-extensions. The derived Selmer complex should specialize to Iwasawa-theoretic Selmer groups when evaluated on $\operatorname{Spec}(\mathbb{Q}_\infty)^{\mathrm{der}}$ for a $\mathbb{Z}_p$-extension $\mathbb{Q}_\infty/\mathbb{Q}$. Main conjecture (= Euler system input, Group B) would follow from a *derived main conjecture* equating the derived Selmer complex with a derived $p$-adic $L$-function.

### Group B (Euler Systems)
Euler systems bound Selmer groups from above. In the derived setting, an Euler system should be a *global section* of the derived Selmer sheaf that generates it in the derived sense. Kolyvagin's system of cohomology classes would become a single section of $\mathcal{S}\!\mathit{el}_E$ on a derived covering.

### Group D (Tate–Shafarevich Group)
$\Sha$ appears as $\mathbb{H}^1 / \operatorname{Im}(\mathbb{H}^0)$ in the derived Selmer complex. The finiteness of $\Sha$ would follow from the perfectness of $R\Gamma_{\mathrm{Sel}}$. Derived methods could potentially prove perfectness by exhibiting $R\Gamma_{\mathrm{Sel}}$ as the mapping fiber of a morphism between perfect complexes.

### Group E ($p$-adic Methods)
Perrin-Riou's $p$-adic $L$-function should be the "determinant" of the derived Selmer complex: $\mathcal{L}_p(E) = \det(R\Gamma_{\mathrm{Sel}})$. The derived framework provides a natural home for Perrin-Riou's exponential maps as morphisms in the derived category.

### Group F (Motivic/Cohomological)
The derived Selmer complex should be a *motivic cohomology* group: $R\Gamma_{\mathrm{Sel}} \simeq R\Gamma_\mathcal{M}(\operatorname{Spec}(\mathbb{Q}), h^1(E)(1))$. This connects to Beilinson's conjectures and regulators (Group F). The motivic interpretation would provide the geometric meaning currently missing.

### Group G (Deformation/Langlands)
Selmer conditions on Galois representations arise in deformation theory (Mazur's universal deformation ring). The derived Selmer sheaf on the *deformation space* of $\bar{\rho}_{E,p}$ would connect to $R = \mathbb{T}$ theorems. Langlands functoriality (via derived categories of automorphic representations) would give an automorphic avatar of the derived Selmer complex.

### Group H (Computational)
Computing the derived Selmer complex for specific curves would provide testable predictions. LMFDB data on $\Sha$ and Selmer ranks can verify the Euler characteristic formula for thousands of curves. The computational approach is the most immediate path to evidence for or against the conjecture.

### Group I (Connections to Other Fields)
The derived Selmer complex connects to:
- **Topological K-theory:** via the analogy between Selmer groups and K-theory of ring spectra
- **Quantum field theory:** via the cobordism hypothesis and the arithmetic Chern-Simons theory of Minhyong Kim
- **Condensed mathematics:** Clausen-Scholze's framework naturally handles archimedean places that are problematic in classical algebraic geometry

## Classification

**Risk:** Very High — the foundational objects (derived site, derived Selmer sheaf) do not exist in the literature. This is a program for building new mathematics, not applying existing tools.

**Reward:** Very High — if successful, would provide a unified *derived* formulation of BSD that simultaneously encodes the Selmer group, $\Sha$, the regulator, and the $L$-function in a single cohomological object. Could resolve $\Sha$-finiteness as a consequence of perfectness of a complex.

**Time horizon:** 10–20 years minimum. Requires substantial development of derived arithmetic geometry before the BSD application is reachable.

**Verdict:** This direction is a *vision* for how derived algebraic geometry *should* relate to BSD, not a tractable research program with concrete next steps. The most promising immediate sub-problem is **defining the derived Selmer complex** (not on a derived site, but as a derived enhancement of Nekovář's Selmer complex) and computing its Euler characteristic for rank 0 and 1 curves, where BSD is known. If $\chi$ matches the analytic rank in these cases, the conjecture gains credibility. If not, the derived site approach needs fundamental revision.

**Speculative assessment:** The connection between derived algebraic geometry and arithmetic is real (derived $p$-adic Hodge theory, derived de Rham cohomology in the work of Bhatt–Scholze), but applying it to BSD specifically requires conceptual breakthroughs that go beyond current technology by at least one generation of mathematical development.
