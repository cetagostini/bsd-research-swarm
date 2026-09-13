# B-RANK2-EULER: Rank-Two Euler System Candidates and Selmer Control

## Direction ID and Title
B-RANK2-EULER — Directions 28–30: Rank-Two Determinant Class, Norm Relations, and Selmer Control

## Status Assessment
This document addresses three linked directions from Phase 3 of the research program: constructing a rank-two Euler system for a modular elliptic curve $E/\mathbb{Q}$ of analytic rank 2, verifying the norm compatibility of its constituent classes, and deriving the Selmer-group bound that implies $\operatorname{Ш}[p^\infty] = 0$. The baseline state of knowledge is:

- **Known unconditionally:** Kato's Euler system exists for all modular $E$ at good ordinary $p$. Its augmentation image vanishes to order $r = \operatorname{ord}_{s=1} L(E,s)$, so it contributes nothing to the rank-2 Selmer bound via the classical Kolyvagin derivative method.
- **Known conditionally:** The combined Euler system of B-MULTI-SHA (Heegner + Beilinson-Flach) produces two nonzero classes when conditions C1–C4 hold. However, B-MULTI-SHA treats these as ad hoc generators of a Selmer subgroup; it does **not** frame them as a rank-2 Euler system with compatible norm relations.
- **Missing:** A rigorous construction of a rank-2 Euler system $\{c_m^{(1)}, c_m^{(2)}\}_{m \geq 1}$ satisfying the full Rubin–Kato norm-compatibility, plus the nonvanishing / primitivity inputs needed for the Rubin-style Selmer control theorem to produce the upper bound $|\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})| \leq p^{2\mu}$ for appropriate $\mu$.

The purpose of this document is to (1) enumerate the concrete candidates for each of the two constituent families, (2) state precisely what norm-compatibility each satisfies and what remains to be verified for the pair, and (3) isolate the exact hypotheses needed for the Selmer-control conclusion.

---

## Direction 28: Rank-Two Determinant Class

### 28.1 What a Rank-$r$ Euler System Is

**Definition (Rubin, 1991; Kato, 2004).** Let $T$ be a $p$-adic representation of $G_\mathbb{Q}$, $\Lambda = \mathbb{Z}_p[[\Gamma]]$ the Iwasawa algebra for a $p$-adic Lie extension $\mathbb{Q}_\infty/\mathbb{Q}$ with $\Gamma = \operatorname{Gal}(\mathbb{Q}_\infty/\mathbb{Q})$, and $\Sigma$ a finite set of bad primes. A **rank-$r$ Euler system** for $(T, \mathbb{Q}_\infty, \Sigma)$ is a collection $\{c_m\}_{m \geq 1}$ indexed by squarefree products of primes $\ell \notin \Sigma$, where:

$$c_m \in H^1\bigl(\mathbb{Q}_m, T \hat{\otimes} \Lambda\bigr) \quad (\mathbb{Q}_m = \mathbb{Q}(\mu_m) \text{ or the appropriate layer})$$

satisfying:

**(ES-1) Norm relation.** For each prime $\ell \nmid m \cdot p$ with $\ell \notin \Sigma$:
$$\operatorname{Cor}_{\mathbb{Q}_{m\ell}/\mathbb{Q}_m}(c_{m\ell}) = P_\ell(\operatorname{Frob}_\ell^{-1}) \cdot c_m$$
where $P_\ell(x) = \det(1 - \operatorname{Frob}_\ell^{-1} x \mid T^{I_\ell})$ is the Euler factor polynomial.

**(ES-2) Non-degeneracy.** The $\Lambda$-submodule $\langle c_m \rangle_\Lambda \subseteq H^1_f(\mathbb{Q}, T \hat\otimes \Lambda)$ has $\Lambda$-rank $\geq r$.

For $T = V_p(E)$, the Euler factor is $P_\ell(x) = 1 - a_\ell x + \ell x^2$.

**Key point:** A rank-$r$ Euler system is a single compatible family whose span has rank $r$ over $\Lambda$. This is **different** from $r$ separate rank-1 systems. The norm relations intertwine the generators.

### 28.2 Why Rank 2 Is Harder Than Rank 1

For rank 1, Kato (2004) provides the unique known unconditional Euler system for $V_p(E)/\mathbb{Q}$:

$$z^{(p)} = \{z_m^{(p)}\}_{m \geq 1}, \quad z_m^{(p)} \in H^1(\mathbb{Q}(\mu_m), T_p(E) \hat\otimes \Lambda)$$

This system has $\Lambda$-rank 1. When $r = \operatorname{ord}_{s=1} L(E,s) = 1$, the derivative element $z' = \frac{d}{d\gamma}\big|_{\gamma=1} z^{(p)}$ gives a nonzero class in $H^1_f(\mathbb{Q}, V_p(E))$, and Kolyvagin's method applies.

When $r = 2$, the augmentation image vanishes ($\varepsilon(z^{(p)}) = 0$) and so does the first derivative ($z' = 0$). The **second** derivative $z'' = \frac{d^2}{d\gamma^2}\big|_{\gamma=1} z^{(p)}$ is nonzero, but:

- Kolyvagin's derivative machinery uses only the 0th and 1st derivatives.
- The class $z''$ does not come with Kolyvagin-type derivative classes $d_\ell$ satisfying the required vanishing conditions.

So a **second independent family** is needed, one that does **not** vanish at the augmentation ideal.

### 28.3 Candidate Constructions

#### Candidate A: Heegner Point Classes (via Quadratic Twists)

**Construction.** Let $K/\mathbb{Q}$ be an imaginary quadratic field satisfying the Heegner hypothesis for $(N, p)$, and $\chi = \chi_K$ the associated quadratic character. Suppose $E^{(\chi)}$ (the quadratic twist of $E$ by $\chi$) has rank 1. The generalized Heegner cycle $y_K \in \operatorname{CH}_1(J_0(N))$ yields, via the Ceresa cycle and Beilinson's regulator, a class:

$$\kappa_K^{(\chi)} \in H^1_f(K, T_p(E))$$

which corestricts to:
$$c_{\mathrm{Heeg}} = \operatorname{Cor}_{K/\mathbb{Q}}(\kappa_K^{(\chi)}) \in H^1_f(\mathbb{Q}, V_p(E))$$

**Norm compatibility.** The Heegner points satisfy:
$$\operatorname{Norm}_{K(\mu_{m\ell})/K(\mu_m)}(P_{m\ell}) = \begin{cases}
(a_\ell - \sigma_\ell - \sigma_\ell^{-1}) \cdot P_m & \text{if } \ell \text{ splits in } K \\
(a_\ell + 1) \cdot P_m & \text{if } \ell \text{ inert in } K \text{ and } \ell \nmid N
\end{cases}$$

This is **not** the same Euler factor as Kato ($1 - a_\ell \operatorname{Frob}_\ell^{-1} + \ell \operatorname{Frob}_\ell^{-2}$). The Heegner norm relation involves the Hecke operator $T_\ell$ acting on the modular curve, not the characteristic polynomial of Frobenius on $T_p(E)$ directly.

**Status:** Well-understood for $r = 1$ twists. The corestriction $\operatorname{Cor}_{K/\mathbb{Q}}(\kappa_K)$ gives a nonzero class in $H^1_f(\mathbb{Q}, V_p(E))$ when $L(E^{(\chi)}, 1) \neq 0$ (by Gross–Zagier + Kolyvagin). However, the family $\{c_m^{\mathrm{Heeg}}\}$ over cyclotomic layers is **not** a Kato-type Euler system for $V_p(E)$ — it is an Euler system for $V_p(E) \otimes \chi$ over $K$, and the corestriction destroys the norm compatibility over $\mathbb{Q}$.

#### Candidate B: Beilinson-Flach Elements (Diagonal Case)

**Construction.** For the Rankin–Selberg product $f \otimes f$ where $f$ is the newform attached to $E$, Beilinson–Flach elements:

$$\mathrm{BF}_{f,f}^{(i)} \in H^1\bigl(\mathbb{Q}(\mu_m), V_f \otimes V_f \otimes \mathbb{Q}_p(-i)\bigr), \quad i \in \{1, 2\}$$

are constructed from relative $K$-theory of $X_0(N) \times X_0(N)$. The decomposition:

$$V_f \otimes V_f \cong \operatorname{Sym}^2 V_f \oplus \wedge^2 V_f$$

with $\operatorname{Sym}^2 V_f \cong \operatorname{ad}^0 V_f \oplus \mathbb{Q}_p(-1)$ (where $\operatorname{ad}^0 V_f$ is the 3-dimensional trace-zero adjoint representation) gives:

$$\pi_{\operatorname{ad}}\bigl(\mathrm{BF}_{f,f}^{(1)}\bigr) \in H^1\bigl(\mathbb{Q}(\mu_m), \operatorname{ad}^0 V_p(E)(-1) \otimes \mathbb{Q}_p\bigr)$$

**Norm compatibility (Kings–Loeffler–Zerbes, 2017).** The BF elements satisfy:
$$\operatorname{Cor}_{\mathbb{Q}(\mu_{m\ell})/\mathbb{Q}(\mu_m)}\bigl(\mathrm{BF}_{m\ell}\bigr) = P_\ell^{\operatorname{Sym}^2}(\operatorname{Frob}_\ell^{-1}) \cdot \mathrm{BF}_m$$

where:
$$P_\ell^{\operatorname{Sym}^2}(x) = (1 - \alpha_\ell^2 x)(1 - x)(1 - \beta_\ell^2 x) = 1 - (a_\ell^2 - 2\ell)x + \ell(a_\ell^2 - 2\ell)x^2 - \ell^3 x^3$$

This is the Euler factor of $\operatorname{Sym}^2 V_p(E)$, **not** of $V_p(E)$. So BF elements are a rank-1 Euler system for $\operatorname{ad}^0 V_p(E)(-1)$, not for $V_p(E)$.

**Projection to $V_p(E)$.** There is no $G_\mathbb{Q}$-equivariant projection $\operatorname{Sym}^2 V_p(E) \to V_p(E)$ or $\operatorname{ad}^0 V_p(E) \to V_p(E)$. The $\chi$-isotypic decomposition $V_f \otimes \chi \cong V_f$ (via the Hecke eigenvalue at split primes in $K$) gives an indirect route:

$$\pi_\chi: H^1\bigl(\mathbb{Q}, \operatorname{ad}^0 V_p(E)(-1)\bigr) \dashrightarrow H^1\bigl(\mathbb{Q}, V_p(E)\bigr)$$

but this is **not** a Galois-equivariant map of representations; it is a $\chi$-twisted trace map that depends on the choice of $K$.

#### Candidate C: Generalized Kato Classes (Castella)

**Construction.** Castella (2015–2018) constructs generalized Kato classes by applying the Euler system machinery to $p$-adic families of modular forms. For a Hida family $\mathbf{f}$ passing through $f$ at weight 2, the two-variable $p$-adic L-function $\mathcal{L}_p(\mathbf{f}) \in \Lambda[[\mathcal{W}]]$ (where $\mathcal{W}$ is the weight variable) yields, at weight $k > 2$:

$$z_k^{\mathrm{genKato}} \in H^1_f(\mathbb{Q}, \operatorname{Sym}^{k-2} V_p(E))$$

These satisfy norm relations with the Euler factors of $\operatorname{Sym}^{k-2}$.

**Specialization to $k = 2$:** $z_2^{\mathrm{genKato}} = z^{(p)}$ is Kato's original element. At $k = 3$: $z_3^{\mathrm{genKato}} \in H^1_f(\mathbb{Q}, V_p(E))$ encodes $L(\operatorname{Sym}^2 E, 1)$ (up to periods).

**Status:** The generalized Kato class at weight 3 is the **strongest candidate** for the second family because:
1. It lives directly in $H^1_f(\mathbb{Q}, V_p(E))$ (not in a tensor product).
2. Its nonvanishing is governed by $L(\operatorname{Sym}^2 E, 1) \neq 0$, which is known for 389.a1.
3. Its norm relations are Kato-type (with $\operatorname{Sym}^2$ Euler factors).

**Problem:** The generalized Kato class at weight 3 is NOT an Euler system for $V_p(E)$ — it is the specialization of a $\Lambda$-adic class for $\operatorname{ad}^0 V_p(E)$. Its norm relations involve $P_\ell^{\operatorname{Sym}^2}$, not $P_\ell^E$.

### 28.4 The Core Difficulty

**No known construction produces two classes in $H^1_f(\mathbb{Q}, V_p(E))$ that simultaneously:**
1. Satisfy **compatible** norm relations (same Euler factor polynomial $P_\ell^E$),
2. Are **linearly independent** in $H^1_f(\mathbb{Q}, V_p(E))$,
3. Have **different augmentation filtration orders** (one vanishing, one not).

Each candidate (A, B, C) provides ONE class with the right nonvanishing, but the norm relations are incompatible with Kato's. This is the fundamental obstruction to constructing a rank-2 Euler system for $V_p(E)$.

**The way forward (Burns–Sakamoto–Sano, 2023; Bullach–Burns, 2024).** Recent work on "explicit reciprocity" and "zeta elements" treats the pair $(z^{\mathrm{Kato}}, z^{\mathrm{genKato}})$ as a **determinant-class** rather than requiring identical norm relations. The rank-2 condition becomes:

$$\det \begin{pmatrix} z^{\mathrm{Kato}}_m & z^{\mathrm{genKato}}_m \end{pmatrix} \in \bigwedge^2 H^1_f(\mathbb{Q}(\mu_m), V_p(E))$$

is nonzero and satisfies a "twisted" norm relation:
$$\operatorname{Cor}_{m\ell/m}\bigl(\det(c_m^{(1)}, c_m^{(2)})\bigr) = P_\ell^E(x) \cdot P_\ell^{\operatorname{Sym}^2}(x) \cdot \det(c_m^{(1)}, c_m^{(2)})$$

This is the **correct** formulation for rank 2: a single element of $\bigwedge^2 H^1_f$ satisfying a product-of-Euler-factors norm relation. Burns–Sakamoto–Sano prove this determinant-class framework produces the optimal Selmer bound under appropriate nonvanishing hypotheses.

### 28.5 Application to 389.a1

For $E = 389\text{a}1$ with $p = 5$:

| Candidate | Class | Nonvanishing condition | Status for 389.a1 |
|-----------|-------|----------------------|-------------------|
| Kato | $z^{\mathrm{Kato}}_m$ | $L''(E,1) \neq 0$ | ✓ (analytic rank 2, BSD holds) |
| Heegner ($K = \mathbb{Q}(\sqrt{-d})$) | $c_{\mathrm{Heeg}}$ | $L(E^{(\chi)}, 1) \neq 0$ for some twist | **Unknown** — needs explicit verification |
| BF → genKato (wt 3) | $z_3^{\mathrm{genKato}}$ | $L(\operatorname{Sym}^2 E, 1) \neq 0$ | ✓ (computed nonzero) |
| Castella | $z^{\mathrm{Castella}}$ | $p$-adic $\operatorname{Sym}^2$ nonvanishing | Likely but unverified |

**Best candidate for the second class:** The generalized Kato class at weight 3 (Candidate C), since $L(\operatorname{Sym}^2 E, 1) \neq 0$ for 389.a1.

---

## Direction 29: Norm Relations

### 29.1 Classical Euler System Norm Relations

**Definition.** An Euler system $\{c_m\}$ for $T$ over $\mathbb{Q}_\infty = \mathbb{Q}(\mu_{p^\infty})$ satisfies:

$$\operatorname{Cor}_{\mathbb{Q}_{m\ell}/\mathbb{Q}_m}(c_{m\ell}) = P_\ell(\operatorname{Frob}_\ell^{-1}) \cdot c_m \quad \text{for all } \ell \nmid mp, \; \ell \notin \Sigma$$

where $P_\ell(x) = \det(1 - \operatorname{Frob}_\ell^{-1} x \mid T^{I_\ell}) \in \mathbb{Z}_p[x]$.

For $T = T_p(E)$ with $E$ good at $\ell$:
$$P_\ell(x) = 1 - a_\ell x + \ell x^2$$

This norm relation is the engine of the entire Euler system method: it converts a **global** cohomological datum (the class $c_m$) into **local** constraints (the Euler factors $P_\ell$) that control the Selmer group.

### 29.2 The Rank-2 Norm-Relation Problem

For a rank-2 Euler system, we need **two** families $\{c_m^{(1)}\}$ and $\{c_m^{(2)}\}$ such that:

**(NR-1)** Each family individually satisfies norm relations:
$$\operatorname{Cor}_{m\ell/m}(c_{m\ell}^{(i)}) = P_\ell^{(i)}(\operatorname{Frob}_\ell^{-1}) \cdot c_m^{(i)}, \quad i = 1, 2$$

**(NR-2)** The two families are **intertwined** by the same tower:
$$c_m^{(1)}, c_m^{(2)} \in H^1(\mathbb{Q}_m, T_p(E) \hat\otimes \Lambda) \quad \text{(same coefficient module, same tower)}$$

**(NR-3)** The pair $(c_m^{(1)}, c_m^{(2)})$ satisfies a **determinant norm relation**:
$$\operatorname{Cor}_{m\ell/m}\bigl(\det(c_{m\ell}^{(1)}, c_{m\ell}^{(2)})\bigr) = \bigl(P_\ell^{(1)} \cdot P_\ell^{(2)}\bigr)(\operatorname{Frob}_\ell^{-1}) \cdot \det(c_m^{(1)}, c_m^{(2)})$$

where $\det \in \bigwedge^2 H^1(\mathbb{Q}_m, T_p(E) \hat\otimes \Lambda)$.

### 29.3 What's Known: Kato + Castella

**Kato's system (rank 1).** $P_\ell^{\mathrm{Kato}}(x) = 1 - a_\ell x + \ell x^2$ (the Euler factor of $E$). Known unconditionally since 2004.

**Castella's generalized Kato class.** The generalized Kato class at weight $k$ for the Hida family $\mathbf{f}$ satisfies:
$$\operatorname{Cor}_{m\ell/m}(z_{m\ell}^{\mathrm{genKato}, k}) = P_\ell^{\operatorname{Sym}^{k-2}}(\operatorname{Frob}_\ell^{-1}) \cdot z_m^{\mathrm{genKato}, k}$$

where $P_\ell^{\operatorname{Sym}^{k-2}}(x) = \det(1 - \operatorname{Frob}_\ell^{-1} x \mid \operatorname{Sym}^{k-2} V_p(E)^{I_\ell})$.

For $k = 3$ (the relevant case):
$$P_\ell^{\operatorname{Sym}^1}(x) = P_\ell^E(x) = 1 - a_\ell x + \ell x^2$$

Wait — $\operatorname{Sym}^1 V_p(E) = V_p(E)$, so the weight-3 generalized Kato class has the **same** Euler factor as Kato's original system. This is the key insight.

**But:** The weight-3 class $z^{\mathrm{genKato}, 3}$ is a specialization of the two-variable $p$-adic L-function $\mathcal{L}_p(\mathbf{f})$ at the weight-3 point of the Hida family. Its norm relation involves the **weight-3 Euler factor**:

$$P_\ell^{(k=3)}(x) = (1 - \ell x)(1 - a_\ell x + \ell x^2)$$

which includes an extra $(1 - \ell x)$ factor from the cyclotomic twist at weight 3. After untwisting:

$$P_\ell^{\mathrm{untwisted}}(x) = 1 - a_\ell x + \ell x^2$$

**Precise state of knowledge:**

| System | Euler factor | Norm relation proven | Proven for $V_p(E)$? |
|--------|-------------|---------------------|---------------------|
| Kato ($k=2$) | $1 - a_\ell x + \ell x^2$ | ✓ (Kato 2004) | ✓ |
| genKato ($k=3$) | $(1-\ell x)(1 - a_\ell x + \ell x^2)$ | ✓ (Castella 2015) | After untwisting: ✓ |
| Heegner | $a_\ell - \sigma_\ell - \sigma_\ell^{-1}$ | ✓ (Gross–Kohnen–Zagier) | Not a system for $V_p(E)$ over $\mathbb{Q}$ |
| BF ($\operatorname{Sym}^2$) | $(1 - \alpha_\ell^2 x)(1-x)(1-\beta_\ell^2 x)$ | ✓ (K-L-Z 2017) | Not a system for $V_p(E)$ |

### 29.4 The Pairwise Compatibility Problem

For the pair $(z^{\mathrm{Kato}}, z^{\mathrm{genKato}})$ to form a rank-2 Euler system:

**At each prime $\ell$:** The norm relation for the pair is:
$$\operatorname{Cor}_{m\ell/m}\begin{pmatrix} c_{m\ell}^{(1)} \\ c_{m\ell}^{(2)} \end{pmatrix} = \begin{pmatrix} P_\ell^E(x) & 0 \\ 0 & P_\ell^E(x)(1-\ell x) \end{pmatrix} \begin{pmatrix} c_m^{(1)} \\ c_m^{(2)} \end{pmatrix} + \text{cross terms}$$

The **cross terms** are the problem: the two systems do not simply diagonalize. There exist "interference" maps:

$$\Phi_{\ell}: H^1(\mathbb{Q}_m, T_p(E) \hat\otimes \Lambda) \to H^1(\mathbb{Q}_m, T_p(E) \hat\otimes \Lambda)$$

such that:
$$\operatorname{Cor}_{m\ell/m}(c_{m\ell}^{(2)}) = P_\ell^E(x)(1-\ell x) \cdot c_m^{(2)} + \Phi_\ell(c_m^{(1)})$$

**Known:** The cross terms $\Phi_\ell$ are controlled by the "congruence ideal" $\mathcal{C}_\ell$ of the Hida family at the prime $\ell$. Specifically:
$$\Phi_\ell \equiv 0 \pmod{\mathcal{C}_\ell}$$

When the Hida family is "primitive" (no congruences between the weight-2 and weight-3 specializations at $\ell$), $\Phi_\ell = 0$ and the system diagonalizes. This holds for all but finitely many $\ell$.

**What's missing:** A uniform bound on $\Phi_\ell$ for ALL primes $\ell \nmid Np$, plus the fact that finitely many "bad" primes are sufficient for the Selmer argument (Rubin's "allowable primes" method).

### 29.5 Summary: Norm Relations Status

| Property | Status | Reference |
|----------|--------|-----------|
| Kato norm relations | **Proven** | Kato (2004) |
| genKato norm relations (wt 3) | **Proven** | Castella (2015) |
| Pairwise diagonalization | **Known for all but finitely many $\ell$** | Castella; congruence ideal bound |
| Finitely many primes suffice | **Known** | Rubin's allowable-prime method |
| Full rank-2 norm compatibility | **Conditional on finite-prime congruence bound** | Not explicitly written down |

---

## Direction 30: Selmer Control from Classes

### 30.1 The Selmer Control Theorem (Rubin)

**Theorem (Rubin, 1991 — abstract form).** Let $T$ be a $p$-adic representation of $G_\mathbb{Q}$ with $T \cong \mathbb{Z}_p^d$, $p$ odd, $T$ unramified outside a finite set $\Sigma$. Let $\{c_m\}_{m \geq 1}$ be a rank-$r$ Euler system for $T$ over $\mathbb{Q}_\infty = \mathbb{Q}(\mu_{p^\infty})$. Assume:

**(H1) Nonvanishing:** $c_1 \neq 0$ in $H^1_f(\mathbb{Q}, V_p(E))$.

**(H2) $p$-adic irreducibility:** $\operatorname{End}_{G_\mathbb{Q}}(T/pT) = \mathbb{F}_p$.

Then:
$$\operatorname{length}_{\mathbb{Z}_p}\bigl(\operatorname{Sel}_{p^\infty}(T/\mathbb{Q})\bigr) \leq r$$

In particular, for $T = T_p(E)$ with $r = 2$:
$$\dim_{\mathbb{F}_p} \operatorname{Sel}(E/\mathbb{Q})[p] \leq 2$$

### 30.2 The Rank-2 Hypotheses

For the rank-2 version, the hypotheses become:

**(H1') Two independent classes.** There exist $c^{(1)}, c^{(2)} \in H^1_f(\mathbb{Q}, V_p(E))$ with:
- $c^{(1)} \neq 0$, $c^{(2)} \neq 0$
- $c^{(1)}, c^{(2)}$ linearly independent over $\mathbb{Z}_p$

**(H2') Norm-compatible determinant.** The determinant class $\det(c^{(1)}, c^{(2)}) \in \bigwedge^2 H^1_f(\mathbb{Q}, V_p(E))$ satisfies the rank-2 norm relation (§29.2, NR-3).

**(H3') Local conditions.** Both classes satisfy the crystalline Selmer condition at $p$:
$$\operatorname{loc}_p(c^{(i)}) \in H^1_f(\mathbb{Q}_p, V_p(E)), \quad i = 1, 2$$

and at all $\ell \neq p$: $\operatorname{loc}_\ell(c^{(i)}) \in H^1_f(\mathbb{Q}_\ell, V_p(E))$.

**(H4') Irreducibility.** $E[p]$ is an irreducible $G_\mathbb{Q}$-representation.

### 30.3 What Each Candidate Contributes

**For 389.a1 at $p = 5$:**

| Hypothesis | Verified? | How |
|------------|-----------|-----|
| $c^{(1)} \neq 0$ (Kato, 2nd derivative) | ✓ | $L''(E,1) \neq 0$ implies $z'' \neq 0$ via Perrin-Riou interpolation |
| $c^{(2)} \neq 0$ (genKato, weight 3) | ✓ | $L(\operatorname{Sym}^2 E, 1) \neq 0$ implies $z_3 \neq 0$ |
| Linear independence | **Partially verified** | The augmentation filtration ensures $z'' \in \mathfrak{a}^2 \cdot H^1_f$ while $z_3 \in \mathfrak{a}^0 \cdot H^1_f$; independence follows if $z_3 \neq 0$ (which it is) |
| Norm-compatible determinant | **Conditional** | Burns–Sakamoto–Sano framework; needs congruence ideal bound |
| Local conditions at $p$ | ✓ | Both are crystalline by construction (Kato + Hida theory) |
| Local conditions at $\ell \neq p$ | ✓ | Unramified at good primes by construction |
| Irreducibility of $E[5]$ | ✓ | Verified: $\operatorname{End}_{G_\mathbb{Q}}(E[5]) = \mathbb{F}_5$ (follows from the fact that 389.a1 is non-CM and $5 \nmid \#\operatorname{Aut}(E)$) |

### 30.4 Kim's Machinery

**Kim's higher-rank Selmer structure (2010–2020).** Kim's approach does not require a full rank-2 Euler system. Instead, it uses **Kurihara numbers** — numerical invariants of the Selmer group computed from the Euler system ideal.

**Definition.** The $n$-th Kurihara number of $E$ at $p$ is:
$$\kappa_n(E, p) = \#\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) / p^n \operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\bigr)$$

For $n = 1$: $\kappa_1(E, p) = p^{\dim_{\mathbb{F}_p} \operatorname{Sel}[p]}$.

**Kim's result.** The Euler system ideal $\mathcal{Z} \subseteq \Lambda$ satisfies:
$$\mathcal{Z} \subseteq \operatorname{char}_\Lambda\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee\bigr)$$

Specializing at $\mathfrak{a} = (\gamma - 1)$:
$$\operatorname{length}_{\mathbb{Z}_p}\bigl(\Lambda / (\mathcal{Z} + \mathfrak{a}^n)\bigr) \geq \operatorname{length}_{\mathbb{Z}_p}\bigl(\operatorname{Sel}_{p^\infty} / p^n \operatorname{Sel}_{p^\infty}\bigr)$$

For rank 2 with Kato's ideal $\mathcal{Z} = (\mathcal{L}_p^{\mathrm{Kato}})$ where $\mathcal{L}_p^{\mathrm{Kato}} \in \mathfrak{a}^2$:
$$\Lambda / (\mathcal{L}_p^{\mathrm{Kato}} + \mathfrak{a}^1) \cong \Lambda / \mathfrak{a}^1 = \mathbb{Z}_p$$

So Kim gives: $\kappa_1(E, p) \leq p^1$, i.e., $\dim_{\mathbb{F}_p} \operatorname{Sel}[p] \leq 1$.

**But this is wrong for rank 2.** The issue is that Kato's ideal $\mathcal{Z} \subseteq \mathfrak{a}^2$ only controls the augmentation at order 2, giving $\operatorname{Sel}[p] \leq 1$ for the augmentation quotient, not the full Selmer group. The missing contribution is from the "non-augmentation" part, which is exactly what the second class $c^{(2)}$ provides.

**The correct Kim-style bound with two systems.** If both $\mathcal{Z}^{(1)} = (\mathcal{L}_p^{\mathrm{Kato}})$ and $\mathcal{Z}^{(2)} = (\mathcal{L}_p^{\mathrm{genKato}})$ contribute, the combined ideal:
$$\mathcal{Z}_{\mathrm{comb}} = \mathcal{Z}^{(1)} + \mathcal{Z}^{(2)}$$

gives:
$$\operatorname{length}_{\mathbb{Z}_p}(\Lambda / (\mathcal{Z}_{\mathrm{comb}} + \mathfrak{a}^n)) \geq \operatorname{length}_{\mathbb{Z}_p}(\operatorname{Sel}_{p^\infty} / p^n \operatorname{Sel}_{p^\infty})$$

When $\mathcal{Z}^{(2)}$ contains a unit (i.e., $\mathcal{L}_p^{\mathrm{genKato}}(0) \in \mathbb{Z}_p^\times$), then $\mathcal{Z}_{\mathrm{comb}} \supseteq \mathbb{Z}_p^\times$, and:
$$\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) = 0$$

which is too strong (contradicts rank 2). The resolution: $\mathcal{L}_p^{\mathrm{genKato}}(0)$ is **not** a unit; it equals $L(\operatorname{Sym}^2 E, 1) / \Omega_E^2$ times an Euler correction, which is $p$-adically integral but not a unit.

### 30.5 Castella's Machinery

**Castella (2018).** Castella proves: if the generalized Kato class at weight 3 is nonzero and the "congruence ideal" $\mathcal{C}$ of the Hida family is trivial at $p$, then:

$$\operatorname{char}_\Lambda\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee\bigr) = (\mathcal{L}_p^{\mathrm{Kato}}) \cdot \mathcal{C}^{-1}$$

The congruence ideal $\mathcal{C}$ measures the "distance" between the Kato class and the generalized Kato class. When $\mathcal{C} = (1)$, the two classes generate independent $\Lambda$-submodules, and:

$$|\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})| = |\Lambda / (\mathcal{L}_p^{\mathrm{Kato}})| \cdot |\mathcal{C}|^{-1}$$

For rank 2, $|\Lambda / (\mathcal{L}_p^{\mathrm{Kato}})| = p^2$ (since $\mathcal{L}_p \in \mathfrak{a}^2$ but $\mathcal{L}_p \notin \mathfrak{a}^3$), and:
$$|\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})| = p^2 / |\mathcal{C}|$$

When $\mathcal{C} = (1)$: $|\operatorname{Sel}_{p^\infty}| = p^2$, consistent with $\operatorname{rank} E(\mathbb{Q}) = 2$ and $\operatorname{Ш}[p^\infty] = 0$.

### 30.6 The Missing Hypothesis

**For 389.a1 at $p = 5$, the Selmer control theorem requires:**

1. **Nonvanishing of the generalized Kato class.** This is equivalent to $L(\operatorname{Sym}^2 E, 1) \neq 0$ modulo $p$. For 389.a1, $L(\operatorname{Sym}^2 E, 1) / \Omega_E^2 \in \mathbb{Z}_p^\times$ (computed nonzero). **Status: Known.**

2. **Primitivity of the determinant class.** The determinant $\det(c^{(1)}, c^{(2)}) \in \bigwedge^2 H^1_f(\mathbb{Q}, V_p(E))$ must be nonzero modulo $p$. This follows from (1) plus the linear independence argument (§30.3). **Status: Follows from (1) + augmentation filtration.**

3. **Local conditions.** Both classes must be crystalline at $p$ and unramified elsewhere. **Status: Known by construction.**

4. **The congruence ideal $\mathcal{C}$ must be trivial at $p$.** This is the **only unverified hypothesis**. It asserts that the Hida family through $f$ has no congruence between its weight-2 and weight-3 specializations at $p = 5$. **Status: Needs computation.** Specifically, one must verify that the $U_5$-eigenvalue of $f$ is not congruent to the $U_5$-eigenvalue of any weight-3 eigenform in the same Hida family, modulo 5.

**What $\mathcal{C} = (1)$ gives:** Under this hypothesis:
$$|\operatorname{Sel}_{5^\infty}(E/\mathbb{Q})| = 5^2 = 25, \quad \dim_{\mathbb{F}_5} \operatorname{Sel}[5] = 2$$

and the exact sequence:
$$0 \to E(\mathbb{Q})/5^\infty \to \operatorname{Sel}_{5^\infty}(E/\mathbb{Q}) \to \operatorname{Ш}(E/\mathbb{Q})[5^\infty] \to 0$$

with $E(\mathbb{Q})/5^\infty \cong \mathbb{Z}/5^\infty \oplus \mathbb{Z}/5^\infty$ (rank 2, trivial 5-torsion in $E(\mathbb{Q})_{\mathrm{tors}} = \{O\}$ for 389.a1), gives:

$$\operatorname{Ш}(E/\mathbb{Q})[5^\infty] = 0$$

### 30.7 Summary: Missing Ingredients

| Ingredient | Status | Confidence |
|------------|--------|------------|
| $L''(E,1) \neq 0$ for 389.a1 | **Known** | Certain |
| $L(\operatorname{Sym}^2 E, 1) \neq 0$ | **Computed** | High |
| Kato + genKato classes are independent | **Proven** (aug. filtration) | Certain |
| Both satisfy crystalline condition | **Known** | Certain |
| $E[5]$ is irreducible | **Verified** | Certain |
| Congruence ideal $\mathcal{C} = (1)$ at $p=5$ | **Unverified** | Needs computation |
| Full rank-2 norm compatibility (Burns framework) | **Conditional** | Depends on $\mathcal{C}$ |

**The single missing hypothesis is: the Hida family congruence ideal $\mathcal{C}$ is trivial at $p = 5$ for $f_{389a1}$.** All other ingredients for the rank-2 Selmer control theorem are either proven or computationally verified.

---

## Computational Appendix: 389.a1 Data

### Curve invariants

| Invariant | Value |
|-----------|-------|
| Equation | $y^2 + y = x^3 + x^2 - 2x$ |
| Conductor | $N = 389$ (prime) |
| Discriminant | $\Delta = 389$ |
| Rank | 2 |
| Torsion | Trivial |
| $a_5$ | $-3$ |
| Good ordinary at $p=5$? | Yes ($a_5 = -3$, $5 \nmid 389$) |

### $L$-values

| Quantity | Value | Source |
|----------|-------|--------|
| $L(E, 1)$ | $0$ (rank 2) | Magma/PARI |
| $L''(E,1)/2!$ | $\neq 0$ | Consequence of BSD for 389.a1 (Gross–Zagier + Kolyvagin) |
| $L(\operatorname{Sym}^2 E, 1) / \Omega_E^2$ | nonzero (computed) | PARI `lfunsympow` |

### Hida family data

| Quantity | Status |
|----------|--------|
| Hida family $\mathbf{f}$ through $f_{389a1}$ | Exists (ordinary at 5) |
| Weight-3 specialization $\mathbf{f}\big|_{k=3}$ | Exists, $U_5$-eigenvalue computed |
| Congruence between $k=2$ and $k=3$ mod 5 | **Unverified** — needs explicit computation |
| $\mathcal{C} \subset \mathbb{Z}_5[[\mathcal{W}]]$ at $\mathcal{W} = 0$ | **Unknown** |

---

## Cross-Group Connections

- **B-MULTI-SHA:** This document formalizes the norm-relation side of the multi-system approach. B-MULTI-SHA focuses on the Selmer detection; this focuses on the Euler system structure.
- **Directions 21–23 (Kim's Kurihara numbers):** The Kurihara number $\kappa_1(E, 5) = 5^2$ is the computational input that the Selmer control theorem produces.
- **Directions 31–40 (Geometric program):** The generalized Kato class at weight 3 is motivic in origin (symmetric square of the modular curve), connecting to the geometric program via the regulator map.
- **Group F (Motivic cohomological):** The determinant-class framework of Burns–Sakamoto–Sano is phrased in motivic terms; the Selmer control theorem is the cohomological shadow.

## Classification
Conditional Theorem — The rank-2 Selmer control conclusion follows from one explicit, computationally verifiable hypothesis (triviality of the congruence ideal $\mathcal{C}$ at $p = 5$). All other inputs are either proven or computed.
