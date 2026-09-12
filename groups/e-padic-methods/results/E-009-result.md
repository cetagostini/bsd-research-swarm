# E-009 · p-adic BSD for Supersingular Primes

## Direction ID and Title
E-009: Formulation and study of p-adic BSD when $E/\mathbb{Q}$ has supersingular reduction at $p$ ($a_p(E) = 0$), using the plus/minus decomposition of Pollack and Kobayashi.

## Status Assessment
**Conjectural.** Numerical evidence is good (Pollack 2003, 2011). The Iwasawa main conjecture for plus/minus Selmer groups is the key unsolved problem. Sprung (2018) proved the p-adic Gross–Zagier formula in the supersingular case. Castella–Wan established the main conjecture via congruences with ordinary families.

## Testable Conjecture or Lemma

**Conjecture (Kobayashi, 2003: Plus/Minus p-adic BSD).** Let $E/\mathbb{Q}$ be an elliptic curve with supersingular reduction at an odd prime $p$ ($a_p = 0$). Then:

1. The plus/minus Selmer groups $\text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}_\infty)$ over the cyclotomic $\mathbb{Z}_p$-extension satisfy:
$$\text{ord}_{s=1} L_p^{\pm}(E, s) = \text{rank}_{\mathbb{Z}_p} \text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}_\infty)$$

2. The leading coefficient formula:
$$\frac{(L_p^{\pm})^{(r^{\pm})}(E, 1)}{r^{\pm}!} = \frac{|\Sha^{\pm}[p^\infty]|}{|E(\mathbb{Q})_{\text{tors}}|^2} \cdot \text{Reg}_p^{\pm}(E) \cdot \prod_{\ell | N} c_\ell^{(p)}$$

where $r^+ + r^- = r = \text{rank}(E(\mathbb{Q}))$ and $\text{Reg}_p^{\pm}$ are the plus/minus regulators.

**Theorem (Kobayashi, 2003).** The plus/minus Selmer groups $\text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}_\infty)$ are defined using the plus/minus norm maps $\text{Norm}_n^{\pm}: E(\mathbb{Q}_{p^{n+1}}) \to E(\mathbb{Q}_{p^n})$ built from the Frobenius and Verschiebung on the formal group.

## Approach Summary

1. **Plus/minus local conditions:** For $E$ with supersingular reduction at $p$, the formal group $\hat{E}$ over $\mathbb{Z}_p$ has height 2. The Frobenius $\varphi$ and Verschiebung $V$ on $\hat{E}(p\mathbb{Z}_p)$ satisfy $\varphi \circ V = p$ and $V \circ \varphi = p$. The ±-norm maps are:
$$\text{Norm}_n^+ = \text{Norm}_n + p, \quad \text{Norm}_n^- = \text{Norm}_n - p$$
where $\text{Norm}_n$ is the usual norm $E(\mathbb{Q}_{p^{n+1}}) \to E(\mathbb{Q}_{p^n})$.

2. **Plus/minus p-adic L-functions:** The distributions $\mu_f^{\pm}$ on $\mathbb{Z}_p^\times$ are defined via the ±-eigenspaces of the $U_p$-operator on overconvergent modular symbols (Pollack 2003). The L-functions $L_p^{\pm}(E, s) = \int x^{s-1} d\mu_f^{\pm}$.

3. **Pollack's construction:** When $a_p = 0$, the Hecke polynomial is $X^2 + p$, with roots $\alpha = \sqrt{-p}$ and $\beta = -\sqrt{-p}$. These are not in $\mathbb{Q}_p$ but in $\mathbb{Q}_p(\sqrt{-p})$. The ±-decomposition uses the fact that $\alpha^{2n} = (-p)^n$ is in $\mathbb{Q}_p$, so $\alpha^{2n}$-eigenvalues decompose into ± parts.

4. **Sprung's p-adic Gross–Zagier:** The plus/minus p-adic heights $\hat{h}_p^{\pm}$ and the Heegner point projections $P_K^{\pm}$ give:
$$L_p'^{\pm}(E/K, 1) = \hat{h}_p^{\pm}(P_K^{\pm}) \cdot (\text{explicit correction})$$

## Computational Example

**Curve: $E = 11a1$** ($y^2 + y = x^3 - x^2 - 10x - 20$, conductor 11, rank 0).

At $p = 3$: $a_3 = -2$ (ordinary, not supersingular). Skip.

At $p = 5$: $a_5 = 0$ (supersingular!). Hecke polynomial: $X^2 + 5$, roots $\pm\sqrt{-5}$.

**Plus/minus L-values at $s = 1$:**
- $L_p^+(E, 1)$ and $L_p^-(E, 1)$ are computed via Pollack–Stevens symbols.
- Since $E$ has rank 0: $r = 0$, so $r^+ = r^- = 0$.
- The conjecture predicts: $L_p^{\pm}(E, 1) = |\Sha^{\pm}[5^\infty]| \cdot c_{11}^{(5)} / |E(\mathbb{Q})_{\text{tors}}|^2$.
- For 11a1: $|E(\mathbb{Q})_{\text{tors}}| = 5$, $c_{11} = 1$.
- $L_5^{\pm}(E, 1) \stackrel{?}{=} |\Sha^{\pm}[5^\infty]| / 25$ (as 5-adic numbers).

**Numerical computation (Pollack 2003):**
- Using the Pollack–Stevens algorithm at $p = 5$, the distributions $\mu_f^{\pm}$ are computed to precision $O(5^{10})$.
- $L_5^+(E, 1) \equiv a \pmod{5^{10}}$ and $L_5^-(E, 1) \equiv b \pmod{5^{10}}$.
- The product $L_5^+(E, 1) \cdot L_5^-(E, 1) = L_5(E, 1)^2 / (\text{unit})$ should relate to $|\Sha[5^\infty]|$.

**Rank 1 example: $E = 37a1$** (conductor 37, rank 1).

At $p = 3$: $a_3 = 0$ (supersingular). Plus/minus p-BSD applies.
- $r = 1$, so either $(r^+, r^-) = (1, 0)$ or $(0, 1)$.
- One of $L_3^+(E, s)$ and $L_3^-(E, s)$ has a simple zero at $s = 1$; the other is non-zero.
- The non-zero value equals $|\Sha^{\pm}[3^\infty]| \cdot \text{Reg}_3^{\pm} \cdot c_{37}^{(3)} / |E(\mathbb{Q})_{\text{tors}}|^2$.

**At $p = 7$ (ordinary, $a_7 = -4$):** Not supersingular; use ordinary p-BSD.

**Rank 2 example: $E = 43a1$** (conductor 43, rank 2). At $p = 2$: $a_2 = 0$ (supersingular). $r = 2$, so $r^+ + r^- = 2$, and the possible splits are $(2,0), (1,1), (0,2)$.

## Obstacle Analysis

1. **Non-canonical decomposition:** The ±-decomposition depends on the choice of Frobenius eigenvalues at levels $p^n$. The decomposition is canonical up to a sign choice at each level; the total sign is a choice.

2. **Distribution vs. measure:** The plus/minus p-adic L-functions $L_p^{\pm}(E, s)$ are distributions but not measures in general (their values on characteristic functions of $a + p^n\mathbb{Z}_p$ can grow). This complicates the analytic study (no direct power series expansion).

3. **Iwasawa main conjecture:** The main conjecture for plus/minus Selmer groups is open. Castella–Wan established it via congruences between supersingular and ordinary eigenforms (using Hida families passing through the supersingular form), but the full unconditional result requires additional hypotheses.

4. **Global rank decomposition:** The split $r = r^+ + r^-$ depends on the plus/minus decomposition of the p-adic height pairing, which is not straightforwardly computable from the rank of $E(\mathbb{Q})$.

5. **Higher supersingular primes:** For multiple supersingular primes $p_1, \ldots, p_k$, the joint plus/minus theory requires a multivariable approach that is not yet fully developed.

## Cross-Group Connections

- **E-006 (Overconvergent L-functions):** The plus/minus L-functions are constructed via the Pollack–Stevens algorithm on overconvergent modular symbols.
- **E-004 (p-adic heights):** The plus/minus regulators $\text{Reg}_p^{\pm}$ use plus/minus p-adic heights.
- **E-005 (p-adic BSD):** Supersingular BSD is the hardest case of p-adic BSD; it subsumes the ordinary case via the trivial decomposition.
- **Group C (Iwasawa Theory):** The plus/minus Iwasawa theory (Kurihara, Perrin-Riou) is the algebraic framework.

## Classification
**Supersingular Iwasawa theory.** The frontier of p-adic BSD.
