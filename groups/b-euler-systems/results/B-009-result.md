# B-009: Rubin's Method and Selmer Group Bounds

## Direction ID and Title
B-009 — Rubin's Method and Selmer Group Bounds

## Status Assessment
Rubin's method is the general framework for converting Euler systems into Selmer group bounds. The three-step argument — define the Euler system ideal, prove the bounding inequality via the Bockstein map, deduce the Selmer rank bound — is the backbone of all Euler system applications to BSD. The method yields a sharp bound (equality $\mathcal{Z} = \operatorname{char}_\Lambda(\operatorname{Sel}^\vee)$) in the CM case and for $T = \mathbb{Z}_p(1)$. For non-CM elliptic curves, the method gives $\subseteq$ (Kato), and equality requires Galois deformation theory input (Skinner-Urban).

## Testable Conjecture or Lemma

**Theorem B-009 (Rubin).** Let $T$ be a $p$-adic representation of $G_K$ (for $K$ a number field) with an Euler system $\{c_m\}$. Define:
$$\mathcal{Z} = \operatorname{char}_\Lambda\left(\text{image of } \{c_m\} \text{ in } H^1_\Sigma(K, T \otimes \Lambda)\right)$$
Then:

(a) **Bounding inequality:** $\mathcal{Z} \subseteq \operatorname{char}_\Lambda\left(\operatorname{Sel}(T/K_\infty)^\vee\right)$.

(b) **Rank bound:** $\dim_{\mathbb{F}_p} \operatorname{Sel}(T/K)[p] \leq \operatorname{length}_\Lambda(\Lambda / \mathcal{Z})$.

(c) **Sharpness criterion:** Equality in (a) holds if and only if:
   (i) The local conditions at $v \mid p$ are geometrically defined ($H^1_f$ conditions from $p$-adic Hodge theory),
   (ii) The prime-to-$p$ Selmer conditions match the Euler system support exactly,
   (iii) The Euler system is non-degenerate: the Kolyvagin derivative classes $\kappa_\ell \in H^1(K, T/\mathfrak{m}T)$ span a subspace of dimension equal to $\operatorname{rk}_p \operatorname{Sel}(T/K)$.

(d) **Non-degeneracy for $r = 0$:** If $\operatorname{ord}_{s=1} L(T, s) = 0$, the non-degeneracy condition is automatic: $c_1 \neq 0$ in $H^1_f$ implies $\mathcal{Z} \not\subseteq \omega \cdot \Lambda$, hence $\operatorname{Sel}(T/K)[p] = 0$.

## Approach Summary

The Bockstein homomorphism $\beta: H^1_\Sigma(K, T/p) \to H^2_\Sigma(K, T)[p]$ arising from the short exact sequence $0 \to T \xrightarrow{p} T \to T/p \to 0$ is the key technical tool. The Euler system classes $c_m$ map to elements in $H^1_\Sigma(K(m), T/p)$ via reduction mod $p$, and the Bockstein measures the obstruction to lifting these to $H^1_\Sigma(K(m), T)$. The global duality pairing $\langle \cdot, \cdot \rangle: H^1_\Sigma(K, T/p) \times H^1_\Sigma(K, T^*(1)/p) \to \mathbb{F}_p$ identifies the image of the Bockstein with the Pontryagin dual of $\operatorname{Sel}(T^*(1)/K)[p]$, yielding the bound.

For sharpness (equality), one needs the "control theorem": the specialization map $\operatorname{Sel}(T/K_\infty) \to \operatorname{Sel}(T/K)$ should be surjective (or at least have controlled kernel and cokernel). This is guaranteed by the Greenberg-type condition: $H^0(\mathbb{Q}_v, V/T) = 0$ for all $v \mid p$, which holds when $T = T_p(E)$ with $E$ having good ordinary reduction at $p$ and $a_p \not\equiv 1 \pmod{p}$.

The non-degeneracy condition (iii) is the hardest to verify in practice. For $r = 0$, it is automatic because $c_1 \neq 0$. For $r = 1$, it follows from the Gross-Zagier formula: the existence of a Heegner point of infinite order guarantees that the Kolyvagin derivative at one prime $\ell$ is non-zero in $H^1(K, E[p])$. For $r \geq 2$, non-degeneracy is completely open.

## Computational Example

- **$T = T_p(E)$, $E = $ 11a1, $p = 5$**: The Euler system ideal $\mathcal{Z} = (\mathcal{L}_5^{\mathrm{Kato}}) \subset \Lambda$. Since $L(E,1) \neq 0$, $\mathcal{L}_5^{\mathrm{Kato}}$ is a unit in $\Lambda / \omega$, so $\operatorname{Sel}(E/\mathbb{Q})[5] = 0$. Verify: $\operatorname{III}(E/\mathbb{Q}) = 0$, $E(\mathbb{Q})[5] = 0$, confirming $\operatorname{Sel} = 0$.
- **$T = T_p(E)$, $E = $ 37a1, $p = 3$**: $\mathcal{L}_3^{\mathrm{Kato}}$ has a simple zero at the augmentation ideal. The bounding inequality gives $\operatorname{Sel}[3] \leq 1$. Verify: $P = (0, 0) \in E(\mathbb{Q})$ has infinite order, so $\operatorname{Sel}[3] = 1$. The sharpness criterion is satisfied by the Gross-Zagier non-degeneracy.
- **$T = \mathbb{Z}_3(1)$, $K = \mathbb{Q}$**: The cyclotomic units $\{c_m = 1 - \zeta_m\}$ form the Euler system. $\mathcal{Z} = (L_3^{\mathrm{Kubota-Leopoldt}})$. Rubin's method gives the classical Iwasawa main conjecture for $\mathbb{Q}$: $\operatorname{char}(\operatorname{Sel}^\vee) = (L_3)$.

## Obstacle Analysis

The gap between $\subseteq$ and $=$ for non-CM curves at general primes $p$ is the central unsolved problem. The control theorem requires the surjectivity of $\operatorname{Sel}(T/K_\infty) \to \operatorname{Sel}(T/K)$, which can fail when the $\mu$-invariant is positive or when $H^0(\mathbb{Q}_p, V/T) \neq 0$. For supersingular primes, the Selmer conditions must be modified (Kobayashi's $\pm$-conditions), and the Rubin method applies separately to each $\pm$-component, with weaker conclusions. The non-degeneracy condition for $r \geq 2$ remains the most significant open problem.

## Cross-Group Connections
- **Group A (BSD Formula)**: Rubin's method is the mechanism that converts Euler systems into BSD.
- **Group B-007 (BSD via bounds)**: The specific inequality and equality results.
- **Group F (Iwasawa Theory)**: The characteristic ideal equality is the Iwasawa main conjecture.

## Classification
Theorem (bounding inequality and CM sharpness); Partial Result (non-CM sharpness)
