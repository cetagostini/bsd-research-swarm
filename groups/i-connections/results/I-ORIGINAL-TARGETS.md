# Directions 41–49: Original Work Targets for BSD Rank 2

**Status:** These directions identify research targets where a genuine new contribution is possible. Each direction states what is known, what is missing, and what would constitute a real result—not a survey, not a restatement, but an original mathematical statement with proof or formalization.

**Achievability key:**
- **Green**: A well-prepared graduate student or postdoc could plausibly produce this within 6–12 months.
- **Yellow**: Requires expertise in a specific area; plausible within 1–2 years with focused effort.
- **Red**: Major open problem; contribution would be incremental, not a complete resolution.

---

## Direction 41: Higher-Rank p-Converse in Restricted Setting

### Achievability: Yellow

### What's known

The **p-converse theorem** (for rank ≤ 1) is proven:
- **Skinner–Urban (2014):** Under good ordinary reduction at p, residual surjectivity of $\bar\rho_{E,p}$, and $p \nmid 6 \cdot |E_{\text{tor}}(\mathbb{Q})|$: if $L(E,1) \neq 0$, then $\operatorname{rank} E(\mathbb{Q}) = 0$ and $|\Sha(E)[p^\infty]| < \infty$. Conversely, if $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \cong \mathbb{Z}_p$ (Selmer rank 1), then $\operatorname{ord}_{s=1} L(E,s) = 1$.
- **Castella (2017), Wan (2014):** Extended p-converse to supersingular primes via plus/minus Selmer groups.
- **Gross–Zagier + Kolyvagin:** Gives rank 1 ⟹ analytic rank 1 unconditionally for all E/Q.

The **analytic rank 2 case** is essentially open. We have:
- **Kolyvagin's Euler system:** Only produces one independent point (Heegner point). Cannot bound the Selmer group when the Mordell–Weil rank is ≥ 2.
- **Kim's Kurihara numbers:** For rank 2, Kim constructs normalized elements in the semilocal Selmer group and extracts Fitting-ideal information, but this requires knowing that the global Selmer rank is 2 as input—it does not *prove* it from analytic data.
- **Castella–Wan:** Recent work on generalized Kato classes produces elements in $H^1_f$ at auxiliary primes, but the nonvanishing required to bootstrap to a full rank-2 Selmer bound is unproven.

### What's missing

The **unproved implication** is:

> **(Hypotheses:** $E/\mathbb{Q}$ with good ordinary reduction at $p \geq 5$, $\bar\rho_{E,p}: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{F}_p)$ surjective, $p \nmid 6 \cdot |E_{\text{tor}}(\mathbb{Q})|$.
>
> **If** $\operatorname{ord}_{s=1} L(E,s) = 2$ (i.e., $L(E,1) = L'(E,1) = 0$, $L''(E,1) \neq 0$),
>
> **then** $\operatorname{rank} E(\mathbb{Q}) = 2$ and $|\Sha(E)[p^\infty]| < \infty$.)

No current method proves this. The p-converse for Selmer rank 1 uses the fact that the $\Lambda$-adic Selmer group has rank 1 and Kolyvagin controls the quotient. For rank 2, there is no analogue of Kolyvagin's argument, and the Euler system of Rankin–Selberg convolutions (used by Skinner–Urban) only gives divisibility in one direction.

### What would constitute a genuine contribution

1. **A conditional p-converse for Selmer rank 2** under an explicit nonvanishing hypothesis on a generalized Kato class or Beilinson–Kato element. State: "If [explicit class] $\neq 0$ in $H^1_f(\mathbb{Q}, V_p(E))$, then $\operatorname{rank} E(\mathbb{Q}) \geq 2$." This is currently absent from the literature even as a conditional statement with a named hypothesis.

2. **A computation** showing that for 389.a1 at $p = 5$, the relevant Kato class or generalized Kato element is nonzero (even modulo $p$). This would be the first verification that the rank-2 machinery produces a concrete nonzero element for a specific curve.

3. **An impossibility argument:** Show that the existing Euler system framework (Rubin's formalism) provably cannot detect rank ≥ 2 without new input. This is widely believed but never formally demonstrated.

### Obstacle analysis

The fundamental obstacle is that Kolyvagin's method bounds the Selmer group *from above* given one cohomology class. For rank 2, we need two independent classes, and no Euler system is known to produce them. The generalized Kato classes (Castella, Howard) live in the correct Selmer group but their nonvanishing is only known under parity (root number $-1$, which forces odd analytic rank). For root number $+1$ (the generic case for rank 2), no nonvanishing result exists.

---

## Direction 42: Complex Leading-Term Comparison

### Achievability: Yellow

### What's known

The **BSD formula** predicts:

$$\frac{L''(E,1)}{2!} = \frac{\Omega^+(E) \cdot \operatorname{Reg}(E) \cdot |\Sha(E)| \cdot \prod c_p}{|E_{\text{tor}}(\mathbb{Q})|^2}$$

where $\operatorname{Reg}(E) = \det(\hat{h}(P_i, P_j))$ is the real regulator (Néron-Tate height pairing determinant).

The **Iwasawa Main Conjecture** (Skinner–Urban 2014, conditional on Selmer hypotheses) gives:

$$\operatorname{char}_\Lambda(X(E/\mathbb{Q}_\infty)) = (L_p(E, T))$$

where $L_p(E, T) \in \mathbb{Z}_p[[T]]$ is the p-adic L-function. Specializing at $T = 0$:

$$L_p(E, 0) = \left(1 - \frac{a_p}{p}\right)^{-1} \cdot \frac{L(E,1)}{\Omega_p(E)}$$

This connects the *value* $L(E,1)$ to the *order* of the Selmer group (via the characteristic ideal), but does not directly connect $L''(E,1)$ to the *regulator*.

### What's missing

The missing statement is:

> **The p-adic BSD formula (Perrin-Riou, Schneider):** Under the IMC and $\mu = 0$:
>
> $$L_p''(E, 0) = \mathscr{E}_p(E) \cdot \frac{L''(E,1)}{2! \cdot \Omega^+(E)} \cdot \frac{|\Sha(E)[p^\infty]| \cdot \operatorname{Reg}_p(E)}{|E_{\text{tor}}|^2}$$
>
> where $\mathscr{E}_p(E)$ is an explicit Euler-like factor and $\operatorname{Reg}_p(E)$ is the p-adic regulator.

**What is NOT automatic from the IMC:**

1. **Rationality of $L''(E,1)/\Omega$:** The IMC identifies the characteristic ideal of the Selmer group with the ideal generated by $L_p(E,T)$. This controls the *order of vanishing* of $L_p$ at $T=0$ and the *valuation* of the leading coefficient. But it does not, by itself, prove that $L''(E,1)/\Omega^+(E) \in \mathbb{Q}$. The integrality/rationality statement requires a comparison between the archimedean period $\Omega^+$ and the p-adic period $\Omega_p$, which is a separate result (the Gross period relation, known for modular forms but requiring explicit verification).

2. **Integrality:** Even given rationality, the IMC gives the p-adic valuation of $L_p''(E,0)$ but not its archimedean size. The statement "$L''(E,1)/(2! \cdot \Omega^+) \in \mathbb{Q}$ and its denominator is bounded by $|E_{\text{tor}}|^2 / \prod c_p$" requires the full BSD formula, which is what we're trying to prove.

3. **Comparison of regulators:** The real regulator $\operatorname{Reg}(E) = \det(\hat{h}_\infty(P_i,P_j))$ and the p-adic regulator $\operatorname{Reg}_p(E) = \det(\hat{h}_p(P_i,P_j))$ are defined using different height pairings. Their ratio $\operatorname{Reg}(E)/\operatorname{Reg}_p(E)$ involves the p-adic period $\Omega_p$ and the Colmez–Gross relation, which is proven for CM curves but open in general.

### What would constitute a genuine contribution

1. **An explicit verification** that for 389.a1 at $p = 5$, the ratio $L''(E,1)/(2! \cdot \Omega^+)$ is rational with denominator dividing $|E_{\text{tor}}|^2 / \prod c_p$. This is a computation, not a theorem, but it would be the first such verification for a rank-2 curve using *independent* methods (not assuming BSD).

2. **A proof** that for curves satisfying the Skinner–Urban hypotheses, the p-adic leading term $L_p''(E,0)$ determines the real leading term $L''(E,1)$ up to an explicit factor involving $\Omega_p/\Omega^+$ and the Euler factor $\mathscr{E}_p$. This is known in principle (Perrin-Riou's regulator map does this) but has never been made fully explicit for a rank-2 curve.

3. **A formalization** of the statement: "IMC + $\mu = 0$ + rationality of $L''/\Omega$ ⟹ BSD leading coefficient formula." This is a logical implication, not a computation, and formalizing it would clarify exactly which inputs are needed.

### Obstacle analysis

The deep issue is that the IMC is a statement about the *p-adic* L-function, while the BSD formula involves the *archimedean* L-function. The interpolation property of $L_p$ relates $L_p(E,0)$ to $L(E,1)/\Omega_p$, but for the second derivative, the comparison involves the p-adic regulator, which is a different object from the real regulator. The Colmez–Gross formula (relating p-adic and archimedean heights for CM points) is proven, but no analogous result exists for non-CM curves.

---

## Direction 43: Finite Prime Support for Sha

### Achievability: Red

### What's known

**Finiteness of $\Sha(E)[p^\infty]$ for a fixed $E$ and all $p$:**

- **Kolyvagin (1990):** If $\operatorname{rank} E(\mathbb{Q}) \leq 1$ and $L(E,1) \neq 0$ or $L'(E,1) \neq 0$ (Gross–Zagier condition), then $\Sha(E)$ is finite. This gives finiteness of $\Sha(E)[p^\infty]$ for *all* primes $p$ simultaneously.
- **Skinner–Urban (2014):** Under their hypotheses (good ordinary at $p$, residual surjectivity), $\Sha(E)[p^\infty]$ is finite. But this is proven *prime by prime*, not uniformly.

**What we don't know:** For a fixed curve $E$ with $\operatorname{rank} E(\mathbb{Q}) \geq 2$, we cannot prove $\Sha(E)[p^\infty] = 0$ (or even finite) for *any* single prime $p$, let alone all but finitely many.

### What's missing

The target theorem would be:

> **Conjecture:** For a fixed elliptic curve $E/\mathbb{Q}$, the set
> $$\{p \text{ prime} : \Sha(E)[p^\infty] \neq 0\}$$
> is finite.

This is *not* a consequence of the IMC (which handles one prime at a time) nor of modularity (which gives the functional equation but not Sha finiteness). It is an independent statement about the global arithmetic of $E$.

**What could bound those primes:**

1. **The conductor $N_E$:** Every element of $\Sha(E)[p]$ gives a torsor $X$ of period $p$ that is locally trivial everywhere. The torsor $X$ is a curve of genus 1 with a map to $E$ of degree $p$. By Faltings' theorem (Mordell conjecture for curves of genus ≥ 2), the number of such torsors is finite for each $p$, but this doesn't bound $p$ itself.

2. **The discriminant $\Delta_E$:** For $p > |\Delta_E|$, one might expect that $\Sha(E)[p] = 0$ for local reasons (the curve has good reduction at all primes not dividing $\Delta_E$, and the local conditions become vacuous). This is not proven.

3. **The Cassels–Tate pairing:** The pairing is alternating, so $|\Sha(E)[p]| = p^{2k}$. For $p$ large enough that $E[p]$ is irreducible as a $G_\mathbb{Q}$-module, one expects $\Sha(E)[p] = 0$, but this is only proven under additional hypotheses (e.g., $p$ does not divide the Tamagawa numbers).

### What would constitute a genuine contribution

1. **A proof that $\Sha(E)[p] = 0$ for all $p > B(E)$** for some explicit bound $B(E)$ depending on $E$. Even a conditional result (assuming the IMC at all primes) would be new.

2. **A proof that the number of primes $p$ with $\Sha(E)[p] \neq 0$ is bounded** by a function of the conductor $N_E$ (e.g., $\leq \omega(N_E) + C$ for some absolute constant $C$). This would connect Sha to the arithmetic complexity of $E$.

3. **A computational verification** that for 389.a1, $\Sha(E)[p^\infty] = 0$ for all primes $p$ (not just $p = 2, 3, 5$). This requires controlling the Selmer group at all primes simultaneously, which is a major computational challenge.

### Obstacle analysis

The fundamental obstacle is that existing methods (Euler systems, Iwasawa theory) work *one prime at a time*. There is no known global argument that controls $\Sha$ at all primes simultaneously. The function field analogue (Artin–Tate) proves finiteness of $\Sha$ using the Brauer group of a surface, but the number field analogue (the Arakelov Brauer group) is not well-understood.

---

## Direction 44: Remove One Hypothesis

### Achievability: Green–Yellow

### What's known

The Skinner–Urban p-converse theorem has the following hypotheses:
1. $E/\mathbb{Q}$ has **good ordinary reduction at $p$**.
2. The residual representation $\bar\rho_{E,p}: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{F}_p)$ is **surjective**.
3. $p \nmid 6 \cdot |E_{\text{tor}}(\mathbb{Q})|$.
4. $p \geq 5$.

Each hypothesis is used in a specific part of the proof:
- **(1) Good ordinary:** Required for the construction of the $\Lambda$-adic Selmer group and the control theorem relating $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ to $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^{\Gamma}$. For supersingular primes, the Selmer group has a different structure (Kobayashi's plus/minus Selmer groups).
- **(2) Residual surjectivity:** Used to ensure that the Galois representation $\rho_{E,p}$ is "large enough" for the Taylor–Wiles method to work. Specifically, it ensures that $H^2(\mathbb{Q}, \operatorname{ad}^0 \bar\rho_{E,p}) = 0$, which is needed for the deformation ring to be well-behaved.
- **(3) $p \nmid |E_{\text{tor}}|$:** Ensures that the Kummer map $E(\mathbb{Q})/p \hookrightarrow H^1(\mathbb{Q}, E[p])$ is injective, so the Selmer group correctly reflects the Mordell–Weil group.
- **(4) $p \geq 5$:** Technical condition for the Fontaine–Laffaille theory to apply at $p$.

### What's missing

The most tractable hypothesis to remove is **(1) good ordinary reduction**, because:

- **Castella (2017) and Wan (2014)** have already extended the p-converse to supersingular primes using Kobayashi's plus/minus Selmer groups. The supersingular case is now understood (though the proof is different, not a simple removal of the hypothesis).

- The harder target is removing **(2) residual surjectivity**. This is used in the Taylor–Wiles method to ensure that the universal deformation ring is a power series ring. When $\bar\rho_{E,p}$ is not surjective (e.g., when the image is contained in a Borel subgroup), the deformation ring has more complicated structure, and the Taylor–Wiles method requires modification.

**The exact place where residual surjectivity is used:**

In the Skinner–Urban proof, the key input from the Taylor–Wiles method is:

> The Hecke algebra $\mathbb{T}$ acting on the space of modular forms is isomorphic to the universal deformation ring $R$ of $\bar\rho_{E,p}$.

This isomorphism requires $H^2(\mathbb{Q}, \operatorname{ad}^0 \bar\rho_{E,p}) = 0$, which follows from residual surjectivity (by a group cohomology argument). When $\bar\rho_{E,p}$ is not surjective, $H^2 \neq 0$ in general, and the deformation ring $R$ may have relations. The Taylor–Wiles method can still work (Diamond, Fujiwara, Kisin), but the output is weaker: instead of $R \cong \mathbb{T}$, one gets a surjection $R \twoheadrightarrow \mathbb{T}$ with possibly nontrivial kernel.

### What would constitute a genuine contribution

1. **Remove residual surjectivity for a specific family:** For example, prove the p-converse for curves with $\bar\rho_{E,p}$ having image contained in a Borel subgroup (i.e., $E$ has a $p$-isogeny). This is a concrete, well-defined case where the Taylor–Wiles method fails but the arithmetic might still be accessible.

2. **Reduce the $p$-converse to a purely Galois-theoretic statement:** State: "If $H^1_f(\mathbb{Q}, V_p(E))$ has $\mathbb{Z}_p$-rank $\geq 2$, then $\operatorname{ord}_{s=1} L(E,s) \geq 2$, *without* assuming residual surjectivity." This would be a genuinely new result, even if the proof uses the IMC.

3. **Identify exactly which curves fail the residual surjectivity hypothesis** and verify the p-converse computationally for those curves. This is a finite computation for each $p$ (the moduli of curves with non-surjective $\bar\rho_{E,p}$ is known).

### Obstacle analysis

The Taylor–Wiles method is the bottleneck. Without residual surjectivity, the method produces a weaker isomorphism, and the control of the Selmer group is correspondingly weaker. Alternative approaches (e.g., Kolyvagin's Euler systems) don't require residual surjectivity but are limited to rank ≤ 1.

---

## Direction 45: Transfer Across Isogeny

### Achievability: Green

### What's known

Let $\phi: E \to E'$ be an isogeny of elliptic curves over $\mathbb{Q}$. The following are **isogeny-invariant** (i.e., the same for $E$ and $E'$):

1. **The L-function:** $L(E, s) = L(E', s)$ (by modularity and the fact that isogenous curves have the same conductor and the same local factors at all primes).
2. **The root number:** $w_E = w_{E'}$.
3. **The rank:** $\operatorname{rank} E(\mathbb{Q}) = \operatorname{rank} E'(\mathbb{Q})$ (by the Mordell–Weil theorem and the fact that $\phi$ induces an injection $E(\mathbb{Q})/\text{tors} \hookrightarrow E'(\mathbb{Q})/\text{tors}$ of finite index).
4. **The parity of $|\Sha|$:** The Cassels–Tate pairing shows $|\Sha(E)| / |\Sha(E')| = (\deg \phi)^2 \cdot (\text{index})^2$ up to local factors.

The following are **NOT isogeny-invariant** (they change):

1. **The periods:** $\Omega^+(E) \neq \Omega^+(E')$ in general; the ratio involves $\deg \phi$.
2. **The Tamagawa numbers:** $c_p(E) \neq c_p(E')$ in general.
3. **The torsion subgroup:** $|E_{\text{tor}}(\mathbb{Q})| \neq |E'_{\text{tor}}(\mathbb{Q})|$ in general.
4. **The Sha group itself:** $\Sha(E)$ and $\Sha(E')$ are not isomorphic in general (though their orders are related).

### What's missing

**The exact tracking of how Selmer information changes under isogeny:**

Given $\phi: E \to E'$ of degree $d$, the induced map on Selmer groups:

$$\phi_*: \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \to \operatorname{Sel}_{p^\infty}(E'/\mathbb{Q})$$

has kernel and cokernel controlled by:

$$0 \to E'(\mathbb{Q})[\hat\phi] \to \operatorname{Sel}_{p^\infty}(E[\hat\phi]/\mathbb{Q}) \to \operatorname{Sel}_{p^\infty}(E'/\mathbb{Q})[\phi] \to 0$$

What is missing is:

1. **An explicit formula** for the ratio $|\Sha(E)[p^\infty]| / |\Sha(E')[p^\infty]|$ in terms of local data (Tamagawa numbers, torsion, index). This is known in principle (it follows from the BSD formula, assuming BSD), but an *unconditional* formula (not assuming BSD) is not in the literature.

2. **The behavior of the Cassels–Tate pairing under isogeny:** The pairing on $\Sha(E)$ and the pairing on $\Sha(E')$ are related by the isogeny, but the exact relationship involves the "transgression" map in the long exact sequence. This has been worked out in special cases (e.g., Cassels 1964 for 2-isogenies) but not in full generality.

3. **The change in the p-adic regulator under isogeny:** The real regulator changes by a factor involving $\deg \phi$ and the index. The p-adic regulator changes differently (involving the p-adic period ratio). Tracking this exactly would clarify the p-adic BSD formula.

### What would constitute a genuine contribution

1. **An unconditional formula** for $|\Sha(E)[p^\infty]| / |\Sha(E')[p^\infty]|$ in terms of local data, for a specific isogeny (e.g., a 2-isogeny or 3-isogeny). This would be a new result, not requiring BSD.

2. **A computation** tracking how the 2-descent data for 389.a1 changes under a specific isogeny. This would demonstrate the isogeny transfer concretely.

3. **A formalization** of the isogeny invariance of the L-function and rank, including the explicit formulas for how periods, Tamagawa numbers, and torsion change.

### Obstacle analysis

The obstacle is not conceptual but computational: the formulas for how Sha changes under isogeny are known in principle (they follow from the BSD formula) but are rarely made explicit. The unconditional version (not assuming BSD) requires controlling the kernel and cokernel of the isogeny map on Selmer groups, which is a standard homological algebra exercise—but one that hasn't been carried out systematically.

---

## Direction 46: Parameterized Descent Theorem

### Achievability: Yellow

### What's known

**Families of elliptic curves with two rational sections:**

Consider the Legendre family $E_\lambda: y^2 = x(x-1)(x-\lambda)$ or a similar 1-parameter family. For generic $\lambda$, $\operatorname{rank} E_\lambda(\mathbb{Q}(\lambda)) = 1$ (the generic rank is 1, generated by a section). For special values of $\lambda$, the rank can jump.

**What's known about specialization:**
- **Silverman's specialization theorem:** For a nonconstant family $E \to \mathbb{A}^1$ with generic rank $r$, the set $\{t \in \mathbb{Z} : \operatorname{rank} E_t(\mathbb{Q}) \geq r\}$ is infinite (Silverman 1983). Moreover, $\operatorname{rank} E_t(\mathbb{Q}) \geq r$ for all but finitely many $t$.
- **Néron–Tate height comparison:** The canonical height of a section specializes to the canonical height of the specialized point, up to an error controlled by the discriminant.

**What's known about rank 2 in families:**
- If the generic rank is 2 (i.e., $E(\mathbb{Q}(t))$ has rank 2), then by Silverman, $\operatorname{rank} E_t(\mathbb{Q}) \geq 2$ for all but finitely many $t$. But constructing such a family with *proven* generic rank 2 is nontrivial.
- **Shioda (1990s):** Constructed families of elliptic surfaces with high rank, but over $\mathbb{Q}(t)$, not $\mathbb{Q}$.

### What's missing

The target result:

> **Theorem (Parameterized Descent).** Let $\pi: \mathcal{E} \to \mathbb{A}^1$ be a family of elliptic curves over $\mathbb{Q}$ with two independent sections $P(t), Q(t) \in \mathcal{E}(\mathbb{Q}(t))$. For a specialization $t = t_0 \in \mathbb{Z}$:
>
> 1. $P(t_0), Q(t_0) \in E_{t_0}(\mathbb{Q})$ are independent if $\hat{h}(P(t_0)) \hat{h}(Q(t_0)) - \hat{h}(P(t_0), Q(t_0))^2 > 0$.
> 2. The 2-Selmer group $\operatorname{Sel}_2(E_{t_0}/\mathbb{Q})$ has dimension $\geq 2$.
> 3. If $\dim \operatorname{Sel}_2(E_{t_0}/\mathbb{Q}) = 2$, then $\operatorname{rank} E_{t_0}(\mathbb{Q}) = 2$ and $\Sha(E_{t_0})[2] = 0$.

**What is missing from the literature:**

- Part (1) is standard (height pairing criterion).
- Part (2) requires the sections to remain independent modulo 2 and to pass all local conditions. This is a computation that can be done for specific families.
- Part (3) is the content of the **Selmer upper bound**: if the Selmer group has dimension exactly 2 and we have 2 independent points, then rank = 2 and Sha[2] = 0. This is elementary but requires *proving* that the Selmer group doesn't have extra elements from Sha.

**The honest statement:** We can prove rank ≥ 2 for specializations where the height pairing is positive definite. We *cannot* prove rank = 2 (i.e., Sha[2] = 0) without actually computing the Selmer group at each specialization. The parameterized descent theorem would automate this computation for a family, but the Selmer group depends on local data at each prime, which varies with $t_0$.

### What would constitute a genuine contribution

1. **An explicit family** with two proven independent sections and a computation showing that for 10+ specializations $t_0$, the Selmer group has dimension exactly 2 (hence rank = 2, Sha[2] = 0). This would be the first systematic verification of rank 2 in a parameterized family.

2. **A local-condition analysis:** For a specific family, determine the set of primes where the local Selmer conditions vary with $t_0$, and show that for "most" $t_0$, the local conditions are satisfied at all primes. This would give a positive-density result for rank-2 specializations.

3. **A formalization** of the statement: "Two independent sections + height pairing positive definite ⟹ rank ≥ 2." This is trivial but has never been formalized in a proof assistant.

### Obstacle analysis

The obstacle is that the Selmer group is not a continuous function of the parameter $t_0$. It jumps at primes of bad reduction and at primes where the local conditions change. Controlling these jumps is a finite computation for each $t_0$ but not easily parameterized.

---

## Direction 47: Restricted Visibility Result

### Achievability: Yellow

### What's known

**Visibility of Sha** (Cremona–Mazur 1997, Agashe–Stein 2005):

The idea: if $A$ is an abelian variety over $\mathbb{Q}$ that "covers" $E$ (i.e., there is a map $A \to E$), then elements of $\Sha(E)$ can sometimes be "seen" as elements of $\Sha(A)$, which is easier to compute.

**The visibility exact sequence:**

$$0 \to \Sha(A)[N] \to \Sha(A \times E)[N] \to \Sha(E)[N] \to H^1(\mathbb{Q}, A[N]) \to \cdots$$

More precisely, for an abelian subvariety $B \subset J_0(N)$ (the Jacobian of the modular curve $X_0(N)$) and an elliptic curve $E$ that is a quotient of $B$, there is an exact sequence:

$$0 \to \Sha(B) \to \Sha(J_0(N)) \to \Sha(E) \to 0$$

(up to issues with the kernel of the map $B \to E$).

**What's proven:**
- Agashe–Stein (2005): For specific curves, elements of $\Sha(E)$ have been "explained" by visibility in $J_0(N)$. For example, the curve 571a1 has $|\Sha| = 9$, and all 9 elements are visible in $J_0(571)$.
- Cremona–Mazur (1997): Constructed examples of Sha elements using visibility in Jacobians of modular curves.

**What's NOT proven:**
- Visibility does not automatically exhaust $\Sha$. There may be elements of $\Sha(E)$ that are not visible in any known abelian variety.
- The visibility method is *constructive*: it produces elements of $\Sha$ but does not prove that *all* elements are obtained this way.

### What's missing

The target result:

> **Theorem (Restricted Visibility).** Let $E/\mathbb{Q}$ be a curve of conductor $N$. Let $B \subset J_0(N)$ be an abelian subvariety with a surjection $\pi: B \twoheadrightarrow E$. Then:
>
> 1. **Injectivity:** The map $\Sha(B)[\deg \pi] \to \Sha(E)[\deg \pi]$ is injective (under suitable hypotheses on the kernel of $\pi$).
> 2. **Local triviality:** Every element of $\Sha(B)$ that maps to a nonzero element of $\Sha(E)$ is locally trivial at all primes (by definition of Sha).
> 3. **Non-exhaustion:** In general, $\Sha(B) \to \Sha(E)$ is NOT surjective. The cokernel is controlled by $H^1(\mathbb{Q}, \ker \pi)$.

**What is missing from the literature:**

- Part (1) is known under suitable hypotheses (Agashe–Stein, Theorem 4.1).
- Part (2) is the definition of Sha.
- Part (3) is the key: quantifying the cokernel. For a specific curve $E$, we want to know: what fraction of $\Sha(E)$ is visible in $B$? Is the cokernel trivial?

### What would constitute a genuine contribution

1. **For 389.a1:** Construct the Jacobian $J_0(389)$ and an abelian subvariety $B$ mapping to $E$. Compute $\Sha(B)[p]$ for $p = 2, 3, 5$ and verify that the image in $\Sha(E)[p]$ is the full group. This would prove $\Sha(E)[p] = 0$ for those $p$ by visibility (if $\Sha(B)[p] = 0$).

2. **A general criterion:** Prove that if $\Sha(B)[p] = 0$ and the kernel of $\pi: B \to E$ has no $p$-torsion, then $\Sha(E)[p] = 0$. This is a conditional result but would reduce Sha vanishing for $E$ to Sha vanishing for $B$.

3. **A computation** showing that for a specific curve, the visibility method accounts for all of $\Sha$. This requires computing $\Sha(B)$ and showing that the map to $\Sha(E)$ is surjective.

### Obstacle analysis

The obstacle is that visibility is a *sufficient* condition for Sha vanishing, not a *necessary* one. There is no guarantee that $\Sha(E)$ is fully visible in any known abelian variety. For curves of large conductor (like 389.a1), the Jacobian $J_0(N)$ is a very high-dimensional abelian variety, and computing its Sha is extremely difficult.

---

## Direction 48: Family-Level Selmer Distribution

### Achievability: Yellow

### What's known

**Average rank in families:**
- **Bhargava–Shankar (2015):** The average rank of all elliptic curves over $\mathbb{Q}$ (ordered by height) is at most 1.5 (later improved to 1.17). This is an *average* result, not a pointwise one.
- **Dokchitser–Dokchitser (2010):** For the family of quadratic twists $E_d$ of a fixed curve $E$, the root numbers $w_{E_d}$ are equidistributed (under mild hypotheses). This gives the parity distribution.

**Average Selmer rank:**
- **Smith (2022):** Proved that the average 2-Selmer rank in the family of all elliptic curves over $\mathbb{Q}$ is 3. This implies that the average rank is at most 3 (a weak bound, but unconditional).
- **Klagsbrun–Mazur–Rubin (2014):** For the family of quadratic twists of a fixed curve with root number $-1$, the average 2-Selmer rank is 1, implying that "most" twists have rank 1.

### What's missing

The target result:

> **Theorem (Family-Level Selmer Distribution).** Let $\mathcal{F}$ be an explicit family of elliptic curves (e.g., all curves of conductor $N$ with $N \leq X$, or all twists $E_d$ of a fixed curve). Let $S_r$ be the set of curves in $\mathcal{F}$ with $\operatorname{Sel}_2(E/\mathbb{Q}) \cong (\mathbb{Z}/2)^r$. Then:
>
> 1. $\lim_{X \to \infty} \frac{|S_2 \cap \mathcal{F}_{\leq X}|}{|\mathcal{F}_{\leq X}|} = c_2$
>
> for an explicit constant $c_2 > 0$.

**What is missing:**

- **Individual finiteness vs. average:** An average-size result (e.g., "the average 2-Selmer rank is 3") does NOT imply that any specific curve has Selmer rank 2. The distribution could be concentrated at ranks 0 and 6, with no curves of rank 2.
- **The exact local conditions:** For a family of curves, the local Selmer conditions at each prime $p$ depend on the reduction type of $E$ at $p$. For the family of all curves of conductor $\leq X$, the reduction type varies, and the local conditions are hard to control uniformly.
- **The proved counting argument:** Bhargava–Shankar's method counts orbits of prehomogeneous vector spaces, which gives the average size of the Selmer group but not its distribution.

### What would constitute a genuine contribution

1. **An explicit family** (e.g., twists of 389.a1) where the 2-Selmer rank is computed for all twists $|d| \leq D$ (say $D = 10^4$), and the distribution is shown to match a predicted formula. This would be computational evidence for a family-level result.

2. **A local-condition analysis:** For the family of twists $E_d$ of 389.a1, determine the local Selmer conditions at all primes dividing $d$ and show that they are satisfied for a positive proportion of $d$. This would give a lower bound on the proportion of twists with Selmer rank 2.

3. **A formalization** of the statement: "If the local Selmer conditions are satisfied at all primes, then the 2-Selmer group has rank ≤ 2 + (number of bad primes)." This is a standard result but has never been formalized.

### Obstacle analysis

The obstacle is that Selmer rank is not a *local* property. It depends on global arithmetic (the Mordell–Weil group and Sha), which is not determined by local data. Average results (Bhargava–Shankar) control the *expectation* but not the *variance*, and the variance is what determines the proportion of curves with a specific Selmer rank.

---

## Direction 49: Formalize Arithmetic Certificate Checker

### Achievability: Green

### What's known

**Formalization of number theory in Lean 4:**

- **Lean 4 + Mathlib:** Contains formalizations of algebraic number theory (rings of integers, ideals, class groups), group cohomology (basic definitions), and elliptic curves (Weierstrass equations, group law, torsion).
- **Perfectoid spaces (Scholze's theorem):** Formalized in Lean by Buzzard et al. (2024). This is a major achievement but does not directly help with BSD.
- **L-functions:** Basic definitions formalized, but analytic continuation and functional equation are NOT formalized.

**What's formalized for elliptic curves:**
- Weierstrass equations, discriminant, j-invariant
- The group law on $E(\mathbb{Q})$
- Torsion subgroups (basic structure)
- **NOT formalized:** 2-descent, Selmer groups, Sha, Cassels–Tate pairing, heights, regulators

**What's formalized for 2-descent:**
- The 2-descent map $E(\mathbb{Q})/2E(\mathbb{Q}) \hookrightarrow \mathbb{Q}^\times / (\mathbb{Q}^\times)^2 \times \mathbb{Q}^\times / (\mathbb{Q}^\times)^2$ is a standard construction, but it has not been formalized in any proof assistant.
- The local conditions for the 2-Selmer group (Hilbert symbols, Legendre symbols) are computable but not formalized.

### What's missing

The target:

> **A Lean 4 formalization** of the following:
>
> 1. **Local certificate format:** A data structure representing a local solubility certificate for a 2-descent covering, including:
>    - The homogeneous space $C: dw^2 = a + bt^2 + ct^4$
>    - For each prime $p$, a point $(w, t) \in \mathbb{Q}_p$ with $C(w, t) = 0$
>    - At $p = \infty$, a real point
>
> 2. **Certificate verifier:** A Lean function that, given a local certificate, verifies:
>    - The point satisfies the equation (mod $p^k$ for suitable $k$)
>    - The Hilbert symbol conditions are satisfied
>    - The class is in the image of the 2-descent map
>
> 3. **Descent data structure:** A Lean structure representing a 2-descent on $E/\mathbb{Q}$, including:
>    - The 2-isogeny $\phi: E \to E'$ (if it exists)
>    - The descent map $\delta: E(\mathbb{Q})/2E(\mathbb{Q}) \to \mathbb{Q}^\times / (\mathbb{Q}^\times)^2$
>    - The Selmer group $\operatorname{Sel}_2(E/\mathbb{Q})$ as a subset of $\mathbb{Q}^\times / (\mathbb{Q}^\times)^2$

**What is NOT the same as a formalization of the abstract exact-sequence lemma:**

The abstract statement "there is an exact sequence $0 \to E(\mathbb{Q})/2 \to \operatorname{Sel}_2 \to \Sha[2] \to 0$" is a *definition*, not a theorem. It can be formalized trivially by defining $\operatorname{Sel}_2$ as the kernel of the localization map and $\Sha[2]$ as the cokernel. What is hard is:

1. **Computing** $\operatorname{Sel}_2$ for a specific curve (this requires actual arithmetic).
2. **Verifying** that a given set of classes is the full Selmer group (this requires checking all local conditions).
3. **Proving** that $\Sha[2] = 0$ (this requires showing that every locally trivial class is globally trivial).

### What would constitute a genuine contribution

1. **A Lean 4 formalization** of the 2-descent map for a curve with a 2-isogeny (e.g., $E: y^2 = x^3 + ax^2 + bx$ with the 2-isogeny $(x, y) \mapsto (x^2/b, y(x^2-b)/b\sqrt{b})$). This is a self-contained formalization project that would produce a reusable library.

2. **A formalization of the local solubility test** for a binary quartic form $ax^4 + bx^2 + c$ over $\mathbb{Q}_p$. This is the core of the 2-Selmer group computation and is well-suited to formalization (it's a finite computation for each $p$).

3. **A Lean 4 function** that, given an elliptic curve $E/\mathbb{Q}$ and a candidate 2-Selmer class (represented as a pair of rational numbers), verifies that the class satisfies all local conditions. This is a "certificate checker" that can be used to verify computational results.

### Obstacle analysis

The obstacle is not mathematical but engineering: formalizing 2-descent in Lean 4 requires:
- A formalization of the Hilbert symbol $(a, b)_p$ for all primes $p$ (including $p = 2$, which is the hardest case).
- A formalization of the 2-descent map, which involves solving conics over $\mathbb{Q}_p$.
- A formalization of the exact sequence relating $E(\mathbb{Q})/2$, $\operatorname{Sel}_2$, and $\Sha[2]$.

None of these are conceptually difficult, but they require significant effort in a proof assistant. The existing Mathlib infrastructure (algebraic number theory, group cohomology) provides a foundation, but the specific constructions needed for 2-descent are not yet built.

---

## Summary Table

| Dir | Title | Achievability | Key Gap | Novel Contribution |
|-----|-------|---------------|---------|-------------------|
| 41 | Higher-rank p-converse | Yellow | No Euler system for rank 2 | Conditional p-converse with explicit nonvanishing hypothesis |
| 42 | Leading-term comparison | Yellow | Rationality of $L''/\Omega$ not automatic from IMC | Explicit verification for 389.a1 or formalized implication |
| 43 | Finite prime support for Sha | Red | No global argument controls all primes | Proof that $\Sha(E)[p] = 0$ for $p > B(E)$ |
| 44 | Remove one hypothesis | Green–Yellow | Taylor–Wiles needs residual surjectivity | Remove surjectivity for curves with $p$-isogeny |
| 45 | Transfer across isogeny | Green | Formulas known in principle, not made explicit | Unconditional formula for $|\Sha(E)|/|\Sha(E')|$ |
| 46 | Parameterized descent | Yellow | Selmer group jumps with parameter | Explicit family with 10+ rank-2 specializations |
| 47 | Restricted visibility | Yellow | Visibility not guaranteed to exhaust Sha | Verify full visibility for 389.a1 |
| 48 | Family-level Selmer | Yellow | Average ≠ pointwise | Explicit counting for twists of 389.a1 |
| 49 | Certificate checker | Green | Engineering, not mathematics | Lean 4 formalization of 2-descent for 1-isogeny curve |

---

## Priority Recommendation

**Highest priority (achievable and novel):**

1. **Direction 49** (formalization): This is an engineering project, not a research problem, and can be completed in 6 months. It produces a reusable artifact (a Lean 4 library for 2-descent) that benefits the entire project.

2. **Direction 45** (isogeny transfer): This is a straightforward computation that produces explicit formulas. It has not been done systematically in the literature.

3. **Direction 44** (hypothesis removal): Identifying exactly where residual surjectivity is used and removing it for curves with $p$-isogenies is a well-defined problem with a clear path to a result.

**Medium priority (requires more effort):**

4. **Direction 46** (parameterized descent): Constructing an explicit family with 10+ rank-2 specializations requires careful computation but is feasible.

5. **Direction 41** (p-converse): Stating a conditional p-converse with an explicit nonvanishing hypothesis is a conceptual contribution, not a computational one.

**Lower priority (major open problems):**

6. **Directions 42, 43, 47, 48:** These involve major open problems (rationality of $L''/\Omega$, global Sha bounds, visibility exhaustion, family-level Selmer distribution) where a contribution would be incremental, not a complete resolution.
