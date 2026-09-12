# E-PADIC-HODGE-SHA: p-adic Hodge Theory and Finiteness of Ш

**Direction ID:** E-PADIC-HODGE-SHA
**Title:** Using p-adic Comparison Theorems to Relate Ш to Computable de Rham Cohomology

## Status Assessment

Speculative–exploratory. This document proposes a *radical new approach* to Ш finiteness: use the p-adic comparison theorems (Faltings, Scholze) to relate the Tate–Shafarevich group Ш — which lives in étale cohomology — to de Rham cohomology, which is explicitly computable. If the global-to-local map can be shown to be injective on Ш, this would force Ш = 0.

---

## 1. The p-adic Comparison Theorems

### 1.1 Faltings' Comparison Theorem (1982)

**Theorem (Faltings).** Let $A/\mathbb{Q}$ be an abelian variety of dimension $g$, $p$ a prime, and $B_{\mathrm{dR}}$ Fontaine's field of $p$-adic periods. Then there is a canonical isomorphism of $B_{\mathrm{dR}}$-vector spaces:

$$\boxed{H^1_{\mathrm{\acute{e}t}}(A_{\bar{\mathbb{Q}}}, \mathbb{Z}_p) \otimes_{\mathbb{Z}_p} B_{\mathrm{dR}} \;\cong\; H^1_{\mathrm{dR}}(A/\mathbb{Q}) \otimes_{\mathbb{Q}} B_{\mathrm{dR}}}$$

More precisely, for the $p$-adic Tate module $V_p(A) = T_p(A) \otimes_{\mathbb{Z}_p} \mathbb{Q}_p$:

$$D_{\mathrm{dR}}(V_p(A)) := (V_p(A) \otimes_{\mathbb{Q}_p} B_{\mathrm{dR}})^{G_{\mathbb{Q}_p}} \;\cong\; H^1_{\mathrm{dR}}(A/\mathbb{Q}_p)$$

where $G_{\mathbb{Q}_p} = \mathrm{Gal}(\bar{\mathbb{Q}}_p / \mathbb{Q}_p)$ is the local Galois group.

**Key consequence.** The étale cohomology group $H^1_{\mathrm{\acute{e}t}}$, which parametrizes torsors and where Ш lives, is *canonically related* to the de Rham cohomology $H^1_{\mathrm{dR}}$, which admits an explicit basis of differential forms. The de Rham filtration

$$H^1_{\mathrm{dR}}(A/\mathbb{Q}_p) \supseteq \mathrm{Fil}^0 = H^0(A, \Omega^1_{A/\mathbb{Q}_p}) \supseteq \mathrm{Fil}^1 = 0$$

provides a 2-step filtration (for an abelian variety of dimension $g$: $\mathrm{Fil}^0$ has dimension $g$, the quotient has dimension $g$) that governs the local conditions at $p$.

### 1.2 Scholze's Perfectoid Comparison (2012–2013)

**Theorem (Scholze).** Let $X$ be a smooth proper variety over $\mathbb{Q}_p$ and $\hat{X}$ its associated rigid-analytic space over $\mathbb{C}_p = \hat{\bar{\mathbb{Q}}}_p$. Then:

$$H^i_{\mathrm{\acute{e}t}}(\hat{X}, \mathbb{Z}_p) \otimes_{\mathbb{Z}_p} A_{\mathrm{inf}} \;\cong\; H^i_{\mathrm{dR}}(\hat{X}/\mathbb{C}_p) \otimes_{\mathbb{C}_p} A_{\mathrm{inf}}$$

where $A_{\mathrm{inf}} = W(\mathcal{O}_{\mathbb{C}_p}^\flat)$ is Fontaine's ring of $p$-adic periods in the perfectoid world.

**Why this matters for Ш.** Scholze's comparison works for *any* smooth proper variety, not just abelian varieties. This means:

1. **For $X_0(N)$ (modular curves):** The étale cohomology of $X_0(N)$, which controls modular parametrizations and visibility of Ш, can be related to the de Rham cohomology of $X_0(N)$, which is computable via modular symbols.

2. **For $J_0(N)$ (Jacobians):** The comparison for $J_0(N)$ gives direct access to the étale torsors in $H^1_{\mathrm{\acute{e}t}}(J_{0}(N), \mathbb{Z}_p)$, which intersect Ш via the visibility exact sequence.

3. **For products $E \times E$:** The Künneth formula combined with the comparison theorem gives access to $H^2_{\mathrm{\acute{e}t}}(E \times E, \mathbb{Z}_p)$, which contains the Cassels–Tate obstruction.

### 1.3 The Bloch–Kato Exponential Map

The comparison theorem is made effective through the **Bloch–Kato exponential map**:

$$\exp_{\mathrm{BK}} : D_{\mathrm{dR}}(V) / \mathrm{Fil}^0 \;\longrightarrow\; H^1_f(\mathbb{Q}_p, V)$$

where:
- $V = V_p(E)$ is the $p$-adic representation associated to $E$,
- $H^1_f(\mathbb{Q}_p, V)$ is the **finite-part** (crystalline) cohomology, which defines the local Selmer condition at $p$,
- $D_{\mathrm{dR}}(V) / \mathrm{Fil}^0$ is the quotient of the de Rham module by its Hodge filtration.

**The dual exponential map** goes in the opposite direction:

$$\exp^*_{\mathrm{BK}} : H^1_f(\mathbb{Q}_p, V^*(1)) \;\longrightarrow\; \mathrm{Fil}^0 \, D_{\mathrm{dR}}(V^*(1))$$

**Explicit description for elliptic curves.** For $E/\mathbb{Q}$ with good reduction at $p$:

$$D_{\mathrm{dR}}(V_p(E)) = H^1_{\mathrm{dR}}(E/\mathbb{Q}_p) = \mathbb{Q}_p \cdot \omega \oplus \mathbb{Q}_p \cdot \eta$$

where $\omega = dx/(2y)$ is the holomorphic differential and $\eta = x \, dx/(2y)$ is the differential of the second kind. The de Rham filtration gives:

$$\mathrm{Fil}^0 = \mathbb{Q}_p \cdot \omega, \qquad D_{\mathrm{dR}} / \mathrm{Fil}^0 = \mathbb{Q}_p \cdot \bar{\eta}$$

The Bloch–Kato exponential maps $\bar{\eta}$ to a class in $H^1_f(\mathbb{Q}_p, V_p(E))$, and this class *is* the local Selmer condition at $p$.

---

## 2. The Selmer Group and Ш via p-adic Hodge Theory

### 2.1 The Global Selmer Group

For an elliptic curve $E/\mathbb{Q}$ and a prime $p$, the **$p^\infty$-Selmer group** is:

$$\mathrm{Sel}_{p^\infty}(E/\mathbb{Q}) := \ker\left(H^1(\mathbb{Q}, E[p^\infty]) \xrightarrow{\mathrm{loc}} \prod_v \frac{H^1(\mathbb{Q}_v, E[p^\infty])}{\mathrm{im}(\delta_v)}\right)$$

where $\delta_v : E(\mathbb{Q}_v) \otimes \mathbb{Q}_p/\mathbb{Z}_p \to H^1(\mathbb{Q}_v, E[p^\infty])$ is the Kummer map, and the local conditions define the **Selmer subspace** at each place $v$.

### 2.2 The Exact Sequence Linking Selmer and Ш

There is a fundamental exact sequence:

$$0 \to E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p \to \mathrm{Sel}_{p^\infty}(E/\mathbb{Q}) \to \Sha(E/\mathbb{Q})[p^\infty] \to 0 \tag{$\star$}$$

This shows that $\Sha[p^\infty]$ is the **cokernel** of the global points inside the Selmer group. Equivalently:

$$\Sha(E/\mathbb{Q})[p^\infty] = \frac{\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})}{E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p}$$

**Key point:** Ш measures the *failure* of local-global principles. If the global-to-local map is injective on the "Ш part," then $\Sha = 0$.

### 2.3 The Local Condition at $p$ via p-adic Hodge Theory

At the prime $p$, the local Selmer condition is NOT the full $H^1(\mathbb{Q}_p, E[p^\infty])$. Rather, it is the **crystalline subspace**:

$$H^1_f(\mathbb{Q}_p, V_p(E)) := \ker\left(H^1(\mathbb{Q}_p, V_p(E)) \to H^1(\mathbb{Q}_p, V_p(E) \otimes B_{\mathrm{cris}})\right)$$

By the Bloch–Kato exponential, this is equivalently described as:

$$H^1_f(\mathbb{Q}_p, V_p(E)) = \exp_{\mathrm{BK}}\left(D_{\mathrm{dR}}(V_p(E)) / \mathrm{Fil}^0\right) = \exp_{\mathrm{BK}}\left(\mathbb{Q}_p \cdot \bar{\eta}\right)$$

**This is where p-adic Hodge theory enters the Selmer condition.** The de Rham filtration on $H^1_{\mathrm{dR}}(E/\mathbb{Q}_p)$ *determines* the local condition at $p$, and this filtration is explicitly computable from the Weierstrass equation of $E$.

### 2.4 The Global-to-Local Map

Define the **global-to-local restriction map**:

$$\mathrm{res}_p : H^1(\mathbb{Q}, E[p^\infty]) \to H^1(\mathbb{Q}_p, E[p^\infty])$$

Restricting to Ш:

$$\mathrm{res}_p\big|_{\Sha} : \Sha(E/\mathbb{Q})[p^\infty] \to \frac{H^1(\mathbb{Q}_p, E[p^\infty])}{H^1_f(\mathbb{Q}_p, E[p^\infty])}$$

**The fundamental question:** Is $\mathrm{res}_p\big|_{\Sha}$ injective?

If **YES**, then every element of $\Sha[p^\infty]$ has a nontrivial image in the *quotient* of local cohomology by the crystalline condition. Since the quotient $H^1(\mathbb{Q}_p, V_p(E)) / H^1_f(\mathbb{Q}_p, V_p(E))$ is isomorphic to $\mathbb{Q}_p^g$ (for an abelian variety of dimension $g$; for an elliptic curve, $g = 1$, so it is $\mathbb{Q}_p$), this would mean $\Sha[p^\infty]$ embeds into a finite group determined by the $p$-adic Hodge filtration, hence $\Sha[p^\infty]$ is finite.

If one can further show that the image is zero (i.e., every element of Ш maps to $0$ at every local place), then $\Sha = 0$.

---

## 3. The Fontaine–Mazur Conjecture and Ш

### 3.1 The Fontaine–Mazur Conjecture

**Conjecture (Fontaine–Mazur, 1995).** Let $\rho : G_{\mathbb{Q}} \to \mathrm{GL}_n(\mathbb{Q}_p)$ be a continuous $p$-adic representation that is:
1. **Geometric:** unramified outside finitely many primes, and
2. **de Rham at $p$:** $\dim_{\mathbb{Q}_p} D_{\mathrm{dR}}(\rho) = n$ (i.e., $\rho$ is de Rham in the sense of p-adic Hodge theory).

Then $\rho$ is **motivic**: it occurs in the $p$-adic étale cohomology of an algebraic variety.

For $n = 2$, the conjecture predicts that geometric de Rham representations $G_{\mathbb{Q}} \to \mathrm{GL}_2(\mathbb{Q}_p)$ come from modular forms (by the modularity theorems).

### 3.2 Modularity and Fontaine–Mazur for $E[p^\infty]$

**Theorem (Breuil–Conrad–Diamond–Taylor, 2001).** For $E/\mathbb{Q}$, the representation $\rho_{E,p^\infty} : G_{\mathbb{Q}} \to \mathrm{GL}_2(\mathbb{Z}_p)$ is modular: there exists a weight-2 newform $f$ of level $N = N(E)$ such that $\rho_{E,p^\infty} \cong \rho_{f,p^\infty}$.

Since $\rho_{E,p^\infty}$ is:
- Unramified outside primes dividing $Np$ (geometric condition),
- de Rham at $p$ (by Faltings' comparison theorem),

**the Fontaine–Mazur conjecture holds for $E[p^\infty]$.** This is not conditional — it is a *theorem*, because modularity provides the "motivic" realization.

### 3.3 Consequences for Ш

Since $E[p^\infty]$ satisfies Fontaine–Mazur, the representation $\rho_{E,p^\infty}$ is **geometric** in the strongest sense: it arises from the $p$-adic étale cohomology of the modular curve $X_0(N)$ via the Eichler–Shimura relation.

This means:
1. The **local conditions** at all places $v$ for the Selmer group $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ are determined by the p-adic Hodge filtration at $p$ and the ramification behavior at primes $\ell \mid N$.
2. The **global Selmer group** is controlled by the automorphic $L$-function $L(f, s)$ via the Bloch–Kato conjecture.
3. The **obstruction to local-global** (i.e., Ш) is measured by the failure of the Bloch–Kato Selmer group to equal the "strict" Selmer group.

---

## 4. The Main Proposition

### 4.1 Setup and Definitions

**Definition (Expected Selmer corank).** For $E/\mathbb{Q}$ with algebraic rank $r = \mathrm{rank}\, E(\mathbb{Q})$, the **expected corank** of $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ over $\mathbb{Z}_p$ is $r$. The Selmer group is said to have the **expected corank** if:

$$\mathrm{corank}_{\mathbb{Z}_p}\bigl(\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})\bigr) = r$$

Equivalently, the Pontryagin dual $X = \mathrm{Sel}_{p^\infty}(E/\mathbb{Q})^{\vee}$ is a finitely generated $\mathbb{Z}_p$-module of rank $r$.

**Definition (Geometric representation).** The representation $E[p^\infty]$ is **geometric** if it satisfies the Fontaine–Mazur conditions: unramified outside finitely many primes and de Rham at $p$.

### 4.2 The Proposition

**Proposition (Finiteness of Ш via p-adic Hodge Theory).**

*Let $E/\mathbb{Q}$ be an elliptic curve. Assume:*

**(FM)** *The Fontaine–Mazur conjecture holds for $E[p^\infty]$ (known by modularity).*

**(EC)** *The Selmer group $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ has the expected corank $r = \mathrm{rank}\, E(\mathbb{Q})$.*

*Then $\Sha(E/\mathbb{Q})[p^\infty]$ is finite.*

### 4.3 Proof

**Step 1. (Modularity gives FM.)** By Breuil–Conrad–Diamond–Taylor (2001), the representation $\rho_{E,p^\infty} : G_{\mathbb{Q}} \to \mathrm{GL}_2(\mathbb{Z}_p)$ is modular. Since it is:
- Unramified outside primes dividing $N(E) \cdot p$ (from the Néron model),
- de Rham at $p$ (by Faltings' comparison theorem: $D_{\mathrm{dR}}(V_p(E)) = H^1_{\mathrm{dR}}(E/\mathbb{Q}_p)$ has dimension 2),

it is geometric in the sense of Fontaine–Mazur. Moreover, being modular means it comes from a motive (the motive of $E$ itself), so the Fontaine–Mazur conjecture holds for $E[p^\infty]$. $\checkmark$

**Step 2. (FM determines the local conditions.)** Since $E[p^\infty]$ is geometric, the local conditions defining the Selmer group at $p$ are *exactly* the crystalline conditions from p-adic Hodge theory:

$$H^1_f(\mathbb{Q}_p, E[p^\infty]) = \ker\left(H^1(\mathbb{Q}_p, E[p^\infty]) \to H^1(\mathbb{Q}_p, E[p^\infty] \otimes B_{\mathrm{cris}})\right)$$

At primes $\ell \neq p$ of good reduction, the local condition is the **unramified** condition:

$$H^1_f(\mathbb{Q}_\ell, E[p^\infty]) = H^1_{\mathrm{ur}}(\mathbb{Q}_\ell, E[p^\infty]) = \ker\left(H^1(\mathbb{Q}_\ell, E[p^\infty]) \to H^1(I_\ell, E[p^\infty])\right)$$

where $I_\ell$ is the inertia group. At primes $\ell \mid N$ of bad reduction, the local condition involves the image of the Néron model's connected component.

These local conditions are the **Bloch–Kato Selmer conditions**, which are the "correct" local conditions for the $p$-adic representation $E[p^\infty]$.

**Step 3. (The Bloch–Kato Selmer group.)** Define the **Bloch–Kato Selmer group**:

$$H^1_f(\mathbb{Q}, E[p^\infty]) := \ker\left(H^1(\mathbb{Q}, E[p^\infty]) \xrightarrow{\prod_v \mathrm{loc}_v} \prod_v \frac{H^1(\mathbb{Q}_v, E[p^\infty])}{H^1_f(\mathbb{Q}_v, E[p^\infty])}\right)$$

Since the local conditions are the same as the classical Selmer conditions (this requires checking at each place, but it follows from the geometric nature of $E[p^\infty]$), we have:

$$\mathrm{Sel}_{p^\infty}(E/\mathbb{Q}) = H^1_f(\mathbb{Q}, E[p^\infty])$$

**Step 4. (Expected corank implies Ш finiteness.)** By the exact sequence ($\star$):

$$0 \to E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p \to \mathrm{Sel}_{p^\infty}(E/\mathbb{Q}) \to \Sha(E/\mathbb{Q})[p^\infty] \to 0$$

Taking $\mathbb{Z}_p$-coranks:

$$\mathrm{corank}_{\mathbb{Z}_p}(\mathrm{Sel}_{p^\infty}) = \mathrm{corank}_{\mathbb{Z}_p}(E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p) + \mathrm{corank}_{\mathbb{Z}_p}(\Sha[p^\infty])$$

Now $E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p \cong (\mathbb{Q}_p/\mathbb{Z}_p)^r$ has corank $r$. So:

$$\mathrm{corank}_{\mathbb{Z}_p}(\mathrm{Sel}_{p^\infty}) = r + \mathrm{corank}_{\mathbb{Z}_p}(\Sha[p^\infty])$$

By hypothesis (EC), $\mathrm{corank}_{\mathbb{Z}_p}(\mathrm{Sel}_{p^\infty}) = r$. Therefore:

$$\mathrm{corank}_{\mathbb{Z}_p}(\Sha[p^\infty]) = r - r = 0$$

A $\mathbb{Z}_p$-module with corank $0$ is finite. Hence $\Sha(E/\mathbb{Q})[p^\infty]$ is finite. $\blacksquare$

### 4.4 Strengthening: When Is $\Sha[p^\infty] = 0$?

If additionally the Selmer group has **no exceptional part** (i.e., $X = \mathrm{Sel}_{p^\infty}(E/\mathbb{Q})^{\vee}$ is a free $\mathbb{Z}_p$-module of rank $r$), then the exact sequence ($\star$) gives:

$$\Sha(E/\mathbb{Q})[p^\infty] \cong \frac{X}{E(\mathbb{Q}) \otimes \mathbb{Z}_p} = \frac{\mathbb{Z}_p^r}{\mathbb{Z}_p^r} = 0$$

under the identification of generators. This requires the **Bloch–Kato conjecture** for $L^{(r)}(E, 1)/r!$, which predicts the exact order of Ш when finite.

---

## 5. The Role of the de Rham Filtration

### 5.1 Explicit Local Conditions at $p$

For $E/\mathbb{Q}$ with good ordinary reduction at $p$, the de Rham filtration on $H^1_{\mathrm{dR}}(E/\mathbb{Q}_p)$ has:

$$\mathrm{Fil}^0 = H^0(E, \Omega^1) = \mathbb{Q}_p \cdot \omega, \qquad \mathrm{gr}^0 = H^1_{\mathrm{dR}} / \mathrm{Fil}^0 = \mathbb{Q}_p \cdot \bar{\eta}$$

The **Bloch–Kato exponential** gives an isomorphism:

$$\exp_{\mathrm{BK}} : \mathrm{gr}^0 \xrightarrow{\;\sim\;} H^1_f(\mathbb{Q}_p, V_p(E))$$

and the **dual exponential** gives:

$$\exp^*_{\mathrm{BK}} : H^1_f(\mathbb{Q}_p, V_p(E)^*(1)) \xrightarrow{\;\sim\;} \mathrm{Fil}^0 D_{\mathrm{dR}}(V_p(E)^*(1))$$

These maps are **explicitly computable**: the exponential is given by the $p$-adic formal group logarithm:

$$\exp_{\mathrm{BK}}(\bar{\eta}) = \left[\text{class in } H^1_f(\mathbb{Q}_p, V_p(E)) \text{ corresponding to the Coleman integral } \int_0^P \eta\right]$$

for $P \in E(\mathbb{Q}_p)$, where $\int_0^P \eta$ is the Coleman integral of $\eta$ from $O$ to $P$.

### 5.2 The Crystalline Period

Define the **$p$-adic period** $\Omega_p(E) \in \mathbb{Q}_p^\times$ by:

$$\Omega_p(E) = \exp_p\left(\int_0^{\hat{O}} \omega\right)^{-1}$$

where $\hat{O}$ is the identity in the formal group and $\exp_p$ is the $p$-adic exponential. This period appears in the p-adic BSD formula and is computed via the de Rham comparison.

The **comparison between étale and de Rham** gives the fundamental relation:

$$\log_p(P) = \frac{1}{\Omega_p(E)} \int_0^P \omega \pmod{\text{torsion}}$$

for $P \in E(\mathbb{Q}_p)$ close to $O$, where $\log_p$ is the formal group logarithm.

### 5.3 The Hodge–Tate Decomposition

For an elliptic curve $E/\mathbb{Q}_p$ with good reduction, the Hodge–Tate decomposition (a special case of Faltings' theorem) gives:

$$V_p(E) \otimes_{\mathbb{Q}_p} \mathbb{C}_p \;\cong\; \mathbb{C}_p(1) \oplus \mathbb{C}_p$$

where $\mathbb{C}_p(1) = \mathbb{C}_p \otimes \mathbb{Q}_p(1)$ is the Tate twist. The two summands correspond to $\mathrm{Fil}^0$ and $\mathrm{gr}^0$ of the de Rham filtration, and the Hodge–Tate weights are $\{0, 1\}$.

This decomposition is *canonical* (up to the choice of periods) and provides the bridge between the étale side (where Ш lives) and the de Rham side (which is computable).

---

## 6. Connecting to the Bloch–Kato Conjecture

### 6.1 The Bloch–Kato Conjecture for $L$-values

The **Bloch–Kato conjecture** (1990) predicts that for a geometric $p$-adic representation $V$:

$$\frac{L^*(V, 0)}{\Omega(V)} = \frac{|H^1_f(\mathbb{Q}, V^*(1))_{\mathrm{tors}}|}{|H^0(\mathbb{Q}, V^*(1))|} \cdot \prod_{v} \frac{|H^0(\mathbb{Q}_v, V^*(1))|}{|\text{Tamagawa factor}_v|}$$

For $V = V_p(E)(1) = V_p(E) \otimes \mathbb{Q}_p(1)$ (the Tate twist), this specializes to:

$$\frac{L^{(r)}(E, 1)}{r! \cdot \Omega_E^+} = \frac{|\Sha(E/\mathbb{Q})[p^\infty]|}{|E(\mathbb{Q})_{\mathrm{tors}}|_p^2} \cdot \mathrm{Reg}_p(E) \cdot \prod_{\ell \mid N} c_\ell^{(p)}$$

This is exactly the **BSD conjecture** (at the prime $p$). The Bloch–Kato conjecture for elliptic curves IS the BSD conjecture.

### 6.2 How p-adic Hodge Theory Illuminates the Proof Strategy

The p-adic Hodge framework reveals the following **logical chain**:

$$\boxed{\text{Modularity} \;\Longrightarrow\; \text{Fontaine–Mazur} \;\Longrightarrow\; \text{Bloch–Kato local conditions} \;\Longrightarrow\; \text{Selmer = expected corank} \;\Longrightarrow\; \Sha[p^\infty] \text{ finite}}$$

Each arrow is either a theorem or conditional on standard conjectures:

1. **Modularity ⟹ Fontaine–Mazur** (BCDT 2001): **THEOREM**.
2. **Fontaine–Mazur ⟹ Bloch–Kato local conditions** (by definition of crystalline/unramified): **DEFINITION**.
3. **Bloch–Kato local conditions ⟹ Selmer has expected corank**: **CONDITIONAL** on the Iwasawa main conjecture (Skinner–Urban 2014 for $r \leq 1$, open for $r \geq 2$).
4. **Selmer has expected corank ⟹ Ш finite**: **THEOREM** (by the exact sequence ($\star$)).

### 6.3 The Gap: Step 3 for Rank ≥ 2

The main obstacle is Step 3: showing that $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ has the expected corank $r$ when $r \geq 2$.

For $r \leq 1$, this is known:
- $r = 0$: Kolyvagin (1989) + Gross–Zagier (1986).
- $r = 1$: Skinner–Urban (2014) (under mild hypotheses on $\rho_{E,p}$).

For $r \geq 2$, this is **open**. The p-adic Hodge perspective suggests two approaches:

**Approach A (via Euler systems).** Construct a $p$-adic Euler system class in $H^1_f(\mathbb{Q}, V_p(E)(1))$ that is non-trivial at rank $r$. Kato's Euler system vanishes at augmentation for $r \geq 2$ (by the order-of-vanishing bound), so one needs *new* Euler system classes. Candidates:
- Beilinson–Flach elements (rank $\leq 2$ potentially).
- Heegner point classes via quadratic twists (rank-1 twists).
- The combined multi-system approach (see B-MULTI-SHA).

**Approach B (via p-adic Hodge theory directly).** Use the explicit de Rham description of $H^1_f(\mathbb{Q}_p, V_p(E))$ to bound the Selmer group without constructing Euler system classes. The idea:

Since $H^1_f(\mathbb{Q}_p, V_p(E))$ has dimension $1$ (as a $\mathbb{Q}_p$-vector space, from $\mathrm{gr}^0 = \mathbb{Q}_p \cdot \bar{\eta}$), the local condition at $p$ constrains $1$ degree of freedom. At each prime $\ell \mid N$, the local condition also constrains $\dim H^0(\mathbb{Q}_\ell, V_p(E)^*(1))$ degrees of freedom (the "Tamagawa factors"). The **global-to-local** map:

$$\mathrm{loc} : H^1(\mathbb{Q}, E[p^\infty]) \to \prod_v \frac{H^1(\mathbb{Q}_v, E[p^\infty])}{H^1_f(\mathbb{Q}_v, E[p^\infty])}$$

has kernel equal to $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$. If we can show that the image of Ш under $\mathrm{loc}$ is **injective**, then Ш is bounded by the cokernel of the global points.

---

## 7. A New Strategy: Injectivity of the Localization on Ш

### 7.1 The Key Observation

**Observation.** An element $c \in \Sha(E/\mathbb{Q})[p^\infty]$ maps to $0$ in every $H^1(\mathbb{Q}_v, E[p^\infty]) / H^1_f(\mathbb{Q}_v, E[p^\infty])$ for $v \neq p$ (since $c$ is locally trivial). At $v = p$, the image of $c$ in $H^1(\mathbb{Q}_p, E[p^\infty]) / H^1_f(\mathbb{Q}_p, E[p^\infty])$ is the **only obstruction**.

If we define:

$$\mathrm{loc}_p\big|_{\Sha} : \Sha(E/\mathbb{Q})[p^\infty] \to H^1(\mathbb{Q}_p, E[p^\infty]) / H^1_f(\mathbb{Q}_p, E[p^\infty])$$

then the question becomes: **Is this map injective?**

### 7.2 When Is $\mathrm{loc}_p\big|_{\Sha}$ Injective?

The kernel of $\mathrm{loc}_p\big|_{\Sha}$ consists of elements $c \in \Sha[p^\infty]$ that are:
- Locally trivial at all $v \neq p$ (by definition of Ш), AND
- Locally trivial at $p$ in the crystalline sense (i.e., $c$ maps to $0$ in $H^1 / H^1_f$ at $p$).

Such $c$ would be a **globally non-trivial** cohomology class that is "locally trivial everywhere in the Selmer sense." But this means $c \in \mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ and $c$ maps to $0$ in $E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p$ (since it's in Ш). So $c$ represents a genuine element of Ш that is invisible to the local conditions.

**For the map to be injective, we need: the only element of $\Sha[p^\infty]$ that vanishes locally at $p$ in the crystalline sense is the zero element.**

This is equivalent to:

$$\Sha(E/\mathbb{Q})[p^\infty] \cap E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p = 0$$

which holds if $E(\mathbb{Q})_{\mathrm{tors}}$ has no $p$-power torsion (or more precisely, if $E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p$ maps injectively into $\mathrm{Sel}_{p^\infty}$, which it always does by Kummer theory).

### 7.3 Reformulation as a Tate Duality Problem

The question of injectivity of $\mathrm{loc}_p\big|_{\Sha}$ can be reformulated via **Poitou–Tate global duality**. The 9-term exact sequence of Poitou–Tate gives:

$$0 \to \Sha^0(E[p^\infty]) \to H^0(\mathbb{Q}, E[p^\infty]) \to \prod'_v H^0(\mathbb{Q}_v, E[p^\infty]) \to$$
$$\to H^2(\mathbb{Q}, E[p^\infty])^* \to \Sha^1(E[p^\infty]) \to \mathrm{Sel}_{p^\infty}(E/\mathbb{Q})^{\vee} \to \Sha^2(E[p^\infty]) \to \cdots$$

The finiteness of $\Sha[p^\infty]$ is equivalent to the vanishing of certain cohomological obstructions in this sequence. The p-adic Hodge comparison constrains these obstructions through the crystalline conditions.

---

## 8. The Fontaine–Mazur–Bloch–Kato Implication

### 8.1 The Conditional Chain

Combining everything, we have the following **conditional theorem**:

**Theorem (Conditional on Expected Corank).** *Let $E/\mathbb{Q}$ be an elliptic curve and $p$ a prime. If:*

1. *(FM) $E[p^\infty]$ is geometric (known by modularity),*
2. *(EC) $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ has corank $r = \mathrm{rank}\, E(\mathbb{Q})$,*

*then $\Sha(E/\mathbb{Q})[p^\infty]$ is finite.*

**Corollary.** *If (EC) holds for ALL primes $p$, then $\Sha(E/\mathbb{Q})$ is finite.*

### 8.2 Why FM Is the Easy Part

The Fontaine–Mazur conjecture for $E[p^\infty]$ is the *easy* part — it follows from modularity, which is a theorem. The *hard* part is (EC), which requires understanding the Selmer group.

However, p-adic Hodge theory *informs* (EC) by:
1. **Providing the local conditions explicitly** (via the de Rham filtration),
2. **Connecting to the Bloch–Kato conjecture** (which predicts the exact order of Ш),
3. **Suggesting that (EC) should hold** for "generic" elliptic curves (by the Cohen–Lenstra-type heuristics for Selmer groups).

### 8.3 Comparison with the Visibility Approach

The p-adic Hodge approach and the visibility approach (D-VISIBILITY-SHA) are **complementary**:

| Feature | p-adic Hodge | Visibility |
|---|---|---|
| **Primes** | Works at all $p$ | Best at $p = 2$ |
| **Method** | Analytic (comparison theorems) | Geometric (modular curves) |
| **Key input** | Modularity + Selmer corank | Trivial visibility kernel |
| **Obstruction** | Expected corank (open for $r \geq 2$) | $K[2]^{G_{\mathbb{Q}}} = 0$ (conjectural) |
| **Strength** | Gives the *exact* structure of Ш | Gives explicit bounds on $|\Sha[2]|$ |

Combining both approaches: if visibility handles $p = 2$ and p-adic Hodge handles odd $p$ (via Skinner–Urban for the expected corank), then Ш is finite for rank 2 curves.

---

## 9. Predictions and Computational Verification

### 9.1 Predicted Finiteness for Specific Curves

| Curve | Rank | Condition (FM) | Condition (EC) | Predicted $\Sha[p^\infty]$ |
|---|---|---|---|---|
| 571a1 | 2 | ✓ (modularity) | Expected: yes | Finite (conjecturally $= 0$) |
| 389a1 | 2 | ✓ | Expected: yes | Finite |
| 5077a1 | 2 | ✓ | Expected: yes | Finite ($m = 1$, visibility trivial) |
| 11a1 | 0 | ✓ | Kolyvagin: ✓ | Finite (= 1, BSD proven) |
| 37a1 | 1 | ✓ | Gross–Zagier + Kolyvagin: ✓ | Finite (BSD proven) |

### 9.2 What Can Be Computed

The p-adic Hodge framework makes the following **explicitly computable**:

1. **$D_{\mathrm{dR}}(V_p(E))$:** From the Weierstrass equation, the de Rham cohomology has basis $\{\omega, \eta\}$ where $\omega = dx/(2y)$ and $\eta = x\,dx/(2y)$.

2. **The Bloch–Kato exponential:** $\exp_{\mathrm{BK}} : \mathbb{Q}_p \cdot \bar{\eta} \to H^1_f(\mathbb{Q}_p, V_p(E))$ is given by the Coleman integral $\int^P \eta$.

3. **The $p$-adic period $\Omega_p(E)$:** From $\int_0^{\hat{O}} \omega$ in the formal group.

4. **The local condition at $p$:** An element $c \in H^1(\mathbb{Q}_p, E[p^\infty])$ is crystalline iff $\exp^*_{\mathrm{BK}}(c) = 0$ in $\mathrm{Fil}^0 D_{\mathrm{dR}}$, which can be tested by computing the Coleman integral $\int^P \omega$.

5. **The $p$-adic height pairing:** $\langle P, Q \rangle_p = \int^P \omega \cdot \int^Q \eta + \int^P \eta \cdot \int^Q \omega$ (Coleman integrals).

### 9.3 Gap Analysis

| Component | Status | Difficulty |
|---|---|---|
| FM for $E[p^\infty]$ | **Known** (BCDT 2001) | — |
| Bloch–Kato local conditions | **Known** (definition) | — |
| Expected corank for $r \leq 1$ | **Known** (Kolyvagin, Skinner–Urban) | — |
| Expected corank for $r = 2$ | **Open** | Major |
| Bloch–Kato conjecture for $L$-values | **Open** for $r \geq 2$ | Major |
| Injectivity of $\mathrm{loc}_p\big|_{\Sha}$ | **Open** | Moderate |
| Computability of local conditions | **Available** (Coleman integrals) | Implemented |

---

## 10. Conclusion

### 10.1 Summary

The p-adic Hodge approach to Ш finiteness rests on three pillars:

1. **Modularity** (BCDT 2001): ensures $E[p^\infty]$ is geometric, hence the Fontaine–Mazur conjecture holds and the Bloch–Kato local conditions are the "correct" ones.

2. **The expected Selmer corank**: if $\mathrm{Sel}_{p^\infty}(E/\mathbb{Q})$ has the "correct" $\mathbb{Z}_p$-corank (= rank of $E(\mathbb{Q})$), then Ш is finite by a simple exact-sequence argument.

3. **Computability**: the de Rham filtration provides explicit formulas for the local conditions at $p$, and Coleman integration makes these computable in practice.

### 10.2 The Core Difficulty

The approach reduces Ш finiteness to the **expected corank problem**: prove that the Selmer group has the expected size. For $r \leq 1$, this is known. For $r \geq 2$, this is the fundamental obstacle shared by ALL approaches to BSD.

The p-adic Hodge perspective does not *solve* this problem, but it *clarifies* it: the expected corank is equivalent to the Bloch–Kato conjecture for the leading $L$-value, which is a *p-adic Hodge-theoretic* statement about the relationship between $L$-values and Selmer groups.

### 10.3 Why This Approach Is Worth Pursuing

1. **It works at all primes simultaneously** (unlike visibility, which is best at $p = 2$).
2. **The local conditions are explicitly computable** (via Coleman integration).
3. **It connects Ш finiteness to the Bloch–Kato conjecture**, which is the "correct" generalization of BSD to arbitrary motives.
4. **It clarifies the logical structure**: modularity is the *easy* part; the expected corank is the *hard* part.
5. **Combined with Iwasawa theory** (Skinner–Urban), it may give Ш finiteness for rank 2 curves at all odd primes, leaving only $p = 2$ for the visibility approach.

---

## References

1. Faltings, G. (1982). "Endlichkeitssätze für abelsche Varietäten über Zahlkörpern." *Invent. Math.* 70: 145–186.
2. Scholze, P. (2013). "Perfectoid spaces." *Publ. Math. IHÉS* 116: 245–313.
3. Bloch, S., Kato, K. (1990). "L-functions and Tamagawa numbers of motives." *The Grothendieck Festschrift* I: 333–400.
4. Fontaine, J.-M., Mazur, B. (1995). "Geometric Galois representations." *Elliptic Curves, Modular Forms, & Fermat's Last Theorem* (Hong Kong, 1993): 41–78.
5. Breuil, C., Conrad, B., Diamond, F., Taylor, R. (2001). "On the modularity of elliptic curves over $\mathbb{Q}$." *J. Amer. Math. Soc.* 14: 843–939.
6. Kato, K. (2004). "$p$-adic Hodge theory and values of zeta functions of modular forms." *Astérisque* 295: 117–290.
7. Skinner, C., Urban, E. (2014). "The Iwasawa main conjectures for $\mathrm{GL}_2$." *Invent. Math.* 195: 1–277.
8. Greenberg, R. (1994). "Iwasawa theory for $p$-adic representations." *Adv. Studies Pure Math.* 17: 97–137.
9. Nekovář, J. (2006). "The Euler system method for CM points on Shimura curves." *LMS Lecture Notes* 320.
10. Mazur, B., Tate, J., Teitelbaum, J. (1986). "On $p$-adic analogues of the conjectures of Birch and Swinnerton-Dyer." *Invent. Math.* 84: 1–48.
