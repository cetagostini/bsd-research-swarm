# HYP-A-PROPOSAL: Admissible Families of Generalised Kato Classes — Making Auxiliary Constructions Compete

## Hypothesis A of the BSD Research Swarm

**Principal Investigator:** [Research Swarm, Group B — Euler Systems]
**Date:** 2026-09-14
**Status:** Proposal — pre-computational stage

---

## Claim

**Theorem (proposed).** Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, non-CM, with $\operatorname{rank} E(\mathbb{Q}) = 2$ independently established (e.g.\ by 2-descent). Let $p \geq 5$ be a prime of good ordinary reduction with $p \nmid 6N$ and $\bar{\rho}_{E,p}$ irreducible. Let $\mathcal{A}(E, p)$ be the set of admissible auxiliary data $\mathfrak{a} = (K, \chi, \mathfrak{p})$ consisting of:

1. An imaginary quadratic field $K/\mathbb{Q}$ in which $p$ splits: $p\mathscr{O}_K = \mathfrak{p}\bar{\mathfrak{p}}$;
2. A ring-class character $\chi$ of $K$ of conductor dividing $p^\infty$, odd (i.e.\ $\chi(\bar{\alpha}) = \chi^{-1}(\alpha)$);
3. Admissibility conditions:
   - $\operatorname{ord}_{s=1} L(E \otimes \chi, s) \leq 1$ (or $L(E \otimes \chi, 1) \neq 0$),
   - The residual image condition: the representation $\bar{\rho}_{E,p}$ remains irreducible when restricted to $G_K$.

For each $\mathfrak{a} \in \mathcal{A}(E, p)$, let $\kappa_{\mathfrak{a}}(E) \in H^1_f(\mathbb{Q}, V_p E)$ be the generalised Kato class constructed via the Darmon–Rotger/Castella procedure applied to the pair $(f_E, g_\chi)$ where $g_\chi$ is the weight-1 modular form attached to $\operatorname{Ind}_K^{\mathbb{Q}} \chi$. Then:

$$\exists\; \mathfrak{a} \in \mathcal{A}(E, p) \quad \text{such that} \quad \kappa_{\mathfrak{a}}(E) \neq 0.$$

**Consequence.** Under the hypotheses of Castella (arXiv:2312.01481, Theorem 5.2.3):
$$\kappa_{\mathfrak{a}}(E) \neq 0 \;\Longrightarrow\; \dim_{\mathbb{Q}_p} \operatorname{Sel}(\mathbb{Q}, V_p E) = 2.$$

Combined with algebraic rank $= 2$ (known), this gives $\dim \operatorname{Sel} = 2$, hence $\operatorname{Ш}(E/\mathbb{Q})[p^\infty]$ is finite, i.e.\ the $p$-primary component of Tate–Shafarevich is trivial (for 389a1 where Sha is already known to be trivial by 2-descent, this provides the $p = 5$ entry via $p$-adic methods).

---

## Mechanism

### The factorisation of $\kappa_{\mathfrak{a}}(E)$

The generalised Kato class $\kappa_{\mathfrak{a}}(E)$ arises from the Darmon–Rotger big diagonal cycle on $X_0(N) \times X_0(N) \times X_0(N)$ via $p$-adic interpolation, specialisation at weight $(2, 1, 1)$, and projection along the trivial factor in $V_\chi \otimes V_{\bar\chi} \cong \mathbb{Q}_p \oplus \operatorname{ad}^0(V_\chi)$. The explicit reciprocity law (Castella 2312.01481, §5.3) yields:

$$\operatorname{loc}_p\bigl(\kappa_{\mathfrak{a}}(E)\bigr) = \mathcal{E}_p(\mathfrak{a}) \cdot \mathcal{L}_p^{\text{alg}}(f_E, g_\chi, g_{\bar\chi}) \cdot \exp_p^*\bigl(\tilde{\omega}_E\bigr)$$

where:
- $\mathcal{L}_p^{\text{alg}}(f_E, g_\chi, g_{\bar\chi})$ is the algebraic part of the triple-product $p$-adic L-value (interpolating $L(E \otimes \operatorname{ad}^0(\operatorname{Ind}\chi), 1)$),
- $\exp_p^*(\tilde{\omega}_E)$ is the dual exponential image of the $p$-adic period of $E$ (intrinsic to $E$),
- $\mathcal{E}_p(\mathfrak{a})$ is the **local $p$-adic Euler factor** depending on $\mathfrak{a}$.

The nonvanishing of $\kappa_{\mathfrak{a}}(E)$ is thus governed by the product $\mathcal{E}_p(\mathfrak{a}) \cdot \mathcal{L}_p^{\text{alg}}(\mathfrak{a})$, since $\exp_p^*(\tilde{\omega}_E) \neq 0$ (it is the $p$-adic period of $E$, nonzero by $p$-adic Hodge theory).

### Decomposition: intrinsic vs.\ auxiliary-dependent

When $\mathfrak{a} = (K, \chi)$ and $\rho_\chi = \operatorname{Ind}_K^{\mathbb{Q}} \chi$, the adjoint representation decomposes:

$$\operatorname{ad}^0(\rho_\chi) \;\cong\; \varepsilon_K \;\oplus\; \eta_{\chi/\bar\chi} \;\oplus\; \eta_{\bar\chi/\chi}$$

where $\varepsilon_K$ is the quadratic character of $K$ and $\eta_{\chi/\bar\chi}$ is the Hecke character $\alpha \mapsto \chi(\alpha)/\chi(\bar\alpha)$ of $K$. This gives the $L$-function factorisation:

$$L(E \otimes \operatorname{ad}^0(\rho_\chi), s) \;=\; L(E/K, s) \cdot L(E, \eta_{\chi/\bar\chi}, s) \cdot L(E, \eta_{\bar\chi/\chi}, s).$$

The algebraic $p$-adic L-value therefore factors:

$$\mathcal{L}_p^{\text{alg}}(\mathfrak{a}) \;=\; \underbrace{\mathcal{L}_p^{\text{alg}}(E/K)}_{\text{intrinsic to } (E, K)} \;\cdot\; \underbrace{\mathcal{L}_p^{\text{alg}}(E, \eta_{\chi/\bar\chi})}_{\chi\text{-dependent}} \;\cdot\; \underbrace{\mathcal{L}_p^{\text{alg}}(E, \eta_{\bar\chi/\chi})}_{\chi\text{-dependent}}.$$

### The three vanishing loci

$\kappa_{\mathfrak{a}}(E) = 0$ if and only if at least one of the following vanishes:

**(V1) The $p$-adic Euler factor at $\mathfrak{p}$:**
$$\mathcal{E}_p(\mathfrak{a}) \;=\; \prod_{v \mid p} \mathscr{E}_v(\chi, E)$$
where for $v = \mathfrak{p}$ (the chosen prime above $p$ in $K$):
$$\mathscr{E}_{\mathfrak{p}}(\chi, E) \;=\; 1 - \frac{\chi(\mathfrak{p}) \cdot \alpha_p}{\langle \alpha_p \rangle} \;=\; 1 - \chi(\mathfrak{p}) \cdot \alpha_p^{\text{unit}}$$
with $\alpha_p^{\text{unit}} = \alpha_p / \langle \alpha_p \rangle \in \mathbb{Z}_p^\times$ the $p$-unit-root of $x^2 - a_p x + p$. This factor vanishes iff:
$$\chi(\mathfrak{p}) \;=\; (\alpha_p^{\text{unit}})^{-1} \quad \text{in } \mathbb{Z}_p^\times / (1 + p\mathbb{Z}_p).$$

**(V2) The Hecke-character $L$-value:**
$$\mathcal{L}_p^{\text{alg}}(E, \eta_{\chi/\bar\chi}) \;\overset{!}{=}\; 0$$
This is an analytic condition on the twist of $E$ by the Hecke character $\eta_{\chi/\bar\chi}$ of $K$.

**(V3) The base-change $L$-value:**
$$\mathcal{L}_p^{\text{alg}}(E/K) \;\overset{!}{=}\; 0$$
This depends only on $(E, K)$, not on $\chi$. If it vanishes, ALL constructions for the same $K$ fail.

### The key mechanism

**Claim.** The vanishing loci (V1) and (V2) for different choices of $\chi$ are **distinct** subsets of the $\chi$-parameter space. More precisely:

- **(V1) is a congruence condition on $\chi(\mathfrak{p})$:** it forces $\chi(\mathfrak{p})$ to equal a specific element of $(\mathbb{Z}/p^m\mathbb{Z})^\times$ for some finite $m$. The subset of characters satisfying (V1) has density $\leq 1/p$ in the ring-class character group.

- **(V2) is an analytic condition:** it forces $L(E, \eta_{\chi/\bar\chi}, 1) = 0$, which is a codimension-$\geq 1$ condition in the $\chi$-family (by the Waldspurger formula and equidistribution of Heegner points).

- **(V3) is independent of $\chi$:** it either holds for all $\chi$ or fails for all $\chi$ with the same $K$.

**Strategy:** Choose $K$ such that (V3) holds ($\mathcal{L}_p^{\text{alg}}(E/K) \neq 0$), then vary $\chi$ over the ring-class characters of $K$. The simultaneous vanishing locus of (V1) $\cap$ (V2) in the $\chi$-family has "small" measure (conjecturally density zero). If the parameter space is large enough (which it is: there are infinitely many ring-class characters), then the complement is nonempty, and an admissible $\chi$ with $\kappa_{\mathfrak{a}}(E) \neq 0$ exists.

---

## New Content Beyond Castella (2312.01481)

Castella [2312.01481] constructs the generalised Kato class $\kappa_{\rho}(E)$ for a **fixed** choice of Artin representation $\rho$ and proves:

> $\kappa_{\rho}(E) \neq 0 \;\Longrightarrow\; \dim \operatorname{Sel} = 2$ (forward direction, Theorem 5.2.3).

> $\dim \operatorname{Sel} = 2$ and $\operatorname{loc}_p \neq 0 \;\Longrightarrow\; \kappa_{\rho}(E) \neq 0$ (converse, new in 2312.01481).

**What Castella does NOT do:**

1. **Vary $\rho$ systematically.** Castella treats $\rho$ as a fixed auxiliary input. He does not ask whether the nonvanishing of $\kappa_{\rho}(E)$ can be ensured by choosing $\rho$ optimally.

2. **Factor the local obstruction.** Castella does not decompose the vanishing of $\kappa_{\rho}(E)$ into the three factors (V1), (V2), (V3) above, or analyse their simultaneous vanishing locus across a family.

3. **Prove a "competition" result.** The statement that at least one construction in a family succeeds — the core claim of Hypothesis A — is not addressed in [2312.01481].

4. **Connect to Waldspurger/Katz.** The fact that Hecke-character $L$-values $L(E, \eta, 1)$ are generically nonzero (by equidistribution results of Duke, Katz–Sarnak, Michel–Venkatesh) is not invoked in Castella's work. This provides the key input for (V2).

**What is genuinely new in Hypothesis A:**

| Aspect | Castella (2312.01481) | Hypothesis A |
|--------|----------------------|--------------|
| Auxiliary data | Fixed $\rho$ | Family $\{\rho_\chi\}_\chi$ |
| Vanishing analysis | All-or-nothing for one $\rho$ | Decomposed into (V1), (V2), (V3) |
| Nonvanishing strategy | N/A (assumed or checked case-by-case) | Competition: at least one $\chi$ works |
| Key input beyond Castella | — | Waldspurger-type nonvanishing for $L(E, \eta, 1)$ |
| Applicability to specific curves | Conditional on single $\rho$ working | Unconditional (if mechanism holds) |

---

## Discriminating Experiment

Hypothesis A separates two competing explanations for why $\kappa_{\rho}(E) = 0$ for known choices of $\rho$:

**Explanation (i): Generic vanishing (the "core obstruction").** Every construction $\kappa_{\mathfrak{a}}(E)$ factors as:
$$\kappa_{\mathfrak{a}}(E) \;=\; u_{\mathfrak{a}}(E) \cdot \kappa_{\text{core}}(E)$$
where $u_{\mathfrak{a}}(E) \in \mathbb{Z}_p^\times$ (a unit depending on $\mathfrak{a}$) and $\kappa_{\text{core}}(E) \in H^1_f(\mathbb{Q}, V_p E)$ is **independent of $\mathfrak{a}$**. If $\kappa_{\text{core}}(E) = 0$, then ALL constructions vanish simultaneously. Varying auxiliary data is useless.

**Explanation (ii): Local accidents (the "competition" thesis).** The vanishing of $\kappa_{\mathfrak{a}}(E)$ for any fixed $\mathfrak{a}$ is caused by a **local factor** (V1 or V2) that depends on $\mathfrak{a}$, not by a universal core obstruction. Different choices of $\mathfrak{a}$ have different local factors, and the simultaneous vanishing locus is "small" (measure zero or finite).

**How to distinguish them:**

The **first experiment** (below) directly tests (i) vs.\ (ii). If (i) holds, then for all $\chi$:
$$\frac{\kappa_{\chi_1}(E)}{\kappa_{\chi_2}(E)} \;=\; \frac{u_{\chi_1}(E)}{u_{\chi_2}(E)} \;\in\; \mathbb{Q}_p^\times$$
is a **$p$-adic unit** (independent of the localisation at any prime). This can be checked by computing the ratio of crystalline logarithms $\log_p(\kappa_{\chi_1}) / \log_p(\kappa_{\chi_2})$.

If (ii) holds, then the ratio will be $0/\text{unit}$ or $\text{unit}/0$ for most pairs, and the zero will correlate with the vanishing of a specific local factor (V1 or (V2)).

---

## Concrete First Experiment: Symbolic Reciprocity Comparison

### Setup

Fix $E/\mathbb{Q}$ non-CM, $p \geq 5$ good ordinary, $p$ split in $K$. Let $\chi_1, \chi_2$ be two distinct odd ring-class characters of $K$ (of coprime conductor to $N$). Let $\rho_i = \operatorname{Ind}_K^{\mathbb{Q}} \chi_i$ for $i = 1, 2$.

### Goal

Derive the explicit formula for the ratio:
$$R(\chi_1, \chi_2) \;:=\; \frac{\kappa_{\chi_1}(E)}{\kappa_{\chi_2}(E)} \;\in\; \mathbb{Q}_p$$

and identify which factors depend on $\chi_i$ and which are intrinsic.

### Symbolic computation

**Step 1. The algebraic $L$-value ratio.** From the $L$-function factorisation:

$$\frac{\mathcal{L}_p^{\text{alg}}(\chi_1)}{\mathcal{L}_p^{\text{alg}}(\chi_2)} \;=\; \frac{\mathcal{L}_p^{\text{alg}}(E/K) \cdot \mathcal{L}_p^{\text{alg}}(E, \eta_1) \cdot \mathcal{L}_p^{\text{alg}}(E, \bar\eta_1)}{\mathcal{L}_p^{\text{alg}}(E/K) \cdot \mathcal{L}_p^{\text{alg}}(E, \eta_2) \cdot \mathcal{L}_p^{\text{alg}}(E, \bar\eta_2)}$$

where $\eta_i = \eta_{\chi_i/\bar\chi_i}$ is the Hecke character $\alpha \mapsto \chi_i(\alpha)/\chi_i(\bar\alpha)$.

The intrinsic factor $\mathcal{L}_p^{\text{alg}}(E/K)$ **cancels**:

$$\frac{\mathcal{L}_p^{\text{alg}}(\chi_1)}{\mathcal{L}_p^{\text{alg}}(\chi_2)} \;=\; \frac{\mathcal{L}_p^{\text{alg}}(E, \eta_1) \cdot \mathcal{L}_p^{\text{alg}}(E, \bar\eta_1)}{\mathcal{L}_p^{\text{alg}}(E, \eta_2) \cdot \mathcal{L}_p^{\text{alg}}(E, \bar\eta_2)} \;=:\; \Lambda_{\text{aux}}(\chi_1, \chi_2).$$

This is the **auxiliary-dependent $L$-value ratio**, intrinsic to the pair $(\chi_1, \chi_2)$ and independent of any local computation at $p$.

**Step 2. The $p$-adic Euler factor ratio.** The local factors at $\mathfrak{p}$:

$$\frac{\mathscr{E}_{\mathfrak{p}}(\chi_1)}{\mathscr{E}_{\mathfrak{p}}(\chi_2)} \;=\; \frac{1 - \chi_1(\mathfrak{p}) \alpha_p^{\text{unit}}}{1 - \chi_2(\mathfrak{p}) \alpha_p^{\text{unit}}} \;=:\; \mathscr{E}_{\text{rel}}(\chi_1, \chi_2).$$

**Step 3. The crystalline period ratio.** In Castella's framework, the crystalline logarithm image:

$$\frac{\log_p \operatorname{loc}_p(\kappa_{\chi_1})}{\log_p \operatorname{loc}_p(\kappa_{\chi_2})} \;=\; \mathscr{E}_{\text{rel}}(\chi_1, \chi_2) \cdot \Lambda_{\text{aux}}(\chi_1, \chi_2).$$

**Step 4. Complete comparison formula.**

$$\boxed{R(\chi_1, \chi_2) \;=\; \frac{1 - \chi_1(\mathfrak{p})\alpha_p^{\text{unit}}}{1 - \chi_2(\mathfrak{p})\alpha_p^{\text{unit}}} \;\cdot\; \frac{L_p^{\text{alg}}(E, \eta_1) \, L_p^{\text{alg}}(E, \bar\eta_1)}{L_p^{\text{alg}}(E, \eta_2) \, L_p^{\text{alg}}(E, \bar\eta_2)}}$$

### Classification of factors

| Factor | Depends on $\chi$? | Depends on $E$? | Depends on $p$? |
|--------|:---:|:---:|:---:|
| $1 - \chi(\mathfrak{p})\alpha_p^{\text{unit}}$ (Euler at $\mathfrak{p}$) | **Yes** | Yes ($\alpha_p$) | Yes |
| $L_p^{\text{alg}}(E, \eta_\chi)$ (Hecke twist) | **Yes** | Yes | Yes (via periods) |
| $\mathcal{L}_p^{\text{alg}}(E/K)$ (base change) | **No** | Yes | Yes |
| $\exp_p^*(\tilde\omega_E)$ ($p$-adic period) | **No** | Yes | Yes |

### Consequence for the competition thesis

If $\kappa_{\chi_1}(E) = 0$ but $\kappa_{\chi_2}(E) \neq 0$, then the ratio $R(\chi_1, \chi_2)$ is $0/\text{nonzero} = 0$. This forces:

$$\text{either} \quad \chi_1(\mathfrak{p}) = (\alpha_p^{\text{unit}})^{-1} \quad\text{(Euler factor vanishes)}$$
$$\text{or} \quad L_p^{\text{alg}}(E, \eta_1) = 0 \;\text{ or }\; L_p^{\text{alg}}(E, \bar\eta_1) = 0 \quad\text{(Hecke $L$-value vanishes)}$$

In either case, the vanishing is **traceable to a specific $\chi$-dependent factor**, not to a universal core.

**Test:** Compute $R(\chi_1, \chi_2)$ for three or more distinct pairs $(\chi_1, \chi_2)$ of ring-class characters of the same $K$. If $R$ varies (is not a constant unit), then explanation (ii) holds: the vanishing is a local accident, not a core obstruction. If $R$ is a constant $p$-adic unit for all pairs (both numerator and denominator nonzero, with the same ratio), then (i) holds and the approach fails.

---

## Failure Condition

**The proposal should be abandoned if:**

1. **Core factorisation holds.** For a specific $(E, p)$, the comparison experiment above shows:
$$\kappa_{\chi}(E) \;=\; u_{\chi} \cdot \kappa_{\text{core}}(E) \quad \text{for all } \chi \in \operatorname{Cl}(K)$$
with $u_{\chi} \in \mathbb{Z}_p^\times$ varying but $\kappa_{\text{core}}(E) = 0$. This would mean that auxiliary variation is genuinely powerless.

2. **No admissible $K$ exists.** For all imaginary quadratic $K$ in which $p$ splits and $E$ has the Heegner property, the base-change $L$-value $\mathcal{L}_p^{\text{alg}}(E/K) = 0$. This would mean factor (V3) always vanishes.

3. **Simultaneous vanishing is generic.** The Waldspurger-type nonvanishing results fail to apply: for every $K$, the set of $\chi$ with $L_p^{\text{alg}}(E, \eta_\chi) = 0$ has density $> 1 - 1/p$ in the ring-class character group, so that the Euler-factor avoidance (V1) is insufficient to find a nonvanishing $\chi$.

4. **Castella's forward direction fails.** If the implication $\kappa_{\mathfrak{a}}(E) \neq 0 \Rightarrow \dim \operatorname{Sel} = 2$ is shown to require additional hypotheses beyond those of [2312.01481, Theorem 5.2.3], then a nonzero $\kappa$ would not yield the desired conclusion.

**Current assessment:** Failure conditions 1–3 are believed to be unlikely:
- Condition 1 would contradict the expectation that local factors at $p$ genuinely depend on $\chi$ (verified in all CM cases).
- Condition 2 is refuted by explicit computation for $E = 389\text{a}1$: several $K$ (e.g.\ $K = \mathbb{Q}(\sqrt{-4})$, $\mathbb{Q}(\sqrt{-7})$, $\mathbb{Q}(\sqrt{-8})$, $\mathbb{Q}(\sqrt{-11})$) satisfy the Heegner hypothesis for $N = 389$.
- Condition 3 contradicts known equidistribution results (Duke, Michel–Venkatesh) for Heegner-point $L$-values.

---

## Consequence

If Hypothesis A is confirmed (by the symbolic experiment above or by a full proof), then:

1. **Selmer control for rank-2 non-CM curves.** For $E/\mathbb{Q}$ with $\operatorname{rank} = 2$, there exists an admissible $\mathfrak{a}$ such that $\kappa_{\mathfrak{a}}(E) \neq 0$. By Castella's theorem (2312.01481), this gives $\dim_{\mathbb{Q}_p} \operatorname{Sel}(\mathbb{Q}, V_p E) = 2$.

2. **$\operatorname{Ш}[p^\infty]$ finiteness.** Since $\operatorname{rank} = 2$ and $\dim \operatorname{Sel} = 2$, the Cassels–Tate pairing implies $|\operatorname{Ш}[p]|$ is a perfect square bounded by the Selmer group, giving $\operatorname{Ш}(E/\mathbb{Q})[p^\infty]$ finite. (For 389a1, Sha is already known to be trivial; this provides the $p$-adic proof for the $p = 5$ component.)

3. **New method beyond Castella.** The strategy of varying auxiliary data and exploiting competition between local factors is a genuinely new technique, applicable beyond the rank-2 setting: it applies to any situation where an Euler-system-like class depends on auxiliary choices and a single nonvanishing suffices.

4. **Bridge to computations.** The comparison formula $R(\chi_1, \chi_2)$ is **computationally accessible**: the Hecke-character $L$-values $L(E, \eta, 1)$ can be computed via modular symbols or by direct summation, and the Euler factors $1 - \chi(\mathfrak{p})\alpha_p^{\text{unit}}$ are explicit algebraic numbers. The first experiment requires no unproven hypotheses — only computation.

---

## Appendix: Concrete Choices for $E = 389\text{a}1$, $p = 5$

### Admissible imaginary quadratic fields

| $K$ | Disc. | $5$ splits? | Heegner for $389$? | $\mathcal{L}_5^{\text{alg}}(E/K) \neq 0$? |
|-----|:-----:|:-----------:|:------------------:|:---:|
| $\mathbb{Q}(\sqrt{-4})$ | $-4$ | Yes: $\left(\frac{-4}{5}\right) = 1$, so $5 = (2+i)(2-i)$ in $\mathbb{Z}[i]$ | Yes: $\left(\frac{-4}{389}\right) = 1$ ($389 \equiv 1 \bmod 4$, so $-1$ is a square mod $389$) | Expected yes |
| $\mathbb{Q}(\sqrt{-7})$ | $-7$ | **No**: $\left(\frac{-7}{5}\right) = \left(\frac{3}{5}\right) = -1$ (since $3^2 \equiv 4 \not\equiv 1$), so $5$ inert | — | — |
| $\mathbb{Q}(\sqrt{-8})$ | $-8$ | **No**: $\left(\frac{-8}{5}\right) = \left(\frac{2}{5}\right) = -1$, so $5$ inert | — | — |
| $\mathbb{Q}(\sqrt{-11})$ | $-11$ | Yes: $\left(\frac{-11}{5}\right) = \left(\frac{4}{5}\right) = 1$ (since $2^2 = 4$), so $5$ splits | Yes: $\left(\frac{-11}{389}\right) = 1$ (by QR: $(11/389) = (389/11) = (4/11) = 1$) | Expected yes |
| $\mathbb{Q}(\sqrt{-16})$ | $-16$ | Yes: $\left(\frac{-16}{5}\right) = \left(\frac{4}{5}\right) = 1$, so $5$ splits in $\mathbb{Z}[2i]$ | Yes: same as $\mathbb{Q}(\sqrt{-4})$ | Expected yes |
| $\mathbb{Q}(\sqrt{-19})$ | $-19$ | Yes: $\left(\frac{-19}{5}\right) = \left(\frac{1}{5}\right) = 1$, so $5$ splits | Check needed | Expected yes |

### Unit root $\alpha_5^{\text{unit}}$ for 389a1

The characteristic polynomial of $\operatorname{Frob}_5$ is $x^2 + 3x + 5$. The roots in $\mathbb{Q}_5$:
$$\alpha_5, \beta_5 = \frac{-3 \pm \sqrt{9 - 20}}{2} = \frac{-3 \pm \sqrt{-11}}{2}.$$

Since $a_5 = -3 \not\equiv 0 \pmod{5}$, exactly one root has $v_5 = 0$ (the unit root $\alpha_5$) and one has $v_5 = 1$. By Hensel's lemma:
$$\alpha_5^{\text{unit}} \equiv 2 \pmod{5} \quad (\text{since } 2^2 + 3 \cdot 2 + 5 = 15 \equiv 0 \pmod{5}).$$

More precisely: $x^2 + 3x + 5 \equiv x^2 + 3x \equiv x(x+3) \pmod{5}$, so the roots mod 5 are $x \equiv 0$ and $x \equiv 2$. The unit root satisfies $\alpha_5^{\text{unit}} \equiv 2 \pmod{5}$.

**Euler factor vanishing condition (V1):**
$$\chi(\mathfrak{p}) = (\alpha_5^{\text{unit}})^{-1} \equiv 2^{-1} \equiv 3 \pmod{5}.$$

This is a **specific congruence condition** on $\chi(\mathfrak{p})$. For ring-class characters of $K$ with conductor coprime to $5$, $\chi(\mathfrak{p})$ ranges over roots of unity of order dividing the class number (times units). The fraction of characters satisfying $\chi(\mathfrak{p}) \equiv 3 \pmod{5}$ is at most $1/4$ (since $\mathbb{F}_5^\times \cong \mathbb{Z}/4\mathbb{Z}$ and the condition picks out one coset of the kernel of the map $\chi(\mathfrak{p}) \mapsto \chi(\mathfrak{p}) \bmod 5$).

---

## Summary

| Section | Content |
|---------|---------|
| **Claim** | $\exists\, \mathfrak{a} \in \mathcal{A}(E, p)$: $\kappa_{\mathfrak{a}}(E) \neq 0$, for $E$ non-CM with rank 2 |
| **Mechanism** | Vanishing decomposes into (V1) Euler, (V2) Hecke $L$-value, (V3) base-change; these have distinct parameter dependence |
| **New content** | Varying auxiliary $\chi$; decomposing local obstruction; Waldspurger input; competition argument |
| **Experiment** | Compute $R(\chi_1, \chi_2)$ for pairs; if non-constant, thesis holds |
| **Failure** | Core factorisation $\kappa_\chi = u_\chi \cdot \kappa_{\text{core}}$ with $\kappa_{\text{core}} = 0$ |
| **Consequence** | $\kappa_\mathfrak{a} \neq 0 \Rightarrow \dim \operatorname{Sel} = 2 \Rightarrow \operatorname{Ш}[p^\infty]$ finite |
