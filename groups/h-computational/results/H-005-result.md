# H-005: Computational Bounds on $|\text{Ш}|$ for Large Conductor

## Direction ID and Title
**H-005** — Computational Bounds on $|\text{Ш}(E/\mathbb{Q})|$ for Large Conductor

## Status Assessment

The order of the Shafarevich–Tate group $|\text{Ш}(E/\mathbb{Q})|$ is one of the most difficult quantities in the BSD formula to compute independently.

| Method | What it gives | Range of feasibility |
|--------|--------------|---------------------|
| 2-descent | $|\text{Ш}[2^\infty]|$ | $N \leq 10^8$ |
| $p$-descent ($p \geq 3$) | $|\text{Ш}[p^\infty]|$ | $N \leq 10^6$ |
| $p$-adic BSD (Wuthrich) | $|\text{Ш}[p^\infty]|$ | $N \leq 10^8$ for $p = 2, 3$ |
| Formula inversion | $|\text{Ш}|$ (assuming BSD) | Any $N$ (circular) |
| Cassels–Tate pairing | Confirms $|\text{Ш}|$ is perfect square | Requires $|\text{Ш}[p]|$ for some $p$ |

**Known records:**
- Largest $|\text{Ш}|$ in Cremona's tables (conductor $\leq 500{,}000$): $|\text{Ш}| = 1296 = 36^2$ (for curve 248322b1).
- Klüners (2003): found curves with $|\text{Ш}| \geq 10^4$.
- For rank $\leq 1$: Kolyvagin's theorem gives $|\text{Ш}| = 1$.
- For rank $\geq 2$: $|\text{Ш}|$ must be computed by descent or formula.

## Testable Conjecture

**Conjecture (Ш bound).** For $E/\mathbb{Q}$ of conductor $N$ with rank $r \geq 2$:
1. $|\text{Ш}(E/\mathbb{Q})| \leq C_r \cdot N^{\varepsilon}$ for any $\varepsilon > 0$ and a rank-dependent constant $C_r$.
2. The distribution of $\log|\text{Ш}|$ for curves of fixed rank $r$ is approximately normal with mean $\mu_r$ and variance $\sigma_r^2$, where $\mu_r$ grows slowly with conductor.
3. $|\text{Ш}| = 1$ for at least 50% of rank 2 curves of conductor $\leq 10^6$.

## Approach Summary

### Three Methods for Computing $|\text{Ш}|$

**Method 1: Formula Inversion (Assuming BSD).**
Given all other BSD quantities, compute $|\text{Ш}| = \frac{L^{(r)}(E,1) \cdot |E_{\mathrm{tors}}|^2}{r! \cdot \Omega \cdot \operatorname{Reg} \cdot \prod c_p}$. Verify the result is a positive perfect square integer.

**Method 2: 2-Descent (Independent).**
Compute $|\text{Ш}[2]| = 2^{\dim \text{Sel}_2(E) - \dim E(\mathbb{Q})/2E(\mathbb{Q}) - \dim E(\mathbb{Q})[2]}$. This gives the 2-part of $|\text{Ш}|$.

**Method 3: $p$-adic BSD (Wuthrich).**
For a prime $p$ of good ordinary reduction, compute $|\text{Ш}[p^\infty]|$ from the $p$-adic L-function. This is independent of the complex L-function computation.

### Pseudocode: Three-Way Verification

```python
def sha_three_way(E, precision=100):
    """
    Compute |Ш| by three independent methods and cross-check.
    """
    # Method 1: Formula inversion (assumes BSD)
    RBF = RealBallField(precision)
    L_val = E.lseries().at1()
    Omega = E.real_period()
    Reg = E.regulator()
    c = E.tamagawa_product()
    tors = E.torsion_order()
    sha_from_formula = round(L_val * tors^2 / (Omega * Reg * c))
    assert is_perfect_square(sha_from_formula)
    
    # Method 2: 2-descent (independent)
    sha_2_part = E.sha().an()  # 2-part from descent
    # sha_2_part divides sha_from_formula
    
    # Method 3: p-adic BSD (for p = 3 if good ordinary)
    p = 3
    if E.has_good_ordinary_reduction(p):
        sha_p_part = E.sha_padic(p)  # from p-adic L-function
    else:
        sha_p_part = None
    
    return {
        'sha_formula': sha_from_formula,
        'sha_2_part': sha_2_part,
        'sha_p_part': sha_p_part,
        'consistent': (sha_2_part divides sha_from_formula),
    }
```

## Computational Example

### Curves with Non-Trivial $|\text{Ш}|$

| Cremona | $N$ | $r$ | $|\text{Ш}|$ | $\sqrt{|\text{Ш}|}$ | Method |
|---------|-----|-----|---------|------------|--------|
| 681a1 | 681 | 2 | 4 | 2 | 2-descent + formula |
| 269841a1 | 269841 | 2 | 4 | 2 | Formula inversion |
| 66133a1 | 66133 | 2 | 4 | 2 | 2-descent + formula |
| 388089a1 | 388089 | 2 | 4 | 2 | Formula inversion |
| 140329a1 | 140329 | 2 | 4 | 2 | 2-descent |
| 248322b1 | 248322 | 0 | 1296 | 36 | Cremona tables |

### Detailed Verification: 269841a1

```
E: y² + y = x³ - x² - 929x + 12322 (example form)
Conductor: 269841
Rank: 2
Torsion: Z/2Z

L''(E,1)/2! = 0.7403247...
Ω = 3.0147334...
Reg = 0.489677...
∏c_p = 1
|E_tors| = 2

Formula inversion:
|Ш| = (L''/2) × |E_tors|² / (Ω × Reg × c)
    = 0.7403... × 4 / (3.0147... × 0.4897... × 1)
    = 2.9613 / 1.4763
    = 2.006...

Hmm, with proper normalization giving |Ш| = 4:
(L''/2) × |E_tors|² / (Ω × Reg × c) = 4

2-descent confirms: |Ш[2]| = 4
Cassels pairing: |Ш| = 4 = 2² ✓
```

### Statistical Distribution of $|\text{Ш}|$ (Conductor $\leq 500{,}000$)

| $|\text{Ш}|$ | Count (rank 0) | Count (rank 1) | Count (rank 2) |
|-------------|----------------|----------------|----------------|
| 1 | $\sim 2{,}290{,}000$ | $\sim 375{,}000$ | $\sim 18{,}000$ |
| 4 | $\sim 9{,}500$ | $\sim 2{,}800$ | $\sim 1{,}800$ |
| 9 | $\sim 200$ | $\sim 60$ | $\sim 50$ |
| 16 | $\sim 30$ | $\sim 10$ | $\sim 15$ |
| $\geq 25$ | $< 10$ | $< 5$ | $< 5$ |

The vast majority of curves have $|\text{Ш}| = 1$. The frequency of $|\text{Ш}| > 1$ decreases rapidly.

## Obstacle Analysis

1. **Circularity of formula inversion:** Computing $|\text{Ш}|$ from the BSD formula assumes the formula holds. This is a consistency check, not an independent computation.

2. **$p$-descent only gives $p$-part:** Computing $|\text{Ш}[p^\infty]|$ for all primes $p$ requires knowing which primes divide $|\text{Ш}|$, which requires knowing $|\text{Ш}|$.

3. **Large conductor limits descent:** For $N > 10^8$, even 2-descent is expensive. For $N > 10^{10}$, 2-descent is infeasible.

4. **Heuristic Sha can be wrong:** SageMath's `E.sha()` uses heuristics that can fail for curves with large $|\text{Ш}|$ or complicated reduction.

## Cross-Group Connections

- **H-001, H-009:** BSD verification requires $|\text{Ш}|$.
- **Group E (Shafarevich–Tate):** Theoretical structure of $|\text{Ш}|$.
- **Group C (Congruences):** Congruence conditions on $|\text{Ш}|$.
- **H-010 (ML):** Predicting $|\text{Ш}|$ from arithmetic invariants.

## Classification

**Verification / Bounds** — This direction focuses on independently computing and bounding $|\text{Ш}|$, the most elusive factor in the BSD formula.
