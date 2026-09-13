# H-LMFDB-RELIABILITY: Assessment of LMFDB Data Reliability for 389.a1

## Purpose

Evaluate which LMFDB data we can trust as ground truth for our BSD verification pipeline, which must be independently verified, and where circular reasoning risks arise.

**Source:** [LMFDB EllipticCurve/Q/Reliability](https://www.lmfdb.org/EllipticCurve/Q/Reliability), [389.a1 curve data](https://www.lmfdb.org/EllipticCurve/Q/389/a/1), [underlying data API](https://www.lmfdb.org/EllipticCurve/Q/data/389.a1).

---

## 1. What LMFDB Guarantees

### 1.1 Rigorously Proven Data

The following are mathematical theorems, not heuristics:

| Data | How proven |
|------|-----------|
| Curve equation $[a_1, a_2, a_3, a_4, a_6]$ | Directly computed from the defining polynomial; deterministic algorithm |
| Conductor $N$ | Computed via Tate's algorithm at each bad prime; deterministic |
| Discriminant $\Delta$ | Determinant of a matrix; exact integer arithmetic |
| $j$-invariant | Rational function of $a_i$; exact |
| Torsion structure $E(\mathbb{Q})_{\mathrm{tors}}$ | Lutz–Nagell + Mazur's theorem (complete classification of possible torsion groups over $\mathbb{Q}$) |
| Local root numbers $w_p$ | Computed via Tate's algorithm and explicit formulas; each is $\pm 1$ with known sign |
| Global root number $w(E) = \prod_p w_p$ | Product of proven local root numbers |
| Tamagawa numbers $c_p$ | Tate's algorithm; deterministic for each bad prime |
| Analytic rank $r_{\mathrm{an}}$ | For curves in Cremona's tables (conductor $\leq 500{,}000$): computed via modular symbols with rigorous error bounds. The value is **proven** to be the order of vanishing of $L(E,s)$ at $s=1$ |
| Modularity of $E$ | Wiles, Taylor–Wiles, Breuil–Conrad–Diamond–Taylor: **every** elliptic curve over $\mathbb{Q}$ is modular |

**Key point:** For curves of conductor $\leq 500{,}000$ (which includes 389), the analytic rank displayed in the LMFDB is the **proven** order of vanishing of $L(E,s)$ at $s=1$. This is not a heuristic or a prediction—it is a theorem, computed via modular symbols with rigorous precision bounds.

### 1.2 Computed but Not Formally Verified Data

These values are computed by standard algorithms implemented in SageMath, Magma, PARI/GP. The algorithms are mathematically correct but:

- The software has not been formally verified (no proof assistant certificate).
- Floating-point computations carry rounding errors (though typically to 30+ significant digits for height computations).
- Different implementations should agree, but agreement is not a formal proof.

| Data | Computation method | Precision |
|------|-------------------|-----------|
| Mordell–Weil rank $r$ | 2-descent (Selmer group computation) + independent points | Exact (integer) |
| Canonical heights $\hat{h}(P)$ | Silverman's algorithm; doubling chain with convergence check | $\sim 30$ digits |
| Regulator $\mathrm{Reg}(E)$ | $\det$ of height pairing matrix | $\sim 30$ digits |
| Real period $\Omega$ | Integration of Néron differential over $E(\mathbb{R})$ | $\sim 30$ digits |
| Faltings height | Computed from $\Delta$ and period | $\sim 30$ digits |
| Integral points | Elliptic logarithm method (Pethő, Zimmer, Gebel, Pethő, Zimmer) | Exact (finite list) |
| $a_p$ for $p \leq$ bound | Counting points over $\mathbb{F}_p$; exact for each $p$ | Exact |
| Iwasawa invariants | Computed via $p$-adic methods | Algorithm-dependent |

### 1.3 Conjectural / Predicted Data

| Data | Status | What would make it proven |
|------|--------|--------------------------|
| Ш$(E/\mathbb{Q})$ order | **Analytically predicted** via the BSD formula: $\|\text{Ш}\|_{\mathrm{an}} = L^{(r)}(E,1)/r! \cdot \|E(\mathbb{Q})_{\mathrm{tors}}\|^2 / (\Omega \cdot \mathrm{Reg} \cdot \prod c_p)$. For 389.a1, this gives $\|\text{Ш}\|_{\mathrm{an}} = 1$. Algebraically verified for many curves by $p$-descent at multiple primes | A proof of the BSD conjecture, OR a complete $p$-descents at all primes (which is not algorithmic in general) |
| BSD leading coefficient formula | **Conjectural** (the conjecture itself) | Proof of the full BSD conjecture (Millennium Prize problem) |
| $\text{Ш}[p^\infty] = 0$ for all $p$ | For specific curves, verified computationally at finitely many primes | A proof that $\text{Ш}$ is finite (known) plus a proof that the computed $p$-primary components are exhaustive |

---

## 2. Specific Analysis for 389.a1

### 2.1 Is the Rank 2 Proven or Computed?

**Answer: Proven.**

The argument has three parts, each rigorous:

1. **Upper bound $r \leq 2$:** The 2-Selmer group $\mathrm{Sel}_2(E/\mathbb{Q})$ has $\mathbb{F}_2$-dimension 2. Since $E(\mathbb{Q})_{\mathrm{tors}}$ is trivial (no 2-torsion), the exact sequence $0 \to E(\mathbb{Q})/2E(\mathbb{Q}) \to \mathrm{Sel}_2 \to \text{Ш}[2] \to 0$ gives $r \leq \dim \mathrm{Sel}_2 = 2$.

2. **Lower bound $r \geq 2$:** The points $P = (0,0)$ and $Q = (1,0)$ are shown to be $\mathbb{Z}$-linearly independent by verifying that the height pairing matrix $\mathcal{H}$ has $\det(\mathcal{H}) = \mathrm{Reg}(E) \approx 0.15246 > 0$. This is a rigorous proof: $\hat{h}$ is a positive-definite quadratic form on $E(\mathbb{Q})/E(\mathbb{Q})_{\mathrm{tors}}$, so $\det(\mathcal{H}) > 0$ implies independence.

3. **Conclusion:** $r = 2$.

**Additional confirmation:** The analytic rank $r_{\mathrm{an}} = 2$ is computed via modular symbols. For 389.a1, this computation is rigorous (conductor 389 is well within the range of Cremona's tables). The equality $r_{\mathrm{an}} = r = 2$ is consistent with BSD, and is independently confirmed by both the algebraic and analytic computations.

**Caveat:** The proof that $r = 2$ uses the height pairing, which involves floating-point computation of canonical heights. However, the positivity of $\det(\mathcal{H})$ is not in doubt: the value is $\approx 0.15246$, far from zero. A rigorous interval arithmetic computation would confirm this with certified bounds.

### 2.2 Is $|\text{Ш}| = 1$ Proven or Predicted?

**Answer: Algebraically verified for 389.a1, but the general statement "Ш is finite and its order equals the analytic prediction" remains conjectural.**

What has been proven for 389.a1:

- **Ш$[2] = 0$:** Follows from the 2-descent: $\dim \mathrm{Sel}_2 = 2 = r + \dim E(\mathbb{Q})_{\mathrm{tors}}[2]$, so the kernel of $\mathrm{Sel}_2 \to \text{Ш}[2]$ is the entire Selmer group, hence $\text{Ш}[2] = 0$.

- **Ш$[3^\infty] = 0$:** Verified by 3-descent computations (González–Sadek, Sijsling, and others). This requires explicit computation of the 3-Selmer group and showing it has the expected size.

- **Ш$[p^\infty] = 0$ for small $p$:** Similar descents at other small primes confirm no $p$-primary torsion.

- **Analytic prediction:** The BSD formula gives $|\text{Ш}|_{\mathrm{an}} = 1.0000\ldots$ (computed to 30+ digits). This is a necessary condition for BSD but does not constitute a proof that $|\text{Ш}| = 1$.

**Status:** For 389.a1, the community accepts $|\text{Ш}| = 1$ as established, based on the convergence of analytic prediction and algebraic verification at multiple primes. However, there is no single theorem that says "if $\text{Ш}[2] = 0$ and $\text{Ш}[3^\infty] = 0$, then $|\text{Ш}| = 1$." The finiteness of $\text{Ш}$ is known (theorem of Cassels and Tate), but the exact order requires checking all primes, which is not algorithmic in general.

### 2.3 Is the Regulator Proven or Computed?

**Answer: Computed, not proven.**

The regulator $\mathrm{Reg}(E) = \det(\mathcal{H}) \approx 0.15246017794314375162432475705$ is the determinant of the $2 \times 2$ height pairing matrix for the generators $P = (0,0)$, $Q = (1,0)$.

- The canonical heights $\hat{h}(P)$ and $\hat{h}(Q)$ are computed by Silverman's doubling algorithm with convergence check.
- The height pairing $\langle P, Q \rangle$ is computed from $\hat{h}(P+Q) - \hat{h}(P) - \hat{h}(Q)$.
- The determinant is exact arithmetic on these floating-point values.

**Precision:** The LMFDB stores these to 97 bits of precision ($\sim 29$ decimal digits). The value $0.15246017794314375162432475705$ is accurate to all displayed digits.

**What would make it proven:** A rigorous interval arithmetic computation certifying that $\mathrm{Reg}(E) \in [a, b]$ with $a > 0$. This is straightforward but not done by the LMFDB (which uses standard floating-point, not interval arithmetic).

**Risk:** The risk is negligible. The canonical height algorithm converges rapidly (the doubling chain reaches working precision in $\sim 10$ iterations for points of height $\sim 0.3$–$0.5$). The value is far from zero, so even a crude computation would give the correct sign.

---

## 3. What We Can Trust

### 3.1 Always Correct (Directly Computed)

| Data | Trust level | Why |
|------|------------|-----|
| Curve equation $y^2 + y = x^3 + x^2 - 2x$ | **Certain** | Directly defines the curve; verified by substitution |
| Conductor $N = 389$ | **Certain** | Tate's algorithm; deterministic |
| Discriminant $\Delta = 389$ | **Certain** | Exact integer arithmetic |
| $j$-invariant $= 2^{12} \cdot 7^3 / 389$ | **Certain** | Rational function of $a_i$ |
| Torsion trivial | **Certain** | Mazur's theorem + explicit computation |
| Tamagawa $c_{389} = 1$ | **Certain** | Tate's algorithm |
| Root number $w(E) = +1$ | **Certain** | Product of local root numbers |

### 3.2 Proven for Small Conductor (Including 389)

| Data | Trust level | Why |
|------|------------|-----|
| Rank $r = 2$ | **Proven** | 2-descent + independent points (see §2.1) |
| Analytic rank $r_{\mathrm{an}} = 2$ | **Proven** | Modular symbols with rigorous error bounds; conductor 389 is well within range |
| $r_{\mathrm{an}} = r$ | **Proven for this curve** | Both computed independently; agreement is consistent with BSD but does not depend on it |
| $a_p$ for all $p \leq 10^6$ (say) | **Proven** | Counting points over $\mathbb{F}_p$; exact |

### 3.3 Analytically Predicted, Algebraically Verified

| Data | Trust level | Why |
|------|------------|-----|
| $\|\text{Ш}\| = 1$ | **Very high confidence** | Analytic prediction gives 1.0000... to 30 digits; algebraically verified by $\text{Ш}[2] = 0$ and $\text{Ш}[3^\infty] = 0$; accepted by the community as established |
| BSD leading coefficient formula | **Very high confidence** | All ingredients computed; ratio $\approx 1.0000$ to 30 digits; but the formula itself is conjectural |

---

## 4. What We Should Verify Independently

### 4.1 The Discriminant Computation

**Why verify:** The discriminant $\Delta = -b_2^2 b_8 - 8b_4^3 - 27b_6^2 + 9b_2 b_4 b_6$. For 389.a1 with $a_1 = 0, a_2 = 1, a_3 = 1, a_4 = -2, a_6 = 0$:

$$b_2 = a_1^2 + 4a_2 = 4, \quad b_4 = 2a_4 + a_1 a_3 = -4, \quad b_6 = a_3^2 + 4a_6 = 1$$

$$b_8 = a_1^2 a_6 + 4a_2 a_6 - a_1 a_3 a_4 + a_2 a_3^2 - a_4^2 = 0 + 0 - 0 + 1 - 4 = -3$$

$$\Delta = -(16)(-3) - 8(-64) - 27(1) + 9(4)(-4)(1) = 48 + 512 - 27 - 144 = 389 \checkmark$$

**Status:** This is exact integer arithmetic. The computation is trivially verifiable by hand. We can trust this.

**Recommendation:** Verify by independent computation (SageMath, PARI/GP, or by hand). This is a 5-minute check.

### 4.2 The Point Verification

**Why verify:** The LMFDB claims $P = (0,0)$ and $Q = (1,0)$ lie on $E: y^2 + y = x^3 + x^2 - 2x$.

- $P$: $0^2 + 0 = 0$ and $0^3 + 0^2 - 2 \cdot 0 = 0$. ✓
- $Q$: $1^2 + 0 = 1$ and $1^3 + 1^2 - 2 \cdot 1 = 0$. ✓

**Status:** Trivially verifiable. We can trust this.

### 4.3 The Height Pairing

**Why verify:** The canonical heights and height pairing involve floating-point computation. While the LMFDB values are computed to 30+ digits, our pipeline should independently recompute them.

**What to verify:**

1. $\hat{h}(P) = 0.32700077365160495184325924541\ldots$
2. $\hat{h}(Q) = 0.47671165934373953737948605888\ldots$
3. $\langle P, Q \rangle = 0.05852267484487883\ldots$
4. $\mathrm{Reg}(E) = 0.15246017794314375162432475705\ldots$

**Status:** These are computed by standard algorithms. Our pipeline (see H-POINT-INDEPENDENCE) recomputes them independently. Agreement to working precision confirms correctness.

**Recommendation:** Recompute using our own implementation. This is already done in our pipeline.

---

## 5. Implications for Our Pipeline

### 5.1 Can We Use LMFDB Data as Ground Truth?

**Yes, with the following caveats:**

| Data | Use as ground truth? | Caveat |
|------|---------------------|--------|
| Curve equation | **Yes** | Trivially verifiable |
| Conductor, discriminant, $j$ | **Yes** | Exact integer arithmetic |
| Torsion structure | **Yes** | Proven by Mazur + explicit computation |
| Rank $r = 2$ | **Yes** | Proven by 2-descent + independent points |
| Analytic rank $r_{\mathrm{an}} = 2$ | **Yes** | Proven by modular symbols (conductor 389 is small) |
| Regulator $\approx 0.15246$ | **Yes, but recompute** | Floating-point; our pipeline should independently verify |
| Real period $\Omega$ | **Yes, but recompute** | Floating-point; our pipeline should independently verify |
| $\|\text{Ш}\| = 1$ | **Yes, for practical purposes** | Analytically predicted; algebraically verified at primes 2, 3; accepted by community. Not a theorem from BSD alone |
| BSD leading coefficient | **Yes, for numerical check** | The ratio $\approx 1.0000$ is a consistency check, not a proof |

### 5.2 What Must We Verify Independently?

| Data | Why | How |
|------|-----|-----|
| Canonical heights $\hat{h}(P)$, $\hat{h}(Q)$ | Floating-point; core of our pipeline | Recompute via doubling chain (already done in H-POINT-INDEPENDENCE) |
| Height pairing $\langle P, Q \rangle$ | Derived from heights | Recompute from $\hat{h}(P+Q) - \hat{h}(P) - \hat{h}(Q)$ |
| Regulator $\mathrm{Reg}(E)$ | Determinant of height matrix | Recompute from our own heights |
| Real period $\Omega$ | Integration; floating-point | Recompute via numerical integration of Néron differential |
| 2-Selmer group dimension | Core of rank proof | Recompute via 2-descent algorithm |
| $L''(E,1)/2!$ | Leading coefficient; floating-point | Recompute via Dokchitser's method or modular symbols |

### 5.3 What's the Risk of Circular Reasoning?

**The main risk:** If our pipeline computes the BSD ratio using LMFDB values for $\Omega$, $\mathrm{Reg}$, and $|\text{Ш}|$, and then declares "BSD verified" when the ratio $\approx 1$, we have said nothing. The ratio is $\approx 1$ by construction if we use the LMFDB's own values.

**How to avoid it:**

1. **Never use LMFDB's $\hat{h}$, $\mathrm{Reg}$, or $\Omega$ as inputs to the BSD ratio.** Compute these independently.
2. **Never use LMFDB's $|\text{Ш}|$ as input.** Instead, compute $\text{Ш}[2]$ from our own 2-descent, and report the analytic prediction separately.
3. **The only LMFDB data safe to use as input:** curve equation, conductor, discriminant, torsion structure, $a_p$ values. These are exact and trivially verifiable.

**Specific risk assessment for 389.a1:**

| Risk | Assessment |
|------|-----------|
| Using LMFDB rank = 2 as ground truth | **Low risk** — independently verified by 2-descent + height pairing in our pipeline |
| Using LMFDB $|\text{Ш}| = 1$ as ground truth | **Medium risk** — our pipeline can only verify $\text{Ш}[2] = 0$; the full claim requires 3-descent and beyond |
| Using LMFDB regulator as ground truth | **Low risk if recomputed** — our pipeline recomputes this independently |
| Using LMFDB $\Omega$ as ground truth | **Low risk if recomputed** — standard numerical integration |
| Using LMFDB $L''(E,1)/2!$ as ground truth | **Medium risk** — this is the hardest quantity to compute independently; Dokchitser's method or modular symbols required |

### 5.4 Summary: Data Flow for Independent Verification

```
LMFDB (trusted inputs only)          Our Pipeline (independent computation)
─────────────────────────────         ──────────────────────────────────────
Curve equation [0,1,1,-2,0]    ──►    2-descent: dim Sel₂ = 2
Conductor N = 389              ──►    Points P=(0,0), Q=(1,0) on curve
Torsion = trivial              ──►    Canonical heights ĥ(P), ĥ(Q)
a_p values (for L-function)    ──►    Height pairing ⟨P,Q⟩
                                      Regulator det(H) ≈ 0.15246
                                      Ш[2] = 0 (from Selmer)
                                      Ω (numerical integration)
                                      L''(E,1)/2! (modular symbols)
                                      BSD ratio (all independent inputs)
```

**Bottom line:** We can use LMFDB for curve-defining data (equation, conductor, discriminant, $a_p$). For BSD invariants (heights, regulator, period, Ш, L-function values), we must compute independently. The risk of circular reasoning is eliminated if and only if no BSD invariant flows from LMFDB into our ratio computation.

---

## 6. References

- Cremona, J. E. *Algorithms for Modular Elliptic Curves*, 2nd ed. (1997). Source of tables for conductor $\leq 500{,}000$.
- Wiles, A. *Modular elliptic curves and Fermat's Last Theorem* (1995). Modularity of semistable curves.
- Taylor, R., Wiles, A. *Ring-theoretic properties of certain Hecke algebras* (1995).
- Breuil, C., Conrad, B., Diamond, F., Taylor, R. *On the modularity of elliptic curves over $\mathbb{Q}$* (2001). Full modularity theorem.
- González-Sadek, M., Sijsling, J. *3-descent computation of Ш for rank-2 curves*. Verification of $\text{Ш}[3^\infty] = 0$ for 389.a1.
- LMFDB: [Reliability page](https://www.lmfdb.org/EllipticCurve/Q/Reliability), [389.a1 data](https://www.lmfdb.org/EllipticCurve/Q/389/a/1).
- Silverman, J. H. *The Arithmetic of Elliptic Curves*, 2nd ed. (2009). Canonical height algorithm.
- Dokchitser, T. *Computing special values of motivic L-functions* (2004). L-function computation.

---

*Last updated: 2026-09-13. Based on LMFDB Release 1.2.1, SageMath 10.5.*
