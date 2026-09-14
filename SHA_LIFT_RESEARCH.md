# Sha-Lifting Research: Iteration 1

**Date:** 2026-09-14
**Author:** Mr. Implementation
**Reviewed by:** Dr. Science (SHA_LIFT_REVIEW.md)
**Status:** Iteration 1 complete — claim survives as classical theory; proof corrected per review; unconditional computation added

---

## 1. Precise Claim

**Claim (Lifting Dichotomy).** For an elliptic curve $E/\mathbb{Q}$ of rank 2 and a prime $p$ with $|\text{Ш}(E/\mathbb{Q})[p^\infty]| = p^2$, the Cassels–Tate pairing forces $\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2$ (not $\mathbb{Z}/p^2$). Consequently, the CT radical $D_1 = p\text{Ш}[p^2] \cap \text{Ш}[p] = 0$, and **no nontrivial class in $\text{Ш}[p]$ lifts to $\text{Ш}[p^2]$**.

**What is new:** This is not a new theorem — it follows from the Cassels–Tate pairing structure (Cassels/Wall). What IS new is:
1. Framing it as a **lifting obstruction** via the CT radical $D_n$
2. Deriving the **family-level criterion**: for $|\text{Ш}[p^\infty]| = p^2$, the lifting behavior is completely determined by the $p$-primary decomposition type
3. Identifying the **sharp dichotomy**: either ALL classes lift (when $\text{Ш}[p^\infty] \cong \mathbb{Z}/p^2$) or NONE do (when $\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2$), with no intermediate case possible for $|Ш|=p^2$

---

## 2. Mathematical Framework

### 2.1 The Lifting Map

For $E/\mathbb{Q}$ and prime $p$, the Kummer sequence gives:
$$0 \to E(\mathbb{Q})/pE(\mathbb{Q}) \xrightarrow{\delta} H^1(\mathbb{Q}, E[p]) \to H^1(\mathbb{Q}, E)[p] \to 0$$

The $p$-Selmer group $\text{Sel}_p(E/\mathbb{Q})$ consists of classes in $H^1(\mathbb{Q}, E[p])$ that are locally in the image of $\delta$ at all places $v$.

**Definition.** The multiplication map $p: \text{Ш}[p^2] \to \text{Ш}[p]$ sends $\eta \mapsto p\eta$. Its kernel is $\text{Ш}[p]$; its image is $p\text{Ш} \cap \text{Ш}[p] = p\text{Ш}[p^2]$.

**Proposition 1.** For $\xi \in \text{Ш}[p]$:
$$\xi \text{ lifts to } \text{Ш}[p^2] \iff \xi \in p\text{Ш}[p^2]$$

*Proof.* $\xi$ lifts to $\text{Ш}[p^2]$ iff there exists $\eta \in \text{Ш}[p^2]$ with $p\eta = \xi$. This is exactly the statement $\xi \in \text{im}(p: \text{Ш}[p^2] \to \text{Ш}[p]) = p\text{Ш}[p^2]$. $\square$

**Note (per review).** The Kummer exact sequence gives $0 \to E(\mathbb{Q})/pE(\mathbb{Q}) \to \text{Sel}_p(E/\mathbb{Q}) \to \text{Ш}[p] \to 0$. The map $\text{Ш}[p] \to \text{Sel}_p$ is **not** well-defined (Ш[p] is a quotient of Sel_p, not a subgroup); the injection $\text{Ш}[p] \hookrightarrow H^1(\mathbb{Q}, E[p])$ requires a splitting and is non-canonical. The proper lifting criterion uses the multiplication map $p$ and the Cassels–Tate radical, not a descent map.

### 2.2 Cassels–Tate Pairing Constraint (corrected per review)

The Cassels–Tate pairing $\text{CT}: \text{Ш} \times \text{Ш} \to \mathbb{Q}/\mathbb{Z}$ is:
- Bilinear
- Alternating: $\text{CT}(x, x) = 0$ for all $x$
- Non-degenerate on $\text{Ш}[n]/(\text{Ш}[n] \cap n\text{Ш})$ for each $n$

**Important correction:** CT non-degeneracy does NOT apply directly to $\text{Ш}[p]$; it applies to the quotient $\text{Ш}[p]/(\text{Ш}[p] \cap p\text{Ш})$. For $\text{Ш} \cong \mathbb{Z}/p^2$, we have $\text{Ш}[p] = \mathbb{Z}/p$ but $\text{Ш}[p]/p\text{Ш}[p] = 0$, so non-degeneracy at level $p$ is vacuous. The real obstruction is at level $p^2$.

**Proposition 2.** For $|\text{Ш}[p^\infty]| = p^2$, the CT pairing forces $\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2$, NOT $\mathbb{Z}/p^2$.

*Proof (corrected).* A finite abelian group admits a nondegenerate alternating bilinear form if and only if it is *balanced*: isomorphic to $\prod (\mathbb{Z}/n_i)^2$ over equal pairs (Cassels; Wall's classification).

- If $\text{Ш}[p^\infty] \cong \mathbb{Z}/p^2$: this is *unbalanced* (single cyclic factor), so no nondegenerate alternating form exists. ✗

- If $\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2$: this is *balanced* ($(\mathbb{Z}/p)^2$). The standard alternating form $\text{CT}(e_1, e_2) = 1/p$, $\text{CT}(e_1, e_1) = \text{CT}(e_2, e_2) = 0$ is non-degenerate. ✓

Therefore $\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2$ is the only CT-compatible structure. This is classical (Cassels/Wall). $\square$

### 2.3 The Lifting Dichotomy

**Corollary (Lifting Dichotomy).** For $|\text{Ш}[p^\infty]| = p^2$ on a rank-2 curve:
- $\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2$ (forced by CT)
- $p\text{Ш}[p^\infty] = 0$ (since every element has order $p$)
- The multiplication map $p: \text{Ш}[p^2] \to \text{Ш}[p]$ has image $p\text{Ш}[p^2] = 0$
- The Cassels–Tate radical $D_1 = p\text{Ш}[p^2] \cap \text{Ш}[p] = 0$
- **No nontrivial class in $\text{Ш}[p]$ lifts to $\text{Ш}[p^2]$**

---

## 3. Test Cases

### 3.1 Curve 194040.cu1

- **Conductor:** 194040
- **Rank:** 2
- **$|\text{Ш}|$:** 4 = $2^2$
- **Torsion:** $\mathbb{Z}/2\mathbb{Z}$

**Analysis:**
- $|\text{Ш}[2^\infty]| = 4 = 2^2$
- CT forces $\text{Ш}[2^\infty] \cong (\mathbb{Z}/2)^2$ (NOT $\mathbb{Z}/4$)
- $\text{Ш}[2] \cong (\mathbb{Z}/2)^2$: 4 elements, 3 nontrivial
- **Prediction:** None of the 3 nontrivial elements lift to $\text{Ш}[4]$
- The multiplication map $p: \text{Ш}[4] \to \text{Ш}[2]$ has trivial image (since $\text{Ш}[2^\infty] \cong (\mathbb{Z}/2)^2$), contributing 2 independent classes to $\text{Sel}_2$

**Consistency check (corrected per review):** $|\text{Sel}_2| = 2^{r + T + S} = 2^{2+1+2} = 32$ where $T = \dim E(\mathbb{Q})[2] = 1$ (torsion $\mathbb{Z}/2\mathbb{Z}$) and $S = \dim \text{Ш}[2] = 2$. Previous value of 16 was incorrect. For the 58 torsion-free pool curves: $|\text{Sel}_2| = 2^{2+0+2} = 16$.

### 3.2 Curve 194766.bg1

- **Conductor:** 194766
- **Rank:** 2 (certified by PARI: [2,2,2])
- **$|\text{Ш}|$:** 4 = $2^2$

**Same analysis:** $\text{Ш}[2^\infty] \cong (\mathbb{Z}/2)^2$, no nontrivial lifting.

**Note:** Previous iteration incorrectly cited 246464.ba1, which does not exist (conductor 246464 has no rank-2 curves). Corrected per Dr. Science's review.

### 3.3 Control Cases

- **389.a1:** $|\text{Ш}| = 1$ (trivial Sha). No lifting question arises.
- **571.a1:** $|\text{Ш}| = 1$ (trivial Sha). No lifting question arises.
- **433.a1, 681.a1:** $|\text{Ш}| = 1$ (from rigorous_sha_results.json). No lifting question arises.

**Observation:** For conductor $\leq 10{,}000$, all 2388 rank-2 curves have $|\text{Ш}| = 1$ (from cycle3_sha_exhaust.json). Nontrivial Sha for rank-2 curves is rare in this range.

---

## 4. Family-Level Criteria

### 4.1 General Structure Theorem

**Theorem (CT-determined lifting).** For $E/\mathbb{Q}$ of rank 2 and prime $p$ with $|\text{Ш}[p^\infty]| = p^n$:

The $p$-primary decomposition $\text{Ш}[p^\infty] \cong \bigoplus_{i=1}^r \mathbb{Z}/p^{a_i}$ (with $a_1 \geq a_2 \geq \cdots \geq a_r \geq 1$, $\sum a_i = n$) must satisfy:
1. $r$ is even (CT non-degeneracy on $\text{Ш}[p]/p\text{Ш}[p] \cong (\mathbb{Z}/p)^r$)
2. The number of liftable classes in $\text{Ш}[p]$ is $p^k$ where $k = \#\{i : a_i \geq 2\}$
3. The number of non-liftable classes is $p^r - p^k$

### 4.2 Specific Cases (corrected per review)

| $|\text{Ш}[p^\infty]|$ | CT-compatible structures | Liftable classes | Non-liftable |
|---|---|---|---|
| $p^2$ | $(\mathbb{Z}/p)^2$ only | 1 (identity only) | $p^2 - 1$ (all nontrivial) |
| $p^4$ | $(\mathbb{Z}/p)^4$ or $(\mathbb{Z}/p^2)^2$ | $(\mathbb{Z}/p)^4$: 1; $(\mathbb{Z}/p^2)^2$: $p^2$ | $(\mathbb{Z}/p)^4$: $p^4 - 1$; $(\mathbb{Z}/p^2)^2$: 0 |
| $p^6$ | $(\mathbb{Z}/p)^6$, $(\mathbb{Z}/p)^2 \times (\mathbb{Z}/p^2)^2$, $(\mathbb{Z}/p^3)^2$ | Varies by structure | Varies |

**Note:** $\mathbb{Z}/p^3 \oplus \mathbb{Z}/p$ is NOT CT-compatible (unbalanced). Previous table row was incorrect. Verified by brute-force enumeration of all groups of order ≤ 64 (Dr. Science's review).

### 4.3 The Sharp Dichotomy for $|\text{Ш}| = p^2$ (a $p^2$ coincidence)

For rank-2 curves with $|\text{Ш}| = p^2$:

$$\boxed{\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2 \implies D_1 = 0 \implies \text{no lifting}}$$

This is the ONLY possibility. The alternative ($\text{Ш}[p^\infty] \cong \mathbb{Z}/p^2$) is forbidden by CT non-degeneracy (unbalanced).

**Important caveat:** This "all-or-nothing" dichotomy is specific to $|Ш| = p^2$. At $|Ш| = p^4$, both branches exist: $(\mathbb{Z}/p)^4$ (none lift) and $(\mathbb{Z}/p^2)^2$ (all lift). At $|Ш| = p^6$, mixed cases occur. The statement "no intermediate case possible" in the original version was false as a general claim.

---

## 5. Obstruction Analysis

### 5.1 What the Obstruction Looks Like

For $\xi \in \text{Ш}[p]$, the obstruction to lifting is whether $\xi \in p\text{Ш}[p^2]$. When $\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2$, we have $p\text{Ш}[p^\infty] = 0$, so every nontrivial $\xi \in \text{Ш}[p]$ has $\xi \notin p\text{Ш}[p^2]$. The obstruction is absolute.

When the obstruction is active, each nontrivial class in $\text{Ш}[p]$ represents a genuine arithmetic obstruction: a homogeneous space for $E$ that is locally soluble everywhere but has no global rational point.

### 5.2 Can We Compute the Obstruction Explicitly?

For the 2-descent on 194040.cu1:
- The curve has torsion $\mathbb{Z}/2\mathbb{Z}$, so $E[2] \cong \mathbb{Z}/2 \times \mathbb{Z}/2$
- The Selmer group $\text{Sel}_2$ classifies 2-coverings of $E$
- Each element of $\text{Ш}[2]$ corresponds to a 2-covering that is locally soluble everywhere but has no global point

**Computational challenge:** Computing the Cassels–Tate radical explicitly requires:
1. An explicit representation of Selmer group elements as homogeneous spaces
2. Computation of the CT pairing matrix on $\text{Ш}[2]$
3. Verification of local solubility at all primes

This requires SageMath/Magma for the actual Galois cohomology computation. PARI provides rank and $s$-value but not explicit pairing data.

---

## 6. What This Means for the BSD Program

### 6.1 The Good News

The Lifting Dichotomy gives a **concrete structural constraint** on Ш for rank-2 curves:
- For $|\text{Ш}| = p^2$: Ш is forced to be elementary abelian (exponent $p$)
- This means Ш has no "hidden" higher-order structure at this level
- The CT radical $D_1 = 0$, giving a clean characterization of liftable vs non-liftable classes

### 6.2 The Bad News

The triviality of $D_1$ means that Sha classes at level $p$ are "maximally obstructed":
- They cannot be "resolved" by going to level $p^2$
- Each nontrivial class in $\text{Ш}[p]$ contributes an independent element to $\text{Sel}_p$
- This makes $\text{Sel}_p$ larger, not smaller

### 6.3 Implication for Descent Strategy

For the BSD program's goal of proving $\text{Ш}[p^\infty] = 0$:
- The lifting approach cannot "kill" Sha — if $\text{Ш}[p] \neq 0$ and $\text{Ш}[p^\infty] \cong (\mathbb{Z}/p)^2$, there are no liftable classes
- Each nontrivial class in $\text{Ш}[p]$ contributes an independent element to $\text{Sel}_p$
- This makes $\text{Sel}_p$ larger, not smaller
- The only way to prove $\text{Ш}[p] = 0$ is to show $\text{Sel}_p$ has exactly the "expected" size (i.e., no Sha contribution)
- This requires an independent bound on $|\text{Sel}_p|$, which is what Kato's Euler system provides **when $L(E,1) \neq 0$** (rank 0)

---

## 7. Next Directions (Iteration 2, per Dr. Science's review)

**E1 (bounded, priority): Finish the sweep**
- Run `run_pool_descent.py` over *all* rank-2 |Ш|=4 curves in LMFDB (paginate past 100)
- Record counts and any deviation from s=2
- Falsifier: any curve with failed certification or s ≠ 2 → a p=2 BSD anomaly (genuine discovery, stop everything)
- Decision: once sweep complete with uniform s=2, treat "s=2 uniform" as empirical fact, move to E2

**E2 (bounded, discriminating): Hunt for higher Ш[2]**
- Search mid-conductor ranges for rank-2 curves with dim Ш[2] ≥ 3 (s=3/4) or failed certification at rank 2 (4-torsion signature)
- Outcome space:
  - (i) only s=2 ever appears → strong statistical statement, pivot to E3/E4
  - (ii) s=4 found → first concrete p⁴ "none-lift" instance
  - (iii) failed certification at rank 2 → first (ℤ/4)²-type candidate (the "all-lift" branch) — pivotal object, seek Magma 4-descent before deep investment

**E3 (family-level criterion): Quadratic twist stability**
- For 194040.cu1 with analytic |Ш|=4: compute dim Ш^{(d)}[2] for quadratic twists E^{(d)} of rank 2
- Test whether the 2-part structure is twist-stable (always (ℤ/2)² when BSD predicts |Ш|=4)
- A provable twist-stability lemma would be the first non-classical output

**E4 (reframed, per Phd. Math review): Odd-primary scope for 194040.cu1**
- For p ∈ {3, 5,7}: compute dim Sel_p by p-descent (`ellpadicbsd` for the conjectural value + independent p-Selmer bound where Kato applies)
- State honestly, per prime: *unconditionally finite / finite outside exceptional set / open*
- No "certificate" language. The deliverable is an honest map of which primes are reachable for a concrete rank-2 curve

**Decision rule:** Park after two unproductive rounds. Honest bottom line: at rank 2 with |Ш|=p², lifting is trivially settled by descent; the genuinely open problem is the odd part of Ш / finiteness at odd p, where Kato + small-prime descent is the right tool.

---

## 8. Unconditional Computation (Dr. Science's contribution)

**Method:** PARI `ellrank(E, effort)` via `cypari2` (pip-installable, no SageMath needed).

**Semantics:** output [r₁, r₂, s, pts] with r₁ ≤ rank ≤ r₂; r₁ = r₂ guarantees rank certification and is guaranteed to fail if Ш has 4-torsion. C := dim Sel₂ satisfies C = T + R + S where T = dim E(ℚ)[2], R = rank, S = dim Ш[2].

**Pool:** 100 smallest-conductor rank-2 curves with analytic |Ш|=4 (LMFDB `rank=2&sha=4`, sorted by conductor).

**Result:** **100/100 → [2, 2, 2], rank certified.** T = 1 (42 curves with rational 2-torsion) or T = 0 (58 torsion-free). Hence:
- S = dim Ш[2] = 2 always
- 2Ш[4] = 0 (no 4-torsion)
- Ш[2^∞] ≅ (ℤ/2)², |Ш[2^∞]| = 4, finite
- No class lifts to Ш[4]

**Controls validated:**
- 389.a1 (rank 2, |Ш|=1): [2,2,0] certified, Ш[2]=0 ✓
- 37.a1 (rank 1): [1,1,0] certified ✓
- 102.c1 (rank 0, |Ш|=4): [0,0,2] certified, Ш[2]≅(ℤ/2)² ✓
- 210.e1, 582.d1 (rank 0, |Ш|=16): [0,2,0] **not** certified — 4-torsion signature ✓

**Consequence:** for p=2 and each of these 100 rank-2 curves: **Ш[2^∞] is provably finite, |Ш[2^∞]| = 4**. For odd p, finiteness requires separate arguments (p-adic L-functions, Kato divisibility under applicable hypotheses — not unconditionally available at rank 2).

---

## 9. Files Produced

| File | Description |
|------|-------------|
| `computation/sha_lift_research.py` | Main computation script: Sha structure analysis, CT compatibility, lifting predictions |
| `computation/run_pool_descent.py` | PARI 2-descent pool runner (reusable for E1/E2) |
| `computation/sha_lift_pool_results.json` | 100-curve pool results + derived dims (C, T, S, |Sel₂|) |
| `computation/sha_lift_controls_results.json` | 5 control curves, both signatures |
| `SHA_LIFT_RESEARCH.md` | This document: full research findings |
| `SHA_LIFT_REVIEW.md` | Dr. Science's independent review |

---

## 9. Verification

- [x] Mathematical argument is correct (CT balanced structure → even rank, classical)
- [x] Test cases consistent (194040.cu1, 194766.bg1 both have $|\text{Ш}| = 4 = 2^2$)
- [x] Control cases verified (389.a1, 37.a1, 102.c1, 210.e1, 582.d1)
- [x] **Unconditional 2-descent over 100-curve pool** (Dr. Science's review): 100/100 → rank certified 2, Ш[2]≅(ℤ/2)², no class lifts to Ш[4]
- [x] PARI rank certification semantics validated against controls
- [ ] Odd-primary finiteness: requires p-adic L-function certificate under verified hypotheses (see Track B)
- [ ] Extension to |Ш| = p⁴: no **rank-2** curve with |Ш|≥9 has been found in LMFDB. However, the p⁴ all-lift branch IS exercised by controls 210.e1 and 582.d1 (rank 0, s=0, |Ш|_an=16, Ш[2^∞]≅(ℤ/4)²) and potentially by the d=2 twist of 194040.cu1 (|Ш|_an=64, uncertified, see N1).

---

## 10. Obstructions Found (updated per review)

1. **No rank-2 curve with |Ш| ≥ 9 has been found in LMFDB searches so far.** The "Direction B" (extension to |Ш| = p⁴) has no **rank-2** empirical testbed. However, the p⁴ all-lift branch IS exercised at rank 0 by controls 210.e1 and 582.d1 (s=0, |Ш|_an=16, Ш[2^∞]≅(ℤ/4)²). The d=2 twist of 194040.cu1 (|Ш|_an=64, uncertified, see N1) may exercise the mixed p⁶ branch. A database search finding no rank-2 example is not a nonexistence theorem.

2. **Gap between analytic and algebraic Sha:** For rank-2 curves, LMFDB reports analytic Sha (from BSD formula), not algebraic Sha (which is unproven). The Lifting Dichotomy applies to algebraic Sha; for analytic Sha, it's a prediction conditional on BSD.

3. **Previous blockers resolved:**
   - ~~No SageMath/Magma~~ → PARI via `cypari2` completes 2-descent in < 1s/curve
   - ~~Only 2 curves available~~ → LMFDB has 100+ rank-2 curves with analytic |Ш| = 4
   - ~~LMFDB rate limiting~~ → Pool script with pagination resolves this
