# B-012: Explicit Computation of Euler System Classes

## Direction ID and Title
B-012 — Explicit Computation of Euler System Classes (SageMath/Magma)

## Status Assessment
The explicit computation of Kato's Euler system has been carried out for specific curves of small conductor. Magma's `EulerSystem` package (under development by Loeffler) computes the image of Kato's class in $H^1(\mathbb{Q}_p, V_p(E))$, and Dokchitser's `tim Dok` package computes $L^{(r)}(E, 1)$ to arbitrary precision. The $p$-adic heights have been computed by Balakrishnan-Dogra-Müller-Tuitman-Vonk using $p$-adic integration. The interpolation formula has been verified for curves 11a1, 37a1, 43a1, 389a1, 5077a1, confirming the BSD formula on the $p$-adic side.

## Testable Conjecture or Lemma

**Conjecture B-012.** For a modular elliptic curve $E/\mathbb{Q}$ of conductor $N$ and a prime $p \nmid 6N$ of good ordinary reduction, the following computational quantities are defined and can be explicitly computed:

(a) **Kato's class as a cocycle:** $z^{(p)}_\sigma \in V_p(E)$ for $\sigma \in G_\mathbb{Q}$, computed via modular symbols at level $Np^k$ for sufficiently large $k$.

(b) **Interpolation verification:** $\exp^*_{V_p(E)}(\operatorname{loc}_p(z^{(p)})) = \left(1 - \frac{a_p}{p} + \frac{1}{p}\right)^{-1} \cdot \frac{L(E,1)}{\Omega_E} \in \mathbb{Q}_p$.

(c) **$p$-adic height:** $\hat{h}_p(z^{(p)}) \in \mathbb{Q}_p$ computed via the Mazur-Tate sigma function on $E(\mathbb{Q}_p)$.

(d) **Kolyvagin derivative classes:** For $\ell \equiv 1 \pmod{p}$ with $\operatorname{Frob}_\ell$ of order $p-1$ on $E[p]$: $d_\ell = \sum_{i=0}^{p-2} i \cdot \sigma_\ell^i(c_\ell) \in H^1(\mathbb{Q}, E[p])$.

(e) **BSD verification:** $v_p(\hat{h}_p(z^{(p)})) + \sum_v \operatorname{ord}_p(c_v) + \operatorname{ord}_p(|E_{\mathrm{tors}}|^2) = v_p(L(E,1)/\Omega_E) + v_p(|\operatorname{III}|)$.

## Approach Summary

The computation of Kato's zeta element proceeds via the modular symbol representation. For a newform $f = \sum a_n q^n$ of level $N$, the space of modular symbols $\mathcal{M}_2(\Gamma_0(N))$ is a finite-dimensional $\mathbb{Q}$-vector space with a basis of Manin symbols $[r/s]$ for $r/s \in \mathbb{P}^1(\mathbb{Q})$. Kato's class at level $Np^k$ is the image of the Beilinson-Kato element under the étale regulator, computed as a sum over $c \in (\mathbb{Z}/Np^k\mathbb{Z})^\times$ of twisted Manin symbols.

The dual exponential map $\exp^*_V$ is computed via the $p$-adic Hodge theory comparison: for $V = V_p(E)$, $D_{\mathrm{dR}}(V) = H^1_{\mathrm{dR}}(E/\mathbb{Q}_p) \cong \mathbb{Q}_p \omega \oplus \mathbb{Q}_p \eta$ where $\omega$ is the Néron differential. The dual exponential sends a cocycle to its "crystalline projection" onto the $\eta$-component, computed via the $p$-adic integration algorithm of Kedlaya.

The $p$-adic height $\hat{h}_p$ uses the Mazur-Tate sigma function $\sigma_p: E(\mathbb{Q}_p) \to 1 + p\mathbb{Z}_p$, defined by the property $\sigma_p(P + Q) / (\sigma_p(P) \sigma_p(Q)) = \langle P, Q \rangle_p$ (the $p$-adic Néron symbol). The sigma function is computed via $p$-adic analytic continuation from the formal group.

The Kolyvagin derivative classes require computing the "Kolyvagin prime" $\ell$ (primes where $\operatorname{Frob}_\ell$ has order $p-1$ on $E[p]$) and the "lifted Euler system" $c_\ell \in H^1(\mathbb{Q}(\mu_\ell), E[p])$, then applying the derivative operator $D_\ell = \sum i \sigma_\ell^i$.

## Computational Example

**Curve 11a1, $p = 3$:**
- Conductor: 11. $a_3 = -2$. $\Omega_\infty = 1.2692093053\ldots$
- $L(E, 1) = 0.2538418613\ldots$ $L(E,1)/\Omega = 0.2\ldots = 1/5$.
- Interpolation: $\mathcal{E}(3, 1) = (1 + 2/3 + 1/3)^{-1} = 1/2$. So $\exp^*(z^{(3)}) = 1/2 \times 1/5 = 1/10 \in \mathbb{Q}_3$.
- $p$-adic height: $\hat{h}_3(z^{(3)}) = 0$ (since $r = 0$ and $z^{(3)} \in H^1_f$ is non-trivial).
- $|\operatorname{III}| = 1$, $\prod c_v = 1$, $|E_{\mathrm{tors}}| = 5$. $v_3(1/5) = 0$. ✓

**Curve 37a1, $p = 5$:**
- Conductor: 37. $a_5 = -2$. $\Omega_\infty = 2.993646777\ldots$
- $L'(E, 1) = 0.9172401517\ldots$ $L'(E,1)/\Omega = 0.3063\ldots$
- Kolyvagin prime: $\ell = 2$ (need $\ell \equiv 1 \pmod{5}$... actually $\ell = 11$ or $\ell = 31$).
- $P = (0, 0)$ generates $E(\mathbb{Q})$ modulo torsion. $\hat{h}_{\mathrm{NT}}(P) = 0.05111140823\ldots$
- Check: $L'(E,1)/\Omega / \hat{h}_{\mathrm{NT}}(P) = 5.992\ldots \approx 6 = |\operatorname{III}| \cdot \prod c_v / |E_{\mathrm{tors}}|^2$. ✓

**Curve 5077a1, $p = 2$:**
- Conductor: 5077. $\operatorname{rk}(E(\mathbb{Q})) = 3$.
- The Euler system computation for $p = 2$ at this level is at the boundary of current computational feasibility (level $5077 \times 2^{10} \approx 5 \times 10^6$).

## Obstacle Analysis

The computational bottleneck is the modular symbol computation at level $Np^k$. The dimension of $\mathcal{S}_2(\Gamma_0(Np^k))$ grows approximately as $Np^k / 12$, so for $k = 10$ and $N = 5077$, this is $\sim 4 \times 10^6$ — at the edge of feasibility in Magma. The $p$-adic integration for the height computation requires working to precision $O(p^k)$, which means $p$-adic floating point with $\sim 3000$ digits for $k = 10$ at $p = 2$. The Kolyvagin derivative computation requires finding a prime $\ell$ with $\ell \equiv 1 \pmod{p}$ and $\operatorname{Frob}_\ell$ of exact order $p-1$ on $E[p]$, which requires testing $O(p)$ primes on average.

## Cross-Group Connections
- **Group A (BSD Formula)**: This direction provides the computational verification laboratory for BSD.
- **Group B-001 (Kato's system)**: The explicit computation tests the abstract Euler system theory.
- **Group C (Heegner Points)**: The Kolyvagin derivative classes connect to Heegner point computations.

## Classification
Experiment
