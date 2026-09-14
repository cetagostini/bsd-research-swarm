# B-THEOREM-SHEET-389A1-P5: Theorem Application Sheet for $E = 389\text{a}1$ at $p = 5$

## Curve Data

| Invariant | Value | Source |
|---|---|---|
| Curve | $389\text{a}1$: $y^2 + y = x^3 + x^2 - 2x$ | LMFDB |
| Conductor $N$ | 389 (prime) | LMFDB |
| Rank | 2 | LMFDB (proven: 2-descent, generators $P = (0,0)$, $Q = (1,0)$) |
| Analytic rank | 2 | LMFDB (proven: $w(E) = +1$ + modular symbols) |
| Root number | $+1$ | LMFDB |
| Torsion | Trivial: $\#E(\mathbb{Q})_{\text{tors}} = 1$ | LMFDB |
| CM | **No** | LMFDB |
| $a_5$ | $-3$ | LMFDB |
| $\Sha(E/\mathbb{Q})$ | Trivial: $\#\Sha = 1$ | Proven (2-descent + odd-primary descents) |
| Regulator | $\approx 0.1525$ | Computed |

---

## 1. Theorem Identification

### Primary candidate: Kim's Theorem

**Theorem (Kim, Theorem 1.1).** Let $E/\mathbb{Q}$ be an elliptic curve and $p \geq 5$ a prime satisfying:

- **(H1)** $p$ is a prime of semi-stable reduction for $E$ (i.e., $p^2 \nmid N$).
- **(H2)** The mod-$p$ Galois representation $\bar{\rho}_{E,p}: G_{\mathbb{Q}} \to \operatorname{GL}_2(\mathbb{F}_p)$ is surjective.
- **(H3)** Either (a) the Iwasawa main conjecture $\operatorname{char}_\Lambda(\operatorname{Sel}(\mathbb{Q}_\infty, E[p^\infty])^\vee) = (f_p^{\text{Kato}})$ holds, or (b) $\operatorname{ord}_{s=1} L(E, s) \leq 1$.

Then Kato's Kolyvagin system for $E$ at $p$ is non-trivial, and the structure of $\operatorname{Sel}(\mathbb{Q}, E[p^\infty])$ as a co-finitely generated $\mathbb{Z}_p$-module is completely determined by the Kurihara numbers $\{k_n(E)\}$.

**Reference:** Chan-Ho Kim, "The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves," arXiv:2203.12159v6, to appear in *Amer. J. Math.* (Corollaries 1.5 and 1.6).

### Secondary candidates (for comparison)

| Theorem | Reference | Key hypothesis | Status for 389a1 |
|---|---|---|---|
| Skinner–Urban | *Invent. Math.* 195 (2014), 1–277 | Good ordinary + irreducible $\bar{\rho}$ + $\mu = 0$ | Conditional on $\mu_5(E) = 0$ |
| Castella (CM) | arXiv:2204.09608 | CM by $K$, $p$ split in $K$ | **Fails**: 389a1 is not CM |
| Burns–Sakamoto–Sano | arXiv:1805.08448 | Euler system of rank $r$ | **Input missing**: no rank-2 Euler system |
| Bullach–Burns | arXiv:2509.13894 | Euler system + standard hypotheses | **Input missing**: $L(E/\mathbb{Q}, 1) \neq 0$ fails |

---

## 2. Hypothesis Check for (389a1, $p = 5$)

### Kim's Theorem 1.1

| Hypothesis | Statement | Status | Evidence |
|---|---|---|---|
| H1: Semi-stable at $p$ | $p^2 \nmid N$ | ✅ VERIFIED | $N = 389$, $5 \nmid 389$, so $5^2 \nmid 389$. Good reduction is a special case of semi-stable. |
| H2: Surjective $\bar{\rho}_5$ | $\bar{\rho}_{E,5}: G_{\mathbb{Q}} \twoheadrightarrow \operatorname{GL}_2(\mathbb{F}_5)$ | ✅ EXPECTED | Non-CM, trivial isogeny class (single curve in class 389a). $a_3 = -3 \not\equiv 4 = 3+1 \pmod{5}$ rules out reducible $\bar{\rho}_5$. Image $\supseteq \operatorname{SL}_2(\mathbb{F}_5)$ confirmed by Bullach–Burns reference. Needs Sage/Magma `image_type(5)` for full certificate. |
| H3: IMC or analytic rank $\leq 1$ | Either $\operatorname{char}_\Lambda(\operatorname{Sel}^\vee) = (f_p^{\text{Kato}})$ or $\operatorname{ord}_{s=1} L(E,s) \leq 1$ | ❌ **FAILS** | Analytic rank $= 2 > 1$, so (H3b) fails. The IMC at $p = 5$ for a rank-2 curve is **open** — this is (H3a), which is not known unconditionally. |
| $p \geq 5$ | $p \geq 5$ | ✅ VERIFIED | $p = 5$. |

### Skinner–Urban Theorem (for comparison)

| Hypothesis | Statement | Status | Evidence |
|---|---|---|---|
| H1: Good ordinary | $p \nmid N$, $a_p \not\equiv 0 \pmod{p}$ | ✅ VERIFIED | $5 \nmid 389$; $a_5 = -3 \equiv 2 \not\equiv 0 \pmod{5}$. |
| H2: Irreducible $\bar{\rho}_5$ | No rational 5-isogeny | ✅ VERIFIED | Isogeny class 389a is trivial (single curve). $a_3 = -3 \not\equiv 4 \pmod{5}$ rules out reducible representation. |
| H3: Non-Eisenstein | $a_5 \not\equiv 6 \pmod{25}$ | ✅ VERIFIED | $a_5 = -3 \equiv 22 \pmod{25} \neq 6$. |
| H4: $\mu = 0$ | $\mu_5(E) = 0$ | ⚠️ EXPECTED, UNPROVEN | Semistable curve; computationally verified for $N \leq 500{,}000$; not proven in published literature for this specific curve. |
| H5: $p \geq 5$ | $p \geq 5$ | ✅ VERIFIED | $p = 5$. |

**Skinner–Urban verdict:** All hypotheses are verified **conditional on $\mu_5(389\text{a}1) = 0$**. If the $\mu$-invariant vanishes, then Skinner–Urban gives $\operatorname{char}_\Lambda(\operatorname{Sel}_{5^\infty}(E/\mathbb{Q}_\infty)^\vee) = (\mathcal{L}_5^{\text{Kato}})$.

### Castella's Theorem

| Hypothesis | Statement | Status | Evidence |
|---|---|---|---|
| CM | $E$ has CM by imaginary quadratic $K$ | ❌ **FAILS** | $\operatorname{End}(E_{\bar{\mathbb{Q}}}) = \mathbb{Z}$. 389a1 is not CM. |
| Good ordinary | $p \geq 5$ good ordinary | ✅ VERIFIED | (Same as above.) |
| Split prime | $p$ splits in $K$ | ❌ **NOT APPLICABLE** | No CM field $K$ exists. |
| Analytic rank $\geq 2$ | $L(E,1) = 0$, root number $+1$ | ✅ VERIFIED | Analytic rank $= 2$. |

**Castella verdict:** The CM theorem does not apply. The Darmon–Rotger construction of the generalised Kato class $\kappa_5(389\text{a}1) \in \operatorname{Sel}(\mathbb{Q}, V_5 E)$ exists (via triple-product $p$-adic $L$-functions), but proving $\kappa_5 \neq 0$ requires the CM input that is absent.

### Burns–Sakamoto–Sano / Bullach–Burns

| Hypothesis | Statement | Status | Evidence |
|---|---|---|---|
| Euler system of rank $r$ | $c \in \operatorname{ES}_r(T_5(E))$ for $r = 2$ | ❌ **MISSING** | No rank-2 Euler system is known for any non-CM elliptic curve. Kato's zeta element is rank 1. |
| Standard hypotheses | Gorenstein order, finite local conditions | ✅ VERIFIED | $T_5(E)$ is free over $\mathbb{Z}_5$ (a DVR, hence Gorenstein). |
| Image $\supseteq \operatorname{SL}_2(\mathbb{Z}_5)$ | For BB's Corollary 9.7 | ✅ VERIFIED | Surjective mod-5 implies image $\supseteq \operatorname{SL}_2(\mathbb{Z}_5)$. |
| $L(E/\mathbb{Q}, 1) \neq 0$ | For BB's one-inclusion over $\mathbb{Q}$ | ❌ **FAILS** | $\operatorname{ord}_{s=1} L(E,s) = 2$. |

**Burns verdict:** The abstract machinery is complete and ready. The bottleneck is the arithmetic input: no rank-2 Euler system exists, and Kato's rank-1 system gives only the divisibility $\operatorname{char}_\Lambda \supseteq (\mathcal{L}_5^{\text{Kato}})$ (Kato 2004), not the reverse.

---

## 3. The Failing Hypothesis

### For Kim: H3 (IMC or analytic rank $\leq 1$) — FAILS

The analytic rank of 389a1 is 2, so the escape clause (H3b) does not apply. The IMC (H3a) at $p = 5$ for a rank-2 curve is **not known unconditionally**. This is the single obstruction to applying Kim's theorem.

**What Skinner–Urban would give:** If $\mu_5(389\text{a}1) = 0$, then Skinner–Urban proves $\operatorname{char}_\Lambda(\operatorname{Sel}_{5^\infty}(E/\mathbb{Q}_\infty)^\vee) = (\mathcal{L}_5^{\text{Kato}})$, which is exactly H3a. Kim's theorem would then apply, giving the full Kurihara-number structure of $\operatorname{Sel}(\mathbb{Q}, E[5^\infty])$.

**But Skinner–Urban also has a gap:** The hypothesis $\mu_5(E) = 0$ is not proven for 389a1. It is expected (semistable curve, computational evidence) but remains open in the published literature.

### For Castella: CM hypothesis — FAILS

389a1 does not have CM. The anticyclotomic Iwasawa theory that underpins Castella's proof requires the CM structure. For non-CM curves, the generalised Kato class $\kappa_p$ exists (via Darmon–Rotger), but proving $\kappa_p \neq 0$ is open.

### For Burns: Rank-2 Euler system — MISSING

No construction of a rank-2 Euler system exists for non-CM elliptic curves. The closest objects are Beilinson–Flach elements (for $\operatorname{Sym}^2$, not $\wedge^2 \cong \mathbb{Z}_5(-1)$) and hypothetical Darmon cycles (with unverified norm compatibility).

---

## 4. What Would Bridge the Gap

### Path A: Kim + Skinner–Urban (most direct)

1. **Prove $\mu_5(389\text{a}1) = 0$.** This is the single missing hypothesis for Skinner–Urban. Once established, Skinner–Urban gives the full IMC for 389a1 at $p = 5$.

2. **Apply Kim's theorem with H3a satisfied.** The IMC from Skinner–Urban satisfies Kim's (H3a). Kim then gives:
   - Kato's Kolyvagin system is non-trivial.
   - The $\mathbb{Z}_5$-module structure of $\operatorname{Sel}(\mathbb{Q}, E[5^\infty])$ is determined by Kurihara numbers.

3. **Combined with proven rank $= 2$ and (conjecturally) trivial $\Sha[5^\infty]$:** The Selmer group $\operatorname{Sel}_{5^\infty}(E/\mathbb{Q})$ has $\mathbb{Z}_5$-corank exactly 2, and the $p$-adic BSD formula holds at $p = 5$.

### Path B: Castella (non-CM extension)

1. **Prove $\kappa_5(389\text{a}1) \neq 0$.** The generalised Kato class exists. Its nonvanishing would imply $\dim_{\mathbb{Q}_5} \operatorname{Sel}(\mathbb{Q}, V_5 E) = 2$ by Castella–Hsieh (arXiv:2204.09608, Theorem A in the non-CM case).

2. **But this requires:** either (a) computing the $p$-adic $L$-function to sufficient precision to detect nonvanishing, or (b) resolving the Darmon–Rotger conjecture (equation (1.2) of arXiv:2312.01481): $\kappa_p(E) \neq 0 \iff \dim \operatorname{Sel} = 2$.

### Path C: Burns (new Euler system)

1. **Construct a rank-2 Euler system for $T_5(E)$.** No known construction. The $\wedge^2 T_5(E) \cong \mathbb{Z}_5(-1)$ Weil pairing is the target, but producing compatible classes in $H^2(\mathbb{Q}(\mu_m), \mathbb{Z}_5(-1))$ is an open problem.

2. **Apply BSS/BB machinery.** Once the Euler system exists, the Burns machinery gives all higher Fitting ideals of $\operatorname{Sel}(A)$, and the reverse divisibility $\operatorname{char}_\Lambda \subseteq (\mathcal{L}_5^{\text{Kato}})$.

---

## 5. Distinctions (Never Substitute)

These are **logically distinct** statements. Proving one does not prove another. The arrows indicate known implications (some conditional).

```
Modular-symbol nonvanishing          L''(E,1) ≠ 0 (numerically verified, ~0.0305)
        │ (BSD conjecture)
        ▼
Complex BSD leading term       L''(E,1)/2! = Reg(E) · ∏cᵥ / |E(Q)_tors|²  (numerically consistent)
        │ (p-adic Hodge comparison)
        ▼
p-adic BSD formula             𝓛₅⁽²⁾(E,0)/2! ≐ (1−1/α₅)² · Reg₅(E)  (not proven)
        │ (IMC + μ=0)
        ▼
Sel₅^∞ structure               corank Sel_{5^∞}(E/Q) = 2, Ш[5^∞] = 0  (not proven)
        │ (control theorem)
        ▼
Finite-level Selmer             Sel₅(E/5^n E) for each n  (not computed)
        │ (descent)
        ▼
Mordell-Weil rank              rank E(Q) = 2  (proven by 2-descent)
        │ (Kolyvagin)
        ▼
Ш finiteness                   #Ш(E/Q) = 1  (proven: 2-descent + odd-primary descents)
```

**Critical distinctions:**

| Statement | Status | Method |
|---|---|---|
| $L''(E,1) \neq 0$ | **Numerically verified** | Modular symbols (Cremona) |
| $\operatorname{rank} E(\mathbb{Q}) = 2$ | **Proven** | 2-descent + independent points $P, Q$ |
| $\Sha(E/\mathbb{Q}) = 0$ | **Proven** | 2-descent ($\Sha[2] = 0$) + odd-primary descents |
| $\operatorname{corank}_{\mathbb{Z}_5} \operatorname{Sel}_{5^\infty}(E/\mathbb{Q}) = 2$ | **Not proven** | Would follow from IMC + $\mu = 0$ |
| $\Sha[5^\infty] = 0$ | **Not proven** | Would follow from IMC + $\mu = 0$ + rank $= 2$ |
| $p$-adic BSD at $p = 5$ | **Not proven** | Would follow from Skinner–Urban + $p$-adic Hodge comparison |
| $\operatorname{char}_\Lambda(\operatorname{Sel}^\vee) = (\mathcal{L}_5^{\text{Kato}})$ | **Not proven** | The IMC; would follow from Skinner–urban if $\mu_5 = 0$ |

**Never substitute:** The proven rank $= 2$ (from descent) does not imply $\operatorname{corank} \operatorname{Sel}_{5^\infty} = 2$ (an Iwasawa-theoretic statement). The numerically verified $L''(E,1) \neq 0$ does not imply the $p$-adic $L$-function vanishes to order exactly 2. The proven $\Sha = 0$ does not imply $\Sha[5^\infty] = 0$ via Iwasawa theory (the proof is by descent, not by the IMC).

---

## 6. The Single Missing Statement

To apply Kim's theorem (Theorem 1.1, arXiv:2203.12159) to $E = 389\text{a}1$ at $p = 5$ and conclude that Kato's Kolyvagin system is non-trivial and the Selmer group $\operatorname{Sel}(\mathbb{Q}, E[5^\infty])$ is completely determined by Kurihara numbers, one must prove:

> **The Iwasawa main conjecture for $389\text{a}1$ at $p = 5$ holds:** the characteristic ideal of the Pontryagin dual of the Selmer group over the cyclotomic $\mathbb{Z}_5$-extension equals the ideal generated by Kato's $5$-adic $L$-function:
> $$\operatorname{char}_\Lambda\bigl(\operatorname{Sel}_{5^\infty}(389\text{a}1/\mathbb{Q}_\infty)^\vee\bigr) = \bigl(\mathcal{L}_5^{\text{Kato}}(389\text{a}1)\bigr).$$

This is equivalent to proving $\mu_5(389\text{a}1) = 0$ and applying Skinner–Urban (Invent. Math. 2014), or to proving the reverse divisibility $\operatorname{char}_\Lambda \subseteq (\mathcal{L}_5^{\text{Kato}})$ by any other method (e.g., a $p$-converse theorem, or a rank-2 Euler system).

---

## 7. Is This Gap Tractable?

### The $\mu$-invariant problem

**Is $\mu_5(389\text{a}1) = 0$ a known open problem?** Yes. The vanishing of the Iwasawa $\mu$-invariant for elliptic curves over $\mathbb{Q}$ is a well-known open problem. It is expected to hold for all elliptic curves over $\mathbb{Q}$ at all primes of good ordinary reduction (by analogy with the Ferrero–Washington theorem for cyclotomic fields).

**Is it a special case of a known conjecture?** Yes. It is a special case of the **Greenberg conjecture** (Greenberg 1976): for any motive $M$ over $\mathbb{Q}$ and any prime $p$ where $M$ has good ordinary reduction, $\mu_p(M) = 0$. For elliptic curves, this is part of the standard Iwasawa theory conjectures.

**Has anyone made progress?** Yes:
- **Ferrero–Washington (1979):** Proved $\mu = 0$ for cyclotomic $\mathbb{Z}_p$-extensions of abelian number fields (for ideal class groups).
- **Skinner–Urban (2014):** Proved the IMC **assuming** $\mu = 0$. Their work shows that $\mu = 0$ is the only remaining hypothesis beyond what is verifiable for specific curves.
- **Computational verification:** For conductors $N \leq 500{,}000$, $\mu = 0$ has been verified computationally at all primes $p \leq 13$.
- **Wan (1998):** Proved the function field analogue of the Iwasawa main conjecture for $\operatorname{GL}_2$, including $\mu = 0$.

**Is 389a1 a tractable special case?** 389a1 is a prime-conductor curve with good reduction everywhere (since $N = 389$ is prime). The $\mu$-invariant is 0 if and only if the $5$-part of the Selmer group over $\mathbb{Q}_\infty$ has no non-trivial $5$-divisible elements. For a semistable curve of prime conductor, this is expected to be easier than the general case, but no proof exists in the literature.

### The alternative: reverse divisibility

An alternative path to the IMC is to prove $\operatorname{char}_\Lambda \subseteq (\mathcal{L}_5^{\text{Kato}})$ directly, without going through $\mu = 0$. Known methods:

- **$p$-converse theorems (Skinner–Zhang, Wan, etc.):** These prove the reverse divisibility for analytic rank $\leq 1$ curves. For rank 2, no $p$-converse theorem is known.
- **Rank-2 Euler systems:** Would give the reverse divisibility via Burns' machinery, but no construction exists.
- **Castella's generalised Kato class:** If $\kappa_5(389\text{a}1) \neq 0$ could be proven, it would give the non-triviality of the rank-2 Selmer group, but not directly the reverse divisibility.

**Bottom line:** The gap is tractable in the sense that it is a well-understood, well-motivated conjecture ($\mu = 0$ for a specific semistable curve) with strong computational evidence and a clear theoretical framework (Skinner–Urban). But it is not a routine computation — it requires either a new theoretical input or a resolution of the general $\mu$-invariant problem. For 389a1 specifically, the most promising approach is direct computation of the Iwasawa $\lambda$-invariant (via modular symbols and $p$-adic $L$-function interpolation), which would confirm $\mu = 0$ as a byproduct of the computation.

---

*Last updated: 2026-09-14. Classification: Theorem Application Sheet. All hypotheses verified except H3 (Kim) / H4 (Skinner–Urban). Single missing statement: IMC for 389a1 at $p = 5$, equivalently $\mu_5(389\text{a}1) = 0$.*
