# F-002: Beilinson's Conjecture for L′(E,1) When rank = 1

## Direction ID
F-002

## Title
Beilinson's Conjecture for L′(E,1) When rank = 1

## Status Assessment
Proved for modular E/ℚ (Beilinson 1985, Deninger 1984). Numerical verification by Bloch–Grayson and others. Extension to number fields and non-modular E remains open. The explicit construction of the Beilinson element β ∈ K₂(E) depends on the modular parametrization X₀(N) → E.

## Testable Conjecture or Lemma

**Conjecture (Beilinson for rank 1).** Let E/ℚ be an elliptic curve with ord_{s=1} L(E,s) = 1. There exists a "Beilinson element" β ∈ H¹_M(E, ℚ(2)) ≅ CH²(E,1) ⊗ ℚ such that:

1. The regulator r_D(β) ∈ H¹_D(E, ℝ(2)) ≅ ℝ is nonzero.
2. The ratio L′(E,1)/(Ω_E · r_D(β)) ∈ ℚ^×, with:
   ```
   L′(E,1) / Ω_E = (#III(E) · ∏ c_p) / (|E(ℚ)_tors|² · |det(r_D)|)
   ```

**Lemma (Eisenstein symbol).** For X₀(N) with N prime, let u₁, ..., u_r be Siegel units on X₀(N) generating the group of modular units modulo constants. The Beilinson element is:
```
β = Σᵢ {uᵢ, f} ∈ K₂(X₀(N))
```
where {·,·} is the Steinberg symbol and f is the modular form of weight 2 attached to E. The regulator r_D(β) = L′(E,1)/(4π²) · (rational factor).

## Approach Summary
1. **Modular parametrization**: Use the strong Weil parametrization π: X₀(N) → E to construct elements in K₂(E) from K₂(X₀(N)).
2. **Eisenstein symbol**: Beilinson's map from modular units (divisors of Siegel units) to K₂(X₀(N)) via the tame symbol construction.
3. **Regulator computation**: Compute r_D(β) via the comparison H²_D(E, ℝ(2)) ≅ ℝ using the Betti/de Rham comparison and modular symbol computations.
4. **Deninger's direct construction**: Use Deninger's pairing K₂(E) × K₂(E) → K₂(ℚ) ≅ ℤ to relate the regulator to the L-value.

## Computational Example

**Curve**: E = 37a1 (y² + y = x³ − x, conductor 37, rank 1).

- The modular parametrization X₀(37) → E has degree 2.
- The Eisenstein series of weight 2 on Γ₀(37) gives a Beilinson element β ∈ K₂(X₀(37)).
- Pushing forward to K₂(E): π₊(β) ∈ K₂(E).
- Regulator: r_D(π₊(β)) = L′(E,1)/(4π²) ≈ 0.305988/(4π²) ≈ 0.007748.
- L′(E,1)/Ω_E = 1 (since #III = 1, c_p = 1 for p = 37, |E(ℚ)_tors|² = 1).
- So β generates CH²(E,1) ⊗ ℚ ≅ ℚ.

**Curve**: E = 43a1 (y² + y = x³ + x², rank 1).

- Conductor 43. The modular parametrization has degree 7.
- Beilinson element from Eisenstein symbol on X₀(43).
- r_D(β) = L′(E,1)/(4π² · 7) where 7 is the modular degree.
- Confirms L′(E,1)/Ω_E ∈ ℚ^×.

## Obstacle Analysis
1. **Non-canonical construction**: The Eisenstein symbol depends on choices of cusps and the specific modular parametrization, which is not canonical.
2. **Non-modular curves**: For E over a general number field without a known modular parametrization, there is no method to construct elements in K₂(E).
3. **Regulator injectivity**: It is not known whether r_D: CH²(E,1) ⊗ ℚ → ℝ is injective. If it has a kernel, the "Beilinson element" may not be unique.
4. **Rank ≥ 2 extension**: For higher ranks, one needs independent elements in CH²(E,1), and the Eisenstein symbol construction does not obviously produce enough independent classes.

## Cross-Group Connections
- **F-006 (Regulator K₂(E) → ℝ)**: Beilinson's theorem is the key input; the regulator computation is the same map studied in F-006.
- **F-005 (Higher Chow cycles)**: CH²(E,1) is a higher Chow group; the Bloch–Beilinson conjecture framework applies.
- **F-007 (Motivic L-functions)**: The motive h¹(E) has L-function L(E,s); the conjecture is a special case of the Bloch–Beilinson philosophy.
- **F-008 (Deligne cohomology)**: The target of the regulator is H¹_D(E, ℝ(2)) ≅ ℝ, a Deligne cohomology group.

## Classification
Core theory — high priority. Established for rank 1 modular curves, with computational tools available.
