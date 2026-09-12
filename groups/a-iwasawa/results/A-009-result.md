# A-009: Iwasawa Invariants and Growth of Selmer Groups

## Status Assessment

Computing Iwasawa invariants ($\mu$ and $\lambda$) for Selmer groups is both a theoretical and computational endeavor. The $\mu = 0$ conjecture is open for non-CM curves, but extensive numerical evidence supports it. The $\lambda$-invariant is computable from the $p$-adic L-function (under the Main Conjecture). The direction is actively progressing with a realistic timeline of 3–5 years for comprehensive computational databases and 10+ years for a proof of $\mu = 0$.

## Testable Conjecture

**Conjecture (Iwasawa Growth Formula).** Let $E/\mathbb{Q}$ have good ordinary reduction at $p$ with $E[p]$ irreducible. Then for all $n \gg 0$,

$$\dim_{\mathbb{F}_p} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p] = \lambda(E, p) \cdot n + \nu(E, p)$$

where $\lambda(E, p) = \operatorname{ord}_{T=0} L_p(E, T)$ (the $\lambda$-invariant of the $p$-adic L-function) and $\nu(E, p)$ is given by Greenberg's formula:

$$\nu = \lambda + \mu \cdot (p-1) \cdot p^{n_0 - 1} - \delta_p$$

with $\delta_p = \dim_{\mathbb{F}_p} E(\mathbb{Q}_p)[p] + \sum_{\ell | N, \ell \neq p} \dim_{\mathbb{F}_p} E(\mathbb{Q}_\ell)[p] - 1$ for $n_0 = 0$ when $\mu = 0$.

## Approach Summary

**Phase 1: Systematic computation of $\lambda$ from $L_p$.** For all curves $E/\mathbb{Q}$ with $N \leq 500$ and $p \in \{3, 5, 7, 11\}$, compute $L_p(E, T)$ via Pollack–Stevens (ordinary case) or Pollack plus/minus (supersingular case). Extract $\lambda = \deg \overline{L_p(E, T)}$ via Weierstrass preparation. Build a database of $(E, p, \lambda)$ triples.

**Phase 2: Finite-layer Selmer group computation.** For the same curves and primes, compute $|\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p]|$ for $n = 0, 1, \ldots, 8$ using Magma. Fit the Iwasawa formula and extract $\lambda$ and $\nu$. Compare with the $p$-adic L-function prediction.

**Phase 3: The $\mu = 0$ program.** The most promising approach to $\mu = 0$ is via the "Greenberg–Stevens method": show that $\mu(E, p) = 0$ for a dense set of primes $p$ (by the Ferrero–Washington theorem in the CM case and by density arguments in the non-CM case), then use the fact that $\mu$ is locally constant in families to extend to all primes. This requires control of the Selmer group in $p$-adic families (Hida families).

## Computational Example

**Curve 11a1** at $p = 3$:

$L_p(11a1, T) \in \mathbb{Z}_3[[T]]$: compute via Pollack–Stevens. $a_3 = -2$, ordinary. The Weierstrass polynomial: $f(T) = T - 3 \cdot (\text{unit})$? Actually for 11a1, $L(11a1, 1)/\Omega \approx 0.2538$, so $L_p(11a1, 0) \neq 0$ and $\lambda = 0$.

Growth: $\dim_{\mathbb{F}_3} \operatorname{Sel}_{3^\infty}(E/\mathbb{Q}_n)[3] = 0 \cdot n + \nu$. At $n = 0$: $|\operatorname{Sel}_{3^\infty}(E/\mathbb{Q})[3]| = 1$ (trivial), so $\nu = 0$.

**Curve 37a1** at $p = 3$: analytic rank 1, so $\lambda \geq 1$. Compute $L_p(37a1, T) = T \cdot g(T)$ with $g(0) \neq 0$. $\lambda = 1$. Growth: $\dim_{\mathbb{F}_3} \operatorname{Sel}_{3^\infty}(E/\mathbb{Q}_n)[3] = n + \nu$. At $n = 0$: $|\operatorname{Sel}_{3^\infty}(E/\mathbb{Q})[3]| = 1$, so $\nu = 0$. At $n = 1$: predicted $|\operatorname{Sel}_{3^\infty}(E/\mathbb{Q}_1)[3]| = 3^1 = 3$.

**Table for 11a1 at $p = 5$ ($\lambda = 1$):**

| $n$ | Predicted $\|\operatorname{Sel}[5]\|$ | Formula |
|---|---|---|
| 0 | 1 | $5^{0+\nu}$ |
| 1 | 5 | $5^{1+\nu}$ |
| 2 | 25 | $5^{2+\nu}$ |

## Obstacle Analysis

The main barrier is computational: computing Selmer groups over $\mathbb{Q}_n$ for large $n$ is expensive because the degree $[\mathbb{Q}_n : \mathbb{Q}] = p^n$ grows exponentially. Current Magma implementations can handle $n \leq 8$ for $p = 3$ and $n \leq 5$ for $p = 5$ for moderate-conductor curves. Beyond these ranges, one needs either: (a) more efficient algorithms (e.g., using the explicit description of $E(\mathbb{Q}_n) \otimes \mathbb{Q}_p/\mathbb{Z}_p$ via Kummer theory and the Cassels–Tate pairing), or (b) indirect methods (computing $\lambda$ from the $p$-adic L-function rather than from Selmer groups). Strategy (b) is the standard approach but requires the Main Conjecture as input.

## Cross-Group Connections

- **Group A (Main Conjecture):** $\lambda = \operatorname{ord}_{T=0} L_p$ is a consequence of the Main Conjecture.
- **Group D (p-adic L-functions):** Numerical computation of $L_p$ gives $\lambda$ directly.
- **Group E (Greenberg's Conjecture):** $\mu = 0$ is Greenberg's conjecture.
- **Group F (BSD Formula):** The growth formula controls $|\operatorname{III}(E/\mathbb{Q}_n)[p^\infty]|$.

## Classification

Theorem (growth formula: Iwasawa; $\mu = 0$: Conjecture for non-CM)
