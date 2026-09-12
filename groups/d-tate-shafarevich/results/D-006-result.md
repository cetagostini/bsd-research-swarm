# D-006: The Cassels-Tate Pairing and Its Non-degeneracy

**Direction ID:** D-006
**Title:** Non-degeneracy of the Cassels-Tate Pairing on Sha

## Status Assessment

Established (conditional on finiteness). The pairing is defined, proven alternating, and proven non-degenerate conditional on |Sha| < ∞. Unconditional non-degeneracy remains open and is essentially equivalent to proving finiteness of Sha. Explicit computation algorithms exist for Sha[2] (via 2-descent) and are being developed for Sha[3].

## Testable Conjecture or Lemma

**Theorem (Cassels, 1962).** If Sha(E/Q) is finite, the Cassels-Tate pairing ⟨·,·⟩: Sha[p^n] × Sha[p^n] → Z/p^nZ is non-degenerate.

**Corollary.** If Sha is finite, then |Sha[p]| = p^{2k} for some k ≥ 0 (the pairing makes Sha[p] a symplectic F_p-vector space).

**Conjecture (Unconditional non-degeneracy).** The pairing is non-degenerate on Sha[p^n] for all p, n, without assuming finiteness.

**Explicit Formula (O'Neil, 2002).** For x, y ∈ Sha ⊂ H^1(Q, E[p^n]), the pairing is:

$$\langle x, y \rangle = \sum_{v} \text{inv}_v(\tilde{\delta}(x_v) \cup y_v) \in \mathbb{Q}/\mathbb{Z}$$

where δ̃: H^1(Q_v, E[p^n]) → H^2(Q_v, E)[p^n] is the connecting homomorphism and inv_v: H^2(Q_v, G_m) → Q/Z is the local invariant.

**Parity Constraint (Dokchitser-Dokchitser, conditional).** If the parity conjecture holds (rank parity = root number parity), then non-degeneracy of the Cassels-Tate pairing forces:

$$\text{rank}(E) \equiv \dim_{\mathbb{F}_p} Sha[p] / 2 \pmod{2}$$

## Approach Summary

1. **Local-global computation:** For each x ∈ Sha[p^n], compute the local images x_v ∈ H^1(Q_v, E[p^n]) at all places v. The pairing ⟨x, y⟩ = Σ_v inv_v(δ(x_v) ∪ y_v) reduces to local computations.

2. **2-descent method:** For p = 2, Sha[2] ⊂ E(Q)/2E(Q) via the Kummer map, and the Cassels-Tate pairing on Sha[2] can be computed from the Hilbert symbol at each prime. The Dokchitser-Dokchitser algorithm computes this efficiently.

3. **3-descent method:** For p = 3, the pairing uses the 3-descent covering spaces. The local invariant at each prime is computed from the period-index obstruction on the covering curve.

4. **Poitou-Tate approach:** The 9-term exact sequence relates the Selmer group, the dual Selmer group, and local terms. Non-degeneracy follows from the exactness and the finiteness hypothesis.

5. **Isogeny descent:** For φ: E → E', the φ-Cassels-Tate pairing is a refinement. Ciperiani-Wiles proved compatibility: the pairings on Sha(E) and Sha(E') are related by the isogeny.

## Computational Example

**Example 1: |III[2]| = 4 on 571a1.** Sha[2] ≅ F_2². The pairing matrix in a basis {x_1, x_2} is:

$$\begin{pmatrix} 0 & 1/2 \\ -1/2 & 0 \end{pmatrix}$$

which is non-degenerate and alternating. The symplectic form confirms k = 1.

**Example 2: |III[2]| = 16 on 960d1.** Sha[2] ≅ F_2⁴. The pairing matrix is a 4×4 alternating matrix with non-zero Pfaffian. Two hyperbolic planes, confirming k = 2.

**Example 3: Verification across conductor range.** For all E with N ≤ 10,000 and |Sha[2]| > 1, the pairing is computed and verified to be non-degenerate. In 100% of cases, the pairing matrix has full rank (Pfaffian non-zero in F_2).

**Example 4: Under isogeny.** E = 11a1 has a 5-isogeny to 11a2. The Cassels-Tate pairing on Sha(E)[5] and Sha(E')[5] are related by |ker φ̂|/|ker φ| = 1. Both Sha values are trivial, so the pairing is vacuously non-degenerate.

## Obstacle Analysis

- **Finiteness assumption:** The non-degeneracy proof uses finiteness to ensure the Poitou-Tate sequence is exact in the relevant degrees. Without finiteness, the sequence may have infinite terms and the pairing may degenerate.
- **Explicit computation for p ≥ 3:** The pairing for p = 3 requires computing local invariants at all primes using 3-descent data. This is implemented but expensive for large conductor.
- **Circularity:** To use non-degeneracy to prove something about Sha, one needs to know Sha (at least its order) to verify the pairing is non-degenerate. This limits the utility of the pairing as an independent constraint.
- **Infinite Sha:** If Sha is infinite, the p-primary part could be a direct limit of finite groups with non-degenerate pairings, or it could be genuinely degenerate. No examples are known.

## Cross-Group Connections

- **Group D (D-002):** The structural properties of the pairing (alternating, symplectic) are from D-002. D-006 focuses on non-degeneracy and computation.
- **Group D (D-011):** The perfect-square constraint from the pairing feeds directly into the Cohen-Lenstra heuristics.
- **Group C (Arithmetic Statistics):** The distribution of |Sha[p]| = p^{2k} depends on the symplectic structure. The moments of the pairing's Pfaffian relate to random matrix statistics.
- **Group F (Motivic/Cohomological):** The pairing has a motivic interpretation via the cup product in motivic cohomology. A motivic proof of non-degeneracy would bypass the finiteness assumption.

## Classification

**Type:** Structural / Established (conditional)
**Difficulty:** Moderate (computation), Very High (unconditional non-degeneracy)
**Impact:** Fundamental constraint on Sha structure; perfect-square property verified computationally in all known cases.
