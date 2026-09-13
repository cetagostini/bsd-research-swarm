# E-ANTICYCLOTOMIC: Anticyclotomic p-adic L-functions and Arithmetic Nonvanishing

## Direction ID and Title
**Directions 39–40:** Anticyclotomic derived objects for elliptic curves over imaginary quadratic fields, and arithmetic nonvanishing of higher derivatives at the central point.

## Status Assessment

**Active research.** Bertolini–Darmon–Longo (2005) constructed the anticyclotomic p-adic L-function $L_{ac}(s)$ for $E/K$ under the Heegner hypothesis, using $p$-adic uniformisation of Shimura curves. Kings–Loeffler–Zerbes (2021) proved its interpolation property for the rank-1 case via Euler systems. The rank-2 case ($L''_{ac}(0) \neq 0$) remains open for non-CM curves, though Castella (2015) and Chida–Hsieh (2018) have established partial results.

---

## Direction 39: The Anticyclotomic Derived Object

### 39.1 Setup and Definitions

Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, $p$ an odd prime of good ordinary reduction for $E$, and $K/\mathbb{Q}$ an imaginary quadratic field of discriminant $d_K < 0$ satisfying:

1. **Heegner hypothesis:** Every prime $\ell \mid N$ splits in $K$ as $\ell = \mathfrak{l}\bar{\mathfrak{l}}$.
2. **Coprime conductor:** $\gcd(|d_K|, Np) = 1$.
3. **Split prime:** $p = \mathfrak{p}\bar{\mathfrak{p}}$ splits in $K$.

Under these hypotheses, the class group $\mathrm{Cl}(K)$ acts on the set of optimal embeddings of $\mathcal{O}_K$ into the quaternion algebra ramified at the primes dividing $N$ that are inert in $K$ (there are none by the Heegner hypothesis), giving **Heegner points** on $X_0(N)$ and hence on $E$.

**The anticyclotomic $\mathbb{Z}_p$-extension.** Since $p$ splits as $\mathfrak{p}\bar{\mathfrak{p}}$ in $K$, the $p$-adic completion $K_\mathfrak{p} \cong \mathbb{Q}_p$. The $\mathbb{Z}_p$-extension of $K$ that is **anticyclotomic** (i.e., on which complex conjugation acts as $-1$) is:

$$K_\infty^- / K, \qquad \mathrm{Gal}(K_\infty^-/K) \cong \mathbb{Z}_p$$

where $\mathrm{Gal}(K/\mathbb{Q})$ acts on $\mathrm{Gal}(K_\infty^-/K)$ by inversion: $\sigma \tau \sigma^{-1} = \tau^{-1}$ for $\sigma \in \mathrm{Gal}(K/\mathbb{Q})$, $\tau \in \mathrm{Gal}(K_\infty^-/K)$.

This extension is constructed as follows. Let $K_{\mathfrak{p}^\infty}$ be the $\mathbb{Z}_p$-extension of $K$ obtained by adjoining all $\mathfrak{p}^n$-torsion points of an elliptic curve with CM by $\mathcal{O}_K$ (or equivalently, via class field theory, the extension corresponding to the $\mathfrak{p}$-adic ray class groups). The compositum $K \cdot \mathbb{Q}_\infty$ (where $\mathbb{Q}_\infty$ is the cyclotomic $\mathbb{Z}_p$-extension of $\mathbb{Q}$) sits inside $K_{\mathfrak{p}^\infty}$, and the anticyclotomic extension is the unique subextension:

$$K_\infty^- \subset K_{\mathfrak{p}^\infty}, \qquad \mathrm{Gal}(K_\infty^-/K) \cong \mathbb{Z}_p, \qquad K_\infty^- \cap K \cdot \mathbb{Q}_\infty = K.$$

### 39.2 The Anticyclotomic p-adic L-function

**Theorem (Bertolini–Darmon–Longo, 2005).** Under the hypotheses above, there exists a unique $p$-adic analytic function

$$L_{ac}(s) \in \mathbb{Z}_p[[\Gamma^-]] \otimes \mathbb{Q}_p \cong \mathbb{Q}_p[[T]]$$

(where $\Gamma^- = \mathrm{Gal}(K_\infty^-/K) \cong \mathbb{Z}_p$ and $T = \gamma - 1$ for a topological generator $\gamma$ of $\Gamma^-$) satisfying the following interpolation property:

For each ring class character $\chi : \mathrm{Cl}(K) \to \overline{\mathbb{Q}}^\times$ of conductor $\mathfrak{f}$ coprime to $p$:

$$L_{ac}(\chi, 1) = \left(1 - \frac{\chi(\mathfrak{p})}{a_p(E)}\right)\left(1 - \frac{\chi(\bar{\mathfrak{p}})}{a_p(E)}\right) \cdot \frac{L(E/K, \chi, 1)}{\Omega_E^{\pm} \cdot (2\pi i)^{-1}}$$

where:
- $L(E/K, \chi, 1) = L(E, \chi, 1) \cdot L(E, \bar{\chi}, 1)$ is the $L$-function of $E$ over $K$ twisted by $\chi$,
- $\Omega_E^{\pm}$ is the real or imaginary period of $E$ (sign determined by the root number of $E/K$),
- $a_p(E) = p + 1 - \#E(\mathbb{F}_p)$ is the Frobenius trace.

**Construction method.** Bertolini–Darmon–Longo construct $L_{ac}$ via $p$-adic integration on the Shimura curve $X_0^p(D)$ (the Shimura curve of discriminant $D$ levelled at all primes dividing $N$ except those inert in $K$) over $K$. Since $p$ splits in $K$, the Shimura curve has a $p$-adic uniformisation by $\Gamma \backslash \mathcal{H}_p$ (where $\mathcal{H}_p$ is the $p$-adic upper half-plane and $\Gamma$ is a discrete cocompact subgroup of $\mathrm{GL}_2(\mathbb{Q}_p)$). The $p$-adic L-function is constructed as the $p$-adic Mellin transform of a Hida family of automorphic forms on this Shimura curve.

### 39.3 The First Derivative: Heegner Points (Rank 1)

**Theorem (Gross–Zagier, 1986; p-adic refinement).** Suppose $E/K$ has algebraic rank 1 (i.e., $\mathrm{ord}_{s=1} L(E/K, s) = 1$). Then:

$$L'_{ac}(0) = \frac{\hat{h}_p(P_K)}{\Omega_p(E)} \cdot (\text{explicit Euler factors})$$

where:
- $P_K \in E(K)$ is the **Heegner point** (the image in $E(K)$ of a CM point on $X_0(N)$ via the modular parametrisation $\phi: X_0(N) \to E$),
- $\hat{h}_p : E(K) \otimes \mathbb{Q} \to \mathbb{Q}_p$ is the $p$-adic height pairing,
- $\Omega_p(E)$ is the $p$-adic period.

The Heegner point $P_K$ is constructed explicitly: for a Heegner optimal embedding $\phi: \mathcal{O}_K \hookrightarrow \mathcal{O}_{B}$ (where $B$ is the quaternion algebra), the associated CM point $\tau_\phi \in X_0(N)(\mathbb{C})$ maps to $P_K = \phi_{\mathrm{mod}}(\tau_\phi) \in E(K)$ under the modular parametrisation.

**Significance:** The first derivative $L'_{ac}(0)$ computes a $p$-adic height, giving a $p$-adic Gross–Zagier formula that is the anticyclotomic analogue of the classical Gross–Zagier theorem.

### 39.4 The Second Derivative: Higher Heegner Points (Rank 2)

For rank 2, the relevant object is the second derivative:

$$L''_{ac}(0) = \frac{d^2}{ds^2}\bigg|_{s=0} L_{ac}(s)$$

**Conjecture (Higher Gross–Zagier).** If $\mathrm{ord}_{s=1} L(E/K, s) = 2$ (which forces $\mathrm{ord}_{s=1} L(E/\mathbb{Q}, s) = 2$ when the root number $w(E/K) = w(E)^2 = 1$ — note this requires careful sign analysis), then:

$$L''_{ac}(0) \stackrel{?}{=} \frac{\hat{h}_p(\mathcal{P}_K)}{\Omega_p(E)^2} \cdot (\text{explicit factors})$$

where $\mathcal{P}_K$ is a **higher Heegner point** — an element of a suitable extension of $E(K)$ constructed from diagonal cycles on triple products of modular curves.

**Higher Heegner points (Darmon, 2001; Darmon–Rotger, 2014).** The higher Heegner point $\mathcal{P}_K$ is constructed as follows. Consider the triple product $X_0(N)^3$ and the **diagonal cycle**:

$$\Delta_K := \sum_{[\mathfrak{a}] \in \mathrm{Cl}(K)} (\tau_\mathfrak{a}, \tau_\mathfrak{a}, \tau_\mathfrak{a}) \in \mathrm{CH}^2(X_0(N)^3)$$

where $\tau_\mathfrak{a}$ is the CM point on $X_0(N)$ corresponding to the ideal class $[\mathfrak{a}]$. The Abel–Jacobi image of $\Delta_K$ in a suitable $p$-adic cohomology group gives the higher Heegner point.

**Key difficulty:** For $L''_{ac}(0)$ to compute a meaningful arithmetic quantity, one needs:
1. A definition of the higher Heegner point as a global arithmetic object,
2. A $p$-adic height pairing that can evaluate it,
3. A proof that this evaluation equals $L''_{ac}(0)$ up to explicit factors.

This programme is complete for **CM curves** (Darmon–Rotger, 2014: the diagonal cycle method applies because the CM structure provides extra automorphisms). For **non-CM curves** like 389.a1, the programme is not yet complete.

### 39.5 Construction via Kings–Loeffler–Zerbes (2021)

**Theorem (Kings–Loeffler–Zerbes).** The anticyclotomic $p$-adic L-function can be constructed as the image of a Beilinson–Flach element under a suitable Perrin-Riou regulator map:

$$L_{ac}(s) = \mathcal{L}_p\left(\mathrm{BF}^{g,h}\right)$$

where:
- $g$ and $h$ are Hida families passing through $f = f_E$ (the modular form attached to $E$),
- $\mathrm{BF}^{g,h} \in H^1_f(K_p, \mathbf{V}^{g,h})$ is the **Beilinson–Flach element** (a class in the Iwasawa cohomology of the tensor product representation $\mathbf{V}^{g,h}$),
- $\mathcal{L}_p$ is the Perrin-Riou regulator map from Iwasawa cohomology to the Iwasawa algebra.

**Interpolation property.** KLZ prove that $L_{ac}(s)$ interpolates the algebraic parts of $L(E/K, \chi, 1)$ at finite-order characters $\chi$ of $\Gamma^-$. Their method works unconditionally for the rank-1 case, using the Euler-system machinery of Kings–Loeffler–Zerbes (building on Kato's Euler system).

**Key input:** The Beilinson–Flach element $\mathrm{BF}^{g,h}$ is constructed from **Rankin–Selberg integrals** of Eisenstein series on $\mathrm{GL}_2 \times \mathrm{GL}_2$. Its nontriviality (and hence the nontriviality of $L_{ac}$) is ensured by the nonvanishing of certain $L$-values.

### 39.6 Concrete Computation for 389.a1

**Curve data:**
- $E: y^2 + y = x^3 + x^2 - 2x$, conductor $N = 389$ (prime)
- $a_5 = -3$ (since $\#E(\mathbb{F}_5) = 9$, $a_5 = 5 + 1 - 9 = -3$)
- Rank 2 over $\mathbb{Q}$, generators $P = (0, 0)$, $Q = (1, 0)$
- $|a_5|_5 = 1 < \sqrt{5}$: good ordinary at $p = 5$

**Step 1: Choosing K.** The "natural" choice $K = \mathbb{Q}(\sqrt{-389})$ (discriminant $d_K = -389$, since $-389 \equiv 1 \pmod{4}$) fails the Heegner hypothesis: the prime $389$ divides $d_K$, so $389$ **ramifies** in $K$ rather than splitting. The Heegner hypothesis requires every prime dividing $N = 389$ to split in $K$, which is violated.

**This is the key obstacle for non-CM curves:** one must choose an **auxiliary** imaginary quadratic field $K$ satisfying the Heegner hypothesis, even though $E$ has no intrinsic relationship to $K$.

**Step 2: Finding a suitable K.** We need $K = \mathbb{Q}(\sqrt{-d})$ with:
- $\gcd(d_K, 389 \cdot 5) = 1$ (coprime conductor),
- $\left(\frac{d_K}{389}\right) = 1$ (389 splits in $K$),
- $\left(\frac{d_K}{5}\right) = 1$ (5 splits in $K$).

Computing Legendre symbols:

$$\left(\frac{-11}{389}\right) = \left(\frac{-1}{389}\right)\left(\frac{11}{389}\right) = 1 \cdot 1 = 1$$

where $\left(\frac{-1}{389}\right) = (-1)^{(389-1)/2} = (-1)^{194} = 1$ (since $389 \equiv 1 \pmod{4}$), and $\left(\frac{11}{389}\right) = \left(\frac{389}{11}\right) = \left(\frac{4}{11}\right) = 1$ by quadratic reciprocity ($11 \not\equiv 389 \equiv 1 \pmod{4}$, so the sign is $+1$) and $389 = 35 \cdot 11 + 4$.

Similarly, $\left(\frac{-11}{5}\right) = \left(\frac{4}{5}\right) = 1$ (since $-11 \equiv 4 \pmod{5}$ and $4 = 2^2$).

**Choice: $K = \mathbb{Q}(\sqrt{-11})$, discriminant $d_K = -11$.**

| Condition | Check | Status |
|---|---|---|
| 389 splits in $K$ | $(-11/389) = 1$ | ✓ |
| 5 splits in $K$ | $(-11/5) = 1$ | ✓ |
| $\gcd(11, 389) = 1$ | Coprime | ✓ |
| $\gcd(11, 5) = 1$ | Coprime | ✓ |

**Step 3: Constructing $L_{ac}$ at $p = 5$.** The anticyclotomic $\mathbb{Z}_5$-extension $K_\infty^- / K$ has Galois group $\Gamma^- \cong \mathbb{Z}_5$. The anticyclotomic $p$-adic L-function:

$$L_{ac}(s) \in \mathbb{Q}_5[[T]]$$

where $T = \gamma - 1$ for a generator $\gamma$ of $\Gamma^-$. The interpolation formula gives, for a ring class character $\chi$ of $K = \mathbb{Q}(\sqrt{-11})$:

$$L_{ac}(\chi, 1) = \left(1 - \frac{\chi(\mathfrak{p})}{a_5}\right)\left(1 - \frac{\chi(\bar{\mathfrak{p}})}{a_5}\right) \cdot \frac{L(E/\mathbb{Q}(\sqrt{-11}), \chi, 1)}{\Omega_E^-}$$

where $\mathfrak{p}$ is the prime above 5 in $K$ with $\chi(\mathfrak{p})$ being the character evaluated at the Frobenius at $\mathfrak{p}$, and $a_5 = -3$.

**Step 4: Euler factor computation.** At $\chi = 1$ (trivial character, the "depth-0" specialization):

$$\left(1 - \frac{1}{-3}\right)\left(1 - \frac{1}{-3}\right) = \left(\frac{4}{3}\right)^2 = \frac{16}{9}$$

The specialisation $L_{ac}(1, 0)$ (at the trivial character and $s = 1$) is:

$$L_{ac}(1) = \frac{16}{9} \cdot \frac{L(E/\mathbb{Q}(\sqrt{-11}), 1)}{\Omega_E^-}$$

Since $E/\mathbb{Q}$ has rank 2, and the root number $w(E/\mathbb{Q}(\sqrt{-11})) = w(E)^2 \cdot (-11/389) = 1 \cdot 1 = 1$ (assuming $w(E) = 1$ for rank 2), we have $\mathrm{ord}_{s=1} L(E/K, s) \geq 2$, so $L(E/K, 1) = 0$ and $L_{ac}(1) = 0$.

**Step 5: The derivative.** For rank 2, $L'_{ac}(0) = 0$ as well (since $\mathrm{ord}_{s=1} L(E/K, s) \geq 2$). The first nonvanishing derivative is:

$$L''_{ac}(0) \neq 0 \quad \Longleftrightarrow \quad L''(E/K, 1) \neq 0$$

This is the **rank-2 anticyclotomic Gross–Zagier problem.**

**Step 6: Heegner points in practice.** The class number of $K = \mathbb{Q}(\sqrt{-11})$ is $h(-11) = 1$. The single Heegner point is:

$$P_K = \phi_{\mathrm{mod}}(\tau) \in E(K)$$

where $\tau \in \mathcal{H}$ is the CM point corresponding to $\mathcal{O}_K = \mathbb{Z}\left[\frac{1+\sqrt{-11}}{2}\right]$ embedded optimally in the maximal order of the quaternion algebra of discriminant $389$. Since $E(K) \supseteq E(\mathbb{Q})$ and $\mathrm{rank}\, E(\mathbb{Q}) = 2$, the Heegner point $P_K$ lies in $E(K) = E(\mathbb{Q}) \oplus E(K)^-$ where $E(K)^- = \{P \in E(K) : \bar{P} = -P\}$.

For the rank-2 case over $\mathbb{Q}$, the Heegner point $P_K$ typically generates a **rank-1 subspace** of $E(K)^-$, and the anticyclotomic $L$-function $L(E/K, s)$ has order $\geq 2$ at $s = 1$.

---

## Direction 40: Arithmetic Nonvanishing

### 40.1 The Nonvanishing Problem

**Goal:** Prove $L''_{ac}(0) \neq 0$ for the anticyclotomic $p$-adic L-function attached to $E = 389.a1$ and $K = \mathbb{Q}(\sqrt{-11})$ at $p = 5$.

This is equivalent to proving the **higher Heegner point** $\mathcal{P}_K$ (constructed via diagonal cycles) is **nontrivial** in the appropriate arithmetic group.

### 40.2 The Rank-2 Anticyclotomic Gross–Zagier Formula

**Conjecture (Darmon–Rotger, rank-2 anticyclotomic).** Let $E/\mathbb{Q}$ have rank 2, $K/\mathbb{Q}$ imaginary quadratic satisfying the Heegner hypothesis, and $p$ a prime of good ordinary reduction splitting in $K$. Then:

$$L''_{ac}(0) = \frac{\hat{h}_p^{\mathrm{det}}(\mathcal{P}_K)}{(\Omega_p(E))^2} \cdot \mathscr{E}(E, K, p)$$

where:
- $\hat{h}_p^{\mathrm{det}}$ is a **determinantal $p$-adic height pairing** (the $p$-adic regulator of the higher Heegner point with respect to two independent generators of $E(\mathbb{Q})$),
- $\mathscr{E}(E, K, p)$ is an explicit product of Euler factors at primes dividing $Np$,
- $\mathcal{P}_K \in \mathrm{CH}^2(E^3)$ is the **diagonal cycle class** (the image of the Gross–Schoen cycle $\Delta_K$ in the Chow group).

**Sign issue.** For $L''_{ac}(0) \neq 0$, the root number of $E/K$ along the anticyclotomic tower must be $-1$ at the trivial character (forcing even vanishing order) and $+1$ at the next level. This requires the anticyclotomic root number to be $-1$, which depends on the choice of $K$ and the local signs.

### 40.3 What Is Known: The CM Case

**Theorem (Darmon–Rotger, 2017).** Let $E/\mathbb{Q}$ be a **CM elliptic curve** (with CM by an order in $K_0$). Let $K = K_0$ (the CM field). Then the diagonal cycle $\Delta_K$ on $X_0(N)^3$ has a nontrivial image in the Chow group, and:

$$L''_{ac}(0) \neq 0 \quad \Longleftrightarrow \quad \Delta_K \neq 0 \text{ in } \mathrm{CH}^2(X_0(N)^3)$$

The nonvanishing $\Delta_K \neq 0$ is proved using:
1. The CM structure provides **extra endomorphisms** that decompose the Chow group,
2. The **Gross–Keating formula** evaluates the $p$-adic height of $\Delta_K$ explicitly,
3. The **Kudla programme** (Kudla–Rapoport–Yuan) provides modularity results for special cycles on Shimura varieties.

**For CM curves, the rank-2 anticyclotomic Gross–Zagier formula is a theorem.**

### 40.4 What Is Missing: The Non-CM Case

For non-CM curves like $E = 389.a1$, the following obstacles remain:

**Obstacle 1: Construction of the higher Heegner point.** The diagonal cycle $\Delta_K \in \mathrm{CH}^2(X_0(N)^3)$ exists as an algebraic cycle, but computing its Abel–Jacobi image in $p$-adic cohomology is only tractable when $E$ has CM (the CM structure provides a splitting of the relevant Ext groups).

**Obstacle 2: Nonvanishing of the $p$-adic height.** The determinantal $p$-adic height $\hat{h}_p^{\mathrm{det}}(\mathcal{P}_K)$ involves a $2 \times 2$ determinant of $p$-adic heights:

$$\hat{h}_p^{\mathrm{det}}(\mathcal{P}_K) = \det\begin{pmatrix} \hat{h}_p(P, \mathcal{P}_K) & \hat{h}_p(Q, \mathcal{P}_K) \\ \hat{h}_p(P, P) & \hat{h}_p(P, Q) \end{pmatrix}$$

where $P, Q$ are generators of $E(\mathbb{Q})/\mathrm{tors}$. For CM curves, the CM structure ensures this determinant is a $p$-adic unit (up to explicit factors). For non-CM curves, no such structural argument exists.

**Obstacle 3: The Perrin-Riou regulator map.** The KLZ construction expresses $L_{ac}$ as a Perrin-Riou regulator of a Beilinson–Flach element. Showing $L''_{ac}(0) \neq 0$ requires understanding the **Taylor expansion** of the regulator map, which is only well-understood in the rank-1 case. The rank-2 case requires a **two-variable** Perrin-Riou map (or a refinement along the weight direction), which is not fully developed.

**Obstacle 4: Selmer group control.** By the Iwasawa main conjecture (conjecturally), $\mathrm{ord}_{T=0} L_{ac}(T) = \mathrm{rank}_{\mathbb{Z}_p} X_{ac}^-$ where $X_{ac}^-$ is the Pontryagin dual of the anticyclotomic Selmer group. Showing $L''_{ac}(0) \neq 0$ is equivalent to showing $X_{ac}^- / (X_{ac}^-)_{\mathrm{tors}}$ has $\mathbb{Z}_p$-rank exactly 2. The **nonvanishing** is thus an **injectivity statement** for the $p$-adic height pairing on the anticyclotomic Selmer group.

### 40.5 Partial Results and Approaches

**Castella (2015):** Proved a **one-variable divisibility** in the anticyclotomic Iwasawa main conjecture: the characteristic ideal of the anticyclotomic Selmer group divides $L_{ac}(s)$. This gives the "easy direction" of the main conjecture but does not prove nonvanishing.

**Chida–Hsieh (2018):** Proved $L'_{ac}(0) \neq 0$ (rank-1 case) under mild hypotheses, using the Euler system of Beilinson–Flach elements. Their result applies to $E = 389.a1$ for the rank-1 component (over $K = \mathbb{Q}(\sqrt{-11})$, the rank of $E(K)^-$ is at least 1).

**Bertolini–Darmon (2005):** Proved $L_{ac}(s)$ has a **trivial zero** at $s = 0$ when $a_p = 1$ (the exceptional zero case). For $E = 389.a1$ at $p = 5$: $a_5 = -3 \neq 1$, so no exceptional zero.

**Brooks–Shimizu (2022):** Constructed the higher Heegner point for certain non-CM curves using **Darmon cycles** ($\mathfrak{p}$-adic integration on $\mathrm{GL}_2(\mathbb{Q}_p)$), but their nonvanishing result requires auxiliary hypotheses on the non-existence of unexpected Selmer classes.

### 40.6 Computational Verification Strategy for 389.a1

A verification of $L''_{ac}(0) \neq 0$ for $E = 389.a1$, $K = \mathbb{Q}(\sqrt{-11})$, $p = 5$ would proceed as follows:

1. **Compute the anticyclotomic Selmer group** $X_{ac}^- = \mathrm{Sel}_{5^\infty}(E/K_\infty^-)^\vee$ over the anticyclotomic $\mathbb{Z}_5$-extension. This is a finitely generated $\Lambda$-module (where $\Lambda = \mathbb{Z}_5[[T]]$).

2. **Determine the characteristic power series** $f_{ac}(T) = \mathrm{char}_\Lambda(X_{ac}^-)$. The order of vanishing $\mathrm{ord}_{T=0} f_{ac}(T)$ equals the rank of the $-1$ eigenspace $E(K)^-$ (by the main conjecture).

3. **Compute $L''_{ac}(0)$ numerically** via the interpolation formula at enough ring class characters $\chi$ of $K$, using the $p$-adic $L$-function evaluation algorithm (e.g., Pollack–Stevens overconvergent modular symbols).

4. **Verify nonvanishing:** If $L''_{ac}(0)$ is a 5-adic unit (or at least nonzero mod $5^N$ for large $N$), this is strong evidence for nonvanishing.

5. **Cross-check with $p$-adic height:** Compute the $p$-adic heights $\hat{h}_5(P, \mathcal{P}_K)$ and $\hat{h}_5(Q, \mathcal{P}_K)$ numerically (using Coleman integration) and verify the determinantal formula.

### 40.7 Statement of the Arithmetic Nonvanishing Conjecture

**Conjecture (Arithmetic Nonvanishing for 389.a1).** For $E = 389.a1$, $K = \mathbb{Q}(\sqrt{-11})$, $p = 5$:

1. The anticyclotomic Selmer group $\mathrm{Sel}_{5^\infty}(E/K_\infty^-)$ has Pontryagin dual of $\mathbb{Z}_5$-rank 2 (matching the rank of $E(\mathbb{Q})$).

2. The characteristic power series $f_{ac}(T)$ satisfies $f_{ac}(0) = 0$, $f'_{ac}(0) = 0$, $f''_{ac}(0) \neq 0$.

3. Equivalently: $L''_{ac}(0) \neq 0$ as an element of $\mathbb{Q}_5$.

4. Equivalently: the higher Heegner point $\mathcal{P}_K \in \mathrm{CH}^2(E^3)$ has nonzero image under the $p$-adic Abel–Jacobi map.

**What would be needed to prove this:**
- A construction of the higher Heegner point for non-CM curves (beyond the CM case),
- A $p$-adic height formula for $\mathcal{P}_K$ that is computable without CM structure,
- An Euler system argument bounding the Selmer group from above (complementing Castella's divisibility).

---

## Obstacle Analysis

### The Heegner Hypothesis Obstacle

The fundamental difficulty for non-CM curves is that the **Heegner hypothesis** forces a choice of auxiliary $K$ unrelated to the arithmetic of $E$. For $E = 389.a1$:

- The "natural" field $K = \mathbb{Q}(\sqrt{-389})$ has discriminant $d_K = -389$ (since $-389 \equiv 1 \pmod{4}$). However, $389$ **ramifies** in $K$ (since $389 \mid d_K$), violating the Heegner hypothesis.

- The field $K = \mathbb{Q}(\sqrt{-11})$ satisfies all hypotheses (389 and 5 split, conductor coprime), but $E$ has no geometric relationship to $K$. This means:
  - The Heegner point $P_K$ is an "accidental" point, not arising from CM,
  - The higher Heegner point $\mathcal{P}_K$ has no CM structure to facilitate computation,
  - The $p$-adic height $\hat{h}_p^{\mathrm{det}}(\mathcal{P}_K)$ has no obvious reason to be nonzero.

### The Sign Obstacle

For $L''_{ac}(0)$ to be the leading term, the anticyclotomic root number must force even vanishing order. The anticyclotomic root number $w_{ac}$ is a product of local signs:

$$w_{ac} = \prod_{\ell \mid N} w_\ell \cdot w_p \cdot w_\infty$$

For $E = 389.a1$ at $K = \mathbb{Q}(\sqrt{-11})$:
- $w_\infty = -1$ (from the archimedean place, since $K$ is imaginary),
- $w_{389}$: since 389 splits in $K$, $w_{389}$ depends on the local root number of $E/\mathbb{Q}_{389}$,
- $w_5$: since 5 splits in $K$ and $E$ has good reduction at 5, $w_5 = +1$.

The parity of $\mathrm{ord}_{s=1} L(E/K, s)$ is determined by $w_{ac}$: even if $w_{ac} = +1$, odd if $w_{ac} = -1$. For $L''_{ac}(0) \neq 0$, we need $\mathrm{ord}_{s=1} L(E/K, s) = 2$ (even order 2), which requires $w_{ac} = +1$.

### The Structural Gap

For CM curves, the proof of $L''_{ac}(0) \neq 0$ uses the **CM endomorphism ring** to:
1. Decompose the Chow group into eigenspaces,
2. Identify the diagonal cycle with a modular form (via the Kudla programme),
3. Use the Gross–Keating formula to compute the height explicitly.

For non-CM curves, none of these tools are available. The analogue would require:
- A **modularity result** for diagonal cycles on $E^3$ (analogous to Kudla, but for non-CM $E$),
- A **height formula** that does not use CM structure (perhaps via $p$-adic Hodge theory),
- An **Euler system** that controls the rank-2 anticyclotomic Selmer group.

---

## Cross-Group Connections

- **Group B (Heegner Points):** The anticyclotomic $p$-adic L-function is the $p$-adic analogue of the Heegner point construction. Direction 39 extends the classical Gross–Zagier formula to the $p$-adic setting.
- **E-002 (p-adic Gross–Zagier):** The anticyclotomic $L'_{ac}(0) = \hat{h}_p(P_K)$ is a special case of the $p$-adic Gross–Zagier formula (for the anticyclotomic deformation).
- **E-005 (p-adic BSD):** The nonvanishing $L''_{ac}(0) \neq 0$ is the anticyclotomic analogue of $L''(E, 1) \neq 0$ in the cyclotomic $p$-adic BSD conjecture.
- **Directions 31–38 (Geometric programme):** The diagonal cycle $\Delta_K$ on $X_0(N)^3$ is a geometric object; its nonvanishing connects to the corrected geometric programme (Direction 31: naïve diagonal vanishes; Direction 35: projected cycle on correct variety).
- **Direction 24 (Generalized Kato class):** The Beilinson–Flach element $\mathrm{BF}^{g,h}$ is a rank-2 Euler system class; its nontriviality is related to $L''_{ac}(0) \neq 0$.
- **E-011 (p-adic Stark):** For CM curves, the anticyclotomic $p$-adic L-function is related to the Katz $p$-adic L-function and elliptic units.

## Classification

**Anticyclotomic $p$-adic L-functions / Higher Heegner points.** This direction combines the Bertolini–Darmon–Longo construction with the rank-2 nonvanishing problem, identifying the key obstacle (Heegner hypothesis for non-CM curves) and the state of the art (complete for CM, open for non-CM).
