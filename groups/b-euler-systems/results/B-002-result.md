# B-002: Beilinson-Flach Elements for Rankin-Selberg Products

## Direction ID and Title
B-002 — Beilinson-Flach Elements for Rankin-Selberg Products

## Status Assessment
Beilinson-Flach elements $\mathrm{BF}_{f,g}^{(i)}$ are now established as genuine Euler systems for the representation $V_f \otimes V_g$ by the work of Kings, Sprang, and Loeffler-Zerbes. The Iwasawa main conjecture for $GL(2) \times GL(2)$ Rankin-Selberg products has been proved in many cases using these elements. The $p$-adic L-function $\mathcal{L}_p(f,g)$ satisfies the expected interpolation property at classical points. The anticyclotomic theory remains only partially developed, and the simultaneous ramification issue at primes dividing $\mathrm{lcm}(N_f, N_g)$ is a genuine obstruction to full generality.

## Testable Conjecture or Lemma

**Lemma B-002.** Let $f, g$ be newforms of weights $k_f, k_g$ and levels $N_f, N_g$ with $p \nmid N_f N_g$ a prime of good ordinary reduction for both. Let $\mathbb{V}_{f,g} = V_f \otimes V_g$ be the tensor product Galois representation. The Beilinson-Flach elements $\mathrm{BF}_{f,g}^{(i)} \in H^1(\mathbb{Q}(\mu_m), \mathbb{V}_{f,g} \otimes \mathbb{Q}_p(-i))$ for $i \in \{1,2\}$ satisfy:

$$\operatorname{Cor}_{m\ell/m}\left(\mathrm{BF}_{f,g,\, m\ell}^{(i)}\right) = P_\ell^{(i)}(\mathrm{Frob}_\ell^{-1}) \cdot \mathrm{BF}_{f,g,\,m}^{(i)}$$

where $P_\ell^{(1)}(x) = (1 - \alpha_\ell^f \alpha_\ell^g x)(1 - \alpha_\ell^f \beta_\ell^g x)$ and $P_\ell^{(2)}(x) = (1 - \alpha_\ell^f \alpha_\ell^g x)(1 - \beta_\ell^f \alpha_\ell^g x)$, with $\alpha_\ell^f, \beta_\ell^f$ the roots of $x^2 - a_\ell(f) x + \ell^{k_f - 1}$. The resulting $p$-adic L-function satisfies:

$$\mathcal{L}_p(f,g)\big|_{s=1} = \left(1 - \frac{a_p(f) a_p(g)}{p}\right)\left(1 - \frac{a_p(f) \bar{a}_p(g)}{p}\right) \cdot \frac{L(f \otimes g, 1)}{(2\pi i)^{k_f + k_g - 2} \Omega_f^+ \Omega_g^+}$$

## Approach Summary

The construction proceeds via the Beilinson-Flach elements on the product $X_0(N_f) \times X_0(N_g)$. One starts with the Rankin-Selberg integral representation $\Lambda(f \otimes g, s) = \int_{\Delta} f(z) g(z) y^s \, \frac{dx\,dy}{y^2}$ and constructs motivic cohomology classes on the product using Eisenstein series of weight $(k_f, k_g)$ on $GL(2) \times GL(2)$. The key geometric input is the existence of CM points on $X_1(N)$ at auxiliary primes $\ell \equiv 1 \pmod{m}$, which provide the cycles needed for the norm compatibility.

For the anticyclotomic tower, one restricts to the case where $g = \bar{f}$ (the complex conjugate), which yields the adjoint square representation $\mathrm{ad}^0(f)$. The anticyclotomic $p$-adic L-function $\mathcal{L}_p^{\mathrm{anti}}(f)$ lives in the Iwasawa algebra of the anticyclotomic $\mathbb{Z}_p$-extension of the imaginary quadratic field $K$ and interpolates $L(\mathrm{ad}^0 f, \chi, 1)$ for anticyclotomic characters $\chi$ of $K$.

The application to BSD for the twist $E^{(\chi)}$ proceeds by specializing the two-variable $p$-adic L-function at the character $\chi$ and applying the Euler system bound to the $\chi$-isotypic component of the Selmer group of $E$ over $K$.

## Computational Example

Test cases:
- **$f = $ newform of 11a1**, $g = $ newform of 37a1: Compute $\mathrm{BF}_{f,g}^{(1)}$ for $p = 3$ and verify interpolation at $s = 1$ against $L(f \otimes g, 1) / (\Omega_f \Omega_g)$ computed via Dokchitser's method.
- **$E = $ 11a1**, $K = \mathbb{Q}(\sqrt{-3})$, $\chi$ the trivial character: The Beilinson-Flach element specialized to the anticyclotomic tower should yield $L_p(\mathrm{ad}^0 f, 1)$ matching $\frac{L'(11a1, 1)}{\Omega_{11a1}} \cdot |\operatorname{III}| \cdot \prod c_v / |E_{\mathrm{tors}}|^2$.
- **$f = $ newform of 11a1**, $g = f$ (self-product): The resulting $p$-adic L-function is $\mathcal{L}_p(\mathrm{Sym}^2 f)$, testable against the symmetric square $L$-value computed via Magma's `LSeries` function.

## Obstacle Analysis

The main obstruction is the prime-to-$p$ Euler system norm relation at primes $\ell$ simultaneously dividing $N_f$ and $N_g$. When $\gcd(N_f, N_g)$ has many prime factors, the set of auxiliary primes $\ell$ at which the CM point construction works becomes sparse, potentially breaking the Euler system machine. The anticyclotomic Iwasawa theory for the adjoint representation additionally requires control of the $\mu$-invariant, which is known to vanish only under restrictive hypotheses (e.g., $p$ split in $K$ and $E$ having good ordinary reduction at all primes above $p$).

## Cross-Group Connections
- **Group A (BSD Formula)**: Direct computation of $p$-parts of BSD for twists of $E$ by ring class characters.
- **Group C (Heegner Points)**: When $g$ corresponds to a character, the specialization recovers Heegner point information.
- **Group F (Iwasawa Theory)**: The two-variable main conjecture is an Iwasawa-theoretic statement.

## Classification
Theorem (Euler system and norm compatibility); Conjecture (full anticyclotomic BSD application)
