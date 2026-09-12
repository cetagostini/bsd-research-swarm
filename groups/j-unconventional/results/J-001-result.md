# J-001: Mirror Symmetry for Elliptic Curves and L-values

**Direction ID:** J-001
**Status:** Explored — Speculative
**Classification:** Speculative/Bridge

---

## Status Assessment

**Feasibility: Very Low (near-term), Moderate (long-term as framework)**

Homological mirror symmetry (HMS) for elliptic curves is a *theorem*, not a conjecture: Polishchuk–Zaslow (2000) established the equivalence $D^b(\operatorname{Coh}(E)) \simeq D^b(\operatorname{Fuk}(\check{E}))$ for abelian varieties, and the SYZ conjecture is verified for elliptic curves (the mirror is simply the dual torus). However, the *arithmetic* content of this equivalence — specifically any connection to L-values, BSD rank, or the Tate–Shafarevich group — is entirely conjectural with no computational evidence.

The core difficulty is categorical: HMS lives over $\mathbb{C}$ (or a Novikov ring), while BSD is an arithmetic statement over $\mathbb{Q}$. Bridging this requires a $p$-adic or motivic enhancement of mirror symmetry that does not currently exist.

**Current state of knowledge:**
- HMS for elliptic curves: ✅ Proven
- Regulators detecting L-values (Beilinson conjectures): Partially proven, general framework established
- Floer-theoretic invariants → arithmetic L-values: ❌ No construction, no examples, no heuristic evidence
- Lagrangian correspondences → motivic cohomology classes: ❌ No known mechanism

---

## Testable Conjecture or Lemma

### Conjecture (Mirror-Regulator Bridge for Rank 0 and 1)

Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$ with conductor-dual $\check{E} = \operatorname{Pic}^0(E)$ (the dual abelian variety, which for elliptic curves is $E$ itself over $\mathbb{C}$). Let $\omega$ be a generator of $H^0(E, \Omega^1_E)$.

Denote by $\operatorname{Fuk}(\check{E})$ the derived Fukaya category of $\check{E}$ with the flat metric, and let $\mathcal{L}_P \in \operatorname{Ob}(\operatorname{Fuk}(\check{E}))$ be the Lagrangian torus fiber of the SYZ fibration over a point $P \in \check{E}$.

**Claim (to be tested):** There exists a class $[\mathcal{L}_P] \in K_0(D^b(\operatorname{Fuk}(\check{E})))$ such that under the Polishchuk–Zaslow equivalence $\Phi: D^b(\operatorname{Fuk}(\check{E})) \xrightarrow{\sim} D^b(\operatorname{Coh}(E))$, the pushforward $\Phi([\mathcal{L}_P])$ defines an element in $\operatorname{CH}^1(E)_{\mathbb{Q}}$ whose Beilinson regulator image in $H^1_D(E, \mathbb{Q}(1))$ has norm

$$\|\operatorname{reg}(\Phi([\mathcal{L}_P]))\|^2 \stackrel{?}{=} \frac{L'(E, 1)}{\Omega_E}$$

when $\operatorname{ord}_{s=1} L(E, s) = 1$, and similarly for higher-order vanishing via iterated extensions.

### Precise Variant (Weak Form)

**Conjecture W.** For $E/\mathbb{Q}$ with $\operatorname{rank} E(\mathbb{Q}) = r$, there exist $r$ Lagrangian submanifolds $\mathcal{L}_1, \ldots, \mathcal{L}_r$ in $\operatorname{Fuk}(\check{E})$ such that $\{\Phi([\mathcal{L}_i])\}_{i=1}^r$ are linearly independent in $K_0(D^b(\operatorname{Coh}(E))) \otimes \mathbb{Q}$ and span a subspace mapping isomorphically to the identity component of $\operatorname{CH}^1(E)_{\mathbb{Q}}$ under the Abel–Jacobi map.

This is testable: for a given $E$, compute $\Phi$ explicitly (polynomial-time for elliptic curves), enumerate Lagrangian fibers, and check whether the resulting divisor classes generate the expected subspace.

---

## Approach Summary

### Step 1: The Mirror Symmetry Setup (Established)

For an elliptic curve $E = \mathbb{C}/(\mathbb{Z} + \tau\mathbb{Z})$ with Kähler form $\omega_B = \frac{i}{2}\operatorname{Im}(\tau)|dz|^2$, the SYZ fibration is:

$$\pi: E \to S^1, \quad z \mapsto \operatorname{Re}(z)$$

The mirror $\check{E}$ is the dual torus $E^\vee = \mathbb{C}/(\mathbb{Z} + \check{\tau}\mathbb{Z})$ where $\check{\tau} = -1/\tau$ (in the simplest case; the full moduli involves the B-field). The Polishchuk–Zaslow equivalence sends:

- **Objects:** Lagrangian torus fibers $\mathcal{L}_\theta = \pi^{-1}(\theta)$ to skyscraper sheaves $\mathcal{O}_{P_\theta}$
- **Morphisms:** Floer cohomology $HF^*(\mathcal{L}_\theta, \mathcal{L}_{\theta'})$ to $\operatorname{Ext}^*(\mathcal{O}_{P_\theta}, \mathcal{O}_{P_{\theta'}})$
- **Fukaya $A_\infty$ structure:** Maps to the DG algebra structure on $\operatorname{Ext}^*$

### Step 2: The Arithmetic Hurdle (Not Yet Bridged)

The above is over $\mathbb{C}$. To reach BSD, we need:

1. **Arithmetic model:** Choose $E/\mathbb{Q}$ and a $\mathbb{Q}$-rational model of $\check{E}$. The Fukaya category must be "arithmeticized" — either via $p$-adic HMS (Kontsevich's suggestion, explored by Seidel, Abouzaid) or via integral/real structures.

2. **Regulator construction:** Given $\Phi([\mathcal{L}]) \in K_0(D^b(\operatorname{Coh}(E)))$, apply the Beilinson regulator:
$$\operatorname{reg}: K_1(E) \to H^1_D(E, \mathbb{Q}(1)) \cong \operatorname{Hom}(E(\mathbb{Q}), \mathbb{R})$$

3. **Period comparison:** Show that the period integrals $\int_{\mathcal{L}} \omega$ for Lagrangians in $\operatorname{Fuk}(\check{E})$ are related to the real period $\Omega_E = 2\int_{E(\mathbb{R})} |\omega|$ appearing in the BSD formula.

### Step 3: The Bridge (Conjectural)

The key missing ingredient is a *motivic* version of HMS:

$$\Phi_{\mathrm{mot}}: \operatorname{Mot}(\operatorname{Fuk}(\check{E})) \xrightarrow{?} \operatorname{Mot}(E)$$

mapping Floer-theoretic K-theory to motivic cohomology. This would give a direct path:

$$\text{Lagrangian } \mathcal{L} \xrightarrow{\Phi_{\mathrm{mot}}} \text{cycle } Z \in \operatorname{CH}^1(E) \xrightarrow{\text{reg}} H^1_D(E, \mathbb{Q}(1)) \xrightarrow{\text{norm}} \mathbb{R}$$

---

## Computational Example

### Example: $E = 37a1$ (rank 1 curve)

The elliptic curve $y^2 + y = x^3 - x$ (Cremona label 37a1) has:
- Analytic rank: 1
- $L'(E, 1) \approx 0.30599$
- Real period: $\Omega_E \approx 2.99385$
- Regulator: $R \approx 0.05111$
- BSD ratio: $L'(E,1)/\Omega_E \approx 0.10219 \approx R \cdot |\text{III}| / |E(\mathbb{Q})_{\text{tors}}|^2$ (with $|\text{III}| = 1$)

**What mirror symmetry gives (concretely):** For $E = \mathbb{C}/(\mathbb{Z} + \tau\mathbb{Z})$ with $\tau = \frac{1+i\sqrt{37}}{2}$, the SYZ fibers $\mathcal{L}_\theta$ for $\theta \in \mathbb{R}/\mathbb{Z}$ map to points $P_\theta \in E$. The *only* Lagrangians that can contribute to the rank are those invariant under the $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ action on the mirror — i.e., the Lagrangian must be defined over $\mathbb{Q}$.

For 37a1, the Mordell generator $P_0 = (0, 0)$ would correspond (if Conjecture W holds) to a specific Lagrangian $\mathcal{L}^* \subset \check{E}(\mathbb{C})$ whose Floer cohomology class, under $\Phi$, recovers $[P_0] \in \operatorname{CH}^1(E)$.

**Status:** No explicit $\mathcal{L}^*$ has been computed. The computational challenge is to identify which Lagrangians in $\operatorname{Fuk}(\check{E})$ are arithmetic (defined over $\mathbb{Q}$ in the appropriate sense).

### Computation: SYZ Fiber Decomposition

For $E = \mathbb{C}/\Lambda$ with $\Lambda = \mathbb{Z} + \tau\mathbb{Z}$, the Lagrangian fiber over $\theta \in S^1$ is:

$$\mathcal{L}_\theta = \{t\tau + \theta : t \in [0,1]\} \subset E$$

The Floer cohomology $HF^*(\mathcal{L}_\theta, \mathcal{L}_{\theta'})$ is 2-dimensional when $\theta \neq \theta'$ (spanned by intersection points) and the $A_\infty$ products recover the group law on $E$ under $\Phi$. This is computationally explicit and verifiable.

---

## Obstacle Analysis

### Obstacle 1: Complex vs. Arithmetic Geometry (Severity: Fundamental)

The Fukaya category is defined over $\mathbb{C}$ (or a Novikov field). BSD is a statement about $L(E/\mathbb{Q}, s)$. There is no known functor:

$$\operatorname{Fuk}(X_\mathbb{C}) \to \text{(arithmetic invariants of } X/\mathbb{Q}\text{)}$$

that respects both the $A_\infty$ structure and Galois actions. This is the central obstacle.

**Partial mitigation:** $p$-adic HMS (Kontsevich, Soibelman, Ardil-Douglas, Efimov) develops a $p$-adic Fukaya category. If established, this could interact with $p$-adic L-functions (Iwasawa theory, Group A).

### Obstacle 2: Rank ≥ 2 Requires Non-Abelian Data (Severity: High)

For rank $\geq 2$, one needs *multiple* independent Lagrangians whose Floer-theoretic products encode the group structure on $E(\mathbb{Q})$. The Fukaya category is additive, not "abelian-group-valued" in the needed sense. Extracting the Mordell–Weil group from Floer data requires a refinement of HMS that tracks integral structures, not just rational/derived equivalence.

### Obstacle 3: The Tate–Shafarevich Group (Severity: Unknown)

The BSD formula involves $|\text{III}|$, which is invisible to classical HMS (it's a purely arithmetic invariant). Any mirror symmetry approach to the *full* BSD formula (not just rank) must somehow encode $\text{III}$, which has no known complex-geometric interpretation.

### Obstacle 4: Bad Reduction (Severity: Moderate)

HMS for elliptic curves with bad reduction (non-smooth fibers) requires orbifold or singular Fukaya categories (Chen–Ruan orbifold cohomology). Most arithmetic elliptic curves have bad reduction at some primes. The framework must handle this.

---

## Cross-Group Connections

| Group | Connection | Strength |
|-------|-----------|----------|
| **A (Iwasawa Theory)** | $p$-adic HMS could connect to $p$-adic L-functions; both use $p$-adic analytic methods | Moderate |
| **B (Euler Systems)** | Lagrangian correspondences might produce Euler system classes if the motivic bridge works | Weak |
| **E (p-adic Methods)** | $p$-adic Fukaya categories (Kontsevich) directly relevant; $p$-adic regulators | Moderate |
| **F (Motivic/Cohomological)** | Core connection: regulators from $K$-theory to Deligne cohomology are the translation mechanism | Strong |
| **J-003 (Categorification)** | HMS is inherently categorical; categorification of BSD and HMS may share tools | Strong |
| **J-009 (Derived AG)** | Derived categories of coherent sheaves are one side of HMS; derived stack approaches to Selmer groups | Moderate |
| **J-011 (Higher Categories)** | Enhancing HMS to $\infty$-categories and motivic homotopy theory | Moderate |
| **J-012 (TMF)** | Topological modular forms relate to elliptic curves via chromatic homotopy; HMS has topological avatars | Weak–Moderate |
| **H (Computational)** | Explicit computation of Floer cohomology, SYZ fibers, and regulators for specific curves | Strong (for testing) |

The most promising cross-pollination is with **Group F** (motivic cohomology provides the regulator maps) and **Group J-003** (categorification of BSD naturally interacts with categorical equivalences).

---

## Classification

| Axis | Assessment |
|------|-----------|
| **Risk** | Very High — requires constructing new mathematical objects (motivic HMS bridge) that may not exist |
| **Reward** | Very High — would provide a completely new geometric construction of BSD data |
| **Near-term deliverables** | Precise conjecture statements (done above); computational tests of Conjecture W for rank 0,1 curves; literature synthesis of $p$-adic HMS |
| **Timeline** | 5–10+ years for any meaningful progress toward BSD |
| **Classification** | **Speculative/Bridge** — connects two well-developed fields (HMS and arithmetic geometry) via an unconstructed bridge |

**Honest assessment:** This direction is unlikely to contribute to BSD in the near term. Its value lies in:
1. Stating precise, testable conjectures (Conjecture W) that decompose the problem
2. Identifying exactly *where* the bridge breaks down (complex vs. arithmetic)
3. Potential for cross-pollination: ideas from HMS (stability conditions, Bridgeland stability) may inspire new approaches in motivic cohomology even without the full bridge

**Recommendation:** Catalogue as a long-term structural investigation. Invest effort only if $p$-adic HMS (Obstacle 1) sees major breakthroughs.
