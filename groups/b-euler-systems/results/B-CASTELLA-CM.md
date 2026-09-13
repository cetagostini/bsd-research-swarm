# B-CASTELLA-CM: Castella's Generalised Kato Classes and Rank Two Results

## Direction ID and Title
B-CASTELLA-CM — Castella's Theorem on Generalised Kato Classes for CM Elliptic Curves of Rank 2

## References
- Castella, F. "Generalised Kato classes on CM elliptic curves of rank 2." *American J. Math.* (to appear). [arXiv:2204.09608](https://arxiv.org/abs/2204.09608)
- Castella, F. "Nonvanishing of generalised Kato classes and Iwasawa main conjectures." [arXiv:2312.01481](https://arxiv.org/abs/2312.01481), proceedings for Bertolini's 60th birthday.
- Castella, F., Hsieh, M.-L. "Nonvanishing of generalised Kato classes and Iwasawa main conjectures." (CH22, first cases in non-CM).
- Darmon, H., Rotger, V. "Diagonal cycles and Euler systems I." *Ann. of Math.* (2017). (DR17, construction of diagonal cycle classes)
- Darmon, H., Rotger, V. "Elliptic curves of rank two and generalised Kato classes." *Math. Proc. Cambridge Philos. Soc.* (2016). (DR16, conjecture formulation)

---

## 1. Castella's Theorem Statement (Exact)

### 1.1 Main Theorem (CM Case, arXiv:2204.09608)

**Theorem (Castella).** Let $E/\mathbf{Q}$ be an elliptic curve with **complex multiplication** by an imaginary quadratic field $K$, and let $p \geq 5$ be a prime such that:
- $p$ is a prime of **good ordinary reduction** for $E$,
- $p$ **splits** in $K$ (i.e., $p\mathscr{O}_K = \mathfrak{p}\bar{\mathfrak{p}}$).

Suppose that $L(E, s)$ vanishes at $s = 1$ and has sign $+1$ in its functional equation, so in particular $\operatorname{ord}_{s=1} L(E, s) \geq 2$.

Then there exists a **generalised Kato class**
$$\kappa_p \in \operatorname{Sel}(\mathbf{Q}, V_p E)$$
satisfying the following **rank-two analogue of Kolyvagin's theorem**:

**(Forward direction — Theorem A).** If $\kappa_p \neq 0$, then
$$\dim_{\mathbf{Q}_p} \operatorname{Sel}(\mathbf{Q}, V_p E) = 2.$$

**(Converse direction — Theorem B).** If $\dim_{\mathbf{Q}_p} \operatorname{Sel}(\mathbf{Q}, V_p E) = 2$, then $\kappa_p \neq 0$ **if and only if** the restriction (localisation) map
$$\operatorname{loc}_p : \operatorname{Sel}(\mathbf{Q}, V_p E) \longrightarrow E(\mathbf{Q}_p) \hat{\otimes} \mathbf{Q}_p$$
is nonzero, where $E(\mathbf{Q}_p) \hat{\otimes} \mathbf{Q}_p = \varprojlim_n E(\mathbf{Q}_p)/p^n E(\mathbf{Q}_p) \otimes_{\mathbf{Z}_p} \mathbf{Q}_p$.

### 1.2 Hypotheses Summary

| Condition | Requirement | Purpose |
|-----------|-------------|---------|
| CM | $E$ has CM by imaginary quadratic $K$ | Anticyclotomic Iwasawa theory applies |
| Good ordinary | $p \geq 5$, $E$ has good ordinary reduction at $p$ | $p$-adic Hodge theory, Hida families exist |
| Split prime | $p$ splits in $K$ | Anticyclotomic tower is "deep enough" |
| Analytic rank $\geq 2$ | $L(E, 1) = 0$, root number $+1$ | Class lives in rank $\geq 2$ Selmer group |

### 1.3 What the Theorem Achieves

The theorem is a **rank-two analogue** of the classical Kolyvagin result:
- **Kolyvagin (rank 0–1):** Heegner point $\neq 0$ $\Longrightarrow$ $\dim \operatorname{Sel} = 1$ and $|\text{Ш}| < \infty$.
- **Castella (rank 2):** Generalised Kato class $\neq 0$ $\Longrightarrow$ $\dim \operatorname{Sel} = 2$.

The converse is more subtle: in rank 2, the nonvanishing of $\kappa_p$ depends on whether the Selmer classes are "visible" at $p$ (i.e., whether $\operatorname{loc}_p$ is nonzero). This condition is automatic when Sha has no $p$-torsion, but is an additional hypothesis in general.

---

## 2. The Generalised Kato Class

### 2.1 Construction

The generalised Kato class $\kappa_p$ is constructed via a **modified Darmon–Rotger procedure**. The construction proceeds in several steps:

**Step 1: Triple product setup.** Choose a triple of Hida families $(\boldsymbol{\varphi}, \boldsymbol{g}, \boldsymbol{h})$ where:
- $\boldsymbol{\varphi}$ is the Hida family passing through $f_E$ (the weight-2 eigenform associated to $E$),
- $\boldsymbol{g}$ and $\boldsymbol{h}$ are auxiliary Hida families of weight 1 forms (associated to Artin representations $\varrho_1$ and $\varrho_2$ respectively).

The tame characters satisfy $\chi_\varphi \chi_g \chi_h = \omega^{2a}$ for some $a \in \mathbf{Z}$, where $\omega$ is the Teichmüller character.

**Step 2: Big diagonal class.** By the work of Darmon–Rotger and Bertolini–Seveso–Venerucci, there exists a **big diagonal class**
$$\kappa(\boldsymbol{\varphi}, \boldsymbol{g}, \boldsymbol{h}) \in H^1(\mathbf{Q}, \mathbf{V}^\dagger)$$
where $\mathbf{V}^\dagger$ is a self-dual twist of the triple tensor product of the Galois representations attached to the three families. This class is constructed by **$p$-adic interpolation** of the Abel–Jacobi images of generalised Gross–Kudla–Schoen diagonal cycles on triple products of modular curves.

**Step 3: Arithmetic specialisation.** Specialise the families at an **arithmetic point** $\underline{Q} = (Q_0, Q_1, Q_2)$ in the "unbalanced" region where $k_{Q_0} \geq k_{Q_1} + k_{Q_2}$ (weights $(2, 1, 1)$), obtaining
$$\kappa_p(f, g, h) \in H^1(\mathbf{Q}, V_p E \otimes \varrho), \quad \varrho := \varrho_1 \otimes \varrho_2.$$

**Step 4: Projection to $V_p E$.** When $\varrho_2 \simeq \varrho_1^\vee$ (so that $\varrho$ contains the trivial representation), one has
$$V_\varrho \simeq \mathbf{Q}_p \oplus \operatorname{ad}^0(V_{\varrho_1}).$$
Project $\kappa_p(f, g, h)$ along the trivial factor to obtain
$$\kappa_p(E) \in H^1(\mathbf{Q}, V_p E).$$

**Step 5: CM modification.** In the CM case, Castella modifies this construction using the CM structure. The key idea is to choose $\varrho_1$ to be **induced from a character of the CM field** $K$, which makes the Artin formalism produce the correct L-function factorisation:
$$L(E \otimes \varrho, s) = L(E, s) \cdot L(E \otimes \operatorname{ad}^0(\varrho_1), s).$$

When $L(E \otimes \operatorname{ad}^0(\varrho_1), 1) \neq 0$ (which holds by choosing $\varrho_1$ appropriately), the projection $\kappa_p(E)$ is the desired class.

### 2.2 Properties of $\kappa_p$

1. **Selmer condition.** When $L(E \otimes \varrho, 1) = 0$, the class $\kappa_p(f, g, h)$ satisfies the **crystalline (Bloch–Kato) Selmer condition** at $p$. This follows from the explicit reciprocity law of Darmon–Rotger and Bertolini–Seveso–Venerucci.

2. **Non-crystalline when $L$-value nonzero.** Conversely, when $L(E \otimes \varrho, 1) \neq 0$, the class $\kappa_p(f, g, h)$ is **non-crystalline** at $p$. This is the key input: the nonvanishing of a central $L$-value forces the class out of the crystalline Selmer subgroup.

3. **Relation to $L$-values.** The class $\kappa_p$ is related to $L(E \otimes \varrho, 1)$ via the **explicit reciprocity law**: roughly, $\kappa_p = 0$ if and only if $L(E \otimes \varrho, 1) \neq 0$ (in the appropriate sense).

4. **Invariance.** The construction is (up to explicit scalars) independent of the choice of auxiliary forms $g, h$, provided the $\operatorname{ad}^0$ $L$-value is nonzero.

### 2.3 The Diagonal Cycle Main Conjecture

Castella's proof exploits a deep connection to a **main conjecture in anticyclotomic Iwasawa theory**. Specifically:

**Conjecture (Big diagonal class main conjecture, Conjecture A of [2204.09608]).** Assume the local root number condition $\varepsilon_\ell(\mathbf{V}_{\underline{Q}}^\dagger) = +1$ for all primes $\ell \mid N_\varphi N_g N_h$. Then the characteristic ideal of the Selmer group of the big diagonal class equals the ideal generated by the $p$-adic $L$-function:
$$\operatorname{char}_\Lambda\bigl(\operatorname{Sel}(\mathbf{Q}, \mathbf{V}^\dagger)^\vee\bigr) = (\mathcal{L}_p(\boldsymbol{\varphi}, \boldsymbol{g}, \boldsymbol{h})).$$

In the CM case, Castella **proves** a sufficient specialisation of this conjecture by linking it to the anticyclotomic Iwasawa main conjecture (which is known in the CM setting by work of Bertolini–Darmon, Chida–Hsieh, and others).

---

## 3. Applicability to 389.a1

### 3.1 The Curve 389.a1

| Property | Value |
|----------|-------|
| Label | 389.a1 |
| Equation | $y^2 + y = x^3 + x^2 - 2x$ |
| Conductor | $N = 389$ (prime) |
| CM | **No** |
| Analytic rank | **2** |
| Root number | $+1$ |
| Torsion | Trivial: $E(\mathbf{Q})_{\text{tors}} = \{O\}$ |
| $\operatorname{Ш}$ | Trivial: $|\text{Ш}(E/\mathbf{Q})| = 1$ |
| Mordell–Weil | $E(\mathbf{Q}) \simeq \mathbf{Z}^2$ |
| $L''(E,1)/2!$ | $\neq 0$ |

### 3.2 Does Castella's CM Theorem Apply to 389.a1?

**No.** Castella's theorem (arXiv:2204.09608) **requires** the elliptic curve to have complex multiplication. The curve 389.a1 does **not** have CM, so the theorem does not apply directly.

More precisely, Castella's proof relies on the following CM-specific inputs:
1. **Anticyclotomic Iwasawa theory:** The proof reduces the diagonal cycle main conjecture to the **anticyclotomic Iwasawa main conjecture** for the CM field $K$. This reduction uses the CM structure essentially — it exploits the factorisation of Galois representations over $K$.
2. **Splitting of Galois representations:** In the CM case, $V_p E$ splits over $K$ as a sum of characters, which simplifies the Selmer group analysis.
3. **Known Iwasawa theory:** The anticyclotomic main conjecture is known for CM fields (by work of Rubin, Bertolini–Darmon, Chida–Hsieh), providing the key equality $\mathcal{Z} = \operatorname{char}(\operatorname{Sel}^\vee)$.

None of these ingredients are available for the non-CM curve 389.a1.

### 3.3 What the Darmon–Rotger Construction Gives for 389.a1

Despite Castella's CM theorem not applying, the **underlying construction** (the Darmon–Rotger generalised Kato class) does exist for any elliptic curve $E/\mathbf{Q}$ of positive even analytic rank:

For 389.a1, choose $\varrho_1, \varrho_2$ to be odd irreducible 2-dimensional Artin representations with $\varrho_2 \simeq \varrho_1^\vee$. Then the generalised Kato class
$$\kappa_p(389a1) \in \operatorname{Sel}(\mathbf{Q}, V_p E)$$
exists for any prime $p > 3$ of good ordinary reduction (e.g., $p = 5, 7, 11, \ldots$).

**What is known for this class:**
- $\kappa_p(389a1) = 0$ $\Longrightarrow$ nothing (no converse without additional hypotheses).
- $\kappa_p(389a1) \neq 0$ $\Longrightarrow$ $\dim \operatorname{Sel}(\mathbf{Q}, V_p E) = 2$ (this implication was proved by Castella–Hsieh (CH22) in the non-CM case under certain hypotheses on $\varrho_1$).

**What is NOT known:**
- Whether $\kappa_p(389a1) \neq 0$ in the first place.
- The full equivalence $\kappa_p \neq 0 \iff \dim \operatorname{Sel} = 2$ (only one direction is known conditionally).

### 3.4 Computational Expectation

For 389.a1, we expect:
- $\operatorname{Sel}(\mathbf{Q}, V_5 E)$ is 2-dimensional (matching the rank 2).
- The generalised Kato class $\kappa_5(389a1) \neq 0$ (since $\text{Ш}[5^\infty] = 0$, the localisation map $\operatorname{loc}_5$ is nonzero, and the Selmer group is spanned by the Mordell–Weil generators).
- The BSD conjecture predicts: $L''(E,1)/2! = |\text{Ш}| \cdot \operatorname{Reg}(E) \cdot \prod c_v / |E(\mathbf{Q})_{\text{tors}}|^2$, which with $|\text{Ш}| = 1$ and trivial torsion gives $L''(E,1)/2! = \operatorname{Reg}(E) \cdot \prod c_v$.

**Status:** Open. Proving $\kappa_5(389a1) \neq 0$ unconditionally would be a major breakthrough — it would establish the existence of non-torsion Selmer classes for this curve via $p$-adic methods.

---

## 4. Castella's Non-CM Discussion (arXiv:2312.01481)

### 4.1 What Castella Proves for Non-CM Curves

In [2312.01481], Castella extends his CM method to the non-CM setting. The main result is:

**Theorem (Castella, Theorem 5.2.3 of [2312.01481]).** Let $E/\mathbf{Q}$ be an elliptic curve (not necessarily CM) and let $p > 3$ be a prime of good ordinary reduction. Suppose that $\operatorname{ord}_{s=1} L(E, s) \geq 2$ and the root number is $+1$. Let $\kappa_p(E) \in \operatorname{Sel}(\mathbf{Q}, V_p E)$ be the generalised Kato class obtained from the Darmon–Rotger construction.

**(Forward direction):**
$$\kappa_p(E) \neq 0 \quad\Longrightarrow\quad \dim_{\mathbf{Q}_p} \operatorname{Sel}(\mathbf{Q}, V_p E) = 2.$$

**(Converse — if and only if):** Assuming $\dim_{\mathbf{Q}_p} \operatorname{Sel}(\mathbf{Q}, V_p E) = 2$, then $\kappa_p(E) \neq 0$ **if and only if** the restriction map
$$\operatorname{loc}_p : \operatorname{Sel}(\mathbf{Q}, V_p E) \longrightarrow E(\mathbf{Q}_p) \hat{\otimes} \mathbf{Q}_p$$
is nonzero.

This gives a **new proof** of the Castella–Hsieh result [CH22], but with a sharper converse: [CH22] required the additional hypothesis $(\operatorname{Loc}_p)$: $\operatorname{Sel}(\mathbf{Q}, V_p E) \neq \ker(\operatorname{loc}_p)$, while [2312.01481] shows this hypothesis is not only sufficient but also **necessary** for the nonvanishing of $\kappa_p(E)$.

### 4.2 Obstacles for Full Non-CM Results

The full Darmon–Rotger conjecture (equation (1.2) of [2312.01481]):
$$\kappa_p(E) \neq 0 \quad\overset{?}{\Longleftrightarrow}\quad \dim_{\mathbf{Q}_p} \operatorname{Sel}(\mathbf{Q}, V_p E) = 2$$
remains **open** in the non-CM case. The key obstacles are:

1. **Anticyclotomic Iwasawa main conjecture (non-CM):** In the CM case, Castella reduces to the anticyclotomic main conjecture for the CM field $K$, which is known. In the non-CM case, the analogue requires a main conjecture for **non-abelian** imaginary quadratic extensions, which is **not known** in general.

2. **$p$-adic height pairing:** The proof in the CM case uses the anticyclotomic $p$-adic height, whose properties are well-understood due to the CM structure. In the non-CM case, one needs analogous results for the **Greenberg–Bertolini $p$-adic height** on generalised Kato classes, which requires control of the Selmer group that is itself part of what one wants to prove.

3. **Local condition at $p$:** The condition $(\operatorname{Loc}_p)$ (or its strengthened form: $\operatorname{loc}_p \neq 0$) is a **genuine obstruction**. When $\operatorname{Ш}[p^\infty] \neq 0$, it is conceivable that the Selmer group is 2-dimensional but entirely contained in $\ker(\operatorname{loc}_p)$, in which case $\kappa_p(E) = 0$ despite $\dim \operatorname{Sel} = 2$.

4. **Irreducibility and modularity:** The non-CM proof requires that the residual representation $\bar{\rho}_{E,p}$ be irreducible, which is a mild but necessary hypothesis. For specific curves, this can be verified.

### 4.3 Partial Results Available

The following partial results are known for the non-CM case:

| Result | Status | Conditions |
|--------|--------|------------|
| $\kappa_p(E) \neq 0 \Rightarrow \dim \operatorname{Sel} = 2$ | **Proved** (CH22, new proof in 2312.01481) | $E/\mathbf{Q}$, $p > 3$ good ordinary, $\bar{\rho}_{E,p}$ irreducible |
| $\dim \operatorname{Sel} = 2$ and $\operatorname{loc}_p \neq 0 \Rightarrow \kappa_p(E) \neq 0$ | **Proved** (new in 2312.01481) | Same as above |
| $\operatorname{loc}_p \neq 0$ is **necessary** for $\kappa_p(E) \neq 0$ | **Proved** (new in 2312.01481) | Same as above |
| Full equivalence (1.2) | **Open** | Would require resolving $(\operatorname{Loc}_p)$ |
| $\kappa_p(E) \neq 0$ unconditionally | **Open** for specific curves | Would imply rank 2 BSD |

---

## 5. Connection to Kim's Theorem

### 5.1 Overview

The relationship between Kim's theorem (visibility of Sha) and Castella's theorem is one of **complementary approaches to the same problem**: constructing non-torsion classes in the rank-2 Selmer group.

| Aspect | Castella (Generalised Kato) | Kim (Visibility) |
|--------|----------------------------|-------------------|
| **Object constructed** | Class $\kappa_p \in \operatorname{Sel}(\mathbf{Q}, V_p E)$ | Geometric embedding of Sha into an abelian variety quotient |
| **Method** | $p$-adic interpolation of diagonal cycles | Modular parametrisation and intersection theory |
| **Hypotheses** | CM required (or $\varrho_1$ induced from quadratic field) | Curves of specific conductors where modular degree is understood |
| **Conclusion** | $\kappa_p \neq 0 \Rightarrow \dim \operatorname{Sel} = 2$ | Sha classes are "visible" in modular quotients |
| **Applicability to 389.a1** | NOT directly (no CM) | Potentially applicable (389 is prime, modular parametrisation known) |

### 5.2 How Their Results Complement Each Other

**Castella's contribution** provides a $p$-adic analytic criterion:
- If one can prove $\kappa_p(E) \neq 0$ (e.g., by computing the $p$-adic $L$-function to sufficient precision), then $\dim \operatorname{Sel} = 2$ follows.
- The method is **functorial**: it works for any curve satisfying the hypotheses, without explicit knowledge of the Mordell–Weil group.

**Kim's contribution** provides a geometric/structural approach:
- If one can show that Sha is "visible" in a modular quotient $J_0(N)/A$ (where $A$ is an abelian subvariety), then the Sha classes map nontrivially to the Selmer group.
- The method requires **explicit knowledge** of the modular parametrisation (degree, kernel).

**Complementarity:**
- Castella works "top-down" from $p$-adic $L$-functions; Kim works "bottom-up" from explicit geometry.
- Castella's method is strongest when the CM structure or Artin representation structure is available; Kim's is strongest when the conductor is small and the modular parametrisation is computable.
- Neither method alone resolves the rank-2 BSD conjecture for general non-CM curves.

### 5.3 Which Is More Applicable to 389.a1?

For the specific curve 389.a1 ($y^2 + y = x^3 + x^2 - 2x$, conductor 389, rank 2, non-CM):

**Castella's approach:**
- Does NOT apply directly (no CM).
- The generalised Kato class $\kappa_p(389a1)$ exists (via Darmon–Rotger) for $p = 5, 7, 11, \ldots$, but proving its nonvanishing is **open** without the CM input.
- Would require: (a) verifying the Castella–Hsieh hypotheses for a specific $\varrho_1$, or (b) a new approach to the non-CM Iwasawa main conjecture.

**Kim's approach (visibility of Sha):**
- More directly applicable to 389.a1, since 389 is a prime conductor with a well-understood modular parametrisation.
- However, 389.a1 has **trivial Sha** ($|\text{Ш}| = 1$), so the visibility mechanism has no content: there is nothing to "detect" in Sha.
- The rank-2 Mordell–Weil generators can be computed directly (and are known).

**Conclusion:** For 389.a1 specifically, neither Castella's nor Kim's theorem is the optimal approach. Since Sha is trivial and the rank is known to be 2, the BSD conjecture for 389.a1 reduces to:
1. Computing the regulator $\operatorname{Reg}(E)$ explicitly.
2. Verifying $L''(E,1)/2! = \operatorname{Reg}(E) \cdot \prod c_v$.
3. Verifying the $p$-adic analogue via the $p$-adic BSD conjecture.

The **most effective approach** for 389.a1 is direct computation (Mordell–Weil generators, regulator, $L$-values) rather than either Castella's or Kim's theoretical machinery. The theoretical results are most valuable for curves where Sha is nontrivial and/or the rank-2 generators are not known.

### 5.4 The Broader Picture

For a general non-CM rank-2 curve $E/\mathbf{Q}$ with potentially nontrivial Sha:

- **Castella's framework** (when completed to the full non-CM case) would provide the most systematic approach: construct $\kappa_p$, prove $\kappa_p \neq 0$, deduce $\dim \operatorname{Sel} = 2$.
- **Kim's framework** provides a complementary geometric detection of Sha classes.
- **The Darmon–Rotger conjecture** (equation (1.2)) remains the key open problem: establishing the equivalence $\kappa_p(E) \neq 0 \iff \dim \operatorname{Sel} = 2$ for general $E/\mathbf{Q}$.

---

## 6. Summary: Status for 389.a1

| Question | Answer |
|----------|--------|
| Does Castella's CM theorem apply? | **No** — 389.a1 is not CM |
| Does the Darmon–Rotger construction give a class? | **Yes** — $\kappa_p(389a1) \in \operatorname{Sel}(\mathbf{Q}, V_p E)$ exists |
| Is $\kappa_p(389a1) \neq 0$? | **Open** — expected yes (since $\text{Ш} = 0$, $\operatorname{loc}_p \neq 0$), but unproven |
| Does $\kappa_p \neq 0 \Rightarrow \dim \operatorname{Sel} = 2$? | **Yes** — proved by Castella–Hsieh for non-CM under mild hypotheses |
| Full equivalence (1.2)? | **Open** — requires resolving $(\operatorname{Loc}_p)$ |
| Is Kim's visibility approach applicable? | **Not needed** — Sha is trivial for 389.a1 |
| Best approach for 389.a1? | **Direct computation** (regulator, $L$-values, $p$-adic BSD) |

## 7. Classification

**Status:** Theorem (CM case, [2204.09608]); Partial Result (non-CM forward direction, [2312.01481] and [CH22]); Conjecture (full non-CM equivalence, Darmon–Rotger conjecture (1.2)).

**Key open problem:** Prove $\kappa_p(E) \neq 0$ for a specific non-CM rank-2 curve $E/\mathbf{Q}$. This would be the first unconditional construction of a non-torsion Selmer class via $p$-adic methods in the non-CM, rank-2 setting.
