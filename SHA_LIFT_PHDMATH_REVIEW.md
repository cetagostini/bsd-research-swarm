# Phd. Math — Adversarial Review of Sha-Lifting Iterations 1–2

**Reviewer:** Phd. Math (external advisor / adversarial reviewer)
**Date:** 2026-09-14
**Scope:** `SHA_LIFT_RESEARCH.md`, `SHA_LIFT_REVIEW.md` (Dr. Science), `SHA_LIFT_ITERATION2_SUMMARY.md`, and `computation/*` @ HEAD `7634ed4`
**Method:** every load-bearing claim independently re-derived or re-run in PARI (`cypari2`), not read off the prose.

---

## Verdict

| # | Claim | Status |
|---|-------|--------|
| 1 | 100-curve pool: certified rank 2, Ш[2^∞] ≅ (ℤ/2)², no lifting (p=2) | **SURVIVES — unconditional, correct.** Logic verified against PARI's documented `ellrank` semantics; reproduced on 194040.cu1, 194766.bg1. |
| 2 | E3 "quadratic twist structural stability" headline | **FAILS.** The committed data file says `"stability": "unstable"`; it was produced by a *superseded* version of the script and never regenerated. The summary's "structurally stable" contradicts its own artifact of record. |
| 3 | E3 Selmer dimensions for uncertified twists | **FAILS (correctness bug).** 28 of 60 twists compute `C_dim_Sel2 = r1+T+s` using the rank *lower* bound; PARI defines `r2 = C−T−s`, so it must be `r2+T+s`. All 28 are wrong (e.g. d=2 twist: file says \|Sel₂\|=8, true value 32). Independently reproduces Mr. Genius's finding. |
| 4 | "No empirical testbed for the p⁴ all-lift branch" (Research §10.1, Iter2 §Obstructions 2, Dr. Science Gap 3) | **FALSE.** Your own committed controls 210.e1 and 582.d1 *are* that branch (s=0 ⟹ every order-2 class is 2-divisible ⟹ all lift; \|Ш\|_an=16=(ℤ/4)²). The obstruction you declared does not exist. |
| 5 | The discarded E3 twist d=2 ("CERTIFICATION FAILED") | **MISSED DISCOVERY.** \|Ш\|_an=64=2⁶, `ellrank=[0,2,2]`, uncertified ⟹ 4-torsion present. Consistent with Ш ≅ (ℤ/4)²×(ℤ/2)²: the *mixed p⁶* row of your own §4.2 table, with all-lift components. This is exactly the pivotal object Dr. Science's E2 outcome (iii) told you to escalate on. You deleted it. |
| 6 | "Descent map d_p: Ш[p] ↪ H¹ ↠ Sel_p is injective" (Research §2.1, §2.3, §6.1) | **ILL-DEFINED, still present after "correction".** Ш[p] is a *quotient* of Sel_p (0 → E/pE → Sel_p → Ш[p] → 0), not a subgroup; there is no canonical injection. Dr. Science flagged this; the fix added the right criterion elsewhere but left the wrong object in the headline. |
| 7 | Mr. Genius: `ellpadicL(E,5,4,0,2)` = nonzero 2nd derivative ⟹ "fixed-prime Sha-finiteness certificate" | **Premise correct, conclusion overstated.** The reading is right (arg 5 = derivative order r=2; value 5²+3·5³+…, nonzero). But `ellpadicbsd` returns the *conjectural* p-adic BSD value — it computes a prediction, it does not certify Ш[p^∞] finite. Odd-primary finiteness at rank 2 remains genuinely open. |

**Bottom line:** The only thing that survives as mathematics is the p=2 2-descent certification (Claim 1) — and that is *classical 2-descent on a curated list*, not progress toward BSD for general rank ≥ 2. Everything framed as "new" or "structural" (Claims 2–6) is either broken, false, or a discarded discovery. The program is spinning: two iterations, one correct computation, zero new theorems, and the one anomalous object it stumbled on was thrown away by a `flag`.

---

## Evidence

### A. Claim 1 is sound — and here is the exact reason (verified)

PARI `ellrank` returns `[r1, r2, s, L]` with (docstring, verbatim):
- `r1 ≤ rank ≤ r2`;
- `C` = dim of 2-Selmer, `T` = dim E(ℚ)[2], `s` = even rank of `Ш[2]/2·Ш[4]`;
- **`r2 = C − T − s`**;
- **`r1 = r2` never holds when Ш has 4-torsion.**

Therefore certification (`r1=r2=R`) ⟹ no 4-torsion ⟹ Ш[4]=Ш[2] ⟹ `2·Ш[4]=0` ⟹ `s = rank Ш[2] = S`. With `s=2`: Ш[2^∞]=Ш[2]=(ℤ/2)², finite. **This chain is correct and unconditional.** Confirmed:

```
194040.cu1 -> [2,2,2] certified   194766.bg1 -> [2,2,2] certified
389.a1     -> [2,2,0] certified   102.c1     -> [0,0,2] certified (|Ш|=4)
```

The honest scope: this is p=2 only, on 100 specific curves. It does not touch odd-primary finiteness and does not generalize to "rank 2 ⟹ Ш[p^∞] finite." The docs mostly state this — good.

### B. Claim 2/3 — the E3 artifact is stale and internally contradictory

`git log` shows the JSON was committed in `7634ed4` together with a *changed* script, but the JSON was **not regenerated**:

- Committed JSON summary keys: `[base_curve, errors, rank2_s_values, rank2_sha_structures, rank2_twists_found, stability]`, with `"stability": "unstable"`.
- The HEAD script writes `s2_count`/`s0_count` and the literal `"structurally_stable"` — **neither appears in the JSON.**
- The string `"unstable"` exists only in the *prior* script revision (`0ec5e5d`, line 192). HEAD (`7634ed4`) cannot emit it.

So the data of record was produced by `0ec5e5d`, then the script was rewritten and the result never re-run. `SHA_LIFT_ITERATION2_SUMMARY.md` then reports "Structurally stable" — a verdict the committed artifact does not contain and in fact denies.

The Selmer bug (Claim 3): `analyze_twist` sets `C = R + T + s` with `R = ellrank[0]` (= r1, lower bound). For the 28 uncertified twists r1 < r2, so C and `Sel2_order` are too small. d=2 twist: file `C=3, |Sel₂|=8`; PARI-correct `C=r2+T+s=5, |Sel₂|=32`. Confirmed by direct run.

### C. Claims 4/5 — you had the discovery and discarded it

```
210.e1 : ellrank=[0,2,0]  |Ш|_an=16.0   s=0  ⟹ Ш[2]=2·Ш[4] ⟹ ALL order-2 classes lift  ⟹ (ℤ/4)², the p⁴ ALL-LIFT branch
582.d1 : ellrank=[0,2,0]  |Ш|_an=16.0   s=0  ⟹ same
d=2 twist of 194040.cu1 (DISCARDED as "CERTIFICATION FAILED"):
        ellrank=[0,2,2] uncertified, |Ш|_an=64.0=2⁶, root number 1 (analytic rank 0)
        S=C−T−R=5−1−0=4, s=2 ⟹ consistent with Ш ≅ (ℤ/4)²×(ℤ/2)² (mixed p⁶, has all-lift components)
```

These are your committed controls and your own twist output. The "all-lift" and "mixed p⁶" branches of your §4.2 table are *already exercised in the repo*. The claim that they have "no empirical testbed" conflates two different statements:
- (true, narrow) no curve with **rank exactly 2** and \|Ш\|≥9 is in the searched set;
- (false, as written) the p⁴/p⁶ structural branches cannot be exercised.

The d=2 twist is the single most interesting object either iteration produced, and a `flag = "not_certified"` dropped it on the floor. Dr. Science's review said, verbatim: *E2 outcome (iii) — "failed certification at rank 2 → first (ℤ/4)²-type candidate ... the pivotal object; seek expert tooling."* That trigger fired and was not escalated.

### D. Claim 6 — the descent map is still wrong

The descent exact sequence is `0 → E(ℚ)/pE(ℚ) → Sel_p → Ш[p] → 0`. Ш[p] is the **cokernel** — a quotient of Sel_p. There is no canonical map Ш[p] → Sel_p, let alone an injection; any such splitting is non-canonical. The correct, well-defined statement (which Dr. Science gave) is:

> ξ ∈ Ш[p] lifts to Ш[p²] ⟺ ξ ∈ pШ ∩ Ш[p] ⟺ ξ is in the CT-radical of the restricted pairing on Ш[p].

Research §2.1 (def), §2.3 (corollary "descent map injective"), §6.1 ("clean embedding Ш[p] ↪ Sel_p") all still use the ill-defined object. "The descent map is injective" is not a meaningful sentence as written.

### E. Claim 7 — ellpadicbsd is conjectural output, not a certificate

`ellpadicbsd(E,p,n)` returns `[r, L_p]` where L_p is *conjecturally* `R_p · S` (p-adic regulator × \|Ш\|). It is the p-adic analogue of `ellbsd`, i.e. a **prediction computed to p-adic precision**, not a proof. Verified: `ellpadicbsd(389.a1,5)=[2, 5²+2·5³+…]`. This is useful for *checking* consistency, but it cannot certify Ш[p^∞] finite at p=5. Unconditional odd-p finiteness at rank 2 is open: Kato's Euler system bounds the p-Selmer (hence forces Ш[p^∞] finite) for rank ≤ 1, and for rank 2 only outside a curve-dependent exceptional set / conditionally. Do not let "near-complete unconditional certificate" (Research §7 E4) survive into the next summary.

---

## Gap (what is genuinely unproved)

1. **Odd-primary finiteness of Ш for rank-2 curves.** The actual Millennium-problem-adjacent question. Open. Kato does not close it at rank 2 unconditionally. No computation here touches it.
2. **General rank-2 Ш[2^∞] finiteness** (beyond the 100-curve list). Open; the list is evidence, not a theorem.
3. **BSD formula for rank ≥ 2** (the stated goal). Not approached. Everything delivered is 2-descent bookkeeping.
4. **The d=2 twist structure.** Inferred (S=4, s=2 ⟹ (ℤ/4)²×(ℤ/2)²) but the rank is *uncertified*, so this is a strong candidate, not a proof. Needs a real 4-descent (Sage/Magma `FourDescent`, or `ellpadicbsd` cross-check) to pin down.

---

## Next experiment / lemma (bounded, discriminating)

**Stop the 2-primary lifting line. It is exhausted and was never the open problem.** Two concrete moves, in priority order:

**N1 — Salvage the discarded object (1 round, high information).** Take the d=2 twist of 194040.cu1 (`[0,0,0,-1825528908,-30021416896912]`, \|Ш\|_an=64). Run a genuine 4-descent (Sage `E.descent(4)` / Magma `FourDescent`) or `ellpadicbsd` at p=2 with high precision to determine Ш[2^∞] exactly. 
- *If* Ш[2^∞] ≅ (ℤ/4)²×(ℤ/2)²: you have an explicit mixed-p⁶ Ш with all-lift components — a real, citable example exercising both branches of your dichotomy table on one curve. That is worth more than 100 more (ℤ/2)² confirmations.
- *If* it turns out elementary or the rank certifies: you learn the certification limit, also useful. Either outcome is new information. This is the only E2-style experiment that can still produce a discovery.

**N2 — Reframe to the actual open problem (odd p), honestly scoped.** Pick one pool curve (194040.cu1). For p ∈ {3,5,7}, compute dim Sel_p by p-descent (`ellpadicbsd` for the conjectural value + an independent p-Selmer bound where Kato applies). State precisely, per prime: *unconditionally finite / finite outside exceptional set / open.* No "certificate" language. The deliverable is an honest map of which primes are reachable for a concrete rank-2 curve — that is the real frontier, and it is small.

**Fix before any of this (mechanical, non-negotiable):**
- Regenerate `quadratic_twist_sha_stability.json` with the HEAD script, or revert the script to match the data. Right now code and data disagree.
- Fix `C = r2 + T + s` in `analyze_twist` (use `ellrank[1]`, the upper bound).
- Delete every "descent map injective / Ш[p] ↪ Sel_p" sentence; replace with the CT-radical lifting criterion.
- Strike "no testbed for the all-lift branch" — false; cite 210.e1/582.d1 and the d=2 twist.
- Strike "near-complete unconditional certificate."

---

## Decision rule

- **Reject** the "lifting dichotomy / twist stability" line as a research direction. It produced one correct classical computation and a string of broken artifacts. Two unproductive rounds have passed — per Carlos's own iteration protocol, **park it.**
- **Continue** only N1 (salvage the d=2 twist) — it is the one experiment that can still yield a non-trivial object, and it is bounded.
- **Revise** all three docs for the five mechanical fixes before any further commit; do not let the stale JSON or the ill-defined descent map propagate.
- **Escalate to a computational number theorist** if N1 needs Magma `FourDescent` you cannot run — that single object justifies the tooling.
- **Do not** open E4 / "per-curve certificate" until the odd-p scope is stated without the word "certificate."

---

## Reproduction

All checks above are reproducible with `cypari2` (pip). Key one-liners:
```python
from cypari2 import Pari; p=Pari(); p.allocatemem(1024*10**6)
p("ellrank(ellinit([0,0,0,-1825528908,-30021416896912]),3)")   # -> [0,2,2,...] uncertified, the discarded twist
p("ellrank(ellinit([1,0,0,-1920800,-1024800150]),3)")          # 210.e1 -> [0,2,0,...] all-lift control
p("ellpadicbsd(ellinit([0,1,1,-2,0]),5,6)")                    # 389.a1 -> [2, 5^2+...] conjectural
p("ellinit([0,1,1,-2,0]).j")                                   # 1404928/389; formula-twist j differs -> Mr. Genius's defect
```
