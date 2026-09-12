# F-012: Soulé Regulators and Computational Motivic Cohomology

## Direction ID
F-012

## Title
Soulé Regulators and Computational Motivic Cohomology

## Status Assessment
Active computational research. K₁(𝒪_F) = 𝒪_F^× (units), Soulé regulator = p-adic logarithm. K₂(𝒪_F) computations well-developed via the Galois symbol (Merkurjev–Suslin theorem). K₃(𝒪_F) related to the Bloch group ℬ(F); computations exist for specific fields (Gangl, Zagier, Goncharov). The Rost–Voevodsky theorem (2009) generalizes Merkurjev–Suslin to all n. The comparison between Soulé and Beilinson regulators is open for n ≥ 3.

## Testable Conjecture or Lemma

**Conjecture (Soulé regulator image).** For a number field F and a prime p:

1. The Soulé regulator on K₂:
   ```
   reg_ét: K₂(𝒪_F) → H²_ét(Spec 𝒪_F[1/S], ℤ_p(2))
   ```
   has image equal to the "integral" part of the Bloch–Kato Selmer group.

2. For K₃, the Soulé regulator factors through the Bloch group:
   ```
   K₃(𝒪_F) → ℬ(F) → H³_ét(Spec 𝒪_F[1/S], ℤ_p(3))
   ```
   and the image is related to the special value ζ_F(3).

3. **Soulé–Beilinson comparison**: For n = 2, the diagram commutes:
   ```
   K₂(𝒪_F) --reg_ét--> H²_ét(𝒪_F[1/S], ℤ_p(2))
     |                      |
     reg_D                  comparison
     |                      |
     v                      v
   H²_D(Spec F, ℝ(2)) --p-adic--> H²_ét(𝒪_F[1/S], ℂ_p(2))
   ```

**Theorem (Merkurjev–Suslin, 1982).** For a field F and n > 0:
```
K₂(F)/n ≅ H²_ét(F, μ_n^{⊗2})
```
via the Galois symbol. This gives an explicit formula for the mod-n Soulé regulator on K₂.

**Theorem (Rost–Voevodsky, 2009).** For all m > 0 and all n ≥ 1:
```
K_n(F)/m ≅ H^n_ét(F, μ_m^{⊗n})
```
(the Bloch–Kato conjecture, proved).

## Approach Summary
1. **Galois symbol**: The map K_n(F)/m → H^n_ét(F, μ_m^{⊗n}) is the mod-m Soulé regulator, made explicit by the Rost–Voevodsky theorem.
2. **Steinberg symbols**: For K₂, the Soulé regulator is computed on {a,b} ∈ K₂(F) via the cup product in Galois cohomology.
3. **Bloch group**: For K₃, the regulator factors through the Bloch group ℬ(F), which has explicit presentations.
4. **p-adic comparison**: Relate the Soulé (étale) regulator to the Beilinson (Deligne) regulator via p-adic comparison theorems.
5. **Computational K-theory**: Use algorithms for computing K_n(𝒪_F) for small n and specific F.

## Computational Example

**F = ℚ, K₁(𝒪_ℚ) = ℤ^× = {±1}:**
- Soulé regulator: reg_ét(−1) = p-adic logarithm of −1 = 0 (since −1 ∈ ℤ_p^× has log_p(−1) = 0 for odd p).
- This is consistent with ζ(1) having a pole (not a "special value" in the usual sense).

**F = ℚ, K₂(ℤ) ≅ ℤ/2 (by Tate's computation):**
- The Galois symbol K₂(ℤ)/2 ≅ H²_ét(Spec ℤ[1/2], μ₂^{⊗2}) ≅ ℤ/2.
- The non-trivial class {−1, −1} maps to the quaternion algebra (−1,−1) over ℚ.
- The Soulé regulator on K₂(ℤ) gives a torsion class, consistent with ζ(2) = π²/6 being non-zero.

**F = ℚ(i), K₃(𝒪_F) computation:**
- The Bloch group ℬ(ℚ(i)) has been computed by Gangl–Zagier.
- K₃(𝒪_{ℚ(i)}) ≅ ℤ ⊕ (finite torsion).
- The Soulé regulator on the infinite part gives a value related to ζ_{ℚ(i)}(3) ≈ 1.0795...
- The Beilinson regulator gives the same value up to periods and rational factors.

**F = ℚ(√5), K₂(𝒪_F):**
- K₂(ℤ[√5]) has been computed via the tame symbol and the Birch–Tate conjecture.
- The Birch–Tate conjecture (now a theorem for abelian fields) gives |K₂(𝒪_F)| = |w₂(F)| · |ζ_F(−1)| where w₂(F) is the largest integer m such that Gal(F(μ_m)/F) has exponent 2.

## Obstacle Analysis
1. **Degree ≥ 3**: K₃ and higher K-groups are very large and difficult to compute. The Bloch group ℬ(F) gives a finite presentation of K₃(𝒪_F)/torsion, but computing its rank and the regulator is hard.
2. **Comparison of regulators**: The diagram relating Soulé (étale) and Beilinson (Deligne) regulators is known to commute for K₁ and K₂, but the comparison in degree ≥ 3 requires p-adic Hodge theory that is not fully developed.
3. **Integral structure**: The Soulé regulator maps to ℤ_p-coefficients, while the Beilinson regulator maps to ℝ. The comparison involves p-adic periods whose valuations are not well understood.
4. **Explicit formulas**: For K₃, the Soulé regulator should involve the trilogarithm, but the explicit formula in terms of Galois cohomology cocycles is not fully worked out.

## Cross-Group Connections
- **F-001 (Kato's zeta)**: The Soulé regulator on K-theory maps to the same Galois cohomology groups as Kato's Euler system class.
- **F-004 (Syntomic)**: The syntomic regulator (p-adic side) and the Soulé regulator (étale side) are related by p-adic comparison theorems.
- **F-006 (K₂(E) regulator)**: The Beilinson regulator on K₂(E) has the Soulé regulator as its ℓ-adic counterpart.
- **F-009 (Finiteness of III)**: The Quillen–Lichtenbaum theorem (Voevodsky–Rost) identifies K-theory mod p with étale cohomology, providing the bridge for the K-theoretic approach to finiteness of III.
- **F-003 (Bloch–Kato)**: The Rost–Voevodsky theorem is the proof of the Bloch–Kato conjecture for mod-m Galois cohomology.

## Classification
Computational — tools and verification. The Soulé regulator provides the étale side of the BSD picture, essential for numerical verification.
