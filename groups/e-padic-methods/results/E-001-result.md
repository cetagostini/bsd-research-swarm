# E-001 · Two-Variable p-adic L-functions (Hida Family × Elliptic Curve)

## Direction ID and Title
E-001: Two-variable p-adic L-functions interpolating Hida family members through an ordinary eigenform attached to an elliptic curve $E/\mathbb{Q}$.

## Status Assessment
**Active.** The construction of Greenberg–Stevens (1993) is established: the two-variable p-adic L-function $L_p(f_\infty, s, k)$ exists as a meromorphic element of the Iwasawa algebra $\Lambda = \mathbb{Z}_p[[\mathbb{Z}_p^\times \times \mathbb{Z}_p^\times]]$ (or its fraction field). Integrality and the two-variable Iwasawa main conjecture remain open in the non-CM case.

## Testable Conjecture or Lemma

**Conjecture (Two-Variable p-adic BSD).** Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at an odd prime $p$, and let $\mathbf{f} = \{f_k\}$ be the Hida family through $f = f_2$. Then $L_p(\mathbf{f}, s, k) \in \Lambda$ satisfies:

1. **Interpolation:** For each classical weight $k \geq 2$ and critical integer $j$ with $1 \leq j \leq k-1$:
$$L_p(f_k, j) = \left(1 - \frac{p^{j-1}}{\alpha_k}\right)\left(1 - \frac{p^{j}}{\beta_k}\right) \cdot \frac{L(f_k, j)}{\Omega_{f_k}^{\pm} \cdot (2\pi i)^{j-1} / (j-1)!}$$
where $\alpha_k, \beta_k$ are roots of $X^2 - a_p(f_k)X + p^{k-1}$ with $|\alpha_k|_p = 1$.

2. **Specialisation at $k=2$:** $L_p(\mathbf{f}, s, 2) = L_p(E, s)$, the cyclotomic p-adic L-function of $E$.

3. **Integrality (Conjectural):** $L_p(\mathbf{f}, s, k) \in \Lambda$ (not merely in $\text{Frac}(\Lambda)$) when $E$ has good ordinary reduction at $p$ and $p \nmid \text{ord}_p(N)$.

**Lemma (Control Theorem, Hida).** The natural restriction map $S_k^{\text{ord}}(\Gamma_0(Np)) \to S_2^{\text{ord}}(\Gamma_0(Np))$ sending $f_k \mapsto f_2$ (modular forms modulo the weight-space ideal) is surjective with kernel controlled by the Eisenstein ideal, ensuring the Hida family $\mathbf{f}$ is a finite flat extension of $\Lambda$.

## Approach Summary

1. **Hida's ordinary projector** $e^{\text{ord}} = \lim_{n \to \infty} U_p^{n!}$ projects modular forms to the ordinary subspace. The ordinary Hecke algebra $\mathbf{T}^{\text{ord}}$ is finite and flat over the weight algebra $\Lambda_W = \mathbb{Z}_p[[1 + p\mathbb{Z}_p]]$.

2. **Modular symbols** $\{\gamma, \alpha\}$ for $\gamma \in \Gamma_0(Np)$ and $\alpha \in \mathbb{P}^1(\mathbb{Q})$ provide the bridge between modular forms and distributions on $\mathbb{Z}_p^\times$. The Manin map sends $f_k$ to a measure $\mu_{f_k}$ on $\mathbb{Z}_p^\times$.

3. **Two-variable interpolation:** The Amice transform of the measure $\mu_{f_\infty}$ over the Hida family gives $L_p(f_\infty, s, k)$ as an element of $\Lambda$ interpolating the algebraic parts $L(f_k, j) / \Omega_{f_k}^{\pm}$ at classical points $(j, k)$.

4. **Greenberg–Stevens approach:** Uses the universal ordinary deformation ring and the fact that the Hida family is a quotient of this ring. The two-variable L-function is constructed as the characteristic power series of a Selmer group over the two-variable extension.

## Computational Example

**Setup.** Consider $E = 11a1$ (Cremona label), the curve $y^2 + y = x^3 - x^2 - 10x - 20$ of conductor $N = 11$, with $a_p$ values:
- $p = 5$: $a_5 = -2$ (good ordinary, since $|a_5|_5 = |{-2}|_5 = 1 < 5^{1/2}$)
- $p = 3$: $a_3 = -2$ (good ordinary)

**Hida family computation.** The Hida family $\mathbf{f}$ through $f_{11a1}$ at $p = 5$ has weight space parametrised by $k \in 1 + 4\mathbb{Z}_5$ (since $p-1 = 4$). The $U_5$-eigenvalue $\alpha_k$ varies analytically:
- At $k = 2$: $\alpha_2 = a_5 = -2$ (the unit root of $X^2 + 2X + 5$, which is $-2$ since $v_5(-2) = 0$ and the other root has $v_5 = 1$)
- The weight variable $T = k - 2$ parametrises the family; $L_p(\mathbf{f}, s, k) \in \mathbb{Z}_5[[s, T]]$ (where $s$ denotes the cyclotomic variable, formalised as $s \in 1 + 5\mathbb{Z}_5$).

**Verification at $k = 2$, $s = 1$:** The specialisation $L_p(f_2, 1) = L_p(E, 1)$ should satisfy:
$$L_p(E, 1) = \left(1 - \frac{1}{\alpha_2}\right)\left(1 - \frac{5}{\beta_2}\right) \cdot \frac{L(E, 1)}{\Omega_E^+}$$

For $E = 11a1$: $L(E,1) \approx 0.25384$, $\Omega_E^+ \approx 1.26921$, so $L(E,1)/\Omega_E^+ \approx 0.2 = 1/5$. The Euler factors: $\alpha_2 = -2$, $\beta_2 = 5/(-2) = -5/2$, so $(1 - 1/(-2))(1 - 5/(-5/2)) = (3/2)(3) = 9/2$. This gives $L_p(E, 1) \approx (9/2) \cdot (1/5) = 9/10$ in $\mathbb{Z}_5$, which is a 5-adic unit.

**Verification at $k = 4$:** The weight-4 form $f_4$ in the family is a modular form of weight 4 on $\Gamma_0(55)$ (level $Np = 55$). Its L-value $L(f_4, 2)$ divided by the period $\Omega_{f_4}$ should equal the specialisation of $L_p(\mathbf{f}, 2, 4)$, confirming interpolation.

## Obstacle Analysis

1. **Integrality:** The two-variable L-function is known to lie in $\text{Frac}(\Lambda)$. Proving it lies in $\Lambda$ requires controlling the denominators that arise from the non-unit root $\beta_k$ at higher weights. In the CM case (e.g., $E$ with CM by an imaginary quadratic field), integrality follows from Katz's construction.

2. **Denominator growth:** As $k$ varies, the Euler factor $(1 - p^{j-1}/\alpha_k)$ can introduce unbounded denominators if $\alpha_k$ approaches $p^{j-1}$ p-adically. For weight 2 and $j = 1$, the factor $(1 - 1/\alpha)$ is a p-adic unit when $\alpha$ is a unit root, but higher weights introduce $p$-powers.

3. **Meromorphic continuation:** The two-variable L-function is constructed via interpolation; showing it extends meromorphically to all of $\text{Spec}(\Lambda)$ (not just the classical locus) requires p-adic functional equation arguments that are incomplete.

4. **Computational precision:** Evaluating $L_p(\mathbf{f}, s, k)$ at specific $(s, k) \in \mathbb{Z}_p^\times \times \mathbb{Z}_p^\times$ requires high-precision computation of Hida family coefficients, which becomes expensive for large $k$ (non-classical points in the weight space).

## Cross-Group Connections

- **Group A (Classical BSD):** The specialisation at $k=2$ recovers the cyclotomic p-adic L-function, connecting to A's classical L-value computations via the interpolation formula.
- **Group B (Heegner Points):** For rank-1 specialisations, Heegner points provide the geometric side of the p-adic Gross–Zagier formula (E-002), which is a derivative of the two-variable L-function along the cyclotomic variable.
- **Group C (Iwasawa Theory):** The two-variable L-function generates the characteristic ideal of a two-variable Selmer group; the Iwasawa main conjecture for $\mathbb{Z}_p^2$-extensions is the natural framework.
- **Group D (Euler Systems):** Kato's Euler system over the Hida family provides the inequality $\supseteq$ in the two-variable main conjecture.

## Classification
**Iwasawa theory / p-adic families.** This direction lies at the intersection of Hida theory and Iwasawa main conjectures, with strong computational components.
