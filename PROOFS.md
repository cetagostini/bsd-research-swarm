# Analysis of a_p Bias and BSD: Heuristics, Conditional Results, and Corrections

## Author: BSD Research Swarm
## Date: 2026-09-13 (corrected from 2026-09-12)
## Status: Honest assessment of what is proven, conditional, and speculative

---

## Preamble: What Went Wrong

The previous version of this document labelled four claims as "Theorems." None of them were theorems. This corrected version reclassifies each claim according to its actual logical status and adds a section stating what is genuinely correct.

---

## Heuristic 1: a_p Bias and Analytic Rank (formerly "Theorem 1")

### Status: HEURISTIC — not a theorem, not diagnostic

### Claim

For E/Q with analytic rank r, the partial sum

$$S_E(X) = \sum_{\substack{p \leq X \\ p \nmid N}} \frac{a_p(E)}{p}$$

satisfies

$$S_E(X) = -r \cdot \log\log X + c_E + o(1)$$

as X → ∞.

### Why This Is Only a Heuristic

The derivation appeals to the explicit formula and a Tauberian argument. The critical problem is the error term. Here is what is actually true:

**What the explicit formula gives.** From the Euler product, for Re(s) > 1:

$$\frac{L'(E,s)}{L(E,s)} = -\sum_p \frac{a_p \log p}{p^s} + O(1)$$

Near s = 1, if L(E,s) has a zero of order r at s = 1, the logarithmic derivative has a pole of residue r at s = 1. Via partial summation and contour integration, one gets:

$$\sum_{p \leq X} \frac{a_p}{p} = -r \log\log X + c_E + E(X)$$

**The problem: E(X) is not o(1).** The error term E(X) receives contributions from every non-trivial zero ρ = 1/2 + iγ of L(E,s):

$$E(X) \sim -\sum_{\gamma} \frac{X^{\rho - 1}}{(\rho - 1)\log X} + \ldots$$

Each term X^{ρ-1}/(ρ-1) has magnitude ~ X^{-1/2}/|γ|, which is individually small. But there are ~T log T zeros with |γ| ≤ T, and their sum is not convergent. The partial sums of this oscillatory series are of order O(1) — the same scale as the main term constant c_E. Worse, without GRH, some zeros could have Re(ρ) > 1/2, making individual terms much larger.

**The consequence.** The "o(1)" in the formula is not justified. The actual error is O(1) and oscillates. For any finite X, one cannot reliably distinguish r = 0 from r = 1 from r = 2 based on S_E(X), because the O(1) oscillation from non-trivial zeros is the same size as the differences between these cases for computationally accessible X.

The explicit formula is a precise identity. The heuristic step is the claim that the oscillatory error averages away. This is plausible but unproven, and the computational data does not resolve it because the number of primes used (300) is far too small relative to the height of the zeros contributing to the error.

### What the Computation Actually Shows

Our S_E(X) values at X ~ 300 primes are consistent with the heuristic, but "consistent with" is not evidence for. The values are also consistent with many other explanations. The computation cannot distinguish rank 0 from rank 1 from rank 2 because the signal (-r · log log 300 ≈ -r · 5.5) is swamped by the unknown O(1) constant c_E and the oscillatory error.

---

## Conditional Conjecture 2: L-value Lower Bound (formerly "Theorem 2")

### Status: CONDITIONAL on GRH — not a theorem over Q

### Claim (conditional on GRH for L(E,s))

For E/Q with analytic rank 0 and conductor N:

$$|L(E,1)| \geq \frac{c}{N^{1/2+\varepsilon}}$$

for some c > 0 and all ε > 0.

### What Is Actually Known

- **Unconditionally**, the best lower bound on |L(E,1)| for rank 0 curves is of the form 1/exp(c√log N), coming from the Burgess bound on character sums. This is far weaker than N^{-1/2-ε}.
- **Conditionally on GRH**, the mollifier method (following Soundararajan, Iwaniec-Sarnak) does give bounds of the shape N^{-1/2-ε}. The argument uses the approximate functional equation, a mollifier of length N^θ with θ < 1/2, and GRH to control the error terms in the mollifier moment calculation.
- The exponent 1/2 + ε is expected to be non-optimal. The Lindelöf hypothesis for L(E,s) would give |L(E,1)| ≫ N^{-ε} for any ε > 0.

### Why "Theorem" Was Wrong

GRH is an open conjecture. A result conditional on GRH is a conditional result, not a theorem. The original document did state "assuming GRH" but labelled it "Theorem" without qualification, which is misleading.

---

## Speculation 3: Discriminant Factorization and Rank (formerly "Theorem 3")

### Status: SPECULATION — no known mechanism, small sample

### Claim

Curves with small |L(E,1)| (presumed rank ≥ 2) tend to have discriminants with many distinct prime factors.

### Assessment

- The observation is drawn from 10,196 curves, which is a tiny sample.
- There is **no known mechanism** connecting ω(disc(E)) to rank. The discriminant is Δ = -16(4a³ + 27b²); its factorization depends on the arithmetic of the polynomial x³ + ax + b, not obviously on the analytic properties of L(E,s).
- The suggestion that the abc conjecture is relevant is hand-waving. The abc conjecture bounds radical(abc) in terms of c; it does not connect factorization patterns to rank.
- The Cohen-Lenstra heuristics, which are the standard probabilistic model for ranks of elliptic curves, predict no such correlation.
- The observed correlation in a small sample could easily be an artifact of the way curves were selected or a consequence of the specific range of (a, b) values.

### Verdict

This is a conjecture without supporting theory. It may be worth investigating computationally with a much larger sample, but it should not be cited as a result.

---

## Retraction 4: Parity Detection via a_p Sums (formerly "Theorem 4")

### Status: RETRACTED — the original claim was false

### The Original Claim

$$\lim_{X \to \infty} \frac{S_E(X)}{\log\log X} = -r$$

and therefore the parity of r is detectable from S_E.

### Why This Is Wrong

Even granting the heuristic formula S_E(X) ≈ -r · log log X + c_E + O(1), we get:

$$\frac{S_E(X)}{\log\log X} \to -r$$

for **every** r, whether r is even or odd. The limit is always negative (for r > 0). The sign does not distinguish parity. The original "proof" acknowledged this ("the sign alone doesn't distinguish parity") but then claimed parity was detectable from the "rate of convergence." This is meaningless: the formula has the same shape for all r, and the O(1) error term makes any convergence-rate argument vacuous.

**The original document was internally contradictory**: it stated both that S_E/log log X → -r for all r and that parity was detectable. These are incompatible.

### Retraction

Theorem 4 is retracted in full. There is no known way to detect the parity of the analytic rank from S_E(X) without already knowing r.

---

## What Is Actually Correct

The following are mathematically established facts. None of them are original to this project.

### Fact 1: Galois invariants of the p-torsion

For an elliptic curve E/Q and a prime p, there is a canonical isomorphism:

$$E[p]^{G_{\mathbb{Q}}} \cong E(\mathbb{Q})[p]$$

where G_Q = Gal(Q̄/Q) is the absolute Galois group. This is standard: E[p]^{G_Q} consists of p-torsion points fixed by all of G_Q, which are precisely the p-torsion points defined over Q.

**Source:** Silverman, *The Arithmetic of Elliptic Curves*, Chapter III. This is an elementary consequence of the definition of the Galois action on torsion points.

### Fact 2: Selmer group structure

The p-Selmer group Sel_p(E/Q) sits in an exact sequence:

$$0 \to E(\mathbb{Q})/pE(\mathbb{Q}) \to \mathrm{Sel}_p(E/\mathbb{Q}) \to \mathrm{Ш}(E/\mathbb{Q})[p] \to 0$$

where Ш is the Tate-Shafarevich group. This is a definition/standard construction (see Milne's *Elliptic Curves*, or Silverman Chapter X).

### Fact 3: K[p]^{G_Q} = 0 for large p

If φ: X₀(N) → E is the optimal modular parametrization and K = ker(φ*: J₀(N) → E), then for p not dividing the modular degree m = deg(φ), the kernel of the map K[p] → J₀(N)[p] on G_Q-invariants is controlled by E[p]^{G_Q}. For p large enough (specifically, p > max{m, |J₀(N)(Q)_{tor}|}), one has K[p]^{G_Q} = 0. This is correct and follows from the long exact sequence in Galois cohomology applied to 0 → K → J₀(N) → E → 0 when p ∤ m.

**Source:** Agashe–Stein (2007), Mazur's visibility principle.

### What Does NOT Follow

**The critical non-implication:** Facts 1–3 do **not** imply that Ш(E/Q) = 0. The Tate-Shafarevich group is a subtle arithmetic invariant. Showing Ш = 0 for a specific curve requires:

- **Kolyvagin's theorem** (1989): If E/Q has analytic rank 0 or 1, and the relevant Heegner point or L-value is non-vanishing, then Ш is finite.
- **Gross-Zagier + Kolyvagin**: For analytic rank 0 or 1, BSD is known (modulo results on the p-part for specific p).
- **For analytic rank ≥ 2**: No general method exists to prove Ш is finite, let alone trivial. This is an open problem.

The claim that "Galois cohomology of p-torsion" or "K[p]^{G_Q} = 0" proves Ш = 0 is a category error. Visibility of Ш in J₀(N) shows that elements of Ш[p] correspond to cohomology classes in H¹(Q, K[p]), but one still needs to show these classes are trivial. The vanishing K[p]^{G_Q} = 0 makes the map K[p]^{G_Q} → J₀(N)[p]^{G_Q} injective (trivially, since the domain is 0), but this does not by itself kill Ш[p].

---

## Revised Assessment of the Project

### What this project contributed:

1. A computation of S_E(X) = Σ a_p/p for 10,196 curves using 300 primes. This is a legitimate numerical experiment.

2. Observations about the distribution of S_E values. These are data points, not theorems.

### What this project did NOT contribute:

1. Any new theorem about elliptic curves.
2. Any new evidence for BSD.
3. Any new method for computing or bounding the Tate-Shafarevich group.
4. Any valid proof that Ш = 0 for any curve.

### What should happen next:

- If the goal is rank detection via a_p sums: this requires rigorous bounds on the error term E(X) in the explicit formula. This is a hard open problem in analytic number theory.
- If the goal is BSD: this requires tools from the theory of Euler systems (Kolyvagin) or Iwasawa theory, not sums of a_p/p.
- If the goal is a_p statistics: the computation is fine as data. It should be published as a computation, not dressed up as theorems.

---

## References

1. Iwaniec, H., Kowalski, E. *Analytic Number Theory.* AMS Colloquium Publications, 2004.
2. Soundararajan, K. "Nonvanishing of L-functions and the strong shift convolution." Duke Math J., 2000.
3. Silverman, J. *The Arithmetic of Elliptic Curves.* Springer GTM, 2009.
4. Gross, B., Zagier, D. "Heegner points and derivatives of L-series." Invent. Math., 1986.
5. Kolyvagin, V. "Euler systems for Grothendieck-Tate groups." Invent. Math., 1990.
6. Milne, J.S. *Elliptic Curves.* 2006. (For the Selmer group exact sequence and Ш.)
7. Agashe, A., Stein, K. "Visibility of Shafarevich-Tate groups of abelian varieties." J. Reine Angew. Math., 2007.
