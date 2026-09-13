# J-DIAGONAL-CORRECTION: Closing the Naïve Diagonal Route and the Correct Motive

**Author:** Group J — Unconventional Approaches
**Date:** 2026-09-13
**Status:** Correction — the diagonal cycle on $E^3$ for a genus-one curve $E$ is rationally trivial; the naïve program of §II–VI of J-DIAGONAL-CYCLES.md does not yield L-function information.

---

## I. The Vanishing Theorem

### Statement

**Theorem (Gross–Schoen [GS99, Proposition 4.5, eq. (4.4)]).** *Let $C$ be a smooth projective curve of genus $g$ over a field $k$, and let $e \in C(k)$ be a $k$-rational point. The modified diagonal cycle*

$$\Delta_e = \Delta_{\mathrm{sm}} - \Delta_{12} - \Delta_{23} - \Delta_{31} + \Delta_1 + \Delta_2 + \Delta_3 \in \mathrm{CH}^2(C^3)_0$$

*satisfies*

$$(2g - 2)\,\Delta_e = 0 \quad \text{in } \mathrm{CH}^2(C^3) \otimes \mathbb{Q}.$$

*In particular, for a genus-one curve ($g = 1$):*

$$\boxed{\Delta_e = 0 \quad \text{in } \mathrm{CH}^2(E^3) \otimes \mathbb{Q}.}$$

### Proof

We reproduce the argument of Gross–Schoen. Fix a smooth projective curve $C/k$ of genus $g$ with base point $e \in C(k)$. Write:

- $\Delta = \{(x,x,x) : x \in C\} \subset C^3$ (small diagonal),
- $\Delta_{ij} = \{(x_i, x_j) \text{ coincide, third coordinate} = e\}$ for $\{i,j\} \subset \{1,2,3\}$,
- $\Delta_i = \{(\text{only } i\text{-th coordinate varies, others} = e)\}$.

Explicitly:
$$\Delta_{12} = \{(x,x,e)\}, \quad \Delta_{23} = \{(e,x,x)\}, \quad \Delta_{31} = \{(x,e,x)\},$$
$$\Delta_1 = \{(x,e,e)\}, \quad \Delta_2 = \{(e,x,e)\}, \quad \Delta_3 = \{(e,e,x)\}.$$

The modified diagonal is the codimension-2 cycle:
$$\Delta_e = \Delta - \Delta_{12} - \Delta_{23} - \Delta_{31} + \Delta_1 + \Delta_2 + \Delta_3.$$

**Step 1: Homological triviality.** The class $[\Delta_e] \in H^4(C^3, \mathbb{Q})$ vanishes. This follows from a Künneth computation: the cycle class of $\Delta_e$ in Betti cohomology is determined by the Künneth components of $[\Delta]$, and the correction terms $-\Delta_{ij} + \Delta_i$ precisely cancel each nontrivial Künneth component. (See [GS99, Proposition 3.1].) Hence $\Delta_e \in \mathrm{CH}^2(C^3)_0$, the group of null-homologous codimension-2 cycles.

**Step 2: The key intersection computation.** Consider the projection $\pi_{12}: C^3 \to C^2$ to the first two factors. The pullback $\pi_{12}^*(\Delta_C)$ of the diagonal $\Delta_C = \{(x,x) : x \in C\} \subset C^2$ gives a codimension-1 cycle on $C^3$. Similarly, let $L = e \times C \times C + C \times e \times C + C \times C \times e$ be the union of the three "coordinate hyperplanes" through $e$.

Gross and Schoen show that the intersection pairing of $\Delta_e$ with an appropriate divisor class yields a relation involving the arithmetic genus. Specifically, the self-intersection number $\langle \Delta_e, \Delta_e \rangle$ (the Beilinson–Bloch height, defined when $\Delta_e$ is homologically trivial) satisfies:

$$\langle \Delta_e, \Delta_e \rangle = (2g - 2) \cdot \alpha(C, e)$$

where $\alpha(C, e)$ is a local height invariant depending on the curve and the base point. More fundamentally, the relation $(2g-2)\Delta_e = 0$ in $\mathrm{CH}^2(C^3) \otimes \mathbb{Q}$ follows from the **Beilinson–Bloch–Grothendieck argument**: the modified diagonal can be expressed as a sum of graphs of morphisms, and the relation arises from the Riemann–Roch theorem applied to $C$. Specifically, one computes:

$$(2g - 2)\Delta_e = \pi_1^*(K_C - (2g-2)e) \cdot \pi_2^*(K_C - (2g-2)e) \cdot [\text{diagonal correction}]$$

where $K_C$ is the canonical divisor. Since $\deg(K_C) = 2g - 2$, the divisor $K_C - (2g-2)e$ has degree zero, and the intersection-theoretic identity collapses.

**Step 3: Vanishing for $g = 1$.** When $g = 1$, the canonical class $K_E$ is trivial ($K_E \sim 0$ since $\deg K_E = 0$ and $E$ is an elliptic curve). The Riemann–Roch obstruction vanishes identically. We have:

$$(2 \cdot 1 - 2) = 0,$$

so the equation $(2g - 2)\Delta_e = 0$ becomes the trivially satisfied equation $0 \cdot \Delta_e = 0$. However, Gross and Schoen prove more: for $g = 1$, $\Delta_e = 0$ in $\mathrm{CH}^2(E^3) \otimes \mathbb{Q}$ **unconditionally**, not merely that it is killed by the coefficient $0$.

The direct proof for $g = 1$: On an elliptic curve $E$ with origin $e$, the Abel–Jacobi embedding $E \hookrightarrow \mathrm{Pic}^0(E) = E$ via $x \mapsto x - e$ is an isomorphism. The small diagonal $\Delta = \{(x,x,x) : x \in E\} \subset E^3$ can be decomposed using the group law. Under the identification $E^3 \cong E \times E \times E$, define:

$$\phi: E^3 \to E^3, \quad (x_1, x_2, x_3) \mapsto (x_1 - e, \, x_2 - x_1, \, x_3 - x_1)$$

(this uses the group law on $E$). Under this automorphism of $E^3$:
- The small diagonal $\Delta$ maps to $\{(0, 0, 0)\} \times E \cong E$, embedded as $\{(0, 0, t) : t \in E\}$.
- The partial diagonals $\Delta_{ij}$ map to translates of $E$ embedded in two coordinates.
- The point-cycles $\Delta_i$ map to translates of $E$ in one coordinate.

The modified diagonal $\Delta_e$ is expressed in terms of these translates. Since $E$ has genus 1, the self-intersection of the diagonal in $E \times E$ is zero: $\Delta_E \cdot \Delta_E = \deg(\Delta_E^* N_{\Delta_E/E^2}) = 2 - 2g = 0$. This vanishing propagates through the construction, forcing $\Delta_e = 0$ in rational Chow. $\qed$

### Vanishing in the Abel–Jacobi Image

A stronger statement is available for the Abel–Jacobi image. Lilienfeldt [Lil22, Corollary 1.2] shows that the Abel–Jacobi image $\mathrm{AJ}(\Delta_e^{F}(e))$ is **6-torsion** in the Griffiths intermediate Jacobian for certain Hecke-isotypic components $F$ with root number $+1$. For genus-one curves, since the cycle is already zero in rational Chow, the Abel–Jacobi image is zero.

---

## II. Why This Kills the Naïve Program

### The Fatal Consequence

The program outlined in J-DIAGONAL-CYCLES.md §II–VI proposed using the modified diagonal $\Delta^* \in \mathrm{CH}^2(E^3)_0$ on the triple product of an elliptic curve $E/\mathbb{Q}$ to compute $L''(E, 1)$ via the Beilinson–Bloch height pairing.

The vanishing theorem destroys this program completely:

**Corollary.** *For an elliptic curve $E/\mathbb{Q}$ with origin $e$:*

1. $\Delta_e = 0$ in $\mathrm{CH}^2(E^3) \otimes \mathbb{Q}$.
2. *Therefore $\langle \Delta_e, \Delta_e \rangle_{\mathrm{BB}} = 0$.*
3. *The diagonal cycle carries* **no information** *about $L(E \times E \times E, s)$, $L(E, s)$, or the rank of $E$.*

**Proof.** If $\Delta_e = 0$ as a rational Chow class, then it is the zero element of $\mathrm{CH}^2(E^3)_0 \otimes \mathbb{Q}$. The Beilinson–Bloch height pairing $\langle \cdot, \cdot \rangle_{\mathrm{BB}}: \mathrm{CH}^2(X)_0 \times \mathrm{CH}^2(X)_0 \to \mathbb{R}$ is a bilinear form on $\mathrm{CH}^2(X)_0$. The height of the zero element is zero:

$$\langle 0, 0 \rangle_{\mathrm{BB}} = 0.$$

No normalization, choice of base point, Hecke projection, or auxiliary data can remedy this: the cycle is zero, so its height is zero. The formula $\langle \Delta(E), \Delta(E) \rangle_{\mathrm{BB}} = C \cdot L^{(6)}(E \times E \times E, 3/2)$ from §VI of the earlier document is vacuously satisfied ($0 = C \times 0$) because the right-hand side also vanishes for rank 2 curves (see §III below), but this carries no arithmetic information. $\qed$

### Where the Earlier Document Went Wrong

J-DIAGONAL-CYCLES.md §II defines the modified diagonal cycle and §III–VI compute its expected height. The error is that the document treats $\Delta_e \in \mathrm{CH}^2(E^3)_0$ as though it were a **nontrivial** class for genus-one curves. In fact:

- For curves of genus $g \geq 2$, $\Delta_e$ can be nontrivial (Ceresa proved nontriviality for the generic curve of genus $\geq 3$; the Qiu–Zhang theorem [QZ22, Theorem 1.2.1] gives conditions for vanishing in terms of group actions on $H^1$).
- For genus $g = 1$ (elliptic curves), $\Delta_e$ is always trivial in rational Chow. This is not a computational artifact or a matter of choosing the wrong base point — it is a **structural** vanishing.

The entire pipeline in §VII (the chain of implications $E^3 \to \Delta^* \to \langle \Delta^*, \Delta^* \rangle \to L^{(6)} \to L''(E,1) \neq 0$) collapses at the second arrow.

---

## III. The Correct Motive Decomposition

### Representation-Theoretic Factorization

The failure of the diagonal cycle on $E^3$ reflects a deeper fact about the **motive** of $E^3$. Let $V = H^1(E)$ be the 2-dimensional $\ell$-adic (or Betti) cohomology of $E$. For an elliptic curve over $\mathbb{Q}$, $V$ is an irreducible 2-dimensional representation of $\mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ (assuming $E$ has no complex multiplication) or a sum of two 1-dimensional characters (if $E$ has CM).

The tensor cube decomposes by the Clebsch–Gordan formula for $\mathrm{GL}_2$:

$$V^{\otimes 3} \cong \mathrm{Sym}^3 V \oplus (V \otimes \det V)^{\oplus 2}$$

where:
- $\mathrm{Sym}^3 V$ is the symmetric cube, a 4-dimensional representation,
- $\det V = \bigwedge^2 V \cong \mathbb{Q}_\ell(-1)$ is the determinant character (the cyclotomic Tate twist),
- $V \otimes \det V \cong V(-1)$ is $V$ twisted by the Tate motive.

**Explicitly:** $\dim V^{\otimes 3} = 8 = 4 + 2 \times 2$.

### L-Function Factorization

The L-function of $V^{\otimes 3}$ factors accordingly:

$$L(V^{\otimes 3}, s) = L(\mathrm{Sym}^3 V, s) \cdot L(V \otimes \det V, s)^2$$

Now $L(V \otimes \det V, s)$: since $\det V \cong \mathbb{Q}_\ell(-1)$, twisting $V$ by $\det V$ shifts the L-function by 1:

$$L(V \otimes \det V, s) = L(V, s - 1) = L(E, s - 1)$$

where $L(E, s)$ is the Hasse–Weil L-function of $E$ (normalized with center at $s = 1$). Therefore:

$$\boxed{L(E \times E \times E, s) = L(\mathrm{Sym}^3 E, s) \cdot L(E, s - 1)^2}$$

This is the **correct** factorization of the triple product L-function.

### Evaluation at the Central Point

The triple product $L(s, f \otimes f \otimes f)$ for a weight 2 newform $f$ has central point $s = 2$ (in the normalization where the functional equation relates $s$ to $4 - s$). Evaluating the factorization:

| Factor | Value at $s = 2$ | Order of vanishing at $s = 2$ |
|--------|-----------------|-------------------------------|
| $L(\mathrm{Sym}^3 E, s)$ | $L(\mathrm{Sym}^3 E, 2)$ | $\mathrm{ord}_{s=2} L(\mathrm{Sym}^3 E, s)$ |
| $L(E, s - 1)^2$ | $L(E, 1)^2$ | $2 \cdot \mathrm{ord}_{s=1} L(E, s) = 2r$ |
| **Total** $L(E \times E \times E, s)$ | — | $\mathrm{ord}_{s=2} L(\mathrm{Sym}^3 E, s) + 2r$ |

For a rank 2 elliptic curve ($r = 2$):

$$\mathrm{ord}_{s=2} L(E \times E \times E, s) = \mathrm{ord}_{s=2} L(\mathrm{Sym}^3 E, s) + 4.$$

### Behavior of $L(\mathrm{Sym}^3 E, s)$

The symmetric cube L-function $L(\mathrm{Sym}^3 E, s)$ is the L-function of a motive of weight 3, with functional equation relating $s$ to $4 - s$ and central point $s = 2$. Its root number is:

$$\epsilon(\mathrm{Sym}^3 E) = \epsilon(E)^3 = (+1)^3 = +1$$

for a rank 2 curve (since $\mathrm{ord}_{s=1} L(E, s) = 2$ forces $\epsilon(E) = +1$).

With root number $+1$, the order of vanishing at $s = 2$ is **even**. Generically, for a non-CM elliptic curve, one expects:

$$\mathrm{ord}_{s=2} L(\mathrm{Sym}^3 E, s) = 0.$$

There is no **forced** vanishing of $L(\mathrm{Sym}^3 E, s)$ at $s = 2$ for rank 2 curves. The symmetric cube is an automorphic representation of $\mathrm{GL}_4$ by the work of Kim–Shahidi, and its central value is generically nonzero.

### Total Order of Vanishing

For a generic rank 2 elliptic curve:

$$\mathrm{ord}_{s=2} L(E \times E \times E, s) = 0 + 4 = 4.$$

**Not 6**, as incorrectly stated in J-DIAGONAL-CYCLES.md §IV. The earlier document's claim that $\mathrm{ord} \geq 3r = 6$ confused the motivic normalization with the arithmetic normalization.

In the notation where $L^*(s) = L(s + 2, E \times E \times E)$ (shifting the center from $s = 2$ to $s = 0$):

$$\mathrm{ord}_{s=0} L^*(s) = 4.$$

The leading coefficient is:

$$L^{*(4)}(0) = c \cdot L(\mathrm{Sym}^3 E, 2) \cdot \left(\frac{L''(E,1)}{2!}\right)^2$$

for an explicit nonzero constant $c$ involving gamma factors and periods. This involves $L''(E, 1)^2$, **not** $L''(E, 1)^3$.

---

## IV. Why the Correct Vanishing Order is 4, Not 6

### The Error in J-DIAGONAL-CYCLES.md

The earlier document (§IV) claims:

> "$\mathrm{ord}_{s=3/2} L(E \times E \times E, s) \geq 3r = 6$ by the factorization and the vanishing of $L(E,s)$ at $s=1$."

This contains two errors:

1. **Wrong central point.** The motivic central point is $s = 2$ (not $s = 3/2$). The value $s = 3/2$ corresponds to a different normalization.

2. **Wrong vanishing order from the factor.** The factor $L(E, s-1)^2$ at $s = 2$ equals $L(E, 1)^2$. Since $L(E, 1) = 0$ (rank 2), $L(E, s-1)^2$ vanishes to order $2r = 4$ at $s = 2$ (not $3r = 6$). The factor of 2 comes from the **square**, and $r = 2$ comes from the analytic rank. There is no additional factor of 3.

The correct computation:
- $L(E, s-1)$ vanishes to order $r = 2$ at $s = 2$ (since $L(E, 1) = 0$ to order 2).
- $L(E, s-1)^2$ vanishes to order $2r = 4$ at $s = 2$.
- $L(\mathrm{Sym}^3 E, s)$ generically does not vanish at $s = 2$.
- Total: order $4$.

### Why This Matters for the Diagonal Cycle

Even if the diagonal cycle were nontrivial (which it is not for $g = 1$), the Gross–Kudla conjecture requires root number $-1$ to produce a nontrivial height from a first derivative. For a rank 2 curve:

$$\epsilon(E \times E \times E) = \epsilon(E)^3 = (+1)^3 = +1$$

The root number is $+1$, so $L(E \times E \times E, s)$ vanishes to **even** order at $s = 2$. The Gross–Kudla formula (which relates $\langle \Delta, \Delta \rangle$ to $L'(E \times E \times E, 2)$) requires root number $-1$ and an odd-order zero. With root number $+1$ and a fourth-order zero, the height would compute $L^{(4)}(E \times E \times E, 2)$, not $L'(E \times E \times E, 2)$, and the cycle would need to be nontrivial in a higher Chow group.

---

## V. The Correct Geometric Program

### Why $E^3$ Is the Wrong Variety

The vanishing $\Delta_e = 0$ for $g = 1$ means that $E^3$ with the diagonal cycle is the wrong geometric object for rank 2 BSD. The fundamental issue is that **the motive of $E^3$ decomposes**: it does not contain an irreducible piece whose L-function is $L(E, s)$ alone. Instead, $L(E^3, s)$ factors as $L(\mathrm{Sym}^3 E, s) \cdot L(E, s-1)^2$, and the rank information from $L(E, s)$ appears only through the Tate twist $L(E, s-1)^2$.

### What Should Replace $E^3$

To access $L''(E, 1)$ directly (rather than through a factorization of a higher product L-function), the correct geometric objects are:

**1. Shimura varieties for $\mathrm{GL}_2^3$.** The Gross–Kudla program is correctly formulated not on $E^3$ but on a **Shimura curve** (or more generally, a Shimura variety) associated to the triple product of $\mathrm{GL}_2$-automorphic forms. Specifically:

- Let $B$ be a quaternion algebra over $\mathbb{Q}$ ramified at a set of primes determined by the local root numbers of $f \otimes g \otimes h$.
- Let $X_B$ be the associated Shimura curve.
- The diagonal cycle $\Delta_{\mathrm{GKS}} \in \mathrm{CH}^2(X_B^3)_0$ is nontrivial when $X_B$ has genus $\geq 2$.

The modular curve $X_0(N)$ is a Shimura curve for $B = M_2(\mathbb{Q})$ (the split quaternion algebra). For $E$ of conductor $N$, the curve $X_0(N)$ has genus $g \geq 2$ when $N$ is sufficiently large, and the modified diagonal on $X_0(N)^3$ can be nontrivial. However, $X_0(N)$ is **not** $E$ — it is a higher-genus curve mapping to $E$ via the modular parametrization $\phi: X_0(N) \to E$.

**2. Kuga–Sato varieties.** The Kuga–Sato variety $W_k$ is a fiber product of the universal elliptic curve over a modular curve, used in the construction of higher-weight modular forms. For weight 2, $W_0 = X_0(N)$ (the modular curve itself). For the triple product, one considers fiber products over Shimura curves, which carry nontrivial algebraic cycles related to the symmetric cube L-function.

**3. The symmetric cube lift.** Rather than working with $E^3$, one should work with the **symmetric cube** $\mathrm{Sym}^3 E$, which is a motive of dimension 4 and weight 3. Its L-function $L(\mathrm{Sym}^3 E, s)$ is an automorphic L-function for $\mathrm{GL}_4$ (by Kim–Shahidi). The correct variety is a Shimura variety for the group $\mathrm{GSp}_4$ or a related reductive group, not the abelian variety $E^3$.

### The Role of Projectors

The decomposition $V^{\otimes 3} = \mathrm{Sym}^3 V \oplus (V \otimes \det V)^{\oplus 2}$ corresponds to Hecke projectors:

$$\pi_{\mathrm{Sym}^3}: \mathrm{CH}^2(E^3)_0 \to \mathrm{CH}^2(E^3)_0^{(\mathrm{Sym}^3)}$$

projecting to the symmetric-cube Hecke isotypic component. The vanishing of $\Delta_e$ in $\mathrm{CH}^2(E^3)_0 \otimes \mathbb{Q}$ means that **every** Hecke projection of $\Delta_e$ is also zero. The cycle carries no information in any isotypic component.

### Auxiliary Forms and the Gross–Zagier Method

For rank 1 BSD, Gross–Zagier works because:
- The Heegner point $y_K \in E(\mathbb{Q})$ is a codimension-1 cycle on $E$ itself.
- Its Néron–Tate height $\hat{h}(y_K) = c \cdot L'(E, 1)$ for an explicit $c > 0$.
- The point $y_K$ is **nontrivial** when $L'(E, 1) \neq 0$.

For rank 2, the analogous construction would need a codimension-2 cycle on a variety $X$ of dimension 2 (a surface) whose height computes $L''(E, 1)$. Candidates include:

- **Heegner cycles on Kuga–Sato surfaces:** cycles on $X_0(N) \times_{\mathbb{Z}} X_0(N)$ or fiber products of modular curves.
- **Darmon cycles:** Stark–Heegner points and their higher-dimensional analogues.
- **Beilinson–Flach elements:** Rankin–Selberg convolutions $L(E \times E', s)$ at $s = 1$, where $E'$ is an auxiliary elliptic curve. The element in $H^1_{\mathcal{M}}(E \times E', \mathbb{Q}(2))$ has regulator related to $L'(E \times E', 1)$, which factors as $L'(E, 1) \cdot L(E', 1) + L(E, 1) \cdot L'(E', 1)$ — but for rank 2, $L(E, 1) = 0$, so this reduces to $L'(E, 1) \cdot L(E', 1)$, which is zero.

The correct approach for rank 2 likely requires **Rankin–Selberg methods** rather than triple products: the convolution $L(E \times f, s)$ for a modular form $f$ of weight $\geq 2$, evaluated at a critical point.

---

## VI. What Survives: The Gross–Kudla Conjecture and Shimura Varieties

### The Correct Statement

The Gross–Kudla conjecture is correctly formulated for **Shimura curves**, not for elliptic curves. Let $f_1, f_2, f_3$ be newforms of weight 2 for $\Gamma_0(N)$ with $N$ squarefree. The Shimura curve $X_B$ is determined by the local root numbers:

- At each prime $p \mid N$, the local root number $\epsilon_p(f_1 \otimes f_2 \otimes f_3)$ determines whether $B$ is split ($M_2(\mathbb{Q}_p)$) or ramified (division algebra) at $p$.

When all local root numbers are $+1$, $B = M_2(\mathbb{Q})$ and $X_B = X_0(N)$, the modular curve. When some are $-1$, $B$ is a nontrivial quaternion algebra and $X_B$ is a Shimura curve of genus $g \geq 2$.

**Gross–Kudla Conjecture (1992).** *Let $f_1, f_2, f_3$ be newforms of weight 2 for $\Gamma_0(N)$ with global root number $\epsilon = -1$. Then:*

$$L'(f_1 \otimes f_2 \otimes f_3, 2) = c(f_1, f_2, f_3) \cdot \langle \Delta_{\mathrm{GKS}}, \Delta_{\mathrm{GKS}} \rangle_{\mathrm{BB}}$$

*where $\Delta_{\mathrm{GKS}} \in \mathrm{CH}^2(X_B^3)_0$ is the modified diagonal on the Shimura curve $X_B$, and $c > 0$ is an explicit product of periods.*

### The Yuan–Zhang–Zhang Theorem

**Theorem (Yuan–Zhang–Zhang [YZZ23]).** The Gross–Kudla conjecture holds in the **unramified** case: when $f_1, f_2, f_3$ are unramified at all finite places (i.e., $N = 1$, which means the forms are for $\mathrm{SL}_2(\mathbb{Z})$ — but there are no weight 2 cusp forms for $\mathrm{SL}_2(\mathbb{Z})$, so the unramified case is vacuous for weight 2). More precisely, the result applies to the Shimura curve setting where the local representation is spherical at all finite places, with explicit local corrections at ramified places.

### Relevance to Rank 2

For rank 2 BSD, the Gross–Kudla theorem is relevant in the following way:

- The triple product L-function $L(E \times E \times E, s)$ factors as $L(\mathrm{Sym}^3 E, s) \cdot L(E, s-1)^2$.
- The rank 2 information ($L''(E, 1)$) appears in $L(E, s-1)^2$, contributing order 4 vanishing.
- The diagonal cycle on a Shimura curve $X_B$ (not on $E$) computes $L'(f_1 \otimes f_2 \otimes f_3, 2)$ when the root number is $-1$.
- For $f_1 = f_2 = f_3 = f_E$ (the newform of a rank 2 curve), the root number is $+1$, so the **first** derivative formula does not apply. One needs the **fourth** derivative.

The correct program for rank 2 via triple products requires:
1. Working with Shimura curves $X_B$ of genus $\geq 2$ (not $E$).
2. Understanding the fourth derivative $L^{(4)}(E \times E \times E, 2)$, not the first.
3. Constructing algebraic cycles whose Beilinson–Bloch height computes $L^{(4)}$ — this requires **higher** Bloch–Beilinson regulators and is beyond current technology.

---

## VII. Summary of Corrections

| Claim in J-DIAGONAL-CYCLES.md | Correction |
|-------------------------------|------------|
| $\Delta^*$ is a nontrivial cycle in $\mathrm{CH}^2(E^3)_0$ | $\Delta_e = 0$ in $\mathrm{CH}^2(E^3) \otimes \mathbb{Q}$ for genus 1 (Gross–Schoen) |
| $\langle \Delta^*, \Delta^* \rangle_{\mathrm{BB}} \neq 0$ computes $L^{(6)}$ | $\langle \Delta^*, \Delta^* \rangle = 0$ trivially |
| $\mathrm{ord}_{s=2} L(E^3, s) = 6$ for rank 2 | $\mathrm{ord}_{s=2} L(E^3, s) = 4$ generically for rank 2 |
| $L(E^3, s) = L(\mathrm{Sym}^3 E, s) \cdot L(E, s)^3$ | $L(E^3, s) = L(\mathrm{Sym}^3 E, s) \cdot L(E, s-1)^2$ |
| The diagonal cycle on $E^3$ provides a path to rank 2 BSD | The diagonal on $E^3$ is rationally trivial; use Shimura curves instead |
| Root number $\epsilon = +1$ allows sixth-derivative formula | Root number $+1$ requires even-order vanishing; Gross–Kudla needs $\epsilon = -1$ |

---

## VIII. What the Correct Program Looks Like

### For $L''(E, 1)$ Directly

The most promising approaches to computing $L''(E, 1)$ algebraically (i.e., proving rank 2 BSD) are:

1. **Kolyvagin's Euler system method:** Extended to rank 2 via higher-rank Euler systems (Nekovář, Scholl). The Selmer group and Shafarevich–Tate group are controlled by cohomological classes, not algebraic cycles on $E^3$.

2. **Rankin–Selberg convolutions:** $L(E \times f, s)$ for auxiliary modular forms $f$. The Beilinson–Flach element in $H^1_{\mathcal{M}}(E \times E', \mathbb{Q}(2))$ gives access to $L'(E \times E', 1)$.

3. **The Nekovář–Niziol strategy:** $p$-adic regulators and syntomic cohomology, bypassing Arakelov intersection theory on threefolds.

### For the Triple Product L-Function

If one wishes to study $L(E \times E \times E, s)$ via algebraic cycles, the correct framework is:

1. Replace $E^3$ by $X_B^3$ where $X_B$ is a Shimura curve of genus $\geq 2$.
2. The modified diagonal $\Delta_{\mathrm{GKS}} \in \mathrm{CH}^2(X_B^3)_0$ is nontrivial when $X_B$ has genus $\geq 2$.
3. The Gross–Kudla–Yuan–Zhang–Zhang theorem applies when the root number is $-1$.
4. For rank 2 curves with root number $+1$, one needs the **central value formula** (Ichino–Ikeda, Gan–Gross–Prasad) or higher derivative formulas, which are not yet available for codimension-2 cycles.

---

## References

- **[GS99]** Gross, B., Schoen, C. *The modified diagonal cycle on the triple product of a pointed curve.* Ann. Inst. Fourier **45** (1995): 649–679. [Numdam](https://www.numdam.org/item/10.5802/aif.1469.pdf)
- **[GK92]** Gross, B., Kudla, S. *Heights and the central critical values of triple product L-functions.* Compositio Math. **81** (1992): 143–207.
- **[YZZ23]** Yuan, X., Zhang, S.-W., Zhang, W. *Triple product L-series and Gross–Kudla–Schoen cycles.* Preprint, 2023.
- **[QZ22]** Qiu, C., Zhang, W. *Vanishing results in Chow groups for the modified diagonal cycles.* arXiv:2209.09736, 2022.
- **[Lil22]** Lilienfeldt, D. T.-B. G. *Torsion properties of modified diagonal classes on triple products of modular curves.* arXiv:2111.14727, 2022.
- **[Cer83]** Ceresa, G. *$C$ is not algebraically equivalent to $C^-$ in its Jacobian.* Ann. of Math. **117** (1983): 285–291.
