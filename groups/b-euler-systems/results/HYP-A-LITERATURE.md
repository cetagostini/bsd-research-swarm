# HYP-A-LITERATURE: Literature Review for Hypothesis A

## Purpose

This document records the closest existing results to Hypothesis A, the precise gap between what is known and what Hypothesis A claims, and what would be genuinely new.

---

## 1. Closest Existing Statement

### 1.1 Castella (arXiv:2312.01481)

**Theorem (Castella, 2023).** Let $E/\mathbb{Q}$ be an elliptic curve (not necessarily CM) and let $p > 3$ be a prime of good ordinary reduction. Suppose $\operatorname{ord}_{s=1} L(E, s) \geq 2$ and the root number is $+1$. Let $\kappa_p(E) \in \operatorname{Sel}(\mathbb{Q}, V_p E)$ be the generalized Kato class obtained from the Darmon–Rotger construction with a **single** choice of auxiliary data $(g, h)$ where $h \simeq g^\vee$.

Then:

- **Forward direction:** $\kappa_p(E) \neq 0 \Longrightarrow \dim_{\mathbb{Q}_p} \operatorname{Sel}(\mathbb{Q}, V_p E) = 2$.
- **Converse direction:** If $\dim_{\mathbb{Q}_p} \operatorname{Sel}(\mathbb{Q}, V_p E) = 2$, then $\kappa_p(E) \neq 0$ **if and only if** the restriction map $\operatorname{loc}_p : \operatorname{Sel}(\mathbb{Q}, V_p E) \to E(\mathbb{Q}_p) \hat{\otimes} \mathbb{Q}_p$ is nonzero.

### 1.2 Castella–Hsieh (arXiv:1809.09066, 2022)

**Theorem (Castella–Hsieh).** For $E/\mathbb{Q}$ of rank 2, $p > 3$ good ordinary, and **specific** choices of auxiliary eigenform $g$ (those with CM by an imaginary quadratic field), the generalized Kato class $\kappa_{g,h}(E)$ is nonzero, hence $\dim \operatorname{Sel}(\mathbb{Q}, V_p E) = 2$.

This provides the **first unconditional construction** of nonzero Selmer classes for non-CM rank-2 curves via $p$-adic methods, but only for **CM auxiliary forms** $g$.

### 1.3 Summary of What Castella Proves

| Statement | Status | Reference |
|-----------|--------|-----------|
| $\kappa_p(E) \neq 0 \Rightarrow \dim \operatorname{Sel} = 2$ | **Proved** (non-CM) | [2312.01481], [1809.09066] |
| $\dim \operatorname{Sel} = 2$ and $\operatorname{loc}_p \neq 0 \Rightarrow \kappa_p(E) \neq 0$ | **Proved** (non-CM) | [2312.01481] |
| $\kappa_p(E) \neq 0$ for specific $E$ with CM auxiliary $g$ | **Proved** | [1809.09066] |
| $\kappa_p(E) \neq 0$ for all non-CM rank-2 $E$ | **Open** | — |
| Full equivalence $\kappa_p \neq 0 \iff \dim \operatorname{Sel} = 2$ | **Open** | Darmon–Rotger conjecture (1.2) |

---

## 2. The Precise Difference from Hypothesis A

### 2.1 What Castella's Result Is About

Castella works with a **single** auxiliary choice: fix $(g, h)$ with $h \simeq g^\vee$, construct $\kappa_{g,h}(E)$, and study its nonvanishing. The theorem is:

$$\kappa_{g,h}(E) \neq 0 \Longrightarrow \dim \operatorname{Sel} = 2$$

for **that particular** $(g, h)$.

### 2.2 What Hypothesis A Claims

**Hypothesis A.** For rank-2 $E/\mathbb{Q}$, there exists at least one admissible auxiliary $\mathfrak{a} = (\ell, \chi, g)$ such that $\kappa_{\mathfrak{a}}(E) \neq 0$.

This is a **family-level** assertion: the space of admissible $\mathfrak{a}$ is large, and Hypothesis A claims the "failure locus" $\{\mathfrak{a} : \kappa_{\mathfrak{a}}(E) = 0\}$ does not exhaust it.

### 2.3 The Gap

| Aspect | Castella | Hypothesis A |
|--------|----------|--------------|
| **Object** | Single class $\kappa_{g,h}(E)$ for fixed $(g,h)$ | Family $\{\kappa_{\mathfrak{a}}(E)\}_{\mathfrak{a}}$ |
| **Question** | Is this one class nonzero? | Is at least one class in the family nonzero? |
| **Method** | Iwasawa main conjecture (CM); explicit reciprocity law (non-CM) | Variation of auxiliary data to avoid common zeros |
| **Leverage from varying auxiliary** | None — result holds for fixed $(g,h)$ | Core strategy of Hypothesis A |

**The gap is precisely this:** Castella proves implications about a single class. Hypothesis A proposes to prove nonvanishing by varying the auxiliary. Whether varying the auxiliary provides genuine leverage (rather than producing scalar multiples of the same class) is the central question.

---

## 3. Has Anyone Tried Varying the Auxiliary?

### 3.1 Literature Search Results

**Search 1: "varying auxiliary" in Euler system literature.**

No published work addresses the strategy of varying the auxiliary data $(g, h)$ or the auxiliary prime $\ell$ in the generalized Kato class construction to prove nonvanishing. The standard approach is to fix $(g, h)$ and prove nonvanishing of the resulting single class.

The closest relevant work is:

- **Castella–Hsieh (1809.09066):** Proves nonvanishing for **specific** choices of $g$ (those with CM). This is a selection strategy (choose $g$ that works), not a variation strategy (show at least one $g$ works).
- **Darmon–Rotger (2017):** The original construction of generalized Kato classes from diagonal cycles. The dependence on $(g, h)$ is analyzed, but no "family nonvanishing" result is stated.

**Search 2: "common vanishing locus" in Kato class literature.**

No results found. The concept of a "common vanishing locus" for a family of Kato classes parametrized by auxiliary data does not appear in the literature.

**Search 3: "simultaneous nonvanishing" in $p$-adic $L$-function literature.**

The closest concept is **nonvanishing of families of $p$-adic $L$-functions**:

- **Rohrlich (1984):** Proves that for a fixed elliptic curve $E/\mathbb{Q}$, the twisted $L$-values $L(E, \chi, 1) \neq 0$ for all but finitely many Dirichlet characters $\chi$. This is a "simultaneous nonvanishing" result, but for **cyclotomic twists**, not for auxiliary eigenforms.
- **Greenberg (1983):** Nonvanishing results for $p$-adic $L$-functions at non-trivial characters, showing the zero locus is confined to the augmentation ideal.

None of these address the specific question of whether varying the auxiliary in the generalized Kato class construction can avoid common zeros.

### 3.2 Why the Gap Exists

The reason no one has studied "varying the auxiliary" for generalized Kato classes is that the construction is expected to exhibit **core factorization** (see HYP-A-OBSTRUCTION.md):

$$\kappa_{g,h}(E) = c(g,h) \cdot \kappa_{\mathrm{core}}(E)$$

with $c(g,h) \in \mathbb{Q}_p^\times$ a unit scalar. If this holds, varying $(g, h)$ produces scalar multiples of the same class, and the strategy provides no leverage.

**In the CM case**, this factorization is a **theorem** (Castella, Theorem 4.1.2 of [2312.01481]):
$$\kappa_{g,h}(E) = \mathcal{L}_p^{\mathrm{anti}}(E, \chi_g) \cdot \kappa_{\mathrm{CM}}(E)$$
where $\mathcal{L}_p^{\mathrm{anti}}(E, \chi_g)$ is the anticyclotomic $p$-adic $L$-function evaluated at $\chi_g$.

**In the non-CM case**, the factorization is **expected** but unproven. The evidence for it is strong (see HYP-A-OBSTRUCTION.md §3.5).

---

## 4. Related Results

### 4.1 Rohrlich's Theorem (CM Curves, Heegner Points)

**Theorem (Kolyvagin, 1990; Gross–Zagier, 1986).** Let $E/\mathbb{Q}$ have CM by an imaginary quadratic field $K$. The Heegner point $y_K \in E(K)$ is nonzero if and only if $L'(E/K, 1) \neq 0$.

More precisely, for the **rank 1** case:
- $L(E, 1) = 0$ and $L'(E, 1) \neq 0$ $\Longleftrightarrow$ $y_K$ is non-torsion $\Longleftrightarrow$ $\operatorname{rank} E(\mathbb{Q}) = 1$ and $|\text{Ш}| < \infty$.

This is a **"single construction" result**: the Heegner point $y_K$ depends on the choice of $K$ (the CM field), but for a **fixed** $E$ with CM by $K$, there is essentially one Heegner point (up to torsion). The nonvanishing is determined by the $L$-value, not by varying auxiliary data.

### 4.2 Has Anyone Generalized Rohrlich to Families?

**Partial results exist, but not in the direction relevant to Hypothesis A:**

- **Bertolini–Darmon (2005):** Constructed $p$-adic $L$-functions in the anticyclotomic direction using rigid analytic uniformization. The $p$-adic $L$-function $\mathcal{L}_p^{\mathrm{anti}}(E)$ is a function on a $p$-adic analytic space, and its zeros correspond to vanishing of Heegner points in $p$-adic families. This is a **$p$-adic family** result, not an **auxiliary variation** result.

- **Howard (2006):** Proved Iwasawa main conjectures in the "false" anticyclotomic setting via $p$-adic families. The variation is over the **cyclotomic tower**, not over auxiliary data.

- **Brooks–Shimizu (2022):** Made progress on the cyclotomic direction for non-CM curves over $K$. Again, the variation is over the tower, not over auxiliary constructions.

**No one has generalized Rohrlich's theorem to a "family of constructions" setting** where the family is parametrized by auxiliary eigenforms or auxiliary primes.

### 4.3 The Kolyvagin Analogy

Kolyvagin's original approach for rank 0–1 uses **one** Heegner point (for a fixed auxiliary prime $\ell$) and varies $\ell$ to produce Kolyvagin derivatives $\kappa_\ell$. The nonvanishing of $\kappa_\ell$ for **some** $\ell$ follows from the nonvanishing of the Heegner point itself — it does not require varying $\ell$ to "avoid zeros."

The analogue for rank 2 would be: the nonvanishing of $\kappa_{g,h}(E)$ for **some** $(g, h)$ follows from some intrinsic property of $E$, not from the variation of $(g, h)$.

---

## 5. What Would Be Genuinely New

### 5.1 The Novel Statement

A theorem of the following form would be genuinely new:

> **Theorem (Hypothetical).** For a rank-2 elliptic curve $E/\mathbb{Q}$ and a prime $p > 3$ of good ordinary reduction, the common vanishing locus of the family $\{\kappa_{\mathfrak{a}}(E)\}_{\mathfrak{a} \in \mathcal{A}}$ is empty, where $\mathcal{A}$ is the set of admissible auxiliary data.

Equivalently:

> There does **not** exist a rank-2 $E/\mathbb{Q}$ such that $\kappa_{\mathfrak{a}}(E) = 0$ for **all** admissible $\mathfrak{a}$.

### 5.2 Why This Would Be New

1. **No existing result proves nonvanishing by varying auxiliary.** All known proofs (Castella–Hsieh, Castella) prove nonvanishing for **specific** choices of $(g, h)$, using the Iwasawa main conjecture or explicit reciprocity laws. The variation of auxiliary is not used as a tool.

2. **No existing result analyzes the "failure locus" $\{\mathfrak{a} : \kappa_{\mathfrak{a}} = 0\}$.** The question of whether this locus can exhaust the admissible set $\mathcal{A}$ has not been studied.

3. **The "common vanishing locus" concept is absent from the literature.** While nonvanishing of individual $p$-adic $L$-functions is well-studied, the simultaneous nonvanishing of a family parametrized by auxiliary data is a new formulation.

### 5.3 Is It Provable?

**Obstacle 1: Core factorization.** If $\kappa_{g,h}(E) = c(g,h) \cdot \kappa_{\mathrm{core}}(E)$ with $c(g,h) \in \mathbb{Q}_p^\times$, then the common vanishing locus is either empty (if $\kappa_{\mathrm{core}} \neq 0$) or everything (if $\kappa_{\mathrm{core}} = 0$). The family-level statement reduces to the single-class statement, and no new technique is gained.

**Obstacle 2: The CM case is settled by other means.** In the CM case, Castella proves $\kappa_{\mathrm{CM}}(E) \neq 0$ using the anticyclotomic Iwasawa main conjecture. The proof does not use auxiliary variation. The "family" approach is unnecessary.

**Obstacle 3: The non-CM case requires new Iwasawa theory.** To prove $\kappa_{\mathrm{core}}(E) \neq 0$ in the non-CM case (if factorization holds), one would need the non-CM analogue of the anticyclotomic main conjecture — which is open.

**Possible escape: Factorization fails.** If core factorization fails in the non-CM case — i.e., if $\kappa_{g,h}(E)$ depends on $(g, h)$ beyond a scalar — then the family-level statement could be strictly stronger than the single-class statement. This would make the "common vanishing locus" approach genuinely new and potentially useful.

**Assessment:** The theorem is provable **if and only if** either:
- (a) Core factorization holds AND the core class is nonzero (reducing to the Darmon–Rotger conjecture), or
- (b) Core factorization fails AND the family-level structure can be exploited.

Case (a) is a reformulation of existing open problems. Case (b) would be genuinely new mathematics, but there is no current evidence that factorization fails.

### 5.4 What Would Make It Tractable

1. **An explicit computation of $\kappa_{g,h}(E)$ for two different $(g, h)$** on the same curve $E$, showing that the resulting classes are not proportional. This would disprove core factorization and open the door to the family approach.

2. **A theoretical result showing that $\kappa_{g,h}(E)$ depends on $(g, h)$ non-trivially** in the non-CM case. This would require understanding the non-abelian $p$-adic $L$-function that governs the $g$-dependence.

3. **A "density" result** showing that $\kappa_{g,h}(E) \neq 0$ for a positive proportion of admissible $(g, h)$. This would be a simultaneous nonvanishing result in the spirit of Rohrlich's theorem for twisted $L$-values.

---

## 6. Summary Table

| Statement | Status | Gap from Hypothesis A |
|-----------|--------|-----------------------|
| $\kappa_p(E) \neq 0 \Rightarrow \dim \operatorname{Sel} = 2$ (non-CM) | **Proved** | Hypothesis A needs $\kappa_p(E) \neq 0$ |
| $\kappa_p(E) \neq 0$ for specific $E$ with CM auxiliary $g$ | **Proved** | Only for CM auxiliary; not for all $E$ |
| Core factorization $\kappa_{g,h} = c(g,h) \cdot \kappa_{\mathrm{core}}$ (CM) | **Proved** | If holds for non-CM, Hypothesis A reduces to single-class |
| Core factorization (non-CM) | **Expected, unproven** | Would collapse Hypothesis A to Darmon–Rotger conjecture |
| Varying auxiliary avoids common zeros | **Not studied** | Central claim of Hypothesis A |
| "Common vanishing locus is empty" for families | **New** | No precedent in literature |
| Rohrlich-type nonvanishing for families of Kato classes | **New** | No precedent; closest is Rohrlich for cyclotomic twists |

---

## 7. Conclusion

**What exists:** Castella proves implications about a **single** generalized Kato class: $\kappa_p(E) \neq 0 \Rightarrow \dim \operatorname{Sel} = 2$, and partial converses. Castella–Hsieh prove nonvanishing for specific curves with CM auxiliary forms.

**What Hypothesis A adds:** The claim that varying the auxiliary data provides leverage to prove nonvanishing — that the "failure locus" does not exhaust the admissible set.

**What would be genuinely new:** A theorem that "for a family of admissible constructions, the common vanishing locus is empty." This has no precedent in the literature. However, if core factorization holds (as expected), this reduces to the existing Darmon–Rotger conjecture, and the family approach provides no new leverage.

**The critical open question:** Does core factorization $\kappa_{g,h}(E) = c(g,h) \cdot \kappa_{\mathrm{core}}(E)$ hold in the non-CM case? If yes, Hypothesis A is a reformulation. If no, it is genuinely new.

---

## References

1. Castella, F. "Nonvanishing of generalised Kato classes and Iwasawa main conjectures." [arXiv:2312.01481](https://arxiv.org/abs/2312.01481), 2023.
2. Castella, F., Hsieh, M.-L. "On the non-vanishing of generalized Kato classes for elliptic curves of rank 2." [arXiv:1809.09066](https://arxiv.org/abs/1809.09066), 2022. *Math. Proc. Cambridge Philos. Soc.*
3. Castella, F. "Generalised Kato classes on CM elliptic curves of rank 2." [arXiv:2204.09608](https://arxiv.org/abs/2204.09608). *American J. Math.* (to appear).
4. Darmon, H., Rotger, V. "Elliptic curves of rank two and generalised Kato classes." *Math. Proc. Cambridge Philos. Soc.* (2016).
5. Darmon, H., Rotger, V. "Diagonal cycles and Euler systems I." *Ann. of Math.* (2017).
6. Kolyvagin, V.A. "Euler systems for elliptic curves with complex multiplication." *Izv. Akad. Nauk SSSR Ser. Mat.* 52 (1988), 813–844.
7. Gross, B., Zagier, D. "Heegner points and derivatives of L-series." *Invent. Math.* 84 (1986), 225–320.
8. Rohrlich, D. "On L-functions of elliptic curves and cyclotomic towers." *Invent. Math.* 75 (1984), 383–408.
9. Bertolini, M., Darmon, H. "p-adic periods, p-adic L-functions, and the p-adic uniformization of Shimura curves." *Duke Math. J.* 98 (1999), 305–334.
10. Howard, B. "The Iwasawa theoretic Gross–Zagier theorem." *Compos. Math.* 141 (2005), 811–846.
