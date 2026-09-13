# B-BURNS-EULER: Burns–Sakamoto–Sano and Bullach–Burns Euler System Machinery

## Sources

- **BSS:** Burns, Sakamoto, Sano. "On the theory of higher rank Euler, Kolyvagin and Stark systems, II." [arXiv:1805.08448](https://arxiv.org/abs/1805.08448), 2018. 51 pages.
- **BB:** Bullach, Burns. "On Euler systems and Nekovář–Selmer complexes." [arXiv:2509.13894](https://arxiv.org/abs/2509.13894), 2025 (revised 2026). 148 pages.

---

## 1. Burns–Sakamoto–Sano Theorem

### 1.1 What They Prove

BSS prove the **Mazur–Rubin conjecture** on the existence of a canonical "higher Kolyvagin derivative" homomorphism between modules of higher-rank Euler systems and higher-rank Kolyvagin systems.

**Main Theorem (Theorem 1.1 = Theorem 6.12 + Corollaries 6.13, 6.17).** There exists a canonical homomorphism of $R$-modules:

$$\mathcal{D}_r : \mathrm{ES}_r(T) \to \mathrm{KS}_r(A)$$

where:
- $\mathrm{ES}_r(T)$ = module of Euler systems of rank $r$ for $T$
- $\mathrm{KS}_r(A)$ = module of Kolyvagin systems of rank $r$ for $A = T/MT$
- Under mild additional hypotheses, $\mathcal{D}_r$ is **surjective**.

### 1.2 Exact Hypotheses

Fix:
- An odd prime $p$
- A number field $K$
- A continuous $G_K$-representation $T$ that is **free of finite rank** over a Gorenstein $\mathbb{Z}_p$-order $\mathcal{R}$
- A power $M$ of $p$; set $A := T/MT$, $R := \mathcal{R}/(M)$
- A finite set $S$ of places of $K$ containing $S_\infty(K) \cup S_p(K) \cup S_{\mathrm{ram}}(A)$
- "Standard hypotheses" on the Selmer structure (finite local conditions at all places, canonical Bloch–Kato conditions at $p$)

**Key structural requirements:**
1. $\mathcal{R}$ is a **Gorenstein order** (not merely a DVR — this is the generalization over Mazur–Rubin)
2. $T$ is $\mathcal{R}$-free of finite rank
3. The Selmer structure $\mathcal{F}$ satisfies standard running hypotheses (finiteness of local/global cohomology, existence of canonical dual Selmer structure $\mathcal{F}^*$)

**What is NOT required:**
- The coefficient ring need not be a DVR or principal ideal ring (it can be an arbitrary Gorenstein $\mathbb{Z}_p$-order)
- Leopoldt's conjecture is NOT needed (removed by BSS's canonical rank reduction)
- No "stub system" hypothesis (overcome via exterior power biduals)

### 1.3 Conclusions About Selmer Modules

**Theorem 1.2 (= Theorem 5.2).** Under standard hypotheses:

(i) $\mathrm{KS}_r(A)$ is **free of rank one** over $R$.

(ii) For each $\kappa \in \mathrm{KS}_r(A)$ and each $i \geq 0$:
$$I_i(\kappa) \subseteq \mathrm{Fitt}_R^i(\mathrm{Sel}(A))$$
where $\mathrm{Sel}(A) = H^1_{\mathcal{F}^*}(K, A^*(1))^*$ is the dual Selmer module, and $I_i(\kappa)$ is a canonical ideal associated to $\kappa$.

(iii) If $R$ is a **principal ideal ring** and $\kappa$ is a basis of $\mathrm{KS}_r(A)$, then:
$$I_i(\kappa) = \mathrm{Fitt}_R^i(\mathrm{Sel}(A))$$

**Combined conclusion (Theorem 1.3).** For any Euler system $c \in \mathrm{ES}_r(T)$:
$$I_i(\kappa(c)) \subseteq \mathrm{Fitt}_R^i(\mathrm{Sel}(A))$$

and if $R$ is a principal ideal ring:
$$\langle I_i(\kappa(c)) \mid c \in \mathrm{ES}_r(T) \rangle_R = \mathrm{Fitt}_R^i(\mathrm{Sel}(A))$$

This means **all higher Fitting ideals** of the Selmer module are determined by the Euler system.

### 1.4 Application: Rubin–Stark Elements (Theorem 1.5 = Theorem 7.1)

For a one-dimensional $p$-adic character $\chi$ of $G_K$ of finite prime-to-$p$ order, with $L = K^{\ker(\chi)}$ and $r$ = number of archimedean places of $K$: assuming all archimedean places split in $L$, no $p$-adic place splits in $L$, and $\chi$ is neither trivial nor Teichmüller:

$$\langle I_i(\kappa(c)) \mid c \in \mathrm{ES}_r(T_\chi) \rangle_\mathcal{O} = \mathrm{Fitt}_\mathcal{O}^i\left((\mathbb{Z}_p \otimes_\mathbb{Z} \mathrm{Cl}(\mathcal{O}_L))^\chi\right)$$

This determines **all higher Fitting ideals of the $\chi$-part of the $p$-adic class group** from Rubin–Stark elements — unconditionally, without Leopoldt's conjecture.

---

## 2. Bullach–Burns Theorem

### 2.1 What They Prove

BB develop a theory of Euler and Kolyvagin systems **relative to Nekovář–Selmer complexes** over local complete Gorenstein rings. Their theory is:
- **Finer** than both Mazur–Rubin (over DVRs) and Sakamoto et al. (over Gorenstein rings)
- **Requires fewer hypotheses**
- **Allows Greenberg local conditions** (beyond the classical "relaxed" conditions)

### 2.2 How It Extends Burns–Sakamoto–Sano

| Aspect | BSS (2018) | BB (2025) |
|--------|-----------|-----------|
| Coefficient ring | Gorenstein $\mathbb{Z}_p$-order $\mathcal{R}$ | Local complete Gorenstein ring |
| Selmer groups | Classical Selmer modules (Pontryagin duals) | **Nekovář–Selmer complexes** (determinants) |
| Local conditions | Relaxed (Bloch–Kato) | **Greenberg conditions** (more general) |
| Conclusion | Fitting ideals of Selmer modules | **Determinants of Selmer complexes** |
| $\mu = 0$ hypothesis | Often needed | **Removed entirely** |
| Trivial zeros mod $p$ | Problematic | **Systematically handled** |

**Key innovations of BB:**

1. **Selmer complexes replace Selmer groups.** Instead of bounding Fitting ideals of Selmer modules $H^1_{\mathcal{F}}(K, A)$, BB bound the **determinant** $\det_R R\Gamma_{\mathcal{F}}(K, A)$ of the full Selmer complex. This is strictly finer: the determinant contains information about all cohomology groups, not just $H^1$.

2. **Relative core vertices.** Where Mazur–Rubin require a "core vertex" (a prime where the Selmer group has a specific structural property), BB introduce **relative core vertices** — a weaker notion proven to exist via the Cebotarev density theorem and Artin–Verdier duality.

3. **Control of residual triviality.** BB handle the case where Kolyvagin systems become trivial upon reduction mod $p$ — forced by "trivial zeros mod $p$" in the Greenberg setting. This is done by keeping careful track of "error terms" in a delicate limit argument.

4. **General $\mathcal{R} \to R$ morphism.** The theory is relative to a morphism $\mathcal{R} \to R$ of local complete Gorenstein rings, making it applicable to deformation rings.

### 2.3 Implications for Rank 2

**Theorem (BB, Corollary 9.7).** Let $E/\mathbb{Q}$ be a rational elliptic curve, $K/\mathbb{Q}$ a finite abelian extension with $L(E/K, 1) \neq 0$, and $p > 3$ such that:
- $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ acts on $T_p(E)$ with image containing $\mathrm{SL}_2(\mathbb{Z}_p)$, and
- Either $E$ has potentially good reduction at $p$, or $K(\sqrt{-2(A/B)})$ contains no $p$-th root of unity.

Then the pair $(h^1(E/K)(1), \mathbb{Z}_p[\mathrm{Gal}(K/\mathbb{Q})])$ validates **one inclusion** in Kato's generalised Iwasawa main conjecture. If additionally $K/\mathbb{Q}$ is a $p$-extension and $E$ has good ordinary reduction at $p$, the conjecture is **fully valid**.

**Key point for rank 2:** This result:
- Avoids all hypotheses relating to trivial zeros modulo $p$ (no "non-anomalous" condition needed)
- Applies when $E$ has additive reduction at $p$
- The proof **uses higher-rank Stark systems** even though the conclusion is about rank-one Euler systems (Kato's zeta elements)

**For 389.a1 at $p = 5$:** The hypotheses require:
1. $\rho_{E,5}$ has image containing $\mathrm{SL}_2(\mathbb{Z}_5)$ — **known** (389.a1 has surjective mod-5 representation)
2. $E$ has potentially good reduction at $5$ — **true** (389.a1 has good reduction at 5, $a_5 = -3$)
3. $L(E/K, 1) \neq 0$ — this is the **analytic rank 0** condition for $E/K$, which fails for $K = \mathbb{Q}$ since $\mathrm{ord}_{s=1} L(E, s) = 2$

**Conclusion:** BB's theorem applies to 389.a1 over extension fields $K/\mathbb{Q}$ where $L(E/K, 1) \neq 0$, but **not** directly over $\mathbb{Q}$ (where the analytic rank is 2). For the rank-2 problem over $\mathbb{Q}$, one needs a different input.

---

## 3. The Abstract Control Machinery

### 3.1 How Burns' Machinery Controls Selmer Groups

The pipeline is:

```
Euler system c ∈ ES_r(T)
        │
        ▼ (higher Kolyvagin derivative D_r, canonical)
Kolyvagin system κ(c) ∈ KS_r(A)
        │
        ▼ (regulator map Reg_r, bijective)
Stark system ε(c) ∈ SS_r(A)
        │
        ▼ (Fitting ideal inclusion)
I_i(κ(c)) ⊆ Fitt_R^i(Sel(A))
```

**Input needed:**
1. A $p$-adic representation $T$ over a Gorenstein order $\mathcal{R}$
2. A Selmer structure $\mathcal{F}$ satisfying standard hypotheses
3. **Arithmetic classes:** An element $c \in \mathrm{ES}_r(T)$ — a compatible family of cohomology classes satisfying norm-compatibility relations at auxiliary primes

**Output:**
1. Lower bounds on Fitting ideals: $I_i(\kappa(c)) \subseteq \mathrm{Fitt}_R^i(\mathrm{Sel}(A))$
2. If $R$ is a principal ideal ring and the map is surjective: **equality** $\mathrm{Fitt}_R^i(\mathrm{Sel}(A)) = \langle I_i(\kappa(c)) \rangle$
3. Over $\mathcal{R}$ (inverse limit): analogous statements for Selmer modules of $T$ itself

### 3.2 What the Machinery Does NOT Do

- It does **not produce** Euler systems — it only consumes them
- It gives **upper bounds** on Selmer groups (via Fitting ideals), not lower bounds
- The reverse inclusion (lower bound) requires the Euler system to be "non-degenerate" — the Kolyvagin system $\kappa(c)$ must be a basis of the rank-one module $\mathrm{KS}_r(A)$
- For rank $r > 1$ applied to rank-$r$ Selmer groups, the output is about **Fitting ideals of exterior powers** of the Selmer group, not the Selmer group itself

### 3.3 BB's Refinement

BB's version replaces the Fitting ideal conclusion with:

$$\det_R R\Gamma_{\mathcal{F}}(K, A) \supseteq \text{(ideal determined by the Euler system)}$$

This is the **determinant of the Selmer complex**, which is strictly finer than the Fitting ideal of $H^1$ alone. In particular:
- It controls $H^0$ and $H^2$ as well as $H^1$
- It works for **Greenberg Selmer groups** (not just relaxed conditions)
- It removes the $\mu = 0$ hypothesis by working with complexes rather than modules

---

## 4. Applicability to 389.a1

### 4.1 Can Burns' Machinery Be Applied?

**Yes, in principle — but with critical gaps.**

For $E = 389.a1$ at $p = 5$:
- $T = T_5(E)$ is free of rank 2 over $\mathcal{R} = \mathbb{Z}_5$
- $\mathbb{Z}_5$ is a DVR, hence Gorenstein ✓
- The Selmer structure with Bloch–Kato local conditions satisfies standard hypotheses ✓
- The representation $\rho_{E,5}$ is surjective (image $\supseteq \mathrm{SL}_2(\mathbb{Z}_5)$) ✓

The machinery can be applied **once an Euler system is provided**.

### 4.2 What Arithmetic Classes Are Needed

For rank $r = 2$, the machinery needs $c \in \mathrm{ES}_2(T_5(E))$:

**Option A: A rank-2 Euler system.**
A compatible family $\{c_m^{(2)}\}$ of classes in $H^2(\mathbb{Q}(\mu_m), \wedge^2 T_5(E))$ satisfying norm compatibility. Since $\wedge^2 T_5(E) \cong \mathbb{Z}_5(-1)$ (Weil pairing), these live in $H^2(\mathbb{Q}(\mu_m), \mathbb{Z}_5(-1))$. **No such system is known to exist for any non-CM elliptic curve.**

**Option B: Reduce to rank 1 via rank-agnostic method.**
Apply BSS/BB's machinery with $r = 1$ to Kato's Euler system $z^{(5)} \in H^1_f(\mathbb{Q}, T_5(E) \hat\otimes \Lambda)$ of rank 1. This gives:
$$\mathrm{char}_\Lambda(\mathrm{Sel}_{5^\infty}(E/\mathbb{Q}_\infty)^\vee) \supseteq (\mathcal{L}_5^{\mathrm{Kato}})$$

This is **Kato's divisibility** — already known unconditionally (Kato 2004). The machinery does not improve on this without additional input.

**Option C: Kato's zeta element over an extension field $K$.**
Apply BB's theorem to $(E, K)$ where $K/\mathbb{Q}$ is abelian and $L(E/K, 1) \neq 0$. This proves one inclusion in Kato's IMC for $E/K$. But for $K = \mathbb{Q}$, the rank is 2 and $L(E, 1) = 0$.

### 4.3 What's Missing

1. **A rank-2 Euler system for $T_5(E)$.** No construction exists. The closest objects are Beilinson–Flach elements (for $\mathrm{Sym}^2$, not $\wedge^2$) and hypothetical Darmon cycles (with unverified norm compatibility).

2. **The reverse divisibility.** Kato gives $\mathrm{char} \supseteq (\mathcal{L}_5)$. The reverse $\mathrm{char} \subseteq (\mathcal{L}_5)$ requires either:
   - The full Iwasawa Main Conjecture (Skinner–Urban proves this under GRH for $p = 3$; for $p = 5$, only the divisibility is known)
   - A $p$-converse theorem (not available for non-CM curves at rank 2)

3. **A non-trivial class in $H^1_f(\mathbb{Q}, T_5(E))$.** For rank 2, Kato's class $z^{(5)}$ vanishes at the augmentation. The "second derivative" class $z^{(5)''}$ is the candidate, but its non-vanishing in the integral lattice is unproven.

---

## 5. Connection to Kim and Castella

### 5.1 Kim's Approach

**Kim (2020)** proved the plus/minus Main Conjecture for supersingular elliptic curves with $a_p = 0$. This is **not applicable** to 389.a1 at $p = 5$ ($a_5 = -3$, good ordinary).

The program's reference to "Kim: higher-rank Selmer structure via Kurihara numbers" likely refers to **Kurihara's** Fitting-ideal computations (Kurihara 2002, 2010), not to a specific theorem of Kim. Kurihara's work computes Fitting ideals of Selmer groups at Eisenstein primes and connects them to refined BSD — but this is a **computation method**, not a theorem that proves new results about specific curves.

**Verdict:** Kim/Kurihara methods are complementary to Burns' machinery (they compute what Burns' machinery bounds) but do not provide the missing input for 389.a1.

### 5.2 Castella's Approach

**Castella (2019, 2022, 2023)** constructs "generalized Kato classes" in two settings:

- **CM case (2204.09608):** For $E/\mathbb{Q}$ with CM by $K$, $p$ split in $K$, analytic rank 2: constructs a nonzero class $\kappa_{\mathrm{gen}} \in H^1_f(K, T_p(E) \otimes \mathcal{O}_\infty^{\mathrm{anti}})$ from the anticyclotomic restriction of Kato's class. The augmentation image is **nonzero** at the rank-2 point.

- **Non-CM case (2312.01481):** Uses Beilinson–Flach elements for $f \otimes f$, projects to $\mathrm{Sym}^2$, and extracts a class with controlled augmentation behavior. **The key non-vanishing statement for the augmentation order $< r$ is open for non-CM curves.**

**Verdict:** Castella's CM result is the closest existing construction to the missing arithmetic input for rank 2. For non-CM curves like 389.a1, the construction is partial — the geometric projection from $\mathrm{Sym}^2$ to $V_p(E)$ is not $G_\mathbb{Q}$-equivariant.

### 5.3 Comparison of Approaches

| Method | Input | Output | Applicable to 389.a1? |
|--------|-------|--------|----------------------|
| **Burns–Sakamoto–Sano** | Euler system of rank $r$ | Higher Fitting ideals of Selmer module | Yes, given the Euler system |
| **Bullach–Burns** | Euler system (relaxed conditions) | Determinant of Selmer complex | Yes, given the Euler system |
| **Kim/Kurihara** | Computation of Selmer group | Explicit Fitting ideal generators | Partially (computation method) |
| **Castella (CM)** | Anticyclotomic Kato class | Nonzero class at rank-2 point | No (389.a1 is non-CM) |
| **Castella (non-CM)** | Beilinson–Flach elements | Generalized Kato class (partial) | The construction exists; key non-vanishing is open |

### 5.4 Which Is Most Applicable to Rank 2?

**For the abstract framework:** Bullach–Burns is the strongest — it works with Greenberg conditions, removes $\mu = 0$, and gives determinant-level control. But it still needs an Euler system as input.

**For the arithmetic input:** Castella's non-CM construction is the most promising. The missing step is proving that the generalized Kato class for 389.a1 at $p = 5$ has augmentation order $< 2$ (i.e., it does not vanish modulo the augmentation ideal). This is a concrete, verifiable arithmetic statement.

**For 389.a1 specifically:** The most applicable existing result is the **one-inclusion theorem of BB** applied to $E/K$ for abelian $K/\mathbb{Q}$ where $L(E/K, 1) \neq 0$. This proves half of Kato's IMC for $E/K$ unconditionally (under the standard hypotheses on $\rho_{E,5}$). Combined with Castella's construction (if the non-vanishing is verified), this would give:

$$\mathrm{char}_\Lambda(\mathrm{Sel}_{5^\infty}(E/\mathbb{Q}_\infty)^\vee) = (\mathcal{L}_5^{\mathrm{Kato}})$$

which is the Iwasawa Main Conjecture for 389.a1 at $p = 5$ — the strongest possible conclusion from Euler system methods.

---

## Summary: Status for 389.a1

| Component | Status |
|-----------|--------|
| Abstract Euler system machinery (BSS/BB) | **Complete** — no gap in the theory |
| Kato's Euler system for 389.a1 at $p = 5$ | **Exists** — rank-1 zeta element $z^{(5)}$ |
| Kato's divisibility $\mathrm{char} \supseteq (\mathcal{L}_5)$ | **Proven** (Kato 2004) |
| Reverse divisibility $\mathrm{char} \subseteq (\mathcal{L}_5)$ | **Open** for $p = 5$ |
| Rank-2 Euler system | **Does not exist** (no construction) |
| Castella's generalized Kato class (non-CM) | **Partial** — construction exists, non-vanishing open |
| BB's one-inclusion over $K$ with $L(E/K,1) \neq 0$ | **Proven** (for appropriate $K$) |
| Full IMC for 389.a1 at $p = 5$ | **Open** |

**Bottom line:** The Burns machinery is ready. The bottleneck is the arithmetic input: either a rank-2 Euler system (does not exist) or a non-trivial arithmetic class at the rank-2 specialization point (Castella's construction, with open non-vanishing). For 389.a1, no existing theorem closes the gap between Kato's divisibility and the full Iwasawa Main Conjecture at $p = 5$.
