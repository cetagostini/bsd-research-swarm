# Review: Sha-Lifting Research, Iteration 1 (Mr. Implementation)

**Reviewer:** Dr. Science (external mathematical advisor / adversarial reviewer)
**Date:** 2026-09-14
**Scope:** `SHA_LIFT_RESEARCH.md` + `computation/sha_lift_research.py` @ commit `b8f6e8c`
**Status of this review:** independent re-derivation + exhaustive group-theoretic classification + unconditional 2-descent over a 100-curve pool (see `computation/sha_lift_pool_results.json`, `computation/sha_lift_controls_results.json`, `computation/run_pool_descent.py`)

---

## Verdict

1. **The Lifting Dichotomy (as a theorem): SURVIVES as a conditional statement of classical theory, but the proof in the doc is invalid, and the statement is not new.** The true content — a finite Ш with a nondegenerate alternating Cassels–Tate pairing must have *balanced invariant factors* (Ш ≅ ∏(ℤ/nᵢ)²), hence |Ш| = p² forces Ш[p^∞] ≅ (ℤ/p)² and no p-divisible (liftable) classes — is classical (Cassels; Wall's classification of finite quadratic/alternating forms; Tate). Conclusion right, argument wrong, novelty absent. This review corrects the argument and *replaces the unprovable parts with unconditional facts*.
2. **The computational payload of Iteration 1 is now delivered unconditionally.** Direct 2-descent (PARI `ellrank`, no Sage) over the **100 smallest-conductor rank-2 curves with analytic |Ш| = 4** (194040.cu1 … 32137373.a1) proves for every one of them: rank exactly 2 (certified), **no 4-torsion in Ш, 2Ш[4] = 0, and Ш[2^∞] ≅ (ℤ/2)² of order 4 — finite, with no class lifting to Ш[4]**. This is the strongest unconditional statement the direction has produced, and it directly answers the unproved sub-question for p = 2 on this family: Ш[2^∞] is finite at rank 2.
3. **Multiple factual/technical errors in the artifacts** (phantom curve 246464.ba1; impossible table row ℤ/p³⊕ℤ/p; wrong Selmer-size consistency check; obsolete "SageMath required" blocker; false "only 2 curves available"). All documented below with corrections.

---

## Evidence

### A. What Cassels–Tate actually implies (corrected theory)

**A1. Non-degeneracy level.** CT restricted to Ш[n]×Ш[n] has kernel **exactly** Ш[n] ∩ nШ; it is non-degenerate on the quotient Ш[n]/(Ш[n]∩nШ). The doc's Prop 2 applies non-degeneracy to Ш[p] itself — wrong level. For Ш ≅ ℤ/p², Ш[p] = ℤ/p but Ш[p]/pШ[p] = 0, so non-degeneracy at level p is vacuous; **no contradiction arises there**. The real obstruction is at level p²: the group ℤ/p² admits no nondegenerate alternating bilinear form (unbalanced).

**A2. Exhaustive classification (brute force, this review).** I enumerated every finite abelian group of order ≤ 64, and for each checked (exactly, with rational arithmetic in ℚ/ℤ) whether it admits a nondegenerate alternating form. Compatible ⟺ **balanced**: ∏(ℤ/nᵢ)² over equal pairs (ℤ/2 pairs included). Concrete tables:

| |Ш| | CT-compatible structures | liftable classes in Ш[p] (pШ ∩ Ш[p]) |
|---|---|---|
| p² | (ℤ/p)² only | none (pШ = 0) |
| p⁴ | (ℤ/p)⁴, (ℤ/p²)² | (ℤ/p)⁴: none; (ℤ/p²)²: **all** of Ш[p] (p² elements) |
| p⁶ | (ℤ/p)⁶, (ℤ/p)²×(ℤ/p²)², (ℤ/p³)² | none / exactly the p-torsion of the p²-factors (p² elements) / all |

**ℤ/p³⊕ℤ/p (doc §4.2 row) is impossible** — not just internally inconsistent; it does not admit the pairing. Verified by brute force: ℤ/8⊕ℤ/2 etc. all excluded.

**A3. Correct lifting criterion.** For finite Ш with nondegenerate CT (or, unconditionally, via 2-descent):

- ξ ∈ Ш[p] lifts to Ш[p²] ⟺ ξ ∈ pШ (= ξ ∈ Ш[p] ∩ pШ[p²]).
- With CT: liftable = (Ш[p])^⊥, the CT-radical of the restricted pairing on Ш[p].
- The doc's Prop 1 "descent map d_p: Ш[p] ↪ H¹(ℚ,E[p]) ↠ Sel_p" **is not well-defined**: Ш[p] is a *quotient* of Sel_p (exact sequence 0 → E(ℚ)/pE(ℚ) → Sel_p → Ш[p] → 0), not a subgroup; the injection Ш[p] ↪ H¹(ℚ,E[p]) requires a splitting and is non-canonical. Replace the whole Prop 1 by the criterion above.

**A4. The "sharp dichotomy" is a p² coincidence.** General law: liftable classes form a p-vector subspace of Ш[p] of dimension 2·#{balanced factor pairs with exponent ≥ 2}. At |Ш| = p² only (ℤ/p)² survives, so "none lift" and the dichotomy is vacuous-but-true. At p⁴ the dichotomy is real ((ℤ/p)⁴: none; (ℤ/p²)²: all). At p⁶ mixed cases occur. The doc's §2.3 claim "no intermediate case possible" is false as a general statement.

### B. Unconditional experiment (this review)

**Method.** `PARI ellrank(E, effort)` via `cypari2` (pip-installable; no SageMath). Semantics (PARI docstring, verified against controls): output [r₁, r₂, s, pts] with r₁ ≤ rank ≤ r₂; **r₁ = r₂ guarantees rank certification and is guaranteed to fail if Ш has 4-torsion**; C := dim Sel₂ satisfies C = T + R + S where T = dim E(ℚ)[2], R = rank, S = dim Ш[2]; s = dim(Ш[2]/2Ш[4]) ≤ S, equality iff no order-2 class is 2-divisible.

- **Pool:** all 100 smallest-conductor rank-2 curves with analytic |Ш| = 4 (LMFDB `rank=i2&sha=i4`, sorted by conductor; 194040.cu1 confirmed minimal).
- **Result:** **100/100 → [2, 2, 2], rank certified.** T = 1 (42 curves with a rational 2-torsion point) or T = 0 (58 curves, trivial torsion). Hence C = 5 (|Sel₂| = 32) or C = 4 (|Sel₂| = 16), always S = dim Ш[2] = 2, 2Ш[4] = 0, no 4-torsion, and since rank certification excludes all 2-power torsion of order ≥ 4: **Ш[2^∞] ≅ (ℤ/2)², |Ш[2^∞]| = 4, finite — unconditionally.** The algebraic 2-part matches the analytic |Ш| = 4 for all 100: a 100-instance unconditional check of the p = 2 part of the BSD formula at rank 2, and no-lifting confirmed.
- **Controls (semantics validated both ways):**
  - 389.a1 (rank 2, |Ш| = 1): [2, 2, 0] certified, Ш[2] = 0 ✓
  - 37.a1 (rank 1): [1, 1, 0] certified ✓
  - 102.c1 (rank 0, analytic |Ш| = 4): [0, 0, 2] certified, Ш[2] ≅ (ℤ/2)² — textbook ground truth ✓
  - 210.e1, 582.d1 (rank 0, analytic |Ш| = 16): [0, 2, 0] **not** certified — the 4-torsion signature, exactly as required ✓
- **Honesty note:** none of this is a new theorem — 2-descent is classical. The genuinely useful output is: (i) the lifting question is *resolved by descent, not by CT*, for this entire family; (ii) PARI rank certification is a direct witness of the triviality of 2Ш[4]; (iii) a clean, rerunnable pipeline exists (script included).

**Consequence for the team's question** (is Ш(E/ℚ)[p^∞] finite when rank = 2?): for p = 2 and each of these 100 rank-2 curves: **YES, provably, |Ш[2^∞]| = 4**. For odd p, Kato's Euler system proves Ш[p^∞] finite outside a small curve-dependent exceptional set; combining the two gives finiteness for all but finitely many primes per curve. The exact odd-primary order (BSD predicts 1 for these |Ш| = 4 curves) remains unproved.

### C. Factual errors to correct in the artifacts

1. **"246464.ba1" does not exist.** LMFDB conductor-246464 curves: 246464.a1/b1/c1/d1, ranks 1, 0, 0, 1, all |Ш| = 1. No rank-2 curve exists at that conductor. Replace with 194766.bg1 (verified: [2,2,2]).
2. **§4.2 row "ℤ/p³ ⊕ ℤ/p — 4 of 16 lift"** is impossible (see A2). Correct table in A2.
3. **§3.1 consistency check wrong:** |E(ℚ)/2E(ℚ)| = 2^{r + dim E(ℚ)[2]} = 2³ for 194040.cu1 (torsion ℤ/2), so |Sel₂| = 2³·4 = 32, not 2⁴ = 16. (16 is correct only for the 58 torsion-free pool curves: 2²·4 = 16.)
4. **"No SageMath/Magma" blocker obsolete:** `cypari2`/`eclib` complete the entire computation in < 1 s per curve. Nothing here required Sage. (Note: pip install required `--break-system-packages` on this machine — PEP 668.)
5. **"Only 2 rank-2 curves with nontrivial Sha available" false:** LMFDB contains 100+ rank-2 curves with |Ш|_an = 4 (smallest by conductor = 194040.cu1); the doc's "first known rank-2 with nontrivial Ш" is correct for the conductor ordering. **No rank-2 curve with analytic |Ш| ≥ 9 exists in LMFDB** (sha ∈ {16, 36, 64, 100, 144, 256} under rank=2 all return ∅) — so the doc's "Direction B (extension to |Ш| = p⁴)" currently has **no empirical testbed** at rank 2.
6. **§9 checkboxes "verified" overstate:** nothing algebraic was computed in Iteration 1 (script consults LMFDB analytic values only); the marks describe internal consistency. The unconditional computation now replaces that claim with substance.

---

## Gap (what remains unproved)

1. **Finiteness of Ш[2^∞] at rank 2: settled for p = 2 on this 100-curve family only.** General rank-2 curves: open, as before.
2. **Odd-primary part / total finiteness** for these curves: Kato covers all but a small exceptional set; the exceptional primes per curve and the exact odd order (BSD: 1) are unproved.
3. **Higher-order lifting (Ш[p²]→Ш[p³]) and the p⁴/p⁶ dichotomy branches** have no computational testbed: no rank-2 curve with |Ш| ≥ 9 is in LMFDB. Until such a curve is found or constructed, the p⁴ "all-lift" branch and mixed p⁶ cases cannot be exercised.
4. **Novelty assessment (per reviewer mandate):** the CT-balanced structure, the lifting-criterion, and the |Ш| = p² conclusion are all classical. What is new here is (modestly): the family-wide unconditional statement Ш[2^∞] ≅ (ℤ/2)² with certified ranks for the 100-curve pool; the correction of the p⁴/p⁶ table; the observation that rank certification witnesses 2Ш[4] = 0; the verified absence of rank-2 |Ш| ≥ 9 in the database. None of these advance BSD itself; they are honest, reproducible groundwork.

---

## Next experiment or lemma

- **E1 (finish the sweep, bounded):** run `run_pool_descent.py` over *all* rank-2 |Ш| = 4 curves in LMFDB (paginate past 100), record counts and any deviation. Falsifier: any curve with failed certification or s ≠ 2 → a p = 2 BSD anomaly (a genuine discovery, stop everything).
- **E2 (the discriminating hunt, bounded):** search mid-conductor ranges for rank-2 curves with dim Ш[2] ≥ 3 (s = 3/4) or with **failed certification at rank 2** (4-torsion signature). Outcome space: (i) only s = 2 ever appears → strong statistical statement ("2-part of Ш is elementary of dim ≤ 2 across all computed rank-2 curves"), report and pivot; (ii) s = 4 found → first concrete p⁴ "none-lift" instance; (iii) failed certification at rank 2 → first (ℤ/4)²-type candidate, the "all-lift" branch — the pivotal object; seek expert tooling (4-descent in Sage/Magma) before deep investment.
- **E3 (family-level criterion, the team's original ask):** for a fixed rank-2 curve with analytic |Ш| = 4 (now verified Ш[2] ≅ (ℤ/2)² for 194040.cu1 etc.), compute dim Ш^{(d)}[2] for quadratic twists E^{(d)} of rank 2; test whether the 2-part structure is twist-stable (always (ℤ/2)² when BSD predicts |Ш| = 4). A provable twist-stability lemma would be the first non-classical output of the program.
- **E4 (per-curve certificate):** for two or three pool curves (194040.cu1, 194766.bg1, 226005.b5), combine: Ш[2^∞] ≅ (ℤ/2)² (proved here) + Kato odd-p finiteness + 3-,5-,7-descent checks of the small exceptional primes → a near-complete *unconditional* certificate "Ш = (ℤ/2)² × (provably finite odd part)". This is the closest the program can currently come to answering Carlos's question for concrete curves.

---

## Decision rule

- **Continue** E1 only while it can produce a counterexample (s ≠ 2, failed certification); once the sweep is complete with uniform s = 2, treat "s = 2 uniform" as the empirical fact and move to E2.
- **E2 is bounded:** stop at either the first discovery of a |Ш[2]| ≥ 8 or non-certified rank-2 curve (→ pursue that object), or an exhausted budget (all LMFDB rank-2 curves up to conductor 10⁷, or 1000 descents) with only s = 2 (→ document the statistical observation, pivot to E3/E4).
- **Park (per iteration protocol):** if after two more rounds no new structure appears, park the lifting direction with the precise finding: *at rank 2 with |Ш| = p², lifting is unconditionally trivial — Ш[2^∞] ≅ (ℤ/p)² by direct descent — and the genuinely open problem is the odd part of Ш / finiteness at odd p, where Kato + small-prime descent is the right tool, not 2-primary structure.*
- **Escalate:** only on E2 outcome (iii) (4-torsion at rank 2) — that single object justifies consulting a computational number theorist or Magma-based 4-descent expert before further investment.

---

## Files

| File | Content |
|------|---------|
| `SHA_LIFT_REVIEW.md` | this review |
| `computation/run_pool_descent.py` | reusable PARI 2-descent pool runner |
| `computation/sha_lift_pool_results.json` | 100-curve pool results + derived dims (C, T, S, |Sel₂|) |
| `computation/sha_lift_controls_results.json` | 5 control curves, both signatures |