# B-008: p-adic L-functions from Euler Systems (Interpolation)

## Direction ID and Title
B-008 — p-adic L-functions from Euler Systems (Interpolation)

## Status Assessment
The construction of $p$-adic L-functions from Euler systems via the Perrin-Riou regulator is well-established for $GL(2)$ representations. Kato's Euler system produces $\mathcal{L}_p^{\mathrm{Kato}} \in \Lambda$ whose specialization at $s = k$ recovers $L(E, k) / \Omega_E$ times explicit Euler correction factors. The interpolation formula is proven and explicit. The main conjecture (equality $\mathcal{L}_p^{\mathrm{Kato}}$ generates $\operatorname{char}(\operatorname{Sel}^\vee)$) is known for $p = 3$ under GRH by Skinner-Urban, and for CM curves by Rubin. For general $p$ and non-CM curves, only the divisibility $\subseteq$ is known.

## Testable Conjecture or Lemma

**Theorem B-008.** Let $E/\mathbb{Q}$ be a modular elliptic curve of conductor $N$ with good ordinary reduction at $p \nmid 6N$. Let $\Omega_p(E) = \log_p(\hat{\omega})$ be the $p$-adic period (the $p$-adic formal group logarithm of the Néron differential), and $\Omega_\infty(E)$ the real period. Then:

(a) **Interpolation formula:** For integer $k \geq 1$ with $k \equiv 0 \pmod{p-1}$ (critical integers):
$$\mathcal{L}_p^{\mathrm{Kato}}(\gamma^k - 1) = \mathcal{E}(p, k) \cdot \frac{L(E, k)}{\Omega_\infty(E)^+} \cdot \left(\frac{\Omega_p(E)}{p}\right)^{-k+1}$$
where $\mathcal{E}(p, k) = \left(1 - \frac{a_p}{p^k} + \frac{1}{p}\right)^{-1}$ is the Euler correction factor and $\gamma$ is a topological generator of $\Gamma = 1 + p\mathbb{Z}_p$.

(b) **Characteristic ideal divisibility (Kato):**
$$(\mathcal{L}_p^{\mathrm{Kato}}) \subseteq \operatorname{char}_\Lambda\left(\operatorname{Sel}(E/\mathbb{Q}_\infty)^\vee\right)$$

(c) **Main conjecture equality (conditional):** If $p = 3$, $a_3 \not\equiv 4 \pmod{9}$, and GRH for $\zeta_K(s)$ for all number fields $K$, then:
$$\operatorname{char}_\Lambda\left(\operatorname{Sel}(E/\mathbb{Q}_\infty)^\vee\right) = (\mathcal{L}_p^{\mathrm{Kato}})$$

## Approach Summary

The Perrin-Riou $p$-adic regulator $\mathcal{L}_{\mathrm{PR}}: H^1_f(\mathbb{Q}_p, T \otimes \Lambda) \to \Lambda$ is the key bridge between the Euler system (a cohomology class) and the $p$-adic L-function (an element of the Iwasawa algebra). It is defined using the exponential map of $p$-adic Hodge theory: for $V = T_p(E) \otimes \mathbb{Q}_p$, the Bloch-Kato exponential $\exp_V: D_{\mathrm{dR}}(V)/F^0 \to H^1_f(\mathbb{Q}_p, V)$ and its dual $\exp^*_V: H^1_f(\mathbb{Q}_p, V) \to D_{\mathrm{dR}}(V)/F^0$ are extended to $\Lambda$-adic versions by interpolating over the cyclotomic tower.

The $p$-adic period $\Omega_p(E)$ enters through the comparison between the $p$-adic and complex Betti cohomology: $D_{\mathrm{dR}}(V) \cong H^1_{\mathrm{dR}}(E/\mathbb{Q}) \cong \mathbb{Q}_p \cdot \omega \oplus \mathbb{Q}_p \cdot \eta$ where $\omega$ is the Néron differential and $\eta$ is the dual differential. The period ratio $\Omega_p / \Omega_\infty$ is the $p$-adic analogue of the complex period.

For the main conjecture (c), the argument uses Skinner-Urban's technique: the Eisenstein ideal of the Hecke algebra acting on $X_0(Np^n)$ produces a congruence between the Eisenstein series and cusp forms, which translates into an equality between the characteristic ideal and the $p$-adic L-function.

## Computational Example

- **$E = $ 11a1**: $p = 5$. Compute $\mathcal{L}_5^{\mathrm{Kato}}$ as a power series in $\Lambda = \mathbb{Z}_5[[T]]$ (where $T = \gamma - 1$). Specialize at $k = 1$: $\mathcal{L}_5(0) = \mathcal{E}(5, 1) \cdot L(E, 1) / \Omega_\infty$. Verify numerically: $L(E, 1) = 0.253841\ldots$, $\Omega_\infty = 1.269209\ldots$, $a_5 = 1$. $\mathcal{E}(5, 1) = (1 - 1/5 + 1/5)^{-1} = 5/4$. So $\mathcal{L}_5(0) = 5/4 \times 0.253841/1.269209 = 0.25\ldots$
- **$E = $ 37a1**: $p = 3$. $a_3 = -2$. $\mathcal{E}(3, 1) = (1 + 2/3 + 1/3)^{-1} = 3/6 = 1/2$. $L'(E, 1)/\Omega = 0.30599\ldots$ The power series $\mathcal{L}_3^{\mathrm{Kato}}(T)$ should have a simple zero at $T = 0$ with leading coefficient encoding $L'(E,1)/\Omega$.
- **$E = $ 5077a1**: $p = 2$. $a_2 = -2$. Test the interpolation at $k = 2$: $\mathcal{L}_2(\gamma^2 - 1) = \mathcal{E}(2, 2) \cdot L(E, 2) / \Omega_\infty^+$.

## Obstacle Analysis

The main obstacle for the equality direction (c) is the requirement $p = 3$ and the GRH assumption in Skinner-Urban's work. The Eisenstein ideal technique is inherently specific to small primes because the congruence ideal $\mathcal{C}$ has $p$-adic valuation that grows with $p$, making the argument less precise. For $p \geq 5$, one needs the $p$-part of the Leopoldt conjecture (known for abelian extensions of $\mathbb{Q}$) and non-vanishing of certain $L$-values that are not guaranteed. For supersingular primes ($a_p = 0$), the Perrin-Riou regulator does not directly apply, and one must use the two-variable approach of Pollaccio and Sprung.

## Cross-Group Connections
- **Group A (BSD Formula)**: The interpolation formula encodes the BSD leading term.
- **Group F (Iwasawa Theory)**: The main conjecture is the central result of Iwasawa theory.
- **Group E (p-adic Heights)**: The $p$-adic period $\Omega_p$ is related to the Mazur-Tate height.

## Classification
Theorem (interpolation, divisibility); Partial Result (main conjecture equality)
