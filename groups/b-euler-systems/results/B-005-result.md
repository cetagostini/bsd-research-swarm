# B-005: Higher-Rank Euler Systems (Nekovář, Schappacher)

## Direction ID and Title
B-005 — Higher-Rank Euler Systems (Nekovář, Schappacher)

## Status Assessment
Higher-rank Euler systems are entirely conjectural for $GL(2)$ representations. Nekovář (2006) defined the abstract framework: an Euler system of rank $r$ for a $p$-adic representation $V$ is a collection of classes in $H^r(\mathbb{Q}(V)_{/\mathrm{cyc}}, \wedge^r V)$ satisfying compatibility under corestriction. No explicit construction of a rank $r \geq 2$ Euler system for any $GL(2)$ representation exists. The motivic cohomology groups $H^r_{\mathcal{M}}(\mathbb{Q}, \operatorname{Sym}^{r-1} V_E)$ for $r \geq 3$ are computationally inaccessible. The direction is classified as Speculation with a clear theoretical framework but no constructive evidence.

## Testable Conjecture or Lemma

**Conjecture B-005.** Let $E/\mathbb{Q}$ be an elliptic curve with $\operatorname{ord}_{s=1} L(E,s) = r \geq 2$, and let $p$ be a prime of good ordinary reduction. There exists a collection of classes $\{\mathbf{c}_m^{(r)}\}_{m \text{ sqfree}}$ with $\mathbf{c}_m^{(r)} \in H^r_{\mathcal{M}}\left(\operatorname{Spec}(\mathbb{Q}(\mu_m)), \operatorname{Sym}^{r-1}(H^1_{\mathrm{ét}}(E_{\bar{\mathbb{Q}}}, \mathbb{Z}_p)) \otimes \mathbb{Q}_p(r)\right)$ satisfying:

(a) **Norm compatibility:** For $\ell \nmid mp$ prime, $\operatorname{Cor}_{m\ell/m}(\mathbf{c}_{m\ell}^{(r)}) = P_\ell^{(r)}(\operatorname{Frob}_\ell^{-1}) \cdot \mathbf{c}_m^{(r)}$ where $P_\ell^{(r)}(x) = \prod_{j=0}^{r-1}(1 - \alpha_\ell^{r-1-2j} x)$ with $\alpha_\ell$ the unit root of $x^2 - a_\ell x + \ell$.

(b) **Regulator image:** The syntomic regulator satisfies:
$$\operatorname{reg}_{\mathrm{syn}}(\mathbf{c}_1^{(r)}) = \frac{L^{(r)}(E,1)}{r! \cdot \Omega_E} \cdot p^{-\alpha(r)}$$
where $\alpha(r)$ is an explicit correction factor involving $p$-adic periods.

(c) **Selmer bound:** The classes $\{\mathbf{c}_m^{(r)}\}$ yield $\dim_{\mathbb{F}_p} \operatorname{Sel}(E/\mathbb{Q})[p] \leq r$ (which is trivially true, but the content is that the bound is sharp when combined with the lower bound from Heegner points).

## Approach Summary

The construction of higher-rank Euler systems requires algebraic cycles in higher codimension on the $r$-fold product $X_0(N)^r$ or on higher-dimensional Shimura varieties. For $r = 2$, the relevant cycles are Beilinson's elements in $K_2(X_0(N))$, arising from the Eisenstein symbol on the Kuga-Sato variety. The Beilinson regulator $\operatorname{reg}_B: K_2(X_0(N)) \to H^2_{\mathcal{D}}(X_0(N), \mathbb{R}(2))$ maps these to classes whose archimedean period recovers $L'(E, 1)$.

For $r \geq 3$, one needs cycles in $\operatorname{CH}^r(\mathcal{X}, 2r-k)$ for a suitable smooth compactification $\mathcal{X}$ of the Kuga-Sato variety $W^{r-2} = E \times \cdots \times E \times_{\operatorname{Spec}(\mathbb{Q})} X_0(N)$. The motivic cohomology groups are related to higher polylogarithms: Deninger (1988) showed that the higher polylogarithm $\mathrm{Li}_r$ on $X_0(N)$ should produce the relevant classes, and Wildeshaus (1997) gave the motivic interpretation. However, the norm compatibility under Hecke correspondences at auxiliary primes $\ell$ has never been verified for any specific cycle.

A secondary approach uses Nekovář's $p$-adic height machinery: starting from Kato's rank-1 Euler system, the $p$-adic height pairing produces a "derivative" class in $H^1$ that carries rank-2 information. This is the only partially constructive route for $r = 2$.

## Computational Example

- **$E = $ 5077a1** ($r = 3$): $y^2 + y = x^3 - 7x + 6$, conductor 5077. The expected rank-3 Euler system class $\mathbf{c}_1^{(3)} \in H^3_{\mathcal{M}}(\operatorname{Spec}(\mathbb{Q}), \operatorname{Sym}^2(V_E) \otimes \mathbb{Q}_p(3))$ is inaccessible to current computation. However, the $p$-adic height $\hat{h}_p$ on Kato's zeta element can be computed as a proxy.
- **$E = $ 389a1** ($r = 2$): $y^2 + y = x^3 + x^2 - 2x$, conductor 389. Beilinson's $K_2$ class on $X_0(389)$ should yield $L'(E, 1) = 0$ (here $r = 2$, $L(E,1) = 0$ and $L'(E,1) = 0$). The $K_2$ element is computationally accessible via modular symbols in Magma.
- **$E = $ 681a1** ($r = 2$): Test the Nekovář secondary class construction for $p = 5$.

## Obstacle Analysis

The fundamental obstruction is the absence of a geometric construction of algebraic cycles satisfying norm compatibility. For $r = 1$, Kato's cycles exist as Beilinson elements in relative $K$-groups of modular curves, and the Hecke action provides norm compatibility. For $r \geq 2$, the relevant cycles (if they exist) live in higher Chow groups or higher $K$-groups of Kuga-Sato varieties, and the Hecke correspondences act on these groups in a way that is not understood. Additionally, the injectivity of the regulator map $\operatorname{reg}_{\mathrm{syn}}: H^r_{\mathcal{M}} \to H^r_{\mathrm{syn}}$ is known only in special cases (e.g., $r = 1$ by Besser), making it impossible to verify the regulator image even if the cycle were constructed.

## Cross-Group Connections
- **Group A (BSD Formula)**: The regulator image (b) directly encodes the BSD leading coefficient for rank $r$.
- **Group E (p-adic Heights)**: The Nekovář $p$-adic height is the bridge between rank-1 and rank-2 Euler systems.
- **Group F (Iwasawa Theory)**: Higher-rank Iwasawa theory requires new structural results on $\Lambda$-modules.

## Classification
Speculation
