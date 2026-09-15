# Verified Strategy Inputs for Rank-2 BSD Program (Dr. Science)

**Date:** 2026-09-15
**Status:** independent verifications feeding the strategic re-direction (see thread). All values re-derived directly with PARI (cypari2), not read off prose.

---

## 1. Big-image eligibility of 194040.cu1 (input to Track A: per-curve Kato finiteness)

Frobenius-field irreducibility witnesses via nonsquare characteristic-polynomial discriminant:
`frob_q char poly X² - a_q X + q`, discriminant `D = a_q² - 4q`, nonsquare mod ell ⟹ E[ell] irreducible (Serre; standard).

E = 194040.cu1 = `[0,0,0,-456382227,-3752677112114]`, Δ = 4260366878423040. Bad primes {2,3,5,7,11}.

| ell | witness q (prime, good reduction) | a_q | D mod ell | nonsquare |
|----:|---:|---:|---:|---|
| 3  | 13  | -6 | 2  | yes |
| 5  | 23  | -8 | 2  | yes |
| 7  | 13  | -6 | 5  | yes |
| 13 | 19  | -4 | 5  | yes |
| 37 | 19  | -4 | 14 | yes |

So ρ_{E,ell} is irreducible at ell ∈ {3,5,7,13,37}. **CORRECTION (2026-09-15, verified with PARI):** 389 does not divide 194040 at all — Δ_min = 2¹¹·3⁸·5¹·7⁸·11¹, v₃₈₉(Δ) = 0, and N(E) = 194040. The valuation-1 transvection at 389 belongs to **389a1** (Δ = 389), not to this curve. The big-image input for Kato at {3,5,7,13,37} rests on the Frobenius-discriminant witnesses alone. **Consequence (corrected):** Kato's theorem does NOT by itself give Ш[p^∞] finite at rank 2 — an upper bound closing the Selmer-corank chain is an additional unproven input (see Kim arXiv:2404.05186, Thm 2.6/2.9, Prop 2.7). The missing step is exactly the lemma Track A must supply.

**Literature correction (2026-09-15):** "No rank-2 ℚ-curve with proven-finite Ш" is FALSE. Coates–Liang–Sujatha (arXiv:1005.4206, Thm 1.3) prove Ш(E_i/ℚ)[p^∞] = 0 for five rank-2 CM curves y²=x³−D·x (D = −14,17,−33,−34,−39) at every good split prime p ≡ 1 (mod 4), p < 30,000, unconditionally via Rubin's main conjecture for ℚ(i) — with only four unresolved (E,p) pairs (29, 277 for D=−14; 577 for D=−34; 17 for D=−39), none for D=17. Stein–Wuthrich prove Ш[p]=0 (hence Ш[p^∞]=0) for 1,534,422 non-CM rank-2 pairs (N ≤ 30,000, 5 ≤ p < 1000, ρ̄ surjective) and for 389a at all but one good ordinary p < 48,859. Banwait (arXiv:2609.08431, Sep 2026) extends the CM criterion to the cyclotomic side and settles p=577 for y²=x³−34x. Per-prime rank-2 Ш-finiteness is a **published** phenomenon for both CM and non-CM curves; the open statement is (a) horizontal: Ш[p]=0 for all p > M — open for every rank-2 curve — and (b) vertical total finiteness, i.e. (a) + (b) jointly, which is Ш finite outright.

## 2. Rank-2 CM curves over ℚ exist in abundance (input to Track B: Castella route)

Direct PARI sweep (ellrank, effort 1, rank certified = [2,2,s]):
- j=0 (CM by ℤ[ζ₃]): y² = x³ ± d, squarefree d, |d| ≤ 400: **117 rank-2 curves** (e.g. d=11,15,17,24,26,37,39,43,...; s=0).
- j=1728 (CM by ℤ[i]): y² = x³ + d·x, d ≤ 200: **27 rank-2 curves** (e.g. d=14,33,34,39,46,55,63,65,66,...; s=0).

These satisfy Castella's framework (CM, split ordinary p ≥ 5); Theorem B: κ_p ≠ 0 ⟹ dim Sel = 2 ⟹ Ш[p^∞] finite provably at rank 2.

**Correction (2026-09-15, verified with primary sources):** The top Track B candidate j1728_d68 (y²=x³+68x, N=9248, LMFDB 9248g2) has j=1728 and is **2-isogenous to y²=x³−17x (9248g1), which is CLS curve E₂ (D=17)** — identical a_p at all good primes. **Coates–Liang–Sujatha Theorem 1.3 (arXiv:1005.4206) already proves Ш(E₂/ℚ)[p^∞] = 0 at every good split prime p ≡ 1 (mod 4), p < 30,000, with exception set exactly {(E₁,29), (E₁,277), (E₄,577), (E₅,17)} — (E₂, 5) is NOT in it, so Ш[5^∞] = 0 for the d68 isogeny class is proven, unconditionally (Rubin's main conjecture for ℚ(i)).** Banwait (arXiv:2609.08431, Sep 2026) additionally settles the four CLS-inconclusive pairs with a cyclotomic unit-condition criterion (Prop. 7.4/7.2), with a Lean 4 formalisation of the first equivalence.

**Hard consequence for the program:** d68 at p=5 is **NOT an open case** — the flagship Track B target has already been settled by the literature. What remains genuinely open at rank 2 is NOT per-prime Ш-finiteness for CM curves in these five classes (fully covered below 30,000), and NOT Ш[p]=0 p-by-p for non-CM curves (Stein–Wuthrich cover 1,534,422 pairs + 389a), but: (a) the horizontal statement Ш[p]=0 for all p > M — open for every rank-2 curve ℚ; (b) the j=0 (ℤ[ζ₃]) CM family, which is NOT covered by CLS/Banwait (their family is x³−D·x, CM by ℤ[i]); (c) genuine vertical cases at anomalous primes in classes NOT covered by the CLS five; (d) the exact 2-primary structure of Ш (twist example still open, see §3).

## 3. The d=2 twist: Kolyvagin upgrade to a proven structure (input to N1)

E^(2) = 194040.cu1 twisted by D=2: `[0,0,0,-1825528908,-30021416896912]`, conductor 1552320.

Direct PARI verification:
- `lfun(E,1) = 2.95639422788402` (nonzero), root number +1 ⟹ **analytic rank 0**.
- `ellrank = [0,2,2]`, torsion ℤ/2, C = T + r₂ + s = 1 + 2 + 2 = 5.
- Kolyvagin (L(1) ≠ 0 ⟹ rk = 0 and Ш finite, unconditionally): R = 0 ⟹ S = dim Ш[2] = C − T − R = 4, dim(2Ш[4]) = r₂ − R = 2.
- **CORRECTION (2026-09-15, per Mr. Genius + verified):** The exact statement "Ш[2^∞] ≅ (ℤ/2)²×(ℤ/4)², |Ш[2^∞]|=64 — proven, not conjectural" is **NOT established**. Kolyvagin's theorem gives finiteness of Ш and the cohomological dimensions only; the numerical BSD ratio L(1)/ellbsd = 64.0 is consistent with |Ш[2^∞]| = 2⁶ but allows (ℤ/2)² × (ℤ/2^a)² for any a ≥ 2. Proving the exact 2-primary structure requires additional descent arithmetic (4-descent/8-descent), not just finiteness. Status: rk E^(2)(ℚ) = 0 and Ш finite — proven; analytic ratio 64 — numerical; exact order 64 — open.

This remains the first fully-worked 2-descent/twist instance in the program, and the N1 4-descent experiment (making the lifting classes explicit) is the honest way to try to pin the exact structure.

## 4. Method notes

- PARI `ellinit` discriminant is component **11** (index 12 is j, index 13 roots) — earlier code grabbing `E[12]` read j.
- `lfunrootres` output [L, r, w]: component 0 is the residue computation and can read 0 even when L(E,1) ≠ 0; use `lfun(E, 1.0)` directly for the value.
- Negative-dimension bug in Track D (S = r₂ + s − R, not r₂ − R) is fixed per Mr. Genius; verified on the base curve: S = 2, d = 0.
- E3 twist-stability: v2 JSON (`quadratic_twist_sha_stability_v2.json`) with corrected C = r₂ + T + s reports "structurally_stable": 60 twists, 5 certified rank-2 (4× Ш[2]≅(ℤ/2)², 1× trivial), 28 unresolved. The v1 "unstable" artifact was written by the flawed script (C = r₁ + T + s); superseded.

---

## Priority (my recommendation, thread of 2026-09-15)

1. **Track A** — finish the 194040.cu1 Kato finiteness certificate (chain: Kato cotorsion → Mazur control → torsion-module algebra → Kato divisibility → numerical bound), with the big-image verified here. Milestone: first rank-2 curve with proven-finite Ш outside a small explicit set.
2. **Track B** — Castella κ_p computation on the 144 CM rank-2 curves; first proven κ_p ≠ 0 at rank 2.
3. **N1** — 4-descent on the d=2 twist to make the proven (ℤ/4)² classes explicit.

All three bounded; each has a discriminating falsifier; park any that stagnates after two rounds.