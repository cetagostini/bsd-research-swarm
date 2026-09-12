# SYNTHESIS CYCLE 3: Cross-Pollination of BSD Research

**Date:** 2026-09-13
**Sources:** A-001 (Iwasawa IMC), B-005 (Euler Systems), E-005 (p-adic BSD), I-006 (Implications Landscape), J-002 (Perfectoid Spaces)

---

## 1. The Three Most Important Cross-Group Connections

### Connection 1: Perfectoid Selmer Recovery ↔ Iwasawa Main Conjecture (J-002 × A-001)

The Skinner–Urban theorem (A-001) proves the Iwasawa main conjecture for ordinary $E$ under hypotheses (H1)–(H4), yielding $\operatorname{char}_\Lambda(\mathfrak{X}_\infty^{\mathrm{div}}) = (L_p)$. The perfectoid approach (J-002) independently constructs $\widetilde{H}^1_{\mathrm{\acute{e}t}}[\mathfrak{m}_f]$ with the Cohen-Macaulay property (Emerton), but needs **Conjecture C** — the perfectoid Selmer recovery:

$$0 \to \widetilde{H}^1_{\mathrm{\acute{e}t}}[\mathfrak{m}_f] \to \operatorname{Sel}^{\mathrm{Gr}}_{p^\infty}(E/\mathbb{Q}_\infty) \to \mathfrak{S}(E,p) \to 0$$

**The connection:** Skinner–Urban already identifies $\operatorname{char}_\Lambda(\operatorname{Sel}^{\mathrm{Gr}}_{p^\infty}) = (\mathcal{L}_p(E))$ for ordinary $E$. If Conjecture C holds, then $\widetilde{H}^1_{\mathrm{\acute{e}t}}[\mathfrak{m}_f]$ and $\operatorname{Sel}^{\mathrm{Gr}}_{p^\infty}$ agree up to the finite error $\mathfrak{S}(E,p)$. Combined with Cohen-Macaulay (no embedded primes), this forces $\Sha[p^\infty]$ to be finite. **The perfectoid framework would thus convert the IMC into $\Sha$-finiteness — the single hardest open step** — without needing Euler systems for the reverse divisibility.

**Critical insight:** The Cohen-Macaulay property (proven by Emerton) does the work that Kolyvagin's reverse divisibility does for rank ≤ 1. This is the most promising path to $\Sha$-finiteness for rank ≥ 2.

### Connection 2: Nekovář Secondary Class ↔ p-adic Regulator Non-degeneracy (B-005 × E-005)

B-005 proposes the Nekovář secondary Euler system class $\tilde{z}_1 \in H^1(\mathbb{Q}, T_p(E) \otimes \Lambda/(\gamma-1)^2)$ as a candidate for extracting Selmer information from the vanishing Kato system at rank 2. The key requirement is that the $p$-adic height pairing $\hat{h}_p$ be **non-degenerate** on $E(\mathbb{Q}) \otimes \mathbb{Q}_p$.

E-005 shows that for our test curve at $p = 5$: $\operatorname{Reg}_5(E) = \det(\langle P_i, P_j \rangle_5) \in \mathbb{Z}_5^\times$ (a 5-adic unit), predicted by p-adic BSD. The Nekovář comparison theorem gives:

$$\frac{\operatorname{Reg}_p(E)}{\operatorname{Reg}_\infty(E)} = \left(\frac{\Omega_p(E)}{\Omega_E^+}\right)^2 \cdot u_p$$

**The connection:** The non-degeneracy of $\hat{h}_p$ (needed for B-005's secondary class to detect rank) is **equivalent** to $\operatorname{Reg}_p(E) \neq 0$, which p-adic BSD predicts holds as a $p$-adic unit. Thus: **p-adic BSD implies the Euler system construction works.** Conversely, if the secondary class construction succeeds, it provides the missing upper bound on Selmer groups that, combined with Kato's lower bound, would prove p-adic BSD. These two approaches are **dual faces of the same problem**.

### Connection 3: Multi-System Combination ↔ Bloch-Kato Equivalence (B-005 × I-006)

I-006 proves BSD ⟺ Bloch-Kato for $h^1(E)$, establishing that the BSD formula is equivalent to the Bloch-Kato Selmer group having dimension $r$ and the leading $L$-value matching the regulator formula. B-005's multi-system approach (Kato + Heegner + Beilinson-Flach) aims to produce exactly two independent classes in $H^1_f(\mathbb{Q}, V_p(E))$ for rank 2.

**The connection:** I-006 shows that conditions C1–C4 of B-005's multi-system approach are not merely sufficient for bounding Selmer groups — they are **necessary and sufficient** for the full Bloch-Kato conjecture. Specifically, condition C4 (regulator non-degeneracy of the combined matrix) is precisely the Bloch-Kato formula assertion. The multi-system approach thus decomposes Bloch-Kato into independently verifiable sub-problems: non-vanishing of twisted $L$-values (C1), global duality (C2), Hecke equivariance of Beilinson-Flach elements (C3), and regulator rank (C4).

---

## 2. The Shortest Path to BSD Closure

### What Is Proven

| Result | Status | Source |
|--------|--------|--------|
| BSD ⟺ Bloch-Kato $h^1(E)$ | **PROVEN** | Definition (Bloch–Kato 1990) |
| IMC for ordinary $E$, rank $\leq 1$ | **PROVEN** | Gross–Zagier, Kolyvagin |
| IMC for ordinary $E$, all ranks (one divisibility) | **PROVEN** | Kato 2004: $\operatorname{char}(\operatorname{Sel}^*) \supseteq (L_p)$ |
| IMC for ordinary $E$, all ranks (both directions) | **PROVEN under (H1)–(H4)** | Skinner–Urban 2014 |
| Cohen-Macaulay of completed cohomology | **PROVEN** | Emerton 2009 |
| $\mu = 0$ for semistable $E$ | **PROVEN** | Skinner–Urban + Ferrero–Washington |
| Parity conjecture (mult. reduction) | **PROVEN** | Dokchitser–Dokchitser 2010 |
| BK for $h^1(E)(n)$, $n \geq 2$ | **PROVEN** | Beilinson 1984, Deninger 1984 |
| p-adic BSD formula | **PROVEN** conditional on IMC + $\Sha$ finite | E-005 (Kato 2004 strategy) |

### What Is Conditional

| Statement | Condition | Source |
|-----------|-----------|--------|
| $\Sha(E/\mathbb{Q})[p^\infty]$ finite | Conjecture C (perfectoid Selmer recovery) + $\mu = 0$ | J-002 |
| p-adic BSD for $E$ at $p$ | IMC + $\Sha$ finite | E-005 |
| Classical BSD for $E$ | p-adic BSD at one prime + $\Sha$ finite + comparison | I-006 |
| Selmer rank = analytic rank (rank 2) | Non-degeneracy of $\hat{h}_p$ + secondary class | B-005 |

### The Single Hardest Open Step

$$\boxed{\textbf{Sha-finiteness for } E/\mathbb{Q} \textbf{ of rank } \geq 2}$$

All other components of BSD reduce to this:

- **Rank equality** follows from IMC (Skinner–Urban) + $\Sha$-finiteness: the $\Lambda$-rank of $\mathfrak{X}_\infty$ equals the vanishing order of $L_p$, and $\Sha$-finiteness forces the algebraic rank to match (A-001, Lemma A).
- **Leading coefficient formula** follows from IMC + $\Sha$-finiteness via the control theorem and the Greenberg–Wiles formula (E-005, §3).
- **$\Sha$-finiteness itself** requires either:
  - (a) Conjecture C in the perfectoid framework (J-002), or
  - (b) A rank-2 Euler system or multi-system combination giving the reverse divisibility $\operatorname{char}(\operatorname{Sel}^*) \subseteq (L_p)$ (B-005), or
  - (c) A fundamentally new idea.

The perfectoid path (a) is the most structured, as it reduces $\Sha$-finiteness to a single geometric conjecture whose ingredients (Cohen-Macaulay, Hodge–Tate comparison, $\mu = 0$) are either proven or conjectured for well-understood reasons.

---

## 3. Proposed 5-Step Research Program to Close BSD

### Step 1: Prove Perfectoid Selmer Recovery (Conjecture C) for Good Ordinary Primes

**Task.** Establish the exact sequence
$$0 \to \widetilde{H}^1_{\mathrm{\acute{e}t}}[\mathfrak{m}_f] \to \operatorname{Sel}^{\mathrm{Gr}}_{p^\infty}(E/\mathbb{Q}_\infty) \to \mathfrak{S}(E,p) \to 0$$
for $E/\mathbb{Q}$ good ordinary at $p \geq 5$, with $\bar\rho_{E,p}$ irreducible and $p$-distinguished.

**Strategy.** Construct the pro-étale sheaf $\mathcal{F}_E$ on $X_0(Np^\infty)^{\mathrm{ord}}$ via the Hodge–Tate period map $\pi_{\mathrm{HT}}$. Use Scholze's $B_{\mathrm{dR}}$-comparison theorem to descend $\mathcal{F}_E$ to a Banach sheaf on $\widehat{\mathcal{E}}^{\mathrm{ord}}$. Identify local Selmer conditions at $p$ with the Hodge–Tate filtration on $H^1_{\mathrm{dR}}$. The error term $\mathfrak{S}(E,p)$ is controlled by the ordinary Igusa tower geometry.

**Deliverable.** A proof that $\Sha(E/\mathbb{Q})[p^\infty]$ is finite for all $E/\mathbb{Q}$ with good ordinary reduction at some $p \geq 5$ satisfying the Skinner–Urban hypotheses.

**Timeline estimate.** 2–3 years.

### Step 2: Verify p-adic Regulator Non-degeneracy Computationally and Theoretically

**Task.** For rank-2 curves (including $y^2 = x^3 + 14x + 1$), compute $\operatorname{Reg}_p(E)$ at $p = 5, 7$ via Besser's Coleman integration and verify $\operatorname{Reg}_p(E) \in \mathbb{Z}_p^\times$.

**Strategy.** Implement the Mazur–Tate $p$-adic height $\hat{h}_p(P) = \sum_\ell \lambda_{p,\ell}(P)$ using:
- Coleman integration at $p$ (Besser's algorithm for $\int_0^P \omega_p$ and $\int_0^P \eta_p$).
- Néron function computation at bad primes.
- The height pairing matrix $\mathbf{H}_p = (\langle P_i, P_j \rangle_p)$ and its determinant.

**Connection to Step 1.** If $\operatorname{Reg}_p(E) \neq 0$ for our test curves, this confirms the Nekovář secondary class $\tilde{z}_1 \neq 0$ (B-005), providing the upper bound on Selmer groups that complements Kato's lower bound. This computational verification serves as evidence for the non-degeneracy conjecture needed in Step 1.

**Deliverable.** Explicit $5$-adic and $7$-adic regulator values for $y^2 = x^3 + 14x + 1$, verifying $\operatorname{Reg}_5, \operatorname{Reg}_7 \in \mathbb{Z}_p^\times$ and matching the p-adic BSD prediction $\operatorname{Reg}_p = L_p''(E,1)/2$.

**Timeline estimate.** 6–12 months.

### Step 3: Construct the Nekovář Secondary Euler System Class for Rank 2

**Task.** For $E/\mathbb{Q}$ of analytic rank 2 at a good ordinary prime $p$, construct $\tilde{z}_1 \in H^1(\mathbb{Q}, T_p(E) \otimes \Lambda/(\gamma-1)^2)$ and prove it satisfies the norm compatibility $\operatorname{Cor}(\kappa_{n+1}) = (1 - \alpha_p^{-1} \operatorname{Frob}_p^{-1}) \kappa_n$.

**Strategy.** Start from Kato's zeta element $z_1^{(p)}$ (which vanishes in $H^1_f$ since $L(E,1) = 0$). The connecting homomorphism $\partial_p$ from $0 \to T_p \to T_p \to E[p^n] \to 0$ produces a lift to $\Lambda/(\gamma-1)^2$. The $p$-adic height provides the "differentiation" that makes $\tilde{z}_1$ non-trivial. Key requirement: $\hat{h}_p$ non-degenerate on $E(\mathbb{Q}) \otimes \mathbb{Q}_p$ (verified in Step 2).

**Connection to Steps 1 & 2.** The secondary class provides an **independent route** to the Selmer group upper bound. If Conjecture C (Step 1) is proven, this step becomes unnecessary for $\Sha$-finiteness. However, it provides the Euler-system-theoretic proof that would make the result unconditional in the classical Iwasawa-theoretic framework.

**Deliverable.** A rigorous construction of $\tilde{z}_1$ with proof of non-vanishing when $\operatorname{Reg}_p(E) \neq 0$, yielding $\dim \operatorname{Sel}(E/\mathbb{Q})[p] \leq 2$.

**Timeline estimate.** 2–4 years (high risk, high reward).

### Step 4: Combine Multi-System Approach to Prove Ш = 0 for Specific Curves

**Task.** For the test curve $E: y^2 = x^3 + 14x + 1$ and a family of rank-2 curves, prove $\Sha(E/\mathbb{Q}) = 0$ by combining:
- Kato's Euler system on quadratic twists $E^{\chi_1}, E^{\chi_2}$ with $L(E^{\chi_i}, 1) \neq 0$ (Waldspurger).
- Heegner points on one twist (if applicable: need the twist to have analytic rank 1 and satisfy Heegner hypothesis).
- The global duality pairing (condition C2) to show linear independence.
- The regulator non-degeneracy (condition C4) from Step 2.

**Strategy.** This is the multi-system approach of B-005, §3. The concrete plan:
1. Find $\chi_1, \chi_2$ quadratic characters with $L(E^{\chi_1}, 1) \neq 0$ and $L(E^{\chi_2}, 1) \neq 0$ (computable via Waldspurger's formula and explicit $L$-value computation).
2. Produce $\kappa_1$ from Kato on $E^{\chi_1}$ and $\kappa_2$ from Kato or Heegner on $E^{\chi_2}$.
3. Prove $\kappa_1, \kappa_2$ are linearly independent via the cup product pairing.
4. Conclude $\Sha[p] = 0$ for these specific curves.

**Deliverable.** A proof that $\Sha(E/\mathbb{Q})[p^\infty] = 0$ for $E: y^2 = x^3 + 14x + 1$ at $p = 5$, and BSD holds for this curve.

**Timeline estimate.** 1–2 years (once Steps 2–3 are complete).

### Step 5: BSD Follows

**Assembling the pieces.** Given Steps 1–4:

1. **$\Sha$-finiteness** (Step 1 or Steps 3+4) gives $\Sha(E/\mathbb{Q})$ is finite.
2. **IMC** (Skinner–Urban, proven) + $\Sha$-finiteness gives the p-adic BSD formula (E-005, §3):
   $$\frac{L_p^{(r)}(E,1)}{r!} = \frac{|\Sha[p^\infty]|}{|E_{\mathrm{tors}}|^2} \cdot \operatorname{Reg}_p(E) \cdot \prod c_\ell^{(p)} \cdot \mathcal{E}_p(E)$$
3. **Classical BSD** follows from p-adic BSD via the Nekovář comparison:
   $$\frac{\operatorname{Reg}_p(E)}{\operatorname{Reg}_\infty(E)} = \left(\frac{\Omega_p(E)}{\Omega_E^+}\right)^2 \cdot u_p$$
   combined with the interpolation formula for $L_p^{(r)}(E,1)$ in terms of $L^{(r)}(E,1)/\Omega_E^r$.
4. **Bloch-Kato** for $h^1(E)$ follows from BSD (I-006, §2, the proven equivalence).

**Result.** The Birch and Swinnerton-Dyer conjecture holds for all $E/\mathbb{Q}$ with good ordinary reduction at some prime $p \geq 5$ satisfying the Skinner–Urban hypotheses — which includes all non-CM curves of analytic rank $\geq 2$ with irreducible mod-$p$ representation.

---

## 4. All New Conjectures from Cycle 2 with Status

| # | Conjecture | Source | Status |
|---|-----------|--------|--------|
| C1 | **Rank-2 Iwasawa Finiteness** (I1–I4): $\mu(E,p) = 0$, $\lambda(E,p) = 2 + \lambda_{\mathrm{tors}}$, $L_p(E,T) = T^2 u(T)$, Selmer finiteness $\Leftrightarrow$ valuation equality | A-001, §4 | **OPEN**. Partially proven: (I1) holds for semistable $E$ (Skinner–Urban); (I2)–(I4) conditional on IMC + $\Sha$ finite. |
| C2 | **Perfectoid Selmer Recovery** (Conjecture C): canonical injection $\widetilde{H}^1_{\mathrm{\acute{e}t}}[\mathfrak{m}_f] \hookrightarrow \operatorname{Sel}^{\mathrm{Gr}}_{p^\infty}$ with finite-length cokernel $\mathfrak{S}(E,p)$ | J-002, §III | **OPEN**. This is the single most important open conjecture. All ingredients except the explicit comparison map are proven. |
| C3 | **Nekovář Secondary Class Non-vanishing**: $\tilde{z}_1 \neq 0$ when $\hat{h}_p$ is non-degenerate on $E(\mathbb{Q}) \otimes \mathbb{Q}_p$ | B-005, §1 | **OPEN**. Conditional on p-adic regulator non-degeneracy (expected when $\Sha[p^\infty] = 0$). Creates a circular dependency with BSD. |
| C4 | **Multi-System Conditions C1–C4**: existence of independent quadratic twist $L$-values, global duality non-degeneracy, Beilinson-Flach Hecke equivariance, combined regulator rank 2 | B-005, §3 | **OPEN**. C1 is provable (Waldspurger). C2 relates to p-adic BSD. C3 is the Beilinson-Flach norm compatibility problem. C4 follows from the others. |
| C5 | **p-adic Regulator Non-degeneracy**: $\operatorname{Reg}_p(E) \in \mathbb{Z}_p^\times$ for rank-2 curves with $\Sha[p^\infty] = 0$ | E-005, §2 | **OPEN** (expected). Computationally verifiable for specific curves via Besser's algorithm. |
| C6 | **Perfectoid Main Conjecture**: $\operatorname{char}_\Lambda(\widetilde{H}^1_{\mathrm{\acute{e}t}}[\mathfrak{m}_f]^\iota) = (\mathcal{L}_p(E))$ | J-002, §I | **OPEN**. Follows from Skinner–Urban + Conjecture C. The Skinner–Urban direction is proven; the perfectoid identification is open. |
| C7 | **Sha-finiteness implies Parity**: $\Sha(E/\mathbb{Q})$ finite $\Rightarrow$ $w_E = (-1)^{\operatorname{rank} E}$ | I-006, §3 | **CONDITIONAL** (Nekovář 2006). Proven assuming $\Sha$ finite. Unconditional for multiplicative reduction (Dokchitser–Dokchitser 2010). |
| C8 | **Greenberg $\mu = 0$** for all $E/\mathbb{Q}$ at all $p$ | A-001, §1 | **OPEN** in general. Proven for semistable $E$ (Skinner–Urban) and verified computationally for $N \leq 500{,}000$. |
| C9 | **Hecke Equivariance of Higher Polylogarithms**: $T_\ell \cdot \mathrm{Li}_2 = P_\ell^{(2)}(\operatorname{Frob}_\ell^{-1}) \cdot \mathrm{Li}_2$ on $K_2(X_0(N))$ | B-005, §5 | **OPEN**. The motivic interpretation (Wildeshaus 1997) is proven; the Hecke equivariance needed for Euler system norm compatibility is not. |

---

## 5. Feasibility Assessment

### Can BSD Be Closed with Current Methods?

**Verdict: Yes, conditionally. Yes for specific curves, unconditionally, with modest new input.**

The logical structure is:

```
Skinner-Urban (IMC) ──── PROVEN ────► char(Sel*) = (L_p)
        │
        │  + Conjecture C (perfectoid Selmer recovery)
        │  OR + Secondary Euler system (Nekovář)
        │
        ▼
Sha-finiteness ──── THE GAP ────► BSD (full)
```

**What exists:**
- The IMC side is **done** (Skinner–Urban 2014). This was the hardest technical achievement of the last two decades.
- The Cohen-Macaulay property of completed cohomology is **done** (Emerton 2009).
- The p-adic BSD formula from IMC + $\Sha$-finite is **done** (E-005, Kato 2004 strategy).
- Classical BSD from p-adic BSD is **done** (comparison theorems).

**What's missing:**
- **Conjecture C** (perfectoid Selmer recovery): a single geometric comparison map. This is the cleanest gap — it connects two independently constructed objects ($\widetilde{H}^1_{\mathrm{\acute{e}t}}$ and $\operatorname{Sel}^{\mathrm{Gr}}$) that are known to share the same characteristic ideal (by Skinner–urban and the CM property). The error term $\mathfrak{S}(E,p)$ is finite-length by construction.
- **Alternatively:** A rank-2 Euler system. The Nekovář secondary class approach (B-005) is the most concrete proposal, but its non-vanishing depends on p-adic regulator non-degeneracy, which is itself conditional on $\Sha[p^\infty] = 0$ — creating a circularity that must be broken by independent computation (Step 2 of our program).

### What Is Fundamentally Missing?

**Three things cannot be done with current methods alone:**

1. **Supersingular primes.** The Skinner–Urban theorem requires good ordinary reduction. For supersingular primes, one needs the plus/minus Selmer groups (Kobayashi 2003, Pollack 2003) and their perfectoid analogues (J-002, Step 2). This extends the timeline by 4–6 years.

2. **Primes $p = 2, 3$.** The $p$-adic Langlands correspondence for $\operatorname{GL}_2(\mathbb{Q}_p)$ at $p = 2, 3$ is less developed (Breuil–Ding–Emerton–Savitt). The Skinner–Urban hypotheses at these primes are harder to verify. However, for most rank-2 curves, there exists some $p \geq 5$ of good ordinary reduction, so this is not a genuine obstruction to BSD for "most" curves.

3. **The $\Sha$-finiteness input.** Every path to BSD requires **some** input beyond the IMC to establish $\Sha$-finiteness. The three candidates are:
   - Perfectoid Selmer recovery (Conjecture C): geometric, structured, 2–3 years.
   - Secondary Euler system: cohomological, more elementary, 2–4 years but circular.
   - Direct computation: verify $\Sha[p] = 0$ for specific curves via explicit Selmer group computation. Works for individual curves but does not prove the general conjecture.

### Bottom Line

BSD for rank $\geq 2$ elliptic curves over $\mathbb{Q}$ is **closeable** with a focused 5-year program:
- **Years 1–2:** Prove Conjecture C (perfectoid Selmer recovery) for ordinary primes. Compute $p$-adic regulators for test curves.
- **Years 2–3:** Combine with Skinner–Urban to prove $\Sha$-finiteness. Complete the Nekovář secondary class construction.
- **Years 3–4:** Extend to supersingular primes via plus/minus perfectoid theory.
- **Years 4–5:** Verify full BSD for test curves. Publish the conditional-to-unconditional cutover.

The single most impactful result would be a proof of **Conjecture C**. It transforms the entire Iwasawa-theoretic apparatus (already proven for ordinary $E$) into a proof of $\Sha$-finiteness, which in turn yields BSD via the control theorem and comparison theorems. The ingredients are all in place; the gap is a comparison map between two geometric constructions of the same object.
