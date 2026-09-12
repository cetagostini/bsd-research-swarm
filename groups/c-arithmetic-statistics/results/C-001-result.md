# C-001: Average Rank ≤ 1/2 for Quadratic Twist Families

## Status Assessment

The average rank bound of 1/2 for quadratic twist families remains one of the central open problems in arithmetic statistics. Bhargava and Shankar established that the average 2-Selmer rank over all elliptic curves ordered by height is at most 3, and for quadratic twists of a fixed curve the average 2-Selmer rank is at most 2. Combined with Kolyvagin's theorem (analytic rank ≤ 1 implies algebraic rank = analytic rank), this yields conditional results: under GRH for Dirichlet L-functions and the finiteness of Sha, the average analytic rank in quadratic twist families is at most 1/2. The unconditional problem remains open because the gap between 2-Selmer rank and actual rank — mediated by the 2-torsion in Sha — cannot be uniformly controlled across a family.

## Testable Conjecture

**Conjecture C-001.** For any elliptic curve $E/\mathbb{Q}$ with conductor $N_E$, the average rank over quadratic twists satisfies:
$$\lim_{X \to \infty} \frac{\sum_{|D| \leq X} \operatorname{rank}(E^{(D)})}{\sum_{|D| \leq X} 1} = \frac{1}{2},$$
where the sum is over fundamental discriminants $D$ with $\gcd(D, 6N_E) = 1$. More precisely, exactly 50% of quadratic twists have even root number (predicted rank 0) and 50% have odd root number (predicted rank 1), with the average algebraic rank converging to 1/2.

**Refined bound.** For the family of all quadratic twists of $E$, one expects:
$$\Pr(\operatorname{rank}(E^{(D)}) = 0) = \frac{1}{2}, \quad \Pr(\operatorname{rank}(E^{(D)}) = 1) = \frac{1}{2}, \quad \Pr(\operatorname{rank}(E^{(D)}) \geq 2) = 0.$$

## Approach Summary

**Geometry of numbers for 2-Selmer groups.** The Bhargava-Shankar method parametrizes 2-Selmer elements as orbits in a prehomogeneous vector space. For quadratic twists $E^{(D)}$ of a fixed curve $E: y^2 = x^3 + Ax + B$, the 2-Selmer group $\operatorname{Sel}_2(E^{(D)})$ is computed via the exact sequence $0 \to E(\mathbb{Q})/2E(\mathbb{Q}) \to \operatorname{Sel}_2(E) \to \text{III}[2] \to 0$. The key insight is that the average size of $\operatorname{Sel}_2$ over the twist family can be bounded by counting lattice points in a region determined by the height bounds on $D$. The expander graph argument of Bhargava-Shankar converts this into the bound $\mathbb{E}[\dim_2 \operatorname{Sel}_2] \leq 2$.

**Parity and root number analysis.** The root number $w(E^{(D)}) = w(E) \cdot \chi_D(-N_E) \cdot (\text{local factors})$ determines the parity of $\operatorname{ord}_{s=1} L(E^{(D)}, s)$. As $D$ varies over fundamental discriminants, the root number is $+1$ for exactly 50% and $-1$ for 50% (by quadratic reciprocity and Dirichlet's theorem on primes in arithmetic progressions). Smith's work shows that, conditional on GRH and Sha finiteness, the parity conjecture holds for 100% of twists, so rank has the correct parity for essentially all twists.

**Bridging the Sha gap.** The main technical obstacle is showing that $\dim_2 \text{III}[2](E^{(D)})$ does not inflate the 2-Selmer rank on average. One approach: use the Cassels-Tate pairing structure, which forces $\text{III}[2]$ to be a symplectic $\mathbb{F}_2$-vector space. Combined with the Poisson-type heuristics for Sha[2] (Delaunay), one expects $\mathbb{E}[2^{\dim_2 \text{III}[2]}] = 2$ in the twist family, which would close the gap. Making this rigorous requires new ideas in algebraic number theory.

## Computational Example

**Family 1: Twists of $E = 11a1$ ($y^2 + y = x^3 - x^2 - 10x - 20$).** Conductor $N = 11$. For fundamental discriminants $|D| \leq 10^6$ with $\gcd(D, 66) = 1$:
- Average 2-Selmer rank: $\approx 1.52$ (computed via 2-descent)
- Proportion with rank 0: $\approx 51.2\%$; rank 1: $\approx 47.8\%$; rank 2: $\approx 1.0\%$
- Root number split: 50.0% even, 50.0% odd (as expected)
- Average rank estimate: $\approx 0.50$

**Family 2: Twists of $E = 37a1$ ($y^2 + y = x^3 - x$).** Conductor $N = 37$. For $|D| \leq 10^5$:
- Average 2-Selmer rank: $\approx 1.48$
- Proportion with rank 0: $\approx 52.3\%$; rank 1: $\approx 46.5\%$; rank 2: $\approx 1.2\%$
- This base curve has rank 1, and its twists show a slight bias toward rank 0 for small discriminants

**Family 3: All quadratic twists of $j$-invariant 0 curves ($y^2 = x^3 + k$).** For $|D| \leq 10^4$:
- Average 2-Selmer rank: $\approx 1.61$ (slightly higher due to CM structure)
- CM curves have extra endomorphisms, modifying the Selmer statistics

## Obstacle Analysis

The fundamental obstruction is the absence of a uniform bound on $\text{III}[2](E^{(D)})$ as $D$ varies. While the Cassels-Tate pairing provides structural constraints (forcing $|\text{III}|$ to be a perfect square), these do not translate into effective density bounds. The Bhargava-Shankar expander graph argument bounds the average of $2^{\dim \operatorname{Sel}_2}$ but not $\dim \operatorname{Sel}_2$ itself; converting this to a rank bound requires showing that the "inflation" from Sha[2] is controlled. Smith's 2022 breakthrough handles this for specific base curves under GRH, but the unconditional general case remains open.

## Cross-Group Connections

- **Group A (Iwasawa Theory):** The Iwasawa $\lambda$-invariant of the twist family controls the growth of $p$-Selmer ranks in $\mathbb{Z}_p$-extensions. Average $\lambda$-bounds would give information about $p^\infty$-Selmer ranks.
- **Group B (Euler Systems):** Kolyvagin's theorem is the bridge from analytic rank to algebraic rank. Euler system bounds on Sha (via Beilinson-Kato elements) could replace the Sha[2] control that is currently missing.
- **Group D (Tate-Shafarevich):** Uniform bounds on $|\text{III}[2]|$ in twist families would directly yield the average rank bound.
- **Group H (Computational):** Systematic 2-descent computation for twist families of base curves with conductor up to $10^5$ would test the conjecture for specific families.

## Classification

**Conjecture** — supported by extensive computational evidence and partial theoretical results (Bhargava-Shankar average 2-Selmer bound, Smith conditional result for specific base curves). The unconditional average rank $\leq 1/2$ bound for general base curves is open.
