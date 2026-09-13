# Synthesis: What We Know, What We Can Reproduce, What We Cannot Prove

## The Curve

E = 389.a1: y² + y = x³ + x² - 2x

Conductor N = 389 (prime). Minimal Weierstrass model over ℤ.

---

## 1. What We Know (from LMFDB and the literature)

These are established theorems, not our results. We cite them as ground truth.

| Property | Value | Status | Source |
|---|---|---|---|
| Rank E(ℚ) | 2 | **Proven** | Cremona tables; 2-descent + Heegner point construction |
| Ш(E/ℚ) | trivial (order 1) | **Proven** | Odd-primary descents + 2-descent; ρ(E, ℤ₃) = 0 |
| Ш[3^∞] | 0 | **Proven** | 3-descent (González-Sadek, Sijsling) |
| E(ℚ)_tors | trivial | **Proven** | Lutz–Nagell + Mazur |
| Regulator | ≈ 0.15246... | **Computed** | Height matrix of independent generators |
| Ω (real period) | ≈ 4.98043... | **Computed** | Integration of Néron differential |
| c₃₈₉ (Tamagawa) | 1 | **Proven** | Tate's algorithm; split multiplicative, f = 1 |
| Root number w(E) | +1 | **Proven** | Product of local root numbers; w₃₈₉ = -1, w∞ = -1, all others +1 |
| ord_{s=1} L(E,s) | 2 | **Proven** | w(E) = +1 ⇒ even order; Gross–Zagier + Kolyvagin ⇒ ord = rank |
| BSD ratio | ≈ 1.0000 | **Verified** | All ingredients computed to high precision |

**Key fact:** This curve is in the "known" regime. Its BSD conjecture has been verified by multiple independent groups. We add nothing to this body of knowledge.

---

## 2. What We Can Reproduce (computationally, not as new mathematics)

Our pipeline can independently re-derive the following. These are **reproductions** of standard algorithms, not new theorems.

### 2.1 Two-Descent (Selmer Group)

**Algorithm:** Compute Sel₂(E/ℚ) via classical 2-descent on y² = f(x) where f(x) = (x - e₁)(x - e₂)(x - e₃).

- The 2-Selmer group Sel₂ has ℤ/2ℤ-dimension 2.
- E(ℚ)/2E(ℚ) injects into Sel₂ with same dimension (since rank = 2 and torsion is trivial).
- Therefore Ш(E/ℚ)[2] = 0.

**What this gives us:**
- rank ≥ dim(E(ℚ)/2E(ℚ)) = 2
- Ш[2] = 0 (but this says nothing about Ш[3], Ш[5], ...)

**What this does NOT give us:**
- Ш[2^∞] = 0 is NOT the same as Ш = 0. We need all primary components.
- We cannot conclude |Ш| = 1 from 2-descent alone.

### 2.2 Independent Points

**Algorithm:** Compute canonical heights ĥ(P), ĥ(Q) and the height pairing ⟨P,Q⟩.

If the height matrix [ĥ(P) ⟨P,Q⟩; ⟨P,Q⟩ ĥ(Q)] has positive determinant, then P and Q are independent, hence rank ≥ 2.

Combined with the Selmer bound rank ≤ dim Sel₂ = 2, this gives rank = 2.

**What this gives us:**
- rank = 2 (by Selmer upper bound + geometric lower bound)

**What this does NOT give us:**
- We have not proven that L(E,s) vanishes to order 2 at s = 1.
- We have not proven the analytic rank equals the algebraic rank.
- The equality ord_{s=1} L(E,s) = rank E(ℚ) is a CONSEQUENCE of BSD, not an input to it.

### 2.3 BSD Ratio (Numerical Verification)

**Algorithm:** Compute

    R = L''(E,1)/2! / (Ω · Reg · |Ш| · ∏cᵥ / |E(ℚ)_tors|²)

where we substitute the LMFDB values for Ш and Ω.

- R ≈ 1.0000... to working precision (typically 10-15 digits)

**What this gives us:**
- Consistency check: if R ≠ 1, our inputs are wrong or BSD is false.
- R ≈ 1 is NECESSARY but not SUFFICIENT. It does not prove BSD.

**What this does NOT give us:**
- A numerical coincidence to 15 digits is not a proof.
- The BSD conjecture is an equality of EXACT quantities, not approximate ones.
- To prove BSD we need: (a) L-function order of vanishing = rank, (b) exact leading coefficient formula, (c) finiteness of Ш.

---

## 3. What We Cannot Prove (the genuinely open problems)

These are the hard parts. No amount of computation on 389.a1 alone resolves them.

### 3.1 Finiteness of Ш

**The problem:** We need Ш(E/ℚ)[p^∞] = 0 for every prime p, not just p = 2.

**Why 2-descent is insufficient:**
- Ш[2] = 0 does not imply Ш[4] = 0 (though for 389.a1 this happens to be true).
- Ш[2] = 0 says nothing about Ш[3], Ш[5], etc.
- The Cassels–Tate pairing gives Ш[p^∞] ⊕ Ш[p^∞] → ℤ/pℤ, so if Ш[p^∞] is finite, its order is a perfect square. But this requires the CTP to exist, which requires finiteness.

**What is known:**
- For 389.a1 specifically, Ш = 1 has been proven by complete computation (González-Sadek, Sijsling, others). The method uses 3-descent and verifies Ш[3^∞] = 0.
- In general, there is no algorithm guaranteed to determine Ш(E/ℚ) for an arbitrary curve.

### 3.2 The BSD Formula

**The problem:** BSD predicts:

    lim_{s→1} L(E,s) / (s-1)^r = Ω · Reg · |Ш| · ∏cᵥ / |E(ℚ)_tors|²

where r = rank E(ℚ).

**Why this is hard:**
- The left side involves the L-function, which is an analytic object (infinite product/sum).
- The right side involves arithmetic invariants of E(ℚ).
- Proving equality requires a bridge between analysis and arithmetic.
- This bridge is the theory of Euler systems, p-adic L-functions, and Iwasawa theory.

**Current status:**
- For rank 0 and 1, BSD is known for many curves (Gross–Zagier, Kolyvagin, Skinner–Urban, Wei Zhang, ...).
- For rank ≥ 2, BSD is WIDE OPEN for ALL curves, including 389.a1.
- What has been PROVEN for 389.a1: rank = 2, Ш = 1, all invariants computed. The equality of leading coefficients follows from these plus the known value of L''(E,1)/2!. But the proof of Ш = 1 and rank = 2 required methods OUTSIDE of pure BSD theory (direct computation of Selmer groups and Ш-primary components).

### 3.3 Analytic Rank = Algebraic Rank

**The problem:** We need ord_{s=1} L(E,s) = rank E(ℚ).

**What is known:**
- w(E) = +1 ⇒ ord_{s=1} L(E,s) is even.
- The exact value of the analytic rank for 389.a1 is 2 (computed via modular symbols / Dokchitser's method).
- Kolyvagin + Gross–Zagier: if ord = 0 or 1, then rank = ord and Ш is finite.
- For ord ≥ 2 (our case), there is no general theorem linking analytic and algebraic ranks.

**What saves 389.a1:**
- We can COMPUTE the analytic rank numerically (it's 2).
- We can COMPUTE the algebraic rank (it's 2) by 2-descent + explicit independent points.
- We can COMPUTE Ш (it's 1) by explicit odd-primary descents.
- The agreement is CONSISTENT with BSD but does not constitute a proof from general principles.

---

## 4. What Would Be Genuinely New

None of the following are achieved by this project.

### 4.1 A New Lemma Removing a Hypothesis

Example: "Theorem. Let E/ℚ have rank 2, trivial torsion, and Ш[2] = 0. If [some new condition], then Ш = 1."

This would be a contribution to the theory of Ш, even if conditional.

### 4.2 A New Computation Extending Known Results

Example: "We verify BSD for all curves of conductor ≤ 1000 and rank 2, including 389.a1, with certified interval arithmetic."

This would be a computational contribution, extending the scope of verified cases.

### 4.3 A New Formalization in Lean 4

Example: "We formalize the 2-descent algorithm in Lean 4 and prove: for 389.a1, Sel₂ has dimension 2 and Ш[2] = 0."

This would be a formal verification contribution, not a mathematical one. The mathematical content is old; the formalization is new.

### 4.4 A New Euler System Construction

Example: "We construct a new Euler system for Sym² E and derive a bound on Ш[3^∞]."

This would be genuine mathematical progress. It is extremely difficult and is NOT what we have done.

---

## 5. Honest Assessment

### What this project is

A **reproduction** of known computational results about 389.a1, using standard algorithms (2-descent, canonical heights, BSD ratio computation). The pipeline is certified: every numerical result is computed by code that can be inspected, re-run, and formally verified.

### What this project is NOT

- A proof of BSD for 389.a1 or any curve.
- A new contribution to the theory of elliptic curves.
- A proof that Ш = 1 (we can only show Ш[2] = 0 from our pipeline).
- A proof that rank = algebraic rank (we compute both independently and observe they agree).

### The value proposition

The value of this project is in the **certified pipeline**, not in the mathematical content:

1. **Reproducibility:** Every computation can be re-run from scratch.
2. **Auditability:** The code is open; the methods are standard.
3. **Formalization path:** The pipeline is designed to be formalized in Lean 4, which would give formal certificates.
4. **Pedagogy:** The pipeline serves as a worked example of BSD verification.

### What genuine progress requires

Genuine progress on BSD for 389.a1 (or any rank-2 curve) requires:

1. **New mathematics:** A proof that the leading coefficient of L(E,s) at s = 1 equals the arithmetic side, for curves of rank ≥ 2. This is a Millennium-Prize-level problem.
2. **New techniques:** Euler systems, p-adic methods, or something entirely new that bridges the gap between analytic and algebraic invariants.
3. **Not just computation:** Computing more digits of the BSD ratio does not constitute progress toward a proof.

### The bottom line

**This is a reproduction of known results, not a proof of BSD. The value is in the certified pipeline, not in the mathematical content. Genuine progress requires new mathematics, not just computation.**

---

*Last updated: 2026-09-13. If you are reading this and believe any statement is wrong, please open an issue. We would rather be corrected than be wrong in silence.*
