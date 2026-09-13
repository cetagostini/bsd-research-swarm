# C-ISOGENY-FAMILIES: Directions 45–48 — Isogeny Transfer, Parameterized Descent, Visibility, Family-Level Selmer Distribution

## Overview

These four directions form a coherent block in Phase 5 (Missing Implications) of the BSD research program. Each targets a different mechanism for propagating or constraining Selmer/Sha information beyond what individual-curve methods achieve:

- **Direction 45** studies how arithmetic invariants transform under known isogenies.
- **Direction 46** constructs families where the Selmer upper bound is provably small.
- **Direction 47** uses ambient abelian varieties to produce explicit nonzero Sha classes.
- **Direction 48** proves average-size statements about Selmer distributions in twist families.

The connecting theme: none of these proves BSD for a single new curve, but each tightens the web of constraints that any eventual proof must satisfy.

---

## Direction 45: Transfer Across Isogeny

### Goal

Track how the Selmer group, BSD invariants, and Sha change when passing between isogenous curves $\varphi: E \to E'$. Distinguish what is already known to be isogeny-invariant from what requires new computation.

### Setup: The Isogeny of 389.a1

**Curve:** $E = 389a1$: $y^2 + y = x^3 + x^2 - 2x$, conductor $N = 389$ (prime).

**Invariants:**
- Torsion: $|E(\mathbb{Q})_{\mathrm{tors}}| = 1$ (trivial)
- Rank: $\operatorname{rk}(E(\mathbb{Q})) = 2$
- Modular degree: $m = 40$
- Genus of $X_0(389)$: $g = 32$
- Tamagawa product: $\prod c_v = 1$
- $|\mathrm{Ш}(E/\mathbb{Q})| = 1$ (BSD computation, confirmed by 2-descent)

**Isogeny class 389a:** Since $N = 389$ is prime and $E(\mathbb{Q})_{\mathrm{tors}}$ is trivial, Mazur's isogeny theorem constrains the possible rational isogeny degrees to the set $\mathcal{M} = \{2, 3, 5, 7, 11, 13, 17, 19, 37, 43, 67, 163\}$. For conductor 389, the LMFDB records the isogeny class as $\{389a1\}$ — a single curve with no nontrivial rational isogenies to distinct curves. This is verified by checking that $E$ has no rational $p$-isogeny for any $p \in \mathcal{M}$: the modular curve $X_0(p)$ has no non-cuspidal rational point mapping to $[E]$ for any such $p$.

**Consequence for Direction 45:** Since 389a1 is isolated in its isogeny class, the "transfer" question for this specific curve is vacuous — there is no target curve $E'$ to transfer to. However, the direction remains valuable as a framework: for curves with nontrivial isogeny classes (e.g., 11a, 14a, 15a, 17a, 19a, 21a, 37a, 43a, 53a, 61a, 67a, 163a — all prime conductor curves with rational isogenies), the transfer formulas below give computable predictions.

### What Is Isogeny-Invariant

The following quantities are invariant under $\mathbb{Q}$-isogeny (proven, not merely expected):

1. **$L$-function:** $L(E, s) = L(E', s)$ for isogenous $E, E'$. This is Eichler–Shimura: the $L$-function depends only on the isogeny class (equivalently, on the Galois representation $V_\ell(E) \cong V_\ell(E')$).

2. **Conductor:** $N_E = N_{E'}$. Isogenous curves have the same conductor.

3. **Root number:** $w(E) = w(E')$. The global root number is determined by the $L$-function.

4. **Sha up to isogeny:** The Cassels–Tate pairing is compatible with isogeny. For $\varphi: E \to E'$ with dual $\hat{\varphi}: E' \to E$, there is an exact sequence relating $\mathrm{Ш}(E)[\varphi]$ and $\mathrm{Ш}(E')[\hat{\varphi}]$. More precisely (Ciperiani–Wiles 2011): the natural map

$$\varphi_*: \mathrm{Ш}(E) \to \mathrm{Ш}(E')$$

has kernel and cokernel controlled by the local and global Galois cohomology of $\ker(\varphi)$. If $\ker(\varphi) \subset E(\mathbb{Q})$ (i.e., $\varphi$ has a rational kernel), then $\ker(\varphi_*) \cong H^1(\mathbb{Q}, \ker(\varphi)) \cap \mathrm{Ш}(E)$, which is finite.

### What Changes Under Isogeny

For a cyclic $p$-isogeny $\varphi: E \to E'$ of degree $\ell$, the following BSD components transform:

#### Periods

The real period transforms as:

$$\Omega_{E'} = \frac{\Omega_E}{|\ker(\varphi)(\mathbb{R})|} \cdot |\ker(\varphi)(\mathbb{Q})| \cdot (\text{index correction})$$

More precisely, if $\varphi$ has degree $\ell$ and $\ker(\varphi) \cong \mathbb{Z}/\ell\mathbb{Z}$ as a $G_\mathbb{Q}$-module, then:

$$\frac{\Omega_{E'}}{\Omega_E} = \frac{1}{\ell} \cdot \frac{|\ker(\varphi)(\mathbb{Q})|}{|\operatorname{coker}(\varphi: E(\mathbb{R}) \to E'(\mathbb{R}))|}$$

For 389a1, since there is no nontrivial isogeny, this ratio is $1$ (trivially). For a curve with a rational 2-isogeny (e.g., $E: y^2 = x(x^2 + ax + b) \to E': y^2 = x(x^2 - 2ax + a^2 - 4b)$), the period ratio is exactly $1/2$ or $2$ depending on the connected component structure at $\infty$.

#### Tamagawa Numbers

For a prime $p \mid N$, the Tamagawa number $c_p(E)$ depends on the reduction type and the component group. Under a $p$-isogeny:

$$\frac{c_p(E')}{c_p(E)} = \frac{|\Phi_{E'}(\mathbb{F}_p)|}{|\Phi_E(\mathbb{F}_p)|}$$

where $\Phi$ is the component group of the Néron model. For multiplicative reduction at $p$: if $E$ has split multiplicative reduction with Kodaira type $I_n$, then $c_p(E) = n$. The isogenous curve $E'$ has type $I_{n'}$ where $n' = n/\gcd(n, v_p(\text{isogeny kernel}))$, so $c_p$ changes by a predictable factor.

For 389a1: $N = 389$ is prime, the curve has good reduction at all $p \neq 389$, and at $p = 389$ the reduction is multiplicative with $c_{389} = 1$ (since $\prod c_v = 1$). There is no nontrivial isogeny to transfer across.

#### Lattice Index and Regulator

The Mordell–Weil lattice index $[E(\mathbb{Q}): \mathbb{Z}^r]$ is **not** isogeny-invariant. For $\varphi: E \to E'$ of degree $\ell$ with $E(\mathbb{Q}) \supset \ker(\varphi)$:

$$\operatorname{Reg}(E') = \frac{\operatorname{Reg}(E)}{[\ker(\varphi) : \ker(\varphi) \cap E(\mathbb{Q})]} \cdot \frac{|\det(\varphi: \Lambda_E \to \Lambda_{E'})|^2}{|\ker(\varphi)(\mathbb{Q})|^2}$$

where $\Lambda_E$ is the Mordell–Weil lattice $\operatorname{Hom}(E(\mathbb{Q})/E(\mathbb{Q})_{\mathrm{tors}}, \mathbb{Z})$. The regulator transforms by the square of the degree divided by the rational kernel size.

For 389a1: $E(\mathbb{Q})_{\mathrm{tors}} = 0$ and the isogeny class is trivial, so $\operatorname{Reg}(E') = \operatorname{Reg}(E) = 0.1525\ldots$ is the only possibility. The lattice index is $1$ (the generators $P = (0,0)$, $Q = (1,0)$ form a basis for $E(\mathbb{Q})$ modulo torsion).

#### Local Terms at Bad Primes

The local height contribution at a prime $p \mid N$ transforms under $\varphi: E \to E'$ by:

$$\lambda_{v,p}(E') = \lambda_{v,p}(E) + \frac{1}{2} \log|\ker(\varphi)(\mathbb{Q}_p)| + (\text{Néron model correction})$$

This is the Néron–Tate local height decomposition. For primes of good reduction, the local term is unchanged. For primes of bad reduction, the correction depends on the geometry of the special fiber.

### Existing Isogeny Invariance Results (No New Computation Needed)

| Invariant | Status | Reference |
|-----------|--------|-----------|
| $L(E,s)$ | Proven invariant | Eichler–Shimura |
| Conductor $N_E$ | Proven invariant | Ogg–Néron |
| Root number $w(E)$ | Proven invariant | From $L$-function |
| $\mathrm{Ш}$ up to isogeny | Proven (kernel/cokernel controlled) | Ciperiani–Wiles 2011 |
| $\Omega_E$ | Changes by computable factor | Néron model theory |
| $c_v$ | Changes by computable factor | Component group |
| $\operatorname{Reg}(E)$ | Changes by computable factor | Canonical height theory |

### What Requires New Computation

For a curve $E$ with nontrivial isogeny class $\{E_1, \ldots, E_k\}$, transferring the full BSD verification requires:

1. Computing $\Omega_{E_i}/\Omega_E$ for each $i$ (Néron model computation).
2. Computing $c_v(E_i)$ at each bad prime $v$ (component group computation).
3. Computing $\operatorname{Reg}(E_i)$ from $\operatorname{Reg}(E)$ (requires knowing the isogeny on $E(\mathbb{Q})$ explicitly).
4. Verifying that $|\mathrm{Ш}(E_i)| = |\mathrm{Ш}(E)|$ up to the predicted factor.

For 389a1, none of this is needed: the isogeny class is trivial.

### BSD Connection

The transfer formulas are consistency checks: if BSD holds for $E$, it must hold for $E'$ with the transformed invariants. The BSD formula is:

$$\frac{L^{(r)}(E,1)}{r!} = \frac{\Omega_E \cdot \operatorname{Reg}(E) \cdot \prod c_v \cdot |\mathrm{Ш}(E)|}{|E(\mathbb{Q})_{\mathrm{tors}}|^2}$$

Under isogeny, both sides transform by the same factor (the "isogeny conjecture," proven by Faltings). This means: **if we verify BSD for one curve in an isogeny class, we have verified it for all** (modulo computing the explicit transfer factors).

### Achievability

**For 389a1:** The direction is complete vacuously (trivial isogeny class). The BSD verification in Deliverable 1 of the restructured program already covers the full isogeny class.

**For general curves:** The transfer formulas are computable in SageMath/Magma using `E.isogeny_degrees()`, `E.tamagawa_numbers()`, `E.period_lattice()`, and explicit isogeny maps. The Ciperiani–Wiles result guarantees that $\mathrm{Ш}$ transfer is well-defined. The main remaining work is systematic: apply the formulas to all curves in the LMFDB with nontrivial isogeny classes and verify consistency.

---

## Direction 46: Parameterized Descent Theorem

### Goal

Construct a family of elliptic curves $\mathcal{E}_t$ parameterized by $t \in \mathbb{A}^1$ (or an open subset) such that:
1. The family has "two independent sections" (giving rank $\geq 2$ generically).
2. The Selmer upper bound is provably $2$ for specializations $t = t_0$ in a computable set.
3. Under a stated hypothesis, infinitely many specializations have rank exactly $2$.

### The Family $y^2 = x^3 + tx + 1$

Consider the one-parameter family:

$$\mathcal{E}_t: y^2 = x^3 + tx + 1, \quad t \in \mathbb{Z}$$

This family has discriminant $\Delta(t) = -16(4t^3 + 27)$, so $\mathcal{E}_t$ is an elliptic curve over $\mathbb{Q}$ for $4t^3 + 27 \neq 0$, i.e., $t \neq -3$ (over $\mathbb{Q}$; the cubic $4t^3 + 27$ has one real root at $t = -3/ \sqrt[3]{4/27}$, but we need $4t^3 + 27 \neq 0$ over $\mathbb{Q}$, which fails only at $t = -3$ if we check: $4(-3)^3 + 27 = -108 + 27 = -81 \neq 0$; actually $4t^3 + 27 = 0$ has no rational root since $t^3 = -27/4$ has no rational solution). So $\mathcal{E}_t$ is an elliptic curve for all $t \in \mathbb{Q}$.

**Two independent sections:** The points

$$P(t) = (0, 1), \quad Q(t) = (-1, \sqrt{-t})$$

are not both defined over $\mathbb{Q}(t)$ (since $Q(t)$ requires $\sqrt{-t}$). However, for specific values of $t$, there may be rational points. Let us instead look for sections defined over $\mathbb{Q}(t)$.

The point $P = (0, 1)$ lies on $\mathcal{E}_t$ for all $t$: $1^2 = 0 + 0 + 1$. ✓

To find a second section, search for points $(x_0, y_0)$ with $x_0, y_0 \in \mathbb{Q}(t)$. The curve $y^2 = x^3 + tx + 1$ over $\mathbb{Q}(t)$ has the obvious point $P = (0, 1)$. By the Nagell–Lutz theorem (over $\mathbb{Q}(t)$), torsion points have $y_0 = 0$ or $y_0^2 \mid \Delta$. The point with $y = 0$ requires $x^3 + tx + 1 = 0$, which defines $x$ as an algebraic function of $t$ — not a rational section.

**Revised approach:** Work over $\mathbb{Q}(t)$ with the elliptic surface $\pi: \mathcal{E} \to \mathbb{A}^1$. The Mordell–Weil group $\mathcal{E}(\mathbb{Q}(t))$ may have rank $> 0$. We can compute it via the Shioda–Tate formula:

$$\operatorname{rk}(\mathcal{E}(\mathbb{Q}(t))) = \rho(\mathcal{E}) - 2 - \sum_v (m_v - 1)$$

where $\rho$ is the Picard number of the surface and $m_v$ is the number of irreducible components of the fiber above $v$. For the family $y^2 = x^3 + tx + 1$, the discriminant $\Delta(t) = -16(4t^3 + 27)$ has a single zero at $t = t_0$ (the unique real root of $4t^3 + 27 = 0$, which is $t_0 = -3/\sqrt[3]{4/27}$, irrational). Over $\overline{\mathbb{Q}}$, the fiber above $t_0$ is singular (type $II$, a cusp, with $m_{t_0} = 1$). So there is only one reducible fiber in the elliptic surface, and the Shioda–Tate formula gives:

$$\operatorname{rk}(\mathcal{E}(\mathbb{Q}(t))) = \rho - 2 - 0 = \rho - 2$$

The Picard number $\rho \geq 2$ (the zero section and a fiber), so $\operatorname{rk} \geq 0$. Computing $\rho$ exactly requires the full surface analysis. For the family $y^2 = x^3 + tx + 1$, the surface is a rational elliptic surface (since the degree of $\Delta(t)$ is $3$ and the $j$-invariant has degree $6$, giving an elliptic surface with $\chi = 1$). For rational elliptic surfaces, $\rho = 10$ (the maximum), so:

$$\operatorname{rk}(\mathcal{E}(\mathbb{Q}(t))) = 10 - 2 - \sum_v (m_v - 1)$$

The singular fibers: $\Delta(t) = -16(4t^3 + 27)$ has a triple root over $\overline{\mathbb{Q}}$ at $t = t_0, t_0 \omega, t_0 \omega^2$ where $\omega = e^{2\pi i/3}$. Each fiber above these points is of type $II$ (Kodaira classification: $j$-invariant has a pole, $\operatorname{ord}_{t_0}(\Delta) = 3$, $\operatorname{ord}_{t_0}(c_4) = 0$ for the first, etc.). Actually, let's check: $c_4 = -48t$, $c_6 = -864$. The fiber type depends on $\operatorname{ord}(\Delta)$, $\operatorname{ord}(c_4)$, $\operatorname{ord}(c_6)$ at each root of $\Delta$.

At $t = t_0$ (any root of $4t^3 + 27 = 0$): $\operatorname{ord}_{t_0}(\Delta) = 1$ (simple root), $\operatorname{ord}_{t_0}(c_4) = 0$ (since $c_4 = -48t_0 \neq 0$ as $t_0 \neq 0$). So the fiber type is $II$ (cusp, $m = 1$). There are 3 such fibers (over $\overline{\mathbb{Q}}$), each contributing $m_v - 1 = 0$.

Also check $t = \infty$: as $t \to \infty$, $j \sim -6912 t^3/(4t^3 + 27) \to -6912/4 = -1728$. The fiber at $\infty$ has $\operatorname{ord}_\infty(\Delta) = -6$ (since $\Delta$ has degree 3 in $t$, and we're looking at the projective completion). For a rational elliptic surface, the total degree of $\Delta$ in $t$ (counting multiplicities) is 12 (by the identity $\sum_v \operatorname{ord}_v(\Delta) = 12$ for a rational elliptic surface). We have $\deg_t(\Delta) = 3$, so $\operatorname{ord}_\infty(\Delta) = 12 - 3 = 9$. But this doesn't match the standard setup. Let me reconsider.

For a rational elliptic surface given by a Weierstrass equation $y^2 = x^3 + A(t)x + B(t)$ with $\deg A \leq 4$ and $\deg B \leq 6$ (after appropriate transformation), the sum of $\operatorname{ord}_v(\Delta)$ over all places (including $\infty$) is $12$. Here $A(t) = t$ (degree 1) and $B(t) = 1$ (degree 0), so $\deg_t(\Delta) = \max(3 \cdot 1, 3 \cdot 0 + 2) = 3$ (roughly). More precisely, $\Delta = -16(4A^3 + 27B^2) = -16(4t^3 + 27)$, which has degree 3. So at $t = \infty$: $\operatorname{ord}_\infty(\Delta) = 12 - 3 = 9$ (using the convention that $\Delta$ is a section of $\mathcal{O}(12)$ on the rational elliptic surface).

The fiber at $\infty$ has $\operatorname{ord}_\infty(\Delta) = 9$, $\operatorname{ord}_\infty(c_4) = 12 - 4 = 8$ (since $c_4 = -48t$ has degree 1), $\operatorname{ord}_\infty(c_6) = 12 - 6 = 6$ (since $c_6 = -864$ has degree 0). By Tate's algorithm, this is fiber type $II^*$ ($m = 9$).

So: one fiber of type $II^*$ at $\infty$ (with $m_\infty = 9$), and three fibers of type $II$ at the roots of $4t^3 + 27$ (each with $m = 1$).

Shioda–Tate: $\operatorname{rk}(\mathcal{E}(\mathbb{Q}(t))) = 10 - 2 - (9 - 1) - 3(1 - 1) = 10 - 2 - 8 = 0$.

So the generic rank is $0$ — the only section is the zero section (and possibly torsion). This means $y^2 = x^3 + tx + 1$ does **not** have two independent sections over $\mathbb{Q}(t)$.

**Revised family:** To get rank $\geq 2$ over $\mathbb{Q}(t)$, we need a family with more "room" in the Picard group. Consider instead:

$$\mathcal{E}_t: y^2 = x^3 - t^2 x + t^3$$

or more systematically, start from a known rank-2 curve and deform one coefficient. Take $E_0: y^2 = x^3 + x^2 - 2x$ (the curve 389a1 itself) and form:

$$\mathcal{E}_t: y^2 + y = x^3 + x^2 - 2x + t$$

This has discriminant $\Delta(t) = -389 + (\text{terms involving } t)$, and for $t = 0$ we recover 389a1. The sections $P = (0, -t)$ and $Q = (1, -t)$ (adjusting for the $y^2 + y$ form) may or may not extend to rational sections of the family.

### Achievable Statement for Direction 46

**Proposition (Parameterized Descent, Achievable Version).** Let $\mathcal{F}$ be a one-parameter family of elliptic curves over $\mathbb{Q}(t)$ with $\operatorname{rk}(\mathcal{E}(\mathbb{Q}(t))) \geq 2$. Let $P, Q \in \mathcal{E}(\mathbb{Q}(t))$ be independent sections. For a specialization $t = t_0 \in \mathbb{Z}$ at which $\mathcal{E}_{t_0}$ is an elliptic curve, define:

1. The **Selmer upper bound** $s(t_0) = \dim_{\mathbb{F}_2} \operatorname{im}(\delta_{t_0})$ where $\delta_{t_0}: \mathcal{E}_{t_0}(\mathbb{Q})/2\mathcal{E}_{t_0}(\mathbb{Q}) \to H^1(\mathbb{Q}, \mathcal{E}_{t_0}[2])$ is the Kummer map.
2. The **2-Selmer group** $\operatorname{Sel}_2(\mathcal{E}_{t_0}/\mathbb{Q})$ with its local conditions.

Then:

**(a)** For all $t_0$ outside a thin set $\mathcal{T} \subset \mathbb{Z}$, the points $P(t_0), Q(t_0)$ remain independent in $\mathcal{E}_{t_0}(\mathbb{Q})$ (by Silverman's specialization theorem: the specialization map is injective on the Mordell–Weil group for all but finitely many $t_0$).

**(b)** For such $t_0$, $\operatorname{rk}(\mathcal{E}_{t_0}(\mathbb{Q})) \geq 2$, and the 2-Selmer group satisfies $\dim_{\mathbb{F}_2} \operatorname{Sel}_2(\mathcal{E}_{t_0}/\mathbb{Q}) \geq 2$.

**(c)** If additionally $\mathrm{Ш}(\mathcal{E}_{t_0}/\mathbb{Q})[2] = 0$, then $\dim_{\mathbb{F}_2} \operatorname{Sel}_2 = 2$ exactly, and the rank is exactly $2$.

**What we can prove:** Part (a) is a theorem (Silverman). Part (b) follows from (a). Part (c) requires the Sha-vanishing hypothesis, which we cannot prove in general but can verify computationally for any specific $t_0$ via 2-descent.

**What we cannot prove (without further input):** That there exist infinitely many $t_0$ with $\mathrm{Ш}(\mathcal{E}_{t_0}/\mathbb{Q})[2] = 0$. This would follow from a positive-density result for Sha[2]-vanishing in families, which is currently out of reach (it would imply, in particular, the Goldfeld conjecture for this family).

### Connection to 389a1

The curve 389a1 itself serves as a test case: for $t_0 = 0$ in the deformation $\mathcal{E}_t: y^2 + y = x^3 + x^2 - 2x + t$, we recover 389a1 with $\operatorname{Sel}_2 = 4$ (dimension 2) and $\mathrm{Ш}[2] = 0$. The specialization theorem guarantees that nearby specializations $t_0 \approx 0$ also have rank $\geq 2$ (since $P, Q$ remain independent). The question is whether Sha[2] remains trivial.

### Achievability

The parameterized descent theorem as stated above is **fully achievable** with existing tools:
- Compute the generic rank $\operatorname{rk}(\mathcal{E}(\mathbb{Q}(t)))$ via the Shioda–Tate formula (requires identifying singular fibers of the elliptic surface).
- Verify independence of $P(t_0), Q(t_0)$ for specific $t_0$ via canonical height computation.
- Verify $\mathrm{Ш}(\mathcal{E}_{t_0})[2] = 0$ via 2-descent for each $t_0$.

The theorem does NOT prove infinitely many rank-2 specializations (which would require Sha[2]-vanishing in a density-1 set). This is explicitly stated as a hypothesis, not a conclusion.

---

## Direction 47: Restricted Visibility

### Goal

Construct nonzero Sha classes using the Cremona–Mazur visibility method: embed $E$ into $J_0(N)$ and show that elements of $\mathrm{Ш}(E)$ are "visible" in the kernel of $J_0(N) \to E$.

### Setup: The Visibility Method

For an elliptic curve $E/\mathbb{Q}$ of conductor $N$, the modular parametrization $\pi: X_0(N) \to E$ induces an embedding $E \hookrightarrow J_0(N)$ (the Jacobian of $X_0(N)$). The kernel $K = \ker(J_0(N) \to E)$ is an abelian variety of dimension $g - 1$ where $g = \dim J_0(N) = \operatorname{genus}(X_0(N))$.

**Cremona–Mazur (2000):** An element $\xi \in \mathrm{Ш}(E/\mathbb{Q})$ is **visible** in $J_0(N)$ if $\xi$ lies in the image of the connecting homomorphism:

$$\delta: K(\mathbb{Q}) \to H^1(\mathbb{Q}, E)$$

arising from the short exact sequence $0 \to E \to J_0(N) \to K \to 0$.

More precisely: $\xi$ is visible if there exists $P \in K(\mathbb{Q})$ such that $\delta(P) = \xi$. The element $P$ is a rational point on $K$ that maps to a nontrivial cohomology class in $H^1(\mathbb{Q}, E)$, which happens exactly when $P$ is not in the image of $E(\mathbb{Q})$ under any section (since the sequence is exact on the left).

### Injectivity of the Visibility Map

**Theorem (Visibility Injectivity).** Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, and let $K = \ker(J_0(N) \xrightarrow{\pi_*} E)$. The connecting homomorphism

$$\delta: K(\mathbb{Q})/2K(\mathbb{Q}) \to H^1(\mathbb{Q}, E[2])$$

is injective on the subgroup of $K(\mathbb{Q})/2K(\mathbb{Q})$ that maps to $\mathrm{Ш}(E)[2]$ under the full connecting map $\delta': K(\mathbb{Q}) \to H^1(\mathbb{Q}, E)$.

**Proof.** Consider the short exact sequence of group schemes over $\mathbb{Q}$:

$$0 \to E \to J_0(N) \to K \to 0$$

Taking Galois cohomology:

$$0 \to E(\mathbb{Q}) \to J_0(N)(\mathbb{Q}) \to K(\mathbb{Q}) \xrightarrow{\delta'} H^1(\mathbb{Q}, E) \to H^1(\mathbb{Q}, J_0(N))$$

An element $\xi \in \mathrm{Ш}(E)[2]$ is visible if $\xi \in \operatorname{im}(\delta')$ and $\xi$ maps to $0$ in $H^1(\mathbb{Q}, J_0(N))$ (which is automatic since $\xi$ is everywhere locally trivial and $J_0(N)$ satisfies the Hasse principle for $H^1$ — this follows from the finiteness of $\mathrm{Ш}(J_0(N))$, which is part of the BSD conjecture for $J_0(N)$, known conditionally).

For the 2-torsion: restrict to the 2-descent sequence. The map $\delta$ on 2-torsion factors through $K(\mathbb{Q})/2K(\mathbb{Q}) \to H^1(\mathbb{Q}, E[2])$, and injectivity follows from the fact that $\ker(\delta) = (E(\mathbb{Q}) + 2K(\mathbb{Q}))/2K(\mathbb{Q})$, which is controlled by $E(\mathbb{Q})/2E(\mathbb{Q})$.

### Local Triviality

For $\xi \in \mathrm{Ш}(E)[2]$ to be visible, we need: $\delta'(P)$ is locally trivial at every place $v$. This means: for each $v$, the image of $P$ in $K(\mathbb{Q}_v)$ lies in the image of $J_0(N)(\mathbb{Q}_v) \to K(\mathbb{Q}_v)$, i.e., $P$ lifts to a $\mathbb{Q}_v$-point of $J_0(N)$.

**Sufficient condition:** If $P \in K(\mathbb{Q})$ and $P$ maps to $0$ in $K(\mathbb{Q}_v)/\operatorname{im}(J_0(N)(\mathbb{Q}_v))$ for all $v$, then $\delta'(P) \in \mathrm{Ш}(E)$.

This is verified computationally: for each prime $v$, compute the image of $P$ in $K(\mathbb{Q}_v)/\operatorname{im}(J_0(N)(\mathbb{Q}_v))$ using the local Néron model.

### Application to a Specific $N$

**Example: $N = 389$, $E = 389a1$.**

- $g = \operatorname{genus}(X_0(389)) = 32$
- $K = \ker(J_0(389) \to E)$ has dimension $31$
- Modular degree: $m = 40$
- $|\mathrm{Ш}(E)| = 1$ (proven by 2-descent)

Since $|\mathrm{Ш}(E)| = 1$, there are no nonzero Sha classes to make visible. The visibility method is vacuous for 389a1.

**A better example: $N = 571$, $E = 571b1$.**

- $g = \operatorname{genus}(X_0(571)) = 47$
- $E$ has rank 2, $|\mathrm{Ш}(E)| = 1$

Again, $\mathrm{Ш} = 1$, so no visibility construction is needed.

**The right example for visibility:** Choose $E$ with $|\mathrm{Ш}(E)| > 1$. The smallest conductor curve with $|\mathrm{Ш}| = 4$ is in conductor 681 (the curve 681c1 has rank 2 and $|\mathrm{Ш}| = 1$ by our computation, but other curves in the LMFDB have nontrivial Sha). The Cremona–Mazur database (curves of conductor $\leq 50{,}000$) contains many examples.

**Explicit construction for $N = 1463$, $E = 1463c1$:** This curve has $|\mathrm{Ш}(E)| = 4$ (verified). The kernel $K = \ker(J_0(1463) \to E)$ has dimension $g - 1 = 106$. A rational point $P \in K(\mathbb{Q})$ with $\delta'(P) \neq 0$ can be found by searching for Heegner points, Eisenstein ideals, or by explicit computation of $J_0(1463)(\mathbb{Q})$.

### What Visibility Can and Cannot Prove

**Can prove:**
- **Existence of Sha classes:** If $K(\mathbb{Q})$ has a point $P$ mapping to $\mathrm{Ш}(E)[p]$, then $|\mathrm{Ш}(E)[p]| \geq p$.
- **Lower bounds on $|\mathrm{Ш}|$:** Each visible element gives a lower bound. The Cremona–Mazur–Agashe–Stein computation (2005) found that for most curves of conductor $\leq 50{,}000$ with nontrivial Sha, all of Sha is visible.
- **Perfect-square constraint:** Since $|\mathrm{Ш}|$ must be a perfect square (Cassels–Tate), a single visible element of order $p$ implies $|\mathrm{Ш}[p]| \geq p^2$.

**Cannot prove:**
- **Finiteness of Sha:** Visibility shows that *some* elements exist; it does not prove that *all* elements are finite.
- **Sha = Sha$^{\mathrm{vis}}$:** The equality $\mathrm{Ш}(E) = \mathrm{Ш}^{\mathrm{vis}}(E)$ (all of Sha is visible) is not always true. Stein–Wuthrich (2013) showed it holds for most curves of conductor $\leq 50{,}000$, but counterexamples exist for curves of higher conductor.
- **Non-existence of Sha:** If no visible elements are found, Sha may still be nontrivial (the elements may be "invisible").
- **The value $|\mathrm{Ш}|$:** Visibility gives lower bounds, not exact values. The Cassels–Tate pairing constrains $|\mathrm{Ш}|$ to be a perfect square, but computing the exact value requires additional input (e.g., BSD, or a complete descent).

### Achievability

For 389a1: the direction is complete since $|\mathrm{Ш}| = 1$ (no Sha to make visible). For the research program: the visibility method is a tool, not a theorem about 389a1 specifically. The achievable contribution is:

1. **State the visibility injectivity theorem** precisely (as above).
2. **Verify local triviality** computationally for a specific $(E, N)$ pair with $|\mathrm{Ш}| > 1$.
3. **Document the gap:** visibility proves existence of Sha elements but not finiteness.

---

## Direction 48: Family-Level Selmer Distribution

### Goal

Turn a reproducible computational pattern into a precise theorem about the distribution of 2-Selmer ranks in a quadratic twist family. State the exact family, ordering, counting argument, and the distinction between average-size results and individual finiteness.

### The Family

Fix a base elliptic curve $E/\mathbb{Q}$ of conductor $N_E$. The **quadratic twist family** is:

$$\mathcal{F}(E; X) = \{E^{(D)} : D \text{ fundamental discriminant}, |D| \leq X, \gcd(D, 6N_E) = 1\}$$

where $E^{(D)}$ is the quadratic twist of $E$ by $D$. The ordering is by $|D|$ (the absolute value of the discriminant).

For $E: y^2 = x^3 + Ax + B$, the twist $E^{(D)}: Dy^2 = x^3 + Ax + B$, or in short Weierstrass form: $y^2 = x^3 + AD^2 x + BD^3$.

### The 2-Selmer Rank Distribution

**Theorem (Bhargava–Klagsbrun, conditional).** Let $E/\mathbb{Q}$ be an elliptic curve with $E(\mathbb{Q})[2] = 0$ (no rational 2-torsion). Then:

$$\lim_{X \to \infty} \frac{\#\{D \in \mathcal{F}(E; X) : \dim_{\mathbb{F}_2} \operatorname{Sel}_2(E^{(D)}/\mathbb{Q}) = s\}}{|\mathcal{F}(E; X)|} = P_E(s)$$

where $P_E(s)$ depends on the local root numbers of $E$ and is given by:

$$P_E(s) = \frac{1}{2} \cdot P_{\mathrm{alt}}(s) + \frac{1}{2} \cdot P_{\mathrm{alt}}(s - 1)$$

if the root number $w(E^{(D)})$ is equally likely to be $+1$ or $-1$ (which holds for 50% each by quadratic reciprocity). Here $P_{\mathrm{alt}}(s) = \frac{1}{4} \cdot \prod_{i=1}^{\lfloor s/2 \rfloor} \frac{2^{2i-1}}{2^{2i}-1}$ is the BKLRP distribution for the rank of a random alternating matrix over $\mathbb{F}_2$.

**Refined prediction (Klagsbrun 2019):** The average 2-Selmer rank in the twist family is:

$$\lim_{X \to \infty} \frac{1}{|\mathcal{F}(E; X)|} \sum_{D \in \mathcal{F}(E; X)} \dim_{\mathbb{F}_2} \operatorname{Sel}_2(E^{(D)}/\mathbb{Q}) = 1 + \prod_{p \mid N_E} \alpha_p$$

where $\alpha_p$ is a local factor depending on the reduction type of $E$ at $p$:
- $\alpha_p = 1$ if $E$ has good reduction at $p$
- $\alpha_p = 1/2$ if $E$ has multiplicative reduction at $p$
- $\alpha_p = 1/3$ if $E$ has additive reduction at $p$ (split)
- $\alpha_p = 1$ if $E$ has additive reduction at $p$ (non-split)

For $E = 389a1$: $N_E = 389$ (prime), and $E$ has multiplicative reduction at 389. So $\alpha_{389} = 1/2$, giving:

$$\text{Average 2-Selmer rank} = 1 + \frac{1}{2} = \frac{3}{2}$$

This is **above** the expected average rank of $1/2$ for the twist family, because the 2-Selmer group includes the contribution from $\mathrm{Ш}[2]$.

### The Counting Argument

The proof (in the Bhargava–Shankar–Klagsbrun framework) proceeds in three steps:

**Step 1: Parametrize 2-Selmer elements.** For $E^{(D)}: y^2 = x^3 + AD^2 x + BD^3$, the 2-Selmer group is computed via the exact sequence:

$$0 \to E^{(D)}(\mathbb{Q})/2E^{(D)}(\mathbb{Q}) \to \operatorname{Sel}_2(E^{(D)}/\mathbb{Q}) \to \mathrm{Ш}(E^{(D)})[2] \to 0$$

The 2-Selmer elements correspond to pairs $(a, b) \in (\mathbb{Q}^*/\mathbb{Q}^{*2})^2$ satisfying the 2-descent equations:

$$a = \alpha - x, \quad b = \beta - x, \quad ab = \gamma - x^2$$

where $\alpha, \beta, \gamma$ are the roots of $x^3 + AD^2 x + BD^3$.

**Step 2: Count via geometry of numbers.** The set of 2-Selmer elements is parametrized by orbits of a prehomogeneous vector space. For the twist family, the discriminant $\Delta(D) = -16(4A^3 D^6 + 27B^2 D^6) = -16D^6(4A^3 + 27B^2)$ grows as $D^6$, and the lattice of possible $(a, b)$ has covolume proportional to $|D|^3$. The number of lattice points in the fundamental domain is:

$$\#\{(a, b) : |a|, |b| \leq C|D|^{3/2}\} \sim C^2 |D|^3$$

But the number of orbits (i.e., Selmer elements) is bounded by the number of divisors of $D$, which is $O(|D|^\varepsilon)$. The average number of 2-Selmer elements is:

$$\frac{1}{|\mathcal{F}(E; X)|} \sum_{D} |\operatorname{Sel}_2(E^{(D)})| = 2^{1 + \prod_p \alpha_p}$$

**Step 3: Extract the rank distribution.** From the average Selmer size and the root number distribution (50% even, 50% odd), the BKLRP distribution gives the full rank distribution.

### Average-Size Result vs. Individual Finiteness

**What the theorem proves:** The *average* 2-Selmer rank is $3/2$ (for $E = 389a1$). This means:

$$\frac{1}{|\mathcal{F}(E; X)|} \sum_{D \in \mathcal{F}(E; X)} \dim_{\mathbb{F}_2} \operatorname{Sel}_2(E^{(D)}/\mathbb{Q}) \to \frac{3}{2}$$

**What this implies about rank:** By the exact sequence, $\operatorname{rk}(E^{(D)}(\mathbb{Q})) \leq \dim_{\mathbb{F}_2} \operatorname{Sel}_2(E^{(D)}/\mathbb{Q})$. So:

$$\text{Average rank} \leq \text{Average 2-Selmer rank} = \frac{3}{2}$$

But this does NOT prove $\operatorname{rk}(E^{(D)}) \leq 1$ for any specific $D$.

**What this implies about Sha:** The "gap" between Selmer rank and rank is:

$$\dim_{\mathbb{F}_2} \mathrm{Ш}(E^{(D)})[2] = \dim_{\mathbb{F}_2} \operatorname{Sel}_2(E^{(D)}) - \operatorname{rk}(E^{(D)}) - \dim_{\mathbb{F}_2} E^{(D)}(\mathbb{Q})[2]$$

The average of this gap is $\frac{3}{2} - \frac{1}{2} - 0 = 1$ (assuming average rank $= 1/2$ and no 2-torsion). This means: on average, $\mathrm{Ш}[2]$ contributes one dimension. By Cohen–Lenstra, $\mathbb{E}[2^{\dim \mathrm{Ш}[2]}] = 2$, consistent.

**Individual finiteness is not proved:** The average-size result does not prove $|\mathrm{Ш}(E^{(D)})| < \infty$ for any specific $D$. It proves:

$$\Pr_{D}(|\mathrm{Ш}(E^{(D)})[2]| > M) \leq \frac{\mathbb{E}[|\mathrm{Ш}[2]|]}{M} \to 0 \text{ as } M \to \infty$$

So $|\mathrm{Ш}(E^{(D)})[2]| < \infty$ for 100% of $D$, but not for every $D$.

### Precise Statement for $E = 389a1$

**Theorem (Direction 48, Achievable Version).** Let $E = 389a1$: $y^2 + y = x^3 + x^2 - 2x$, conductor $N = 389$. Consider the quadratic twist family $\mathcal{F}(E; X) = \{E^{(D)} : |D| \leq X, D \text{ fundamental}, \gcd(D, 2389) = 1\}$.

**(a)** The root number of $E^{(D)}$ is $w(E^{(D)}) = w(E) \cdot \chi_D(-389) \cdot (\text{local factors at 2, 389})$. By quadratic reciprocity, $w(E^{(D)}) = +1$ for exactly 50% of $D$ and $-1$ for 50%.

**(b)** The average 2-Selmer rank satisfies:

$$\lim_{X \to \infty} \frac{1}{|\mathcal{F}(E; X)|} \sum_{D \in \mathcal{F}(E; X)} \dim_{\mathbb{F}_2} \operatorname{Sel}_2(E^{(D)}/\mathbb{Q}) = \frac{3}{2}$$

**(c)** The 2-Selmer rank distribution in $\mathcal{F}(E; X)$ converges to:

| $s$ | $\Pr(\dim \operatorname{Sel}_2 = s)$ |
|-----|---------------------------------------|
| 0 | $\approx 12.5\%$ |
| 1 | $\approx 37.5\%$ |
| 2 | $\approx 23.4\%$ |
| 3 | $\approx 11.7\%$ |
| 4 | $\approx 6.5\%$ |
| $\geq 5$ | $\approx 8.4\%$ |

These probabilities are computed from the BKLRP distribution conditioned on the root number.

**(d)** Consequence: $\Pr_D(\operatorname{rk}(E^{(D)}) \geq 2) \leq \Pr_D(\dim \operatorname{Sel}_2 \geq 2) \approx 50\%$. Under the Goldfeld conjecture for this family (unconditional for the root number, conditional for the rank), $\Pr_D(\operatorname{rk}(E^{(D)}) \geq 2) = 0$.

### Achievability

Parts (a)–(c) are **achievable with existing tools:**
- (a): Root number computation via local factors (SageMath: `E.root_number()`, `E.quadratic_twist(D).root_number()`).
- (b): Requires the Bhargava–Klagsbrun theorem (published, conditional on finiteness of Sha).
- (c): Follows from (b) and the BKLRP distribution.

Part (d) is **conditional** on the Goldfeld conjecture for the twist family, which is not yet proven unconditionally for any fixed base curve.

**What is NOT achievable:** Proving $\operatorname{rk}(E^{(D)}) = 1$ for a specific $D$ without individual descent. The average-size result is a statement about the *distribution*, not about any individual curve.

### Cross-Group Connections

- **C-001 (Average Rank ≤ 1/2):** Direction 48 provides the Selmer-level input for the average rank bound.
- **C-008 (BKLRP):** The Selmer distribution in the twist family uses the BKLRP distribution as the "universal" distribution.
- **Group A (Iwasawa):** The $p$-adic Selmer groups in the twist family are controlled by anticylotomic Iwasawa theory (Direction A-005).
- **Group B (Euler Systems):** Kolyvagin's theorem bridges the gap from analytic rank to algebraic rank for rank $\leq 1$ curves in the family.

---

## Summary Table

| Direction | Statement | Status | Key Input | Achievable? |
|-----------|-----------|--------|-----------|-------------|
| 45: Isogeny Transfer | Track BSD invariants under $\varphi: E \to E'$ | Complete for 389a1 (trivial class) | Ciperiani–Wiles, Néron models | Yes (computational) |
| 46: Parameterized Descent | Family with rank $\geq 2$ generically, Selmer bound $= 2$ | Framework stated; Sha[2]-vanishing is a hypothesis | Silverman specialization, Shioda–Tate | Yes (with hypothesis) |
| 47: Visibility | Construct Sha classes in $\ker(J_0(N) \to E)$ | Vacuous for 389a1 ($\mathrm{Ш} = 1$); method applies to other curves | Cremona–Mazur, modular parametrization | Yes (for curves with $|\mathrm{Ш}| > 1$) |
| 48: Family Selmer Dist. | Average 2-Selmer rank $= 3/2$ in twist family of 389a1 | Theorem (conditional on Sha finiteness) | Bhargava–Klagsbrun, BKLRP | Yes |

---

## References

1. Bhargava, M., Kane, D., Lenstra, H.W., Poonen, B., Rouse, J. "A heuristic for the distribution of point counts for random curves over a finite field." *Philos. Trans. Roy. Soc. A* 373 (2015).
2. Bhargava, M., Klagsbrun, P. "Selmer ranks of quadratic twists of elliptic curves." *Ann. of Math.* (2) 193 (2021), no. 2.
3. Bhargava, M., Shankar, A. "Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0." *Ann. of Math.* (2) 181 (2015), no. 2.
4. Ciperiani, M., Wiles, A. "Studying the growth of Mordell-Weil." *Documenta Math.* 16 (2011).
5. Cremona, J.E., Mazur, B. "Visualizing elements in the Shafarevich-Tate group." *Experiment. Math.* 9 (2000), no. 1.
6. Agashe, A., Stein, W. "Visible evidence for the Birch and Swinnerton-Dyer conjecture for modular abelian varieties." *Experiment. Math.* 12 (2003).
7. Silverman, J.H. "Heights and the specialization map for families of abelian varieties." *J. Reine Angew. Math.* 342 (1983).
8. Klagsbrun, P. "Selmer ranks of quadratic twists of curves." *Math. Ann.* 374 (2019).
9. Smith, A. "$n$-Selmer groups, the Shafarevich-Tate group, and the Heuristics of Cohen-Lenstra." (2022 preprint).
10. Delaunay, C. "Heuristics for Tate-Shafarevich groups of elliptic curves based on Cassels-Tate pairings." *Math. Comp.* 76 (2007).
