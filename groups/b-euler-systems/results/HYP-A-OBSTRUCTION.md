# HYP-A-OBSTRUCTION: Obstruction Analysis for Hypothesis A

## Role and Scope

This document analyses the **earliest and most fundamental reason** Hypothesis A could fail. We focus on what could go **wrong**, not what could go right.

---

## 0. Hypothesis A (Restated)

**Hypothesis A.** For rank-2 elliptic curves $E/\mathbb{Q}$, there exists at least one admissible auxiliary construction $\mathfrak{a}$ (choice of auxiliary prime $\ell$, character $\chi$, auxiliary modular form $g$) such that the generalized Kato class
$$\kappa_{\mathfrak{a}}(E) \in \operatorname{Sel}(\mathbb{Q}, V_p E)$$
is **nonzero**.

The premise is that the space of admissible $\mathfrak{a}$ is large enough that vanishing of $\kappa_{\mathfrak{a}}(E)$ for some $\mathfrak{a}$ does not imply vanishing for all $\mathfrak{a}$. The hope is that different $\mathfrak{a}$ produce classes whose nonvanishing is controlled by **different** local or global conditions, so that the "failure locus" $\{\mathfrak{a} : \kappa_{\mathfrak{a}}(E) = 0\}$ does not exhaust the admissible set.

---

## 1. The Fundamental Obstruction: Factorization Through a Core Class

### 1.1 The Factoring Scenario

**Scenario (Core Factorization).** Suppose the generalized Kato class construction factors as

$$\kappa_{\mathfrak{a}}(E) = u_{\mathfrak{a}}(E) \cdot \kappa_{\mathrm{core}}(E)$$

where:

- $\kappa_{\mathrm{core}}(E) \in H^1_f(\mathbb{Q}, V_p E)$ is a class **independent of $\mathfrak{a}$** (i.e., depends only on $E$ and $p$),
- $u_{\mathfrak{a}}(E) \in \mathbb{Q}_p^\times$ is a scalar depending on $\mathfrak{a}$.

Then:

$$\kappa_{\mathfrak{a}}(E) = 0 \iff \kappa_{\mathrm{core}}(E) = 0 \quad (\text{for all } \mathfrak{a})$$

since $u_{\mathfrak{a}}(E)$ is a unit (in particular, nonzero). Varying $\mathfrak{a}$ produces **different nonzero scalar multiples** of the same class. The question of existence of a nonzero $\kappa_{\mathfrak{a}}(E)$ collapses to:

> **Does $\kappa_{\mathrm{core}}(E) \neq 0$?**

This is exactly the **original problem** — the nonvanishing of a single class attached to $E$ — and varying $\mathfrak{a}$ has provided no leverage whatsoever.

### 1.2 What This Means for Hypothesis A

If core factorization holds, then Hypothesis A is **equivalent** to the simpler assertion:

> There exists $E/\mathbb{Q}$ of rank 2 with $\kappa_{\mathrm{core}}(E) \neq 0$.

This is a statement about the **Darmon-Rotger conjecture** (equation (1.2) of [2312.01481]), not about any family-level phenomenon. The auxiliary data $\mathfrak{a}$ is an inert parameterization of the same class.

**Verdict:** If core factorization holds, reject Hypothesis A as **non-redundant** — it reduces to a previously open problem without added content.

---

## 2. Can Core Factorization Happen? The Structure of Castella's Construction

### 2.1 What Castella's Class Looks Like

Castella ([2312.01481]) constructs the generalized Kato class $\kappa_p(E)$ via the following steps:

**Step 1.** Choose auxiliary data $(g, h)$ where $g$ and $h$ are (Hida families of) modular forms of weight 1, with $h$ the dual of $g$ (i.e., $\rho_h \cong \rho_g^\vee$).

**Step 2.** The Beilinson-Flach element $\mathrm{BF}_{f,g,h} \in H^1(\mathbb{Q}(\mu_m), V_f \otimes V_g \otimes V_h)$ for the triple product $f \otimes g \otimes h$.

**Step 3.** Since $h$ is dual to $g$, the representation $V_g \otimes V_h \cong \operatorname{End}(V_g) \cong \mathbb{Q}_p \oplus \operatorname{ad}^0(V_g)$. Projecting along the trivial factor:
$$\pi_1: V_f \otimes V_g \otimes V_h \to V_f \cong V_p E$$

**Step 4.** The image $\pi_1(\mathrm{BF}_{f,g,h})$ defines a class
$$\kappa_{g,h}(E) \in H^1_f(\mathbb{Q}, V_p E)$$

(the Selmer condition at $p$ follows from the interpolation property of Beilinson-Flach elements when the central $L$-value $L(f \otimes g \otimes h, 1/2) = L(E, 1) \cdot L(E \otimes \operatorname{ad}^0(\rho_g), 1)$ has the appropriate vanishing/nonvanishing).

### 2.2 The Auxiliary Dependence

The class $\kappa_{g,h}(E)$ depends on $(g, h)$ through:

**(a) The projection.** The map $\pi_1: V_f \otimes V_g \otimes V_h \to V_f$ is the projection onto the **trivial isotypic component** of $V_g \otimes V_h$. This projection depends on the decomposition
$$V_g \otimes V_h \cong \mathbb{Q}_p \oplus \operatorname{ad}^0(V_g)$$
which depends on $g$ (the structure of $V_g$). However, the trivial factor $\mathbb{Q}_p$ inside $V_g \otimes V_g^\vee$ is **canonical** (given by the identity endomorphism), so the projection $\pi_1$ is independent of $g$ up to a **normalization scalar**.

**(b) The Beilinson-Flach element.** The class $\mathrm{BF}_{f,g,h}$ depends on $(f, g, h)$. The key question is: after projection to $V_f$, how does the dependence on $(g, h)$ manifest?

**(c) The explicit reciprocity law.** The norm relations for $\mathrm{BF}_{f,g,h}$ involve the Euler factors:
$$P_\ell^{f,g,h}(x) = (1 - \alpha_\ell^f x)(1 - \alpha_\ell^g x)(1 - \alpha_\ell^h x) \cdots$$
which depend on $(g, h)$.

### 2.3 The Crucial Factorization Question

**Question.** Does the projection $\pi_1(\mathrm{BF}_{f,g,h})$ factor as
$$\pi_1(\mathrm{BF}_{f,g,h}) = c(g,h) \cdot \kappa_{\mathrm{core}}(f)$$
for some scalar $c(g,h) \in \mathbb{Q}_p^\times$ and some class $\kappa_{\mathrm{core}}(f) \in H^1_f(\mathbb{Q}, V_p E)$ independent of $(g,h)$?

### 2.4 Analysis: Why Factorization Is Plausible

There are structural reasons to suspect that core factorization holds:

**Reason 1: The trivial factor is canonical.** The projection $V_g \otimes V_g^\vee \to \mathbb{Q}_p$ is the trace map $\operatorname{tr}: \operatorname{End}(V_g) \to \mathbb{Q}_p$, which is independent of $g$ (it's the canonical identification of the trivial representation inside the tensor product of a representation with its dual). So the projection step does not introduce $g$-dependence in the **map**, only in the **element being projected**.

**Reason 2: Beilinson-Flach elements have universal structure.** The Beilinson-Flach elements are constructed from **diagonal classes** $\Delta_{g,h} = \{(x, x) : x \in X_0(N)\}$ on $X_0(N) \times X_0(N)$, which depend on the pair $(g, h)$ only through the Hecke eigenvalues. When projected to the $f$-isotypic component, the image depends on the **pairing** $\langle g, h \rangle$ (the Petersson inner product) rather than on $g$ and $h$ individually.

**Reason 3: Normalization.** If one normalizes the Beilinson-Flach element by $\langle g, g \rangle^{-1}$ (the Petersson norm), the resulting class in $H^1_f(\mathbb{Q}, V_p E)$ becomes:
$$\kappa_{g,h}(E) = \frac{1}{\langle g, g \rangle} \cdot \pi_1(\mathrm{BF}_{f,g,h})$$
This normalization removes the dependence on the scaling of $g$, but it is **not** clear that it removes all dependence on the **isomorphism class** of $g$.

### 2.5 Analysis: Why Factorization Might Fail

**Reason 1: Local factors at $\ell$ genuinely differ.** For an auxiliary prime $\ell$, the Beilinson-Flach element has a **local factor at $\ell$** that depends on the eigenvalues $\alpha_\ell^g, \alpha_\ell^h$. This local factor appears multiplicatively in the global class:
$$\kappa_{\ell,g,h}(E) = \mathcal{L}_\ell(g,h) \cdot \kappa_{\mathrm{unram}}(E)$$
where $\mathcal{L}_\ell(g,h)$ depends on $\ell, g, h$ and $\kappa_{\mathrm{unram}}(E)$ is the "away-from-$\ell$" part. **If** $\mathcal{L}_\ell(g,h)$ can vanish for some $\ell$ but not all $\ell$, then varying $\ell$ is genuinely useful.

However, the scalar $\mathcal{L}_\ell(g,h)$ is typically a **unit** (nonvanishing at the relevant $p$-adic point), because:
- At good primes $\ell \nmid Np$, the Euler factor is $(1 - a_\ell/\ell) \neq 0$ for $\ell \neq p$ (and $a_\ell/\ell$ is $p$-adically small).
- At primes $\ell \mid N$, the Euler factor involves the Tamagawa factor, which is also a unit for $p \nmid N$.

**This means the local factor at $\ell$ is generically a unit, and the $\ell$-dependence does not introduce zeros.**

**Reason 2: The global L-value governs nonvanishing.** The class $\kappa_{g,h}(E)$ is related (via the explicit reciprocity law) to the value:
$$L(f \otimes g \otimes h, 1/2) = L(E, 1) \cdot L(E \otimes \operatorname{ad}^0(\rho_g), 1)$$
The factor $L(E, 1) = 0$ (since $\operatorname{ord}_{s=1} L(E, s) = 2$). The factor $L(E \otimes \operatorname{ad}^0(\rho_g), 1)$ depends on $g$ but is **expected to be nonzero** for "most" $g$ (by the nonvanishing conjecture for $L$-functions).

The question is: does the nonvanishing of $\kappa_{g,h}(E)$ depend on $L(E \otimes \operatorname{ad}^0(\rho_g), 1) \neq 0$, or on a deeper condition?

### 2.6 The Factorization Theorem (What Is Actually Known)

**Theorem (Castella, Theorem 4.1.2 of [2312.01481], in the CM case).** For $E$ with CM by $K$, and $\rho_g = \operatorname{Ind}_{G_K}^{G_\mathbb{Q}}(\chi_g)$ induced from a Hecke character $\chi_g$ of $K$:

$$\kappa_{g,h}(E) = \mathcal{L}_p^{\mathrm{anti}}(E, \chi_g) \cdot \kappa_{\mathrm{CM}}(E)$$

where:
- $\mathcal{L}_p^{\mathrm{anti}}(E, \chi_g)$ is the **anticyclotomic $p$-adic $L$-function** evaluated at $\chi_g$, which depends on $g$.
- $\kappa_{\mathrm{CM}}(E) \in H^1_f(\mathbb{Q}, V_p E)$ is a **fixed class** depending only on $E$ and $p$.

**This IS core factorization in the CM case.** The anticyclotomic $p$-adic $L$-function $\mathcal{L}_p^{\mathrm{anti}}(E, \chi_g)$ is a scalar, and $\kappa_{\mathrm{CM}}(E)$ is the core class. Varying $g$ (i.e., varying $\chi_g$) changes the scalar but not the class.

### 2.7 Consequence: Hypothesis A Fails in the CM Case

In the CM case:
$$\kappa_{g,h}(E) = 0 \iff \kappa_{\mathrm{CM}}(E) = 0$$
for **all** admissible $(g, h)$.

This means:
1. **Varying $g$ does not help.** Different $g$ produce scalar multiples of the same class.
2. **Varying $\ell$ does not help.** The auxiliary prime enters only through the local Euler factor at $\ell$, which is a unit.
3. **The question reduces to $\kappa_{\mathrm{CM}}(E) \neq 0$.**

In the CM case, Castella proves $\kappa_{\mathrm{CM}}(E) \neq 0$ using the anticyclotomic Iwasawa main conjecture (which is known for CM fields). But this proof does **not** use the variation of auxiliary data — it proves nonvanishing of the **fixed** core class directly.

**Conclusion for CM curves:** Hypothesis A is vacuously true (there exists a nonzero class) but **the method of varying $\mathfrak{a}$ was not the operative mechanism**. The nonvanishing was proved by other means.

---

## 3. The Non-CM Case: Does Factorization Hold?

### 3.1 The General Setup

For a non-CM curve $E/\mathbb{Q}$, the construction of $\kappa_{g,h}(E)$ from Beilinson-Flach elements proceeds as in §2.1. The key question is whether the factorization
$$\kappa_{g,h}(E) = c(g,h) \cdot \kappa_{\mathrm{core}}(E)$$
holds with $c(g,h) \in \mathbb{Q}_p^\times$ a unit scalar.

### 3.2 Arguments For Factorization in the Non-CM Case

**Argument 1: Motivic structure.** The Beilinson-Flach class $\mathrm{BF}_{f,g,h}$ is the image of a **motivic element** — the diagonal cycle on $X_0(N) \times X_0(N)$ — under the étale regulator. After projection to $V_f$, the motivic structure constrains the $g$-dependence. Specifically, the projection factors through the **motive** $h^1(E)$, and the motivic realization map is independent of $(g, h)$. The $g$-dependence enters only through the **period** (the comparison between Betti and de Rham cohomologies), which is a scalar.

**Argument 2: Functoriality.** The projection $\pi_1: V_f \otimes \operatorname{End}(V_g) \to V_f$ is the **counit** of the adjunction between a representation and its dual. This is a canonical map, independent of $g$. The Beilinson-Flach element, after projection, becomes a class in $H^1_f(\mathbb{Q}, V_p E)$ whose dependence on $(g, h)$ is entirely through the **normalization** (the Petersson inner product, the periods, etc.), which are scalars.

**Argument 3: The CM case is generic.** In the CM case, the factorization is a **theorem** (§2.6). The non-CM case should exhibit the same structure, because:
- The projection $\pi_1$ is the same canonical map.
- The Beilinson-Flach elements have the same motivic origin.
- The only difference is that the anticyclotomic $p$-adic $L$-function (which provides the scalar $c(g,h)$ in the CM case) is replaced by an appropriate **non-abelian** $p$-adic $L$-function.

### 3.3 Arguments Against Factorization in the Non-CM Case

**Counter-argument 1: The non-abelian $p$-adic $L$-function is not a scalar.** In the CM case, $\mathcal{L}_p^{\mathrm{anti}}(E, \chi_g)$ is a scalar (the value of a $p$-adic $L$-function at a character). In the non-CM case, the analogue would be a **$p$-adic $L$-function on a non-abelian group**, which is a function, not a scalar. The "evaluation at $g$" of this function might not factor as a product of a $g$-dependent scalar and a $g$-independent class.

**Counter-argument 2: Selmer conditions at $\ell$ interact non-trivially.** The Selmer condition at the auxiliary prime $\ell$ requires the class to be in $H^1_f(\mathbb{Q}_\ell, V_p E)$, which is the **unramified** or **flat** condition depending on $\ell$. For different $\ell$, these conditions cut out different subspaces of $H^1(\mathbb{Q}_\ell, V_p E)$. The global class $\kappa_{g,h}(E)$ must satisfy the Selmer condition at $\ell$ **and** at all other primes. Changing $\ell$ changes the Selmer condition, which could change the global class non-trivially.

However, this counter-argument is **weakened** by the fact that the Beilinson-Flach element is constructed to automatically satisfy the local conditions at $\ell$ (this is built into the definition of $\mathrm{BF}_{f,g,h}$). So the $\ell$-dependence is "pre-processed" into the construction, and the global class adapts to the local condition at $\ell$ by construction.

### 3.4 The Local Factor at $\ell$: Genuine or Trivial?

**Detailed analysis.** The Beilinson-Flach element $\mathrm{BF}_{f,g,h}$ at the auxiliary prime $\ell$ has a local factor:
$$\mathcal{L}_\ell(f,g,h) = (1 - \beta_\ell^f \operatorname{Frob}_\ell^{-1}) \cdot (1 - \alpha_\ell^g \operatorname{Frob}_\ell^{-1}) \cdot (1 - \alpha_\ell^h \operatorname{Frob}_\ell^{-1})$$
(up to normalization), where $\beta_\ell^f, \alpha_\ell^g, \alpha_\ell^h$ are eigenvalues of Frobenius at $\ell$.

After projection to $V_f$ (the trivial factor of $V_g \otimes V_h$), the local factor becomes:
$$\mathcal{L}_\ell^{\mathrm{proj}}(f,g,h) = (1 - \beta_\ell^f / \ell) \cdot \langle g, g \rangle_\ell^{-1}$$
where $\langle g, g \rangle_\ell$ is the local Petersson inner product at $\ell$.

The first factor $(1 - \beta_\ell^f / \ell)$ is **independent of $g$** and is a $p$-adic unit (since $\ell \neq p$ and $|\beta_\ell^f| = \sqrt{\ell}$).

The second factor $\langle g, g \rangle_\ell^{-1}$ depends on $g$ but is a **normalization constant**, not a local obstruction. It can be absorbed into the scalar $c(g,h)$.

**Conclusion:** The local factor at $\ell$ is a unit (independent of $g$, up to normalization). It does not introduce $g$-dependent zeros.

### 3.5 Synthesis: The Weight of Evidence

| Evidence | Direction | Strength |
|----------|-----------|----------|
| CM case: factorization is a theorem (§2.6) | **For** | Strong |
| Projection $\pi_1$ is canonical | **For** | Moderate |
| Motivic origin constrains $g$-dependence | **For** | Moderate |
| Local factor at $\ell$ is a unit (§3.4) | **For** | Strong |
| Non-abelian $p$-adic $L$-function is not a scalar | **Against** | Weak (the evaluation at $g$ is still a scalar) |
| Selmer conditions at $\ell$ vary | **Against** | Weak (built into the construction) |

**Assessment:** The evidence **overwhelmingly favors** core factorization in the non-CM case as well. The factorization
$$\kappa_{g,h}(E) = c(g,h) \cdot \kappa_{\mathrm{core}}(E)$$
is expected to hold with $c(g,h) \in \mathbb{Q}_p^\times$ a unit scalar. This has not been **proved** in the non-CM case, but all structural evidence points to it.

---

## 4. What Would Be Needed to Refute Core Factorization

### 4.1 A Genuine $g$-Dependence of the Class

To refute core factorization, one would need to exhibit two admissible pairs $(g_1, h_1)$ and $(g_2, h_2)$ such that:
$$\kappa_{g_1,h_1}(E) \neq 0 \quad \text{and} \quad \kappa_{g_2,h_2}(E) = 0$$

This would show that the classes are **not** scalar multiples of each other, and that the $g$-dependence is genuine.

**Status:** No such example is known. In the CM case, this is impossible (by the factorization theorem). In the non-CM case, it would require:
1. A computation of $\kappa_{g,h}(E)$ for specific $(E, p, g, h)$.
2. Showing that the result depends on $(g, h)$ beyond a scalar.

**Computational barrier:** Computing $\kappa_{g,h}(E)$ requires evaluating Beilinson-Flach elements, which involves computing relative $K$-theory classes on $X_0(N) \times X_0(N)$. This is computationally intractable for $N = 389$ (genus 34) with current tools.

### 4.2 A Non-Scalar Dependence on $\ell$

To refute core factorization via $\ell$-variation, one would need to show that the class $\kappa_{\ell,g,h}(E)$ is genuinely $\ell$-dependent (beyond a unit scalar).

**Status:** The local factor analysis (§3.4) suggests this is impossible: the $\ell$-dependence is absorbed into a unit scalar. However, the analysis assumed that the local factor at $\ell$ is the **only** $\ell$-dependent part. There could be **global** $\ell$-dependence (e.g., through the Selmer group $H^1_f(\mathbb{Q}_\ell, V_p E)$ interacting with the global class).

**What would settle this:** An explicit computation of $\kappa_{\ell,g,h}(E)$ for two different values of $\ell$ (with the same $g, h$), showing that the resulting classes in $H^1_f(\mathbb{Q}, V_p E)$ are not proportional.

---

## 5. The Local Factor Vanishing Question

### 5.1 Setup

Hypothesis A implicitly assumes that varying $\mathfrak{a} = (\ell, \chi, g)$ can avoid local obstructions. Specifically, for a fixed $E$ and $p$:

$$\kappa_{\mathfrak{a}}(E) = 0 \iff \text{(some local condition at } \ell \text{ or } p \text{ fails)}$$

If the local condition at $\ell$ fails for **all** admissible $\ell$, then varying $\ell$ doesn't help.

### 5.2 The Local Condition at $\ell$

The Selmer condition at $\ell$ for $\kappa_{\mathfrak{a}}(E)$ is:
$$\operatorname{loc}_\ell(\kappa_{\mathfrak{a}}(E)) \in H^1_f(\mathbb{Q}_\ell, V_p E)$$

where $H^1_f(\mathbb{Q}_\ell, V_p E)$ is:
- $H^1_{\mathrm{ur}}(\mathbb{Q}_\ell, V_p E)$ if $\ell \nmid Np$ (the unramified classes),
- A more general condition (flat, crystalline) if $\ell \mid N$.

**The Beilinson-Flach construction ensures** that $\kappa_{\mathfrak{a}}(E)$ automatically satisfies the local condition at $\ell$ (this is built into the definition of the element). So the local condition at $\ell$ **cannot** vanish — it is satisfied by construction.

### 5.3 The Local Condition at $p$

The Selmer condition at $p$ is:
$$\operatorname{loc}_p(\kappa_{\mathfrak{a}}(E)) \in H^1_f(\mathbb{Q}_p, V_p E) = H^1_g(\mathbb{Q}_p, V_p E)$$
(the Bloch-Kato Selmer condition, equivalently, the crystalline condition for good ordinary $p$).

This condition is **independent of $\mathfrak{a}$** — it is a property of the cohomology class at $p$, not of the auxiliary data. The Beilinson-Flach element satisfies this condition by the **explicit reciprocity law** (Kings-Loeffler-Zerbes), which is independent of $(g, h)$.

**Conclusion:** The local conditions at both $\ell$ and $p$ are satisfied by construction (for all admissible $\mathfrak{a}$). The vanishing of $\kappa_{\mathfrak{a}}(E)$, if it occurs, is a **global** phenomenon — the class is locally trivial everywhere but globally nonzero, or vice versa.

### 5.4 Can Local Factors Vanish for ALL $\mathfrak{a}$?

**No.** The local factors at $\ell$ are units (§3.4), and the local conditions at $\ell$ and $p$ are satisfied by construction (§5.2–5.3). The question is not about local factors vanishing but about the **global** class being zero.

If $\kappa_{\mathfrak{a}}(E) = 0$, it is because the global cohomology class vanishes — not because any local factor is zero. This is consistent with the core factorization scenario (§1.1): the global class is zero because the core class is zero.

---

## 6. Rejection Criterion

### 6.1 The Criterion

**Reject Hypothesis A** if the generalized Kato class construction factors as:

$$\kappa_{\mathfrak{a}}(E) = u_{\mathfrak{a}}(E) \cdot \kappa_{\mathrm{core}}(E)$$

with $u_{\mathfrak{a}}(E) \in \mathbb{Q}_p^\times$ a unit scalar and $\kappa_{\mathrm{core}}(E)$ independent of $\mathfrak{a}$.

### 6.2 Evidence for Rejection

| Evidence | Status |
|----------|--------|
| Factorization proved in CM case (Castella, Thm 4.1.2) | **Known** |
| Factorization conjectured for non-CM case | **Expected** |
| Local factor at $\ell$ is a unit | **Verified** (for good $\ell \nmid Np$) |
| Projection $\pi_1$ is canonical | **Verified** (trace map) |
| Example of $g$-dependent nonvanishing | **None known** |

### 6.3 Evidence Against Rejection

| Evidence | Status |
|----------|--------|
| Factorization not proved for non-CM | **Open** |
| Non-abelian $p$-adic $L$-function structure | **Unknown** (no explicit formula) |
| Potential for global $g$-dependence | **Not excluded** |

### 6.4 Verdict

**Hypothesis A is likely false** (or rather, vacuously non-informative) **if core factorization holds.** The evidence strongly suggests it does, at least for the Castella construction from Beilinson-Flach elements. The varying auxiliary data $\mathfrak{a}$ produces **different scalar multiples** of the same class, and the nonvanishing question reduces to a single class.

**To salvage Hypothesis A**, one would need either:
1. A proof that core factorization **fails** in the non-CM case (showing $g$-dependent nonvanishing), or
2. A **different** construction of generalized Kato classes where the auxiliary dependence is genuinely non-trivial.

---

## 7. The Broader Implication

### 7.1 What This Means for the BSD Research Program

If Hypothesis A fails (due to core factorization), then:

1. **The Euler system approach to rank 2 cannot be "bootstrapped"** by varying auxiliary data. The obstruction is intrinsic to the curve $E$, not to the choice of construction.

2. **The problem reduces to the Darmon-Rotger conjecture:** proving $\kappa_{\mathrm{core}}(E) \neq 0$ for specific curves. This is a single-class nonvanishing problem, not a family-level phenomenon.

3. **The CM proof strategy (Castella's anticyclotomic method) does not extend** to non-CM curves by varying the auxiliary data — it extends (if at all) by proving the non-CM analogue of the anticyclotomic main conjecture.

4. **Alternative approaches** (Burns-Sakamoto-Sano, Bullach-Burns) that use the **module structure** of the Selmer group (Fitting ideals, zeta elements) rather than single-class nonvanishing may be more promising, because they do not require a single nonzero class — they require information about the characteristic ideal, which is a weaker input.

### 7.2 The Remaining Path

The most promising route for rank-2 BSD (for 389.a1 at $p = 5$) is:

1. **Skinner-Urban** (conditional on $\mu = 0$): proves $\operatorname{char}(X) = (\mathcal{L}_p)$, which gives $\Sha[5^\infty] = 0$ if the rank is independently known.
2. **Kato + explicit computation**: proves $\dim \operatorname{Sel}_5[5] \leq 2$ (the upper bound).
3. **Mordell-Weil generators**: prove $\operatorname{corank} \geq 2$ (the lower bound).
4. **Combination**: $\operatorname{corank} = 2$, $\Sha[5^\infty] = 0$.

This path does **not** require Hypothesis A, nor does it require the nonvanishing of any generalized Kato class. It uses the Euler system for the **upper bound** and the Mordell-Weil theorem for the **lower bound**, with the Iwasawa main conjecture (Skinner-Urban) bridging the gap.

**The generalized Kato class approach** (Hypothesis A) is an **alternative** route that would give a direct construction of nonzero Selmer classes, but it is not the only route, and the core factorization obstruction suggests it is not viable as a method for producing such classes by varying auxiliary data.

---

## 8. Summary

| Question | Answer |
|----------|--------|
| What is the earliest obstruction? | Core factorization: $\kappa_{\mathfrak{a}}(E) = u_{\mathfrak{a}} \cdot \kappa_{\mathrm{core}}(E)$ |
| Can this happen? | **Yes** — proved in CM case, expected in non-CM |
| What does Castella's paper say? | Theorem 4.1.2 proves factorization in CM case |
| Local factors at $\ell$? | Units (by construction); cannot vanish |
| Local factors at $p$? | Independent of $\mathfrak{a}$ (by construction) |
| Rejection criterion met? | **Yes** (for CM); **expected** (for non-CM) |
| Does varying $\mathfrak{a}$ help? | **No** (under core factorization) |
| What replaces Hypothesis A? | Skinner-Urban (conditional on $\mu = 0$) + explicit rank |

**Final assessment:** Hypothesis A is **almost certainly false** as a methodological claim — the auxiliary variation does not produce genuinely different classes. The correct approach to rank-2 BSD is not to find a "good" auxiliary construction, but to prove the nonvanishing of a **fixed** class (or to bypass the class entirely via the Iwasawa main conjecture).

---

## References

- Castella, F. "Generalised Kato classes on CM elliptic curves of rank 2." *American J. Math.* (to appear). [arXiv:2204.09608](https://arxiv.org/abs/2204.09608)
- Castella, F. "Nonvanishing of generalised Kato classes and Iwasawa main conjectures." [arXiv:2312.01481](https://arxiv.org/abs/2312.01481)
- Darmon, H., Rotger, V. "Diagonal cycles and Euler systems I." *Ann. of Math.* (2017).
- Kings, G., Loeffler, D., Zerbes, S.L. "Rankin-Euler classes and the Bloch-Kato conjecture." (2017).
- Skinner, C., Urban, E. "The Iwasawa main conjectures for $\mathrm{GL}_2$." *Invent. Math.* 195 (2014), 1–277.
- Kato, K. "$p$-adic Hodge theory and values of zeta functions of modular forms." *Astérisque* 295 (2004).
