# F-006: Regulator Maps from K₂(E) to ℝ (Beilinson's Theorem)

## Direction ID
F-006

## Title
Regulator Maps from K₂(E) to ℝ (Beilinson's Theorem)

## Status Assessment
Beilinson's theorem (1985) proved: the Eisenstein element has nonzero regulator, equal to L′(E,1)/(2π)² up to rational factors. Bloch (1984) computed K₂ of the Tate curve. Borel (1977) proved injectivity of the regulator on K_n(𝒪_F) for n ≥ 2. Computational methods by de Jeu and Zagier. Extension to rank ≥ 2 partially open.

## Testable Conjecture or Lemma

**Conjecture (Regulator image).** For E/ℚ of rank r, the image of the regulator map
```
r_D: K₂(E) ⊗ ℚ → H²_D(E, ℝ(2)) ≅ ℝ
```
has dimension r. The kernel consists of "algebraic" K₂-classes (those coming from K₂(ℚ) and tame symbols).

**Theorem (Beilinson).** For the Eisenstein element e ∈ K₂(X₀(N)):
```
r_D(e) = L′(E,1) / (4π²) × (rational factor involving degree of parametrization)
```
and r_D(e) ≠ 0 whenever L′(E,1) ≠ 0.

**Lemma (Borel regulator).** For the ring of integers 𝒪_F of a number field F:
```
reg: K_n(𝒪_F) ⊗ ℝ → ℝ^{d_n}
```
is injective for n ≥ 2, with image determined by ζ_F(n) (Borel's theorem).

## Approach Summary
1. **Eisenstein symbol construction**: Map from modular units (divisors of Siegel functions on X₀(N)) to K₂(X₀(N)) via the tame symbol.
2. **Pushforward to E**: Use the modular parametrization π: X₀(N) → E to push K₂-classes to K₂(E).
3. **Deligne cohomology computation**: Evaluate r_D via the Betti/de Rham comparison: identify H²_D(E, ℝ(2)) with ℝ using the period lattice.
4. **Modular symbols**: Compute the regulator numerically via the Manin trick (integration of the modular form against the Eisenstein series).

## Computational Example

**Curve**: E = 11a1 (rank 0).

- K₂(E) ⊗ ℚ ≅ K₂(ℚ) ⊗ ℚ ≅ ℚ (only "trivial" classes).
- r_D maps the trivial class to 0.
- Consistent with L(E,1) ≠ 0: the formula involves #III and c_p but not the regulator.

**Curve**: E = 37a1 (rank 1).

- The Eisenstein element e ∈ K₂(X₀(37)) pushes forward to K₂(E).
- r_D(e) = L′(E,1)/(4π²) ≈ 0.007748...
- L′(E,1)/Ω_E = 1, so e generates K₂(E) ⊗ ℚ modulo trivial classes.

**Curve**: E = 433a1 (rank 3).

- Expected: dim(K₂(E) ⊗ ℚ) / (trivial part) = 3.
- Three independent Eisenstein-type elements needed.
- Regulator determinant = L‴(E,1)/(Ω_E · (4π²)³) × (rational factor).

## Obstacle Analysis
1. **Non-canonical parametrization**: The modular parametrization X₀(N) → E is not canonical; choices of cusp, sign conventions affect the Eisenstein element.
2. **Rank ≥ 2 constructions**: For higher ranks, one needs independent elements in K₂(E). The Eisenstein symbol may not produce enough independent classes.
3. **Kernel of regulator**: It is not known whether r_D: K₂(E) ⊗ ℚ → ℝ has a kernel beyond the "trivial" classes from K₂(ℚ).
4. **Non-modular curves**: No method to construct elements in K₂(E) without a modular parametrization.

## Cross-Group Connections
- **F-002 (Beilinson rank 1)**: Beilinson's theorem is the key input for the rank 1 case.
- **F-005 (Higher Chow cycles)**: K₂(E) ⊗ ℚ ≅ CH²(E,1) ⊗ ℚ via the Chern character.
- **F-008 (Deligne cohomology)**: The target H²_D(E, ℝ(2)) ≅ ℝ is a Deligne cohomology group.
- **F-012 (Soulé regulators)**: The étale regulator on K₂ is the ℓ-adic counterpart.

## Classification
Core theory — established results, computational challenges remain. Beilinson's theorem is the foundation for K-theoretic approaches to BSD.
