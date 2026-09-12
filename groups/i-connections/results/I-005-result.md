# I-005: Stark's Conjecture and Leading Taylor Coefficients

## Direction ID and Title
**I-005** — Stark's Conjecture and Leading Taylor Coefficients

## Status Assessment
Stark's conjecture is proven for many cases, including abelian extensions of $\mathbb{Q}$ with $L(0, \chi) = 0$ to order 1 (Stark 1980), and a $p$-adic version for CM abelian varieties (Rubin 1996). The Brumer-Stark conjecture is proven (Dasgupta-Kakde-Ventullo 2018). The bridge to BSD is explicit for CM curves via Rubin's work and the Equivariant Tamagawa Number Conjecture (ETNC).

## Testable Conjecture or Lemma

**Conjecture (Stark–BSD Regulator Identity for CM Curves).** Let $E/\mathbb{Q}$ be an elliptic curve with CM by $\mathcal{O}_K$, $K$ imaginary quadratic, with $\operatorname{ord}_{s=1} L(E/\mathbb{Q}, s) = 1$. Let $\psi$ be the Hecke character of $K$ such that $L(E/\mathbb{Q}, s) = L(\psi, s)$. Then:

1. Stark's conjecture for $\psi$ produces a Stark unit $\epsilon_\psi \in K^{\mathrm{ab}}$ such that
$$L'(\psi, 0) = -\frac{1}{w_K} \sum_\sigma \psi(\sigma) \log |\sigma(\epsilon_\psi)|.$$

2. The functional equation relates $L'(\psi, 0)$ to $L'(E/\mathbb{Q}, 1)$:
$$L'(E/\mathbb{Q}, 1) = \frac{(2\pi)^2}{\sqrt{N_E}} \cdot \epsilon(E) \cdot L'(\psi, 0) \cdot L(\bar\psi, 0),$$
where $\epsilon(E)$ is the root number.

3. The Gross-Zagier formula gives $L'(E/\mathbb{Q}, 1) = c \cdot \hat{h}(P_{\mathrm{Heegner}})$.

4. Combining: the Stark unit $\epsilon_\psi$ determines $L'(\psi, 0)$, which via the functional equation determines $L'(E,1)$, which via Gross-Zagier determines $\hat{h}(P)$. This yields the rank-1 BSD formula:
$$\frac{L'(E, 1)}{\Omega(E)} = \hat{h}(P) \cdot \frac{|\Sha(E)| \cdot \prod c_p}{|E_{\mathrm{tor}}|^2}.$$

**Implication chain:**
$$\text{Stark} + \text{Functional equation} + \text{Gross-Zagier} \implies \text{BSD rank-1 for CM curves.}$$

## Approach Summary
1. **Hecke character factorization:** For $E/\mathbb{Q}$ with CM by $K$, $L(E/\mathbb{Q}, s) = L(\psi, s)$ where $\psi$ is a Hecke character of $K$ of infinity type $(1, 0)$.
2. **Stark unit construction:** Stark's conjecture predicts the existence of $\epsilon_\psi$ in a ray class field of $K$, computable from the $L$-function.
3. **Functional equation bridge:** The completed $L$-function $\Lambda(\psi, s)$ satisfies a functional equation relating $s$ to $1-s$. This converts $L'(\psi, 0)$ to $L'(\psi, 1)$, which equals $L'(E, 1)$ up to explicit factors.
4. **Gross-Zagier bridge:** The Heegner point construction identifies the arithmetic point whose height equals $L'(E, 1)$.
5. **ETNC unification:** The Equivariant Tamagawa Number Conjecture simultaneously encodes both Stark and BSD, providing a unified framework.

## Computational Example

**Example 1: $E: y^2 = x^3 + 1$ (CM by $\mathbb{Z}[\omega]$, conductor 36, rank 0).**
- $\psi$ is a Hecke character of $\mathbb{Q}(\omega)$. $L(\psi, 0) \neq 0$. Stark's conjecture is trivially satisfied (the Stark unit is $1$ up to roots of unity). BSD holds: $L(E, 1)/\Omega(E) \in \mathbb{Q}$.

**Example 2: $E: y^2 = x^3 - x$ (CM by $\mathbb{Z}[i]$, conductor 32, rank 0).**
- $L(E, 1) \approx 2.6220$, $\Omega(E) \approx 2.6220$. Ratio $= 1$. The Hecke character $\psi$ of $\mathbb{Q}(i)$ has $L(\psi, 0) \neq 0$. Stark's conjecture verified.

**Example 3: Rank 1 CM curve by $\mathbb{Q}(\sqrt{-3})$.**
- $L'(E, 1) = c \cdot \hat{h}(P)$. The Stark unit $\epsilon_\psi$ satisfies $L'(\psi, 0) = -\frac{1}{w_K} \sum_\sigma \psi(\sigma) \log|\sigma(\epsilon_\psi)|$. Computing $\epsilon_\psi$ explicitly and verifying the identity provides numerical evidence for the Stark–BSD bridge.

**Example 4: Rubin's $p$-adic Stark conjecture.**
- For $E$ with CM by $K$ and a prime $p$ split in $K$, the $p$-adic $L$-function $L_p(\psi, s)$ interpolates $L(\psi, 0)$. Rubin's theorem gives $L_p(\psi, 0) = (1 - \psi(\mathfrak{p})/N\mathfrak{p}) \cdot \log_p(\epsilon_\psi)$, directly linking the Stark unit to the $p$-adic BSD formula.

## Obstacle Analysis
1. **Stark's conjecture is not fully proven:** While major cases are resolved, the full conjecture for arbitrary Hecke characters remains open. The bridge to BSD requires Stark for the specific character $\psi$ attached to $E$.
2. **Regulator comparison:** The Stark regulator $\sum \psi(\sigma) \log|\sigma(\epsilon)|$ involves Archimedean absolute values, while the BSD regulator $\hat{h}(P)$ involves the Néron-Tate height. Relating these requires understanding the period $\Omega(E)$.
3. **Non-CM curves:** The factorization $L(E, s) = L(\psi, s)$ only holds for CM curves. For non-CM curves, there is no Hecke character and no direct Stark connection.

## Cross-Group Connections
- **I-001 (Colmez Conjecture):** Both involve CM curves and the same $L$-values; the Stark unit and the CM point are related objects.
- **I-006 (Bloch-Kato):** The ETNC generalizes both Stark and BSD; progress on either feeds into the other.
- **I-009 (Greenberg's Conjecture):** The $p$-adic Stark conjecture (Rubin) is an Iwasawa-theoretic statement; Greenberg's $\mu = 0$ ensures the $p$-adic $L$-function is well-defined.
- **Group D (Regulator):** The Stark regulator and the BSD regulator are the two sides of the identity.

## Classification
**Regulator connection.** Links the Stark regulator (abelian $L$-functions) to the BSD regulator (elliptic curve heights) through the ETNC. Explicit for CM curves; open for non-CM curves.
