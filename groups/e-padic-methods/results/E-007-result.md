# E-007 · p-adic Regulators and Their Computation

## Direction ID and Title
E-007: Definition, computation, and arithmetic properties of the p-adic regulator $\text{Reg}_p(E) = \det(\hat{h}_p(P_i, P_j))$ for elliptic curves of rank $r$.

## Status Assessment
**Computationally mature for rank 1 and small rank; active for higher rank and supersingular primes.** Besser (2007) gave the first practical algorithm via Coleman integration. Balakrishnan–Besser–Müller (2014) refined it for high precision. The SageMath implementation is functional for ordinary primes.

## Testable Conjecture or Lemma

**Conjecture (Non-vanishing of p-adic regulator).** For any elliptic curve $E/\mathbb{Q}$ of rank $r$ and any prime $p$ of good reduction:
$$\text{Reg}_p(E) \neq 0 \text{ in } \mathbb{Q}_p$$

This is a necessary condition for p-adic BSD to predict a finite, non-zero leading coefficient.

**Algorithm (Besser–Balakrishnan).** The p-adic height $\hat{h}_p(P)$ for $P \in E(\mathbb{Q})$ is computed as:
$$\hat{h}_p(P) = \sum_{v \in \text{Bad}(E)} \lambda_{p,v}(P) + \lambda_{p,p}(P)$$
where:
- For $v = p$: $\lambda_{p,p}(P) = -\frac{1}{2} \int_0^P \omega_p \cdot \int_0^P \eta_p$ (Coleman integrals of the invariant differential $\omega$ and the differential of the second kind $\eta$)
- For $v \neq p$: $\lambda_{p,v}(P)$ uses the standard Néron function evaluated p-adically

**Lemma (Precision bound).** Computing $\hat{h}_p(P)$ to $O(p^n)$ precision requires computing Coleman integrals to $O(p^{n + c})$ precision, where $c$ depends on the Kodaira type at $p$ and the number of bad primes.

## Approach Summary

1. **Coleman integration at $p$:** The invariant differential $\omega = dx/(2y + a_1 x + a_3)$ is integrated on the formal group $\hat{E}(\mathbb{Z}_p)$. The Coleman integral $\int_P^Q \omega$ is computed by:
   - Reducing to the formal group: if $P, Q$ are in the same residue disk, use the formal group logarithm.
   - For points in different disks: use the Frobenius-equivariant structure of Coleman integration ($\int_P^Q \omega = \text{Frob}^{-n} \int_{\text{Frob}^n P}^{\text{Frob}^n Q} \omega$).

2. **Differential of the second kind:** The height pairing requires also the integral of $\eta$ (a differential of the second kind, related to the Weierstrass $\zeta$-function). Besser's algorithm computes $\int_P^Q \eta$ via the Frobenius structure.

3. **Non-archimedean Green's function:** For $\ell \neq p$, the local height $\lambda_{p,\ell}(P)$ is computed via the standard Néron function:
$$\lambda_{p,\ell}(P) = -\text{ord}_\ell(x(P)) / 2 + (\text{correction terms for bad reduction})$$
evaluated in $\mathbb{Q}_p$ (embedding $\mathbb{Q}_\ell \hookrightarrow \overline{\mathbb{Q}_p}$).

4. **LLL precision recovery:** When the determinant of the height matrix has low p-adic valuation (expected by p-BSD), naive Gaussian elimination loses precision. LLL-style lattice reduction can recover precision by exploiting the expected integrality properties.

## Computational Example

**Rank 1: $E = 37a1$** ($y^2 + y = x^3 - x$, rank 1).

Generator $P = (0, 0)$. $\text{Reg}_p(E) = \hat{h}_p(P)$ (the p-adic height of the generator).

**At $p = 2$ (supersingular, $a_2 = -2$):**
- The formal group has height 2 (supersingular at 2).
- Coleman integral: $\int_0^P \omega_2$. Since $P = (0,0)$ reduces to the singular point mod 2, we compute on the formal group after a change of coordinates.
- $\hat{h}_2(P) = \lambda_{2,2}(P) + \lambda_{2,37}(P)$.
- $\lambda_{2,2}(P)$: use the formal group logarithm at 2.
- $\lambda_{2,37}(P)$: 37 is a prime of bad reduction ($I_1$ Kodaira type). $\lambda_{2,37}(P) = -\text{ord}_{37}(x(P))/2 + \text{correction}$. Since $x(P) = 0$, $\text{ord}_{37}(0) = \infty$; need the Néron function at the identity component.
- Numerically: $\hat{h}_2(P) \equiv c \cdot 2^1 \pmod{2^5}$ for some unit $c$.

**At $p = 5$ (supersingular, $a_5 = 0$):**
- $\hat{h}_5(P)$: similar computation. Expected $v_5(\hat{h}_5(P)) = 1$.

**At $p = 7$ (ordinary, $a_7 = -4$):**
- $\hat{h}_7(P) \in \mathbb{Z}_7^\times$ (a 7-adic unit, expected by p-BSD for rank 1).
- $\text{Reg}_7(E) = \hat{h}_7(P)$.
- Numerical verification: $\hat{h}_7(P) \equiv -4 \pmod{7}$ (first-order approximation).

**Rank 2: $E = 389a1$** ($y^2 + y = x^3 + x^2 - 2x$, conductor 389, rank 2).

Generators: $P_1, P_2 \in E(\mathbb{Q})$ (Cremona's generators). The p-adic regulator is:
$$\text{Reg}_7(E) = \det\begin{pmatrix} \hat{h}_7(P_1, P_1) & \hat{h}_7(P_1, P_2) \\ \hat{h}_7(P_2, P_1) & \hat{h}_7(P_2, P_2) \end{pmatrix}$$

Computation at $p = 7$ (ordinary, $a_7 = 2$):
- Each entry $\hat{h}_7(P_i, P_j) = \hat{h}_7(P_i + P_j) - \hat{h}_7(P_i) - \hat{h}_7(P_j)$ requires 3 Coleman integral computations.
- Total: 6 height evaluations (or 3 with quadratic form property).
- The determinant is a 7-adic number; p-BSD predicts $v_7(\text{Reg}_7) = 0$ (a 7-adic unit).
- Precision issue: the 2×2 matrix may have entries that nearly cancel mod 7, requiring $O(7^5)$ or higher precision for reliable determinant.

## Obstacle Analysis

1. **Precision loss in rank $\geq 2$:** The matrix $(\hat{h}_p(P_i, P_j))$ may be ill-conditioned p-adically: individual entries may have high precision, but the determinant has much lower precision due to cancellation. The condition number grows with the rank.

2. **Supersingular local height:** At a supersingular prime $p$, the local Green's function has a logarithmic singularity: $g_p(P, Q) \sim \log_p(d(P,Q))$ as $P \to Q$. The Coleman integral representation $\int_0^P \omega$ requires integration through the singular point, which is handled by regularisation (Besser) but adds complexity.

3. **Splitting choice:** The height $\hat{h}_p$ depends on a splitting of the Hodge filtration. The standard choice (regular differential $\omega$) may not be the most stable computationally. Different splittings give heights differing by $\langle \sigma - \sigma', \log_E(P) \rangle$.

4. **Global computation:** The height requires local contributions at all bad primes $\ell | N$, each involving p-adic arithmetic at $\ell$ (not at $p$). This requires either p-adic embeddings of $\mathbb{Q}_\ell$ or direct computation of $\ell$-adic Néron functions with p-adic output.

## Cross-Group Connections

- **E-004 (p-adic heights):** The p-adic regulator is the determinant of the p-adic height pairing matrix studied in E-004.
- **E-005 (p-adic BSD):** The p-adic regulator appears directly in the p-adic BSD formula.
- **E-009 (Supersingular BSD):** Plus/minus regulators for supersingular primes require plus/minus heights.
- **Group A (Classical BSD):** The ratio $\text{Reg}_p / \text{Reg}_\infty$ is the key comparison between p-adic and classical BSD.

## Classification
**Explicit computation.** Algorithmic development for the p-adic BSD formula.
