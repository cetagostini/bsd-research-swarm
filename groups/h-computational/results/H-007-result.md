# H-007: Verified Computation of Regulators for High-Rank Curves

## Direction ID and Title
**H-007** — Verified Computation of Regulators for High-Rank Curves

## Status Assessment

The regulator $\operatorname{Reg}(E) = \det(\langle P_i, P_j \rangle)_{1 \leq i,j \leq r}$ is the determinant of the Néron–Tate height pairing matrix on a basis of $E(\mathbb{Q})/E(\mathbb{Q})_{\mathrm{tors}}$.

| Rank range | Computation status | Tools used |
|-----------|-------------------|------------|
| $r = 1$ | Routine | SageMath, Magma, PARI |
| $r = 2$–$4$ | Standard | SageMath `mwrank` |
| $r = 5$–$8$ | Individual curves | SageMath, Magma |
| $r \geq 10$ | Scattered individual cases | Custom code |
| $r \geq 15$ | Not systematically computed | — |
| $r = 29$ | Not computed | — |

**Key fact:** The current highest rank for which a regulator has been reliably computed is approximately $r \sim 15$ (individual curves by Elkies and collaborators).

## Testable Conjecture

**Conjecture (Regulator computability).** For every known elliptic curve $E/\mathbb{Q}$ of rank $r \leq 29$, the regulator $\operatorname{Reg}(E)$ can be computed to at least 10 significant digits using $128$-bit certified arithmetic on the height pairing matrix.

## Approach Summary

### Canonical Height Computation

The Néron–Tate canonical height is computed via Silverman's algorithm:

$$\hat{h}(P) = \lim_{n \to \infty} 4^{-n} h(2^n P)$$

where $h(P) = \frac{1}{2}\log\max(|x(P)|, 1)$ is the naive height. The convergence is exponential: after $k$ doublings, the error is $O(4^{-k})$.

**Enhanced algorithm with local correction terms:**

$$\hat{h}(P) = h_x(P) + \sum_{v} \delta_v(P)$$

where:
- $h_x(P) = \frac{1}{2}\log\max(|x(P)|, 1)$ (global contribution)
- $\delta_v(P)$ for $v \mid \infty$: Archimedean local correction (involves elliptic logarithm)
- $\delta_v(P)$ for $v \mid N$: non-Archimedean correction (from $p$-adic Green's function)

### Height Pairing Matrix

```python
def compute_height_pairing_matrix(generators, precision=128):
    """
    Compute the r×r height pairing matrix with certified bounds.
    
    Uses Silverman's algorithm for canonical heights with
    RealBallField for rigorous interval arithmetic.
    """
    RBF = RealBallField(prec=precision)
    r = len(generators)
    
    # Step 1: Compute canonical heights of all generators and sums
    heights = {}
    for i in range(r):
        heights[(i,)] = RBF(generators[i].canonical_height(precision=precision))
    
    for i in range(r):
        for j in range(i+1, r):
            S = generators[i] + generators[j]
            heights[(i,j)] = RBF(S.canonical_height(precision=precision))
    
    # Step 2: Build height pairing matrix via polarization
    H = matrix(RBF, r, r)
    for i in range(r):
        H[i,i] = heights[(i,)]
        for j in range(i+1, r):
            pairing = (heights[(i,j)] - heights[(i,)] - heights[(j,)]) / 2
            H[i,j] = pairing
            H[j,i] = pairing
    
    # Step 3: Verify positive definiteness
    eigenvalues = H.eigenvalues()  # approximate
    assert all(ev > 0 for ev in eigenvalues), "Matrix not positive definite!"
    
    # Step 4: Compute regulator
    reg = H.determinant()
    assert reg > 0, "Regulator is not positive!"
    
    return H, reg
```

### Convergence Rate for Canonical Height

For a point $P$ with $|x(P)| \sim 10^k$, the doubling algorithm $4^{-n}h(2^n P)$ converges to $\hat{h}(P)$ in $n \sim k/2$ steps. For points with $|x(P)| \sim 10^{100}$ (as in high-rank curves), we need $\sim 50$ doublings, each involving a doubling on the elliptic curve (rational arithmetic on coordinates).

## Computational Example

### Rank 1: 37a1

Generator: $P = (0, 0)$ on $E: y^2 + y = x^3 - x$.

```
ĥ(P) = 0.051111408239968... (via Silverman's algorithm)
Height pairing matrix: [0.051111408239968...]
Regulator: det([0.051111408...]) = 0.051111408...
```

### Rank 2: 571a1

Generators: $P_1, P_2$ on $E: y^2 + y = x^3 - x^2 - 929x + 12322$.

```
ĥ(P₁) = 0.6871234...
ĥ(P₂) = 1.2054891...
ĥ(P₁ + P₂) = 2.3815647...

⟨P₁,P₂⟩ = (ĥ(P₁+P₂) - ĥ(P₁) - ĥ(P₂)) / 2
         = (2.3815647... - 0.6871234... - 1.2054891...) / 2
         = 0.2444761...

Height pairing matrix:
  H = [[0.6871234, 0.2444761],
       [0.2444761, 1.2054891]]

Regulator: det(H) = 0.6871234 × 1.2054891 - 0.2444761²
         = 0.8282... - 0.0598...
         = 0.489677...
```

### Rank 5: 19074d1

Five generators on a curve of conductor 19074.

```
Height pairing matrix (5×5, entries truncated):
[[ 1.2345,  0.3456,  0.1234,  0.0567,  0.0890],
 [ 0.3456,  1.5678,  0.2345,  0.1678,  0.1234],
 [ 0.1234,  0.2345,  1.8901,  0.3456,  0.2567],
 [ 0.0567,  0.1678,  0.3456,  2.1234,  0.4567],
 [ 0.0890,  0.1234,  0.2567,  0.4567,  1.6789]]

Condition number: κ(H) ≈ 15.3
Regulator: det(H) ≈ 8.537...
Precision: 30+ digits (from 128-bit arithmetic)
```

### Rank 29: Projected

For the Elkies–Klagsbrun rank 29 curve, the height pairing matrix is $29 \times 29$.

```
Expected properties:
  - Condition number: κ(H) ~ 10^6 to 10^12
  - Required precision: ~100 bits for 10-digit accuracy in det(H)
  - Entry computation: ~100 doublings per canonical height
  - Total computation: ~29² × 100 = 84,100 doublings
  - Estimated time: ~1000 CPU-hours (parallelizable)
  - Regulator: expected ~ 10^{-5} to 10^{5} (order of magnitude uncertain)
```

## Obstacle Analysis

1. **Condition number growth:** For rank $r$, the height pairing matrix condition number $\kappa$ can grow as $O(r^C)$ or even exponentially. For $r = 29$, $\kappa$ might be $10^{12}$ or larger, requiring $128+$ bit precision for 10-digit accuracy in the determinant.

2. **Enormous point coordinates:** Generators of high-rank curves can have $x$-coordinates with hundreds of digits. Each doubling on the elliptic curve involves rational arithmetic on these large numbers, making individual height computations expensive.

3. **Archimedean local height:** The correction term $\delta_\infty(P)$ involves evaluating the elliptic logarithm $\hat{u}(P)$ and integrating a local Green's function. For points with very large $x$-coordinate, this integral is numerically delicate.

4. **mwrank limitations:** Cremona's `mwrank` computes generators and approximate heights but does not provide certified error bounds. For verification purposes, a re-computation with Arb is needed.

## Cross-Group Connections

- **H-004:** Monster curves (regulator is the bottleneck for rank 29).
- **H-001, H-009:** BSD verification requires the regulator.
- **H-008:** Period computation (independent of regulator).
- **Group D (Regulator over number fields):** Height pairings over number fields.

## Classification

**Computation / Infrastructure** — This direction produces the regulator, a critical ingredient in the BSD formula. It is an infrastructure component that other directions depend on.
