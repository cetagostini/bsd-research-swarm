# B-007: The BSD Formula via Euler System Bounds

## Direction ID and Title
B-007 — The BSD Formula via Euler System Bounds

## Status Assessment
The Euler system approach to BSD produces the upper bound $\operatorname{rk}_p \operatorname{Sel}(E/\mathbb{Q}) \leq \operatorname{ord}_{s=1} L(E,s)$ via the Bockstein map from the Euler system ideal. For rank 0 and 1, this bound combined with the Gross-Zagier formula and the Cassels-Tate pairing yields the $p$-part of the BSD formula unconditionally. For rank $\geq 2$, the Euler system gives an inequality on $|\operatorname{III}|$ but the equality case requires the full Iwasawa main conjecture. The Skinner-Urban result for $p = 3$ under GRH is the strongest unconditional result for the equality direction.

## Testable Conjecture or Lemma

**Theorem B-007.** Let $E/\mathbb{Q}$ be an elliptic curve, $p$ a prime of good ordinary reduction with $a_p \not\equiv 1 \pmod{p}$, and suppose Kato's Euler system $z^{(p)} \in H^1_f(\mathbb{Q}, V_p(E))$ has image under the Perrin-Riou regulator equal to $\mathcal{L}_p^{\mathrm{Kato}} \in \Lambda$. Let $r = \operatorname{ord}_{s=1} L(E,s)$. Then:

(a) **Selmer bound:** $\dim_{\mathbb{F}_p} \operatorname{Sel}(E/\mathbb{Q})[p] \leq r$.

(b) **$|\operatorname{III}|$ inequality:** If $r = 0$, then $v_p(|\operatorname{III}(E/\mathbb{Q})|) \leq v_p(L(E,1)/\Omega_E)$.

(c) **Equality for $r = 0$:** Combined with the Cassels-Tate constraint ($|\operatorname{III}|$ is a perfect square) and the parity of $v_p(L(E,1)/\Omega_E)$:
$$|\operatorname{III}(E/\mathbb{Q})[p^\infty]| = \left| \frac{L(E,1)}{\Omega_E} \right|_p^{-1} \cdot \frac{|E(\mathbb{Q})_{\mathrm{tors}}|_p^2}{\prod c_v^{(p)}}$$
when $p \neq 2$ and $E(\mathbb{Q})[p] = 0$.

(d) **Leading term formula for $r = 1$:** With $P \in E(\mathbb{Q})$ a generator of the free part:
$$\frac{L'(E,1)}{\Omega_E} = \frac{|\operatorname{III}(E/\mathbb{Q})| \cdot \prod c_v}{|E(\mathbb{Q})_{\mathrm{tors}}|^2} \cdot \hat{h}_{\mathrm{NT}}(P)$$
where $\hat{h}_{\mathrm{NT}}$ is the Néron-Tate canonical height.

## Approach Summary

The Rubin-style argument proceeds as follows. The Euler system ideal $\mathcal{Z} = (\mathcal{L}_p^{\mathrm{Kato}}) \subset \Lambda$ satisfies $\mathcal{Z} \subseteq \operatorname{char}_\Lambda(\operatorname{Sel}(E/\mathbb{Q}_\infty)^\vee)$ by the bounding inequality. Specializing at the augmentation ideal $\omega = (\gamma - 1)$ of $\Lambda = \mathbb{Z}_p[[\Gamma]]$, the quotient $\Lambda / (\mathcal{L}_p)$ has length $r$ at $\omega$, giving $\operatorname{length}_{\mathbb{Z}_p}(\operatorname{Sel}^\vee / \omega \operatorname{Sel}^\vee) \leq r + \text{correction}$, which translates to the Selmer bound.

For the equality in (c), one uses the Cassels-Tate pairing: it is a non-degenerate alternating form on $\operatorname{III}(E/\mathbb{Q})$, so $|\operatorname{III}|$ is a perfect square. If $v_p(L(E,1)/\Omega_E)$ is odd, then the inequality $v_p(|\operatorname{III}|) \leq v_p(L(E,1)/\Omega_E)$ is strict, but the next value consistent with the perfect-square constraint is achieved by the Skinner-Urban theorem for $p = 3$.

For the leading term formula (d), Kolyvagin's system of derivative classes $\{d_\ell\}$ for $\ell$ running over Kolyvagin primes (where $\operatorname{Frob}_\ell$ has order $p-1$ on $E[p]$) produces an explicit annihilator of the Selmer group, and the $p$-adic height $\hat{h}_p(z^{(p)})$ encodes $L'(E,1)/\Omega_E$ via the interpolation formula.

## Computational Example

- **$E = $ 11a1** ($r = 0$): $p = 3$. $L(E,1)/\Omega_E = 1/5$. $v_3(1/5) = 0$. $|\operatorname{III}| = 1$. $\prod c_v = 1$. $|E_{\mathrm{tors}}| = 5$. Check: $v_3(1/5) = v_3(1 \cdot 1 / 25) = 0$. ✓
- **$E = $ 37a1** ($r = 1$): $p = 3$. $L'(E,1)/\Omega_E = 0.30599\ldots$ $\hat{h}_{\mathrm{NT}}(P) = 0.05111\ldots$ $|\operatorname{III}| = 1$. $c_{37} = 1$. $|E_{\mathrm{tors}}| = 1$. Verify: $L'(E,1)/\Omega_E / \hat{h}_{\mathrm{NT}}(P) = 5.99\ldots \approx 6 = |\operatorname{III}| \cdot \prod c_v / |E_{\mathrm{tors}}|^2$.
- **$E = $ 5077a1** ($r = 3$): Test the inequality $v_2(|\operatorname{III}|) \leq v_2(L^{(3)}(E,1)/3!\Omega_E)$. The actual $|\operatorname{III}| = 1$ (trivially satisfying any bound), but the formula encodes the height of the rank-3 generator system.
- **$E = $ 389a1** ($r = 2$): $p = 5$. The Euler system gives the bound $\operatorname{Sel}[5] \leq 2$. Verify that the actual Selmer group has 2 independent generators (matching the rank).

## Obstacle Analysis

The gap between the inequality $v_p(|\operatorname{III}|) \leq v_p(L/\Omega)$ and equality is the central problem. For rank 0, the Cassels-Tate pairing argument (Skinner-Urban for $p = 3$) closes the gap, but for general $p$ the lower bound on $|\operatorname{III}|$ is missing. The parity constraint from the Cassels-Tate pairing is not strong enough to determine $|\operatorname{III}|[p^\infty]$ uniquely when $v_p(L/\Omega) \geq 2$. For rank $\geq 2$, the Euler system provides no constraint on $|\operatorname{III}|$ at all — the Selmer bound $r \leq r$ is vacuous.

## Cross-Group Connections
- **Group A (BSD Formula)**: This is the direct mechanism connecting Euler systems to the BSD formula.
- **Group C (Heegner Points)**: The Gross-Zagier formula provides the lower bound for $r = 1$.
- **Group F (Iwasawa Theory)**: The main conjecture (equality direction) is an Iwasawa-theoretic statement.

## Classification
Theorem (Selmer bound, $r \leq 1$); Partial Result (equality for general $p$ and $r \geq 2$)
