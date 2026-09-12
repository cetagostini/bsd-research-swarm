# F-004: Syntomic Cohomology and p-Adic Regulators (Besser)

## Direction ID
F-004

## Title
Syntomic Cohomology and p-Adic Regulators (Besser)

## Status Assessment
Active research. The K₂ case is well-developed (Besser 2000), with explicit formulas via Coleman integration. K₃ and higher cases are open. Yamashita and Asakawa studied the syntomic regulator on higher K-theory using rigid analytic methods.

## Testable Conjecture or Lemma

**Conjecture (Syntomic–Perrin-Riou comparison).** For a modular elliptic curve E/ℚ and a prime p of good reduction, the composite
```
K₂(ℚ_p) →^{reg_p} H²_syn(E, ℤ_p(2)) →^{comp} H¹_dR(E)/F⁰
```
coincides with the Perrin-Riou regulator map on the image of Kato's zeta element. More precisely:
```
reg_p(z_Kato) = L_p(E,1)  in  ℤ_p/(p-adic periods)
```

**Lemma (Besser's formula).** For a smooth curve X over a p-adic field K with good reduction at p:
```
reg_p({f,g}) = ∫_γ log_p(f) dlog_p(g)
```
where {f,g} ∈ K₂(X) is a Steinberg symbol, log_p is the p-adic logarithm, and γ is a Coleman path.

## Approach Summary
1. **Syntomic site**: Use the Fontaine–Messing definition of H^i_syn(X, ℤ_p(j)) as hypercohomology of the syntomic complex (A_cris, F^r, φ).
2. **Besser's regulator**: The map K_n(X) → H^n_syn(X, ℤ_p(j)) via the Denis lemma and p-adic polylogarithms.
3. **Coleman integration**: Compute the p-adic regulator explicitly using Coleman's theory of p-adic integration of closed 1-forms.
4. **Comparison**: Show that the syntomic regulator and the Perrin-Riou regulator agree on Kato's class, removing the "up to units" ambiguity.

## Computational Example

**Curve**: E: y² = x³ − x over ℚ₅ (good reduction at 5).

- Steinberg symbol: {x, y} ∈ K₂(E_{ℚ₅}).
- Besser's formula: reg₅({x,y}) = ∫_γ log₅(x) dlog₅(y) where γ is a path on E(ℚ₅).
- Coleman integration: ∫_γ x · dy/y = (explicit 5-adic number computable via the Frobenius structure).
- The result equals L₅(E,1) modulo 5-adic periods, confirming the syntomic–Perrin-Riou comparison.

**Higher depth (K₃)**: For a Steinberg symbol {x,y,z} ∈ K₃(E), the expected formula involves:
```
reg_p({x,y,z}) = ∫∫ log_p(x) dlog_p(y) ∧ dlog_p(z)
```
(iterated Coleman integral), but the convergence and independence of path are not established.

## Obstacle Analysis
1. **Higher-depth polylogarithms**: For n ≥ 3, the p-adic polylogarithm of depth n−1 is not well understood. Its relationship to motivic polylogarithms is conjectural.
2. **Iterated Coleman integration**: The theory of iterated Coleman integrals (depth ≥ 2) exists in principle (via the work of Anderson, Coleman, de Shalit) but is not fully developed computationally.
3. **Comparison in families**: The syntomic–Perrin-Riou comparison needs to hold in families (over the universal deformation space of E), which requires p-adic Hodge theory in families.
4. **Supersingular primes**: The syntomic cohomology and the Perrin-Riou map both require modification at supersingular primes.

## Cross-Group Connections
- **F-001 (Kato's zeta)**: The syntomic regulator is the bridge between Kato's class (arithmetic) and L_p(E,1) (analytic).
- **F-006 (Regulator K₂(E) → ℝ)**: The Archimedean counterpart: Beilinson's regulator vs. the p-adic syntomic regulator.
- **F-012 (Soulé regulators)**: The Soulé regulator (étale side) and the syntomic regulator (p-adic side) are related by p-adic comparison theorems.

## Classification
Technical tool — enabling technology. The syntomic regulator is essential for making Kato's theorem unconditional.
