# B-001: Kato's Euler System for Modular Forms — Generalization to Rank ≥ 2

## Direction ID and Title
B-001 — Kato's Euler System for Modular Forms — Generalization to Rank ≥ 2

## Status Assessment
Kato's zeta elements $z_k^{(p)} \in H^1(\mathbb{Q}, V_p(E))$ provide an unconditional Euler system for any modular elliptic curve $E/\mathbb{Q}$, yielding the bound $\operatorname{rk}(E(\mathbb{Q})) \leq 1$ via the Iwasawa-theoretic Selmer group estimate. For analytic rank $\geq 2$, the zeta element lies in a high power of the augmentation ideal $\omega^r \subset \Lambda = \mathbb{Z}_p[[\Gamma]]$, rendering the naive Euler system bound vacuous. The direction of generalization via secondary classes (Nekovář's $p$-adic height pairings) or congruence arguments with higher-rank modular forms is partially explored but no construction achieves a non-trivial Selmer class for $r \geq 2$.

## Testable Conjecture or Lemma

**Conjecture B-001.** Let $E/\mathbb{Q}$ be a modular elliptic curve with $\operatorname{ord}_{s=1} L(E,s) = r \geq 2$ and let $p$ be a prime of good ordinary reduction with $a_p \not\equiv 1 \pmod{p}$. Define the Kolyvagin-Selmer group
$$\operatorname{Sel}_{\mathrm{KS}}(E/\mathbb{Q}) = \ker\left(H^1(\mathbb{Q}, E[p^\infty]) \to \prod_v \frac{H^1(\mathbb{Q}_v, E[p^\infty])}{E(\mathbb{Q}_v) \otimes \mathbb{Q}_p/\mathbb{Z}_p}\right).$$
Then there exists a secondary Euler system class $\kappa \in H^1_f(\mathbb{Q}, V_p(E))$ arising from the Nekovář $p$-adic height pairing on Kato's zeta elements such that:
$$\hat{h}_p(\kappa) = \left(1 - \frac{a_p}{p} + \frac{1}{p}\right)^{-1} \cdot \frac{L^{(r)}(E,1)}{r! \cdot \Omega_E} \cdot p^{-\alpha}$$
where $\alpha = v_p\left(|\operatorname{III}(E/\mathbb{Q})[p^\infty]| \cdot \prod c_v^{(p)} / |E(\mathbb{Q})_{\mathrm{tors}}|_p^2\right)$ and $\hat{h}_p$ is the Mazur-Tate $p$-adic height.

## Approach Summary

The primary approach modifies Kato's construction via the Nekovář-style extension class machinery. Starting from the zeta element $z^{(p)} \in H^1(\mathbb{Q}, V_p(E))$ which maps to zero under the Bloch-Kato logarithm when $r \geq 2$, one constructs a secondary class $\delta(z^{(p)}) \in H^1(\mathbb{Q}, V_p(E))$ using the connecting homomorphism in the exact sequence $0 \to V_p(E) \to B_{\mathrm{dR}} \otimes V_p(E) \to B_{\mathrm{dR}}/B^+_{\mathrm{dR}} \otimes V_p(E) \to 0$.

A second avenue uses congruences between $E$ and higher-rank modular forms. If $f$ is the newform attached to $E$ and $g$ is a newform with $L(g,1) = 0$ to order $r$, and if $f \equiv g \pmod{\mathfrak{p}}$ for a prime $\mathfrak{p} \mid p$ of the Hecke field, then Kato's zeta element for $g$ reduces modulo $\mathfrak{p}$ to yield information about the Selmer group of $E$. This "congruence Euler system" approach requires the vanishing of a certain congruence ideal $\mathcal{C}(f,g)$ and control of the $\mu$-invariant.

The third approach extends Kato's system to a two-variable setting over a CM field $K$, where the Iwasawa algebra becomes $\Lambda_G = \mathbb{Z}_p[[\operatorname{Gal}(K(p^\infty)/K)]]$ with $\operatorname{rank}_\Lambda G = 2$. The larger augmentation ideal allows the zeta element to carry more Selmer-theoretic information, potentially yielding a bound sharper than the cyclotomic one.

## Computational Example

Test curves with Cremona labels:
- **37a1** ($r = 1$): $E: y^2 + y = x^3 - x$, conductor 37. Kato's class $z^{(p)}$ for $p = 3$ yields $\hat{h}_3(z^{(3)}) \neq 0$ and $L'(E,1)/\Omega_E = 0.30599\ldots$ Verification: $v_3(L'(E,1)/\Omega_E) = 0$ matches $v_3(|\operatorname{III}|) = 0$.
- **5077a1** ($r = 2$): $E: y^2 + y = x^3 - 7x + 6$, conductor 5077. The curve has $\operatorname{rk}(E(\mathbb{Q})) = 3$ (analytic rank 3, verified). For $p = 2$, Kato's zeta element $z^{(2)}$ lies in $\omega^3 \cdot H^1_f$, and the secondary construction is the target.
- **389a1** ($r = 1$): $E: y^2 + y = x^3 + x^2 - 2x$, conductor 389. Test the congruence approach with $p = 5$ against weight-2 forms of level 389 with $a_5 = 0$.

## Obstacle Analysis

The fundamental obstruction is that the cyclotomic Iwasawa algebra $\Lambda = \mathbb{Z}_p[[\Gamma]]$ is a principal ideal domain, and the image of Kato's zeta element under the Perrin-Riou regulator is a single element $\mathcal{L}_p^{\mathrm{Kato}} \in \Lambda$. When $\operatorname{ord}_{s=1} L(E,s) = r$, the element $\mathcal{L}_p^{\mathrm{Kato}}$ lies in $\omega^r$, and the quotient $\Lambda / (\mathcal{L}_p^{\mathrm{Kato}})$ has length $r$ at the augmentation ideal. This provides no bound on $\operatorname{Sel}(E/\mathbb{Q})[p]$ when $r \geq 2$ because the Euler system machine only gives $\operatorname{char}(\operatorname{Sel}^\vee) \supseteq (\mathcal{L}_p)$, which is trivially satisfied when $\mathcal{L}_p \in \omega^r$. Breaking through requires either a fundamentally new Euler system (multi-variable) or a secondary construction that converts the "dead" zeta element into live Selmer classes.

## Cross-Group Connections
- **Group A (BSD Formula)**: Direct input to the $p$-part of the BSD leading-term formula via $\hat{h}_p(\kappa)$.
- **Group D (Heegner Points)**: The secondary class construction interacts with Gross-Zagier when $r = 2$ and Heegner points exist.
- **Group F (Iwasawa Theory)**: The $\mu$-invariant question for the congruence approach is an Iwasawa-theoretic problem.

## Classification
Conjecture
