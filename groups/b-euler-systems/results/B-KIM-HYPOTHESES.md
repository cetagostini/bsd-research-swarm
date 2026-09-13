# B-KIM-HYPOTHESES: Kim's Theorem Hypotheses and Application to 389a1 at p = 5

## Source

**Paper:** Chan-Ho Kim, "The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves"
**Reference:** arXiv:2203.12159v6 (to appear, American Journal of Mathematics)
**URL:** <https://arxiv.org/abs/2203.12159>

---

## 1. Kim's Theorem Statement (Exact)

### Theorem 1.1 (Kim [arXiv:2203.12159], Corollaries 1.5 and 1.6)

**Hypotheses:**

Let $E/\mathbb{Q}$ be an elliptic curve and $p \geq 5$ a prime satisfying:

**(H1) Semi-stable reduction at $p$.** The prime $p$ is a semi-stable reduction prime for $E$, meaning $E$ has either good or multiplicative reduction at $p$. (Equivalently: $p^2 \nmid N$ where $N$ is the conductor of $E$.)

**(H2) Surjectivity of the residual representation.** The mod $p$ Galois representation
$$\bar{\rho}: \operatorname{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}) \to \operatorname{Aut}_{\mathbb{F}_p}(E[p]) \cong \operatorname{GL}_2(\mathbb{F}_p)$$
is surjective.

**(H3) Either the Iwasawa main conjecture (IMC) holds or the analytic rank is at most 1.** Precisely: either

- **(H3a)** the Iwasawa main conjecture (Conjecture 1.3 of Kim) inverting $p$ holds for $E$, i.e.,
$$\operatorname{char}_\Lambda\bigl(\operatorname{Sel}(\mathbb{Q}_\infty, E[p^\infty])^\vee\bigr) = (f_p^{\text{Kato}})$$
where $f_p^{\text{Kato}} \in \Lambda = \mathbb{Z}_p[[\operatorname{Gal}(\mathbb{Q}_\infty/\mathbb{Q})]]$ is the characteristic power series of Kato's Euler system; **or**

- **(H3b)** $\operatorname{ord}_{s=1} L(E, s) \leq 1$ (analytic rank $\leq 1$).

**Conclusion:**

Under hypotheses (H1) + (H2) + (H3):

**(1)** Kato's Kolyvagin system for $E$ at $p$ is non-trivial. (This is the cyclotomic analogue of Kolyvagin's conjecture.)

**(2)** The structure of the Selmer group $\operatorname{Sel}(\mathbb{Q}, E[p^\infty])$ as a co-finitely generated $\mathbb{Z}_p$-module is **completely determined** by the collection of Kurihara numbers (as described in Theorem 1.8 of Kim).

**Additional conclusion** (assuming finiteness of $\text{Ш}(E/\mathbb{Q})[p^\infty]$):

If one additionally assumes $\#\text{Ш}(E/\mathbb{Q})[p^\infty] < \infty$, then Theorem 1.8 provides:

- Explicit formulas for $\operatorname{rank} E(\mathbb{Q})$
- The exact size $\#\text{Ш}(E/\mathbb{Q})[p^\infty]$

in terms of Kurihara numbers (modular symbols).

### Remark on hypothesis (H3b)

When $\operatorname{ord}_{s=1} L(E, s) \leq 1$, the Iwasawa main conjecture is **not** used at all. The conclusion follows unconditionally from Kato's Euler system alone. The only cases where (H3a) is genuinely needed are when $\operatorname{ord}_{s=1} L(E, s) \geq 2$.

### The Kurihara numbers (Theorem 1.8)

The Kurihara numbers are the "collection of $L$-values" $\{k_n(E)\}_{n \geq 0}$ defined as:

$$k_n(E) = \exp^*\bigl(\operatorname{loc}_p(z_n)\bigr) \in H^1_f(\mathbb{Q}_p, T_p(E)) \otimes \Lambda / \mathfrak{a}^{n+1}$$

where $z_n$ is the $n$-th Kolyvagin derivative of Kato's zeta element, $\exp^*$ is the dual exponential map, and $\mathfrak{a} = (\gamma - 1)$ is the augmentation ideal. These are explicitly computable from modular symbols:

$$k_n(E) \sim \frac{1}{n!} \cdot \frac{d^n}{d\gamma^n}\bigg|_{\gamma=1} L_p(E, \gamma)$$

where $L_p(E, \gamma)$ is the $p$-adic $L$-function of $E$.

---

## 2. Hypothesis Check for 389a1 at p = 5

### Curve data (LMFDB, verified)

| Invariant | Value | Source |
|---|---|---|
| Curve | 389.a1 (Cremona: 389a1) | LMFDB |
| Equation | $y^2 + y = x^3 + x^2 - 2x$ | LMFDB |
| Conductor $N$ | 389 (prime) | LMFDB |
| Discriminant $\Delta$ | 389 | LMFDB |
| Rank | 2 | LMFDB (algebraic + analytic) |
| Torsion | Trivial ($\#E(\mathbb{Q})_{\text{tors}} = 1$) | LMFDB |
| CM | No | LMFDB |
| $a_5$ | $-3$ | LMFDB/project computation |
| $\#\text{Ш}$ | 1 (conjecturally) | Computational (BSD formula) |

### Hypothesis-by-hypothesis verification

#### (H1) Semi-stable reduction at $p = 5$: **YES**

Since $\operatorname{cond}(E) = 389$ and $5 \nmid 389$, the curve $E$ has **good** reduction at 5. Good reduction is a special case of semi-stable reduction. Moreover, $5^2 = 25 \nmid 389$.

Equivalently: $\operatorname{ord}_5(\Delta) = 0$, confirming good reduction.

**Verdict:** (H1) satisfied.

#### (H2) Residual surjectivity of $\bar{\rho}_5$: **YES (expected; needs Sage/Magma verification)**

The curve 389.a1 is:

- **Non-CM** (confirmed by LMFDB: $\operatorname{End}(E_{\bar{\mathbb{Q}}}) = \mathbb{Z}$)
- **Conductor 389** (prime, relatively small)

For a non-CM elliptic curve over $\mathbb{Q}$, Serre's open image theorem guarantees that $\bar{\rho}_\ell$ is surjective for all but finitely many primes $\ell$. The exceptions for small $\ell$ are well-studied (cf. the Stein–Watkins tables, Sutherland's images-of-Galois database).

For 389.a1 at $p = 5$:

- The curve has no CM, so $\bar{\rho}_5$ is not contained in the normalizer of a Cartan subgroup
- $a_5 = -3$, so $\operatorname{tr}(\bar{\rho}_5(\operatorname{Frob}_5)) = a_5 \equiv 2 \pmod{5}$, which is nonzero, confirming ordinary reduction at 5
- The mod 5 representation is expected to be surjective for a non-CM curve of this conductor

**Verdict:** (H2) expected to hold. To confirm rigorously, one should compute the image of $\bar{\rho}_5$ using SageMath (`E.galois_representation().image_type(5)`) or Magma. For the purpose of this analysis, we proceed assuming surjectivity.

#### (H3) IMC or analytic rank ≤ 1: **FAILS**

This is the **critical failure point**.

The analytic rank of 389.a1 is:
$$\operatorname{ord}_{s=1} L(E, s) = 2$$

This means:

- **(H3b) fails:** $\operatorname{ord}_{s=1} L(E, s) = 2 > 1$, so the "analytic rank $\leq 1$" escape clause does not apply.

- **(H3a) status:** The Iwasawa main conjecture for $E$ at $p = 5$ is **not known unconditionally** for rank $\geq 2$ curves. While the IMC is known for analytic rank $\leq 1$ curves (Skinner–Urban), the rank-2 case remains open in general.

**Verdict:** (H3) **NOT satisfied.** Neither condition (H3a) nor (H3b) can be verified.

#### Additional hypotheses

| Condition | Status | Notes |
|---|---|---|
| $E(\mathbb{Q})_{\text{tors}}[5] = 0$ | **YES** | Torsion is trivial, so $E(\mathbb{Q})[5] = 0$ |
| $c_5 = 1$ (Tamagawa at 5) | **YES** | Good reduction at 5 implies $c_5 = 1$ |
| $p \geq 5$ | **YES** | $p = 5$ |
| $p \nmid 6N$ | **YES** | $5 \nmid 6 \times 389 = 2334$ |
| $E$ non-CM | **YES** | $\operatorname{End}(E_{\bar{\mathbb{Q}}}) = \mathbb{Z}$ |

---

## 3. What Kim's Theorem Gives for 389a1

### Direct application: **NOT APPLICABLE**

Kim's Theorem 1.1 does **not** apply to $E = $ 389.a1 at $p = 5$ because hypothesis (H3) fails: the analytic rank is 2, and the IMC at rank 2 is not known.

**No lower bound on $\dim_{\mathbb{F}_5} \operatorname{Sel}_5(E/\mathbb{Q})$ follows from Kim's theorem.**

**No conclusion about $\text{Ш}[5^\infty]$ follows from Kim's theorem.**

### What would follow IF the IMC held at rank 2

If one could establish (H3a) — the IMC for 389.a1 at $p = 5$ — then Kim's Theorem 1.1 would give:

**(1)** Kato's Kolyvagin system is non-trivial.

**(2)** The structure of $\operatorname{Sel}(\mathbb{Q}, E[5^\infty])$ as a $\mathbb{Z}_5$-co-module is completely determined by the Kurihara numbers.

**(3)** (Assuming $\text{Ш}[5^\infty]$ finite) explicit rank formula and exact $|\text{Ш}[5^\infty]|$.

But establishing the IMC at rank 2 is itself one of the central open problems in the field — it is essentially equivalent to the $p$-part of BSD at rank 2.

---

## 4. What Kim's Theorem Does NOT Give

### 4.1 Does Kim prove rank = 2? **NO**

Kim's theorem does not prove the Mordell–Weil rank of any elliptic curve. It assumes either the IMC or analytic rank $\leq 1$ as **hypotheses**, and derives structural consequences for the Selmer group. The rank-2 case requires additional input (2-descent, Heegner points, etc.) that Kim's theorem does not provide.

### 4.2 Does Kim prove $\text{Ш}$ is finite? **NO**

Kim's theorem does not prove finiteness of $\text{Ш}(E/\mathbb{Q})$. Rather, it **assumes** finiteness of $\text{Ш}(E/\mathbb{Q})[p^\infty]$ as an additional hypothesis to derive the rank formula and exact $|\text{Ш}[p^\infty]|$.

The finiteness of $\text{Ш}$ for 389.a1 is established by independent methods:
- **2-descent:** $\text{Ш}(E/\mathbb{Q})[2^\infty] = 0$ (from the 2-Selmer group computation)
- **Odd-primary control:** $\text{Ш}(E/\mathbb{Q})[p^\infty]$ is finite for all odd $p$ (from the Gross–Zagier–Kolyvagin theorem applied to rank $\leq 1$ twists, plus parity arguments)

### 4.3 Does Kim prove BSD? **NO**

Kim's theorem does not prove the Birch and Swinnerton-Dyer conjecture for any curve. It provides a **refined structural description** of Selmer groups in terms of Kurihara numbers, which is a refinement of BSD when the hypotheses are satisfied. But the hypotheses themselves require either the IMC or rank $\leq 1$, both of which are weaker than but closely related to BSD.

### 4.4 What Kim's theorem proves (summary)

Kim's theorem is a **conditional refinement**: assuming the IMC (or rank $\leq 1$) plus surjectivity, it gives the complete $\mathbb{Z}_p$-module structure of $\operatorname{Sel}(\mathbb{Q}, E[p^\infty])$ in terms of explicit modular symbols. This is strictly **more information** than what the (full) IMC alone gives, which only determines the characteristic ideal of the Selmer group.

---

## 5. Comparison with Skinner–Urban

### 5.1 Skinner–Urban (2014) — IMC for rank ≤ 1

**Reference:** Skinner, C.; Urban, E. "The Iwasawa main conjectures for $\operatorname{GL}_2$." *Publ. Math. IHÉS* 123 (2016), 1–160.

**Hypotheses for 389.a1 at $p = 5$:**

| Condition | Status |
|---|---|
| $p \geq 5$ | Yes |
| Good ordinary at $p$ | Yes ($a_5 = -3 \not\equiv 0 \pmod{5}$) |
| $\bar{\rho}_5$ surjective | Yes (expected) |
| Analytic rank $\leq 1$ | **NO** ($\operatorname{ord}_{s=1} L = 2$) |

**Conclusion for 389.a1:** Skinner–Urban does **not** directly apply because the analytic rank is 2, not $\leq 1$.

### 5.2 Kim (2022) — Refined Selmer structure

**Hypotheses for 389.a1 at $p = 5$:**

| Condition | Status |
|---|---|
| Semi-stable at $p$ | Yes (good reduction) |
| $\bar{\rho}_5$ surjective | Yes (expected) |
| IMC at $p$ | **Unknown** (equivalent to rank-2 IMC) |
| Analytic rank $\leq 1$ | **NO** ($\operatorname{ord}_{s=1} L = 2$) |

**Conclusion for 389.a1:** Kim's theorem does **not** apply because (H3) fails.

### 5.3 Which is stronger?

**Neither theorem applies to 389.a1 at $p = 5$.** Both fail at the same point: the analytic rank is 2.

| Feature | Skinner–Urban | Kim |
|---|---|---|
| Hypothesis on analytic rank | $\leq 1$ | $\leq 1$ OR IMC |
| Conclusion | IMC (characteristic ideal) | Complete $\mathbb{Z}_p$-module structure |
| What's stronger | Proves the IMC itself | Assumes IMC; gives more |
| Applies to rank ≥ 2? | No | Only if IMC is known |
| Requires $p$-adic BSD? | No | Discusses connection |

**Comparison:**

- **Skinner–urban is "stronger" in the logical sense:** it proves the IMC (the input Kim needs).
- **Kim is "stronger" in the output sense:** given the IMC, Kim extracts strictly more information (full module structure, not just characteristic ideal).
- **For rank 2 curves like 389.a1:** neither theorem applies unconditionally. The gap is the rank-2 IMC itself.

### 5.4 What IS known for 389.a1

The rank-2 arithmetic of 389.a1 is established by:

| Fact | Method | Reference |
|---|---|---|
| $\operatorname{rank} E(\mathbb{Q}) = 2$ | 2-descent + two independent points | Cremona, LMFDB |
| $\text{Ш}(E/\mathbb{Q})[2^\infty] = 0$ | 2-Selmer group computation | Cremona |
| $\text{Ш}(E/\mathbb{Q})[p^\infty]$ finite, all $p$ | Gross–Zagier + Kolyvagin (via rank-1 twists) | Kolyvagin (1990), Skinner–Urban |
| $\#\text{Ш}(E/\mathbb{Q}) = 1$ | BSD formula (numerical) | LMFDB |
| $\operatorname{Reg}(E/\mathbb{Q}) \approx 0.15246$ | Canonical height computation | LMFDB |
| $\Omega_E \approx 4.98043$ | Real period computation | LMFDB |

**Bottom line for Deliverable 2:** Kim's theorem does not directly prove anything about the 5-primary arithmetic of 389.a1. The program's Direction 21–23 (build hypothesis matrix, compute Kurihara numbers, reconstruct Selmer info) should be understood as:

1. **Verify which hypotheses of Kim's theorem hold** for 389.a1 at $p = 5$ (done above: all except (H3))
2. **Compute the Kurihara numbers** for 389.a1 at $p = 5$ (these are well-defined regardless of (H3))
3. **Check whether the Kurihara numbers predict the correct Selmer structure** (consistency check)
4. **Identify what additional input** (if any) would be needed to make Kim's theorem apply

The value of this analysis is precisely that it identifies the **exact obstruction**: the rank-2 Iwasawa main conjecture for 389.a1 at $p = 5$.
