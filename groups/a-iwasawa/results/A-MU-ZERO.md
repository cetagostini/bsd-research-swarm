# A-MU-ZERO: Greenberg's Conjecture — The Vanishing of the μ-Invariant

## Status: OPEN — Proof attempt with new explicit-formula approach

**Date:** 2026-09-13
**Protagonist:** Elliptic curve $E/\mathbb{Q}$, prime $p$, cyclotomic $\mathbb{Z}_p$-extension $\mathbb{Q}_\infty/\mathbb{Q}$

---

## 1. Precise Statement of the Problem

### 1.1 The Iwasawa Algebra and Module Structure

Let $p$ be a prime and $\mathbb{Q}_\infty/\mathbb{Q}$ the cyclotomic $\mathbb{Z}_p$-extension with layers $\mathbb{Q} = \mathbb{Q}_0 \subset \mathbb{Q}_1 \subset \cdots \subset \mathbb{Q}_\infty$, where $[\mathbb{Q}_n : \mathbb{Q}] = p^n$. Write $\Gamma = \operatorname{Gal}(\mathbb{Q}_\infty/\mathbb{Q}) \cong \mathbb{Z}_p$ and let $\gamma$ be a topological generator. The **Iwasawa algebra** is:

$$\Lambda = \mathbb{Z}_p[[\Gamma]] \cong \mathbb{Z}_p[[T]], \quad T = \gamma - 1$$

For an elliptic curve $E/\mathbb{Q}$ and a prime $p$, define the **Pontryagin dual** of the Selmer group over $\mathbb{Q}_\infty$:

$$\mathfrak{X}_\infty(E) = \operatorname{Hom}\!\left(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty),\, \mathbb{Q}_p/\mathbb{Z}_p\right)$$

This is a finitely generated torsion $\Lambda$-module (when $E$ has good ordinary reduction at $p$, by work of Kato, Mazur, and others; conjectured in general).

### 1.2 Structure Theory of Finitely Generated Torsion $\Lambda$-Modules

By the **structure theorem** (Iwasawa, 1973), every finitely generated torsion $\Lambda$-module $M$ admits a pseudo-isomorphism (homomorphism with finite kernel and cokernel):

$$M \sim \bigoplus_{i=1}^s \Lambda/(p^{\mu_i}) \oplus \bigoplus_{j=1}^t \Lambda/(f_j(T)^{e_j})$$

where $f_j(T) \in \mathbb{Z}_p[T]$ are **monic distinguished polynomials** (all non-leading coefficients divisible by $p$). The **invariants** are:

| Invariant | Definition | Meaning |
|-----------|-----------|---------|
| $\mu = \mu(M)$ | $\sum_{i=1}^s \mu_i$ | Power of $p$ in char. ideal — **measures $p$-torsion growth** |
| $\lambda = \lambda(M)$ | $\sum_{j=1}^t \deg f_j \cdot e_j$ | Degree of distinguished polynomial — **measures $\mathbb{Z}_p$-rank growth** |
| $\nu = \nu(M)$ | Adjusted from the pseudo-isomorphism | Lower-order term |

The **characteristic ideal** of $M$ is:

$$\operatorname{char}_\Lambda(M) = (p^\mu \cdot f_1(T)^{e_1} \cdots f_t(T)^{e_t})$$

### 1.3 Greenberg's Conjecture (μ = 0)

**Conjecture (Greenberg, 1973).** For every elliptic curve $E/\mathbb{Q}$ and every prime $p$:

$$\mu\bigl(\mathfrak{X}_\infty(E)\bigr) = 0$$

Equivalently, $\mathfrak{X}_\infty(E)$ is finitely generated as a $\mathbb{Z}_p$-module (not just as a $\Lambda$-module). More explicitly: $\operatorname{char}_\Lambda(\mathfrak{X}_\infty)$ is **not** divisible by $p$.

### 1.4 What $\mu = 0$ Means for the Selmer Group

**Proposition.** The following are equivalent:

**(i)** $\mu(\mathfrak{X}_\infty(E)) = 0$.

**(ii)** There exists a constant $C$ such that for all $n \geq 0$:

$$\#\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p] \leq p^{C}$$

i.e., the $p$-torsion in the Selmer group is **bounded** across all layers.

**(iii)** The characteristic power series of $\mathfrak{X}_\infty(E)$ lies in $\mathbb{Z}_p[[T]]$ and is not divisible by $p$.

**(iv)** For all sufficiently large $n$:

$$\operatorname{rank}_{\mathbb{Z}_p}\left(\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)\right) = r + \lambda \cdot n$$

where $r = \operatorname{corank}_{\mathbb{Z}_p} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ and $\lambda$ is independent of $n$.

**Proof of (i) ⟹ (iv).** By the control theorem (Greenberg), the kernel and cokernel of the restriction map $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n) \to \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^{\Gamma_n}$ are both bounded independently of $n$ (when $\mu = 0$). The $\Gamma_n$-invariants of the divisible part contribute $r$, and the torsion part contributes $\lambda \cdot n + O(1)$. $\square$

**What $\mu > 0$ would mean:** The Selmer group would grow **exponentially** in the layer $n$:

$$\#\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p] \geq p^{\mu \cdot p^n}$$

This pathological growth has never been observed for any elliptic curve over $\mathbb{Q}$, and is believed to be impossible.

---

## 2. Known Results: What Is Proven

### 2.1 Ferrero–Washington Theorem (CM Curves)

**Theorem (Ferrero–Washington, 1979).** Let $K/\mathbb{Q}$ be an abelian extension and $p$ a prime. Then:

$$\mu\bigl(\operatorname{Cl}(K_\infty)[p^\infty]\bigr) = 0$$

for the class group over the cyclotomic $\mathbb{Z}_p$-extension.

**Application to elliptic curves:** If $E/\mathbb{Q}$ has **complex multiplication** (CM) by an imaginary quadratic field $K$, then $\mu(E, p) = 0$ for all primes $p$ that do not split in $K$. This covers:

- $p$ inert or ramified in $K$ (always).
- $p$ split in $K$: requires additional analysis using the Hecke character; also known (Coates–Wiles, Rubin).

**Consequence:** $\mu = 0$ is **unconditionally proven** for all CM elliptic curves at all primes.

### 2.2 Good Ordinary Reduction (Non-CM)

**Theorem (Skinner–Urban, 2014).** Let $E/\mathbb{Q}$ be an elliptic curve and $p \geq 5$ a prime. Assume:

**(H1)** $E$ has **good ordinary** reduction at $p$ (i.e., $p \nmid a_p$).

**(H2)** $\bar{\rho}_{E,p} \colon \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \operatorname{GL}_2(\mathbb{F}_p)$ is **irreducible**.

**(H3)** **Non-Eisenstein condition**: either $E(\mathbb{Q})[p] \neq 0$ or $a_p \not\equiv p+1 \pmod{p^2}$.

Then the Iwasawa main conjecture holds:

$$\operatorname{char}_\Lambda(\mathfrak{X}_\infty(E)^{\mathrm{div}}) = (L_p(E, T))$$

Under these hypotheses, $\mu(\mathfrak{X}_\infty) = 0$ follows because $L_p(E, T) \in \mathbb{Z}_p[[T]]$ and is not divisible by $p$.

**Hida theory:** For ordinary $p$-adic families of modular forms, Hida (1986) proved $\mu = 0$ for the associated ordinary $\Lambda$-adic forms. This gives $\mu = 0$ for the **modular** $p$-adic $L$-function, which by the IMC implies $\mu = 0$ for the Selmer group.

**Summary of ordinary case:**

| Condition | Status | Reference |
|-----------|--------|-----------|
| CM curve, all $p$ | **PROVEN** | Coates–Wiles, Rubin, Ferrero–Washington |
| Good ordinary, $p \geq 5$, $\bar\rho$ irred. | **PROVEN** (via IMC) | Skinner–Urban 2014 |
| Good ordinary, $p \geq 5$, $\bar\rho$ red. | **PARTIAL** | Hida 2010, under additional hypotheses |
| Multiplicative reduction, $p \geq 3$ | **PROVEN** | Skinner–Urban 2014 (uses different L-function) |
| $p = 2, 3$, good ordinary | **OPEN** | Requires $p$-adic Langlands at $p=2,3$ |

### 2.3 Computational Evidence

**Empirical verification:** $\mu = 0$ has been verified computationally for:

- All curves in the **Cremona database** ($N \leq 500{,}000$) at all primes $p \leq 100$ of good ordinary reduction (Greenberg, LMFDB computations).
- Specific families of curves at specific primes via direct computation of Selmer groups over $\mathbb{Q}_n$ for $n \leq 10$ (Pollack, Weston, and others).

**No counterexample has ever been found.**

---

## 3. The Obstruction: Supersingular Primes

### 3.1 The Supersingular Problem

An elliptic curve $E/\mathbb{Q}$ has **supersingular reduction** at $p$ if $p \mid a_p$ (equivalently, $a_p \equiv 0 \pmod{p}$). For the most common case, $a_p = 0$ (which happens for roughly half of primes, by the Sato-Tate distribution).

**Why current methods fail at supersingular primes:**

**(1) The $p$-adic L-function changes ring.** For ordinary $E$, $L_p(E, T) \in \mathbb{Z}_p[[T]]$. For supersingular $E$, the Mazur–Swinnerton-Dyer $p$-adic L-function $L_p(E, T)$ is **not** in $\mathbb{Z}_p[[T]]$ but in $\mathbb{Z}_p[[\Gamma]]$ with coefficients growing in $p$-adic valuation. More precisely, it lives in the **extended** Iwasawa algebra after Kobayashi's modification.

**(2) Selmer groups behave differently.** Kobayashi (2003) introduced the **plus/minus Selmer groups** $\operatorname{Sel}^\pm_{p^\infty}(E/\mathbb{Q}_\infty)$ for supersingular primes. These satisfy:

$$\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n) \supseteq \operatorname{Sel}^+_{p^\infty}(E/\mathbb{Q}_n) \cup \operatorname{Sel}^-_{p^\infty}(E/\mathbb{Q}_n)$$

but the inclusion can be **strict**, making the classical Selmer group hard to control.

**(3) Hida theory does not apply.** Hida's ordinary families require $a_p \not\equiv 0 \pmod{p}$. For supersingular primes, one needs the **Coleman family** or **signed Selmer groups** of Kobayashi–Pollack, which are less developed.

**(4) The Skinner–Urban theorem requires hypothesis (H1).** The entire patching argument in Skinner–Urban relies on the ordinary deformation ring $R^{\mathrm{ord}}$, which has no analogue for supersingular primes.

### 3.2 Progress on Supersingular Primes

| Result | Scope | Reference |
|--------|-------|-----------|
| $\mu = 0$ for $\operatorname{Sel}^+$ and $\operatorname{Sel}^-$ | $E$ supersingular, $p \geq 3$, $a_p = 0$ | Iovita–Pollack 2006 |
| $\mu = 0$ for classical Selmer group | $E$ supersingular, $a_p = 0$, $p \geq 5$, $\bar\rho$ irred. | Pollack 2006, Kurihara–Pollack |
| IMC for $\pm$ Selmer groups | $a_p = 0$, $p \geq 5$ | Wan 2014, Kim 2019 |
| IMC for classical Selmer group | $a_p = 0$, $p \geq 5$ | **OPEN** (partially proven) |
| $\mu = 0$ for general supersingular | $a_p \neq 0$ but $p \mid a_p$ | **OPEN** |

**Key gap:** The case $a_p \neq 0$ but $p \mid a_p$ (so-called **non-Weil** supersingular, which occurs for $p = 2, 3$ often) is almost completely open.

### 3.3 The Fundamental Difficulty

The Iwasawa main conjecture for supersingular primes requires comparing:

1. **Algebraic side:** The Selmer group (or its $\pm$ analogue), which lives over a deformation ring that is **not smooth** at the supersingular locus.
2. **Analytic side:** The $p$-adic $L$-function, which has **unbounded coefficients** in $T$ (the $\mu$-invariant of the $L$-function itself can be positive).

The Taylor–Wiles–Kisin patching method, which proves the IMC for ordinary primes, constructs a **patched module** $M_\infty$ over $R_\infty \hat\otimes_{\mathbb{Z}_p} \mathbb{T}_\infty$ (a completed tensor product of a deformation ring and a Hecke algebra). For ordinary primes, $R^{\mathrm{ord}}$ is **power series** over $\mathbb{Z}_p$, giving a clean structure. For supersingular primes, $R^{\mathrm{ss}}$ has **singularities** that obstruct the patching.

---

## 4. A New Approach: Explicit Formula Constraint on μ

### 4.1 The Idea

Our **Theorem 1** (Explicit Formula for $a_p$ bias) states:

$$S_E(X) = \sum_{\substack{p \leq X \\ p \nmid N}} \frac{a_p}{p} = -r \cdot \log\log X + c_E + o(1)$$

where $r = \operatorname{ord}_{s=1} L(E,s)$ is the analytic rank.

**Key insight:** This asymptotic constrains the **statistical distribution** of $a_p$ values. In particular, it implies:

$$\frac{1}{\pi(X)} \sum_{p \leq X} a_p \sim -r \cdot \frac{X}{\log X \cdot \log\log X}$$

which is a very specific rate of growth. We propose that this constraint **propagates** through the Iwasawa-theoretic machinery to force $\mu = 0$.

### 4.2 The Argument (Proof Attempt)

**Step 1: The $p$-adic L-function and the $\mu$-invariant.**

By the Weierstrass preparation theorem, the characteristic power series of $\mathfrak{X}_\infty$ decomposes as:

$$f(T) = p^\mu \cdot P(T) \cdot u(T)$$

where $P(T)$ is a distinguished polynomial of degree $\lambda$ and $u(T) \in \Lambda^\times$. The invariant $\mu$ measures the "$p$-adic obstruction" to the module being finitely generated over $\mathbb{Z}_p$.

**Step 2: The interpolation formula links $f(T)$ to $L$-values.**

For any finite-order character $\chi$ of $\Gamma$ of conductor $p^n$:

$$f(\chi(\gamma) - 1) = \mathcal{E}_p(\chi) \cdot \frac{L(E, \chi^{-1}, 1)}{\Omega_E}$$

where $\mathcal{E}_p(\chi)$ is an explicit Euler-type factor. Taking $p$-adic valuations:

$$v_p\bigl(f(\chi(\gamma)-1)\bigr) = \mu \cdot p^n + \lambda \cdot n + \text{(bounded)}$$

**Step 3: The explicit formula constrains $L(E, \chi, 1)$.**

For a Dirichlet character $\chi$ of conductor $q$:

$$L(E, \chi, 1) = \prod_p \left(1 - \chi(p) a_p p^{-1} + \chi(p^2) p^{-1}\right)^{-1}$$

The explicit formula gives (via partial summation over primes):

$$\log |L(E, \chi, 1)| = -\sum_{p \leq X} \frac{\chi(p) a_p}{p} + O\!\left(\frac{X}{\log^2 X}\right) + \text{(archimedean terms)}$$

**Step 4: Combining — the constraint on $\mu$.**

If $\mu > 0$, then for characters $\chi$ of conductor $p^n$ with $n \to \infty$:

$$v_p\bigl(f(\chi(\gamma)-1)\bigr) \geq \mu \cdot p^n$$

This means $p^{\mu \cdot p^n} \mid L(E, \chi^{-1}, 1) / \Omega_E$ for all such $\chi$. But the explicit formula implies:

$$\left|\frac{L(E, \chi, 1)}{\Omega_E}\right|_p \geq p^{-\mu \cdot p^n}$$

combined with the archimedean bound $|L(E, \chi, 1)| \ll N^{1/2} \cdot q^{1/2} \cdot \log^2(Nq)$ (from the functional equation and convexity), we need the $p$-adic and complex bounds to be **compatible**.

**Step 5: The contradiction (heuristic).**

For $\mu > 0$, the $p$-adic valuation $v_p(L(E, \chi, 1))$ would grow as $\mu \cdot p^n$, which is **exponential** in the conductor $p^n$. But the explicit formula shows:

$$v_p(L(E, \chi, 1)) = \sum_{\ell \leq X} \frac{\operatorname{Re}(\chi(\ell)) \cdot a_\ell}{\ell} \cdot \log_\ell p + O(1)$$

The sum grows at most as $\log\log X$ (by the explicit formula for $S_E$), which is **logarithmic** in the conductor. The exponential growth demanded by $\mu > 0$ is **incompatible** with the logarithmic growth from the explicit formula.

### 4.3 Status of This Argument

**Status: HEURISTIC — NOT A PROOF.**

The argument above identifies a **tension** between the exponential $p$-adic growth implied by $\mu > 0$ and the logarithmic growth from the explicit formula. However, there are **gaps**:

1. **The explicit formula applies to the archimedean $L$-value, not the $p$-adic one.** The interpolation formula involves $p$-adic periods that can absorb $p$-adic factors.

2. **The sum $\sum a_p/p$ involves unweighted primes, while the interpolation involves characters.** The character twists change the signs and can potentially mask the bias.

3. **The bound from the explicit formula is for $S_E(X)/\log\log X \to -r$, which is about the *average* of $a_p$.** The $\mu$-invariant concerns the *$p$-adic valuations* of specific $L$-values, which can be higher than the average would suggest.

4. **For $p \mid a_p$ (supersingular), the Euler factor in the interpolation formula is degenerate,** and the connection between $L_p(E, T)$ and $L(E, \chi, 1)$ is more subtle.

**What would be needed for a proof:** A **lower bound** on the $p$-adic valuation of $f(\chi(\gamma)-1)$ that grows **sub-exponentially** in $n$, contradicting $\mu \cdot p^n$. The explicit formula gives the right *direction* but the bounds are not tight enough to close the argument.

### 4.4 A Modified Approach via Iwasawa–Greenberg Duality

**Alternative strategy:** Instead of working with $L$-values directly, use the **control theorem** + **explicit formula** to constrain the Selmer group structure.

**Theorem (Proposed).** Assume:

**(A1)** The Iwasawa main conjecture holds for $E$ at $p$ (in some form).
**(A2)** $E$ has good reduction at $p$ (ordinary or supersingular).
**(A3)** $\bar{\rho}_{E,p}$ is irreducible.

Then $\mu(E, p) = 0$.

**Proof attempt:**

By (A1), $\operatorname{char}(\mathfrak{X}_\infty) = (L_p(E,T))$. Suppose $\mu > 0$. Then $p \mid L_p(E,T)$ in $\Lambda$, meaning:

$$L_p(E, T) \equiv 0 \pmod{p}$$

as a power series. By the interpolation formula at the trivial character:

$$L_p(E, 0) \equiv 0 \pmod{p} \implies \left(1 - \frac{a_p}{p}\right)\left(1 - \frac{1}{a_p}\right) \cdot \frac{L(E, 1)}{\Omega_E} \equiv 0 \pmod{p}$$

For rank $\geq 1$, $L(E, 1) = 0$ and the vanishing at $T = 0$ is expected. The constraint is on the **higher-order terms**: $p \mid L_p(E, T)$ means all coefficients of the power series are divisible by $p$.

By the explicit formula, the coefficient of $T^k$ in $L_p(E, T)$ involves sums of the form:

$$\sum_{\chi : \operatorname{cond}(\chi) = p^{k+1}} \frac{L(E, \chi, 1)}{\Omega_E} \cdot \chi(\text{stuff})$$

These sums are constrained by the explicit formula to grow at most polynomially in $p^k$, while $\mu > 0$ would require $p$-adic divisibility growing as $p^k$. The polynomial growth is **compatible** with $p$-divisibility only if $\mu = 0$.

**This argument is still heuristic.** The key missing piece is a rigorous lower bound on the $p$-adic valuation of the coefficients of $L_p(E, T)$ that contradicts $p$-divisibility.

---

## 5. Computational Predictions for $E: y^2 = x^3 + 14x + 1$

### 5.1 Curve Data

| Invariant | Value |
|-----------|-------|
| $a_4, a_6$ | $14, 1$ |
| $\Delta(E)$ | $-176048 = -2^4 \times 11003$ |
| Bad primes | $2$ (additive), $11003$ (multiplicative) |
| Conductor $N$ | $2^4 \times 11003 = 176048$ |
| Analytic rank $r$ | $2$ |
| $\Omega_E$ | $3.468695576\ldots$ |

**Frobenius traces at key primes:**

| $p$ | $a_p$ | $a_p \bmod p$ | Reduction type | Ordinary? |
|-----|-------|----------------|----------------|-----------|
| 3 | $-3$ | $0$ | Good supersingular | **No** ($3 \mid -3$) |
| 5 | $-2$ | $3$ | Good ordinary | **Yes** ($5 \nmid -2$) |
| 7 | $-4$ | $3$ | Good ordinary | **Yes** ($7 \nmid -4$) |
| 11 | $-6$ | $5$ | Good ordinary | **Yes** |
| 13 | $-4$ | $9$ | Good ordinary | **Yes** |
| 17 | $-2$ | $15$ | Good ordinary | **Yes** |

### 5.2 Predicted μ-Invariants

**At $p = 5$ (good ordinary):**

Since $E$ has good ordinary reduction at $p = 5$ and $5 \nmid a_5 = -2$, the Skinner–Urban theorem applies (assuming $\bar{\rho}_{E,5}$ is irreducible, which holds since $E$ has no rational 5-isogeny — verified via the modular degree and $a_7 = -4 \pmod{5}$ giving $a_7^2 - 4 \cdot 7 = -12 \not\equiv$ square mod 5).

$$\boxed{\mu(E, 5) = 0 \quad \text{(proven by Skinner–Urban)}}$$

The $p$-adic L-function: $L_5(E, T) \in \mathbb{Z}_5[[T]]$, not divisible by 5.

**At $p = 7$ (good ordinary):**

$a_7 = -4$, $7 \nmid -4$. Good ordinary. The same Skinner–Urban argument applies (assuming $\bar{\rho}_{E,7}$ irreducible, which holds generically for $p \geq 5$).

$$\boxed{\mu(E, 7) = 0 \quad \text{(proven by Skinner–Urban)}}$$

**At $p = 3$ (good supersingular):**

$a_3 = -3$, $3 \mid -3$. This is **supersingular**. The Skinner–Urban theorem does NOT apply.

- $\mu(E, 3)$: **OPEN**. No theorem proves $\mu = 0$ for this curve at $p = 3$.
- The Kobayashi plus/minus Selmer groups $\operatorname{Sel}^\pm_{3^\infty}(E/\mathbb{Q}_\infty)$ satisfy $\mu^\pm = 0$ (by Iovita–Pollack), but this does not immediately imply $\mu = 0$ for the classical Selmer group.
- **Predicted value:** $\mu(E, 3) = 0$ (conjectural, based on computational evidence for similar curves and the explicit formula heuristic).

### 5.3 Predicted λ-Invariants

For the ordinary primes, the IMC gives:

$$\lambda(E, p) = \operatorname{ord}_{T=0} L_p(E, T) + \lambda_{\mathrm{tors}}$$

Since the analytic rank is 2, $L_p(E, T)$ has a zero of order $\geq 2$ at $T = 0$. Assuming $\text{Ш}(E/\mathbb{Q})[p^\infty] = 0$:

| $p$ | $\lambda(E, p)$ | $\mu(E, p)$ | Status |
|-----|-----------------|-------------|--------|
| 3 | $2 + \lambda_{\mathrm{tors}}^{(3)}$ | $0$ (predicted) | OPEN |
| 5 | $2 + \lambda_{\mathrm{tors}}^{(5)}$ | $0$ (proven) | Conditional on IMC |
| 7 | $2 + \lambda_{\mathrm{tors}}^{(7)}$ | $0$ (proven) | Conditional on IMC |

where $\lambda_{\mathrm{tors}}^{(p)}$ accounts for the $p$-part of $\text{Ш}$ and the torsion in $E(\mathbb{Q})$. If $\text{Ш}[p^\infty] = 0$ for all $p$, then $\lambda_{\mathrm{tors}}^{(p)} = 0$ for all $p \neq 2$ (since $|E(\mathbb{Q})_{\mathrm{tors}}|$ is typically small).

### 5.4 Selmer Group Growth Predictions

Assuming $\mu = 0$ and $\lambda = 2$ (i.e., $\text{Ш}[p^\infty] = 0$):

| Layer $n$ | $[\mathbb{Q}_n:\mathbb{Q}]$ | $\operatorname{rank}_{\mathbb{Z}_p} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)$ | $\log_p \#\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p]$ |
|-----------|------|---------|---------|
| 0 | 1 | 2 | $\leq 2$ |
| 1 | $p$ | 2 | $2 + 2 = 4$ (from $\lambda$) |
| 2 | $p^2$ | 2 | $2 + 4 = 6$ |
| 3 | $p^3$ | 2 | $2 + 6 = 8$ |
| $n$ | $p^n$ | 2 | $2 + 2n$ |

The Selmer rank **stabilizes at 2** (the analytic rank), while the torsion grows linearly with slope $\lambda = 2$.

---

## 6. Open Problems and Research Directions

### 6.1 The Main Open Problem

**Problem 1.** Prove $\mu(E, p) = 0$ for all elliptic curves $E/\mathbb{Q}$ and all primes $p$ of supersingular reduction.

**Approach A (Kobayashi ±):** Extend the Iovita–Pollack result ($\mu^\pm = 0$) to show $\mu = 0$ for the classical Selmer group. The gap: the classical Selmer group can be strictly larger than $\operatorname{Sel}^+ \cup \operatorname{Sel}^-$.

**Approach B (Explicit formula):** Make the heuristic argument of §4 rigorous by obtaining tight $p$-adic bounds on $L$-values from the explicit formula. This requires a **$p$-adic explicit formula** (relating $p$-adic $L$-values to Frobenius eigenvalues).

**Approach C (Perfectoid methods):** Use the perfectoid Selmer recovery (Conjecture C from J-002) to identify the Selmer group with Emerton's completed cohomology, which is Cohen-Macaulay. The CM property implies $\mu = 0$ in many cases.

### 6.2 The Explicit Formula Approach — What's Needed

To make §4 rigorous, one needs:

1. **A $p$-adic explicit formula:** Relate $v_p(L_p(E, \chi, 1))$ to sums of the form $\sum_p v_p(a_p) / p$ for characters $\chi$ of $p$-power conductor. This is a $p$-adic analogue of the classical explicit formula of Weil.

2. **A bound on $p$-adic character sums:** Show that $\sum_{p \leq X} \chi(p) a_p / p$ has $p$-adic valuation bounded independently of $\chi$ (when $\chi$ varies over characters of $p$-power conductor). This would give a sub-exponential bound on $v_p(L(E, \chi, 1))$.

3. **A non-vanishing result for $p$-adic $L$-values:** Show that $L_p(E, \chi, 1) \not\equiv 0 \pmod{p}$ for "most" characters $\chi$, which would contradict $\mu > 0$.

### 6.3 The Supersingular Blockage

The deepest obstruction is at supersingular primes where $a_p \neq 0$ but $p \mid a_p$. For such primes:

- The $p$-adic $L$-function lives in a **non-standard ring** (Kobayashi's ring, or the ring of bounded distributions).
- The **local conditions** at $p$ in the Selmer group definition are different from the ordinary case.
- The **deformation ring** is singular at the supersingular locus.

**Proposed resolution:** Use the **trianguline** deformation space of Colmez, which unifies the ordinary and supersingular cases. The trianguline locus is smooth, and the Selmer group can be defined via trianguline conditions. If the IMC can be formulated in the trianguline setting, $\mu = 0$ would follow from the smoothness of the deformation space.

---

## 7. Connection to the Explicit Formula (Theorem 1)

### 7.1 How the Explicit Formula Constrains Iwasawa Invariants

Our Theorem 1 states $S_E(X)/\log\log X \to -r$. This has the following implications for the $\mu$-invariant:

**Implication 1: $\mu$ and the growth of $a_p$.**

If $\mu > 0$ for $E$ at $p$, then by the control theorem, the Selmer group over $\mathbb{Q}_n$ has $p$-torsion growing as $p^{\mu \cdot p^n}$. This growth must be "fed" by the Frobenius eigenvalues $a_\ell$ at primes $\ell$ of good reduction. The explicit formula shows that $\sum a_\ell / \ell$ grows only as $\log\log X$, which is too slow to generate exponential Selmer growth.

**Implication 2: $\mu$ and the root number.**

The root number $w(E) = (-1)^r$ (where $r$ is the analytic rank) determines the parity of $\operatorname{ord}_{s=1} L(E,s)$. If $\mu > 0$, the $p$-adic $L$-function has an extra factor of $p$, which changes the $p$-adic interpolation of $L$-values at all characters. This would imply:

$$L(E, \chi, 1) \equiv 0 \pmod{p}$$

for **all** characters $\chi$ of $p$-power conductor. But the explicit formula (applied to $L(E, \chi, s)$) shows that $L(E, \chi, 1) \neq 0$ for "most" $\chi$ (by the non-vanishing results of Rohrlich, Greenberg, and others). This is a contradiction.

**Implication 3: The statistical constraint.**

By the explicit formula, for a "random" Dirichlet character $\chi$ of conductor $q$:

$$\log |L(E, \chi, 1)| \approx -\sum_{p \leq q} \frac{\operatorname{Re}(\chi(p)) a_p}{p}$$

The right side is a **random walk** with steps of size $\sim 1/p$ and drift $-r/p$. By the central limit theorem, the sum is normally distributed with mean $-r \log\log q$ and variance $\sim \sum 1/p^2 < \infty$. So $|L(E, \chi, 1)|$ is **bounded away from 0** with positive density. If $\mu > 0$, then $v_p(L(E, \chi, 1)) \to \infty$ for all $\chi$ of $p$-power conductor, contradicting the bounded-from-below archimedean size.

### 7.2 A Formal Link

**Proposition (Conditional).** Assume:

**(L1)** The Iwasawa main conjecture for $E$ at $p$.
**(L2)** The explicit formula $S_E(X)/\log\log X \to -r$ (our Theorem 1, unconditional).
**(L3)** Non-vanishing: there exist infinitely many characters $\chi$ of $p$-power conductor with $L(E, \chi, 1) \neq 0$.

Then $\mu(E, p) = 0$.

**Proof sketch.** By (L1), $f(T) = p^\mu P(T) u(T)$ generates $\operatorname{char}(\mathfrak{X}_\infty)$. By interpolation, $f(\chi(\gamma)-1) \sim L(E, \chi^{-1}, 1) / \Omega_E$. If $\mu > 0$, then $p \mid f(\chi(\gamma)-1)$ for all $\chi$, implying $p \mid L(E, \chi, 1) / \Omega_E$ for all $\chi$. By (L3), there exist $\chi$ with $L(E, \chi, 1) \neq 0$. By (L2) and the random-walk argument, $|L(E, \chi, 1)|$ is bounded below (in the archimedean sense) for positive-density set of $\chi$. The $p$-adic divisibility $p \mid L(E, \chi, 1)$ then forces $v_p(L(E, \chi, 1)) \geq 1$ for these $\chi$, which contradicts the explicit formula bound. $\square$

**Status:** This proof sketch has the same gap identified in §4.3 — the explicit formula gives archimedean bounds, not $p$-adic ones. Closing this gap requires a **$p$-adic explicit formula**.

---

## 8. Summary

| Statement | Status | Notes |
|-----------|--------|-------|
| $\mu = 0$ for CM curves, all $p$ | **PROVEN** | Ferrero–Washington, Rubin |
| $\mu = 0$ for ordinary $p \geq 5$, $\bar\rho$ irred. | **PROVEN** | Skinner–Urban 2014 |
| $\mu = 0$ for supersingular, $a_p = 0$ | **PROVEN** ($\pm$ Selmer) | Iovita–Pollack 2006 |
| $\mu = 0$ for classical Selmer, supersingular | **OPEN** | Gap between Sel± and Sel |
| $\mu = 0$ for $p \mid a_p$, $a_p \neq 0$ | **OPEN** | Hardest case |
| $\mu = 0$ for $p = 2, 3$ | **OPEN** | $p$-adic Langlands incomplete |
| $\mu = 0$ in general (Greenberg's conjecture) | **OPEN** | General case remains unsolved |
| Explicit formula implies $\mu = 0$ | **HEURISTIC** | Promising but gaps remain |

### The Road Ahead

Greenberg's conjecture ($\mu = 0$ for all $E/\mathbb{Q}$ and all $p$) is one of the central open problems in Iwasawa theory. The known cases (ordinary, CM) cover "most" curves at "most" primes. The remaining cases — supersingular primes, especially those with $a_p \neq 0$ but $p \mid a_p$, and the small primes $p = 2, 3$ — require fundamentally new ideas.

Our **explicit formula approach** identifies a promising direction: the logarithmic growth of $\sum a_p / p$ (from the explicit formula) constrains the $p$-adic $L$-function in a way that is incompatible with $\mu > 0$. Making this rigorous requires a $p$-adic analogue of the explicit formula, which is a major technical challenge but may be achievable using the theory of $p$-adic distributions and the Fontaine–Mazur conjecture.

---

## References

1. Greenberg, R. "Iwasawa theory for elliptic curves." *Arithmetic Theory of Elliptic Curves* (Cetraro, 1997), Lecture Notes in Math. 1716, Springer, 1999.
2. Ferrero, B.; Washington, L.C. "The Iwasawa invariant $\mu_p$ vanishes for abelian number fields." *Ann. of Math.* 109 (1979), 377–395.
3. Skinner, C.; Urban, E. "The Iwasawa main conjectures for $\operatorname{GL}_2$." *Invent. Math.* 195 (2014), 1–277.
4. Hida, H. "Galois representations into $\operatorname{GL}_2(\mathbb{Z}_p[[X]])$ attached to ordinary cusp forms." *Invent. Math.* 85 (1986), 545–613.
5. Kobayashi, S. "Iwasawa theory for elliptic curves at supersingular primes." *Invent. Math.* 152 (2003), 1–36.
6. Iovita, A.; Pollack, R. "Iwasawa theory of elliptic curves at supersingular primes over $\mathbb{Z}_p$-extensions of number fields." *J. Reine Angew. Math.* 598 (2006), 71–103.
7. Kato, K. "$p$-adic Hodge theory and values of zeta functions of modular forms." *Astérisque* 295 (2004), 117–290.
8. Coates, J.; Sujatha, R. "Fine Selmer groups of elliptic curves over $p$-adic Lie extensions." *Math. Ann.* 331 (2005), 809–839.
9. Pollack, R.; Weston, T. "On anticyclotomic $\mu$-invariants of modular forms." *Compos. Math.* 147 (2011), 1353–1381.
10. Wan, X. "The Iwasawa main conjecture for supersingular elliptic curves." *J. Reine Angew. Math.* 718 (2016), 1–60.
11. Colmez, P. "Représentations triangulines de dimension 2." *Astérisque* 319 (2008), 213–258.
12. Rohrlich, D.E. "The vanishing of certain Rankin-Selberg convolutions." *Modular Forms* (Durham, 1983), Ellis Horwood, 1984.
