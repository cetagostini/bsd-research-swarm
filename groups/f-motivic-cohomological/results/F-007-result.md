# F-007: Motivic L-Functions and Their Special Values

## Direction ID
F-007

## Title
Motivic L-Functions and Their Special Values

## Status Assessment
The framework is well-developed conjecturally. Deligne (1979) proved the critical values conjecture. Beilinson's conjecture for non-critical values is proved in many cases for modular forms. The full motivic t-structure remains one of the deepest open problems. The Langlands program in its motivic incarnation predicts automorphic L-functions are motivic.

## Testable Conjecture or Lemma

**Conjecture (Bloch–Beilinson).** Let M be a pure motive over ℚ of weight w. For any integer n:

1. **Order of vanishing:**
   ```
   ord_{s=n} L(M,s) = dim H^0(ℚ, M^*(n)) - dim H¹_M(ℚ, M^*(n)) + rank(reg_D)
   ```
   where H¹_M is motivic cohomology and reg_D is the regulator to Deligne cohomology.

2. **Leading coefficient:**
   ```
   L^{(r)}(M,n) / Ω(M,n) ∈ ℚ^×
   ```
   where Ω(M,n) is a product of periods computed from the Hodge filtration.

**Theorem (Deligne, critical values).** For M and n "critical" (where L(M,s) can be normalized by periods):
```
L(M,n) / Ω(M,n) ∈ ℚ^×
```

## Approach Summary
1. **Triangulated category of motives DM(k)**: Voevodsky's derived category of Nisnevich sheaves with transfers, ℚ-coefficients.
2. **Motivic t-structure**: The conjectural t-structure whose heart is the category of mixed motives MM.
3. **L-functions via ℓ-adic realization**: For each ℓ, the ℓ-adic cohomology gives a Galois representation; the L-function is the Euler product of local factors.
4. **Regulator maps**: Motivic → Deligne (Beilinson), motivic → étale (Soulé), motivic → absolute Hodge (Deligne).
5. **Artin formalism**: Products, twists, symmetric powers of motives and their L-functions.

## Computational Example

**Motive M = ℚ(0)** (trivial motive):
- L(ℚ(0), s) = ζ(s), the Riemann zeta function.
- Critical values: ζ(2k) = (-1)^{k+1} B_{2k} (2π)^{2k} / (2(2k)!) for k ≥ 1.
- Non-critical: ζ(0) = -1/2, ζ(-k) = -B_{k+1}/(k+1) for k ≥ 1.

**Motive M = h¹(E) for E = 11a1**:
- L(h¹(E), s) = L(E, s), the L-function of E.
- Critical point: n = 1 (the central point for weight 0 motive h¹(E)).
- L(E,1)/Ω_E = 1/5 ∈ ℚ^×, confirming Deligne's conjecture for the "critical" normalization.

**Motive M = h²(S) for S a K3 surface**:
- L(h²(S), s) involves the transcendental lattice.
- Critical point: n = 2.
- Partial results by van Geemen, Top via explicit computation of the Picard lattice and transcendental lattice.

## Obstacle Analysis
1. **Motivic t-structure**: The existence of a t-structure on DM whose heart is the category of mixed motives is the fundamental open problem. Without it, "the motive of X" is not a well-defined object.
2. **Standard conjectures**: The standard conjectures (Lefschetz, Hodge) are needed to make the category of pure motives abelian semisimple.
3. **Non-critical values**: For n outside the critical range, the Beilinson conjecture requires the regulator, which is harder to compute and verify.
4. **Beyond GL₂**: For automorphic representations of GL_n with n ≥ 3, the motivic interpretation of their L-functions is largely conjectural.

## Cross-Group Connections
- **F-003 (Bloch–Kato)**: The Bloch–Kato conjecture is the "special values" part of the motivic framework.
- **F-008 (Deligne cohomology)**: The target of the regulator map is Deligne cohomology.
- **F-011 (Deninger)**: Deninger's program seeks the cohomological realization of motivic L-functions.
- **F-012 (Soulé)**: The Soulé regulator maps K-theory to étale cohomology, the ℓ-adic side of the motivic picture.

## Classification
Structural framework — foundational. The motivic perspective is the "correct" framework in which BSD is a special case.
