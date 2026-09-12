# J-005: Machine Learning Patterns in LMFDB Rank Data

## Direction ID and Title

**J-005: Machine Learning Patterns in LMFDB Rank Data**

## Status Assessment

**Feasibility: Medium. Technical readiness: High. Mathematical yield: Uncertain.**

The LMFDB currently hosts >300 million elliptic curves over $\mathbb{Q}$ with complete conductor, Tamagawa numbers, torsion, and root number data for curves up to conductor $\sim 10^6$ (and partial data to conductor $\sim 10^9$). Rank computations via analytic methods (via Dokchitser's `rank` GP script or Birch–Swinnerton-Dyer numerical verification) are available for a substantial fraction. This is more than sufficient data for supervised ML.

However, the honest assessment is sobering: **no ML system has yet produced a mathematical insight about rank that was not already known or trivially derivable from existing heuristics.** The Katz–Sarnak heuristics already predict ~50/50 rank 0/1 distribution. Bhargava–Shankar proved average rank $\leq 0.885$. The gap between what ML can find (statistical correlations in finite data) and what constitutes a mathematical theorem is enormous.

**Current state**: Exploratory work by He–Lee (2023) and LMFDB-based studies have applied basic classifiers. No published symbolic regression results exist for rank prediction. The field is wide open but the bar for genuine mathematical contribution is high.

## Testable Conjecture or Lemma

**Conjecture (ML-Discoverable Rank Predictability).** There exists a function $f: \mathbb{N}^5 \to \mathbb{Q}$ computable from the feature vector $(N, c_2, c_3, c_p, w)$ (conductor, Tamagawa numbers at 2 and 3, number of primes dividing $N$, root number) such that for a random elliptic curve $E/\mathbb{Q}$ with conductor $N \leq X$:

$$\Pr[\operatorname{rank}(E) = f(N, c_2, c_3, \#\{p \mid N\}, w)] \geq 0.75 + o(1) \quad \text{as } X \to \infty$$

**Stronger variant (Symbolic Regression Target).** The root number $w = \prod_{p \leq \infty} w_p$ satisfies a closed-form relationship with local Tamagawa numbers and torsion that, combined with a parity constraint, predicts rank with accuracy $> 0.90$ for rank $\leq 2$ curves.

**Why this is interesting:** If rank were genuinely unpredictable from local data, no ML model should exceed ~50% accuracy on rank-0 vs rank-1 classification (by the Katz–Sarnak model). Any statistically significant excess would suggest exploitable local-to-global structure beyond root number parity.

## Approach Summary

### ML Pipeline Architecture

**Stage 1: Data Collection and Feature Engineering**

Source: LMFDB PostgreSQL dumps, accessed via `lmfdb.org/api/`. Target table: `ec_curves`.

Feature vector $\mathbf{x} \in \mathbb{R}^{18}$:

| Index | Feature | Type | Source |
|-------|---------|------|--------|
| 0 | $\log N$ (log conductor) | continuous | `conductor` |
| 1 | $\omega(N)$ (number of distinct prime factors) | integer | derived |
| 2 | $c_2$ (Tamagawa number at 2) | integer | `tamagawa_numbers` |
| 3 | $c_3$ (Tamagawa number at 3) | integer | `tamagawa_numbers` |
| 4 | $\prod_p c_p$ (product of all Tamagawa numbers) | integer | `tamagawa_numbers` |
| 5 | $\|E(\mathbb{Q})_{\text{tors}}\|$ | integer | `torsion` |
| 6 | $w = \prod w_p \in \{-1, +1\}$ (global root number) | ±1 | `root_number` |
| 7 | $a_2, a_3, a_5, a_7$ (trace of Frobenius at small primes) | integer | `anlist` |
| 8 | $\Delta \pmod{p}$ for $p = 2,3,5$ | categorical | `disc` |
| 9 | $j$-invariant valuation at 2, 3 | integer | `jinv` |
| 10 | $\text{rank}_4 = \#\{p \mid N : w_p = -1\}$ (number of primes with bad root number) | integer | derived |
| 11 | $N \bmod 12$ (residue class) | categorical | derived |

Target $y \in \{0, 1, 2, 3, 4+\}$ (analytic rank, computed via Dokchitser or verified BSD).

**Stage 2: Model Architectures**

**(a) Gradient-Boosted Trees (baseline).** XGBoost with 500 trees, max depth 8, learning rate 0.05. This is the strongest baseline for tabular data. Expected accuracy: ~70% on rank 0/1 classification.

**(b) Feed-Forward Neural Network.** Architecture:
```
Input(18) → Dense(128, ReLU) → Dropout(0.3)
         → Dense(64, ReLU)  → Dropout(0.2)
         → Dense(32, ReLU)
         → Dense(5, Softmax)
```
Adam optimizer, lr=1e-3, batch size 4096, 100 epochs. Label smoothing $\epsilon = 0.05$.

**(c) Symbolic Regression (PySR).** Run PySR with operators $\{+, -, \times, \div, \exp, \log, \text{pow}\}$ and 50 iterations of Pareto-optimal search. Target: closed-form formula $f(\mathbf{x})$ approximating rank. Use root mean squared error + complexity penalty. Maximum expression complexity: 30 nodes.

**(d) UMAP/t-SNE Visualization.** 2D embedding of the 18-dimensional feature space, colored by rank, to identify geometric clusters and decision boundaries.

**Stage 3: Training Procedure**

- **Split**: 70% train / 15% validation / 15% test, stratified by rank.
- **Oversampling**: SMOTE for rank 3+ classes (which are rare: <0.1% of curves).
- **Cross-validation**: 5-fold stratified CV for hyperparameter selection.
- **Evaluation**: Accuracy, macro-F1, per-class precision/recall, ROC-AUC (one-vs-rest).
- **Feature importance**: SHAP values to identify which features contribute most to predictions.

**Stage 4: Symbolic Extraction**

- If any model achieves >75% accuracy, extract SHAP interaction effects.
- Run PySR on the residuals (errors) of the best model to find missing structure.
- Compare PySR-discovered formulas against known heuristics (Bhargava–Shankar, Katz–Sarnak).

## Computational Example

### Concrete Feature Sets

**Example 1: Rank 0 curve**
- Curve: `11a1` ($y^2 + y = x^3 - x^2 - 10x - 20$)
- Feature vector: $(N, \omega, c_2, c_3, \prod c_p, |E_{\text{tors}}|, w, a_2, a_3, a_5, a_7, \text{rank}_4, N \bmod 12)$
- $= (11, 1, 1, 1, 1, 5, +1, -2, -1, -2, -1, 0, 11)$
- Analytic rank: 0

**Example 2: Rank 1 curve**
- Curve: `37a1` ($y^2 + y = x^3 - x$)
- Feature vector: $= (37, 1, 1, 1, 1, 1, -1, -2, -2, -4, 1, 1, 1)$
- Analytic rank: 1

**Example 3: Rank 2 curve**
- Curve: `389a1` ($y^2 + y = x^3 + x^2 - 2x$)
- Feature vector: $= (389, 1, 1, 1, 1, 1, +1, -2, 2, -4, 1, 0, 5)$
- Analytic rank: 2

### Expected Outputs

| Model | Rank 0 Acc. | Rank 1 Acc. | Rank 2 Acc. | Macro-F1 |
|-------|-------------|-------------|-------------|----------|
| XGBoost (baseline) | 0.78 | 0.72 | 0.45 | 0.65 |
| Neural Network | 0.80 | 0.75 | 0.50 | 0.68 |
| PySR (best formula) | 0.73 | 0.68 | 0.35 | 0.59 |

**Interpretation:** If models achieve these numbers, it confirms rank is partially predictable from local data. If models cannot exceed ~50% on rank 0/1, it supports the Katz–Sarnak picture that rank is essentially random beyond root number.

### Symbolic Regression Target Formula

PySR might discover a relationship like:
$$\hat{r}(E) \approx \frac{1 - w}{2} + \alpha \cdot \frac{\omega(N) - 1}{\log \log N} + \beta \cdot \frac{\prod c_p - 1}{\prod c_p}$$
where $\alpha, \beta$ are small constants. The first term is the root number contribution (parity prediction); the other terms capture local data signal.

## Obstacle Analysis

### 1. Correlation vs. Causation
The most fundamental obstacle. ML can find that curves with conductor divisible by many small primes tend to have higher rank, but this could be a spurious artifact of the conductor range sampled. Any ML-discovered "pattern" requires independent mathematical validation. **Mitigation:** Use out-of-distribution testing (train on $N < 10^5$, test on $10^5 < N < 10^6$) to distinguish genuine patterns from memorization.

### 2. Class Imbalance
Rank 0 and 1 dominate (~50% each). Rank 2 is ~2-5%. Rank $\geq 3$ is $<0.1\%$. Standard ML will ignore minority classes. **Mitigation:** SMOTE, focal loss ($\gamma = 2$), and separate binary classifiers for each rank threshold.

### 3. Overfitting to Finite Data
LMFDB conductor ranges are not random samples—they are computationally bounded. Curves with conductor $< 1000$ are complete; larger conductors are sampled with bias toward "interesting" curves. **Mitigation:** Stratify evaluation by conductor range; check for distribution shift.

### 4. Feature Engineering Bias
Choosing which invariants to include is itself a mathematical hypothesis. Including root number essentially "cheats" for rank prediction (since root number determines parity). **Mitigation:** Ablation study: measure accuracy with and without root number.

### 5. Interpretability Gap
Even if a neural network achieves 90% accuracy, a black-box model contributes nothing to mathematical understanding. **Mitigation:** SHAP analysis + symbolic regression on residuals. Only closed-form formulas are publishable mathematics.

### 6. No Ground Truth for Large Conductors
For conductor $> 10^6$, rank computation becomes expensive and Sha verification is incomplete. Labels may be unreliable. **Mitigation:** Only use curves with verified rank (via Dokchitser with precision checks or confirmed BSD).

## Cross-Group Connections

### Group C (Arithmetic Statistics)
**Strongest connection.** ML rank prediction is essentially an arithmetic statistics question: what is the distribution of rank as a function of conductor-level invariants? C-001 through C-005 on rank distribution heuristics directly feed into feature selection. ML results could provide computational evidence for or against conjectures in this group.

### Group H (Computational)
**Direct synergy.** H-group directions on explicit rank computation (H-001: explicit bounds, H-003: computing Sha) provide the training data quality. Conversely, ML-identified "hard" curves (where models fail) could guide computational efforts.

### Group A (Iwasawa Theory)
**Indirect.** Iwasawa invariants $\lambda, \mu$ for $p$-adic L-functions could serve as additional features. If ML finds that $\lambda$-invariant predicts rank better than conductor alone, it would suggest Iwasawa-theoretic structure in rank distributions.

### Group D (Tate-Shafarevich)
**Moderate.** If ML discovers that $|\Sha|$ correlates with specific conductor factorizations, it could suggest new heuristics for Sha distribution. Symbolic regression on the BSD formula components is in scope.

### Group E ($p$-adic Methods)
**Indirect.** $p$adic regulators and $p$-adic L-values could serve as features for rank prediction. The $p$-adic BSD formula provides alternative rank signatures.

### Group I (Connections)
**Moderate.** I-001 through I-004 on modularity and Galois representations connect to the trace of Frobenius features ($a_p$ values). ML on Galois representation data could identify patterns invisible in arithmetic invariants alone.

## Classification

**Risk: HIGH. Reward: MODERATE (computational), LOW (theoretical).**

- **Risk factors:** (1) ML results are inherently non-proof; any "discovery" requires separate mathematical validation. (2) Overfitting is almost guaranteed given the gap between conductor ranges computationally accessible and the asymptotic regime. (3) The feature space is low-dimensional (18 features), limiting what deep learning can discover beyond what traditional statistics can.

- **Reward potential:** (1) Computational: identifying "interesting" curves (e.g., rank $\geq 3$ candidates) for further study is immediately useful. (2) Statistical: confirming or refuting whether rank is predictable from local data beyond root number parity is a genuine contribution. (3) Formula discovery: if symbolic regression finds a closed-form rank predictor with provable properties, that would be a significant conjecture.

- **Realistic outcome:** A well-executed study would produce (a) baseline accuracy numbers for rank prediction, (b) SHAP-based feature importance rankings, (c) candidate symbolic formulas, (d) a curated dataset of "hard" curves where all models fail. This is a useful computational contribution but unlikely to yield new theorems without substantial additional mathematical work.

- **Classification:** Computational/Exploratory. Primarily useful as evidence-gathering for Group C (Arithmetic Statistics) conjectures.
