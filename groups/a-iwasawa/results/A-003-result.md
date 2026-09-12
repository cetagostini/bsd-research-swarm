# A-003: Selmer Groups over $\mathbb{Z}_p$-extensions and Greenberg's Conjecture

## Status Assessment

Greenberg's conjecture ($\mu = 0$ and pseudo-nullity of $\mathfrak{X}_\infty$) is one of the deepest open problems in Iwasawa theory for elliptic curves. It is proven for CM curves (Ferrero–Washington + Rubin) but entirely open for non-CM curves. The direction is promising but long-term (10+ years for a proof in the non-CM case). Computational verification is feasible now and provides essential evidence.

## Testable Conjecture

**Conjecture (Greenberg).** Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at $p$. Then

$$\mu(E/\mathbb{Q}_\infty) = 0 \quad \text{and} \quad \mathfrak{X}_\infty = \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee$$

is pseudo-null as a $\Lambda$-module, i.e., $\operatorname{ann}_\Lambda(\mathfrak{X}_\infty) \neq 0$ and for every prime $\mathfrak{p} \subset \Lambda$ of height 1, the localization $(\mathfrak{X}_\infty)_\mathfrak{p} = 0$. Equivalently, the growth formula holds:

$$\dim_{\mathbb{F}_p} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p] = \lambda \cdot n + \nu \quad \text{for all } n \gg 0$$

with no $\mu \cdot p^n$ term, and $|\operatorname{III}(E/\mathbb{Q}_n)[p^\infty]|$ bounded independently of $n$.

## Approach Summary

**Phase 1: Computational evidence.** For curves with $N \leq 300$ and $p \in \{3, 5, 7\}$, compute $|\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p]|$ for layers $n = 0, 1, \ldots, 10$ using Magma's explicit cohomology computations. Fit the Iwasawa formula $\mu p^n + \lambda n + \nu$ and verify $\mu = 0$.

**Phase 2: Pseudo-nullity verification.** For the same curves, compute the $\Lambda$-module presentation matrix of $\mathfrak{X}_\infty$ from the finite-layer data using the control theorem. Verify that the presentation matrix has the pseudo-nullity property: its Fitting ideal has height $\geq 2$.

**Phase 3: Theoretical approach.** The most promising strategy for proving $\mu = 0$ in the non-CM case is via the $p$-adic Langlands correspondence. If one can show that the $(\varphi, \Gamma)$-module of $E[p^\infty]$ over $\mathbb{Q}_p$ has no non-trivial étale lattice with $\mu > 0$, then $\mu(E/\mathbb{Q}_\infty) = 0$ follows. This connects to Breuil–Mézard conjectures and the moduli of Galois deformation rings.

## Computational Example

**Curve 11a1** at $p = 3$:

| Layer $n$ | $|\operatorname{Sel}_{3^\infty}(E/\mathbb{Q}_n)[3]|$ | Predicted ($\mu = 0$) |
|---|---|---|
| 0 | 1 | $\lambda \cdot 0 + \nu = \nu$ |
| 1 | 1 | $\lambda \cdot 1 + \nu$ |
| 2 | 1 | $\lambda \cdot 2 + \nu$ |

For 11a1 at $p = 3$: $a_3 = -2$, $L_p$ has $\lambda = 0$ (no vanishing). So $\lambda = 0$ and $|\operatorname{Sel}_{3^\infty}[3]| = 1$ for all $n$, consistent with $\mu = 0$.

**Curve 37a1** at $p = 3$: $a_3 = -2$, analytic rank 1. The $\lambda$-invariant should be $\geq 1$. At layer $n = 0$: $|\operatorname{Sel}_{3^\infty}(E/\mathbb{Q})[3]| = 1$ (trivial 3-part of Ш). The growth pattern tests $\mu = 0$ vs $\mu > 0$.

## Obstacle Analysis

The fundamental obstacle is that $\mu = 0$ for non-CM curves requires a method that does not use CM structure. Ferrero–Washington's proof uses the fact that the $\mu$-invariant of a $p$-adic CM character vanishes (by the theory of complex multiplication and $p$-adic Hodge theory). In the non-CM case, the analogous statement would follow from the Fontaine–Mazur conjecture (every geometric Galois representation is de Rham) combined with Breuil–Mézard, but these are far from proven. A more accessible strategy might use the fact that $\mu = 0$ is equivalent to the $p$-adic L-function $L_p(E, T)$ having bounded denominators, which can be checked computationally and might be approachable via modularity of $p$-adic L-functions.

## Cross-Group Connections

- **Group A (Main Conjecture):** Greenberg's conjecture is a prerequisite for the Main Conjecture in its strongest form.
- **Group D (Iwasawa Invariants):** Direct computation of $\mu$ and $\lambda$ from the $p$-adic L-function.
- **Group C (Euler Systems):** Euler system bounds on the Selmer group give upper bounds on $\lambda$.
- **Group F (BSD Formula):** Bounded Ш in the tower is a consequence of Greenberg's conjecture.

## Classification

Conjecture
