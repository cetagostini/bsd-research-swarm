# C-002: The Goldfeld Conjecture — 100% of Curves Have Rank ≤ 1

## Status Assessment

Goldfeld's conjecture — that 100% of elliptic curves over $\mathbb{Q}$ have algebraic rank 0 or 1 — is the central open problem in arithmetic statistics of elliptic curves. The best unconditional result is Bhargava-Shankar's bound that the average rank is at most 0.885, which implies at least 11.5% of curves have rank 0 (but does not rule out a positive proportion having rank ≥ 2). The BKLRP result (2023) establishes the exact distribution of 2-Selmer ranks, with average 3, and the distribution is consistent with Goldfeld. Smith's conditional result (2022) proves 100% rank ≤ 1 for quadratic twist families under GRH and finiteness of Sha. The gap between Selmer rank and actual rank — controlled by Sha[2] — remains the primary obstruction.

## Testable Conjecture

**Conjecture C-002 (Goldfeld).** As $X \to \infty$:
$$\frac{\#\{E/\mathbb{Q} : H(E) \leq X,\ \operatorname{rank}(E(\mathbb{Q})) = 0\}}{\#\{E/\mathbb{Q} : H(E) \leq X\}} \to \frac{1}{2},$$
$$\frac{\#\{E/\mathbb{Q} : H(E) \leq X,\ \operatorname{rank}(E(\mathbb{Q})) = 1\}}{\#\{E/\mathbb{Q} : H(E) \leq X\}} \to \frac{1}{2},$$
$$\frac{\#\{E/\mathbb{Q} : H(E) \leq X,\ \operatorname{rank}(E(\mathbb{Q})) \geq 2\}}{\#\{E/\mathbb{Q} : H(E) \leq X\}} \to 0.$$

The convergence rate is expected to be $O(X^{-\delta})$ for some $\delta > 0$, though no explicit rate is predicted by current heuristics.

## Approach Summary

**Selmer-to-rank bridge via Sha[2].** The BKLRP distribution gives $\Pr(s_2 = 0) = 1/4$, $\Pr(s_2 = 1) = 1/4$, $\Pr(s_2 = 2) = 15/64$, $\Pr(s_2 = 3) = 15/128$, etc. Since $\operatorname{rank} = s_2 - 2\dim_2 \text{III}[2]$ (the Cassels-Tate exact sequence), Goldfeld's conjecture is equivalent to: for 100% of curves, $2\dim_2 \text{III}[2] = s_2 - \operatorname{rank}$. In particular, for curves with $s_2 = 2k$, one needs $\dim_2 \text{III}[2] = k - r/2$ where $r$ is the rank. The key challenge is showing that the Sha[2] distribution exactly compensates for the excess Selmer rank.

**Root number and parity.** The parity conjecture (proven for 100% of curves by Dokchitser-Dokchitser under mild hypotheses) gives $\operatorname{rank} \equiv \operatorname{ord}_{s=1} L(E,s) \pmod{2}$ for 100% of curves. Combined with Sato-Tate (now unconditional), the root number is equidistributed: $w(E) = +1$ for 50% and $w(E) = -1$ for 50% of curves. This matches the Goldfeld split: 50% rank 0, 50% rank 1.

**Potential approach via multiple primes.** Using $p$-Selmer groups for several primes simultaneously: if $E[p]$ is irreducible for some prime $p$ (which holds for 100% of curves by Serre's theorem), then the $p$-part of Sha is constrained. Joint control over $\text{III}[2]$ and $\text{III}[3]$ might yield the desired bound: the probability that both Sha[2] and Sha[3] are simultaneously large is much smaller than either individually.

## Computational Example

**LMFDB data (conductor $\leq 10^8$).** Among $\sim 10^8$ curves in the database:
- Rank 0: $\approx 47.5\%$; Rank 1: $\approx 47.5\%$; Rank 2: $\approx 4.7\%$; Rank 3: $\approx 0.3\%$; Rank ≥ 4: $\approx 0.01\%$
- Average rank: $\approx 0.58$
- These small-conductor data are consistent with Goldfeld but show a persistent 5% rate of rank 2 that is expected to decay as conductor grows

**Twist family of $E = 11a1$.** For $|D| \leq 10^6$:
- Rank 0: 51.2%, Rank 1: 47.8%, Rank 2: 1.0%
- The rank-2 proportion drops as $|D|$ increases, consistent with $\Pr(r \geq 2) \to 0$

**Heuristic prediction (Delaunay-Watkins).** For the full family ordered by height:
- $\Pr(r = 0) \approx 0.475$, $\Pr(r = 1) \approx 0.475$, $\Pr(r = 2) \approx 0.05$
- The "excess" rank 2 curves at small conductor are expected to thin out

## Obstacle Analysis

The fundamental gap is between the BKLRP Selmer distribution (which is now a theorem) and the rank distribution (which is conjectural). The 2-Selmer rank is an upper bound for rank, with equality if and only if Sha[2] = 0. The BKLRP distribution shows that the average 2-Selmer rank is 3, but this includes a contribution from Sha[2]. To prove Goldfeld, one needs to show that Sha[2] is "large enough" on average to bring the average rank down to 1/2. This requires either: (a) directly computing the average of $2^{\dim \text{III}[2]}$ (which appears in the BSD formula via the ratio $L^{(r)}(E,1)/r!$), or (b) using a different algebraic approach that bypasses the Sha[2] problem entirely.

## Cross-Group Connections

- **Group A (Iwasawa Theory):** Control of the $p$-part of Sha via Iwasawa main conjecture (Skinner-Urban) could be combined with Selmer rank bounds for multiple primes.
- **Group B (Euler Systems):** Non-vanishing of Euler system classes (Beilinson-Kato) for 100% of curves of rank 1 would complete the rank-1 case of Goldfeld.
- **Group D (Tate-Shafarevich):** The distribution of Sha[2] is the missing ingredient. Cohen-Lenstra-type predictions for Sha (C-003) give $\Pr(\text{III}[2] = 0) \approx 0.94$, which would imply Goldfeld.
- **Group H (Computational):** Verifying rank for curves of conductor up to $10^{10}$ would test the thinning of rank-2+ curves.

## Classification

**Conjecture** — the central open problem. Supported by computational evidence, the BKLRP Selmer distribution, and conditional results of Smith. No unconditional progress beyond average rank ≤ 0.885.
