# A-001: Main Conjecture of Iwasawa Theory for Elliptic Curves over Q

## Status Assessment

The Main Conjecture is the central pillar of Iwasawa-theoretic approaches to BSD. Skinner–Urban (2014) proved it under auxiliary hypotheses (good ordinary reduction at $p \geq 5$, irreducible $E[p]$, non-Eisenstein condition, $\mu = 0$). The direction remains highly promising: removing these hypotheses is a major program with a realistic timeline of 5–10 years for the non-Eisenstein condition at $p \geq 5$, and significantly longer for $p = 2, 3$. Kato's divisibility is unconditional; the gap is the reverse divisibility.

## Testable Conjecture

**Conjecture (Strong Main Conjecture).** Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, $p$ an odd prime of good ordinary reduction with $E[p]$ irreducible. Then

$$\operatorname{char}_{\Lambda}\left(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee / (\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee)_{\mathrm{div}}\right) = \left(L_p(E, T)\right)$$

where $L_p(E, T) \in \mathbb{Z}_p[[T]]$ is the Mazur–Swinnerton-Dyer $p$-adic L-function satisfying the interpolation formula

$$L_p(E, \chi, 1) = \left(1 - \frac{a_p \chi(p)}{p}\right)\left(1 - \frac{\overline{\chi(p)}}{a_p}\right) \cdot \frac{L(E, \chi, 1)}{\Omega_E}$$

for all finite-order characters $\chi$ of $\Gamma = \operatorname{Gal}(\mathbb{Q}_\infty/\mathbb{Q})$.

## Approach Summary

**Phase 1: Computational verification.** For each prime $p \in \{5, 7, 11, 13\}$ and curves from the Cremona database with conductor $N \leq 500$, compute the $\Lambda$-module structure of $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)^\vee$ for layers $n = 0, 1, \ldots, 8$ using Magma's Selmer group machinery. Compare the characteristic polynomial of the finite-layer approximation with the Weierstrass polynomial of $L_p(E, T)$ truncated to the same precision.

**Phase 2: Remove the non-Eisenstein condition.** The key input is the Taylor–Wiles–Kisin patching method adapted to the Eisenstein case. One constructs a patched module $M_\infty$ over a deformation ring $R_\infty$ and a Hecke algebra $\mathbb{T}_\infty$, and shows that the support of $M_\infty$ on $\operatorname{Spec} R_\infty$ is cut out by the $p$-adic L-function. The Eisenstein case requires handling the reducibility locus in the deformation space.

**Phase 3: Extend to $p = 2, 3$.** The Ihara lemma input fails at these primes. One strategy is to replace the Shimura curve argument with a purely Galois-theoretic approach using the $p$-adic Langlands correspondence for $\mathrm{GL}_2(\mathbb{Q}_p)$, which is now well-understood for $p \geq 5$ and developing for $p = 2, 3$.

## Computational Example

**Curve 11a1** ($y^2 + y = x^3 - x^2 - 10x - 20$, conductor $N = 11$, rank 0).

At $p = 5$: $a_5 = -2$. The $5$-adic L-function $L_p(E, T) \in \mathbb{Z}_5[[T]]$ has Weierstrass polynomial $f(T) = T + 5$ (up to a 5-adic unit). The Selmer group $\operatorname{Sel}_{5^\infty}(E/\mathbb{Q}_\infty)^\vee$ should have $\lambda = 1$ and $\mu = 0$, consistent with $f(T)$. At layer $n = 0$: $|\operatorname{Sel}_{5^\infty}(E/\mathbb{Q})| = 1$ (trivial 5-part of Ш). At layer $n = 1$: predicted $|\operatorname{Sel}_{5^\infty}(E/\mathbb{Q}_1)[5]| = 5^1$.

**Curve 37a1** ($y^2 + y = x^3 - x$, conductor $N = 37$, rank 1).

At $p = 3$: $a_3 = -2$. The analytic rank is 1, so $L_p(E, T)$ vanishes to order 1 at $T = 0$. The Selmer group $\operatorname{Sel}_{3^\infty}(E/\mathbb{Q}_\infty)^\vee$ has $\lambda \geq 1$; the Main Conjecture predicts $\lambda = 1$ and the leading coefficient encodes the $p$-adic regulator.

## Obstacle Analysis

The primary obstacle is the non-Eisenstein condition in Skinner–Urban: one needs $a_p \not\equiv p + 1 \pmod{p^2}$. This fails for specific curves (e.g., $X_0(11)$ at $p = 5$ where $a_5 = -2$ and $-2 \not\equiv 6 \pmod{25}$, so this curve passes; but curves with $a_p = p + 1$ are common). Removing this requires either: (a) a direct argument showing the Eisenstein deformation ring quotient does not contribute extra Selmer classes, or (b) an alternative patching construction avoiding the Eisenstein locus entirely. Strategy (a) is pursued by Skinner–Urban via congruence modules but needs the Ihara lemma input.

## Cross-Group Connections

- **Group C (Euler Systems):** Kato's Euler system is the primary input for the divisibility $\operatorname{char}(\mathfrak{X}) \supseteq (L_p)$. Strengthening the Euler system bound directly improves the Main Conjecture.
- **Group D (Modular Symbols):** Numerical computation of $L_p(E, T)$ via Pollack–Stevens provides the analytic side of the conjecture.
- **Group F (BSD Formula):** The Main Conjecture is the $p$-adic input to the BSD formula; the leading coefficient of $L_p$ gives the $p$-part of BSD.
- **Group B (Heegner Points):** In the rank-1 case, Heegner points provide an alternative Euler system input via Gross–Zagier–Kolyvagin.

## Classification

Theorem (under Skinner–Urban hypotheses)
