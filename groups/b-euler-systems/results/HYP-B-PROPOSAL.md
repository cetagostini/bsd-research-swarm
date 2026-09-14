# Hypothesis B: Collision Term as Arithmetic Detector

## Claim

Let $F$ be a number field, $p$ an odd prime, and $V$ a $p$-adic representation of $G_F$ over a finite extension $E/\mathbb{Q}_p$. Let $c_1, c_2: \mathcal{R} \to H^1(F_p, V)$ be two analytic families of local classes over a one-dimensional deformation space $\mathcal{R}$, with $c_1(0) = c_2(0) = c_0 \neq 0$. Writing $c_i(t) = c_0 + t\, c_i' + O(t^2)$, define

$$\delta \;=\; c_0 \,\wedge\, (c_2' - c_1') \;\in\; (t)/(t^2) \otimes_E \textstyle\bigwedge^2_E H^1(F_p,\, V)\,.$$

**Claim.** When $c_1, c_2$ arise from distinct global constructions (e.g.\ a Kato Euler system and a higher-rank system per arXiv:1805.08448), $\delta$ detects the *second-order* arithmetic data at the critical point that scalar specialization annihilates—specifically, the leading obstruction in the equivariant Tamagawa number conjecture (Burns--Kurihara--Sano, arXiv:1910.07404).

## Mechanism

Over $\mathcal{R}$, the pair defines $\Phi = c_1 \wedge c_2 \in \bigwedge^2_{\mathcal{O}_{\mathcal{R}}} H^1(F_p, \hat{V}_{\mathcal{R}})$. Modulo $t^2$: $\Phi \equiv [t] \otimes \delta$ since $c_0 \wedge c_0 = 0$. This is intrinsic before scalar specialization: it lives in $(t)/(t^2) \otimes \bigwedge^2 H^1(F_p, V)$. Changes of parameter $t \mapsto ut$ rescale by $u$; changes of lift $c_i \mapsto c_i + t\, d_i$ shift $\delta$ by $c_0 \wedge (d_2 - d_1)$. Thus $\delta$ is canonical modulo $c_0 \wedge H^1(F_p, V)$, i.e., it lives in the **Arf invariant quotient** $(t)/(t^2) \otimes \bigwedge^2 H^1 / (c_0 \wedge H^1)$.

## Obstacles

**1. Rank-one vanishing.** If both families lie in the same one-dimensional Selmer subspace, $\delta = 0$ identically. *Required:* $\dim_E H^1(F_p, V) \geq 2$ with the two families spanning distinct lines. Natural setting: $V = \mathrm{Ind}_{G_K}^{G_F} W$ for quadratic $F/K$, so $H^1(F_p, V) \cong H^1(K_{\mathfrak{p}}, W) \oplus H^1(K_{\mathfrak{p}^\sigma}, W^\sigma)$.

**2. Squared transition law.** Basis change at $\ell$ multiplies each class by $\alpha_\ell(t)$, hence $\delta$ by $\alpha_\ell(t)^2$—wrong power. *Fix:* Work with interchanged families (Galois involution $\sigma$). Then $\sigma(\delta) = -\delta$, so $\delta \cdot \sigma(\delta) = -\delta^2$ is a norm, yielding the correct Euler factor under functional-equation matching.

## Research Question

Does there exist $V$, deformation space $\mathcal{R}$, and families $c_1, c_2$ such that $\delta$ is (a) canonical integral, (b) lies in $H^1_f$ (Selmer-compatible), (c) obeys the correct first-power transition law, and (d) does not vanish for rank-one reasons? Candidate: Hilbert modular induction $V = \mathrm{Ind}_K^F W$ with $\mathrm{Gal}(F/K)$-interchanged families.

## First Experiment

1. **Choose $V$:** Hilbert modular $V = \mathrm{Ind}_K^F W$ over real quadratic $F/K$. By Shapiro, $H^1(F_p, V) \cong H^1(K_{\mathfrak{p}}, W) \oplus H^1(K_{\mathfrak{p}^\sigma}, W^\sigma)$; if $W$ ordinary, each summand is 1-dimensional, confirming generic rank 2.
2. **Specialization maps:** Two summands specialize via the two embeddings $K \hookrightarrow E$. The families $c_1, c_2$ are projections of a single global class $\mathbf{c}(t)$.
3. **Lift ambiguity:** Local modifications parametrized by $H^1_f(F_p, V)$; ambiguity in $\delta$ is $c_0 \wedge H^1_f$.
4. **Transition law:** $\sigma$ interchanges summands; $\delta \mapsto -\delta$, so $\delta \cdot \sigma(\delta) = -\delta^2$ is a norm (correct Euler factor).

## Failure Conditions

1. **Rank-one collapse:** $c_1 \wedge c_2 = 0$ for all $t$ (representation too small).
2. **Arbitrary dependence:** quotient by $c_0 \wedge H^1_f$ is zero (object ill-defined).
3. **Wrong target:** $\delta \notin \operatorname{im}(\bigwedge^2 H^1_f(F, V) \to \bigwedge^2 H^1(F_p, V))$ (no global existence).
4. **Wrong Euler factors:** transition involves $\alpha^2$ with no involution correction.

## References

- Burns, Kurihara, Sano. *On equivariant Euler systems for CM motives.* arXiv:1910.07404.
- Burns, Kurihara, Sano. *Stark elements and higher rank Euler systems.* arXiv:1805.08448.
- Kato. *p-adic Hodge theory and values of zeta functions of modular forms.* Astérisque 295 (2004).
