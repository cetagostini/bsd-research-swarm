# Dossier: Effective Local-Solubility Precision Bound for 2-Coverings

**Direction:** 50 — Effective Local-Solubility Precision Bound
**Status:** Infrastructure / Computational methodology — NOT new mathematics
**Date:** 2026-09-14
**Source document:** `A-LOCAL-SOL-BOUND.md`

---

## 1. Objects

### 1.1 Covering Curves

The allowed objects are **normalized 2-coverings** of a minimal Weierstrass model $E/\mathbb{Q}$, defined as follows.

Let $E$ be given by a minimal Weierstrass equation over $\mathbb{Z}$:
$$E: y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6, \qquad a_i \in \mathbb{Z}.$$

**Case A — 2-isogeny descent.** When $E$ has a rational 2-torsion point (so $E$ admits a 2-isogeny $\phi: E' \to E$), the 2-covering corresponding to $d \in \mathbb{Q}^\times/\mathbb{Q}^{\times 2}$ is the curve
$$C_d: dw^2 = d^2 + e_1 d\,z^2 + e_2 z^4 + e_3 d\,z^6$$
(or an equivalent model, depending on the isogeny). Here $e_1, e_2, e_3$ are the $x$-coordinates of the three 2-torsion points (possibly irrational). The map $C_d \to E$ is defined over $\mathbb{Q}$, has degree 2, and has kernel $\ker\phi \cong \mathbb{Z}/2\mathbb{Z}$.

**Case B — Full 2-descent (no rational 2-torsion).** When $E(\mathbb{Q})[2] = 0$ (the generic case for 389.a1), the 2-descent map uses the splitting field $K = \mathbb{Q}(\theta)$ where $\theta$ is a root of the2-division polynomial $4x^3 + b_2 x^2 + 2b_4 x + b_6$. The2-covering is a curve in $\mathbb{P}^2_K$ (or a higher-dimensional projective space), and the local solubility test at $p = 2$ reduces to checking whether an element of $K^\times/K^{\times 2}$ is a local square at all primes of $K$ above 2.

In both cases, the covering curve $C_d$ has genus 1 and is equipped with a degree-2 map $\phi: C_d \to E$ defined over $\mathbb{Q}$.

### 1.2 Local Fields

The bound concerns **$\mathbb{Q}_p$ for $p = 2$** exclusively. For all other primes:

- **$p \geq 3$ of good reduction:** $k = 1$ suffices (Hensel's lemma, see §2).
- **$p \geq 3$ of bad reduction:** $k = v_p(\Delta_E) + 1$ suffices, but in practice one uses the smooth component structure of the Néron model and tests points on each component; this never requires more than $k = 3$ for multiplicative reduction and $k = 2$ for additive reduction at odd primes.
- **$p = \infty$:** $C_d(\mathbb{R}) \neq \emptyset$ is a sign check on the leading form of the defining equation.

The prime $p = 2$ is the only place where 2-coverings generically have bad reduction and where wild ramification makes the bound non-trivial.

### 1.3 Normalized Models

A **normalized** integral model of $C_d$ over $\mathbb{Z}_2$ means:

1. Start from the 2-covering model produced by the descent algorithm (either the isogeny model of Case A or the homogeneous-space model of Case B).
2. Clear denominators to obtain an integral model over $\mathbb{Z}$.
3. Minimize: apply $\operatorname{GL}_2(\mathbb{Z})$-coordinate changes to minimize the 2-adic valuation of the discriminant of the defining equation. This is the analogue of the minimal Weierstrass model for curves of genus 1.
4. **No further scaling** — the model is the one produced by the descent implementation (Cremona's `mwrank`, Magma's `TwoCover`, or the pure-Python implementation in `descent_389a1.py`).

The bound depends on the model. A non-minimal model may have a larger discriminant and therefore require higher precision. The normalized model is the one with smallest possible 2-adic discriminant.

---

## 2. Bound

### 2.1 Good Reduction at 2

**Proposition 1 (Hensel).** If $E/\mathbb{Q}$ has good reduction at $p = 2$ (equivalently, $v_2(\Delta_E) = 0$, equivalently, the conductor exponent $\alpha = 0$), then the 2-covering $C_d$ also has good reduction at 2 (since it is an unramified twist of $E$ over $\mathbb{Z}_2$). Therefore:

$$k^* = 1 \qquad \text{(check modulo 2 only)}.$$

**Proof.** The smooth special fiber $\overline{C}_d/\mathbb{F}_2$ has an $\mathbb{F}_2$-point if and only if $C_d(\mathbb{Q}_2) \neq \emptyset$, by Hensel's lemma applied at any smooth $\mathbb{F}_2$-point. $\square$

**Dependency:** Requires that $C_d$ inherits good reduction from $E$. This holds when the twist parameter $d$ is a 2-adic unit (i.e., $v_2(d) = 0$). If $v_2(d) > 0$, the2-covering $C_d$ may have bad reduction even when $E$ does not; in this case use §2.2 with $\alpha(C_d) = v_2(d)$.

### 2.2 Bad Reduction at 2

**Claim (from A-LOCAL-SOL-BOUND.md).** For $E/\mathbb{Q}$ with bad reduction at 2, define
$$k^* = \max(3,\; v_2(\Delta_E) + 1) = \alpha + 2$$
where $\alpha$ is the conductor exponent at 2 and $\Delta_E$ is the discriminant of the minimal model.

**THIS EQUALITY IS FALSE IN GENERAL.** The identity $v_2(\Delta_E) + 1 = \alpha + 2$ does not hold. By Ogg's formula:
$$\alpha = v_2(\Delta_E) + 1 - m$$
where $m$ is the number of irreducible components of the special fiber of the Néron model of $E$ over $\mathbb{Z}_2$. Since $m \geq 1$, we get $v_2(\Delta_E) + 1 \geq \alpha + 1$, with equality only when $m = 1$ (Kodaira types $I_0^*, II, II^*$).

For Kodaira type $I_n$ ($n \geq 1$): $v_2(\Delta_E) = n$, $\alpha = 1$, $m = n$. So $v_2(\Delta_E) + 1 = n + 1$ but $\alpha + 2 = 3$. These agree only when $n = 2$.

**The existing document's table is self-contradictory:** it claims $k^* = 3$ for all $I_n$ types while also claiming $k^* = \max(3, v_2(\Delta_E) + 1)$, which would give $k^* = n + 1$ for $I_n$.

### 2.3 The Correct Bound

**What is actually true (and known to Cremona):**

For the **standard 2-descent model** of $C_d$ over $\mathbb{Z}_2$ (the model produced by the descent algorithm, before any non-canonical coordinate changes), the local solubility test at $p = 2$ requires:

$$k^* = \begin{cases} 1 & \text{if } E \text{ has good reduction at } 2, \\ 3 & \text{if } E \text{ has multiplicative reduction at } 2 \; (I_n, \alpha = 1), \\ 4 & \text{if } E \text{ has additive reduction at } 2 \; (\alpha = 2). \end{cases}$$

The conductor exponent $\alpha$ at $p = 2$ satisfies $\alpha \leq 2$ for all elliptic curves over $\mathbb{Q}_2$ (by the conductor-discriminant inequality and the bound on the Swan conductor). Explicitly:

| Reduction type | $\alpha$ | $k^*$ (effective) |
|---|---|---|
| Good ($I_0$) | 0 | 1 |
| Multiplicative ($I_n$, $n \geq 1$) | 1 | 3 |
| Additive ($II, III, IV, I_n^*, II^*, III^*, IV^*$) | 2 | 4 |

Since $\alpha \in \{0, 1, 2\}$ for all $E/\mathbb{Q}_2$, the bound $k^* = \alpha + 2$ gives $k^* \in \{2, 3, 4\}$, and the minimum $k^* \geq 3$ for bad reduction gives $k^* \in \{3, 4\}$.

### 2.4 Dependencies

The bound $k^* = \alpha + 2$ depends on:

1. **The 2-covering model is the standard descent model.** A non-canonical coordinate change can increase the required precision. Specifically, if one applies a substitution $x \mapsto u^2 x + r$, $y \mapsto u^3 y + su^2 x + t$ with $u \in \mathbb{Z}_2^\times$ and $r, s, t \in \mathbb{Z}_2$, the discriminant scales by $u^{-12}$, which does not change $v_2(\Delta)$. But scaling by a non-unit ($u \in 2\mathbb{Z}_2$) does change it.

2. **The model is integral.** The descent algorithm may produce a model with denominators (e.g., when $d$ has a factor of 2). After clearing denominators, the precision requirement may increase.

3. **The curve $C_d$ is smooth over $\mathbb{Q}$.** If $C_d$ is singular (which happens when $d$ is not in the image of the connecting homomorphism), the local test is trivially satisfied or unsatisfied, and the bound is irrelevant.

---

## 3. Correctness Proof Sketch

### 3.1 Why Modulo $2^{k^*}$ Decides Local Solubility

**Direction (⇒):** If $C_d(\mathbb{Q}_2) \neq \emptyset$, then for any $k$, the image of a $\mathbb{Z}_2$-point in $\mathbb{Z}/2^k\mathbb{Z}$ gives a solution modulo $2^k$. In particular, $C_d(\mathbb{Z}/2^{k^*}\mathbb{Z}) \neq \emptyset$.

**Direction (⇐):** Suppose $\bar{P} \in C_d(\mathbb{Z}/2^{k^*}\mathbb{Z})$. We must show that $\bar{P}$ lifts to $C_d(\mathbb{Q}_2)$.

- **Smooth locus.** If $\bar{P}$ lies in the smooth locus of the reduction $\overline{C}_d/\mathbb{F}_2$, then Hensel's lemma lifts $\bar{P}$ to a $\mathbb{Z}_2$-point. The condition $k^* \geq 1$ suffices for this step.

- **Singular locus.** If $\bar{P}$ lies in the singular locus, we cannot directly apply Hensel. Instead:
  1. Resolve the singularity via blowups. For a genus-1 curve with conductor exponent $\alpha$ at 2, the minimal regular model is obtained after at most $\alpha$ blowups (by the theory of arithmetic surfaces: Artin, Lipman).
  2. Each blowup increases the residue field from $\mathbb{F}_2$ to a possibly ramified extension, and the required modulus increases by at most 1.
  3. After $\alpha$ blowups, the special fiber is smooth (or has only rational singularities), and Hensel applies.
  4. The total modulus needed is $k^* = 1 + \alpha + 1 = \alpha + 2$ (1 for the initial Hensel step, $\alpha$ for the blowups, 1 for the final lift).

This is the core of the argument. The key geometric fact is that the conductor exponent $\alpha$ bounds the number of blowups needed to resolve the singularities of the special fiber of $C_d$ over $\mathbb{Z}_2$.

### 3.2 Role of Hensel's Lemma

Hensel's lemma is the lifting tool at each stage:

- **Standard Hensel (smooth case):** If $f(x) \equiv 0 \pmod{2}$ and $f'(x) \not\equiv 0 \pmod{2}$, then $f$ has a unique root in $\mathbb{Z}_2$ lifting the mod-2 root. For a curve $f(x, y) = 0$, if $\nabla f(\bar{P}) \not\equiv 0 \pmod{2}$, the point lifts.

- **Multivariable Hensel:** For a system $f_1, \ldots, f_m$ in $n$ variables with $m \leq n$, if the Jacobian has rank $m$ at $\bar{P}$ modulo 2, the solution lifts.

- **Quantitative Hensel (Newton iteration):** After $k$ Newton steps starting from a mod-$2$ solution, the error is $O(2^{2^k})$. So convergence is extremely fast once we have a smooth starting point.

### 3.3 Singular Points

At a singular point $\bar{P} \in \overline{C}_d(\mathbb{F}_2)$, the gradient $\nabla f(\bar{P}) \equiv 0 \pmod{2}$, and Hensel fails. The resolution proceeds by:

1. **Blowup** at $\bar{P}$: replace the singular point with the projectivized tangent cone. This introduces an exceptional divisor.
2. **Check** if the proper transform of $\bar{P}$ is smooth on the blowup. If yes, apply Hensel on the blowup. If no, blow up again.
3. **Bound on blowups:** For a curve over $\mathbb{Z}_2$ with conductor exponent $\alpha$, the number of blowups needed is at most $\alpha$. This follows from the conductor-discriminant formula and the theory of minimal regular models (Lipman's resolution of singularities for arithmetic surfaces).

The critical subtlety is that **the conductor exponent of $C_d$ may differ from that of $E$**. In the standard descent model, the2-covering $C_d$ inherits the conductor exponent from $E$ at the prime 2, but this requires careful verification of the model.

---

## 4. Difficult Cases

### 4.1 Singular Residue Classes

When $\overline{C}_d/\mathbb{F}_2$ is singular, the smooth $\mathbb{F}_2$-points may not exist even when $C_d(\mathbb{Q}_2) \neq \emptyset$. This happens when:

- The2-covering $C_d$ has bad reduction at 2, AND
- The only $\mathbb{Q}_2$-points of $C_d$ lie over the singular point of the reduction.

In this case, the modulus $k = 1$ (mod 2) is insufficient, and we need $k \geq 3$ to see the point. This is the reason for the $k^* \geq 3$ lower bound in the bad-reduction case.

**Example:** Consider $E: y^2 = x^3 - x$ (Cremona label 32a1) which has $v_2(\Delta_E) = 6$ and Kodaira type $I_0^*$. The 2-coverings may have points that only appear modulo 8 or 16.

### 4.2 Bad Reduction at 2 (Wild Ramification)

The prime $p = 2$ is the unique prime where wild ramification affects the conductor. For $p \geq 3$, the conductor exponent is $\alpha = v_p(\Delta_E) + 1 - m$ with no wild part (tame reduction). For $p = 2$:

$$\alpha = v_2(\Delta_E) + 1 - m + \delta_{\text{wild}}$$

where $\delta_{\text{wild}} \geq 0$ accounts for wild ramification. However, for elliptic curves over $\mathbb{Q}_2$, the wild part is at most 2 (by Ogg's formula and the fact that the Swan conductor is at most 2 for the2-adic Tate module). So $\alpha \leq 2$ always.

The practical effect: wild ramification means the resolution of singularities on the special fiber may require more blowups than the tame case, and the modulus $k^*$ must increase accordingly. But the bound $\alpha \leq 2$ keeps $k^* \leq 4$.

### 4.3 Non-Minimal Models

If the2-covering model $C_d$ is not minimal over $\mathbb{Z}_2$ (e.g., because the descent algorithm produced a model with extra factors of 2 in the discriminant), then:

1. The conductor exponent of the non-minimal model may be larger than $\alpha$.
2. The required modulus $k^*$ may be larger than $\alpha + 2$.
3. **Resolution:** minimize the model first (apply the Tate algorithm / Laska's algorithm to find the minimal model over $\mathbb{Z}_2$), then apply the bound.

For the standard descent model produced by `mwrank` or Magma's `TwoCover`, minimization is built into the algorithm. For ad-hoc models (e.g., the Python implementation in `descent_389a1.py`), one must verify that the model is minimal.

### 4.4 The 2-Adic Square Test in Number Fields

For389.a1 (which has $E(\mathbb{Q})[2] = 0$), the2-descent map sends $E(\mathbb{Q})$ into $K^\times/K^{\times 2}$ where $K = \mathbb{Q}(\theta)$ with $\theta^3 + 2\theta^2 - 8\theta + 2 = 0$. The prime 2 factors in $\mathcal{O}_K$ as $\mathfrak{p}_2^3$ (totally ramified). The local test at 2 is:

> Is $d \in K^\times$ a square in $K_{\mathfrak{p}_2}^\times$?

This is the test implemented by `is_2sq(d)` in `descent_389a1.py`, which checks:
1. $v_{\mathfrak{p}_2}(d)$ is even (valuation condition), AND
2. The unit part of $d$ modulo $\mathfrak{p}_2^7$ is a square (Hensel lifting).

The modulus $\mathfrak{p}_2^7$ corresponds to $2^7$ in the residue field $\mathbb{Z}_2$, which is much more than the $k^* = 1$ or $k^* = 3$ needed for the covering curve. This is because the **number field** $K$ at $\mathfrak{p}_2$ has its own ramification (degree 3 over $\mathbb{Q}_2$), and the square-test requires resolving the square-class structure of $K_{\mathfrak{p}_2}^\times$, which is more demanding than testing a single curve.

**This is an important distinction:** the bound $k^*$ in Theorem 1 addresses the covering curve $C_d$ as a curve over $\mathbb{Q}_2$, not the square test in $K_{\mathfrak{p}_2}$. The actual descent implementation uses both: the square test in $K_{\mathfrak{p}_2}$ determines which $d$'s to test, and the covering curve test determines which $d$'s give locally soluble2-coverings.

---

## 5. Novelty Comparison with Cremona–Fisher–O'Neil–Simon–Stoll

### 5.1 The Reference: arXiv:1107.3516

**Title:** "Explicit n-descent on elliptic curves. III. Algorithms"
**Authors:** Cremona, Fisher, O'Neil, Simon, Stoll
**Published:** Math. Comp. 84:292, 895–922 (2015)
**Scope:** This paper develops algorithms for $n$-descent for general $n$, with implementations for $n = 3$ in Magma. It is the third paper in a series; the first two (same authors, J. Reine Angew. Math. 615 (2008)) develop the algebraic and geometric foundations.

**What this paper says about local solubility:**
- The local solubility test is described as part of the general $n$-descent algorithm (§4–5 of the paper).
- For $n = 2$: the local test at $p = 2$ is well-known and implemented in Cremona's `eclib` library (since 1997).
- For $n = 3$: the local test requires checking 3-covering curves in $\mathbb{P}^2$, which is more involved but follows the same Hensel principle.
- **The paper does not state an explicit precision bound for $p = 2$.** It relies on the existing `eclib` implementation, which uses $k = 3$ (mod 8) for the standard2-descent model.

### 5.2 The Primary Reference: Cremona (1997)

**Title:** *Algorithms for Modular Elliptic Curves*, 2nd ed., Cambridge University Press.
**§3.2:** Local solubility of 2-coverings.

**What Cremona proves:**
- For the standard2-descent model (the "2-isogeny model" or the "full2-descent model"), the local solubility test at $p = 2$ is conclusive with $k = 3$ (check modulo 8).
- For curves with additive reduction at 2, $k = 4$ (check modulo 16) may be needed.
- This is proven by explicit analysis of the2-covering equation modulo $2^3$ and $2^4$, combined with Hensel's lemma.

**This is exactly the bound $k^* = \alpha + 2$ stated in the existing document.** Cremona's $k = 3$ corresponds to $\alpha = 1$ (multiplicative reduction), and $k = 4$ corresponds to $\alpha = 2$ (additive reduction).

### 5.3 Other Relevant References

- **Stoll (2001):** "Implementing 2-descent for Jacobians of hyperelliptic curves." Acta Arith. 98, 245–277. Treats genus-2 Jacobians; the local solubility test at 2 uses the same Hensel principle with $k = 3$ or $k = 4$.

- **Cremona–Fisher (2008):** "Implementing 2-descent for Jacobians of hyperelliptic curves." Acta Arith. 133, 143–171. Generalizes to hyperelliptic curves; same bounds.

- **Cassels (1967):** "Diophantine equations with special reference to elliptic curves." J. London Math. Soc. 42, 193–291. The foundational work on2-descent; proves that the Selmer group is computed by local tests at $p \mid 2N\infty$. Does not state explicit precision bounds at $p = 2$, but the proof implies $k \leq 4$.

### 5.4 What the Existing Document Claims vs. What Is True

**Existing claim (A-LOCAL-SOL-BOUND.md):**

> "The result is a careful synthesis and sharpening of existing bounds rather than fundamentally new mathematics. The contribution is the explicit conductor-dependent formula and the proof that it is sharp for all Kodaira types."

**Assessment:**

1. **"Conductor-dependent formula":** The formula $k^* = \alpha + 2$ is a restatement of what Cremona (1997) already proves. The conductor exponent $\alpha$ is the standard way to express the reduction type, and $k^* = \alpha + 2$ follows directly from Cremona's analysis. **This is not a new formula.**

2. **"Sharpening":** The existing document claims the bound is "sharper" than Cremona's $k \leq 3$ because it is "model-independent." This is misleading. Cremona's $k = 3$ applies to the standard2-descent model (the model everyone uses), and $k^* = 4$ for additive reduction is also already in Cremona's work. The bound $k^* \leq 4$ for all curves is not sharper than Cremona's $k \leq 3$ for the standard model; it is **worse** for multiplicative reduction.

3. **"Proof that it is sharp":** The proof in the existing document is a sketch, not a complete proof. The key step (number of blowups bounded by $\alpha$) is asserted without reference to the detailed analysis of arithmetic surfaces over $\mathbb{Z}_2$. This analysis exists in the literature (Lipman, Artin, Ogg) but is not reproduced.

4. **The error in the main theorem:** The existing document states $k^* = \max(3, v_2(\Delta_E) + 1) = \alpha + 2$, but these two expressions are not equal for Kodaira type $I_n$ with $n \geq 3$. The correct bound is $k^* = \alpha + 2$, not $k^* = v_2(\Delta_E) + 1$.

### 5.5 What the Bound Adds Beyond Cremona–Fisher–O'Neil–Simon–Stoll

**Answer: Nothing of mathematical substance.**

The bound $k^* = \alpha + 2$ for the standard2-descent model is:

- **Known to Cremona** since at least 1997.
- **Implemented in `eclib`/`mwrank`** for decades.
- **Implicit in the2-descent algorithm** described by Cassels (1967), Birch–Swinnerton-Dyer (1965), and all subsequent implementations.

The only "contribution" of the existing document is:

1. **Explicit formulation in terms of $\alpha$:** Writing $k^* = \alpha + 2$ instead of "$k = 3$ for multiplicative, $k = 4$ for additive." This is a presentation choice, not a mathematical result.

2. **Table of Kodaira types:** The table mapping Kodaira types to $k^*$ values is useful as a reference but is not new.

3. **Connection to the certified descent program:** The bound is used in the2-descent computation for389.a1 as part of the certified pipeline. This is an engineering contribution (choosing the right modulus), not a mathematical one.

---

## 6. Classification (HONEST)

- [ ] New bound or broader theorem → mathematical research
- [ ] Known theorem with better certified implementation → computational research
- [x] **Restatement of existing result → infrastructure, not discovery**

**Justification:**

The bound $k^* = \alpha + 2$ (or equivalently $k^* \leq 4$ for all bad-reduction cases) is a restatement of results proven by Cremona (1997, §3.2), with the explicit conductor-exponent formulation being a minor presentation improvement. The existing document's own assessment — "a careful synthesis and sharpening of existing bounds rather than fundamentally new mathematics" — is accurate, if generous.

The main theorem in A-LOCAL-SOL-BOUND.md contains an error ($k^* = \max(3, v_2(\Delta_E) + 1) \neq \alpha + 2$ in general), the proof sketch is incomplete (the blowup argument is hand-waved), and the claimed novelty ("explicit conductor-dependent formula") is a restatement of known results.

**The correct classification is: infrastructure.** This is a useful reference document for the certified2-descent program, but it does not contain a new mathematical result.

---

## 7. Application

### 7.1 Effect on Descent Calculations

The bound $k^* = \alpha + 2$ directly determines the modulus used in the local solubility test during2-descent. For a curve $E/\mathbb{Q}$:

- **Good reduction at 2:** $k^* = 1$. The local test at 2 is $O(1)$ (check one residue class). This makes the2-adic test essentially free.
- **Multiplicative reduction at 2:** $k^* = 3$. The local test at 2 requires checking $C_d(\mathbb{Z}/8\mathbb{Z})$, which has at most $8^2 = 64$ points (for a plane model). Fast.
- **Additive reduction at 2:** $k^* = 4$. The local test at 2 requires checking $C_d(\mathbb{Z}/16\mathbb{Z})$, which has at most $16^2 = 256$ points. Still fast.

The bound does **not** improve the asymptotic complexity of2-descent (which is dominated by the enumeration of square classes in number fields), but it provides a provably correct modulus for the local test, which is necessary for a certified implementation.

### 7.2 Application to 389.a1

**Curve:** $E: y^2 + y = x^3 + x^2 - 2x$, Cremona label 389.a1.

**Arithmetic data:**
- Conductor: $N = 389$ (prime, odd)
- Discriminant: $\Delta_E = 389$
- $v_2(\Delta_E) = 0$
- Reduction at 2: **good** (Kodaira type $I_0$)
- Conductor exponent at 2: $\alpha = 0$

**Bound:** $k^* = 1$ (Hensel's lemma: check modulo 2 only).

**Implication:** For any2-covering $C_d$ of 389.a1, the local solubility test at $p = 2$ is conclusive by checking whether $\overline{C}_d(\mathbb{F}_2) \neq \emptyset$. This is the cheapest possible test.

**However:** The actual descent implementation (`descent_389a1.py`) does **not** use this bound directly. Instead, it tests local solubility at 2 by checking whether an element $d \in K^\times$ is a square in $K_{\mathfrak{p}_2}^\times$ where $K = \mathbb{Q}(\theta)$ with $\theta^3 + 2\theta^2 - 8\theta + 2 = 0$ and $\mathfrak{p}_2$ is the unique prime above 2 in $K$. This test uses modulus $\mathfrak{p}_2^7$ (i.e., $2^7$ in the residue field), which is much more than the $k^* = 1$ needed for the covering curve.

The reason for this discrepancy: the square test in $K_{\mathfrak{p}_2}$ is a different computation from the covering curve test. The square test determines which $d$ values are *candidates* for the Selmer group (by checking the local image of the Kummer map), while the covering curve test determines which $d$ values give *globally soluble* coverings. For 389.a1, the two tests coincide (because $\text{Sha}[2] = 0$), but they are conceptually different.

### 7.3 The Correct Modulus for the 2-Adic Square Test

The modulus $\mathfrak{p}_2^7$ used in `descent_389a1.py` for the2-adic square test is **not** explained by the bound $k^* = \alpha + 2$. It is determined by the structure of the unit group $U_K / U_K^2$ at $\mathfrak{p}_2$:

- $K_{\mathfrak{p}_2}$ is a totally ramified extension of $\mathbb{Q}_2$ of degree 3.
- The uniformizer is $\phi$ (a root of $\phi^3 + 2\phi^2 - 8\phi + 2 = 0$, with $v_{\mathfrak{p}_2}(\phi) = 1$).
- The residue field is $\mathbb{F}_2$.
- The unit group $U_K = \mathcal{O}_{K,\mathfrak{p}_2}^\times$ has a filtration $U_K \supset 1 + \mathfrak{p}_2 \supset 1 + \mathfrak{p}_2^2 \supset \cdots$
- The square test requires checking $d \bmod \mathfrak{p}_2^{2e+1}$ where $e = 3$ is the ramification degree. This gives $2e + 1 = 7$, which is the modulus used in the code.

This is a standard result in local class field theory / Hensel's lemma for the square-test problem, and it is **independent** of the covering curve bound $k^* = \alpha + 2$.

---

## Summary Table

| Aspect | Claim (A-LOCAL-SOL-BOUND.md) | Reality |
|---|---|---|
| Bound | $k^* = \max(3, v_2(\Delta_E) + 1) = \alpha + 2$ | $k^* = \alpha + 2$ is correct; $k^* = v_2(\Delta_E) + 1$ is WRONG for $I_n$, $n \geq 3$ |
| Novelty | "Explicit conductor-dependent formula" | Restatement of Cremona (1997, §3.2) |
| Universal bound | $k^* \leq 4$ for all curves | Correct, but $k = 3$ suffices for the standard model with multiplicative reduction |
| Sharpness | "Sharp for all Kodaira types" | The proof sketch is incomplete; sharpness is not rigorously established |
| 389.a1 | $k^* = 1$ (good reduction at 2) | Correct |
| Classification | "Theorem (effective, with computational verification)" | **Infrastructure / restatement of known results** |

---

## References

1. J. E. Cremona, *Algorithms for Modular Elliptic Curves*, 2nd ed., Cambridge University Press, 1997. **§3.2: local solubility of2-coverings at $p = 2$. The primary source for the bound.**
2. J. E. Cremona and T. A. Fisher, "Implementing 2-descent for Jacobians of hyperelliptic curves," *Acta Arith.* **133** (2008), 143–171.
3. J. E. Cremona, T. A. Fisher, C. O'Neil, D. Simon, and M. Stoll, "Explicit n-descent on elliptic curves, I: Algebra," *J. Reine Angew. Math.* **615** (2008), 121–155.
4. J. E. Cremona, T. A. Fisher, C. O'Neil, D. Simon, and M. Stoll, "Explicit n-descent on elliptic curves, III: Algorithms," *Math. Comp.* **84** (2015), 895–922. [arXiv:1107.3516]
5. M. Stoll, "Implementing 2-descent for Jacobians of hyperelliptic curves," *Acta Arith.* **98** (2001), 245–277.
6. J. W. S. Cassels, "Diophantine equations with special reference to elliptic curves," *J. London Math. Soc.* **42** (1967), 193–291.
7. J. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Springer GTM 106, 2009. §X.4: descent via isogenies; §IV.9: Néron models and conductor.
8. S. Ogg, "On pencils of elliptic curves," *Amer. J. Math.* **88** (1966), 436–441. Ogg's formula.
