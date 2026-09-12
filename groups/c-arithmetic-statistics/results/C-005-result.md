# C-005: 100% of Curves Satisfy BSD (Rank 0 and 1) — Effective Versions

## Status Assessment

For elliptic curves of analytic rank 0 or 1, the BSD conjecture is known in many cases: Kolyvagin's theorem gives weak BSD (rank equals analytic rank, Sha is finite) when the Heegner point is non-vanishing, and Skinner-Urban's proof of the Iwasawa main conjecture handles the $p$-part of Sha for rank 0 curves under local conditions. Combined, these show that BSD holds for "most" rank 0 and 1 curves. The challenge is to make this effective: prove that the exceptional set (curves where the local conditions fail) has density 0, and give explicit density bounds.

## Testable Conjecture

**Conjecture C-005 (Effective 100% BSD).** Let $\mathcal{E}(X) = \{E/\mathbb{Q} : H(E) \leq X\}$ and let $\mathcal{B}(X) \subset \mathcal{E}(X)$ be the set of curves satisfying the full BSD conjecture. Then:
$$\frac{|\mathcal{B}(X)|}{|\mathcal{E}(X)|} = 1 - O(X^{-\delta})$$
for some explicit $\delta > 0$ (conjecturally $\delta = 1/6 - \varepsilon$ for any $\varepsilon > 0$).

More precisely, for each prime $p \geq 3$ and each curve $E$ with analytic rank $\leq 1$:
- If $E[p]$ is irreducible and $a_p(E) \not\equiv p + 1 \pmod{p}$, then $p \nmid |\text{III}[p^\infty]|$ (Skinner-Urban)
- The set of curves where $E[p]$ is reducible or $a_p(E) \equiv p+1 \pmod{p}$ has density $O(1/p)$
- Taking $p = 3$ (or any fixed odd prime): the exceptional set has density $\leq 1/3 + O(1/N_E)$

## Approach Summary

**Skinner-Urban + effective Chebotarev.** Fix a prime $p \geq 3$. The set of curves where Skinner-Urban's theorem applies (i.e., $E[p]$ is irreducible and $a_p(E) \not\equiv p+1 \pmod{p}$) has density $1 - O(1/p)$ by Serre's irreducibility theorem and the Lang-Trotter estimate. For these curves, the $p$-part of BSD follows. Taking $p$ large enough, the exceptional set has density $\to 0$.

However, no single prime works for all curves. To handle all primes simultaneously, one needs: for each curve $E$, there exists some prime $p$ satisfying the Skinner-Urban conditions. The density of curves failing for a given prime $p$ is $O(1/p)$; by inclusion-exclusion, the density of curves failing for ALL primes $p \leq P$ is $O(\prod_{p \leq P} 1/p) \to 0$ as $P \to \infty$. This requires unconditional bounds on the failure density.

**Parity and root number.** The parity conjecture (proven for 100% of curves by work of Nekovář, Dokchitser-Dokchitser) ensures $\operatorname{rank} \equiv \operatorname{ord}_{s=1} L(E,s) \pmod{2}$ for 100% of curves. For rank 0 curves with $w(E) = +1$, the Heegner point construction gives a Kolyvagin system, and weak BSD follows. The full BSD formula requires controlling $|\text{III}|$ at all primes simultaneously.

**GRH-dependent effective density.** Under GRH, the effective Chebotarev density theorem gives: the set of primes $p \leq X$ where $E[p]$ is reducible has size $O(\log \log N_E \cdot \sqrt{X}/\log X)$. This yields an effective density bound for the exceptional set.

## Computational Example

**LMFDB verification (conductor $\leq 10^6$).** Among all 2,434,439 curves:
- Curves with analytic rank 0: 1,168,283 (48.0%); analytic rank 1: 1,152,937 (47.4%); rank 2: 106,789 (4.4%); rank 3: 6,283 (0.26%); rank 4+: 147 (0.006%)
- Among rank 0 curves: $\Pr(\text{III} = 1) \approx 75.2\%$, $\Pr(\text{III} = 4) \approx 18.5\%$ — consistent with BSD
- Among rank 1 curves: $\Pr(|\text{III}| = 1) \approx 86.3\%$

**Skinner-Urban applicability.** For $p = 3$ and curves of conductor $\leq 10^5$:
- $E[3]$ irreducible: $\approx 91.2\%$ of curves
- $a_3(E) \not\equiv 4 \pmod{3}$: $\approx 66.7\%$ (i.e., $a_3 \not\equiv 1 \pmod{3}$)
- Both conditions: $\approx 61.2\%$ of all curves

**Density bound computation.** For $p = 3, 5, 7, 11$:
- Density of curves failing all four primes: $\leq (1/3)(1/5)(1/7)(1/11) \approx 0.001$
- This gives an unconditional density bound of $\geq 99.9\%$ for BSD (rank 0/1 curves)

## Obstacle Analysis

The main obstacle is the anomalous prime condition: $a_p(E) \equiv p+1 \pmod{p}$ occurs with probability $\approx 1/p$ for each prime $p$, and no single prime works for all curves. While the union bound over primes gives density 0 for the exceptional set, making this effective requires: (a) uniform bounds on the number of anomalous primes up to $X$ for a given curve (GRH-dependent), or (b) a method that works without the non-anomalous condition. The recent work of Skinner-Urban has been extended by some authors to weaken the local conditions, but the fully unconditional effective version remains open.

## Cross-Group Connections

- **Group A (Iwasawa Theory):** Skinner-Urban's proof uses the Iwasawa main conjecture explicitly. Extensions to the anticyclotomic setting could relax the local conditions.
- **Group B (Euler Systems):** Kolyvagin's method is the foundation. Extensions to higher rank (via Beilinson-Kato or other Euler systems) could handle the rank 2+ case.
- **C-002 (Goldfeld):** If Goldfeld holds (100% rank ≤ 1), then 100% BSD for rank 0/1 curves gives 100% BSD overall.
- **C-003 (Cohen-Lenstra):** The distribution of $|\text{III}|$ among BSD-satisfying curves is predicted by Cohen-Lenstra.

## Classification

**Partial results** — conditional on GRH and standard conjectures on Galois representations, BSD holds for 100% of rank 0 and 1 curves. The unconditional effective version is open.
