# E-010 · Greenberg's L-invariant and Its Variations

## Direction ID and Title
E-010: Study of Greenberg's generalised $\mathcal{L}$-invariant for elliptic curves, its relation to the MTT, Darmon, and Colmez $\mathcal{L}$-invariants, and its role in p-adic BSD and p-adic variation.

## Status Assessment
**Established for split multiplicative reduction (all definitions coincide); active for good ordinary primes.** Greenberg (1989, 1994) defined the Iwasawa-theoretic $\mathcal{L}$. Colmez (1990) defined the representation-theoretic $\mathcal{L}$. Berger–Li–Zhu (2008) identified various $\mathcal{L}$-invariants via p-adic Hodge theory. Breuil and Emerton developed p-adic Langlands perspectives.

## Testable Conjecture or Lemma

**Theorem (Uniqueness for split multiplicative, Colmez 1990).** For $E/\mathbb{Q}$ with split multiplicative reduction at $p$, the following definitions of $\mathcal{L}_p(E)$ coincide:

1. **MTT $\mathcal{L}$:** $\mathcal{L}_p^{\text{MTT}}(E) = 2\log_p(q_E)/\text{ord}_p(q_E)$ (from the p-adic L-function derivative).

2. **Greenberg $\mathcal{L}$:** $\mathcal{L}_p^{\text{Gr}}(E) = f'(0) / g'(0)$ where $f(T)$ is the characteristic power series of $\text{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^*$ and $g(T) = T \cdot (\text{trivial zero factor})$.

3. **Colmez $\mathcal{L}$:** $\mathcal{L}_p^{\text{Col}}(V_p(E)) = -\frac{d}{ds}\big|_{s=0} \log_p \det(1 - \varphi | D_{\text{cris}}(V_p(E) \otimes \mathbb{Q}_p(s)))$ involving the crystalline Frobenius on the filtered $\varphi$-module.

4. **Darmon $\mathcal{L}$:** $\mathcal{L}_p^{\text{Dar}}(E) = \log_p(\alpha) / \text{ord}_p(\alpha)$ where $\alpha$ is the p-adic multiplier in the p-adic uniformisation of the Shimura curve.

**Conjecture (Equality for good ordinary).** For $E$ with good ordinary reduction at $p$ and $a_p \equiv 1 \pmod{p}$, the MTT and Greenberg definitions of $\mathcal{L}_p(E)$ coincide. (This is proven for split multiplicative but open for good ordinary.)

**Greenberg's formula (Iwasawa-theoretic).** For $E$ with good ordinary reduction at $p$ and $a_p \equiv 1 \pmod{p^N}$:
$$\mathcal{L}_p^{\text{Gr}}(E) = \lim_{n \to \infty} \frac{1}{p^n} \log_p\left(\frac{a_{p^{n+1}}}{a_{p^n}}\right)$$
where $a_{p^n}$ are the Frobenius traces at level $p^n$ of the $\mathbb{Z}_p$-extension.

## Approach Summary

1. **Greenberg's definition:** The Selmer group $\text{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)$ over the cyclotomic $\mathbb{Z}_p$-extension $\mathbb{Q}_\infty$ has Pontryagin dual with characteristic power series $f(T) \in \mathbb{Z}_p[[T]]$. When $E$ has an exceptional zero at $p$, $f(0) = 0$ and $\mathcal{L}_p^{\text{Gr}}(E) = f'(0) / \mu_p$ where $\mu_p$ is the $\mu$-invariant contribution from the trivial zero.

2. **Colmez's definition:** Via $(\varphi, \Gamma)$-modules: $\mathcal{L}_p^{\text{Col}}(V) = \frac{d}{ds}\big|_{s=0} \log_p \mathcal{L}_p(V(s))$ where $\mathcal{L}_p$ is the p-adic L-function of the representation $V$ and $V(s)$ is the Tate twist.

3. **Berger–Li–Zhu:** Used p-adic Hodge theory (trianguline representations) to show that the Colmez $\mathcal{L}$-invariant equals the MTT $\mathcal{L}$-invariant for modular forms.

4. **p-adic variation (Hida families):** The $\mathcal{L}$-invariant varies analytically in the Hida family. The function $k \mapsto \mathcal{L}_p(E_k)$ (where $E_k$ is the weight-$k$ specialization) is a p-adic analytic function on the weight space.

## Computational Example

**Curve: $E = 11a1$** at $p = 11$ (split multiplicative).

**MTT $\mathcal{L}$:** $\mathcal{L}_{11}^{\text{MTT}}(E) = 2\log_{11}(-11)/1 = 2\log_{11}(11)$.

**Greenberg $\mathcal{L}$:** The characteristic power series of $\text{Sel}_{11^\infty}(E/\mathbb{Q}_\infty)^*$ has $f(0) = 0$ (trivial zero). The Iwasawa $\mu$-invariant is $\mu = 0$ (expected for semistable curves). So $\mathcal{L}_{11}^{\text{Gr}}(E) = f'(0) / (\text{normalisation})$.

**Numerical verification:** $f(T) = T \cdot g(T)$ where $g(0) = \mathcal{L}_{11}^{\text{MTT}}(E) \cdot (\text{unit})$. Computing $g(0)$ to precision $O(11^5)$ via Iwasawa theory (module computation over $\Lambda$) and comparing with $2\log_{11}(11)$.

**Colmez $\mathcal{L}$:** The crystalline Frobenius on $D_{\text{cris}}(V_{11}(E))$ has eigenvalues $\alpha, \beta$ with $\alpha\beta = 11$, $\alpha + \beta = a_{11} = 1$. So $\alpha, \beta$ are roots of $X^2 - X + 11 = 0$: $\alpha = (1 + \sqrt{-43})/2$. In $\mathbb{Q}_{11}$, $\alpha$ and $\beta$ are the two roots, one a 11-adic unit, one not.

$\mathcal{L}_{11}^{\text{Col}}(V_{11}(E)) = \log_{11}(\alpha)/\text{ord}_{11}(\alpha) + \log_{11}(\beta)/\text{ord}_{11}(\beta)$ (simplified formula for the determinant).

**Curve: $E = 14a1$** at $p = 2$ (split multiplicative, $a_2 = 1$).
- $\mathcal{L}_2^{\text{MTT}}(E) = 2\log_2(q_E)/\text{ord}_2(q_E)$.
- Tate period: $q_E = -2 \cdot u$ for some 2-adic unit $u$.

**Good ordinary example: $E = 37a1$** at $p = 7$ ($a_7 = -4$, ordinary, no exceptional zero).
- $\mathcal{L}_7(E)$ is not defined via MTT (no exceptional zero). The Greenberg $\mathcal{L}$ is defined when $a_7 \equiv 1 \pmod{7^N}$ for large $N$ (not the case here: $a_7 = -4 \not\equiv 1 \pmod{7}$).
- For this curve, no exceptional zero at $p = 7$.

**Good ordinary with near-exceptional zero: $E = 91b1$** at $p = 7$.
- If $a_7 \equiv 1 \pmod{7}$ (need to check: this depends on the specific curve), then $\mathcal{L}_7^{\text{Gr}}(E)$ is defined via the Iwasawa-theoretic formula involving $\log_p(a_{p^n})$.

## Obstacle Analysis

1. **Good ordinary equivalence:** All definitions of $\mathcal{L}_p(E)$ are proven equal for split multiplicative reduction. For good ordinary reduction (when $a_p \equiv 1 \pmod{p}$), the equivalence is conjectural. The p-adic Langlands programme (Breuil, Emerton) promises a unified framework but requires completed cohomology.

2. **Computability:** Greenberg's $\mathcal{L}_p^{\text{Gr}}(E)$ requires computing the characteristic power series of the Selmer group over $\mathbb{Z}_p[[T]]$, which is a module computation over the Iwasawa algebra. This is expensive for large conductors.

3. **Variation in families:** The function $k \mapsto \mathcal{L}_p(E_k)$ on the Hida family is expected to be p-adic analytic, but proving this requires control of the Selmer group variation, which is tied to the main conjecture.

4. **Non-ordinary $\mathcal{L}$-invariant:** For supersingular primes ($a_p = 0$), the $\mathcal{L}$-invariant theory is less developed. The plus/minus framework (E-009) provides a substitute but the analogue of $\mathcal{L}_p^{\text{Gr}}$ for plus/minus Selmer groups is not fully established.

## Cross-Group Connections

- **E-003 (MTT L-invariant):** The MTT $\mathcal{L}_p(E)$ is the original definition; E-010 studies its generalisations.
- **E-008 (Exceptional zeros):** The $\mathcal{L}$-invariant is the correction factor in the exceptional zero formula.
- **E-001 (Two-variable L-functions):** The variation of $\mathcal{L}_p(E)$ in the Hida family is a function on the weight space.
- **Group C (Iwasawa Theory):** Greenberg's $\mathcal{L}$-invariant is defined purely in terms of Iwasawa-theoretic objects.

## Classification
**L-invariants / p-adic variation.** The unifying framework for exceptional zero corrections.
