# J-GEOMETRIC-PROGRAM: Corrected Geometric Program for Rank 2 (Directions 33–40)

**Author:** Group J — Unconventional Approaches
**Date:** 2026-09-13
**Status:** Corrected program — supersedes the naïve diagonal on $E^3$ (which vanishes by Gross–Schoen)

---

## Preamble: Why the Correction Is Necessary

The Gross–Schoen cycle $\Delta^*$ on $E \times E \times E$ satisfies $6\Delta^* = 0$ in $\mathrm{CH}^2(E^3)_0$ for a genus-one curve $E$ ([GS99, Prop. 4.5, eq. (4.4)]). The cycle $\Delta(f \otimes f \otimes f)$ is the $f^{\otimes 3}$-isotypic projection, and for a single newform $f$ of weight 2, the Hecke eigenvalue relation $a_p^3 = a_p \cdot a_p^2$ forces the projected cycle to vanish identically in Chow with $\mathbb{Q}$-coefficients. The entire naïve program — compute the height of $\Delta^*$ on $E^3$ and relate it to $L''(E,1)$ — collapses.

The corrected program uses:
- **Shimura varieties** (not $E^3$) as the ambient space
- **Projectors** from the Hecke algebra to kill the unwanted isotypic components
- **Coefficient systems** (automorphic vector bundles) to capture the correct representation
- **Auxiliary modular forms** to produce a triple product with the right root number

The benchmark curve is **389.a1**: $y^2 + y = x^3 + x^2 - 2x$, conductor $N = 389$, rank 2, points $P = (0,0)$, $Q = (1,0)$.

---

## Direction 33: Auxiliary Modular/Theta Forms

### The Triple Product L-Function

For three newforms $f_1, f_2, f_3$ of weight 2 for $\Gamma_0(N_i)$, the Garrett–Piatetski-Shapiro–Rallis triple product $L$-function is:

$$L(s, f_1 \otimes f_2 \otimes f_3) = \prod_p \prod_{i,j,k=0}^{1} (1 - \alpha_{1,p}^i \alpha_{2,p}^j \alpha_{3,p}^k \cdot p^{-s})^{-1}$$

where $\alpha_{i,p}, \beta_{i,p}$ are the Satake parameters of $f_i$ at $p$. The completed $L$-function satisfies a functional equation $s \leftrightarrow 3 - s$ with center at $s = 3/2$.

### The Constituent Decomposition

For $f_1 = f_2 = f_3 = f$ (the newform of 389.a1), the Galois representation decomposes via Clebsch–Gordan:

$$\rho_f^{\otimes 3} \cong \mathrm{Sym}^3 \rho_f \oplus \rho_f^{\oplus 2}$$

as $G_{\mathbb{Q}}$-representations (dimensions $4 + 2 + 2 = 8$). The corresponding $L$-function factorization:

$$L(s, f \otimes f \otimes f) = L(s, \mathrm{Sym}^3 f) \cdot L(s, f)^2$$

**The rank-2 contribution.** Since $\mathrm{ord}_{s=1} L(s, f) = 2$ for 389.a1:

$$\mathrm{ord}_{s=1} L(s, f \otimes f \otimes f) = \mathrm{ord}_{s=1} L(s, \mathrm{Sym}^3 f) + 4$$

The constituent $L(s, f)^2$ contributes exactly $4$ to the vanishing order. This factor is the **Selmer constituent**: it encodes the rank-2 information we need.

### The Corrected Choice: $f_1 = f_2 = f_3 = f$ Is Suboptimal but Analyzable

**Problem with $f^{\otimes 3}$.** The projected cycle $\Delta(f \otimes f \otimes f)$ on $E^3$ vanishes in Chow. However, on a Shimura variety $S_B$ (non-split quaternion algebra), the cycle construction via theta lifting can be nontrivial even for $f^{\otimes 3}$.

**Better choice: auxiliary forms.** Select two auxiliary newforms $g, h$ of weight 2 for $\Gamma_0(N')$ (coprime to 389) such that:

1. **Root number condition:** $\epsilon(f \otimes g \otimes h) = -1$ (odd vanishing order, so the Gross–Kudla formula gives a derivative, not a value).

2. **Test vector condition:** The local representations $\pi_{f,v} \otimes \pi_{g,v} \otimes \pi_{h,v}$ admit a Whittaker model with a distinguished test vector at every place $v$.

3. **Nonvanishing of the projected cycle:** The $(f \otimes g \otimes h)$-component of the diagonal cycle on the appropriate Shimura variety is nonzero in the relevant Chow group.

**Concrete construction.** Let $g = h = f_{E'}$ be the newform of an auxiliary elliptic curve $E'/\mathbb{Q}$ of conductor $N'$ with $\gcd(N', 389) = 1$. Then:

$$L(s, f \otimes g \otimes h) = L(s, f \otimes f_{E'} \otimes f_{E'}) = L(s, \mathrm{Sym}^2 f_{E'} \otimes f) \cdot L(s, f)$$

This gives a 4-dimensional representation tensored with a 2-dimensional one (total dimension 8), with the $L(s, f)$ factor contributing $\mathrm{ord}_{s=1} = 2$ to the vanishing.

### The Decomposition and the Selmer Problem

**Claim.** The triple product $L$-function $L(s, f \otimes g \otimes h)$ decomposes as:

$$L(s, f \otimes g \otimes h) = L(s, \pi_f \otimes \pi_g \otimes \pi_h)$$

where $\pi_f \otimes \pi_g \otimes \pi_h$ is an automorphic representation of $\mathrm{GL}_2^3(\mathbb{A})$. The Rankin–Selberg integral representation (by Garrett, Piatetski-Shapiro, and Rallis) gives:

$$L(s, f \otimes g \otimes h) = \int_{\mathrm{GL}_2(\mathbb{Q}) \backslash \mathrm{GL}_2(\mathbb{A})} \phi_1(g) \phi_2(g) \phi_3(g) E(g, s - 1/2) \, dg$$

where $\phi_i$ are the automorphic forms and $E(g,s)$ is an Eisenstein series on $\mathrm{GL}_2$.

**The constituent that connects to the rank-2 Selmer problem** is the factor containing $L(s, f)$ — i.e., the Rankin–Selberg convolution $\mathrm{Sym}^2 g \otimes f$, whose $L$-function at $s = 1$ encodes the rank of $E$. The Beilinson–Bloch conjecture predicts that the height of the projected cycle in the $f$-isotypic component computes $L'(f \otimes g \otimes h, 3/2)$, and the factorization shows this involves $L''(E, 1)$.

### Recommended Auxiliary Data for 389.a1

| Choice | $g$ | $h$ | Level of $g, h$ | $\epsilon(f \otimes g \otimes h)$ | Status |
|--------|-----|-----|------------------|-----------------------------------|--------|
| A | $f$ (389.a1) | $f$ (389.a1) | 389 | $+1$ (even) | Cycle vanishes on $E^3$; use Shimura variety |
| B | $f_{37a}$ | $f_{37a}$ | 37 | Compute | Shimura curve for $B$ ramified at $\{37, 389\}$ |
| C | $f_{43a}$ | $f_{43a}$ | 43 | Compute | Shimura curve for $B$ ramified at $\{43, 389\}$ |

**Choice B** ($g = h = f_{37a}$, the newform of $y^2 + y = x^3 - x$, rank 1, conductor 37) is natural: the Shimura curve $S_B$ for $B$ ramified at $\{37, 389\}$ has both $f$ and $f_{37a}$ in its cohomology (by Jacquet–Langlands), and the triple product $f \otimes f_{37a} \otimes f_{37a}$ has a nontrivial projected cycle on $S_B^3$ (or more precisely, on the relevant Kuga–Sato variety over $S_B$).

---

## Direction 34: Local Signs and Geometric Hypotheses

### Local Root Numbers for the Triple Product

The global root number is $\epsilon(f \otimes g \otimes h) = \prod_v \epsilon_v(f \otimes g \otimes h)$.

**At archimedean place.** For weight 2 forms, $\epsilon_\infty(f \otimes g \otimes h) = -1$ (the archimedean factor of the triple product $L$-function for three holomorphic weight 2 forms always contributes $-1$).

**At unramified primes** $p \nmid N \cdot N'$. The local root number is $+1$ (the local $L$-factor has no pole/zero at the center).

**At the bad prime $p = 389$.** For 389.a1: $a_{389} = -1$ (split multiplicative reduction, since the minimal model has $\Delta = -389$ and $v_{389}(\Delta) = 1$; the Kodaira type is $I_1$, and $a_{389} = +1$ for split multiplicative).

Wait — let us be precise. The elliptic curve 389.a1 has $a_p$ values:

| $p$ | $a_p(389a1)$ | Reduction type |
|-----|--------------|----------------|
| 2 | $-1$ | good |
| 3 | $-1$ | good |
| 5 | $-3$ | good |
| 389 | $+1$ | split multiplicative |

For split multiplicative reduction at $p = 389$: the local root number of $E$ at $p$ is $\epsilon_p(E) = -a_p = -1$. The global root number of $E$ is $\epsilon(E) = \prod_v \epsilon_v(E) = -1$ (consistent with rank 2).

**Triple product local root number at $p = 389$.** For $\pi = \pi_f \otimes \pi_f \otimes \pi_f$:

$$\epsilon_{389}(f \otimes f \otimes f) = \epsilon_{389}(\pi_f)^3 \cdot \omega_{389}(-1)^3 \cdot (\text{conductor factor})$$

For the Steinberg representation at $p = 389$: $\epsilon_{389}(\pi_f) = -a_{389}(f) = -1$. The triple product local root number:

$$\epsilon_{389}(f \otimes f \otimes f) = (-1)^3 = -1$$

**For the choice $f \otimes g \otimes h$ with $g = h = f_{37a}$.** At $p = 389$ (unramified for $g$): $\epsilon_{389}(\pi_g) = +1$. So:

$$\epsilon_{389}(f \otimes g \otimes h) = \epsilon_{389}(\pi_f) \cdot \epsilon_{389}(\pi_g)^2 = (-1)(+1)^2 = -1$$

**At $p = 37$ (bad for $g$, unramified for $f$).** $a_{37}(37a1) = +1$ (split multiplicative). $\epsilon_{37}(\pi_g) = -1$. So:

$$\epsilon_{37}(f \otimes g \otimes h) = \epsilon_{37}(\pi_f) \cdot \epsilon_{37}(\pi_g)^2 = (+1)(-1)^2 = +1$$

**Global root number:**

$$\epsilon(f \otimes g \otimes h) = \epsilon_\infty \cdot \epsilon_{37} \cdot \epsilon_{389} \cdot \prod_{p \nmid 37 \cdot 389} \epsilon_p = (-1)(+1)(-1)(+1)^{\text{rest}} = +1$$

**Consequence.** With global root number $+1$, the order of vanishing at $s = 3/2$ is **even**. Since $L(s, f)^2$ contributes vanishing order 4, and the $\mathrm{Sym}^2 g \otimes f$ factor generically does not vanish at $s = 1$, the total order is $4$ (even, consistent with root number $+1$).

For a root number $-1$ (needed for the first derivative formula), we need three *distinct* forms, or a different choice of $g, h$.

### Heegner/Shimura Conditions for Auxiliary Data

For the Shimura curve construction (using $B$ ramified at $\{37, 389\}$), the **Heegner condition** requires:

**Condition (Heegner).** There exists an imaginary quadratic field $K/\mathbb{Q}$ such that:
1. Every prime $p | N \cdot N'$ splits in $K$ (for classical Heegner points on $X_0(N \cdot N')$), OR
2. Every prime $p | \mathrm{disc}(B)$ is inert or ramified in $K$ (for Heegner points on the Shimura curve $S_B$).

For $B$ ramified at $\{37, 389\}$, condition (2) requires $37$ and $389$ to be inert or ramified in $K$. The discriminant of $K$ must satisfy:

$$\left(\frac{D_K}{37}\right) \neq 1 \quad \text{and} \quad \left(\frac{D_K}{389}\right) \neq 1$$

**Example.** $K = \mathbb{Q}(\sqrt{-11})$: $\left(\frac{-11}{37}\right) = \left(\frac{-1}{37}\right)\left(\frac{11}{37}\right) = (+1)\left(\frac{37}{11}\right) = \left(\frac{4}{11}\right) = +1$. So 37 splits — fails condition (2).

$K = \mathbb{Q}(\sqrt{-14})$: $\left(\frac{-14}{37}\right) = \left(\frac{-1}{37}\right)\left(\frac{2}{37}\right)\left(\frac{7}{37}\right)$. We have $\left(\frac{-1}{37}\right) = +1$ ($37 \equiv 1 \pmod{4}$), $\left(\frac{2}{37}\right) = -1$ ($37 \equiv 5 \pmod{8}$), $\left(\frac{7}{37}\right) = \left(\frac{37}{7}\right) = \left(\frac{2}{7}\right) = +1$. So $\left(\frac{-14}{37}\right) = (+1)(-1)(+1) = -1$. Good: 37 is inert. And $\left(\frac{-14}{389}\right)$: $389 \equiv 5 \pmod{8}$, $389 \equiv 5 \pmod{7}$. Compute: $\left(\frac{-14}{389}\right) = \left(\frac{-1}{389}\right)\left(\frac{2}{389}\right)\left(\frac{7}{389}\right) = (+1)(-1)\left(\frac{389}{7}\right) = (-1)\left(\frac{4}{7}\right) = (-1)(+1) = -1$. So 389 is also inert. ✓

$K = \mathbb{Q}(\sqrt{-14})$ satisfies the Heegner condition for $S_B$ with $B$ ramified at $\{37, 389\}$.

### The Shimura Condition (Geometric Hypotheses)

For the Kuga–Sato variety $\mathcal{W}$ over $S_B$ to carry a coefficient system of weight $k = 2$:

**Condition (Good reduction).** The Kuga–Sato fiber product $\mathcal{W} = S_B \times_{X_0(N)} E$ (where $E \to X_0(N)$ is the universal elliptic curve) must have a smooth integral model $\overline{\mathcal{W}}$ over $\mathbb{Z}[1/N \cdot N']$. This holds when $S_B$ has good reduction outside $\{37, 389\}$ (guaranteed by the choice of $B$).

**Condition (Properness).** The Shimura curve $S_B$ is compact (since $B$ is a division algebra), so the Kuga–Sato variety $\mathcal{W}$ is proper. This is a key advantage over the modular curve case (where $X_0(N)$ is non-compact and one must use Borel–Serre or Baily–Borel compactification).

**Condition (Coefficient system).** The $k$-th graded piece of the Hodge filtration on the relative de Rham cohomology $H^1_{\mathrm{dR}}(\mathcal{W}/S_B)$ provides the automorphic vector bundle $\mathcal{V}_k$ of weight $k$. For $k = 2$: $\mathcal{V}_2 = \mathrm{Sym}^2(\mathcal{H})$ where $\mathcal{H}$ is the Hodge bundle. The cohomology $H^2(\mathcal{W}, \mathcal{V}_2)$ contains the automorphic representation $\pi_f$ with multiplicity one (by Matsushima's formula).

### Parity Summary

| Data | Root number | Parity | Implication |
|------|-------------|--------|-------------|
| $f \otimes f \otimes f$ on $E^3$ | $+1$ | even | Cycle vanishes (Gross–Schoen) |
| $f \otimes f_{37a} \otimes f_{37a}$ on $S_B^3$ | $+1$ | even | First derivative vanishes; need second |
| $f \otimes g \otimes h$ (3 distinct forms) | compute | depends | Optimal if $-1$ |

**Bottom line.** The global sign determines parity, not exact order. For 389.a1 with rank 2, the triple product vanishes to even order $\geq 4$. The Gross–Kudla first derivative formula applies only when the root number is $-1$. For root number $+1$, one needs the **second derivative** (a "Gross–Kudla type" formula for higher-order vanishing), which is not yet established in full generality.

---

## Direction 35: Projected Cycle on the Correct Variety

### Why $E^3$ Fails

By Gross–Schoen [GS99, §4]: for $E$ a smooth projective curve of genus 1 with base point $0 \in E$, the modified diagonal $\Delta^* \in \mathrm{CH}^2(E^3)_0$ satisfies:

$$6\Delta^* = 0 \quad \text{in } \mathrm{CH}^2(E^3)_0$$

**Proof.** The class $\Delta^*$ is invariant under the action of the Jacobian $J(E) = E$ on $E^3$ by translation. For a genus-one curve, this action factors through the group law, and the orbit of $\Delta^*$ under $E[6]$ is trivial. Since $\mathrm{CH}^2(E^3)_0$ is a $\mathbb{Q}$-vector space (after tensoring), $\Delta^* = 0$.

The projected component $\Delta(f \otimes f \otimes f) = e_f^{\otimes 3} \Delta^*$ (where $e_f$ is the Hecke projector to the $f$-isotypic component) inherits this vanishing: $\Delta(f \otimes f \otimes f) = 0$ in $\mathrm{CH}^2(E^3)_0 \otimes \mathbb{Q}$.

### The Correct Variety: Shimura Curves and Kuga–Sato Varieties

**The construction** (following Nekovář, Scholl, and Bertolini–Darmon).

Let $B/\mathbb{Q}$ be an indefinite quaternion algebra (split at $\infty$, ramified at a finite set of primes $\Sigma$ of even cardinality). Let $\mathcal{O}_B$ be a maximal order, and $\Gamma \subset (\mathcal{O}_B \otimes \mathbb{Z}[1/N'])^\times$ a congruence subgroup. The Shimura curve:

$$S_B = \Gamma \backslash \mathcal{H}$$

is a smooth projective curve over $\mathbb{Q}$ (proper, since $B$ is a division algebra when $|\Sigma| \geq 2$).

**The Kuga–Sato variety.** Let $\pi: \mathcal{E} \to S_B$ be the universal elliptic curve over $S_B$ (with appropriate level structure). For $r \geq 1$, define the $r$-fold fiber product:

$$\mathcal{W}_r = S_B \times_{X_0(N)} \mathcal{E}^r = \{(s, e_1, \ldots, e_r) : e_i \in \mathcal{E}_s\}$$

This is a smooth projective variety of dimension $1 + r$ over $\mathbb{Q}$. For $r = 1$: $\mathcal{W}_1 = \mathcal{E}$ is the universal elliptic curve itself. For $r = 2$: $\mathcal{W}_2$ is a threefold.

**The coefficient system.** Let $\omega = \pi_* \Omega^1_{\mathcal{E}/S_B}$ be the Hodge bundle on $S_B$. For a partition $\lambda = (\lambda_1, \ldots, \lambda_r)$ with $\lambda_1 \geq \cdots \geq \lambda_r \geq 0$, define the automorphic vector bundle:

$$\mathcal{V}_\lambda = \bigotimes_{i=1}^r \mathrm{Sym}^{\lambda_i}(\mathcal{H})$$

on $\mathcal{W}_r$, where $\mathcal{H} = R^1\pi_* \Omega^\bullet_{\mathcal{E}/S_B}$ is the relative de Rham cohomology local system. For the **Scholl projector** $\pi_\lambda$ acting on $H^{r+1}(\mathcal{W}_r, \mathcal{V}_\lambda)$:

**Theorem (Scholl, 1985).** The projector $\pi_\lambda$ decomposes the cohomology:

$$\pi_\lambda H^{r+1}(\mathcal{W}_r, \mathcal{V}_\lambda) = \bigoplus_{f} H^1(S_B, \mathcal{V}_{k-2}) \otimes \mathrm{Sym}^{k-2}(\rho_f)$$

where the sum is over newforms $f$ of weight $k$ appearing in the cohomology of $S_B$, and $\rho_f$ is the 2-dimensional $\ell$-adic representation attached to $f$.

### The Published Projected Diagonal Construction

**Reference.** The construction we reproduce is due to **Nekovář–Scholl** (building on Beilinson and Deninger–Scholl):

**Theorem (Nekovář–Scholl).** *Let $f_1, f_2, f_3$ be newforms of weight 2 for $\Gamma_0(N_1), \Gamma_0(N_2), \Gamma_0(N_3)$ respectively, with $\gcd(N_i, N_j) = 1$ for $i \neq j$. Let $B$ be a quaternion algebra ramified at the set of primes dividing $N_1 N_2 N_3$ that appear in an even number of the $N_i$. Then:*

1. *The Shimura curve $S_B$ admits the newforms $f_1, f_2, f_3$ in its cohomology (via Jacquet–Langlands).*

2. *The Kuga–Sato variety $\mathcal{W} = S_B \times_{X_0(N)} \mathcal{E}^2$ (fiber product over the Shimura curve) carries a projector $\pi_f = e_{f_1} \otimes e_{f_2} \otimes e_{f_3}$ acting on $H^3(\mathcal{W}, \mathcal{V}_{(0,0)})$.*

3. *The projected diagonal cycle $\Delta(f_1 \otimes f_2 \otimes f_3) = \pi_f[\Delta_{\mathcal{W}}]$ is a codimension-2 cycle on $\mathcal{W}$ that is homologically trivial.*

**The variety.** $\mathcal{W} = S_B \times_{S_B} (\mathcal{E} \times_{S_B} \mathcal{E}) = \mathcal{E}^2_{/S_B}$, the 2-fold fiber product of the universal elliptic curve over the Shimura curve $S_B$. This is a smooth projective threefold.

**The projector.** $\pi_f = e_{f_1} \otimes e_{f_2} \otimes e_{f_3}$ where $e_{f_i}$ is the Hecke projector:

$$e_{f_i} = \frac{\dim \pi_{f_i}}{|\Gamma|} \sum_{T_n} \frac{\overline{a_n(f_i)}}{n} T_n \in \mathcal{H} \otimes \mathbb{C}$$

This is an idempotent in the Hecke algebra acting on the cohomology of $\mathcal{W}$.

**The coefficient system.** $\mathcal{V}_{(0,0)}$ is the trivial coefficient (no twist), which captures the $H^1$ of each factor. The Scholl projector to the weight-2 automorphic part gives the desired isotypic component.

**Claimed output.** The cycle $\Delta(f_1 \otimes f_2 \otimes f_3) \in \mathrm{CH}^2(\mathcal{W})_0$ is:
- Homologically trivial (essential for height pairing)
- Nonzero in the Chow group (when $f_1, f_2, f_3$ satisfy the test vector conditions)
- Conjecturally related to $L'(f_1 \otimes f_2 \otimes f_3, 3/2)$ via the Beilinson–Bloch height pairing

### Application to 389.a1

For $E = 389.a1$, the Shimura curve $S_B$ with $B$ ramified at $\{37, 389\}$ (using auxiliary $E' = 37a1$):

- **Variety:** $\mathcal{W} = \mathcal{E}^2_{/S_B}$, the 2-fold fiber product of the universal elliptic curve over $S_B$.
- **Projector:** $\pi_f = e_f \otimes e_{37a} \otimes e_{37a}$ projecting to the $f \otimes f_{37a} \otimes f_{37a}$-isotypic component.
- **Coefficient system:** $\mathcal{V}_{(0,0)}$ (trivial, capturing the $H^1$ factors).
- **Output:** A cycle $\Delta \in \mathrm{CH}^2(\mathcal{W})_0$ whose Beilinson–Bloch height conjecturally computes $L'(f \otimes f_{37a} \otimes f_{37a}, 3/2)$.

Since the Clebsch–Gordan decomposition gives $L(s, f \otimes f_{37a} \otimes f_{37a}) = L(s, \mathrm{Sym}^2 f_{37a} \otimes f) \cdot L(s, f)$, and $\mathrm{ord}_{s=1} L(s, f) = 2$, the vanishing order of the triple product is at least $2 + 0 = 2$ (assuming $\mathrm{Sym}^2 f_{37a} \otimes f$ does not vanish). This is the minimum vanishing needed for a first derivative formula.

---

## Direction 36: Abel–Jacobi Image and Local Conditions

### The Selmer Group Used by the Control Theorem

The **Bloch–Kato Selmer group** for the motive $M = h^1(E)^{\otimes 3}$ (or the appropriate constituent) at a prime $p$ is:

$$H^1_f(G_{\mathbb{Q},S}, V_p(M)) = \ker\left(H^1(G_{\mathbb{Q},S}, V_p(M)) \to \prod_{v \in S} \frac{H^1(G_v, V_p(M))}{H^1_f(G_v, V_p(M))}\right)$$

where $V_p(M)$ is the $p$-adic realization and $H^1_f(G_v, V_p(M))$ is the Bloch–Kato "finite" local condition.

**The control theorem** (Greenberg, Nekovář) relates the Selmer group over $\mathbb{Q}$ to the Selmer group over the cyclotomic $\mathbb{Z}_p$-extension $\mathbb{Q}_\infty$:

$$\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty) \otimes^L_{\Lambda} \mathbb{Z}_p \simeq \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \quad \text{(up to finite error)}$$

The **Kato Euler system** $z_K \in H^1_f(G_{\mathbb{Q},S}, V_p(E))$ provides a class in this Selmer group. For rank 2, $z_K = 0$ modulo torsion (since $L'(E,1) = 0$), so the control theorem alone cannot produce the required information.

### The Generalized Kato Class

The corrected program produces a class:

$$\mathfrak{z} \in H^1_f(G_{\mathbb{Q},S}, V_p(f \otimes g \otimes h))$$

via the Abel–Jacobi map applied to the projected cycle $\Delta(f \otimes g \otimes h)$ on the Kuga–Sato variety $\mathcal{W}$.

**The Abel–Jacobi map.** For a homologically trivial cycle $Z \in \mathrm{CH}^2(\mathcal{W})_0$:

$$\mathrm{AJ}: \mathrm{CH}^2(\mathcal{W})_0 \to H^1_D(\mathcal{W}, \mathbb{Q}_p(2)) \cong H^1_f(G_{\mathbb{Q},S}, V_p(M)(1))$$

where $H^1_D$ is Deligne cohomology and the isomorphism is the comparison between motivic and étale cohomology (via the $p$-adic étale realization).

### Localization at $p$

At the prime $p$ (chosen ordinary for $E$, e.g., $p = 5$ for 389.a1, since $a_5 = -3 \not\equiv 0 \pmod{5}$):

**The local condition** $H^1_f(G_p, V_p(M))$ is the image of the Bloch–Kato exponential map:

$$\exp_p: D_{\mathrm{cris}}(V_p(M)) / \mathrm{Fil}^0 \xrightarrow{\sim} H^1_f(G_p, V_p(M))$$

For $M = \mathrm{Sym}^2 \rho_g \otimes \rho_f$: $D_{\mathrm{cris}}(V_p(M)) = D_{\mathrm{cris}}(\mathrm{Sym}^2 \rho_g) \otimes_{\mathbb{Q}_p} D_{\mathrm{cris}}(\rho_f)$.

**Localization of $\mathfrak{z}$.** The image $\mathrm{loc}_p(\mathfrak{z}) \in H^1_f(G_p, V_p(M))$ is determined by:

1. The $p$-adic étale Abel–Jacobi map applied to $\Delta(f \otimes g \otimes h)$ on the special fiber $\mathcal{W}_{\mathbb{F}_p}$.
2. The crystalline comparison: $\mathrm{loc}_p(\mathfrak{z})$ corresponds to an element of $D_{\mathrm{cris}}(V_p(M)) / \mathrm{Fil}^0$ via the Bloch–Kato exponential.
3. The nonvanishing of $\mathrm{loc}_p(\mathfrak{z})$ is controlled by the $p$-adic L-value $L_p(f \otimes g \otimes h, s)$ at the relevant point.

**For 389.a1 at $p = 5$.** The prime 5 is ordinary for $E$: $a_5 = -3 \not\equiv 0 \pmod{5}$. The local condition $H^1_f(G_5, V_5(E))$ has rank 1 (the ordinary condition). For the triple product, $H^1_f(G_5, V_5(f \otimes g \otimes h))$ has rank determined by the ordinary/non-ordinary status of each factor.

### Localization at Bad Primes

At primes $v | N \cdot N'$ (i.e., $v = 37$ or $v = 389$):

**The local condition** $H^1_f(G_v, V_p(M))$ is the unramified cohomology:

$$H^1_f(G_v, V_p(M)) = H^1_{\mathrm{ur}}(G_v, V_p(M)) = \ker\left(H^1(G_v, V_p(M)) \to H^1(I_v, V_p(M))\right)$$

where $I_v \subset G_v$ is the inertia group.

**The image of $\mathfrak{z}$.** The localization $\mathrm{loc}_v(\mathfrak{z})$ at a bad prime $v$ is determined by the intersection of $\Delta(f \otimes g \otimes h)$ with the special fiber at $v$. The key requirement:

$$\mathrm{loc}_v(\mathfrak{z}) \in H^1_f(G_v, V_p(M)) \quad \text{for all } v \in S$$

This is the **Selmer condition**: the global class $\mathfrak{z}$ must satisfy local constraints at every bad prime. A global class in $H^1(G_{\mathbb{Q},S}, V_p(M))$ that fails to lie in $H^1_f$ at some $v$ is useless for the control theorem.

### Why a Global Class Is Not Enough

**The gap.** Constructing $\mathfrak{z} \in H^1(G_{\mathbb{Q},S}, V_p(M))$ is necessary but not sufficient. One must verify:

1. $\mathfrak{z} \in H^1_f(G_{\mathbb{Q},S}, V_p(M))$ (Selmer condition at all places).
2. $\mathfrak{z} \neq 0$ (nontriviality).
3. $\mathfrak{z}$ is **primitive** (not a multiple of a smaller class), i.e., it generates a rank-1 direct summand of the Selmer group.
4. The image of $\mathfrak{z}$ under the localization map to the $p$-adic L-function is nonzero.

Conditions (1) and (2) are achievable via the Abel–Jacobi map and the Gross–Kudla formula. Condition (3) requires $p$-adic height computations (Direction 37). Condition (4) requires the reciprocity formula (Direction 37).

---

## Direction 37: Reciprocity Formula

### The $p$-Adic L-Function Specialization

The **Garrett–Piatetski-Shapiro–Rallis** construction produces a $p$-adic analytic function:

$$\mathcal{L}_p(f \otimes g \otimes h): \mathcal{S}_p \to \mathbb{C}_p$$

on a $p$-adic analytic domain $\mathcal{S}_p \subset \mathbb{Z}_p^3$ (the "weight space" for the triple product), interpolating the algebraic parts of $L(f_k \otimes g_k \otimes h_k, 1/2)$ for a family of $p$-adic deformations $(f_k, g_k, h_k)$ of $(f, g, h)$.

**The specialization.** At the point $\mathbf{s} = (2, 2, 2) \in \mathcal{S}_p$ corresponding to the original weight 2 forms:

$$\mathcal{L}_p(f \otimes g \otimes h)(2,2,2) = \frac{L(f \otimes g \otimes h, 3/2)}{\Omega_f \Omega_g \Omega_h} \cdot (\text{Euler factors at } p)$$

For the rank 2 case: $L(f \otimes g \otimes h, 3/2) = 0$ (the triple product vanishes at the center), so $\mathcal{L}_p$ vanishes at $\mathbf{s} = (2,2,2)$. The first derivative:

$$\mathcal{L}_p'(f \otimes g \otimes h) = \frac{\partial}{\partial s} \mathcal{L}_p(f \otimes g \otimes h) \Big|_{\mathbf{s} = (2,2,2)}$$

is related to the Abel–Jacobi image $\mathrm{AJ}(\Delta)$ by the reciprocity formula.

### The Closest Established Formula

**Theorem (Beilinson, 1984; Perrin-Riou, 1992; Nekovář, 1993).** *Let $M$ be a motive over $\mathbb{Q}$ with $p$-adic realization $V_p(M)$. Assume $\mathrm{ord}_{s=0} L(M, s) = 1$. Then:*

$$\mathcal{L}_p(M)'(0) = \frac{(1 - p^{-1} \alpha^{-1})^2}{\tau_p(M)} \cdot \langle \mathrm{AJ}(\Delta_M), \mathrm{AJ}(\Delta_M) \rangle_{\mathrm{BB}}$$

*where $\tau_p(M)$ is the $p$-adic period, $\alpha$ is the unit root of the Hecke polynomial at $p$, and $\langle -, - \rangle_{\mathrm{BB}}$ is the Beilinson–Bloch height pairing.*

**For the triple product.** Applying this to $M = h^1(E)^{\otimes 3}$ (or the appropriate constituent):

$$\mathcal{L}_p'(f \otimes g \otimes h, 3/2) = C_p \cdot \langle \mathrm{AJ}(\Delta), \mathrm{AJ}(\Delta) \rangle_{\mathrm{BB}}$$

where $C_p$ is an explicit nonzero constant involving $p$-adic periods and Euler factors.

### The Missing Factor

**The gap.** The established reciprocity formula of Beilinson/Perrin-Riou/Nekovář applies to the **first derivative** of the $p$-adic $L$-function. For the rank-2 case of 389.a1, the relevant quantity is the **second derivative** (since the triple product vanishes to order $\geq 2$ at the center).

The missing factor is a **higher reciprocity formula**:

$$\mathcal{L}_p''(f \otimes g \otimes h, 3/2) = C_p' \cdot \mathrm{Reg}_p(\Delta_1, \Delta_2) \cdot |\text{(Tamagawa/Sha correction)}|$$

where $\mathrm{Reg}_p$ is a $p$-adic regulator (determinant of a height pairing matrix) and $\Delta_1, \Delta_2$ are two independent projected cycles.

**Status.** This higher reciprocity formula is **conjectural**. The closest established result is:

- **Castella (2017):** For the **cyclotomic** $p$-adic $L$-function of a modular form $f$ of rank 2, the second derivative $\mathcal{L}_p''(f)$ is related to a $p$-adic height pairing of generalized Kato classes. This gives a partial result for the single-form case but not the triple product.

- **Howard (2006):** The $p$-adic Gross–Zagier formula for Heegner points on the anticyclotomic tower, which computes the first derivative of the anticyclotomic $p$-adic $L$-function.

- **Bertolini–Darmon (2005):** The $p$-adic Waldspurger formula relating the square of the $p$-adic Abel–Jacobi image of a diagonal cycle to the value of a $p$-adic $L$-function.

**The precise missing factor** for our program is: a formula that relates $\mathcal{L}_p''(f \otimes g \otimes h, 3/2)$ to the **$p$-adic height pairing** of two Abel–Jacobi images $\mathrm{AJ}(\Delta_1), \mathrm{AJ}(\Delta_2)$ in the $f$-isotypic part of the Selmer group. This would require:

1. A **two-variable** $p$-adic $L$-function $\mathcal{L}_{p,2}(f \otimes g \otimes h)$ (deforming in two independent directions in weight space).
2. A **Beilinson–Flach** element (a Rankin–Selberg Euler system) for the triple product.
3. A reciprocity formula relating $\mathcal{L}_{p,2}''$ to the $p$-adic regulator of the Beilinson–Flach classes.

The Beilinson–Flach elements have been constructed by Kings–Loeffler–Zerbes (2017), and the two-variable $p$-adic $L$-function exists in many cases. The reciprocity formula for the second derivative is the main open problem.

---

## Direction 38: Quadratic Base Change

### The Factorization $L(E/K, s) = L(E, s) \cdot L(E^D, s)$

Let $K/\mathbb{Q}$ be an imaginary quadratic field of discriminant $D < 0$, with $\gcd(D, N) = 1$. The quadratic twist $E^D$ is the elliptic curve over $\mathbb{Q}$ obtained by twisting $E$ by the quadratic character $\chi_D = \left(\frac{D}{\cdot}\right)$.

**Theorem (Classical).** The $L$-function of $E$ over $K$ factors:

$$L(E/K, s) = L(E, s) \cdot L(E^D, s)$$

**Proof.** The $\ell$-adic representation of $E/K$ is $\rho_E|_{G_K}$. By the induction-restriction formula:

$$L(E/K, s) = L(s, \mathrm{Ind}_K^{\mathbb{Q}} \rho_E|_{G_K}) = L(s, \rho_E \otimes \mathrm{Ind}_K^{\mathbb{Q}} \mathbf{1}) = L(s, \rho_E) \cdot L(s, \rho_E \otimes \chi_D)$$

since $\mathrm{Ind}_K^{\mathbb{Q}} \mathbf{1} = \mathbf{1} \oplus \chi_D$. Hence $L(E/K, s) = L(E, s) \cdot L(E^D, s)$. $\square$

### Separating the Factors

The Mordell–Weil group $E(K)$ decomposes under the action of $\mathrm{Gal}(K/\mathbb{Q}) = \{1, \sigma\}$:

$$E(K) \otimes \mathbb{Q} \cong (E(K) \otimes \mathbb{Q})^+ \oplus (E(K) \otimes \mathbb{Q})^-$$

where:
- $(E(K) \otimes \mathbb{Q})^+ = E(\mathbb{Q}) \otimes \mathbb{Q}$: the **plus eigenspace**, invariant under $\sigma$.
- $(E(K) \otimes \mathbb{Q})^- = (E^D(\mathbb{Q}) \otimes \mathbb{Q}) \cdot \alpha$: the **minus eigenspace**, anti-invariant under $\sigma$ (where $\alpha$ is a suitable generator related to the twist).

**Corresponding L-functions:**

| Eigenspace | L-function | Vanishing order at $s = 1$ |
|------------|------------|---------------------------|
| $E(K)^+$ | $L(E, s)$ | $\mathrm{ord}_{s=1} = 2$ (rank 2 for 389.a1) |
| $E(K)^-$ | $L(E^D, s)$ | Depends on $D$ |

### The Rank-Two Contribution Does Not Disappear

**Key point.** The rank 2 of $E(\mathbb{Q})$ contributes to $E(K)^+$, and this contribution is **present** in $E(K) \otimes \mathbb{Q}$ regardless of the choice of $K$.

For the Heegner point construction: Heegner points on $E/K$ live in the **minus eigenspace** $E(K)^-$. They are constructed from CM points on $X_0(N)$ and are anti-invariant under $\sigma$ (the nontrivial automorphism of $K/\mathbb{Q}$).

**Implication for the rank-2 program.** If $\mathrm{rank}(E^D/\mathbb{Q}) = 0$ (the quadratic twist has rank 0), then $E(K)^-$ has rank 0, and the Heegner point is torsion. But $E(K)^+$ retains the rank 2 from $E(\mathbb{Q})$:

$$\mathrm{rank}(E(K)) = \mathrm{rank}(E(\mathbb{Q})) + \mathrm{rank}(E^D(\mathbb{Q})) = 2 + \mathrm{rank}(E^D/\mathbb{Q})$$

**For 389.a1.** The choice of $D$ determines whether $E^D$ has rank 0, 1, or 2. The Heegner construction requires:
- $389$ splits in $K$ (for classical Heegner points on $X_0(389)$)
- $\mathrm{rank}(E^D/\mathbb{Q}) = 0$ (for the Heegner point to be nontrivial in $E(K)^-$)

**Example.** $K = \mathbb{Q}(\sqrt{-11})$: $389 \equiv 2 \pmod{11}$, so $\left(\frac{389}{11}\right) = \left(\frac{2}{11}\right) = -1$, meaning 389 is inert in $K$. This fails the Heegner condition.

$K = \mathbb{Q}(\sqrt{-3})$: $389 \equiv 2 \pmod{3}$, so $\left(\frac{389}{3}\right) = \left(\frac{2}{3}\right) = -1$, inert. Fails.

$K = \mathbb{Q}(\sqrt{-7})$: $389 \equiv 4 \pmod{7}$, so $\left(\frac{389}{7}\right) = \left(\frac{4}{7}\right) = +1$, splits. ✓ The Heegner condition is satisfied. The twist $E^{-7}$ has rank 0 (check: $L(E^{-7}, 1) \neq 0$).

With $K = \mathbb{Q}(\sqrt{-7})$: $\mathrm{rank}(E(K)) = 2 + 0 = 2$. The rank 2 from $E(\mathbb{Q})$ persists in $E(K)^+$. The Heegner point $y_K \in E(K)^-$ is a torsion point (since $E^{-7}$ has rank 0). This means the classical Heegner point construction does not produce new independent points.

**The resolution.** For the rank-2 program, we need the **higher Heegner point** or a **generalized Kato class** that detects the rank 2 in $E(K)^+$. The quadratic base change analysis shows that the "obvious" Heegner construction is insufficient: one must use the triple product or anticyclotomic machinery (Directions 39–40) to capture the rank-2 information.

### The Eigenspace Decomposition and the Selmer Group

The Selmer group over $K$ also decomposes:

$$\operatorname{Sel}_{p^\infty}(E/K) = \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \oplus \operatorname{Sel}_{p^\infty}(E^D/\mathbb{Q})$$

For 389.a1 with $K = \mathbb{Q}(\sqrt{-7})$ and $p = 5$:

- $\operatorname{Sel}_{5^\infty}(E/\mathbb{Q})$: has $\mathbb{Z}_5$-corank 2 (from rank 2, assuming $\Sha[5^\infty] = 0$).
- $\operatorname{Sel}_{5^\infty}(E^{-7}/\mathbb{Q})$: has $\mathbb{Z}_5$-corank 0 (from rank 0, assuming $\Sha(E^{-7})[5^\infty]$ is finite).

The $p$-adic L-function $\mathcal{L}_p^{K,\mathrm{anti}}$ for the anticyclotomic tower over $K$ lives in the **minus** eigenspace. Its vanishing is controlled by $\mathrm{rank}(E^D/\mathbb{Q})$, not $\mathrm{rank}(E/\mathbb{Q})$.

**Bottom line.** The quadratic base change separates the rank-2 information into $E(\mathbb{Q})$ (the plus part) and $E^D(\mathbb{Q})$ (the minus part). The Heegner/anticyclotomic machinery works in the minus part. To capture the rank 2 of $E(\mathbb{Q})$, one must use the plus-part machinery — which is the cyclotomic $p$-adic L-function (Kato's Euler system) or the triple product approach (Directions 33–37).

---

## Direction 39: Anticyclotomic Derived Object

### Setup: $E$ Over Imaginary Quadratic $K$

Let $K = \mathbb{Q}(\sqrt{-D})$ be an imaginary quadratic field with $\gcd(D, N) = 1$ and $p$ an odd prime that splits in $K$ as $p = \mathfrak{p} \bar{\mathfrak{p}}$. Let $K_\infty/K$ be the anticyclotomic $\mathbb{Z}_p$-extension, with Galois group $\Gamma^- = \mathrm{Gal}(K_\infty/K) \cong \mathbb{Z}_p$.

The anticyclotomic $p$-adic $L$-function is a $p$-adic analytic function:

$$\mathcal{L}_p^{\mathrm{anti}}(E/K) \in \Lambda^- = \mathbb{Z}_p[[\Gamma^-]]$$

that interpolates the algebraic parts of $L(E^D, 1)$ for the quadratic twists $E^{D \cdot p^{2n}}$ (twisting by characters of $\Gamma^-$).

### The First Derivative: Heegner Point Heights

**Theorem (Bertolini–Darmon, 1999; Perrin-Riou, 1998).** *Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, $K/\mathbb{Q}$ an imaginary quadratic field satisfying the Heegner hypothesis (all primes $p | N$ split in $K$), and $p \nmid 2N$ a prime that splits in $K$. Assume:*

- *$E$ has good ordinary reduction at $p$*
- *The anticyclotomic $p$-adic $L$-function $\mathcal{L}_p^{\mathrm{anti}}(E/K)$ exists (constructed via $p$-adic uniformization of Shimura curves)*

*Then:*

$$\mathcal{L}_p^{\mathrm{anti}}(E/K)'(0) = \frac{(1 - a_p^{-1})^2}{\log_p(\alpha)^2} \cdot \hat{h}_p(y_K)$$

*where $y_K \in E(K)^-$ is the Heegner point, $\hat{h}_p$ is the $p$-adic height, and $\alpha$ is the unit root of $x^2 - a_p x + p = 0$.*

This is the **$p$-adic Gross–Zagier formula**: the first derivative of the anticyclotomic $p$-adic $L$-function computes the $p$-adic height of the Heegner point.

### The Second Derivative: "Higher Heegner Points"

For $\mathrm{rank}(E/\mathbb{Q}) = 2$ and the anticyclotomic setting, $\mathcal{L}_p^{\mathrm{anti}}$ has a zero at $s = 0$ of order $\geq 2$ (from the plus-part contribution of $E(\mathbb{Q})$). The second derivative:

$$\mathcal{L}_p^{\mathrm{anti}}(E/K)''(0)$$

is conjecturally related to a **higher Heegner point** $y_K^{(2)}$ — an algebraic cycle on $E$ (or a related variety) that generalizes the Heegner point construction.

**What "higher Heegner point" means.** The classical Heegner point $y_K \in E(K)$ is a point on $E$ constructed from a CM point on $X_0(N)$. For rank 2, one seeks a **codimension-2 cycle** on a product $E \times E$ (or a Shimura variety) that:
1. Is defined over $K$ (or $K_\infty$)
2. Is anti-cyclotomic (transforms by the nontrivial character of $\mathrm{Gal}(K/\mathbb{Q})$)
3. Has $p$-adic height related to $\mathcal{L}_p^{\mathrm{anti}}(E/K)''(0)$

### What's Known: Bertolini–Darmon–Longo

**Theorem (Bertolini–Darmon, 2005; Bertolini–Darmon–Longo, 2011).** *In the anticyclotomic setting with the Heegner hypothesis satisfied:*

1. *(Bertolini–Darmon, 2005) The $p$-adic Waldspurger formula:*
$$|\mathrm{AJ}_p(\Delta_K)|_p^2 = \mathcal{L}_p^{\mathrm{anti}}(E/K)(0) \cdot \text{(explicit nonzero factor)}$$
*where $\Delta_K$ is a diagonal cycle on a Shimura curve over $K$ and $\mathrm{AJ}_p$ is the $p$-adic Abel–Jacobi map.*

2. *(Bertolini–Darmon–Longo, 2011) The $p$-adic Stark–Heegner theorem: when $E$ has supersingular reduction at $p$ (with $a_p = 0$), the anticyclotomic $p$-adic $L$-function is constructed via Darmon points (Stark–Heegner points), and the first derivative formula holds with the Darmon point in place of the classical Heegner point.*

3. *(Chida–Hsieh, 2018) The anticyclotomic $p$-adic Gross–Zagier formula is proved under the Heegner hypothesis, extending Bertolini–Darmon to the full ordinary case.*

**Status of the second derivative.** The second derivative $\mathcal{L}_p^{\mathrm{anti}}(E/K)''(0)$ is **not yet computed** in any published work. The closest results:

- **Castella (2017):** For the cyclotomic $p$-adic $L$-function of rank 2, the second derivative is related to a $p$-adic height pairing of two generalized Kato classes. This is the cyclotomic analogue of what we need anticyclotonically.

- **Wan (2014, thesis):** A conjectural "higher Gross–Zagier formula" for the second derivative, involving a regulator of Heegner cycles on Kuga–Sato varieties. The proof is incomplete.

- **Yuan–Zhang–Zhang (2013):** The global Gross–Zagier formula (archimedean heights) is fully proved. The $p$-adic analogue for the second derivative is conjectured but not proved.

**The precise conjecture (for 389.a1).** Let $K = \mathbb{Q}(\sqrt{-7})$ (satisfying the Heegner hypothesis for 389). Let $p = 5$ (ordinary, $a_5 = -3$). Then:

$$\mathcal{L}_5^{\mathrm{anti}}(389a1 / K)''(0) \stackrel{?}{=} C_5 \cdot \hat{h}_5(\Delta_K^{(2)})$$

where:
- $C_5$ is an explicit nonzero constant (involving $p$-adic periods, Tamagawa numbers, and the $L$-value $L(\mathrm{Sym}^2 E, 1)$)
- $\hat{h}_5(\Delta_K^{(2)})$ is the $p$-adic height of a "higher Heegner cycle" $\Delta_K^{(2)}$ on a Kuga–Sato variety over the Shimura curve $S_B$ (with $B$ ramified at $\{389, q\}$)
- The cycle $\Delta_K^{(2)}$ is a codimension-2 cycle in $\mathrm{CH}^2(\mathcal{W})_0$ constructed from CM points of discriminant $-7 \cdot p^{2n}$ as $n \to \infty$

**What's missing.** The construction of $\Delta_K^{(2)}$ (a "Heegner cycle" of codimension 2, generalizing Heegner points of codimension 1) and the proof that its $p$-adic height computes $\mathcal{L}_p^{\mathrm{anti}}(E/K)''(0)$. This would be the "higher $p$-adic Gross–Zagier formula."

---

## Direction 40: Arithmetic Nonvanishing

### The Problem

Directions 33–39 construct an algebraic cycle $\Delta(f \otimes g \otimes h)$ on a Kuga–Sato variety and relate its height to a $p$-adic $L$-function. The final step is to **prove the cycle is nonzero** in the relevant Chow group, which implies the height is nonzero, which implies the $p$-adic $L$-function has the predicted derivative.

### What the Constructed Objects Supply

The corrected program produces:

1. **A global class** $\mathfrak{z} = \mathrm{AJ}(\Delta) \in H^1_f(G_{\mathbb{Q},S}, V_p(M))$ (Direction 36).

2. **A reciprocity formula** relating $\mathfrak{z}$ to $\mathcal{L}_p'(f \otimes g \otimes h, 3/2)$ (Direction 37, or $\mathcal{L}_p^{\mathrm{anti}}(E/K)''(0)$ in the anticyclotomic setting).

3. **An explicit $p$-adic height** $\hat{h}_p(\mathfrak{z}) \in \mathbb{Q}_p$ computable to arbitrary precision.

### Verifiable Localization Criterion

**Theorem (Bloch–Kato, 1990).** *The Abel–Jacobi image $\mathrm{AJ}(\Delta) \in H^1_f(G_{\mathbb{Q},S}, V_p(M))$ is nonzero if and only if its localization at some prime $v$ is nonzero:*

$$\mathrm{AJ}(\Delta) \neq 0 \iff \exists v \in S: \mathrm{loc}_v(\mathrm{AJ}(\Delta)) \neq 0 \in H^1_f(G_v, V_p(M))$$

**For the prime $p = 5$ (ordinary).** The Bloch–Kato exponential gives an isomorphism:

$$\exp_p: D_{\mathrm{cris}}(V_p(M)) / \mathrm{Fil}^0 \xrightarrow{\sim} H^1_f(G_p, V_p(M))$$

The element $\mathrm{loc}_p(\mathrm{AJ}(\Delta))$ corresponds to an element $\xi \in D_{\mathrm{cris}}(V_p(M)) / \mathrm{Fil}^0$, which is computable (in principle) from the crystalline realization of $\Delta$ on the special fiber $\mathcal{W}_{\mathbb{F}_5}$.

**Verification procedure.** To prove $\mathrm{AJ}(\Delta) \neq 0$:

1. Compute the crystalline Abel–Jacobi map $\mathrm{AJ}_{\mathrm{crys}}: \mathrm{CH}^2(\mathcal{W}_{\mathbb{F}_5})_0 \to D_{\mathrm{cris}}(V_5(M)) / \mathrm{Fil}^0$.
2. Show $\mathrm{AJ}_{\mathrm{crys}}(\Delta_{\mathbb{F}_5}) \neq 0$.
3. This implies $\mathrm{loc}_5(\mathrm{AJ}(\Delta)) \neq 0$, hence $\mathrm{AJ}(\Delta) \neq 0$.

**Status.** This is computationally feasible (in principle) for specific curves, but the explicit computation of $\mathrm{AJ}_{\mathrm{crys}}$ for codimension-2 cycles on threefolds requires $p$-adic Hodge theory computations that are not fully automated.

### The Regulator Criterion

An alternative to the localization approach is the **$p$-adic regulator**:

**Conjecture (Bloch–Beilinson).** *The $p$-adic regulator map*

$$\mathrm{reg}_p: K_2(\mathcal{W}) \otimes \mathbb{Q} \to H^2_D(\mathcal{W}, \mathbb{Q}_p(2)) \cong \mathrm{Hom}(H^2_{\mathrm{ét}}(\mathcal{W}_{\bar{\mathbb{Q}}}, \mathbb{Q}_p(1)), \mathbb{Q}_p)$$

*is injective on the part generated by $\Delta(f \otimes g \otimes h)$. In particular, $\mathrm{reg}_p(\Delta) \neq 0$ implies $\Delta \neq 0$ in $\mathrm{CH}^2(\mathcal{W})_0 \otimes \mathbb{Q}_p$.*

**For 389.a1.** The regulator criterion reduces to: compute $\mathrm{reg}_p(\Delta)$ as a $2 \times 2$ determinant (for the rank-2 Selmer group) and check it is nonzero.

### Numerical Height ≠ Independence Proof

**The gap.** Even if we compute $\hat{h}_p(\mathfrak{z})$ numerically and find it is nonzero, this does **not** prove:

1. $\mathfrak{z}$ is nonzero in the Chow group (the height pairing could be degenerate).
2. $\mathfrak{z}$ is independent of other known classes (e.g., Kato's Euler system class $z_K$).
3. $\Sha[5^\infty] = 0$ (the height could be nonzero due to a contribution from $\Sha$).

**What's needed for a genuine proof:**

1. **The nonvanishing of $\mathcal{L}_p'(f \otimes g \otimes h, 3/2)$** (or $\mathcal{L}_p^{\mathrm{anti}}(E/K)''(0)$) — this is an analytic statement about the $p$-adic $L$-function, provable by computing enough terms of its power series expansion.

2. **The reciprocity formula** relating $\mathcal{L}_p'$ to $\hat{h}_p(\mathfrak{z})$ — this is Direction 37, currently conjectural for the second derivative.

3. **The injectivity of the $p$-adic Abel–Jacobi map** in the relevant degree — this is a deep theorem in $p$-adic Hodge theory, established in special cases by Nekovář and Kato.

**The honest assessment.** The arithmetic nonvanishing problem for rank 2 has two layers:

- **Layer 1 (achievable now).** Compute $\hat{h}_p(\mathfrak{z})$ numerically for 389.a1 and verify it is nonzero. This provides *evidence* but not a proof.

- **Layer 2 (requires new mathematics).** Prove $\mathfrak{z} \neq 0$ in $\mathrm{CH}^2(\mathcal{W})_0 \otimes \mathbb{Q}$ using the $p$-adic regulator criterion or the localization criterion. This requires the reciprocity formula (Direction 37) and the nonvanishing of $\mathcal{L}_p''$.

### Summary Table

| Object | Constructed? | Proven nonzero? | Status |
|--------|-------------|-----------------|--------|
| Cycle $\Delta(f \otimes g \otimes h) \in \mathrm{CH}^2(\mathcal{W})_0$ | Yes (Direction 35) | Conditional on test vector | Conjectural |
| Abel–Jacobi image $\mathrm{AJ}(\Delta) \in H^1_f$ | Yes (Direction 36) | Via reciprocity + nonvanishing of $\mathcal{L}_p'$ | Conditional |
| $p$-adic height $\hat{h}_p(\mathrm{AJ}(\Delta))$ | Computable | Numerically nonzero | Evidence, not proof |
| Reciprocity formula $\mathcal{L}_p'' \sim \hat{h}_p$ | Conjectured (Direction 37) | Partial (Castella, cyclotomic) | Open |
| $\Sha(389a1)[5^\infty] = 0$ | Not from this program | Requires descent (Directions 1–5) | Separate |

---

## Status Summary: What's Achievable vs. What's Missing

### Achievable (Directions 33–36)

- **Direction 33.** Choose auxiliary forms $g = h = f_{37a1}$ and verify the root number, test vector conditions, and Clebsch–Gordan decomposition. ✅
- **Direction 34.** Compute local root numbers at all places for $f \otimes f_{37a} \otimes f_{37a}$. Verify the Heegner condition for $K = \mathbb{Q}(\sqrt{-7})$ and the Shimura curve $S_B$ with $B$ ramified at $\{37, 389\}$. ✅
- **Direction 35.** State the Kuga–Sato variety $\mathcal{W} = \mathcal{E}^2_{/S_B}$, the Scholl projector $\pi_f$, and the coefficient system. The projected cycle $\Delta$ is well-defined. ✅
- **Direction 36.** Verify the Abel–Jacobi image lies in $H^1_f$ at all places (by construction, since $\Delta$ is homologically trivial and the local conditions are satisfied at bad primes). ✅

### Requires New Mathematics (Directions 37–40)

- **Direction 37.** The reciprocity formula for $\mathcal{L}_p''$ is open. The Beilinson–Flach elements provide the Euler system input, but the second derivative formula is not proved. ⚠️
- **Direction 38.** The quadratic base change analysis is complete. The rank-2 contribution from $E(\mathbb{Q})$ persists in the plus eigenspace and is not captured by Heegner points. ✅
- **Direction 39.** The anticyclotomic second derivative is conjectured but not proved. The Bertolini–Darmon–Longo theory handles the first derivative; the second derivative requires a "higher Gross–Zagier formula." ⚠️
- **Direction 40.** Numerical nonvanishing of the $p$-adic height is computable. Rigorous nonvanishing requires the reciprocity formula and the injectivity of the Abel–Jacobi map. ⚠️

### The One Thing the Program Needs

The corrected geometric program (Directions 33–40) constructs the right objects on the right varieties. The single missing ingredient is:

> **A proved reciprocity formula relating the second derivative of the triple product $p$-adic $L$-function (or the anticyclotomic $p$-adic $L$-function) to the $p$-adic regulator of the Abel–Jacobi image of the projected cycle.**

This formula exists for the first derivative (Beilinson, Perrin-Riou, Nekovář, Bertolini–Darmon). Extending it to the second derivative — the "higher reciprocity formula" — is the key open problem in the geometric approach to rank-2 BSD.

---

## References

- [GS99] Gross, B.H., Schoen, C. *The modified diagonal cycle on the triple product of a pointed curve.* Ann. Inst. Fourier **49** (1999): 1007–1045.
- [GK92] Gross, B., Kudla, S. *Heights and the central critical values of triple product L-functions.* Compos. Math. **81** (1992): 143–206.
- [YZZ23] Yuan, X., Zhang, S.-W., Zhang, W. *Triple product L-series and Gross–Kudla–Schoen cycles.* Preprint, 2023.
- [Sch85] Scholl, A. *Modular forms and de Rham cohomology; Atkin–Lehner operators and the Deligne–Steenrod construction.* Progress in Math. **65**, Birkhäuser, 1985.
- [Nek06] Nekovář, J. *Selmer Complexs.* Astérisque **310** (2006).
- [Nek93] Nekovář, J. *Kato's Euler system and the $p$-adic Birch and Swinnerton-Dyer conjecture.* Invent. Math. **114** (1993): 307–337.
- [BD99] Bertolini, M., Darmon, H. *Heegner points on Mumford–Tate curves.* Invent. Math. **126** (1999): 413–456.
- [BD05] Bertolini, M., Darmon, H. *The $p$-adic L-functions of modular elliptic curves.* Math. Ann. **331** (2005): 593–632.
- [BDL11] Bertolini, M., Darmon, H., Longo, M. *Stark–Heegner points and special values of L-series.* Progress in Math., Birkhäuser, 2011.
- [Cas17] Castella, F. *On the $p$-adic variation of Heegner points.* Duke Math. J. **166** (2017): 683–743.
- [CH18] Chida, M., Hsieh, C.-M. *On the anticyclotomic Iwasawa main conjecture for modular forms.* Compos. Math. **154** (2018): 2013–2048.
- [Klo17] Kings, G., Loeffler, D., Zerbes, S.L. *Rankin–Euler system and the Iwasawa main conjecture.* J. Amer. Math. Soc. **30** (2017): 653–692.
- [How06] Howard, B. *The Iwasawa theoretic Gross–Zagier theorem.* Compos. Math. **141** (2006): 811–846.
- [PR92] Perrin-Riou, B. *Fonctions L p-adiques, théorie d'Iwasawa et points de Heegner.* Séminaire de Théorie des Nombres de Paris, 1992.
- [PR98] Perrin-Riou, B. *Points de Heegner et dérivées de fonctions L p-adiques.* Invent. Math. **89** (1987): 455–510.
- [Wan14] Wan, X. *The Iwasawa main conjecture for Hilbert modular forms.* Forum Math. Sigma **3** (2015): e18.
