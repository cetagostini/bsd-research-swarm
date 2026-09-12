# F-003: Bloch–Kato Conjecture on Special Values of L-Functions

## Direction ID
F-003

## Title
Bloch–Kato Conjecture on Special Values of L-Functions

## Status Assessment
Open in general. Proven for rank ≤ 1 elliptic curves over ℚ (Gross–Zagier + Kolyvagin). Partial results for CM abelian varieties (Rubin), Hilbert modular forms (Dasgupta, Spies), and function field analogues (Lafforgue). Kato (2004) proves the "≤" direction for all modular motives.

## Testable Conjecture or Lemma

**Conjecture (Bloch–Kato).** Let M be a pure motive over ℚ of weight w with coefficients in a number field F, and let n be an integer. Then:

1. **Order of vanishing:**
   ```
   ord_{s=n} L(M,s) = dim_F H¹_f(ℚ, M^*(n)) − dim_F H⁰(ℚ, M^*(n))
   ```
   where H¹_f is the Bloch–Kato Selmer group.

2. **Leading coefficient:**
   ```
   L^{(r)}(M,n) / Ω_∞(M,n) = (#H¹_f)_tors / #H¹/H¹_f × ∏_p c_p(M,n) / (#H⁰)²
   ```

**Lemma (Kato's inequality).** For M = h^i(X) with X modular, i ≥ 1:
```
ord_{s=n} L(M,s) ≥ dim_F H¹_f(ℚ, M^*(n)) − dim_F H⁰(ℚ, M^*(n))
```

For M = h¹(E), n = 1, this recovers the "rank ≤ analytic rank" direction of BSD.

## Approach Summary
1. **Euler systems**: Construct Kato-type Euler systems in Galois cohomology to bound Selmer groups from above.
2. **Iwasawa theory**: Use the main conjecture to relate characteristic ideals of Selmer groups to p-adic L-functions.
3. **p-adic Hodge theory**: Define H¹_f via Fontaine's period rings (B_dR, B_cris, B_st) and establish local conditions.
4. **Comparison theorems**: Relate Bloch–Kato Selmer groups to classical Selmer groups for abelian varieties, and to Selmer groups of modular forms.
5. **Descent arguments**: Use Kolyvagin's derivative classes and the explicit reciprocity law to produce non-trivial classes in H¹_f.

## Computational Example

**Motive M = h¹(E) for E = 11a1 (rank 0):**
- H¹_f(ℚ, V₅(E)) = Sel₅(E/ℚ) = 0 (trivial 5-Selmer group)
- H⁰(ℚ, V₅(E)) = 0 (no 5-torsion)
- Predicted: ord_{s=1} L(E,s) = 0 − 0 = 0 ✓ (L(E,1) ≠ 0)
- Leading coefficient: L(E,1)/Ω_E = 1/5 = (#III · ∏ c_p) / |E(ℚ)_tors|²

**Motive M = h¹(E) for E = 37a1 (rank 1):**
- H¹_f(ℚ, V₂(E)) ≅ ℤ₂ (the 2-adic Selmer group has rank 1)
- H⁰(ℚ, V₂(E)) = 0
- Predicted: ord_{s=1} L(E,s) = 1 − 0 = 1 ✓

**Motive M = h²(S) for S a K3 surface:**
- Partial results by van Geemen, Top, Elsenhans–Jahnel via explicit computation of transcendental lattices.
- The Bloch–Kato Selmer group H¹_f(ℚ, H²(S)(2)) controls the special value L(H²(S),2).

## Obstacle Analysis
1. **Euler systems beyond GL₂**: No Kato-type Euler systems are known for GL_n with n ≥ 3. This is the central obstruction to proving the Bloch–Kato conjecture in general.
2. **Parity issues**: The parity conjecture (Nekovář) gives necessary conditions on Selmer ranks, but sufficient conditions require constructing actual cohomology classes.
3. **Period computations**: The Archimedean periods Ω_∞(M,n) involve comparison between Betti and de Rham cohomology with Hodge filtration, which is computationally difficult for higher-dimensional motives.
4. **Tamagawa factors**: Local Euler factors at bad primes require detailed knowledge of the reduction type and the Néron model.

## Cross-Group Connections
- **F-001 (Kato's zeta)**: The prototype Euler system; sharpness of Kato's bound = p-part of Bloch–Kato for h¹(E).
- **F-007 (Motivic L-functions)**: The Bloch–Kato conjecture is the "special values" part of the motivic framework.
- **F-009 (Finiteness of III)**: The Bloch–Kato formula for #III is a consequence of the full conjecture.
- **F-010 (Arakelov)**: The Tamagawa factors and periods have Arakelov-geometric interpretations.
- **F-011 (Deninger)**: Deninger's program would provide the cohomological realization of the Bloch–Kato formula.

## Classification
Grand challenge — flagship open problem. The Bloch–Kato conjecture is the most general known framework encompassing BSD.
