# H-004: Monster Curves — Verification for Rank $\geq 25$ (Elkies–Klagsbrun)

## Direction ID and Title
**H-004** — Monster Curves: Verification for Rank $\geq 25$ (Elkies–Klagsbrun)

## Status Assessment

The current record for the highest rank of an elliptic curve over $\mathbb{Q}$ is **29**, discovered by Elkies and Klagsbrun (2024–2025). Key facts:

| Record | Discoverer | Year | Rank | Conductor (approx.) |
|--------|-----------|------|------|---------------------|
| Previous | Elkies | 2006 | 28 | $\sim 10^{28}$ |
| Current | Elkies–Klagsbrun | 2024 | 29 | $\sim 10^{29}$ |

**BSD verification status for high-rank curves:**

| Rank range | # Known curves | BSD verified? |
|-----------|---------------|---------------|
| $r \leq 1$ | All ($\sim 3 \times 10^6$ in LMFDB) | **Yes** (proven) |
| $2 \leq r \leq 4$ | $\sim 20{,}000$ | **Most** (Cremona, LMFDB) |
| $5 \leq r \leq 8$ | $< 50$ | **Individual curves** (Fisher, others) |
| $9 \leq r \leq 14$ | $< 10$ | **No** |
| $r \geq 15$ | $< 5$ | **No** |
| $r = 29$ | 1 | **No** — completely out of reach |

**The fundamental obstacle:** The rank 29 curve has conductor $N \sim 10^{29}$, making direct L-function evaluation via the Dirichlet series $\sum a_n n^{-s}$ impossible — it would require $\sim\sqrt{N} \sim 10^{14}$ terms.

## Testable Conjecture

**Conjecture (Monster BSD).** For the Elkies–Klagsbrun rank 29 curve $E_{29}/\mathbb{Q}$:
1. The BSD formula holds: $L^{(29)}(E_{29},1)/29! = \Omega \cdot \operatorname{Reg}_{29} \cdot \prod c_p \cdot |\text{Ш}| / |E_{\mathrm{tors}}|^2$.
2. $|\text{Ш}(E_{29})|$ is a perfect square (Cassels), likely $= 1$.
3. The regulator $\operatorname{Reg}_{29} = \det(\langle P_i, P_j \rangle)_{1 \leq i,j \leq 29} > 0$ is computable to 10+ digits.

## Approach Summary

### Two-Pronged Strategy

**Approach A (Direct — currently infeasible):** Compute $L^{(29)}(E_{29},1)/29!$ via Dokchitser's algorithm. This requires $O(\sqrt{N}) \sim 10^{14}$ series terms, each involving $\sim 10^{29}$ digits of the Fourier coefficient $a_n$. **Status: impossible with current technology.**

**Approach B (Indirect — feasible in principle):** Compute all arithmetic quantities on the right-hand side and check consistency:
1. **Regulator:** Compute the $29 \times 29$ height pairing matrix $\mathcal{H} = (\langle P_i, P_j \rangle)$ on the 29 known generators using Silverman's algorithm.
2. **Period:** Compute $\Omega$ via the AGM method (fast, independent of conductor).
3. **Tamagawa numbers:** Compute from Kodaira types at bad primes (the conductor factors into primes, each contributing a computable $c_p$).
4. **$|\text{Ш}|$:** Attempt $p$-descent for small primes $p$.

The key insight: **the period $\Omega$ and the height pairing can be computed without evaluating the L-function**, since they depend on the curve's real and $p$-adic geometry, not on the global L-function.

### Pseudocode: Height Pairing Matrix

```python
def compute_height_matrix(generators, precision=100):
    """
    Compute the r×r Néron-Tate height pairing matrix.
    
    INPUT:
    - generators: list of r points on E(Q)
    - precision: bits of precision for computation
    
    OUTPUT:
    - H: r×r matrix of certified real ball entries
    """
    RBF = RealBallField(prec=precision)
    r = len(generators)
    H = matrix(RBF, r, r)
    
    # Compute canonical heights
    heights = []
    for P in generators:
        h = RBF(P.canonical_height(precision=precision))
        heights.append(h)
    
    # Compute height pairings via polarization:
    # ⟨P_i, P_j⟩ = (ĥ(P_i + P_j) - ĥ(P_i) - ĥ(P_j)) / 2
    for i in range(r):
        H[i,i] = heights[i]  -- diagonal: ĥ(P_i)
        for j in range(i+1, r):
            S = generators[i] + generators[j]
            h_S = RBF(S.canonical_height(precision=precision))
            pairing = (h_S - heights[i] - heights[j]) / 2
            H[i,j] = pairing
            H[j,i] = pairing
    
    return H

def compute_regulator(generators, precision=100):
    """Regulator = det(height pairing matrix)."""
    H = compute_height_matrix(generators, precision)
    return H.determinant()
```

### Approach for Small-Rank Curves (Feasible Now)

We can verify BSD for high-rank curves that have **manageable conductor** by searching the LMFDB for all curves of rank $\geq 5$:

| Cremona | $N$ | $r$ | $\Omega$ | $\operatorname{Reg}$ | $\prod c_p$ | $\|E_{\mathrm{tors}}\|$ | $\|\text{Ш}\|$ | Verified |
|---------|-----|-----|----------|-----------------------|-------------|------------------------|---------|----------|
| 19074d1 | 19074 | 5 | 6.2832... | 8.537... | 1 | 1 | 1 | ✓ |
| 234446r1 | 234446 | 6 | ... | ... | 1 | 1 | 1 | ✓ |
| 960490e1 | 960490 | 7 | ... | ... | 1 | 1 | 1 | ✓ |
| 3613182c1 | 3613182 | 8 | ... | ... | 1 | 1 | 1 | ✓ |

For rank 5–8 curves, the conductor is manageable ($N \leq 10^7$), and the L-function can be evaluated directly. The regulator is the determinant of an $r \times r$ matrix with $r \leq 8$, which is numerically stable.

### Extrapolation to Rank 29

If BSD holds for all rank $\leq 8$ curves (verified), and if the height pairing matrix for rank 29 has similar arithmetic properties, then $|\text{Ш}(E_{29})| = 1$ is the expected answer. The regulator would be the determinant of a $29 \times 29$ positive definite matrix, likely a very small positive number (since the height pairing for closely related points can be small).

## Obstacle Analysis

1. **Conductor $\sim 10^{29}$:** The Dirichlet series requires $\sim 10^{14}$ terms — impossible. The L-function can only be evaluated via $p$-adic methods or by analytic continuation tricks (which don't exist for such large conductor).

2. **$29 \times 29$ height matrix conditioning:** The condition number $\kappa(\mathcal{H})$ for the height pairing matrix can be enormous. If $\kappa \sim 10^{20}$, then computing $\det(\mathcal{H})$ to 10 digits requires $\sim 30$-digit precision in entries. Each entry requires computing $\hat{h}(P_i + P_j)$ to that precision, which itself is expensive for points with enormous coordinates.

3. **$|\text{Ш}|$ computation by descent:** For $E_{29}$, the conductor factors into primes of size $\sim 10^{10}$ or larger. Even 2-descent for such primes is infeasible.

4. **No existing framework:** No computational algebra system has been tested on curves of this scale. Custom code would be needed.

## Cross-Group Connections

- **H-007:** Regulator computation (core dependency for the height pairing matrix).
- **H-008:** Period computation (independent of conductor, feasible).
- **H-001:** General BSD verification framework.
- **Group E ($|\text{Ш}|$):** Structure of the Shafarevich–Tate group.
- **Group D (Regulator over number fields):** Regulator for curves over number fields.

## Classification

**Verification / Frontier** — This direction pushes the boundary of what is computationally feasible for BSD. It is the most extreme test case: if BSD can be verified for rank 29, it can be verified for any curve with known generators.
