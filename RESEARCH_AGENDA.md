# BSD Research Agenda — Revised

**Date:** 2026-09-14
**Source:** Expert review (50 directions) + corrections

## Corrections to Previous Summary

### "Every existing Selmer control theorem caps at rank 1" — FALSE
- Kim's results address Selmer groups of arbitrary rank under stated hypotheses
- Castella proves κₚ≠0 ⟹ dim Sel = 2 in specified settings (CM and partial non-CM)
- The productive question: for (389.a1, p=5), which exact hypothesis remains unavailable?

### "BSD ratio = 1 confirms |Ш| = 1" — FALSE
- A numerically computed ratio near one supports the BSD-predicted order
- It does not independently determine the algebraic group
- Genuine descent gives Ш[2]=0 ⟹ Ш[2^∞]=0
- Does NOT eliminate odd-primary components

### Correct achievement statement:
> Certified rank-two arithmetic and vanishing of the 2-primary Sha component;
> numerical leading-term agreement with BSD.

## Three Bounded Workstreams

### Primary: Direction 50 — Effective Local-Solubility Precision Bound

**Goal:** Prove a theorem, not reproduce an existing algorithm.

**Theorem candidate:**
> For a specified class of normalized 2-coverings C/Q_p, local solubility is
> equivalent to a specified finite congruence test at an explicitly bounded precision.

**Required dossier:**
- Objects: which covering curves, local fields, normalized models
- Bound: explicit precision N with every dependency stated
- Correctness: why the finite calculation decides the claimed local condition
- Difficult cases: singular residue classes, bad reduction, wild behavior at 2
- Novelty: what the closest published result does not already provide
- Application: a descent calculation or theorem that becomes stronger

**Classification gates (must answer honestly):**
1. New bound or broader theorem → pursue as mathematical research
2. Known theorem with better certified implementation → pursue as computational research
3. Restatement of existing result → retain as infrastructure, not discovery

**Starting point:** Compare with Cremona-Fisher-O'Neil-Simon-Stoll (arXiv:1107.3516).
State exactly what our bound adds beyond their algorithm.

### Supporting: Direction 49 — Lean Certificate for Real Descent Data

**Goal:** Verify an arithmetic certificate actually used by the descent.

**Not:** "337 lines of Lean." The value is a sound implication:
```
certificate accepted ⟹ a precisely stated arithmetic conclusion
```

**Check:**
- Does the theorem concern genuine mathematical objects or abstract substitutes?
- Which arithmetic facts are assumptions?
- Does the proof depend on sorry or an axiom containing the desired conclusion?
- Does the checker establish completeness where completeness is needed?

**Target:** A modest checker for a genuine local-solubility certificate is more
valuable than a broad "BSD formalization" whose arithmetic content is assumed.

### Exploratory: Fixed-Prime Application of Existing Higher-Rank Theory

**Goal:** One theorem-application sheet for (389.a1, p=5).

**Required sheet:**
- Exact theorem and version (Kim, Castella, or Burns)
- Every hypothesis listed
- Evidence for each hypothesis for 389.a1 at p=5
- Exact conclusion
- Remaining gap to the next desired statement

**Distinctions (never substitute one for another):**
- Modular-symbol nonvanishing
- Finite-level Selmer information
- p^∞-Selmer structure
- Mordell-Weil rank
- Ш finiteness
- Complex BSD leading term

**For Kim/Kurihara route:** The hypothesis (H3) "analytic rank ≤ 1 or IMC" fails
for 389.a1 (analytic rank = 2). Identify what would need to be proven to bridge this gap.

**For Castella route:** The generalized Kato class κₚ exists. The question is
whether κₚ ≠ 0. This is the Darmon-Rotger conjecture (open for non-CM).

## Success Criterion

> One correct, explicitly scoped theorem or certified algorithm, independently
> checked by an arithmetic specialist, with a documented improvement over prior work.

Neither "we are close to BSD" nor "nothing works beyond rank one" is accurate.

## Frozen Directions

All other directions (1-48, excluding 49-50) are frozen until one of the three
workstreams produces a result worth extending.
