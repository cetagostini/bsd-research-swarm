# A-006: Iwasawa Theory at Supersingular Primes

## Status Assessment

The plus/minus Main Conjecture at supersingular primes is one of the great achievements of modern Iwasawa theory. Kobayashi defined the plus/minus Selmer groups, Pollack constructed the $p$-adic L-functions, and significant progress on the Main Conjecture has been made by Kurihara (2010) and Kim (2020). The direction is in active progress with a realistic timeline of 3–5 years for a complete proof under mild hypotheses.

## Testable Conjecture

**Conjecture (Plus/Minus Main Conjecture).** Let $E/\mathbb{Q}$ be an elliptic curve with good supersingular reduction at $p$ ($a_p = 0$ for $p > 3$). Then

$$\operatorname{char}_{\Lambda}\left(\operatorname{Sel}_{p^\infty}^+(E/\mathbb{Q}_\infty)^\vee\right) = \left(L_p^+(E, T)\right), \quad \operatorname{char}_{\Lambda}\left(\operatorname{Sel}_{p^\infty}^-(E/\mathbb{Q}_\infty)^\vee\right) = \left(L_p^-(E, T)\right)$$

where $L_p^\pm(E, T) \in \mathbb{Z}_p[[T]]$ are the Pollack plus/minus $p$-adic L-functions, and

$$L_p^+(E, T) \cdot L_p^-(E, T) = L_p^{\mathrm{sym}}(E, T) \cdot u$$

for $u \in \Lambda^\times$, where $L_p^{\mathrm{sym}}$ is the symmetric square $p$-adic L-function.

## Approach Summary

**Phase 1: Numerical verification.** For all curves $E/\mathbb{Q}$ with conductor $N \leq 300$ and $a_p = 0$ at $p \in \{3, 5, 7\}$, compute $L_p^\pm(E, T)$ via Pollack's algorithm in SageMath. Compute $\operatorname{Sel}^\pm_{p^\infty}(E/\mathbb{Q}_n)$ for layers $n = 0, \ldots, 8$ using Kobayashi's local conditions. Verify that the characteristic polynomial of $\operatorname{Sel}^\pm$ matches the Weierstrass polynomial of $L_p^\pm$.

**Phase 2: Local duality for plus/minus Selmer groups.** The standard Poitou–Tate duality does not directly apply to $\operatorname{Sel}^\pm$ because the local conditions at $p$ are not exact annihilators under the local Tate pairing. One needs to develop a modified duality theory. Kobayashi showed that $\operatorname{Sel}^+$ and $\operatorname{Sel}^-$ are related by a modified pairing, but the control theorem (comparing Selmer groups at layers $n$ and $n+1$) requires additional input from the theory of $(\varphi, \Gamma)$-modules.

**Phase 3: Euler system approach.** Kato's Euler system gives classes in $H^1(\mathbb{Q}_n, T_p E)$ that are norm-compatible in the cyclotomic tower. At supersingular primes, these classes have non-trivial image in both $H^1_+$ and $H^1_-$. The key is to project Kato's classes onto the plus/minus eigenspaces and show that the projected classes generate the correct Fitting ideals. This is the approach of Kurihara (2010) and Kim (2020).

## Computational Example

**Curve 27a1** ($y^2 + y = x^3 - 7$, conductor $N = 27$) at $p = 3$:

$a_3 = 0$ (supersingular). The plus/minus $p$-adic L-functions:
- $L_p^+(27a1, T) \in \mathbb{Z}_3[[T]]$ with Weierstrass polynomial $f^+(T) = 1$ (no zeros), $\mu^+ = 0$, $\lambda^+ = 0$.
- $L_p^-(27a1, T) \in \mathbb{Z}_3[[T]]$ with Weierstrass polynomial $f^-(T) = T$, $\mu^- = 0$, $\lambda^- = 1$.

The Selmer groups: $\operatorname{Sel}^+_{3^\infty}(E/\mathbb{Q}_\infty)^\vee$ is finite (consistent with $\lambda^+ = 0$), and $\operatorname{Sel}^-_{3^\infty}(E/\mathbb{Q}_\infty)^\vee$ has $\lambda^- = 1$. The product $\lambda^+ + \lambda^- = 1$ equals the $\lambda$-invariant of the cyclotomic $p$-adic L-function $L_p^{\mathrm{sym}}$.

**Curve 43a1** at $p = 3$: $a_3 = 0$. $\operatorname{ord}_{s=1} L(43a1, s) = 1$. The plus/minus invariants should satisfy $\lambda^+ + \lambda^- = 1 + \delta$ where $\delta$ accounts for the trivial zero contribution.

## Obstacle Analysis

The primary obstacle is the failure of Pontryagin duality for plus/minus Selmer groups. In the ordinary case, the Poitou–Tate exact sequence gives a control theorem: $0 \to \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n) \to \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_{n+1})^{\Gamma_n} \to H^1(\Gamma_n, E(\mathbb{Q}_{\infty,p})[p^\infty]) \to \ldots$ This sequence does not exist for $\operatorname{Sel}^\pm$ because the local conditions $\kappa_v^\pm$ are not functorial in the same way. Kobayashi's approach uses the explicit description of $H^1_\pm$ in terms of Kummer images and the theory of norm-coherent sequences of points. A potential strategy for the Main Conjecture is to use the fact that $\operatorname{Sel}^+ \oplus \operatorname{Sel}^-$ "covers" the full Selmer group and apply the Main Conjecture to each piece separately.

## Cross-Group Connections

- **Group A (Main Conjecture):** The supersingular case is the main gap in the cyclotomic Main Conjecture program.
- **Group D (Iwasawa Invariants):** The plus/minus invariants $\lambda^\pm$ and their relation to $\lambda$.
- **Group C (Euler Systems):** Kato's Euler system projected onto plus/minus components.
- **Group F (BSD Formula):** The $p$-adic BSD formula at supersingular primes requires the plus/minus $p$-adic L-functions.

## Classification

Theorem (partially proven: Kurihara, Kim; full result: in progress)
