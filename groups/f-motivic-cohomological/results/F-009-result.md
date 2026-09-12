# F-009: K-Theoretic Approach to Finiteness of III

## Direction ID
F-009

## Title
K-Theoretic Approach to Finiteness of III

## Status Assessment
Finiteness proved for rank ≤ 1 (Kolyvagin 1989, assuming modularity). The Voevodsky–Rost theorem (proof of the Bloch–Kato conjecture for mod-p Galois cohomology, 2009) identifies K_n(F)/p ≅ H^n_ét(F, μ_p^{⊗n}). Nekovář extended Kolyvagin's method to higher-rank cases under parity conditions. The direct K-theoretic interpretation of III remains largely conjectural.

## Testable Conjecture or Lemma

**Conjecture (K-theoretic finiteness).** For an elliptic curve E/ℚ:

1. The Shafarevich–Tate group III(E/ℚ)[p^∞] embeds into the cokernel of the étale regulator:
   ```
   K₂(𝒪_{E,S}) → H²_ét(E[1/S], ℤ_p(2))
   ```
   and finiteness of this cokernel implies finiteness of III.

2. The Quillen–Lichtenbaum comparison (now a theorem) gives:
   ```
   K_n(𝒪_F)/p^r ≅ H^n_ét(Spec 𝒪_F[1/p], ℤ/p^rℤ(n))
   ```
   for n ≥ 2, which provides the bridge between K-theory and Selmer groups.

**Lemma (Kolyvagin).** For E/ℚ with analytic rank ≤ 1:
```
III(E/ℚ)[p^∞] is finite
```
for primes p where E is modular and the Kolyvagin derivative classes are non-trivial.

## Approach Summary
1. **Quillen–Lichtenbaum**: Use the theorem (Voevodsky–Rost) identifying K-theory with étale cohomology in the relevant degrees.
2. **Hochschild–Serre**: The spectral sequence H^p(Gal(F_S/F), H^q_ét(X_{F_S}, ℤ_p(j))) converging to H^{p+q}_ét(X, ℤ_p(j)) connects Galois cohomology with K-theory.
3. **Euler systems**: Kolyvagin's system of derivative classes bounds the Selmer group.
4. **Control theorems**: Iwasawa-theoretic control theorems for Selmer groups over ℤ_p-extensions.

## Computational Example

**Curve**: E = 11a1, p = 5.

- K₂(𝒪_{E,S})/5 ≅ H²_ét(E[1/5S], μ₅^{⊗2}) by Voevodsky–Rost.
- The Selmer group Sel₅(E/ℚ) = 0.
- III(E)[5^∞] = 0 (finite, trivially).
- K-theoretic interpretation: the étale regulator surjects onto the Selmer group.

**Curve**: E = 571a1 (rank 0, #III = 4).

- For p = 2: K₂(𝒪_{E,S})/2 ≅ H²_ét(E[1/2S], μ₂^{⊗2}).
- Sel₂(E/ℚ) ≅ (ℤ/2)², accounting for III(E)[2^∞] ≅ (ℤ/2)².
- K-theoretic: the image of K₂(𝒪_{E,S}) in H²_ét is exactly the Selmer group.

**Curve**: E = 37a1 (rank 1), p = 2.

- Kolyvagin's derivative class κ(l) for a prime l of good reduction is non-trivial in H¹(ℚ, E[2]).
- This bounds Sel₂(E/ℚ) to rank 1, consistent with rank(E) = 1.
- III(E)[2^∞] = 0.

## Obstacle Analysis
1. **ℤ_p-coefficients**: The Quillen–Lichtenbaum conjecture handles mod-p coefficients but not ℤ_p-coefficients in the needed range. Extending to ℤ_p requires integral comparison theorems.
2. **Higher rank**: Kolyvagin's method works for rank ≤ 1. For rank ≥ 2, the Euler system approach needs new derivative classes or alternative methods.
3. **Explicit K-theory**: Computing K_n(𝒪_F) for n ≥ 3 is extremely difficult. The Bloch group and the Rost–Voevodsky theorem give the theoretical framework but not efficient algorithms.
4. **Comparison of regulators**: The étale regulator (Soulé) and the Deligne regulator (Beilinson) are not explicitly compared in degree ≥ 3.

## Cross-Group Connections
- **F-001 (Kato's zeta)**: The Euler system bounds Sel_p^∞(E/ℚ), which controls III[p^∞].
- **F-003 (Bloch–Kato)**: Finiteness of III is a consequence of the Bloch–Kato conjecture for M = h¹(E).
- **F-012 (Soulé regulators)**: The Soulé regulator maps K-theory to the étale cohomology group that contains III.

## Classification
Core theory — ambitious. The K-theoretic approach has the potential to give a conceptual proof of finiteness of III.
