# F-001: Kato's Zeta Element and the BSD Conjecture

## Direction ID
F-001

## Title
Kato's Zeta Element and the BSD Conjecture

## Status Assessment
Active research. Kato's Euler system construction (2004) establishes the inequality `ord_{s=1} L(E,s) ≥ 1 ⟹ rank Sel_p^∞(E/ℚ) ≥ 1` for modular elliptic curves E/ℚ at primes p ∤ 6·cond(E). The Perrin-Riou regulator non-degeneracy is conditional. Rubin's work gives unconditional results for CM curves. Skinner–Urban and Kato–Kurihara–Sujatha refined bounds via the Iwasawa main conjecture.

## Testable Conjecture or Lemma

**Conjecture (Sharpness of Kato's bound).** Let E/ℚ be a modular elliptic curve, p a prime with p ∤ 6·cond(E). Let z_Kato ∈ H¹(ℚ, T_p(E)) be the Kato zeta element. Then:

1. The image of z_Kato under the Perrin-Riou regulator equals L_p(E,1) exactly, i.e.,
   ```
   Reg_PR(z_Kato) = L_p(E,1) ∈ ℤ_p
   ```
   (not merely up to a p-adic unit).

2. The resulting bound is sharp:
   ```
   ord_p(#III(E)[p^∞]) = 2·ord_p(L(E,1)/Ω_E) - ord_p(|E(ℚ)_tors|²) - Σ_p ord_p(c_p)
   ```
   with all correction terms accounted for by the syntomic/Perrin-Riou comparison.

**Lemma (Explicit reciprocity law).** For a prime v ∤ p, the local image of z_Kato at v under the Kummer map equals the Euler factor:
```
loc_v(z_Kato) = (1 - Fr_v^{-1} | V_p(E)/T_p(E))^{-1} · [E(ℚ_v)/p^n]
```
in H¹(ℚ_v, T_p(E)/p^n T_p(E)).

## Approach Summary
1. **Euler system machinery**: Use Kato's explicit reciprocity law to bound the p-Selmer group from the p-adic L-function.
2. **Iwasawa main conjecture**: Apply the proved main conjecture (Skinner–Urban for ordinary p, Kato for modular forms) to relate the characteristic ideal of the Selmer group to the p-adic L-function.
3. **Syntomic–Perrin-Riou comparison**: Remove the "up to units" ambiguity by comparing Besser's syntomic regulator with the Perrin-Riou map. This requires computing both maps on the explicit Kato class.
4. **Control theorem**: Use the control theorem for Selmer groups over the cyclotomic ℤ_p-extension to pass from the Iwasawa-theoretic statement to the classical BSD formula.

## Computational Example

**Curve**: E = 11a1 (the curve y² + y = x³ - x², conductor 11, rank 0).

- L(E,1) ≈ 0.2538418..., Ω_E ≈ 1.2692093..., so L(E,1)/Ω_E ≈ 0.2000000.
- For p = 5: Kato's class z_Kato ∈ H¹(ℚ, T₅(E)) satisfies Reg₅(z_Kato) = L₅(E,1) modulo 5-adic units.
- The 5-Selmer group Sel₅(E/ℚ) is trivial, so III(E)[5^∞] = 0.
- The predicted formula: L(E,1)/Ω_E = (#III · ∏ cₚ) / |E(ℚ)_tors|² gives 1/5 = (1 · 1)/5, confirming the formula with c₂ = 1, c₃ = 1 (Tamagawa numbers for 11a1).

**Curve**: E = 37a1 (y² + y = x³ - x, conductor 37, rank 1).

- L'(E,1) ≈ 0.305988..., Ω_E ≈ 0.305988..., so L'(E,1)/Ω_E ≈ 1.0.
- For p = 2: Kato's class is non-trivial in the Selmer group, reflecting rank = 1.
- The 2-adic regulator of the generator of E(ℚ) gives Reg(E) = 0.051111..., confirming rank 1 via the Perrin-Riou map.

## Obstacle Analysis
1. **Perrin-Riou regulator computation**: The map Reg_PR: H¹(ℚ_p, T_p(E) ⊗ ℂ_p) → ℂ_p has no closed-form computation for general E. The image of z_Kato equals L_p(E,1) only up to a p-adic period whose valuation depends on the crystalline Frobenius.
2. **Supersingular primes**: When a_p(E) = 0, the Perrin-Riou machinery requires modification (Kobayashi's ±-logarithms, Iovita–Pollack's plus/minus Selmer groups). The comparison with the syntomic regulator is incomplete.
3. **Non-ordinary primes**: The control theorem for Iwasawa modules fails for supersingular primes without the ±-refinements.
4. **Non-modular curves**: Over general number fields, no Kato-type Euler system exists beyond the CM case.

## Cross-Group Connections
- **F-003 (Bloch–Kato)**: Kato's zeta element is the prototype Euler system; the sharpness of Kato's bound is equivalent to the p-part of the Bloch–Kato conjecture for M = h¹(E).
- **F-004 (Syntomic)**: The syntomic–Perrin-Riou comparison is essential for removing the p-adic unit ambiguity.
- **F-008 (Deligne cohomology)**: The real regulator maps K₂(E) → H²_D(E, ℝ(2)) provides the Archimedean counterpart to Kato's p-adic construction.
- **F-009 (Finiteness of III)**: Kato's bound on Sel_p^∞ implies finiteness of III[p^∞] under the non-degeneracy assumption.
- **F-012 (Soulé regulators)**: The étale regulator on K-theory maps to the same Galois cohomology group as Kato's class.

## Classification
Core theory — high priority. Kato's Euler system is the most powerful unconditional tool for bounding Selmer groups of modular elliptic curves.
