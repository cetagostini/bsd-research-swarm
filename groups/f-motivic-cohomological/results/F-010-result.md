# F-010: Arithmetic Chow Groups and Arakelov Theory for BSD

## Direction ID
F-010

## Title
Arithmetic Chow Groups and Arakelov Theory for BSD

## Status Assessment
Partial results for height computations (Gross–Zagier, Zhang). The arithmetic Riemann–Roch theorem (Faltings) and arithmetic Hodge index theorem (Moriwaki, Yuan–Zhang) are established. The full arithmetic Riemann–Roch approach to BSD is an active research program. Faltings' arithmetic Riemann–Roch gives a formula for the arithmetic degree of the determinant of cohomology line bundle.

## Testable Conjecture or Lemma

**Conjecture (Arithmetic Riemann–Roch for BSD).** For a regular model 𝒳 of E over Spec ℤ:

1. The BSD formula can be expressed as an arithmetic Riemann–Roch formula:
   ```
   deg(det RΓ(𝒳, L)) = (arithmetic intersection terms) + (Archimedean periods)
   ```
   where L is a line bundle on 𝒳 related to the modular parametrization.

2. The Néron–Tate height pairing is an arithmetic intersection number:
   ```
   ⟨P, Q⟩_NT = -deg(𝒪_𝒳(P) · 𝒪_𝒳(Q))_Ar
   ```
   where the intersection is computed in the arithmetic Chow group ĈH²(𝒳).

3. The Faltings height h_F(E) satisfies:
   ```
   exp(-h_F(E)) ~ Ω_E / √|Δ_E|
   ```
   relating the Archimedean period to the arithmetic self-intersection.

**Lemma (Arithmetic Hodge Index).** For a surface 𝒳 over Spec ℤ:
```
signature of ⟨·,·⟩_Ar on ĈH¹(𝒳) = (1, ρ(𝒳) - 1)
```
where ρ(𝒳) is the Picard number of the generic fiber.

## Approach Summary
1. **Arithmetic Chow groups**: ĈH^p(𝒳) = pairs (Z, g) where Z is a codimension-p cycle and g is a Green current, modulo rational equivalences.
2. **Arithmetic intersection**: The pairing ĈH^p × ĈH^{d+1-p} → ℝ combining finite intersections with Archimedean integrals ∫ g₁ ∧ dd^c g₂.
3. **Arithmetic Chern character**: ĉh: K̂₀(𝒳) → ⊕_p ĈH^p(𝒳) ⊗ ℚ.
4. **Faltings' arithmetic Riemann–Roch**: Formula for deg(det RΓ(𝒳, L)) in terms of arithmetic Chern numbers.

## Computational Example

**Curve**: E = 11a1 with regular model 𝒳 → Spec ℤ.

- The Néron model has good reduction at all primes except 2, 3, 5, 7, 11.
- Faltings height: h_F(E) = -log(Ω_E · √|Δ_E|) up to explicit constants.
- For 11a1: Ω_E ≈ 1.269209, Δ_E = -11, so h_F(E) ≈ log(√11/1.269209) ≈ 0.33...
- Arithmetic self-intersection of the zero section: ⟨O, O⟩_Ar = -h_F(E).
- Tamagawa factors c₂ = 1, c₃ = 1 correspond to intersection multiplicities of the special fiber.

**Curve**: E = 37a1 (rank 1).

- The section P = (0,0) of infinite order has arithmetic self-intersection:
  ⟨P, P⟩_Ar = -⟨P, P⟩_NT + (local correction terms at bad primes).
- The regulator Reg(E) = ⟨P, P⟩_NT = det of the arithmetic intersection matrix on the rank-1 lattice.

## Obstacle Analysis
1. **Higher-dimensional models**: For surfaces and higher-dimensional varieties, the arithmetic Chow group ĈH² is not well understood.
2. **Archimedean contribution**: The Green current computation involves transcendental data (Faltings height, Petersson inner product) that cannot be captured algebraically.
3. **Disentangling the formula**: The BSD formula involves both arithmetic (finite) and transcendental (Archimedean) parts; the Arakelov framework unifies them but doesn't separately prove each part.
4. **Global-to-local**: The Tamagawa factors c_p are local intersection numbers, but computing them requires detailed knowledge of the special fiber of the Néron model.

## Cross-Group Connections
- **F-008 (Deligne cohomology)**: The Archimedean part of the arithmetic intersection is computed in Deligne cohomology.
- **F-011 (Deninger)**: In Deninger's framework, the Archimedean periods would come from the "infinite place" contribution to the regularized determinant.
- **F-001 (Kato's zeta)**: The Tamagawa factors in Kato's theorem are the same local intersection numbers.
- **F-005 (Higher Chow cycles)**: The arithmetic Chow group is the "compactified" version of the Chow group.

## Classification
Advanced technique — high potential. Arakelov theory provides a unified geometric framework for all terms of BSD.
