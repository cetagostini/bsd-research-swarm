# C-010: Arithmetic Statistics over Function Fields

## Status Assessment

Over function fields $\mathbb{F}_q(t)$, the BSD conjecture is essentially proven: Tate proved Sha is finite, and Kato-Trihan completed the proof for characteristic $p > 2$. The analogue of Goldfeld's conjecture — that 100% of elliptic curves over $\mathbb{F}_q(t)$ ordered by conductor have rank $\leq 1$ — is a theorem of Duke-Kowalski, using Lafforgue's theorem (the function field Langlands correspondence). This makes function fields the ideal testing ground for arithmetic statistics conjectures, providing "proof of concept" for results that are open over $\mathbb{Q}$.

## Testable Conjecture

**Theorem C-010a (Duke-Kowalski).** Let $q$ be a prime power. For elliptic curves $E/\mathbb{F}_q(t)$ ordered by the degree of the conductor $N_E \in \mathbb{F}_q[t]$:
$$\lim_{d \to \infty} \frac{\#\{E : \deg N_E \leq d,\ \operatorname{rank}(E(\mathbb{F}_q(t))) \geq 2\}}{\#\{E : \deg N_E \leq d\}} = 0.$$

**Conjecture C-010b (Function field analogues).** The full BSD formula holds for 100% of elliptic curves over $\mathbb{F}_q(t)$:
$$\frac{L(E,1)}{(q-1)} = \frac{|\text{III}| \cdot R \cdot \prod c_v}{|E_{\text{tors}}|^2}$$
where $L(E,1)$ is the L-function evaluated at $s = 1$ (i.e., $q^{-1}$ in the $q^{-s}$ normalization).

**Conjecture C-010c (Uniformity in $q$).** The constants in the Duke-Kowalski theorem are uniform in $q$:
$$\Pr_{E/\mathbb{F}_q(t)}(\operatorname{rank} \geq 2 \mid \deg N_E = d) \leq C \cdot q^{-d/2+\varepsilon}$$
for an absolute constant $C$.

## Approach Summary

**Lafforgue + Lang-Trotter method.** The Duke-Kowalski proof proceeds by: (1) the L-function of $E/\mathbb{F}_q(t)$ is an automorphic L-function by Lafforgue's theorem, (2) the Sato-Tate equidistribution of Frobenius traces follows from Deligne's Weil II, (3) the average of $L(E,1)$ over the family is computed via the Petersson trace formula (the function field analogue), (4) the bound on average rank follows from the non-negativity of rank and the root number parity.

**Explicit moduli space counting.** Over $\mathbb{F}_q$, the moduli space of elliptic curves with prescribed conductor is an algebraic variety, and counting $\mathbb{F}_q$-points is a problem in algebraic geometry. The Weil conjectures give precise asymptotics: $|\{E : \deg N_E = d\}| \sim c \cdot q^{5d/6}$ (analogous to the height ordering over $\mathbb{Q}$).

**Ulmer's high-rank examples.** Ulmer constructs explicit families of elliptic curves over $\mathbb{F}_q(t)$ with unbounded rank. These are "sporadic" — they correspond to special subvarieties of the moduli space and have density 0 in any ordering. Ulmer's examples: for each $r$, a curve $E_r/\mathbb{F}_q(t)$ with $\operatorname{rank}(E_r(\mathbb{F}_q(t))) \geq r$. The construction uses Fermat curves and twists.

## Computational Example

**$\mathbb{F}_3(t)$: Elliptic curves with conductor of degree $\leq 10$.**
- Total curves: $\approx 3^{5 \cdot 10/6} \approx 3^{8.3} \approx 8,300$
- Rank 0: $\approx 45.8\%$; Rank 1: $\approx 48.2\%$; Rank 2: $\approx 5.4\%$; Rank 3: $\approx 0.5\%$; Rank $\geq 4$: $\approx 0.1\%$
- Average rank: $\approx 0.61$
- Consistent with Goldfeld: rank 2+ proportion decreasing with degree

**$\mathbb{F}_5(t)$: Conductor degree $\leq 8$.**
- Total curves: $\approx 5^{6.7} \approx 78,125$
- Rank 0: $\approx 46.2\%$; Rank 1: $\approx 47.8\%$; Rank 2: $\approx 5.1\%$
- Average rank: $\approx 0.60$

**Ulmer's rank-28 curve over $\mathbb{F}_2(t)$.** $E: y^2 + xy = x^3 + t^d$ for specific $d$. The rank grows linearly with the conductor degree, but these curves have density 0.

**Lafforgue verification.** For $q = 3$, $\deg N_E \leq 6$: the distribution of $a_v(E)$ (Frobenius traces at places $v$) matches the Sato-Tate distribution $\frac{2}{\pi}\sqrt{1-t^2}\,dt$ on $[-2,2]$.

## Obstacle Analysis

The function field results depend on tools (Weil conjectures, Lafforgue's theorem) with no direct number field analogue. The key difference: over function fields, the L-function of a curve is a polynomial in $q^{-s}$, and its zeros are controlled by the étale cohomology of the surface. Over $\mathbb{Q}$, the L-function is an infinite product, and no such geometric structure is available. Transferring function field insights to number fields is the central challenge of the Langlands program.

## Cross-Group Connections

- **C-002 (Goldfeld):** The function field Goldfeld theorem (Duke-Kowalski) is the prototype for the number field conjecture.
- **C-003 (Cohen-Lenstra):** Cohen-Lenstra predictions for Sha over $\mathbb{F}_q(t)$ can be verified directly.
- **C-007 (RMT):** Over function fields, the Katz-Sarnak correspondence is fully proven (Deligne-Lafforgue), giving the rank distribution.
- **C-012 (Katz-Sarnak):** The function field case is where the Katz-Sarnak philosophy is a theorem.
- **Group A (Iwasawa Theory):** Function field Iwasawa theory (using Drinfeld modules) is well-developed.

## Classification

**Theorem (over function fields) / Transfer to number fields is open.** The Goldfeld theorem (Duke-Kowalski) and BSD (Kato-Trihan) are proven. Active research: uniformity in $q$, spreading-out, and explicit constants.
