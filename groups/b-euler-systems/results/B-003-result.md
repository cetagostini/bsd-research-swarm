# B-003: Darmon Cycles and Stark-Heegner Points

## Direction ID and Title
B-003 — Darmon Cycles and Stark-Heegner Points

## Status Assessment
Darmon cycles are $p$-adically defined cohomology classes $\mathfrak{z}_K \in H^1(\mathbb{Q}, T_\ell(E))$ whose images under the local period map yield Stark-Heegner points $P_K \in E(\mathbb{Q}_p)$. Betina-Dimitrov (2021) proved their existence in the cohomology of certain unitary Shimura varieties. The norm relations at primes $\ell \nmid Np$ remain unproven — the conjectural Shimura curve construction that would yield compatibility has not been realized. Computational evidence supports the conjecture that $\hat{h}(P_K)$ matches the Gross-Zagier-type formula involving $L'(E/K, 1)$.

## Testable Conjecture or Lemma

**Conjecture B-003.** Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N = pM$ with $p$ prime, and $K = \mathbb{Q}(\sqrt{-D})$ an imaginary quadratic field with $(-D, N) = 1$ satisfying the Heegner hypothesis. Let $\mathfrak{z}_K \in H^1(\mathbb{Q}, T_p(E))$ be the Darmon cycle defined via $p$-adic integration on $\mathbb{P}^1(\mathbb{Q})$:

$$P_K = \int_{\alpha_K}^{\beta_K} \omega_f \in E(\mathbb{Q}_p)$$

where $\alpha_K, \beta_K$ are roots of $x^2 + bx + c = 0$ with $b^2 - 4c = -D$. Then:

(a) The global height satisfies $\hat{h}_{\mathrm{NT}}(P_K) = \frac{L'(E/K, 1)}{\Omega_E^+ \Omega_E^-} \cdot \frac{|\operatorname{III}(E/K)| \cdot \prod c_v}{|E(K)_{\mathrm{tors}}|^2 \cdot [E(K): \mathbb{Z}]^2}$.

(b) For primes $\ell \nmid Np$ with $\ell \equiv 1 \pmod{p}$ and $\operatorname{Frob}_\ell$ of order $p-1$ on $E[p]$:

$$\operatorname{Cor}_{K(\ell)/K}(P_{K(\ell)}) = a_\ell \cdot P_K - \left(1 + \ell - a_\ell\right) \cdot P_K^{\sigma_\ell}$$

where $\sigma_\ell \in \operatorname{Gal}(K(\ell)/K)$ is the Frobenius.

## Approach Summary

The Darmon cycle construction proceeds by choosing a geodesic in the Bruhat-Tits tree $\mathcal{T}_p$ of $PGL_2(\mathbb{Q}_p)$ connecting the two roots $\alpha_K, \beta_K \in \mathbb{P}^1(\mathbb{Q}_p)$. The $p$-adic integral $\int_{\alpha_K}^{\beta_K} \omega_f$ is defined using the Manin-Drinfeld theory of $p$-adic integration on $X_0(N)$, where the integrand is the differential associated to the newform $f$ of weight 2 corresponding to $E$.

For the norm compatibility (part (b)), the approach requires lifting the $p$-adic point $P_K$ to a global class in $H^1(\mathbb{Q}, T_\ell(E))$. The conjectural construction uses Shimura curves $X_D$ parametrizing abelian surfaces with quaternionic multiplication: if $P_K$ lifts to a point on $X_D(\mathbb{Q}_p)$, the Hecke correspondence $T_\ell$ on $X_D$ would produce the norm relation. Betina-Dimitrov's existence result provides the local-to-global bridge but does not yet yield the Hecke action.

The computational verification uses $p$-adic integration algorithms (Balakrishnan-Bradshaw-Kedlaya) to compute $P_K$ to high precision and compares $\hat{h}_{\mathrm{NT}}(P_K)$ against $L'(E/K, 1)$ computed via Dokchitser's method.

## Computational Example

- **$E = $ 11a1**: $y^2 + y = x^3 - x^2 - 10x - 20$, conductor 11. Take $p = 11$ (split multiplicative reduction). For $K = \mathbb{Q}(\sqrt{-7})$ (Heegner hypothesis satisfied: $(-7, 11) = 1$): compute $P_K \in E(\mathbb{Q}_{11})$ via $11$-adic integration. Verify $\hat{h}_{11}(P_K) = L'(E/K, 1) / \Omega_E$ up to the expected correction factors.
- **$E = $ 37a1**: conductor 37. $K = \mathbb{Q}(\sqrt{-3})$. $p = 37$. Compute $P_K$ and verify the Gross-Zagier-type formula. This is a rank-1 curve, so $L'(E, 1) \neq 0$ and $P_K$ should be a generator of $E(\mathbb{Q}) \otimes \mathbb{Q}$.
- **$E = $ 43a1**: conductor 43. Test the norm relation at $\ell = 5$ (split in $K = \mathbb{Q}(\sqrt{-7})$, $5 \equiv 1 \pmod{4}$, but need $5 \equiv 1 \pmod{p}$ — adjust $p$ or $\ell$ accordingly).

## Obstacle Analysis

The norm relation (b) is the critical missing piece. The fundamental difficulty is that Stark-Heegner points are defined $p$-adically via integration on $\mathbb{P}^1(\mathbb{Q})$, not via algebraic cycles on a global algebraic variety. Without a global geometric interpretation (a Shimura curve parametrization), the Hecke action at auxiliary primes $\ell$ cannot be defined. The geodesic in $\mathcal{T}_p$ depends on the prime $p$, and changing $\ell$ changes the geodesic in a way that is not controlled by the Hecke correspondence. Greenberg's result that $P_K$ is global for split multiplicative reduction at $p$ is a necessary but not sufficient condition.

## Cross-Group Connections
- **Group A (BSD Formula)**: The height formula (a) directly encodes the BSD leading term for $E/K$.
- **Group C (Heegner Points)**: When $K$ satisfies the classical Heegner hypothesis for a Shimura curve, Darmon points should coincide with actual Heegner points.
- **Group D (Gross-Zagier)**: The height formula (a) is a $p$-adic analogue of Gross-Zagier.

## Classification
Conjecture (Darmon cycles as Euler system); Partial Result (existence of the points)
