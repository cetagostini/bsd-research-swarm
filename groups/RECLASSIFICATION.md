# Reclassification of All Result Files

**Date:** 2026-09-13
**Reason:** Previous claims of "Theorem" and "Lemma" are retracted per RETRACTION.md.
No result file qualifies as Theorem (requires Lean 4 verification or peer review) or Lemma
(requires proof within this research program). All files are honestly reclassified below.

## Classification Rules

| Label | Definition |
|-------|-----------|
| **Theorem** | Formal proof (Lean 4 verified or peer-reviewed). **Currently: NONE qualify.** |
| **Lemma** | Proven within this research program. **Currently: NONE qualify.** |
| **Conjecture** | Testable prediction, computationally verified for examples. |
| **Experiment** | Computational result with code and data. |
| **Speculation** | Theoretically motivated guess; no proof or testable prediction. |

---

## Full Reclassification Table

### Group A — Iwasawa Theory (`groups/a-iwasawa/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| A-SU-EXTEND.md | Theorem (conditional on CFKS) | **Speculation** | Surveys gaps in Skinner–Urban; no new proof; conditional restatement of others' work |
| A-MU-ZERO.md | OPEN / Proof attempt | **Speculation** | Self-described heuristic; explicitly "NOT A PROOF" |
| A-NONABELIAN-SHA.md | Theorem (conditional on CFKS MC) | **Conjecture** | Detailed conditional argument; Ш finite iff unproven CFKS MC holds |
| A-001-deep.md | Theorem + Lemma + Conjecture | **Conjecture** | Original conjectures (I1–I4) are conjectural; restated Skinner–Urban is citation |

### Group B — Euler Systems (`groups/b-euler-systems/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| B-MULTI-SHA.md | Conjecture (conditional C1–C4) | **Speculation** | Conditions C1–C4 are unproven; no unconditional result |
| B-005-deep.md | Theorem (conditional) | **Speculation** | All results conditional on unproven hypotheses |
| B-007-result.md | Theorem (Selmer bound, r ≤ 1) | **Conjecture** | r ≥ 2 contribution is conjectural; r ≤ 1 results are literature citations |
| B-008-result.md | Theorem (interpolation, divisibility) | **Conjecture** | Main conjecture equality conditional (Skinner-Urban at p=3 under GRH) |
| B-009-result.md | Theorem (Rubin bounding inequality) | **Conjecture** | Non-CM sharpness is partial; file's own contribution is conjectural |
| B-010-result.md | Theorem (several cases) + Conjecture | **Conjecture** | General case conditional on GRH; proven special cases are literature citations |
| B-011-result.md | Theorem (BF elements) + Conjecture | **Conjecture** | Parts (a)-(b) proven for BF elements; (c)-(d) open conjectures |
| B-012-result.md | Experiment | **Experiment** | Already correctly classified |

### Group C — Arithmetic Statistics (`groups/c-arithmetic-statistics/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| C-001-result.md | Theorem (avg rank ≤ 1/2) | **Conjecture** | Conditional on Bhargava-Shankar heuristics; no unconditional proof for all families |
| C-002-deep.md | Theorem (Goldfeld ⇒ finite avg |Ш|) | **Conjecture** | Conditional on unproven Goldfeld conjecture |
| C-003-result.md | Conjecture / Heuristic | **Conjecture** | Cohen-Lenstra heuristics for Ш; already correctly classified |
| C-004-result.md | Conjecture (moment asymptotics) | **Conjecture** | Already correctly classified |
| C-005-result.md | Partial results / Conjecture | **Conjecture** | Already correctly classified |
| C-006-result.md | Experiment / Partial results | **Experiment** | Already correctly classified |
| C-007-result.md | Conjecture (RMT distribution) | **Conjecture** | RMT predictions for analytic rank distribution; computationally supported |
| C-008-result.md | Theorem (for p=2, BKLRP 2023) | **Experiment** | File reports on BKLRP theorem (literature); own contribution is expository/computational |
| C-009-result.md | Partial results | **Experiment** | Computational analysis of Bhargava-Shankar bounds with LMFDB verification |
| C-010-result.md | Theorem (over function fields) | **Conjecture** | Transfer to number fields is open |
| C-011-result.md | Theorem (torsion distribution) | **Conjecture** | Torsion densities are literature theorems; torsion-Selmer interaction is conjectural |
| C-012-result.md | Partial results / Conjecture | **Conjecture** | Katz-Sarnak philosophy; full symmetry type determination is open |
| C-RMT-SHA.md | Theorem (average Ш finiteness) | **Conjecture** | Conditional on BSD for rank ≥ 2, Goldfeld, 1-level density σ > 1 |

### Group D — Tate–Shafarevich (`groups/d-tate-shafarevich/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| D-ODD-PRIME-VIS.md | Theorem (odd prime visibility) | **Conjecture** | Computational verification over 108 curves; no formal proof |
| D-VISIBILITY-VERIFY.md | Conjecture (Universal Visibility) | **Experiment** | Exhaustive computational verification (691 curves, N ≤ 5000) |
| D-VISIBILITY-PROOF.md | Theorem (K[2]^G_Q = 0 ⇒ Ш[2] = 0) | **Conjecture** | 340-line argument with gaps noted; not peer-reviewed or formalized |
| D-VISIBILITY-SHA.md | Conjecture + Theorem (conditional) | **Conjecture** | Conditional on Universal Visibility + Iwasawa hypotheses |
| D-001-cycle3.md | Theorem (Ш finiteness for 571a1) | **Conjecture** | Conditional on Iwasawa hypotheses (μ=0, ρ̄ surjective) |
| D-001-deep.md | Theorem + Proposed Theorem | **Speculation** | "Proposed Theorem" conditional on 4 unproven hypotheses |
| D-006-result.md | Experiment (Cassels-Tate pairing) | **Experiment** | Computational verification; structural framework is conditional |
| D-007-result.md | Conjecture (Ш finiteness) | **Conjecture** | Already correctly classified |
| D-008-result.md | Theorem (Agashe-Stein) + Lemma | **Experiment** | Structural visibility framework; proven results are literature citations |
| D-009-result.md | Theorem (Artin-Tate/Geisser) | **Experiment** | Surveys known theorems for function fields; Geisser conjecture (p=char) is open |
| D-010-result.md | Theorem (Greenberg/Kato/SU) | **Conjecture** | Iwasawa framework assembly; theorems are citations; μ=0 is open |
| D-011-result.md | Conjecture (Delaunay) | **Conjecture** | Already correctly classified |
| D-012-result.md | Theorem (GZK, conditional) | **Conjecture** | Conditional on unproven hypotheses |

### Group E — p-adic Methods (`groups/e-padic-methods/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| E-001-result.md | Conjecture (Hida families) | **Conjecture** | Two-variable p-adic L-functions; framework is established, specific predictions conjectural |
| E-002-result.md | Theorem (p-adic Gross-Zagier) | **Conjecture** | Perrin-Riou/Nekovář results are literature; file's extensions are conjectural |
| E-003-result.md | Theorem (MTT L-invariant) | **Conjecture** | MTT is literature; file's generalizations are conjectural |
| E-004-result.md | Experiment (p-adic heights) | **Experiment** | Computational height algorithms; already correctly classified |
| E-005-result.md | Conjecture + Comparison Theorem | **Conjecture** | Comparison theorem is formal equivalence; p-adic BSD is conjectural |
| E-005-deep.md | Theorem + Lemma (conditional) | **Conjecture** | Conditional on Iwasawa MC and Ш finite (both unproven for rank ≥ 2) |
| E-006-result.md | Theorem (Pollack-Stevens) + Conjecture | **Experiment** | Pollack-Stevens is literature; own contribution is algorithmic |
| E-007-result.md | Conjecture + Lemma (precision) | **Experiment** | Computational algorithm development (Coleman integration) |
| E-008-result.md | Theorem (MTT 1986) + Conjecture | **Conjecture** | MTT is literature; Greenberg generalization is open |
| E-009-result.md | Conjecture (Kobayashi) + Theorem | **Conjecture** | Plus/minus Selmer main conjecture is unsolved |
| E-010-result.md | Theorem (Colmez 1990) + Conjecture | **Conjecture** | Colmez is literature; equality for good ordinary is open |
| E-011-result.md | Theorem (Dasgupta-Kakde) + Conjecture | **Conjecture** | Dasgupta-Kakde is literature; CM field connection to p-BSD is open |
| E-PADIC-HODGE-SHA.md | Proposition (Ш finiteness) | **Speculation** | Ш[p^∞] finite only under expected-corank hypothesis (unproven) |

### Group F — Motivic/Cohomological (`groups/f-motivic-cohomological/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| F-001-result.md | Theorem (Kato's zeta element) | **Conjecture** | Kato's Euler system is literature; BSD implications are conjectural |
| F-002-result.md | Conjecture (Beilinson for rank 1) | **Conjecture** | Already correctly classified |
| F-003-result.md | Theorem (Bloch-Kato special values) | **Conjecture** | Bloch-Kato is literature; specific predictions for Ш are conjectural |
| F-003-deep.md | Theorem (Bloch-Kato ⟺ BSD) | **Speculation** | Well-known folklore equivalence; no original proof or formalization |
| F-004-result.md | Experiment (syntomic cohomology) | **Experiment** | Besser algorithm implementation; already correctly classified |
| F-005-result.md | Conjecture (Griffiths groups) | **Speculation** | Higher Chow cycles on elliptic curves; no computational verification |
| F-006-result.md | Theorem (Beilinson regulator) | **Experiment** | Regulator computation from K₂(E) to ℝ; computational implementation |
| F-007-result.md | Conjecture (motivic L-functions) | **Conjecture** | Special values framework; already correctly classified |
| F-008-result.md | Conjecture + Lemma | **Speculation** | Purely conceptual Deligne-Beilinson framework |
| F-009-result.md | Conjecture + Lemma | **Speculation** | K-theoretic approach is speculative; Kolyvagin lemma is literature |
| F-010-result.md | Conjecture + Lemma | **Speculation** | Arakelov theory framework; application to BSD is explicitly conjectural |
| F-011-result.md | Conjecture (Deninger) | **Speculation** | Already correctly classified as speculative |
| F-012-result.md | (cites Merkurjev-Suslin) | **Experiment** | Computational survey of Soulé regulators |
| F-ARAKELov-SHA.md | Theorem (Arakelov BSD) | **Speculation** | Arithmetic Bézout theorem needed is explicitly a Conjecture |

### Group G — Deformation/Langlands (`groups/g-deformation-langlands/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| G-001-result.md | Theorem (Taylor-Wiles extensions) | **Speculation** | Higher-rank Selmer group extensions; no proven results for rank ≥ 2 |
| G-001-deep.md | (no explicit label) | **Speculation** | Pure technical exposition; no proven results or testable predictions |
| G-002-result.md | Theorem (Skinner-Wiles residually reducible) | **Conjecture** | Skinner-Wiles is literature; file's extensions are conjectural |
| G-003-result.md | Theorem (Fontaine-Laffaille) | **Conjecture** | Local deformation ring structure; computationally verified for specific cases |
| G-004-result.md | Theorem (modularity lifting) | **Conjecture** | Higher-dimensional modularity lifting; conditional on unproven hypotheses |
| G-005-result.md | Conjecture (Langlands-Weissman) | **Conjecture** | L-value approach; already correctly classified |
| G-006-result.md | Conjecture + Lemma | **Conjecture** | Symmetric power functoriality; Lemma restates part of conjecture |
| G-007-result.md | Conjecture + Lemma | **Conjecture** | Lemma (Eisenstein Ideal) largely known from Mazur |
| G-008-result.md | Conjecture + Lemma | **Conjecture** | Lemma (Euler Characteristic) is standard mathematics |
| G-009-result.md | Conjecture + Lemma | **Conjecture** | Lemma restates Breuil-Mézard conjecture |
| G-010-result.md | Conjecture + Lemma | **Conjecture** | Lemma (Rank Preservation) unproven within research program |
| G-011-result.md | Conjecture + Lemma | **Conjecture** | Lemma (Colmez Correspondence) is known theorem (Colmez 2010) |

### Group H — Computational (`groups/h-computational/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| H-001-result.md | Verification | **Experiment** | Certified numerical BSD verification for specific curves |
| H-002-result.md | Verification / Data Analysis | **Experiment** | Algebraic = analytic rank for ~3M LMFDB curves |
| H-003-result.md | Infrastructure | **Experiment** | SageMath+PARI L-function pipeline |
| H-004-result.md | Verification / Frontier | **Conjecture** | BSD verification for rank ≥ 25 curves; rank 29 infeasible |
| H-005-result.md | Verification / Bounds | **Conjecture** | Reviews descent records; conjectures on |Ш| growth bounds |
| H-006-result.md | Data Analysis / Conjecture | **Experiment** | Tamagawa number distribution statistics from LMFDB |
| H-007-result.md | Computation / Infrastructure | **Experiment** | Regulator computation methods for high-rank curves |
| H-008-result.md | Computation / Infrastructure | **Experiment** | AGM-based period computation |
| H-009-result.md | Verification | **Experiment** | Strong BSD verification for 10^9+ curves |
| H-009-deep.md | Verification + Discovery | **Experiment** | Discovers 5 rank-3 curves; verifies strong BSD |
| H-010-result.md | Data Science / Conjecture | **Conjecture** | ML pipeline proposal for BSD pattern discovery |
| H-011-result.md | Computation / Verification | **Experiment** | L-function zero computation; GRH and GUE verification |
| H-ML-SHA.md | Complete | **Experiment** | ML on 139 curves: 91.4% accuracy for |Ш| classification |
| H-MODULAR-KERNEL.md | (computational data) | **Experiment** | Modular kernel K[2] computation for 108 rank-2 curves |

### Group I — Connections (`groups/i-connections/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| I-001-result.md | Conjecture (Colmez → BSD for CM) | **Conjecture** | Averaged Colmez proven (Yuan-Zhang); individual case open |
| I-002-result.md | Conjecture (Vojta + BSD → effective Mordell) | **Conjecture** | Both Vojta and BSD are open |
| I-003-result.md | Conjecture (Grothendieck period → L-values) | **Conjecture** | Necessary condition for BSD; open |
| I-004-result.md | Conjecture (Sato-Tate → rank density) | **Conjecture** | Statistical bridge via Katz-Sarnak; not individual-case |
| I-005-result.md | Conjecture (Birch-Swinnerton-Dyer heuristics) | **Conjecture** | Historical BSD heuristic data analysis |
| I-006-result.md | Theorem (BSD ⟺ Bloch-Kato) | **Speculation** | Standard equivalence survey; no new results |
| I-006-deep.md | Theorem (multiple — mostly literature) | **Speculation** | Surveys known equivalences; "Ш finite ⇒ BSD" is conditional |
| I-007-result.md | Conjecture (Modularity → BSD) | **Conjecture** | Modularity theorem + BSD connection |
| I-008-result.md | Conjecture (Parity conjecture) | **Conjecture** | Root number = (-1)^rank; proven for many cases |
| I-009-result.md | Conjecture (Elliptic nets → Ш) | **Conjecture** | Stange's elliptic nets and Ш computation |
| I-010-result.md | Conjecture (Random matrix → L-values) | **Conjecture** | Keating-Snaith predictions for L-function moments |
| FUNCTION-FIELD-SHA.md | Theorem (Artin-Tate — literature) | **Speculation** | Surveys published results; proposes speculative Arithmetic Brauer Embedding |

### Group J — Unconventional (`groups/j-unconventional/results/`)

| File | Previous | Corrected | Notes |
|------|----------|-----------|-------|
| J-001-result.md | Conjecture (mirror symmetry → BSD) | **Speculation** | Fukaya category bridge; entirely conjectural motivic HMS |
| J-002-result.md | Conjecture (perfectoid BSD framework) | **Speculation** | Selmer recovery conjecture; no L-function construction exists |
| J-002-deep.md | Theorem (conditional on PMC) | **Speculation** | Conjecture C is "the single missing piece" |
| J-003-result.md | Conjecture (categorification of BSD) | **Speculation** | Stable ∞-category approach; no formulation exists in literature |
| J-004-result.md | Conjecture (Kudla program) | **Conjecture** | Gross-Zagier is special case; active community progress |
| J-005-result.md | Experiment (ML rank prediction) | **Experiment** | Computational/exploratory; no mathematical proof |
| J-006-result.md | Active Research / High-Risk | **Speculation** | Full conjecture "likely decades away"; 4 fundamental obstacles |
| J-007-result.md | Conjecture (anabelian → Selmer) | **Speculation** | No mechanism exists from fundamental groups to Selmer groups |
| J-008-result.md | Exploratory / Bridge | **Speculation** | Arithmetic Thurston norm not rigorously defined; feasibility 2/10 |
| J-009-result.md | Conjecture (derived Selmer groups) | **Speculation** | Foundational objects don't exist in literature |
| J-010-result.md | Conjecture (quantum invariants → L-values) | **Speculation** | Relies on arithmetic topology dictionary (heuristic) and Volume Conjecture (unproven) |
| J-011-result.md | Conjecture (motivic Adams SS) | **Speculation** | No precedent connecting motivic spectral sequences to rank bounds |
| J-012-result.md | Conjecture (tmf L-function) | **Speculation** | The L-function of tmf is not a defined mathematical object |
| J-DERIVED-SHA.md | Status: Derived approach | **Speculation** | All three hypotheses (H1–H3) conditional |
| J-KUDLA-SHA.md | Classification: Exploratory | **Speculation** | Critical "projection problem" open; feasibility 3/10 |

---

## Summary Statistics

| Classification | Count |
|---------------|-------|
| **Experiment** | 33 |
| **Conjecture** | 48 |
| **Speculation** | 32 |
| ~~Theorem~~ | **0** |
| ~~Lemma~~ | **0** |
| **Total files** | **113** |

### Files That Claimed Ш = 0 or Ш Finite (Now Retracted)

These files previously claimed to prove Ш = 0 or Ш finite. Such claims are **retracted** per
RETRACTION.md. The files retain their content but are reclassified as Conjecture or Speculation:

| File | Retracted Claim | New Status |
|------|----------------|------------|
| A-SU-EXTEND.md | Ш(E/Q)[p^∞] finite (conditional on CFKS) | Speculation |
| A-NONABELIAN-SHA.md | Ш(E/Q)[p^∞] finite (conditional on CFKS MC) | Conjecture |
| A-001-deep.md | Ш(E/Q)[p^∞] finite (conditional on I1–I4) | Conjecture |
| A-MU-ZERO.md | μ = 0 (≡ Ш finiteness under IMC) | Speculation |
| B-MULTI-SHA.md | |Ш[p^∞]| = 1 (under C1–C4) | Speculation |
| B-005-deep.md | Ш(E/Q)[p^∞] = 0 (conditional) | Speculation |
| D-VISIBILITY-SHA.md | Ш finite for all rank ≥ 2 (conditional) | Conjecture |
| D-001-cycle3.md | Ш finite for 571a1; Ш = 1 | Conjecture |
| D-001-deep.md | Ш[p^∞] finite (conditional on 4 hypotheses) | Speculation |
| D-VISIBILITY-PROOF.md | Ш[2] = 0 (conditional on K[2]^G_Q = 0) | Conjecture |
| E-PADIC-HODGE-SHA.md | Ш[p^∞] finite (conditional); Ш = 0 (speculative) | Speculation |
| F-ARAKELov-SHA.md | Ш finite (via Arakelov — unproven Bézout) | Speculation |
| F-009-result.md | Ш finite (K-theoretic — speculative) | Speculation |
| J-DERIVED-SHA.md | Ш finite (conditional on H1–H3) | Speculation |
| J-KUDLA-SHA.md | Ш finite (via Kudla — open projection problem) | Speculation |
| J-002-deep.md | Ш(E/Q)[p^∞] finite (conditional on PMC) | Speculation |

---

## PROOFS.md Reclassification

The four main claims in `PROOFS.md` have been reclassified as follows:

| Original | Corrected | Reason |
|----------|-----------|--------|
| Theorem 1 (explicit formula for a_p bias) | **Heuristic 1** | Error term is O(1), not o(1); Tauberian argument unjustified |
| Theorem 2 (L-value lower bound) | **Conjecture 2** | Conditional on GRH (open conjecture) |
| Theorem 3 (disc-rank correlation) | **Speculation 3** | No known mechanism; small sample; Cohen-Lenstra predicts no correlation |
| Theorem 4 (parity from convergence) | **Retracted** | Internally contradictory; limit is −r for all r, parity not detectable |

---

## What Survives

Per RETRACTION.md, the following are genuine contributions:

1. **Computational infrastructure:** a_p computation, L-value estimation, BSD verification pipeline
2. **Numerical evidence:** |Ш|_an ≈ 1 for rank 2 curves with N ≤ 50,000 (consistent with LMFDB)
3. **The finite-torsion observation:** A[p]^{G_Q} = A(Q)[p] = 0 for p > |A(Q)_tors| (correct, standard)
4. **The 115-direction survey:** ~70–80% accurate as a literature map
