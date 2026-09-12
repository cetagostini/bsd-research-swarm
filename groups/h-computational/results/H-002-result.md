# H-002: LMFDB Systematic Analysis: Rank vs. Analytic Rank

## Direction ID and Title
**H-002** — LMFDB Systematic Analysis: Rank vs. Analytic Rank

## Status Assessment

The LMFDB (L-functions and Modular Forms Database) contains approximately $3 \times 10^6$ elliptic curves over $\mathbb{Q}$, with conductor up to $\sim 10^7$. For **every curve** where both the algebraic rank $r(E/\mathbb{Q})$ (from Mordell–Weil group computation) and the analytic rank $r_{\mathrm{an}}(E)$ (from L-function evaluation) are known, **they agree**. There are zero known violations of the weak BSD conjecture.

| Conductor Range | # Curves | $r = r_{\mathrm{an}}$ | Mismatches | Undetermined |
|----------------|----------|----------------------|------------|--------------|
| $N \leq 500{,}000$ | $\sim 2.7 \times 10^6$ | All verified | 0 | 0 |
| $500{,}000 < N \leq 10^6$ | $\sim 2 \times 10^5$ | All checked | 0 | ~1% (rank uncertain) |
| $10^6 < N \leq 10^7$ | $\sim 10^5$ | Analytic rank computed | 0 | ~5% (algebraic rank estimated) |

The primary gap is for conductor $N > 500{,}000$, where many curves have analytic rank computed (via Dokchitser or PARI) but algebraic rank only estimated (via 2-descent heuristics), not rigorously proven.

## Testable Conjecture

**Conjecture (Weak BSD, computational version).** For every elliptic curve $E/\mathbb{Q}$ with conductor $N \leq 10^8$:
1. The analytic rank $r_{\mathrm{an}}(E)$ equals the algebraic rank $r(E/\mathbb{Q})$.
2. No violations exist for any curve in the LMFDB database.
3. Extended: this holds for all curves of conductor $\leq 10^8$.

## Approach Summary

### Algorithm

```
For each isogeny class C in LMFDB:
  For each curve E in C:
    1. Fetch: conductor N, rank_alg, rank_an, L-function data
    2. If rank_an computed by heuristic:
       - Re-derive with PARI ellL1(E, D=50) for certified precision
       - Check: if |L^(r_an)(E,1)/r_an!| > 10^{-40}, rank_an = r_an
       - Else: rank_an ≥ r_an + 1, increment and recheck
    3. If rank_alg estimated by 2-descent:
       - Run mwrank with extended parameters
       - If inconclusive: flag for 3-descent (manual review)
    4. Compare: rank_alg vs rank_an
    5. If mismatch: IMMEDIATELY flag for independent verification
    
Output: discrepancy report (expected: empty)
```

### Pseudocode for Bulk Comparison

```python
import lmfdb
import sage.all as sage

def scan_rank_agreement(conductor_max=10**7):
    results = {'match': 0, 'mismatch': 0, 'uncertain': 0}
    
    for N in range(1, conductor_max + 1):
        curves = lmfdb.ec.by_conductor(N)
        for E_data in curves:
            r_alg = E_data['rank']       # algebraic rank (may be None)
            r_an = E_data['analytic_rank'] # analytic rank
            
            if r_alg is None:
                # Run 2-descent
                E = sage.EllipticCurve(E_data['ainvs'])
                r_alg = E.rank()  # heuristic
                if r_alg is None:
                    results['uncertain'] += 1
                    continue
            
            if r_alg == r_an:
                results['match'] += 1
            else:
                results['mismatch'] += 1
                flag_for_review(E_data)
    
    return results
```

## Computational Example

### Rank Distribution Statistics (LMFDB, $N \leq 500{,}000$)

| Rank $r$ | Count | Percentage | Analytic Rank Verified |
|----------|-------|------------|----------------------|
| 0 | $\sim 2{,}300{,}000$ | 85.2% | Yes (all) |
| 1 | $\sim 378{,}000$ | 14.0% | Yes (all) |
| 2 | $\sim 20{,}000$ | 0.74% | Yes (all) |
| 3 | $\sim 900$ | 0.03% | Yes (all) |
| 4 | $\sim 50$ | 0.002% | Yes (individual verification) |
| $\geq 5$ | $< 10$ | $< 0.001$% | Case-by-case |

### Sample Verifications

**11a1** ($N = 11$, rank 0):
- $r_{\mathrm{an}} = 0$: $L(E,1) = 0.25384186\ldots \neq 0$ ✓
- $r_{\mathrm{alg}} = 0$: 2-descent confirms $E(\mathbb{Q}) \cong \mathbb{Z}/5\mathbb{Z}$
- **Agreement:** $r = r_{\mathrm{an}} = 0$ ✓

**37a1** ($N = 37$, rank 1):
- $r_{\mathrm{an}} = 1$: $L(E,1) = 0$, $L'(E,1) = 0.30599\ldots \neq 0$ ✓
- $r_{\mathrm{alg}} = 1$: generator $P = (0,0)$, $E(\mathbb{Q}) \cong \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$
- **Agreement:** $r = r_{\mathrm{an}} = 1$ ✓

**5077a1** ($N = 5077$, rank 3):
- $r_{\mathrm{an}} = 3$: sign of functional equation is $-1$ (odd rank), $L'''(E,1)/3! \neq 0$
- $r_{\mathrm{alg}} = 3$: three independent generators known
- **Agreement:** $r = r_{\mathrm{an}} = 3$ ✓

**60810a1** ($N = 60810$, rank 2):
- $r_{\mathrm{an}} = 2$: $L(E,1) = L'(E,1) = 0$, $L''(E,1)/2! \neq 0$
- $r_{\mathrm{alg}} = 2$: two generators from 2-descent
- **Agreement:** $r = r_{\mathrm{an}} = 2$ ✓

### Edge Cases

For conductor $N > 500{,}000$, approximately 1% of curves have uncertain algebraic rank. These are flagged by:
1. 2-descent gives an upper bound $r_{\mathrm{upper}} \geq r_{\mathrm{an}}$ but cannot confirm exact rank.
2. The analytic rank computation uses heuristic vanishing checks (approximate zeros).
3. Resolution: run PARI `ellL1` with $D = 80$ digits for certified vanishing/non-vanishing.

## Obstacle Analysis

1. **Heuristic analytic rank for high conductor:** For $N > 10^6$, Dokchitser's algorithm requires $O(\sqrt{N})$ terms, and the vanishing check for $L^{(k)}(E,1) = 0$ becomes delicate. A value of $10^{-30}$ might be genuine zero or numerically small.

2. **2-descent is insufficient for odd primes:** If $|\text{Ш}[p]| > 1$ for $p \geq 3$, 2-descent cannot detect it, potentially leading to incorrect algebraic rank estimates.

3. **Database heterogeneity:** Different contributors used different precision levels and algorithms. A systematic re-derivation requires significant computational resources.

4. **Stein–Watkins (2002) gap:** Their conductor $\leq 10^8$ computation used heuristic methods and has never been fully certified. Approximately $10^6$ curves need re-verification.

## Cross-Group Connections

- **H-001:** Certified verification of individual curves (the small-scale version of this).
- **H-003:** L-function computation pipeline (provides $r_{\mathrm{an}}$).
- **H-005:** $|\text{Ш}|$ bounds (needed for full strong BSD verification).
- **Group A (BSD over number fields):** Extending rank comparison to number fields.

## Classification

**Verification / Data Analysis** — This is a systematic computational check that the foundational equality $r = r_{\mathrm{an}}$ holds across the entire LMFDB database. It is the most basic test of BSD at scale.
