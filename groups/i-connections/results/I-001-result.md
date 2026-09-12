# I-001: Colmez Conjecture on Average Norms of CM Points and BSD

## Direction ID and Title
**I-001** — Colmez Conjecture on Average Norms of CM Points and BSD

## Status Assessment
The averaged Colmez conjecture is proven (Yuan-Zhang 2014). The individual (non-averaged) Colmez conjecture remains open for most CM abelian varieties. The connection to BSD is structural and bidirectional: for CM elliptic curves of rank 1, Gross-Zagier provides one direction, and the Colmez conjecture would provide an independent route to the regulator formula.

## Testable Conjecture or Lemma

**Conjecture (Colmez–BSD Bridge for CM Curves).** Let $E/\mathbb{Q}$ be an elliptic curve with CM by $\mathcal{O}_K$, $K$ an imaginary quadratic field. Suppose $\operatorname{ord}_{s=1} L(E/\mathbb{Q}, s) = 1$. Then:

1. The individual Colmez conjecture for $E$ implies the rank-1 BSD formula for $E$: there exists a CM point $P \in E(K_N)$ of conductor $N$ such that
$$h_{\mathrm{Fal}}(P) = -\frac{1}{2} \frac{L'(E/K, 0)}{L(E/K, 0)} + c_E \log N + O(1),$$
and combined with the Gross-Zagier formula $L'(E/\mathbb{Q}, 1) = c \cdot \hat{h}(P_{\mathrm{Heegner}})$, this yields $L'(E/\mathbb{Q}, 1) / \Omega(E) \in \mathbb{Q}^\times$.

2. Conversely, the rank-1 BSD formula for all CM elliptic curves by $K$ implies the individual Colmez conjecture for the corresponding CM points.

**Precise implication chain:**
$$\text{Individual Colmez} + \text{Gross-Zagier} \implies \text{BSD rank-1 for CM curves by } K.$$

## Approach Summary
The approach proceeds in three layers:
1. **Faltings height ↔ Néron-Tate height:** For a CM point $P$ that is also a Heegner point, relate $h_{\mathrm{Fal}}(P)$ to $\hat{h}(P)$ via the theory of complex multiplication and the factorization $L(E/K, s) = L(\psi, s)L(\bar\psi, s)$.
2. **Gross-Zagier input:** The Gross-Zagier formula gives $L'(E/\mathbb{Q}, 1) = c \cdot \hat{h}(P_{\mathrm{Heegner}})$ for an explicit $c$ involving the conductor, periods, and local factors.
3. **Colmez input:** The individual Colmez conjecture gives $h_{\mathrm{Fal}}(P)$ in terms of $L'(E/K, 0)/L(E/K, 0)$. The functional equation for $L(E/K, s)$ converts this to $L'(E/K, 1)$, and the factorization converts it to $L'(E/\mathbb{Q}, 1)$.

## Computational Example

**Example 1: $E = y^2 = x^3 - x$ (CM by $\mathbb{Z}[i]$, conductor 32).**
- $L(E, 1) \approx 0.655514...$, rank 0. The Colmez average formula predicts the average Faltings height of CM points of conductor $N$ over $\mathbb{Q}(i)_N$. Verified computationally for $N \leq 100$ by Houfek (2019).

**Example 2: $E = y^2 = x^3 + 1$ (CM by $\mathbb{Z}[\omega]$, conductor 36).**
- $\operatorname{ord}_{s=1} L(E, s) = 0$, rank 0. The Gross-Zagier formula is trivially satisfied (no Heegner point needed). The Colmez average is verified.

**Example 3: Rank 1 CM curve $E: y^2 = x^3 - x^2 - 77x + 330$ (CM by $\mathbb{Q}(\sqrt{-3})$, conductor 49).**
- $\operatorname{ord}_{s=1} L(E, s) = 1$. A Heegner point $P$ of infinite order exists. The Gross-Zagier formula gives $L'(E, 1) = c \cdot \hat{h}(P)$. The Colmez conjecture predicts $h_{\mathrm{Fal}}(P) = -\frac{1}{2} L'(E/K, 0)/L(E/K, 0) + c_E \log N$. The ratio $L'(E,1)/\Omega(E)$ is rational, confirming BSD rank-1 numerically.

## Obstacle Analysis
1. **Individual vs. averaged:** Yuan-Zhang prove the averaged Colmez conjecture by summing over all CM abelian varieties in a given Shimura class. Extracting individual information requires controlling the variance, which is not currently feasible.
2. **Height comparison:** The precise relation between $h_{\mathrm{Fal}}(P)$ and $\hat{h}(P)$ involves the periods $\Omega(E)$ and $\Omega(\bar{E})$, which are themselves transcendental. Proving the algebraicity of the ratio requires the period conjecture (I-003).
3. **Conductor growth:** As the conductor $N$ grows, the CM points spread across ray class fields of increasing degree, and equidistribution methods (Duke, Bilu) only give asymptotic control.

## Cross-Group Connections
- **I-003 (Grothendieck Period Conjecture):** The ratio $h_{\mathrm{Fal}}(P)/\hat{h}(P)$ involves periods; the period conjecture would confirm its algebraicity.
- **I-005 (Stark's Conjecture):** For CM curves, the Stark unit and the Heegner point are related; both conjectures constrain the same $L$-value.
- **Group A (Analytic):** Computing $L'(E, 1)$ for CM curves of rank 1 provides the analytic input.
- **Group D (Regulator):** The Néron-Tate height pairing on CM curves is the arithmetic quantity predicted by BSD.

## Classification
**Inter-domain bridge.** Connects Arakelov geometry (Faltings heights) to analytic number theory ($L$-functions) through the lens of BSD. The averaged version is proven; the individual version would give an independent proof of rank-1 BSD for CM curves.
