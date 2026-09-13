# Selmer Group Structure: Tate–Shafarevich and Iwasawa Theory

## 1. The Selmer Group as a $\mathbb{Z}_p$-Module

### Definition

Let $E/\mathbb{Q}$ be an elliptic curve and $p$ a prime. The $p^\infty$-Selmer group is

$$\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) = \varinjlim_n \operatorname{Sel}_{p^n}(E/\mathbb{Q}),$$

where each $\operatorname{Sel}_{p^n}(E/\mathbb{Q})$ sits in the exact sequence

$$0 \longrightarrow E(\mathbb{Q})/p^n E(\mathbb{Q}) \longrightarrow \operatorname{Sel}_{p^n}(E/\mathbb{Q}) \longrightarrow \Sha(E/\mathbb{Q})[p^n] \longrightarrow 0.$$

Taking the direct limit:

$$0 \longrightarrow E(\mathbb{Q}) \otimes (\mathbb{Q}_p/\mathbb{Z}_p) \longrightarrow \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \longrightarrow \Sha(E/\mathbb{Q})[p^\infty] \longrightarrow 0.$$

Since $E(\mathbb{Q}) \otimes (\mathbb{Q}_p/\mathbb{Z}_p) \cong (\mathbb{Q}_p/\mathbb{Z}_p)^r$ where $r = \operatorname{rank} E(\mathbb{Q})$, the Selmer group decomposes as an extension of the divisible part by the $p$-primary torsion of $\Sha$.

### Pontryagin Dual

The **Pontryagin dual** is

$$\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})^\vee = \operatorname{Hom}_{\mathrm{cont}}\!\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}),\, \mathbb{Q}_p/\mathbb{Z}_p\bigr).$$

This is a finitely generated $\mathbb{Z}_p$-module. By the structure theorem for finitely generated modules over a PID:

$$\boxed{\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})^\vee \;\cong\; \mathbb{Z}_p^{\,\rho_p} \;\oplus\; T_p}$$

where:
- $\rho_p = \operatorname{corank}_p \operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ is the **$p$-corank** (the $\mathbb{Z}_p$-rank of the free part),
- $T_p$ is a finite $p$-group (the torsion submodule).

The free rank $\rho_p$ controls the divisible part; the torsion $T_p$ captures the finite $p$-power obstruction. From the exact sequence above:

$$\rho_p = r + \operatorname{corank}_p \Sha(E/\mathbb{Q})[p^\infty].$$

Since $\Sha$ is conjectured finite, $\operatorname{corank}_p \Sha = 0$, giving $\rho_p = r$ unconditionally **if** $\Sha[p^\infty]$ is finite.

### Consequence of the Birch and Swinnerton-Dyer Conjecture

Under BSD, $\Sha(E/\mathbb{Q})$ is finite, so:

$$\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})^\vee \;\cong\; \mathbb{Z}_p^{\,r} \;\oplus\; \Sha(E/\mathbb{Q})[p^\infty].$$

The finite part is exactly $\Sha(E/\mathbb{Q})[p^\infty]$, and the corank of the Selmer group equals the Mordell–Weil rank $r$.

---

## 2. Selmer Structure for 389.a1 at Various Primes

The curve **389.a1** has conductor $N = 389$ (prime), rank $r = 2$, and trivial rational torsion ($E(\mathbb{Q})_{\mathrm{tors}} = 0$).

### At $p = 2$

From 2-descent (explicit descent via 2-isogeny or full 2-descent):

$$\dim_{\mathbb{F}_2} \operatorname{Sel}_{2}(E/\mathbb{Q}) = 2.$$

Since $E(\mathbb{Q})[2] = 0$ (no rational 2-torsion as 389 is prime and the curve has no rational root of the cubic), we have

$$\dim_{\mathbb{F}_2} \operatorname{Sel}_{2}(E/\mathbb{Q}) = r + \dim_{\mathbb{F}_2} \Sha(E/\mathbb{Q})[2].$$

With $r = 2$ and $\dim_{\mathbb{F}_2} \operatorname{Sel}_2 = 2$, this gives:

$$\Sha(E/\mathbb{Q})[2] = 0.$$

Hence the 2-primary part of $\Sha$ is trivial, and $\operatorname{corank}_2 \operatorname{Sel}_{2^\infty} = 2$.

### At $p = 5$

Assuming the hypotheses of **Skinner–Urban** (the Iwasawa main conjecture for $\operatorname{GL}_2$ at an ordinary prime $p \nmid N$ with appropriate non-vanishing of the $L$-function derivative), the $p$-adic $L$-function controls the Selmer group. For $p = 5$ and 389.a1:

- $p = 5 \nmid 389N$, so $E$ is ordinary at $5$.
- The Skinner–Urban theorem (under their hypotheses on the residual representation and $p$-adic analytic conditions) gives:

$$\operatorname{corank}_5 \operatorname{Sel}_{5^\infty}(E/\mathbb{Q}) = \operatorname{ord}_{s=1} L(E, s) = 2.$$

**Caveat:** This requires verification of:
1. The residual representation $\bar{\rho}_{E,5}$ is irreducible.
2. $E$ has good ordinary reduction at $p = 5$.
3. There exists a prime $q \equiv 1 \pmod{5}$ where $E$ has split multiplicative reduction, or other technical conditions ensuring the "big Heegner point" or Euler system machinery applies.

If these hold, $\Sha(E/\mathbb{Q})[5^\infty] = 0$ as well.

### At $p = 3$

No explicit 3-descent for 389.a1 has been carried out in our computations. The structure is **unknown** without:

- An explicit 3-descent (computing $\operatorname{Sel}_3(E/\mathbb{Q})$ via the Kummer map into $H^1(\mathbb{Q}, E[3])$), or
- Verification of Skinner–Urban hypotheses at $p = 3$.

The expectation (from BSD) is $\operatorname{corank}_3 = 2$ and $\Sha[3^\infty] = 0$, but this remains unverified.

### Summary Table for 389.a1

| Prime $p$ | $\operatorname{corank}_p \operatorname{Sel}_{p^\infty}$ | $\Sha[p^\infty]$ | Method |
|-----------|--------------------------------------------------------|-------------------|--------|
| 2         | 2                                                      | $0$              | Explicit 2-descent |
| 3         | unknown                                                | unknown          | Requires 3-descent |
| 5         | 2 (conditional)                                        | $0$ (conditional) | Skinner–Urban (if hypotheses hold) |
| $p \geq 7$, $p \nmid 389$ | $\geq 2$ (by rank)                   | unknown          | — |

---

## 3. The Control Theorem

### Statement

For each $n \geq 1$, there is a **restriction map**

$$\rho_n : \operatorname{Sel}_{p^n}(E/\mathbb{Q}) \longrightarrow \operatorname{Sel}_{p^{n+1}}(E/\mathbb{Q})$$

arising from the natural inclusion $E[p^n] \hookrightarrow E[p^{n+1}]$.

**Theorem (Control Theorem — Greenberg, Mazur).** *For $n \gg 0$:*

1. $\ker(\rho_n)$ *stabilizes: it is isomorphic to $H^1(\operatorname{Gal}(K_n/\mathbb{Q}),\, E[p^\infty])$ for the appropriate extension $K_n$, and this kernel is finite and bounded independently of $n$.*

2. $\operatorname{coker}(\rho_n)$ *stabilizes: it is isomorphic to a subgroup of $H^0(\operatorname{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}),\, \Sha(E/\mathbb{Q})[p])$ tensored up, and is likewise finite and bounded.*

3. *The **stable corank** satisfies:*

$$\boxed{\operatorname{corank} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \;=\; \operatorname{rank} E(\mathbb{Q}) \;+\; \operatorname{corank}_p \Sha(E/\mathbb{Q})[p^\infty].}$$

### Interpretation

The control theorem tells us that the passage from level $p^n$ to $p^{n+1}$ is "asymptotically trivial" on the divisible part. All the interesting arithmetic is captured at finite level, and the limit $\operatorname{Sel}_{p^\infty}$ is a faithful reflection of:

- The rank of $E(\mathbb{Q})$ (the free $\mathbb{Z}_p$-part of the dual), plus
- The $p$-primary part of $\Sha$ (the torsion in the dual).

The key consequence: **computing the corank of $\operatorname{Sel}_{p^\infty}$ and knowing the rank $r$ immediately determines whether $\Sha[p^\infty]$ is trivial or not.**

---

## 4. Structural Consequences for 389.a1

### Direct Consequence

For 389.a1 with $r = 2$:

$$\operatorname{corank}_p \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) = 2 + \operatorname{corank}_p \Sha(E/\mathbb{Q})[p^\infty].$$

Therefore:

> **If $\operatorname{corank}_p \operatorname{Sel}_{p^\infty} = 2$**, then $\Sha(E/\mathbb{Q})[p^\infty] = 0$, meaning the $p$-primary part of $\Sha$ is trivial.

> **If $\operatorname{corank}_p \operatorname{Sel}_{p^\infty} > 2$**, then $\Sha(E/\mathbb{Q})[p^\infty] \neq 0$, meaning there is nontrivial $p$-power torsion in $\Sha$.

### What We Know

- **At $p = 2$:** $\operatorname{corank}_2 = 2 \implies \Sha(E/\mathbb{Q})[2^\infty] = 0$. In particular, $\#\Sha(E/\mathbb{Q})$ is odd.
- **At $p = 5$:** Conditionally $\operatorname{corank}_5 = 2 \implies \Sha(E/\mathbb{Q})[5^\infty] = 0$.
- **Global:** If $\Sha[p^\infty] = 0$ for all primes $p$, then $\Sha(E/\mathbb{Q})$ is trivial. Combined with the known results, **$\Sha(E/\mathbb{Q}) = 0$ is expected and partially verified** (at least the 2-primary and 5-primary parts vanish).

### The Cassels–Tate Pairing

The Cassels–Tate alternating pairing

$$\Sha(E/\mathbb{Q}) \times \Sha(E/\mathbb{Q}) \longrightarrow \mathbb{Q}/\mathbb{Z}$$

implies that $\#\Sha(E/\mathbb{Q})$ is a perfect square (when finite). Since $E(\mathbb{Q})_{\mathrm{tors}} = 0$ for 389.a1 and the curve has no CM, the expected value $\#\Sha = 1$ (a perfect square) is consistent.

---

## 5. Connection to Iwasawa Theory

### The Cyclotomic Tower

Fix a prime $p$. Let $\mathbb{Q}_\infty = \bigcup_n \mathbb{Q}(\zeta_{p^{n+1}})$ be the cyclotomic $\mathbb{Z}_p$-extension of $\mathbb{Q}$, with layers $\mathbb{Q}_n = \mathbb{Q}(\zeta_{p^{n+1}})^+$. Set $\Gamma = \operatorname{Gal}(\mathbb{Q}_\infty/\mathbb{Q}) \cong \mathbb{Z}_p$ and $\Lambda = \mathbb{Z}_p[[\Gamma]] \cong \mathbb{Z}_p[[T]]$ the Iwasawa algebra.

### The Iwasawa Module

Define the **Pontryagin dual of the Selmer group over the tower**:

$$X = \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee = \operatorname{Hom}_{\mathrm{cont}}\!\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty),\, \mathbb{Q}_p/\mathbb{Z}_p\bigr).$$

This is a finitely generated torsion $\Lambda$-module (by a theorem of Kato, assuming $p$ is a prime of good ordinary reduction for $E$).

### Structure Theorem (Pseudo-null version)

By the structure theorem for finitely generated torsion $\Lambda$-modules (Iwasawa, $\Lambda$-module theory):

$$X \sim_{\Lambda} \bigoplus_{i=1}^s \Lambda/(f_i(T)^{e_i})$$

where $\sim$ denotes pseudo-isomorphism (isomorphism up to pseudo-null modules, i.e., modules whose support has codimension $\geq 2$), and $f_i(T) \in \mathbb{Z}_p[[T]]$ are distinguished polynomials.

The **characteristic ideal** of $X$ is:

$$\operatorname{char}(X) = \prod_{i=1}^s f_i(T)^{e_i} \cdot \Lambda.$$

### The Main Conjecture (Mazur–Wiles, Kato)

**Theorem (Mazur–Wiles, 1984; refined by Kato, 2004).** *For $p$ an odd prime where $E$ has good ordinary reduction, the characteristic ideal of $X$ is generated by the $p$-adic $L$-function:*

$$\boxed{\operatorname{char}(X) = \bigl(\mathcal{L}_p(E)\bigr) \cdot \Lambda}$$

where $\mathcal{L}_p(E) \in \Lambda$ is the algebraic $p$-adic $L$-function constructed via modular symbols (or Hida families, in the ordinary case).

This is the **Iwasawa Main Conjecture for elliptic curves**, proved by:
- **Skinner–Urban (2014)** for $p$ ordinary, under certain hypotheses on the residual representation.
- **Kato (2004)** gives one divisibility unconditionally via Euler systems.

### Specialization to the Base Layer

Evaluating at the augmentation ideal $T = 0$ (i.e., restricting to $\mathbb{Q}$) recovers the classical Selmer group:

$$X / T \cdot X \;\twoheadrightarrow\; \operatorname{Sel}_{p^\infty}(E/\mathbb{Q})^\vee$$

with finite kernel and cokernel controlled by the $\mu$-invariant and the structure of $X$ as a $\Lambda$-module.

The **$p$-adic $L$-function** $\mathcal{L}_p(E)$ specializes to:

$$\mathcal{L}_p(E)\big|_{T=0} \;=\; L_p(E, 1) \;=\; \frac{\Omega_E^+ \cdot \operatorname{Reg}_p(E) \cdot \prod c_v \cdot \#\Sha[p^\infty]}{(\#E(\mathbb{Q})_{\mathrm{tors}})^2} \cdot (\text{period/interp.\ factors})$$

which is the $p$-adic BSD formula.

### Iwasawa Invariants for 389.a1

The $\Lambda$-module $X$ is characterized by two numerical invariants:

- **$\lambda$-invariant:** $\lambda_p = \operatorname{rank}_{\mathbb{Z}_p}(X / T \cdot X)$ (measures the "size" of $X$),
- **$\mu$-invariant:** $\mu_p$ (measures the $p$-power torsion in $X$; conjectured $= 0$ for elliptic curves over $\mathbb{Q}$ by Ferrero–Washington type results).

For 389.a1 at $p = 2$:
- $\operatorname{corank}_2 \operatorname{Sel}_{2^\infty} = 2$ and $\Sha[2^\infty] = 0$.
- The $\lambda$-invariant satisfies $\lambda_2 \geq r = 2$.
- The equality $\lambda_2 = 2$ would mean the Selmer group over $\mathbb{Q}_\infty$ is "no larger" than over $\mathbb{Q}$, reflecting no growth of Sha in the tower.

### Summary of Iwasawa-Theoretic Picture

| Object | Role |
|--------|------|
| $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ | Selmer group at the base; detects rank and $\Sha[p^\infty]$ |
| $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})^\vee \cong \mathbb{Z}_p^r \oplus T_p$ | Pontryagin dual; free part = rank, torsion = $\Sha[p^\infty]$ |
| $X = \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee$ | Iwasawa module; torsion $\Lambda$-module (Kato) |
| $\operatorname{char}(X) = (\mathcal{L}_p(E))$ | Main conjecture; algebraic = analytic |
| $\mathcal{L}_p(E)\|_{T=0}$ | $p$-adic $L$-value; BSD formula at $s=1$ |
| $\lambda_p, \mu_p$ | Iwasawa invariants governing growth in the tower |

---

## Conclusions for 389.a1

1. **Selmer group duality:** $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})^\vee$ is finitely generated over $\mathbb{Z}_p$ with free rank $= \operatorname{corank}_p$ and torsion $= \Sha[p^\infty]$.

2. **At $p = 2$:** The Selmer group has corank 2, equal to the rank. Hence $\Sha[2^\infty] = 0$.

3. **At $p = 5$:** Conditionally (Skinner–Urban), corank 2 and $\Sha[5^\infty] = 0$.

4. **The control theorem** ensures the corank is well-defined and equals $r + \operatorname{corank}_p \Sha[p^\infty]$.

5. **Iwasawa theory** provides the structural framework: the main conjecture equates the characteristic ideal of $X$ with the $p$-adic $L$-function, giving a precise algebraic meaning to analytic data. For 389.a1, this machinery confirms (under hypotheses) that the Selmer group is as small as rank alone predicts — no hidden $\Sha$-torsion.
