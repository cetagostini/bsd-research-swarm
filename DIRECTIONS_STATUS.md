# DIRECTIONS_STATUS.md — Honest Status Map

**Date:** 2026-09-13
**Curve:** 389.a1 (y² + y = x³ + x² − 2x, Δ = 389, rank 2)

---

## Legend

| Symbol | Meaning |
|--------|---------|
| **[K]** | Known toolkit — standard algorithms, literature results |
| **[R]** | Restricted research — active area, partial results exist |
| **[F]** | Major frontier — open problem, no complete path |
| ✅ | Complete (with caveats noted) |
| 🔄 | In progress |
| ⏸️ | Blocked (by tool gap or logical obstruction) |
| ❌ | Not started |
| 🔴 | Retracted (previously claimed complete, now withdrawn) |

---

## Phase 1: Certified Arithmetic [Directions 1–10]

**Goal:** Independently reproduce known rank-2 arithmetic for 389.a1.
**Reality:** Partially attempted. No SageMath/Magma available; pure Python cannot do actual descent.

| Dir | Status | Classification | Agent | Output File | Key Finding | Blocking Issue |
|-----|--------|---------------|-------|-------------|-------------|----------------|
| 1 | ✅ | [K] | Dir1-CertifyCurve | computation/lmfdb_verify.py | 389.a1 confirmed: Δ=389, a₅=−3, #E(F₅)=9, torsion trivial | None (LMFDB lookup) |
| 2 | ⏸️ | [K] | Dir2-FullDescent | computation/selmer_computation.py | **Circular**: assumes \|Ш\|=1, derives Sel₂ dim. Not a real descent. | No SageMath/Magma for Hilbert symbols, homogeneous spaces |
| 3 | 🔄 | [K] | — | — | Local completeness requires explicit Hilbert symbols at 2, 389, ∞ | Depends on Direction 2 |
| 4 | ✅ | [K] | Dir4-5-RankAndSha | computation/heights_389a1.py | P=(0,0), Q=(1,0) with ĥ-matrix positive definite → independent | None (canonical height is computable in pure Python) |
| 5 | 🔴 | [K] | Dir4-5-RankAndSha | — | **RETRACTED**: claimed Ш=0 for rank≥2. Contradicts BSD (194040.cu1 has \|Ш\|=4) | Circular reasoning identified in RETRACTION.md |
| 6 | 🔴 | [K] | CasselsTate-Compute | computation/selmer_results.json | **RETRACTED**: "Nontrivial Ш control" assumed Sha_order=1 | Same circularity as Dir 2 |
| 7 | ❌ | [K] | — | — | Cassels–Tate pairing requires actual Selmer group computation | Blocked by Dir 2 |
| 8 | ❌ | [K] | — | — | 4-descent requires SageMath/Magma | Blocked by tool gap |
| 9 | ❌ | [K] | — | — | Odd-primary (3-descent, 5-descent) requires algebraic number theory | Blocked by tool gap |
| 10 | 🔄 | [K] | Dir10-LatticeIndex | computation/heights_389a1.py | Height matrix computed; lattice index det ≈ 0.0038. Requires Ω for Reg. | Needs certified Ω integration |

**Phase 1 Summary:** 2 of 10 complete (but only identity check and independence). The central deliverable (certified 2-descent) is blocked by lack of computer algebra system. The Ш=0 claim was retracted.

---

## Phase 2: Analytic/Rigorous [Directions 11–20]

**Goal:** Certify L-function and regulator computations.
**Reality:** Partial computation attempted. L-values from LMFDB (not independently computed). No p-adic heights.

| Dir | Status | Classification | Agent | Output File | Key Finding | Blocking Issue |
|-----|--------|---------------|-------|-------------|-------------|----------------|
| 11 | 🔄 | [K] | ModularSymbols | computation/l_function_389a1.py | L(E,1)≈0 computed numerically; not certified to be exactly 0 | Needs SageMath Dokchitser for certified vanishing |
| 12 | ❌ | [K] | Dir11-12-LFunction | — | L″(E,1)/2! needed for BSD ratio; requires high-precision L-series | No independent L-function computation |
| 13 | 🔄 | [K] | Dir10-LatticeIndex | computation/heights_389a1.py | Reg ≈ 0.1947 from height matrix; not independently certified | Needs integration for Ω |
| 14 | ❌ | [K] | — | — | BSD normalization (Tamagawa, torsion, period) requires careful product | Ω computation not done |
| 15 | ❌ | [K] | — | — | p-adic height at p=5 requires Coleman integration | No p-adic computation infrastructure |
| 16 | ❌ | [K] | — | — | Cyclotomic p-adic L-function requires overconvergent modular symbols | Blocked by Dir 15 |
| 17 | ❌ | [K] | — | — | Exceptional zeros: 389.a1 has good reduction at 5, so no trivial zero | Not applicable to this curve at p=5 |
| 18 | ❌ | [R] | — | — | Derived heights: Nekovář-style secondary heights | No implementation exists |
| 19 | ❌ | [R] | — | — | Supersingular counterpart: a₅=−3, not supersingular at 5 | Not applicable to 389.a1 at p=5 |
| 20 | ❌ | [R] | — | — | Determinant-line formula: Perrin-Riou style | Research-level, no code |

**Phase 2 Summary:** 0 of 10 complete. The L-function file (31KB) computes a_p coefficients and estimates L-values numerically, but nothing is certified. The canonical height is computed but not cross-validated.

---

## Phase 3: Iwasawa/Euler Systems [Directions 21–30]

**Goal:** Apply existing higher-rank theorems to 389.a1 at p=5.
**Reality:** Extensive literature survey done. No theorem actually applied. The "Kim's theorem" reference is ambiguous (critic review §5.1).

| Dir | Status | Classification | Agent | Output File | Key Finding | Blocking Issue |
|-----|--------|---------------|-------|-------------|-------------|----------------|
| 21 | 🔄 | [K] | Dir21-23-KimTheorem | — | Hypothesis matrix: H1 (good ordinary, a₅=−3 ✓), H2 (irreducible ρ̄₅, likely), H3 (non-Eisenstein ✓), H4 (μ=0, unproven) | H2 and H4 not rigorously verified |
| 22 | ❌ | [K] | — | — | Kurihara numbers require Λ-module structure of Sel₅(E/Qₙ) | No software computes these |
| 23 | ❌ | [K] | — | — | Semilocal Selmer from Fitting ideals | Depends on Dir 22 |
| 24 | 🔄 | [K→R] | Burns-Euler | groups/b-euler-systems/results/B-BURNS-EULER.md | Kato's Euler system gives char(Sel*) ⊇ (L_p), i.e. dim Sel₅[5] ≤ 2 | One-sided bound only; reverse divisibility open for rank 2 |
| 25 | 🔄 | [K→R] | SkinnerUrban-Check | groups/b-euler-systems/results/B-FITTING-IDEALS.md | Higher Fitting ideals: framework exists (Bullach–Burns) | Not computable without Λ-presentations |
| 26 | ❌ | [R] | — | — | Specialization at augmentation zero: controlling Selmer from Iwasawa module | Requires Λ-module computation |
| 27 | ❌ | [R] | — | — | Integral primitivity: proving a class generates a direct summand | Research-level |
| 28 | ❌ | [F] | — | — | Rank-two determinant class: constructing explicit arithmetic class | Major open problem |
| 29 | ❌ | [R/F] | — | — | Norm relations for multi-system Euler system | Requires Dir 28 |
| 30 | ❌ | [F] | — | — | Selmer control from classes: full reverse divisibility | THE central gap (see SYNTHESIS_CYCLE3.md) |

**Phase 3 Summary:** 0 of 10 complete. The Kato upper bound (dim Sel₅ ≤ 2) is the one unconditional statement from the literature. The Skinner–Urban hypotheses are partially verified but not all proven for 389.a1. The critic review (§5.2) shows the "semilocal Selmer conclusion" is an inequality, not equality.

---

## Phase 4: Geometric [Directions 31–40]

**Goal:** Build correct geometric program (replacing naïve diagonal).
**Reality:** Naïve diagonal correctly identified as vanishing (Gross–Schoen). No correct alternative constructed.

| Dir | Status | Classification | Agent | Output File | Key Finding | Blocking Issue |
|-----|--------|---------------|-------|-------------|-------------|----------------|
| 31 | ✅ | [K] | Dir31-40-GeometricProgram | groups/j-unconventional/results/J-GEOMETRIC-PROGRAM.md | 6Δₑ = 0 in CH₀(E³) by Gross–Schoen Prop 4.5; naïve route closed | None (this is a negative result) |
| 32 | 🔄 | [K] | Dir33-40-GeometricProgram | computation/phase4_quick.json | Motive h¹(E) has correct Hodge type; vanishing order = rank (conjectural) | Standard conjecture, not proven |
| 33 | ❌ | [R] | — | — | Auxiliary modular/theta forms for Shimura curve approach | Requires Shimura curve expertise |
| 34 | ❌ | [K] | — | — | Local signs: root number computation | Not computed |
| 35 | ❌ | [K→R] | — | — | Projected cycle on Shimura variety | Requires Dir 33 |
| 36 | ❌ | [R] | — | — | Abel–Jacobi image conditions | Research-level |
| 37 | ❌ | [R/F] | — | — | Reciprocity formula for diagonal classes | Open problem |
| 38 | 🔄 | [K] | Dir34-38-RootNumbers | groups/j-unconventional/results/J-004-result.md | Quadratic base change: Waldspurger's formula relates L(Eᵈ,1) to period integrals | Computational, not novel |
| 39 | ❌ | [R] | — | — | Anticyclotomic derived object | Research-level |
| 40 | ❌ | [F] | — | — | Arithmetic nonvanishing beyond known cases | Major open problem |

**Phase 4 Summary:** 1 of 10 complete (Dir 31, a negative result). The critic review (§3.2) recommends dropping Phase 4 entirely as too speculative for this program. The geometric approach requires expertise in automorphic forms and Shimura varieties not present.

---

## Phase 5: Missing Implications [Directions 41–50]

**Goal:** Prove one new lemma or implication.
**Reality:** No original lemma produced. Direction 50 (the primary target) lacks a precise statement.

| Dir | Status | Classification | Agent | Output File | Key Finding | Blocking Issue |
|-----|--------|---------------|-------|-------------|-------------|----------------|
| 41 | ❌ | [F] | — | — | Higher-rank p-converse: if Selₚ corank = r, then ord_{s=1} L ≥ r | Open problem (Skinner, 2014 partial) |
| 42 | ❌ | [F] | — | — | Complex leading-term comparison: L^(r)/r! vs p-adic L^(r)/r! | Requires p-adic L-function |
| 43 | ❌ | [F] | — | — | Finite prime support for Ш: bounding primes where Ш has p-torsion | Open problem |
| 44 | ❌ | [R] | — | — | Remove one hypothesis from one named theorem (e.g. Skinner–Urban non-Eisenstein) | Most achievable original target; no work done |
| 45 | ❌ | [K→R] | — | — | Isogeny transfer: if BSD for E, then BSD for E′ (isogenous) | Requires base case |
| 46 | ❌ | [R] | — | — | Parameterized descent: bound Selmer from Frobenius traces alone | No statement written |
| 47 | 🔴 | [R] | Dir46-49-DescentVisibility | — | **RETRACTED**: Universal Visibility (K[p]^{G_Q}=0) carries no Ш info | K[p]^{G_Q}=0 holds for all ranks; non-sequitur to Ш[p]=0 |
| 48 | ❌ | [R] | — | — | Family-level Selmer distribution: average Selmer rank in twist families | Statistical, not individual |
| 49 | 🔄 | [K→R] | Lean-DescentCert | formal/OneSmallLemma.lean | Only file that compiles: Lagrange's theorem (unrelated to BSD) | All other Lean files use `sorry` throughout |
| 50 | ❌ | [R] | — | — | **No precise statement exists.** Critic review §4: Cassels' theorem already gives exact prime set. Not novel as stated. | Need to formulate a genuinely new bound |

**Phase 5 Summary:** 0 of 10 complete. The retractions eliminated Direction 47. Direction 50 lacks mathematical content. Direction 44 ("remove one hypothesis") is the most achievable target per the critic review but no work has begun. Direction 49 has one compiling Lean file (Lagrange's theorem) with no BSD connection.

---

## Overall Summary

### Quantitative

| Metric | Count |
|--------|-------|
| **Directions total** | 50 |
| **Complete** | 3 (Dirs 1, 4, 31) — all basic checks or negative results |
| **In progress** | 10 (Dirs 2, 10, 11, 13, 21, 24, 25, 32, 38, 49) |
| **Blocked** | 5 (Dirs 3, 7, 8, 9, 14) — by tool gap or Dir 2 dependency |
| **Not started** | 28 |
| **Retracted** | 4 (Dirs 5, 6, 47, and partial Dir 2) |
| **Total agents deployed** | ~60+ (visible from hub: 50+ running, ~103 parked) |
| **Total output files** | 543 files total: 163 .md, 308 .py, 26 formal .lean, 163 group .lean, 19 .json, etc. |
| **Group result files** | 138 (across 10 groups A–J) |
| **Compiling Lean files** | 1 (OneSmallLemma.lean — Lagrange's theorem, no BSD content) |

### What's Actually Been Done

1. **Curve identity certified** (Dir 1): 389.a1 confirmed via LMFDB
2. **Point independence partially shown** (Dir 4): Canonical height matrix computed, positive definite
3. **Naïve diagonal closed** (Dir 31): 6Δₑ = 0 correctly identified via Gross–Schoen
4. **Extensive literature survey**: 138 result files across 10 groups surveying ~115 research directions
5. **BSD ratio computed** for 3 rank-2 curves (433.a1, 681.a1, 194040.cu1) — numerical consistency, not proof
6. **5 rank-3 curves discovered** computationally (88024.a1, 75692.a1, 43976.a1, 66848.a1, 191300.b1)
7. **10,196 curves' a_p coefficients computed** (conductor range, |a|,|b| ≤ 50)
8. **Retraction published**: 5 specific errors identified and honestly documented

### What Has NOT Been Done

1. **No actual 2-descent** — selmer_computation.py assumes Ш=1 (circular)
2. **No certified L-function computation** — L-values from LMFDB, not independently computed
3. **No p-adic height computation** — no Coleman integration
4. **No Kurihara numbers** — requires Λ-module computation
5. **No original lemma proven** — Direction 50 has no statement
6. **No theorem applied to 389.a1** — Skinner–Urban, Kato, etc. cited but not instantiated
7. **No Lean formalization compiles** — except OneSmallLemma.lean (unrelated to BSD)

### Key Findings (Honest)

1. **Ш-finiteness is the single hardest gap.** Everything else (rank equality, leading coefficient, p-adic BSD) follows from IMC + Ш finite. (SYNTHESIS_CYCLE3.md)
2. **Kato gives one-sided bound:** dim Sel₅[5] ≤ 2 for 389.a1. Reverse inequality is open for rank ≥ 2.
3. **The retracted claims were wrong:** Universal Visibility, sha_q_vanishing, Poitou-Tate axiom all failed.
4. **The 115-direction survey is ~70–80% accurate** as a literature map (per RETRACTION.md).
5. **Pure Python cannot do 2-descent.** SageMath/Magma is a hard prerequisite.
6. **The critic review identifies 7 logical errors** in the restructured program (rank conflation, tool gaps, inapplicable theorems).

### Blocking Issues (Priority Order)

1. **No SageMath/Magma/PARI** — Blocks Directions 2, 3, 7, 8, 9, 11, 12, 13, 14, 15, 16, 22, 23. Without a computer algebra system, no certified arithmetic computation is possible.
2. **No precise statement for Direction 50** — The primary original-work target has no mathematical content. The critic review shows Cassels' theorem already gives the exact prime set for local solubility.
3. **Rank conflation** — The program uses "rank" without specifying algebraic, analytic, or Selmer corank. These are conjecturally equal but that equivalence IS BSD.
4. **Inapplicable theorem references** — "Kim's theorem" is ambiguous. Castella (2019) applies to analytic rank 0, not rank 2. Skinner–Urban (2014) gives equality under unproven μ=0 hypothesis.
5. **Lean formalization is scaffold only** — 26 files, all but one entirely `sorry`. No path from current state to compiling proofs.

### Honest Assessment

This project has produced:
- A **comprehensive literature survey** (valuable as a learning resource)
- A **correct retraction** of false claims (demonstrates intellectual honesty)
- **Computational infrastructure** for a_p and L-value estimation (sound but needs CAS)
- **No mathematical theorems, no proofs, no original contributions**

The distance to a genuine result is:
- **One certified 2-descent** (requires SageMath; ~1 week of work once available)
- **One precise original lemma statement** (Direction 44 is most achievable; ~1 month of focused work)
- **Full BSD for 389.a1** (requires solving a Millennium Prize problem; not achievable by this program)

The program's value is in mapping the landscape and identifying the gap between what computation can do (reproduce known results, verify numerical consistency) and what proof requires (new mathematics for Ш-finiteness at rank ≥ 2).
