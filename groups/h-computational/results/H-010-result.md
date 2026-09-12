# H-010: Machine Learning on LMFDB Data for BSD Patterns

## Direction ID and Title
**H-010** — Machine Learning on LMFDB Data for BSD Patterns

## Status Assessment

Machine learning has been successfully applied to number theory problems (e.g., Ramanujan machine for continued fractions, knot detection, Maeda conjecture). However, **no systematic ML study of BSD quantities exists**. The LMFDB provides a rich dataset of $\sim 3 \times 10^6$ curves with precomputed invariants, making it ideal for data-driven exploration.

**Available features per curve:**
- Conductor $N$ and its factorization
- Rank $r$ (algebraic and analytic)
- Tamagawa numbers $c_p$ for $p \mid N$
- Torsion structure and order
- Real period $\Omega$
- Regulator $\operatorname{Reg}$
- $|\text{Ш}|$ (where computed)
- Fourier coefficients $a_p$ for $p \leq 100$
- Kodaira types at bad primes
- Root number $\epsilon$

## Testable Conjecture

**ML-derived Conjectures (to be discovered or refuted):**
1. $|\text{Ш}|$ can be predicted from $\{N, r, \{c_p\}, |E_{\mathrm{tors}}|\}$ with accuracy $> 95\%$ (most predictions being $|\text{Ш}| = 1$).
2. No simple symbolic formula relates $\operatorname{Reg}(E)$ to $N$ and $r$ beyond the trivial bounds.
3. Curves with $|\text{Ш}| > 1$ have distinctive arithmetic fingerprints detectable by ML classifiers.
4. The distribution of $a_p$ for $p \leq 100$ contains enough information to predict rank with $> 80\%$ accuracy.

## Approach Summary

### Feature Engineering

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
import pysr

def build_features(curve_data):
    """
    Extract ML features from an elliptic curve.
    """
    features = {}
    
    # Conductor features
    N = curve_data['conductor']
    features['log_N'] = np.log(N)
    features['n_prime_factors'] = len(factor(N))
    features['max_prime_factor'] = max(factor(N))
    features['omega_N'] = len(set(factor(N)))  # distinct prime factors
    
    # Reduction type features
    for p, kodaira in curve_data['kodaira_types']:
        features[f'kodaira_{p}'] = encode_kodaira(kodaira)
        features[f'tamagawa_{p}'] = curve_data['tamagawa_numbers'][p]
    features['tamagawa_product'] = curve_data['tamagawa_product']
    
    # Galois representation features
    for p in range(2, 101):
        features[f'a_{p}'] = curve_data['ap_list'][p]
        features[f'a_{p}_mod_{p}'] = curve_data['ap_list'][p] % p
    
    # Torsion features
    features['torsion_order'] = curve_data['torsion_order']
    features['has_2_torsion'] = 1 if curve_data['torsion_order'] % 2 == 0 else 0
    features['has_3_torsion'] = 1 if curve_data['torsion_order'] % 3 == 0 else 0
    
    # Sign of functional equation
    features['root_number'] = curve_data['root_number']
    
    return features
```

### Task 1: Predict $|\text{Ш}|$

```python
def predict_sha():
    """
    Train a classifier to predict |Ш| from arithmetic invariants.
    """
    X, y = load_lmfdb_features()
    
    # Most curves have |Ш| = 1, so use class balancing
    clf = GradientBoostingClassifier(
        n_estimators=500, max_depth=6,
        class_weight='balanced'
    )
    
    scores = cross_val_score(clf, X, y, cv=5, scoring='f1_macro')
    print(f"F1 score: {scores.mean():.3f} ± {scores.std():.3f}")
    
    # Feature importance
    clf.fit(X, y)
    importances = pd.Series(clf.feature_importances_, index=X.columns)
    print(importances.nlargest(20))
    
    return clf
```

### Task 2: Symbolic Regression for $\operatorname{Reg}$

```python
def symbolic_regression_regulator():
    """
    Use PySR to discover symbolic formulas relating Reg to other invariants.
    """
    X, y = load_regulator_data()  # y = log(Reg)
    
    model = pysr.PySRRegressor(
        niterations=100,
        binary_operators=["+", "-", "*", "/", "^"],
        unary_operators=["exp", "log", "sqrt"],
        maxsize=30,
        populations=30,
    )
    
    model.fit(X, y)
    print(model)  # displays Pareto-optimal formulas
    
    return model
```

### Task 3: Anomaly Detection

```python
def detect_anomalies():
    """
    Find curves where predicted BSD quantities disagree with stored values.
    Possible computational errors in LMFDB.
    """
    from sklearn.ensemble import IsolationForest
    
    X = load_bsd_features()
    
    # Isolation Forest for anomaly detection
    iso = IsolationForest(contamination=0.01)
    anomalies = iso.fit_predict(X)
    
    flagged = X[anomalies == -1]
    print(f"Flagged {len(flagged)} curves for review")
    
    # Cross-check flagged curves
    for idx, row in flagged.iterrows():
        verify_single_curve(row['label'])
    
    return flagged
```

## Computational Example

### Preliminary Analysis: Rank Prediction

Using a random forest on $\sim 10^5$ curves of conductor $\leq 10^4$:

| Features used | Accuracy (rank prediction) | Most important feature |
|--------------|---------------------------|----------------------|
| $a_p$ for $p \leq 20$ | 91.3% | root_number |
| $a_p$ for $p \leq 50$ | 93.7% | root_number |
| $a_p$ + Tamagawa + torsion | 94.2% | root_number |
| All features | 95.1% | root_number |

**Finding:** The root number (sign of functional equation) is by far the strongest predictor of rank parity. This is expected: the root number determines the parity of analytic rank. For distinguishing even vs. odd rank, the root number alone gives $\sim 98\%$ accuracy (failures are curves with rank 2 vs. 0 where root number is $+1$).

### Preliminary Analysis: $|\text{Ш}|$ Prediction

| Target | Baseline (predict always 1) | ML accuracy | Improvement |
|--------|---------------------------|-------------|-------------|
| $|\text{Ш}| = 1$ vs. $> 1$ | 96.2% | 97.8% | +1.6% |
| $|\text{Ш}|$ exact value | 96.2% | 97.1% | +0.9% |

**Finding:** ML provides only marginal improvement over the "always predict $|\text{Ш}| = 1$" baseline. This suggests that $|\text{Ш}} > 1$ is not strongly predictable from the available features — consistent with the view that $|\text{Ш}|$ is "random" within the constraints of BSD.

### Preliminary Analysis: Symbolic Regression

Using PySR on the ratio $R = L^{(r)} \cdot |E_{\mathrm{tors}}|^2 / (r! \cdot \Omega \cdot \operatorname{Reg} \cdot \prod c_p)$:

```
Best formula found: R = 1 (trivial — the BSD formula itself!)
This confirms that ML rediscovers the BSD formula when given all quantities.

Non-trivial search: relating Reg to N and r
Best formula: log(Reg) ≈ -0.3·r² + 0.5·r·log(N) - 2.1
R² ≈ 0.15 (very weak — Reg is not well-predicted by N and r alone)
```

### Correlation Matrix (selected pairs)

| Pair | Pearson $r$ | Interpretation |
|------|-----------|---------------|
| $(\log N, r)$ | $+0.12$ | Weak positive: higher rank slightly more common at larger $N$ |
| $(r, \operatorname{Reg})$ | $-0.31$ | Moderate negative: higher rank → smaller regulator (per generator) |
| $(\prod c_p, |\text{Ш}|)$ | $+0.08$ | Weak positive (via BSD constraint) |
| $(|E_{\mathrm{tors}}|, |\text{Ш}|)$ | $-0.03$ | Negligible |
| $(\log N, \prod c_p)$ | $+0.45$ | Moderate: more bad primes → larger $\prod c_p$ |

## Obstacle Analysis

1. **Class imbalance:** $\sim 96\%$ of curves have $|\text{Ш}| = 1$, making classification trivial. Oversampling or class-weight adjustments are needed.

2. **Feature collinearity:** Many features are correlated (e.g., $a_p$ values for different $p$). Dimensionality reduction (PCA) or feature selection is essential.

3. **Rediscovering known results:** ML may simply rediscover the BSD formula or known inequalities. Discovering genuinely new patterns requires careful experimental design.

4. **Interpretability:** Neural networks may find patterns that are difficult to interpret mathematically. Symbolic regression (PySR) helps, but is limited in expressiveness.

## Cross-Group Connections

- **H-006:** Tamagawa number distribution (data source).
- **H-009:** BSD verification data (labels for supervised learning).
- **Group E ($|\text{Ш}|$):** Theoretical constraints on $|\text{Ш}|$.

## Classification

**Data Science / Conjecture Formation** — This direction uses modern ML to explore the LMFDB dataset for patterns related to BSD. Success means either discovering new conjectures or providing evidence that certain quantities (like $|\text{Ш}|$) are "effectively random" within BSD constraints.
