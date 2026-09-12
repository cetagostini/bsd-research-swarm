# A-008: Iwasawa Theory for Rankin–Selberg Convolutions

## Status Assessment

The Rankin–Selberg Main Conjecture is proven for ordinary forms under the non-critical slope condition by Hsieh (2014), and significant progress has been made by Kings–Loeffler–Zerbes (2021) using Euler systems. The direction is promising and directly applicable to products of elliptic curves. Realistic timeline for complete results in the generic slope case: 5–8 years.

## Testable Conjecture

**Conjecture (Rankin–Selberg Main Conjecture).** Let $E_1, E_2/\mathbb{Q}$ be elliptic curves of conductors $N_1, N_2$ with good ordinary reduction at $p$, and $a_p(E_1) \neq a_p(E_2)$ (non-critical slope). Let $\mathbb{Q}_\infty/\mathbb{Q}$ be the cyclotomic $\mathbb{Z}_p$-extension. Then

$$\operatorname{char}_{\Lambda}\left(\operatorname{Sel}_{p^\infty}(E_1 \times E_2/\mathbb{Q}_\infty)^\vee\right) = \left(\mathscr{L}_p(E_1 \times E_2, T)\right)$$

where $\mathscr{L}_p(E_1 \times E_2, T) \in \Lambda$ interpolizes

$$\mathscr{L}_p(E_1 \times E_2, \chi, 1) = e_p(E_1, E_2, \chi) \cdot \frac{L^{\{p\}}(E_1 \times E_2, \chi, 1)}{\langle f_1, f_1 \rangle \cdot \langle f_2, f_2 \rangle \cdot \Omega_1 \cdot \Omega_2}$$

for finite-order characters $\chi$, where $e_p$ is an explicit Euler factor and $\Omega_i$ are real periods.

## Approach Summary

**Phase 1: Compute $L(E_1 \times E_2, s)$ and its $p$-adic avatar.** For pairs $(E_1, E_2)$ from the Cremona database with $N_1, N_2 \leq 200$ and $a_p(E_1) \neq a_p(E_2)$, compute $L(E_1 \times E_2, 1)$ via Dokchitser's method in PARI/GP. Then compute $\mathscr{L}_p(E_1 \times E_2, T)$ via Hida's Eisenstein family method in SageMath.

**Phase 2: Selmer group computation.** The Selmer group $\operatorname{Sel}_{p^\infty}(E_1 \times E_2/\mathbb{Q}_\infty)$ is defined using the tensor product $T_p E_1 \otimes T_p E_2$ and local conditions from both curves. Compute its $\Lambda$-module structure at finite layers and verify the Main Conjecture.

**Phase 3: Beilinson–Flach Euler system.** The Beilinson–Flach elements $\mathrm{BF}_{f_1, f_2} \in H^1(\mathbb{Q}_n, T_p E_1 \otimes T_p E_2)$ are the Euler system input. They satisfy norm-compatibility under the non-critical slope condition. The strategy is to apply the Rubin–Kolyvagin machine to $\mathrm{BF}_{f_1, f_2}$ to bound the Selmer group, then use congruence modules to establish the reverse divisibility.

## Computational Example

**$E_1 = 11a1$, $E_2 = 37a1$** at $p = 5$:

$a_5(11a1) = -2$, $a_5(37a1) = -2$. The slope condition fails ($a_p$ are equal). Choose $E_2 = 43a1$: $a_5(43a1) = 2$. Now $a_5(E_1) = -2 \neq 2 = a_5(E_2)$, so the non-critical slope condition holds.

$L(11a1 \times 43a1, 1) = \sum_{n=1}^{\infty} a_n(11a1) a_n(43a1) n^{-1}$. This can be computed via the Rankin–Selberg method: $L(f_{11} \times f_{43}, 1) = \frac{(2\pi)^2}{\Omega_{11}^+ \Omega_{43}^+} \cdot \alpha_{11} \alpha_{43}$ for explicit algebraic $\alpha_{11}, \alpha_{43}$.

The $5$-adic L-function $\mathscr{L}_p(11a1 \times 43a1, T)$ should have $\lambda = 0$ (if $L(11a1 \times 43a1, 1) \neq 0$) or $\lambda > 0$ (if vanishing).

## Obstacle Analysis

The critical slope case ($a_p(E_1) = a_p(E_2)$) is the main obstacle. When $E_1 = E_2$, the convolution is the symmetric square $L(E, \operatorname{sym}^2, s)$, and the Rankin–Selberg $p$-adic L-function does not exist in the classical sense. Hida's construction requires $\alpha_{f_1} \neq \alpha_{f_2}$ for the $p$-adic families to be distinct. In the critical slope case, one needs either: (a) a different construction of the $p$-adic L-function using $p$-adic Hodge theory (étale $(\varphi, \Gamma)$-modules), or (b) a deformation argument: perturb $E_2$ to $E_2'$ with $a_p(E_2') \neq a_p(E_1)$, prove the Main Conjecture for $E_1 \times E_2'$, then specialize via congruence. Strategy (b) is pursued by Hsieh and requires control of the Eisenstein ideal.

## Cross-Group Connections

- **Group A (Main Conjecture):** The Rankin–Selberg Main Conjecture generalizes the elliptic curve Main Conjecture (take $E_2$ to be the Tate twist).
- **Group C (Euler Systems):** Beilinson–Flach elements are the Euler system input.
- **Group G (Automorphic Forms):** The Rankin–Selberg convolution is an automorphic $L$-function for $\mathrm{GL}_2 \times \mathrm{GL}_2$.
- **Group F (BSD Formula):** The Bloch–Kato conjecture for $h^1(E_1) \otimes h^1(E_2)$ is the motivic version.

## Classification

Theorem (non-critical slope: Hsieh; critical slope: Conjecture)
