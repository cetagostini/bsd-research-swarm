# J-008: Arithmetic Topology: Knots and Elliptic Curves

## Direction ID and Title

**J-008:** Arithmetic Topology: Knots and Elliptic Curves

## Status Assessment

**Feasibility:** Low-to-Moderate. This direction is **exploratory** and at the frontier of an active research area (arithmetic topology) that has not yet matured to the point of producing results about BSD. The analogy between 3-manifold topology and number theory is mathematically deep and well-established at the level of definitions (Mazur 1963, Kapranov–Reznikov, Morishita), but it remains primarily a *dictionary of analogies* rather than a *tool for proofs*. No instance is known where the arithmetic topology dictionary has resolved an open problem in the arithmetic of elliptic curves. The direction is classified as **Exploratory/Bridge**: high conceptual reward if the dictionary can be made effective, but very low near-term probability of producing a new proof of rank bounds.

**Current state of the field:** The primes-as-knots dictionary is well-developed for $\operatorname{Spec}(\mathbb{Z})$ and its finite extensions. Key correspondences include:

| Topology | Arithmetic |
|---|---|
| Knot $K \subset S^3$ | Prime $\mathfrak{p} \subset \operatorname{Spec}(\mathcal{O}_K)$ |
| Linking number $\operatorname{lk}(K_i, K_j)$ | Legendre symbol $\left(\frac{p_i}{p_j}\right)$ |
| Alexander polynomial $\Delta_K(t)$ | Iwasawa polynomial $f_p(t)$ |
| Milnor $\bar{\mu}$-invariant | Iwasawa $\mu$-invariant |
| Fundamental group $\pi_1(S^3 \setminus K)$ | Galois group $\operatorname{Gal}(K^{(p)}/K)$ |
| Dehn surgery | $p$-descent / class field theory |

The analog of the Thurston norm for arithmetic schemes has been partially explored by Kurihara and Hiranouchi, but a complete theory analogous to the 3-manifold case does not exist.

## Testable Conjecture or Lemma

**Conjecture (Arithmetic Thurston Bound — Speculative).** *Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, and let $\Sigma$ be a finite set of primes including all primes dividing $N$ and all archimedean places. Consider the "arithmetic 3-manifold" $X_E = \operatorname{Spec}(\mathcal{O}_{E,\Sigma})$ where $\mathcal{O}_{E,\Sigma}$ is the ring of $\Sigma$-integers of the splitting field of the $p$-torsion $E[p]$. Define the arithmetic Thurston norm on the Selmer complex $C^\bullet_{\mathrm{Sel}}(E/\mathbb{Q})$ by:*

$$x_{\mathrm{arith}}([\alpha]) = \min \left\{ \sum_i |\chi(D_i)| : [\alpha] = \partial [D], \; D \in C_3(X_E, \mathbb{Z}) \right\}$$

*where $\chi(D_i)$ denotes the Euler characteristic of the bounding surface, weighted by local ramification data. Then:*

$$\operatorname{rk}(E(\mathbb{Q})) \leq x_{\mathrm{arith}}([\mathrm{Sel}(E/\mathbb{Q})])$$

*with equality when $\text{Sha}(E/\mathbb{Q})$ is finite.*

**Remark.** This is highly speculative. The definition of $x_{\mathrm{arith}}$ is not standard and requires developing the analog of Thurston's theory for the étale cohomological dimension of arithmetic schemes. The inequality, if it could be made precise, would give a *topological* proof of a rank bound—a genuinely new type of argument for BSD.

## Approach Summary

The arithmetic topology approach to BSD proceeds in three conceptual stages:

### Stage 1: Arithmetic 3-Manifold Setup

View $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$ as an "arithmetic 3-manifold" by analogy with $\operatorname{Spec}(\mathcal{O}_K) \leftrightarrow M^3$. For an elliptic curve $E/\mathbb{Q}$, the relevant arithmetic 3-manifold is constructed from:
- The base $\operatorname{Spec}(\mathbb{Z}) \leftrightarrow S^3$
- The splitting field of $E[n]$ for appropriate $n$, viewed as a "covering space"
- Primes of bad reduction as "singular fibers" (Dehn fillings)

### Stage 2: Arithmetic Thurston Norm

On a 3-manifold $M$ with $\partial M \neq \emptyset$, Thurston defined a norm on $H_2(M, \partial M; \mathbb{R})$ by:
$$x([\Sigma]) = \min\{\chi_-(S) : [S] = [\Sigma], \; S \text{ properly embedded}\}$$
where $\chi_-(S) = \sum_{i} \max(0, -\chi(S_i))$. This norm detects incompressible surfaces and bounds the Thurston complexity.

The arithmetic analog replaces:
- Properly embedded surfaces $\to$ Selmer classes (unramified cohomology classes)
- Euler characteristics $\to$ Artin conductors / Swan conductors
- Incompressibility $\to$ minimality of the Selmer representation

### Stage 3: Turaev Torsion as Regulator

The Turaev torsion of a 3-manifold is a refinement of the Reidemeister torsion that detects the Thurston norm ball. If an arithmetic Turaev torsion can be defined for $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$, it could serve as the *arithmetic regulator* mapping:
$$\tau_{\mathrm{arith}}: K_1(\operatorname{Spec}(\mathcal{O}_{E,\Sigma})) \to \mathbb{R}$$
and the leading $L$-value $L^*(E,1)$ could be interpreted as this torsion evaluated on the fundamental class—directly paralleling the Cheeger–Müller theorem.

## Computational Example

### Example 1: The Trefoil Knot and $p = 5$

The trefoil knot $3_1$ in $S^3$ has:
- Alexander polynomial: $\Delta_{3_1}(t) = t^2 - t + 1$
- Arf invariant: 1
- Thurston norm: $x(3_1) = 1$ (fibered knot, fiber genus 1)

The arithmetic analog for $p = 5$: the Iwasawa polynomial of $\mathbb{Q}(\mu_5)$ over $\mathbb{Q}$ has Iwasawa invariants $\lambda_5 = 1, \mu_5 = 0$ by Ferrero–Washington. The Iwasawa $\lambda$-invariant $\lambda = 1$ matches the genus of the trefoil fiber, confirming the Alexander polynomial / Iwasawa polynomial correspondence at this prime.

### Example 2: Linking Numbers and Legendre Symbols

For primes $p = 5, q = 11$:
- Legendre symbol: $\left(\frac{5}{11}\right) = 1$ (since $5^5 = 3125 \equiv 1 \pmod{11}$)
- The arithmetic linking number is 1: these two "arithmetic knots" are linked.

For primes $p = 3, q = 7$:
- Legendre symbol: $\left(\frac{3}{7}\right) = -1$ (since $3^3 = 27 \equiv -1 \pmod{7}$)
- Arithmetic linking number: $-1$.

### Example 3: Arithmetic Thurston Norm for $E: y^2 = x^3 - x$ (conductor 32)

This is the curve 32a1 with rank 0 and trivial $\text{Sha}$. The "knot" associated to the prime 2 (the only bad prime) is a singular point of $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$. The arithmetic Thurston norm should be 0, matching $\operatorname{rk}(E) = 0$.

For $E: y^2 = x^3 - x^2 - 4x + 4$ (conductor 20, rank 1): the arithmetic "surface" bounding the Selmer class should have arithmetic Euler characteristic matching the rank 1.

**Caveat:** These examples are heuristic. The arithmetic Thurston norm is not rigorously defined in the literature, so the computations above are conceptual illustrations of what the theory *should* produce, not verified calculations.

## Obstacle Analysis

### Obstacle 1: No Rigorous Definition of Arithmetic Thurston Norm
The Thurston norm on a 3-manifold uses smooth properly embedded surfaces with well-defined Euler characteristics. The arithmetic analog requires a notion of "arithmetic surface" inside $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$ with an Euler characteristic that encodes rank information. Kurihara's partial definition uses ideal class groups but does not extend to the Selmer group setting. **Severity: Fundamental.**

### Obstacle 2: Analytic Information is Missing from the Dictionary
The arithmetic topology dictionary is entirely algebraic/homological. It captures:
- Linking numbers → Legendre symbols (local, algebraic)
- Alexander polynomials → Iwasawa polynomials (algebraic, $p$-adic)

But it does NOT capture:
- $L$-functions and their analytic continuation
- The functional equation
- Central values $L(E,1)$ or $L'(E,1)$

This is the most fundamental gap. The Cheeger–Müller theorem equates analytic torsion (involving $\zeta$-function determinants) with Reidemeister torsion (topological). Finding the arithmetic analog requires an "analytic torsion" of $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$ that connects to $L(E,s)$. **Severity: Fundamental.**

### Obstacle 3: The Dictionary Breaks Down for $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$
The Mazur dictionary works for $\operatorname{Spec}(\mathcal{O}_K)$ where $K$ is a number field—this is a 1-dimensional arithmetic scheme (Krull dimension 1), analogous to a 3-manifold. But $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$ for an elliptic curve $E$ is naturally a 2-dimensional object (dimension 2 over $\mathbb{Z}$). The analogy $\dim = 1 \leftrightarrow 3\text{-manifold}$ does not extend naturally. One must either:
- Work with a 1-dimensional subscheme (losing elliptic curve information), or
- Develop a dictionary for higher-dimensional arithmetic schemes (largely unexplored). **Severity: High.**

### Obstacle 4: No Transfer Principle
Even if the dictionary is made precise, there is no known mechanism to *transfer* a topological proof (e.g., Thurston's norm bounds) to an arithmetic proof. The dictionary is an analogy, not an equivalence of categories. **Severity: High.**

## Cross-Group Connections

### Group A (Iwasawa Theory)
The most direct connection. The Alexander polynomial / Iwasawa polynomial correspondence is the backbone of arithmetic topology. A-001 (Iwasawa main conjecture) and A-002 ($\mu$-invariants) are directly relevant: the Iwasawa $\mu$-invariant equals the Milnor $\mu$-invariant in the arithmetic topology dictionary. Any progress on the arithmetic Thurston norm would immediately feed back to Iwasawa theory.

### Group B (Euler Systems)
Euler system classes in $H^1_f(G_\Sigma, V)$ can be viewed as "arithmetic curves" in the arithmetic 3-manifold. The Rubin–Kolyvagin duality may have a topological interpretation as Poincaré duality for the arithmetic manifold. B-005 (explicit Euler systems) could provide computational data.

### Group D (Tate–Shafarevich Group)
If $\text{Sha}(E)$ is finite, the arithmetic Thurston norm should equal the analytic rank (conjecture above). The finiteness of $\text{Sha}$ is thus a prerequisite for sharpness. D-001 ($p$-descent and Sha) connects via the Dehn surgery / $p$-descent analogy.

### Group E ($p$-adic Methods)
The $p$-adic Hodge theory perspective provides the "local" arithmetic topology at each prime. E-001 ($p$-adic BSD) and E-006 ($p$-adic regulators) could provide the local data needed for the arithmetic Thurston norm computation.

### Group F (Motivic/Cohomological)
The motivic cohomology groups $H^1_{\mathcal{M}}(\operatorname{Spec}(\mathcal{O}_{E,\Sigma}), \mathbb{Z}(2))$ may serve as the correct coefficient system for the arithmetic Thurston norm. F-001 (motivic cohomology and regulators) is directly relevant.

### Group H (Computational)
H-001 (LMFDB database mining) and H-005 (Selmer group computation) could provide computational verification of arithmetic Thurston norm predictions for specific curves.

### Group I (Connections)
I-001 (Birch–Swinnerton-Dyer over function fields) is relevant because the 3-manifold analogy is much cleaner over function fields (where $\operatorname{Spec}(\mathbb{F}_q[t])$ genuinely is a 3-manifold in the étale topology over $\overline{\mathbb{F}_q}$).

## Classification

- **Risk:** Very High. The direction requires developing entirely new definitions (arithmetic Thurston norm, arithmetic Turaev torsion) that may not exist in a useful form.
- **Reward:** Very High if successful. A topological proof of rank bounds would be a completely new paradigm for BSD, potentially avoiding the analytic difficulties that block the rank $\geq 2$ case.
- **Time horizon:** Long-term (10+ years for any substantive result).
- **Recommendation:** This direction is best pursued as a *theoretical exploration* by experts in both 3-manifold topology and arithmetic geometry. The immediate payoff is conceptual: clarifying the dictionary may suggest new constructions even if it doesn't directly prove BSD. Not suitable for near-term computational attack.
- **Feasibility score:** 2/10 (near-term), 6/10 (long-term if the dictionary matures).
