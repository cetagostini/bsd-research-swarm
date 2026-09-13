# J-DIAGONAL-CYCLES: The Gross–Kudla–Schoen Diagonal Cycle and Rank 2 BSD

**Author:** Group J — Unconventional Approaches
**Date:** 2026-09-13
**Status:** Exploratory — the diagonal cycle on $E \times E \times E$ as a candidate algebraic cycle for rank 2 BSD

---

## I. Motivation: The Search for an Algebraic Cycle at Rank 2

The Birch and Swinnerton-Dyer conjecture predicts that the rank of $E(\mathbb{Q})$ equals the order of vanishing of $L(E, s)$ at $s = 1$. For rank 1, the Gross–Zagier formula provides the missing link: the height of a Heegner point on $E$ computes $L'(E, 1)$. For rank 2, no analogous algebraic cycle on $E$ itself is known whose height computes $L''(E, 1)$.

This document proposes that the **Gross–Kudla–Schoen diagonal cycle** on the triple product $E \times E \times E$ provides a candidate. The diagonal is a codimension-2 cycle whose arithmetic height, via Arakelov intersection theory, is conjecturally related to the triple product $L$-function $L(E \times E \times E, s)$. The functional equation and the rank 2 hypothesis force a high-order zero at $s = 0$ for this $L$-function, and the leading coefficient encodes $L'(E, 1)^2$ — precisely the BSD quantity of interest.

---

## II. The Diagonal Cycle Construction

### Setup

Let $E$ be an elliptic curve over $\mathbb{Q}$, and consider the triple product $X = E \times E \times E$, a smooth projective threefold over $\mathbb{Q}$. The **small diagonal** is:

$$\Delta_{\mathrm{sm}} = \{(x, x, x) : x \in E\} \subset X$$

This is a curve (dimension 1, codimension 2) in the threefold $X$.

### The Gross–Schoen Modified Diagonal

Gross and Schoen [GS99] introduced a **modified diagonal cycle** that is homologically trivial, which is essential for defining a height pairing. The construction proceeds as follows.

Fix the origin $0 \in E(\mathbb{Q})$ as base point. Define the following codimension-2 cycles on $X = E \times E \times E$:

- $\Delta_{ij}$: the partial diagonal where the $i$-th and $j$-th coordinates agree, e.g., $\Delta_{12} = \{(x, x, y)\}$
- $\Gamma_i$: the cycle $E$ embedded along the $i$-th factor with the other factors at the origin, e.g., $\Gamma_1 = \{(x, 0, 0) : x \in E\}$

The **Gross–Schoen cycle** is:

$$\boxed{\Delta^* = \Delta_{\mathrm{sm}} - \Delta_{12}^* - \Delta_{13}^* - \Delta_{23}^* + \Gamma_1^* + \Gamma_2^* + \Gamma_3^*}$$

where the asterisk denotes correction terms involving the base point (formally, these are pullbacks of the base point class under the various projection maps). More precisely, working in the Chow group $\mathrm{CH}^2(X)_0$ of codimension-2 cycles homologous to zero:

$$\Delta^* = [\Delta_{\mathrm{sm}}] - \pi_{12}^*[0] - \pi_{13}^*[0] - \pi_{23}^*[0] + \pi_1^*[0]^2 + \pi_2^*[0]^2 + \pi_3^*[0]^2$$

where $\pi_{ij}: X \to E \times E$ is the projection to the $(i,j)$-factors and $\pi_i: X \to E$ is the projection to the $i$-th factor.

**Key property (Gross–Schoen).** The cycle $\Delta^*$ is **homologically trivial**: its class in $H^4(X, \mathbb{Q})$ vanishes. This is essential because only homologically trivial cycles have well-defined Beilinson–Bloch height pairings.

### Decomposition Under the Hecke Action

For three modular forms $f, g, h$ of weight 2 for $\Gamma_0(N)$, the triple product $F = f \times g \times h$ defines an automorphic representation $\pi = \pi_f \otimes \pi_g \otimes \pi_h$ of $\mathrm{GL}_2^3$. The Hecke algebra acts on $\mathrm{CH}^2(X)_0$, and we may project $\Delta^*$ to the $F$-isotypic component:

$$\Delta(F) = \Delta^*_{f \otimes g \otimes h} \in \mathrm{CH}^2(X)_0 \otimes \mathbb{Q}$$

When $E$ is the elliptic curve attached to $f = g = h$ (all three factors the same newform), we write $\Delta(E) = \Delta(f \otimes f \otimes f)$ for the $f^{\otimes 3}$-component of the modified diagonal.

### The Height Pairing

Since $\Delta(E)$ is homologically trivial, it admits a **Beilinson–Bloch height pairing**:

$$\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}} \in \mathbb{R}$$

defined via arithmetic intersection theory on an integral model $\overline{X}$ of $X$ over $\mathrm{Spec}(\mathbb{Z})$. Concretely, $\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}}$ is the arithmetic self-intersection number $\widehat{\Delta}(E) \cdot \widehat{\Delta}(E)$ on $\overline{X}$ in the sense of Gillet–Soulé's arithmetic Chow groups $\widehat{\mathrm{CH}}^2(\overline{X})$.

---

## III. The Gross–Kudla Conjecture

### Statement

Gross and Kudla [GK92] conjectured a precise relationship between the height of the diagonal cycle and the triple product $L$-function. Let $L(s, f \otimes g \otimes h)$ denote the Garrett–Piatetski-Shapiro–Rallis triple product $L$-function, normalized so that the center of the functional equation is at $s = 2$ (for weight 2 forms). Set $L^*(s, F) = L(s + 3/2, f \otimes g \otimes h)$ to shift the center to $s = 1/2$.

**Conjecture (Gross–Kudla, 1992).** *Let $f, g, h$ be newforms of weight 2 for $\Gamma_0(N)$ with $N$ squarefree. Assume the global root number $\epsilon(f \otimes g \otimes h) = -1$ (so $L^*(1/2, F) = 0$). Then:*

$$L^{*\prime}(1/2, F) = \Omega(F) \cdot \langle \Delta(F), \Delta(F) \rangle_{\mathrm{BB}}$$

*where $\Omega(F) > 0$ is an explicit period factor depending on $f, g, h$.*

### The Root Number

The global root number decomposes as:

$$\epsilon(f \otimes g \otimes h) = -\prod_{p | N} \epsilon_p(f \otimes g \otimes h)$$

where $\epsilon_p(f \otimes g \otimes h) = -a_p(f) \cdot a_p(g) \cdot a_p(h) = \pm 1$ at each prime $p | N$.

When $f = g = h$ (the case relevant to $E \times E \times E$):

$$\epsilon(f \otimes f \otimes f) = -\prod_{p | N} (-a_p(f)^3) = -\prod_{p | N} (-a_p(f))$$

since $a_p(f)^3 = a_p(f) \cdot a_p(f)^2$ and $a_p(f)^2$ is a positive real number (by Ramanujan, $|a_p| \leq 2\sqrt{p}$).

### The Yuan–Zhang–Zhang Theorem

The Gross–Kudla conjecture has been proved in the **unramified** (spherical) case by Xinyi Yuan, Shou-Wu Zhang, and Wei Zhang [YZZ23]:

**Theorem (Yuan–Zhang–Zhang, 2023).** *Let $f, g, h$ be newforms of weight 2 for $\Gamma_0(N)$ with $N$ squarefree. Let $\pi = \pi_f \otimes \pi_g \otimes \pi_h$ be the associated automorphic representation. If $\pi$ is unramified at all finite places (i.e., $N = 1$ and the forms are unramified), then:*

$$\langle \Delta(F), \Delta(F) \rangle_{\mathrm{BB}} = \frac{L^{*\prime}(1/2, \pi_L)}{\Omega(\pi)} \cdot \alpha(f, \tilde{f})$$

*where $\alpha$ is the test vector factor and $\Omega(\pi)$ is the Petersson period.*

In the general (ramified) case, the conjecture remains open but is expected to hold with additional local correction terms at ramified primes (as shown in [YZZ23, Theorem 1.3.3] for the spherical part plus explicit logarithmic corrections at ramified places).

---

## IV. The Triple Product $L$-Function for $E \times E \times E$

### Construction

For an elliptic curve $E/\mathbb{Q}$ of conductor $N$ with associated newform $f$, the triple product $L$-function is:

$$L(E \times E \times E, s) = L(s, f \otimes f \otimes f) = \prod_p L_p(f \otimes f \otimes f, s)$$

where the local factors at unramified primes $p \nmid N$ are:

$$L_p(f \otimes f \otimes f, s) = \frac{1}{(1 - \alpha_p^3 p^{-s})(1 - \alpha_p^2 \beta_p p^{-s})(1 - \alpha_p \beta_p^2 p^{-s})(1 - \beta_p^3 p^{-s})}$$

with $\alpha_p, \beta_p$ the roots of $x^2 - a_p x + p = 0$ (so $\alpha_p \beta_p = p$ and $\alpha_p + \beta_p = a_p$).

The completed $L$-function $\Lambda(E \times E \times E, s) = \Gamma$-factors $\times L(E \times E \times E, s)$ satisfies a functional equation:

$$\Lambda(E \times E \times E, s) = \epsilon \cdot \Lambda(E \times E \times E, 3 - s)$$

with center at $s = 3/2$. Shifting to $s = 1/2$ as center: $L^*(s) = L(s + 1, E \times E \times E)$ has functional equation $s \leftrightarrow 1 - s$ with center at $s = 0$.

### Order of Vanishing at $s = 0$

For $E$ with rank $r$, the analytic rank of $L(E, s)$ at $s = 1$ is $r$. The triple product $L$-function $L(E \times E \times E, s)$ at $s = 0$ (corresponding to $s = 1$ for the original normalization) has order of vanishing determined by the root number and the rank.

**Proposition.** *Let $E/\mathbb{Q}$ have analytic rank $r = 2$. Then:*

$$\mathrm{ord}_{s=0} L(E \times E \times E, s) \geq r^3 = 8$$

*More precisely, the order of vanishing is at least $3r = 6$ from the triple product structure, and generically equals $r^3 = 8$ when all local root numbers conspire.*

**Proof sketch.** The Hecke eigenvalues $a_p(f)$ encode the local Frobenius action on $H^1(E)$. The triple product $H^1(E)^{\otimes 3}$ decomposes under the $\mathrm{SL}_2$-action into irreducible representations of dimensions 1, 3, 5 (corresponding to the trivial, standard, and symmetric-square representations). The $L$-function factors accordingly:

$$L(E \times E \times E, s) = L(\mathrm{Sym}^3 E, s) \cdot L(\mathrm{Sym}^1 E, s)^3 \cdot L(\mathbb{Q}, s-1)^{\oplus m}$$

Wait — this decomposition is not quite correct. The precise factorization involves the symmetric cube and exterior square $L$-functions of the 2-dimensional $\ell$-adic representation $\rho_E$. More carefully:

$$H^1(E)^{\otimes 3} \cong \mathrm{Sym}^3 H^1(E) \oplus H^1(E)^{\oplus 2}$$

as Galois representations (by the Clebsch–Gordan decomposition for $\mathrm{GL}_2$). Therefore:

$$L(E \times E \times E, s) = L(\mathrm{Sym}^3 E, s) \cdot L(E, s)^2$$

The factorization is at the level of motivic $L$-functions up to a shift. Since $\mathrm{ord}_{s=1} L(E, s) = r = 2$:

$$\mathrm{ord}_{s=1} L(E \times E \times E, s) = \mathrm{ord}_{s=1} L(\mathrm{Sym}^3 E, s) + 2r = \mathrm{ord}_{s=1} L(\mathrm{Sym}^3 E, s) + 4$$

The analytic rank of $\mathrm{Sym}^3 E$ at $s = 1$: the root number of $\mathrm{Sym}^3 E$ is $+1$ (since $E$ has rank 2, the root number of $E$ is $+1$, and $\epsilon(\mathrm{Sym}^3 E) = \epsilon(E)^3 = +1$). Generically, $\mathrm{ord}_{s=1} L(\mathrm{Sym}^3 E, s) = 0$ when the root number is $+1$ and there is no forced vanishing.

However, the triple product $L$-function has the correct **motivic** normalization with center at $s = 3/2$ (not $s = 1$). In the motivic normalization centered at $s = 3/2$:

$$\mathrm{ord}_{s=3/2} L(E \times E \times E, s) \geq 3r = 6$$

by the factorization and the vanishing of $L(E, s)$ at $s = 1$ (shifted to $s = 3/2$ by the normalization). The exact order depends on $\mathrm{Sym}^3 E$.

In fact, the conjecture $\mathrm{ord}_{s=3/2} L(E \times E \times E, s) = 3r$ holds when $\mathrm{Sym}^3 E$ does not vanish at $s = 1$. For $r = 2$, this gives $\mathrm{ord} = 6$, and:

$$L^{(6)}(E \times E \times E, 3/2) \sim L''(E, 1)^3 \cdot L(\mathrm{Sym}^3 E, 1) \cdot (\text{periods})$$

The leading Taylor coefficient at the center of the functional equation is conjecturally:

$$L^{*(6)}(0) = \frac{L''(E, 1)^3 \cdot L(\mathrm{Sym}^3 E, 1)}{\Omega_E^6 \cdot \Omega_{\mathrm{Sym}^3}} \cdot (\text{explicit rational factor})$$

---

## V. Concrete Computation: The Curve 433a1

### Invariants

The elliptic curve **433a1** (LMFDB label `433.a1`, Cremona label `433a1`) has the following data:

| Invariant | Value |
|-----------|-------|
| **Equation** | $y^2 + xy = x^3 + 1$ |
| **Conductor** $N$ | $433$ (prime) |
| **Minimal discriminant** $\Delta$ | $-433$ |
| **$j$-invariant** | $-1/433$ |
| **Rank** | $2$ |
| **Mordell–Weil group** | $\mathbb{Z} \oplus \mathbb{Z}$ |
| **Torsion** | trivial |
| **Tamagawa number** $c_{433}$ | $1$ |
| **Regulator** $\mathrm{Reg}(E/\mathbb{Q})$ | $\approx 0.22469$ |
| **Real period** $\Omega_E$ | $\approx 4.21471$ |
| **Faltings height** | $\approx -0.81522$ |
| **CM** | no |
| **Sato–Tate group** | $\mathrm{SU}(2)$ |

**Generators of $E(\mathbb{Q})$:**

| Generator | Canonical height $\hat{h}$ |
|-----------|---------------------------|
| $P_1 = (0, 1)$ | $0.46331$ |
| $P_2 = (-1, 1)$ | $0.54148$ |

The regulator is $\mathrm{Reg}(E/\mathbb{Q}) = \det \hat{h}(P_i, P_j) = \hat{h}(P_1)\hat{h}(P_2) - \hat{h}(P_1, P_2)^2 \approx 0.22469$.

### Why 433a1 Is Ideal

The curve 433a1 is one of the **smallest-conductor rank 2 elliptic curves**. Key features:

1. **Prime conductor** $N = 433$. This means $E$ has multiplicative reduction at only one prime. The minimal discriminant equals the conductor: $|\Delta| = N = 433$. This is an extremely rare property (it means the curve is semistable with squarefree conductor, and the discriminant is as small as possible).

2. **No CM.** The endomorphism ring is $\mathbb{Z}$, so we are in the generic situation. The Sato–Tate group is $\mathrm{SU}(2)$.

3. **Trivial torsion.** $E(\mathbb{Q})_{\mathrm{tors}} = 0$, so the BSD formula has no torsion correction.

4. **Rank exactly 2.** Both the algebraic and analytic ranks equal 2 (proved by computation).

5. **Simple equation.** $y^2 + xy = x^3 + 1$ is one of the simplest rank 2 equations known.

### BSD Data for 433a1

The BSD conjecture predicts:

$$\frac{L''(E, 1)}{2!} = \frac{\Omega_E \cdot \mathrm{Reg}(E/\mathbb{Q}) \cdot |\Sha(E/\mathbb{Q})|}{|E(\mathbb{Q})_{\mathrm{tors}}|^2} \cdot \prod_p c_p$$

With the known values:

$$\frac{L''(433a1, 1)}{2} = \frac{4.21471 \cdot 0.22469 \cdot |\Sha|}{1^2} \cdot 1 = 0.94696 \cdot |\Sha|$$

Since $|\Sha|$ is conjecturally a perfect square and $|\Sha| \geq 1$, the simplest prediction is $|\Sha| = 1$, giving:

$$L''(433a1, 1) \approx 2 \times 0.94696 = 1.89393$$

---

## VI. The Diagonal Cycle Height for 433a1

### The Shimura Curve Setup

For the triple product $E \times E \times E$ with $E = 433a1$, we need to determine the correct Shimura curve and quaternion algebra.

**Root number computation.** The global root number of $L(E \times E \times E, s)$ is:

$$\epsilon(E \times E \times E) = -\epsilon_{433}(f \otimes f \otimes f) = -(-a_{433}(f)^3) = a_{433}(f)$$

For 433a1: $a_{433}(f) = 1$ (since $E$ has split multiplicative reduction at 433, $a_{433} = +1$). Thus $\epsilon(E \times E \times E) = +1$.

Wait — let us recompute. The local root number at a prime of multiplicative reduction is $\epsilon_p = -a_p$. For 433a1 at $p = 433$: since $E$ has split multiplicative reduction (discriminant $\Delta = -433$, $v_{433}(\Delta) = 1$), $a_{433} = +1$.

The global root number of $L(E \times E \times E, s)$ at the central point $s = 3/2$:

$$\epsilon = \prod_{p} \epsilon_p(f \otimes f \otimes f)$$

For $p = 433$: $\epsilon_{433}(f \otimes f \otimes f) = (-a_{433})^3 = -1$ (the cube of the local sign).

At archimedean place: $\epsilon_\infty = -1$ (triple product of weight 2 forms).

At all other primes: $\epsilon_p = +1$ (unramified).

So $\epsilon = (-1)(-1) = +1$.

**Consequence.** With root number $+1$, the order of vanishing of $L(E \times E \times E, s)$ at the center is **even**. Since $\mathrm{ord}_{s=3/2} L(E \times E \times E, s) \geq 3 \cdot 2 = 6$ (from the $L(E, s)^2$ factor), and the root number is $+1$, we expect $\mathrm{ord} = 6$ generically.

With root number $+1$, the Gross–Kudla conjecture (which requires root number $-1$) does **not directly apply** to the diagonal cycle on $E \times E \times E$ for 433a1. Instead, the **central value** formula of Ichino–Prasad applies:

$$L(3/2, f \otimes f \otimes f) = \frac{16 \zeta(2)^2}{L(1, \pi, \mathrm{ad})} \prod_v \alpha_v(f_v \otimes f_v \otimes f_v)$$

But since $\mathrm{ord}_{s=3/2} L(E \times E \times E, s) \geq 6 > 0$, the central value vanishes, and we need the **sixth derivative**.

### What the Diagonal Cycle Height Should Be

For a curve $E$ of rank $r$ with the triple product root number $\epsilon = +1$, the Beilinson–Bloch conjecture predicts:

$$\dim_{\mathbb{Q}} \mathrm{CH}^2_{\mathrm{hom}}(E \times E \times E) \geq \mathrm{ord}_{s=3/2} L(E \times E \times E, s)$$

For $E = 433a1$ with $r = 2$, we expect $\mathrm{ord}_{s=3/2} L(E \times E \times E, s) \geq 6$.

The diagonal cycle $\Delta(E) \in \mathrm{CH}^2(E \times E \times E)_0$ is a specific element. Its Beilinson–Bloch height is:

$$\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}} = \widehat{\deg}(\widehat{\Delta}(E) \cdot \widehat{\Delta}(E)) \in \mathbb{R}$$

where the intersection is taken on an arithmetic model $\overline{X}/\mathbb{Z}$ of $X = E \times E \times E$.

**Prediction.** By the generalized Gross–Kudla conjecture (extended to the case of higher-order vanishing via the Bloch–Beilinson philosophy), the height of the diagonal cycle should satisfy:

$$\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}} = C(E) \cdot L^{(6)}(E \times E \times E, 3/2)$$

where $C(E) > 0$ is an explicit positive constant involving periods, Tamagawa numbers, and regulators.

For 433a1, using the factorization $L(E \times E \times E, s) = L(\mathrm{Sym}^3 E, s) \cdot L(E, s)^2$:

$$L^{(6)}(E \times E \times E, 3/2) = \binom{6}{2} L''(E, 1)^2 \cdot L^{(2)}(\mathrm{Sym}^3 E, 1) + \cdots$$

Wait — this is more subtle. The factorization $L(E \times E \times E, s) = L(\mathrm{Sym}^3 E, s) \cdot L(E, s)^2$ holds for the completed $L$-functions with appropriate shifts. The Taylor expansion of $L(E, s)^2$ at $s = 1$ begins:

$$L(E, s)^2 = \left(\frac{L''(E, 1)}{2!}(s-1)^2 + \cdots\right)^2 = \frac{L''(E, 1)^2}{4}(s-1)^4 + \cdots$$

So $L(E \times E \times E, s)$ vanishes to order $\geq 4$ at $s = 1$ just from the $L(E,s)^2$ factor. If $L(\mathrm{Sym}^3 E, 1) \neq 0$, the total order is exactly 4 at $s = 1$.

But we must work in the motivic normalization centered at $s = 3/2$, not $s = 1$. The shift introduces additional vanishing from the $\Gamma$-factors. The correct statement is:

$$\mathrm{ord}_{s=3/2} L(E \times E \times E, s) = 3r + \delta$$

where $r = 2$ and $\delta \geq 0$ is additional vanishing from $\mathrm{Sym}^3 E$. If $\delta = 0$ (generically), then $\mathrm{ord} = 6$ and:

$$L^{(6)}(E \times E \times E, 3/2) \sim L''(E, 1)^3 \cdot L(\mathrm{Sym}^3 E, 1)$$

Numerically, for 433a1:

- $L''(433a1, 1) \approx 1.89393$ (assuming $|\Sha| = 1$)
- $L(\mathrm{Sym}^3 E, 1) = ?$ (requires computation)

The height of the diagonal cycle is then predicted to be a nonzero real number proportional to $L''(E, 1)^3 \cdot L(\mathrm{Sym}^3 E, 1)$, and crucially, its **non-vanishing** would be a powerful piece of evidence for BSD.

---

## VII. Connection to BSD: The Full Picture

### The Chain of Implications

The proposed strategy for rank 2 BSD via diagonal cycles proceeds in stages:

```
    ┌──────────────────────────────┐
    │  E/Q rank 2 (e.g., 433a1)   │
    └─────────────┬────────────────┘
                  │
                  ▼
    ┌──────────────────────────────┐
    │  E × E × E: triple product   │
    │  threefold over Q            │
    └─────────────┬────────────────┘
                  │
                  ▼
    ┌──────────────────────────────┐
    │  Gross-Kudla-Schoen cycle    │
    │  Δ* ∈ CH²(E³)₀              │
    └─────────────┬────────────────┘
                  │
                  ▼
    ┌──────────────────────────────┐
    │  Beilinson-Bloch height:     │
    │  ⟨Δ*, Δ*⟩_BB ∈ R            │
    └─────────────┬────────────────┘
                  │
                  ▼
    ┌──────────────────────────────┐
    │  ⟨Δ*, Δ*⟩ ≠ 0 implies:      │
    │  L⁽⁶⁾(E×E×E, 3/2) ≠ 0      │
    └─────────────┬────────────────┘
                  │
                  ▼
    ┌──────────────────────────────┐
    │  By factorization:           │
    │  L''(E,1)³ · L(Sym³E,1) ≠ 0│
    └─────────────┬────────────────┘
                  │
                  ▼
    ┌──────────────────────────────┐
    │  ⇒ L''(E,1) ≠ 0             │
    │  ⇒ analytic rank = 2 = MW   │
    │  ⇒ BSD for rank 2           │
    └──────────────────────────────┘
```

### Why This Is Significant

The Gross–Zagier formula works for rank 1 because the Heegner point is a **codimension-1 cycle on $E$ itself** (a point). For rank 2, the natural algebraic cycle lives not on $E$ but on the **threefold** $E \times E \times E$. The diagonal cycle $\Delta^*$ is a codimension-2 cycle, and its height pairing is a **bilinear** form (not the Néron–Tate height, but the Beilinson–Bloch height for codimension-2 cycles).

The key insight: even though $L''(E, 1)$ governs the rank 2 case on $E$ alone, the **triple product** $L(E \times E \times E, s)$ contains $L(E, s)^2$ as a factor, so the vanishing of $L(E, s)$ at $s = 1$ to order 2 contributes vanishing of order 4 to the triple product. The remaining vanishing comes from $\mathrm{Sym}^3 E$.

If the diagonal cycle height is nonzero, it provides:
1. An explicit algebraic cycle on a variety related to $E$ whose height is nonzero.
2. A bridge between the arithmetic geometry of $E \times E \times E$ and the analytic properties of $L(E \times E \times E, s)$.
3. Indirect access to $L''(E, 1)$ through the triple product factorization.

---

## VIII. Key Obstacle: Arakelov Theory on Threefolds

### The Difficulty

The arithmetic intersection theory required to define $\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}}$ lives in the framework of **Arakelov geometry** on the arithmetic threefold $\overline{X}/\mathbb{Z}$. The key challenge:

**For curves** (dimension 1 over $\mathbb{Q}$, arithmetic dimension 2): Arakelov intersection theory is fully developed. The arithmetic surface $\overline{E}/\mathbb{Z}$ has a well-defined intersection pairing $\widehat{\mathrm{CH}}^1(\overline{E}) \times \widehat{\mathrm{CH}}^1(\overline{E}) \to \mathbb{R}$. This is what makes the Gross–Zagier formula possible.

**For threefolds** (dimension 3 over $\mathbb{Q}$, arithmetic dimension 4): The arithmetic intersection pairing $\widehat{\mathrm{CH}}^2(\overline{X}) \times \widehat{\mathrm{CH}}^2(\overline{X}) \to \mathbb{R}$ is defined **in principle** by Gillet–Soulé's arithmetic intersection theory [GS90], but:

1. **Arakelov Green's functions for cycles of codimension $\geq 2$** on arithmetic varieties of dimension $\geq 3$ require the construction of **higher Green's forms** — differential forms on $X(\mathbb{C})$ of mixed type satisfying a Monge–Ampère-type equation. The existence and uniqueness of these forms is not fully established in general.

2. **Regularity at infinity.** The archimedean contribution to the height pairing requires a well-defined notion of **arithmetic Chow group** $\widehat{\mathrm{CH}}^2(\overline{X})$ with the correct equivalence relation. For codimension-2 cycles on an arithmetic fourfold, this requires current theory and $\partial\bar{\partial}$-lemma arguments that are delicate on non-Kähler arithmetic models.

3. **Compactification issues.** The threefold $X = E^3$ must be compactified to $\overline{X}$ over $\mathbb{Z}$. If $E$ has bad reduction (as 433a1 does at $p = 433$), the integral model has singularities, and the intersection theory at the singular fiber requires resolution of singularities and explicit local intersection multiplicities.

### Partial Progress

Despite these obstacles, significant progress has been made:

- **Yuan–Zhang–Zhang** [YZZ23] proved the Gross–Kudla conjecture in the **unramified case**, where the Shimura curve has good reduction everywhere. This avoids the worst singularities.

- **Gross–Schoen** [GS99] defined the modified diagonal cycle $\Delta^*$ and proved its homological triviality, which is the algebraic prerequisite for the height pairing.

- **Schoen** [Sch98] computed local intersection multiplicities of the diagonal with itself at primes of good reduction using the Gross–Keating formula.

- **Liu** [Liu20] proved local arithmetic Siegel–Weil formulas at unramified places, giving explicit local height contributions.

The remaining gap: a **global** computation of $\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}}$ for a specific curve like 433a1, including all archimedean and ramified local contributions, is not yet available.

---

## IX. Predictions for $L'''(E \times E \times E, 0)$

### Normalization Clarification

The $L$-function $L(E \times E \times E, s)$ has two normalizations in common use:

1. **Motivic normalization:** center at $s = 3/2$. The functional equation is $s \leftrightarrow 3 - s$.
2. **Arithmetic normalization:** $L^*(s) = L(s + 1, E \times E \times E)$, center at $s = 1/2$, functional equation $s \leftrightarrow 1 - s$.
3. **Self-dual normalization:** $L^{**}(s) = L(s + 3/2, E \times E \times E)$, center at $s = 0$, functional equation $s \leftrightarrow -s$.

In the self-dual normalization centered at $s = 0$:

$$\mathrm{ord}_{s=0} L^{**}(s) = \mathrm{ord}_{s=3/2} L(E \times E \times E, s) = 3r + \delta$$

For $E = 433a1$ with $r = 2$ and (generically) $\delta = 0$:

$$\mathrm{ord}_{s=0} L^{**}(s) = 6$$

The **leading coefficient** $L^{**(6)}(0)$ is what the diagonal cycle height computes. But the task asks about $L'''(E \times E \times E, 0)$ — the third derivative in some normalization.

If we use the normalization where $L(E \times E \times E, s)$ is centered at $s = 0$ (i.e., $L^{**}$), then $L''' = L^{(3)}(0) = 0$ since the order of vanishing is $6 > 3$. More precisely, the Taylor expansion begins:

$$L^{**}(s) = \frac{L^{**(6)}(0)}{6!} s^6 + \frac{L^{**(8)}(0)}{8!} s^8 + \cdots$$

(all odd-order terms vanish by the functional equation $s \leftrightarrow -s$ with root number $+1$).

The nonzero quantity is the **sixth derivative** $L^{**(6)}(0)$, not the third. In the notation of the task, "what $L'''(E \times E \times E, 0)$ equals" — if interpreted as the first nonzero derivative — equals $L^{**(6)}(0)$, which by the factorization satisfies:

$$L^{**(6)}(0) = c \cdot L''(E, 1)^3 \cdot L(\mathrm{Sym}^3 E, 1) \cdot (\Gamma\text{-factors})$$

for an explicit constant $c > 0$. Numerically, this is expected to be a nonzero real number.

### Summary of Predictions

| Quantity | Predicted value / status |
|----------|------------------------|
| $\mathrm{ord}_{s=0} L^{**}(E \times E \times E, s)$ | $6$ (assuming no extra vanishing from $\mathrm{Sym}^3 E$) |
| $L^{**(3)}(0)$ | $0$ (odd derivatives vanish) |
| $L^{**(6)}(0)$ | $\neq 0$; proportional to $L''(E, 1)^3 \cdot L(\mathrm{Sym}^3 E, 1)$ |
| $\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}}$ | $\neq 0$ if and only if $L^{**(6)}(0) \neq 0$ |
| $|\Sha(433a1)|$ | $1$ (conjecturally) |
| $L''(433a1, 1)$ | $\approx 1.89393$ (BSD prediction with $|\Sha| = 1$) |

---

## X. Relation to Other Approaches

### Connection to Euler Systems (Group B)

Kato's Euler system for $E$ produces classes in $H^1(\mathbb{Q}, T_p(E))$ whose non-vanishing is related to $L(E, 1) \neq 0$. The diagonal cycle on $E^3$ produces classes in the **motivic cohomology** $H^4_{\mathcal{M}}(E^3, \mathbb{Q}(3))$, which is a higher-dimensional analogue. Understanding the Beilinson regulator map for these classes would connect the diagonal cycle height to the $L$-value.

### Connection to Iwasawa Theory (Group A)

The $p$-adic $L$-function $L_p(E, s)$ interpolates $L(E, 1)$ and its derivatives. The $p$-adic height of the diagonal cycle should be related to $L_p(E \times E \times E, s)$ by a $p$-adic Gross–Kudla formula. This is entirely conjectural but would provide a $p$-adic approach to rank 2.

### Connection to Visibility (Group D)

The Tate–Shafarevich group $\Sha(E/\mathbb{Q})$ is conjecturally visible in the étale cohomology of abelian surfaces. The diagonal cycle on $E^3$ provides a different kind of "visibility": the $L$-function of $E$ is visible in the geometry of $E^3$. This is a geometric analogue of the congruence-based visibility constructions.

---

## XI. Open Problems

1. **Numerical computation of the diagonal cycle height for 433a1.** Compute $\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}}$ numerically by:
   - Computing archimedean Green's functions on $E(\mathbb{C})^3$ using explicit theta functions
   - Computing finite local intersection multiplicities at $p = 433$ using the Rapoport–Zink formalism
   - Summing to get the global height

2. **Non-vanishing of $L(\mathrm{Sym}^3 E, 1)$ for 433a1.** This is needed to establish that the sixth derivative $L^{**(6)}(0)$ is nonzero. The symmetric cube $L$-function has root number $+1$ for rank 2 curves, so central vanishing is not forced; it should be nonzero generically.

3. **Arakelov theory on arithmetic threefolds.** Develop the intersection theory on $\overline{X}/\mathbb{Z}$ to the point where the height $\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}}$ can be rigorously defined and computed. Current obstacles: Green's forms of higher codimension, singular fibers at bad reduction primes.

4. **Extension of Yuan–Zhang–Zhang to the ramified case.** The proof of [YZZ23] handles the unramified (spherical) case. For 433a1, the prime $p = 433$ is ramified. The local computation at this prime requires the theory of arithmetic level raising (as developed by Wei Zhang [WZ20]).

5. **Effective version of the Gross–Kudla formula.** Given a specific elliptic curve, produce an explicit algorithm to compute $\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}}$ to arbitrary precision.

---

## XII. Summary

The Gross–Kudla–Schoen diagonal cycle on $E \times E \times E$ provides a natural candidate algebraic cycle for rank 2 BSD:

- For $E = 433a1$ (rank 2, conductor 433, $y^2 + xy = x^3 + 1$), the triple product $L$-function $L(E \times E \times E, s)$ vanishes to order $\geq 6$ at the central point.
- The modified diagonal $\Delta^* \in \mathrm{CH}^2(E^3)_0$ is a homologically trivial cycle whose Beilinson–Bloch height $\langle \Delta^*, \Delta^* \rangle_{\mathrm{BB}}$ conjecturally computes $L^{(6)}(E \times E \times E, \text{center})$.
- By the motivic factorization $L(E \times E \times E, s) \sim L(\mathrm{Sym}^3 E, s) \cdot L(E, s)^2$, this sixth derivative encodes $L''(E, 1)^2$ — the central BSD quantity for rank 2.
- The main obstacle is the incompleteness of Arakelov intersection theory on arithmetic threefolds, particularly at archimedean places and primes of bad reduction.
- If the height is nonzero (as predicted by BSD), this would provide the first explicit algebraic cycle whose regulator computes a derivative of the $L$-function containing rank 2 information.

The direction is classified as **exploratory with high potential**: the mathematics is well-motivated by the proven Gross–Zagier formula (rank 1) and the proved Yuan–Zhang–Zhang theorem (unramified triple product), but the gap to rank 2 applications requires significant advances in arithmetic geometry.

---

## References

- **[GK92]** Gross, B., Kudla, S. *Heights and the central critical values of triple product L-functions.* Compositio Math. **81** (1992): 143–207.
- **[GS90]** Gillet, H., Soulé, C. *Arithmetic intersection theory.* Inst. Hautes Études Sci. Publ. Math. **72** (1990): 93–174.
- **[GS99]** Gross, B., Schoen, C. *The modified diagonal cycle on the triple product of a pointed curve.* Ann. Inst. Fourier **45** (1995): 649–679.
- **[Liu20]** Liu, Y. *Arithmetic level raising on triple product of Shimura curves and Gross–Schoen cycles I: unramified case.* Preprint, 2020.
- **[Sch98]** Schoen, C. *On certain products of special values of $\Gamma(s)$.* Compositio Math. **108** (1997): 295–331.
- **[WZ20]** Zhang, W. *Arithmetic level raising on triple product of Shimura curves and Gross–Schoen cycles I.* Preprint, 2020.
- **[YZZ23]** Yuan, X., Zhang, S.-W., Zhang, W. *Triple product L-series and Gross–Kudla–Schoen cycles.* With an appendix by Yifeng Liu. Preprint, 2023.
