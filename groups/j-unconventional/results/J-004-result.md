# J-004: Kudla Program: Arithmetic Siegel–Weil Formula

**Direction ID:** J-004
**Group:** J — Unconventional and Emerging Approaches
**Classification:** Conjecture (major cases proven, full formula open)

---

## Status Assessment

The Kudla program is one of the most actively pursued bridges between automorphic forms and arithmetic geometry. The unramified arithmetic Siegel–Weil formula for unitary Shimura varieties has been established by Kudla–Rapoport, and Liu has proven the local arithmetic Siegel–Weil formula. Yuan–Zhang proved the averaged form of the arithmetic Gross–Zagier formula. The original Gross–Zagier theorem is the $\operatorname{GU}(1,1)$-special case of the program.

However, the **full arithmetic Siegel–Weil formula for $\operatorname{GU}(1,1)$ in the ramified case** — precisely the case needed to express $L'(E,1)$ as an arithmetic intersection number for arbitrary elliptic curves $E/\mathbb{Q}$ — remains open. The global conjecture of Kudla relating generating series of arithmetic intersection numbers to incoherent Eisenstein series has been established in many cases but not in the generality needed for unconditional BSD applications.

**Feasibility assessment:** Medium-term (5–10 years) for the ramified $\operatorname{GU}(1,1)$ case, given current pace. The required ingredients — integral models of Shimura curves at ramified primes, local intersection formulas, and archimedean contributions via the hermitian line bundle — are each the subject of active research. The direction is high-risk in the sense that completing the ramified case requires solving several difficult open problems simultaneously, but it is well-motivated and the community is converging.

---

## Testable Conjecture or Lemma

### Arithmetic Siegel–Weil Formula for GU(1,1) — Conjectural Statement

Let $F = \mathbb{Q}$, let $B$ be an indefinite quaternion algebra over $\mathbb{Q}$ of discriminant $D$, and let $V$ be the space of trace-zero elements in $B$ equipped with the reduced norm quadratic form. Fix an even lattice $L \subset V$ of signature $(1,1)$.

Let $\mathcal{M}$ be the integral model (à la Kisin–Pappas) of the Shimura variety $\operatorname{Sh}_K(G, X)$ associated to $G = \operatorname{GU}(1,1)$ with hyperspecial level $K = K_p K^p$ at good primes and parahoric level at ramified primes. For each $m \in \mathbb{Z}_{>0}$, define the **special cycle**

$$\mathcal{Z}(m) = \{ x \in \mathcal{M} : \exists g \in V,\; q(g) = m,\; x \in \operatorname{CM}(g) \}$$

as a codimension-1 cycle on $\mathcal{M}$, where $\operatorname{CM}(g)$ denotes the locus of points with extra endomorphism by $\mathbb{Z}[g]$.

**Conjecture (Arithmetic Siegel–Weil for GU(1,1)).** *The generating series*

$$\hat{\phi}(\tau) = \hat{E}_2(\tau) + \sum_{m > 0} \widehat{\deg}\bigl(\hat{\mathcal{Z}}(m)\bigr)\, q^m \in M_{3/2}^{\operatorname{Kudla}}(\widehat{\mathbb{Z}})$$

*is a $3/2$-weight Kudla-modular form whose central derivative at $s = 1/2$ encodes the arithmetic degree of $\hat{\mathcal{Z}}(m)$. Here $\hat{\mathcal{Z}}(m) = (\mathcal{Z}(m), g_m)$ is the arithmetic cycle equipped with the Green function $g_m$ (the archimedean component), and $\widehat{\deg}$ is the arithmetic degree in the sense of Gillet–Soulé.*

**Arithmetic Gross–Zagier (Consequence).** For an elliptic curve $E/\mathbb{Q}$ of conductor $N$ of rank 1, with $D \| N$ and $D$ the discriminant of the quaternion algebra:

$$\widehat{\deg}\bigl(\hat{\mathcal{Z}}(1)\bigr) = \frac{L'(E, 1)}{\Omega_E^+} \cdot C_E$$

where $\Omega_E^+$ is the real period and $C_E$ is an explicit product of local Tamagawa-type factors and lattice invariants.

### Lean-Ready Reformulation

**Conjecture (Lean-formalizable).** For $E/\mathbb{Q}$ an elliptic curve of rank 1, the arithmetic intersection number $\hat{\deg}(\hat{\mathcal{Z}}(1))$ on the integral model $\mathcal{M}$ of the Shimura curve for $\operatorname{GU}(1,1)$ equals $c \cdot L'(E,1)/\Omega_E^+$ for an explicit computable constant $c$ depending only on the level structure.

---

## Approach Summary

### Step 1: Setup the Shimura Variety

For $G = \operatorname{GU}(1,1)$ over $\mathbb{Q}$, the Shimura variety $\operatorname{Sh}(G, X)$ is a Shimura curve — a moduli space for abelian surfaces $A$ with:
- $\operatorname{End}(A) \supseteq \mathcal{O}_B$ (quaternionic multiplication),
- a polarization condition on the $\mathcal{O}_B$-module structure,
- level structure given by $K$.

The integral model $\mathcal{M}$ over $\mathbb{Z}[1/N']$ (with suitable localization) requires the Kisin–Pappas integral models at primes dividing the discriminant $D$, where parahoric level replaces hyperspecial.

### Step 2: Define Special Cycles and Arithmetic Intersections

For $m > 0$ and $g \in V$ with $q(g) = m$, the special cycle $\mathcal{Z}(m)$ is a divisor on $\mathcal{M}$. The arithmetic Chow group $\widehat{\mathrm{CH}}^1(\mathcal{M})$ classifies pairs $(Z, g_Z)$ where $Z$ is a divisor and $g_Z$ is a Green current. The arithmetic degree map:

$$\widehat{\deg}: \widehat{\mathrm{CH}}^1(\mathcal{M}_{\mathbb{Z}}) \to \mathbb{R}$$

is the composition of the arithmetic degree with Gillet–Soulé's arithmetic intersection theory.

### Step 3: Construct the Incoherent Eisenstein Series

To the quadratic space $(V, q)$ of signature $(1,1)$, Kudla associates an **incoherent collection** $\{(V_p, q_p)\}_p$ — local quadratic spaces everywhere that do not globalize. The associated Eisenstein series $E(\tau, s)$ is a Siegel–Eisenstein series on $\operatorname{SL}_2$ whose Fourier coefficients $c(m, s)$ at $s = 1/2$ should equal $\widehat{\deg}(\hat{\mathcal{Z}}(m))$.

### Step 4: Local Intersection Formulas

At each prime $p$:
- **$p \nmid ND$:** The local intersection multiplicity is computed by the Kudla–Rapoport intersection formula (unramified case, fully resolved).
- **$p \| D$:** The ramified case requires analyzing the Rapoport–Zink space for $\operatorname{GU}(1,1)$ at $p$, the special fiber of the integral model, and computing intersection multiplicities via the Rapoport–Zink uniformization. This is the **main open case**.
- **$p^2 \| N$:** Supersingular primes require different techniques.

### Step 5: Global Assembly and BSD

The global arithmetic Siegel–Weil formula states:

$$\widehat{\deg}\bigl(\hat{\mathcal{Z}}(m)\bigr) = \sum_{p \leq \infty} \text{loc}_p(c_m)$$

where $\text{loc}_p(c_m)$ is the $p$-adic (or archimedean) Fourier coefficient. For $m = 1$ and $E$ of rank 1, this yields $L'(E, 1)/\Omega_E^+$.

---

## Computational Example

### Example: $E = 11a1$, $D = 11$

Consider the elliptic curve $E: y^2 + y = x^3 - x^2 - 10x - 20$ of conductor $N = 11$ (Cremona label 11a1), which has rank 1. The quaternion algebra $B$ with discriminant $D = 11$ is the unique indefinite quaternion algebra over $\mathbb{Q}$ ramified exactly at $11$.

**Setup:** Take $L = \mathcal{O}_B^{(0)}$ (trace-zero elements) with the reduced norm. Since $B$ is ramified at 11 and $\infty$ is split, the Shimura curve $X_0^B(1)$ has a natural integral model $\mathcal{M}$ over $\mathbb{Z}[1/2]$ (or suitable localization).

**Special cycle $\mathcal{Z}(1)$:** This is the locus of points $x \in \mathcal{M}$ corresponding to abelian surfaces with an extra endomorphism $g$ satisfying $\operatorname{Nm}(g) = 1$. At the prime 11 (ramified), this requires the Kisin–Pappas parahoric integral model.

**Numerical verification (known results):**
- $L'(E, 1) = 0.2538418204...$
- $\Omega_E^+ = 1.2692093044...$
- $L'(E,1)/\Omega_E^+ = 0.19999... \approx 1/5$

The arithmetic intersection number $\widehat{\deg}(\hat{\mathcal{Z}}(1))$ should equal $1/5$ (up to explicit local factors). The constant involves:
- The Tamagawa number $c_{11} = 1$ (split multiplicative reduction).
- Lattice volume factors from the choice of $L$.
- The product of local intersection multiplicities at all primes.

**Remark:** For primes $p \nmid 11$, the local intersection multiplicities are computed by the Kudla–Rapoport formula in terms of representation densities. At $p = 11$, the ramified intersection is the obstruction to a fully unconditional computation.

### Eisenstein Series Coefficients

The incoherent Eisenstein series $E_{3/2}(\tau)$ associated to the incoherent quadratic space has initial Fourier coefficients:

| $m$ | $c(m, 1/2)$ | $\widehat{\deg}(\hat{\mathcal{Z}}(m))$ expected |
|-----|-------------|------------------------------------------------|
| 1   | $a_1$       | $L'(E,1)/\Omega_E^+ \cdot C$                  |
| 2   | $a_2$       | arithmetic intersection of $\mathcal{Z}(2)$   |
| 3   | $a_3$       | arithmetic intersection of $\mathcal{Z}(3)$   |

where $a_m$ are explicit Eisenstein coefficients expressible in terms of representation densities of the lattice $L$.

---

## Obstacle Analysis

### Obstacle 1: Ramified Local Intersection Theory (CRITICAL)

**Status:** Open. The Kudla–Rapoport local arithmetic Siegel–Weil formula has been proven in the unramified case. For primes $p | D$ (discriminant of the quaternion algebra), the local model of the Shimura variety is not smooth, and the Rapoport–Zink space has a more complicated structure.

**Required:** A local intersection formula at ramified primes for the parahoric integral model of the Shimura curve. Recent work by Li, Howard, and others has made progress, but a complete formula analogous to the unramified case is not available.

**Impact without resolution:** One cannot unconditionally compute $\widehat{\deg}(\hat{\mathcal{Z}}(m))$ for Shimura curves arising from ramified quaternion algebras — which are exactly the ones relevant to rank 1 elliptic curves.

### Obstacle 2: Archimedean Contributions

**Status:** Partially resolved. The archimedean component of the arithmetic intersection involves:
- The Green function $g_m$ on the upper half-plane associated to $m$.
- Its arithmetic degree, which is essentially a logarithm of a theta function.
- Harmonic analysis on $\operatorname{SU}(1,1)$ and the Weil representation.

The archimedean Siegel–Weil formula (Ichino) provides the needed identity in many cases, but linking it to the Gillet–Soulé arithmetic degree requires careful normalization.

### Obstacle 3: Integral Models at Bad Primes

**Status:** Active research. The Kisin–Pappas construction provides integral models for Shimura varieties with parahoric level, but:
- Explicit description of the special fiber at ramified primes is difficult.
- Computing intersection multiplicities on the special fiber requires detailed knowledge of the Bruhat–Tits building and local models.
- For the $\operatorname{GU}(1,1)$ case specifically, the local model is a degeneration of a smooth curve, and intersection theory on singular curves is delicate.

### Obstacle 4: From Intersection Numbers to L-values

**Status:** Conceptually clear, technically demanding. Even given the local formulas, assembling them into the global identity requires:
- Matching of normalizations between the automorphic and geometric sides.
- Compatibility of the Gillet–Soulé arithmetic degree with the archimedean Eisenstein coefficient.
- An explicit Waldspurger-type period formula relating the incoherent Eisenstein series to $L(E, s)$.

---

## Cross-Group Connections

### Group A — Iwasawa Theory
The arithmetic Siegel–Weil formula has a natural $p$-adic interpolation: one can consider $p$-adic families of special cycles and ask whether their generating series is $p$-adic analytic. This connects to **A-004 (Iwasawa Main Conjecture for Rank 1)**: the $p$-adic L-function $L_p(E, s)$ should interpolate the arithmetic intersection numbers $\widehat{\deg}(\hat{\mathcal{Z}}(m))$ at critical twists. The Kudla program over $\mathbb{Z}_p$ (rather than $\mathbb{Z}$) may provide a geometric proof of the main conjecture in rank 1.

### Group B — Euler Systems
The special cycles $\mathcal{Z}(m)$ generate classes in cohomology that form an **Euler system** in the sense of Kato. The Kolyvagin system structure implicit in the arithmetic Siegel–Weil formula connects to **B-001 (Kato's Euler System)** and **B-002 (Heegner Points)**: the Heegner point on $E$ is recovered as the image of $\mathcal{Z}(1)$ under the Jacquet–Langlands correspondence. Understanding the full generating series refines the Euler system.

### Group C — Arithmetic Statistics
The distribution of arithmetic intersection numbers $\widehat{\deg}(\hat{\mathcal{Z}}(m))$ as $E$ varies in families connects to **C-001 (Distribution of Ranks)**. The averaged arithmetic Siegel–Weil formula of Yuan–Zhang is a statistical statement about average values of $L'(E, 1)$, directly relevant to the distribution of analytic ranks in families.

### Group E — $p$-adic Methods
The $p$-adic avatars of special cycles (via $p$-adic Hodge theory and the $p$-adic Abel–Jacobi map) connect to **E-001 ($p$-adic L-functions)** and **E-003 (Iwasawa Theory via Shimura Varieties)**. The $p$-adic Siegel–Weil formula, relating $p$-adic heights of special cycles to $p$-adic L-values, is a natural extension.

### Group F — Motivic/Cohomological
The special cycles $\mathcal{Z}(m)$ define motivic cohomology classes. The motivic Siegel–Weil formula, relating these classes to motivic L-values, connects to **F-001 (Motivic L-functions)** and **F-004 (Beilinson–Bloch Conjecture)**. The arithmetic intersection number is the image under the regulator map of the motivic class.

### Group G — Deformation/Langlands
The Eisenstein series at the heart of the Kudla program are automorphic forms on $\operatorname{GL}_2$. Their $p$-adic families connect to **G-001 (Eigenvarieties)** and the $p$-adic Langlands program. The Kudla program provides a geometric construction of $p$-adic families of modular forms via intersection numbers.

### Group H — Computational
Concrete computation of $\widehat{\deg}(\hat{\mathcal{Z}}(m))$ for specific curves connects to **H-001 (Computing Selmer Groups)** and **H-003 (LMFDB Verification)**. Implementing the local intersection formulas computationally would provide new verification data for BSD.

### Group I — Connections
The Kudla program is itself a "connection" direction, linking automorphic forms (Groups G, F) to arithmetic geometry (Groups A, B, E). The arithmetic Siegel–Weil formula unifies the Gross–Zagier formula (B-002) and Kolyvagin's Euler system (B-001) under a single geometric framework.

---

## Classification

| Aspect | Assessment |
|--------|-----------|
| **Risk** | High — requires resolving the ramified local intersection theory |
| **Reward** | Very High — provides geometric proof of rank 1 BSD and framework for higher rank |
| **Timeline** | 5–10 years for full GU(1,1) ramified case |
| **Community** | Active — Kudla, Rapoport, Yang, Liu, Yuan, Zhang, Howard, Li, Brooks |
| **Independence** | Moderate — builds on established Langlands and Shimura variety technology |
| **BSD Impact** | Direct — arithmetic intersection = $L'(E,1)/\Omega_E^+$ in rank 1 |
| **Novelty** | The Kudla program provides the most geometric interpretation of BSD: the L-function value IS an intersection number. No other approach gives such a direct geometric meaning to the BSD formula. |

**Overall Assessment:** This is one of the most promising "unconventional" directions because it has already produced theorems (Gross–Zagier is a special case) and has a clear roadmap. The main obstruction — the ramified local intersection theory — is a well-posed technical problem that multiple groups are attacking. The reward is a complete geometric proof of rank 1 BSD with a natural framework for generalization to higher rank via higher-dimensional Shimura varieties and higher arithmetic Siegel–Weil formulas.
