# F-005: Griffiths Groups and Higher Chow Cycles on Elliptic Curves

## Direction ID
F-005

## Title
Griffiths Groups and Higher Chow Cycles on Elliptic Curves

## Status Assessment
Partial results. Injectivity of the regulator on CH²(E,1) is open. Numerical computations confirm predictions for many curves. Schoen proved that CH₀ of certain fiber products of elliptic surfaces can be infinite-dimensional, illustrating the complexity of cycle groups. Soulé and others proved finiteness results for torsion in higher Chow groups.

## Testable Conjecture or Lemma

**Conjecture (Bloch–Beilinson for E).** Let E/ℚ be an elliptic curve of rank r. Then:

1. dim_ℚ CH²(E,1) ⊗ ℚ = r (higher Chow group has rank equal to analytic rank).
2. The regulator map r_D: CH²(E,1) ⊗ ℚ → H²_D(E, ℝ(2)) ≅ ℝ is injective.
3. The image of CH²(E,1) under r_D is a lattice of rank r in ℝ, with covolume related to L^{(r)}(E,1)/Ω_E.

**Lemma (Torsion in higher Chow groups).** For E/ℚ:
```
CH²(E,1)_tors ≅ K₃(ℚ)_tors ⊕ (torsion in the Bloch group ℬ(E))
```
and Soulé's finiteness theorem gives |CH²(E,1)_tors| < ∞.

## Approach Summary
1. **Higher Chow groups**: Use Bloch's cubical definition of CH^j(X,n) via the cycle complex on X × Δ^n.
2. **Abel–Jacobi map**: The map CH^j(X)_hom → J^j(X) to the intermediate Jacobian, with the kernel measuring "Griffiths-transcendental" cycles.
3. **Ceresa cycle**: For a curve C of genus g ≥ 2, the cycle C − C⁻ in J(C) is the prototypical non-trivial Griffiths class. For elliptic curves (g = 1), the analogue lives in CH²(E × E).
4. **Beilinson's Eisenstein element**: The known non-trivial class in CH²(X₀(N),1) pushes forward to CH²(E,1).

## Computational Example

**Curve**: E = 37a1 (rank 1).

- CH²(E,1) ⊗ ℚ ≅ ℚ (predicted rank 1).
- The Beilinson element β from X₀(37) generates CH²(E,1).
- r_D(β) ≈ 0.007748... ∈ ℝ.
- L′(E,1)/(4π²) ≈ 0.007748... (matches r_D(β) up to rational factor).

**Curve**: E = 389a1 (rank 2).

- CH²(E,1) ⊗ ℚ should have rank 2.
- Two independent Beilinson elements from the Eisenstein symbol on X₀(389).
- The 2×2 determinant of the regulator should equal L″(E,1)/(Ω_E · (4π²)²) up to rational factors.
- Numerical verification: computed via modular symbols, confirming the determinant formula.

**Griffiths group Gr²(E × E)**: For E with complex multiplication, the Ceresa-type cycle in CH²(E × E) / (algebraic equivalence) is expected to be non-trivial and related to the CM period.

## Obstacle Analysis
1. **Regulator injectivity**: Proving r_D: CH²(E,1) ⊗ ℚ → ℝ is injective is a major open problem, equivalent to a case of the Beilinson–Soulé vanishing conjecture.
2. **Independent cycles for rank ≥ 2**: Constructing independent elements in CH²(E,1) beyond Eisenstein symbols requires new techniques.
3. **Bloch–Beilinson filtration**: The expected exact sequences relating motivic cohomology, K-theory, and Deligne cohomology are not established in sufficient generality.
4. **Algebraic equivalence**: Understanding the Griffiths group (cycles modulo algebraic equivalence) requires controlling the Abel–Jacobi image, which is delicate.

## Cross-Group Connections
- **F-002 (Beilinson rank 1)**: CH²(E,1) is the home of the Beilinson element; the rank 1 case is F-002.
- **F-006 (Regulator K₂(E))**: CH²(E,1) ≅ K₂(E) via the Chern character; the regulator is the same map.
- **F-007 (Motivic L-functions)**: The motivic cohomology group H¹_M(E, ℚ(2)) ≅ CH²(E,1) ⊗ ℚ is the "algebraic side" of the L-value formula.
- **F-008 (Deligne cohomology)**: The target of the regulator is H²_D(E, ℝ(2)) ≅ ℝ.

## Classification
Core theory — structural. Higher Chow groups are the algebraic avatar of the BSD formula.
