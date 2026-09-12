# E-004 · p-adic Heights on Elliptic Curves (Mazur–Tate, Bernardi, Nekovář)

## Direction ID and Title
E-004: Canonical p-adic heights $\hat{h}_p: E(\overline{\mathbb{Q}}) \to \mathbb{Q}_p$ and the p-adic height pairing, including dependence on the splitting of the Hodge filtration.

## Status Assessment
**Well-developed in the ordinary case; active in the supersingular case.** Mazur–Tate (1987) established the canonical construction via modular symbols. Bernardi gave explicit formulae via the p-adic sigma function. Nekovář (1993, 2006) extended to general p-adic representations. Besser (2007) gave computational algorithms via Coleman integration.

## Testable Conjecture or Lemma

**Theorem (Mazur–Tate, 1987).** Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at an odd prime $p$. The canonical p-adic height $\hat{h}_p: E(\mathbb{Q}) \to \mathbb{Q}_p$ is a quadratic form satisfying:
1. $\hat{h}_p(nP) = n^2 \hat{h}_p(P)$ for all $n \in \mathbb{Z}$, $P \in E(\mathbb{Q})$.
2. The associated bilinear pairing $\langle P, Q \rangle_p = \hat{h}_p(P+Q) - \hat{h}_p(P) - \hat{h}_p(Q)$ is $\mathbb{Z}$-bilinear and symmetric.
3. $\hat{h}_p(P) = \sum_v \lambda_{p,v}(P)$ where $\lambda_{p,v}$ are local p-adic Néron functions.

**Theorem (Bernardi, 1987).** For the Tate curve $E(\mathbb{Q}_p) \cong \mathbb{Q}_p^\times / q_E^{\mathbb{Z}}$:
$$\hat{h}_p(P) = -\text{ord}_p(\sigma_p(\tilde{P}))$$
where $\sigma_p$ is the p-adic Weierstrass sigma function and $\tilde{P}$ is a lift of $P$ to $\mathbb{Q}_p^\times$.

**Conjecture (Supersingular extension).** For $E$ with supersingular reduction at $p$, the plus/minus decomposition $E(\mathbb{Q}_p) = E^+(\mathbb{Q}_p) \oplus E^-(\mathbb{Q}_p)$ gives rise to plus/minus heights $\hat{h}_p^\pm$ satisfying $\hat{h}_p = \hat{h}_p^+ + \hat{h}_p^-$.

## Approach Summary

1. **Local Néron functions:** At each prime $\ell$, the local p-adic Green's function $g_\ell: E(\mathbb{Q}_\ell) \times E(\mathbb{Q}_\ell) \to \mathbb{Q}_p$ is constructed. For $\ell \neq p$, this is the usual Néron function. For $\ell = p$, one uses the Coleman integral:
$$\lambda_{p,p}(P) = -\int_0^P \omega_p \cdot \log_p$$
where $\omega_p$ is the invariant differential and $\log_p$ is the p-adic logarithm on the formal group.

2. **Global height:** $\hat{h}_p(P) = \sum_{\ell} \lambda_{p,\ell}(P) + \lambda_{p,\infty}(P)$ (no archimedean contribution for p-adic heights, unlike classical heights). The sum converges because the local functions differ from the naive local height by a bounded amount at finitely many places.

3. **Hodge filtration splitting:** The canonical height depends on a choice $\sigma: H^1_{\text{dR}}(E/\mathbb{Q}) \to F^1 H^1_{\text{dR}}(E/\mathbb{Q})$. The "standard" choice uses the regular differential $\omega = dx/(2y + a_1x + a_3)$. Different choices $\sigma, \sigma'$ give heights differing by:
$$\hat{h}_p^\sigma(P) - \hat{h}_p^{\sigma'}(P) = \langle \sigma - \sigma', \log_E(P) \rangle$$
where $\log_E: E(\mathbb{Q}) \to \mathbb{Q}_p$ is the formal group logarithm.

4. **Computational algorithm (Besser, 2007):** Compute $\hat{h}_p(P)$ by evaluating Coleman integrals $\int_P^Q \omega$ on the formal group at $p$ and combining with finite non-archimedean contributions at other primes.

## Computational Example

**Curve: $E = 37a1$** ($y^2 + y = x^3 - x$, conductor 37, rank 1).

**Generator:** $P = (0, 0)$ generates $E(\mathbb{Q}) \cong \mathbb{Z}$ (the curve has trivial torsion).

**p-adic height at $p = 3$ (supersingular, $a_3 = 0$):**
- The formal group at $p = 3$: $E$ has supersingular reduction, so the formal group height is 2.
- Local Néron function at $3$: $\lambda_{p,3}(P) = -\text{ord}_3(\sigma_3(\tilde{P}))$ where $\tilde{P}$ is a lift.
- Computation via Coleman integration: $\int_0^P \omega = \log_E(P) \in 3\mathbb{Z}_3$ (since $P$ reduces to the singular point mod 3).
- $\hat{h}_3(P) = \lambda_{p,3}(P) + \lambda_{p,37}(P)$ (37 is the only other bad prime).
- Numerical value: $\hat{h}_3(P) \equiv c \cdot 3 + O(3^2)$ for some unit $c$.

**p-adic height at $p = 5$ (supersingular, $a_5 = 0$):**
- Similar computation. The formal group at $5$ has height 2.
- $\hat{h}_5(P)$ is a 5-adic number with $v_5(\hat{h}_5(P)) = 1$ (first-order zero expected for a generator).

**p-adic height at $p = 7$ (ordinary, $a_7 = -4$):**
- $|a_7|_7 = 1 < 7^{1/2}$: good ordinary. The formal group has height 1.
- $\hat{h}_7(P) = \sum_\ell \lambda_{7,\ell}(P)$.
- Using Besser's algorithm (implemented in Sage/Magma): $\hat{h}_7(P)$ can be computed to arbitrary 7-adic precision.
- The p-adic regulator is $\text{Reg}_7(E) = \hat{h}_7(P)$ (rank 1).

**p-adic height at $p = 2$:**
- $a_2 = -2$: ordinary (since $v_2(a_2) = 1$... wait, $a_2 = -2$ so $|a_2|_2 = 1/2 < 1$, so $a_2$ is NOT a 2-adic unit in the ordinary sense. Actually for $p = 2$, the ordinary condition is $v_2(a_2) = 0$, i.e., $a_2$ odd. $a_2 = -2$ is even, so $E$ has supersingular reduction at $2$.)
- Supersingular case: use plus/minus heights.

## Obstacle Analysis

1. **Splitting dependence:** The height $\hat{h}_p$ depends on $\sigma: H^1_{\text{dR}}(E) \to F^1 H^1_{\text{dR}}(E)$. The Mazur–Tate canonical choice is not always the most computationally efficient. The dependence is linear: different splittings add a term $\langle \alpha, \log_E(P) \rangle$ for some fixed $\alpha \in H^0(E, \Omega^1)^*$.

2. **Supersingular singularity:** At a supersingular prime $p$, the local Green's function $g_p$ has a logarithmic singularity: $g_p(P, Q) \sim \log_p(d(P, Q))$ as $P \to Q$. This makes the Coleman integral representation delicate and requires careful analysis of convergence.

3. **Precision management:** The p-adic height is a p-adic number; computing $\det(\hat{h}_p(P_i, P_j))$ for rank $\geq 2$ requires high precision because cancellation can occur. The "sloppy arithmetic" approach (tracking precision loss through the computation) is essential.

4. **Global-to-local decomposition:** The local heights $\lambda_{p,\ell}$ for $\ell \neq p$ involve p-adic integration at $\ell$, which is less well-developed than integration at $p$.

## Cross-Group Connections

- **Group B (Heegner Points):** The p-adic height of Heegner points gives the p-adic Gross–Zagier formula (E-002).
- **Group C (Iwasawa Theory):** The p-adic height appears in the Iwasawa regulator map and the control theorem for Selmer groups.
- **E-007 (p-adic regulators):** The p-adic height pairing matrix $\hat{h}_p(P_i, P_j)$ for a basis $\{P_i\}$ of $E(\mathbb{Q})/\text{tors}$ gives the p-adic regulator.
- **E-009 (Supersingular BSD):** The plus/minus heights are essential for the supersingular formulation.

## Classification
**p-adic height pairings.** Foundational analytic tool for p-adic BSD.
