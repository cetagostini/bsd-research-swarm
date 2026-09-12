# E-002 · p-adic Gross–Zagier Formula (Perrin-Riou, Nekovář)

## Direction ID and Title
E-002: p-adic Gross–Zagier formula relating $L_p'(E/K, 1)$ to the p-adic height of Heegner points.

## Status Assessment
**Ordinary case largely established; supersingular extension active.** Perrin-Riou (1987, 1992) proved the formula in the ordinary case. Nekovář (1993, 2006) extended the framework of p-adic height pairings to general settings. The supersingular case (Castella, Wan, Sprung) is ongoing.

## Testable Conjecture or Lemma

**Theorem (Perrin-Riou, p-adic Gross–Zagier, ordinary case).** Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$ with good ordinary reduction at an odd prime $p$. Let $K$ be an imaginary quadratic field with discriminant $D_K$ coprime to $N$ satisfying the Heegner hypothesis (every prime $\ell | N$ splits in $K$). Let $P_K \in E(K)$ be the Heegner point and $\hat{h}_p$ the canonical p-adic height associated to a splitting of the Hodge filtration. Then:

$$L_p'(E/K, 1) = \left(1 - \frac{a_p}{p} + \frac{1}{p}\right)^{-1} \cdot \frac{\hat{h}_p(P_K) \cdot c_E}{[\mathcal{O}_K : \mathbb{Z}[\mathfrak{f}]]}$$

where $c_E = \prod_{\ell | N} c_\ell$ involves Tamagawa factors, and the prefactor accounts for the Euler factor at $p$.

**Conjecture (Supersingular case, Sprung 2018).** When $E$ has supersingular reduction at $p$ ($a_p = 0$), there exists a plus/minus decomposition:
$$L_p'^{\pm}(E/K, 1) = \hat{h}_p^{\pm}(P_K^{\pm}) \cdot (\text{explicit correction factor})$$
where $\hat{h}_p^{\pm}$ are plus/minus p-adic heights and $P_K^{\pm}$ are projections of $P_K$.

## Approach Summary

1. **Heegner points:** The Heegner point $P_K \in E(K)$ is constructed via the modular parametrisation $\phi: X_0(N) \to E$ applied to CM points on $X_0(N)$ corresponding to the order $\mathcal{O}_K$.

2. **p-adic height pairing:** The Mazur–Tate canonical p-adic height $\hat{h}_p: E(\overline{\mathbb{Q}}) \to \mathbb{Q}_p$ is constructed via local p-adic Green's functions. The global height decomposes as $\hat{h}_p(P) = \sum_v \lambda_{p,v}(P)$ over all places $v$.

3. **Perrin-Riou's regulator map:** Uses the exponential map $\exp_p: \hat{E}(p\mathbb{Z}_p) \to p\mathbb{Z}_p$ and Coleman integration to express $L_p'(E/K, 1)$ as a p-adic logarithm of $P_K$ composed with the modular parametrisation.

4. **Euler system bridge:** Kolyvagin's Euler system of Heegner points controls the Selmer group; the p-adic formula is the p-adic shadow of the archimedean Gross–Zagier formula combined with the p-adic BSD conjecture.

## Computational Example

**Setup.** $E = 37a1$: $y^2 + y = x^3 - x$ (conductor $N = 37$, rank 1).

**Heegner hypothesis verification for $K = \mathbb{Q}(\sqrt{-3})$:** $N = 37$ is prime; $37 \equiv 1 \pmod{3}$, so $37$ splits in $K$. The discriminant $D_K = -3$ is coprime to $37$. ✓

**Heegner point computation.** The Heegner point $P_K$ on $E$ corresponding to the optimal embedding $\mathcal{O}_K \hookrightarrow M_0(37)$ generates $E(\mathbb{Q}) \cong \mathbb{Z}$ (the curve has rank 1 and trivial torsion).

**p-adic height at $p = 3$.** The curve $E = 37a1$ has $a_3 = 0$ (supersingular at $p = 3$). Using the plus/minus height:
- $\hat{h}_3^+(P_K)$: compute via Coleman integration on the formal group at $3$.
- $\hat{h}_3^-(P_K)$: uses the odd-component of the p-adic sigma function.

For the ordinary prime $p = 5$: $a_5 = 0$ (also supersingular). For $p = 7$: $a_7 = -4$ (ordinary, $|a_7|_7 = 1$). The ordinary p-adic Gross–Zagier formula applies at $p = 7$:
$$L_p'(E/K, 1) \stackrel{?}{=} \left(1 + \frac{4}{7} + \frac{1}{7}\right)^{-1} \cdot \hat{h}_7(P_K) = \frac{7}{12} \cdot \hat{h}_7(P_K)$$

**Numerical check (rank 1):** Since $P_K$ generates $E(\mathbb{Q})$, the p-adic regulator $\text{Reg}_7(E) = \hat{h}_7(P_K)$, and $L_p'(E, 1) / 1!$ should equal $\hat{h}_7(P_K) \cdot |\Sha[7^\infty]| \cdot \prod c_\ell / |E(\mathbb{Q})_{\text{tors}}|^2$ by p-adic BSD.

## Obstacle Analysis

1. **Non-explicit constants:** Perrin-Riou's formula involves the Coleman logarithm composed with the modular parametrisation, introducing constants that depend on the choice of local parameter at $p$ and the splitting of the Hodge filtration.

2. **Supersingular primes:** When $a_p = 0$, the ordinary p-adic L-function does not exist. The plus/minus decomposition (Pollack) provides a substitute, but the resulting formula is more complex and involves plus/minus regulators.

3. **Height normalisation:** The p-adic height $\hat{h}_p$ depends on the choice of splitting $\sigma: H^1_{\text{dR}}(E) \to F^1 H^1_{\text{dR}}(E)$. Different choices give heights differing by a bounded factor; the "canonical" choice is fixed by the Mazur–Tate convention but is not always computationally optimal.

4. **Multiple Heegner points:** For conductors with multiple prime factors, the Heegner point depends on the choice of factorisation $N = N^+ N^-$, and the formula must account for all contributions.

## Cross-Group Connections

- **Group A (Classical BSD):** The p-adic Gross–Zagier formula is the p-adic analogue of the archimedean formula $L'(E/K, 1) = c \cdot \hat{h}(P_K)$ (Gross–Zagier 1986).
- **Group B (Heegner Points):** Direct dependency: the Heegner point $P_K$ and its archimedean height are computed in Group B; the p-adic formula refines this.
- **Group C (Iwasawa Theory):** The formula implies $\text{ord}_{s=1} L_p(E, s) = \text{rank}(E(\mathbb{Q}))$ for rank 1, which is the rank-1 case of the Iwasawa main conjecture.
- **Group D (Euler Systems):** Kolyvagin's Euler system argument combined with p-adic Gross–Zagier gives the full p-adic BSD in rank $\leq 1$.

## Classification
**Heegner points / p-adic heights.** Core analytic input for p-adic BSD in rank 1.
