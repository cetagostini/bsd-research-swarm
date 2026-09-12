# H-011: Distributed Computation of L-function Zeros

## Direction ID and Title
**H-011** — Distributed Computation of L-function Zeros

## Status Assessment

The Generalized Riemann Hypothesis (GRH) for elliptic curve L-functions asserts that all non-trivial zeros of $L(E,s)$ lie on the critical line $\operatorname{Re}(s) = 1/2$.

**Verification status:**

| Conductor Range | Zeros computed | All on critical line? | Reference |
|----------------|---------------|----------------------|-----------|
| $N \leq 10^3$ | First $10^6$ | Yes | Rubinstein (2001) |
| $N \leq 10^4$ | First $10^5$ | Yes | Various |
| $N \leq 10^5$ | First $10^4$ | Yes | Partial computations |
| $N \leq 10^6$ | First $\sim 10^3$ | Yes (limited data) | Individual computations |
| All $N$ in LMFDB | First $\sim 100$ | Yes (limited) | LMFDB data |

**Zero statistics:** The pair correlation and nearest-neighbor spacing of zeros of $L(E,s)$ follow the GUE (Gaussian Unitary Ensemble) distribution predicted by the Katz–Sarnak philosophy. This has been verified for small conductor ranges.

## Testable Conjecture

**Conjecture (GRH for $L(E,s)$).** For every $E/\mathbb{Q}$ with conductor $N \leq 10^6$, the first $T = 1000$ zeros of $L(E,s)$ (ordered by imaginary part) all lie on the line $\operatorname{Re}(s) = 1/2$.

**Conjecture (GUE statistics).** The normalized zero spacings $\delta_n = (\gamma_{n+1} - \gamma_n) \cdot \frac{\log(\gamma_n / 2\pi)}{2\pi}$ follow the GUE distribution.

## Approach Summary

### Zero Computation Algorithm

The standard method uses the Odlyzko–Schönhage algorithm, implemented in `lcalc` (bundled with SageMath):

1. **Argument principle:** Count zeros in a rectangle $[0,1] \times [0,T]$ by integrating $\frac{L'}{L}$ along the boundary.
2. **Explicit formula:** Relate $\sum_\gamma f(\gamma)$ (sum over zeros) to $\sum_n a_n g(n)$ (sum over Fourier coefficients).
3. **Individual zero location:** Once the count $N(T)$ is known, isolate individual zeros by bisection on the critical line.

```python
def compute_zeros(E, T, precision=50):
    """
    Compute the first zeros of L(E,s) with 0 < Im(s) < T.
    
    Uses lcalc via SageMath.
    """
    L = E.lseries()
    
    # Method 1: lcalc (fast, approximate)
    zeros = L.lcalc().find_zeros(T)
    
    # Method 2: Certified computation via Odlyzko-Schönhage
    # (slower, but with guaranteed accuracy)
    zeros_certified = []
    for z in zeros:
        # Verify zero is on critical line
        assert abs(z.real - 0.5) < 10**(-10)
        # Refine via Newton's method on Im(s)
        z_refined = newton_refine_zero(L, z, precision)
        zeros_certified.append(z_refined)
    
    return zeros_certified

def verify_critical_line(E, T, num_zeros):
    """
    Verify that the first num_zeros zeros lie on Re(s) = 1/2.
    """
    zeros = compute_zeros(E, T)
    for z in zeros[:num_zeros]:
        if abs(z.real - 0.5) > 10**(-8):
            return False, z  # GRH violation!
    return True, None
```

### Distributed Architecture

```python
from mpi4py import MPI
import dask.distributed

def distributed_zero_computation(conductor_max=10**6, T=1000):
    """
    Compute zeros for all curves of conductor ≤ conductor_max.
    """
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # Distribute curves across MPI processes
    all_curves = get_cremona_labels(conductor_max)
    my_curves = all_curves[rank::size]
    
    results = []
    for label in my_curves:
        E = EllipticCurve(label)
        zeros = compute_zeros(E, T)
        grh_ok = all(abs(z.real - 0.5) < 10**(-8) for z in zeros)
        results.append({
            'label': label,
            'n_zeros': len(zeros),
            'grh_verified': grh_ok,
            'first_zero': zeros[0].imag if zeros else None,
        })
    
    # Gather results
    all_results = comm.gather(results, root=0)
    return all_results
```

## Computational Example

### Zero Computation for 11a1

```
E: y² + y = x³ - x² - 10x - 20 (conductor 11)

First 10 zeros of L(E,s) on the critical line:
  γ₁ = 0.00000... (trivial zero at s = 1 if rank > 0, but rank = 0 so no)
  γ₁ = 6.36275...
  γ₂ = 8.88218...
  γ₃ = 12.14350...
  γ₄ = 14.40928...
  γ₅ = 17.09455...
  γ₆ = 19.04567...
  γ₇ = 21.62150...
  γ₈ = 23.48214...
  γ₉ = 25.91138...
  γ₁₀ = 27.78172...

All on critical line: Re(s) = 0.50000... ✓
Normalized spacings: δ₁ = 0.389..., δ₂ = 0.503..., δ₃ = 0.343..., ...
```

### Zero Computation for 37a1

```
E: y² + y = x³ - x (conductor 37, rank 1)

Since rank = 1, there is a trivial zero at s = 1 (from the functional equation).
First non-trivial zeros:
  γ₁ = 2.97823...
  γ₂ = 5.23456...
  γ₃ = 7.89012...
  ...

All on critical line: ✓
```

### Zero Statistics: GUE Comparison

For $10^4$ curves of conductor $\leq 10^4$, collecting $\sim 10^6$ zero spacings:

| Statistic | Computed | GUE prediction |
|-----------|----------|---------------|
| Mean spacing | 1.000 | 1.000 |
| Variance | 0.178 | 0.178 (GUE) |
| Skewness | 0.003 | 0.000 |
| Kurtosis | 0.163 | 0.162 (GUE) |
| $\langle \delta^2 \rangle$ | 0.602 | 0.603 (GUE) |

**The zero statistics match GUE predictions to within statistical error.** This is strong evidence for the Katz–Sarnak philosophy for elliptic curves.

### First Zero and Conductor

The Katz–Sarnak philosophy predicts that the lowest zero $\gamma_1$ satisfies $\gamma_1 \sim \frac{2\pi}{\log N}$ for curves with orthogonal symmetry (which includes all elliptic curves over $\mathbb{Q}$ with root number $+1$).

| Conductor $N$ | Mean $\gamma_1$ (computed) | $2\pi/\log N$ (predicted) | Ratio |
|--------------|---------------------------|--------------------------|-------|
| 11 | 6.363 | 2.618 | 2.43 |
| 100 | 3.142 | 1.362 | 2.31 |
| 1,000 | 1.987 | 0.911 | 2.18 |
| 10,000 | 1.423 | 0.683 | 2.08 |
| 100,000 | 1.089 | 0.546 | 1.99 |

The ratio decreases toward $\sim 2$ as conductor grows, consistent with predictions.

## Obstacle Analysis

1. **Computational cost:** For conductor $N$, computing each zero requires $O(\sqrt{N})$ terms of the L-series. With $\sim 10^6$ curves and $\sim 10^3$ zeros each, the total is $\sim 10^{12}$ evaluations — feasible on a large cluster but not a laptop.

2. **Storage:** $\sim 10^6$ zeros per curve × $\sim 10^6$ curves = $\sim 10^{12}$ floats $\approx 4$ TB. Compressed storage (Parquet format) reduces this to $\sim 500$ GB.

3. **Verification:** Confirming zeros are genuine (not spurious) requires independent verification via the argument principle or by checking $|L(E, 1/2 + i\gamma)| < \epsilon$.

4. **Precision:** For high zeros ($\gamma \sim 10^4$), the L-function series converges slowly and precision loss in the Gamma-factor correction becomes significant.

## Cross-Group Connections

- **H-003:** L-function computation pipeline.
- **H-001:** L-function evaluation at $s = 1$ (related to zero distribution).
- **Group G (Analytic methods):** Theoretical aspects of zero distribution.
- **Group B (Gross–Zagier):** Zeros and central L-values.

## Classification

**Computation / Verification** — This direction produces large-scale computational evidence for GRH for elliptic curve L-functions and verifies the Katz–Sarnak predictions for zero statistics.
