# Computation Scripts — BSD Research Swarm

This directory contains Python scripts and JSON output from the computational
phases of the BSD research swarm.  **All outputs are numerical evidence, not
proof.**  The scripts compute L-values, regulators, Tamagawa numbers, and
Tate–Shafarevich group orders for elliptic curves over ℚ, and check these
against the Birch and Swinnerton-Dyer (BSD) conjecture.

**None of these scripts constitute a proof of BSD.**  They verify the
conjecture numerically to the precision afforded by their approximations.

---

## Scripts

### Phase 4: Explicit Formula and BSD Verification

| Script | Purpose | Known Bugs / Limitations |
|--------|---------|--------------------------|
| `phase4_quick.py` | Quick check of the explicit formula heuristic $S_E(X)/\log\log X \to -r$ for a handful of test curves. | Uses crude point-counting for $a_p$; only 500 primes. Cannot distinguish rank 2 from rank 3 at $X = 10{,}000$. |
| `phase4_verify.py` | Rigorous numerical verification: computes $S_E(X)/\log\log X$ at multiple $X$, smooths $L(E,1)$, and checks the strong BSD formula. | The $S_E/\log\log$ heuristic converges extremely slowly for rank ≥ 3 — all 5 "rank 2 candidates" were actually rank 3 (see `H-009-deep.md`). L-value smoothing uses incomplete-gamma kernel, not the exact analytic continuation. |
| `lmfdb_verify.py` | Fetches curve data from the LMFDB API to cross-check our high-rank candidates and $a_p$ values. | Network-dependent; LMFDB API may return stale or incomplete data. Only fetches, does not recompute. |

### Cycle 3: Exhaustive Search and ML

| Script | Purpose | Known Bugs / Limitations |
|--------|---------|--------------------------|
| `cycle3_sha_exhaust.py` | Exhaustive verification of $\|\text{Ш}\|$ for all rank 2 curves with conductor $N \le 10{,}000$ via PARI's `ellanalyticrank` and `ellbsd`. | Relies on PARI's `ellanalyticrank` for the leading $L$-value — this is a numerical approximation, not a certified computation. |
| `cycle3_rank2_search.py` | Brute-force search for rank 2 candidates among $y^2 = x^3 + ax + b$ with $|a|,|b| \le 100$, using the $S_E/\log\log$ heuristic with 500 primes. | Same slow-convergence issue: cannot reliably distinguish rank 2 from rank 3. LMFDB cross-check needed for any candidate. |
| `cycle3_ml_sha.py` | Trains decision-tree and logistic-regression models on Cremona curves to discover a formula for $\|\text{Ш}\|$ from local invariants. | Dataset had 5 known-bad rows (wrong models, wrong ranks) — now commented out. ML models achieve ~80% binary accuracy but no closed-form formula emerged. Root number estimator is a placeholder (`w = (-1)^rank`). |

### Cycle 4: Visibility and Modular Kernel

| Script | Purpose | Known Bugs / Limitations |
|--------|---------|--------------------------|
| `cycle4_visibility_verify.py` | Tests the universal visibility conjecture for rank 2 curves with $N \le 5000$: computes modular degree, genus of $X_0(N)$, 2-Selmer group, and checks $K[2]^{G_Q} = 0$. | **BUG (ellrank):** Treats PARI's `ellrank` second output as Selmer rank; it is actually a rank upper bound (see PARI docs). **BUG (kernel flag):** The `K2_invariant_trivial` flag is derived from the purported $\|\text{Ш}[2]\|$ ratio, not from computing $K[2]^{G_Q}$ directly. Both bugs affect curves with nontrivial rational 2-torsion. |
| `cycle4_modular_kernel.py` | Computes kernel data $K = \ker(\varphi^*: J_0(N) \to E)$ for rank 2 curves: modular degree, kernel dimension, 2-torsion as $G_\mathbb{Q}$-module. | Fetches Cremona data from GitHub — fragile to URL changes. Kernel dimension is computed as $g(X_0(N)) - 1$ (correct only when $E$ is a quotient, not a factor, of $J_0(N)$). |

### Cycle 5: Odd-Prime Visibility

| Script | Purpose | Known Bugs / Limitations |
|--------|---------|--------------------------|
| `cycle5_odd_prime_visibility.py` | For 14 rank 2 curves where visibility at $p=2$ fails (nontrivial $E(\mathbb{Q})[2]$), tests odd primes $p \in \{3,5,7,11,13\}$ for $K[p]^{G_Q} = 0$. | Uses PARI's `ellrank` with the same rank-upper-bound interpretation bug as cycle 4. Tamagawa number computation uses simplified reduction analysis. |

### Cycle 6: Extended Verification

| Script | Purpose | Known Bugs / Limitations |
|--------|---------|--------------------------|
| `cycle6_extend_verify.py` | Extends exhaustive $\|\text{Ш}\|$ verification to rank 2 curves with $N \le 50{,}000$ (Part A) and the first 100 rank 3 curves (Part B). | Same PARI approximation issues. Rank 3 verification uses `ellanalyticrank` which is not certified for higher-order derivatives. |

### BSD Verification Engines

| Script | Purpose | Known Bugs / Limitations |
|--------|---------|--------------------------|
| `bsd_verify.py` | First BSD verification engine: computes $L(E,1)$, periods, regulators, and checks the BSD formula using mpmath. | Used wrong curve model for 11a1 ($y^2 = x^3 - x - 1$ instead of minimal model) and wrong smoothing kernel. Superseded by `fixed_bsd_verify.py`. |
| `bsd_verify_v2.py` | Second verification engine: focused on $a_p$ computation and L-value estimation at scale. | Still uses approximate $L$-values. No certified computation. |
| `fixed_bsd_verify.py` | Fixes both bugs from `bsd_verify.py`: correct Cremona minimal models and the incomplete-gamma smoothing kernel. Cross-checks against LMFDB. | L-value computation is still an approximation (truncated series with exponential smoothing). The $L$-derivative at $s=1$ for rank ≥ 1 curves uses a numerical method, not certified analytic continuation. |

### Deep Analysis

| Script | Purpose | Known Bugs / Limitations |
|--------|---------|--------------------------|
| `deep_analysis_rank2.py` | Comprehensive BSD analysis for the 5 "rank 2 candidates" from Phase 4: computes $L''(E,1)/2!$, real period $\Omega$, regulator, Tamagawa numbers, predicts $\|\text{Ш}\|$. | All 5 candidates turned out to be rank 3 — the rank 2 analysis is a counterfactual. Uses naive height (not canonical height) for regulator, so values are approximate. |

---

## JSON Output Files

| File | Contents |
|------|----------|
| `phase4_quick.json` | $S_E(X)/\log\log X$ values at multiple $X$ for test curves. |
| `phase4_verify.json` | Full Phase 4 verification results including strong BSD checks. |
| `lmdb_verification.json` | LMFDB cross-check data. |
| `cycle3_sha_exhaust.json` | Exhaustive $\|\text{Ш}\|$ for rank 2, $N \le 10{,}000$. |
| `cycle3_rank2.json` | Brute-force rank 2 search results. |
| `cycle3_ml_sha.json` | ML model training results and conjecture. |
| `cycle4_visibility.json` | Visibility kernel analysis for rank 2, $N \le 5000$. |
| `cycle4_modular_kernel.json` | Modular kernel data for rank 2, $N \le 2000$. |
| `cycle5_odd_prime_visibility.json` | Odd-prime visibility test results. |
| `cycle6_extend_verify.json` | Extended verification to $N \le 50{,}000$ and rank 3. |
| `bsd_results.json` | First BSD verification output (superseded). |
| `bsd_results_v2.json` | Second BSD verification output. |
| `fixed_bsd_results.json` | Fixed BSD verification with LMFDB cross-checks. |
| `deep_rank2_results.json` | Deep analysis of the 5 rank-3 curves (misclassified as rank 2). |
| `new_conjectures.json` | Conjectures generated from ML analysis. |

---

## What the Outputs Mean

- **Numerical evidence, not proof.**  Every $\|\text{Ш}\|$ value is a
  floating-point computation rounded to the nearest integer.  A ratio of
  1.000000000 does not constitute a proof that BSD holds.
- **PARI/GP's `ellanalyticrank`** returns a numerical approximation to the
  analytic rank and leading $L$-value.  For curves with conductor $N \le
  500{,}000$ (Cremona tables), these values are known to be correct by other
  means — but the script itself does not certify this.
- **The explicit formula heuristic** $S_E(X)/\log\log X \to -r$ converges
  too slowly to be useful for rank classification at moderate $X$.  Use root
  number parity and 2-descent instead.
- **ML models** achieved ~80% binary accuracy on $\|\text{Ш}\| = 1$ vs
  $\|\text{Ш}\| > 1$, but no closed-form formula was discovered.
