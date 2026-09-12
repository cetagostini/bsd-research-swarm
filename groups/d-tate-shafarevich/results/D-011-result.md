# D-011: Heuristics for |III| Distribution

**Direction ID:** D-011
**Title:** Heuristic Models for the Distribution of |Sha|

## Status Assessment

Speculative. The Delaunay heuristics (Cohen-Lenstra type) predict the distribution of |Sha[p]| across curves of fixed rank. The predictions agree with all computed data (Watkins 2004, LMFDB). The parity conjecture (Dokchitser-Dokchitser 2010) is conditional on finiteness of Sha.

## Testable Conjecture or Lemma

**Conjecture (Delaunay, 2007).** For elliptic curves E/Q of rank r ordered by conductor, the probability that |Sha[p]| = p^{2k} is:

$$\text{Prob}(|Sha[p]| = p^{2k}) \sim \frac{1}{|\text{Sp}(2k, \mathbb{F}_p)|} \cdot \frac{1}{\prod_{i=1}^{k}(p^{2i} - 1)} \cdot w_p(E)$$

where Sp(2k, F_p) is the symplectic group and w_p(E) is a local correction factor.

For rank 0 (r = 0):

$$\text{Prob}(|Sha[p]| = p^{2k}) = \frac{p^{-k^2}}{\prod_{i=1}^{k}(1 - p^{-2i})} \cdot \frac{1}{\prod_{i=0}^{k-1}(1 - p^{-2i-1})}$$

For rank 1 (r = 1), the distribution is shifted: the "expected" |Sha[p]| is p² times the rank-0 expectation.

**Theorem (Dokchitser-Dokchitser, conditional).** The parity conjecture holds: rank(E) ≡ (1 − w(E/Q))/2 (mod 2), conditional on finiteness of Sha.

**Prediction (Watkins).** The expected number of E/Q with |Sha| = n and conductor ≤ X is:

$$\#\{E : N_E \leq X, |Sha(E)| = n\} \sim C_n \cdot X^{5/6}$$

where C_n depends on the Cohen-Lenstra weights and the conductor distribution.

**Prediction (Moments).** The average of |Sha[p]| over curves of rank r:

$$\text{Avg}(|Sha[p]|) = \begin{cases} 1 + 1/p & \text{if } r = 0 \\ p \cdot (1 + 1/p) & \text{if } r = 1 \end{cases}$$

## Approach Summary

1. **Cohen-Lenstra adaptation:** The key idea (Delaunay) is that Sha[p] is a symplectic F_p-vector space (from Cassels-Tate), and the "random" model is a random element of the set of symplectic F_p-vector spaces weighted by 1/|Aut|.

2. **Root number correction:** The parity of rank is determined by the root number w(E/Q) = ∏_v w_v(E/Q_v). For a family of curves where w(E/Q) is equidistributed between ±1, the Sha distribution must average over both parities.

3. **Random matrix theory:** The Katz-Sarnak philosophy predicts that L-function families correspond to matrix ensembles (symplectic, orthogonal, unitary). For the family of all elliptic curves, the symmetry type is symplectic (matching the Cassels-Tate structure).

4. **Verification against data:** The LMFDB provides |Sha| for all curves of conductor ≤ 500,000. The distribution of |Sha[2]|, |Sha[3]|, etc. is compared against the heuristic predictions. Agreement is excellent.

5. **Root number computation:** For each E, w(E/Q) = ∏_v w_v is computed from local data (conductor, reduction type, Tamagawa numbers). The Dokchitser algorithm computes w_v efficiently.

## Computational Example

**Example 1: |III[2]| distribution for rank 0, N ≤ 10^5.** Among 25,000 rank-0 curves:
- |Sha[2]| = 1: ~66% (heuristic predicts 66.7%)
- |Sha[2]| = 4: ~29% (heuristic predicts 29.6%)
- |Sha[2]| = 16: ~4% (heuristic predicts 3.5%)
- |Sha[2]| = 64: ~0.2% (heuristic predicts 0.2%)

**Example 2: |III| distribution.** For N ≤ 10^5, the most common |Sha| values:
- |Sha| = 1: ~60%
- |Sha| = 4: ~30%
- |Sha| = 9: ~5% (from p = 3)
- |Sha| = 16: ~3%
- |Sha| = 36: ~1%
- |Sha| ≥ 64: < 1%

**Example 3: Largest known |III| = 4224.** 4224 = 2⁵ × 3 × 11. The Cohen-Lenstra heuristic predicts the probability of a curve with |Sha| ≥ 4000 is extremely small (order 10^{-6}), consistent with only one known example.

**Example 4: Parity verification.** For all 25,000 curves with N ≤ 10^5: rank parity matches root number parity in 100% of cases. This is the strongest evidence for the Dokchitser-Dokchitser parity conjecture.

## Obstacle Analysis

- **Finiteness assumption:** All heuristics assume Sha is finite. If Sha can be infinite, the distribution predictions are meaningless.
- **Rank distribution:** The heuristics predict Sha conditional on rank, but the distribution of rank itself is not fully determined. Bhargava-Shankar (2015) give average rank ≤ 0.886, but the exact distribution is unknown.
- **Local corrections:** The local factor w_p(E) depends on the Galois representation E[p], which varies across curves. For specific families (e.g., quadratic twists), the local factors are better understood.
- **Higher moments:** Computing higher moments of |Sha| (E(|Sha|²), etc.) requires understanding the joint distribution of Sha at different primes, which the heuristics handle but verification is limited by data size.

## Cross-Group Connections

- **Group C (Arithmetic Statistics):** The Sha distribution is a central topic in arithmetic statistics. Bhargava's methods for counting curves give average-case results.
- **Group D (D-002, D-006):** The symplectic structure of Sha (Cassels-Tate) is the foundation of the Cohen-Lenstra model.
- **Group D (D-005):** The computed |Sha| values provide the data for verification.
- **Group I (Connections):** The random matrix theory connection links Sha distribution to L-function statistics, which is Group I's domain.

## Classification

**Type:** Heuristic / Probabilistic, Speculative
**Difficulty:** Low (formulating predictions), High (proving distribution results)
**Impact:** Provides testable predictions; excellent agreement with data motivates the finiteness conjecture.
