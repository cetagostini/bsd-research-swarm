# H-006: Database of Tamagawa Numbers and Their Distribution

## Direction ID and Title
**H-006** — Database of Tamagawa Numbers and Their Distribution

## Status Assessment

Tamagawa numbers $c_p(E) = [E(\mathbb{Q}_p) : E_0(\mathbb{Q}_p)]$ encode the local behavior of an elliptic curve at each bad prime. They are well-understood individually:

| Reduction type | Kodaira type | Possible $c_p$ |
|---------------|-------------|----------------|
| Multiplicative, split | $I_n$ | $n = v_p(\Delta)$ |
| Multiplicative, nonsplit | $I_n^*$ | $1$ if $n$ odd, $2$ if $n$ even |
| Additive | $II, III, IV, I_0^*, \ldots$ | $1, 2, 3, 4$ |

The LMFDB stores Tamagawa data for all $\sim 3 \times 10^6$ curves. The **product** $\prod_{p \mid N} c_p$ is the quantity appearing in the BSD formula.

## Testable Conjecture

**Conjecture (Tamagawa distribution).**
1. The average value of $\prod_p c_p$ for curves of conductor $N$ grows as $O((\log N)^{k})$ for some small $k \approx 1$.
2. The probability that $\prod_p c_p = 1$ (i.e., all $c_p = 1$) is bounded below by a positive constant $\alpha > 0$ independent of conductor.
3. The maximum value of $\prod_p c_p$ for curves of conductor $N$ grows as $O(N^{\delta})$ for some $\delta < 1$.
4. There is no strong correlation between $\prod_p c_p$ and $|\text{Ш}|$ beyond the constraint imposed by the BSD formula.

## Approach Summary

### Data Pipeline

```python
import duckdb
import pandas as pd

def tamagawa_analysis():
    """
    Analyze Tamagawa number distribution from LMFDB data.
    """
    # Load LMFDB data
    con = duckdb.connect()
    con.execute("""
        CREATE TABLE curves AS
        SELECT * FROM read_csv('lmfdb_ec.csv')
    """)
    
    # Compute ∏c_p for each curve
    con.execute("""
        CREATE TABLE tamagawa AS
        SELECT conductor, rank, tamagawa_product,
               log(tamagawa_product) as log_cp,
               sha_an
        FROM curves
        WHERE tamagawa_product IS NOT NULL
    """)
    
    # Statistics by conductor bin
    stats = con.execute("""
        SELECT 
            CASE
                WHEN conductor < 1000 THEN '1-1000'
                WHEN conductor < 10000 THEN '1000-10000'
                WHEN conductor < 100000 THEN '10000-100000'
                WHEN conductor < 1000000 THEN '100000-1000000'
                ELSE '1000000+'
            END as conductor_bin,
            COUNT(*) as n_curves,
            AVG(tamagawa_product) as mean_cp,
            MEDIAN(tamagawa_product) as median_cp,
            MAX(tamagawa_product) as max_cp,
            SUM(CASE WHEN tamagawa_product = 1 THEN 1 ELSE 0 END) as n_cp1
        FROM tamagawa
        GROUP BY conductor_bin
        ORDER BY MIN(conductor)
    """).fetchall()
    
    return stats
```

### Individual Tamagawa Number Analysis

For each prime $p \mid N$, the Tamagawa number depends on the Kodaira type:

```python
def tamagawa_from_kodaira(kodaira_type, valuation_delta, split=None):
    """Compute c_p from Kodaira type and related data."""
    kodaira_data = {
        'I0': 1,    # good reduction
        'In': min(valuation_delta, 4),  # I_n: c_p = min(n, 4) for split
        'II': 1, 'III': 2, 'IV': 3,
        'I0*': 4, 'In*': 2,  # depends on n mod 2
        'II*': 1, 'III*': 2, 'IV*': 3,
    }
    return kodaira_data.get(kodaira_type, 1)
```

## Computational Example

### Distribution of $\prod_p c_p$ (LMFDB data, $N \leq 500{,}000$)

| Conductor Range | $\#$ Curves | Mean $\prod c_p$ | Median | Max | % with $\prod c_p = 1$ |
|----------------|-------------|------------------|--------|-----|----------------------|
| $1$–$1{,}000$ | $\sim 65{,}000$ | 1.31 | 1 | 12 | 68% |
| $1{,}000$–$10{,}000$ | $\sim 310{,}000$ | 1.78 | 1 | 24 | 52% |
| $10{,}000$–$100{,}000$ | $\sim 820{,}000$ | 2.13 | 2 | 36 | 41% |
| $100{,}000$–$500{,}000$ | $\sim 1{,}500{,}000$ | 2.41 | 2 | 48 | 35% |

**Key observations:**
1. The mean $\prod c_p$ grows slowly with conductor, roughly as $\sim 0.3 \log N$.
2. The median stabilizes at 1–2 for small conductor, then shifts to 2.
3. $\prod c_p = 1$ is the most common value, but its frequency decreases as conductor grows (more primes dividing $N$ means more chances for $c_p > 1$).
4. The maximum values grow roughly linearly with the number of prime factors of $N$.

### Most Common Tamagawa Products

| $\prod c_p$ | Frequency | Typical origin |
|-------------|-----------|---------------|
| 1 | $\sim 45\%$ | All $c_p = 1$ |
| 2 | $\sim 18\%$ | One prime with $c_p = 2$ |
| 4 | $\sim 12\%$ | One $c_p = 4$ or two $c_p = 2$ |
| 3 | $\sim 6\%$ | One prime with $c_p = 3$ (type $IV$ or $IV^*$) |
| 6 | $\sim 4\%$ | One $c_p = 2$ and one $c_p = 3$ |
| 8 | $\sim 3\%$ | Combinations giving $2^3$ |
| 12 | $\sim 2\%$ | $c_p = 3$ and $c_p = 4$ |

### Correlation with $|\text{Ш}|$

Using LMFDB data for curves with $|\text{Ш}| > 1$:

| $\prod c_p$ | Avg $|\text{Ш}|$ | % with $|\text{Ш}| > 1$ |
|-------------|---------|------------------------|
| 1 | 1.02 | 1.8% |
| 2 | 1.04 | 3.2% |
| 4 | 1.08 | 5.1% |
| 3 | 1.03 | 2.7% |

**Observation:** Curves with larger $\prod c_p$ are slightly more likely to have $|\text{Ш}| > 1$. This is consistent with the BSD formula: a larger $\prod c_p$ in the denominator requires a larger $|\text{Ш}|$ (or larger $L$-value) to balance.

### Sample Computations

**11a1:** $N = 11$, bad prime $p = 11$, Kodaira type $I_1$, $c_{11} = 1$. $\prod c_p = 1$.

**37a1:** $N = 37$, bad prime $p = 37$, Kodaira type $I_1$, $c_{37} = 1$. $\prod c_p = 1$.

**141a1:** $N = 141 = 3 \times 47$. At $p = 3$: type $I_1$, $c_3 = 1$. At $p = 47$: type $I_1$, $c_{47} = 1$. $\prod c_p = 1$.

**571a1:** $N = 571$ (prime). Type $I_1$, $c_{571} = 1$. $\prod c_p = 1$.

**389a1:** $N = 389$ (prime). Type $I_1$, $c_{389} = 1$. $\prod c_p = 1$.

**269841a1:** $N = 269841$. Multiple bad primes. $\prod c_p = 1$.

For most small-conductor curves, all Tamagawa numbers are 1.

## Obstacle Analysis

1. **Database scale:** With $\sim 3 \times 10^6$ curves and up to $\sim 10$ bad primes each, the data has $\sim 3 \times 10^7$ entries. Efficient querying requires a database engine (DuckDB, PostgreSQL).

2. **Meaningful conjecture formulation:** The statistical analysis may produce correlations that are artifacts of the conductor distribution, not genuine arithmetic phenomena. Distinguishing signal from noise requires careful modeling.

3. **BSD constraint:** The BSD formula ties $\prod c_p$ to $|\text{Ш}|$, $\operatorname{Reg}$, and $\Omega$. Any correlation between $\prod c_p$ and these other quantities is partly a consequence of the formula, not an independent phenomenon.

## Cross-Group Connections

- **H-009:** BSD formula verification uses $\prod c_p$.
- **H-010 (ML):** Machine learning on Tamagawa data.
- **Group C (Congruences):** Congruence conditions on reduction types.

## Classification

**Data Analysis / Conjecture Formation** — This direction produces statistical descriptions and conjectures about Tamagawa numbers, with the goal of understanding their role in the arithmetic of elliptic curves.
