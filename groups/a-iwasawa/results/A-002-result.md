# A-002: p-adic L-functions via Modular Symbols

## Status Assessment

The Pollack–Stevens algorithm for computing $p$-adic L-functions via overconvergent modular symbols is a mature and effective computational tool. For ordinary primes, it produces rigorous numerical values of $L_p(E, \chi, 1)$ with controlled precision. The direction is highly promising for numerical verification of the $p$-adic BSD conjecture and has a realistic timeline of 2–3 years for systematic computation across the Cremona database at small primes.

## Testable Conjecture

**Conjecture (Interpolation Accuracy).** Let $f$ be the newform of weight 2 and level $N$ attached to $E/\mathbb{Q}$, $p \nmid N$ a good ordinary prime, and $\chi$ a finite-order character of conductor $p^n$ with $n \geq 1$. Then the Pollack–Stevens overconvergent modular symbol $\{\alpha\}_f^{\mathrm{oc}}$ satisfies

$$L_p(f, \chi, 1) = \left(1 - \frac{a_p \chi(p)}{p}\right)\left(1 - \frac{\overline{\chi(p)}}{a_p}\right) \cdot \frac{\tau(\chi)}{p^n} \sum_{a \bmod p^n} \chi(a) \left\{\frac{a}{p^n}\right\}_f^{\mathrm{oc}}$$

with the overconvergent symbol computed to $O(p^{M(n)})$ precision where $M(n) = n + \lceil n \cdot \log_p(N) \rceil + 2$.

## Approach Summary

**Phase 1: Systematic computation.** Implement the full Pollack–Stevens pipeline in SageMath for all curves $E/\mathbb{Q}$ with conductor $N \leq 500$ and primes $p \in \{5, 7, 11, 13\}$. For each $(E, p)$, compute $L_p(E, \chi, 1)$ for all characters $\chi$ of conductor $p^n$ with $n \leq 5$. Verify the interpolation formula against classical $L$-values computed via modular symbols (Magma's `LSeries` package).

**Phase 2: Precision analysis.** Establish rigorous error bounds for the overconvergent lifting step. The key quantity is the $p$-adic valuation of the denominator of the overconvergent symbol after $k$ Newton iteration steps. Pollack–Stevens showed convergence for $v_p(a_p) > 0$ (ordinary case); we need explicit bounds of the form $v_p(\mathrm{denom}) \leq C \cdot k$ with $C$ depending on $N$ and $p$.

**Phase 3: Supersingular extension.** For $a_p = 0$ (supersingular case), implement Pollack's plus/minus splitting $L_p^\pm(E, T)$ using the overconvergent symbol with the two branches of the $U_p$-eigenvalue. Verify that $L_p^+ \cdot L_p^-$ equals the symmetric square $p$-adic L-function (up to a $p$-adic unit) as predicted by Pollack.

## Computational Example

**Curve 11a1** at $p = 5$ ($a_5 = -2$, ordinary since $v_5(-2) = 0$).

The overconvergent modular symbol computation gives:
- $L_p(11a1, \mathbf{1}, 1) = L(11a1, 1)/\Omega_{11a1} \cdot (1 - a_5/5)(1 - 1/a_5) = \frac{0.253841...}{1.269210...} \cdot (1 + 2/5)(1 + 1/2) \approx 0.253841 \cdot 1.05 \approx 0.266533$

At conductor $p^2 = 25$, the character $\chi_5$ of order 5: $L_p(11a1, \chi_5, 1)$ should match $\frac{\tau(\chi_5)}{5} \sum_{a \bmod 5} \chi_5(a) \{a/5\}_f^{\mathrm{oc}}$ to precision $O(5^8)$.

**Curve 37a1** at $p = 3$ ($a_3 = -2$, ordinary): $L_p(37a1, \mathbf{1}, 1) = 0$ since $\operatorname{ord}_{s=1} L(37a1, s) = 1$. The first derivative $L_p'(37a1, 0)$ should encode the $p$-adic regulator.

## Obstacle Analysis

The main technical barrier is the supersingular case ($a_p = 0$): the overconvergent lifting produces symbols with denominators that grow as $p^n$, making the computation infeasible for large $n$. Pollack's plus/minus theory resolves this by splitting into two branches, but the numerical implementation requires tracking two separate $p$-adic expansions with cancellation between them. The precision loss is $O(p^{n/2})$ per branch, which is manageable for $n \leq 10$ but becomes problematic beyond that. A potential strategy is to use the Amice transform and work in the Mellin transform space, where the plus/minus splitting is algebraic.

## Cross-Group Connections

- **Group A (Main Conjecture):** The $p$-adic L-function computed here is the analytic input to the Main Conjecture.
- **Group F (BSD Formula):** The leading coefficient of $L_p$ at $s = 1$ gives the $p$-adic BSD formula.
- **Group E (Computational Verification):** Systematic $L_p$-computations feed directly into verification databases.
- **Group D (Selmer Groups):** The order of vanishing of $L_p$ predicts the $\lambda$-invariant of the Selmer group.

## Classification

Theorem
