# Track B: Fixed-Prime Sha-Finiteness Certificate

**Curve:** 389.a1 — $y^2 + y = x^3 + x^2 - 2x$
**Prime:** $p = 5$
**Date:** 2026-09-15T01:31:40
**Software:** PARI/GP 2.17.2 via cypari2
**Certificate status:** CERTIFIED

---

## Certificate Statement

$$\text{Sha}(E/\mathbb{Q})[5^\infty] \text{ is finite.}$$

This is a **fixed-prime, fixed-curve** certificate. It does **not** prove:
- $\text{Sha}[5] = 0$ (only that $\text{Sha}[5^\infty]$ is finite)
- Total Sha finiteness (only the 5-primary part)
- BSD leading-term formula
- The result for other primes or curves

---

## Validation Gates

Every status below is **derived** from a successful computation, not hardcoded.
Missing/failed inputs prevent a certified conclusion.

| Check | Value | Status |
|-------|-------|--------|
| Rank certified = 2 | 2 (r1=r2) | CERTIFIED |
| Derivative nonzero | val=2 < prec=7 | CERTIFIED |
| Ordinary at 5 | a_5 = -3 | CERTIFIED |
| Galois image | GL_2(F_5): irred=True, transv=True | CERTIFIED |
| **All pass** | | **CERTIFIED** |

---

## Divisibility Chain

The certificate rests on the chain (with $X$ = cyclotomic Selmer dual):

$$2 \leq \text{corank}\, \text{Sel}_{5^\infty} \leq \text{rank}_{\mathbb{Z}_5}(X/TX) \leq \text{ord}_T \text{char}_\Lambda(X) \leq \text{ord}_T L_5(E,T) \leq 2$$

The links come from **five** distinct results:

### 1. Kato cotorsion [Kim, Thm 2.6]

$X$ is a finitely generated torsion $\Lambda$-module.

Hypotheses:
- E has ordinary reduction at p=5
- p-adic Galois image is large (contains SL_2(Z_5))

**Status:** HYPOTHESES_MET

### 2. Mazur control [Kim, Prop 2.7]

$\text{corank}\, \text{Sel}_{5^\infty} = \text{rank}_{\mathbb{Z}_5}(X/TX)$, because the restriction map to $\Gamma$-invariants has finite kernel and cokernel.

Hypotheses:
- Restriction map to Gamma-invariants has finite kernel and cokernel
- Follows from Kato cotorsion + ordinary/large-image hypotheses

**Status:** HYPOTHESES_MET

### 3. Torsion-module algebra [Kim, Thm 2.9]

$\text{rank}_{\mathbb{Z}_5}(X/TX) \leq \text{ord}_T \text{char}_\Lambda(X)$.

This is a general fact about finitely generated torsion $\Lambda$-modules.

**Status:** HYPOTHESES_MET

### 4. Kato divisibility [Kim, Thm 2.9]

$(L_5) \subseteq \text{char}_\Lambda(X)$, hence $\text{ord}_T \text{char}_\Lambda(X) \leq \text{ord}_T L_5(E,T)$.

Hypotheses:
- Kato's Euler system: (L_5) is contained in char_Lambda(X)
- Requires: ordinary reduction, large Galois image

**Status:** HYPOTHESES_MET

### 5. Numerical upper bound

PARI `ellpadicL(E, 5, prec, 0, 2)` computes the **second derivative** $L_5''(E,0)$:

```
5^2 + 3*5^3 + 5^4 + 2*5^5 + 5^6 + O(5^7)
```

The derivative has $5$-adic valuation 2 with absolute precision 7.
Since $\text{val} < \text{prec}$, the derivative is **nonzero**, giving $\text{ord}_T L_5(E,T) \leq 2$.

**Status:** CERTIFIED

### Lower bound: $\text{corank} \geq 2$

**Status:** CERTIFIED

$E(\mathbb{Q})$ has rank 2 (certified by PARI `ellrank`). Two independent points generate a $\mathbb{Z}^2$ subgroup, so $\text{corank}\, \text{Sel}_{5^\infty} \geq 2$.

### Combined

$$2 \leq \text{corank} \leq \text{rank}(X/TX) \leq \text{ord}_T \text{char} \leq \text{ord}_T L_5 \leq 2$$

Therefore $\text{corank} = 2$, and $\text{Sha}[5^\infty]$ is finite.

### Ordinary reduction at $p = 5$

$a_5 = -3$, which is $\not\equiv 0 \pmod{5}$. So $E$ is ordinary at 5. Verified.

### Galois image at $p = 5$

The argument uses the **characteristic polynomial discriminant**, not the trace or determinant alone.
A nonsquare trace or determinant does not prove surjectivity (e.g. $\text{diag}(1,2)$ over $\mathbb{F}_5$ has both nonsquare).

**Step 1 — Irreducibility.** Frobenius at 3 has characteristic polynomial $X^2 - a_3 X + 3$ with $a_3 = -2$.
Discriminant: $a_3^2 - 4 \cdot 3 = -2^2 - 12 = -8 \equiv 2 \pmod{5}$.
$F_5^\times$ squares are $\{1, 4\}$; $2 \notin \{1, 4\}$, so the discriminant is a **nonsquare**.
Therefore the residual representation $\bar{\rho}_5$ is **irreducible** over $\mathbb{F}_5$.

**Step 2 — Inertia transvection.** $E$ has multiplicative reduction at the conductor prime 389, with minimal discriminant $\Delta = 389$.
$v_{389}(\Delta) = 1$, so the inertia group at 389 acts via a **nontrivial transvection** modulo 5.

**Step 3 — $\text{SL}_2(\mathbb{F}_5)$.** Irreducibility (Step 1) + transvection (Step 2) implies the image contains $\text{SL}_2(\mathbb{F}_5)$.

**Step 4 — $\text{GL}_2(\mathbb{F}_5)$.** The cyclotomic character gives $\det = \chi_5$, so the image is $\text{GL}_2(\mathbb{F}_5)$.

**Step 5 — Lifting.** Standard $p \geq 5$ lifting lemma gives $\text{SL}_2(\mathbb{Z}_5) \subset \text{image}$.

$j = 1404928/389$.

---

## Conclusion

All links in the chain are verified:

$$2 \leq \text{corank} \leq \text{rank}(X/TX) \leq \text{ord}_T \text{char} \leq \text{ord}_T L_5 \leq 2$$

Therefore $\text{corank} = 2$, and

$$\text{Sha}(E/\mathbb{Q})[5^\infty] \text{ is finite.}$$

This is **established machinery applied to a benchmark** — not claimed novelty.

---

## Remaining Questions

1. **Is $\text{Sha}[5] = 0$?** For 389.a1, BSD predicts $|\text{Sha}| = 1$ (trivial Sha). The certificate proves 5-primary finiteness, not vanishing.
2. **What about other primes?** Each prime needs its own certificate. For 389.a1, $|\text{Sha}| = 1$ predicts trivial Sha at all primes.
3. **What about rank > 2?** The certificate route generalizes: for rank $r$, one needs a nonzero $r$-th derivative of $L_p$. For $r > 2$, this becomes harder.

---

## Sources

- [PARI: ellpadicL, elllocalred](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html)
- [Kim, A user's guide to Beilinson–Kato's zeta elements](https://arxiv.org/abs/2404.05186), Theorems 2.6, 2.9; Proposition 2.7
- [Kim, The structure of Selmer groups and the Iwasawa main conjecture](https://arxiv.org/abs/2203.12159), Theorems 1.8, 1.10
- [Kim, Refined Tamagawa number conjectures for GL_2](https://arxiv.org/abs/2505.09121), Conjecture 1.6; Corollary 1.11
