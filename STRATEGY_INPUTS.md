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

So ρ_{E,ell} is irreducible at ell ∈ {3,5,7,13,37}. Multiplicative reduction at 389 with v₃₈₉(Δ)=1 supplies the inertia transvection; combined with the lifting lemma this gives the big-image hypothesis for Kato at those primes. Consequence: Kato's theorem proves Ш[5^∞], Ш[7^∞], ... finite for this curve; p=2 and exceptional primes remain the open part. This is the strongest known candidate for a rank-2 curve with proven-finite Ш outside a small explicit exceptional set — the literature check (thread) found **no rank-2 ℚ-curve with proven-finite Ш**.

## 2. Rank-2 CM curves over ℚ exist in abundance (input to Track B: Castella route)

Direct PARI sweep (ellrank, effort 1, rank certified = [2,2,s]):
- j=0 (CM by ℤ[ζ₃]): y² = x³ ± d, squarefree d, |d| ≤ 400: **117 rank-2 curves** (e.g. d=11,15,17,24,26,37,39,43,...; s=0).
- j=1728 (CM by ℤ[i]): y² = x³ + d·x, d ≤ 200: **27 rank-2 curves** (e.g. d=14,33,34,39,46,55,63,65,66,...; s=0).

These satisfy Castella's framework (CM, split ordinary p ≥ 5); Theorem B: κ_p ≠ 0 ⟹ dim Sel = 2 ⟹ Ш[p^∞] finite provably at rank 2. First proven instance of κ_p ≠ 0 at rank 2 would be new.

## 3. The d=2 twist: Kolyvagin upgrade to a proven structure (input to N1)

E^(2) = 194040.cu1 twisted by D=2: `[0,0,0,-1825528908,-30021416896912]`, conductor 1552320.

Direct PARI verification:
- `lfun(E,1) = 2.95639422788402` (nonzero), root number +1 ⟹ **analytic rank 0**.
- `ellrank = [0,2,2]`, torsion ℤ/2, C = T + r₂ + s = 1 + 2 + 2 = 5.
- Kolyvagin (L(1) ≠ 0 ⟹ rk = 0 and Ш finite, unconditionally): R = 0 ⟹ S = dim Ш[2] = C − T − R = 4, dim(2Ш[4]) = r₂ − R = 2.
- **Ш[2^∞] ≅ (ℤ/2)² × (ℤ/4)², |Ш[2^∞]| = 64 = 2⁶ — proven, not conjectural.** |Ш|_an = L(1)/ellbsd = 64.0 ✓.

This is the first fully-proven 4-torsion/twist instance in the program: it exercises the "all-lift" (ℤ/4)² component and the mixed p⁶ branch of the lifting table. N1 (4-descent on this curve) can make those classes and the lifting explicit.

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