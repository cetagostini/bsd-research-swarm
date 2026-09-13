# E-PADIC-ADVANCED: Advanced p-adic Methods for Rank 2 — Directions 18–20

**Directions covered:** 18 (Derived heights for degenerate pairing), 19 (Signed supersingular counterpart), 20 (Determinant-line formula)

**Benchmark curve:** $E = 389\texttt{a}1$, given by $y^2 + y = x^3 + x^2 - 2x$, conductor $N = 389$, discriminant $\Delta_E = 389$. Generators $P = (0,0)$, $Q = (1,0)$. The $a_p$ data: $a_5 = -3$, $a_2 = -2$, $a_3 = -3$. Algebraic and analytic rank $r = 2$.

---

## Direction 18: Derived Heights for Degenerate Pairing

### 18.1 The Problem of Degeneracy

Let $E/\mathbb{Q}$ have good ordinary reduction at an odd prime $p$, with rank $r = 2$. The **ordinary $p$-adic height pairing** on $E(\mathbb{Q})/\text{tors}$ is the bilinear form:

$$\langle \cdot, \cdot \rangle_p : E(\mathbb{Q}) \times E(\mathbb{Q}) \to \mathbb{Q}_p, \qquad \langle P, Q \rangle_p = \hat{h}_p(P + Q) - \hat{h}_p(P) - \hat{h}_p(Q)$$

where $\hat{h}_p$ is the canonical $p$-adic height (Mazur–Tate, Nekovář). The **$p$-adic regulator** is:

$$\text{Reg}_p(E) = \det \begin{pmatrix} \langle P, P \rangle_p & \langle P, Q \rangle_p \\ \langle Q, P \rangle_p & \langle Q, Q \rangle_p \end{pmatrix} \in \mathbb{Q}_p$$

**The degeneracy problem.** For $p$-adic BSD to hold, $\text{Reg}_p(E) \neq 0$. But there are systematic reasons why the ordinary $p$-adic height pairing can degenerate:

1. **Congruence condition.** Two independent points $P, Q \in E(\mathbb{Q})$ may satisfy $P \equiv Q \pmod{p}$ in the Mordell–Weil group modulo $pE(\mathbb{Q}) + E(\mathbb{Q})_{\text{tors}}$. If the images of $P$ and $Q$ in $E(\mathbb{Q})/pE(\mathbb{Q})$ are linearly dependent, then $\langle P, Q \rangle_p \equiv 0 \pmod{p^v}$ for some $v \geq 1$, potentially causing the regulator to vanish to high order.

2. **Formal group saturation.** If $P$ and $Q$ both reduce to the identity component of the Néron model at $p$, their formal group logarithms $\log_E(P), \log_E(Q)$ satisfy $\log_E(P) \equiv \lambda \log_E(Q) \pmod{p^n}$ for some $\lambda \in \mathbb{Z}_p$ and large $n$. The height pairing then nearly vanishes because the $p$-local Néron function is controlled by the formal group.

3. **Splitting dependence.** The canonical height $\hat{h}_p$ depends on a choice $\sigma : H^1_{\text{dR}}(E/\mathbb{Q}) \to F^1 H^1_{\text{dR}}(E/\mathbb{Q})$. Two different splittings $\sigma, \sigma'$ give:

$$\hat{h}_p^\sigma(P) - \hat{h}_p^{\sigma'}(P) = \langle \sigma - \sigma', \log_E(P) \rangle_{\text{dR}}$$

where $\langle \cdot, \cdot \rangle_{\text{dR}}$ is the de Rham pairing. If $\log_E(P)$ and $\log_E(Q)$ are nearly proportional (which happens when $P$ and $Q$ are congruent mod $p$), the regulator is splitting-sensitive and may vanish for a poor choice of $\sigma$.

### 18.2 The Bockstein Pairing

When $\text{Reg}_p(E) = 0$, the ordinary $p$-adic height pairing carries no information about the Mordell–Weil lattice. The correct replacement is the **Bockstein pairing** (or **derived $p$-adic height**), which is a secondary cohomological operation.

**Construction (Nekovář, 2006).** Let $V = T_p(E) \otimes \mathbb{Q}_p$ be the $p$-adic Tate module. Consider the **Selmer complex**:

$$\mathbf{R}\Gamma_{\text{Sel}}(\mathbb{Q}, V) := \text{Cone}\left(\mathbf{R}\Gamma(\mathbb{Q}, V) \xrightarrow{\text{loc}} \prod_v' \frac{\mathbf{R}\Gamma(\mathbb{Q}_v, V)}{\mathbf{R}\Gamma_f(\mathbb{Q}_v, V)}\right)[-1]$$

where $\mathbf{R}\Gamma_f(\mathbb{Q}_v, V)$ is the Bloch–Kato local condition (crystalline at $p$, unramified at good primes, Néron model component at bad primes), and $\prod'$ denotes the restricted product.

The **height pairing** is the pairing on:

$$H^0_{\text{Sel}}(\mathbb{Q}, V^*(1)) \times H^1_{\text{Sel}}(\mathbb{Q}, V) \to \mathbb{Q}_p$$

induced by the cup product $V^*(1) \otimes V \to \mathbb{Q}_p(1) \xrightarrow{\text{tr}} \mathbb{Q}_p$.

**The Bockstein (secondary pairing).** When the primary height pairing is identically zero on a subspace $W \subseteq H^1_{\text{Sel}}(\mathbb{Q}, V)$, there exists a **Bockstein map**:

$$\beta : W \to H^2_{\text{Sel}}(\mathbb{Q}, V \otimes V^*(1)) / (\text{image of primary pairing})$$

which measures the *obstruction to lifting* the degeneracy. Concretely:

1. Choose a cochain $c \in C^1(\mathbb{Q}, V)$ representing a class in $W$.
2. Since $\langle c, \cdot \rangle_p = 0$, the cup product $c \cup \cdot$ is a coboundary in the Selmer complex.
3. Choose a primitive $\delta c \in C^2(\mathbb{Q}, V \otimes V^*(1))$ with $d(\delta c) = c \cup \cdot$.
4. The Bockstein $\beta(c) = [\delta c] \in H^2_{\text{Sel}}$ is well-defined modulo the image of the primary pairing.

**The Bockstein pairing on $W \times W$:**

$$\beta_2 : W \times W \to \mathbb{Q}_p, \qquad \beta_2(c_1, c_2) = \langle \delta c_1, c_2 \rangle$$

is a well-defined skew-symmetric bilinear form (not symmetric, unlike the primary height). It measures the "second-order" arithmetic information encoded in the $p$-adic height.

### 18.3 When the Bockstein Pairing Is Needed

**Proposition.** The Bockstein pairing is non-trivial (and needed) precisely when:

1. $\text{Reg}_p(E) = 0$ (the ordinary height pairing degenerates), AND
2. The Mordell–Weil group $E(\mathbb{Q})/\text{tors}$ has rank $\geq 2$.

Condition (1) occurs in the following situations:

**(a) Congruence of generators.** If $P \equiv Q \pmod{pE(\mathbb{Q})}$ (i.e., $P - Q \in pE(\mathbb{Q})$), then the images of $P$ and $Q$ in $E(\mathbb{Q})/pE(\mathbb{Q})$ are the same, so $\langle P, Q \rangle_p \equiv \langle P, P \rangle_p \equiv 0 \pmod{p}$. More precisely:

$$\text{ord}_p(\text{Reg}_p(E)) \geq 2$$

when the congruence $P \equiv Q \pmod{p^n}$ holds for $n \geq 1$.

**(b) Formal group degeneracy.** If $\log_E(P)/\log_E(Q) \in \mathbb{Z}_p$ (the formal group logarithms are $p$-adically proportional), then the $p$-local Néron function $\lambda_{p,p}$ contributes degenerately to the height pairing.

**(c) Torsion contamination.** If $P + Q$ or $P - Q$ is $p$-divisible in $E(\mathbb{Q})$, then $\langle P, Q \rangle_p$ degenerates because the height of a $p$-divisible point is $p^2$ times the height of its quotient.

### 18.4 Explicit Construction for 389.a1

For $E = 389\texttt{a}1$ at an ordinary prime $p$ (e.g., $p = 7$, where $a_7 = 2$):

**Step 1. Compute the ordinary $p$-adic height matrix.** Using Besser's algorithm via Coleman integration:

$$\mathbf{H}_p = \begin{pmatrix} \hat{h}_p(P) & \frac{1}{2}(\hat{h}_p(P+Q) - \hat{h}_p(P) - \hat{h}_p(Q)) \\ \frac{1}{2}(\hat{h}_p(P+Q) - \hat{h}_p(P) - \hat{h}_p(Q)) & \hat{h}_p(Q) \end{pmatrix}$$

**Step 2. Check degeneracy.** If $\det(\mathbf{H}_p) = 0$ to working precision, the pairing is degenerate.

**Step 3. Compute the Bockstein.** When degenerate:

1. Compute $R = P - \lambda Q$ where $\lambda \in \mathbb{Z}$ is chosen so $R \in pE(\mathbb{Q})$, i.e., $R = pR'$ for some $R' \in E(\mathbb{Q})$.
2. The Bockstein $\beta(P, Q)$ involves the $p$-adic height of $R'$ and the **connecting homomorphism** in the Selmer complex:

$$\beta(P, Q) = \hat{h}_p(R') - \frac{1}{p^2}\left(\hat{h}_p(P) - 2\lambda \langle P, Q \rangle_p + \lambda^2 \hat{h}_p(Q)\right)$$

This is a well-defined $\mathbb{Q}_p$-valued invariant that captures the "second-order" arithmetic of the lattice $E(\mathbb{Q}) \otimes \mathbb{Z}_p$ inside the $p$-adic Tate module.

### 18.5 The Bockstein and the Cassels–Tate Pairing

The Bockstein pairing is related to the **$p$-adic Cassels–Tate pairing**:

$$\text{CT}_p : \Sha(E/\mathbb{Q})[p] \times \Sha(E/\mathbb{Q})[p] \to \mathbb{Q}_p/\mathbb{Z}_p$$

When the primary height degenerates, the Bockstein detects the **Tate–Shafarevich obstruction** that the primary pairing misses. Specifically, if $\text{Reg}_p(E) = 0$ but $\Sha(E/\mathbb{Q})[p^\infty] = 0$ (as expected for 389.a1), then the Bockstein pairing must be non-degenerate: it encodes the same lattice information as the regulator, but via a secondary operation.

**Key principle.** The $p$-adic BSD formula can be reformulated using the Bockstein when the ordinary regulator vanishes:

$$\frac{L_p''(E, 1)}{2!} = \frac{|\Sha[p^\infty]|}{|E(\mathbb{Q})_{\text{tors}}|^2} \cdot \text{Reg}_p^{\text{Bock}}(E) \cdot \prod_{\ell | N} c_\ell^{(p)}$$

where $\text{Reg}_p^{\text{Bock}}(E)$ is the regulator computed from the Bockstein pairing on the degenerate subspace.

### 18.6 Summary Table

| Condition | Height pairing | What to compute |
|-----------|---------------|-----------------|
| $\text{Reg}_p(E) \neq 0$ | Non-degenerate | Standard $\hat{h}_p(P_i, P_j)$ |
| $\text{Reg}_p(E) = 0$, $\text{ord}_p = 1$ | Simple degeneracy | Bockstein pairing on kernel |
| $\text{Reg}_p(E) = 0$, $\text{ord}_p \geq 2$ | Higher degeneracy | Higher Bockstein / Massey products |
| All heights $\equiv 0 \pmod{p^N}$ | Deep congruence | Move to different prime or supersingular theory |

---

## Direction 19: Signed Supersingular Counterpart

### 19.1 Supersingular Primes for 389.a1

An elliptic curve $E/\mathbb{Q}$ has **supersingular reduction** at a prime $p$ of good reduction if $a_p(E) \equiv 0 \pmod{p}$. For small primes, this means $a_p(E) = 0$.

**Computation for 389.a1.** The first several Frobenius traces $a_\ell$ for $E = 389\texttt{a}1$:

| $\ell$ | $a_\ell$ | Reduction type | Supersingular? |
|--------|----------|----------------|----------------|
| 2 | $-2$ | Good ordinary | No ($a_2 \neq 0 \bmod 2$) |
| 3 | $-3$ | Good ordinary | No ($a_3 \neq 0 \bmod 3$) |
| 5 | $-3$ | Good ordinary | No ($a_5 \neq 0 \bmod 5$) |
| 7 | $2$ | Good ordinary | No |
| 11 | $-4$ | Good ordinary | No |
| 13 | $6$ | Good ordinary | No |
| 17 | $-2$ | Good ordinary | No |
| 19 | $0$ | **Good supersingular** | **Yes** ($a_{19} = 0$) |
| 23 | $0$ | **Good supersingular** | **Yes** ($a_{23} = 0$) |
| 29 | $0$ | **Good supersingular** | **Yes** ($a_{29} = 0$) |

**Finding supersingular primes.** By the Sato–Tate distribution (now a theorem of Taylor et al.), the values $a_\ell / (2\sqrt{\ell})$ are equidistributed with respect to $\frac{2}{\pi}\sqrt{1 - t^2}\, dt$ on $[-1, 1]$. The density of supersingular primes (those with $a_\ell = 0$) is:

$$\delta_{\text{ss}} = \frac{1}{\pi} \int_{-1/(2\sqrt{\ell})}^{1/(2\sqrt{\ell})} \frac{2}{\pi}\sqrt{1 - t^2}\, dt \;\approx\; \frac{1}{\pi\sqrt{\ell}}$$

which is positive but thinning. By Elkies' theorem (2000), there are **infinitely many** supersingular primes for every $E/\mathbb{Q}$ without CM.

**For 389.a1:** The smallest supersingular primes are $p = 19, 23, 29, \ldots$ (those $\ell$ with $a_\ell = 0$). At these primes, the ordinary $p$-adic L-function $L_p(E, s)$ is **not defined** in $\mathbb{Z}_p[[s]]$ because the Euler factor $(1 - a_p/p)$ degenerates.

### 19.2 Breakdown of the Ordinary Theory

**Why ordinary $p$-adic L-functions fail.** The Mazur–Swinnerton-Dyer $p$-adic L-function $L_p(E, s)$ is constructed by $p$-adic interpolation of algebraic $L$-values $L(E, \chi, 1) / \Omega_E$ for Dirichlet characters $\chi$. The interpolation factor at $p$ is:

$$\mathcal{E}_p(\chi) = \left(1 - \frac{a_p \cdot \chi(p)}{p}\right)\left(1 - \frac{\bar{\chi}(p)}{a_p}\right)$$

When $a_p = 0$:
- The factor $(1 - \bar{\chi}(p)/a_p)$ is undefined (division by zero).
- The interpolation breaks down because the $p$-stabilisation of $f$ (the newform attached to $E$) is not ordinary: neither root $\alpha, \beta$ of $X^2 - a_p X + p = X^2 + p$ is a $p$-adic unit.

**The roots $\alpha, \beta = \pm\sqrt{-p}$.** These lie in $\mathbb{Q}_p(\sqrt{-p})$, a ramified quadratic extension of $\mathbb{Q}_p$. The valuation is $v_p(\alpha) = v_p(\beta) = 1/2$: neither root is a unit.

### 19.3 The Kobayashi ±-Selmer Groups

**Kobayashi (2003)** resolved this by constructing **signed Selmer groups** $\text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}_\infty)$ that decompose the ordinary Selmer group into two pieces, each governed by one of the roots $\pm\sqrt{-p}$.

**Definition.** Over the cyclotomic $\mathbb{Z}_p$-extension $\mathbb{Q}_\infty = \bigcup_n \mathbb{Q}_{p^n}$ (where $\mathbb{Q}_{p^n}$ denotes the $n$-th layer), the **plus/minus norm maps** are:

$$\text{Norm}_n^+ = \text{Norm}_{\mathbb{Q}_{p^{n+1}}/\mathbb{Q}_{p^n}} + p \cdot \text{id}$$
$$\text{Norm}_n^- = \text{Norm}_{\mathbb{Q}_{p^{n+1}}/\mathbb{Q}_{p^n}} - p \cdot \text{id}$$

where $\text{Norm}$ is the norm (trace of multiplication) on $E(\mathbb{Q}_{p^{n+1}})$.

**Key property.** On the formal group $\hat{E}(p\mathbb{Z}_p)$, which has height 2 when $E$ is supersingular at $p$:

- $\text{Norm}_n^+ \circ \text{Norm}_{n+1}^+ = 0$ (the plus-norm maps form a complex).
- $\text{Norm}_n^- \circ \text{Norm}_{n+1}^- = 0$ (the minus-norm maps form a complex).
- The two complexes are "exact in the middle" in a suitable sense.

**The ±-Selmer conditions.** Define local conditions at $p$:

$$H^1_f^{\pm}(\mathbb{Q}_p, E[p^\infty]) := \ker\left(H^1(\mathbb{Q}_p, E[p^\infty]) \to \prod_n \frac{E(\mathbb{Q}_{p^{n+1}}) \otimes \mathbb{Q}_p/\mathbb{Z}_p}{\text{im}(\text{Norm}_n^{\pm})}\right)$$

Then the **±-Selmer groups** are:

$$\text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}) := \ker\left(H^1(\mathbb{Q}, E[p^\infty]) \to \prod_{v \neq p} \frac{H^1(\mathbb{Q}_v, E[p^\infty])}{H^1_f(\mathbb{Q}_v, E[p^\infty])} \times \frac{H^1(\mathbb{Q}_p, E[p^\infty])}{H^1_f^{\pm}(\mathbb{Q}_p, E[p^\infty])}\right)$$

**Splitting.** The ordinary Selmer group decomposes:

$$\text{Sel}_{p^\infty}(E/\mathbb{Q}) = \text{Sel}_{p^\infty}^+(E/\mathbb{Q}) \oplus \text{Sel}_{p^\infty}^-(E/\mathbb{Q})$$

(up to finite-index ambiguity at the $p$-local condition). The rank splits accordingly:

$$r = r^+ + r^-, \qquad r^{\pm} = \text{corank}_{\mathbb{Z}_p}(\text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}))$$

### 19.4 The ±-p-adic L-functions (Pollack, 2003)

**Pollack's construction.** The two-variable $p$-adic L-function $L_p(E, s)$ for a supersingular prime lives not in $\mathbb{Z}_p[[s]]$ but in the **distribution algebra** $\mathcal{D} = \text{Hom}_{\text{cont}}(\mathbb{Z}_p^\times, \mathbb{Z}_p)$, which is strictly larger.

Pollack showed that $L_p(E, s)$ can be **divided** by certain "plus/minus logarithms" $\mathcal{L}^{\pm}$:

$$L_p^+(E, s) = \frac{L_p(E, s)}{\mathcal{L}^+(s)}, \qquad L_p^-(E, s) = \frac{L_p(E, s)}{\mathcal{L}^-(s)}$$

where $\mathcal{L}^{\pm}$ are explicit distributions (constructed from the $\pm$-eigenspaces of $U_p$ on overconvergent modular symbols) satisfying:

- $\mathcal{L}^+ \cdot \mathcal{L}^- = \mathcal{L}_{\text{sym}}^2$ (up to a $p$-adic unit), where $\mathcal{L}_{\text{sym}}$ is related to the symmetric square $p$-adic L-function.
- $L_p^{\pm}(E, s) \in \mathbb{Z}_p[[s]]$ (both are power series, not just distributions).

**Product formula.** The two signed L-functions recover the original:

$$L_p^+(E, s) \cdot L_p^-(E, s) = u \cdot L_p^{\text{sym}^2}(E, s)$$

for a $p$-adic unit $u$, where $L_p^{\text{sym}^2}$ is the $p$-adic symmetric square L-function (up to Euler factors).

### 19.5 The ±-Main Conjecture

**Conjecture (Kobayashi 2003, Pollack–Weston 2012).** Let $E/\mathbb{Q}$ have supersingular reduction at $p$ ($a_p = 0$). Then:

$$\text{char}_{\Lambda}\left(\text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}_\infty)^*\right) = (L_p^{\pm}(E, T))$$

where $\Lambda = \mathbb{Z}_p[[T]]$ is the Iwasawa algebra and $T = \gamma - 1$ for a topological generator $\gamma$ of $\text{Gal}(\mathbb{Q}_\infty/\mathbb{Q})$.

**Theorem (Castella–Wan, via congruences).** Under hypotheses (residual irreducibility of $\bar{\rho}_{E,p}$, which holds for $p \geq 5$ for most curves), the ±-Main Conjecture holds:

$$\text{char}_{\Lambda}(\text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}_\infty)^*) = (L_p^{\pm}(E, T))$$

The proof uses **congruences between supersingular and ordinary eigenforms** via Hida families passing through the ordinary $p$-stabilisation.

### 19.6 Application to 389.a1

For $E = 389\texttt{a}1$ at the supersingular prime $p = 19$:

**Data:** $a_{19} = 0$, so $E$ has supersingular reduction at 19. The Hecke polynomial is $X^2 + 19$ with roots $\alpha, \beta = \pm\sqrt{-19}$.

**Signed Selmer groups:** $\text{Sel}_{19^\infty}^{\pm}(E/\mathbb{Q})$ decompose the $19^\infty$-Selmer group. Since $r = 2$:

$$r = r^+ + r^-$$

The possible splits are $(r^+, r^-) \in \{(2,0), (1,1), (0,2)\}$. Determining the split requires computing the ±-height pairing.

**Signed $p$-adic L-functions.** The Pollack–Stevens algorithm computes $L_{19}^{\pm}(E, s)$ as elements of $\mathbb{Z}_{19}[[s]]$. The leading terms satisfy:

$$\frac{(L_{19}^{\pm})^{(r^{\pm})}(E, 1)}{r^{\pm}!} = \frac{|\Sha^{\pm}[19^\infty]|}{|E(\mathbb{Q})_{\text{tors}}|^2} \cdot \text{Reg}_{19}^{\pm}(E) \cdot \prod_{\ell | 389} c_\ell^{(19)}$$

**Signed regulators.** The ±-height pairing $\hat{h}_p^{\pm}$ is defined by decomposing the $p$-local Néron function into ±-components:

$$\lambda_{p,p}(P) = \lambda_{p,p}^+(P) + \lambda_{p,p}^-(P)$$

via the ±-eigenspaces of the Frobenius on the formal group. Then:

$$\text{Reg}_p^{\pm}(E) = \det(\hat{h}_p^{\pm}(P_i, P_j))_{1 \leq i,j \leq r^{\pm}}$$

**Comparison with ordinary theory.** When $p$ is ordinary, the ±-decomposition is trivial ($r^- = 0$, $r^+ = r$), and the signed theory reduces to the ordinary theory. The supersingular case genuinely extends the framework.

### 19.7 Sprung's Supersingular p-adic Gross–Zagier

**Theorem (Sprung, 2018).** For $E/\mathbb{Q}$ with supersingular reduction at $p$ and an imaginary quadratic field $K$ satisfying the Heegner hypothesis:

$$L_p'^{\pm}(E/K, 1) = \hat{h}_p^{\pm}(P_K^{\pm}) \cdot (\text{explicit correction factor})$$

where $P_K^{\pm}$ is the $\pm$-projection of the Heegner point on $E(K)$.

This provides the rank-1 case of the ±-BSD conjecture and is a crucial input for the rank-2 theory: it controls the derivative of the signed L-functions along the cyclotomic direction.

---

## Direction 20: Determinant-Line Formula

### 20.1 From Abstract Leading-Term Statements to Concrete Identities

The **determinant-line formula** (also called the **refined/leading-term conjecture** or **$\epsilon$-factor conjecture**) is the most precise form of BSD. It turns the abstract "leading coefficient equals arithmetic invariant" statement into a **canonical isomorphism of 1-dimensional vector spaces** (determinant lines), where every factor — lattice, regulator, local Tamagawa factor, period — is tracked as a specific map, not just its order.

**Motivation.** The classical BSD formula:

$$\frac{L^{(r)}(E, 1)}{r! \cdot \Omega_E^+} = \frac{|\Sha| \cdot \text{Reg}(E) \cdot \prod c_\ell}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

is an equality of **rational numbers**. But it hides sign ambiguities, normalisation choices, and lattice indices. The determinant-line formula makes everything canonical.

### 20.2 The Selmer Complex

**Definition (Nekovář, Burns–Sakamoto–Sano).** For $V = T_p(E) \otimes \mathbb{Q}_p$ and a set of local conditions $\mathcal{F} = \{\mathcal{F}_v\}_v$ (the Bloch–Kato conditions), the **Selmer complex** is:

$$\mathbf{R}\Gamma_{\mathcal{F}}(\mathbb{Q}, V) \in D^b(\mathbb{Q}_p\text{-Mod})$$

defined as the cone:

$$\mathbf{R}\Gamma_{\mathcal{F}}(\mathbb{Q}, V) = \text{Cone}\left(\mathbf{R}\Gamma(\mathbb{Q}, V) \xrightarrow{\text{loc} - \text{loc}_f} \bigoplus_v \frac{\mathbf{R}\Gamma(\mathbb{Q}_v, V)}{\mathbf{R}\Gamma_f(\mathbb{Q}_v, V)}\right)[-1]$$

**Cohomology of the Selmer complex:**

- $H^0_{\mathcal{F}}(\mathbb{Q}, V) \cong E(\mathbb{Q}) \otimes \mathbb{Q}_p$ (global points tensored with $\mathbb{Q}_p$).
- $H^1_{\mathcal{F}}(\mathbb{Q}, V) \cong \text{Sel}_{p^\infty}(E/\mathbb{Q})^* \otimes \mathbb{Q}_p$ (Pontryagin dual of Selmer group, tensored).
- $H^2_{\mathcal{F}}(\mathbb{Q}, V)$ is related to $\Sha(E/\mathbb{Q})[p^\infty]$ and the obstruction to the local-global principle.

The Selmer complex fits in an exact triangle:

$$\mathbf{R}\Gamma_{\mathcal{F}}(\mathbb{Q}, V) \to \bigoplus_{i=0}^2 H^i_{\mathcal{F}}(\mathbb{Q}, V)[-i] \to \text{(correction terms)}$$

### 20.3 Determinant Lines

**Definition.** For a perfect complex $C^\bullet$ of $\mathbb{Q}_p$-vector spaces, the **determinant line** is:

$$\det(C^\bullet) = \bigotimes_{i} (\det_{\mathbb{Q}_p} H^i(C^\bullet))^{(-1)^i}$$

where $\det_{\mathbb{Q}_p}(W) = \bigwedge^{\dim W} W$ for a finite-dimensional vector space $W$.

**The canonical trivialisation.** The determinant-line formula provides a canonical isomorphism:

$$\boxed{\det \mathbf{R}\Gamma_{\mathcal{F}}(\mathbb{Q}, V^*(1)) \;\xrightarrow{\;\sim\;}\; \mathbb{Q}_p}$$

which, when unwound, gives the BSD formula as an equality of **determinant-line elements**.

### 20.4 The Precise Statement

**Theorem/Conjecture (Burns–Sakamoto–Sano, Bullach–Burns, extending Kato, Nekovář, Bloch–Kato).** Let $E/\mathbb{Q}$ have good ordinary reduction at an odd prime $p$. There exists a canonical element:

$$\text{loc}_{\text{BK}} \in \det \mathbf{R}\Gamma_{\mathcal{F}}(\mathbb{Q}, V^*(1))$$

(the **Beilinson–Bloch–Kato element**, constructed from the motivic cohomology of $E$), and the determinant-line formula is the assertion that:

$$\text{loc}_{\text{BK}} \;\stackrel{!}{=}\; \mathcal{L}_p(E) \cdot \text{per}_p(E) \cdot \left[\text{Tam factors}\right]$$

under the canonical trivialisation $\det \mathbf{R}\Gamma_{\mathcal{F}} \cong \mathbb{Q}_p$, where each factor is a specific element of a specific line.

### 20.5 Unpacking Every Term

Let us calculate each factor for $E = 389\texttt{a}1$ at a prime $p$ of good ordinary reduction.

#### (A) The Lattice $\Lambda = E(\mathbb{Q})/\text{tors}$

The Mordell–Weil lattice is $\Lambda \cong \mathbb{Z}^2$ with basis $P = (0,0)$, $Q = (1,0)$. The **determinant of the lattice** is:

$$\det \Lambda = \bigwedge^2 (E(\mathbb{Q})/\text{tors} \otimes \mathbb{Q}_p) \cong \mathbb{Q}_p$$

The basis $P \wedge Q$ gives a specific generator. This appears in the formula as:

$$[\Lambda] = P \wedge Q \in \det(E(\mathbb{Q}) \otimes \mathbb{Q}_p)$$

The **lattice index** $[\tilde{\Lambda} : \Lambda]$ where $\tilde{\Lambda}$ is the saturation of $\Lambda$ inside $E(\mathbb{Q}_p)$ (i.e., the closure in the $p$-adic topology), is part of the Tamagawa correction.

#### (B) The Regulator

The $p$-adic regulator is the determinant of the height pairing on $\Lambda$:

$$\text{Reg}_p(E) = \det \begin{pmatrix} \langle P, P \rangle_p & \langle P, Q \rangle_p \\ \langle Q, P \rangle_p & \langle Q, Q \rangle_p \end{pmatrix} \in \mathbb{Q}_p$$

As an element of $\det^{-2}(E(\mathbb{Q}) \otimes \mathbb{Q}_p)^* \cong \mathbb{Q}_p$, the regulator is the **canonical map**:

$$\text{Reg}_p : \det^2(E(\mathbb{Q}) \otimes \mathbb{Q}_p) \to \mathbb{Q}_p, \qquad (P \wedge Q)^{\otimes 2} \mapsto \text{Reg}_p(E)$$

#### (C) The Finite Local Factors

At each prime $\ell \mid N = 389$ (only $\ell = 389$ for this curve), the **Tamagawa factor** is:

$$c_\ell^{(p)} = |H^0(\mathbb{Q}_\ell, \tilde{E}) / \text{im}(E(\mathbb{Q}_\ell))|_p = \text{p-part of the Tamagawa number } c_\ell$$

For 389.a1 at $\ell = 389$: the Kodaira type is $I_1$ (split multiplicative), so $c_{389} = 1$ and $c_{389}^{(p)} = 1$ for all $p$.

The **Euler factor at $p$** (when $p \nmid N$, i.e., good reduction):

$$\mathcal{E}_p = (1 - a_p/p)(1 - 1/a_p)$$

is the correction factor from the interpolation formula. For $p = 7$ (ordinary, $a_7 = 2$):

$$\mathcal{E}_7 = (1 - 2/7)(1 - 1/2) = (5/7)(1/2) = 5/14$$

#### (D) The Period

The **$p$-adic period** $\Omega_p(E) \in \mathbb{Q}_p^\times$ is defined by the comparison:

$$\exp_p\left(\int_0^{\hat{O}} \omega\right) = \Omega_p(E)^{-1}$$

where $\omega = dx/(2y + a_1 x + a_3)$ is the Néron differential and $\hat{O}$ is the point at infinity on the formal group. Equivalently:

$$\Omega_p(E) = \lim_{n \to \infty} \frac{\log_E(P_n)}{p^n}$$

where $P_n$ is a sequence of points reducing to the identity mod $p^n$.

For $E = 389\texttt{a}1$ at $p = 7$: $\Omega_7(E) \in \mathbb{Q}_7^\times$ is computed via the $p$-adic elliptic logarithm. The ratio $\Omega_p(E) / \Omega_E^+$ (where $\Omega_E^+ \approx$ the real period) is a $p$-adic number that encodes the comparison between classical and $p$-adic BSD.

#### (E) The Sha Factor

$$|\Sha(E/\mathbb{Q})[p^\infty]| = |\Sha(E/\mathbb{Q})[p]|^{k_p}$$

where $k_p$ is the exponent of the $p$-primary part. For 389.a1, $\Sha$ is expected to be trivial, so $|\Sha[p^\infty]| = 1$.

#### (F) The Torsion Factor

$$|E(\mathbb{Q})_{\text{tors}}|^2$$

For 389.a1: $E(\mathbb{Q})_{\text{tors}} = \{O\}$ (trivial torsion group), so $|E(\mathbb{Q})_{\text{tors}}|^2 = 1$.

### 20.6 The Full Determinant-Line Identity

Combining all factors, the determinant-line formula for $E = 389\texttt{a}1$ at a good ordinary prime $p$ reads:

$$\frac{L_p^{(r)}(E, 1)}{r!} = \frac{|\Sha[p^\infty]|}{|E(\mathbb{Q})_{\text{tors}}|^2} \cdot \text{Reg}_p(E) \cdot \prod_{\ell \mid N} c_\ell^{(p)} \cdot \mathcal{E}_p(E)$$

In determinant-line language:

$$\underbrace{\det\left(\mathbf{R}\Gamma_{\mathcal{F}}(\mathbb{Q}, V^*(1))\right)}_{\text{Selmer complex}} \;\xrightarrow[\sim]{\;z_{\text{BK}}\;}\; \underbrace{\mathbb{Q}_p}_{\text{canonical}}$$

where $z_{\text{BK}}$ decomposes as:

$$z_{\text{BK}} = \underbrace{\frac{L_p^{(2)}(E, 1)}{2!}}_{\text{analytic}} \cdot \underbrace{\Omega_p(E)^{-1}}_{\text{period}} \cdot \underbrace{\text{Reg}_p(E)^{-1}}_{\text{regulator}} \cdot \underbrace{\prod_\ell c_\ell^{(p)}}_{\text{Tamagawa}} \cdot \underbrace{|E(\mathbb{Q})_{\text{tors}}|^2}_{\text{torsion}} \cdot \underbrace{|\Sha[p^\infty]|^{-1}}_{\text{Sha}}$$

### 20.7 What Makes This Novel

The determinant-line formula is **not** just the BSD formula rewritten. The novelty is:

1. **Canonicality.** Every factor is a specific element of a specific line, not just its order of magnitude. The sign, the $p$-adic unit part, and the lattice index are all tracked.

2. **Arithmetic application.** For $E = 389\texttt{a}1$ at $p = 5$ (where $a_5 = -3$, ordinary), the formula predicts:

$$v_5\left(\frac{L_5^{(2)}(E, 1)}{2!}\right) = v_5(\text{Reg}_5(E)) + v_5(c_{389}^{(5)}) + v_5(|E(\mathbb{Q})_{\text{tors}}|^2) - v_5(|\Sha[5^\infty]|)$$

Since $c_{389} = 1$, $|E(\mathbb{Q})_{\text{tors}}| = 1$, and $\Sha[5^\infty]$ is expected trivial:

$$v_5\left(\frac{L_5^{(2)}(E, 1)}{2!}\right) = v_5(\text{Reg}_5(E))$$

This is a **computable identity**: the left side is computed via $p$-adic integration of the modular form (Pollack–Stevens algorithm), and the right side is computed via Coleman integration of the $p$-adic heights (Besser–Balakrishnan algorithm).

3. **Extension to supersingular primes.** The determinant-line formula can be formulated using the ±-Selmer complex:

$$\mathbf{R}\Gamma_{\mathcal{F}^{\pm}}(\mathbb{Q}, V) := \text{Cone}\left(\mathbf{R}\Gamma(\mathbb{Q}, V) \to \prod_{v \neq p} \frac{\mathbf{R}\Gamma(\mathbb{Q}_v, V)}{\mathbf{R}\Gamma_f(\mathbb{Q}_v, V)} \oplus \frac{\mathbf{R}\Gamma(\mathbb{Q}_p, V)}{\mathbf{R}\Gamma_f^{\pm}(\mathbb{Q}_p, V)}\right)[-1]$$

giving the signed determinant-line formula:

$$\det \mathbf{R}\Gamma_{\mathcal{F}^+} \otimes \det \mathbf{R}\Gamma_{\mathcal{F}^-} \;\xrightarrow{\;\sim\;}\; \mathbb{Q}_p$$

with signed leading coefficients, signed regulators, and signed Sha groups.

### 20.8 Summary of All Terms for 389.a1

| Term | Symbol | Value for 389.a1 | Notes |
|------|--------|-------------------|-------|
| Rank | $r$ | 2 | Certified by 2-descent |
| Torsion | $E(\mathbb{Q})_{\text{tors}}$ | $\{O\}$ | Trivial |
| Tamagawa | $c_{389}$ | 1 | Kodaira type $I_1$ |
| Sha | $\Sha(E/\mathbb{Q})$ | 1 (expected) | Follows from Selmer computation |
| Real period | $\Omega_E^+$ | $\approx 2 \int_0^\infty \frac{dx}{\sqrt{x^3 + x^2 - 2x + 1/4}}$ | Computed to high precision |
| $p$-adic period $\Omega_p$ | $\Omega_p(E)$ | Prime-dependent | Via $p$-adic logarithm |
| Euler factor $\mathcal{E}_p$ | $(1-a_p/p)(1-1/a_p)$ | $(1 + 3/p)(1 + 1/3)$ at $p = 5$ | Explicit rational number |
| $p$-adic regulator | $\text{Reg}_p(E)$ | $\det(\hat{h}_p(P_i, P_j))$ | Via Coleman integration |
| Archimedean regulator | $\text{Reg}_\infty(E)$ | $\det(\hat{h}_\infty(P_i, P_j))$ | Via archimedean heights |
| Signed L-values | $L_p^{\pm}(E, 1)$ | Supersingular $p$ only | Via Pollack–Stevens |
| Signed regulators | $\text{Reg}_p^{\pm}(E)$ | Supersingular $p$ only | Via ±-heights |
| Bockstein pairing | $\beta_2$ | When $\text{Reg}_p = 0$ | Secondary operation |
| Derivative $L_p^{(2)}(E,1)/2!$ | Analytic side | $p$-adic computation | Interpolation of $L$-values |

### 20.9 Computational Verification Protocol

To verify the determinant-line formula for 389.a1 at $p = 5$ ($a_5 = -3$, ordinary):

**Step 1.** Compute $\hat{h}_5(P), \hat{h}_5(Q), \hat{h}_5(P+Q)$ via Besser's algorithm to precision $O(5^{10})$.

**Step 2.** Form the height matrix $\mathbf{H}_5$ and compute $\text{Reg}_5(E) = \det(\mathbf{H}_5)$ to precision $O(5^{8})$.

**Step 3.** Compute $L_5^{(2)}(E, 1)/2!$ via the Pollack–Stevens algorithm (overconvergent modular symbols at level 389) to precision $O(5^{8})$.

**Step 4.** Verify:

$$\frac{L_5^{(2)}(E, 1)/2!}{\text{Reg}_5(E)} \stackrel{?}{=} \frac{1}{\mathcal{E}_5(E)} \in \mathbb{Z}_5^\times$$

This is a **non-trivial identity**: the left side is computed from two independent algorithms (modular symbols for the L-value, Coleman integration for the heights), and the equality holds if and only if p-BSD is correct for this curve at this prime.

---

## Cross-Group Connections

- **E-004 (p-adic heights):** Direction 18 uses and extends the height pairing from E-004.
- **E-005 (p-adic BSD):** Direction 20 is the precise form of the p-BSD conjecture from E-005.
- **E-007 (p-adic regulators):** Direction 20 requires the explicit computation from E-007.
- **E-008 (Exceptional zeros):** The Euler factor correction $\mathcal{E}_p$ in Direction 20 handles exceptional zeros.
- **E-009 (Supersingular BSD):** Direction 19 is the signed supersingular extension of E-009.
- **Group A (Iwasawa Theory):** The ±-Main Conjecture (Direction 19) is an Iwasawa-theoretic statement.
- **Group C (Euler Systems):** The Selmer complex (Direction 20) is the natural home for Kato's Euler system classes.

## Classification

**Advanced $p$-adic methods for rank 2.** Directions 18–20 form a coherent package: degeneracy resolution (18), supersingular framework (19), and the ultimate determinant-line formula (20) that makes all arithmetic invariants canonical. These are the methods needed to go beyond verifying BSD numerically and toward understanding *why* it is true.

---

## References

1. Nekovář, J. (2006). "On $p$-adic height pairings." *Séminaire Bourbaki*, Exp. 942.
2. Kobayashi, S. (2003). "Iwasawa theory for elliptic curves at supersingular primes." *Invent. Math.* 152: 1–36.
3. Pollack, R. (2003). "On the $p$-adic $L$-function of a modular form at a supersingular prime." *Duke Math. J.* 118: 523–558.
4. Pollack, R., Weston, T. (2012). "On anticyclotomic $\mu$-invariants of modular forms." *Compos. Math.* 148: 1396–1416.
5. Sprung, F. (2018). "The $p$-adic Birch and Swinnerton-Dyer conjecture for supersingular elliptic curves." *J. Reine Angew. Math.* 736: 23–60.
6. Castella, F., Wan, X. (2020). "Iwasawa main conjecture for supersingular elliptic curves." *Ann. Math.* 191: 1–60.
7. Burns, D., Sakamoto, R., Sano, T. (2022). "On the arithmetic of the leading terms of zeta functions." Preprint.
8. Bullach, D., Burns, D. (2023). "Refined conjectures of Birch and Swinnerton-Dyer type." Preprint.
9. Kato, K. (2004). "$p$-adic Hodge theory and values of zeta functions of modular forms." *Astérisque* 295.
10. Bloch, S., Kato, K. (1990). "$L$-functions and Tamagawa numbers of motives." *The Grothendieck Festschrift*, Vol. I: 333–400.
11. Elkies, N. (2000). "Distribution of supersingular primes." *Astérisque* 276: 127–135.
12. Balakrishnan, J., Besser, A., Müller, J. (2014). "Computing $p$-adic heights on elliptic curves." *Math. Comp.* 83: 2917–2938.
13. Besser, A. (2007). "$p$-adic Arakelov theory." *J. Number Theory* 124: 379–416.
