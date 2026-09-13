# E-PCONVERSE · p-Converse Theorems, Leading-Term Comparisons, Sha Finiteness, and Hypothesis Removal

## Directions 41–44 from the Restructured Program (Phase 5: Missing Implications)

---

## Direction 41: Higher-Rank p-Converse

### Status Assessment

**Open for $r \geq 2$ in general; proven for $r = 1$ unconditionally; proven for $r = 2$ for CM curves under additional hypotheses.** The $r = 0$ case (analytic non-vanishing implies algebraic non-vanishing) is classical (Kolyvagin, Gross–Zagier). The $r = 1$ case (analytic rank $\geq 1$ implies algebraic rank $\geq 1$) is known unconditionally by combining Kolyvagin's Euler system with the work of Kato (2004) and the non-vanishing of Heegner points. For $r \geq 2$, the problem is completely open for non-CM curves.

### Precise Statement

**The p-Converse Theorem.** Let $E/\mathbb{Q}$ be an elliptic curve, $p$ a prime of good ordinary reduction, and $r \geq 0$ an integer. The *p-converse* to the Iwasawa main conjecture asserts:

$$\operatorname{corank}_{\mathbb{Z}_p}\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\bigr) \geq r \quad \Longrightarrow \quad \operatorname{ord}_{s=1} L(E, s) \geq r$$

or equivalently (under modularity), the contrapositive: if $L(E, s)$ vanishes to order $< r$ at $s = 1$, then $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ has corank $< r$.

This is the *reverse* direction of the implication that Kato's Euler system establishes. Kato proves:

$$\operatorname{ord}_{s=1} L(E, s) \geq r \quad \Longrightarrow \quad \operatorname{corank}_{\mathbb{Z}_p}\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})\bigr) \geq r$$

The p-converse asks for the opposite implication.

### What Is Known

| Rank $r$ | Status | Key Results |
|----------|--------|-------------|
| $r = 0$ | **Theorem** | If $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ is finite, then $L(E, 1) \neq 0$. Proven by Kolyvagin (1989) for $p$-part; extended by Gross (1986) via Waldspurger. |
| $r = 1$ | **Theorem** | If $\operatorname{corank}_{\mathbb{Z}_p} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \geq 1$, then $\operatorname{ord}_{s=1} L(E, s) \geq 1$. Proven by: Skinner (2014) using the Eisenstein ideal; combined with Kato's Euler system. Also follows from Nekovář's work on Kolyvagin's Euler system for $r = 1$. |
| $r = 2$ (CM) | **Partial** | Castella (2015, 2019): For $E/\mathbb{Q}$ with CM by an imaginary quadratic field $K$ and $p$ split in $K$, proves the p-converse for $r = 2$ under the additional hypothesis that the generalized Kato class is non-trivial. |
| $r = 2$ (non-CM) | **Open** | No proof exists. |
| $r \geq 3$ | **Open** | Completely open in all cases. |

### The Core Difficulty for $r \geq 2$

**Kato's Euler system produces a single class** $z_f^{(p)} \in H^1(\mathbb{Q}, T_p(E))$. For $r = 0$ and $r = 1$, the non-vanishing of $z_f^{(p)}$ (or its image under the dual exponential) forces $\operatorname{corank} \leq r$, which combined with Kato's inequality $\operatorname{corank} \geq r$ gives equality. For $r \geq 2$, the image of $z_f^{(p)}$ under the dual exponential map vanishes (since $\exp^*_{V_p(E)}$ factors through $\operatorname{Fil}^0 D_{\mathrm{dR}}(V_p(E))$, which has rank 1). The Euler system class thus lives entirely in the "finite part" of the cohomology and cannot by itself detect the rank.

**What is missing:** A *higher Euler system* — a family of cohomology classes parametrized by auxiliary data (e.g., products of modular curves, Rankin–Selberg convolutions) that is "non-degenerate" enough to force $\operatorname{corank} \leq r$. The candidates are:

1. **Beilinson–Flach elements** $z_{\mathrm{BF}}^{(f,g)} \in H^1(\mathbb{Q}, T_p(f) \otimes T_p(g))$ for two modular forms $f, g$. When $g$ is an Eisenstein series, these specialize to Kato's classes. When both $f = g$, they produce classes in the symmetric square, which is related to $r = 2$ via the Bloch–Kato filtration.

2. **Generalized Kato classes** (Castella): For $E/\mathbb{Q}$ and a quadratic character $\chi$ of an imaginary quadratic field $K$, construct classes in $H^1(\mathbb{Q}, T_p(E) \otimes \chi)$ from the Rankin–Selberg convolution $L(f \otimes \chi, s)$. The non-vanishing of these classes at $s = 1$ is the key input.

3. **Kim's higher-rank Selmer structure** (Kim 2020): Uses Kurihara numbers — elements of the completed group ring $\mathbb{Z}_p[[\operatorname{Gal}(K_\infty/K)]]$ — to produce a *higher-rank Selmer condition* that detects the full Selmer group when $r \geq 2$. The Kurihara numbers encode arithmetic data from local points and Heegner cycles.

### Castella's Result for CM Curves (Sketch)

**Theorem (Castella 2015).** Let $E/\mathbb{Q}$ have CM by $\mathcal{O}_K$ where $K = \mathbb{Q}(\sqrt{-D})$, $p$ an odd prime splitting in $K$ as $\mathfrak{p}\bar{\mathfrak{p}}$. Assume:
- (H1) $E[p]$ is irreducible as a $G_{\mathbb{Q}}$-representation.
- (H2) The generalized Kato class $\kappa_p(E, \chi) \in H^1(\mathbb{Q}, T_p(E) \otimes \chi)$ is non-trivial, where $\chi$ is the character of $K/\mathbb{Q}$.

Then: $\operatorname{corank}_{\mathbb{Z}_p} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) = 2 \Longrightarrow \operatorname{ord}_{s=1} L(E, s) \geq 2$.

The proof constructs the generalized Kato class from the Rankin–Selberg convolution $L(f \otimes \chi_K, s)$, uses the CM structure to identify it with an elliptic unit (via the Gross–Stark conjecture / Shimura's reciprocity law), and applies Perrin-Riou's explicit reciprocity to relate its $p$-adic valuation to the derivative of $L_p(E, s)$.

### What Is Missing for Non-CM Curves

1. **No generalized Kato class is known to be non-trivial** for a specific non-CM curve $E/\mathbb{Q}$ at a specific prime $p$ when $r = 2$. The non-vanishing hypothesis (H2) in Castella's theorem is verified for CM curves using the CM structure but is completely open otherwise.

2. **The Beilinson–Flach Euler system** $z_{\mathrm{BF}}^{(f,f)}$ lives in $H^1(\mathbb{Q}, \operatorname{Sym}^2 T_p(f))$, not in $H^1(\mathbb{Q}, T_p(f))$. The "projection" from $\operatorname{Sym}^2$ to the standard representation requires an algebraic cycle on $E \times E$, and the relevant cycle (the diagonal) has trivial Abel–Jacobi image by Gross–Schoen.

3. **The $p = 2, 3$ case** is excluded from all current results. Ihara's lemma, which is essential to the Skinner–Urban argument, fails at small primes.

4. **Supersingular primes** require a fundamentally different approach (Kobayashi's $\pm$-Selmer groups, Wan's Iwasawa main conjecture). No p-converse result of any kind is known at supersingular primes for $r \geq 2$.

### BSD Connection

The p-converse is one half of the equivalence:
$$\operatorname{rank} E(\mathbb{Q}) = r \quad \Longleftrightarrow \quad \operatorname{ord}_{s=1} L(E, s) = r$$
Without the p-converse, Kato's Euler system proves only the $\Leftarrow$ direction (analytic rank $\geq r$ implies algebraic rank $\geq r$). The $\Rightarrow$ direction (algebraic rank $\geq r$ implies analytic rank $\geq r$) is needed to complete the rank-prediction part of BSD for $r \geq 2$.

---

## Direction 42: Complex Leading-Term Comparison

### Status Assessment

**Proven for $r = 0$ under mild hypotheses; open for $r \geq 1$ in general.** The comparison relates the leading coefficient of the complex $L$-function to the leading coefficient of the $p$-adic $L$-function, connecting classical BSD to $p$-adic BSD.

### Precise Statement

**Classical BSD (rank $r$).**
$$\frac{L^{(r)}(E, 1)}{r!} = \Omega_E^+ \cdot R_E \cdot \frac{|\Sha(E/\mathbb{Q})| \cdot \prod_{v \mid N} c_v}{|E(\mathbb{Q})_{\mathrm{tors}}|^2}$$

where $\Omega_E^+ = \int_{E(\mathbb{R})} |\omega|$ is the real period, $R_E = \det(\hat{h}_\infty(P_i, P_j))_{1 \leq i,j \leq r}$ is the classical regulator, $c_v$ are Tamagawa numbers, and $\hat{h}_\infty$ is the Néron–Tate height.

**$p$-adic BSD (rank $r$).**
$$\frac{L_p^{(r)}(E, 0)}{r!} = \frac{|\Sha(E/\mathbb{Q})[p^\infty]|}{|E(\mathbb{Q})_{\mathrm{tors}}|_p^2} \cdot R_p(E) \cdot \prod_{v \mid N} c_v^{(p)} \cdot \mathcal{E}_p(E)$$

where $R_p(E) = \det(\hat{h}_p(P_i, P_j))_{1 \leq i,j \leq r}$ is the $p$-adic regulator, $c_v^{(p)}$ is the $p$-part of $c_v$, $|E(\mathbb{Q})_{\mathrm{tors}}|_p$ is the $p$-part of the torsion order, and $\mathcal{E}_p(E)$ is the exceptional zero correction factor (equal to 1 if no exceptional zero).

**The Comparison Problem.** Eliminate $\Sha$ and $c_v$ from both formulas and relate:
$$\frac{L^{(r)}(E, 1) / r!}{L_p^{(r)}(E, 0) / r!} \quad = \quad \frac{\Omega_E^+ \cdot R_E \cdot |E(\mathbb{Q})_{\mathrm{tors}}|_p^2 \cdot \mathcal{E}_p^{-1}}{R_p(E) \cdot |E(\mathbb{Q})_{\mathrm{tors}}|^2 \cdot \Omega_E^+} \quad \times \quad \frac{|\Sha|}{|\Sha[p^\infty]|} \cdot \frac{\prod c_v}{\prod c_v^{(p)}}$$

The ratio simplifies to:
$$\frac{L^{(r)}(E, 1) / r!}{L_p^{(r)}(E, 0) / r!} = \frac{R_E}{R_p(E)} \cdot \frac{1}{|E(\mathbb{Q})_{\mathrm{tors}}|_{p'}^2} \cdot \frac{|\Sha|}{|\Sha[p^\infty]|} \cdot \frac{\prod c_v}{\prod c_v^{(p)} \cdot \mathcal{E}_p}$$

where $|E(\mathbb{Q})_{\mathrm{tors}}|_{p'}$ is the prime-to-$p$ part of the torsion order. The key ratio is:

$$\boxed{\frac{R_E}{R_p(E)} = \frac{\det(\hat{h}_\infty(P_i, P_j))}{\det(\hat{h}_p(P_i, P_j))} \stackrel{?}{=} \frac{(\Omega_E^+)^r}{(\Omega_p(E))^r} \cdot (\text{$p$-adic unit})}$$

where $\Omega_p(E) \in \mathbb{Q}_p^\times$ is the $p$-adic period.

### The Interpolation Factor

For $r = 0$, the comparison is:
$$L_p(E, 1) = \mathcal{E}_p(E) \cdot \left(1 - \frac{a_p}{\alpha}\right)\left(1 - \frac{1}{\beta}\right) \cdot \frac{L(E, 1)}{\Omega_E^+}$$

where $\alpha, \beta$ are roots of $x^2 - a_p x + p = 0$ with $|\alpha|_p = 1$ (for ordinary $p$). This is the *interpolation formula* — it expresses the $p$-adic $L$-value in terms of the complex $L$-value divided by the real period, times an explicit Euler factor.

For $r \geq 1$, the analogous formula involves the *$p$-adic period* $\Omega_p(E)$:
$$\frac{L_p^{(r)}(E, 0)}{r!} = \left(\frac{\Omega_E^+}{\Omega_p(E)}\right)^r \cdot \frac{L^{(r)}(E, 1)}{r!} \cdot (\text{Euler factors}) \cdot (\text{correction})$$

### What Is Known

1. **$r = 0$, no exceptional zero (Mazur–Tate–Teitelbaum 1986).** The interpolation formula is proven:
$$L_p(E, 1) = \left(1 - \frac{a_p}{\alpha}\right) \cdot \frac{L(E, 1)}{\Omega_E^+}$$
This is an identity in $\mathbb{Q}_p$ (up to $p$-adic units). The Euler factor $(1 - a_p/\alpha)$ is the "missing" factor at $p$ in the Euler product of $L(E, s)$.

2. **$r = 0$, with exceptional zero (MTT, Greenberg–Stevens).** When $a_p = 1$ (or $E$ has split multiplicative reduction at $p$), $L_p(E, 1) = 0$ and the comparison involves the $\mathcal{L}$-invariant:
$$L_p'(E, 1) = \mathcal{L}_p(E) \cdot \left(1 - \frac{1}{p}\right) \cdot \frac{L(E, 1)}{\Omega_E^+}$$

3. **$r = 1$ (Perrin-Riou 1992).** The comparison for the first derivative:
$$L_p'(E, 0) = \frac{\Omega_E^+}{\Omega_p(E)} \cdot \left(1 - \frac{a_p}{\alpha}\right) \cdot L'(E, 1) + (\text{correction from }p\text{-adic height splitting})$$
This is known up to the choice of $p$-adic height (the *splitting* of the Hodge filtration at $p$).

4. **$r \geq 2$ (Open).** No rigorous comparison exists. The difficulty is that the $p$-adic regulator $R_p(E) = \det(\hat{h}_p(P_i, P_j))$ depends on the choice of $p$-adic height $\hat{h}_p$, which in turn depends on:
   - A choice of splitting $\sigma: D_{\mathrm{dR}}(V_p(E)) / \mathrm{Fil}^0 \to D_{\mathrm{dR}}(V_p(E))$ of the Hodge filtration.
   - The $p$-adic period $\Omega_p(E)$, which is defined by the Fontaine comparison isomorphism.

### The p-adic Period

The $p$-adic period $\Omega_p(E) \in \mathbb{Q}_p^\times$ is defined as follows. By the comparison isomorphism (Faltings):
$$D_{\mathrm{dR}}(V_p(E)) := (V_p(E) \otimes_{\mathbb{Q}_p} B_{\mathrm{dR}})^{G_{\mathbb{Q}_p}} \cong H^1_{\mathrm{dR}}(E/\mathbb{Q}_p)$$

choose a basis $\{\omega, \eta\}$ of $H^1_{\mathrm{dR}}(E/\mathbb{Q}_p)$ with $\omega$ the Néron differential and $\eta$ a differential of the second kind. Then:
$$\Omega_p(E) = \exp_p\left(\int_O^{\hat{O}} \omega\right)^{-1}$$
where $\hat{O}$ is the identity of the formal group and $\exp_p$ is the $p$-adic exponential. Equivalently, $\Omega_p(E) = \log_p(\hat{\omega})$ where $\hat{\omega}$ is the generator of the invariant differential of the formal group.

**Explicit formula:** For $E: y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6$ with Néron differential $\omega = dx/(2y + a_1 x + a_3)$:
$$\Omega_p(E) = \log_p\left(\hat{x}(p)\right) / \hat{x}(p) \quad \text{(formal group logarithm)}$$

### What Is Missing

1. **For $r \geq 2$:** The comparison $\det(\hat{h}_\infty(P_i, P_j)) / \det(\hat{h}_p(P_i, P_j)) \stackrel{?}{=} (\Omega_E^+ / \Omega_p(E))^r$ requires understanding how the classical Néron–Tate height and the $p$-adic height are related *at the level of the determinant*. For $r = 1$, this is a single ratio; for $r = 2$, it involves a $2 \times 2$ determinant and cross-terms.

2. **The splitting problem:** The $p$-adic height $\hat{h}_p$ depends on a choice of splitting $\sigma$ of the Hodge filtration $0 \to \mathrm{Fil}^0 \to D_{\mathrm{dR}} \to D_{\mathrm{dR}} / \mathrm{Fil}^0 \to 0$. Different choices give heights differing by a bilinear form. For $r = 1$, this cancels in the ratio; for $r \geq 2$, the interaction between the splitting and the regulator matrix is non-trivial.

3. **The syntomic regulator (Besser):** Besser (1999) defined a $p$-adic regulator via syntomic cohomology that does not depend on a choice of splitting. The comparison:
$$\operatorname{reg}_{\mathrm{syn}} : K_2(E) \to H^2_{\mathrm{syn}}(E/\mathbb{Z}_p, 2)$$
is expected to give a canonical $p$-adic height. However, computing $\operatorname{reg}_{\mathrm{syn}}$ explicitly for specific curves is not yet practical.

### BSD Connection

The complex leading-term comparison is the bridge between classical BSD and $p$-adic BSD. If both are true, then:
$$\frac{L^{(r)}(E, 1)}{r! \cdot \Omega_E^+ \cdot R_E} = \frac{|\Sha| \cdot \prod c_v}{|E(\mathbb{Q})_{\mathrm{tors}}|^2}$$
$$\frac{L_p^{(r)}(E, 0)}{r! \cdot R_p(E)} = \frac{|\Sha[p^\infty]| \cdot \prod c_v^{(p)} \cdot \mathcal{E}_p}{|E(\mathbb{Q})_{\mathrm{tors}}|_p^2}$$
together with the comparison formula, determines $|\Sha|$ from $|\Sha[p^\infty]|$ and the prime-to-$p$ part of $|\Sha|$ from the $L$-value. This is the key step for extracting the *full* $|\Sha|$ (not just the $p$-part) from $p$-adic methods.

---

## Direction 43: Finite Prime Support for Sha

### Status Assessment

**Open.** No proof exists that $\Sha(E/\mathbb{Q})[p^\infty] = 0$ for all sufficiently large $p$ for a *single* fixed elliptic curve $E/\mathbb{Q}$. This is a question about uniformity: given $E$, bound the set of "exceptional" primes $p$ for which $\Sha[p^\infty] \neq 0$.

### Precise Statement

**Conjecture (Finite Support).** For any elliptic curve $E/\mathbb{Q}$, the set
$$\mathcal{S}(E) = \{ p \text{ prime} : \Sha(E/\mathbb{Q})[p^\infty] \neq 0 \}$$
is finite. Moreover, there should exist a bound $\mathcal{S}(E) \subseteq \{ p : p \leq C(E) \}$ where $C(E)$ depends on $E$.

**Stronger Conjecture (Uniform Bound).** There exists a function $C: \mathbb{R}_{>0} \times \mathbb{Z}_{>0} \to \mathbb{R}_{>0}$ such that for all $E/\mathbb{Q}$ with conductor $N \leq X$ and $|\Delta_E| \leq Y$:
$$\mathcal{S}(E) \subseteq \{ p : p \leq C(X, Y) \}$$

### What Is Known

1. **$\Sha[p^\infty]$ is finite for each $p$** (conditional on finiteness of $\Sha$): If $\Sha$ is finite (a consequence of BSD), then $\Sha[p^\infty] \neq 0$ for only finitely many $p$ (trivially: $\Sha$ is a finite group, so it has finitely many prime-power torsion components).

2. **For $p \gg N_E$ (large relative to the conductor):** The residual representation $E[p]$ is often irreducible (by Serre's result: for all but finitely many $p$, $E[p]$ is irreducible). Moreover, for large $p$, $a_p(E)$ satisfies Hasse's bound $|a_p| \leq 2\sqrt{p}$, so $a_p \not\equiv p + 1 \pmod{p}$ automatically. This means the Skinner–Urban hypotheses hold for all sufficiently large $p$, yielding $\Sha[p^\infty] = 0$ under the main conjecture.

3. **Conditional result (Skinner–Urban + finiteness of $\Sha$).** Assume:
   - The Iwasawa main conjecture holds for $E$ at $p$ (Skinner–Urban).
   - $\Sha(E/\mathbb{Q})$ is finite.
   - $E[p]$ is irreducible.
   - $p \nmid 6N_E$ and $a_p \not\equiv p + 1 \pmod{p}$.
   
   Then $\Sha[p^\infty] = 0$. For all sufficiently large $p$, the last two conditions hold automatically (by Hasse's bound and Serre's irreducibility theorem). So $\Sha[p^\infty] = 0$ for all $p \gg_E 0$.

4. **Unconditional: the set $\{p : \Sha[p^\infty] \neq 0\}$ has density 0.** This follows from the work of Helfgott (2003) on the distribution of $a_p$ modulo $p$, combined with the fact that for density-1 sets of primes, the Skinner–Urban conditions hold.

### The Key Problem: Making It Effective

The conditional result above shows that $\Sha[p^\infty] = 0$ for all $p \gg_E 0$, but the implicit constant depends on:
1. The Serre irreducibility bound: $E[p]$ is irreducible for $p > C_1(E)$ (effective but large).
2. The Hasse bound: $|a_p| \leq 2\sqrt{p} < p$ for $p > 4$ (trivially effective).
3. The condition $p \nmid 6N_E$ (trivially effective: $p > N_E$ suffices).

**The effective Serre bound.** By a result of Hindry (1988, conditional on GRH): $E[p]$ is irreducible for all $p > C \cdot (\log N_E)^2$. Unconditionally, by Bilu–Parent–Rebolledo (2013): $E[p]$ is irreducible for $p > 73$ (for non-CM curves) or $p > 5$ (for CM curves, with explicit exceptions).

**Thus (conditional on GRH + finiteness of $\Sha$):**
$$\mathcal{S}(E) \subseteq \{ p : p \leq C \cdot (\log N_E)^2 \}$$

**Unconditionally (conditional only on finiteness of $\Sha$):**
$$\mathcal{S}(E) \subseteq \{ p : p \leq \max(73, N_E) \}$$

### What Global Object Could Bound the Exceptional Primes?

The exceptional primes are constrained by:

1. **The $L$-function $L(E, s)$.** The $L$-value $L(E, 1)$ (or $L^{(r)}(E, 1)$ for positive rank) encodes the product $\prod c_v \cdot |\Sha| / |E(\mathbb{Q})_{\mathrm{tors}}|^2$ by BSD. The $p$-adic valuation $v_p(L^{(r)}(E, 1) / \Omega_E R_E)$ is the order of $\Sha[p^\infty]$ (modulo $p$-parts of $c_v$ and torsion). For $p \gg_E 0$, this valuation is 0, so $\Sha[p^\infty] = 0$.

2. **The conductor $N_E$.** All arithmetic of $E$ is governed by $N_E$. The set $\mathcal{S}(E)$ should be bounded by a function of $N_E$ alone.

3. **The discriminant $\Delta_E$.** The minimal discriminant controls the bad reduction. The primes $p$ for which $E$ has bad reduction are exactly $p \mid N_E$, and for these, the Tamagawa number $c_p$ is bounded by $v_p(\Delta_E)$.

4. **The modular form $f_E$.** The Fourier coefficients $a_n$ of $f_E$ encode all arithmetic information. The prime $p \in \mathcal{S}(E)$ implies a congruence $a_\ell \equiv \sigma_1(\ell) \pmod{p}$ for many primes $\ell$ (coming from the Eisenstein ideal). The density of such congruences is controlled by the level $N_E$ and the weight.

### Obstacles

1. **Unconditional finiteness of $\Sha$.** The above argument assumes $\Sha$ is finite, which is itself unproven in general. Without this, one cannot conclude $\Sha[p^\infty] = 0$ for large $p$ even conditionally on the main conjecture.

2. **Effective constants.** The Bilu–Parent–Rebolledo bound ($p > 73$) is effective but does not account for the additional Skinner–Urban conditions (non-anomalousness, $\mu = 0$). Making all constants effective requires:
   - Effective GRH-dependent bounds for the distribution of $a_p \pmod{p}$.
   - Effective bounds for the $\mu$-invariant (currently known only for very specific curves).

3. **The $p \mid N_E$ case.** For primes of bad reduction ($p \mid N_E$), the Skinner–Urban machinery does not apply directly. These primes need separate treatment (via the Cassels–Tate pairing or Néron model analysis).

### BSD Connection

If $\Sha[p^\infty] = 0$ for all $p > C(E)$, then the $p$-part of BSD is automatically satisfied for all $p > C(E)$: the $p$-adic $L$-function's leading coefficient equals the $p$-adic regulator times Tamagawa factors (since $\Sha[p^\infty] = 1$). This reduces the full $p$-part of BSD to finitely many primes, each of which can in principle be checked computationally.

---

## Direction 44: Remove One Hypothesis from Skinner–Urban

### Status Assessment

**Focused research target.** The Skinner–Urban (2014) theorem proves the Iwasawa Main Conjecture for $E/\mathbb{Q}$ at an ordinary prime $p$ under several hypotheses. We analyze one hypothesis in detail and trace exactly where it is used in the proof.

### The Skinner–Urban Hypotheses

**Theorem (Skinner–Urban 2014).** Let $E/\mathbb{Q}$ be an elliptic curve, $p \geq 5$ a prime. Assume:

**(SU1)** $E$ has good ordinary reduction at $p$.
**(SU2)** $E[p]$ is an irreducible $G_{\mathbb{Q}}$-representation.
**(SU3)** Either $E(\mathbb{Q})[p] \neq 0$ or $a_p \not\equiv p + 1 \pmod{p^2}$ (the "non-Eisenstein" condition).
**(SU4)** The Iwasawa $\mu$-invariant $\mu(E/\mathbb{Q}_\infty) = 0$.

Then:
$$\operatorname{char}_{\Lambda}\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^{\vee}\bigr) = \bigl(L_p(E, T)\bigr)$$

### Focus: Hypothesis (SU2) — Irreducibility of $E[p]$

**Why this hypothesis:** (SU2) is the most natural candidate for removal because:
- It fails only for a *finite* set of primes $p$ for any fixed $E$ (by Serre's open image theorem for non-CM curves).
- For CM curves, $E[p]$ is reducible for all $p$ that split in the CM field.
- The reducible case is the one where the Euler system machinery (Kato) fails most visibly.

### Where (SU2) Is Used in the Proof

**Step 1: Selmer group is $\Lambda$-cotorsion.** The irreducibility of $E[p]$ ensures that $H^0(\mathbb{Q}, E[p^\infty]) = 0$ (no rational $p$-power torsion points, unless $E(\mathbb{Q})[p] \neq 0$ which is handled by (SU3)). This implies $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^{\vee}$ is a torsion $\Lambda$-module, which is required for the characteristic ideal to be defined.

*Without (SU2):* If $E[p]$ is reducible, say $E[p]$ fits in $0 \to \mu_p \to E[p] \to \mathbb{Z}/p \to 0$, the Selmer group may not be $\Lambda$-torsion. Instead, it could have $\Lambda$-rank $> 0$. The main conjecture must then be reformulated (as a statement about the characteristic ideal of the torsion submodule, or via Greenberg's $\Sigma$-Selmer groups).

**Step 2: The Eisenstein ideal.** Skinner–Urban use the *Eisenstein ideal* $\mathfrak{I} \subset \mathbf{T}$ (the Hecke algebra acting on modular forms of level $Np$) to construct congruences between the modular form $f_E$ and Eisenstein series. The ideal $\mathfrak{I}$ is defined by:
$$\mathfrak{I} = (T_\ell - 1 - \ell : \ell \nmid Np) + (U_q - 1 : q \mid N) + (U_p - a_p)$$

The key property: $\mathbf{T} / \mathfrak{I} \cong \mathbb{Z}/p$ (the Eisenstein quotient). The irreducibility of $E[p]$ is used to show that the Hecke algebra $\mathbf{T}$ acting on $S_2(\Gamma_0(Np))$ is Gorenstein (or at least has controlled singular locus), which is needed for the $\mathfrak{I}$-adic completion argument.

*Without (SU2):* When $E[p]$ is reducible, the Hecke algebra $\mathbf{T}$ is not Gorenstein at $\mathfrak{I}$: there are extra congruences between $f_E$ and Eisenstein series that come from the reducible structure. This creates "pseudo-null" submodule contributions to $\mathfrak{X}_\infty$ that are not detected by the $p$-adic $L$-function.

**Step 3: The "congruence module" argument.** The proof identifies:
$$\operatorname{char}_{\Lambda}(\mathfrak{X}_\infty^{\mathrm{div}}) \stackrel{!}{=} \mathfrak{I} \cdot \Lambda = (L_p(E, T))$$
via a comparison of the congruence module $\eta_{\mathfrak{I}} := \mathfrak{I} / \mathfrak{I}^2$ with the characteristic ideal. The irreducibility of $E[p]$ ensures that $\eta_{\mathfrak{I}}$ is cyclic (generated by a single element), which is used to identify it with the $p$-adic $L$-function.

*Without (SU2):* The congruence module $\eta_{\mathfrak{I}}$ can be non-cyclic, and the identification with $L_p(E, T)$ fails. The correction term is a *congruence module* $\mathfrak{C}$ that measures the failure of Gorensteinness:
$$\operatorname{char}_{\Lambda}(\mathfrak{X}_\infty^{\mathrm{div}}) = (L_p(E, T)) \cdot \mathfrak{C}^{-1}$$
where $\mathfrak{C}$ is an explicit ideal of $\Lambda$ that depends on the reducible structure of $E[p]$.

**Step 4: Ihara's lemma.** The Skinner–Urban argument uses Ihara's lemma for the Shimura curve $X_0^D(N)$ (where $D$ is the discriminant of the quaternion algebra ramified at $p$ and $\infty$). Ihara's lemma asserts that the map:
$$S_2(\Gamma_0(N)) \oplus S_2(\Gamma_0(N)) \to S_2(\Gamma_0(Np))$$
given by $f \mapsto (f, f | U_p)$ is injective modulo Eisenstein series. Irreducibility of $E[p]$ is used to ensure that $f_E$ does not lie in the kernel.

### Can (SU2) Be Weakened or Removed?

**Partial results:**

1. **Skinner (2014), reducible case:** When $E[p]$ has a $G_{\mathbb{Q}}$-stable line (i.e., $E[p]$ fits in $0 \to \mu_p \to E[p] \to \mathbb{Z}/p \to 0$), the main conjecture can be proved under the additional hypothesis that the extension class $[E[p]] \in H^1(\mathbb{Q}, \mu_p)$ is "non-trivial in a suitable sense." This covers many curves with reducible $E[p]$.

2. **Greenberg's $\Sigma$-Selmer groups:** By modifying the local conditions at primes where $E$ has bad reduction (adding an auxiliary set $\Sigma$), Greenberg defines Selmer groups $\operatorname{Sel}_{p^\infty}^\Sigma(E/\mathbb{Q})$ that are $\Lambda$-cotorsion even when $E[p]$ is reducible. The main conjecture for $\operatorname{Sel}^\Sigma$ may be easier to prove.

3. **Kurihara's approach (2002):** For the case $E(\mathbb{Q})[p] \neq 0$ (which is a special case of reducible $E[p]$ where the stable line corresponds to a rational $p$-torsion point), Kurihara proved the main conjecture under the hypothesis $a_p \not\equiv 1 \pmod{p}$. This uses the structure of the Eisenstein ideal more directly and avoids some of the Gorensteinness issues.

4. **The $p = 2, 3$ case:** Even with (SU2), the theorem excludes $p = 2, 3$ because Ihara's lemma fails at small primes. Removing this restriction requires a fundamentally different proof that avoids Ihara's lemma entirely. The $p$-adic Langlands program (Emerton) may eventually provide such a proof.

### What Would Be Needed for Full Removal

To remove (SU2) completely, one would need:

1. **A reformulation of the main conjecture** for non-$\Lambda$-torsion Selmer groups (using Fitting ideals instead of characteristic ideals, as in the work of Burns–Kurihara–Sano).

2. **A Gorensteinness replacement:** Instead of requiring $\mathbf{T}$ to be Gorenstein, one needs a bound on the *failure* of Gorensteinness (the congruence module $\mathfrak{C}$) in terms of computable invariants of $E$.

3. **A new approach to Ihara's lemma** that works at all primes, including $p = 2, 3$. This is one of the major open problems in the Langlands program.

### BSD Connection

Removing (SU2) would extend the $p$-part of BSD (via the main conjecture) to *all* ordinary primes $p$, including those where $E[p]$ is reducible. Since reducible $E[p]$ occurs for a density-zero set of primes, the gain is primarily theoretical: it would mean that for a fixed curve $E$, the $p$-part of BSD holds for *all* ordinary primes $p \geq 5$, not just those with irreducible $E[p]$.

For the benchmark curve 389.a1, the irreducibility of $E[p]$ has been checked computationally for all $p \leq 1000$, so (SU2) is not an obstruction in practice. The theoretical removal of (SU2) would, however, strengthen the applicability of the main conjecture to CM curves and to arithmetic families where reducibility is systematic.

---

## Summary Table

| Direction | Statement | Status | Key Obstacle |
|-----------|-----------|--------|-------------|
| 41: Higher-rank p-converse | $\operatorname{corank} \geq r \Rightarrow \operatorname{ord} L \geq r$ | Open for $r \geq 2$ (non-CM) | No higher Euler system known; generalized Kato class non-vanishing unknown |
| 42: Leading-term comparison | $\frac{L^{(r)}/r!}{L_p^{(r)}/r!} = (\text{interpolation factor})$ | Known for $r \leq 1$; open for $r \geq 2$ | Splitting of Hodge filtration; $p$-adic period for $r \geq 2$ |
| 43: Finite support for Sha | $\Sha[p^\infty] = 0$ for $p \gg_E 0$ | Conditional on finiteness of $\Sha$ | Requires unconditional finiteness of $\Sha$; effective bounds needed |
| 44: Remove (SU2) | Main conjecture without irreducibility of $E[p]$ | Partial (special cases) | Gorensteinness of Hecke algebra fails; Ihara's lemma at small primes |
