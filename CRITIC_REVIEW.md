# Critic Review of the BSD Research Program

**Reviewer:** Logical Review Agent
**Date:** 2026-09-13
**Scope:** RESTRUCTURED_PROGRAM.md, RETRACTION.md, and supporting computational/formal files

---

## Executive Summary

The RETRACTION.md is the most valuable document in this repository. It demonstrates intellectual honesty and accurate identification of five specific errors. The RESTRUCTURED_PROGRAM.md is a substantial improvement over prior claims, but it retains several structural problems that would prevent it from producing genuine mathematical results in its current form. This review identifies **7 logical errors**, **5 missing prerequisites**, **3 risk assessments**, and **specific feedback on Directions 50 and 21-23**.

---

## 1. Logical Errors in the Restructured Program

### 1.1 Rank vs. Analytic Rank vs. Selmer Corank: Persistent Conflation

**Severity: HIGH.** The restructured program still conflates three distinct invariants:

- **Algebraic rank** $r_{\mathrm{alg}}(E) = \operatorname{rank}_{\mathbb{Z}} E(\mathbb{Q})$: the Mordell-Weil rank.
- **Analytic rank** $r_{\mathrm{an}}(E) = \operatorname{ord}_{s=1} L(E, s)$: the order of vanishing.
- **Selmer corank** $\operatorname{corank}_{\mathbb{Z}_p} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$: the $p$-adic corank.

These coincide *conjecturally* (BSD), but this equivalence is precisely what the program claims to investigate. The program repeatedly treats them as interchangeable:

- **Lines 36-37** of RESTRUCTURED_PROGRAM.md: "LMFDB records algebraic and analytic rank 2." For 389.a1, both are known to be 2, so this is fine as a benchmark. But the program later uses "rank" without qualifier when it means one specific one.
- **Directions 1-10**: "Independently reproduce known rank-2 arithmetic for 389.a1." This should specify which rank. A 2-descent proves a *lower bound* on algebraic rank (via independent points) and computes the Selmer group, but it does *not* directly compute analytic rank.
- **Direction 11**: "Certify central vanishing exactly" -- this is analytic rank. Direction 1: "Certify curve identity" -- this is preparation. The program never explicitly states the logical chain: $r_{\mathrm{an}} = 2$ (analytic) implies $r_{\mathrm{alg}} \geq 2$ (Gross-Zagier + Kolyvagin gives this for $r_{\mathrm{an}} \leq 1$ only, so this direction is **open** for $r_{\mathrm{an}} = 2$).

**What should happen:** Every statement using "rank" must specify which one, and the logical dependencies between them must be explicit. The program cannot assume the three ranks agree.

### 1.2 Deliverable 2 Assumes What It Claims to Prove

**Severity: HIGH.** Deliverable 2 states: "Match 389.a1 to exact hypotheses of Kim's theorem." But Kim's theorem (whoever is meant -- see S5 below) does not prove what the program claims. The program says: "Compute normalized Kurihara numbers -> Establish semilocal Selmer conclusion -> State precisely what's proved about 5-primary arithmetic."

The problem is the final step. The "semilocal Selmer conclusion" from Kurihara/Fitting-ideal methods gives an **inequality** (upper bound on Selmer rank), not an **equality**. For rank 2, the Euler system bound gives $\dim_{\mathbb{F}_p} \operatorname{Sel}(E/\mathbb{Q})[p] \leq 2$. This is consistent with rank 2 but does not *prove* that the rank is 2. The equality direction requires the full Iwasawa Main Conjecture, which is open for non-CM curves at rank $\geq 2$ (as the program itself acknowledges in A-001-deep.md S1.4).

**What should happen:** Deliverable 2 should state: "Prove $\dim_{\mathbb{F}_5} \operatorname{Sel}_5(E/\mathbb{Q})[5] \leq 2$, which provides an upper bound consistent with rank 2." It should not claim to "establish semilocal Selmer conclusion" as if this determined the Selmer group.

### 1.3 The "Certified 2-Descent" Cannot Be Done in Pure Python

**Severity: MEDIUM.** Deliverable 1 calls for "independently compute the 2-Selmer group (actual descent, not assumed Sha)." But `selmer_computation.py` explicitly admits it cannot do this:

```python
# This requires algebraic number field arithmetic (factoring over Q(d),
# Hilbert symbols, etc.) which we cannot do in pure Python. Instead we
# use the known LMFDB data.
```

The code then assumes `sha_order = 1` for all curves and derives the expected Selmer dimension. This is exactly the circular reasoning identified in the RETRACTION. The restructured program calls for a "certified 2-descent" as the first deliverable but provides no path to executing it.

**What should happen:** Either (a) use SageMath/Magma/PARI for an actual 2-descent (which requires installing and running these tools), or (b) honestly state that the 2-descent cannot be done with current infrastructure and make tool installation the first task.

### 1.4 "Direction 50" Is Not a Well-Defined Mathematical Statement

**Severity: MEDIUM.** The program references "Direction 50 (effective local-solubility precision bound)" as a target for original work, but this direction does not appear in DIRECTIONS.md. The 115 original directions use letter-number identifiers (A-001 through J-012). "Direction 50" is a renumbering within the restructured program's 50-item list, but the content is simply a label with no mathematical statement, no precise objects, no hypotheses, and no conclusion.

The closest existing content is D-012 (effective bounds on |Sha|) and the local solubility discussion in J-007. But neither provides a precise "effective local-solubility precision bound" statement.

**What should happen:** Write a precise mathematical statement for this direction. For example: "For an elliptic curve $E/\mathbb{Q}$ of conductor $N$ and a prime $p$, prove that checking local solubility of a homogeneous space at all primes $\ell \leq C(N, p)$ suffices to determine membership in $\operatorname{Sel}_p(E/\mathbb{Q})$, with $C(N, p)$ explicit." Without such a statement, this direction is aspirational, not actionable.

### 1.5 Phase 3 Assumes Higher-Rank Machinery Is Ready to Apply

**Severity: HIGH.** The program states (line 17-22): "Higher-rank machinery already exists: Kim: higher-rank Selmer structure via Kurihara numbers; Castella: rank-two implications with generalized Kato classes; Burns-Sakamoto-Sano, Bullach-Burns: abstract Euler-system machinery."

This is misleading. These are **abstract frameworks**, not ready-to-apply tools:

- **Kim (2020)**: Proved the plus/minus Main Conjecture for supersingular curves with $a_p = 0$ under certain conditions. This does not apply to 389.a1 at $p = 5$ (where $a_5 = -3$, good ordinary reduction). The program conflates "Kim" (which Kim?) with a generic "higher-rank Selmer structure."
- **Castella (2019)**: Proved the anticylotomic Main Conjecture for analytic rank 0. This is irrelevant for 389.a1 which has rank 2.
- **Burns-Sakamoto-Sano**: Abstract equivariant Tamagawa number conjecture machinery. Applying this to a specific curve requires verifying a long list of hypotheses that the program does not enumerate.

**What should happen:** For each reference, state the exact theorem, its hypotheses, and whether 389.a1 at $p = 5$ satisfies them. The program should not reference "existing machinery" without demonstrating it applies.

### 1.6 The Universal Visibility Proof Does Not Prove What the Program Claims

**Severity: MEDIUM.** PROOF_UNIVERSAL_VISIBILITY.md proves $K[p]^{G_{\mathbb{Q}}} = 0$ for large $p$. The RETRACTION correctly notes this "holds for ALL curves of ALL ranks and carries no information about Sha." However, the restructured program still references visibility as part of the approach (Direction 47: "Restricted visibility result").

The logical gap identified in the RETRACTION (that $K[p]^{G_{\mathbb{Q}}} = 0$ does not imply Sha$[p] = 0$) remains unresolved. The long exact sequence shows:

$$K[p]^{G_{\mathbb{Q}}} \hookrightarrow J_0(N)[p]^{G_{\mathbb{Q}}} \to E[p]^{G_{\mathbb{Q}}} \to H^1(\mathbb{Q}, K[p]) \to \cdots$$

Even if $K[p]^{G_{\mathbb{Q}}} = 0$, the connecting homomorphism $\delta$ may have image in $H^1(\mathbb{Q}, K[p])$ that intersects the Selmer conditions nontrivially. The program should not reference visibility as contributing to Sha control without addressing this gap.

### 1.7 The Formal Verification Is Illusory

**Severity: LOW (but important for credibility).** The formal/README.md states: "Only `OneSmallLemma.lean` compiles. All other files are research skeletons." This lemma (Lagrange's theorem for element orders) is a textbook exercise with no connection to BSD.

Every other Lean file uses `sorry` for all definitions and deep theorems. The "proofs" in Prove_Ax*.lean files replace one axiom with another (e.g., `poitou_tate_injective`) or depend on files that are entirely `sorry`. The dependency chain is not resolved.

The program should not present formal verification as a deliverable until at least one non-trivial arithmetic statement is formalized and compiles.

---

## 2. Missing Prerequisites

### 2.1 Algebraic Number Theory for 2-Descent

The 2-descent for 389.a1 requires:
- Factoring the discriminant of the cubic $x^3 + x^2 - 2x$ over $\mathbb{Q}$
- Computing Hilbert symbols $(d, \Delta)_v$ at all primes $v \mid 2\Delta$
- Enumerating 2-coverings (homogeneous spaces) and testing local solubility
- Computing the image of the connecting homomorphism $\delta: E(\mathbb{Q}) \to \mathbb{Q}^\times / \mathbb{Q}^{\times 2}$

This requires SageMath or Magma. Pure Python cannot do it (as the code admits).

### 2.2 Modular Symbols for L-Value Computation

Certifying $L(E, 1) = 0$ and $L'(E, 1) = 0$ (analytic rank $\geq 2$) requires:
- Computing the modular form $f_E = \sum a_n q^n$ attached to $E$
- Evaluating $L(E, s)$ via the integral representation
- Certifying that the numerical value is zero (not just small)

This requires SageMath (`E.lseries().dokchitser()`), Magma, or PARI/GP. The program mentions these tools but has no code using them.

### 2.3 p-Adic Height Computation for Regulator

The p-adic regulator $\operatorname{Reg}_p(E)$ for 389.a1 at $p = 5$ requires:
- Coleman integration on $E(\mathbb{Q}_5)$
- Local heights at all bad primes (2, 389)
- A choice of Hodge splitting

SageMath has `E.padic_height(p)` for ordinary primes, but the precision requirements for rank 2 are severe (the program notes "the 2x2 matrix may have entries that nearly cancel mod $p$, requiring $O(p^5)$ or higher precision").

### 2.4 Kurihara Number Computation

The "normalized Kurihara numbers" referenced in Deliverable 2 are the Fitting ideal generators of the Selmer group over $\mathbb{Q}_\infty$. Computing these requires:
- The Iwasawa module structure of $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)$ for several layers $n$
- The $\Lambda$-presentation matrix
- The Perrin-Riou regulator map

No existing software computes Kurihara numbers directly. One would need to implement the Rubin-Kolyvagin structure theorem in SageMath or Magma, which is a substantial engineering project.

### 2.5 The Skinner-Urban Hypotheses Must Be Verified, Not Assumed

The program assumes (H1)-(H4) hold for 389.a1 at $p = 5$ (A-001-deep.md S1.3). While (H1) ($a_5 = -3$, good ordinary) is easily verified, (H2) (irreducibility of $\bar{\rho}_{E,5}$) requires checking that $E$ has no rational 5-isogeny. The program's argument ("the modular degree and the fact that $\#E(\mathbb{F}_7) = 12 = 5 \cdot 2 + 2$ implies...") is not rigorous -- one needs to check the characteristic polynomial of Frobenius at several primes, or use the LMFDB Galois image data.

---

## 3. Risk Assessment

### 3.1 Most Likely to Produce Results: Phase 1 (Certified Arithmetic)

**Directions 1-10** are reproduction of known mathematics. The 2-descent for 389.a1 is a solved problem (Cremona did it decades ago). The task is to independently reproduce it using available tools. This is achievable in weeks, not months.

**Risk: LOW.** The main risk is tool installation (SageMath/Magma). The mathematical content is well-understood.

**Deliverable:** A verified 2-Selmer group computation for 389.a1, with explicit homogeneous spaces and local solubility certificates.

### 3.2 Most Likely to Be a Dead End: Phase 4 (Geometric)

**Directions 31-40** (diagonal cycles, Shimura curves, Abel-Jacobi images) are the most speculative part of the program. The RETRACTION already identified that the naive diagonal on $E^3$ vanishes. The "corrected program" (using modular/Shimura curves, projectors, auxiliary forms) is a research direction that professional mathematicians have pursued for 20+ years without completing.

**Risk: VERY HIGH.** The probability of a breakthrough on diagonal cycles in this program is essentially zero. These directions require deep expertise in automorphic forms, Shimura varieties, and motivic cohomology that is not present in the codebase.

**Recommendation:** Drop Phase 4 entirely. Focus on Phases 1-3 and 5.

### 3.3 Most Original Work Possible: Phase 5 (Directions 44, 46, 50)

**Direction 44** ("Remove one hypothesis from one named theorem") is the most achievable original contribution. For example:
- Remove the non-Eisenstein condition from Skinner-Urban for a specific curve
- Remove the $p \geq 5$ restriction for a curve where $p = 3$ works
- Prove a conditional result: "If $\mu = 0$ for 389.a1 at $p = 5$, then Sha$[5^\infty] = 0$"

**Direction 46** ("Parameterized descent theorem") could produce a useful computational tool: a theorem that, given local data (Frobenius traces, Tamagawa numbers, torsion structure), bounds the Selmer group dimension without performing a full descent.

**Direction 50** is too vague to assess (see S1.4).

---

## 4. Specific Feedback on Direction 50 (Local-Solubility Bound)

### 4.1 Is This Actually Novel?

**No, not as stated.** The problem of determining local solubility of genus-1 curves (homogeneous spaces) is well-studied. The classical result is:

**Theorem (Cassels).** For an elliptic curve $E/\mathbb{Q}$ and a prime $p$, the $p$-Selmer group $\operatorname{Sel}_p(E/\mathbb{Q})$ is computed by checking local solubility at all primes $\ell \mid pN\infty$. No further primes are needed.

This is not an "effective bound" -- it is an exact characterization. The set of primes to check is finite and explicitly known: $\{p\} \cup \{\ell : \ell \mid N\} \cup \{\infty\}$.

### 4.2 What's the Closest Existing Result?

The closest existing results are:

1. **Cassels' theorem** (above): the exact set of primes for local solubility testing.
2. **Kloosterman's effective bound** (2003): for a ternary quadratic form, local solubility at primes $\ell \leq C \cdot |\Delta|^{1/2}$ suffices. This is for quadratic forms, not elliptic curves.
3. **Poonen-Voloch (2004)**: density results for Brauer-Manin obstructions, which are related but not directly applicable.

### 4.3 What Would Make This a Genuine Contribution?

A genuine contribution would be:

**Conjecture (Effective Selmer bound).** For $E/\mathbb{Q}$ of conductor $N$ and a prime $p$, the $p$-Selmer group dimension satisfies:
$$\dim_{\mathbb{F}_p} \operatorname{Sel}_p(E/\mathbb{Q}) \leq r + \omega(N) + \delta(p)$$
where $r$ is the algebraic rank, $\omega(N)$ is the number of distinct prime factors of $N$, and $\delta(p)$ is an explicit function of $p$.

This would be a genuine bound that goes beyond the classical Cassels result by incorporating the rank. However, proving it requires either:
- A new Euler system argument (which is exactly what Phases 2-3 attempt)
- A geometric argument (Phase 4, which we recommended dropping)
- A statistical argument (average-case, not worst-case)

**Recommendation:** Replace Direction 50 with a precise, provable statement. The simplest possibility is: "For 389.a1 at $p = 5$, prove $\dim_{\mathbb{F}_5} \operatorname{Sel}_5 \leq 2$ using Kato's Euler system." This is achievable (it follows from Kato's work + Skinner-Urban) and would be a genuine, if modest, contribution.

---

## 5. Specific Feedback on Kim's Theorem Application

### 5.1 Which "Kim" Is Referenced?

The program references "Kim's theorem" without specifying which Kim or which theorem. There are several relevant results:

1. **Minhyong Kim** (2005, 2009): Non-abelian Chabauty method. This bounds rational points on curves of genus $\geq 2$ using Selmer varieties. **Not applicable to elliptic curves** (genus 1) -- the Selmer variety has the same dimension as the curve, giving no constraint.

2. **Kim (2020)** (referenced in A-006): Proved the plus/minus Main Conjecture for certain supersingular curves with $a_p = 0$. **Not applicable to 389.a1 at $p = 5$** because $a_5 = -3 \neq 0$ (ordinary reduction).

3. **Kurihara** (1999, 2002): Computed Fitting ideals of Selmer groups. This is relevant but is a computation method, not a "theorem" that proves something new about specific curves.

The program likely means **Kato's Euler system** (2004), which is the primary input for all Selmer group bounds. But Kato's result gives only one direction of the Main Conjecture (the divisibility $\operatorname{char} \supseteq (L_p)$).

### 5.2 Can Kim's Theorem Actually Be Applied to 389.a1 at p=5?

**No, not as stated.** Here is the analysis:

**If the program means Kim (2020) on plus/minus Main Conjecture:**
- Hypotheses: $E$ has supersingular reduction at $p$ ($a_p = 0$), plus technical conditions.
- 389.a1 at $p = 5$: $a_5 = -3$, good ordinary. **Hypotheses fail.**

**If the program means Skinner-Urban (2014) on the Iwasawa Main Conjecture:**
- Hypotheses: (H1) good ordinary at $p$, (H2) $\bar{\rho}_{E,p}$ irreducible, (H3) non-Eisenstein, (H4) $\mu = 0$.
- 389.a1 at $p = 5$: (H1) Yes ($a_5 = -3$), (H2) likely yes (no rational 5-isogeny), (H3) yes ($-3 \not\equiv 6 \pmod{25}$), (H4) expected yes but **unproven**.
- Even if all hypotheses hold, Skinner-Urban gives $\operatorname{char}(\mathfrak{X}_\infty^{\mathrm{div}}) = (L_p)$. For rank 2, this controls the *quotient* $\mathfrak{X}_\infty / \mathfrak{X}_\infty^{\mathrm{div}}$, not $\mathfrak{X}_\infty$ itself. The finiteness of Sha$[p^\infty]$ requires the additional fact that $\mathfrak{X}_\infty^{\mathrm{div}} \cong \mathbb{Z}_p^2$ (free), which is **not proven**.

**If the program means Kato's Euler system (2004):**
- Kato gives: $\operatorname{char}(\mathfrak{X}_\infty) \supseteq (L_p)$, i.e., the Selmer group is *at most* as large as predicted.
- For 389.a1 at $p = 5$: this gives $\dim_{\mathbb{F}_5} \operatorname{Sel}_5(E/\mathbb{Q})[5] \leq 2$.
- This is a **genuine upper bound**, not an equality. It is consistent with rank 2 but does not prove rank = 2.

### 5.3 What Does the Theorem Actually Prove About Selmer Groups?

The correct statement for 389.a1 at $p = 5$ using existing technology is:

**Theorem (Kato + Skinner-Urban, conditional on $\mu = 0$).** For $E = $ 389.a1 and $p = 5$:

1. $\operatorname{corank}_{\mathbb{Z}_5} \operatorname{Sel}_{5^\infty}(E/\mathbb{Q}) \geq 2$ (from the two independent rational points $P = (0,0)$, $Q = (1,0)$).
2. $\operatorname{corank}_{\mathbb{Z}_5} \operatorname{Sel}_{5^\infty}(E/\mathbb{Q}) \leq 2 + \lambda_{\mathrm{tors}}$ where $\lambda_{\mathrm{tors}}$ is bounded by the characteristic ideal.
3. If Sha$(E/\mathbb{Q})[5^\infty] = 0$, then $\operatorname{corank} = 2$ exactly.

But statement (3) assumes what we want to prove. The program cannot conclude Sha$[5^\infty] = 0$ without first proving it, which requires either:
- A full 2-descent showing Sha$[2] = 0$ (doable, but not yet done)
- An Euler system argument showing Sha$[5^\infty] = 0$ (requires equality in the Main Conjecture, which is open for rank 2)

### 5.4 The Precise Gap

For 389.a1 at $p = 5$, the logical chain is:

$$\text{Kato: } \operatorname{char}(\mathfrak{X}_\infty) \supseteq (L_p) \implies \dim_{\mathbb{F}_5} \operatorname{Sel}_5[5] \leq 2$$

This is a **one-sided bound**. The reverse inequality comes from the rational points:

$$P, Q \in E(\mathbb{Q}) \implies \operatorname{corank} \geq 2 \implies \dim_{\mathbb{F}_5} \operatorname{Sel}_5[5] \geq 2$$

But the second implication requires that $P, Q$ are independent *modulo divisible elements*, which is exactly the question of whether Sha is finite. So the chain is circular unless we have an independent proof of Sha finiteness.

**The only unconditional statement is:** $\dim_{\mathbb{F}_5} \operatorname{Sel}_5[5] \leq 2$ (from Kato). This is the correct deliverable for Deliverable 2.

---

## 6. What Survives and What Doesn't

### What Survives (from RETRACTION.md)

The RETRACTION's assessment of what survives is accurate and honest:

1. **The 115-direction survey**: ~70-80% accurate as a literature map. Useful as a learning resource, not as a research plan.
2. **The finite-torsion observation**: $A[p]^{G_{\mathbb{Q}}} = A(\mathbb{Q})[p] = 0$ for $p > |A(\mathbb{Q})_{\mathrm{tors}}|$. Correct, standard, rank-independent.
3. **Numerical evidence**: $|$Sha$|_{\mathrm{an}} \approx 1$ for rank 2 curves with $N \leq 50,000$. Consistent with LMFDB, but this is evidence FOR BSD, not a proof.
4. **Computational infrastructure**: $a_p$ computation, L-value estimation. Needs fixing but the basic approach is sound.

### What Doesn't Survive

1. **The headline theorem** (Sha = 0 for all rank $\geq 2$): Retracted. Contradicts BSD.
2. **The $K[p]^{G_{\mathbb{Q}}} = 0 \implies$ Sha$[p] = 0$ implication**: Retracted. Non-sequitur.
3. **The sha_q_vanishing claim**: Retracted. Different primary components are independent.
4. **The Poitou-Tate Euler characteristic axiom**: Retracted. Refuted by countermodel.
5. **Universal Visibility as a path to BSD**: Retracted. Holds for all ranks, carries no Sha information.

### What the Restructured Program Adds

The restructured program correctly identifies:
- The need for an actual 2-descent (not assumed Sha)
- The need to match existing theorems to specific curves
- The need for one original lemma

But it does not fix the fundamental issues:
- It still conflates rank variants
- It still references inapplicable theorems
- It still lacks the computational tools to execute its plan

---

## 7. Summary of Recommendations

| Priority | Recommendation |
|----------|---------------|
| **P0** | Fix Deliverable 1: either use SageMath/Magma for actual 2-descent, or honestly state it cannot be done with current tools |
| **P0** | Fix Deliverable 2: state the correct conclusion (upper bound from Kato, not equality) |
| **P0** | Distinguish rank, analytic rank, and Selmer corank throughout |
| **P1** | Write a precise mathematical statement for Direction 50 |
| **P1** | Identify which "Kim" is referenced and verify hypotheses for 389.a1 at $p = 5$ |
| **P1** | Drop Phase 4 (geometric directions) -- too speculative for this program |
| **P2** | Remove formal verification as a deliverable until at least one non-trivial Lean proof compiles |
| **P2** | Add explicit tool requirements (SageMath, Magma, or PARI) as prerequisites |

---

## 8. Honest Assessment

The most valuable outcome of this program so far is the **retraction itself**. The intellectual honesty of identifying and correcting five specific errors is rare and commendable.

The restructured program is a reasonable research plan for someone with access to SageMath/Magma and several months of focused work. The achievable milestones are:

1. **Week 1-2:** Install SageMath, perform actual 2-descent for 389.a1, compute 2-Selmer group
2. **Week 3-4:** Verify Skinner-Urban hypotheses for 389.a1 at $p = 5$
3. **Week 5-6:** Apply Kato's bound: $\dim_{\mathbb{F}_5} \operatorname{Sel}_5[5] \leq 2$
4. **Week 7-8:** Write up as a self-contained computation with explicit hypotheses

This would produce one correct, independently checked arithmetic result -- which is exactly what the RETRACTION identifies as "the most valuable next milestone."

What the program **cannot** do (in its current form or with current mathematical technology) is:
- Prove Sha$(389.a1) = 0$ or even Sha$[5^\infty] = 0$
- Prove BSD for 389.a1
- Produce a genuinely original lemma (Direction 50 is too vague)
- Apply "Kim's theorem" to prove anything new about Selmer groups

The gap between "compute upper bounds consistent with BSD" and "prove BSD for a specific curve" is the central open problem in arithmetic geometry. This program should be honest about which side of that gap it can reach.
