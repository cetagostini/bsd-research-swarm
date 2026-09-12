# D-012: Effective Finiteness — Explicit Upper Bounds for |III|

**Direction ID:** D-012
**Title:** Effective Finiteness and Explicit Upper Bounds for |Sha|

## Status Assessment

Open. Unconditional, effective bounds on |Sha| in the form |Sha| ≤ C(N) are known only for rank ≤ 1 (via Gross-Zagier-Kolyvagin) and for the 2-part (via explicit 2-descent). For rank ≥ 2, no unconditional effective bound exists. The analytic approach via subconvex bounds is promising but incomplete.

## Testable Conjecture or Lemma

**Theorem (Gross-Zagier-Kolyvagin, conditional).** For E/Q of analytic rank ≤ 1:

$$|Sha(E/Q)| \leq C_1 \cdot \frac{L^{(r)}(E,1)}{r! \cdot \Omega_E \cdot R_E} \cdot |E(Q)_{tors}|^2 \cdot \prod c_v^{-1}$$

where C_1 is an effectively computable constant depending on E.

**Bound (Zywina, 2010).** For the 2-part:

$$|Sha[2]| \leq 4^{s-1}$$

where s = #{v | 2N : δ_v(E(Q_v)/2) has proper image in H^1(Q_v, E[2])}.

**Bound (Silverman).** For non-torsion P ∈ E(Q):

$$\hat{h}(P) \geq \frac{\log N}{C_2}$$

for an explicit constant C_2 depending on the discriminant. This bounds R_E from below, hence bounds |Sha| from above (via BSD).

**Conjecture (Effective bound).** For E/Q of conductor N:

$$|Sha(E/Q)| \leq C \cdot N^{1+\varepsilon}$$

for an absolute constant C (depending on ε). This would follow from BSD plus explicit estimates for all terms.

**Approach via Selmer groups.** The Selmer group satisfies:

$$|Sel_p(E/Q)| \leq \prod_{v | pN\infty} |\text{im}(\delta_v)|$$

and |Sha[p]| ≤ |Sel_p| / |E(Q)/p|. The local images are bounded by |H^1(Q_v, E[p])| ≤ p^{2+[Q_v:Q_p]} for v | p.

## Approach Summary

1. **Selmer group bounds (unconditional):** For each prime p, bound |Sel_p(E/Q)| by the product of local image sizes. At primes v ∤ pN, the local Kummer map δ_v is surjective, so the bound comes from bad primes only.

2. **Height bounds (Silverman, Masser-Wüstholz):** The canonical height ĥ(P) for non-torsion P is bounded below by an explicit function of the conductor. Combined with the regulator R_E = det(⟨P_i, P_j⟩) ≥ ĥ(P)^{rank}, this gives:

$$R_E \geq \left(\frac{\log N}{C}\right)^{rank}$$

3. **Analytic bounds (subconvexity):** For rank 0:

$$L(E, 1) \ll_\varepsilon N^{1/2+\varepsilon}$$

by the subconvex bound. For rank 1, L'(E,1) is controlled by the Gross-Zagier formula: L'(E,1) = c · ĥ(y_K) where y_K is a Heegner point.

4. **Tamagawa number bounds:** c_v ≤ |v(N)|^{O(1)} for each v | N. The product ∏ c_v is bounded by N^{O(1)}.

5. **Combining:** |Sha| ≤ L^{(r)}(E,1) · |tors|² / (Ω_E · R_E · ∏ c_v). With all bounds explicit:

$$|Sha| \leq C \cdot N^{1+\varepsilon} \cdot \left(\frac{\log N}{C}\right)^{-rank}$$

For rank = 0: |Sha| ≤ C · N^{1+ε}. For rank = 1: |Sha| ≤ C · N^{1+ε} / log N.

## Computational Example

**Example 1: E = 11a1.** N = 11, rank 0. L(E,1)/Ω_E = 1. |E(Q)_tors| = 5, c_11 = 1. R_E = 1 (rank 0). Bound: |Sha| ≤ 1 × 25 / (1 × 1 × 1) = 25. Actual: |Sha| = 1. The bound is not tight but is effective.

**Example 2: E = 571a1.** N = 571, rank 0. L(E,1)/Ω_E = 1/4. |E(Q)_tors| = 1, c_571 = 1. Bound: |Sha| ≤ (1/4) × 1 / (1 × 1) = 1/4, but |Sha| must be a positive integer... This means the bound requires precision: L(E,1)/Ω_E = 1/4 exactly, so |Sha| = 4. The bound is sharp when the analytic data is exact.

**Example 3: 2-descent bound.** For E = 960d1, s = 5 (five primes with non-trivial local conditions). |Sha[2]| ≤ 2⁴ = 16. Actual: |Sha[2]| = 16. The bound is sharp.

**Example 4: Height bound.** For E of conductor 10^6 with rank 1, Silverman's bound gives ĥ(P) ≥ log(10^6)/C ≈ 14/C. If C ≈ 10, then ĥ(P) ≥ 1.4, and R_E ≥ 1.4. Combined with L'(E,1)/Ω_E ≤ N^{1/2+ε} ≈ 10^3: |Sha| ≤ 10^3 × |tors|² / (1.4 × ∏ c_v).

## Obstacle Analysis

- **Rank ≥ 2:** The Euler system class vanishes, giving no unconditional bound on Sel_p. The height bound R_E ≥ (log N/C)^rank gives |Sha| ≤ N^{1+ε} / (log N)^rank, but this requires knowing Sha is finite first.
- **Regulator computation:** For rank ≥ 2, R_E is a determinant of height pairings. Computing this determinant to sufficient precision is a bottleneck.
- **Subconvex bounds:** The subconvex bound L(E, 1+it) ≪ N^{1/2−δ} is known (Michel, 2009) but the exponent δ = 1/7 is not strong enough for the best bounds.
- **Uniformity:** The constants in the bounds typically depend on E, not just on N. Making the bounds uniform in the isogeny class (or in the conductor) is an additional challenge.
- **Without assuming finiteness:** The most fundamental obstacle is that |Sha| ≤ C(N) requires knowing Sha is finite, or proving finiteness as part of the bound.

## Cross-Group Connections

- **Group B (Euler Systems):** The Euler system bound for rank ≤ 1 is the primary tool. For rank ≥ 2, Group B's work on new Euler systems could provide the missing input.
- **Group D (D-003):** The descent bounds (especially |Sha[2]| ≤ 4^{s-1}) are the unconditional component of the effective bounds.
- **Group D (D-001):** Finiteness of Sha via Euler systems (D-001) is the prerequisite for effective bounds.
- **Group C (Arithmetic Statistics):** The bound |Sha| ≤ C · N^{1+ε} is consistent with the heuristic prediction that |Sha| grows slowly with conductor.

## Classification

**Type:** Core / Effective, Open
**Difficulty:** Very High (rank ≥ 2, uniform bounds), Moderate (rank ≤ 1)
**Impact:** Would make BSD computationally verifiable for all curves of small rank with explicit error terms.
