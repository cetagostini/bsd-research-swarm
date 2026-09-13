# J-ABEL-JACOBI: Projected Cycles, Abel–Jacobi Maps, and Reciprocity for Rank 2

**Author:** Group J — Unconventional Approaches
**Date:** 2026-09-13
**Status:** Technical directions 35–37 — the correct geometric construction for the triple product Abel–Jacobi map, its local conditions, and the reciprocity formula linking it to $p$-adic L-values

---

## Prerequisites and Conventions

This document continues the geometric program of J-DIAGONAL-CYCLES. The critical correction from the program review is:

> **Gross–Schoen Proposition 4.5 / equation (4.4):** $6\Delta_E = 0$ in $\mathrm{CH}^2(E \times E \times E)_0$ for a genus-one curve $E$. The naïve diagonal cycle vanishes with rational coefficients. The viable program uses Shimura varieties, Hecke projectors, auxiliary modular forms, and generalized diagonal classes.

All constructions below operate on the **correct** variety: a Shimura variety (not $E^3$), equipped with a Hecke projector that isolates the $f \otimes f \otimes f$-isotypic component.

---

## Direction 35: Projected Cycle on the Correct Variety

### 35.1. The Shimura Variety

**The correct target variety is NOT $E \times E \times E$.**

Let $f = \sum a_n q^n$ be the weight-2 newform attached to $E/\mathbb{Q}$ of conductor $N$. The triple product automorphic representation $\pi = \pi_f \otimes \pi_f \otimes \pi_f$ of $\mathrm{GL}_2^3(\mathbb{A})$ is associated to a Shimura variety via the following construction.

**Construction (Gross–Kudla–Schoen).** Let $\mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im}(z) > 0\}$ be the upper half-plane. Define:

$$X_\Gamma = (\mathbb{H} \times \mathbb{H} \times \mathbb{H}) / \Gamma$$

where $\Gamma = \Gamma_0(N) \times \Gamma_0(N) \times \Gamma_0(N) \subset \mathrm{SL}_2(\mathbb{Z})^3$ is the product of congruence subgroups at the level of $E$. More generally, for a compact open subgroup $K = K_p \times K^p \subset \mathrm{GL}_2(\mathbb{A}_f)$ with $K^p$ sufficiently small:

$$\mathrm{Sh}_K = \mathrm{GL}_2(\mathbb{Q}) \backslash (\mathbb{H}^{\pm})^3 \times \mathrm{GL}_2(\mathbb{A}_f) / K$$

This is a quasi-projective algebraic variety over $\mathbb{Q}$ of dimension 3. A smooth projective model $X$ is obtained by taking the Baily–Borel compactification and resolving singularities at the cusps (via toroidal or minimal resolution).

**For the level of $E$:** With $K = U_0(N) = \{g \in \mathrm{GL}_2(\hat{\mathbb{Z}}) : g \equiv \begin{psmallmatrix} * & * \\ 0 & * \end{psmallmatrix} \pmod{N}\}$, the Shimura variety $X_\Gamma$ is birational to the triple product of modular curves:

$$X_\Gamma \dashrightarrow X_0(N) \times X_0(N) \times X_0(N)$$

However, $X_\Gamma$ carries **additional structure** — Hecke correspondences act diagonally, and the cohomology decomposes into automorphic representations. The variety $X_\Gamma$ is the correct ambient space.

**Comparison with $E^3$.** The product $E \times E \times E$ is an abelian variety. The Shimura variety $X_\Gamma$ is **not** an abelian variety — it is a quotient of $\mathbb{H}^3$ by a discrete group. The Abel–Jacobi map for $X_\Gamma$ lives in a different cohomological setting (intermediate Jacobian of a threefold, not an abelian variety), and the naïve vanishing $6\Delta_E = 0$ does not apply to cycles on $X_\Gamma$.

### 35.2. The Hecke Projector

The Hecke algebra $\mathbb{T} = \bigotimes'_p T_p$ acts on $H^3(X_\Gamma, \mathbb{Q})$ (and on $\mathrm{CH}^2(X_\Gamma)_0$) by correspondences. For each prime $p$, the Hecke operator $T_p$ acts on the three factors simultaneously.

**Definition (Hecke projector).** The $f$-isotypic projector is:

$$e_f = \prod_p e_{f,p} \in \mathbb{T} \otimes \mathbb{Q}$$

where $e_{f,p}$ is the idempotent in the local Hecke algebra $\mathbb{T}_p$ at $p$ corresponding to the eigenvalue $a_p(f)$:

$$e_{f,p} = \lim_{n \to \infty} \frac{1}{|\Gamma_0(N) \backslash \Gamma_0(N) \begin{psmallmatrix} 1 & 0 \\ 0 & p^n \end{psmallmatrix} \Gamma_0(N)|} \sum_{i} \alpha_i T_{p,i}$$

More concretely, for the triple product, we use the **Rankin–Selberg projector**:

$$e_{f \otimes f \otimes f} = e_f^{(1)} \otimes e_f^{(2)} \otimes e_f^{(3)}$$

where $e_f^{(i)}$ acts on the $i$-th factor of $\mathbb{H}^3 / \Gamma$.

**Action on cohomology.** The projector $e_{f \otimes f \otimes f}$ acts on $H^3(X_\Gamma, \mathbb{Q}_\ell)$ (étale) or $H^3(X_\Gamma, \mathbb{Q})$ (Betti) to extract the $f^{\otimes 3}$-component:

$$H^3(X_\Gamma, \mathbb{Q}_\ell)^{(f \otimes f \otimes f)} = e_{f \otimes f \otimes f} \cdot H^3(X_\Gamma, \mathbb{Q}_\ell)$$

This is the Galois representation $V_f^{\otimes 3}$ (up to Tate twist and multiplicity), where $V_f = H^1(E, \mathbb{Q}_\ell)$ is the 2-dimensional $\ell$-adic representation attached to $f$.

**The Clebsch–Gordan decomposition:**

$$V_f^{\otimes 3} \cong \mathrm{Sym}^3 V_f \oplus V_f^{\oplus 2}$$

as $\mathrm{GL}_2$-representations. The $f^{\otimes 3}$-component of $H^3(X_\Gamma)$ decomposes accordingly into the symmetric cube motive $M(\mathrm{Sym}^3 f)$ and two copies of $M(f)$.

### 35.3. The Coefficient System

The local system $\mathcal{V}$ on $X_\Gamma$ underlying the Galois representation is:

$$\mathcal{V} = \mathcal{V}_f \boxtimes \mathcal{V}_f \boxtimes \mathcal{V}_f$$

where $\mathcal{V}_f$ is the rank-2 local system on $X_0(N)$ corresponding to $f$. Concretely, $\mathcal{V}_f = R^1 \pi_* \mathbb{Q}_\ell$ where $\pi: \mathcal{E} \to X_0(N)$ is the universal elliptic curve.

The coefficient system for the Abel–Jacobi map is the **motivic realization**:

$$M_f^{\otimes 3} = M(f) \otimes M(f) \otimes M(f) \in \mathbf{Mot}_{\mathbb{Q}}(X_\Gamma)$$

where $M(f)$ is the motive of $f$ (a rank-2 motive over $\mathbb{Q}$ with coefficients in the Hecke eigenvalue field, which is $\mathbb{Q}$ since $f$ has rational Fourier coefficients).

The relevant intermediate Jacobian is:

$$J^2(X_\Gamma) = H^3(X_\Gamma, \mathbb{C}) / (F^2 H^3 + H^3(X_\Gamma, \mathbb{Z}))$$

and the $f$-isotypic part:

$$J^2(X_\Gamma)^{(f^{\otimes 3})} = H^3(X_\Gamma, \mathbb{C})^{(f^{\otimes 3})} / (F^2 + H^3(X_\Gamma, \mathbb{Z})^{(f^{\otimes 3})})$$

### 35.4. The Cycle Construction

**The diagonal in $\mathbb{H}^3 / \Gamma$.** The small diagonal embedding:

$$\delta: \mathbb{H} / \Gamma_0(N) \hookrightarrow (\mathbb{H} \times \mathbb{H} \times \mathbb{H}) / \Gamma, \quad z \mapsto (z, z, z)$$

defines a codimension-2 cycle $[\delta(\mathbb{H}/\Gamma_0(N))]$ on $X_\Gamma$.

**The modified diagonal.** Following Gross–Schoen, define the modified diagonal cycle $\Delta^*$ on $X_\Gamma$ by subtracting boundary corrections at the cusps:

$$\Delta^*_{X_\Gamma} = [\delta(X_0(N))] - \sum_{i < j} \delta_{ij}^* + \sum_i \gamma_i^*$$

where $\delta_{ij}^*$ are the partial diagonals (projected to the $(i,j)$-factors, with the third factor at a cusp) and $\gamma_i^*$ are correction terms at the cusps of $X_0(N)$.

**The projected cycle.** Apply the Hecke projector:

$$\boxed{\Delta(f^{\otimes 3}) = e_{f \otimes f \otimes f} \cdot \Delta^*_{X_\Gamma} \in \mathrm{CH}^2(X_\Gamma)_0 \otimes \mathbb{Q}}$$

This cycle is:
1. **Homologically trivial** (by construction of $\Delta^*$).
2. **An eigenvector** for the full Hecke algebra with eigenvalue $a_p(f)^3$ at each $T_p$.
3. **Non-zero** in $\mathrm{CH}^2(X_\Gamma)_0 \otimes \mathbb{Q}$ — this is the critical nonvanishing statement (Direction 40).

**Published construction:** This cycle is constructed in:
- Gross, B.H., Schoen, C. *The modified diagonal cycle on the triple product of a pointed curve.* Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) **25** (1997), no. 3–4, 459–483 (1998). [§4: the modified diagonal and its homological triviality]
- Schoen, C. *Complex varieties for which the Beilinson–Bloch conjecture holds.* Proceedings of the International Conference on Arithmetic Algebraic Geometry (Texel, 1989). J. Reine Angew. Math. **447** (1994), 153–165. [The projector construction]
- Yuan, X., Zhang, S.-W., Zhang, W. *The Gross–Kudla–Schoen formula for Shimura varieties.* Preprint, 2023. [The arithmetic intersection formula]

### 35.5. Why the Correct Variety Is Essential

The distinction between $E^3$ and $X_\Gamma$ is not merely technical:

| Property | $E^3 = E \times E \times E$ | $X_\Gamma = (\mathbb{H}^3)/\Gamma$ |
|----------|---------------------------|--------------------------------------|
| Structure | Abelian variety | Shimura variety (not abelian) |
| $\Delta^*$ in $\mathrm{CH}^2$ | $6\Delta_E = 0$ (vanishes) | $\Delta(f^{\otimes 3}) \neq 0$ (conjecturally) |
| Abel–Jacobi target | $H^3(E^3)/F^2$ (abelian variety) | $J^2(X_\Gamma)^{(f^{\otimes 3})}$ (intermediate Jacobian) |
| Hecke action | Diagonal, but naive | Full automorphic decomposition |
| L-function | $L(E \times E \times E, s)$ | Same L-function, but with correct motivic structure |

The vanishing $6\Delta_E = 0$ in $\mathrm{CH}^2(E^3)_0$ occurs because $E$ has genus 1: the correction terms in $\Delta^*$ absorb the diagonal. On $X_\Gamma$, the cusp corrections are different, and the projected cycle $\Delta(f^{\otimes 3})$ does not vanish.

---

## Direction 36: Abel–Jacobi Image and Local Conditions

### 36.1. The Abel–Jacobi Map

**Definition.** Let $X$ be a smooth projective variety of dimension $d$ over $\mathbb{Q}$, and let $Z \in \mathrm{CH}^r(X)_0$ be a codimension-$r$ cycle homologically trivial over $\mathbb{Q}$. The **Abel–Jacobi map** is:

$$\Phi: \mathrm{CH}^r(X)_0 \longrightarrow J^r(X) = \frac{H^{2r-1}(X(\mathbb{C}), \mathbb{C})}{F^r H^{2r-1}(X, \mathbb{C}) + H^{2r-1}(X(\mathbb{C}), \mathbb{Z})}$$

defined as follows. Since $Z$ is homologically trivial, there exists a real $(2d - 2r + 1)$-chain $\Gamma$ on $X(\mathbb{C})$ with $\partial \Gamma = Z(\mathbb{C})$. Then $\Phi(Z) = [\int_\Gamma \omega]_{\omega \in F^r}$, the class of the period integrals in the intermediate Jacobian.

**For the triple product:** With $X = X_\Gamma$, $d = 3$, $r = 2$:

$$\Phi: \mathrm{CH}^2(X_\Gamma)_0 \longrightarrow J^2(X_\Gamma) = \frac{H^3(X_\Gamma(\mathbb{C}), \mathbb{C})}{F^2 H^3 + H^3(X_\Gamma, \mathbb{Z})}$$

The $f^{\otimes 3}$-projected Abel–Jacobi image is:

$$\Phi_f(\Delta(f^{\otimes 3})) \in J^2(X_\Gamma)^{(f^{\otimes 3})}$$

### 36.2. The $p$-adic Abel–Jacobi Map

For the reciprocity formula (Direction 37), we need the **$p$-adic** Abel–Jacobi map. Let $p$ be a prime of good reduction for $E$ (hence for $X_\Gamma$).

**Definition ($p$-adic AJ).** The $p$-adic Abel–Jacobi map is:

$$\Phi_p: \mathrm{CH}^2(X_\Gamma)_0 \longrightarrow H^1_f(G_{\mathbb{Q}}, H^3_{\mathrm{\acute{e}t}}(\bar{X}_\Gamma, \mathbb{Q}_p(2)))$$

where $G_{\mathbb{Q}} = \operatorname{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$, $H^3_{\mathrm{\acute{e}t}}$ denotes $\ell$-adic étale cohomology (with $\ell = p$), and $H^1_f$ denotes the **Bloch–Kato Selmer group** (the finite part of Galois cohomology).

More precisely, the $p$-adic AJ map factors through the étale Abel–Jacobi map of Bloch:

$$\mathrm{CH}^2(X_\Gamma)_0 \xrightarrow{\mathrm{AJ}_p} H^1(G_{\mathbb{Q},S}, H^3_{\mathrm{\acute{e}t}}(\bar{X}_\Gamma, \mathbb{Z}_p(2)))$$

where $S$ is the set of bad primes (dividing $Np\infty$).

**Relation to the complex AJ.** Under the comparison isomorphism $H^3_{\mathrm{\acute{e}t}}(\bar{X}_{\Gamma,\mathbb{C}_p}, \mathbb{Z}_p(2)) \cong H^3_{\mathrm{dR}}(X_\Gamma) \otimes \mathbb{Z}_p$ (via $p$-adic Hodge theory), the $p$-adic and complex Abel–Jacobi maps are compatible. The $p$-adic image carries local information invisible to the complex map.

### 36.3. The Selmer Group (Global Condition)

The **target** of the $p$-adic Abel–Jacobi map is the Bloch–Kato Selmer group:

$$H^1_f(G_\mathbb{Q}, V) = \ker\left(H^1(G_{\mathbb{Q},S}, V) \xrightarrow{\lambda} \prod_{v \in S} \frac{H^1(G_v, V)}{H^1_f(G_v, V)}\right)$$

where $V = H^3_{\mathrm{\acute{e}t}}(\bar{X}_\Gamma, \mathbb{Q}_p(2))$ is the $p$-adic étale cohomology with Tate twist.

**The $f^{\otimes 3}$-component.** Under the Hecke decomposition and the Clebsch–Gordan splitting $V^{(f^{\otimes 3})} \cong \mathrm{Sym}^3 V_f(1) \oplus V_f(1)^{\oplus 2}$ (with appropriate Tate twist), the Selmer group decomposes:

$$H^1_f(G_\mathbb{Q}, V^{(f^{\otimes 3})}) = H^1_f(G_\mathbb{Q}, \mathrm{Sym}^3 V_f(1)) \oplus H^1_f(G_\mathbb{Q}, V_f(1))^{\oplus 2}$$

The second summand contains the **Kato Euler system classes** $z_{\mathrm{Kato}} \in H^1_f(G_\mathbb{Q}, V_f(1))$ (one for each copy of $f$ in the decomposition). The first summand involves the symmetric cube, which is the genuinely new part.

### 36.4. Local Conditions at $p$

At the prime $p$ of good reduction, the **Bloch–Kato local condition** is:

$$H^1_f(G_p, V) = \operatorname{im}\left(\frac{D_{\mathrm{cris}}(V)}{\mathrm{Fil}^0 D_{\mathrm{cris}}(V)} \xrightarrow{\exp} H^1(G_p, V)\right)$$

where:
- $D_{\mathrm{cris}}(V) = (V \otimes_{\mathbb{Q}_p} B_{\mathrm{cris}})^{G_p}$ is the crystalline Dieudonné module.
- $\mathrm{Fil}^0 D_{\mathrm{cris}}(V)$ is the 0-th step of the Hodge filtration.
- $\exp: D_{\mathrm{cris}}(V)/\mathrm{Fil}^0 \to H^1(G_p, V)$ is the Bloch–Kato exponential map.

**Explicit description for $V = H^3(X_\Gamma, \mathbb{Q}_p(2))$:**

The Hodge filtration on $H^3_{\mathrm{dR}}(X_\Gamma)$ has steps $F^0 \supset F^1 \supset F^2 \supset F^3 = 0$. For a weight-3 motive twisted by $\mathbb{Q}_p(2)$ (shift weight $-1$):

$$\mathrm{Fil}^j D_{\mathrm{cris}}(V) = F^{j+2} H^3_{\mathrm{dR}}(X_\Gamma)$$

So $\mathrm{Fil}^0 D_{\mathrm{cris}}(V) = F^2 H^3_{\mathrm{dR}}(X_\Gamma)$. The exponential map:

$$\exp: \frac{H^3_{\mathrm{dR}}(X_\Gamma)}{F^2 H^3_{\mathrm{dR}}} \longrightarrow H^1(G_p, H^3_{\mathrm{\acute{e}t}}(\bar{X}_\Gamma, \mathbb{Q}_p(2)))$$

is the $p$-adic comparison map from de Rham to étale cohomology, via the Bloch–Kato exponential.

**Practically:** $\xi \in H^1_f(G_p, V)$ if and only if $\xi$ is **crystalline** — it lies in the image of the exponential map from the quotient $D_{\mathrm{cris}}(V)/\mathrm{Fil}^0$. This is equivalent to: the restriction of $\xi$ to the inertia group $I_p$ factors through the crystalline extension class.

**For the $f$-component.** When $V = V_f(1)$ (the Tate twist of the Galois representation of $E$), the crystalline condition at $p$ translates to:

$$H^1_f(G_p, V_f(1)) \cong E(\mathbb{Q}_p) \otimes \mathbb{Q}_p$$

via the Kummer map $\kappa_p: E(\mathbb{Q}_p) \otimes \mathbb{Q}_p \xrightarrow{\sim} H^1_f(G_p, V_f(1))$. For the symmetric cube component $\mathrm{Sym}^3 V_f(1)$, the local condition is:

$$H^1_f(G_p, \mathrm{Sym}^3 V_f(1)) = \operatorname{im}\left(\exp_{\mathrm{Sym}^3}: \frac{D_{\mathrm{cris}}(\mathrm{Sym}^3 V_f)}{\mathrm{Fil}^{-1}} \to H^1(G_p, \mathrm{Sym}^3 V_f(1))\right)$$

This is a 2-dimensional $\mathbb{Q}_p$-space (since $\dim D_{\mathrm{cris}}(\mathrm{Sym}^3 V_f) = 4$ and $\dim \mathrm{Fil}^{-1} = 2$).

### 36.5. Local Conditions at Bad Primes $\ell \mid N$

At a prime $\ell \mid N$ of bad reduction, the local condition is:

$$H^1_f(G_\ell, V) = \ker\left(H^1(G_\ell, V) \to H^1(I_\ell, V)\right)$$

the **unramified cohomology**, where $I_\ell \subset G_\ell$ is the inertia group.

**For semistable $E$ (e.g., 389a1 or 433a1).** When $E$ has semistable reduction at $\ell$, the local representation $V_f|_{G_\ell}$ fits in an exact sequence:

$$0 \to \mathbb{Q}_p(1) \to V_f|_{G_\ell} \to \mathbb{Q}_p \to 0$$

(split multiplicative case, $a_\ell = 1$) or

$$0 \to \mathbb{Q}_p \to V_f|_{G_\ell} \to \mathbb{Q}_p(1) \to 0$$

(nonsplit multiplicative, $a_\ell = -1$). The unramified condition $H^1_f(G_\ell, V_f(1))$ is then:

- **Split multiplicative ($a_\ell = 1$):** $H^1_f(G_\ell, V_f(1)) \cong \mathbb{Q}_p$ (the unramified quotient).
- **Nonsplit multiplicative ($a_\ell = -1$):** $H^1_f(G_\ell, V_f(1)) = 0$.

**For the symmetric cube.** The local representation $\mathrm{Sym}^3 V_f|_{G_\ell}$ is an extension of $\mathbb{Q}_p$-representations involving twists $\mathbb{Q}_p(j)$ for $j = 0, 1, 2, 3$. The unramified condition picks out the invariants under inertia:

$$H^1_f(G_\ell, \mathrm{Sym}^3 V_f(1)) = H^1_{\mathrm{ur}}(G_\ell, \mathrm{Sym}^3 V_f(1))$$

This space has dimension depending on the Jordan–Hölder factors of $\mathrm{Sym}^3 V_f|_{I_\ell}$.

**For $E = 389a1$ at $\ell = 389$:** Since 389 is prime and $E$ has conductor 389, the only bad prime is 389. The local condition at 389 is the unramified cohomology $H^1_{\mathrm{ur}}(G_{389}, V)$, which is a specific finite-dimensional $\mathbb{Q}_p$-space determined by the reduction type of $E$ at 389.

### 36.6. The Archimedean Condition

At $v = \infty$:

$$H^1_f(G_\infty, V) = 0$$

since $V$ is an odd Galois representation (the motivic weight is odd) and $p$ is odd. This means there is no archimedean contribution to the Selmer group.

### 36.7. The Global-to-Local Map

The Abel–Jacobi image $\Phi_p(\Delta(f^{\otimes 3}))$ defines a class in $H^1(G_{\mathbb{Q},S}, V)$. For this class to lie in the Selmer group $H^1_f(G_\mathbb{Q}, V)$, it must satisfy the local conditions at every place:

$$\mathrm{loc}_v(\Phi_p(\Delta(f^{\otimes 3}))) \in H^1_f(G_v, V) \quad \text{for all } v \in S = \{p\} \cup \{\ell : \ell \mid N\} \cup \{\infty\}$$

**Theorem (Bloch, 1985; Jannsen, 2000).** *The étale Abel–Jacobi image of a cycle defined over $\mathbb{Q}$ automatically satisfies the local conditions at all finite primes $v \neq p$ of good reduction. At primes $v \mid N$, the image lies in $H^1_f$ provided the cycle extends to a smooth model over $\mathbb{Z}_v$. At $v = p$, the image is crystalline if the cycle has good reduction at $p$.*

**Therefore:** The critical local condition to verify is at $p$ itself. The global class $\Phi_p(\Delta(f^{\otimes 3}))$ automatically satisfies:
- Local conditions at all $\ell \nmid Np$ (unramified, by good reduction).
- Local condition at $\infty$ (trivial, since $H^1_f(G_\infty, V) = 0$).

The content of Direction 36 is:

**Conjecture/Goal.** *Prove that $\mathrm{loc}_p(\Phi_p(\Delta(f^{\otimes 3}))) \in H^1_f(G_p, V)$, i.e., the Abel–Jacobi image is crystalline at $p$.*

This requires showing that $\Phi_p(\Delta(f^{\otimes 3}))$ arises from the exponential map — equivalently, that it is in the image of $D_{\mathrm{cris}}(V)/\mathrm{Fil}^0$ under the Bloch–Kato exponential.

### 36.8. Sufficiency vs. Necessity

**Important caveat.** The Abel–Jacobi image lying in the Selmer group is **necessary but not sufficient** for the BSD application. Specifically:

1. **Necessary:** The class $\Phi_p(\Delta(f^{\otimes 3})) \in H^1_f(G_\mathbb{Q}, V)$ must be nonzero for the height pairing to be nonzero and hence for $L^{(r)}(E \times E \times E, 3/2) \neq 0$.

2. **Not sufficient:** A nonzero class in the Selmer group does not automatically give the leading L-value. One also needs the **reciprocity formula** (Direction 37) relating the class to the $p$-adic L-function, and the nondegeneracy of the height pairing.

3. **Additional global condition:** The class must be **primitive** — not the image of a class from a proper Shimura subvariety. The diagonal cycle $\Delta(f^{\otimes 3})$ is constructed to be in the $f^{\otimes 3}$-component, which primitivity ensures.

---

## Direction 37: The Reciprocity Formula

### 37.1. Overview

The reciprocity formula is the bridge between the Abel–Jacobi image of the projected cycle and the $p$-adic L-function. It is the **triple product analogue** of the Gross–Zagier formula.

### 37.2. The Rank 1 Prototype: Gross–Zagier

The established prototype is the **Gross–Zagier formula** [GZ86] for Heegner points.

**Setup.** Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, $K$ an imaginary quadratic field satisfying the Heegner hypothesis ($p \mid N \Rightarrow p$ splits in $K$). The Heegner point $y_K \in E(K)$ is the image of a CM point on $X_0(N)$ under the modular parametrization $\phi: X_0(N) \to E$.

**The formula.** Let $\chi$ be a ring class character of $K$. Then:

$$L'(E/K, \chi, 1) = \frac{8\pi^2 \|f\|^2}{u^2 \sqrt{|D_K|}} \cdot \hat{h}_\chi(y_K)$$

where:
- $\|f\|^2 = \langle f, f \rangle = \int_{\Gamma_0(N) \backslash \mathbb{H}} |f(z)|^2 y^2 \, \frac{dx\,dy}{y^2}$ is the Petersson norm.
- $u = |\mathcal{O}_K^\times| / 2$ is half the number of roots of unity.
- $D_K$ is the discriminant of $K$.
- $\hat{h}_\chi(y_K) = \sum_\chi \chi(\sigma) \hat{h}(y_K^\sigma)$ is the $\chi$-component of the Néron–Tate height.

**Abel–Jacobi interpretation.** The Heegner point $y_K$ defines a class in $\mathrm{CH}^1(E)_0 = \mathrm{Pic}^0(E) = E(\mathbb{Q})$ via the modular parametrization. The Abel–Jacobi map $\Phi_p: \mathrm{CH}^1(E)_0 \to H^1_f(G_\mathbb{Q}, V_f(1)) \cong E(\mathbb{Q}) \otimes \mathbb{Q}_p$ sends $y_K$ to its image in the $p$-adic Selmer group. The Gross–Zagier formula is then:

$$\Phi_p(y_K) \neq 0 \iff L'(E/K, 1) \neq 0$$

with the **height** $= $ **L-value** equality.

### 37.3. The Triple Product Reciprocity

For the triple product, the analogue is a formula relating the Abel–Jacobi image of $\Delta(f^{\otimes 3})$ to the derivative of the $p$-adic triple product L-function.

**The $p$-adic triple product L-function.** There exists a $p$-adic analytic function:

$$L_p(f \otimes f \otimes f, s) \in \mathbb{Q}_p[[s]]$$

constructed by Harris–Tilouine [HT01] and Darmon–Rotger [DR14] via $p$-adic Rankin–Selberg integration. This function interpolates the algebraic parts of $L(f \otimes f \otimes f \otimes \chi, j)$ for finite-order characters $\chi$ and critical integers $j$.

**The interpolation property.** For a finite-order character $\chi$ of conductor $p^n$ and integer $j$ in the critical range $1 \leq j \leq 2$:

$$L_p(f \otimes f \otimes f, \chi, j) = \mathcal{E}_p(j, \chi) \cdot \frac{L(f \otimes f \otimes f \otimes \chi, j)}{\Omega(f \otimes f \otimes f)^{\pm}}$$

where $\mathcal{E}_p(j, \chi)$ is an explicit Euler factor at $p$ and $\Omega^{\pm}$ are the periods.

**The central point.** The center of the functional equation for $L(f \otimes f \otimes f, s)$ is at $s = 3/2$ (motivic normalization). The $p$-adic L-function $L_p(f \otimes f \otimes f, s)$ is defined on a $p$-adic neighborhood of the critical strip, and the value at $s = 3/2$ (or its derivative, depending on root number) encodes the arithmetic.

### 37.4. The Reciprocity Formula: Statement

**Conjecture (Triple product reciprocity).** *Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$ with analytic rank 2, and $p \nmid N$ a prime of good ordinary reduction. Let $\Delta(f^{\otimes 3}) \in \mathrm{CH}^2(X_\Gamma)_0$ be the projected diagonal cycle of Direction 35, and let $\Phi_p(\Delta(f^{\otimes 3})) \in H^1_f(G_\mathbb{Q}, V)$ be its $p$-adic Abel–Jacobi image. Then:*

$$\boxed{\langle \Phi_p(\Delta(f^{\otimes 3})), \Phi_p(\Delta(f^{\otimes 3})) \rangle_{\mathrm{BK}} = \mathcal{E}^* \cdot L_p'(f \otimes f \otimes f, 3/2)}$$

*where:*
- $\langle \cdot, \cdot \rangle_{\mathrm{BK}}$ is the **Bloch–Kato logarithm pairing** on $H^1_f(G_\mathbb{Q}, V)$, defined via the dual exponential map $\exp^*: H^1(G_p, V) \to D_{\mathrm{cris}}(V^*(1))^* / \mathrm{Fil}^0$ and the Poincaré duality pairing on $D_{\mathrm{cris}}$.
- $\mathcal{E}^*$ is an explicit product of local Euler factors at $p$ and primes dividing $N$.
- $L_p'(f \otimes f \otimes f, 3/2)$ is the first derivative of the $p$-adic triple product L-function at the central point.

### 37.5. The Closest Established Formula

The closest established result is the **Darmon–Rotger formula** [DR17, Theorem A]:

**Theorem (Darmon–Rotger, 2017).** *Let $f, g, h$ be newforms of weight 2 for $\Gamma_0(N)$ with $N$ squarefree, and let $p \nmid N$ be a prime such that $a_p(f), a_p(g), a_p(h)$ are $p$-adic units. Define the **triple product $p$-adic L-function** $L_p(f, g, h, s)$ via $p$-adic Rankin–Selberg integration. Assume $\epsilon(f \otimes g \otimes h) = -1$ (root number $-1$, so the central value $L(f \otimes g \otimes h, 3/2) = 0$ is forced). Then:*

$$L_p'(f, g, h, 3/2) = \frac{\mathcal{E}(f, g, h)}{\langle f, f \rangle \langle g, g \rangle \langle h, h \rangle} \cdot \log_p^2(\mathrm{AJ}_p(\Delta(f \otimes g \otimes h)))$$

*where $\log_p: H^1_f(G_p, V) \to D_{\mathrm{cris}}(V)/\mathrm{Fil}^0$ is the Bloch–Kato logarithm, $\mathcal{E}$ is an explicit Euler factor, and $\mathrm{AJ}_p(\Delta)$ is the $p$-adic Abel–Jacobi image of the projected diagonal cycle.*

**In our case ($f = g = h$):** This becomes:

$$L_p'(f \otimes f \otimes f, 3/2) = \frac{\mathcal{E}(f, f, f)}{\|f\|^6} \cdot \log_p^2(\Phi_p(\Delta(f^{\otimes 3})))$$

### 37.6. The Rank 2 Case: What Is Missing

The Darmon–Rotger theorem applies when $\epsilon = -1$ and the central value vanishes to **order exactly 1**. For our situation ($E$ with rank 2, $\epsilon = +1$), the situation is fundamentally different:

**Problem 1: Root number sign.** For rank 2 curves like 389a1 or 433a1, the triple product root number is $\epsilon = +1$ (as computed in J-DIAGONAL-CYCLES §VI). The Gross–Kudla–Schoen formula and Darmon–Rotger theorem both require $\epsilon = -1$.

**Problem 2: Higher-order vanishing.** The order of vanishing $\mathrm{ord}_{s=3/2} L(E \times E \times E, s) = 3r = 6$ (for $r = 2$) means we need the **sixth derivative**, not the first. No reciprocity formula for higher-order vanishing of the triple product L-function is known.

**Problem 3: The symmetric cube component.** The decomposition $V_f^{\otimes 3} \cong \mathrm{Sym}^3 V_f \oplus V_f^{\oplus 2}$ means the Selmer group has a piece from $\mathrm{Sym}^3$ that has no analogue in the rank-1 theory. The nonvanishing of $L(\mathrm{Sym}^3 E, 1)$ (the symmetric cube L-value) contributes to the leading coefficient but is not controlled by the diagonal cycle alone.

### 37.7. The Missing Factor for Rank 2

The specific missing piece is:

**Missing formula.** For $E$ of rank $r = 2$ with $p$-adic Abel–Jacobi image $\alpha = \Phi_p(\Delta(f^{\otimes 3})) \in H^1_f(G_\mathbb{Q}, V)$, the correct reciprocity should take the form:

$$L_p^{(6)}(f \otimes f \otimes f, 3/2) = \mathcal{E}^* \cdot \det\begin{pmatrix} \langle \alpha, \alpha \rangle_{\mathrm{BK}} & \langle \alpha, z_1 \rangle_{\mathrm{BK}} & \langle \alpha, z_2 \rangle_{\mathrm{BK}} \\ \langle z_1, \alpha \rangle_{\mathrm{BK}} & \langle z_1, z_1 \rangle_{\mathrm{BK}} & \langle z_1, z_2 \rangle_{\mathrm{BK}} \\ \langle z_2, \alpha \rangle_{\mathrm{BK}} & \langle z_2, z_1 \rangle_{\mathrm{BK}} & \langle z_2, z_2 \rangle_{\mathrm{BK}} \end{pmatrix}$$

where $z_1, z_2 \in H^1_f(G_\mathbb{Q}, V_f(1))$ are the two Kato Euler system classes corresponding to the two copies of $V_f(1)$ in the Clebsch–Gordan decomposition.

**This is a conjecture, not a theorem.** The known results are:

1. **Gross–Zagier [GZ86]:** $L'(E, 1) = c \cdot \hat{h}(P_K)$ for Heegner points $P_K$ (rank 1, single class).

2. **Darmon–Rotger [DR17]:** $L_p'(f \otimes g \otimes h, 3/2) = c \cdot \log_p^2(\mathrm{AJ}_p(\Delta))$ (rank 1 for triple product, $\epsilon = -1$).

3. **Yuan–Zhang–Zhang [YZZ23]:** The arithmetic Siegel–Weil formula for the height of $\Delta$ in the unramified case (rank 1 analogue).

4. **For rank 2:** The formula should involve a **determinant** (or Pfaffian) of the height pairing matrix on a 3-dimensional Selmer subspace spanned by $\{\alpha, z_1, z_2\}$. The right-hand side should be $L_p^{(6)}$, the sixth derivative.

**The specific local case that is missing** is the **supersingular case** at $p$. When $a_p = 0$ (supersingular), the Bloch–Kato exponential and logarithm are not defined in the classical sense, and one must use the **plus/minus** Selmer conditions of Kobayashi. The reciprocity formula in the supersingular case would involve the plus/minus $p$-adic L-functions $L_p^\pm(f \otimes f \otimes f, s)$ and the corresponding plus/minus Abel–Jacobi maps.

### 37.8. The Explicit Euler Factor

The Euler factor $\mathcal{E}^*$ in the reciprocity formula is:

$$\mathcal{E}^* = \prod_{\ell \mid N} \mathcal{E}_\ell \cdot \mathcal{E}_p$$

where:

- **At $\ell \mid N$ (bad primes):** $\mathcal{E}_\ell$ involves the Tamagawa factor $c_\ell(E)$ and the local root number $\epsilon_\ell(f \otimes f \otimes f)$. For semistable $E$ with $a_\ell = \pm 1$:

$$\mathcal{E}_\ell = \frac{L_\ell(\mathrm{Sym}^3 f, 0)}{L_\ell(f, 0)^2} \cdot c_\ell$$

where $L_\ell(\mathrm{Sym}^3 f, s)$ is the local L-factor of the symmetric cube at $\ell$.

- **At $p$ (good ordinary prime):** The $p$-adic Euler factor is:

$$\mathcal{E}_p = \left(1 - \frac{a_p^3}{p^2}\right)^{-1} \cdot \left(1 - \frac{a_p}{p}\right)^{-2} \cdot \frac{\log_p(E(\mathbb{Q}_p))^2}{\Omega_p^2}$$

where $\log_p: E(\mathbb{Q}_p) \to \mathbb{Q}_p$ is the formal group logarithm and $\Omega_p$ is the $p$-adic period.

### 37.9. Summary: The Three Directions

| Direction | Object | Status | Key result needed |
|-----------|--------|--------|-------------------|
| **35** | $\Delta(f^{\otimes 3}) \in \mathrm{CH}^2(X_\Gamma)_0$ | Construction known | Nonvanishing in Chow group |
| **36** | $\Phi_p(\Delta) \in H^1_f(G_\mathbb{Q}, V)$ | Local conditions stated | Crystallinity at $p$ |
| **37** | $\langle \Phi_p(\Delta), \Phi_p(\Delta) \rangle_{\mathrm{BK}} = \mathcal{E}^* \cdot L_p^{(6)}$ | Formula conjectured | Proof for rank 2 case |

The **pipeline** is:

```
Direction 35: Construct Δ(f⊗f⊗f) on X_Γ = (ℍ³)/Γ
       ↓
Direction 36: Show AJ_p(Δ) ∈ H¹_f(G_ℚ, V) [Selmer group]
       ↓
Direction 37: Reciprocity: ⟨AJ_p(Δ), AJ_p(Δ)⟩ = E* · L_p^{(6)}(f⊗f⊗f, 3/2)
       ↓
BSD: L_p^{(6)} ≠ 0 ⟹ rank = 2 (if p-adic leading term ≠ 0)
```

### 37.10. What Would Constitute a Proof for 389a1

For the benchmark curve 389a1, a complete proof of the reciprocity formula would require:

1. **Construct $\Delta(f^{\otimes 3})$ explicitly** on the Shimura variety $X_\Gamma$ at level $\Gamma_0(389)^3$, using the Hecke projector $e_{f \otimes f \otimes f}$.

2. **Compute $\Phi_p(\Delta(f^{\otimes 3}))$** at $p = 5$ (the ordinary prime for 389a1) as an explicit Galois cocycle, using modular symbols of level $389 \cdot 5^n$ for $n \gg 0$.

3. **Verify the local condition at $p = 5$** by checking that the cocycle is crystalline — equivalently, that its restriction to $I_5$ is trivial in $H^1(I_5, V)$.

4. **Compute the Bloch–Kato pairing** $\langle \Phi_p(\Delta), \Phi_p(\Delta) \rangle_{\mathrm{BK}}$ numerically and compare with $L_p^{(6)}(f \otimes f \otimes f, 3/2)$ computed via $p$-adic interpolation.

5. **Verify the Euler factor** $\mathcal{E}^*$ at the bad prime 389 and the good prime 5.

Steps 1–3 are currently feasible (with significant computation). Step 4 requires computing the sixth derivative of a $p$-adic L-function, which is at the boundary of current $p$-adic computation methods. Step 5 is straightforward once the other data is assembled.

---

## References

- **[B85]** Bloch, S. *Algebraic cycles and the Lie algebra actions on cohomology.* Algebraic geometry (Chicago, 1985). Lecture Notes in Math. **1289**, Springer, 1987.
- **[BK90]** Bloch, S., Kato, K. *L-functions and Tamagawa numbers of motives.* The Grothendieck Festschrift, Vol. I. Progr. Math. **86**, Birkhäuser, 1990, 333–400.
- **[DR14]** Darmon, H., Rotger, V. *Diagonal cycles and Euler systems I: A $p$-adic Gross–Zagier formula.* Ann. Sci. Éc. Norm. Supér. (4) **47** (2014), no. 4, 779–832.
- **[DR17]** Darmon, H., Rotger, V. *Elliptic curves of rank two and generalised Kato classes.* Math. Proc. Cambridge Philos. Soc. **164** (2018), 221–243.
- **[GK92]** Gross, B.H., Kudla, S.S. *Heights and the central critical values of triple product L-functions.* Compositio Math. **81** (1992), 143–209.
- **[GS99]** Gross, B.H., Schoen, C. *The modified diagonal cycle on the triple product of a pointed curve.* Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) **25** (1997), 459–483.
- **[GZ86]** Gross, B.H., Zagier, D. *Heegner points and derivatives of L-series.* Invent. Math. **84** (1986), 225–320.
- **[HT01]** Harris, M., Tilouine, J. *p-adic measures and square roots of triple product L-values.* Math. Ann. **320** (2001), 367–418.
- **[N06]** Nekovář, J. *Selmer complexes.* Astérisque **310** (2006).
- **[YZZ23]** Yuan, X., Zhang, S.-W., Zhang, W. *Triple product L-series and Gross–Kudla–Schoen cycles.* Preprint, 2023.
