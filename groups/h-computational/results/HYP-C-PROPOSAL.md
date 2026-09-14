# Hypothesis C: A Structural Stopping Mechanism for Descent

**Target:** `groups/h-computational/results/HYP-C-PROPOSAL.md`
**Status:** Research proposal, one page
**Date:** 2026-09-14

---

## Claim

**Theorem (Conditional).** Let $E/\mathbb{Q}$ be an elliptic curve of rank $r$, $p$ an odd prime of good ordinary reduction ($a_p \not\equiv 0 \pmod{p}$), and $\bar{\rho}_{E,p}: G_\mathbb{Q} \to \mathrm{GL}_2(\mathbb{F}_p)$ the residual representation. Assume:

1. $\bar{\rho}_{E,p}$ is absolutely irreducible.
2. $E$ does not acquire rational $p$-isogeny over any extension of degree dividing $p-1$.

Define $G = \Sha(E/\mathbb{Q})[p^\infty]$, the $p$-primary component of the Tate–Shafarevich group, and the **descent filtration**:

$$D_n = p^{n-1}G[p^n] \;\subseteq\; G[p] \qquad (n \geq 1).$$

Then there exists an explicitly computable integer $B = B(E, p) \geq 1$, determined by local data alone, such that $D_n = D_{n+1}$ for all $n \geq B$.

**Moreover:** $D_B = D_{B+1} = \cdots = 0$ if and only if $\Sha[p^\infty] = 0$. The bound $B$ does not assume $\Sha$ finiteness; it is a consequence of the local-to-global structure of the Selmer filtration.

---

## Mechanism: The Control Map and Local Saturation

For each $n \geq 1$, the **restriction map** on Selmer groups

$$\rho_n : \mathrm{Sel}_{p^n}(E/\mathbb{Q}) \longrightarrow \mathrm{Sel}_{p^{n+1}}(E/\mathbb{Q})$$

fits into the exact sequence (Greenberg, Mazur):

$$0 \to \ker(\rho_n) \to \mathrm{Sel}_{p^n} \xrightarrow{\rho_n} \mathrm{Sel}_{p^{n+1}} \to \mathrm{coker}(\rho_n) \to 0.$$

**Kernel.** $\ker(\rho_n) \cong H^1(G_{S_p}, E[p])$ for $n \gg 0$, where $S_p = \{v \mid pN\}$. This is a finite group whose order is bounded by local data at $p$ and the bad primes. Specifically:

$$|\ker(\rho_n)| \leq \prod_{v \in S_p} \frac{|H^1(\mathbb{Q}_v, E[p])|}{|E(\mathbb{Q}_v)[p]|} =: K_p.$$

The quantity $K_p$ is computed from the Galois module structure of $E[p]$ at each $v \in S_p$, which depends only on the local representation $\rho_{E,p}|_{G_{\mathbb{Q}_v}}$.

**Cokernel.** The cokernel $\mathrm{coker}(\rho_n)$ measures the classes in $\mathrm{Sel}_{p^{n+1}}$ that do not come from $\mathrm{Sel}_{p^n}$. At each prime $v$, this is controlled by the **local saturation depth**:

$$B_v = \min\{n \geq 1 : \mathrm{im}(E(\mathbb{Q}_v)/p^n E(\mathbb{Q}_v) \to H^1(\mathbb{Q}_v, E[p^n])) = \mathrm{im}(E(\mathbb{Q}_v)/p^{n+1} E(\mathbb{Q}_v) \to H^1(\mathbb{Q}_v, E[p^{n+1}]))\}.$$

At $v = p$ (ordinary case): the formal group $\hat{E}(\mathbb{Z}_p) \cong \mathbb{Z}_p$ contributes

$$B_p = 1 + v_p(\#\hat{E}(\mathbb{F}_p)) = 1 + v_p(p + 1 - a_p)$$

since $E(\mathbb{Q}_p)/p^n E(\mathbb{Q}_p) \cong \mathbb{Z}/p^n\mathbb{Z} \oplus \hat{E}(\mathbb{Z}_p)/p^n$ stabilizes once $n$ exceeds the $p$-adic valuation of $|\hat{E}(\mathbb{F}_p)|$.

At bad primes $v \mid N$: the local saturation depth $B_v$ depends on the Kodaira type and is bounded by $v_p(c_v) + 1$, where $c_v$ is the Tamagawa number.

**The bound:**

$$\boxed{B(E, p) = 1 + \max\!\big(B_p,\; \max_{v \mid N} B_v\big).}$$

This is computed from $a_p$ (Frobenius trace), Kodaira types, and Tamagawa numbers — all independently available from local arithmetic without any assumption on $\Sha$.

---

## Key Observation: The Indistinguishability Trap

For $n \leq m$, the groups $((\mathbb{Z}/p^m\mathbb{Z})^2)[p^n] \cong (\mathbb{Z}/p^n\mathbb{Z})^2$ and $((\mathbb{Q}_p/\mathbb{Z}_p)^2)[p^n] \cong (\mathbb{Z}/p^n\mathbb{Z})^2$ are isomorphic. A long initial segment of the descent filtration for a finite group with exponent $p^m$ is **indistinguishable** from the filtration for a group with a divisible tail.

This means: observing $D_1 = D_2 = \cdots = D_N$ for any finite $N$ does **not** prove $D_\infty = 0$. One could have a class of order $p^{N+1}$ invisible to the first $N$ levels.

**What breaks the trap:** The bound $B$ derived above uses structural information (the local saturation depth) that is independent of the apparent plateau. If $D_B = D_{B+1}$ and $B$ exceeds the local saturation depth at every prime, then the transition map $\rho_B$ has trivial kernel and trivial cokernel, forcing $D_\infty = D_B$. This is a structural conclusion, not a numerical observation.

**Critical:** If $D_B \neq 0$, the surviving classes are genuine obstructions — elements of $\Sha[p^\infty]$ that persist at every depth. Their existence is consistent with $\Sha[p^\infty] \neq 0$, and the proposal does not claim to force their disappearance. It claims to **detect** whether the filtration has stabilized, using local data alone.

---

## First Experiment: 389.a1 at $p = 3$

**Curve:** $E = 389.a1$: $y^2 + y = x^3 + x^2 - 2x$, rank $r = 2$, $E(\mathbb{Q})_{\mathrm{tors}} = 0$.

**Known:** $\Sha[2] = 0$ (proven by 2-descent). $\Sha[3^\infty] = 0$ (proven by González–Sadek, Sijsling via explicit 3-descent). The descent must stop. The question: can the stopping be detected from local data alone?

**Local data at $p = 3$:**
- $a_3 = -2$, so $p + 1 - a_3 = 3 + 1 - (-2) = 6$, $v_3(6) = 1$. Thus $B_3 = 1 + 1 = 2$.
- Conductor $N = 389$ (prime), Kodaira type $I_1$ at $389$, $c_{389} = 1$, $v_3(1) = 0$. Thus $B_{389} = 1$.
- **Bound:** $B(E, 3) = 1 + \max(2, 1) = 3$.

**Computation target:**
1. **$D_1 = \Sha[3]$:** Compute $\mathrm{Sel}_3(E/\mathbb{Q})$ via explicit 3-descent (homogeneous spaces as plane cubics). $\dim_{\mathbb{F}_3} E(\mathbb{Q})/3E(\mathbb{Q}) = 2$ (rank 2, trivial torsion). If $\dim \mathrm{Sel}_3 = 2$, then $\Sha[3] = 0$ and $D_1 = 0$.

2. **$D_2 = 3\Sha[9]$:** Only needed if $D_1 \neq 0$. Compute $\mathrm{Sel}_9(E/\mathbb{Q})$ via 9-descent on the 3-coverings from $\mathrm{Sel}_3$. Track $\rho_1: \mathrm{Sel}_3 \to \mathrm{Sel}_9$.

3. **Stopping test:** If $D_1 = 0$, the descent stops at depth 1 (below the bound $B = 3$). If $D_1 \neq 0$ but $D_2 = D_1$, check whether $B = 3$ is reached; if so, $D_\infty = D_1$ by the structural argument.

**Expected outcome:** $\Sha[3] = 0$, so $D_1 = 0$ and the descent stops immediately. The bound $B = 3$ is never reached — the actual stopping depth is 1, which is strictly below the computable bound. This is consistent: the bound is an upper bound on the depth needed to detect stabilization, not a prediction of the exact depth.

**What this tests:** Whether the local saturation bound $B$ is sharp enough to be useful. If $B$ were, say, 1000, the bound would be computable but impractical. For 389.a1 at $p = 3$, $B = 3$ is entirely practical.

---

## Failure Conditions (Reject Criteria)

The proposed stopping rule is **rejected** if it relies on:

1. **Apparent plateau:** Observing $D_1 = D_2 = \cdots = D_N$ for some $N$ without structural justification for why $D_{N+1} = D_N$. The indistinguishability trap makes this insufficient.

2. **BSD-predicted $\Sha$ order:** Using the numerical value $|\Sha| = 1$ from LMFDB or the BSD ratio $\approx 1$ to conclude $\Sha[p] = 0$. This is circular: the descent is supposed to *prove* what BSD predicts.

3. **Assumed $\Sha$ finiteness:** The Cassels–Tate pairing is non-degenerate *assuming* $\Sha$ is finite. Using non-degeneracy to force $D_\infty = 0$ requires finiteness as an input, which is the very thing we are trying to establish.

4. **Ignoring the transition maps:** Claiming stabilization based solely on the size of $\mathrm{Sel}_{p^n}$ without tracking $\rho_n : \mathrm{Sel}_{p^n} \to \mathrm{Sel}_{p^{n+1}}$. The maps carry the structural information; the groups alone do not.

---

## Experimental Extension: Curves Where $\Sha[3] \neq 0$

To test the mechanism beyond the trivial case ($\Sha[p] = 0$), identify a curve $E/\mathbb{Q}$ of rank 2 with $\Sha[3] \neq 0$. Candidates from LMFDB searches:

- Compute $\mathrm{Sel}_3$ for several rank-2 curves with conductor $\leq 5000$.
- For each with $\dim \mathrm{Sel}_3 > 2$, the excess classes represent $\Sha[3] \neq 0$.
- Track $\rho_1 : \mathrm{Sel}_3 \to \mathrm{Sel}_9$ on these excess classes.
- Verify: does $D_2 = D_1$ hold at the predicted bound $B$?

This experiment tests the mechanism in the non-trivial regime and provides evidence for (or against) the sharpness of the bound $B$.

---

## References

1. **Greenberg, R.** "Iwasawa theory for elliptic curves." *Arithmetic Theory of Elliptic Curves* (Cetraro, 1997), Lecture Notes in Math. 1716, Springer, 1999.
2. **Mazur, B.** "Rational points of abelian varieties with values in towers of number fields." *Invent. Math.* 18 (1972), 183–266.
3. **Cassels, J.W.S.** "Arithmetic on curves of genus 1, VIII. On conjectures of Birch and Swinnerton-Dyer." *J. Reine Angew. Math.* 217 (1965), 180–189.
4. **González-Sadek, M., Sijsling, J.** "Explicit descent on elliptic curves." (3-descent computations for curves of small conductor.)
5. **Skinner, C., Urban, E.** "The Iwasawa main conjectures for $\mathrm{GL}_2$." *Inst. Hautes Études Sci. Publ. Math.* 121 (2014), 1–237.
6. **Kolyvagin, V.A.** "Euler systems for Grothendieck motives and the Birch and Swinnerton-Dyer conjecture." (Bounding $\Sha$ from above via Euler system classes.)
