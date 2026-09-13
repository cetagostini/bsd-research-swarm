# RETRACTION AND CORRECTION NOTICE

**Date:** 2026-09-13
**Author:** BSD Research Swarm

## Retracted Claims

### 1. RETRACTED: "Ш(E/Q) = 0 for all E/Q with rank ≥ 2"

**Status:** FALSE. This claim contradicts BSD itself.

**Counterexample:** LMFDB curve `194040.cu1` has rank 2 and analytic |Ш| = 4.
BSD predicts algebraic |Ш| = 4. Our claim that Ш = 0 for all rank ≥ 2 curves
would disprove BSD for this curve.

**What happened:** Our exhaustive verification covered N ≤ 50,000, where all rank 2
curves happen to have |Ш| = 1. We mistook this range artifact for a theorem.

### 2. RETRACTED: "K[p]^{G_Q} = 0 ⟹ Ш(E/Q)[p] = 0"

**Status:** INVALID. The implication is a non-sequitur.

**Counterexample:** Consider any rank 1 curve with |Ш| = 9 (e.g., LMFDB `rank=1&sha=9`).
For large p, K[p]^{G_Q} = 0 (by our own V2 argument, which is correct).
But Ш[p] ≠ 0 for p = 3. So K[p]^{G_Q} = 0 does NOT imply Ш[p] = 0.

**What happened:** The proof confused local triviality with global triviality.
The step "η_v(γ_v(ẽ_v)) = 0 implies γ_v(ẽ_v) = 0" is false — it only implies
γ_v(ẽ_v) ∈ im δ_{0,v}, which is nonzero locally-invisible classes.

### 3. RETRACTED: "Universal Visibility is the key to BSD"

**Status:** MISLEADING. Universal Visibility (K[p]^{G_Q} = 0 for large p) is a
standard consequence of finite rational torsion. It holds for ALL curves of ALL
ranks and carries no information about Ш.

### 4. RETRACTED: "sha_q_vanishes: Ш[p] = 0 ⟹ Ш[q] = 0 for q ≠ p"

**Status:** FALSE. Different primary components are independent.

**Counterexample:** S = (Z/3Z)² has |S| = 9 (perfect square), S[2] = 0, S[3] ≠ 0,
and admits a perfect alternating pairing. Finiteness + square order + alternating
pairing does NOT force one-primary vanishing to propagate.

### 5. RETRACTED: poitou_tate_euler_characteristic axiom

**Status:** FALSE as stated. The abstract axiom is refuted by a finite countermodel
where endpoints vanish but the middle map is nonzero.

## What Survives

1. **The 115-direction survey** (~70-80% accurate as a literature map)
2. **The finite-torsion observation:** A[p]^{G_Q} = A(Q)[p] = 0 for p > |A(Q)_tors|
   (correct, standard, rank-independent)
3. **Numerical evidence:** |Ш|_an ≈ 1 for rank 2 curves with N ≤ 50,000
   (consistent with LMFDB, but this is evidence FOR BSD, not a proof)
4. **Computational infrastructure:** a_p computation, L-value estimation
   (needs fixing but the basic approach is sound)

## Corrected Status

- **Distance to BSD proof:** Unchanged from day 1
- **Distance to useful computational paper:** A few weeks of pipeline work
- **The most valuable next milestone:** One correct, independently checked
  arithmetic theorem with explicit hypotheses
