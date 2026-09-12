# E-003 · Mazur–Tate–Teitelbaum L-invariant and BSD

## Direction ID and Title
E-003: The Mazur–Tate–Teitelbaum (MTT) $\mathcal{L}$-invariant $\mathcal{L}_p(E)$ and its role in p-adic BSD with exceptional zeros.

## Status Assessment
**Established for split multiplicative reduction; active for good ordinary and other cases.** Teitelbaum (1992) proved $\mathcal{L}_p(E) = 2\log_p(q_E)/\text{ord}_p(q_E)$ for split multiplicative reduction. The general good ordinary case remains open.

## Testable Conjecture or Lemma

**Theorem (Teitelbaum, 1992).** Let $E/\mathbb{Q}$ be an elliptic curve with split multiplicative reduction at a prime $p$, with Tate period $q_E \in p\mathbb{Z}_p$. Then:
$$\mathcal{L}_p(E) = \frac{2\log_p(q_E)}{\text{ord}_p(q_E)}$$
and $\mathcal{L}_p(E) \neq 0$ (since $q_E$ is not a root of unity in $\mathbb{Q}_p^\times$).

**Theorem (MTT p-adic BSD with exceptional zero).** Under the same hypotheses:
$$L_p'(E, 1) = \mathcal{L}_p(E) \cdot \frac{L(E, 1)}{\Omega_E^+} \cdot \left(1 - \frac{1}{a_p}\right)^{-1}$$
where the rightmost factor corrects for the vanished interpolation factor.

**Corollary.** The p-adic BSD formula becomes:
$$L_p'(E, 1) = \mathcal{L}_p(E) \cdot \frac{|\Sha(E/\mathbb{Q})| \cdot \prod_\ell c_\ell}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

## Approach Summary

1. **Tate uniformisation:** $E(\mathbb{Q}_p) \cong \mathbb{Q}_p^\times / q_E^{\mathbb{Z}}$ via the Tate curve. Every point $P \in E(\mathbb{Q}_p)$ lifts to $\tilde{P} \in \mathbb{Q}_p^\times$, and $\text{ord}_p(\tilde{P})$ gives the local parameter.

2. **p-adic L-function construction:** Via modular symbols, $L_p(E, s)$ is constructed as a p-adic integral $\int_{\mathbb{Z}_p^\times} x^{s-1} d\mu_f$ where $\mu_f$ is the modular symbol measure. At $s = 1$, the interpolation factor $(1 - a_p/p)$ vanishes when $a_p = 1$ (split multiplicative).

3. **Exceptional zero analysis:** Since $a_p = 1$ for split multiplicative reduction, the Euler factor $(1 - 1/a_p) = 0$, forcing $L_p(E, 1) = 0$. The derivative $L_p'(E, 1)$ is computed by differentiating the interpolation formula with respect to $s$.

4. **Tate period logarithm:** The key identity $\mathcal{L}_p(E) = 2\log_p(q_E)/\text{ord}_p(q_E)$ arises from comparing the p-adic L-function derivative with the p-adic logarithm on the Tate curve.

## Computational Example

**Curve: $E = 11a1$** ($y^2 + y = x^3 - x^2 - 10x - 20$, conductor 11).

At $p = 11$: The curve has split multiplicative reduction at $p = 11$ (since the discriminant $\Delta = -11^5$ and $c_{11} = 1$). The Tate period is $q_E = -11$ (up to a 11-adic unit).

**Computation of $\mathcal{L}_{11}(E)$:**
- $\text{ord}_{11}(q_E) = \text{ord}_{11}(-11) = 1$
- $\log_{11}(-11) = \log_{11}(11) + \log_{11}(-1) = \log_{11}(11)$ (since $\log_{11}(-1) = 0$ as $(-1)^2 = 1$)
- By the p-adic logarithm: $\log_{11}(11) = \log_{11}(1 + 10) = 10 - 10^2/2 + 10^3/3 - \cdots$ in $\mathbb{Q}_{11}$
- More precisely, $\log_{11}(11) = \log_p(p)$ which in normalised p-adic valuation satisfies $v_{11}(\log_{11}(11)) = 1/(11-1) = 1/10$ (Iwasawa normalisation)
- $\mathcal{L}_{11}(E) = 2\log_{11}(-11) / 1 = 2\log_{11}(11)$

**Numerical value:** $\mathcal{L}_{11}(E) \approx 2 \cdot 10 \cdot (1 - 10/2 + \cdots) \pmod{11^3}$. Working to 11-adic precision $O(11^5)$: $\log_{11}(11) \equiv 10 - 50 + 1000/3 - \cdots \pmod{11^5}$.

**Verification of MTT formula:** $L(E, 1) / \Omega_E^+ \approx 0.2 = 1/5$. The exceptional zero factor $(1 - 1/a_{11})^{-1}$ where $a_{11} = 1$: this factor is infinite (the zero), so one takes the derivative. The MTT conjecture asserts $L_{11}'(E, 1) = \mathcal{L}_{11}(E) \cdot L(E, 1)/\Omega_E^+$.

**Additional example: $E = 14a1$** ($y^2 + xy + y = x^3 + 4x - 6$, conductor 14).
At $p = 2$: $E$ has split multiplicative reduction ($a_2 = 1$). Tate period $q_E \in 2\mathbb{Z}_2$. $\mathcal{L}_2(E) = 2\log_2(q_E)/\text{ord}_2(q_E)$.

## Obstacle Analysis

1. **Non-split multiplicative reduction:** When $a_p = -1$ (non-split), the Tate uniformisation gives $E(\mathbb{Q}_p) \cong (K^\times / q_E^{\mathbb{Z}})$ for the unramified quadratic extension $K/\mathbb{Q}_p$, and the formula for $\mathcal{L}_p$ requires modification. Venerucci (2016) addressed this case.

2. **Good ordinary reduction with $a_p \equiv 1$:** When $E$ has good ordinary reduction but $a_p = 1$ (or $a_p \equiv 1 \pmod{p^N}$ for large $N$), the Tate uniformisation is unavailable. The correct $\mathcal{L}_p(E)$ requires p-adic logarithms of Heegner points or Shimura curve parametrisations.

3. **Multiple primes:** When $E$ has split multiplicative reduction at several primes $p_1, \ldots, p_k$, the exceptional zero has order $k$, and $\mathcal{L}_{p_1, \ldots, p_k}$ is a more complex invariant involving mixed Tate periods.

4. **Non-vanishing:** The non-vanishing of $\mathcal{L}_p(E)$ (equivalent to $q_E$ not being a p-adic root of unity) is clear for the Tate period but requires argument in the good ordinary case.

## Cross-Group Connections

- **Group A (Classical BSD):** The MTT formula $L_p'(E, 1) = \mathcal{L}_p(E) \cdot L(E,1)/\Omega_E$ is the p-adic refinement of the classical BSD formula when the p-adic L-function has a trivial zero.
- **Group C (Iwasawa Theory):** Greenberg (1994) gave the Iwasawa-theoretic interpretation: the exceptional zero corresponds to a trivial zero in the characteristic ideal of the Selmer group over the $\mathbb{Z}_p$-extension.
- **Group E (E-010):** Greenberg's generalised $\mathcal{L}$-invariant and Colmez's representation-theoretic $\mathcal{L}$-invariant must coincide with the MTT $\mathcal{L}_p(E)$ (proven for split multiplicative).

## Classification
**L-invariants / exceptional zeros.** The foundational case of the exceptional zero phenomenon.
