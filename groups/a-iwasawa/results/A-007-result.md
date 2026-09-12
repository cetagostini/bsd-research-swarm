# A-007: Non-Commutative Iwasawa Theory

## Status Assessment

Non-commutative Iwasawa theory is the most ambitious direction in the Iwasawa-theoretic approach to BSD. It aims to unify BSD across all Artin twists in a single framework. The theory is largely conjectural: the CFKS conjecture is proven only in trivial cases (pro-$p$ extensions where the Selmer group vanishes). The Fukaya–Kato formulation using K-theory is mathematically complete but lacks computational verification. Realistic timeline for significant progress: 10–20 years.

## Testable Conjecture

**Conjecture (CFKS Cotorsion).** Let $E/\mathbb{Q}$ be an elliptic curve and $F_\infty/\mathbb{Q}$ a Galois extension with $G = \operatorname{Gal}(F_\infty/\mathbb{Q})$ a compact $p$-adic Lie group of dimension $d \geq 2$. Assume $F_\infty$ contains the cyclotomic $\mathbb{Z}_p$-extension $\mathbb{Q}_\infty$ and that $F_\infty$ is obtained by adjoining the $p$-power torsion points of an elliptic curve $E'$ (the "false Tate curve" extension: $G \cong \mathbb{Z}_p \rtimes \mathbb{Z}_p^\times$). Then

$$\operatorname{Sel}_{p^\infty}(E/F_\infty) \text{ is } \mathbb{Z}_p[[G]]\text{-cotorsion}$$

and the Fukaya–Kato Main Conjecture holds: the non-commutative $p$-adic L-function $\mathcal{L}_p(E/F_\infty) \in K_1(\mathbb{Z}_p[[G]][1/p])$ generates the characteristic ideal of $\operatorname{Sel}_{p^\infty}(E/F_\infty)^\vee$ in the appropriate localization.

## Approach Summary

**Phase 1: False Tate curve extension.** Let $F_\infty = \mathbb{Q}(E'[p^\infty])$ for an elliptic curve $E'/\mathbb{Q}$. Then $G = \operatorname{Gal}(F_\infty/\mathbb{Q})$ embeds into $\mathrm{GL}_2(\mathbb{Z}_p)$. Compute $\operatorname{Sel}_{p^\infty}(E/F_n)$ for the first few layers $F_n$ of the false Tate tower using Magma. Verify cotorsion by checking that the $\mathbb{Z}_p$-corank stabilizes.

**Phase 2: K-theoretic formulation.** The Fukaya–Kato Main Conjecture uses the Whitehead group $K_1(\mathbb{Z}_p[[G]])$ and its localization. For $G = \mathrm{GL}_2(\mathbb{Z}_p)$, compute $K_1(\mathbb{Z}_p[[G]])$ via the Bass–Heller–Swan decomposition and the Dennis–Trace map to cyclic homology. The non-commutative $p$-adic L-function lives in $K_1(\mathbb{Z}_p[[G]][1/p])$.

**Phase 3: Specialization to Artin characters.** For each Artin character $\chi$ of $G$, the specialization map $K_1(\mathbb{Z}_p[[G]][1/p]) \to K_1(\overline{\mathbb{Q}_p}) = \overline{\mathbb{Q}_p}^\times$ sends $\mathcal{L}_p$ to $L_p(E, \chi, 1)$. Verify this for low-dimensional characters computationally.

## Computational Example

**Curve 11a1** in the false Tate curve extension $F_\infty = \mathbb{Q}(E'[3^\infty])$ where $E' = 11a1$ at $p = 3$:

$G = \operatorname{Gal}(F_\infty/\mathbb{Q}) \hookrightarrow \mathrm{GL}_2(\mathbb{Z}_3)$. Layers: $F_0 = \mathbb{Q}$, $F_1 = \mathbb{Q}(E'[3])$ (degree dividing 48 over $\mathbb{Q}$). At layer $F_1$: compute $\operatorname{Sel}_{3^\infty}(11a1/F_1)$. The cotorsion conjecture predicts $\operatorname{corank}_{\mathbb{Z}_3} \operatorname{Sel}_{3^\infty}(11a1/F_1) = 0$ (since $L(11a1, 1) \neq 0$ and $L(11a1, \chi, 1) \neq 0$ for all low-dimensional $\chi$).

For the twist by the standard representation $\rho$ of $\mathrm{GL}_2(\mathbb{Z}_3)$: $L(11a1, \rho, 1)$ should be non-zero and its $3$-adic valuation should match the $3$-adic valuation of $\mathcal{L}_p(\rho)$.

## Obstacle Analysis

The fundamental obstacle is the abstractness of $K_1(\mathbb{Z}_p[[G]])$. For commutative $G$, $K_1(\Lambda) = \Lambda^\times$ is simply the group of units, and the characteristic ideal is principal. For non-commutative $G$, $K_1(\mathbb{Z}_p[[G]])$ is not a ring and has no simple description. The Ore localization $\mathbb{Z}_p[[G]][1/p]$ is non-trivial to construct, and the characteristic variety is defined via Fitting invariants in the abelianization. Even defining the interpolation problem for $\mathcal{L}_p$ requires specifying the image of $K_1(\mathbb{Z}_p[[G]][1/p])$ under all Artin character specializations, which is the equivariant Tamagawa number conjecture (ETNC). The ETNC is known for abelian extensions (by Burns–Greither and Huber–Kings) but open for non-abelian $G$.

## Cross-Group Connections

- **Group A (Main Conjecture):** The commutative Main Conjecture is a special case (abelian $G$).
- **Group C (Euler Systems):** Euler systems over non-abelian extensions provide the algebraic input.
- **Group H (Galois Representations):** The $p$-adic Langlands program for $\mathrm{GL}_2$ is needed for the false Tate curve case.
- **Group F (BSD Formula):** The non-commutative Main Conjecture implies BSD for all Artin twists simultaneously.

## Classification

Conjecture
