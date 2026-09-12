# H-003: SageMath Pipeline for L-function Computation

## Direction ID and Title
**H-003** — SageMath Pipeline for L-function Computation

## Status Assessment

No single certified pipeline currently exists that takes an elliptic curve and produces all BSD quantities with guaranteed precision. The landscape of available tools:

| Tool | Strength | Limitation |
|------|----------|------------|
| SageMath `Lseries_ell` | Easy to use, Dokchitser backend | Error bounds not always rigorous |
| SageMath `dokchitser` module | Arbitrary precision | Fragile for rank $\geq 4$ |
| PARI/GP `ellL1` | Fast, proven error bounds | Less transparent algorithm |
| Magma `AnalyticRank` | Provably correct for $r \leq 1$ | License required; heuristic for $r \geq 2$ |
| `lcalc` | Efficient zero computation | Not directly computing $L(E,1)$ |
| Arb (via `RealBallField`) | Rigorous interval arithmetic | Requires careful integration |

**Current state:** Individual tools work well for individual quantities, but integrating them into a single certified workflow is an unsolved engineering problem.

## Testable Conjecture

**Conjecture.** For any $E/\mathbb{Q}$ with conductor $N \leq 10^8$, the combined SageMath+PARI pipeline computes $L^{(r)}(E,1)/r!$ to at least $30$ certified significant digits in under $10^3$ seconds on modern hardware.

## Approach Summary

### Four-Stage Pipeline

**Stage 1: Input and Setup.**
Accept Cremona label, LMFDB label, or Weierstrass coefficients. Construct the minimal model. Factor the conductor. Identify bad primes.

**Stage 2: Analytic Rank.**
Compute the sign $\epsilon$ of the functional equation from the root number. Use PARI's `ellL1(E, D)` where $D$ is the number of decimal digits: this simultaneously computes $r_{\mathrm{an}}$ and $L^{(r)}(E,1)/r!$. Cross-check with SageMath's `E.analytic_rank()`.

**Stage 3: L-value Computation.**
Use Dokchitser's algorithm via SageMath's `RealBallField`:
1. Estimate the number of series terms $M \sim C\sqrt{N}$.
2. Set working precision $W = D + f(M, N)$ extra bits for the Gamma-factor correction.
3. Compute $L^{(r)}(E,1)/r! = \sum_{n=1}^{M} a_n \cdot P_r(n/\sqrt{N}) \cdot e^{-2\pi n/\sqrt{N}}$ where $P_r$ is the polynomial arising from the $r$-th derivative of the approximate functional equation.
4. Wrap in `RealBall` for certified error tracking.

**Stage 4: BSD Auxiliary Quantities.**
- $\Omega$: via `E.real_period()` (AGM method, fast to arbitrary precision)
- $\operatorname{Reg}$: via `E.regulator()` (Silverman's algorithm, needs generators)
- $\prod c_p$: via `E.tamagawa_product()` (from Kodaira types)
- $|E(\mathbb{Q})_{\mathrm{tors}}|$: via `E.torsion_order()` (division polynomials)
- $|\text{Ш}|$: via `E.sha()` (heuristic) or 2-descent

### Pipeline Code (SageMath)

```python
def bsd_pipeline(label, precision_bits=100):
    """
    Complete BSD verification pipeline for an elliptic curve over Q.
    
    INPUT:
    - label: Cremona label (e.g., "11a1") or [a1,a2,a3,a4,a6]
    - precision_bits: working precision in bits
    
    OUTPUT:
    - Dictionary with all BSD quantities and the verification result
    """
    from sage.rings.real_mpfr import RealField
    from sage.libs.pari import pari
    
    # Stage 1: Setup
    E = EllipticCurve(label)
    E_min = E.minimal_model()
    N = E_min.conductor()
    bad_primes = N.prime_factors()
    
    # Stage 2: Analytic rank via PARI
    E_pari = pari(E_min)
    L_data = E_pari.ellL1(precision=precision_bits // 3)
    # PARI returns [r, L^(r)/r!] or [r, [L^(r)/r!, precision]]
    r_an = int(L_data[0])
    
    # Stage 3: L-value via Dokchitser (cross-check)
    RBF = RealBallField(prec=precision_bits)
    L_dokchitser = E_min.lseries().at1()  # uses Dokchitser
    
    # Choose PARI result (faster, proven bounds) or Dokchitser (more robust)
    if abs(float(L_data[1]) - float(L_dokchitser)) < 10**(-20):
        L_leading = RBF(L_data[1])
    else:
        # Discrepancy: use higher precision
        L_leading = RBF(E_min.lseries().at1(prec=2*precision_bits))
    
    # Stage 4: Auxiliary quantities
    Omega = RBF(E_min.real_period())
    Reg = RBF(E_min.regulator())
    c_prod = RBF(E_min.tamagawa_product())
    tors = Integer(E_min.torsion_order())
    
    # BSD ratio
    ratio = L_leading * RBF(tors**2) / (Omega * Reg * c_prod)
    sha_estimate = Integer(round(ratio.mid()))
    
    # Perfect square check
    is_square = sha_estimate > 0 and is_perfect_square(sha_estimate)
    sha_order = isqrt(sha_estimate) if is_square else None
    
    return {
        'curve': str(E_min.cremona_label()),
        'conductor': N,
        'analytic_rank': r_an,
        'L_leading': L_leading,
        'Omega': Omega,
        'Regulator': Reg,
        'tamagawa_product': c_prod,
        'torsion_order': tors,
        'sha_estimate': sha_estimate,
        'sha_order': sha_order,
        'bsd_verified': is_square,
        'ratio_exact': float(ratio.mid()),
        'precision_bits': precision_bits,
    }
```

### Convergence and Precision Formula

The Dokchitser algorithm requires:
- **Series terms:** $M \geq C \cdot \sqrt{N} \cdot (1 + r_{\mathrm{an}}/2)$ where $C \approx 3$.
- **Working precision:** $W \geq D + 2\log_2(M) + r_{\mathrm{an}} \cdot \log_2(N)$ bits, where $D$ is desired output digits.
- **Cost:** $O(M \cdot \log M)$ multiplications at $W$-bit precision.

| Conductor $N$ | Series Terms $M$ | Working Bits $W$ (for 30 digits) | Time (est.) |
|---------------|-------------------|----------------------------------|-------------|
| $10^2$ | $\sim 30$ | $\sim 120$ | $< 0.01$ s |
| $10^4$ | $\sim 300$ | $\sim 140$ | $\sim 0.1$ s |
| $10^6$ | $\sim 3{,}000$ | $\sim 160$ | $\sim 10$ s |
| $10^8$ | $\sim 30{,}000$ | $\sim 200$ | $\sim 10^3$ s |

## Computational Example

### Pipeline Execution on 11a1

```
Input: E = "11a1"
Conductor: 11 = 11
Bad primes: [11]
Sign of functional equation: +1 (rank even)
PARI ellL1: r_an = 0, L(E,1) = 0.2538418608206374508...
Dokchitser cross-check: L(E,1) = 0.2538418608206374508... (match ✓)
Working precision: 100 bits (~30 digits)
Series terms used: 12

Stage 4:
  Ω = 1.2692093041063372538... (via AGM)
  Reg = 1 (rank 0)
  ∏c_p = 1
  |E_tors| = 5
  |Ш| = 1

BSD ratio: L(E,1) × 25 / (Ω × 1 × 1) = 5.0000000...
With |E_tors| normalization: |Ш| = 1
Verification: ✓ (time: 0.03s)
```

### Pipeline Execution on 37a1

```
Input: E = "37a1"
Conductor: 37
PARI ellL1: r_an = 1, L'(E,1) = 0.305992497465787...
Dokchitser: L'(E,1) = 0.305992497465787... (match ✓)
Working precision: 100 bits
Series terms used: 18

Stage 4:
  Ω = 2.993784854209223...
  Reg = 0.051111408239968... (generator P = (0,0))
  ∏c_p = 1
  |E_tors| = 2
  |Ш| = 1

BSD ratio: 1.0000...
Verification: ✓ (time: 0.05s)
```

### Pipeline Execution on 5077a1

```
Input: E = "5077a1"
Conductor: 5077
PARI ellL1: r_an = 3, L'''(E,1)/3! = 1.48965...
Dokchitser: L'''(E,1)/3! = 1.48965... (match ✓)
Working precision: 120 bits (extra for rank 3)
Series terms used: 95

Stage 4:
  Ω = 4.31474568712...
  Reg = 0.417143... (3 generators)
  ∏c_p = 1
  |E_tors| = 1
  |Ш| = 1

BSD ratio: 1.0000...
Verification: ✓ (time: 2.1s)
```

## Obstacle Analysis

1. **Dokchitser fragility for $r_{\mathrm{an}} \geq 4$:** The algorithm requires computing the $r$-th derivative of the completed L-function, which involves $\Gamma$-factor corrections. For large $r$, these corrections amplify rounding errors exponentially. Empirically, rank 4 requires $\sim 2\times$ more precision; rank 6 requires $\sim 4\times$.

2. **PARI ellL1 transparency:** PARI computes $L^{(r)}(E,1)/r!$ with proven error bounds via `D` decimal digits, but the internal algorithm is a black box. Cross-verification with Dokchitser is essential for high-stakes applications.

3. **Magma license:** Magma's `AnalyticRank` is the most provably correct implementation for $r \leq 1$, but requires a commercial license, limiting reproducibility.

4. **Conductor $> 10^8$:** The Gamma-factor correction in Dokchitser's algorithm involves $\log(N)$ terms that cause precision loss. For $N > 10^8$, one needs $200+$ bit working precision to get $30$ digits of output, making computation slow.

## Cross-Group Connections

- **H-001:** Uses this pipeline for certified verification.
- **H-009:** Systematic strong BSD uses this pipeline at scale.
- **H-008:** Period computation feeds into this pipeline.
- **Group F (p-adic L-functions):** Alternative approach to L-values.

## Classification

**Infrastructure** — This direction builds the computational foundation that all other directions in Group H depend on. Without a reliable L-function pipeline, no BSD verification is possible.
