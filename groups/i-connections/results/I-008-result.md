# I-008: Parity Conjecture (Root Number = Sign of Functional Equation)

## Direction ID and Title
**I-008** — Parity Conjecture (Root Number = Sign of Functional Equation)

## Status Assessment
The parity conjecture is the weakest consequence of BSD. It is proven conditionally (assuming $\Sha$ is finite) by Nekovar (2006) and Dokchitser-Dokchitser (2010). Unconditionally, it is known for curves with at least one prime of multiplicative reduction (Nekovar) and for curves with potentially good reduction at all odd primes (Dokchitser-Dokchitser). The Gross-Zagier-Kolyvagin theorem implies it for rank $\leq 1$. Open in full generality.

## Testable Conjecture or Lemma

**Conjecture (Parity Conjecture).** For every elliptic curve $E/\mathbb{Q}$:
$$w_E = (-1)^{\operatorname{rank} E(\mathbb{Q})},$$
where $w_E \in \{+1, -1\}$ is the root number (sign of the functional equation).

**Lemma (BSD Implies Parity).** BSD for $E$ implies the parity conjecture for $E$.

*Proof sketch:* BSD gives $\operatorname{ord}_{s=1} L(E, s) = \operatorname{rank} E(\mathbb{Q})$. The functional equation gives $\Lambda(E, s) = w_E \cdot \Lambda(E, 2-s)$, so $\operatorname{ord}_{s=1} L(E, s)$ has the same parity as the order of vanishing at $s = 1$, which is even if $w_E = +1$ and odd if $w_E = -1$. Hence $w_E = (-1)^{\operatorname{rank} E(\mathbb{Q})}$. $\square$

**Lemma (Parity from Cassels-Tate).** Assume $\Sha(E)$ is finite. Then the Cassels-Tate pairing on $\Sha(E)[p^\infty]$ is a non-degenerate alternating form, so $|\Sha(E)[p^\infty]| = p^{2k}$. Combined with the exact sequence relating $\operatorname{Sel}_{p^\infty}(E)$ to $E(\mathbb{Q})/p^n$ and $\Sha(E)[p^n]$, this gives:
$$(-1)^{\operatorname{rank} E(\mathbb{Q})} = w_E.$$

## Approach Summary
1. **Root number computation:** The global root number $w_E = \prod_v w_{E,v}$ is a product of local root numbers. At good primes, $w_{E,p} = +1$. At bad primes, $w_{E,p}$ depends on the reduction type. The archimedean root number is $w_{E,\infty} = -1$.
2. **Gross-Zagier-Kolyvagin (rank $\leq 1$):** If $w_E = -1$, then $\operatorname{ord}_{s=1} L(E, s) \geq 1$ (odd). Heegner point methods (Gross-Zagier) produce a point of infinite order, confirming $\operatorname{rank} \geq 1$. If $w_E = +1$, Kolyvagin shows $\operatorname{rank} = 0$ (assuming $\Sha$ finite).
3. **Cassels-Tate pairing:** For the unconditional case, the key is to show that the parity of $\dim_{\mathbb{F}_p} \operatorname{Sel}_p(E)$ matches $w_E$ without assuming $\Sha$ finite. This requires new methods beyond the Cassels-Tate pairing.
4. **Dokchitser-Dokchitser method:** Use the parity of the $p$-Selmer group over the minimal field where $E$ has semistable reduction, then descend to $\mathbb{Q}$.

## Computational Example

**Example 1: $E: y^2 = x^3 - x$ (conductor 32).**
- $w_E = +1$ (even root number). $\operatorname{rank} E(\mathbb{Q}) = 0$. Parity: $(-1)^0 = +1 = w_E$. ✓

**Example 2: $E: y^2 + y = x^3 - x^2 - 10x - 20$ (conductor 11).**
- $w_E = +1$. $\operatorname{rank} = 0$. ✓

**Example 3: $E: y^2 = x^3 - x^2 - 77x + 330$ (conductor 49, rank 1).**
- $w_E = -1$. $\operatorname{rank} = 1$. $(-1)^1 = -1 = w_E$. ✓

**Example 4: Curve with $w_E = -1$ and $\operatorname{rank} = 1$ (known by Gross-Zagier).**
- For any $E$ with $w_E = -1$, the analytic rank is $\geq 1$ (odd). Gross-Zagier-Kolyvagin confirms $\operatorname{rank} = 1$ (assuming $\Sha$ finite). This is the "easy" direction of the parity conjecture.

**Example 5: Curve with $w_E = +1$ and $\operatorname{rank} = 0$ (known by Kolyvagin).**
- For any $E$ with $w_E = +1$ and $L(E, 1) \neq 0$, Kolyvagin shows $\operatorname{rank} = 0$. The "hard" direction is showing $\operatorname{rank} = 0$ when $w_E = +1$ but $L(E, 1) = 0$ (analytic rank $\geq 2$).

## Obstacle Analysis
1. **Unconditional parity is open:** The Cassels-Tate pairing argument requires $\Sha$ to be finite. Without this, the parity of the Selmer group is not determined by the root number.
2. **High rank:** For curves with $w_E = +1$ and potentially large rank (e.g., $L(E, 1) = L'(E, 1) = 0$), the parity conjecture says the rank is even, but proving this requires controlling $\Sha$.
3. **No Euler system for $w_E = +1$:** When $w_E = +1$, there is no Heegner point of infinite order. The parity conjecture for this case requires a different source of arithmetic information.

## Cross-Group Connections
- **I-004 (Sato-Tate):** The root number distribution in families is a coarser version of Sato-Tate; both constrain the parity of the analytic rank.
- **I-009 (Greenberg's Conjecture):** The $\mu$-invariant is the "$p$-adic shadow" of the parity conjecture.
- **I-010 (Fontaine-Mazur):** Fontaine-Mazur for the Selmer group would imply that every element of $\Sha[p^\infty]$ is motivic, which would give parity unconditionally.
- **Group C (Root Numbers):** Computing $w_E$ for individual curves and families is the analytic input.

## Classification
**Weakest consequence of BSD.** The parity conjecture is the minimal arithmetic content of BSD. Proving it unconditionally would be a major breakthrough, confirming the "easy" part of the rank prediction without assuming the full conjecture.
