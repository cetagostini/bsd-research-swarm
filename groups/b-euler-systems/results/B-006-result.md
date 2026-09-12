# B-006: Euler Systems for GL(n) — Discovery and Verification

## Direction ID and Title
B-006 — Euler Systems for GL(n) — Discovery and Verification

## Status Assessment
Euler systems are known for $GL(1)$ (cyclotomic units), $GL(2)$ (Kato, Beilinson-Flach), and $GL(2) \times GL(2)$ (Rankin-Selberg BF elements). For $GL(n)$ with $n \geq 3$, no Euler system has been constructed for any Galois representation. The geometry of Shimura varieties for $GL(n)$ ($n \geq 3$) — particularly Picard modular surfaces and Siegel modular varieties — is far more complex, and the algebraic cycles generating the expected cohomology are unknown. The direction is Conjectural with no constructive progress.

## Testable Conjecture or Lemma

**Conjecture B-006.** Let $\pi$ be a regular algebraic cuspidal automorphic representation of $GL(n)/\mathbb{A}_\mathbb{Q}$ with associated $p$-adic Galois representation $\rho_p: G_\mathbb{Q} \to GL(n, \overline{\mathbb{Q}}_p)$. Assume $\rho_p$ is irreducible and geometric. There exists an Euler system $\{c_m \in H^1_f(\mathbb{Q}(m), \rho_p)\}$ indexed by squarefree products $m$ of primes where $\pi$ is unramified, satisfying:

(a) **Norm compatibility:** $\operatorname{Cor}_{m\ell/m}(c_{m\ell}) = P_\ell(\operatorname{Frob}_\ell^{-1}) \cdot c_m$ where $P_\ell(x) = \det(1 - \rho_p(\operatorname{Frob}_\ell)^{-1} x \mid V^I_\ell)$ is the Euler factor at $\ell$.

(b) **Non-vanishing:** For $\pi = \operatorname{sym}^{n-1} f$ with $f$ a weight-2 newform attached to an elliptic curve $E$, and $\operatorname{ord}_{s=1} L(\operatorname{sym}^{n-1} f, s) = 0$:
$$\exp^*_{V_{\rho_p}}(\operatorname{loc}_p(c_1)) = \mathcal{E}(p) \cdot \frac{L(\operatorname{sym}^{n-1} f, 1)}{\Omega_f^{(n)}}$$
where $\mathcal{E}(p)$ is an explicit Euler correction factor and $\Omega_f^{(n)}$ is the $n$-th symmetric power period.

(c) **Selmer bound:** $\dim H^1_f(\mathbb{Q}, \rho_p) - \dim H^0(\mathbb{Q}, \rho_p) \leq \operatorname{ord}_{s=1} L(\pi, s)$.

## Approach Summary

For $GL(3)$, the most promising approach uses the Shimura variety for the unitary group $U(2,1)$, which is a Picard modular surface. The Hodge conjecture for certain cycles on this surface would produce classes in $H^2_{\mathcal{M}}$ whose regulators are related to $GL(3)$ $L$-values. Alternatively, the Rankin-Selberg method $GL(3) \times GL(2) \to GL(6)$ could produce Euler systems from the known $GL(2)$ system via functorial lifts, but the transfer of Euler system properties through functoriality is not understood.

A second approach uses the Eisenstein cohomology of $GL(n)$: for the Borel-Serre compactification of the locally symmetric space $\Gamma \backslash \mathcal{H}^n$ (where $\mathcal{H}^n$ is the $n$-fold product of upper half-planes), the Eisenstein classes in cohomology are related to $GL(n)$ $L$-values via the Langlands-Shahidi method. Harder (2004) proved that the Eisenstein cohomology of $GL(3)$ over a totally real field produces classes whose regulators give $L$-values of $GL(3)$ forms.

For computational verification, one can test the Bloch-Kato conjecture for $\operatorname{Sym}^2 f$ using the known $L$-values (computed via the symmetric square $L$-function in Magma) and the Selmer group (computable via Galois representations).

## Computational Example

- **$f = $ newform of 11a1**, $\operatorname{Sym}^2 f$: The symmetric square $L$-function $L(\operatorname{Sym}^2 f, s)$ has analytic conductor $\sim 11^3 = 1331$. Compute $L(\operatorname{Sym}^2 f, 1)$ and verify the Bloch-Kato conjecture for the Galois representation $\operatorname{Sym}^2 V_p(E)$ at $p = 3$.
- **$f = $ newform of 37a1**, $\operatorname{Sym}^2 f$: Rank-1 curve. $L(\operatorname{Sym}^2 f, 1) \neq 0$. Test whether the Selmer group $H^1_f(\mathbb{Q}, \operatorname{Sym}^2 V_3(E))$ is trivial, as predicted by the Bloch-Kato conjecture.
- **$f = $ newform of 27a1** (CM by $\mathbb{Q}(\sqrt{-3})$), $\operatorname{Sym}^2 f$: This decomposes as $\operatorname{Sym}^2 f = \chi \oplus \pi$ for a character $\chi$ and a $GL(2)$ form $\pi$. The Euler system should decompose accordingly.

## Obstacle Analysis

The fundamental obstruction for $GL(n)$, $n \geq 3$, is the absence of algebraic cycles on the relevant Shimura varieties that would generate the correct cohomology. For $GL(2)$, Kato's cycles come from CM points (0-cycles) on $X_0(N)$; for $GL(3)$, one needs 1-cycles (curves) on Picard modular surfaces, and no explicit family of such curves is known. The representation-theoretic approach via functoriality (inducing Euler system properties from $GL(2)$ to $GL(n)$) requires controlling the image of $H^1_f(\mathbb{Q}, V_f)$ under the functorial lift $V_f \to \operatorname{Sym}^{n-1} V_f$, which is not a map on cohomology.

## Cross-Group Connections
- **Group A (BSD Formula)**: The Selmer bound (c) is the Bloch-Kato conjecture for $GL(n)$ representations.
- **Group B-002 (Beilinson-Flach)**: The $GL(2) \times GL(2)$ BF elements are input for the Rankin-Selberg approach.
- **Group F (Iwasawa Theory)**: The main conjecture for $GL(n)$ requires new Iwasawa-theoretic techniques.

## Classification
Conjecture
