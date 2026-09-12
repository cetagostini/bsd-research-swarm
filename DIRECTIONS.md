# BSD Research Swarm — Research Directions

**115 precise mathematical research directions organized into 10 groups**

Each direction includes:
- **Statement**: Precise mathematical claim or question
- **Tools needed**: Software, databases, techniques
- **What's known**: Key results already proven
- **Main obstacle**: The specific technical barrier
- **BSD connection**: How this direction advances toward proving BSD
- **Status**: {Unexplored, In Progress, Promising, Dead End, Partial Result}
- **Classification**: {Theorem, Lemma, Conjecture, Experiment, Speculation}

---

## Overview

| Group | Name | Directions | Status |
|-------|------|------------|--------|
| A | Iwasawa Theory | 12 | Active |
| B | Euler Systems | 12 | Active |
| C | Arithmetic Statistics | 12 | Active |
| D | Tate-Shafarevich Group (III) | 12 | Active |
| E | p-adic Methods | 11 | Active |
| F | Motivic/Cohomological | 12 | Active |
| G | Deformation/Langlands | 11 | Active |
| H | Computational | 11 | Active |
| I | Connections | 10 | Active |
| J | Unconventional | 12 | Active |
| **Total** | | **115** | |

---


# Directions A: Iwasawa Theory

## A-001: Main Conjecture of Iwasawa Theory for Elliptic Curves over Q

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve and $p$ an odd prime of good ordinary reduction. Let $\mathbb{Z}_p[[\Gamma]] \cong \mathbb{Z}_p[[T]]$ be the Iwasawa algebra for $\Gamma = \operatorname{Gal}(\mathbb{Q}_\infty/\mathbb{Q})$ where $\mathbb{Q}_\infty$ is the cyclotomic $\mathbb{Z}_p$-extension. The Main Conjecture (now a theorem under certain hypotheses) asserts that the characteristic ideal of the Pontryagin dual $\mathfrak{X}_\infty(E) = \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee$ as a finitely generated torsion $\Lambda$-module satisfies

$$\operatorname{char}_{\Lambda}\bigl(\mathfrak{X}_\infty(E)^{\mathrm{div}}\bigr) = \bigl(L_p(E, T)\bigr)$$

where $L_p(E, T) \in \mathbb{Z}_p[[T]]$ is the algebraic $p$-adic L-function constructed by interpolation of critical values $L(E, \chi, 1)$ for finite-order characters $\chi$ of $\Gamma$, and $\mathfrak{X}_\infty(E)^{\mathrm{div}}$ denotes the maximal divisible submodule quotient.

### Tools Needed

- **Magma**: Computation of Selmer groups in finite layers $\mathbb{Q}_n/\mathbb{Q}$, verification of $\Lambda$-module structure via $\Lambda$-presentations
- **SageMath**: Modular symbols for $L_p(E, \chi, 1)$ computations, Pollack–Stevens overconvergent symbols
- **Lean 4**: Formalization of the relevant commutative algebra (structure theorem for torsion $\Lambda$-modules, Weierstrass preparation)
- **LMFDB / Cremona database**: Curves with known analytic ranks, conductor ranges for systematic verification

### What's Known

- Skinner–Urban (2014) proved the Main Conjecture for $E/\mathbb{Q}$ at primes $p \geq 5$ under the hypotheses: (i) $E$ has good ordinary reduction at $p$, (ii) $E[p]$ is irreducible, (iii) $E$ has a rational point of order $p$ or $a_p \not\equiv p+1 \pmod{p^2}$ (the "non-Eisenstein" condition), and (iv) the Iwasawa $\mu$-invariant vanishes.
- Kato (2004) established the divisibility $\operatorname{char}(\mathfrak{X}_\infty^{\mathrm{div}}) \supseteq (L_p)$ via his Euler system of modular elements.
- The reverse divisibility (equality) requires input from the $p$-adic Langlands program or congruence/module-theoretic arguments.
- Kurihara (2002) and Perrin-Riou connected the Main Conjecture to the refined Birch–Swinnerton-Dyer conjecture via the $\mathcal{L}$-invariant.

### Main Obstacle

Removing the auxiliary hypotheses of Skinner–Urban—specifically, the non-Eisenstein condition and the assumption $\mu = 0$—and extending to primes $p = 2, 3$. The Skinner–Urban argument relies on Ihara's lemma for the relevant Shimura curve, which fails in low conductor or at small primes. A purely Galois-representation-theoretic proof avoiding Ihara's lemma does not currently exist.

### BSD Connection

The Main Conjecture directly controls the $p$-part of BSD: the characteristic ideal of the Selmer group encodes the $p$-adic valuation of $L(E,1)/\Omega_E$ when $\operatorname{ord}_{s=1} L(E,s) = 0$. For positive analytic rank, it predicts the structure of the $p^\infty$-Selmer group in terms of the $p$-adic L-function's leading coefficient, giving the $p$-adic BSD formula.

### Status

Partial Result

### Classification

Theorem

---

## A-002: p-adic L-functions via Modular Symbols

### Statement

Let $f = \sum a_n q^n$ be the weight-2 newform attached to $E/\mathbb{Q}$ of conductor $N$, and $p \nmid N$ a good ordinary prime. The Pollack–Stevens method constructs the $p$-adic L-function $L_p(f, s)$ as a $p$-adic analytic function on $\operatorname{Hom}_{\mathrm{cts}}(\mathbb{Z}_p^\times, \mathbb{C}_p)$ by computing the $p$-adic interpolation of modular symbols

$$\{\alpha\}_f = 2\pi i \int_\alpha^{\sqrt{-1}\infty} f(z)\, dz \in \mathbb{C}$$

via overconvergent modular symbols on the $p$-adic upper half-plane. The precise claim is that for any finite-order character $\chi$ of conductor $p^n$ and infinity type $j$ (with $j$ even, $0 \leq j \leq k-2$), one has

$$L_p(f, \chi, j+1) = \left(1 - \frac{a_p \chi(p)}{p^{j+1}}\right)\left(1 - \frac{\overline{\chi(p)}}{a_p}\right) \cdot \frac{\tau(\chi)}{p^n} \sum_{a \bmod p^n} \chi(a) \{a/p^n\}_f$$

where $\{a/p^n\}_f$ is the modular symbol evaluated by the Pollack–Stevens algorithm lifting a classical symbol to an overconvergent one with controlled denominator.

### Tools Needed

- **SageMath**: `mspadic` module for Pollack–Stevens overconvergent modular symbols, direct computation of $L_p(f, \chi, j+1)$
- **Magma**: Classical modular symbol computation as input, verification of Manin symbol relations
- **PARI/GP**: Verification of interpolation property against algebraic parts computed via Darmon-style integration
- **Custom verification scripts**: Comparison of Pollack–Stevens output with Shimura–Shintani–Waldspurger algebraic parts

### What's Known

- Pollack–Stevens (2007) gave an algorithmic method for computing $p$-adic L-functions of modular forms via overconvergent modular symbols, implementing the interpolation of $L$-values at critical integers.
- Lauder (2004) provided an independent algorithm using $p$-adic cohomology.
- Pollack (2006, 2008) showed that at supersingular primes, $L_p(f, s)$ splits into two branches $L_p^+(f, T)$ and $L_p^-(f, T)$ (plus/minus $p$-adic L-functions), each having bounded denominators.
- Bellaïche (2012) proved the exceptional zero conjecture for the $p$-adic L-function in the case of a trivial zero.

### Main Obstacle

At supersingular primes ($a_p = 0$), the Pollack–Stevens algorithm produces symbols with unbounded denominators, preventing direct numerical computation. While Pollack's plus/minus splitting resolves this theoretically, the numerical precision required grows with the number of interpolation points, and rigorous error bounds are difficult to establish. Extending the method to weight $k > 2$ and to non-trivial nebentypus remains technically demanding.

### BSD Connection

Numerical computation of $L_p(f, s)$ is the primary tool for verifying the $p$-adic BSD conjecture for specific curves. The order of vanishing of $L_p(f, s)$ at $s = 1$ predicts the rank of the Selmer group over $\mathbb{Q}_\infty$, and the leading coefficient encodes the $p$-adic regulator, $\mathcal{L}$-invariant, and Tamagawa factors.

### Status

In Progress

### Classification

Theorem

---

## A-003: Selmer Groups over $\mathbb{Z}_p$-extensions and Greenberg's Conjecture

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at $p$, and let $\mathbb{Q}_\infty/\mathbb{Q}$ be the cyclotomic $\mathbb{Z}_p$-extension with layers $\mathbb{Q}_n$. Let $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)$ be the $p^\infty$-Selmer group defined by the local conditions:

$$\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n) = \ker\left(H^1(\mathbb{Q}_n, E[p^\infty]) \to \prod_v \frac{H^1(\mathbb{Q}_{n,v}, E[p^\infty])}{\operatorname{im}\,\kappa_v}\right)$$

where $\kappa_v$ is the Kummer map. Greenberg's conjecture predicts that $\mathfrak{X}_\infty = \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee$ is a finitely generated $\mathbb{Z}_p$-module, equivalently, the $\mu$-invariant $\mu(E/\mathbb{Q}_\infty) = 0$ and $\lambda(E/\mathbb{Q}_\infty) < \infty$. More precisely, $\mathfrak{X}_\infty$ is pseudo-null as a $\Lambda$-module.

### Tools Needed

- **Magma**: Direct computation of Selmer groups over $\mathbb{Q}_n$ for small $n$ via flat cohomology and local Tate duality, computation of $\Lambda$-coranks and $\lambda$-invariants for layers up to $n \approx 10$–$15$
- **SageMath**: Tracking the growth of $|\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)|$ as a function of $n$ to estimate $\lambda$-invariant
- **PARI/GP**: Class group and unit computations in $\mathbb{Q}_n$ for the local conditions at primes above $p$
- **Lean 4**: Formalization of Greenberg's structure theory for Selmer groups in $\mathbb{Z}_p$-extensions

### What's Known

- Greenberg (1989, 1999) conjectured $\mu = 0$ and pseudo-nullity. He proved that if $E$ has good supersingular reduction at $p$ or if $a_p = 0$, then certain modified Selmer groups are cotorsion.
- Ferrero–Washington (1979) proved $\mu = 0$ for cyclotomic $\mathbb{Z}_p$-extensions of abelian number fields (CM case).
- Kurihara (2002) showed that Greenberg's conjecture implies that $|\text{III}(E/\mathbb{Q}_n)[p^\infty]|$ is bounded independently of $n$.
- For CM curves, Rubin (1991) proved the Main Conjecture using Euler systems, giving strong control on $\lambda$-invariants.
- Numerical evidence (Washington, Pollack, Balcı, etc.) supports $\mu = 0$ for thousands of curves.

### Main Obstacle

No technique currently proves $\mu(E/\mathbb{Q}_\infty) = 0$ for a single non-CM elliptic curve. Ferrero–Washington uses CM structure and $p$-adic Hodge theory that is unavailable in the non-CM case. The pseudo-nullity conjecture requires understanding the full $\Lambda$-module structure of $\mathfrak{X}_\infty$, which in turn requires knowledge of the dual Selmer group at primes dividing the conductor.

### BSD Connection

If $\mathfrak{X}_\infty$ is $\mathbb{Z}_p$-cotorsion with bounded $p$-part of Tate–Shafarevich groups in the tower, then the $p$-adic BSD formula at layer $n$ relates $\operatorname{ord}_{s=1} L(E/\mathbb{Q}_n, s)$ to the $\mathbb{Z}_p$-corank of $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)$, validating BSD's rank prediction in the tower and providing uniform control on Tamagawa factors.

### Status

Promising

### Classification

Conjecture

---

## A-004: Iwasawa Theory for Imaginary Quadratic Fields

### Statement

Let $K$ be an imaginary quadratic field in which $p$ splits as $\mathfrak{p}\bar{\mathfrak{p}}$, and let $E/K$ be an elliptic curve with complex multiplication by $\mathcal{O}_K$ (or more generally, a non-CM curve defined over $\mathbb{Q}$ base-changed to $K$). Let $K_\infty/K$ be the $\mathbb{Z}_p^2$-extension—the compositum of the two independent $\mathbb{Z}_p$-extensions of $K$. The Bertolini–Darmon program seeks to construct $p$-adic L-functions over $K$ and prove an Iwasawa Main Conjecture relating the characteristic ideal of $\operatorname{Sel}_{p^\infty}(E/K_\infty)^\vee$ (as a module over $\Lambda(G_\infty)$ for $G_\infty = \operatorname{Gal}(K_\infty/K) \cong \mathbb{Z}_p^2$) to a two-variable $p$-adic L-function $\mathscr{L}_p(E/K) \in \Lambda(G_\infty)$ interpolating $L(E/K, \psi, 1)$ for ring class characters $\psi$ of $K$.

### Tools Needed

- **Magma**: Computation of Heegner points and Stark–Heegner points over ring class fields of $K$, verification of the Gross–Zagier formula in layers of the anticylotomic tower
- **SageMath**: Rankin–Selberg $L$-values for $E$ twisted by ring class characters, modular symbol methods for CM forms
- **PARI/GP**: Hilbert class field computations, ring class field tower enumeration
- **LMFDB**: Systematic extraction of CM curves and their $L$-value data

### What's Known

- Bertolini–Darmon (2005) constructed $p$-adic L-functions in the anticylotomic direction using rigid analytic uniformization and $p$-adic integration on Mumford curves.
- Howard (2006) proved a "three-variable" Iwasawa Main Conjecture for CM elliptic curves in the ordinary case, using congruences between Eisenstein series and CM forms.
- For $E/K$ with CM by $\mathcal{O}_K$, Rubin's Euler system of elliptic units gives the anticylotomic Main Conjecture unconditionally.
- Brooks–Shimizu (2022) made progress on the cyclotomic direction for non-CM curves over $K$.

### Main Obstacle

For the full $\mathbb{Z}_p^2$-extension, the Iwasawa algebra $\Lambda(G_\infty) \cong \mathbb{Z}_p[[S, T]]$ is two-variable, and the structure theory of modules over two-variable rings is vastly more complicated than over $\mathbb{Z}_p[[T]]$. The characteristic ideal is no longer principal in general, and pseudo-null modules play a fundamental role. Construction of the two-variable $p$-adic L-function in the non-CM case is not yet complete.

### BSD Connection

The two-variable Main Conjecture controls the variation of $\operatorname{Sel}_{p^\infty}(E/K_n)$ through the entire $\mathbb{Z}_p^2$-tower, relating the $p$-adic valuation of $L(E/K, \psi, 1)$ to the structure of Selmer groups over all ring class fields. This is the most direct path from Iwasawa theory to the full BSD conjecture over number fields beyond $\mathbb{Q}$.

### Status

In Progress

### Classification

Theorem

---

## A-005: Anticylotomic Iwasawa Theory

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$, $K$ an imaginary quadratic field with $(N, D_K) = 1$ satisfying the Heegner hypothesis (every prime dividing $N$ splits in $K$), and $p \nmid 2ND_K$ a rational prime splitting in $K$ as $\mathfrak{p}\bar{\mathfrak{p}}$. Let $K_\infty^-/K$ be the anticylotomic $\mathbb{Z}_p$-extension, characterized by the action of complex conjugation $\operatorname{Gal}(K_\infty^-/\mathbb{Q}) \cong \mathbb{Z}_p \rtimes \mathbb{Z}/2\mathbb{Z}$ where the nontrivial element of $\mathbb{Z}/2\mathbb{Z}$ acts on $\mathbb{Z}_p$ by $x \mapsto -x$. Define the anticylotomic Selmer group $\operatorname{Sel}^-(E/K_\infty^-)$ by imposing relaxed conditions at $\mathfrak{p}$ and strict conditions at $\bar{\mathfrak{p}}$ (or vice versa). The precise claim is:

1. $\operatorname{Sel}^-(E/K_\infty^-)^\vee$ is a torsion $\Lambda^-$-module of bounded $\mu$-invariant (conjecturally $\mu = 0$).
2. Its $\lambda$-invariant satisfies $\lambda^- = \operatorname{ord}_{s=1} L(E^{(K)}/\mathbb{Q}, s)$ where $E^{(K)}$ is the quadratic twist.
3. The main conjecture: $\operatorname{char}_{\Lambda^-}(\operatorname{Sel}^-(E/K_\infty^-)^\vee) = (\mathscr{L}_p^-(E/K))$ where $\mathscr{L}_p^-$ is the Bertolini–Darmon anticylotomic $p$-adic L-function.

### Tools Needed

- **Magma**: Heegner point computation in layers of the anticylotomic tower, explicit Stark–Heegner points via rigid analytic methods
- **SageMath**: Verification of the Gross–Zagier formula at finite layers, computation of anticylotomic $L$-values
- **PARI/GP**: Ring class field computation, Heegner discriminant enumeration
- **Custom computation**: Anticylotomic $p$-adic L-function via Chida–Hsieh or Bertolini–Darmon integration

### What's Known

- Bertolini–Darmon (2005) constructed $\mathscr{L}_p^-(E/K)$ and proved the anticylotomic Main Conjecture when $E$ has CM by $K$.
- Chida–Hsieh (2018) proved the anticylotomic Main Conjecture for general $E/\mathbb{Q}$ in the "analytic rank $\leq 1$" case (combining Kato's Euler system with Heegner points).
- Howard (2006) proved Iwasawa main conjectures in the "false" anticylotomic setting via $p$-adic families.
- Castella (2019) proved the anticylotomic Main Conjecture in the case of analytic rank 0 under certain technical conditions.
- Brooks (2021) proved $\mu = 0$ for the anticylotomic Selmer group of $E/K$ under mild hypotheses.

### Main Obstacle

In the "generic rank" case ($\operatorname{ord}_{s=1} L(E^{(K)}, s) \geq 2$), the anticylotomic Main Conjecture remains open. The Euler system of Heegner points is rank-1 by nature (it lives in a rank-1 module), so higher-rank cases require either: (a) a different Euler system (e.g., Beilinson–Flach elements from Rankin–Selberg convolutions), or (b) new Iwasawa-theoretic arguments leveraging congruences.

### BSD Connection

Anticylotomic Iwasawa theory controls the $p$-part of BSD for the quadratic twist $E^{(K)}/\mathbb{Q}$: the $\lambda$-invariant predicts the rank, the main conjecture equates the $p$-adic L-function with the Selmer group, and the method of Coleman–Chabauty in the anticylotomic tower gives explicit $p$-adic formulas for $|{\text{Ш}}(E^{(K)}/\mathbb{Q})[p^\infty]|$.

### Status

Promising

### Classification

Theorem

---

## A-006: Iwasawa Theory at Supersingular Primes

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve and $p$ a prime of supersingular reduction ($a_p = 0$ for $p > 3$, or $a_p = \pm p$ for the endomorphism case). The $p$-adic L-function $L_p(E, T)$ does not exist as an element of $\mathbb{Z}_p[[T]]$ in the classical sense because the Euler factor at $p$ vanishes at all finite-order characters of the cyclotomic tower. Kobayashi (2003) defined plus and minus Selmer groups $\operatorname{Sel}_{p^\infty}^\pm(E/\mathbb{Q}_n)$ by replacing the local condition at $p$ with conditions on the images under $\operatorname{res}_p: H^1(\mathbb{Q}_{n,p}, E[p^\infty]) \to H^1(\mathbb{Q}_{\infty,p}, E[p^\infty])$ restricted to $\pm$-eigenspaces of the Frobenius on the $p$-divisible group. The claim is:

$$\operatorname{char}_{\Lambda}\left(\operatorname{Sel}_{p^\infty}^+(E/\mathbb{Q}_\infty)^\vee\right) = \left(L_p^+(E, T)\right), \quad \operatorname{char}_{\Lambda}\left(\operatorname{Sel}_{p^\infty}^-(E/\mathbb{Q}_\infty)^\vee\right) = \left(L_p^-(E, T)\right)$$

where $L_p^\pm(E, T) \in \mathbb{Z}_p[[T]]$ are the Pollack plus/minus $p$-adic L-functions satisfying $L_p^+ L_p^- = L_p^{\mathrm{sym}}$ (the symmetric square $p$-adic L-function up to a unit).

### Tools Needed

- **SageMath**: Pollack's plus/minus $p$-adic L-function computation via overconvergent modular symbols with explicit $\log$-and-$\exp$ maps
- **Magma**: Kobayashi plus/minus local conditions computation, explicit description of $H^1_{\pm}$ in terms of Kummer images
- **PARI/GP**: Verification of $\pm$-Selmer group orders at finite layers against leading coefficients of $L_p^\pm$
- **Lean 4**: Formalization of the supersingular local Tate duality used in the plus/minus Selmer group axioms

### What's Known

- Kobayashi (2003) defined $\operatorname{Sel}^\pm_{p^\infty}(E/\mathbb{Q}_\infty)$ and proved they are $\Lambda$-cotorsion.
- Pollack (2006) constructed $L_p^\pm(E, T) \in \mathbb{Z}_p[[T]]$ and proved they satisfy interpolation properties.
- Kurihara (2010) proved the Main Conjecture for the plus/minus Selmer groups for $p = 3$ under certain conditions.
- Sprung (2013) proved the Iwasawa Main Conjecture at supersingular primes for CM curves using $p$-adic methods.
- Kim (2020) proved the plus/minus Main Conjecture for certain curves with $a_p = 0$.
- Iovita–Pollack (2006) extended the plus/minus construction to higher weight modular forms.

### Main Obstacle

The plus/minus local conditions at $p$ destroy Pontryagin duality in the usual sense: $\operatorname{Sel}^+$ and $\operatorname{Sel}^-$ are not dual to each other via the standard pairing. This makes the algebraic arguments from the ordinary case (where duality gives a control theorem) inapplicable. Bridging the gap requires either a new duality theory for plus/minus Selmer groups or a fundamentally different proof strategy, such as Beilinson–Flach Euler systems adapted to the supersingular setting.

### BSD Connection

For curves with supersingular reduction at $p$ and $\operatorname{ord}_{s=1} L(E, s) \geq 2$, the classical approach via cyclotomic Main Conjecture fails entirely. The plus/minus Main Conjecture restores the connection between $p$-adic L-values and Selmer groups, making it the essential tool for $p$-adic BSD at supersingular primes. Numerically, $L_p^\pm$ have bounded denominators, enabling computation of the $p$-adic regulator.

### Status

In Progress

### Classification

Theorem

---

## A-007: Non-Commutative Iwasawa Theory

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve and $F_\infty$ a Galois extension of $\mathbb{Q}$ with Galois group $G = \operatorname{Gal}(F_\infty/\mathbb{Q})$ that is a compact $p$-adic Lie group of dimension $\geq 2$ that is **non-abelian** (e.g., $F_\infty = \tilde{\mathbb{Q}}_{S,p}^{\mathrm{cyc}}$ the compositum of all $\mathbb{Z}_p$-extensions of all number fields, or $F_\infty/\mathbb{Q}$ with $G \cong \mathrm{GL}_2(\mathbb{Z}_p) \times \mathbb{Z}_p$). The completed group ring $\mathbb{Z}_p[[G]]$ is non-commutative. Coates–Fukaya–Kaczorowski–Sujatha (2005) conjecture that for any $\mathbb{Z}_p$-extension $K_\infty/\mathbb{Q}$ contained in $F_\infty$, the Selmer group $\operatorname{Sel}_{p^\infty}(E/F_\infty)$ is $\mathbb{Z}_p[[G]]$-cotorsion, and the characteristic element $\operatorname{char}_{\mathbb{Z}_p[[G]]}(\operatorname{Sel}_{p^\infty}(E/F_\infty)^\vee)$ exists in the K-theory group $K_1(\mathbb{Z}_p[[G]])$ and is given by a $p$-adic L-function.

### Tools Needed

- **Lean 4**: Formalization of K-theory of $p$-adic group rings, Ore localization, and the non-commutative Fitting invariant
- **Magma**: Computation of $\operatorname{Sel}_{p^\infty}(E/F_n)$ for layers $F_n$ of non-abelian extensions, testing cotorsion predictions
- **SageMath**: Verification of the $\mathbb{Z}_p[[G]]$-module structure via presentation matrices over non-commutative rings
- **PARI/GP**: Computation of Artin conductors and $\varepsilon$-factors for non-abelian Artin representations

### What's Known

- Coates–Fukaya–Kaczorowski–Sujatha (2005) proved that for $F_\infty$ the maximal pro-$p$ extension of $\mathbb{Q}$ unramified outside $p$, $\operatorname{Sel}_{p^\infty}(E/F_\infty)$ is trivial (hence cotorsion).
- Fukaya–Kato (2014) formulated a precise non-commutative Main Conjecture using K-theory and pseudo-isomorphism of non-commutative modules.
- Ritter–Weiss (2010, 2013) proved the non-commutative Main Conjecture for tori, providing a model for the elliptic curve case.
- Nickel (2011) extended the result of CFKS to a wider class of non-commutative extensions.
- Harris–Sujatha (2016) studied the structure of the Selmer group over pro-$p$-dihedral extensions.

### Main Obstacle

The K-theoretic formulation is extremely abstract: $K_1(\mathbb{Z}_p[[G]])$ for non-commutative $G$ has no simple explicit description, and constructing the non-commutative $p$-adic L-function as an element of $K_1$ requires the equivariant Tamagawa number conjecture (ETNC) or a deep input from the $p$-adic Langlands program. For $\mathrm{GL}_2(\mathbb{Z}_p)$-extensions (arising from Hida families), even defining the interpolation problem is technically unsolved.

### BSD Connection

Non-commutative Iwasawa theory unifies the BSD conjecture across all primes simultaneously: the non-commutative $p$-adic L-function encodes $L(E, \chi, 1)$ for **all** Artin characters $\chi$ of $G$ in a single object, and its specialization to $\chi$ recovers the $\chi$-component of the equivariant BSD conjecture. A proof of the non-commutative Main Conjecture would imply BSD for $E$ twisted by all Artin representations of $G$.

### Status

Unexplored

### Classification

Conjecture

---

## A-008: Iwasawa Theory for Rankin–Selberg Convolutions

### Statement

Let $f$ and $g$ be modular forms of weights $k$ and $\ell$ respectively, and consider the Rankin–Selberg convolution $L(f \times g, s)$. In the Iwasawa-theoretic setting, one seeks a $p$-adic L-function $\mathscr{L}_p(f \times g)$ interpoling the algebraic parts of $L(f \times g, \chi, j)$ for critical integers $j$ and finite-order characters $\chi$. Hida's framework: let $\mathbf{f}$ and $\mathbf{g}$ be $p$-adic families of modular forms passing through $f$ and $g$, with $U_p$-eigenvalues $\alpha_f$ and $\alpha_g$. Assume $\alpha_f \neq \alpha_g$ (the "non-critical" or "generic" slope condition). Then there exists $\mathscr{L}_p(f \times g) \in \Lambda$ (or $\Lambda \hat{\otimes} \Lambda$ for two-variable families) satisfying:

$$\mathscr{L}_p(f \times g)(\chi, j) = \frac{e_p(f, g, \chi, j) \cdot L^{\{p\}}(f \times g, \chi, j)}{\langle f, f \rangle \cdot \langle g, g \rangle \cdot \Omega_f \cdot \Omega_g}$$

for explicitly defined Euler-type factors $e_p$ and Petersson inner products, and critical periods $\Omega_f, \Omega_g$.

### Tools Needed

- **Magma**: Hida family computation, ordinary $p$-adic families of modular forms via `HidaFamily` or custom implementation
- **SageMath**: Beilinson–Flach element computation, Rankin–Selberg $L$-values, Garrett–Rankin triple product $L$-values
- **PARI/GP**: $L$-function special values for Rankin–Selberg products via Dokchitser's method
- **Custom computation**: Double/triple $p$-adic integration for the Rankin–Selberg $p$-adic L-function

### What's Known

- Hida (1991, 2004) constructed the Rankin–Selberg $p$-adic L-function for ordinary forms via Eisenstein families and proved its interpolation property under the non-critical slope condition.
- Hsieh (2014) proved the Rankin–Selberg Main Conjecture for ordinary forms, relating $\operatorname{char}(\operatorname{Sel}_{p^\infty}(E_1 \times E_2/\mathbb{Q}_\infty)^\vee)$ to Hida's $p$-adic L-function.
- Kings–Loeffler–Zerbes (2021) constructed Euler systems for Rankin–Selberg convolutions of Hilbert modular forms (Garrett–Rankin motives) and used them toward the Main Conjecture.
- Dasgupta–Kakde (2022) gave new proofs of the Rankin–Selberg Main Conjecture in the ordinary case using the Gross–Stark unit and its generalizations.

### Main Obstacle

The non-critical slope condition $\alpha_f \neq \alpha_g$ fails when both forms have the same $U_p$-eigenvalue, which occurs systematically when $f = g$ (the symmetric square case) or when $f$ and $g$ are congruent modulo $p$. In the critical slope case, Hida's construction does not produce a $p$-adic L-function, and the Euler system of Beilinson–Flach elements may not have the required norm-compatibility. Understanding the critical-slope Rankin–Selberg $p$-adic L-function requires input from $p$-adic Hodge theory (étale $(\varphi, \Gamma)$-modules).

### BSD Connection

For the product $E_1 \times E_2$ of two elliptic curves, the Rankin–Selberg $L$-function $L(E_1 \times E_2, s)$ is the motivic $L$-function of the tensor product of their Tate modules. The Iwasawa Main Conjecture for $L(E_1 \times E_2)$ controls the $p$-adic valuation of $L(E_1 \times E_2, 1)$, which (by the Bloch–Kato conjecture) should equal the order of a Selmer group related to $\operatorname{Ext}^1_{\mathcal{M}}(\mathbb{Q}(0), h^1(E_1) \otimes h^1(E_2))$. This is the deepest known case of BSD for motives of rank $> 1$ beyond the elliptic curve itself.

### Status

Promising

### Classification

Theorem

---

## A-009: Iwasawa Invariants and Growth of Selmer Groups

### Statement

For an elliptic curve $E/\mathbb{Q}$ and prime $p$ of good ordinary reduction, the $\mu$- and $\lambda$-invariants of the Selmer group over the cyclotomic $\mathbb{Z}_p$-extension $\mathbb{Q}_\infty$ are defined by: if $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)^\vee \sim_{\Lambda} \bigoplus_i \Lambda/(f_i(T))$ (pseudo-isomorphism), then

$$\mu = \sum_i \operatorname{ord}_p \operatorname{cont}(f_i), \qquad \lambda = \sum_i \deg \bar{f}_i$$

where $\bar{f}_i$ is the distinguished polynomial obtained from $f_i$ by Weierstrass preparation. The growth of Selmer groups in the tower is governed by:

$$\dim_{\mathbb{F}_p} \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p] = \mu p^n + \lambda n + \nu$$

for all sufficiently large $n$ (Iwasawa's formula), where $\nu \in \mathbb{Z}$ depends on the constant term.

### Tools Needed

- **Magma**: Direct computation of $|\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_n)[p]|$ for $n$ up to $10$–$20$, fitting the Iwasawa polynomial
- **SageMath**: Computation of $\mu$ and $\lambda$ from the $p$-adic L-function (Weierstrass degree and $p$-adic valuation), verification of Greenberg's formula for $\nu$
- **PARI/GP**: Iwasawa invariants for class groups in $\mathbb{Z}_p$-extensions (Ferrero–Washington verification, analogies)
- **Custom verification**: Tracking $a_p(E/\mathbb{Q}_n)$ (Frobenius traces in layers) to predict $\lambda$-growth from congruence data

### What's Known

- Greenberg (1999) computed $\mu = 0$ and $\lambda = \operatorname{ord}_{s=1} L_p(E, T)$ for curves with CM and good ordinary reduction.
- Pollack (2001) computed $\mu$ and $\lambda$ for over 1000 curves, confirming $\mu = 0$ and giving $\lambda$ consistent with the $p$-adic L-function.
- Washington (1994) showed that for random $\Lambda$-modules, $\mu = 0$ occurs generically, providing heuristic evidence.
- Ferrero–Washington (1979) proved $\mu = 0$ for the $p$-part of class groups in cyclotomic $\mathbb{Z}_p$-extensions.
- For the anticylotomic direction, Brooks (2021) proved $\mu = 0$ for the anticylotomic Selmer group under mild conditions.
- Kim (2022) computed Iwasawa invariants for curves at supersingular primes using plus/minus theory, finding $\lambda^+ + \lambda^- = \lambda$.

### Main Obstacle

No method currently proves $\mu(E/\mathbb{Q}_\infty) = 0$ for non-CM elliptic curves. The Ferrero–Washington method uses CM $p$-adic Hodge theory (the fact that the $\mu$-invariant of a CM character is zero). In the non-CM case, one needs: either (a) a descent argument showing $\mu = 0$ by comparing Selmer groups at different primes, or (b) a direct proof using the $p$-adic Langlands correspondence. Furthermore, computing $\nu$ explicitly (the "constant term" in Iwasawa's formula) requires detailed knowledge of the local Tamagawa factors at primes dividing $N$.

### BSD Connection

The $\mu$-invariant controls whether the $p$-part of $\text{III}(E/\mathbb{Q})$ can be infinite (it cannot if $\mu = 0$). The $\lambda$-invariant equals $\operatorname{ord}_{T=0} L_p(E, T)$ under the Main Conjecture, hence equals the analytic rank modulo $p$-adic interpolation artifacts. Iwasawa's growth formula gives a uniform bound on $|\text{III}(E/\mathbb{Q}_n)[p^\infty]|$ as $n \to \infty$, which is the tower-BSD prediction for the boundedness of Tate–Shafarevich groups.

### Status

In Progress

### Classification

Theorem

---

## A-010: Refined Iwasawa Theory with Euler System Input

### Statement

The classical Main Conjecture gives a divisibility $\operatorname{char}(\mathfrak{X}) \supseteq (L_p)$ from the Euler system (Kato's modular elements) and an equality $\operatorname{char}(\mathfrak{X}) = (L_p)$ from the congruence module / Eisenstein ideal. A "refined" Main Conjecture is the statement that there exists an explicit basis element $\kappa \in \mathfrak{X}$ (the Euler system class) such that:

1. The Pontryagin pairing $\langle \kappa, - \rangle : \mathfrak{X} \to \Lambda$ identifies $\mathfrak{X}$ with an ideal $I \subseteq \Lambda$.
2. The image of $\kappa$ under the dual exponential map at $p$ equals $L_p(E, T)$ times a unit: $\exp_p^*(\kappa) = L_p(E, T) \cdot u$ for $u \in \Lambda^\times$.
3. The Fitting ideal $\operatorname{Fitt}_\Lambda(\mathfrak{X}) = (L_p(E, T))$, which is stronger than the characteristic ideal equality when $\mathfrak{X}$ is not cyclic.

### Tools Needed

- **Magma**: Computation of Kato's Euler system classes $z_n \in H^1(\mathbb{Q}_n, T_p E)$ via Beilinson–Kato elements, verification of norm-compatibility
- **SageMath**: Dual exponential maps $\exp_p^*: H^1_f(\mathbb{Q}_p, V_p E) \to D_{\mathrm{dR}}(V_p E)/\mathrm{Fil}^0$ and their numerical values
- **Lean 4**: Formalization of the Rubin–Kolyvagin structure theorem relating Euler systems to Selmer group Fitting ideals
- **PARI/GP**: Comparison of Fitting ideals with $p$-adic L-values for specific curves

### What's Known

- Kato (2004) constructed the Euler system and proved $\operatorname{char}(\mathfrak{X}) \supseteq (L_p)$ and $\operatorname{char}(\mathfrak{X}_{\mathrm{div}}) \subseteq (L_p)$ (i.e., equality on the divisible part).
- Rubin (1991) proved the Euler-system-to-Main-Conjecture implication in the CM case, showing that the Euler system generator gives the Fitting ideal.
- Kurihara (2002) showed that the Fitting ideal version is equivalent to the refined BSD conjecture for the $p$-part.
- Perrin-Riou (1995, 2000) developed the $p$-adic regulator map relating Euler system classes to $p$-adic L-values via the $\mathcal{L}$-invariant.
- Howard (2006) established the Fitting ideal Main Conjecture in certain "binary" Iwasawa-theoretic settings (false Tate curve modules).

### Main Obstacle

The gap between the characteristic ideal and Fitting ideal is the central obstruction: $\operatorname{Fitt} \subseteq \operatorname{char}$ always, but equality fails when $\mathfrak{X}$ is not $\Lambda$-cyclic (i.e., when $\mathfrak{X}$ needs more than one generator). Showing that $\mathfrak{X}$ is cyclic as a $\Lambda$-module—or proving equality of Fitting and characteristic ideals by other means—requires an analysis of the $\Lambda$-module structure beyond pseudo-isomorphism. This is currently out of reach in the non-CM case.

### BSD Connection

The refined Main Conjecture with Fitting ideals is equivalent to the $p$-adic BSD formula: $L_p^{(\alpha)}(E, 1) = \frac{\mathcal{L}_p \cdot c_p \cdot |\text{Ш}[p^\infty]|}{|E(\mathbb{Q})_{\mathrm{tors}}|^2}$ where $\alpha = \operatorname{ord}_{s=1} L_p(E,s)$ and $\mathcal{L}_p$ is the $p$-adic regulator. Proving the Fitting ideal version simultaneously gives both the order of the $p$-part of $\text{Ш}$ and the $p$-adic regulator, which are the arithmetic content of BSD.

### Status

Promising

### Classification

Conjecture

---

## A-011: Two-Variable $p$-adic L-functions for Imaginary Quadratic Base

### Statement

Let $K$ be an imaginary quadratic field where $p = \mathfrak{p}\bar{\mathfrak{p}}$ splits, and $E/\mathbb{Q}$ an elliptic curve with good ordinary reduction at $p$ satisfying the Heegner hypothesis for $K$. Let $K_\infty = K_\infty^{\mathrm{cyc}} \cdot K_\infty^-$ be the $\mathbb{Z}_p^2$-extension of $K$. The claim is that there exists a unique (up to unit) two-variable $p$-adic L-function

$$\mathscr{L}_p(E/K) \in \Lambda(G_\infty) = \mathbb{Z}_p[[\operatorname{Gal}(K_\infty/K)]] \cong \mathbb{Z}_p[[S, T]]$$

satisfying: for every ring class character $\psi$ of conductor $\mathfrak{f}$ of $K$ with $\mathfrak{f}$ coprime to $p$, and every integer $j \geq 0$ of appropriate parity,

$$\mathscr{L}_p(E/K)(\psi, j) = \frac{\mathcal{E}_p(\psi, j) \cdot L(E/K, \psi, j+1)}{\Omega_E^{\pm} \cdot \langle f, f \rangle_K}$$

where $\mathcal{E}_p$ is an explicit Euler factor at $p$ and $\Omega_E^{\pm}$ is a period. The interpolation property must hold simultaneously in both the cyclotomic and anticylotomic directions.

### Tools Needed

- **Magma**: Heegner points and their $p$-adic avatars (Stark–Heegner points) in ring class fields, double Dirichlet series partial computation
- **SageMath**: Rankin–Selberg $L$-values for $E$ twisted by ring class characters, double $p$-adic integration on $p$-adic upper half-plane times $p$-adic multiplicative group
- **PARI/GP**: Ring class field enumeration, computation of Heegner discriminants, verification of Euler factors
- **Custom computation**: Bertolini–Darmon $p$-adic integration over Mumford curves, Chida–Hsieh machinery

### What's Known

- Bertolini–Darmon (1999, 2005) constructed a one-variable $p$-adic L-function in the anticylotomic direction via rigid analytic uniformization.
- Hsieh (2014) constructed the anticylotomic $p$-adic L-function unconditionally (removing the CM assumption).
- For CM elliptic curves, Rubin's construction via elliptic units gives the two-variable $p$-adic L-function directly.
- Dasgupta–Darmon–Pollack (2010) studied the two-variable $p$-adic L-function in the setting of Hilbert modular forms over real quadratic fields.
- Castella–Hsieh (2020) made progress toward the two-variable construction for non-CM curves via Hida families.

### Main Obstacle

The fundamental difficulty is constructing a global object that simultaneously interpolates in two independent $p$-adic directions. In the one-variable case, the modular symbol $\{a/p^n\}_f$ naturally lives on $\mathbb{Z}_p^\times$. For two variables, one needs either: (a) a two-variable modular symbol on $(\mathbb{Z}_p^\times)^2$, which lacks a natural modular-analytic interpretation; or (b) a double $p$-adic integral combining the cyclotomic measure (from modular symbols) with the anticylotomic measure (from Heegner points), for which the required convergence is not established. The Shimura–Waldspurger period for the Rankin–Selberg convolution $L(E \times \chi_K, s)$ is needed but its $p$-adic interpolation is not fully understood.

### BSD Connection

The two-variable $p$-adic L-function encodes the full BSD conjecture for $E$ over all ring class fields of $K$ in a single object. Its specialization to the cyclotomic line gives the cyclotomic Main Conjecture for $E/K$, and to the anticylotomic line gives the anticylotomic Main Conjecture for $E/K$. Its order of vanishing at the central point $(s_0, s_1) = (1,0)$ in $\operatorname{Hom}(G_\infty, \mathbb{C}_p)$ predicts $\operatorname{rank} E(K)$, and its leading coefficient gives the $p$-adic BSD formula over $K$.

### Status

Unexplored

### Classification

Speculation

---

## A-012: Iwasawa Theory at Eisenstein Primes

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve and $p$ a prime such that $E$ admits a congruence modulo $p$ with an Eisenstein series: specifically, $a_\ell(E) \equiv 1 + \ell \pmod{p}$ for all primes $\ell \nmid Np$ (the "Eisenstein" condition). This occurs when $E[p]$ is reducible as a Galois representation, fitting in an exact sequence

$$0 \to \mu_p \to E[p] \to \mathbb{Z}/p\mathbb{Z} \to 0$$

over $\mathbb{Q}$. Let $f$ be the newform attached to $E$, and let $\mathbb{T}$ be the Hecke algebra acting on the space of modular forms of weight 2 and level $\Gamma_0(N)$. The Eisenstein ideal $\mathscr{I} \subset \mathbb{T}$ is generated by $T_\ell - (1 + \ell)$ for $\ell \nmid Np$ and $U_p - 1$. The claim is that:

1. The $\mathscr{I}$-adic Selmer group $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)$ has $\lambda$-invariant strictly larger than the "expected" value $\operatorname{ord}_{s=1} L_p(E, T)$ by an amount related to $\dim_{\mathbb{F}_p} \mathbb{T}/\mathscr{I}$.
2. The extra $\lambda$-contribution comes from the extension class in $\operatorname{Ext}^1_{G_\mathbb{Q}}(\mathbb{Z}/p\mathbb{Z}, \mu_p) \cong \mathbb{Z}/p\mathbb{Z}$ representing $E[p]$.
3. A modified Main Conjecture holds: $\operatorname{char}_\Lambda(\mathfrak{X}) = (L_p(E, T) \cdot \mathcal{E}_{\mathrm{Eis}})$ where $\mathcal{E}_{\mathrm{Eis}}$ is the Eisenstein correction factor.

### Tools Needed

- **Magma**: Computation of the Hecke algebra $\mathbb{T}$ modulo $p$ for specific levels, verification of the Eisenstein congruence $a_\ell \equiv 1 + \ell \pmod{p}$
- **SageMath**: Modular symbols modulo $p$ (Wiles–Merel method), computation of the Eisenstein ideal quotient $\mathbb{T}/\mathscr{I}$
- **PARI/GP**: Verification of the reducibility of $E[p]$ for specific curves by computing Galois action on $p$-torsion
- **Lean 4**: Formalization of the Mazur–Ribet argument relating Eisenstein ideals to class groups

### What's Known

- Mazur (1977) pioneered the study of Eisenstein ideals for prime conductor $N$, proving that $|\mathbb{T}/\mathscr{I}|$ divides the numerator of $(N-1)/12$ (the "Eisenstein ideal theorem").
- Ribet (1990, 1998) proved that the reducibility of $E[p]$ is equivalent to the existence of a $p$-isogeny $E \to E'$ over $\mathbb{Q}$ and connected $\mathbb{T}/\mathscr{I}$ to class numbers via the Shimura subgroup and the cuspidal subgroup.
- Kurihara (2002) computed the Fitting ideal of the Selmer group at Eisenstein primes and showed the refined BSD formula holds modulo the Eisenstein ideal.
- Mazur–Tate–Teitelbaum (1986) established the "$p$-adic Birch–Swinnerton-Dyer conjecture at Eisenstein primes" with the $\mathcal{L}$-invariant correction.
- Greenberg–Vatsal (2000) studied the variation of Iwasawa invariants under Eisenstein congruences between different curves.

### Main Obstacle

The reducibility of $E[p]$ means the Euler system machinery (Kato) requires adaptation: the standard norm-compatibility relations for Kato's classes use the irreducibility assumption to ensure the Selmer group is $\Lambda$-torsion. When $E[p]$ is reducible, there can be a non-trivial $\Lambda$-submodule of $\mathfrak{X}$ that is not detected by the $p$-adic L-function, arising from the extension class of $E[p]$. The explicit correction factor $\mathcal{E}_{\mathrm{Eis}}$ depends on the $p$-adic valuation of the period ratio $\Omega^+/\Omega^-$, which is the $\mathcal{L}$-invariant of Mazur–Tate–Teitelbaum, and is not accessible to purely algebraic methods.

### BSD Connection

Eisenstein primes are where BSD fails in its naive form: $L_p(E, 1) = 0$ even when $E$ has analytic rank 0 (the "exceptional zero" phenomenon). The corrected BSD formula $L_p'(E, 1) = \mathcal{L} \cdot \frac{L(E,1)}{\Omega_E} \cdot c_p \cdot |\text{Ш}[p^\infty]|$ involves the $\mathcal{L}$-invariant. Iwasawa theory at Eisenstein primes controls the exceptional zero and its correction, making it essential for a complete proof of the $p$-adic BSD conjecture.

### Status

Promising

### Classification

Theorem

---

# DIRECTIONS_B.md — Euler Systems

## B-001: Kato's Euler System for Modular Forms — Generalization to Rank ≥ 2

**Statement:** Kato (2004) constructed an Euler system of zeta elements $z_k^{(p)} \in H^1(\mathbb{Q}, V_p(E))$ for a modular elliptic curve $E/\mathbb{Q}$, where $V_p(E) = T_p(E) \otimes_{\mathbb{Z}_p} \mathbb{Q}_p$. These satisfy norm-compatibility relations under $\text{Cor}_{m,n}$ for $m \mid n$, and their image under the dual exponential map $\exp^*_{V_p(E)}$ interpolates the special value $L(E,1)$ when $r = 0$ and $L'(E,1)$ when $r = 1$. The question is: can Kato's zeta elements be modified or extended (e.g., via congruence arguments with higher-rank modular forms, or by constructing secondary classes in the spirit of Nekovář's $p$-adic height pairings) to yield non-trivial Selmer group classes when $\text{ord}_{s=1} L(E,s) \geq 2$? More precisely, does there exist a construction producing elements in the Bloch-Kato Selmer group $H^1_f(\mathbb{Q}, V_p(E))$ whose non-vanishing is controlled by the rank of the L-function?

**Tools needed:** SageMath (modular forms, Hecke operators, computation of $p$-adic heights), Lean 4 (formal verification of norm relations), Magma (elliptic curve databases, Selmer group computations)

**What's known:** Kato's Euler system yields the bound $\text{rk}(E(\mathbb{Q})) \leq \dim_{\mathbb{Q}_p} H^1_f(\mathbb{Q}, V_p(E)) - \dim_{\mathbb{Q}_p} H^1_f(\mathbb{Q}, V_p(E)^*(1))$ unconditionally (where $V^*(1)$ is the Tate dual). Combined with Gross-Zagier, this proves weak BSD for analytic rank $\leq 1$. For rank $\geq 2$, the Selmer group bound is not sharp: the Euler system ideal $\mathcal{Z}$ in the Iwasawa algebra can vanish at the augmentation ideal when $L(E,1) = 0$ to order $\geq 2$, yielding no useful information.

**Main obstacle:** The cyclotomic Euler system is controlled by a single-variable Iwasawa algebra $\Lambda = \mathbb{Z}_p[[\Gamma]]$ where $\Gamma = \text{Gal}(\mathbb{Q}(\mu_{p^\infty})/\mathbb{Q})$. The analytic rank condition forces the zeta element to lie in a high power of the augmentation ideal, killing its Selmer-theoretic content. Multi-variable extensions (e.g., over CM fields) or secondary Euler systems in the sense of Nekovář are needed.

**BSD connection:** If a non-trivial class $\kappa \in H^1_f(\mathbb{Q}, V_p(E))$ can be constructed from an Euler system for an elliptic curve with $r \geq 2$, then $\text{III}(E/\mathbb{Q})[p^\infty]$ is finite and the $p$-part of the BSD formula is controlled by the $p$-adic height of $\kappa$. This would give a direct Euler-system proof of weak BSD for higher rank.

**Status:** In Progress

**Classification:** Conjecture

---

## B-002: Beilinson-Flach Elements for Rankin-Selberg Products

**Statement:** Given two modular forms $f, g$ of weights $k_f, k_g$ and levels $N_f, N_g$ respectively, Beilinson-Flach elements $\text{BF}_{f,g}^{(i)} \in H^1(\mathbb{Q}(\mu_m), \mathbb{V}_{f,g} \otimes \mathbb{Q}_p(-i))$ for $i \in \{1, 2\}$ are classes in the Galois cohomology of the Rankin-Selberg motive $M(f) \otimes M(g)$. Here $\mathbb{V}_{f,g}$ is the tensor product of the Galois representations $V_f \otimes V_g$, and the elements satisfy norm relations in a two-variable Iwasawa algebra $\Lambda_{\text{cyc}} \hat\otimes \Lambda_{\text{anticycl}}$. The precise question is: do the Beilinson-Flach elements form a genuine Euler system (satisfying explicit norm-compatibility under $\text{Cor}_{m,n}$ in both the cyclotomic and anticyclotomic towers) whose Rubin-style bounds on the Selmer group $H^1_\Sigma(\mathbb{Q}, \mathbb{V}_{f,g})$ yield non-vanishing results for $L(f \otimes g, 1)$?

**Tools needed:** Magma (modular symbols, Rankin-Selberg L-values), SageMath (p-adic L-function interpolation), PARI/GP (Hecke eigenvalues at bad primes)

**What's known:** Kings, Sprang, and Loeffler-Zerbes established that Beilinson-Flach elements are Euler systems for the representation $V_f \otimes V_g$ and used them to prove the Iwasawa main conjecture for $GL(2) \times GL(2)$ Rankin-Selberg products in many cases. The $p$-adic L-function $\mathcal{L}_p(f,g)$ interpolates $L(f \otimes g, 1)/\Omega_f \Omega_g$ at classical points. For $g = \bar{f}$ (the adjoint square), this yields the Iwasawa main conjecture for $\text{Sym}^2 f$.

**Main obstacle:** The two-variable Euler system requires control of primes dividing the level at which $f$ and $g$ are simultaneously ramified. The prime-to-$p$ Euler system norm relations require the existence of suitable CM points on $X_1(N)$ at auxiliary primes $\ell \equiv 1 \pmod{m}$, and these may not exist when the conductor $N_f N_g$ has many prime factors. The anticyclotomic Iwasawa theory is only partially developed.

**BSD connection:** When $f$ corresponds to an elliptic curve $E/\mathbb{Q}$ and $g$ to a character $\chi$ of an imaginary quadratic field $K$, the Beilinson-Flach elements control the Selmer group of $E$ over $K$ with $\chi$-eigenspace conditions. This directly connects to BSD for the twist $E^{(\chi)}$ and to the $p$-part of the Birch-Swinnerton-Dyer formula for $E/K$.

**Status:** Promising

**Classification:** Theorem (for the Iwasawa main conjecture side; the full BSD application remains a Conjecture)

---

## B-003: Darmon Cycles and Stark-Heegner Points

**Statement:** For an elliptic curve $E/\mathbb{Q}$ of conductor $N = pM$ with $p$ prime, and an imaginary quadratic field $K = \mathbb{Q}(\sqrt{-D})$ satisfying the Heegner hypothesis $(−D, N) = 1$, Stark-Heegner points $P_K \in E(\mathbb{Q}_p)$ are conjectured to be the images under the local period map of Darmon cycles $\mathfrak{z}_K \in H^1(\mathbb{Q}, T_\ell(E))$. These points are defined purely via $p$-adic integration on $\mathbb{P}^1(\mathbb{Q})$ — specifically, as integrals $\int_{\alpha}^{\beta} \omega_f$ where $\omega_f$ is the differential associated to a modular form $f$ of weight 2 corresponding to $E$, and $\alpha, \beta$ are the roots of $x^2 + bx + c = 0$ with $b^2 - 4c = -D$. The precise question is: (a) do Darmon cycles satisfy Euler system norm relations at auxiliary primes $\ell$, and (b) does the resulting Euler system bound $\text{rk}(E(\mathbb{Q}))$ as in Kolyvagin's argument for classical Heegner points?

**Tools needed:** PARI/GP ($p$-adic integration, Stark-Heegner point computation), Magma (elliptic curve conductor computations), SageMath (modular symbols, overconvergent modular forms)

**What's known:** Darmon (2001) conjectured the existence of Stark-Heegner points and proved their basic properties under the assumption that $E$ is modular (now a theorem). Greenberg (2004) showed that the points $P_K$ are global when $E$ has split multiplicative reduction at $p$. Betina and Dimitrov (2021) proved the existence of Darmon cycles in the cohomology of certain unitary Shimura varieties. Computational verifications exist for many examples: the points $P_K$ satisfy the expected relation $[K:\mathbb{Q}] \cdot P_K = P_K^+ + P_K^-$ under the action of complex conjugation, and their Néron-Tate heights match the predicted formula involving $L'(E/K, 1)$.

**Main obstacle:** (a) The norm relations for Darmon cycles at primes $\ell \nmid Np$ remain unproven. The conjectural Shimura curve construction that would yield norm compatibility has not been realized. (b) Even assuming norm relations, the key non-degeneracy condition — that the system of points $\{P_K^{\mathfrak{q}}\}$ indexed by Kolyvagin-type cohomology classes is non-trivial — requires a local computation at $p$ involving the $p$-adic logarithm $\log_p: E(\mathbb{Q}_p) \to \mathbb{Q}_p$ and the explicit formula for the $p$-adic L-function. (c) The definition depends on the choice of a geodesic in the Bruhat-Tits tree, and it is unclear how this choice interacts with norm relations.

**BSD connection:** If Darmon cycles form a genuine Euler system, then Kolyvagin's machinery applies directly: the non-vanishing of $P_K$ implies $\text{rk}(E(\mathbb{Q})) \leq 1$, and the explicit formula gives $L'(E,1)/\Omega_E = c \cdot \hat{h}(P_K)$ where $\hat{h}$ is the Néron-Tate height and $c$ involves Tamagawa numbers and $|\text{III}|$. This would extend the Gross-Zagier-Kolyvagin theorem to the case of Heegner points that are only $p$-adically defined.

**Status:** In Progress

**Classification:** Conjecture (Darmon cycles as Euler system); Partial Result (existence of the points themselves)

---

## B-004: Rubin's Euler System for CM Elliptic Curves

**Statement:** Let $E/\mathbb{Q}$ be an elliptic curve with complex multiplication by an order $\mathcal{O}_K$ in an imaginary quadratic field $K$. The CM Euler system consists of elliptic units $c_m \in E(K(m)) \otimes \mathbb{Q}$ (the images of Siegel units under the CM period map) indexed by squarefree products $m$ of primes splitting in $K$. These satisfy norm relations: if $\ell \nmid m$ is a prime splitting in $K$ as $\ell = \mathfrak{l}\bar{\mathfrak{l}}$, then $\text{Tr}_{K(m\ell)/K(m)}(c_{m\ell}) = P_\ell(\text{Frob}_\mathfrak{l}^{-1}) \cdot c_m$ where $P_\ell(x) = (1 - \alpha_\ell x)(1 - \bar\alpha_\ell x)$ is the Euler factor. Rubin's method applies these to compute the Selmer group $\text{Sel}(E/K) = \ker\left(H^1(K, E[p^\infty]) \to \prod_v H^1(K_v, E[p^\infty])/H^1_f(K_v, E[p^\infty])\right)$. The precise statement to investigate is: for which CM curves $E$ and primes $p$ does Rubin's Euler system yield the exact Selmer group rank predicted by BSD, i.e., $\text{rk}_p \text{Sel}(E/K) = \text{ord}_{s=1} L(E/K, s)$?

**Tools needed:** Magma (CM curve computation, Hecke characters, Selmer group verification), SageMath (elliptic units, Stark units), PARI/GP (class field theory computations, L-values)

**What's known:** Rubin (1991) proved that for CM elliptic curves $E/K$ with good ordinary reduction at $p$, the Euler system bound gives $\text{rk}_p \text{Sel}(E/K) \leq \text{ord}_{s=1} L(E/K,s)$ — the "upper bound" direction of BSD. The converse (lower bound) is known by other methods when $r \leq 1$. For $r \geq 2$, the lower bound is open. Rubin also proved the Iwasawa main conjecture for CM fields: the characteristic ideal of the Pontryagin dual of the Selmer group over $K_\infty = K(E[p^\infty])$ equals the ideal generated by the Katz $p$-adic L-function. This implies $\text{III}(E/K)[p^\infty]$ is finite when $L(E/K,1) \neq 0$.

**Main obstacle:** (a) The equality $\text{rk}_p \text{Sel}(E/K) = \text{ord}_{s=1} L(E/K,s)$ requires the lower bound, which for $r \geq 2$ needs a non-trivial global point — the "Heegner point" analogue for CM curves. When $r = 2$, one needs two independent points, and constructing them from the Euler system alone is insufficient. (b) The ordinary condition at $p$ fails when $E$ has supersingular reduction at $p$, requiring a different Selmer condition (Kobayashi's $\pm$-Selmer groups or Sprung's approach). (c) The Euler system must be "non-degenerate": the image of the Kolyvagin derivative classes $d_m \in H^1(K, E[p])$ under localization must span the correct Selmer-local conditions.

**BSD connection:** Rubin's Euler system directly bounds the $p$-part of $|\text{III}(E/K)|$ and the $p$-adic valuation of $L(E/K,1)/\Omega_E$. Combined with the Gross-Zagier formula for CM twists, this proves BSD for analytic rank $\leq 1$ for CM curves unconditionally. For higher rank, the upper bound on Selmer rank plus the Cassels-Tate pairing ($|\text{III}|$ is a perfect square) gives partial information.

**Status:** Promising

**Classification:** Theorem (upper bound on Selmer rank); Partial Result (full BSD for rank $\geq 2$)

---

## B-005: Higher-Rank Euler Systems (Nekovář, Schappacher)

**Statement:** Nekovář (1993, 2006) and Schappacher-Scholl (1988) proposed a framework for "higher-rank Euler systems" — collections of classes $\mathbf{c}^{(k)} \in \text{Ext}^k_{\mathcal{M}}(\mathbb{Q}(0), M)$ in the category of mixed motives for $k \geq 2$, where $M$ is a motivic Galois representation. For a modular form $f$ with $\text{ord}_{s=1} L(f,s) = r \geq 2$, the conjecture is that there exist classes $\mathbf{c}^{(r)}$ in motivic cohomology $H^{r}_{\mathcal{M}}(\text{Spec}(\mathbb{Q}), \text{Sym}^{r-1}(H^1(E)) \otimes \mathbb{Q}(r))$ whose regulator image equals $L^{(r)}(f,1)/r!$. The precise question is: can these higher extensions be realized concretely (e.g., as higher Chow cycles, Beilinson regulators of polylogarithmic classes, or extensions of mixed Shimura varieties) and do they satisfy norm compatibility?

**Tools needed:** SageMath (polylogarithm computation, motivic cohomology), Lean 4 (formalization of extension classes), Magma (modular symbol computation)

**What's known:** Beilinson (1984, 1986) constructed elements in $K_2$ of modular curves whose Beilinson regulators recover $L'(E,1)$. Deninger (1988) and Wildeshaus (1997) studied higher polylogarithmic extensions on $X_0(N)$. Scholl (1985) showed that the higher Chow groups $\text{CH}^r(\mathcal{X}, 2r-k)$ for modular varieties carry classes whose regulators should give the "higher Beilinson elements." Nekovář (2006) defined the abstract framework: an Euler system of rank $r$ for a $p$-adic representation $V$ is a collection of classes in $H^r(\mathbb{Q}(V)_{/\text{cyc}}, \wedge^r V)$ satisfying compatibility under corestriction maps. No explicit construction of rank $r \geq 2$ Euler systems for $GL(2)$ representations is known.

**Main obstacle:** (a) The motivic cohomology groups $H^r_{\mathcal{M}}(\mathbb{Q}, \text{Sym}^{r-1} V_E)$ are not well-understood for $r \geq 3$; there is no computational handle on them. (b) Even for $r = 2$ (the "rank 2" case), the expected classes in $K_2$ of modular curves have not been shown to satisfy any Euler system-type norm relations. (c) The regulator maps to Deligne cohomology $H^r_{\mathcal{D}}(\mathbb{R}, \text{Sym}^{r-1} V_E \otimes \mathbb{R})$ are known to be injective only in special cases. (d) There is no analogue of Kolyvagin's derivative construction for higher extensions.

**BSD connection:** If higher-rank Euler systems exist and satisfy the expected properties, the BSD formula follows: the regulator $\text{Reg}_r(\mathbf{c}^{(r)})$ in Deligne cohomology equals the leading Taylor coefficient $L^{(r)}(E,1)/r!$ up to explicit periods, Tamagawa numbers, and $|\text{III}|$. This would settle BSD for all analytic ranks.

**Status:** Unexplored

**Classification:** Speculation

---

## B-006: Euler Systems for GL(n) — Discovery and Verification

**Statement:** For a cuspidal automorphic representation $\pi$ of $GL(n)/\mathbb{A}_\mathbb{Q}$ with associated $p$-adic Galois representation $\rho_p: G_\mathbb{Q} \to GL(n, \overline{\mathbb{Q}}_p)$, does there exist an Euler system — a compatible collection of classes $\{c_m \in H^1(\mathbb{Q}(m), \rho_p)\}$ indexed by squarefree products $m$ of primes where $\pi$ is unramified — satisfying norm-compatibility $\text{Cor}_{m\ell/m}(c_{m\ell}) = P_\ell(\text{Frob}_\ell^{-1}) c_m$ where $P_\ell$ is the Hecke polynomial of $\pi$ at $\ell$? The expected structure: for $\pi = \text{sym}^{n-1} f$ with $f$ a weight-2 newform, the Euler system classes should live in the Bloch-Kato Selmer group $H^1_f(\mathbb{Q}(m), \rho_p)$ and their images under the dual exponential map should interpolate the critical $L$-values $L(\pi, 1/2)$.

**Tools needed:** Magma (Galois representations, automorphic forms), SageMath (L-functions for $GL(n)$, Langlands functoriality), PARI/GP (Artin L-functions, Dirichlet series)

**What's known:** Euler systems exist for: (i) $GL(1)$ — cyclotomic units (Thaine, Rubin), (ii) $GL(2)$ — Kato's zeta elements, Beilinson-Flach elements, (iii) $GL(2) \times GL(2)$ — Rankin-Selberg Beilinson-Flach elements (Loeffler-Zerbes), (iv) CM representations — Rubin's elliptic units. For $GL(n)$ with $n \geq 3$, the Langlands program predicts the existence of Galois representations $\rho_p$ attached to regular algebraic cuspidal automorphic $\pi$ (established for $n \leq 4$ by Taylor et al. for regular weight, and for solvable base change by Harris-Taylor). However, no Euler system is known for any $GL(n)$ representation with $n \geq 3$. The "Euler system of Rankin-Selberg type" for $GL(3) \times GL(2)$ is conjectured but unconstructed.

**Main obstacle:** (a) The geometry of Shimura varieties for $GL(n)$ ($n \geq 3$) is vastly more complicated than for $GL(2)$: the relevant Shimura varieties (e.g., Picard modular surfaces for unitary groups, or Siegel modular varieties for $GSp(2n)$) have higher-dimensional strata, and the construction of algebraic cycles generating the expected cohomology is a major open problem. (b) The Beilinson conjectures for $GL(n)$ are barely tested computationally. (c) The norm compatibility requires auxiliary level-raising at primes $\ell$, and for $GL(n)$ this involves delicate problems in the deformation theory of Galois representations.

**BSD connection:** The Bloch-Kato conjecture for $\rho_p$ (which specializes to BSD when $\rho_p$ arises from an elliptic curve) predicts that $\dim H^1_f(\mathbb{Q}, \rho_p) - \dim H^0(\mathbb{Q}, \rho_p) = \text{ord}_{s=1} L(\pi, s)$, and an Euler system would provide the upper bound. For $\pi = \text{sym}^n f$ with $f$ the automorphic form attached to $E$, the $GL(n)$ Euler system directly controls the symmetric power $L$-values relevant to BSD via the method of symmetric power functoriality.

**Status:** Unexplored

**Classification:** Conjecture

---

## B-007: The BSD Formula via Euler System Bounds

**Statement:** Let $E/\mathbb{Q}$ be an elliptic curve, $p$ a prime of good ordinary reduction, and suppose an Euler system $\{c_m\}$ for $V_p(E)$ exists with $c_1 \neq 0$ in $H^1_f(\mathbb{Q}, V_p(E))$. Then the Euler system machine produces: (1) an upper bound $\text{rk}_p \text{Sel}(E/\mathbb{Q}) \leq 1$ via the Bockstein map, (2) a formula $v_p\left(\frac{L'(E,1)}{\Omega_E}\right) = v_p\left(\hat{h}(c_1)\right) + \sum_v \text{ord}_p(c_v) + \text{ord}_p(|E(\mathbb{Q})_{\text{tors}}|^2) - \text{ord}_p(|\text{III}(E/\mathbb{Q})|)$, where $\hat{h}(c_1)$ is the $p$-adic height of the Euler system class. The precise question: given a proven Euler system bound $\text{rk}_p \text{Sel} \leq s$, does the Rubin-style formula for the leading term of the characteristic power series yield the exact BSD formula, or only an inequality $\leq$?

**Tools needed:** Magma (Selmer group computation, $p$-adic heights), PARI/GP (Iwasawa-theoretic computations), SageMath ($p$-adic L-functions, Bockstein maps)

**What's known:** Rubin (1991) proved that for CM elliptic curves, the Euler system bound gives $\text{Sel}_p(E/K)^{\text{Gal}(K/\mathbb{Q})} \leq L_p(E,1)$ exactly — the "Euler system = $p$-adic L-function" identity is the Iwasawa main conjecture. Kato (2004) proved: if $\text{Sel}(E/\mathbb{Q}) = 0$ (analytic rank 0), then the characteristic ideal of $\text{Sel}(E/\mathbb{Q}_\infty)$ divides the Katz $p$-adic L-function, yielding $v_p(|\text{III}|) \leq v_p(L(E,1)/\Omega_E)$. Combined with the Cassels-Tate constraint ($|\text{III}|$ is a perfect square), this gives $|\text{III}|[p^\infty] = L(E,1)/\Omega_E$ up to $p$-adic units. The inequality $\leq$ (not $=$) is the fundamental limitation.

**Main obstacle:** The Euler system gives an upper bound on the Selmer group, hence an upper bound on $|\text{III}|$. To obtain equality, one needs either: (a) the converse inequality from a lower bound on $|\text{III}|$ (the Cassels-Tate pairing parity argument works for rank 0 but requires $\text{III}$ to be finite), or (b) the full Iwasawa main conjecture, which would equate the characteristic ideal of $\text{Sel}$ with the $p$-adic L-function ideal. For rank $\geq 2$, neither approach closes the gap without additional input (e.g., Skinner-Urban's result for $p = 3$ under GRH).

**BSD connection:** This is the direct road from Euler systems to the BSD formula. The equality case would prove the $p$-part of BSD: $\text{ord}_p\left(\frac{L^{(r)}(E,1)}{r! \Omega R}\right) = \text{ord}_p\left(\frac{|\text{III}| \prod c_v}{|E(\mathbb{Q})_{\text{tors}}|^2}\right)$.

**Status:** Promising

**Classification:** Theorem (for $r \leq 1$); Partial Result (inequality for $r \geq 2$)

---

## B-008: p-adic L-functions from Euler Systems (Interpolation)

**Statement:** Given an Euler system $\{c_m \in H^1(\mathbb{Q}(m), T)\}$ for a Galois representation $T$ (e.g., $T = T_p(E)$ for a modular elliptic curve $E$), the "improper Euler system" machinery of Rubin and Perrin-Riou constructs a $p$-adic L-function $\mathcal{L}_p \in \Lambda = \mathbb{Z}_p[[\Gamma]]$ (where $\Gamma = 1 + p\mathbb{Z}_p$) such that for integers $k \geq 1$ with $E$ of weight $k-1$:
$$\mathcal{L}_p(\gamma^k - 1) = \left(1 - \frac{a_p}{p^k} + \frac{1}{p}\right)^{-1} \cdot \frac{L(E, k)}{\Omega_E^+} \cdot \text{(Euler factors)}$$
where $\gamma$ is a topological generator of $\Gamma$. The precise question is: can the interpolation factor be made explicit and the $p$-adic L-function be shown to generate the characteristic ideal of the Pontryagin dual of $\text{Sel}(E/\mathbb{Q}_\infty)$ (i.e., the Iwasawa main conjecture for the cyclotomic tower)?

**Tools needed:** PARI/GP ($p$-adic L-function computation, Iwasawa algebra), SageMath (Fourier coefficients of modular forms, $p$-adic regulators), Magma (Iwasawa theory computations)

**What's known:** For $E$ with good ordinary reduction at $p$, Kato's Euler system produces $\mathcal{L}_p^{\text{Kato}} \in H^1(I_\mathbb{Q}, \hat{T})$ (in the Iwasawa cohomology) via the Perrin-Riou $p$-adic regulator $\mathcal{L}_{\text{PR}}: H^1_f(\mathbb{Q}_p, T \otimes \Lambda) \to \Lambda$. The interpolation property is: the specialization of $\mathcal{L}_p^{\text{Kato}}$ at the trivial character recovers $L(E,1)/\Omega_E$ (times explicit fudge factors) when $a_p \neq 1$. For supersingular $E$ ($a_p = 0$), Pollaccio's construction or the use of a Shimura curve over a totally real field yields a two-variable $p$-adic L-function in $\Lambda \hat\otimes \mathbb{Z}_p[[\text{Gal}(K_\infty/K)]]$. Perrin-Riou's explicit reciprocity law converts the Euler system to the $p$-adic L-function.

**Main obstacle:** (a) The interpolation factor involves the $p$-adic period $\Omega_p(E) = \log_p(\hat\omega)$ (the $p$-adic formal group logarithm of the Néron differential), and relating this to the archimedean period $\Omega_\infty(E)$ requires the $p$-adic Hodge theory comparison (Fontaine's $\mathcal{D}_{\text{dR}}$/$\mathcal{D}_{\text{cris}}$ functor). The "fudge factor" is explicit but complicated. (b) The main conjecture requires that $\mathcal{L}_p$ is a unit multiple of the characteristic element — this is known by Skinner-Urban for $p = 3$ and $E$ with $a_p \not\equiv p+1 \pmod{p^2}$, but remains open in general. (c) For supersingular primes, the two-variable approach introduces analytic continuation questions.

**BSD connection:** The $p$-adic L-function encodes the BSD formula: its order of vanishing at the trivial character is $\text{rk}(E(\mathbb{Q}))$, and its leading coefficient is $L^{(r)}(E,1)/r! \cdot \Omega_p^{-r} \cdot (\text{correction factors})^{-1}$. The main conjecture equates this with $|\text{III}[p^\infty]| \cdot \prod c_v^{(p)} / |E(\mathbb{Q})_{\text{tors}}|_p^2$.

**Status:** Promising

**Classification:** Theorem (interpolation property); Partial Result (main conjecture in some cases)

---

## B-009: Rubin's Method and Selmer Group Bounds

**Statement:** Rubin's method (1991) for bounding Selmer groups from Euler systems proceeds via a three-step argument: (1) define the "Euler system ideal" $\mathcal{Z} = \text{char}_\Lambda(\text{image of } \{c_m\} \text{ in } H^1_\Sigma(K, T \otimes \Lambda))$, (2) prove the "bounding inequality" $\mathcal{Z} \subseteq \text{char}_\Lambda(\text{Sel}(T/K_\infty)^\vee)$ using the Bockstein homomorphism and the global duality pairing, (3) deduce $\dim_{\mathbb{F}_p} \text{Sel}(T/K)[p] \leq \text{length}_\Lambda(\Lambda/\mathcal{Z})$. The precise question is: for which representations $T$ and fields $K$ does Rubin's method yield a sharp bound, i.e., $\mathcal{Z} = \text{char}_\Lambda(\text{Sel}^\vee)$ (equality, not just inclusion)?

**Tools needed:** Magma (Galois cohomology, Selmer groups, Bockstein maps), SageMath (Iwasawa algebra computations, structure theory of $\Lambda$-modules), Lean 4 (formalization of the bounding argument)

**What's known:** Rubin proved equality $\mathcal{Z} = \text{char}_\Lambda(\text{Sel}^\vee)$ in the following cases: (a) $T = T_p(E)$ for $E$ with CM by $K$ and $p$ split in $K$ (the CM case), (b) $T = \mathbb{Z}_p(1)$ (cyclotomic units and the classical main conjecture). For non-CM elliptic curves, Kato's Euler system gives $\subseteq$ (the inclusion), and equality requires additional input from the Galois deformation theory (Skinner-Urban). The method applies to any representation $T$ with an Euler system, but the bound is sharp only when: (i) the local conditions at primes $v \mid p$ are "geometrically defined" (Bloch-Kato $H^1_f$), (ii) the prime-to-$p$ Selmer conditions match the Euler system support, and (iii) the Euler system is "non-degenerate" (the image spans a full-rank submodule).

**Main obstacle:** (a) For non-CM curves, the local-global compatibility at $p$ (needed to match the Euler system's local image with the Bloch-Kato condition) requires results from $p$-adic Hodge theory that are only available when $E$ has good ordinary reduction at $p$ and $a_p \not\equiv 1 \pmod{p}$. (b) The "non-degeneracy" of the Euler system is a subtle condition: it requires that the Kolyvagin derivative classes $\kappa_\ell \in H^1(K, E[p])$ for primes $\ell$ where $E$ has good reduction and $\ell \equiv 1 \pmod{p}$ span a subspace of dimension equal to $\text{rk}(E(\mathbb{Q}))$. For $r = 0$, non-degeneracy is automatic; for $r = 1$, it follows from the Gross-Zagier formula; for $r \geq 2$, it is completely open. (c) The equality $\mathcal{Z} = \text{char}(\text{Sel}^\vee)$ requires $\text{III}(E/\mathbb{Q})[p^\infty]$ to be finite, which is what one is trying to prove.

**BSD connection:** Rubin's method, when sharp, directly yields the $p$-part of BSD: the characteristic ideal equality encodes both the rank equality and the leading-term formula. Specifically, if $\mathcal{Z} = (L_p(E))$ in $\Lambda$, then specializing at the augmentation ideal gives $v_p(L(E,1)/\Omega_E) = v_p(|\text{III}| \cdot \prod c_v / |E(\mathbb{Q})_{\text{tors}}|^2)$.

**Status:** Promising

**Classification:** Theorem (CM case); Partial Result (non-CM, ordinary, rank $\leq 1$)

---

## B-010: Euler Systems and Iwasawa Main Conjectures

**Statement:** The Iwasawa Main Conjecture (IMC) for a $p$-adic representation $T$ over a number field $F$ states: $\text{char}_\Lambda(\text{Sel}(T/F_\infty)^\vee) = (L_p(T))$ where $F_\infty/F$ is a $\mathbb{Z}_p$-extension, $\Lambda = \mathbb{Z}_p[[\text{Gal}(F_\infty/F)]]$, $\text{Sel}(T/F_\infty)$ is the Pontryagin dual of the Selmer group, and $L_p(T) \in \Lambda$ is the $p$-adic L-function. Euler systems are the primary tool for proving $\supseteq$ (the characteristic ideal divides the $p$-adic L-function). The precise direction: for which combinations of $(T, F, F_\infty)$ can Euler systems prove the full IMC (equality, not just divisibility), and what additional hypotheses (e.g., GRH, the $p$-part of the Leopoldt conjecture, the non-vanishing of certain $\mu$-invariants) are required?

**Tools needed:** Magma (Iwasawa modules, characteristic ideals), PARI/GP (p-adic L-functions, class field towers), SageMath (Iwasawa algebra structure), Lean 4 (formal verification of the main conjecture for specific cases)

**What's known:** Euler systems have proven the IMC for: (i) $T = \mathbb{Z}_p(1)$ over $\mathbb{Q}$ — Mazur-Wiles (1984), using cyclotomic units, (ii) $T = T_p(E)$ for CM $E/K$, $p$ split in $K$ — Rubin (1991), using elliptic units, (iii) $T = T_p(f)$ for weight-2 modular forms, $p$ ordinary — Kato (2004), proving $\subseteq$ with equality conditional on $p$-adic Hodge-theoretic input, (iv) $T = \text{ad}^0(T_p(f))$ — Skinner-Urban (2014) for $p = 3$ under GRH, using the Eisenstein ideal. The $\subseteq$ direction (Euler system bound) is unconditional in all cases; the $\supseteq$ direction (lower bound on Selmer group) requires either: the $p$-adic Hodge theory input (Fontaine-Laffaille, ordinary case) or the Galois deformation theory of the $\text{ad}^0$ representation plus modularity of the associated eigenvariety.

**Main obstacle:** (a) For supersingular primes, the Iwasawa algebra has a different structure (the $\mu$-invariant may be positive, and the $\Lambda$-module structure of $\text{Sel}^\vee$ is more complicated). Kobayashi's $\pm$-Selmer groups require separate treatment. (b) The $\supseteq$ direction for non-CM curves beyond $p = 3$ requires new techniques in the deformation theory of Galois representations. (c) For totally real fields $F \neq \mathbb{Q}$, the modularity of Galois representations is less complete (known for $F$ of small degree by work of Taylor et al.), and the Euler system must be constructed from Hilbert modular forms. (d) The Greenberg conjecture ($\mu = 0$ for $\mathbb{Z}_p$-extensions of CM fields) is needed for the cleanest formulation but remains unproven.

**BSD connection:** The IMC, together with the interpolation property of the $p$-adic L-function, implies the $p$-part of the BSD formula. Specifically, if $\text{char}_\Lambda(\text{Sel}^\vee) = (L_p)$, then specializing at the trivial character $s = 0$ gives $L_p(0) = L(E,1)/\Omega_E \times (\text{fudge factors})$, and the length of $\text{Sel}^\vee / (L_p(0))$ encodes $|\text{III}[p^\infty]| \cdot \prod c_v^{(p)} / |E(\mathbb{Q})_{\text{tors}}|_p^2$.

**Status:** Promising

**Classification:** Theorem (several cases); Partial Result (general case)

---

## B-011: Syntomic Regulators and Euler System Classes

**Statement:** For a smooth proper variety $X/\mathbb{Z}_p$ and a cycle class $\alpha \in \text{CH}^r(X, k)$ in higher Chow groups (or equivalently, motivic cohomology $H^{2r-k}_{\mathcal{M}}(X, \mathbb{Q}(r))$), the syntomic regulator is a map $\text{reg}_{\text{syn}}: H^{2r-k}_{\mathcal{M}}(X, \mathbb{Q}(r)) \to H^r_{\text{syn}}(X/\mathbb{Z}_p, k)$ where the target is Besser's syntomic cohomology, an extension of Fontaine-Messing's crystalline cohomology theory that works for varieties over $\mathbb{Z}_p$ (not just $\mathbb{F}_p$). For Euler system classes arising from modular curves $X_0(N)$, the precise question is: (a) can Kato's zeta elements $z_k^{(p)} \in H^1(\mathbb{Q}_p, V_p(E))$ be lifted to syntomic classes $\tilde{z}_k \in H^1_{\text{syn}}(\text{Spec}(\mathbb{Z}_p), T_p(E) \otimes \mathbb{Q}_p)$, and (b) does the syntomic regulator recover the Perrin-Riou $p$-adic regulator $\mathcal{L}_{\text{PR}}$?

**Tools needed:** SageMath ($p$-adic Hodge theory computations, syntomic cohomology), Magma (crystalline cohomology, comparison maps), Lean 4 (formalization of syntomic cohomology)

**What's known:** Besser (1999, 2003) constructed syntomic cohomology for smooth varieties over $W(k)$ (the ring of Witt vectors) and proved that the syntomic regulator factors through the motivic-to-étale regulator. For modular curves, Kings and Loeffler-Zerbes computed the syntomic regulator on Beilinson-Flach elements explicitly and showed it matches the Perrin-Riou regulator. The connection to $p$-adic L-functions: $\text{reg}_{\text{syn}}(\text{BF}_{f,g}) = \mathcal{L}_p(f,g)$ in the Iwasawa algebra, where $\mathcal{L}_p(f,g)$ is the Rankin-Selberg $p$-adic L-function. For higher Chow cycles on $X_0(N)$, the syntomic regulator of Beilinson's Eisenstein classes gives the $p$-adic L-function of the symmetric square of $f$.

**Main obstacle:** (a) The syntomic cohomology groups $H^1_{\text{syn}}(\text{Spec}(\mathbb{Z}_p), T)$ for $T = T_p(E)$ are finite-dimensional $\mathbb{Q}_p$-vector spaces, and the regulator lands in a subspace determined by the Hodge filtration on $D_{\text{dR}}(T)$. The dimension constraint means that not all Euler system classes can lift — one needs a "crystalline" condition. (b) The explicit computation of syntomic regulators for general (non-Eisenstein) cycles on modular curves is extremely difficult; Besser's algorithmic approach requires $p$-adic analytic continuation of the $p$-adic polylogarithm. (c) For $r \geq 2$ (higher rank), the syntomic cohomology is not well-understood: the expected $H^2_{\text{syn}}$ groups have not been computed for any variety.

**BSD connection:** The syntomic regulator provides the bridge between motivic cohomology (where Euler system classes live geometrically) and $p$-adic L-functions (which encode BSD). If $\text{reg}_{\text{syn}}$ is injective on the relevant motivic cohomology group, then the non-vanishing of the Euler system class implies the non-vanishing of $\mathcal{L}_p$ at the central point, which by the main conjecture (B-010) implies the BSD leading-term formula.

**Status:** In Progress

**Classification:** Theorem (for Beilinson-Flach elements); Partial Result (for general Euler system classes)

---

## B-012: Explicit Computation of Euler System Classes (SageMath/Magma)

**Statement:** For a modular elliptic curve $E/\mathbb{Q}$ of conductor $N$ and a prime $p \nmid 6N$ of good ordinary reduction, explicitly compute Kato's zeta element $z^{(p)} \in H^1(\mathbb{Q}, V_p(E))$ and its images under localization at small primes $\ell \mid N$ and $\ell = p$. The computational goals are: (1) express the class $z^{(p)}$ as a cocycle $\sigma \mapsto z_\sigma \in V_p(E)$ for $\sigma \in G_\mathbb{Q}$, (2) compute the $p$-adic height $\hat{h}_p(z^{(p)}) \in \mathbb{Q}_p$, (3) verify the interpolation formula $\exp^*_{V_p(E)}(\text{loc}_p(z^{(p)})) = \left(1 - \frac{a_p}{p} + \frac{1}{p}\right)^{-1} \cdot \frac{L(E,1)}{\Omega_E} \in \mathbb{Q}_p$, (4) compute the Kolyvagin derivative classes $d_\ell \in H^1(\mathbb{Q}, E[p])$ for primes $\ell$ with $\ell \equiv 1 \pmod{p}$ and $\text{ord}_\ell(N) \leq 1$.

**Tools needed:** SageMath (modular symbols, $p$-adic heights via Mazur-Tate-Teitelbaum, Kolyvagin derivative classes), Magma (Euler system computation via modular abelian varieties, Heegner point computation), PARI/GP (high-precision $p$-adic L-functions)

**What's known:** The computation of Kato's Euler system has been carried out for specific curves:
- Cremona's database provides $L(E,1)/\Omega_E$ for all curves of conductor $\leq 10^8$.
- Dokchitser's `tim Dok` package computes $L^{(r)}(E,1)$ to arbitrary precision.
- Magma's `EulerSystem` package (under development by David Loeffler) computes the image of Kato's class in $H^1(\mathbb{Q}_p, V_p(E))$ for curves of small conductor.
- The $p$-adic heights $\hat{h}_p$ have been computed by Balakrishnan-Dogra-Müller-Tuitman-Vonk using $p$-adic integration on $X_0(N)$ (the "quadratic Chabauty" method).
- For specific curves (e.g., 11a1, 37a1, 43a1, 5077a1), the Kolyvagin derivative classes and their local images at $p$ have been computed explicitly.

**Main obstacle:** (a) The computation of $z^{(p)}$ as an actual cocycle requires modular symbols at level $Np^k$ for $k \gg 1$, which is computationally expensive for large $N$ or $p$. The space of modular symbols of level $Np^k$ has dimension growing like $Np^k$, so $k = 10$ already gives level $\sim 10^{12}$ for typical inputs. (b) The $p$-adic height $\hat{h}_p$ requires the $p$-adic sigma function (or equivalently, the formal group logarithm on a $p$-adic covering of $E(\mathbb{Q}_p)$), which is computed via $p$-adic integration with precision issues. (c) The Kolyvagin derivative $d_\ell = \sum_{i=0}^{p-2} i \cdot \sigma_\ell^i(c_\ell)$ requires the "Kolyvagin prime" $\ell$ to have $\text{Frob}_\ell$ of order exactly $p-1$ on $E[p]$, and the cocycle $c_\ell$ at level $\ell$ must be computed explicitly. (d) Verification of the BSD formula requires $|\text{III}(E/\mathbb{Q})[p^\infty]|$, which is only computable when it is finite.

**BSD connection:** This direction is the explicit verification laboratory for BSD: compute both sides of the BSD formula $L^{(r)}(E,1)/r! = \Omega R |\text{III}| \prod c_v / |E(\mathbb{Q})_{\text{tors}}|^2$ numerically and verify equality. The Euler system computation provides the $p$-adic side (the Selmer group bound and the $p$-adic height), while the analytic computation provides the $L$-value side. Agreement is evidence for BSD; disagreement would disprove it.

**Status:** In Progress

**Classification:** Experiment

---

# Research Directions — Group C: Arithmetic Statistics

**12 directions studying average behavior of ranks, Sha, and L-functions over families of elliptic curves.**

---

## C-001: Average Rank ≤ 1/2 for Quadratic Twist Families (Bhargava-Shankar)

### Statement

Prove that for any elliptic curve $E/\mathbb{Q}$, the average rank of its quadratic twists $E^{(D)}$ as $|D| \to \infty$ (over fundamental discriminants $D$ ordered by absolute value) is at most $1/2$, i.e.,
$$\limsup_{X \to \infty} \frac{\sum_{\substack{|D| \leq X \\ D \text{ fundamental}}} \operatorname{rank}(E^{(D)})}{\#\{D : |D| \leq X,\, D \text{ fundamental}\}} \leq \frac{1}{2}.$$
Equivalently, show that at least 50% of quadratic twists have analytic (and algebraic) rank 0, and at most 50% have rank 1.

### Tools Needed

- Bhargava's geometry-of-numbers methods for counting orbits in prehomomorphic representations
- 2-descent and the connection between 2-Selmer ranks and orbits of class group elements
- Kolyvagin's theorem: analytic rank ≤ 1 implies algebraic rank = analytic rank
- Expander graph arguments (Bhargava-Shankar) to bound average 2-Selmer rank

### What's Known

- **Bhargava-Shankar (2015):** Average 2-Selmer rank $\leq 3$ over all elliptic curves ordered by height. For quadratic twists of a fixed curve $E$, average 2-Selmer rank $\leq 2$ (implied by Selmer group bounds).
- **Bhargava-Shankar (2015):** Average rank of all elliptic curves (ordered by height) is at most $0.885$ (later refined).
- **Smith (2022):** For $E = X_0(32a1)$ and similar base curves, 100% of twists have rank 0 or 1, conditional on GRH + finiteness of Sha, via a parity-based approach.
- **Kane (2013):** Unconditional upper bound of $1/2 + o(1)$ on average analytic rank in certain families, conditional on GRH for Dirichlet L-functions.
- **Heath-Brown (1993):** For $E: y^2 = x^3 - x$, average rank of twists is at most 2 (unconditional).

### Main Obstacle

The 2-Selmer group captures only 2-power torsion in Sha. A curve could have rank 0 but large 2-part of Sha, inflating the 2-Selmer rank. Controlling the 2-torsion in Sha uniformly across a family — or extracting rank information despite this — remains the core difficulty. The expander graph argument of Bhargava-Shankar gives average 2-Selmer rank $\leq 2$ but bridging from 2-Selmer rank to actual rank requires excluding the contribution from $\text{Sha}[2]$.

### BSD Connection

If average rank $\leq 1/2$ is established and the non-negativity conjecture ($\operatorname{rank} \geq 0$) holds, then rank 0 curves must constitute at least 50% of the family. By Kolyvagin's theorem, rank 0 and analytic rank 1 curves satisfy weak BSD. This would show that weak BSD holds for a positive-density family, with the full BSD formula governing the leading coefficient.

### Status

**Partial results established; full bound open.** Average 2-Selmer rank $\leq 2$ is proven for quadratic twist families. Conditional on GRH, average analytic rank $\leq 1/2$ for certain families. Unconditional average rank $\leq 1/2$ remains open for general base curves.

### Classification

**Conjecture** — supported by extensive computational evidence and partial theoretical results.

---

## C-002: The Goldfeld Conjecture: 100% of Curves Have Rank ≤ 1

### Statement

Prove that 100% of elliptic curves $E/\mathbb{Q}$ (ordered by conductor $N_E$, or equivalently by naive height $H(E) = \max(|A|^3, |B|^2)$ for the minimal model $y^2 = x^3 + Ax + B$) have algebraic rank 0 or 1. Formally:
$$\lim_{X \to \infty} \frac{\#\{E : H(E) \leq X,\, \operatorname{rank}(E(\mathbb{Q})) \geq 2\}}{\#\{E : H(E) \leq X\}} = 0.$$
Goldfeld (1979) conjectured that 50% have rank 0 and 50% have rank 1, with 0% having rank $\geq 2$.

### Tools Needed

- Bhargava-Shankar: average 2-Selmer rank bounds via geometry of numbers
- Bhargava-Kane-Lenstra-Poonen-Rouse: average 2-Selmer rank = 3 over all elliptic curves (proven)
- Parity conjecture: root number determines parity of rank
- Deuring's theorem on distribution of Frobenius traces (Sato-Tate for non-CM curves)

### What's Known

- **Bhargava-Shankar (2015):** Average 2-Selmer rank $\leq 3$, implying average rank $\leq 0.885$ (using $r \leq s_2 - \delta$ where $\delta$ accounts for Sha).
- **Bhargava-Kane-Lenstra-Poonen-Rouse (2023):** Average 2-Selmer rank $= 3$ exactly, with explicit distribution: $\Pr(s_2 = 0) = 1/4$, $\Pr(s_2 = 1) = 1/4$, $\Pr(s_2 = 2) = 15/64$, etc.
- **Bhargava-Shankar (2015):** At least 66.48% of curves have rank 0 or 1 (complementary to the average rank bound).
- **Smith (2022):** For families of quadratic twists of a fixed curve, 100% have rank $\leq 1$, conditional on GRH and finiteness of Sha[2∞].
- **Delaunay-Watkins:** Computational verification that rank distribution matches $\Pr(r=0) \approx 47.5\%$, $\Pr(r=1) \approx 47.5\%$, $\Pr(r=2) \approx 5\%$ (for curves of conductor up to $10^8$).

### Main Obstacle

The gap between Selmer rank and actual rank. The 2-Selmer group has average size $2^3 = 8$, but $\operatorname{rank} \leq s_2 - 2\dim_2 \text{Sha}[2]$. Showing that Sha[2] is "usually trivial" or that it accounts for the right correction is the key bottleneck. The distribution of 2-Selmer ranks is now fully understood, but the map from Selmer rank to rank involves the unknown distribution of $\text{Sha}[2^\infty]$.

### BSD Connection

The Goldfeld conjecture is a distributional refinement of BSD. If 100% of curves have rank $\leq 1$, then BSD is known for 100% of curves (by Kolyvagin + Gross-Zagier). The strong BSD formula then applies to the generic curve. The conjecture implies that the "interesting" cases of BSD (rank $\geq 2$) form a density-zero set.

### Status

**Open conjecture.** Best unconditional result: average rank $\leq 0.885$ (Bhargava-Shankar). Best conditional: 100% of rank $\leq 1$ for twist families (Smith, conditional on GRH + Sha finiteness). The analogous statement over function fields is known (Duke-Kowalski).

### Classification

**Conjecture** — the central open problem in arithmetic statistics of elliptic curves.

---

## C-003: Cohen-Lenstra Heuristics for Tate-Shafarevich Groups

### Statement

Predict and verify the distribution of $\text{III}(E/\mathbb{Q})$ as $E$ varies over families of elliptic curves. The Cohen-Lenstra philosophy (originally for class groups of quadratic fields) predicts that for an odd prime $p$, the probability that $p | \#\text{III}(E/\mathbb{Q})$ is:
$$\Pr(p \mid \#\text{III}) = 1 - \prod_{i=1}^{\infty} (1 - p^{-2i}) = \frac{1}{p} + \frac{1}{p^2} - \frac{1}{p^5} - \cdots$$
and more generally, the distribution of $\text{III}[p^k]$ should follow a specific measure on finite abelian $p$-groups weighted by $1/|\text{Aut}|$.

### Tools Needed

- Cassels-Tate pairing: $\text{III}$ is a non-degenerate alternating pairing, so $\#\text{III}$ is a perfect square
- Root number parity: $(-1)^{\operatorname{rank}} = w(E) = \pm 1$, and $\#\text{III} \equiv (-1)^{r/2} \pmod{?}$ (parity constraints)
- Delaunay's refinement: Cohen-Lenstra heuristics adapted to account for the Cassels pairing structure
- Descent methods to compute $\text{III}[p^k]$ for individual curves

### What's Known

- **Cohen-Lenstra (1984):** Original heuristics for class groups, extended by Cohen-Martinet to number fields.
- **Delaunay (2001, 2007):** Refined heuristics for $\text{III}$ of elliptic curves, accounting for the Cassels-Tate pairing. Predicts $\Pr(\text{III}[p] \cong (\mathbb{Z}/p)^{2k}) = \frac{1}{|(\mathbb{Z}/p)^{2k}| \cdot |\text{Aut}((\mathbb{Z}/p)^{2k})|} \cdot (\text{normalizing constant})$.
- **Watkins (2008):** Extensive computational verification for curves of conductor $\leq 10^8$: distribution of $\#\text{III}$ matches Cohen-Lenstra-Delaunay predictions.
- **Klagsbrun-Sherman (2021):** Average size of $|\text{III}[p]|$ in families of quadratic twists of a fixed curve, conditional on standard conjectures.

### Main Obstacle

The Cassels-Tate pairing forces $\#\text{III}$ to be a perfect square, imposing global constraints not present in the original Cohen-Lenstra setting. Moreover, Sha is linked to rank via BSD ($\#\text{III}$ appears in the leading coefficient), so the distribution of $\text{III}$ is coupled to the rank distribution. Proving unconditional distributional results for $\text{III}$ in any family remains entirely open — even showing that $\Pr(\#\text{III} > n) \to 0$ as $n \to \infty$ in a suitable sense is hard.

### BSD Connection

The order of $\text{III}$ appears directly in the BSD formula:
$$\frac{L^{(r)}(E,1)}{r!} = \frac{\Omega \cdot R \cdot |\text{III}| \cdot \prod c_v}{|E(\mathbb{Q})_{\text{tors}}|^2}.$$
Understanding the distribution of $|\text{III}|$ is equivalent (assuming the rest of BSD) to understanding the distribution of $L^{(r)}(E,1)/r!$ among curves of fixed rank. The Cohen-Lenstra heuristics thus give a statistical refinement of BSD.

### Status

**Conjectural heuristics, computationally well-verified.** No unconditional proof of distributional results for $\text{III}$ in any family. Conditional results exist under GRH and finiteness of Sha.

### Classification

**Conjecture** — heuristics with strong computational support, no theoretical proof.

---

## C-004: Moments of L-functions and Rank Distribution

### Statement

Compute the $k$-th moment of central L-values (or derivatives) of elliptic curve L-functions over families:
$$M_k(f, X) = \sum_{\substack{E \in \mathcal{F}(X)}} L^{(j)}(E, 1)^k$$
where $\mathcal{F}(X)$ is a family of elliptic curves ordered by conductor/height up to $X$, and $j$ depends on the parity of the family. The conjectural formula (Katz-Sarnak, Keating-Naor) predicts specific asymptotics involving products of zeta functions and L-functions. The first two moments determine average rank and rank variance.

### Tools Needed

- Approximate functional equation: $L(E,1) = 2 \sum_{n=1}^{N} \frac{a_n(E)}{\sqrt{n}} W(n/N)$ (smooth cutoff $W$)
- Spectral theory of automorphic forms: the $a_n(E)$ are Fourier coefficients of weight-2 newforms
- The Petersson trace formula and Kuznetsov formula for sums of Fourier coefficients over families
- Random matrix theory (Katz-Sarnak) for prediction of moment asymptotics

### What's Known

- **First moment ($k=1$):** Duke (1995), Perelli-Pitou: $\sum_{|D| \leq X} L(E^{(D)}, 1) \sim c \cdot X \log X$ for quadratic twists. This gives the average central value.
- **Second moment ($k=2$):** Soundararajan (2000), Young (2011): $\sum_{|D| \leq X} L(E^{(D)}, 1)^2 \sim c' \cdot X (\log X)^2$. This determines the variance of central values and (via the recipe) the variance of analytic ranks.
- **Higher moments:** Third moment known in limited cases (Young). Fourth moment and above: conjectural formulas exist (Conrey-Keating-Rubinstein-Snaith) but are unproven.
- **Sign changes of $a_p(E)$:** Kowalski-Michel-VanderKam: distribution of $a_p$ over families of twists follows Sato-Tate.

### Main Obstacle

Beyond the second moment, the approximate functional equation produces off-diagonal terms that require subconvexity estimates for twisted L-functions of degree $\geq 4$ (as Rankin-Selberg convolutions). The spectral methods that work for the first two moments encounter arithmetic sums that are not amenable to current analytic techniques for $k \geq 3$.

### BSD Connection

The moments of $L(E,1)$ (for rank 0 curves) and $L'(E,1)$ (for rank 1 curves) are precisely the moments of the leading BSD coefficient (divided by $\Omega \cdot \prod c_v / |E_{\text{tors}}|^2$). The $k$-th moment encodes the $k$-th moment of $|\text{III}| \cdot R$ among curves of a given rank. Higher moments would give fine information about the distribution of Sha and regulators.

### Status

**First and second moments established in key families; higher moments open.** Conjectural recipes for all moments exist (Conrey-Keating-Rubinstein-Snaith) and are verified computationally.

### Classification

**Partial results / Conjecture** — first two moments proven, higher moments conjectural.

---

## C-005: 100% of Curves Satisfy BSD (Rank 0 and 1) — Effective Versions

### Statement

Prove that for 100% of elliptic curves $E/\mathbb{Q}$ (ordered by conductor $N_E \leq X$ as $X \to \infty$), the full BSD conjecture holds:
$$\frac{L^{(r)}(E,1)}{r!} = \frac{\Omega_E \cdot R_E \cdot |\text{III}(E/\mathbb{Q})| \cdot \prod_{v} c_v}{|E(\mathbb{Q})_{\text{tors}}|^2}.$$
For rank 0 and 1 curves, this combines Gross-Zagier, Kolyvagin, and Skinner-Urban's results. The goal is to make this effective: give an explicit density $1 - O(X^{-\delta})$ for the set of curves satisfying BSD.

### Tools Needed

- Gross-Zagier formula: $L'(E,1) = c \cdot \hat{h}(P)$ for the Heegner point $P$
- Kolyvagin's descent: Heegner point non-vanishing implies rank 1 and finite Sha
- Skinner-Urban (2014): Main conjecture of Iwasawa theory for $\operatorname{GL}_2$ implies BSD for rank 0 curves with $p \nmid |\text{III}[p^\infty]|$
- Effective Chebotarev density theorem (GRH-dependent)

### What's Known

- **Skinner-Urban (2014):** For $E/\mathbb{Q}$ with $\operatorname{rank} E(\mathbb{Q}) = 0$, $w(E) = +1$, and $p$ an odd prime with $p \nmid 6N_E$, if $a_p(E) \not\equiv p+1 \pmod{p}$ and $E[p]$ is irreducible, then $p \nmid |\text{III}[p^\infty]|$, so the $p$-part of BSD holds.
- **Combined (Gross-Zagier + Kolyvagin + Skinner-Urban):** BSD is known for all curves with analytic rank $\leq 1$ satisfying mild local conditions (the "generic" rank 0 and 1 curves).
- **Remaining exceptions:** Curves with $E[p]$ reducible, or with $a_p(E) \equiv p+1 \pmod{p}$ (anomalous primes), or with $\operatorname{III}[p^\infty]$ potentially nontrivial. These have density 0 but no uniform effective bound is known.

### Main Obstacle

The local conditions in Skinner-Urban's theorem (irreducibility of $E[p]$, non-anomalousness) fail for density-zero sets, but no single prime $p$ works for all curves. To get a density-1 statement, one needs either: (a) a uniform bound showing the exceptional set has density 0 (not just that each curve has "some good prime"), or (b) results for multiple primes simultaneously. Making the density effective requires GRH.

### BSD Connection

This is the most direct arithmetic-statistics approach to BSD: showing that the conjecture is true for essentially all curves, with the exceptional set being negligible. It builds on the known cases of BSD (rank 0, 1) and extends them to a measure-theoretic statement about the entire moduli space.

### Status

**Conditionally proven for density-1 set; unconditional density-1 is open.** Under GRH + standard conjectures on Galois representations, BSD holds for 100% of rank 0 and 1 curves. The unconditional statement requires handling the anomalous prime issue uniformly.

### Classification

**Partial results** — conditional on GRH and standard conjectures, effective unconditional version is open.

---

## C-006: Average Tamagawa Numbers in Families

### Statement

Compute the average value of the product of Tamagawa numbers $\prod_{p \mid N_E} c_p(E)$ over families of elliptic curves $E/\mathbb{Q}$ ordered by conductor or height. Specifically:
$$\lim_{X \to \infty} \frac{1}{\#\mathcal{F}(X)} \sum_{E \in \mathcal{F}(X)} \prod_{p \mid N_E} c_p(E) = C_{\mathcal{F}}$$
for an explicit constant $C_{\mathcal{F}}$ depending on the family. The Tamagawa numbers $c_p = [E(\mathbb{Q}_p) : E_0(\mathbb{Q}_p)]$ measure the component group at bad primes.

### Tools Needed

- Kodaira-Néron classification: $c_p$ determined by the type of bad reduction (additive, split/non-split multiplicative)
- Ogg's formula: conductor exponent $f_p = v_p(N_E) = 1 + \delta_p + n_p$ relating reduction type to conductor
- Local Tate uniformization: for multiplicative reduction, $c_p = -v_p(j(E))$ (split) or $\leq 2 \cdot |v_p(j(E))|$ (non-split)
- Siegel mass formulas for counting curves with prescribed local data

### What's Known

- **Bhargava-Shankar (2015):** In the course of bounding average rank, they compute the average of $2^{\omega(N_E)}$ (number of bad primes) and related quantities. The Tamagawa product appears but is not isolated.
- **Dokchitser-Dokchitser (2010):** Local arithmetic of Tamagawa numbers: explicit formulas for $c_p$ in terms of Tate curve parameters.
- **Lang-Trotter (1976):** Heuristics for average values of arithmetic invariants ordered by conductor.
- **Computational data (LMFDB):** For curves of conductor $\leq 10^5$, the distribution of $\prod c_p$ is available and matches predictions.

### Main Obstacle

Tamagawa numbers depend on the precise local reduction type at each bad prime, which involves subtle arithmetic (e.g., whether reduction is split or non-split multiplicative). Averaging over families requires summing $c_p$ over all possible reduction types at each prime, weighted by their density — this is a multi-dimensional sieve problem that has not been carried out systematically.

### BSD Connection

The Tamagawa product $\prod c_v$ appears directly in the BSD formula. Understanding its average value is necessary to convert average central L-value results (C-004) into average information about $|\text{III}| \cdot R$. If the average Tamagawa product is $C_{\text{Tam}}$, then from the first moment of L-values and the BSD formula, one deduces average information about $|\text{III}| \cdot R / |E_{\text{tors}}|^2$.

### Status

**Partial results.** Average Tamagawa numbers computed for specific families (e.g., quadratic twists of a fixed curve). General family averages involve open sieving problems.

### Classification

**Experiment / Partial results** — computational data available, theoretical framework partially developed.

---

## C-007: Distribution of Analytic Ranks via Random Matrix Theory

### Statement

Use the Katz-Sarnak philosophy to predict the distribution of analytic ranks of elliptic curves in families, via the distribution of the order of vanishing of characteristic polynomials of random matrices from classical compact groups. For a family $\mathcal{F}$ with symmetry type $\mathcal{G} \in \{O, SO(\text{even}), SO(\text{odd}), Sp, U\}$, the proportion of curves with analytic rank $r$ should equal:
$$\Pr(\operatorname{ord}_{s=1} \det(I - A) = r)$$
where $A$ is drawn from the Haar measure on $\mathcal{G}$ (or its $N \to \infty$ limit).

### Tools Needed

- Katz-Sarnak density theorem: zeros near $s=1$ of L-functions in a family follow the distribution of eigenvalues near 1 of the corresponding classical group
- Keating-Snaith: moments of characteristic polynomials of random matrices
- Explicit formulas relating $\operatorname{ord}_{s=1} L(E,s)$ to sums over zeros
- The $n$-level density statistics of L-function families (Ozlu-Srebro, Rubinstein, etc.)

### What's Known

- **Katz-Sarnak (1999):** Proved that for function field families, the distribution of low-lying zeros matches random matrix predictions. For number field families, the 1-level density is proven in many cases.
- **Rubinstein (2001):** Computed 1-level densities for the family of all elliptic curves; results consistent with symplectic symmetry ($Sp$, predicting even-order vanishing as dominant).
- **Bhargava-Shankar:** The average 2-Selmer rank = 3 is consistent with symplectic symmetry predictions.
- **Watkins (2004):** Computation of $a_p$ for millions of curves, verifying Sato-Tate and low-lying zero statistics.
- **Conrey-Keating-Rubinstein-Snaith (2016):** Explicit predictions for rank distributions from random matrix theory, including the prediction that $\Pr(r \geq 4) \sim 0$ (consistent with Goldfeld).

### Main Obstacle

The random matrix predictions for rank distribution (as opposed to zero statistics) involve averages of characteristic polynomials at the edge, which are more delicate than bulk statistics. The 1-level density detects the symmetry type but does not directly give the rank distribution — one needs to take limits of increasing matrix size, which involves understanding the rate of convergence in the Katz-Sarnak correspondence.

### BSD Connection

If the random matrix prediction is correct and 100% of curves have rank $\leq 1$ (consistent with symplectic symmetry), then BSD holds for 100% of curves. The distribution of the leading BSD coefficient $L^{(r)}(E,1)/r!$ among rank-$r$ curves is also predicted by random matrix theory (via the distribution of the first derivative of the characteristic polynomial at 1), giving a statistical version of the strong BSD formula.

### Status

**Heuristic predictions well-established; rigorous 1-level density proven in many families.** Full rank distribution from RMT is conjectural. The connection between RMT predictions and Selmer rank distributions (C-008) is a major research direction.

### Classification

**Conjecture / Partial results** — 1-level density proven, full rank distribution predicted.

---

## C-008: Selmer Group Statistics (Bhargava-Kane-Lenstra-Poonen-Rouse)

### Statement

Determine the exact distribution of $p$-Selmer ranks $\dim_{\mathbb{F}_p} \text{Sel}_p(E/\mathbb{Q})$ for elliptic curves ordered by height. For $p = 2$, the average 2-Selmer rank is known to be exactly 3. The goal is to extend this to: (a) all primes $p$, (b) the joint distribution of $p$-Selmer ranks for multiple primes, and (c) the distribution of $p^\infty$-Selmer ranks (incorporating $p$-adic aspects).

### Tools Needed

- Bhargava's parametrization: 2-Selmer elements correspond to orbits of $(\mathbb{Z}/2)^3$-torsors, $3$-Selmer elements to orbits of binary cubic forms, etc.
- Geometry of numbers: counting lattice points in fundamental domains for prehomogeneous vector spaces
- Wishing technique: relating Selmer groups to class groups of number fields
- Poisson-type distribution heuristics (Bhargava-Klagsbrun)

### What's Known

- **Bhargava-Shankar (2015):** Average 2-Selmer rank $\leq 3$ (upper bound).
- **Bhargava-Kane-Lenstra-Poonen-Rouse (2023):** The distribution of 2-Selmer ranks is: $\Pr(s_2 = 0) = 1/4$, $\Pr(s_2 = 1) = 1/4$, $\Pr(s_2 = 2) = 15/64$, $\Pr(s_2 = 3) = 15/128$, ... — this is the distribution of ranks of random alternating matrices over $\mathbb{F}_2$ with the Cassels-Tate constraint.
- **Bhargava-Shankar-Wang (2022):** Average 3-Selmer rank $\leq 4$ (via geometry of numbers for binary cubic forms).
- **Klagsbrun (2019):** Average $p$-Selmer rank for quadratic twists of a fixed curve, conditional on finiteness of Sha.
- **Delaunay (2017):** Heuristic predictions for the distribution of $p$-Selmer ranks, matching Cohen-Lenstra for $\text{III}[p]$.

### Main Obstacle

For $p \geq 3$, the parametrization of $p$-Selmer elements involves higher-dimensional prehomogeneous representations (e.g., for $p = 3$: $3 \times 3 \times 3$ tensors). The geometry-of-numbers counting in these spaces is substantially harder. The BKLRP distribution for $p = 2$ uses the special structure of the 2-descent map; general $p$ requires new algebraic and analytic inputs.

### BSD Connection

The Selmer group is the "computable approximation" to the Mordell-Weil group: $E(\mathbb{Q})/pE(\mathbb{Q}) \hookrightarrow \text{Sel}_p(E/\mathbb{Q}) \twoheadrightarrow \text{III}[p]$. The distribution of Selmer ranks constrains the distribution of both rank and Sha. The BKLRP result shows that the average "defect" $\operatorname{rank} - s_2$ is explained by Sha[2], and the exact distribution of $s_2$ is consistent with Goldfeld's conjecture.

### Status

**2-Selmer distribution fully determined (2023).** 3-Selmer average bounded. General $p$-Selmer distribution: conjectural.

### Classification

**Theorem (for $p=2$) / Conjecture (for $p \geq 3$)**.

---

## C-009: Proportion of Rank 2+ Curves: Upper Bounds

### Statement

Improve the upper bound on the density of elliptic curves $E/\mathbb{Q}$ with $\operatorname{rank}(E(\mathbb{Q})) \geq 2$:
$$\limsup_{X \to \infty} \frac{\#\{E : H(E) \leq X,\, \operatorname{rank}(E(\mathbb{Q})) \geq 2\}}{\#\{E : H(E) \leq X\}} \leq \varepsilon$$
for the smallest possible $\varepsilon$. Goldfeld predicts $\varepsilon = 0$. Current best bound: $\varepsilon \leq 0.115$ (Bhargava-Shankar).

### Tools Needed

- Bhargava-Shankar: average 2-Selmer rank bound
- Markov/Chebyshev inequality: $\Pr(\operatorname{rank} \geq 2) \leq \Pr(s_2 \geq 2) = \frac{\mathbb{E}[s_2] - 1}{2-1}$ (crude bound)
- Improved: use the full Selmer rank distribution (BKLRP) to bound $\Pr(s_2 \geq 2)$
- Smith's parity argument: if the parity conjecture holds, then $\Pr(\operatorname{rank} \text{ odd}) = 1/2$, so $\Pr(\operatorname{rank} \geq 2) \leq 1 - \Pr(\operatorname{rank} = 0) - 1/2$

### What's Known

- **Bhargava-Shankar (2015):** $\Pr(\operatorname{rank} \geq 2) \leq 0.115$ (from average rank $\leq 0.885$ and non-negativity).
- **BKLRP (2023):** $\Pr(s_2 \geq 2) = 1 - 1/4 - 1/4 = 1/2$. Since $\operatorname{rank} \leq s_2$, this gives $\Pr(\operatorname{rank} \geq 2) \leq 1/2$ (a weaker but distribution-based bound).
- **Smith (2023):** If Sha[2] satisfies certain heuristics, then $\Pr(\operatorname{rank} \geq 2) = 0$ in twist families.
- **Heuristic (Delaunay-Watkins):** $\Pr(\operatorname{rank} \geq 2) \approx 0.05$ computationally.

### Main Obstacle

The fundamental gap is between Selmer rank and rank. A curve with $s_2 = 4$ could have rank 0 (if Sha[2] has rank 4) or rank 4 (if Sha[2] = 0). Current methods cannot distinguish these cases. A breakthrough would require either: controlling Sha[2] on average, or using a different descent (3-descent, $p$-descent) that has a better rank-to-Selmer ratio.

### BSD Connection

The proportion of rank $\geq 2$ curves measures the prevalence of the "unknown" cases of BSD. If $\Pr(\operatorname{rank} \geq 2) = 0$, then BSD is essentially fully resolved (for 100% of curves). Even a bound $\varepsilon < 1/2$ would be significant — it would show that rank $\geq 2$ curves are a minority, contradicting any "equidistribution" scenario.

### Status

**Open.** Best bound: $\leq 11.5\%$. The BKLRP distribution gives $\Pr(s_2 \geq 2) = 50\%$, but this does not directly improve the rank bound without Sha control.

### Classification

**Partial results** — upper bounds established, target is 0%.

---

## C-010: Arithmetic Statistics over Function Fields

### Statement

Study the BSD conjecture for elliptic curves over $\mathbb{F}_q(t)$ (function fields of curves over finite fields) using the arithmetic statistics approach. The key advantage: over function fields, the BSD conjecture is largely proven (Grothendieck, Tate, Milne, Kato-Trihan), and the analogue of Goldfeld's conjecture is known (Duke-Kowalski). The goal is to use function field results to: (a) test conjectures from the number field case, (b) prove new results via spreading-out and specialization, and (c) study families parameterized by moduli spaces over $\mathbb{F}_q$.

### Tools Needed

- Grothendieck's proof of BSD for constant curves over function fields (assuming finiteness of Sha)
- Tate's theorem: Sha is finite for elliptic curves over function fields of characteristic $p > 0$
- Deligne's Weil II: equidistribution of Frobenius eigenvalues
- Drinfeld modules and shtukas for the function field Langlands correspondence
- Lafforgue's theorem (for $\operatorname{GL}_n$ over function fields)

### What's Known

- **Tate (1966):** Sha is finite for elliptic curves over global function fields.
- **Kato-Trihan (2003):** BSD holds for elliptic curves over function fields of characteristic $p > 2$ (assuming the $p$-part is handled, which was completed by Kato-Trihan using Iwasawa theory).
- **Duke-Kowalski (2000):** Analogue of the Goldfeld conjecture: 100% of elliptic curves over $\mathbb{F}_q(t)$ (ordered by conductor in $\mathbb{F}_q[t]$) have rank $\leq 1$. This uses Lafforgue's theorem and the Lang-Trotter method.
- **Ulmer (2002):** Explicit families of elliptic curves over $\mathbb{F}_q(t)$ with unbounded rank — these are "exceptional" families that do not contradict Goldfeld (density 0).
- **Baier-Brüdern (2020):** Moments of L-functions of elliptic curves over function fields, using automorphic methods.

### Main Obstacle

The function field results use deep tools (Weil conjectures, Lafforgue) that have no number field analogue. Transferring insights from function fields to number fields is the Langlands program's central challenge. For arithmetic statistics specifically, the function field analogue of the Bhargava-Shankar geometry-of-numbers method is the study of moduli spaces of curves over $\mathbb{F}_q$ — but the counting arguments are algebraic rather than analytic, and the translation is not straightforward.

### BSD Connection

Over function fields, BSD is (essentially) a theorem. The function field case serves as a "proof of concept" for arithmetic statistics: all the conjectures (Goldfeld, Cohen-Lenstra, RMT predictions) can be verified or refuted in this setting. Ulmer's examples of unbounded rank show that "100% rank ≤ 1" is the right statement — the high-rank curves are parameterized by special subvarieties of the moduli space.

### Status

**Largely resolved over function fields.** BSD proven (Kato-Trihan), Goldfeld proven (Duke-Kowalski). Active research: uniformity of estimates in $q$, explicit constants, and spreading-out to characteristic 0.

### Classification

**Theorem (over function fields) / Transfer to number fields is open.**

---

## C-011: N-Torsion Statistics and 2-Selmer Rank Distributions

### Statement

Study the distribution of $E[n](\mathbb{Q})$ (rational $n$-torsion) and $\dim_{\mathbb{F}_p} E(\mathbb{Q})[p]$ as $E$ varies over all elliptic curves ordered by height, and relate these to the distribution of Selmer ranks. For a prime $p$, compute:
$$\Pr(E[p] \subset E(\mathbb{Q})) = \lim_{X \to \infty} \frac{\#\{E : H(E) \leq X,\, E[p] \subset E(\mathbb{Q})\}}{\#\{E : H(E) \leq X\}}.$$
This connects to Selmer group statistics because a full $p$-torsion structure forces $\operatorname{Sel}_p$ to contain $E[p](\mathbb{Q}) \cong (\mathbb{Z}/p)^2$ as a subgroup.

### Tools Needed

- Mazur's torsion theorem: possible torsion structures over $\mathbb{Q}$ are classified ($\mathbb{Z}/n$ for $n = 1,\ldots,10, 12$ and $\mathbb{Z}/2 \times \mathbb{Z}/2n$ for $n = 1,\ldots,4$)
- Modular curves $X_1(n)$: $E[n] \subset E(\mathbb{Q})$ iff $E$ corresponds to a $\mathbb{Q}$-point on $X_1(n)$
- Galois cohomology: the Kummer map $E(\mathbb{Q})/pE(\mathbb{Q}) \to H^1(\mathbb{Q}, E[p])$ identifies torsion as part of the Selmer group
- Geometry of numbers for counting points on modular curves of bounded height

### What's Known

- **Bhargava-Shankar (2015):** Average number of $\mathbb{Z}/2 \times \mathbb{Z}/2$-torsion points = $15/8$ (from the distribution of 2-Selmer ranks).
- **Bhargava (2010):** The number of hyperelliptic class-group orbits (related to 2-torsion) of bounded discriminant is finite and explicitly computable.
- **Lozano-Robledo (2019):** Precise frequencies of each torsion structure among curves of conductor $\leq X$, matching heuristics.
- **Dokchitser-Dokchitser (2010):** Local conditions for $p$-torsion in terms of Galois representations.
- **Delaunay-Fukisaki:** Heuristic for the density of curves with $E[p] \subset E(\mathbb{Q})$ is $p^{-\dim \text{GL}_2(\mathbb{F}_p)} \cdot |\mathbb{P}^1(\mathbb{F}_p)| = O(p^{-2})$.

### Main Obstacle

The modular curve $X_1(n)$ for $n \geq 11$ has genus $\geq 2$, so by Faltings's theorem it has finitely many rational points. This means $\Pr(E[n] \subset E(\mathbb{Q})) = 0$ for $n \geq 11$. The problem is interesting for $n \leq 10, 12$, where $X_1(n)$ has genus 0 or 1 and the density is positive. Relating the torsion distribution to the full Selmer rank distribution requires understanding the interaction between torsion and Sha[n], which is the hard problem.

### BSD Connection

Torsion appears in the BSD formula via $|E(\mathbb{Q})_{\text{tors}}|^2$ in the denominator. For curves with prescribed torsion, the BSD formula has a specific structure (e.g., for $E[n] \subset E(\mathbb{Q})$, the curve admits an $n$-isogeny, which constrains the L-function). The distribution of torsion affects the distribution of the BSD leading coefficient. Moreover, the Cassels-Tate pairing on Sha is a bilinear form on $\text{III}[n]$, and its structure is constrained by $E[n](\mathbb{Q})$.

### Status

**Torsion distribution well-understood (genus 0,1 cases).** Connection to Selmer distributions partially established for $p = 2$. For $p \geq 3$, the link is heuristic.

### Classification

**Theorem (torsion distribution) / Partial results (Selmer connection).**

---

## C-012: Katz-Sarnak Philosophy for Families of Elliptic Curves

### Statement

Develop and verify the Katz-Sarnak density matrix / n-level density framework for families of elliptic curve L-functions, establishing that the low-lying zeros of $L(E, s)$ in a family $\mathcal{F}$ follow the distribution of eigenvalues near 1 of a classical compact group $\mathcal{G}(\mathcal{F})$. The symmetry type $\mathcal{G}(\mathcal{F})$ determines the rank distribution: $O$ (orthogonal) predicts even/odd rank equidistribution, $Sp$ (symplectic) predicts rank 0 dominance, $U$ (unitary) is irrelevant for self-dual families.

### Tools Needed

- Explicit formula: $\sum_\gamma \phi(\gamma) = \hat{\phi}(0) \log N + \sum_p (\text{local terms}) + O(1)$ connecting zeros to prime sums
- $n$-level density: $\frac{1}{|\mathcal{F}(X)|} \sum_{E \in \mathcal{F}(X)} \sum_{\gamma_1, \ldots, \gamma_n} \phi_1(\gamma_1 \log N) \cdots \phi_n(\gamma_n \log N)$ for test functions $\phi_i$ supported in $(-\sigma, \sigma)$
- The Katz-Sarnak prediction: for $n$-level density with support $\sigma < 1$, the result depends only on the symmetry type $\mathcal{G}$
- Kuznetsov/Petersson formulas for averages of Fourier coefficients over families of newforms

### What's Known

- **Katz-Sarnak (1999):** Proved that over function fields, $n$-level density matches the random matrix prediction for all $n$, for families with monodromy group equal to a classical group.
- **Rubinstein (2001):** 1-level density for the family of all elliptic curves (by conductor): results consistent with symplectic symmetry (support $\sigma < 2/3$).
- **Dueñez-Huynh-Miller-Miller (2012):** Distinguished 1-level densities for rank 0 and rank 1 subfamilies, consistent with the even/odd orthogonal symmetry types.
- **Bui-Heap (2015):** 2-level density for the family of quadratic twists, symplectic symmetry confirmed for $\sigma < 1$.
- **Young (2014):** 1-level density for the family of all elliptic curves, improving the support to $\sigma < 1$ under GRH.
- **Shparlinski-Takloo-Bashgh (2017):** 1-level density for families of elliptic curves over number fields with restricted torsion.

### Main Obstacle

To detect the symmetry type unconditionally (without GRH), one needs to handle off-diagonal terms in the explicit formula for support $\sigma > 1$. For symplectic families, the $n$-level density for $\sigma > 1$ would distinguish symplectic from orthogonal — but this requires estimates on sums over primes of $a_p(E)$ (Fourier coefficients) in families that go beyond current automorphic techniques. For $\sigma < 1$, the answer is always a linear combination of symmetry types, and distinguishing them is not possible without larger support.

### BSD Connection

The Katz-Sarnak philosophy, if fully established, would determine the rank distribution: symplectic symmetry predicts $\Pr(r = 0) \approx 45.7\%$, $\Pr(r = 1) \approx 46.3\%$, $\Pr(r = 2) \approx 5.9\%$, $\Pr(r \geq 4) \approx 0\%$ (these come from the distribution of orders of vanishing of $Sp$ characteristic polynomials at 1). This would resolve the Goldfeld conjecture (C-002) and give the fine BSD rank distribution. Moreover, the $n$-level density predicts correlations among zeros, which via the explicit formula translate to correlations among central values — giving moment predictions (C-004) and hence statistical versions of the strong BSD formula.

### Status

**1-level density established in many families for limited support.** Full $n$-level density proven only over function fields. The number field case requires support $\sigma > 1$ to determine symmetry type, which is open unconditionally.

### Classification

**Partial results / Conjecture** — 1-level density proven, full Katz-Sarnak correspondence open over $\mathbb{Q}$.

---

# Group D: Research Directions — Tate-Shafarevich Group (III)

12 precise mathematical research directions attacking finiteness, structure, and computability of Sha.

---

## D-001: Finiteness of III via Euler Systems (Kato, 2004)

**ID:** D-001
**Title:** Finiteness of the Tate-Shafarevich Group via Euler Systems
**Status:** Speculative
**Classification:** Core

### Statement

For E/Q an elliptic curve of analytic rank ≤ 1, Kato (2004) proved that the p-part of Sha(E/Q) is finite for all primes p, conditional on the surjectivity of the p-adic Galois representation ρ_{E,p}. The central conjecture to extend this is:

> **Conjecture (Kato).** For any E/Q and any prime p, if the p-adic Selmer group Sel_p(E/Q) is cotorsion over Z_p, then Sha(E/Q)[p^∞] is finite.

The question for rank ≥ 2 is: can one construct Euler systems or p-adic L-function interpolations that control the p∞-Selmer group even when rank(E) ≥ 2?

### Tools Needed

- Kato's Euler system of Heegner-type classes z_n ∈ H¹(G_Q, T_p(E)) at primes n
- Perrin-Riou's p-adic regulator maps and p-adic L-functions
- Rubin's Euler system formalism adapted to GL_2
- The Iwasawa main conjecture for GL_2 over Q (Kato, Skinner-Urban)

### What's Known

1. **Kato (2004):** Constructed an Euler system {z_f^(p)} for E/Q from modular symbols. For analytic rank ≤ 1, the Euler system class is non-trivial, yielding an unbounded cohomology class that forces finiteness of Sha[p^∞] via the Kolyvagin-Logachev descent argument.
2. **Skinner-Urban (2014):** Proved the Iwasawa main conjecture for ordinary p-ordinary elliptic curves over Q, connecting the characteristic ideal of the Selmer group to the p-adic L-function.
3. **Kolyvagin-Logachev (1992):** For E of rank ≤ 1 with root number −1, Heegner point descent directly bounds |Sha|.
4. **Rohrlich, Greenberg:** For p-ordinary E/Q with L(E,1) ≠ 0, Sha[p^∞] is finite and its order divides the algebraic part of L(E,1)/Ω_E up to p-adic units.

### Main Obstacle

For rank ≥ 2, no Euler system is known whose classes are sufficiently non-trivial to bound Sha. Kato's Euler system class z_f^(p) maps to zero under the dual exponential map when rank ≥ 2. Constructing a rank-2 Euler system (analogous to Kolyvagin's system for rank 1) is the central open problem. The Gross-Zagier-Kolyvagin paradigm has no known higher-rank generalization.

### BSD Connection

Finiteness of Sha[p^∞] is the essential hypothesis in the BSD formula. Without it, the p-adic valuation of the leading coefficient of the L-function cannot be compared to the algebraic regulator. Kato's result, combined with Gross-Zagier, proves the p-part of BSD for rank ≤ 1 (modulo the p-adic L-function computation).

---

## D-002: Cassels-Tate Duality and III Structure

**ID:** D-002
**Title:** Cassels-Tate Duality and the Internal Structure of Sha
**Status:** Established
**Classification:** Structural

### Statement

The Cassels-Tate pairing is an alternating, bilinear form on Sha(E/K):

$$\langle \cdot, \cdot \rangle_{CT}: \text{Sha}(E/K) \times \text{Sha}(E/K) \to \mathbb{Q}/\mathbb{Z}$$

Cassels (1962) proved this pairing is alternating and non-degenerate on the p-primary parts for all primes p. The duality theorem states:

> **Theorem (Cassels, 1962).** The pairing ⟨·,·⟩_{CT} descends to a non-degenerate pairing on Sha(E/K)[p^n] for each prime p and integer n. In particular, |Sha(E/K)[p]| is a perfect square.

More precisely, the pairing factors through Galois cohomology: for classes c₁, c₂ ∈ Sha ⊂ H¹(G_K, E), Cassels defined ⟨c₁,c₂⟩ = δ(c₁) ∪ c₂ ∈ H³(G_S, Z) ≅ Q/Z, where δ is the coboundary in the Kummer sequence 0 → E[m] → E → E → 0.

### Tools Needed

- Galois cohomology of E over number fields: H¹(G_S, E[p^n])
- The exact sequence 0 → E(K)/p^n E(K) → Sel_{p^n}(E/K) → Sha(E/K)[p^n] → 0
- Local duality: H¹(K_v, E)[p^n] × E(K_v)/p^n → H²(K_v, μ_{p^n}) ≅ Q/Z
- Cassels's Poitou-Tate exact sequence
- Flat cohomology for p = 2,3 (Edixhoven, Scholl)

### What's Known

1. **Cassels (1962):** Constructed the pairing and proved it is alternating. The pairing is defined via cup products in Galois cohomology and uses the fundamental class in local duality.
2. **Tate (1958, unpublished):** Independently discovered the duality; Cassels published the proof.
3. **Kramer (1981):** Showed that Sha(E/K)[p] is a symplectic F_p-vector space under the pairing.
4. **O'Neil (2002):** Extended the pairing to Sha of abelian varieties and computed it explicitly for Jacobians of curves.
5. **Sharif (2014):** Used Cassels-Tate duality to constrain the p-rank of Sha for curves with rank ≥ 2.
6. **Non-degeneracy:** Cassels proved non-degeneracy modulo the finiteness conjecture for Sha. If Sha is finite, the pairing is non-degenerate on every p-primary component.

### Main Obstacle

Non-degeneracy is proved only conditional on finiteness of Sha. Constructing an unconditional non-degeneracy result (without assuming |Sha| < ∞) remains open. Additionally, the pairing's behavior under isogenies and its explicit computation for specific curves are difficult — no efficient general algorithm exists.

### BSD Connection

The parity of rank (conjectured = analytic rank parity) follows from the alternating property: |Sha[p]| is a perfect square, so the Cassels-Tate pairing forces the rank contribution to the BSD formula to respect parity. The structure constants of Sha[p^n] directly enter the algebraic BSD formula through the Tamagawa number product and the regulator.

---

## D-003: Descent Methods for Bounding |III|

**ID:** D-003
**Title:** Descent Methods for Bounding |Sha| via Selmer Groups
**Status:** Active
**Classification:** Computational / Theoretical

### Statement

For E/Q and a prime p, the classical descent sequence controls Sha[p] through the Selmer group:

> **Exact sequence:** 0 → E(Q)/p·E(Q) → Sel_p(E/Q) → Sha(E/Q)[p] → 0

The descent computes |Sel_p(E/Q)| by studying the images of the local Kummer maps δ_v: E(Q_v)/p → H¹(Q_v, E[p]). The core problem is:

> **Problem.** For each p, compute the image of Sel_p(E/Q) in ∏_v H¹(Q_v, E[p]) and determine the size of the kernel and cokernel of the global-to-local map. Bounds on |Sha[p]| follow from:

$$|Sha[p]| = \frac{|Sel_p(E/Q)|}{|E(Q)/p·E(Q)|}$$

For higher descent (p^n-descent), one iterates: the p^n-Selmer group fits in

$$0 → E(Q)/p^n·E(Q) → Sel_{p^n}(E/Q) → Sha[p^n] → 0$$

and the image of the p^{n+1}-Selmer in the p^n-Selmer is controlled by the connecting homomorphism E(Q)/p^n → H¹(Q, E[p^n]).

### Tools Needed

- Kummer exact sequence: 0 → E[p^n] → E → E → 0 and associated long exact sequence in Galois cohomology
- Local Kummer maps δ_v: E(Q_v)/p^n → H¹(Q_v, E[p^n])
- Two-descent via 2-isogenies (Birch-Swinnerton-Dover), complete 2-descent (Cassels, Cremona)
- Explicit n-descent (Fisher, Stoll, Schaefer, Connell)
- Minimisation and reduction algorithms for the Selmer variety

### What's Known

1. **Birch-Swinnerton-Dyer (1965):** Original descent computations for specific curves, discovering the rank ↔ |Sha| connection empirically.
2. **Cassels (1967):** Developed complete 2-descent for elliptic curves over Q.
3. **Silverman (1992), X.4:** General theory of descent via isogenies.
4. **Fisher (2008), Stoll (2007):** Efficient algorithms for 2-descent and 4-descent on curves of the form y² = x³ + ax + b.
5. **Schaefer-Connell (2001):** Complete n-descent for n = 3,5 via covering spaces. Computed Sha[3] and Sha[5] for many curves.
6. **González-Jiménez, Najman (2020):** Systematic computation of Sha[p] for p = 2,3,5 on all curves with conductor ≤ 10^6 in LMFDB.
7. **Cremona-Siksek:** Extended 2-descent with refined information at bad primes, reducing Sha[2] computation.
8. **Nekovář (2006):** Developed the Selmer complex formalism giving unconditional bounds on Sha in many cases.

### Main Obstacle

Higher descent (p^n for large n) becomes computationally intractable: the Selmer group is a subspace of a product of local cohomology groups whose dimension grows. The restriction maps become harder to compute. For p = 2, there are also issues with 2-adic logarithm convergence and the wild ramification at 2. For p ≥ 5, the covering curve theory is incomplete.

### BSD Connection

Descent is the primary algebraic method for computing |Sha[p]| in practice. The 2-descent bounds enter the verification of BSD for curves of rank ≤ 1 (Cremona's tables). For rank ≥ 2, multiple descents (combining 2-descent and 3-descent) can sometimes determine Sha completely, allowing verification of the leading term formula.

---

## D-004: p-adic Methods for III

**ID:** D-004
**Title:** p-adic Methods for Controlling Sha
**Status:** Active
**Classification:** Core

### Statement

p-adic interpolation provides two complementary approaches to Sha:

> **Schneider's p-adic conjecture (1982).** For E/Q ordinary at p, there is a p-adic L-function L_p(E, s) interpolating L(E, χ, 1) for Dirichlet characters χ of p-power conductor. The order of vanishing of L_p at s = 1 equals rank E(Q).

> **Kato's Euler system bound (2004).** The Pontryagin dual Sel_p(E/Q)^∨ is a finitely generated torsion Z_p[[Γ]]-module (Γ = Gal(Q_∞/Q)), and its characteristic ideal divides the ideal generated by L_p(E).

The key structural result is:

$$|Sha[p^n]| \leq \frac{|Sel_{p^n}(E/Q)|}{|E(Q)/p^n·E(Q)|}$$

and the Iwasawa main conjecture controls the left-hand side in the limit n → ∞.

### Tools Needed

- p-adic L-functions: interpolation of L-values via modular symbols, overconvergent modular symbols (Pollack, Stevens)
- Perrin-Riou's exponential map: H¹(Q_p, T_p(E)) → D_{cris}(V_p(E)) ≅ B_{dR}^+
- Iwasawa theory: Z_p[[T]]-modules, characteristic ideals, µ-invariant, λ-invariant
- The control theorem: for E p-ordinary, the natural map Sel_{p^n}(E/Q) → Sel_{p^∞}(E/Q_∞)^{Γ_n} has kernel and cokernel bounded independently of n
- Perrin-Riou's p-adic regulator and the Coleman map

### What's Known

1. **Mazur (1972):** For E ordinary at p, the Selmer group over the cyclotomic Z_p-extension is a cotorsion Z_p[[T]]-module.
2. **Kato (2004):** Char(Sel_p(E/Q)^∨) | L_p(E) in Z_p[[T]], giving the divisibility direction of the Iwasawa main conjecture.
3. **Skinner-Urban (2014):** For E ordinary at p, the reverse divisibility holds (full main conjecture for the p-adic L-function).
4. **Pollack (2003):** For E supersingular at p, constructed ±p-adic L-functions and proved the main conjecture in the "good µ" case.
5. **Kobayashi (2003):** Defined plus/minus Selmer groups for supersingular E and proved control theorems.
6. **Kurihara (2013):** Used p-adic methods to refine the leading term of the p-adic L-function and extract exact Sha[p^∞] orders.

### Main Obstacle

For supersingular primes (a_p ≡ 0 mod p), the standard Selmer group is not cotorsion over Z_p[[T]], and the ±-Selmer groups of Pollack-Kobayashi are needed but are less well-behaved. The µ-invariant is conjecturally zero (never proven in general for E/Q). For rank ≥ 2, the Euler system bound does not determine the exact order of Sha — it gives only divisibility by certain powers of p.

### BSD Connection

The p-adic BSD conjecture (Mazur-Tate-Teitelbaum) asserts:

$$L_p^{(r)}(E,1) = \frac{(1 - a_p p^{-1} + p^{-1})^? \cdot \mathcal{L}_p(E) \cdot |Sha[p^∞]| \cdot \prod c_v^{(p)}}{|E(Q)_{tors}|^2}$$

where the p-adic regulator ℒ_p(E) is a determinant of p-adic heights. This refines classical BSD by extracting p-adic valuations of the leading L-value coefficient.

---

## D-005: Computational Bounds on |III| for Specific Curves

**ID:** D-005
**Title:** Computational Bounds on |Sha| for Specific Curves
**Status:** Active
**Classification:** Computational

### Statement

For specific elliptic curves E/Q of small conductor (N ≤ 10^6 in LMFDB), compute or bound |Sha(E/Q)|:

> **Problem.** Given an elliptic curve E/Q of conductor N, determine |Sha(E/Q)| exactly by combining:
> (a) 2-descent to compute Sha[2]
> (b) 3-descent to compute Sha[3]
> (c) Bounds from the Birch-Swinnerton-Dyer conjecture (assuming rank known)
> (d) Verification that the analytic Sha (computed from L(E,1)) matches the algebraic Sha

The expected formula is:

$$|Sha_{\text{alg}}| = \frac{L^{(r)}(E,1) \cdot |E(Q)_{tors}|^2}{r! \cdot \Omega_E \cdot R_E \cdot \prod c_v}$$

### Tools Needed

- Cremona's `mwrank` / `eclib` for 2-descent
- Magma/Sage implementations of complete 2-descent and 3-descent
- LMFDB database of curves with precomputed ranks, torsion, Tamagawa numbers, and analytic Sha
- Dokchitser's `Tim Dokchitser's L-functions` for computing L(E,1) to high precision
- Shimura's reciprocity law for computing periods Ω_E
- The modular parametrization (modular symbols) for L-values

### What's Known

1. **Cremona (1997–2023):** Complete verification of BSD (including |Sha|) for all curves of conductor ≤ 500,000 via 2-descent + modular L-values.
2. **Watkins (2002):** Largest known |Sha| = 4,224, found on a curve of rank 0.
3. **LMFDB (2024):** Stores data for all elliptic curves over Q of conductor ≤ 500,000 with computed Sha[2] and analytic Sha estimates.
4. **Stein-Wuthrich (2013):** Systematic computation of Sha for rank 2 curves using Magma.
5. **Rizzo (2003):** Computed |Sha| for all curves with |Sha[2]| = 16 and verified BSD.
6. **Elkies (2006):** Found curves of rank ≥ 28, but Sha computation for high-rank curves is difficult because descent is expensive.

### Main Obstacle

For curves of rank ≥ 2, 2-descent alone cannot determine Sha — one needs p-descent for multiple primes p. The computational bottleneck is computing the image of the local Kummer maps at bad primes. For large conductor, the modular L-function computation becomes expensive, and the analytic Sha estimate (from L(E,1) or the leading coefficient) may not have enough precision to distinguish |Sha| = 1 from |Sha| = 4.

### BSD Connection

This direction provides the empirical database that motivates and tests all other directions. Every conjecture about Sha ultimately must agree with computed data. The verification of BSD for all curves of conductor ≤ 500,000 is the most compelling evidence for the conjecture.

---

## D-006: The Cassels-Tate Pairing and Its Non-degeneracy

**ID:** D-006
**Title:** Non-degeneracy of the Cassels-Tate Pairing on Sha
**Status:** Established
**Classification:** Structural

### Statement

The Cassels-Tate pairing on Sha(E/K)[p^n]:

$$\langle \cdot, \cdot \rangle: Sha[p^n] \times Sha[p^n] \to \mathbb{Z}/p^n\mathbb{Z}$$

is defined via the cup product in Galois cohomology. For x, y ∈ Sha ⊂ H¹(K, E[p^n]), the pairing is:

$$\langle x, y \rangle = \sum_v \text{inv}_v(\delta(x_v) \cup y_v) \in \mathbb{Q}/\mathbb{Z}$$

where δ: H¹(K_v, E[p^n]) → H²(K_v, E) is the coboundary and inv_v: H²(K_v, G_m) → Q/Z is the local invariant map.

> **Theorem (Cassels, 1962).** If Sha(E/K) is finite, then ⟨·,·⟩ is non-degenerate on every p-primary component. In particular, |Sha[p]| is a perfect square.

### Tools Needed

- Galois cohomology: the fundamental class in H²(K_v, G_m) ≅ Q/Z
- Cup product: H¹(K_v, E[p^n]) × H²(K_v, E[p^n]) → H³(K_v, E[p^n] ⊗ E[p^n]) → H³(K_v, μ_{p^n}) → Q/Z
- Poitou-Tate global duality: 9-term exact sequence
- Flat cohomology: for p | N (bad reduction), the pairing requires modifications (Cassels, O'Neil)

### What's Known

1. **Cassels (1962):** Proved the pairing is alternating and that non-degeneracy follows from finiteness.
2. **Kramer (1981):** Sha[p] is a symplectic F_p-vector space. Hence |Sha[p]| = p^{2k} for some k.
3. **O'Neil (2002):** Constructed an explicit formula for the pairing using the arithmetic of the curve. For Sha ⊂ H¹(K, E[m]), the pairing can be computed via local index computations.
4. **Sharif (2014):** Showed that if Sha[p] ≠ 0 and E has rank r, then |Sha[p]| ≥ p^{2⌊r/2⌋}.
5. **Dokchitser-Dokchitser (2010):** Developed explicit algorithms for computing the Cassels-Tate pairing on Jacobians of hyperelliptic curves.
6. **Ciperiani-Wiles (2011):** Extended the pairing to the case of isogenies and proved compatibility under isogeny.

### Main Obstacle

Unconditional non-degeneracy (without assuming |Sha| < ∞) is open. If Sha is infinite, the pairing could be degenerate. Even conditional non-degeneracy is hard to use for constructive purposes: knowing |Sha[p]| is a perfect square doesn't determine its value. The pairing computation requires knowing Sha itself, creating a circularity for direct computation.

### BSD Connection

The perfect-square constraint from the Cassels-Tate pairing interacts with the BSD formula: for an isogeny φ: E → E', the analytic Sha changes by a factor related to |E'(Q)[φ]|/|E(Q)[φ̂]|, and the algebraic Sha changes by the same factor via the Cassels-Tate pairing.

---

## D-007: Structure Constants — III[p^n] and p^∞-Selmer Groups

**ID:** D-007
**Title:** Structure Constants of III[p^n] and Control via p^∞-Selmer Groups
**Status:** Active
**Classification:** Structural / Iwasawa-theoretic

### Statement

For E/Q and prime p, the p∞-Selmer group fits in:

$$0 \to E(Q) \otimes \mathbb{Q}_p/\mathbb{Z}_p \to \text{Sel}_{p^\infty}(E/Q) \to Sha[p^\infty] \to 0$$

The structure of Sha[p^∞] is constrained by:

> **Conjecture.** Sha(E/Q)[p^∞] is finite, hence isomorphic to ⊕_i Z/p^{n_i}Z for some n_i ≥ 1.

The **µ-invariant** and **λ-invariant** of the Selmer group over the cyclotomic Z_p-extension Q_∞/Q control the growth:

$$|\text{Sel}_{p^n}(E/Q)| = p^{\mu p^n + \lambda n + \nu}$$

for n sufficiently large, where µ, λ, ν are the Iwasawa invariants.

### Tools Needed

- Iwasawa theory: Z_p[[T]]-module structure, pseudo-isomorphism, structure theorem
- The control theorem: |ker(Sel_{p^n}(E/Q) → Sel_{p^∞}(E/Q_∞)^{Γ_n})| and |coker| are bounded
- Greenberg's formula for the µ-invariant
- Mazur's deformation theory: H¹_f(Q_p, Ad^0 ρ_E) and its relation to Selmer varieties
- The dual Selmer complex: RΓ_f(Z[1/S], T_p(E))^∨

### What's Known

1. **Greenberg (1999a,b):** For E/Q ordinary at p, the µ-invariant of Sel_p(E/Q_∞) vanishes if and only if E has good ordinary reduction at p and certain integrality conditions hold. Proved µ = 0 for all E/Q with good ordinary reduction and p not dividing N·#E(Q)_{tors}.
2. **Skinner-Urban (2014):** Implies λ = ord_{s=1} L_p(E,s) for ordinary primes (via the main conjecture).
3. **Kurihara (2013):** Computed the structure of Sha[p] for curves with specific Selmer ranks using the structure theorem for Z_p[[T]]-modules.
4. **Ochi (2011):** Showed that for many E/Q, the Pontryagin dual of Sel_{p^∞}(E/Q) is isomorphic to Z_p^r ⊕ M where M is finite, and |M| = |Sha[p^∞]|·|E(Q)_{tors}/p^∞|.

### Main Obstacle

For supersingular primes, the Iwasawa theory of the cyclotomic extension is insufficient: the Selmer group is not cotorsion over Z_p[[T]]. The ±-Selmer groups of Pollack-Kobayashi give an alternative, but the structure constants (µ±, λ±) are not well-understood in general. For rank ≥ 2, the relationship between the analytic rank and the λ-invariant is conjectural.

### BSD Connection

The Iwasawa main conjecture for E/Q implies BSD modulo p: from the equality of the characteristic ideal of Sel_{p^∞}^∨ with (L_p(E)), one can extract the p-adic valuation of |Sha[p^∞]|, the p-part of the regulator, and the p-part of the Tamagawa numbers. This is the deepest known approach to the p-part of BSD.

---

## D-008: Visibility Method for Elements of III

**ID:** D-008
**Title:** Visibility of Elements of Sha in Jacobians of Modular Curves
**Status:** Active
**Classification:** Computational / Structural

### Statement

For an elliptic curve E/Q of conductor N, the modular parametrization φ: X_0(N) → E induces a map on Jacobians:

$$J_0(N) \xrightarrow{\pi} E$$

Elements of Sha(E/Q) can be "seen" as divisors on X_0(N) that map non-trivially under π but are locally trivial. The visibility method exploits:

> **Principle (Mazur, 1997).** If P ∈ J_0(N) is a point with π(P) = 0 and P is not torsion, then P contributes to ker(π) and potentially to Sha(E).

More precisely, one considers the exact sequence:

$$0 \to \ker(\pi) \to J_0(N) \xrightarrow{\pi} E \to 0$$

and studies the connecting homomorphism δ: E(Q) → H¹(Q, ker(π)).

### Tools Needed

- Modular curves X_0(N), X_1(N), their Jacobians J_0(N), J_1(N)
- Hecke algebra action on J_0(N) and the E-isotypic component
- Visibility in multiple abelian varieties (Clark, 2003): for E₁ × E₂ → J_0(N), Sha(E₁) and Sha(E₂) can be simultaneously visible
- Explicit computations on J_0(N) via period matrices and Abel-Jacobi maps
- Cremona's database of modular symbols

### What's Known

1. **Mazur (1997):** Introduced the visibility philosophy: elements of Sha are geometric objects on modular curves.
2. **Cremona-Mazur, Agashe-Stein (2005):** Computed visible Sha for all curves of conductor ≤ 50,000 using the visibility method in J_0(N).
3. **Clark (2003):** Generalized visibility to multiple quotients of J_0(N): if E₁, ..., E_k are distinct isogeny classes of conductor N, then Sha(E_i) can be visible in the kernel of J_0(N) → ∏ E_j.
4. **Creutz (2013):** Showed that for E/Q of rank 0, the visible part of Sha accounts for all of Sha[2] in most cases. For rank ≥ 2, visibility is less effective.
5. **Sharif (2014):** Used visibility to construct curves with |Sha[p]| = p^{2k} for arbitrary k.
6. **Stein-Wuthrich (2013):** Showed that for most curves of conductor ≤ 50,000, Sha = Sha^{vis}, i.e., all of Sha is visible.

### Main Obstacle

Visibility accounts for all known examples of Sha, but there is no proof that Sha = Sha^{vis} in general. For large Sha, the dimension of the kernel of J_0(N) → E grows, but explicit computation on J_0(N) (period computation, height pairing) becomes impractical for large N. The method also depends on the modular parametrization, which is not available for curves over general number fields.

### BSD Connection

Visibility provides a geometric mechanism for elements of Sha to exist: if Sha ≠ 0, there must be a "reason" (a non-trivial divisor on X_0(N)). The BSD leading term determines |Sha|, and visibility explains where those |Sha| non-trivial elements come from geometrically.

---

## D-009: III over Function Fields

**ID:** D-009
**Title:** The Tate-Shafarevich Group over Function Fields
**Status:** Active
**Classification:** Structural

### Statement

For E/k(t) an elliptic curve over a function field k(t) (k a finite field or number field), Sha behaves differently than over number fields:

> **Theorem (Artin-Tate, 1967, unpublished; Milne, 1968).** If k is a finite field F_q and E/F_q(t) has non-constant j-invariant, then Sha(E/F_q(t)) is finite.

> **Conjecture (Geisser, 2004).** For E/F_q(t), the order of Sha satisfies the function-field BSD formula:

$$L(E/F_q(t), 1) = \frac{|Sha(E/F_q(t))| \cdot \prod c_v \cdot \deg(h)}{|E(F_q(t))_{tors}|^2}$$

where h is the canonical height pairing and L is the Goss L-function.

### Tools Needed

- Arithmetic of curves over finite fields: the zeta function Z(C/F_q, T)
- The Néron model of E over C (a surface) and its Tate-Shafarevich group in the Picard scheme
- Geometric class field theory: the Artin-Tate duality for abelian varieties over function fields
- Goss L-functions: L(E/F_q(t), s) for s ∈ Z_p
- Ulmer's constructions of high-rank elliptic curves over F_q(t)

### What's Known

1. **Artin-Tate (1967):** For E/F_q(t), the BSD conjecture is equivalent to finiteness of Sha and can be reduced to a statement about the Néron-Severi group of the associated surface (via the Tate conjecture, proved by Tate for abelian varieties over finite fields).
2. **Milne (1968):** Proved the Artin-Tate conjecture for surfaces fibered over curves, yielding finiteness of Sha in many cases.
3. **Geisser (2004):** Proved finiteness of Sha[p] for p ≠ char(k) using the Weil conjectures.
4. **Ulmer (2002, 2007):** Constructed explicit curves E/F_q(t) with arbitrarily large rank, and computed Sha for some of them. Found that |Sha| can be large.
5. **Tan (2021):** Proved the full Artin-Tate conjecture (and hence BSD for function fields) for elliptic curves E/F_q(t) with non-constant j-invariant.
6. **Deshpande (2022):** Extended the results to the constant-j case under certain conditions.

### Main Obstacle

For E/k(t) with k = Q (function field over a number field), finiteness of Sha is still open. The Tate conjecture approach does not work because the Weil conjectures are not available. For curves of constant j-invariant over F_q(t), the Artin-Tate conjecture is only partially proved.

### BSD Connection

The function-field case is the closest setting to number fields where BSD is fully proved (in many cases). The method of proof — reducing to the Tate conjecture for surfaces — has no direct analogue over number fields, but the structural insights (the role of the Néron-Severi group, the duality between Sha and the Brauer group) inform the number-field theory.

---

## D-010: The p-part of III and Iwasawa Theory

**ID:** D-010
**Title:** The p-part of Sha in the Iwasawa-theoretic Framework
**Status:** Active
**Classification:** Core

### Statement

For E/Q ordinary at p, consider the cyclotomic Z_p-extension Q_∞/Q with Galois group Γ ≅ Z_p. The Selmer group over Q_∞:

$$\text{Sel}_{p^\infty}(E/Q_\infty) = \varinjlim \text{Sel}_{p^n}(E/Q_n)$$

is a cofinitely generated cotorsion module over Λ = Z_p[[Γ]] ≅ Z_p[[T]]. Its Pontryagin dual X_∞ = Sel_{p^∞}(E/Q_∞)^∨ is a finitely generated torsion Λ-module.

> **Conjecture (Iwasawa Main Conjecture for E, Kato 2004, Skinner-Urban 2014).** The characteristic ideal of X_∞ equals the ideal generated by the p-adic L-function L_p(E) in Λ:

$$\text{char}_\Lambda(X_\infty) = (L_p(E))$$

The p-part of Sha is recovered from the control theorem:

$$|Sha(E/Q)[p^n]| \leq |\text{Sel}_{p^n}(E/Q)| \cdot |E(Q)/p^n·E(Q)|^{-1}$$

and the growth of the Selmer group is governed by the Iwasawa invariants µ and λ.

### Tools Needed

- Iwasawa algebra Λ = Z_p[[T]] and its module theory
- The control theorem (Greenberg, 1989): Sel_{p^n}(E/Q) → Sel_{p^∞}(E/Q_∞)^{Γ_n}
- The characteristic ideal and pseudo-null modules
- Perrin-Riou's big exponential map: H¹(Q_p, T_p(E) ⊗ Λ) → D_{cris}(V_p(E)) ⊗ Λ
- The Euler system of Kato and its regulator map
- Greenberg's Selmer conditions at bad primes

### What's Known

1. **Greenberg (1989):** Developed the Iwasawa theory of Selmer groups of abelian varieties, proving the control theorem and defining the µ, λ invariants.
2. **Kato (2004):** char_Λ(X_∞) | (L_p(E)) — the "half" of the main conjecture from the Euler system.
3. **Skinner-Urban (2014):** Full main conjecture for E/Q ordinary at p, under mild hypotheses (essentially all E/Q ordinary at p with L(E,1) = 0).
4. **Wan (2014):** Main conjecture for supersingular primes using ±-Selmer groups and Perrin-Riou's regulator.
5. **Iovita-Pollack (2013):** Extended the main conjecture to the anticyclotomic setting for CM curves.
6. **Büyükboduk-Lei (2019):** Proved the main conjecture for Heegner points in the anticyclotomic setting.

### Main Obstacle

For rank ≥ 2, the Euler system bound char_Λ(X_∞) | (L_p(E)) does not determine char_Λ(X_∞) exactly — there could be a non-trivial µ-invariant factor. The full main conjecture (Skinner-Urban) determines the characteristic ideal, but extracting the exact p-adic valuation of |Sha[p^∞]| requires knowledge of the µ-invariant, which is conjecturally zero but unproven in general.

### BSD Connection

The Iwasawa main conjecture for E/Q, combined with the Birch-Swinnerton-Dyer conjecture, implies:

$$v_p(|Sha[p^\infty]|) = v_p\left(\frac{L^{(r)}(E,1)}{r! \cdot \Omega_E \cdot R_E \cdot \prod c_v}\right)$$

This is the p-adic BSD conjecture, and the Iwasawa main conjecture is the deepest known approach to it.

---

## D-011: Heuristics for |III| Distribution

**ID:** D-011
**Title:** Heuristic Models for the Distribution of |Sha|
**Status:** Speculative
**Classification:** Heuristic / Probabilistic

### Statement

The distribution of |Sha(E/Q)| across isogeny classes of elliptic curves is predicted by:

> **Conjecture (Delaunay, 2007).** For elliptic curves E/Q of rank r ordered by conductor N, the values of |Sha[p]|/p^{2⌊r/2⌋} follow the distribution predicted by the Cohen-Lenstra-Martinet heuristics, adapted with the local root number correction:

$$\text{Prob}(|Sha[p]| = p^{2k}) \sim \frac{1}{p^{k(k-1)} \cdot \prod_{i=1}^{k}(p^{2i}-1)} \cdot w_p(E)$$

where w_p(E) is a local correction factor depending on the Galois representation E[p].

> **Parity Conjecture (Dokchitser-Dokchitser, 2010).** The parity of rank(E) equals the parity predicted by the global root number w(E/Q):

$$\text{rank}(E) \equiv \frac{1-w(E/Q)}{2} \pmod{2}$$

This implies |Sha[p]| is a perfect square (from Cassels-Tate) and that the p-rank of Sha adjusts to match the analytic rank parity.

### Tools Needed

- Cohen-Lenstra-Martinet heuristics: adapted for the symplectic structure of Sha
- Root numbers: w(E/Q) = ∏_v w_v(E/Q_v), computed from local data
- Random matrix theory: the Katz-Sarnak philosophy linking L-function families to matrix ensembles
- The Dokchitser-Dokchitser parity theorem (conditional on finiteness of Sha)
- Birch-Swinnerton-Dyer data from LMFDB and Cremona's tables

### What's Known

1. **Delaunay (2001, 2007):** Predicted the distribution of |Sha| using Cohen-Lenstra heuristics adapted to the symplectic group Sp(2k, F_p). For rank 0, the expected frequency of Sha[p] = p^{2k} is proportional to 1/|Sp(2k, F_p)|.
2. **Dokchitser-Dokchitser (2010):** Proved the parity conjecture for all elliptic curves over Q (conditional on finiteness of Sha and the Shafarevich-Tate conjecture for the Galois representation).
3. **Watkins (2004):** Computed the largest known |Sha| = 4,224 on a rank-0 curve and verified that it agrees with heuristic predictions.
4. **Root number computations (Martin, Dokchitser-Dokchitser):** Systematic computation of root numbers for curves of conductor ≤ 10^5. Verified that the parity of rank matches the root number in all computed cases.
5. **Bhargava-Shankar (2015):** Proved that the average rank of elliptic curves over Q is at most 0.886, consistent with the heuristic prediction that half of curves have rank 0 and half have rank 1.

### Main Obstacle

The Cohen-Lenstra heuristics predict the distribution of Sha for fixed rank, but the distribution of rank itself is not fully understood. The root number w(E/Q) changes sign with probability 1/2 in families, but for specific curves, w(E/Q) is determined and cannot be averaged over. The heuristics also assume Sha is finite, which is the conjecture being investigated.

### BSD Connection

The BSD formula relates |Sha| to L-function data: for rank r, the r-th derivative L^{(r)}(E,1) is non-zero and |Sha| appears in the leading coefficient. The distribution of |Sha| is thus equivalent to the distribution of L-values, which is predicted by random matrix theory (the Katz-Sarnak philosophy). The heuristics for Sha are the algebraic counterpart of the Keating-Snaith predictions for L-function moments.

---

## D-012: Effective Finiteness — Explicit Upper Bounds for |III|

**ID:** D-012
**Title:** Effective Finiteness and Explicit Upper Bounds for |Sha|
**Status:** Open
**Classification:** Core / Effective

### Statement

The goal is to prove unconditional, effective bounds:

> **Problem.** For E/Q of conductor N, prove that |Sha(E/Q)| ≤ C(N) for some explicit function C(N), without assuming finiteness of Sha.

If Sha is finite, the bound should be:

$$|Sha(E/Q)| \leq C \cdot N^{1+\varepsilon}$$

for some absolute constant C (depending on ε), refining the conjectural bound from the BSD formula.

An effective approach combines:
(a) Selmer group bounds from Galois cohomology
(b) Height bounds from the geometry of numbers
(c) Analytic bounds from the L-function

### Tools Needed

- The Selmer variety and its dimension bounds (from the Euler characteristic formula)
- Global duality: Poitou-Tate exact sequence for Sel_p(E/Q)
- The height pairing on E(Q): the regulator R_E = det(⟨P_i, P_j⟩) ≥ c(N, rank) by Silverman's bound
- Analytic number theory: bounds on L(E,1) or L^{(r)}(E,1) from subconvexity and moments
- The Gross-Zagier formula: for rank 1, the central derivative is a height of a Heegner point
- Explicit estimates for Tamagawa numbers c_v

### What's Known

1. **Gross-Zagier (1986), Kolyvagin (1991):** For E of analytic rank ≤ 1, Sha is finite and |Sha| is bounded by an expression involving the L-value and the Heegner point height.
2. **Silverman (1981):** The canonical height satisfies ĥ(P) ≥ c₁(N) for non-torsion P ∈ E(Q).
3. **Zywina (2010):** Proved effective bounds on |Sha[p]| for p = 2 using explicit 2-descent:

$$|Sha[2]| \leq 4^{s-1}$$

where s = #{v | 2N : δ_v(E(Q_v)/2) ≠ 0}.

4. **Nekovář (2006):** Using the Selmer complex, obtained unconditional bounds on Sha for many curves, but not in the form |Sha| ≤ C(N).
5. **Masser-Wüstholz (1993):** Effective bounds for the isogeny theorem give bounds on the regulator, which indirectly bound Sha via BSD.
6. **Dokchitser (2010):** Showed that for rank ≥ 2, |Sha[p]| is bounded by p^{2·rank(Jac(C))} where C is a covering curve of E.
7. **Skinner-Urban (2014):** Conditional on the main conjecture, |Sha[p^∞]| is bounded by p^{v_p(L_p^{(r)}(E,1))}.

### Main Obstacle

For rank ≥ 2, no unconditional bound on |Sha| is known. The Selmer group Sel_p(E/Q) can be controlled by the Euler system only for rank ≤ 1. For rank ≥ 2, the Euler system class vanishes, and no replacement is available. The height bounds are effective but only give |Sha| ≤ (height)^{rank}, which is not useful without knowing Sha is finite. The analytic approach requires subconvex bounds for L(E, 1+it) and explicit residue formulas, which are available for rank 0 and 1 but not for higher rank.

### BSD Connection

An effective bound on |Sha| would make the BSD formula into a theorem (for curves of small rank): if |Sha| ≤ C(N) and rank = 0 or 1, one can compute Sha exactly by combining the analytic L-value with the algebraic Selmer group computation. This would complete the proof of BSD for rank ≤ 1 with explicit error terms, and for rank ≥ 2, it would reduce the conjecture to verifying finiteness.

---

# Directions E: p-adic Methods

---

## E-001 · Two-variable p-adic L-functions (Hida family × elliptic curve)

### Statement

Construct the two-variable p-adic L-function $L_p(f_\infty, s)$ interpolating special values of L-functions attached to the members $f_k$ of the Hida family $\{f_k\}$ passing through an ordinary eigenform $f$ of weight 2 attached to an elliptic curve $E/\mathbb{Q}$. The two variables are the cyclotomic variable $s$ (arising from the $\mathbb{Z}_p^\times$-extension of $\mathbb{Q}$) and the weight variable $k$ (parametrising the Hida family). Establish interpolation: for critical integers $j$ with $1 \le j \le k-1$,

$$L_p(f_k, j) = \left(1 - \frac{p^{j-1} \beta_k^{-1}}{}\right)\left(1 - \frac{p^{j} \alpha_k^{-1}}{}\right) \frac{\Gamma(j)}{(2\pi i)^j} \frac{L(f_k, j)}{\Omega_{f_k}^{\pm}}$$

where $\alpha_k, \beta_k$ are roots of the Hecke polynomial at $p$ and $\Omega_{f_k}^{\pm}$ are periods, and study the resulting measure on $\mathbb{Z}_p^\times \times \mathbb{Z}_p^\times$.

### Tools needed

- Hida's ordinary projection and control theorem
- Modular symbols / Shimura's period integrals
- $p$-adic interpolation of distributions (Amice transform)
- Galois deformations in the ordinary case

### What's known

- Hida (1986): existence of the Hida family for ordinary $f$; control theorem for weight spaces.
- Greenberg–Stevens (1993): construction of the two-variable $p$-adic L-function; proof that it is an element of the Iwasawa algebra $\Lambda = \mathbb{Z}_p[[\mathbb{Z}_p^\times \times \mathbb{Z}_p^\times]]$ (or its fraction field).
- Interpolation formula is valid at classical specialisations; meromorphic continuation expected.
- Emerton, Pollack, Weston: variation of $\mu$- and $\lambda$-invariants across families.

### Main obstacle

Showing integrality (rather than mere meromorphy) of the two-variable $p$-adic L-function as an element of $\mathbb{Z}_p[[T_1, T_2]]$, and controlling denominators arising from non-unit root $\alpha_k$ at varying $k$. The classical CM case is well-understood; the non-CM case remains open for full integrality.

### BSD connection

The two-variable $p$-adic L-function specialises at $k=2$ to the cyclotomic $p$-adic L-function $L_p(E, s)$, whose central value at $s=1$ encodes the algebraic rank via the $p$-adic BSD conjecture. Variation over the weight variable lets one study the rank of $E$ through the behaviour of Selmer groups in families, connecting to the Iwasawa main conjecture for $E$ over the $\mathbb{Z}_p$-extension.

### Status

Active. Construction known; integrality and main conjecture aspects ongoing.

### Classification

Iwasawa theory / $p$-adic families

---

## E-002 · p-adic Gross-Zagier formula (Perrin-Riou, Nekovář)

### Statement

Prove and refine the $p$-adic analogue of the Gross–Zagier formula: relate the first derivative $L_p'(E/K, 1)$ of the $p$-adic L-function of an elliptic curve $E/\mathbb{Q}$ over an imaginary quadratic field $K$ (satisfying Heegner hypotheses) to the $p$-adic height $\hat{h}_P(P_K)$ of the Heegner point $P_K \in E(K)$, i.e.

$$L_p'(E/K, 1) = \frac{\hat{h}_P(P_K) \cdot c_E}{[\mathcal{O}_K : \mathbb{Z}[f]]}$$

where $c_E$ involves Tamagawa factors and the conductor, and $\hat{h}_P$ is the $p$-adic height pairing. The formula must account for the chosen $p$-adic height (canonical, Mazur–Tate, or Bernardi) and the associated logarithm $\log_P : E(\mathbb{Q}_p) \to \mathbb{Q}_p$.

### Tools needed

- Heegner points on $X_0(N)$ and modular parametrisation $\phi : X_0(N) \to E$
- $p$-adic heights: Mazur–Tate canonical height, Bernardi height, Nekovář's extension to general settings
- Perrin-Riou's $p$-adic Gross–Zagier formula (explicit regulator maps)
- Kolyvagin's Euler systems and Rubin's extensions

### What's known

- Gross–Zagier (1986): archimedean formula $L'(E/K, 1) = c \cdot \hat{h}(P_K)$ for the Néron–Tate height.
- Perrin-Riou (1987, 1992): $p$-adic Gross–Zagier formula in the ordinary case, relating $L_p'$ to $p$-adic heights.
- Nekovář (1993, 2006): systematic framework for $p$-adic height pairings on Selmer groups; extension to cases where $E$ has supersingular reduction at $p$ (with technical conditions).
- Howard (2006): Gross–Zagier in the setting of Shimura curves.

### Main obstacle

The formula of Perrin-Riou is stated in terms of the Coleman–p-adic logarithm composed with the modular parametrisation, which introduces non-explicit constants. Extracting a clean, computationally effective formula with explicit dependence on the chosen $p$-adic height (and its dependence on the choice of splitting of the Hodge filtration) remains difficult. Supersingular primes require fundamentally new constructions (Castella, Wan, Sprung).

### BSD connection

Central: the $p$-adic Gross–Zagier formula directly gives the order of vanishing of the $p$-adic L-function at the central point, which by $p$-BSD should equal the algebraic rank. Combined with Kolyvagin's Euler system, it establishes $p$-adic BSD in rank 1 and yields a formula for the $p$-adic regulator.

### Status

Active. Ordinary case largely established; supersingular extension ongoing.

### Classification

Heegner points / $p$-adic heights

---

## E-003 · Mazur–Tate–Teitelbaum L-invariant and BSD

### Statement

Study the L-invariant $\mathcal{L}_p(E)$ defined by Mazur, Tate, and Teitelbaum in their $p$-adic analogue of BSD. For an elliptic curve $E/\mathbb{Q}$ with split multiplicative reduction at a prime $p$, the $p$-adic L-function satisfies $L_p(E, 1) = \mathcal{L}_p(E) \cdot \frac{L(E, 1)}{\Omega_E}$ when $E$ has an exceptional zero at $p$ (i.e., $a_p = 1$). The conjecture is:

$$\mathcal{L}_p(E) = \frac{2 \log_p(q_E)}{\text{ord}_p(q_E)}$$

where $q_E \in p\mathbb{Z}_p$ is the Tate period of $E$. Establish the arithmetic significance of $\mathcal{L}_p(E)$ and its non-vanishing, and relate it to $p$-adic BSD.

### Tools needed

- Tate's parametrisation $E(\mathbb{Q}_p) \cong \mathbb{Q}_p^\times / q_E^{\mathbb{Z}}$
- Modular symbols and $p$-adic measures for constructing $L_p(E, s)$
- Teitelbaum's formula linking $\mathcal{L}_p(E)$ to the $p$-adic logarithm of $q_E$
- Greenberg's framework for exceptional zeros in Iwasawa theory

### What's known

- Mazur–Tate–Teitelbaum (1986): original definition and conjecture for $\mathcal{L}_p(E)$.
- Teitelbaum (1992): proof of the formula $\mathcal{L}_p(E) = 2\log_p(q_E)/\text{ord}_p(q_E)$ in the split multiplicative case.
- Greenberg (1994): systematic study of exceptional zeros; formula for the derivative $L_p'(E, 1)$ in the multiplicative reduction case involving $\mathcal{L}_p(E)$.
- Pixel-by-pixel computational verification for large databases of curves.
- Bertolini–Darmon–Rotger: $\mathcal{L}$-invariants appearing in $p$-adic Beilinson formulae for $\text{GL}_2$.

### Main obstacle

For good ordinary primes (non-split multiplicative or good reduction with $a_p = 1$ is degenerate), the analogue of the MTT $\mathcal{L}$-invariant is not simply $2\log_p(q_E)/\text{ord}_p(q_E)$ and requires entirely different techniques (e.g., Darmon–Rotger's $\mathcal{L}$-invariants via $p$-adic iterated integrals). Defining and computing $\mathcal{L}_p(E)$ for general good ordinary primes is not resolved.

### BSD connection

The MTT L-invariant is exactly the correction factor that appears in $p$-BSD when the $p$-adic L-function has an exceptional zero. Its non-vanishing is equivalent to the $p$-adic BSD formula remaining meaningful despite the vanishing of the interpolation factor. The conjecture $L_p'(E, 1) = \mathcal{L}_p(E) \cdot L(E,1)/\Omega$ is the rank-0 case of $p$-BSD with exceptional zero.

### Status

Established for split multiplicative reduction; active for good ordinary and other cases.

### Classification

L-invariants / exceptional zeros

---

## E-004 · p-adic heights on elliptic curves (Mazur–Tate, Bernardi, Nekovář)

### Statement

Study the theory of canonical $p$-adic heights $\hat{h}_p : E(\bar{\mathbb{Q}}) \to \mathbb{Q}_p$ on elliptic curves $E/\mathbb{Q}$ and the associated $p$-adic height pairing $\langle \cdot, \cdot \rangle_p : E(K) \times E(K) \to \mathbb{Q}_p$. Construct the height via local $p$-adic Green's functions $g_p : E(\mathbb{Q}_p) \times E(\mathbb{Q}_p) \to \mathbb{Q}_p$ satisfying:

$$\hat{h}_p(P) = \sum_{v} \lambda_{p,v}(P)$$

where $\lambda_{p,v}$ are local $p$-adic Néron functions at each place $v$. The canonical height depends on a choice of splitting of the Hodge filtration on $H^1_{\mathrm{dR}}(E/\mathbb{Q})$; study this dependence and the resulting bilinear pairing on the Mordell–Weil group.

### Tools needed

- $p$-adic uniformisation (Tate curve, Raynaud's theory)
- Local $p$-adic Arakelov–Green's functions (Besser, Coleman)
- Coleman integration on elliptic curves
- Nekovář's general theory of $p$-adic heights on motives

### What's known

- Mazur–Tate (1987): original construction of canonical $p$-adic height using modular symbols; they showed $\hat{h}_p$ is a quadratic form.
- Bernardi (1981/1987): explicit formulae for the $p$-adic sigma function and $p$-adic height via the $p$-adic elliptic logarithm; for Tate curves, $\hat{h}_p(P) = \text{ord}_p(\sigma_p(\tilde{P}))$ in terms of the $p$-adic Weierstrass sigma function.
- Nekovář (1993/2006): systematic construction of $p$-adic heights on Selmer groups of $p$-adic representations, not just elliptic curves; relates $p$-adic height to Galois cohomology.
- Besser (2007): computation of $p$-adic heights via Coleman integration on curves.
- Gross–Zagier type formulae require precise normalisation of $\hat{h}_p$.

### Main obstacle

The $p$-adic height is not intrinsic: it depends on a choice of splitting $\sigma : H^1_{\mathrm{dR}}(E) \to F^1 H^1_{\mathrm{dR}}(E)$ of the Hodge filtration, or equivalently a choice of differential. Different choices give heights differing by a bounded quantity; the choice that makes $\hat{h}_p$ equal to the canonical Mazur–Tate height is not always the most computationally convenient. Making $\hat{h}_p$ explicit and computable in the supersingular case is especially challenging: the local Green's function has a logarithmic singularity and the Coleman integral representation requires care.

### BSD connection

The $p$-adic regulator $\text{Reg}_p(E) = \det(\langle P_i, P_j \rangle_p)_{1 \le i,j \le r}$ formed from the $p$-adic height pairing on a basis of $E(\mathbb{Q})/\text{tors}$ appears in the $p$-adic BSD formula as the analogue of the archimedean regulator. $p$-BSD asserts $L_p^{(r)}(E, 1)/r! = \frac{|\Sha| \cdot \text{Reg}_p \cdot \prod c_\ell}{|E(\mathbb{Q})_{\text{tors}}|^2}$ up to an explicit $p$-adic unit.

### Status

Well-developed in the ordinary case; active in the supersingular case.

### Classification

$p$-adic height pairings

---

## E-005 · p-adic Birch and Swinnerton-Dyer conjecture (vis-à-vis classical)

### Statement

Formulate precisely and investigate the $p$-adic Birch and Swinnerton-Dyer conjecture ($p$-BSD), which asserts for an elliptic curve $E/\mathbb{Q}$ with good ordinary reduction at $p$ and rank $r = \text{rank}(E(\mathbb{Q}))$:

$$\frac{L_p^{(r)}(E, 1)}{r!} = \frac{|\Sha(E/\mathbb{Q})[p^\infty]|}{|E(\mathbb{Q})_{\text{tors}}|^2} \cdot \text{Reg}_p(E) \cdot \prod_{\ell | N} c_\ell^{(p)} \cdot \mathcal{E}_p(E)$$

where $\text{Reg}_p(E)$ is the $p$-adic regulator, $c_\ell^{(p)}$ are $p$-adic Tamagawa numbers, and $\mathcal{E}_p(E)$ is a correction factor (trivial when there is no exceptional zero). Compare systematically with classical BSD:

$$\frac{L^{(r)}(E, 1)}{r!} = \frac{|\Sha| \cdot \text{Reg}_\infty \cdot \prod c_\ell \cdot \Omega_E^\pm}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

and clarify the precise relationship between $\text{Reg}_p$ and $\text{Reg}_\infty$, between $p$-adic and complex L-values, and the role of the period $\Omega_E$.

### Tools needed

- Iwasawa main conjecture (Mazur–Swinnerton-Dyer, Rubin, Kato)
- Perrin-Riou's $p$-adic L-function and regulator map
- Control theorems for Selmer groups in $\mathbb{Z}_p$-extensions
- $p$-adic Hodge theory (Bloch–Kato exponential and logarithm)

### What's known

- Mazur–Tate–Teitelbaum (1986): $p$-BSD formulated; proved in many rank 0 cases.
- Kato (2004): Euler systems establishing the $\le$ direction of the Iwasawa main conjecture for modular forms, hence the $\supseteq$ inequality for $\Sha[p^\infty]$.
- Rubin: main conjecture for CM elliptic curves; $p$-BSD in the CM case.
- Skinner–Urban (2014): Iwasawa main conjecture for $\text{GL}_2$ over $\mathbb{Q}$ under technical hypotheses, yielding $p$-BSD when $\text{ord}_{s=1} L(E,s) \le 1$.
- Nekovář: comparison of $p$-adic and classical regulators via $p$-adic Hodge theory.

### Main obstacle

The comparison $\text{Reg}_p(E) / \text{Reg}_\infty(E)$ is not an explicit constant in general: it involves the $p$-adic period $\Omega_p(E)$ (a $p$-adic analogue of the real period) whose relation to $\Omega_E$ is governed by $p$-adic Hodge theory (Fontaine's $B_{\mathrm{dR}}$, $B_{\mathrm{cris}}$). Making this fully explicit and computable, especially for rank $\ge 2$, is the main obstruction to verifying $p$-BSD numerically beyond rank 1.

### BSD connection

$p$-BSD is the $p$-adic incarnation of BSD itself: the Iwasawa main conjecture implies the $p$-part of BSD. The two conjectures are formally equivalent under standard compatibility between $p$-adic and complex L-functions, modulo the comparison of regulators and Tamagawa numbers.

### Status

Conjectural in general; established for rank $\le 1$ under standard hypotheses (Heegner point method + Kato Euler system).

### Classification

Main conjecture / comparison

---

## E-006 · Coleman's p-adic L-functions via overconvergent modular symbols

### Statement

Construct $p$-adic L-functions attached to overconvergent modular forms (and eigenforms of finite slope) using Coleman's overconvergent modular symbols. For a $p$-stabilised eigenform $f = f_p(X) \in S_k^{\dagger}(\Gamma_0(Np))$ of slope $\alpha$ (i.e., $|a_p(f)|_p = |\alpha|_p < 1$ for the smaller root $\alpha$), produce a $p$-adic distribution $\mu_f$ on $\mathbb{Z}_p^\times$ such that for critical $j$:

$$\int_{\mathbb{Z}_p^\times} x^j \, d\mu_f = \mathcal{E}(f, j) \cdot \frac{L(f, j)}{\Omega_f^{\pm}}$$

where $\mathcal{E}(f, j)$ is an explicit Euler-type factor. This must work beyond the ordinary case — for finite slope forms where Hida's theory does not apply.

### Tools needed

- Coleman's theory of overconvergent modular forms (finite slope, $U_p$-eigenforms)
- Stevens' modular symbols and their $p$-adic interpolation
- Pollack–Stevens overconvergent modular symbols: algorithmic construction of $\mu_f$
- $p$-adic Banach spaces and compact operators (eigenvalue perturbation)

### What's known

- Coleman (1997): overconvergent modular forms of finite slope interpolate classical eigenforms.
- Pollack–Stevens (2011): algorithmic construction of overconvergent modular symbols; explicit $p$-adic L-functions for finite-slope forms.
- Pollack (2011): plus/minus $p$-adic L-functions for supersingular primes via Pollack–Stevens symbols.
- Darmon–Pollack: computational verification for large databases of modular forms.
- Blanco-Chacón, Harron: effective computation of overconvergent L-functions.

### Main obstacle

The $U_p$-operator on overconvergent modular symbols is compact but not diagonalisable in general; its eigenvalues cluster, and convergence of the iterative construction of $\mu_f$ is only guaranteed in the finite-slope case. For slope zero (ordinary), one recovers Hida's theory. For higher slopes, the precision loss in $p$-adic computations grows and can make numerical verification impractical. The question of whether $\mu_f$ extends to a measure (vs. merely a distribution) is tied to the growth of Fourier coefficients.

### BSD connection

For an elliptic curve $E/\mathbb{Q}$ with supersingular reduction at $p$ (so $a_p = 0$), the ordinary $p$-adic L-function does not exist. Coleman's construction via overconvergent symbols gives a replacement $p$-adic L-function whose special values at $s=1$ encode the same arithmetic (rank, $\Sha$, Tamagawa numbers) as the classical L-function. This is essential for any formulation of $p$-BSD at supersingular primes.

### Status

Active. Algorithmic constructions available; ongoing refinement of precision and extension to higher-dimensional cases.

### Classification

Overconvergent methods

---

## E-007 · p-adic regulators and their computation

### Statement

Define and compute the $p$-adic regulator $\text{Reg}_p(E)$ associated to an elliptic curve $E/\mathbb{Q}$ of rank $r$: given generators $P_1, \ldots, P_r$ of the free part of $E(\mathbb{Q})$, form the $r \times r$ matrix

$$(\text{Reg}_p(E))_{ij} = \hat{h}_p(P_i, P_j)$$

where $\hat{h}_p$ is the $p$-adic height pairing. Develop efficient algorithms for computing $\text{Reg}_p(E)$ to high $p$-adic precision, and study its arithmetic properties: $p$-adic integrality, relation to the classical regulator, and vanishing/non-vanishing.

### Tools needed

- Explicit $p$-adic heights: Coleman integration, $p$-adic sigma functions (Bernardi, Besser)
- Descent: computing $E(\mathbb{Q})/pE(\mathbb{Q})$ and generators via Mordell–Weil sieve
- $p$-adic precision management (sloppy arithmetic, LLL-style methods)
- Database: Cremona's tables, LMFDB for verification

### What's known

- Bernardi: explicit formulae for $p$-adic heights of points on Tate curves.
- Besser (2007): algorithm for $p$-adic heights on elliptic curves over $\mathbb{Q}$ via Coleman integration, with implementations in Magma/Sage.
- Mazur–Rubin: computational study of $p$-adic regulators for families of curves; observed non-vanishing.
- Balakrishnan–Besser–Müller (2014): practical computation of $p$-adic heights to high precision using Coleman integrals.
- For rank 1, $\text{Reg}_p(E) = \hat{h}_p(P)$ for a generator $P$; studied extensively in connection with $p$-BSD.

### Main obstacle

For rank $\ge 2$, the $p$-adic height pairing matrix has entries that are $p$-adic numbers of unbounded denominator (as precision increases). The conditional number can grow, making reliable computation of $\det(\hat{h}_p(P_i, P_j))$ to high $p$-adic precision expensive. Moreover, the splitting of the Hodge filtration used in the canonical height is often chosen for theoretical convenience; switching to a computationally optimal splitting is non-trivial. Supersingular primes add the difficulty that the local height has a logarithmic singularity.

### BSD connection

The $p$-adic regulator appears directly in the $p$-adic BSD formula. The sign of $\text{Reg}_p(E)$ (a $p$-adic unit, if $p$-BSD holds) and its $p$-adic valuation encode arithmetic information about the curve. Non-vanishing of $\text{Reg}_p$ is a necessary condition for $p$-BSD to predict a finite, non-zero leading coefficient.

### Status

Computationally mature for rank 1 and small rank; active development for higher rank and supersingular primes.

### Classification

Explicit computation

---

## E-008 · The exceptional zero phenomenon (trivial zeroes of p-adic L-functions)

### Statement

Study the exceptional zero phenomenon: an elliptic curve $E/\mathbb{Q}$ with split multiplicative reduction at $p$ satisfies $a_p(E) = 1$, causing the interpolation factor $(1 - a_p^{-1})$ in the construction of $L_p(E, s)$ to vanish at $s = 1$. The $p$-adic L-function therefore has a "trivial zero" at the central point, even though $L(E, 1) \ne 0$ (rank 0 case). Characterise this phenomenon completely: when it occurs, the order of the trivial zero, the leading coefficient (involving $\mathcal{L}_p(E)$), and the relationship to the $p$-adic BSD formula.

More precisely, for $E$ with split multiplicative reduction at $p$, the $p$-adic L-function satisfies:

$$L_p(E, 1) = \mathcal{L}_p(E) \cdot \frac{L(E, 1)}{\Omega_E} \cdot (\text{Euler factors at bad primes})$$

and the $p$-adic BSD conjecture becomes:

$$L_p'(E, 1) = \mathcal{L}_p(E) \cdot \frac{|\Sha| \cdot \prod c_\ell}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

### Tools needed

- Tate curve uniformisation and the Tate period $q_E$
- Mazur–Tate–Teitelbaum construction of $L_p(E, s)$
- Greenberg's Iwasawa-theoretic analysis of exceptional zeros
- $p$-adic logarithm and $p$-adic L-functions of characters

### What's known

- Mazur–Tate–Teitelbaum (1986): identification and naming of the exceptional zero; conjecture for the leading term.
- Teitelbaum (1992): proof for split multiplicative reduction that $L_p(E, 1) = 0$ and formula for $\mathcal{L}_p(E)$.
- Greenberg (1994): Iwasawa-theoretic explanation; the exceptional zero corresponds to a trivial zero in the characteristic ideal of the Selmer group.
- Darmon (2001): exceptional zeros in the context of $p$-adic uniformisation of Shimura curves.
- Venerucci (2016): exceptional zeros and $p$-adic BSD for non-split multiplicative reduction.
- Castella (2015): exceptional zeros for good ordinary primes (when $a_p = 1$ in a suitable sense).

### Main obstacle

For good ordinary reduction with $a_p = 1$ (or more precisely, $a_p \equiv 1 \pmod{p}$ to sufficient precision), the exceptional zero phenomenon is harder to define and study because the Tate uniformisation is not available. The correct analogue of $\mathcal{L}_p(E)$ involves $p$-adic logarithms of Heegner points or Shimura curve parametrisations. The general exceptional zero conjecture (arbitrary reduction type, arbitrary number of primes dividing the conductor) is not fully settled.

### BSD connection

Exceptional zeros are the primary obstruction to applying $p$-BSD naively: the $p$-adic L-function vanishes, so one needs $L_p'(E, 1)$ instead of $L_p(E, 1)$. The MTT conjecture (now largely proved) gives the correct $p$-BSD formula by replacing the central value with the derivative and incorporating $\mathcal{L}_p(E)$. This is essential for numerical verification of $p$-BSD.

### Status

Largely resolved for split multiplicative primes; active for good ordinary and non-split cases.

### Classification

Special values / interpolation

---

## E-009 · p-adic BSD for supersingular primes

### Statement

Formulate and study $p$-BSD when $E/\mathbb{Q}$ has supersingular reduction at $p$ (i.e., $a_p(E) = 0$). In this case the ordinary $p$-adic L-function $L_p^{\text{ord}}(E, s)$ does not exist. The two main approaches are:

1. **Plus/minus $p$-adic L-functions** (Pollack, Kobayashi): decompose $L_p(E, s) = L_p^+(E, s) \oplus L_p^-(E, s)$ using $\log_p^\pm$ maps on $E(\mathbb{Q}_{p^n})$; conjecture that each piece satisfies a modified $p$-BSD formula involving plus/minus regulators and plus/minus Selmer groups.

2. **Overconvergent construction** (via E-006): construct $L_p(E, s)$ as a distribution via overconvergent modular symbols (Pollack–Stevens) and formulate $p$-BSD directly.

The plus/minus $p$-BSD conjecture (Kobayashi, 2003) asserts:

$$\text{ord}_{s=1} L_p^{\pm}(E, s) = \text{rank}_{\mathbb{Z}_p} \text{Sel}_{p^\infty}^{\pm}(E/\mathbb{Q}_\infty)$$

and the leading coefficient formula involves $\text{Reg}_p^{\pm}(E)$ (plus/minus regulators) and plus/minus $p$-adic height pairings.

### Tools needed

- Kobayashi's plus/minus $p$-adic L-functions and local conditions
- Pollack's overconvergent modular symbols approach
- Sprung's $p$-adic Gross–Zagier in the supersingular case
- Castella–Wan: $p$-adic BSD in the supersingular case via Hida families

### What's known

- Kobayashi (2003): plus/minus Selmer groups; conjecture for plus/minus $p$-BSD.
- Pollack (2003): plus/minus $p$-adic L-functions; verified conjecture numerically.
- Kurihara, Perrin-Riou: Iwasawa theory for supersingular primes.
- Sprung (2018): $p$-adic Gross–Zagier for supersingular primes using plus/minus heights.
- Castella–Wan: Iwasawa main conjecture for supersingular primes via congruences with ordinary families.

### Main obstacle

The plus/minus decomposition is not canonical — it depends on the choice of Frobenius eigenvalues at level $p^n$ — and the resulting $p$-adic L-functions $L_p^\pm$ are distributions but not measures in general, complicating their analytic study. The plus/minus regulators $\text{Reg}_p^\pm$ involve logarithms of points on the formal group and the sign decomposition of the $p$-adic height, which is not straightforwardly defined. Establishing the Iwasawa main conjecture for plus/minus Selmer groups is the key unsolved problem.

### BSD connection

Supersingular primes are the hardest case for $p$-BSD. The formulation via plus/minus pieces is conjectured to be the correct one, with each piece satisfying its own BSD-type formula. The total rank $r = r^+ + r^-$ splits according to the plus/minus decomposition of the $p$-adic height pairing.

### Status

Conjectural. Numerical evidence good; proof of the main conjecture is open.

### Classification

Supersingular Iwasawa theory

---

## E-010 · Greenberg's L-invariant and its variations

### Statement

Study Greenberg's generalised $\mathcal{L}$-invariant for an elliptic curve $E/\mathbb{Q}$ and its relation to the MTT $\mathcal{L}$-invariant (E-003). Greenberg defines $\mathcal{L}(E)$ via Iwasawa theory: it is the ratio of the $\mu$-invariant of the characteristic power series of the Pontryagin dual of the Selmer group to the $\mu$-invariant coming from the exceptional zero. More concretely, for $E$ with good ordinary reduction at $p$ and $a_p \equiv 1 \pmod{p^N}$, Greenberg's formula gives:

$$\mathcal{L}_p(E) = \frac{d}{ds}\Big|_{s=1} \log_p\left(\frac{a_{p^n}}{1}\right) \cdot \frac{1}{n} + \ldots$$

involving the $p$-adic logarithm of Frobenius eigenvalues at levels $n \to \infty$. Establish the relation between:

- MTT L-invariant (from the $p$-adic L-function)
- Greenberg's L-invariant (from Iwasawa theory)
- Darmon's L-invariant (from $p$-adic uniformisation)
- Colmez's L-invariant (from $p$-adic representations)

### Tools needed

- Greenberg's Selmer groups and characteristic ideals
- $p$-adic variation of Galois representations (Hida families, eigenvarieties)
- $p$-adic logarithm of Frobenius
- Fontaine–Perrin-Riou $p$-adic Hodge theory

### What's known

- Greenberg (1989, 1994): Iwasawa-theoretic definition of $\mathcal{L}$; relation to exceptional zeros.
- Colmez (1990): $\mathcal{L}$-invariant for representations of $\text{GL}_2(\mathbb{Q}_p)$; shown to equal MTT $\mathcal{L}$ in the modular case.
- Darmon (2001): $\mathcal{L}$-invariant via $p$-adic uniformisation of Shimura curves; equals MTT $\mathcal{L}$ by a theorem of Sander.
- Berger–Li–Zhu (2008): identification of various $\mathcal{L}$-invariants via $p$-adic Hodge theory.
- Breuil, Emerton: $\mathcal{L}$-invariants in the context of $p$-adic Langlands.

### Main obstacle

All known definitions of $\mathcal{L}_p(E)$ are proven to coincide for $E$ with split multiplicative reduction at $p$. For good ordinary reduction, the various approaches give potentially different quantities; their equivalence is conjectured but not established. The $p$-adic Langlands approach (Breuil, Emerton) promises a unified framework but requires substantial input from completed cohomology and eigenvarieties.

### BSD connection

Greenberg's $\mathcal{L}$-invariant appears as the correction factor in $p$-BSD when the $p$-adic L-function has an exceptional zero. Its non-vanishing (which is open in general but expected) ensures the $p$-BSD formula remains non-degenerate. The variation of $\mathcal{L}_p(E)$ in families (e.g., Hida families) is expected to control the variation of the $p$-adic BSD leading coefficient.

### Status

Established for split multiplicative reduction; active for good ordinary primes.

### Classification

L-invariants / $p$-adic variation

---

## E-011 · p-adic Stark conjectures and their relation to BSD

### Statement

Study the $p$-adic Stark conjecture and its implications for BSD. The classical Stark conjecture relates leading coefficients of Artin L-functions at $s = 0$ to regulators of units. The $p$-adic analogue (Dasgupta–Kakde, Spies) asserts that for a totally real field $F$ and a prime $\mathfrak{p}$ of $F$ above $p$, there exist $p$-adic units $\varepsilon_\chi \in \mathbb{C}_p^\times$ (Stark units) for each character $\chi$ of $\text{Gal}(F^{\text{ab}}/F)$ such that:

$$L_p'(\chi, 0) = \left(1 - \frac{\chi(\mathfrak{p})}{N\mathfrak{p}}\right) \log_p(\varepsilon_\chi)$$

where $L_p$ is the $p$-adic Artin L-function. For $F$ an imaginary quadratic field and $E/\mathbb{Q}$ an elliptic curve with CM by $\mathcal{O}_F$, the Stark units conjecturally generate the $p$-part of the Selmer group, connecting $p$-adic Stark to $p$-BSD.

### Tools needed

- Brumer–Stark units and $p$-adic Artin L-functions (Deligne–Ribet, Cassou-Noguès)
- Dasgupta–Kakde proof of the $p$-adic Stark conjecture for totally real fields
- Rubin's proof of the main conjecture for CM fields
- Katz $p$-adic L-functions and CM abelian varieties

### What's known

- Gross (1981): $p$-adic Stark conjecture formulated for CM fields.
- Dasgupta–Kakde (2022): proof of the $p$-adic Stark conjecture for totally real fields, using Teitelbaum's and Dasgupta's refinements of the Gross–Stark conjecture.
- Rubin: main conjecture for CM fields; the $p$-adic L-function of a CM field has its zeroes related to Selmer groups.
- Darmon–Vonk: conjectured construction of Stark–Heegner points (a $p$-adic analogue of Heegner points for non-split primes), connecting $p$-adic Stark to rank-1 BSD for non-CM curves.

### Main obstacle

For non-CM elliptic curves, the connection between $p$-adic Stark units and Selmer groups is conjectural. The Stark–Heegner point construction of Darmon–Vonk gives $p$-adic points on $E$ that are expected to satisfy a $p$-adic Gross–Zagier formula, but the construction relies on $p$-adic integration on $\text{GL}_2(\mathbb{Q}_p)$ that is not yet fully rigorous. Extending Dasgupta–Kakde to non-totally-real base fields (relevant for BSD on CM elliptic curves over imaginary quadratic fields) is the key step.

### BSD connection

In the CM case, $p$-BSD for $E/F$ (CM field $F$) predicts that the $p$-adic L-function value at $s=1$ is controlled by the $p$-adic regulator of Stark units. The $p$-adic Stark conjecture provides exactly the right construction of these units. For rank 1, the Stark unit should coincide (up to $p$-adic units) with the Heegner point or its $p$-adic analogue. Thus $p$-adic Stark is the rank-0/rank-1 case of $p$-BSD for CM curves.

### Status

Resolved for totally real fields (Dasgupta–Kakde); active for CM fields and non-CM elliptic curves.

### Classification

Stark units / $p$-adic L-values

---

# Directions F: Motivic and Cohomological Methods

---

## F-001: Kato's Zeta Element and the BSD Conjecture

**Statement.**
Kato's Euler system construction produces, for a modular elliptic curve E/ℚ and a prime p, a cohomology class z = z_Kato ∈ H¹(ℚ, T_p(E)) that satisfies explicit reciprocity laws at all primes. The Kato zeta element interpolates the special value L(E,1) (or L′(E,1)) through the Perrin-Riou regulator and controls the p-part of the Selmer group Sel_p^∞(E/ℚ). Precisely, Kato's work establishes the implication

    ord_{s=1} L(E,s) ≥ 1  ⟹  rank Sel_p^∞(E/ℚ) ≥ 1

and, via the "explicit reciprocity law" linking the image of z under local conditions at p to the p-adic L-function L_p(E), gives a framework for bounding the p-part of #III(E/ℚ) in terms of L(E,1)/Ω_E up to p-adic periods. The direction aims to make these bounds unconditional (removing the "up to p-adic units" ambiguity) and to extend the construction to general number fields and higher-weight modular forms.

**Tools needed.**
- Galois cohomology of p-adic representations T_p(E) and V_p(E) = T_p(E) ⊗ ℚ_p
- Perrin-Riou exponential map and p-adic Hodge theory (Fontaine's B_dR, B_cris, B_st)
- Iwasawa theory: characteristic ideals, control theorems for Selmer groups over ℤ_p-extensions
- Modular symbols and p-adic L-functions (Amice–Vélu, Vishik)
- Euler system machinery: Kolyvagin derivative classes, explicit reciprocity

**What's known.**
- Kato (2004) proved the existence of the Euler system and established the "rank ≤ 1" direction of BSD for semistable E/ℚ at primes p ∤ 6·cond(E), conditional on the non-degeneracy of the Perrin-Riou regulator.
- Rubin's Euler system machinery gives unconditional results for CM elliptic curves where the Hecke character provides an explicit zeta element.
- Kato's theorem implies: if L(E,1) ≠ 0, then #III(E)[p^∞] is finite and ord_p(#III(E)) ≤ 2·ord_p(L(E,1)/Ω_E) + correction terms.
- Skinner–Urban and Kato–Kurihara–Sujatha refined the bounds via the Iwasawa main conjecture (proved by Kato for modular forms and by Skinner–Urban for p-ordinary E).

**Main obstacle.**
The Perrin-Riou regulator map Reg_p: H¹(ℚ_p, T_p(E) ⊗ ℂ_p) → ℂ_p is not known to be computable in closed form for general E; the image of Kato's class z under Reg_p equals L_p(E,1) only up to an explicit p-adic period whose p-adic valuation depends on the crystalline structure of E at p. Removing this ambiguity requires a comparison between the syntomic regulator (Besser) and the Perrin-Riou regulator, which is open in general.

**BSD connection.**
Kato's zeta element provides the "Euler system bound" on the p-Selmer group, which is the cohomological avatar of the p-part of the Birch and Swinnerton-Dyer formula. The inequality rank Sel ≤ ord_{s=1} L(E,s) is the easy direction of BSD; equality (and the exact formula for #III) requires the Euler system to be "sharp," which amounts to proving the p-part of BSD.

**Status.** Active research. Partial results for CM curves (Rubin), ordinary primes (Skinner–Urban), and supersingular primes (Kobayashi, Iovita–Pollack). Full resolution open.

**Classification.** Core theory — high priority.

---

## F-002: Beilinson's Conjecture for L′(E,1) When rank = 1

**Statement.**
Let E/ℚ be an elliptic curve with analytic rank 1, so L(E,s) has a simple zero at s = 1. Beilinson's conjecture predicts that the regulator map

    reg_{D}: K₁(E)^(1) → H¹_D(E/ℚ, ℚ(1)) ≅ E(ℚ) ⊗ ℚ  (Beilinson–Soulé)

generalizes to a statement about the leading Taylor coefficient: there exists a "Beilinson element" β ∈ K₂(E)^(2) (a higher Chow cycle or motivic cohomology class in H¹_M(E, ℚ(2))) whose image under the Beilinson regulator

    r_D: H¹_M(E, ℚ(2)) → H¹_D(E, ℝ(2))

is nonzero and satisfies

    L′(E,1) / Ω_E = c · r_D(β)

for an explicit rational constant c involving #III(E), |E(ℚ)_tors|², and the Tamagawa numbers. More precisely, the Bloch–Beilinson conjecture framework predicts an isomorphism between the graded piece of the Chow group CH²(E,1) (higher Chow group of codimension-2 cycles on E with modulus 1) and the tangent space of the Selmer variety, with the regulator measuring the "transcendental part."

**Tools needed.**
- Higher Chow groups CH^j(X,n) as defined by Bloch; motivic cohomology H^i_M(X, ℚ(j)) via Voevodsky's triangulated category DM
- Beilinson regulator map r_D: K_n(X)^(j) → ⊕_p H^n_D(X, ℝ(j)) (Deligne cohomology)
- Eisenstein symbols and modular units (Beilinson's explicit construction via Siegel units on X_0(N))
- Deninger's pairing: K₂(E) × K₂(E) → K₂(ℚ) → K₂(ℚ)^{(2)} ≅ ℤ via the tame symbol / regulator
- Explicit computation of Deligne cohomology: H¹_D(E, ℝ(2)) ≅ ℝ / (period lattice computation)

**What's known.**
- Beilinson (1985) proved L′(E,1)/Ω_E ∈ ℚ^× for E modular by constructing explicit elements in K₂(X_0(N)) using Eisenstein series and showing the regulator is a nonzero period.
- Bloch and Grayson computed numerical examples confirming the conjecture for specific curves.
- Deninger (1984) established a direct link between K₂ of modular curves and the L-function derivative via the Eisenstein symbol.
- For Shimura curves (indefinite quaternion algebras), analogous constructions exist via the Jacquet–Langlands correspondence.

**Main obstacle.**
The explicit construction of β ∈ K₂(E) via Eisenstein symbols depends on the modular parametrization X_0(N) → E, which is highly non-canonical (choice of cusp, sign conventions). No direct construction exists for E without a modular parametrization, and extending to totally real fields requires Shimura curve machinery that is not fully developed for the rank-1 case.

**BSD connection.**
Beilinson's conjecture for L′(E,1) is the "rank 1" case of the general Bloch–Beilinson philosophy: the order of vanishing of L(E,s) at s=1 equals the dimension of a certain motivic cohomology group (here H¹_M(E, ℚ(2)) modulo its "trivial" part), and the leading coefficient is given by the regulator image. This directly implies the rank part of BSD and, combined with Bloch–Kato, gives the formula for #III.

**Status.** Proved for E/ℚ modular (Beilinson, Deninger). Numerical verification in many cases. Extension to number fields and non-modular E open.

**Classification.** Core theory — high priority.

---

## F-003: Bloch–Kato Conjecture on Special Values of L-Functions

**Statement.**
Let M be a pure motive over ℚ of weight w with coefficients in a number field F, and let L(M,s) be its L-function. The Bloch–Kato conjecture (1990) generalizes the Birch and Swinnerton-Dyer conjecture, the Bloch–Beilinson conjecture, and Deligne's conjecture on special values. At an integer point s = n with n ≤ 0 or n > w (the "critical" or "non-critical" regime), the conjecture predicts:

1. **Order of vanishing:** ord_{s=n} L(M,s) = dim_F H¹_f(ℚ, M^*(n)) − dim_F H⁰(ℚ, M^*(n)), where H¹_f ⊆ H¹(ℚ, M^*(n)) is the Bloch–Kato Selmer group (defined via local conditions using Fontaine's periods B_dR, B_cris, B_st) and M^*(n) = M^∨(n)(1) is the dual Tate twist.

2. **Leading coefficient:** L^{(r)}(M,n) / (period) = #H¹_f(ℚ, M^*(n))_tors / #H¹ / H¹_f(ℚ, M^*(n)) × (Tamagawa factors) / (#H⁰(ℚ, M^*(n)))², where the period is an explicit product of periods of M depending on n and the Hodge filtration.

For M = h¹(E), n = 1, this recovers the Birch and Swinnerton-Dyer conjecture exactly.

**Tools needed.**
- Fontaine's p-adic Hodge theory: filtered (φ, N)-modules, (φ, Γ)-modules, rings B_dR, B_cris, B_st, B_ht
- Selmer groups H¹_f(ℚ, V) for V a p-adic representation, defined by local conditions at each prime: H¹_f(ℚ_p, V) = ker(H¹(ℚ_p, V) → H¹(ℚ_p, V ⊗ B_cris)) for p-adic V
- Tamagawa factors: local Euler factors, periods Ω_∞(M) computed from Betti/de Rham/Rham comparison
- Motivic cohomology H^i_M(X, ℚ(j)) and its relation to algebraic K-theory via the Bloch–Lichtenbaum spectral sequence
- The Iwasawa main conjecture (proved for GL_2 by Kato, Skinner–Urban; general case by Emerton et al.)

**What's known.**
- For M = ℚ(0), n ≤ 0: trivially true (values of ζ at negative integers, interpreted via Bernoulli numbers).
- For M = ℚ(1), n = 1: Dirichlet's class number formula (L-functions of Dirichlet characters at s=1).
- For M = h¹(E), n = 1: the Birch and Swinnerton-Dyer conjecture (proven for rank ≤ 1 by Gross–Zagier + Kolyvagin).
- For M = h²(S), n = 2 where S is a K3 surface: partial results by van Geemen, Top, and Elsenhans–Jahnel via explicit computation of transcendental lattices.
- For M = h¹(A) with A an abelian variety over ℚ with GL_2-type: partial results extending Kolyvagin's method (Nekovář).
- Kato (2004) proves the "≤" direction of the Bloch–Kato conjecture for all modular motives M = h^i(X) with X modular, i.e., ord_{s=n} L(M,s) ≤ dim H¹_f.

**Main obstacle.**
The "≥" direction (lower bounds on Selmer groups from L-values) requires constructing enough cohomology classes from the special value, which is the content of the Euler system program. For general motives beyond the modular/GL_2 world, no Euler systems are known. The construction of Kato-type Euler systems for GL_n (n ≥ 3) is the central open problem.

**BSD connection.**
The Bloch–Kato conjecture for M = h¹(E), n = 1 is *exactly* the Birch and Swinnerton-Dyer conjecture. More precisely, H¹_f(ℚ, V_p(E)) = Sel_p^∞(E/ℚ), and the Tamagawa factors, torsion, and period in the Bloch–Kato formula coincide with the classical BSD terms.

**Status.** Open in general. Proven for rank ≤ 1 elliptic curves over ℚ (Gross–Zagier, Kolyvagin). Partial results for CM abelian varieties (Rubin), Hilbert modular forms (Dasgupta, Spies), and function field analogues (Lafforgue).

**Classification.** Grand challenge — flagship open problem.

---

## F-004: Syntomic Cohomology and p-Adic Regulators (Besser)

**Statement.**
Syntomic cohomology, introduced by Fontaine and Messing and developed by Besser, is the p-adic analogue of Deligne cohomology. For a smooth variety X over ℤ_p, the syntomic cohomology H^i_syn(X, ℤ_p(j)) fits in a triangle relating crystalline cohomology and de Rham cohomology, providing a p-adic "absolute Hodge cohomology." Besser defined a concrete p-adic regulator map

    reg_p: K_n(X) → H^n_syn(X, ℤ_p(j))

using p-adic integration (the Amice–Vélu / Vishik p-adic measure attached to modular forms) and showed it agrees with the syntomic regulator constructed by Fontaine–Messing. The key result is that for a smooth curve X over a p-adic field, the composite

    K₂(X) →^{reg_p} H²_syn(X, ℤ_p(2)) →^{comparison} H¹_dR(X)/F⁰

can be computed explicitly via Coleman integration of p-adic polylogarithms. This direction aims to: (a) compute the p-adic regulator for K₂ of elliptic curves explicitly enough to compare with Kato's Perrin-Riou regulator, and (b) extend Besser's p-adic integration methods to higher K-groups K_n (n ≥ 3).

**Tools needed.**
- Syntomic cohomology H^i_syn(X, ℤ_p(j)) as defined by Fontaine–Messing; the syntomic site (X ⊗ ℤ_p, A_cris)
- Besser's p-adic regulator: K_n(X) → H^n_syn(X, ℤ_p(j)) via the Denis lemma and p-adic polylogarithms
- Coleman integration: the theory of p-adic integrals of closed 1-forms on p-adic curves, extended to the polylogarithm sheaf
- de Rham cohomology with its Hodge filtration F^j H^i_dR(X/ℤ_p)
- The crystalline comparison isomorphism: H^i_cris(X/W(k)) ⊗ B_cris ≅ H^i_dR(X/K) ⊗ B_cris

**What's known.**
- Besser (2000) gave an explicit formula for the p-adic regulator on K₂ of curves over p-adic fields in terms of Coleman integrals, proving it coincides with the syntomic regulator.
- Besser, de Jeu, and Roblot extended this to compute K₂ of specific modular curves numerically.
- For K₁ = O^×, the p-adic regulator is the p-adic logarithm, well understood.
- For K₀, it is the degree map. The pattern suggests K_n should involve iterated Coleman integrals (p-adic polylogarithms of depth n−1).
- Yamashita and Asakawa studied the syntomic regulator on higher K-theory of curves using rigid analytic methods.

**Main obstacle.**
For n ≥ 3, the syntomic regulator involves iterated integration that is not yet fully developed in the p-adic setting. The p-adic polylogarithm of depth ≥ 3 is not well understood (its relationship to motivic polylogarithms is conjectural). Without explicit formulas, comparing reg_p with Kato's Perrin-Riou regulator map remains incomplete.

**BSD connection.**
The p-adic regulator is the bridge between Kato's zeta element (an arithmetic object in Galois cohomology) and the special value L(E,1) (an analytic object). If Besser's regulator could be computed explicitly enough to show that reg_p(z_Kato) = L_p(E,1) exactly (not just up to units), this would remove the "up to p-adic periods" ambiguity in Kato's theorem and prove the p-part of BSD unconditionally.

**Status.** Active research. K₂ case well-developed (Besser). K₃ and higher cases open. Computational tools exist but are not yet sufficient for the BSD application.

**Classification.** Technical tool — enabling technology.

---

## F-005: Griffiths Groups and Higher Chow Cycles on Elliptic Curves

**Statement.**
Let E be an elliptic curve over a number field F. The Griffiths group Gr^j(X) = Z^j(X) / (algebraic equivalence) ∩ Z^j(X) measures cycles that are homologically trivial but not algebraically equivalent to zero. For elliptic curves, the relevant Griffiths group is Gr^2(E × E) (codimension-2 cycles on the surface E × E), which contains information about the rank of E via the Ceresa cycle and related constructions. The higher Chow groups CH^j(X,n) (Bloch) provide a refinement: CH²(E,1) maps via the regulator to Deligne cohomology H²_D(E, ℝ(2)) ≅ ℝ, and the image of CH²(E,1) is conjecturally related to L′(E,1)/Ω_E. This direction studies the structure of CH²(E,1) and Gr²(E) for elliptic curves, aiming to connect the "algebraic" side (cycles and their relations) to the "transcendental" side (regulator values and L-function coefficients).

**Tools needed.**
- Higher Chow groups CH^i(X,n): Bloch's original definition via the cubical structure on the cycle complex, or Voevodsky's motivic cohomology H^{2i−n}_M(X, ℤ(i))
- The Abel–Jacobi map: CH^j(X)_hom → H^{2j−1}(X, ℂ) / (F^j + H^{2j−1}(X, ℤ)) (intermediate Jacobian)
- Ceresa cycle: the cycle C − C^{−} in the Jacobian J(C) of a curve C, where C is embedded via an Abel–Jacobi map
- Bloch's conjecture: for a surface S with p_g = 0, CH₀(S) is representable (finite-dimensional)
- The Bloch–Beilinson filtration on CH^j(X)_ℚ with graded pieces related to Ext groups in Voevodsky's category

**What's known.**
- Bloch (1984) proved that for an elliptic curve E over ℚ, CH²(E,1) is isomorphic (via the regulator) to a subgroup of ℝ, and the image contains the period Ω_E.
- Beilinson showed that CH²(X_0(N),1) has rank ≥ 1 for any N, generated by the "Beilinson element" constructed from Siegel units.
- For E/ℚ with rank 1, CH²(E,1) is expected to have rank exactly 1 over ℚ, with the regulator map being injective on the transcendental part.
- Soulé and others proved finiteness results for torsion in higher Chow groups.
- Schoen proved that CH₀ of certain fiber products of elliptic surfaces can be infinite-dimensional, illustrating the complexity of cycle groups.

**Main obstacle.**
Proving injectivity (or even finite kernel) of the regulator map on CH²(E,1) is a major open problem, closely related to the Beilinson–Soulé vanishing conjecture. The Bloch–Beilinson filtration is largely conjectural: the expected exact sequences relating motivic cohomology, K-theory, and Deligne cohomology are not established in sufficient generality.

**BSD connection.**
The rank of CH²(E,1) over ℚ is expected to equal ord_{s=1} L(E,s). For rank 1, this means the Beilinson element in CH²(E,1) should be the unique (up to ℚ^×) nontrivial class, and its regulator should give L′(E,1)/Ω_E. For rank ≥ 2, one needs "enough" higher Chow cycles to account for the order of vanishing, which is the content of the Bloch–Beilinson conjecture.

**Status.** Partial results. Injectivity of regulator on CH²(E,1) open. Numerical computations confirm predictions for many curves.

**Classification.** Core theory — structural.

---

## F-006: Regulator Maps from K₂(E) to ℝ (Beilinson's Theorem)

**Statement.**
For a smooth projective variety X over ℚ, Beilinson constructed a regulator map

    r_D: K_n(X) ⊗ ℚ → ⊕_p H^n_D(X, ℚ(p))

from Quillen K-theory to Deligne cohomology. For an elliptic curve E/ℚ with n = 2, p = 2, the relevant piece is

    r_D: K₂(E) →^{Chow} CH²(E,1) →^{reg} H²_D(E, ℝ(2)) ≅ ℝ.

Beilinson's theorem (1985) shows that for the modular curve X = X_0(N), the composite is nonzero: the "Eisenstein element" e ∈ K₂(X) constructed from the Eisenstein series of weight 2 has a nonzero regulator, equal to L′(E,1)/(2π)² up to rational factors. This direction studies: (a) the kernel and cokernel of r_D on K₂(E), (b) the relation between r_D and other regulators (étale, syntomic, Beilinson's Borel regulator), and (c) explicit computation of r_D for specific curves.

**Tools needed.**
- Quillen K-theory K_n(X) for schemes; the Brown–Gersten–Quillen spectral sequence
- Deligne cohomology H^i_D(X, ℝ(p)): defined as H^i(X, ℂ) with Hodge filtration, i.e., the hypercohomology of the complex ℤ(p)_D = (2πi)^p ℤ → Ω^0 → ··· → Ω^{p−1}
- The Chern character ch: K_n(X) ⊗ ℚ → ⊕_i H^{2i−n}(X, ℚ(i)) connecting K-theory to motivic cohomology
- Beilinson's Eisenstein symbol: a map from modular units (divisors of Siegel units) on X_0(N) to K₂(X_0(N))
- The Abel–Jacobi map and extensions of mixed Hodge structures

**What's known.**
- Beilinson (1985) proved that r_D(e) ≠ 0 for the Eisenstein element e ∈ K₂(X_0(N)), establishing L′(E,1) ∈ (2π)² · ℚ^× for E = J_0(N).
- Bloch (1984) computed K₂ of the Tate curve and related it to the Kubert–Lichtenbaum conjecture on units in cyclotomic fields.
- Deninger (1984) gave a direct construction linking K₂(X_0(N)) to modular forms via Eisenstein series.
- Borel (1977) proved that the regulator map K_n(𝒪_F) ⊗ ℝ → ℝ^{d_n} is injective for n ≥ 2, with image determined by ζ_F(n) (Borel's theorem on the K-theory of rings of integers).
- For n = 2: K₂(𝒪_F) ⊗ ℝ ≅ ℝ^{r₂} if F is totally imaginary, and the regulator gives the volume of the "Borel regulator class," related to ζ_F(2).

**Main obstacle.**
Computing r_D on K₂(E) explicitly requires understanding the motivic-to-Deligne comparison at the level of cocycle representatives. For general E (not necessarily a modular quotient of X_0(N)), there is no known construction of nontrivial elements in K₂(E). Even for modular E, the Eisenstein symbol construction is highly non-canonical and depends on choices of cusps and embeddings.

**BSD connection.**
Beilinson's theorem is the prototype for the "rank 1" case of BSD via K-theory: the regulator image of K₂(E) in ℝ is related to L′(E,1)/Ω_E. If the rank of E is r, one expects dim_ℚ (K₂(E) ⊗ ℚ)^{(2)} = r (or more precisely, the motivic cohomology group H¹_M(E, ℚ(2)) has rank r), with the regulator providing the "transcendental" part of the BSD formula.

**Status.** Beilinson's theorem proved. Computational methods exist (de Jeu, Zagier). Extension to rank ≥ 2 partially open.

**Classification.** Core theory — established results, computational challenges remain.

---

## F-007: Motivic L-Functions and Their Special Values

**Statement.**
The motivic L-function L(M, s) of a pure motive M over ℚ (or a number field) is defined via the ℓ-adic realization: for each prime ℓ, the ℓ-adic cohomology H^i_ét(X_ℚ̄, ℚ_ℓ) carries a continuous action of Gal(ℚ̄/ℚ), and L(M, s) is the Euler product of local L-factors defined by the characteristic polynomial of Frobenius at each unramified prime. The conjecture of Deligne (critical values) and Bloch–Beilinson (all values) predicts that the order of vanishing and the leading coefficient of L(M, s) at integer points are governed by motivic cohomology and regulator maps. This direction studies the general framework: how motivic L-functions arise from motivic cohomology complexes (Voevodsky's triangulated category DM), and how their special values should be computed via regulator maps from motivic to Deligne, Betti, de Rham, and étale cohomology.

**Tools needed.**
- Voevodsky's triangulated category of motives DM(k): the derived category of the category of Nisnevich sheaves with transfers, with ℚ-coefficients
- The motivic t-structure (conjectural): pure motives as the heart, mixed motives as the full category
- L-functions of motives: defined via ℓ-adic representations; Artin formalism for products, twists, symmetric powers
- Regulator maps: motivic → Deligne (Beilinson), motivic → étale (Soulé), motivic → absolute Hodge (Deligne)
- The Stark conjecture and its refinements: relating L′(χ, 0) to regulators of units (abelian case)

**What's known.**
- Deligne (1979) proved the conjecture on critical values for motives that are "critical" (where the L-function can be normalized by periods to have algebraic values).
- For non-critical values (s outside the critical range), Beilinson's conjecture predicts the regulator formula, proved in many cases for L-functions of modular forms.
- The Langlands program (in its motivic incarnation, via the "motivic Langlands correspondence") predicts that L-functions of automorphic representations should be motivic L-functions.
- Pure motives: the category of pure motives (Chow motives) is a well-defined abelian category assuming the standard conjectures (which are open).

**Main obstacle.**
The category of mixed motives DM^eff_ℚ does not have a well-understood t-structure: the "motivic t-structure" whose heart would be the category of mixed motives MM is conjectural. Without it, the motivic L-function of a general object of DM cannot be defined rigorously. The standard conjectures (which would make the category of pure motives abelian semisimple) remain open for surfaces in general.

**BSD connection.**
The motive h¹(E) of an elliptic curve E has motivic L-function L(h¹(E), s) = L(E, s). The motivic cohomology groups H^i_M(E, ℚ(j)) are expected to be computable and to yield, via the regulator, the BSD formula. The motivic perspective is the "correct" framework in which BSD is a special case of a universal conjecture on special values.

**Status.** The framework is well-developed conjecturally. Proofs exist only for specific cases (critical values: Deligne; rank ≤ 1: Gross–Zagier–Kolyvagin). The full motivic t-structure remains one of the deepest open problems in algebraic geometry.

**Classification.** Structural framework — foundational.

---

## F-008: Deligne Cohomology and the BSD Formula

**Statement.**
Deligne cohomology H^i_D(X, ℤ(p)) (or ℚ(p), ℝ(p)) for a smooth projective variety X over ℚ is the hypercohomology of the cone complex

    ℤ(p)_D = Cone(ℤ(p) ⊕ F^p Ω^•_X → Ω^•_X)[-1]

where ℤ(p) = (2πi)^p ℤ ⊂ ℂ, and F^p is the Hodge filtration. For an elliptic curve E, the relevant groups are:

- H¹_D(E, ℚ(1)) ≅ E(ℚ) ⊗ ℚ  (the Mordell–Weil group tensored with ℚ)
- H²_D(E, ℚ(2)) ≅ ℝ  (via the regulator on K₂)

The BSD formula can be expressed as a statement about the "size" of the Selmer group in Deligne cohomology: the dimension of the image of the regulator map from motivic cohomology to H¹_D(E, ℝ(1)) = E(ℚ) ⊗ ℝ should equal the rank of E, and the covolume of the lattice (the Néron–Tate height pairing determinant, i.e., the regulator Reg(E)) should appear in the formula

    lim_{s→1} L(E,s) / (s−1)^r = Ω_E · Reg(E) · #III(E) · ∏ c_p / |E(ℚ)_tors|².

This direction studies how the Deligne cohomology framework organizes the terms of BSD.

**Tools needed.**
- Deligne cohomology: H^i_D(X, ℤ(p)) = H^i(X, ℤ(p)_D), defined as the hypercohomology of the cone complex
- Mixed Hodge structures: Deligne's theory of weights and filtrations on cohomology of varieties
- The comparison isomorphisms: H^i_D(X, ℚ(p)) → Ext^1_{MHS}(ℚ, H^i(X, ℚ(p))) (extensions of mixed Hodge structures)
- Arakelov intersection theory: the arithmetic Chow group CH^p(X̄) with its regulator to Deligne cohomology
- The Néron–Tate height: ⟨·,·⟩: E(ℚ) × E(ℚ) → ℝ, the canonical quadratic form whose determinant is Reg(E)

**What's known.**
- For h⁰ and h² of E, the Deligne cohomology is well understood and yields the trivial parts of the L-function.
- The regulator map K₁(E) → H¹_D(E, ℚ(1)) = E(ℚ) ⊗ ℚ is surjective (it is the identity map under the identification K₁(E) = E(ℚ) ⊕ ℚ^× by Bass–Tate).
- Néron–Tate theory gives the height pairing and the regulator Reg(E) as a real number.
- The BSD formula involves Reg(E) only for r ≥ 1; for r = 0, it reduces to L(E,1) / Ω_E = (#III · ∏ c_p) / |E(ℚ)_tors|².

**Main obstacle.**
The "size" of the Selmer group (as a lattice in Deligne cohomology) is not directly accessible via algebraic geometry: it requires the arithmetic input of the Néron–Tate height. The passage from the motivic cohomology group H¹_M(E, ℚ(j)) to the Deligne cohomology group H¹_D(E, ℝ(j)) loses the arithmetic information (torsion, integrality) that distinguishes the Selmer group from its real span.

**BSD connection.**
Deligne cohomology is the natural target of the regulator map and provides the "real" side of the BSD formula. The identification H¹_D(E, ℝ(1)) = E(ℚ) ⊗ ℝ with its lattice structure (from integral motivic cohomology) and the Néron–Tate height pairing encodes the regulator Reg(E). The formula L^{(r)}(E,1) = Ω_E · Reg(E) · #III · ∏ c_p / |E(ℚ)_tors|² can be read as a statement about the covolume of the motivic lattice inside Deligne cohomology.

**Status.** Conceptual framework well-established. The difficulty lies in connecting the motivic lattice (which is arithmetic) to the L-value (which is analytic).

**Classification.** Structural framework — conceptual.

---

## F-009: K-Theoretic Approach to Finiteness of III

**Statement.**
The Shafarevich–Tate group III(E/ℚ) = ker(H¹(ℚ, E) → ∏_v H¹(ℚ_v, E)) is conjecturally finite. The K-theoretic approach seeks to interpret III as the torsion in a K-theoretic or motivic cohomology group and to prove finiteness via algebraic K-theory methods. Specifically:

1. The group III(E/ℚ)[p^∞] embeds into H¹(ℚ, E[p^∞]) / (local images), which is the Bloch–Kato Selmer group H¹_f(ℚ, V_p(E)/T_p(E)) modulo the image of E(ℚ) ⊗ ℚ_p/ℤ_p.

2. Via the motivic-to-étale regulator, one can study the Selmer group as a subgroup of étale motivic cohomology: H¹_ét(E, ℤ_p(1)) / (image of K₁(E)). The finiteness of III is then related to the finiteness of the torsion in the étale K-theory of E.

3. The K-theory of 𝒪_{E,S} (the ring of S-integers of E considered as a scheme) and its relation to class field theory provides an alternative route: the Quillen–Lichtenbaum conjecture (now a theorem, by Voevodsky–Rost) identifies K-theory with étale cohomology, and the resulting finite generation results can be applied to Selmer groups.

**Tools needed.**
- Étale motivic cohomology: H^i_ét(X, ℤ_p(j)) and its relation to algebraic K-theory via the Quillen–Lichtenbaum conjecture (Voevodsky–Rost proof of the Milnor conjecture / Bloch–Kato conjecture)
- Galois cohomology: Selmer groups, local conditions, Poitou–Tate duality
- The Hochschild–Serre spectral sequence: H^p(Gal(F_S/F), H^q_ét(X_{F_S}, ℤ_p(j))) converging to H^{p+q}_ét(X, ℤ_p(j))
- Iwasawa theory: control theorems for Selmer groups over ℤ_p-extensions, characteristic ideals
- Kato's Euler system and Kolyvagin's system of derivatives

**What's known.**
- Kolyvagin (1989) proved III(E/ℚ)[p^∞] is finite for E with analytic rank ≤ 1 (assuming E is modular).
- The Voevodsky–Rost theorem (Milnor conjecture / Bloch–Kato conjecture for mod-p Galois cohomology) identifies K_n(𝔽)/p with H^n_ét(Spec 𝔽, μ_p^{⊗n}), providing the bridge between K-theory and Galois cohomology.
- Nekovář extended Kolyvagin's method to higher-rank cases under parity conditions (the parity conjecture for Selmer ranks).
- Iwasawa-theoretic results (Greenberg, Perrin-Riou) give finiteness results for III over ℤ_p-extensions under certain conditions.

**Main obstacle.**
The direct K-theoretic interpretation of III as a torsion group in K-theory is not rigorous: the expected exact sequence relating K₂(E) → H²_ét(E, ℤ_p(2)) → III → 0 involves the comparison between motivic and étale cohomology, which is not established for degree 2 and p-coefficients in the required generality. The Quillen–Lichtenbaum conjecture handles mod-p coefficients but not ℤ_p-coefficients in the needed range.

**BSD connection.**
The finiteness of III is one of the key ingredients of the BSD formula. A K-theoretic proof of finiteness would ideally also give a formula for #III in terms of K-theoretic invariants (regulators, Tamagawa numbers), which would be the K-theoretic version of the BSD formula.

**Status.** Finiteness proved for rank ≤ 1 (Kolyvagin). Open in general. The K-theoretic approach is largely conjectural but has the potential to give a conceptual proof.

**Classification.** Core theory — ambitious.

---

## F-010: Arithmetic Chow Groups and Arakelov Theory for BSD

**Statement.**
Arakelov geometry (Arakelov, Gillet–Soulé) extends intersection theory to arithmetic varieties by adding "fibers at infinity": for a regular model 𝒳 of a variety X over ℚ, the arithmetic Chow group CĤ^p(𝒳) consists of pairs (Z, g) where Z is a codimension-p cycle and g is a Green current (a smooth form on X(ℂ) satisfying dd^c g + δ_Z = ω for some smooth form ω). The arithmetic intersection pairing

    ⟨·,·⟩_Ar: CĤ^p(𝒳) × CĤ^{d+1−p}(𝒳) → ℝ

(where d = dim X) combines the algebraic intersection number at finite primes with the Archimedean contribution ∫_{X(ℂ)} g₁ ∧ dd^c g₂ ∧ ω^{d−p}. For elliptic curves, the arithmetic Chow group CĤ²(𝒳) (where 𝒳 is a regular model of E over Spec ℤ) contains arithmetic cycles whose intersection theory encodes the height pairing. Arakelov's theorem (refined by Faltings) expresses the Néron–Tate height as an arithmetic intersection number, providing a direct link between the arithmetic of E and the Archimedean periods.

This direction uses arithmetic Chow groups to reinterpret the BSD formula: the regulator Reg(E) is an arithmetic intersection determinant, the Tamagawa factors c_p are local intersection multiplicities, and the period Ω_E is the volume of the complex torus E(ℂ) = ℂ/Λ. The goal is to prove the BSD formula by arithmetic intersection methods.

**Tools needed.**
- Arithmetic Chow groups CĤ^p(𝒳) (Gillet–Soulé): the group of pairs (Z, g) modulo rational equivalences
- Green currents and their functorial properties: the arithmetic Chern character cĥ: K̂₀(𝒳) → ⊕_p CĤ^p(𝒳) ⊗ ℚ
- Faltings' arithmetic Riemann–Roch: a formula for the arithmetic degree of the determinant of cohomology line bundle
- Néron models and their special fibers: the regular model 𝒳 → Spec ℤ and the structure of the special fiber at each prime p
- The arithmetic Hodge index theorem (Moriwaki, Yuan–Zhang): the signature of the arithmetic intersection form

**What's known.**
- Faltings (1992) proved the arithmetic Hodge index theorem and used it to give a proof of the Mordell conjecture via Arakelov theory.
- For E/ℚ, the arithmetic self-intersection of the trivial section on the Néron model gives the Faltings height h_F(E), which is related to Ω_E via exp(−h_F(E)) ~ Ω_E / √|Δ_E| (up to Archimedean factors).
- Moriwaki and Yuan–Zhang proved arithmetic analogues of the Hodge index theorem and Noether's formula in Arakelov geometry.
- The arithmetic Bogomolov–Miyaoka–Yau inequality (Miyaoka, Mourougane) constrains the arithmetic Chern numbers.

**Main obstacle.**
Arakelov geometry works well for curves but the extension to higher-dimensional arithmetic varieties is technically demanding. The main obstacle for BSD is that the arithmetic Chow group CĤ²(𝒳) for a surface 𝒳 is not well understood: the "Archimedean" contribution to the height pairing involves transcendental data (the Faltings height, the Petersson inner product) that cannot be captured by algebraic geometry alone. The formula #III · ∏ c_p / |E(ℚ)_tors|² = L(E,1) · Reg(E) / Ω_E involves both arithmetic (finite) and transcendental (Archimedean) parts in a way that is hard to disentangle.

**BSD connection.**
Arakelov theory provides a unified framework in which all terms of the BSD formula have geometric meaning: Reg(E) is an arithmetic intersection determinant, Ω_E is a volume, c_p are local intersection numbers, #III is an obstruction to global rationality. The goal is to prove the BSD formula as an arithmetic Riemann–Roch theorem.

**Status.** Partial results for height computations (Gross–Zagier, Zhang). The full arithmetic Riemann–Roch approach to BSD is an active research program.

**Classification.** Advanced technique — high potential.

---

## F-011: Deninger's Program: L-Functions and Cohomological Formalism

**Statement.**
Deninger (1994–present) proposed a cohomological framework in which the Hasse–Weil L-function of a variety X over ℚ would be expressed as a regularized determinant

    L(X, s) = det_∞(s − Θ | H^•_?(X))

where Θ is a hypothetical "Frobenius" operator on a cohomology theory H^•_?(X) whose eigenvalues are the zeros and poles of L(X, s). This cohomology should satisfy:

1. **Infinite-dimensional:** The spaces H^i_?(X) are infinite-dimensional (reflecting the infinite number of zeros of L-functions), unlike finite-dimensional ℓ-adic or de Rham cohomology.
2. **Frobenius eigenvalues = zeros of L:** The eigenvalues of Θ on H^i_? are exactly the zeros ρ of L(X, s) with Im(ρ) related to i.
3. **Functional equation:** Comes from a Poincaré duality on H^•_? and the relation Θ ↦ (something involving the weight).
4. **Riemann Hypothesis:** All eigenvalues of Θ on H¹_? have real part 1/2 (i.e., all nontrivial zeros of ζ(s) lie on the critical line).

For an elliptic curve E, the L-function L(E, s) should be expressed as such a determinant, and the BSD conjecture would follow from understanding the structure of H^•_?(E) and the regulator on it.

**Tools needed.**
- Regularized determinants: det_∞(A) for operators A on infinite-dimensional spaces, defined via zeta regularization (ζ_A(s) = Tr(A^{−s}), det_∞(A) = exp(−ζ_A′(0)))
- The Bost–Connes system and its generalizations: quantum statistical mechanical systems whose partition functions are L-functions
- Foliation cohomology: Deninger's model for H^•_? uses the cohomology of a foliation on a "arithmetic site" (not rigorously defined)
- The Sarnak–Deninger program: relating the explicit formula for L-functions to the trace formula on a hypothetical dynamical system
- Absolute Hodge cohomology (Deligne) and motivic cohomology as approximations to H^•_?

**What's known.**
- Deninger showed that for the Riemann zeta function, the explicit formula (relating zeros to primes) has the same form as the Lefschetz trace formula for a dynamical system, suggesting a "universal cohomology" exists.
- Connes (1999) gave a rigorous quantum statistical mechanical interpretation of the Riemann zeta function via the adèle class space ℚ^×\𝔸_ℚ, but this does not give the zeros as eigenvalues.
- For function fields, the ℓ-adic cohomology of the Frobenius acting on H^i_ét(X, ℚ_ℓ) realizes the analogous picture: L(X, s) = ∏_i det(1 − Fr·q^{−s} | H^i_ét)^{(−1)^{i+1}}. The number field case has no such finite-dimensional cohomology.
- Deninger constructed explicit infinite-dimensional spaces for curves over function fields that degenerate to the ℓ-adic cohomology in the limit.

**Main obstacle.**
The fundamental obstacle is the absence of a "Frobenius at the infinite place": in the function field case, Frobenius is a geometric endomorphism; in the number field case, there is no analogous operator on any known cohomology theory. The construction of H^•_?(X) for number field varieties remains purely conjectural.

**BSD connection.**
If Deninger's program succeeds, the BSD formula for E would be a consequence of the cohomological formula L(E,s) = det_∞(s − Θ | H^•_?(E)), combined with a "regularized trace formula" that computes the leading coefficient of det_∞(s − Θ) at s = 1 in terms of the regulator on H^•_?(E) and the "size" of the Selmer group as a subspace.

**Status.** Purely conjectural program. Partial results for function fields and the Riemann zeta function. No construction of H^•_? for general number field varieties.

**Classification.** Visionary program — very high risk, very high reward.

---

## F-012: Soulé Regulators and Computational Motivic Cohomology

**Statement.**
Soulé (1984) constructed regulator maps from algebraic K-theory to étale cohomology:

    reg_ét: K_n(𝒪_F) → H^n_ét(Spec 𝒪_F[1/S], ℤ_p(j))

for a number field F, a set S of primes including those above p and the Archimedean places, and j a twist. These regulators provide the étale side of the Beilinson–Soulé conjecture on the relationship between motivic cohomology, K-theory, and ℓ-adic cohomology. Specifically, the Soulé regulator factors through motivic cohomology:

    K_n(𝒪_F) → H^n_M(Spec 𝒪_F, ℤ(j)) → H^n_ét(Spec 𝒪_F[1/S], ℤ_p(j))

The conjecture of Beilinson–Soulé predicts that H^n_M(Spec 𝒪_F, ℤ(j)) = 0 for n < 0 (or n < j in some conventions), and that the image of the regulator in étale cohomology is the "correct" Selmer group. This direction develops computational methods for the Soulé regulator and uses them to verify BSD-related predictions.

**Tools needed.**
- Étale motivic cohomology: H^n_ét(X, ℤ_p(j)) and its comparison with algebraic K-theory via the Quillen–Lichtenbaum conjecture (theorem of Voevodsky–Rost–Weibel)
- The Chern character in étale cohomology: the maps K_n(X) → H^n_ét(X, ℤ_p(j)) constructed via the Postnikov tower of the K-theory spectrum and the comparison with the motivic spectrum
- Soulé's explicit description of the regulator: using the language of symbols in K-theory (Steinberg symbols {a, b} ∈ K₂ for n=2) and their images in Galois cohomology
- Computational algebraic number theory: computation of K-groups K_n(𝒪_F) for small n and specific F (via the Merkurjev–Suslin theorem for n=2, the Rost–Voevodsky theorem for n=3)
- p-adic L-functions and Iwasawa theory: the Main Conjecture relates characteristic ideals of Selmer groups to p-adic L-functions

**What's known.**
- K₁(𝒪_F) = 𝒪_F^× (units), and the Soulé regulator on K₁ is the p-adic logarithm.
- K₂(𝒪_F) is related to the Brauer group and tame symbols; the Soulé regulator on K₂ is computed via the Galois symbol K₂(F)/p → H²_ét(F, μ_p^{⊗2}).
- K₃(𝒪_F) is related to the Bloch group ℬ(F); computations exist for specific fields (Gangl, Zagier, Goncharov).
- The Merkurjev–Suslin theorem (1982) identifies K₂(F)/n with H²_ét(F, μ_n^{⊗2}), providing an explicit formula for the mod-n Soulé regulator on K₂.
- The Rost–Voevodsky theorem (Bloch–Kato conjecture, proved 2009) generalizes this to all n: K_n(F)/m ≅ H^n_ét(F, μ_m^{⊗n}).

**Main obstacle.**
Computational: for n ≥ 3, the K-groups K_n(𝒪_F) become very large and difficult to compute. The relationship between the Soulé regulator (étale side) and the Beilinson regulator (Deligne/Riemann side) is not explicit in degree ≥ 3, making it hard to compare the étale Selmer group with the analytic data from L-functions.

**BSD connection.**
The Soulé regulator provides the "étale" side of the BSD formula. The Selmer group Sel_p^∞(E/ℚ) is the étale cohomology group H¹_ét(E[1/p], ℤ_p(1)) with local conditions, and the Soulé regulator maps K-theory to this group. The BSD formula in the Bloch–Kato framework is a statement about the image of the Soulé regulator and its relation to L-values.

**Status.** Active computational research. K₂ computations well-developed. K₃ computations in progress. The comparison between Soulé and Beilinson regulators is open for n ≥ 3.

**Classification.** Computational — tools and verification.

---

# Directions G: Deformation Theory and Langlands Program

---

## G-001. Taylor-Wiles Method Extensions for Higher-Rank Selmer Groups

### Statement

Extend the Taylor-Wiles patching method to control Selmer groups of Galois representations $\rho \colon G_{F} \to \mathrm{GL}_n(\overline{\mathbb{F}}_\ell)$ for $n \geq 3$ and number fields $F$ beyond $\mathbb{Q}$. Specifically, for an absolutely irreducible residual representation $\bar\rho$, show that the patched deformation ring $R_\infty$ is isomorphic to the patched Hecke algebra $\mathbb{T}_\infty$ over the ring of diamond operators $\mathbb{S}_\infty \cong \mathcal{O}[[x_1,\ldots,x_r]]$, and deduce that the Selmer group $\mathrm{Sel}_{\Sigma}(F, \mathrm{ad}\,\bar\rho(1))$ has $\mathcal{O}$-corank equal to the order of vanishing of the adjoint L-function $L(\mathrm{ad}\,\bar\rho, s)$ at $s=1$.

### Tools needed

- Taylor-Wiles primes $Q = \{q_1,\ldots,q_N\}$ with $q_i \equiv 1 \pmod{\ell^M}$ and $\bar\rho(\mathrm{Frob}_{q_i})$ having distinct eigenvalues $\{\alpha_i, \beta_i\}$
- Kisin's framing technique: $R_\infty^{\square_Q} \twoheadrightarrow R_Q$ with $R_\infty^{\square_Q} \cong \mathcal{O}[[S_\infty, T_\infty]]$
- Patching of homology of arithmetic groups (Scholze's perfectoid approach or classical Borel-Serre)
- Fontaine-Laffaille theory or Breuil modules for the local deformation rings at $\ell$
- Poitou-Tate duality for Selmer groups

### What's known

- Taylor-Wiles (1995): original method for $\mathrm{GL}_2$ over $\mathbb{Q}$, proves modularity of semistable elliptic curves
- Diamond (1997): extended to $\mathrm{GL}_2$ over totally real fields with specified ramification
- Wiles (1995): the numerical criterion $\#H^1_\Sigma / H^1_{\Sigma,\mathrm{str}} = \#\Phi$ suffices
- Kisin (2009): framed deformation rings avoid the need for vanishing of $H^0$; works for $\mathrm{GL}_n$ over CM fields
- Calegari-Geraghty (2016): extended to general $\mathrm{GL}_n$ over totally real/CM fields using derived Hecke algebras and the $t$-exactness of the completed cohomology functor
- Allen et al. (2018): potential automorphy over CM fields for $\mathrm{GL}_n$

### Main obstacle

For $n \geq 3$, the patched module $M_\infty$ over $R_\infty$ need not be free over $\mathbb{S}_\infty$; the derived Hecke algebra methods of Calegari-Geraghty produce a perfect complex rather than a single module, and extracting the Selmer group requires controlling the cohomological amplitude. Specifically, the obstruction lies in $H^2(G_{F,\Sigma}, \mathrm{ad}^0 \bar\rho)$, which can be nonzero for $n \geq 3$.

### BSD connection

The Selmer group $\mathrm{Sel}(F, V_\ell(E))$ is the $\ell$-primary part of $\mathrm{Sha}(E/F)$ (up to local terms). Controlling its rank via Taylor-Wiles patching directly addresses the algebraic side of BSD. The method produces a congruence ideal $\eta_{\mathbb{T}}$ whose $\mathcal{O}$-adic valuation equals the order of vanishing of $L(\mathrm{ad}\,\bar\rho, s)$ at $s=1$; by the factorization $L(E,s) = L(\mathrm{ad}\,\bar\rho, s) \cdot \zeta_F(s)$, this constrains $\mathrm{ord}_{s=1} L(E,s)$.

### Status

Active research. The $\mathrm{GL}_2$ case over totally real fields is essentially complete (Kisin, 2009). The $\mathrm{GL}_n$ case requires derived methods and is known for regular weight under mild hypotheses (Calegari-Geraghty, 2016). The passage to irregular weight and general coefficient fields remains open.

### Classification

Foundational — enables all modularity lifting results in this group.

---

## G-002. Residually Reducible Galois Representations (Skinner-Wiles)

### Statement

Establish modularity of elliptic curves $E/\mathbb{Q}$ whose associated residual representation $\bar\rho_{E,\ell} \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{F}}_\ell)$ is reducible (i.e., $\bar\rho_{E,\ell} \sim \begin{pmatrix} \chi_1 & * \\ 0 & \chi_2 \end{pmatrix}$ with $\chi_1/\chi_2 = \bar\varepsilon$, the mod-$\ell$ cyclotomic character). Prove that $R = \mathbb{T}$ in the residually reducible case under appropriate Selmer-group vanishing hypotheses.

### Tools needed

- The Skinner-Wiles auxiliary prime technique: choose primes $q$ such that $a_q(E) \not\equiv q+1 \pmod{\ell}$ to force $\bar\rho_{E,\ell}$ to become absolutely irreducible after restriction to $G_{\mathbb{Q}(\mu_\ell)}$
- Deformation conditions at $\ell$: ordinary deformation rings $R_\ell^{\mathrm{ord}}$ parameterizing lifts with a specified filtration
- Wiles's asymptotic formula for $\#H^1_\Sigma / H^1_{\Sigma,\mathrm{str}}$
- Ribet's lemma on raising the level: if $\bar\rho$ is modular of level $N$ and $q \| N$, then modularity at level $N/q$ under suitable conditions
- Greenberg's Selmer group bounds for the reducible case

### What's known

- Skinner-Wiles (1999): proved ordinary modularity for $E/\mathbb{Q}$ with $\bar\rho_{E,\ell}$ reducible and $\ell > 3$, assuming $E$ has good ordinary reduction at $\ell$ and $\mathrm{Sel}_{\ell^\infty}(E/\mathbb{Q})$ is finite
- Skinner-Wiles (2001): extended to allow $\ell = 3$ under additional hypotheses
- Skinner (2014): proved $a_p(E) \equiv p+1 \pmod{\ell^2}$ under certain Selmer-group conditions
- Dasgupta-Kakde (2022): new approach to the reducible case via Eisenstein cocycles and the Gross-Stark conjecture
- Newton (2022): proved modularity in the residually reducible case for $\mathrm{GL}_2$ over totally real fields with some restrictions

### Main obstacle

The ordinary deformation ring $R_\ell^{\mathrm{ord}}$ in the reducible case is typically not a domain and has higher dimension than in the irreducible case. The map $R_\ell^{\mathrm{ord}} \to \mathbb{T}$ need not be an isomorphism; one shows only that $R_\ell^{\mathrm{ord}} / \eta \cong \mathbb{T}/\eta$ for a congruence ideal $\eta$, but controlling the cokernel requires vanishing of a dual Selmer group $H^1_{\Sigma^\perp}(F, \mathrm{ad}\,\bar\rho(1))$. The recent work of Dasgupta-Kakde circumvents some of this but introduces analytic dependencies (the Gross-Stark conjecture, now proved).

### BSD connection

The residually reducible case arises naturally: for any $E/\mathbb{Q}$ and any prime $\ell | \#\mathrm{Sha}(E/\mathbb{Q})[\ell^\infty]$, the residual representation is reducible (by Ribet). Proving modularity in this case is therefore essential for establishing the $\ell$-part of BSD via Galois methods for any elliptic curve with nontrivial Sha. The Selmer-group finiteness hypothesis in Skinner-Wiles is precisely the rank-0 case of BSD.

### Status

Active research. The ordinary case for $\mathrm{GL}_2/\mathbb{Q}$ is essentially resolved (Skinner-Wiles, Dasgupta-Kakde). The crystalline case and the extension to $\mathrm{GL}_2$ over totally real fields remain partially open.

### Classification

Core techniques — essential for rank 0 and rank 1 cases of BSD.

---

## G-003. Fontaine-Laffaille Modules and Local Deformation Rings

### Statement

Classify the local deformation rings $R_v^{\square, \mathbf{v}}$ for $v \nmid \ell$ and $R_\ell^{\square, \mathrm{cr}, \mathbf{v}}$ for $v = \ell$ parameterizing crystalline lifts of a given $\bar\rho|_{G_{\mathbb{Q}_\ell}}$ with prescribed Hodge-Tate weights $\mathbf{v} = (0, k-1)$, $k \geq 2$. Show these rings are formally smooth over $\mathcal{O}$ of the expected dimension, and compute their tangent space dimensions in terms of Fontaine-Laffaille invariants.

### Tools needed

- Fontaine-Laffaille theory: filtered Dieudonné modules over $\mathbb{Z}_\ell$ for $\ell > k$ (the "Fontaine-Laffaille range")
- Kisin's theory of $(\varphi, \hat{G})$-modules extending beyond the FL range
- The framed deformation functor $\mathcal{D}_{\bar\rho}^{\square, \mathrm{cr}, \mathbf{v}} \colon \mathrm{Art}_{\mathcal{O}} \to \mathrm{Sets}$
- Breuil-Kisin classification of crystalline representations via Kisin modules
- Explicit computation of $H^1(G_{\mathbb{Q}_\ell}, \mathrm{ad}\,\bar\rho)$ using local Tate duality

### What's known

- Fontaine-Laffaille (1982): classification of crystalline representations with Hodge-Tate weights in $[0, \ell-2]$
- Kisin (2006): $R_\ell^{\square, \mathrm{cr}, \mathbf{v}}$ is formally smooth of dimension $4 + [F:\mathbb{Q}]\binom{n}{2}$ for $\mathrm{GL}_n$ in the Fontaine-Laffaille range
- Böckle (2001): local deformation rings at $v \neq \ell$ are formally smooth of dimension $n^2$ under the "Taylor-Wiles condition" (no conjugate-self-dual obstructions)
- Gee (2011): explicit computations of tangent space dimensions for $\mathrm{GL}_2$ crystalline deformation rings
- Emerton-Gee (2022): comprehensive study of local-global compatibility for $\mathrm{GL}_n$ over arbitrary number fields using the geometry of stacks of $(\varphi, \hat{G})$-modules

### Main obstacle

Outside the Fontaine-Laffaille range ($\ell \leq k$), Kisin's theory via Breuil modules introduces complications: the crystalline deformation ring $R_\ell^{\square, \mathrm{cr}, \mathbf{v}}$ need not be formally smooth. One must control the Galois cohomology group $H^2(G_{\mathbb{Q}_\ell}, \mathrm{ad}\,\bar\rho)$, which contributes obstructions to smoothness. For $n = 2$ and $\ell \geq 5$, the problem is largely resolved, but for $\ell = 2,3$ or $n \geq 3$, the local rings can have embedded primes and non-reduced structure.

### BSD connection

The local deformation conditions at $\ell$ determine the Selmer conditions cutting out $H^1_f(G_{\mathbb{Q}}, \mathrm{ad}\,\bar\rho)$. The dimension formula for $R_\ell^{\square, \mathrm{cr}}$ enters the Taylor-Wiles numerical criterion: one needs $\dim R_\ell^{\square, \mathrm{cr}} = 4 + \dim H^0(G_{\mathbb{Q}_\ell}, \mathrm{ad}\,\bar\rho) - \dim H^0(G_{\mathbb{Q}_\ell}, \mathrm{ad}^0\bar\rho(1))$ for the patching to work. Smoothness of $R_\ell^{\square, \mathrm{cr}}$ implies no obstructions and hence clean control of the Selmer group.

### Status

Largely resolved for $\mathrm{GL}_2$ and $\ell \geq 5$ (Kisin, 2006). Active research for $\ell = 2,3$ and $\mathrm{GL}_n$ with $n \geq 3$. The Emerton-Gee stack-theoretic framework provides a systematic approach but explicit computations remain difficult.

### Classification

Local analysis — foundational input to the global patching method.

---

## G-004. Modularity Lifting for Higher-Dimensional Representations

### Statement

Prove that a continuous representation $\rho \colon G_F \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ satisfying the following conditions is automorphic:

1. **Residual automorphy**: $\bar\rho|_{G_{F(\zeta_\ell)}}$ is automorphic (a regular algebraic conjugate-self-dual cuspidal automorphic representation $\Pi$ of $\mathrm{GL}_n(\mathbb{A}_F)$ with $\Pi_\infty$ having specified weight).
2. **Local conditions**: $\rho|_{G_{F_v}}$ is crystalline with regular Hodge-Tate weights for $v | \ell$; $\rho$ satisfies the Taylor-Wiles condition at auxiliary primes.
3. **Hyperspecial level**: $\rho|_{G_{F_v}}$ is unramified for $v \nmid N\ell$.
4. **Oddness**: For $F$ totally real and $n$ even, $\det \rho(c_v) = (-1)^{n/2}$ for complex conjugation $c_v$.

### Tools needed

- The Calegari-Geraghty method: patching in the derived category to handle $n \geq 3$
- Potential automorphy (Thorne, 2015): $\bar\rho|_{G_{F'}}$ is automorphic for some solvable CM extension $F'/F$
- Breuil-Mézard conjecture (now theorem for $\mathrm{GL}_2$, partial for $\mathrm{GL}_n$): local geometry controls global modularity
- Derived Hecke algebra: $H^*(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho)$ acts on completed cohomology $\widetilde{H}^*$
- Scholze's perfectoid methods for constructing Galois representations from completed cohomology

### What's known

- Khare-Wintenberger (2009): Serre's conjecture for $\mathrm{GL}_2/\mathbb{Q}$, combining Taylor-Wiles with Ihara's lemma and level raising
- Kisin (2009): modularity of $\mathrm{GL}_2$ over totally real fields with Taylor-Wiles conditions
- Thorne (2015): potential modularity for $\mathrm{GL}_n$ over CM fields, building on Taylor's potential automorphy
- Allen et al. (2018): automorphy lifting for $\mathrm{GL}_n$ over CM fields under the "tame" Taylor-Wiles condition
- Newton-Thorne (2020): proved symmetric power functoriality for $\mathrm{GL}_2$ in many cases, implying strong modularity results
- Calegari (2023): new approaches to the Calegari-Geraghty method via condensed mathematics

### Main obstacle

For $n \geq 3$, the global deformation ring $R_{\bar\rho}^{\Sigma, \mathbf{v}}$ may not be a complete intersection. The patching module $M_\infty$ over $R_\infty$ has nontrivial higher homology in derived patching, and one cannot simply read off the Selmer group from $R = \mathbb{T}$. One needs to control the "defect" $\delta = \mathrm{pd}_{R_\infty}(M_\infty) - \dim R_\infty$, which measures the failure of the patched module to be Cohen-Macaulay. For $\mathrm{GL}_3$, this is handled by Calegari-Geraghty, but for $\mathrm{GL}_n$ with large $n$, the defect grows and its control requires new ideas.

### BSD connection

Higher-dimensional modularity lifting is needed to attack BSD for elliptic curves over number fields $F \neq \mathbb{Q}$ where $\rho_{E,\ell}$ can only be made modular after base change. If $E/F$ is an elliptic curve over a CM field $F$ and $\rho_{E,\ell}$ satisfies the conditions above, then $L(E/F, s) = L(\pi, s)$ for an automorphic $\pi$, giving analytic continuation and functional equation — prerequisites for BSD. Moreover, the automorphy of $\mathrm{Sym}^m \rho_{E,\ell}$ (Newton-Thorne) implies nonvanishing of $L(E, \mathrm{Sym}^m, s)$ in families.

### Status

Active research. The $\mathrm{GL}_2$ case over totally real fields is well-established. The $\mathrm{GL}_n$ case over CM fields is known under residual automorphy hypotheses (Allen et al., 2018). Removing residual automorphy is the main open problem.

### Classification

Core techniques — the engine connecting Galois representations to automorphic forms.

---

## G-005. The Langlands-Weissman Approach to L-Values

### Statement

Develop the Langlands-Weissman framework for Brylinski-Deligne extensions of reductive groups and its associated L-functions, with the goal of expressing central L-values $L(1/2, \pi)$ for representations $\pi$ of groups $G(\mathbb{A}_F)$ in terms of period integrals and cohomological invariants. Specifically, for the "standard L-function" attached to $\mathrm{GL}_2$ via the Rankin-Selberg method extended to Brylinski-Deligne covers, prove an algebraic formula:

$$L^*(1/2, \pi) = \frac{|\alpha(P_\pi)|^2}{\langle \phi, \phi \rangle} \cdot \Omega$$

where $P_\pi$ is the period integral over a Shimura variety, $\phi$ is a test vector, and $\Omega$ is an explicit product of local factors.

### Tools needed

- Brylinski-Deligne central extensions of reductive groups by $K_2$
- Langlands-Weissman L-group formalism for non-connected L-groups
- The Rankin-Selberg integral representation of L-functions
- Ichino-Ikeda (2010) and Gan-Gross-Prasad (2012) conjectures on period integrals
- Relative trace formula (RTF) of Jacquet, and its comparison with the stable trace formula

### What's known

- Weissman (2017-2023): developed the theory of Brylinski-Deligne extensions and their L-groups; constructed L-functions for metaplectic groups using the "small Witt group" formalism
- Gan-Gross-Prasad (2012): conjectures relating periods to L-values for $\mathrm{SO}_n \times \mathrm{SO}_{n+1}$
- Ichino-Ikeda (2010): proved the GGP conjecture in low rank for tempered representations
- Waldspurger (2003): $L(1/2, \pi \times \chi) = $ local factors $\times$ period$^2$ for $\mathrm{GL}_2$
- Beuzart-Plessis (2015): local multiplicity formulas for tempered representations
- Chaudouard (2019): stabilization of the relative trace formula for the Jacquet-Rallis setting

### Main obstacle

The Langlands-Weissman framework introduces metaplectic L-groups whose dual groups are disconnected. The standard functoriality formalism (L-functions from L-homomorphisms) extends, but the representation theory of disconnected groups introduces complications: Arthur's endoscopic classification does not directly apply, and the trace formula must be adapted. For BSD applications, one needs the extension from tempered to non-tempered representations, which requires handling Eisenstein cohomology.

### BSD connection

The Rankin-Selberg method for $L(E, s) = L(1/2, \pi_f)$ expresses the central value as a period integral over an arithmetic quotient. The Langlands-Weissman framework generalizes this to covers of $\mathrm{GL}_2$, which arise naturally in the metaplectic method for quadratic forms (Waldspurger, Gross-Zagier). An algebraic formula for $L(1/2, \pi)$ in terms of periods directly gives the "analytic side" of BSD.

### Status

Active research. The theoretical framework is developed (Weissman, 2023). Explicit L-value formulas are known in low rank (Waldspurger, Gross-Zagier). The general framework for $\mathrm{GL}_n$ and its covers remains incomplete.

### Classification

New framework — potentially unifying approach to central L-values.

---

## G-006. Functoriality and L-Function Special Values (Langlands Program)

### Statement

Establish cases of the Langlands functoriality conjecture relevant to BSD: specifically, prove that for an elliptic curve $E/F$ with associated Galois representation $\rho_{E,\ell}$, the automorphic representation $\pi_E$ attached to $E$ satisfies:

1. **Symmetric power functoriality**: $\mathrm{Sym}^m \pi_E$ is automorphic for all $m \geq 1$
2. **Base change**: $\pi_{E/F'}$ is automorphic for any finite extension $F'/F$
3. **L-value factorization**: $L(E/F', s) = \prod_{\pi'} L(1/2, \pi')$ where $\pi'$ ranges over base change components

and derive consequences for the order of vanishing of $L(E, s)$ at $s = 1$.

### Tools needed

- Arthur's endoscopic classification for $\mathrm{GL}_n$ and classical groups
- The stable trace formula and stabilization (Arthur, Waldspurger, Chaudouard)
- Automorphic induction and base change (Langlands, Arthur-Clozel)
- Potential automorphy theorems (Taylor et al., Thorne)
- Converse theorems (Cogdell-Piatetski-Shapiro for $\mathrm{GL}_n$)
- The Braverman-Kazhdan/Ngô Schwartz space for the trace formula

### What's known

- Harris-Taylor (2001): local Langlands for $\mathrm{GL}_n$
- Henniart (2000): alternative proof of local Langlands for $\mathrm{GL}_n$
- Arthur (2013): endoscopic classification for symplectic and orthogonal groups
- Clozel-Harris-Taylor (2008): automorphy of $\mathrm{Sym}^m$ for $\mathrm{GL}_2$ over $\mathbb{Q}$ with $m \leq 4$ and "most" $E$
- Newton-Thorne (2020): symmetric power functoriality for $\mathrm{GL}_2$ over totally real fields, $m$ arbitrary, for a set of primes of density 1
- Caraiani-Newton (2021): further extensions to $\mathrm{GL}_n$ over CM fields

### Main obstacle

Full symmetric power functoriality for all $m$ simultaneously requires controlling the Arthur-Selberg trace formula for $\mathrm{GL}_m$ as $m \to \infty$. The current methods (potential automorphy + Ihara's lemma + level raising) produce automorphy for each $m$ separately but cannot handle the entire tower uniformly. The spectral side of the trace formula for $\mathrm{GL}_m$ involves representations whose analytic behavior (temperedness, cuspidality) is not well-understood for large $m$.

### BSD connection

Symmetric power functoriality constrains the analytic behavior of $L(E, s)$:
- $\mathrm{Sym}^m \pi_E$ automorphic $\Rightarrow$ $L(E, \mathrm{Sym}^m, s)$ has meromorphic continuation
- Nonvanishing of $L(E, \mathrm{Sym}^m, 1/2)$ for small $m$ (following from automorphy) implies $\mathrm{ord}_{s=1} L(E, s) = 0$ (by the factorization of $L(E, s)$ through symmetric powers)
- Conversely, if $\mathrm{ord}_{s=1} L(E,s) \geq 1$, then $L(E, \mathrm{Sym}^m, 1/2)$ must vanish for all odd $m$

This gives a spectral approach to bounding the analytic rank.

### Status

Active research. Newton-Thorne (2020) is a major breakthrough for $\mathrm{GL}_2$. The full Langlands functoriality conjecture remains open.

### Classification

Functoriality — the deepest structural input to BSD via automorphic methods.

---

## G-007. Deformation Rings and Hecke Algebras at Eisenstein Primes

### Statement

Study the structure of the local deformation ring $R_\ell^{\mathrm{ord}}$ and the Hecke algebra $\mathbb{T}_\ell$ at primes $\mathfrak{p} | p$ of $\mathbb{T}$ where the residual representation $\bar\rho$ is reducible (Eisenstein). Prove that the quotient $R_\ell^{\mathrm{ord}} / \eta_{\mathbb{T}}$ is isomorphic to $\mathbb{T}_\ell / \eta_{\mathbb{T}}$ and compute the structure of $R_\ell^{\mathrm{ord}}$ as a complete local $\mathcal{O}$-algebra, including its Krull dimension, embedding dimension, and the multiplicity of its irreducible components.

### Tools needed

- Ordinary deformation conditions: $R_\ell^{\mathrm{ord}}$ parameterizing lifts with an unramified quotient character
- The Eisenstein ideal $\mathfrak{E} \subset \mathbb{T}$: the ideal generated by $T_q - (q+1)$ for $q \nmid N\ell$
- Mazur's Eisenstein ideal theory (1977) for $X_0(N)$
- The Wiles numerical criterion: $\#H^1_\Sigma / H^1_{\Sigma,\mathrm{str}} = \#\Phi_{\mathrm{loc}}$ implies $R = \mathbb{T}$
- Ribet's converse to Herbrand: $\ell | \#\mathrm{Sha}(E/\mathbb{Q}) \Rightarrow \ell | \#E(\mathbb{Q})_{\mathrm{tors}}$ (or the correct Galois cohomological variant)
- Ohta's control theorem for ordinary cohomology of modular curves

### What's known

- Mazur (1977): the Eisenstein ideal for $X_0(p)$; showed $\mathbb{T}/\mathfrak{E} \cong \mathbb{F}_\ell$ and $\#\mathbb{T}/\mathfrak{E}^2$ relates to numerator of $(p-1)/12$
- Wiles (1995): the numerical criterion in the residually reducible case
- Skinner-Wiles (1999): $R = \mathbb{T}$ for ordinary deformations with reducible residual representation, assuming Selmer-group vanishing
- Ohta (1995, 1999): control theorems for ordinary homology of modular curves; $R_\ell^{\mathrm{ord}}$ is a complete intersection in the $\mathrm{GL}_2/\mathbb{Q}$ case
- Dasgupta-Darmon-Pollack (2011): computation of the ordinary deformation ring at Eisenstein primes for $\mathrm{GL}_2$
- Wake and Wang-Erickson (2019): free-standing deformation rings and the structure of $R_\ell^{\mathrm{ord}}$ without assuming $R = \mathbb{T}$

### Main obstacle

At Eisenstein primes, the tangent space of the deformation functor has dimension $\geq 2$ (because there is a nontrivial extension $\bar\rho \sim \begin{pmatrix} \varepsilon & * \\ 0 & 1 \end{pmatrix}$ and the $*$ can vary freely). This means $R_\ell^{\mathrm{ord}}$ has dimension $\geq 2$, so it cannot be a discrete valuation ring. The congruence ideal $\eta_{\mathbb{T}}$ cuts out a codimension-1 subscheme, but controlling the geometry of $R_\ell^{\mathrm{ord}}$ along the Eisenstein component requires understanding the pseudo-representation and its relation to the adjoint L-value.

### BSD connection

Eisenstein primes correspond to congruences between modular forms of different levels and weights. If $\ell | \#\mathrm{Sha}(E/\mathbb{Q})$, then $\bar\rho_{E,\ell}$ is reducible and the prime above $\ell$ in $\mathbb{T}$ is Eisenstein. The structure of $R_\ell^{\mathrm{ord}}$ at this prime controls the $\ell$-adic Selmer group $\mathrm{Sel}_{\ell^\infty}(E/\mathbb{Q})$ via the pseudo-deformation theory. More precisely, $\mathrm{Sel}_{\ell^\infty}(E/\mathbb{Q})$ is finite if and only if $R_\ell^{\mathrm{ord}} / \eta_{\mathbb{T}}$ is a discrete valuation ring, which is equivalent to the $\mu$-invariant of the $p$-adic L-function vanishing.

### Status

Active research. Well-understood for $\mathrm{GL}_2/\mathbb{Q}$ (Ohta, Dasgupta-Darmon-Pollack). Open for $\mathrm{GL}_n$ with $n \geq 3$ and for $\mathrm{GL}_2$ over general number fields.

### Classification

Core techniques — controls the reducible/Eisenstein cases of BSD.

---

## G-008. Galois Deformation Theory and Selmer Group Structure

### Statement

Develop the general theory of Galois deformation functors $\mathcal{D}_{\bar\rho}^{\Sigma, \mathcal{L}}$ with local conditions $\mathcal{L} = \{L_v\}_{v \in \Sigma}$ and relate their structure to Selmer groups. Specifically:

1. Show that the tangent space $t_{\mathcal{D}} = H^1_{\mathcal{L}}(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho)$ and the obstruction space $\mathrm{Obs} \subset H^2_{\mathcal{L}}(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho)$
2. Prove that the Selmer group $\mathrm{Sel}(F, \mathrm{ad}\,\bar\rho(1))$ is dual to $H^2_{\mathcal{L}^\perp}(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho)$ via Poitou-Tate
3. Deduce that $\dim t_{\mathcal{D}} - \dim \mathrm{Obs} = \dim H^0(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho) - \dim H^0(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho(1)) + \sum_{v \in \Sigma} (\dim L_v - \dim H^0(G_{F_v}, \mathrm{ad}\,\bar\rho))$

### Tools needed

- Mazur's deformation theory (1989): $\mathcal{D}_{\bar\rho}$ is a functor $\mathrm{Art}_{\mathcal{O}} \to \mathrm{Sets}$
- Schlessinger's criteria: pro-representability when $\mathrm{End}_{G_F}(\bar\rho) = \mathcal{O}$
- Poitou-Tate exact sequence for Selmer groups
- Greenberg's Selmer groups: $H^1_{\mathcal{L}}$ and $H^1_{\mathcal{L}^\perp}$ (dual Selmer conditions)
- Böckle's theory of global deformation rings with local conditions
- Nakayama's lemma for complete local rings

### What's known

- Mazur (1989): foundational deformation theory for $\mathrm{GL}_2$
- Böckle (2001): general theory of deformations with local conditions; $R_{\bar\rho}^{\Sigma, \mathcal{L}}$ exists under mild hypotheses
- Nyssen-Rouquier (2002): pseudo-representations and their deformations
- Bellaïche-Chenevier (2009): families of Galois representations and the $\mu$-adic Selmer group
- Kisin (2006): the local-global compatibility for deformation rings and Hecke algebras
- Emerton-Gee (2022): the moduli stack $\mathscr{X}$ of potentially semi-stable representations; $\mathscr{X}$ is a $p$-adic formal algebraic stack

### Main obstacle

The universal deformation ring $R_{\bar\rho}^{\Sigma, \mathcal{L}}$ exists as a complete local $\mathcal{O}$-algebra but its structure can be very complicated: it need not be a domain, a complete intersection, or even Cohen-Macaulay. The relationship $\dim R = \dim t_{\mathcal{D}}$ holds only when $R$ is a complete intersection. In general, one has $\dim R \leq \dim t_{\mathcal{D}}$, with equality iff there are no obstructions. The Selmer group $\mathrm{Sel}(F, \mathrm{ad}\,\bar\rho(1))$ is controlled by $R$ only through the congruence ideal, not directly.

### BSD connection

This direction provides the abstract framework connecting Galois cohomology to Selmer groups. The Selmer group $\mathrm{Sel}(F, V_\ell(E))$ (for $V_\ell(E) = T_\ell(E) \otimes \mathbb{Q}_\ell$) decomposes as:

$$\mathrm{Sel}(F, V_\ell(E)) \hookrightarrow H^1_f(G_{F,\Sigma}, V_\ell(E))$$

where $H^1_f$ is cut out by local conditions at each prime. The deformation-theoretic framework identifies $H^1_f$ with the tangent space of a deformation functor, and the dual Selmer group $H^1_{f^\perp}(G_{F,\Sigma}, V_\ell(E)^*(1))$ with the obstruction space. BSD predicts $\dim \mathrm{Sel} = \mathrm{ord}_{s=1} L(E, s)$, which is equivalent to saying the deformation ring has the "expected" dimension.

### Status

Largely settled in the abstract (Mazur, Böckle, Kisin). Active research on explicit computations and applications to specific arithmetic problems.

### Classification

Foundational — the theoretical backbone of the deformation-theoretic approach.

---

## G-009. The Breuil-Mézard Conjecture and Local-Global Compatibility

### Statement

Prove the Breuil-Mézard conjecture for $\mathrm{GL}_n$ over unramified extensions of $\mathbb{Q}_p$: the Hilbert-Samuel multiplicity $e(R_v^{\square, \mathbf{v}} / \varpi)$ of the framed local deformation ring modulo a uniformizer equals a linear combination of the multiplicities of the special fibers of local Shtukas (or equivalently, the representations in the mod-$\ell$ local Langlands correspondence):

$$e(R_v^{\square, \mathbf{v}} / \varpi) = \sum_{\sigma \in \mathrm{Irr}(\mathrm{GL}_n(k_v))} n_\sigma(\bar\rho|_{G_{F_v}}, \mathbf{v}) \cdot e_\sigma$$

where $e_\sigma$ is the multiplicity of $\sigma$ in the mod-$\ell$ Lusztig datum and $n_\sigma$ is an explicit combinatorial coefficient.

### Tools needed

- Breuil-Mézard (2003): original conjecture for $\mathrm{GL}_2(\mathbb{Q}_p)$
- Kisin's theory of $(\varphi, \hat{G})$-modules
- The mod-$\ell$ local Langlands correspondence (Vignéras, Breuil)
- Potemine's computations of special fibers of local Shtukas
- Emerton-Gee (2022): the stack $\mathscr{X}$ of mod-$p$ representations of $G_{F_v}$
- Geometry of the Emerton-Gee stack: irreducible components, their multiplicities

### What's known

- Breuil-Mézard (2003): conjecture for $\mathrm{GL}_2(\mathbb{Q}_p)$, proved in many cases
- Kisin (2010): proved the conjecture for $\mathrm{GL}_2(\mathbb{Q}_p)$ with crystalline Hodge-Tate weights $(0,1)$
- Helm (2014): geometric Breuil-Mézard for $\mathrm{GL}_2$ over unramified extensions
- Le-Le Hung-Levin-Morra (2020): computational verification for $\mathrm{GL}_2$ and $\mathrm{GL}_3$ over $\mathbb{Q}_p$
- Emerton-Gee (2022): the moduli stack framework proves a "global" version: the irreducible components of the moduli stack of Galois representations are governed by the Breuil-Mézard pattern
- Wang-Erickson (2023): further results on the relationship between deformation rings and the Emerton-Gee stack

### Main obstacle

For $\mathrm{GL}_n$ with $n \geq 3$, the combinatorics of the mod-$\ell$ local Langlands correspondence are not fully understood, and the special fibers of the local Shtuka spaces (Harris-Taylor, Scholze) are difficult to compute explicitly. The Breuil-Mézard multiplicities involve the representation theory of $\mathrm{GL}_n(\mathbb{F}_p)$, which has a complex structure (Lusztig classification involves unipotent classes, Weyl groups, etc.). The connection to deformation rings requires understanding the geometry of $R_v^{\square}$ beyond its reduced structure.

### BSD connection

Local-global compatibility links the local deformation ring geometry to the global Selmer group. The Breuil-Mézard conjecture predicts exactly which crystalline lifts exist and with what multiplicities; this data enters the Taylor-Wiles patching as the local factor $R_v^{\square}$. The Selmer condition at $v = \ell$ is precisely the "ordinary" or "crystalline" locus in $R_v^{\square}$, and the Breuil-Mézard formula computes its degree. The Bloch-Kato conjecture (a consequence of BSD for the $p$-adic realization) predicts that $\dim H^1_f(G_{F_v}, V_p(E)) = $ the order of vanishing of the local L-factor, which is encoded in the Breuil-Mézard data.

### Status

Active research. Known for $\mathrm{GL}_2(\mathbb{Q}_p)$ (Kisin, 2010). Partial results for $\mathrm{GL}_2$ over unramified extensions (Helm, 2014). The Emerton-Gee stack provides a conceptual framework but explicit computations for $n \geq 3$ are ongoing.

### Classification

Local analysis — connects local geometry to global arithmetic.

---

## G-010. Potential Automorphy and Its Consequences for BSD

### Statement

Prove that for every elliptic curve $E/F$ over a CM field $F$, there exists a solvable CM extension $F'/F$ such that $\rho_{E,\ell}|_{G_{F'}}$ is automorphic of the appropriate weight and level. Extend this to show:

1. **Potential modularity**: $\rho_{E,\ell}$ becomes automorphic over $F'$
2. **L-value nonvanishing**: If $\mathrm{ord}_{s=1} L(E/F', s) = 0$, then $\mathrm{ord}_{s=1} L(E/F, s) = 0$
3. **Rank preservation**: $\mathrm{rk}(E/F') = \mathrm{rk}(E/F)$ under the base change

and derive implications for BSD over $F$.

### Tools needed

- Taylor's potential automorphy method (2008): use the Sato-Tate distribution of Hecke eigenvalues
- The Tchebotarev density theorem applied to the image of $\bar\rho_{E,\ell}$
- Solvable base change (Arthur-Clozel): automorphic induction along solvable extensions
- CM lifts: the CM type of $F$ provides a way to make $\bar\rho_{E,\ell}$ conjugate-self-dual
- Lafforgue's automorphy for $\mathrm{GL}_n$ over function fields (by analogy)
- The Calegari-Geraghty method (2016) for potential automorphy over CM fields

### What's known

- Taylor (2008): potential modularity for $\mathrm{GL}_2$ over totally real fields
- Thorne (2015): potential modularity for $\mathrm{GL}_n$ over CM fields
- Allen et al. (2018): automorphy lifting over CM fields for $\mathrm{GL}_n$
- Barnet-Lamb-Gee-Geraghty-Taylor (2011): potential automorphy of all symmetric powers of $\mathrm{GL}_2$ over CM fields
- Newton-Thorne (2020): symmetric power functoriality via potential automorphy
- Kisin (2010): potential modularity of elliptic curves over totally real fields (implied R=T for $\mathrm{GL}_2$)

### Main obstacle

Potential automorphy gives automorphy over $F'$, not over $F$ itself. To descend back to $F$, one needs the base change lifting: if $\pi'$ is automorphic on $\mathrm{GL}_n(\mathbb{A}_{F'})$ and descends to $\mathrm{GL}_n(\mathbb{A}_F)$, then $\pi$ is automorphic. This requires understanding the "norm" map in the automorphic world, which is controlled by Arthur's trace formula. For $\mathrm{GL}_2$, the solvable base change theorem (Langlands, Arthur-Clozel) suffices, but for $n \geq 3$, the descent is more delicate and requires the endoscopic classification.

### BSD connection

Potential automorphy provides the analytic continuation and functional equation of $L(E/F', s) = L(E/F, s) \cdot L(E/F, s \otimes \chi)$ for a character $\chi$ of $\mathrm{Gal}(F'/F)$. The factorization implies:

- If $L(E/F, 1) \neq 0$, then $L(E/F', 1) \neq 0$, so $\mathrm{Sha}(E/F')$ is finite (by Kolyvagin)
- The descent: $\mathrm{Sha}(E/F)[\ell^\infty] \hookrightarrow \mathrm{Sha}(E/F')[\ell^\infty]^{\mathrm{Gal}(F'/F)}$, so finiteness of $\mathrm{Sha}(E/F')$ implies finiteness of $\mathrm{Sha}(E/F)$

This gives a conditional approach to BSD: prove potential automorphy + descent, then apply Kolyvagin.

### Status

Active research. Potential automorphy for $\mathrm{GL}_2$ is well-established (Taylor, Thorne). The descent step is the main bottleneck: known for $n=2$ via Arthur-Clozel, open in general for $n \geq 3$.

### Classification

Applications — connects potential automorphy to explicit BSD consequences.

---

## G-011. p-adic Langlands Program and Elliptic Curves

### Statement

Develop the $p$-adic Langlands correspondence for $\mathrm{GL}_2(\mathbb{Q}_p)$ and its applications to the arithmetic of elliptic curves. Specifically:

1. **Completed cohomology**: Show that the completed cohomology $\widetilde{H}^1(Y_0(N), \mathcal{O})_{\mathfrak{m}}$ carries an action of $\mathrm{GL}_2(\mathbb{Q}_p)$ that realizes the $p$-adic Langlands correspondence
2. **Eigenvarieties**: Construct the eigenvariety $\mathscr{E}$ parameterizing $p$-adic families of automorphic forms and study its geometry near the Eisenstein locus
3. **Control of Selmer groups**: Use the eigenvariety to prove vanishing of $\mu$-invariants and bounds on $\lambda$-invariants of Selmer groups

### Tools needed

- Colmez's $p$-adic Langlands correspondence (2010): bijection between $2$-dimensional $p$-adic representations of $G_{\mathbb{Q}_p}$ and unitary Banach space representations of $\mathrm{GL}_2(\mathbb{Q}_p)$
- Emerton's completed cohomology: $\widetilde{H}^i = \varprojlim_{K} H^i(Y_K, \mathcal{O}/p^n\mathcal{O})$
- Buzzard's eigenvariety construction (2004): spectral varieties and overconvergent modular forms
- Pilloni-Stroh (2013): higher Hida theory and coherent cohomology
- Andreatta-Iovita-Pilloni (2015): overconvergent modular forms on Shimura varieties
- Bellaïche (2012): the eigenvariety at the boundary of the weight space

### What's known

- Colmez (2010): the $p$-adic Langlands correspondence for $\mathrm{GL}_2(\mathbb{Q}_p)$
- Emerton (2006): completed cohomology realizes the $p$-adic Langlands correspondence; the Jacquet module of $\widetilde{H}^1$ recovers the local Galois representation
- Breuil-Emerton (2011): showed the local-global compatibility for the $p$-adic Langlands correspondence
- Chenevier (2011): the eigenvariety is a rigid analytic space of dimension $[F:\mathbb{Q}]$; its irreducible components are controlled by the weight map
- Hansen (2017): universal eigenvariety and its local models
- Ding (2019): $p$-adic families of modular forms and Selmer groups

### Main obstacle

The $p$-adic Langlands correspondence is known only for $\mathrm{GL}_2(\mathbb{Q}_p)$ and some extensions (Breuil, 2010; Ardakov, 2014). For $\mathrm{GL}_n$ with $n \geq 3$, there is no satisfactory $p$-adic Langlands correspondence; the representations involved are not locally analytic and the expected Banach space representations are difficult to construct. Even for $\mathrm{GL}_2$, the extension to $\mathrm{GL}_2(F)$ for $F \neq \mathbb{Q}_p$ is incomplete (partial results by Breuil-Herzig, Le-Morra-Schraen).

### BSD connection

The $p$-adic Langlands program provides the most refined control of $p$-adic Selmer groups. The eigenvariety $\mathscr{E}$ parameterizes $p$-adic families $\{f_k\}$ of modular forms through the Eisenstein point, and the $p$-adic L-function $L_p(f_k, s)$ interpolates the classical L-values $L(f_k, 1)$. The vanishing of the $\mu$-invariant of $L_p$ (Hida's theorem for ordinary families, Emerton for overconvergent families) implies the vanishing of $\mu(\mathrm{Sel}_{p^\infty}(E/\mathbb{Q}))$, which is a necessary condition for the $p$-part of BSD. The $\lambda$-invariant of the Selmer group is then related to the degree of the $p$-adic L-function by the $p$-adic Birch and Swinnerton-Dyer conjecture (Mazur-Tate-Teitelbaum).

### Status

Active research. The $\mathrm{GL}_2(\mathbb{Q}_p)$ correspondence is complete (Colmez, 2010). The eigenvariety framework is well-developed (Buzzard, Chenevier, Hansen). Extension to $\mathrm{GL}_n$ for $n \geq 3$ is a major open problem. Applications to Selmer group control are ongoing (Ding, Hansen, Wake).

### Classification

p-adic methods — provides the most refined arithmetic information via $p$-adic families.

---

# Directions: Group H — Computational Approaches

---

## H-001: Certified Numerical Verification of BSD for Specific Curves

**ID:** H-001
**Title:** Certified Numerical Verification of BSD for Specific Curves

**Statement:** For a given elliptic curve $E/\mathbb{Q}$, compute every quantity in the BSD formula — $L^{(r)}(E,1)$, $\Omega_\infty(E)$, $\prod_p c_p$, $|\text{Ш}(E/\mathbb{Q})|$, $R(E)$, $|E(\mathbb{Q})_{\text{tors}}|^2$ — to sufficient precision to either confirm or refute the BSD prediction $\frac{L^{(r)}(E,1)}{r!} = \frac{\Omega \cdot \text{Reg} \cdot \prod c_p \cdot |\text{Ш}|}{|E(\mathbb{Q})_{\text{tors}}|^2}$ as an exact equality of rational numbers (after accounting for the known power of 2).

**Tools needed:**
- SageMath (`EllipticCurve`, `Lseries`, `ellL1`, `padic_L_function`)
- Magma (`AnalyticRank`, `Sha`, `BSD`, `Periods`)
- PARI/GP (`ellanalyticrank`, `ellperiods`, `ellL1`)
- Arbitrary-precision arithmetic libraries (MPFR, Arb)
- Interval arithmetic for rigorous error bounds (Arb via SageMath's `RealBallField`)

**What's known:**
- BSD is proven for all curves of analytic rank 0 or 1 (Gross–Zagier, Kolyvagin, Skinner–Urban).
- Cremona's database verifies BSD for all curves of conductor $\leq 500{,}000$ (rank 0 and 1 cases).
- For rank $\geq 2$, verification is known only for individual curves; no systematic sweep exists above conductor $10^6$.
- Wuthrich (2005) and collaborators verified BSD for select rank 2 curves using $p$-adic methods.
- The Birch–Swinnerton-Dyer conjecture has been verified numerically for over $10^9$ curves of small conductor via LMFDB data.

**Main obstacle:** For curves of rank $r \geq 2$, the analytic rank must be established by showing $L^{(k)}(E,1) = 0$ for $k < r$ and $L^{(r)}(E,1) \neq 0$. Proving non-vanishing to certified precision is computationally expensive: the L-function series converges slowly, and analytic continuation via the functional equation introduces amplification of rounding errors. The regulator computation requires computing canonical heights of generators to high precision, which is its own bottleneck.

**BSD connection:** This is the most direct computational test of BSD: either the formula holds or it does not. Certifying it for specific high-rank or high-conductor curves extends the evidentiary base and may reveal arithmetic phenomena (e.g., unexpected Ш structure) that guide theoretical work.

**Status:** In Progress

**Classification:** Verification

---

## H-002: LMFDB Systematic Analysis: Rank vs. Analytic Rank

**ID:** H-002
**Title:** LMFDB Systematic Analysis: Rank vs. Analytic Rank

**Statement:** Systematically compare algebraic rank and analytic rank across the entire LMFDB elliptic curve database (currently ~3 million curves over $\mathbb{Q}$, conductor up to $\sim 10^7$), producing a census of matches, mismatches, and curves where one or both quantities are undetermined. Identify any violations of the weak BSD conjecture ($\text{rank} = \text{analytic rank}$).

**Tools needed:**
- LMFDB API and local database mirror (`https://www.lmfdb.org/EllipticCurve/Q/`)
- LMFDB download scripts (`https://beta.lmfdb.org/api/`)
- Python (pandas, numpy, sqlite3) for bulk data analysis
- SageMath for on-demand verification of flagged curves
- PostgreSQL or DuckDB for local query over full dataset

**What's known:**
- LMFDB stores analytic rank (computed via Dokchitser's method) and, for conductor $\leq 500{,}000$, algebraic rank from Cremona's tables.
- For all curves where both are known, they agree — zero violations of weak BSD.
- The gap: for conductor $> 500{,}000$, many curves in LMFDB have analytic rank computed but algebraic rank only estimated (via 2-descent or 2-descent + heuristics), not always proven.
- Stein–Watkins (2002) computed ranks for all curves of conductor $\leq 10^8$ using heuristic methods; a certified re-do is missing.

**Main obstacle:** The database is large but heterogeneous: different contributors used different precision levels, and some analytic rank computations are heuristic (based on sign of functional equation + approximate vanishing). A systematic sweep must re-derive analytic ranks with certified precision and flag curves where algebraic rank requires further descent computation.

**BSD connection:** Weak BSD ($r_{\text{an}} = r$) is the foundational assertion. Finding even one curve where $r_{\text{an}} \neq r$ would disprove BSD. Confirming agreement across the full database strengthens the conjecture and quantifies the "agreement rate" as a function of conductor.

**Status:** In Progress

**Classification:** Verification / Data Analysis

---

## H-003: SageMath Pipeline for L-function Computation

**ID:** H-003
**Title:** SageMath Pipeline for L-function Computation

**Statement:** Build and document a reproducible SageMath pipeline that takes an elliptic curve $E/\mathbb{Q}$ (by conductor and isogeny class, or by Cremona label, or by Weierstrass coefficients) and outputs:
1. $L(E,s)$ evaluated at $s = 1$ to arbitrary certified precision (using `Lseries_ell` or Dokchitser's `Lfunctions` framework).
2. The analytic rank $r_{\text{an}}$ with proof (via vanishing order certificate).
3. The leading coefficient $L^{(r)}(E,1)/r!$ with rigorous error bounds.
4. All auxiliary BSD quantities: $\Omega$, $c_p$, $\text{Reg}$, $|\text{Ш}_{p^\infty}|$ for specified primes $p$, torsion subgroup.

**Tools needed:**
- SageMath ≥ 10.0 (core: `sage.schemes.elliptic_curves`)
- Dokchitser's `Lfunctions` module (bundled in SageMath)
- SageMath `RealBallField` / `ComplexBallField` (Arb backend) for certified numerics
- `pari` interface within SageMath (`gp.ellanalyticrank`)
- Docker/Singularity container for reproducibility

**What's known:**
- SageMath has `E.lseries().at1()` which uses Dokchitser-type algorithms, but it does not always return rigorous error bounds.
- The `dokchitser` module (`sage.lfunctions.dokchitser`) wraps Tim Dokchitser's `Lfunctions` C library and supports arbitrary precision, but the interface is fragile for high analytic rank.
- PARI/GP's `ellL1(E, {D=0}, {flag=0})` computes $L^{(r)}(E,1)/r!$ with proven error bounds via `D` decimal digits.
- Magma's `AnalyticRank` uses a provably correct algorithm for $r_{\text{an}} \leq 1$ (sign of functional equation suffices) but is heuristic for $r_{\text{an}} \geq 2$.
- No single pipeline integrates all of these into a certified, one-command workflow.

**Main obstacle:** Combining multiple backends (SageMath, PARI, Magma) into a single certified pipeline is an engineering challenge. The Dokchitser algorithm requires tuning the number of series terms and working precision based on the conductor and desired output precision. For curves with conductor $N > 10^8$, the current implementations are slow or fail due to precision loss in the Gamma-factor correction.

**BSD connection:** The L-function evaluation is the analytic side of the BSD formula. A reliable, high-precision pipeline is the prerequisite for every other computational direction in this group.

**Status:** In Progress

**Classification:** Infrastructure

---

## H-004: Monster Curves: Verification for Rank ≥ 25 (Elkies–Klagsbrun)

**ID:** H-004
**Title:** Monster Curves: Verification for Rank ≥ 25

**Statement:** Verify the BSD formula for the Elkies–Klagsbrun curves of rank $\geq 25$ (currently the highest known rank for an elliptic curve over $\mathbb{Q}$ is 29, discovered by Elkies–Klagsbrun in 2024–2025). This requires: (a) computing $L^{(r)}(E,1)/r!$ to sufficient precision, (b) computing the regulator $\text{Reg}(E)$ from $r$ independent generators, (c) computing the real period $\Omega$, (d) computing Tamagawa numbers, (e) computing $|\text{Ш}|$ (or bounding it).

**Tools needed:**
- Magma (primary tool for the Elkies–Klagsbrun curves, which were constructed in Magma)
- SageMath for cross-verification
- Dokchitser L-function evaluation at high precision ($\geq 50$ digits)
- Height pairing matrix computation with certified precision (Arb)
- $p$-adic methods for Ш: `mwrank`, `TwoDescent`, `pSelmerGroup`

**What's known:**
- Elkies (2006) found a rank 28 curve; Elkies–Klagsbrun (2024) found rank 29.
- These curves have enormous conductor (e.g., the rank 29 curve has conductor $\sim 10^{30}$), making direct L-function evaluation extremely expensive.
- The generators are known explicitly (Weierstrass coefficients and points), but computing the canonical height pairing matrix to 30+ digits of precision for a $29 \times 29$ matrix is a non-trivial computational task.
- BSD has never been verified for any curve of rank $\geq 10$ (the highest verified rank is believed to be around 7–8 for individual curves).

**Main obstacle:** The conductor is astronomically large ($\sim 10^{29}$ for the rank 29 curve), so the standard L-function series $\sum a_n n^{-s} e^{-2\pi n/(N^{1/2} t)}$ converges extremely slowly. The regulator is the determinant of a $29 \times 29$ matrix of canonical heights; each entry must be computed to $\geq 30$ digits, and the determinant itself may be very small (the height pairing is positive definite but condition number grows with rank).

**BSD connection:** Verifying BSD for the highest-rank curves is the most demanding computational test possible. It probes whether BSD holds in an extreme arithmetic regime and tests the limits of numerical verification methods.

**Status:** In Progress

**Classification:** Verification / Frontier

---

## H-005: Computational Bounds on |Ш| for Large Conductor

**ID:** H-005
**Title:** Computational Bounds on |Ш(E/Q)| for Large Conductor

**Statement:** For elliptic curves $E/\mathbb{Q}$ with conductor $N$ in the range $10^6 \leq N \leq 10^{12}$, compute upper bounds on $|\text{Ш}(E/\mathbb{Q})|$ using the Cassels–Tate pairing, $p$-descent, and the BSD formula itself (as an equality, assuming rank is known). Systematize the computation to cover all isogeny classes in the LMFDB range and beyond.

**Tools needed:**
- SageMath: `E.sha()` (heuristic), `E.pSelmerGroup(p)`, `E.two_descent()`
- Magma: `Sha(E, p)` for $p$-descent, `BSD(E)` for full verification
- PARI/GP: `ellpadicselmer`, `ellglobaldescent`
- Dokchitser–Dokchitser parity conjecture algorithms (`Magma: ParityConjecture`)
- Distributed computing framework (HPC or cloud) for sweeps over $10^6+$ curves

**What's known:**
- $|\text{Ш}|$ is conjectured to be finite (a consequence of BSD).
- The Cassels–Tate pairing implies $|\text{Ш}|$ is a perfect square (Cassels).
- For conductor $\leq 500{,}000$, $|\text{Ш}|$ is computed in Cremona's tables; the largest values are around $|\text{Ш}| \sim 10^4$.
- Kolyvagin's theorem gives $|\text{Ш}| = 1$ for rank 0 and 1 curves (analytic rank ≤ 1).
- For rank $\geq 2$, $|\text{Ш}|$ must be computed by descent or by inverting the BSD formula (assuming everything else is known).
- Klüners (2003) and others have found curves with $|\text{Ш}| \geq 10^4$.

**Main obstacle:** $p$-descent for $|\text{Ш}|$ only gives the $p$-part: computing $|\text{Ш}[p^\infty]|$ for a single prime $p$. To get the full $|\text{Ш}|$, one must either (a) do $p$-descent for all primes $p$ dividing $|\text{Ш}|$ (which requires knowing which primes divide it) or (b) use the BSD formula. For large conductor, even 2-descent is expensive; 3-descent and higher are currently infeasible beyond conductor $\sim 10^8$.

**BSD connection:** The order of Ш appears directly in the BSD formula. Bounding $|\text{Ш}|$ is equivalent to bounding the ratio $\frac{L^{(r)}(E,1)/r!}{\Omega \cdot \text{Reg} \cdot \prod c_p / |E_{\text{tors}}|^2}$. If this ratio is computed to enough precision, it must be a perfect square integer — verifying this is a direct test of BSD.

**Status:** In Progress

**Classification:** Verification / Bounds

---

## H-006: Database of Tamagawa Numbers and Their Distribution

**ID:** H-006
**Title:** Database of Tamagawa Numbers and Their Distribution

**Statement:** Build a comprehensive database of Tamagawa numbers $c_p(E)$ for all primes $p \mid N$ (conductor) across the LMFDB elliptic curve collection, and analyze their statistical distribution: frequency of each value, correlation with conductor, rank, and Ш. Formulate conjectures about the distribution of $\prod_p c_p$ as conductor grows.

**Tools needed:**
- LMFDB API (`https://beta.lmfdb.org/api/`) for bulk download
- Local PostgreSQL/DuckDB database for analysis
- SageMath: `E.tamagawa_numbers()`, `E.tamagawa_product()`
- Magma: `TamagawaNumbers(E)`, `LocalData(E)`
- Python (pandas, matplotlib, scipy) for statistical analysis

**What's known:**
- Tamagawa numbers $c_p = [E(\mathbb{Q}_p) : E_0(\mathbb{Q}_p)]$ where $E_0$ is the set of points with nonsingular reduction.
- For primes of multiplicative reduction: $c_p = v_p(\Delta)$ (split) or $c_p \in \{1, 2\}$ (nonsplit, depending on parity of $v_p(\Delta)$).
- For primes of additive reduction: $c_p \in \{1, 2, 3, 4\}$ (with exact values depending on Kodaira type).
- LMFDB stores `tamagawa_data` for each curve.
- The distribution of Tamagawa numbers is related to the local behavior of $E$ at each prime and is well-understood individually, but the distribution of the product $\prod_p c_p$ as conductor varies is less studied.
- The Birch–Swinnerton-Dyer conjecture implies that $\prod_p c_p$ divides $|\text{Ш}| \cdot |E_{\text{tors}}|^2 \cdot L^{(r)}(E,1) / (r! \cdot \Omega \cdot \text{Reg})$.

**Main obstacle:** The database is large (~3 million curves × up to ~10 primes each) and the analysis is primarily statistical rather than algorithmic. The real challenge is formulating meaningful conjectures: what does the distribution of $\prod_p c_p$ look like as a function of conductor, and does it correlate with any BSD quantity in a predictable way?

**BSD connection:** Tamagawa numbers appear as an explicit factor in the BSD formula. Their distribution constrains the possible values of $|\text{Ш}|$. Understanding their statistics may reveal why certain values of $|\text{Ш}|$ are more common and whether there are hidden constraints.

**Status:** In Progress

**Classification:** Data Analysis / Conjecture Formation

---

## H-007: Verified Computation of Regulators for High-Rank Curves

**ID:** H-007
**Title:** Verified Computation of Regulators for High-Rank Curves

**Statement:** Compute the regulator $\text{Reg}(E) = \det(\langle P_i, P_j \rangle)_{1 \leq i,j \leq r}$ (the determinant of the Néron–Tate height pairing matrix on a basis of $E(\mathbb{Q})/E(\mathbb{Q})_{\text{tors}}$) with certified precision for all known elliptic curves of rank $r \geq 10$. Extend the computation to all curves of rank $\geq 5$ in the LMFDB database.

**Tools needed:**
- SageMath: `E.regulator()`, `E.height_pairing_matrix()`, `E.elliptic_exponential()`
- Magma: `Regulator(E)`, `HeightPairingMatrix()`
- Arb (via SageMath's `RealBallField`) for rigorous ball arithmetic
- Silverman's algorithm for canonical height: $\hat{h}(P) = \lim_{n \to \infty} 4^{-n} h(2^n P)$ with explicit convergence bounds
- `mwrank` for generator computation

**What's known:**
- The Néron–Tate canonical height $\hat{h}(P)$ can be computed via Silverman's algorithm or via the decomposition $\hat{h}(P) = h_x(P) + \sum_v \delta_v(P)$ where $h_x(P) = \frac{1}{2} \log \max(|x(P)|, 1)$ and $\delta_v$ are local correction terms (Archimedean and non-Archimedean).
- For rank 1, the regulator is just $\hat{h}(P)$ for a generator $P$, and this is computed routinely.
- For rank $\geq 10$, the height pairing matrix has condition number that can be enormous (the points may be close in the Mordell–Weil lattice), requiring high precision.
- The current record: regulators are computed for curves of rank up to $\sim 15$ (individual cases). No systematic computation exists for all rank $\geq 5$ curves.
- Cremona's `mwrank` computes generators and heights but without certified error bounds.

**Main obstacle:** (1) Precision: the height pairing matrix is positive definite but can be ill-conditioned; computing its determinant to 10+ significant digits requires 30+ digit precision in the entries. (2) The Archimedean local height $\delta_v(P)$ for $v \mid \infty$ involves evaluating the elliptic logarithm and integrating the local Green's function, which is numerically delicate for points with large $x$-coordinate. (3) For high-rank curves, the generators themselves may have enormous coordinates, making even the initial descent step expensive.

**BSD connection:** The regulator is a direct factor in the BSD formula. For curves of rank $\geq 2$, $\text{Reg}(E) > 0$ and its precise value is needed to test the BSD equality. The regulator also encodes the geometry of the Mordell–Weil lattice, which has independent arithmetic interest.

**Status:** In Progress

**Classification:** Computation / Infrastructure

---

## H-008: Computation of Periods Ω(E) with Guaranteed Precision

**ID:** H-008
**Title:** Computation of Periods Ω(E) with Guaranteed Precision

**Statement:** Compute the real period $\Omega_\infty(E) = 2 \int_{E(\mathbb{R})} |\omega|$ (where $\omega = dx/(2y+a_1 x + a_3)$ is the Néron differential) and the periods $\Omega(E)$ appearing in the BSD formula (including the factor for the number of connected components of $E(\mathbb{R})$) with guaranteed precision for all curves in the LMFDB database, extending to conductor up to $10^{12}$.

**Tools needed:**
- SageMath: `E.omega()`, `E.real_period()`, `E.period_lattice()`
- Magma: `RealPeriod(E)`, `Periods(E)`
- PARI/GP: `ellperiods(E, flag)`
- GNU MPFR / Arb for high-precision real integration
- Gauss–Legendre or Gauss–Jacobi quadrature for the Archimedean integral
- Arithmetic-geometric mean (AGM) method for complete elliptic integrals

**What's known:**
- For $E: y^2 = x^3 + Ax + B$ (short Weierstrass), the real period is $\Omega = 2 \int_{e_1}^{\infty} \frac{dx}{\sqrt{x^3 + Ax + B}}$ (one component) or twice that (two components), where $e_1$ is the largest real root.
- This is a complete elliptic integral, computable via the AGM method in $O(M(n) \log n)$ time for $n$-bit precision (where $M(n)$ is the multiplication cost).
- For general Weierstrass form, the integral is slightly more complex but reduces to the same standard forms.
- PARI/GP's `ellperiods` uses the AGM and is fast and accurate.
- For conductor up to $10^8$, periods are computed to 30+ digits in LMFDB.

**Main obstacle:** (1) For curves with bad reduction, the Néron differential is not the standard $dx/(2y + a_1 x + a_3)$ and one must account for the correct model over $\mathbb{Z}$; this is a subtlety in the computation. (2) The BSD period $\Omega$ includes a factor of $\prod_{p \mid N} m_p$ where $m_p$ is the number of components of the Néron model at $p$; computing $m_p$ requires the Kodaira type at each bad prime. (3) For very large conductor ($N > 10^{12}$), the AGM method is still fast, but the initial reduction to standard form may lose precision if the curve coefficients are enormous.

**BSD connection:** The real period $\Omega$ is a fundamental ingredient in the BSD formula. The conjecture predicts $L^{(r)}(E,1)/r! = \Omega \cdot \text{Reg} \cdot \prod c_p \cdot |\text{Ш}| / |E_{\text{tors}}|^2$, so $\Omega$ must be known to the same precision as the other factors. Any error in $\Omega$ propagates directly into the verification.

**Status:** In Progress

**Classification:** Computation / Infrastructure

---

## H-009: Systematic Verification of the Strong BSD Formula

**ID:** H-009
**Title:** Systematic Verification of the Strong BSD Formula

**Statement:** For all elliptic curves $E/\mathbb{Q}$ of conductor $N \leq 10^6$ where the rank is known (either proven or conjectured), verify the full strong BSD formula:

$$\frac{L^{(r)}(E,1)}{r!} = \frac{\Omega(E) \cdot \text{Reg}(E) \cdot \prod_p c_p \cdot |\text{Ш}(E/\mathbb{Q})|}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

as an exact equality of rational numbers (the left side, after dividing by $\Omega$, must be a rational number whose numerator and denominator match the right side). Catalog all discrepancies and investigate their causes.

**Tools needed:**
- SageMath: full BSD computation via `E.bsd_data()` (where available)
- Magma: `BSD(E)` for individual curves, `AnalyticRank`, `Sha`, `Regulator`
- Cremona's database: `allcurves` package, conductor $\leq 500{,}000$
- LMFDB API for extending to $N \leq 10^6$
- High-precision arithmetic (50+ digits for the L-value)
- Automated discrepancy reporting and classification pipeline

**What's known:**
- For conductor $\leq 500{,}000$, Cremona verified the weak BSD conjecture ($r = r_{\text{an}}$) and the strong BSD formula for rank 0 and 1 curves (where Kolyvagin's theorem applies).
- For rank $\geq 2$, the strong BSD formula is verified for individual curves by Wuthrich, Fisher, and others, but no systematic sweep exists.
- The strong BSD formula involves $|\text{Ш}|$, which is only computable by descent (giving the $p$-part for individual primes $p$) or by inverting the formula (which assumes BSD).
- The Cassels–Tate pairing provides an independent check: $|\text{Ш}|$ must be a perfect square.

**Main obstacle:** For rank $\geq 2$ curves, computing $|\text{Ш}|$ independently (without assuming BSD) is the bottleneck. $p$-descent for $p = 2$ is feasible for most curves of conductor $\leq 10^6$, but higher primes are expensive. The alternative — inverting the formula and checking that the result is a perfect square integer — is a consistency check, not an independent verification.

**BSD connection:** This is the comprehensive test of the strong BSD conjecture. Verifying it across a large database strengthens the case for BSD and may reveal patterns (e.g., which curves have the largest $|\text{Ш}|$, or which have regulators that are unexpectedly small) that inform theoretical work.

**Status:** In Progress

**Classification:** Verification

---

## H-010: Machine Learning on LMFDB Data for BSD Patterns

**ID:** H-010
**Title:** Machine Learning on LMFDB Data for BSD Patterns

**Statement:** Apply modern machine learning techniques (gradient-boosted trees, neural networks, symbolic regression) to the LMFDB elliptic curve database to discover previously unnoticed patterns, correlations, or predictive features related to BSD quantities. Specific targets:
1. Predict $|\text{Ш}|$ from conductor, rank, Tamagawa numbers, and torsion structure.
2. Identify curves where $|\text{Ш}| > 1$ and classify them by arithmetic invariants.
3. Discover symbolic formulas relating $\text{Reg}(E)$ to other curve invariants.
4. Detect anomalies that might indicate computational errors in the database.

**Tools needed:**
- LMFDB bulk data download (CSV/JSON, ~3M curves): `https://beta.lmfdb.org/api/`
- Python: scikit-learn, XGBoost/LightGBM, PyTorch/TensorFlow
- PySR (Cranmer, 2023) for symbolic regression
- SageMath for feature engineering (conductor factorization, Kodaira types, etc.)
- Jupyter notebooks for reproducible analysis
- GPU access for neural network training (if needed)

**What's known:**
- LMFDB stores: conductor, rank (algebraic and analytic), Tamagawa numbers, torsion order, regulator, $\Omega$, $a_p$ for $p \leq 100$, minimal Weierstrass equation, isogeny class.
- The distribution of analytic rank is biased: rank 0 and 1 are most common ($\sim 85\%$ and $\sim 14\%$); rank 2 is $\sim 1\%$; rank $\geq 3$ is extremely rare.
- $|\text{Ш}|$ is 1 for most curves; the frequency of $|\text{Ш}| > 1$ decreases with conductor.
- No non-trivial symbolic relationships between BSD quantities beyond the BSD formula itself are known.
- Adam, et al. (2021) and He–Lee–Oliver (2020) have applied ML to number theory problems with some success, but not specifically to BSD patterns.

**Main obstacle:** The data is heavily skewed (most curves have rank 0 or 1, $|\text{Ш}| = 1$). Standard ML may simply learn the base rates. Symbolic regression may rediscover the BSD formula or known inequalities, but finding genuinely new patterns requires careful feature engineering and domain expertise to distinguish signal from noise.

**BSD connection:** If ML discovers a reliable predictor of $|\text{Ш}|$ or identifies a new arithmetic invariant correlated with BSD quantities, this could guide theoretical investigation. Even negative results (e.g., "no simple formula predicts $|\text{Ш}|$ beyond the BSD formula") are informative.

**Status:** In Progress

**Classification:** Data Science / Conjecture Formation

---

## H-011: Distributed Computation of L-function Zeros

**ID:** H-011
**Title:** Distributed Computation of L-function Zeros

**Statement:** Compute the first $T$ zeros (by height) of the L-function $L(E,s)$ for all elliptic curves $E/\mathbb{Q}$ of conductor $N \leq 10^6$, using distributed computation across a cluster. Verify that all zeros lie on the critical line $\text{Re}(s) = 1/2$ (confirming the Generalized Riemann Hypothesis for these L-functions) and compute the zero statistics (pair correlation, nearest-neighbor spacing) to compare with random matrix theory predictions (GUE).

**Tools needed:**
- Dokchitser's `Lfunctions` library (C) or its SageMath wrapper
- Odlyzko–Schönhage algorithm for computing zeros of L-functions
- Rubinstein's `lcalc` library (bundled in SageMath)
- MPI or Dask for distributed computation
- HPC cluster ($\geq 1000$ cores) or cloud computing (AWS/GCP spot instances)
- SQLite or Parquet files for storing zero data
- Python (numpy, scipy, matplotlib) for statistical analysis

**What's known:**
- GRH for elliptic curve L-functions is verified numerically for all curves of conductor $\leq 10^5$ (approximately) and for the first $\sim 10^6$ zeros.
- The Odlyzko–Schönhage algorithm computes $N(T)$ (the number of zeros with $0 < \text{Im}(s) < T$) and individual zeros in $O(T \log T)$ time (conjecturally).
- $lcalc$ implements this efficiently and is the standard tool.
- Random matrix theory (Katz–Sarnak) predicts that the zeros of $L(E,s)$ for curves in a one-parameter family follow GUE statistics. This has been verified for small conductor ranges.
- The lowest zero $\gamma_1$ is of particular interest: the Katz–Sarnak philosophy predicts $\gamma_1 \sim 1/\log N$ for families with orthogonal symmetry.

**Main obstacle:** (1) Computational cost: for conductor $N$, computing the first zero requires $\sim \sqrt{N}$ terms of the L-function series; for $N = 10^6$, this is $\sim 10^3$ terms per zero, and one needs hundreds of zeros per curve. With $\sim 10^6$ curves in the range, the total is $\sim 10^{11}$ evaluations. (2) Storage: the zero data for each curve is a list of floats; for $10^6$ zeros per curve and $10^6$ curves, this is $\sim 10^{12}$ floats ($\sim 4$ TB). (3) Verification: confirming that the computed zeros are genuine (not spurious) requires independent verification, ideally via the argument principle.

**BSD connection:** While GRH is not part of BSD, the distribution of zeros of $L(E,s)$ controls the analytic behavior of $L(E,1)$: the rate of convergence of the L-function series, the size of $L(E,1)$ for rank 0 curves, and the leading coefficient for rank $\geq 1$ curves. Understanding the zero distribution is essential infrastructure for precise BSD computations. Moreover, GRH for $L(E,s)$ implies that the sign of the functional equation determines the parity of the analytic rank, which is a key input for computational verification.

**Status:** In Progress

**Classification:** Computation / Verification

---

# Research Directions: Group I — Connections to Other Conjectures

Ten precise mathematical research directions exploring the connections between BSD and other major conjectures.

---

## I-001. Colmez Conjecture on Average Norms of CM Points and BSD

### Statement

Let $E$ be an elliptic curve over $\mathbb{Q}$ with complex multiplication by the ring of integers $\mathcal{O}_K$ of an imaginary quadratic field $K$. For a CM point $P \in E(\overline{\mathbb{Q}})$ of conductor $\mathfrak{f}$, let $h_{\mathrm{Fal}}(P)$ denote its Faltings height. Colmez's conjecture (1993) states that there exists a rational number $c_E$ such that for any integer $N \geq 1$,

$$\frac{1}{[K_N : K]} \sum_{\substack{P \in E(K_N) \\ \text{conductor } N}} h_{\mathrm{Fal}}(P) = -\frac{1}{2} \frac{L'(E/K, 0)}{L(E/K, 0)} + c_E \cdot \log N + O(1),$$

where $K_N$ is the ray class field of conductor $N$ over $K$.

The connection to BSD arises because $\operatorname{ord}_{s=0} L(E/K, s) = \operatorname{rank} E(K)$ and $L'(E/K, 0)$ encodes the regulator when the rank is 1. When $E$ has CM by $K$, the $L$-function factorizes as $L(E/K, s) = L(\chi_K, s) \cdot L(E/\mathbb{Q}, s)$, and the analytic rank of $L(E/\mathbb{Q}, s)$ governs the leading term.

### Tools needed

- Faltings heights and Arakelov theory on Shimura curves
- Theta functions on CM abelian varieties (Gross-Zagier type formulas for CM points)
- Cherednik's theory of CM points on Shimura curves and Heegner point constructions
- Equidistribution theorems for CM points (Duke's theorem, Bilu's theorem)
- The Colmez-Yang average formula relating CM values to $L'(E/K, 0)$

### What's known

- **Colmez (1993):** Conjectured the formula; proved a weaker upper bound.
- **Yuan-Zhang (2014):** Proved the averaged version of the Colmez conjecture: the sum over all CM abelian varieties of a given degree weighted by the inverse of the automorphism group equals the predicted value. This is the "Colmez conjecture on average."
- **Gross-Zagier (1986):** For rank 1, the height of Heegner points equals $L'(E/K, 1)$ (up to explicit factors), providing a direct link.
- **Houfek (2019), Kezuka (2020):** Computational verifications for families of CM curves with specific conductors.
- The averaged Colmez conjecture is now known; the non-averaged (individual CM point) version remains open for most cases.

### Main obstacle

- The non-averaged Colmez conjecture requires individual control of the Faltings height of each CM point, not just the average. Current equidistribution methods (Duke, Bilu) give asymptotic information but not exact pointwise formulas.
- Bridging the gap between the averaged result (which involves the Dedekind zeta function of $K$) and the individual curve $L$-function $L(E/\mathbb{Q}, s)$ requires understanding how CM points distribute across individual isogeny classes.

### BSD connection

- **Direct link:** When $E/\mathbb{Q}$ has CM by $K$ and $\operatorname{ord}_{s=1} L(E/\mathbb{Q}, s) = 1$, the Gross-Zagier formula identifies $L'(E/\mathbb{Q}, 1)$ with the Néron-Tate height of a Heegner point. The Colmez conjecture then predicts the Faltings height of this same point, so the two formulas together constrain the relation between Faltings height and Néron-Tate height.
- **Indirect link:** The Colmez conjecture on average implies that the "expected" height of CM points matches the logarithmic derivative of the $L$-function. This is a shadow of BSD in the CM setting: the analytic rank governs the arithmetic height.
- **Implication:** If the individual Colmez conjecture were proven for all CM elliptic curves, it would give an independent proof of the $r=1$ case of BSD for CM curves (via Gross-Zagier), and would constrain the Birch-Swinnerton-Dyer regulator in terms of Faltings heights.

### Status

**Active research.** Average Colmez proven (Yuan-Zhang); individual Colmez known in specific cases. The connection to BSD is structural and bidirectional.

### Classification

**Inter-domain bridge.** Connects Arakelov geometry (heights) to analytic number theory ($L$-functions) through the lens of BSD.

---

## I-002. Vojta's Conjecture and Effective Finiteness for Elliptic Curves

### Statement

Let $X$ be a smooth projective variety over a number field $k$, and let $D$ be an effective Cartier divisor on $X$ with at worst normal crossings. Fix a Weil height $h_X$ and the logarithmic discriminant $d_k$. Vojta's conjecture (1987) asserts: for every $\epsilon > 0$, there exists a proper Zariski-closed subset $Z \subset X$ such that for all $x \in X(k) \setminus Z$,

$$h_{K_X}(x) + m \cdot d_k \leq d_{\mathrm{log}}(D, x) + \epsilon \cdot h_A(x) + O(1),$$

where $d_{\mathrm{log}}(D, x) = -\log \mathrm{dist}(x, D)$ is the proximity function, $h_{K_X}$ is the height with respect to the canonical divisor, and $m$ is the order of vanishing.

For an elliptic curve $E/\mathbb{Q}$ viewed inside $\mathbb{P}^2$, taking $D$ to be the line at infinity, Vojta's conjecture predicts that for points of infinite order $P \in E(\mathbb{Q})$ outside a finite set, the height $h(P)$ is controlled by the proximity function $d_{\mathrm{log}}(\infty, P)$ — which is essentially $-\log |y(P)|$ — with explicit dependence on the discriminant of the field of definition.

### Tools needed

- Diophantine approximation: Schmidt's subspace theorem, its quantitative variants
- Arakelov theory: canonical heights, Weil height machines, Gillet-Soulé intersection theory
- Nevanlinna theory (the function-field analogue, which motivates Vojta's dictionary)
- Explicit Chabauty-Coleman methods for curves of genus $\geq 2$
- The ABC conjecture (Vojta's conjecture for $\mathbb{P}^1$ with $D$ = three points implies ABC)

### What's known

- **Faltings (1991):** Proved the Mordell conjecture (finiteness of rational points on curves of genus $\geq 2$), which is a consequence of Vojta's conjecture for curves.
- **Vojta (1987):** Proved that his conjecture implies Faltings' theorem (then a conjecture), Roth's theorem, Schmidt's subspace theorem, and the Mordell-Lang conjecture for abelian varieties.
- **Hindry-Silverman (1988):** Proved that Vojta's conjecture implies the ABC conjecture.
- **For elliptic curves specifically:** Vojta's conjecture implies that if $E(\mathbb{Q})$ has rank $r \geq 1$, the canonical height of generators satisfies $h(P_i) \leq C(E, \epsilon) \cdot |\Delta_E|^{1+\epsilon}$ for an explicit constant, giving effective upper bounds on the height of generators.
- **No effective bounds** are known unconditionally for the height of generators of $E(\mathbb{Q})$ even for rank 1.

### Main obstacle

- Vojta's conjecture is completely open in general; even the ABC conjecture (its simplest case) has only conditional proofs (Mochizuki's claimed proof is disputed; Tao's polynomial method gives partial results in characteristic $p$).
- The passage from the Diophantine approximation inequality to explicit bounds on heights of points on $E(\mathbb{Q})$ requires understanding the geometry of $E$ inside its ambient projective space and the distribution of rational points near the divisor $D$.
- Even conditional on Vojta, extracting *effective* constants requires quantitative versions of the subspace theorem (Evertse, Schlickewei) which are notoriously difficult.

### BSD connection

- **Direct link:** BSD predicts $L^{(r)}(E, 1) / r! = \Omega \cdot \operatorname{Reg} \cdot |\Sha| \cdot \prod c_p / |E(\mathbb{Q})_{\mathrm{tor}}|^2$, where $\operatorname{Reg}$ is the regulator $\det(\langle P_i, P_j \rangle)$. Vojta's conjecture would bound $h(P_i)$ for a basis of the free part, hence bound $\operatorname{Reg}$ from above, hence bound $L^{(r)}(E,1)$ from above.
- **Effective BSD:** If both Vojta and BSD hold, one gets effective lower bounds on $L^{(r)}(E,1)$ (via the BSD formula's other factors being computable) and effective upper bounds on heights (via Vojta). Together they would give *effective* bounds on the height of generators of $E(\mathbb{Q})$ in terms of the conductor $N_E$.
- **Converse direction:** Progress on BSD (especially effective versions) would constrain the regulator, which is the key ingredient in translating Vojta's qualitative statement into a quantitative one for $E$.
- **Implication:** Vojta + BSD $\implies$ effective Mordell for elliptic curves: there is a computable function $f(N_E, \epsilon)$ such that every generator $P$ of $E(\mathbb{Q})$ satisfies $\hat{h}(P) \leq f(N_E, \epsilon) \cdot N_E^\epsilon$.

### Status

**Open conjecture.** Both Vojta and BSD are open; their combination would resolve effective Mordell. No conditional proofs are known combining both.

### Classification

**Vertical connection.** Links Diophantine geometry (Vojta) to the analytic theory of $L$-functions (BSD) through height theory.

---

## I-003. Grothendieck Period Conjecture and the Period $\Omega(E)$

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve with good reduction everywhere (for simplicity). The real period is

$$\Omega(E) = \int_{E(\mathbb{R})} \omega_E,$$

where $\omega_E$ is the Néron differential. The Grothendieck period conjecture (1966, unpublished, formulated precisely by Kontsevich-Zagier 2001) asserts: two $\mathbb{Q}$-linear relations among periods of algebraic varieties defined over $\overline{\mathbb{Q}}$ arise from algebraic-geometric (motivic) relations. Equivalently, the ring of periods $\mathcal{P}$ has a canonical filtration by the weight of the motivic cohomology, and the map from the de Rham realization to the Betti realization respects this filtration.

For $E$, the period $\Omega(E)$ is a period in the sense of Kontsevich-Zagier: it arises from the comparison isomorphism between de Rham and Betti cohomology $H^1_{\mathrm{dR}}(E/\mathbb{Q}) \otimes_{\mathbb{Q}} \mathbb{C} \cong H^1_{\mathrm{B}}(E, \mathbb{Q}) \otimes_{\mathbb{Q}} \mathbb{C}$. The conjecture predicts that $\Omega(E)$ is *transcendental* (which is known) and that any $\mathbb{Q}$-linear relation $\sum a_i \Omega(E_i) = 0$ among such periods arises from an isogeny or algebraic correspondence between the $E_i$.

### Tools needed

- Periods and the period matrix: comparison between de Rham and Betti cohomology
- Kontsevich-Zagier theory of periods and their conjectures
- Transcendence theory: Baker's theorem, Nesterenko's results on $e^\pi$, modular units
- Motivic cohomology: Chow motives, Voevodsky's category of motives
- Grothendieck's standard conjectures on algebraic cycles

### What's known

- **Kontsevich-Zagier (2001):** Formulated the period conjecture precisely; showed that the ring of periods $\mathcal{P}$ is a countable extension of $\mathbb{Q}^{\mathrm{alg}}$ and conjectured that the weight filtration on $\mathcal{P}$ is strictly compatible with algebraic relations.
- **For elliptic curves:** $\Omega(E)$ is known to be transcendental when $E$ does not have CM (follows from the fact that the $j$-invariant is transcendental for non-CM curves and Nesterenko's theorem). For CM curves, $\Omega(E)/\sqrt{D}$ is transcendental where $D$ is the CM discriminant.
- **Brown (2016):** Proved that $\zeta(3)$ is irrational (a consequence of the period conjecture for $\mathbb{P}^2$), but the general conjecture is far from resolved.
- **Ayoub (2014):** Proved a motivic version of the period conjecture for abelian varieties in the sense that the motivic Galois group acts faithfully on motivic periods, conditional on the standard conjectures.

### Main obstacle

- The Grothendieck period conjecture is among the deepest open problems in transcendence theory. It implies the algebraic independence of $\pi$ and $e^\pi$ (which is open).
- For $\Omega(E)$ specifically: proving that $\Omega(E)$ is not only transcendental but also algebraically independent from other periods (e.g., $\Omega(E')$ for non-isogenous $E'$) requires new ideas in transcendence theory.
- The connection to BSD is through the *algebraicity* of the ratio $L^{(r)}(E,1) / (r! \cdot \Omega)$ — the period conjecture predicts when this ratio is algebraic.

### BSD connection

- **Direct link:** BSD states $L^{(r)}(E,1) / r! = \Omega(E) \cdot \operatorname{Reg}(E) \cdot |\Sha(E)| \cdot \prod c_p / |E(\mathbb{Q})_{\mathrm{tor}}|^2$. The right side is a product of $\Omega(E)$ (a period) and algebraic/arithmetic quantities. The conjecture predicts that $L^{(r)}(E,1) / r!$ is a period of $E$ times algebraic factors, hence that the ratio $L^{(r)}(E,1) / \Omega(E)$ is algebraic.
- **Motivic implication:** If the Grothendieck period conjecture holds, then $L^{(r)}(E,1) / \Omega(E) \in \overline{\mathbb{Q}}$ for all $E$, which is a necessary consequence of BSD. Moreover, the conjecture predicts that the *only* $\overline{\mathbb{Q}}$-linear relations among the $\Omega(E)$ arise from correspondences between the $E$, which constrains the possible values of the regulators.
- **Converse:** Progress on BSD (knowing the exact value of $L^{(r)}(E,1)$) would give specific numerical values of $L^{(r)}(E,1)/\Omega(E)$, providing testable predictions for the Grothendieck period conjecture.
- **Implication:** Grothendieck period conjecture $\implies$ $L^{(r)}(E,1)/\Omega(E) \in \overline{\mathbb{Q}}$ for all $E/\mathbb{Q}$, a necessary condition for BSD.

### Status

**Deep open conjecture.** The implication from Grothendieck period conjecture to the algebraicity of $L^{(r)}/\Omega$ is clear. The converse direction (BSD constraining periods) is largely unexplored.

### Classification

**Foundational connection.** Links transcendence theory and motivic cohomology to the analytic theory of $L$-functions through the BSD period formula.

---

## I-004. Sato-Tate Distribution and $L$-function Zeros Near $s=1$

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve without CM. The Sato-Tate conjecture (now a theorem) asserts that the angles $\theta_p \in [0, \pi]$ defined by $a_p(E) = 2\sqrt{p} \cos \theta_p$ are equidistributed with respect to the measure

$$d\mu_{\mathrm{ST}} = \frac{2}{\pi} \sin^2 \theta \, d\theta.$$

More precisely, for any interval $[a, b] \subset [0, \pi]$,

$$\lim_{x \to \infty} \frac{\#\{p \leq x : \theta_p \in [a,b]\}}{\pi(x)} = \frac{2}{\pi} \int_a^b \sin^2 \theta \, d\theta.$$

The connection to BSD is through the distribution of zeros of $L(E, s)$ near $s=1$. If $\rho = 1 - 1/(\log N_E)$ is the "edge" of the critical strip for the approximate functional equation, the spacing and density of zeros near $s=1$ are influenced by the distribution of $a_p$ (which enters the explicit formula via the sum over primes).

### Tools needed

- Automorphic forms: the modularity theorem (Wiles et al.), automorphy of the symmetric powers $\operatorname{Sym}^n E$
- Serre's Sato-Tate conjecture and its proof (Barnet-Lamb, Geraghty, Harris, Taylor)
- The explicit formula for $L(E, s)$ relating zeros to prime sums over $a_p$
- Random matrix theory: Katz-Sarnak philosophy for zero statistics
- Montgomery's pair correlation conjecture and its analogues for $L$-functions

### What's known

- **Barnet-Lamb, Geraghty, Harris, Taylor (2011):** Proved the Sato-Tate conjecture for all elliptic curves over totally real fields (assuming potential automorphy, which is known).
- **Katz-Sarnak (1999):** Predicted that the distribution of low-lying zeros of $L(E, s)$ near $s=1$ follows the statistics of eigenvalues of matrices in $USp(2g)$ (the symplectic group), where $g$ is the "analytic rank."
- **Iwaniec-Luo-Sarnak (2000):** Verified the Katz-Sarnak prediction for the one-level density of low-lying zeros of $L$-functions of modular forms, under GRH.
- **Conrey et al. (2005):** Showed that the one-level density for $L(E, s)$ matches $USp$ statistics for test functions with Fourier support in $(-2, 2)$.
- The connection between Sato-Tate and the behavior near $s=1$ is through the explicit formula: $\sum_\gamma h(\gamma) = \hat{h}(0) \log N_E / (2\pi) + \sum_p a_p \hat{h}(\log p) / \sqrt{p} + \cdots$, where $\gamma$ ranges over the imaginary parts of zeros.

### Main obstacle

- Extending the zero-density results to *all* test functions (Fourier support beyond $(-2,2)$) requires the Generalized Riemann Hypothesis.
- The Sato-Tate equidistribution controls the *average* behavior of $a_p$, but BSD requires information about the *individual* curve $E$ — specifically, whether $L(E,1) = 0$ or not.
- The explicit formula connects $L(E,1)$ to $\sum_p a_p / \sqrt{p}$ plus zeros, but converting average-case Sato-Tate information into individual-case predictions about vanishing at $s=1$ is the crux of the problem.

### BSD connection

- **Direct link:** The BSD conjecture predicts that $\operatorname{ord}_{s=1} L(E,s) = \operatorname{rank} E(\mathbb{Q})$. The Sato-Tate distribution, via the explicit formula, constrains the *expected* number of zeros near $s=1$. For a "random" elliptic curve ordered by conductor, the expected analytic rank is $\leq 1$ (by the Katz-Sarnak heuristics), consistent with BSD predicting rank $\leq 1$ generically.
- **Density implication:** The Katz-Sarnak philosophy predicts that the proportion of elliptic curves with analytic rank $r$ is approximately $\prod_{j=1}^r \frac{1}{(2j-1)!!}$ (symplectic model). If true, combined with BSD, this would imply density results for ranks of elliptic curves.
- **Converse:** If BSD were proven, the Sato-Tate distribution would give statistical information about the distribution of ranks among curves in a family.
- **Implication:** Sato-Tate + explicit formula + GRH $\implies$ the "average" value of $\operatorname{ord}_{s=1} L(E,s)$ is constrained. Combined with BSD, this gives density results for ranks.

### Status

**Active research.** Sato-Tate proven; low-lying zeros studied conditionally on GRH. The bridge to BSD through density of ranks is partially understood but incomplete.

### Classification

**Statistical bridge.** Connects the equidistribution theory (Sato-Tate) to the vanishing order problem (BSD) through random matrix heuristics and the explicit formula.

---

## I-005. Stark's Conjecture and Leading Taylor Coefficients

### Statement

Let $K/\mathbb{Q}$ be a number field and $\chi$ a character of $\operatorname{Gal}(K^{\mathrm{ab}}/K)$. The Stark conjecture (1975–1980) predicts the existence of "Stark units" $\epsilon \in K^{\mathrm{ab}}$ whose regulator equals the leading Taylor coefficient of the Artin $L$-function at $s=0$:

$$\frac{d}{ds} L(s, \chi)\Big|_{s=0} = -\frac{1}{w_K} \sum_\sigma \chi(\sigma) \log |\sigma(\epsilon)|,$$

where $w_K$ is the number of roots of unity in $K$ and the sum is over $\sigma \in \operatorname{Gal}(K^{\mathrm{ab}}/K)$.

For an elliptic curve $E/\mathbb{Q}$ with CM by $K$, the $L$-function factors: $L(E/\mathbb{Q}, s) = L(\psi, s) L(\bar{\psi}, s)$ where $\psi$ is a Hecke character of $K$. BSD then asserts that $L'(E/\mathbb{Q}, 1) = \Omega \cdot \operatorname{Reg}$ (rank 1 case), which is a statement about the leading Taylor coefficient of the *Hecke* $L$-function. Stark's conjecture, applied to the character $\psi$, would produce a "Stark unit" whose regulator computes this leading coefficient.

### Tools needed

- Stark's conjectures: the original Stark conjecture, refined versions (Rubin, Popescu)
- Rubin's $p$-adic Stark conjecture and its relation to Iwasawa theory
- Hecke characters, CM theory, and the factorization of $L$-functions for CM abelian varieties
- Equivariant Tamagawa number conjecture (ETNC), which refines both Stark and BSD
- The Gross-Stark regulator and its computation

### What's known

- **Stark (1975–1980):** Formulated the conjecture; proved cases for abelian extensions of $\mathbb{Q}$ with $L(0,\chi)=0$ to order 1.
- **Rubin (1996):** Proved a $p$-adic version of Stark's conjecture for CM abelian varieties, which is directly relevant to the BSD connection.
- **Dasgupta, Kakde, Ventullo (2018):** Proved the Brumer-Stark conjecture (a refinement) and made progress on the full Stark conjecture for totally real fields.
- **Popescu (2002):** Proved a base-change version of the Stark conjecture for CM extensions.
- **Gross (1981):** Formulated a $p$-adic analogue of Stark's conjecture relating $p$-adic $L$-functions to $p$-adic regulators of Stark units.

### Main obstacle

- Stark's conjecture in full generality is open, though major cases are resolved.
- The bridge between Stark units (which are algebraic numbers in abelian extensions) and the BSD regulator (which involves the Néron-Tate height of points on $E$) requires relating the Archimedean regulator $\sum \chi(\sigma) \log |\sigma(\epsilon)|$ to the height pairing $\langle P, P \rangle$ on $E$. This is the "Stark-Heegner" bridge.
- For CM curves, the factorization $L(E/\mathbb{Q},s) = L(\psi,s) L(\bar{\psi},s)$ means BSD for $E$ involves $L'(E/\mathbb{Q},1)$, while Stark concerns $L'(\psi,0)$. The functional equation connects these, but the factors of $\Omega(E)$ that appear require careful analysis.

### BSD connection

- **Direct link (CM case):** For $E/\mathbb{Q}$ with CM by $K$ and rank 1, BSD asserts $L'(E,1) = \Omega(E) \cdot \hat{h}(P) \cdot c$. Stark's conjecture for $\psi$ asserts $L'(\psi, 0) = \text{regulator of Stark unit}$. The functional equation relates $L'(E,1)$ to $L'(\psi,0)$ via $\Omega(E)$, so Stark + functional equation $\implies$ a formula for $\hat{h}(P)$ in terms of the Stark unit.
- **ETNC bridge:** The Equivariant Tamagawa Number Conjecture (Burns-Flach, 2001) simultaneously generalizes both BSD and Stark. It predicts that a certain element in relative K-theory — built from the Stark unit and the $L$-value — maps to the trivial element under the regulator map. Proving ETNC for $E$ would imply both BSD and Stark simultaneously.
- **Implication:** For CM elliptic curves, Stark's conjecture $\implies$ the regulator formula in BSD (rank 1), provided the bridge between Stark units and Heegner points is established. In the other direction, BSD for CM curves $\implies$ the Stark conjecture for the Hecke character $\psi$.

### Status

**Partially proven.** Stark's conjecture is known for many cases; the bridge to BSD is explicit for CM curves via Rubin's work and ETNC.

### Classification

**Regulator connection.** Links the Stark regulator (abelian $L$-functions) to the BSD regulator (elliptic curve heights) through the ETNC.

---

## I-006. The Bloch-Kato Conjecture as a Generalization of BSD

### Statement

Let $V$ be a geometric motive over $\mathbb{Q}$ (e.g., the motive $h^1(E)(n)$ associated to an elliptic curve $E$ and Tate twist $n$). The Bloch-Kato conjecture (1990) asserts that the order of the Selmer group

$$H^1_f(\mathbb{Q}, V) = \ker\left(H^1(\mathbb{Q}, V) \to \prod_v H^1(\mathbb{Q}_v, V) / H^1_f(\mathbb{Q}_v, V)\right)$$

equals the order of the "denominator" of the leading Taylor coefficient of $L(V, s)$ at its central point, normalized by periods and local factors:

$$\frac{L^*(V, 0)}{\Omega(V) \cdot \prod_p c_p(V)} \stackrel{?}{=} \frac{|H^1_f(\mathbb{Q}, V^\vee(1))|}{|H^0(\mathbb{Q}, V^\vee(1))| \cdot |H^0(\mathbb{Q}, V)|} \cdot |\text{torsion factor}|.$$

For $V = h^1(E)$, this recovers exactly the Birch and Swinnerton-Dyer conjecture. For $V = h^1(E)(1)$, it gives a statement about the $p$-adic regulator and the formal group.

### Tools needed

- Motivic cohomology: Bloch's higher Chow groups, Voevodsky's motivic cohomology
- Galois cohomology: local and global Selmer groups, Bloch-Kato exponential map
- The Tamagawa number conjecture: Bloch-Kato's formulation, Burns-Flach refinement
- $p$-adic Hodge theory: Fontaine's rings $\mathbf{B}_{\mathrm{dR}}$, $\mathbf{B}_{\mathrm{cris}}$, filtered $(\varphi, N)$-modules
- Special values of $L$-functions: Deligne's conjecture for critical values, Beilinson's regulator

### What's known

- **Bloch-Kato (1990):** Formulated the conjecture; proved it for Tate motives $h^0(\operatorname{Spec} K)(n)$ (Dirichlet unit theorem and class number formula).
- **For elliptic curves ($V = h^1(E)$):** This is BSD, which is known for rank 0 and 1 cases (by Gross-Zagier-Kolyvagin).
- **For $V = h^1(E)(n)$, $n \geq 2$:** These are "higher twists" of BSD. Cases are known for $n \geq 2$ and $\operatorname{ord}_{s=0} L(E, n) = 0$ by work of Beilinson (1984) and Deninger (1984) using Beilinson's regulator.
- **Flach (1992):** Proved cases for symmetric squares of modular forms.
- **Nekovar (1993, 2006):** Extended Kolyvagin's methods to the Bloch-Kato setting, proving cases for rank $\leq 1$.
- **Burns-Flach (2001):** Reframed the conjecture as the equivariant Tamagawa number conjecture (ETNC), which is more amenable to Iwasawa-theoretic methods.

### Main obstacle

- For general motives $V$, the Selmer group $H^1_f(\mathbb{Q}, V)$ is not well-understood: constructing elements (analogues of Heegner points) is difficult beyond rank 1.
- The Bloch-Kato exponential map $\exp: D_{\mathrm{dR}}(V) / F^0 \to H^1_f(\mathbb{Q}, V)$ is well-defined but computing its kernel and cokernel requires $p$-adic Hodge theory beyond current techniques.
- For rank $\geq 2$, even the formulation requires choosing a basis for the Selmer group, and the "denominator" of the $L$-value depends on the choice.

### BSD connection

- **Direct generalization:** BSD is the special case $V = h^1(E)$ of the Bloch-Kato conjecture. Every known instance of BSD is also an instance of Bloch-Kato, and every proof technique for BSD (Heegner points, Kolyvagin, Gross-Zagier) has been or can be extended to the Bloch-Kato framework.
- **Higher twists as test cases:** Proving Bloch-Kato for $V = h^1(E)(n)$ for $n \geq 2$ is in some cases *easier* than BSD (the $L$-function is non-vanishing for $n \geq 2$ by Beilinson's theorem), and the techniques developed there (Beilinson's regulator, Eisenstein symbols) feed back into the rank $\geq 2$ case of BSD.
- **Implication:** Bloch-Kato for all twists $h^1(E)(n)$, $n \in \mathbb{Z}$, is equivalent to BSD plus the non-vanishing conjecture $L(E, n) \neq 0$ for $n \geq 2$ plus the $p$-adic BSD (Perrin-Riou, Schneider). Progress on Bloch-Kato directly implies progress on BSD and vice versa.

### Status

**BSD is a special case.** Known for rank 0, 1 (Gross-Zagier-Kolyvagin). The general Bloch-Kato conjecture is open but has numerous partial results.

### Classification

**Generalization.** BSD embeds into Bloch-Kato as a special case; progress on either directly informs the other.

---

## I-007. Birch-Swinnerton-Dyer and the Hodge Conjecture (for Products of Elliptic Curves)

### Statement

The Hodge conjecture (1950) asserts that for a smooth projective variety $X$ over $\mathbb{C}$, every Hodge class in $H^{2p}(X, \mathbb{Q}) \cap H^{p,p}(X)$ is a $\mathbb{Q}$-linear combination of classes of algebraic cycles.

For the product $X = E_1 \times E_2$ of two elliptic curves, $H^2(X, \mathbb{Q}) \cong H^1(E_1) \otimes H^1(E_2) \oplus \text{other terms}$. The Hodge classes in $H^{1,1}(E_1 \times E_2) \cap H^2(E_1 \times E_2, \mathbb{Q})$ correspond to classes of divisors on $E_1 \times E_2$, which include the graphs of isogenies $E_1 \to E_2$. The Hodge conjecture for $E_1 \times E_2$ predicts that every Hodge class in $H^2$ is algebraic — this is equivalent to saying that the Néron-Severi group $\operatorname{NS}(E_1 \times E_2)$ has rank equal to $2 + \operatorname{Hom}(E_1, E_2) \otimes \mathbb{Q}$.

### Tools needed

- Hodge theory: Hodge decomposition, Hodge structures on $H^1$ of abelian varieties
- Néron-Severi groups, algebraic cycles on products of curves
- The Tate conjecture (the $\ell$-adic analogue of Hodge)
- Modularity and Galois representations attached to elliptic curves
- Shioda-Inose theory for K3 surfaces (arising as quotients of $E \times E$)

### What's known

- **The Hodge conjecture is known for:** products of curves (Lefschetz), abelian surfaces (Shioda), $H^2$ of K3 surfaces (combined work of Bogomolov, Tsen, Todorov, and others).
- **For $E_1 \times E_2$ where $E_1, E_2$ are non-isogenous over $\overline{\mathbb{Q}}$:** The Hodge conjecture holds trivially since $\operatorname{NS}(E_1 \times E_2) = \mathbb{Z}[E_1 \times \{0\}] \oplus \mathbb{Z}[\{0\} \times E_2]$ and the Hodge conjecture predicts rank 2, which is correct.
- **For $E_1 \times E_2$ where $\operatorname{Hom}(E_1, E_2) \neq 0$:** The Hodge conjecture holds since every Hodge class corresponds to a correspondence, and correspondences between isogenous elliptic curves are algebraic (the graph of the isogeny).
- **Zarhin (1983):** Proved the Tate conjecture (and hence Hodge conjecture in the relevant degree) for products of elliptic curves.

### Main obstacle

- The Hodge conjecture for $E_1 \times E_2$ is actually *known* (Zarhin), so the research direction is really about the *interaction* between this known result and BSD.
- The deeper connection is through the *rank* of the Mordell-Weil group: the endomorphism algebra $\operatorname{End}(E_1 \times E_2) \otimes \mathbb{Q}$ influences the Galois representation $V_\ell(E_1 \times E_2)$, which in turn determines the $L$-function $L(E_1 \times E_2, s) = L(E_1, s) L(E_2, s)$.
- The real open question is: for a general abelian surface $A$ (not necessarily a product of elliptic curves), does the Hodge conjecture for $A$ constrain the analytic rank of $A$?

### BSD connection

- **Direct link (products):** BSD for $E_1 \times E_2$ is equivalent to BSD for $E_1$ and BSD for $E_2$ independently (since $L(E_1 \times E_2, s) = L(E_1, s) L(E_2, s)$). The Hodge conjecture, by controlling $\operatorname{NS}(E_1 \times E_2)$, constrains the *endomorphism algebra* $\operatorname{End}(E_1 \times E_2)$, which determines the splitting of the $L$-function.
- **General abelian surfaces:** For an abelian surface $A$ that is *not* a product, the Hodge conjecture for $A \times A$ (which is open) would control the Néron-Severi group and hence the endomorphism algebra, which determines whether $L(A, s)$ factors as a product of $L$-functions of lower-dimensional motives.
- **Tate conjecture link:** The Tate conjecture (proven for abelian varieties over finite fields by Tate) predicts that $\operatorname{rank} \operatorname{NS}(A) = \operatorname{ord}_{s=1} \zeta(A, s)$ (the pole order of the zeta function). For $A$ over $\mathbb{Q}$, this connects the rank of the Néron-Severi group to the analytic behavior of the $L$-function, which is precisely the domain of BSD.
- **Implication:** For a general abelian surface $A/\mathbb{Q}$, the Hodge conjecture + Tate conjecture + BSD would together determine the endomorphism ring, the $L$-function factorization, and the Mordell-Weil rank. Progress on any one constrains the others.

### Status

**Known for products** (Zarhin). The real research direction is extending the Hodge/BSD interplay to non-product abelian varieties and general motives.

### Classification

**Structural connection.** Links the algebraic cycles on $E \times E$ (Hodge) to the analytic rank of $E$ (BSD) through the endomorphism algebra.

---

## I-008. Parity Conjecture (Root Number = Sign of Functional Equation)

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve with conductor $N$. The completed $L$-function $\Lambda(E, s) = N^{s/2} (2\pi)^{-s} \Gamma(s) L(E, s)$ satisfies the functional equation $\Lambda(E, s) = w_E \cdot \Lambda(E, 2-s)$ where $w_E \in \{+1, -1\}$ is the root number. The parity conjecture asserts:

$$w_E = (-1)^{\operatorname{rank} E(\mathbb{Q})}.$$

Equivalently, the analytic rank $\operatorname{ord}_{s=1} L(E, s)$ and the algebraic rank $\operatorname{rank} E(\mathbb{Q})$ have the same parity.

### Tools needed

- Root number computation: local root numbers, Atkin-Lehner involutions, the conductor-discriminant formula
- Galois representations: $V_\ell(E) = T_\ell(E) \otimes \mathbb{Q}_\ell$ and its local behavior at bad primes
- The Cassels-Tate pairing: the alternating pairing on $\Sha(E)$, its non-degeneracy
- Kolyvagin's Euler systems and the structure of Selmer groups
- Deligne's theorem on the sign of the functional equation

### What's known

- **Nekovar (2006):** Proved the parity conjecture for elliptic curves over $\mathbb{Q}$ with at least one prime of multiplicative reduction, conditional on the finiteness of $\Sha$.
- **Dokchitser-Dokchitser (2010):** Proved the parity conjecture for elliptic curves over $\mathbb{Q}$ with potentially good reduction at all odd primes, conditional on the finiteness of $\Sha$.
- **Gross-Zagier-Kolyvagin:** Implies the parity conjecture for rank $\leq 1$ (since if $w_E = -1$, the analytic rank is odd, hence $\geq 1$, and Heegner point methods produce a point of infinite order; if $w_E = +1$, Kolyvagin shows rank $\leq 0$).
- **Dokchitser-Dokchitser (2010):** Unconditionally proved the parity conjecture for all elliptic curves over $\mathbb{Q}$ in the "Shafarevich-Tate" setting (i.e., assuming only that $\Sha$ is finite).
- **Das (2023):** Made progress on unconditional parity using the methods of Bhargava-Shankar on average results.
- The conjecture is still open unconditionally, even for specific families.

### Main obstacle

- The parity conjecture is a consequence of BSD (specifically, the non-degeneracy of the Cassels-Tate pairing plus the formula for the root number). The difficulty is proving it *without* assuming the full BSD conjecture.
- The key insight (Cassels) is that the Cassels-Tate pairing is an alternating bilinear form on $\Sha(E)[p^\infty]$, so $|\Sha(E)[p^\infty]| = p^{2k}$ for some $k$, and the parity of $\dim_{\mathbb{F}_p} \operatorname{Sel}_p(E)$ determines the parity of the rank. But this requires $\Sha$ to be finite.
- Proving parity *unconditionally* (without assuming $\Sha$ is finite) requires new methods that bypass the Cassels-Tate pairing.

### BSD connection

- **Direct link:** BSD $\implies$ parity conjecture. This follows from: (1) $L^{(r)}(E,1) = \Omega \cdot \operatorname{Reg} \cdot |\Sha| \cdot \prod c_p / |E_{\mathrm{tor}}|^2$ implies $\operatorname{ord}_{s=1} L(E,s) = \operatorname{rank} E(\mathbb{Q})$; (2) the functional equation gives $w_E = (-1)^{\operatorname{ord}_{s=1} L(E,s)}$.
- **Partial converse:** The parity conjecture is the *weakest* consequence of BSD. Proving it would confirm the "easy" part of BSD (parity matching) but would not imply the full conjecture.
- **Euler system angle:** Kolyvagin's work shows that if $w_E = -1$, there exists a Heegner point of infinite order. The converse direction (if $\operatorname{rank}$ is odd, then $w_E = -1$) is the parity conjecture and would follow from a sufficiently strong Euler system argument.
- **Implication:** Parity conjecture $\implies$ $w_E = (-1)^{\operatorname{rank} E(\mathbb{Q})}$ for all $E$. This is necessary for BSD but far from sufficient. Conversely, proving BSD for a single elliptic curve with $\Sha$ of non-square order would imply a strong form of the parity conjecture.

### Status

**Conditional proofs known** (assuming $\Sha$ finite). Unconditional proofs known for specific families. Open in full generality.

### Classification

**Weakest consequence of BSD.** The parity conjecture is the minimal arithmetic content of BSD; proving it is a stepping stone toward the full conjecture.

---

## I-009. Selmer Group Parity and Greenberg's Conjecture on $\mu$-invariant

### Statement

Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at $p$. Let $\mathbb{Q}_\infty = \mathbb{Q}(\mu_{p^\infty})$ be the cyclotomic $\mathbb{Z}_p$-extension of $\mathbb{Q}$, and let $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}_\infty)$ be the Pontryagin dual of the Selmer group over $\mathbb{Q}_\infty$. As a $\Lambda$-module (where $\Lambda = \mathbb{Z}_p[[\operatorname{Gal}(\mathbb{Q}_\infty/\mathbb{Q})]]$ is the Iwasawa algebra), this module has an associated characteristic power series $f(T) \in \Lambda$. The $\mu$-invariant $\mu_E$ is the power of $p$ dividing $f(T)$.

Greenberg's conjecture (1973) asserts that $\mu_E = 0$ for all elliptic curves $E/\mathbb{Q}$ with good ordinary reduction at $p$. More broadly, Greenberg's conjecture predicts that for any motive $V$ over $\mathbb{Q}$ that is ordinary at $p$, the $\mu$-invariant of the associated Selmer group over the cyclotomic $\mathbb{Z}_p$-extension vanishes.

The connection to BSD is through the $p$-adic BSD formula (Perrin-Riou, Schneider): the leading term of the characteristic power series at $T = 0$ encodes the $p$-adic $L$-function $L_p(E, 1)$, and the $\mu$-invariant measures the "depth of $p$-adic divisibility" of this leading term.

### Tools needed

- Iwasawa theory: $\Lambda$-modules, structure theorem, $\mu$ and $\lambda$ invariants
- Selmer groups: the classical Selmer group, the strict Selmer group, control theorems (Greenberg)
- $p$-adic $L$-functions: modular symbols, Mazur-Swinnerton-Dyer $p$-adic $L$-function, Perrin-Riou's exponential map
- Hida families: ordinary $p$-adic families of modular forms and their $p$-adic $L$-functions
- The Iwasawa Main Conjecture (IMC): proved by Skinner-Urban (2014) for $E/\mathbb{Q}$ ordinary at $p$ under mild hypotheses

### What's known

- **Ferrero-Washington (1979):** Proved $\mu = 0$ for the cyclotomic $\mathbb{Z}_p$-extension of abelian number fields (the "classical" Iwasawa $\mu$-invariant for the class group).
- **Greenberg (1973):** Conjectured $\mu_E = 0$ for all elliptic curves; gave evidence from numerical computations.
- **Skinner-Urban (2014):** Proved the Iwasawa Main Conjecture for $E/\mathbb{Q}$ ordinary at $p$ (under certain Selmer group hypotheses), relating the characteristic series of the Selmer group to the $p$-adic $L$-function.
- **Kato (2004):** Constructed Euler systems for modular forms, establishing one divisibility of the IMC.
- **Wan (2014):** Proved the IMC for many specific curves by combining Kato's Euler system with results on the dual Selmer group.
- **Pollack-Weston (2014):** Proved the IMC for modular forms in Hida families under "generic" hypotheses.
- $\mu_E = 0$ is known when $E$ has supersingular reduction at $p$ (Kim, 2004) and for many ordinary cases by computation, but remains open in full generality.

### Main obstacle

- Proving $\mu_E = 0$ requires showing that the $p$-adic $L$-function $L_p(E, T) \in \Lambda$ has content 1 (no $p$ in its coefficients). This is a $p$-adic transcendence/arithmetic property of the $p$-adic $L$-function.
- The Iwasawa Main Conjecture equates the characteristic ideal of the Selmer group with the ideal generated by $L_p(E, T)$, so $\mu_E = 0 \iff L_p(E, T)$ is a unit in $\mathbb{Z}_p[[T]]$ modulo the relevant ideal.
- The key difficulty: $L_p(E, T)$ is defined by interpolation of $L$-values, and proving that these interpolated values are $p$-integral requires understanding the $p$-adic valuations of the Bernoulli-like numbers that appear.

### BSD connection

- **Direct link ($p$-adic BSD):** The $p$-adic BSD conjecture (Perrin-Riou, Schneider) states that

$$L_p(E, 1) = \left(1 - \frac{1}{a_p}\right) \cdot \frac{L'(E,1)}{\Omega_p(E)} \cdot \frac{|\Sha(E)|}{|E(\mathbb{Q})_{\mathrm{tor}}|^2} \cdot \operatorname{Reg}_p(E),$$

where $\Omega_p(E)$ is the $p$-adic period and $\operatorname{Reg}_p(E)$ is the $p$-adic regulator. If $\mu_E = 0$, then $L_p(E, T)$ is a well-defined element of $\mathbb{Z}_p[[T]]$, and the $p$-adic BSD formula relates its value at $T=0$ to the classical BSD quantities.

- **Greenberg's $\mu = 0$ $\implies$ $p$-adic BSD is well-posed:** If $\mu_E > 0$, the $p$-adic $L$-function is divisible by $p$ and the $p$-adic BSD formula would need to be modified. Greenberg's conjecture ensures the formula has no "extra" $p$-factors.

- **Classical BSD $\implies$ $\mu_E = 0$ under mild conditions:** If BSD holds and $\Sha(E)$ is finite, the $p$-adic $L$-function $L_p(E, 1) = (1 - 1/a_p) \cdot L'(E,1) / \Omega_p$ is a $p$-adic integer (since $L'(E,1)/\Omega$ is rational by BSD and the $p$-adic regulator is $p$-integral). This implies $\mu_E = 0$.

- **Parity and $\mu$:** The parity of $\operatorname{rank} E(\mathbb{Q})$ is determined by $w_E$. The $\mu$-invariant controls the *$p$-adic* order of the Selmer group, which is a refinement of the parity information. Greenberg's conjecture on $\mu$ is the "$p$-adic shadow" of the parity conjecture.

- **Implication:** BSD $\implies$ Greenberg's $\mu = 0$. Conversely, Greenberg's $\mu = 0$ + IMC $\implies$ the $p$-adic BSD formula is well-posed, which is a necessary condition for $p$-adic approaches to BSD.

### Status

**Open conjecture.** Known for many specific curves and for supersingular reduction. The Iwasawa Main Conjecture (which equates $\mu_E$ with the $\mu$-invariant of the $p$-adic $L$-function) is proven under mild hypotheses (Skinner-Urban).

### Classification

**$p$-adic refinement.** Greenberg's conjecture is the $p$-adic Iwasawa-theoretic shadow of BSD; it is both implied by BSD and necessary for $p$-adic approaches to BSD.

---

## I-010. BSD and the Fontaine-Mazur Conjecture

### Statement

The Fontaine-Mazur conjecture (1993) asserts: a continuous $p$-adic representation $\rho: \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to GL_n(\mathbb{Q}_p)$ that is unramified at almost all primes and de Rham at $p$ is geometric, i.e., it arises from a motive (specifically, it is a subquotient of the étale cohomology of an algebraic variety).

For an elliptic curve $E/\mathbb{Q}$, the associated Galois representation $V_p(E) = T_p(E) \otimes \mathbb{Q}_p$ is known to be geometric (by modularity). The conjecture becomes relevant for BSD through the Selmer group $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$: its Pontryagin dual $X(E/\mathbb{Q})$ has a natural structure as a $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$-module, and the Fontaine-Mazur conjecture predicts constraints on which Galois modules can appear in extensions

$$0 \to V_p(E) \to W \to \mathbb{Q}_p \to 0$$

that are de Rham and unramified almost everywhere. The Selmer group $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ is exactly the group of such extensions that are "flat" at all primes.

### Tools needed

- $p$-adic Hodge theory: Fontaine's classification of $p$-adic representations (de Rham, crystalline, semistable, Hodge-Tate)
- Selmer groups: the Bloch-Kato Selmer group $H^1_f(\mathbb{Q}, V)$ for $V = V_p(E)$
- The Fontaine-Laffaille theory and its generalizations (Breuil, Kisin)
- Modularity and potential modularity: Taylor-Wiles, Skinner-Wiles, Thorne
- Deformation theory of Galois representations: Mazur's theory, the universal deformation ring

### What's known

- **Fontaine-Mazur (1993):** Formulated the conjecture; proved that geometric representations are de Rham at $p$ (one direction).
- **Kisin (2003, 2006):** Proved the Fontaine-Mazur conjecture for $\operatorname{GL}_2$ (dimension 2 representations) over $\mathbb{Q}$: every 2-dimensional $p$-adic representation that is de Rham at $p$ and unramified almost everywhere is modular (hence geometric). This is a landmark result.
- **For $E/\mathbb{Q}$:** The representation $V_p(E)$ is known to be geometric by modularity (Wiles et al.). The relevant question for BSD is about *extensions* of $V_p(E)$, which is where Fontaine-Mazur becomes non-trivial.
- **Greenberg (1989):** Defined the "strict" Selmer group and showed its relation to the $\mu$-invariant, connecting Fontaine-Mazur to Iwasawa theory.
- **Nekovar (2006):** Showed that the Fontaine-Mazur conjecture for extensions $0 \to V_p(E) \to W \to \mathbb{Q}_p \to 0$ implies that certain Selmer group elements are "geometric" (i.e., arise from Heegner points or Beilinson elements).

### Main obstacle

- Kisin's proof of Fontaine-Mazur for $\operatorname{GL}_2$ does not directly apply to extensions of 2-dimensional representations (the representation $W$ in the sequence above is 3-dimensional).
- For the BSD application, one needs to show that *every* extension class in $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ is geometric. This would mean that every element of $\Sha(E)[p^\infty]$ arises from an actual global point (rather than being "phantom"), which is much stronger than finiteness of $\Sha$.
- The Fontaine-Mazur conjecture for $\operatorname{GL}_n$ with $n \geq 3$ is largely open, and the extension $W$ above is 3-dimensional.

### BSD connection

- **Direct link:** The Selmer group $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ classifies extensions $0 \to V_p(E) \to W \to \mathbb{Q}_p(1) \to 0$ that are flat at all primes. The Fontaine-Mazur conjecture predicts these extensions are geometric. If this were known, it would imply:
  1. Every element of $\Sha(E)[p^\infty]$ is "motivic" (arises from a cycle or point).
  2. The $p$-part of the BSD formula has a clean motivic interpretation.
  3. The $p$-adic BSD conjecture (Perrin-Riou) is well-posed.

- **BSD $\implies$ Fontaine-Mazur for the extension:** If BSD holds (and $\Sha$ is finite), then $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ is finitely generated over $\mathbb{Z}_p$, and every element of the $p$-primary Selmer group comes from an actual point of $E(\mathbb{Q})$ or from a $p$-adic unit. These extensions are automatically geometric (by the theory of the Tate module).

- **Fontaine-Mazur $\implies$ structural constraint on BSD:** The Fontaine-Mazur conjecture would imply that the Selmer group has a specific Galois-theoretic structure (being built from geometric representations), which constrains its size. In particular, it would imply that $|\Sha(E)[p^\infty]| = p^{2k}$ for some $k$ (a consequence of the Cassels-Tate pairing), and that the $p$-part of the regulator is non-degenerate.

- **Deformation theory angle:** The universal deformation ring of $V_p(E)$ (Mazur) parametrizes all lifts of the mod-$p$ representation. The Fontaine-Mazur conjecture constrains which points on this deformation space are geometric. If the "BSD locus" (representations arising from the Selmer group) is contained in the "geometric locus" (Fontaine-Mazur), this gives a structural proof of the arithmetic constraints predicted by BSD.

- **Implication:** Fontaine-Mazur for $\operatorname{GL}_3$ over $\mathbb{Q}$ $\implies$ every element of $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ is geometric $\implies$ $\Sha(E)[p^\infty]$ has a clean motivic interpretation. Combined with the IMC, this gives a complete $p$-adic formulation of BSD.

### Status

**Open for $GL_3$.** Fontaine-Mazur is proven for $\operatorname{GL}_2$ (Kisin); the relevant case for BSD involves $\operatorname{GL}_3$ extensions and is open. The connection to BSD is well-understood conceptually but unproven.

### Classification

**Structural prerequisite.** The Fontaine-Mazur conjecture provides the $p$-adic Hodge-theoretic framework within which the $p$-adic BSD conjecture is naturally formulated; proving it for the relevant representations would complete the motivic foundation for BSD.

---

# Directions J-001 through J-012: Unconventional and Emerging Approaches

---

## J-001: Mirror Symmetry for Elliptic Curves and L-values

**Statement.** Investigate whether the homological mirror symmetry correspondence—specifically the equivalence between the derived Fukaya category of an elliptic curve and the derived category of coherent sheaves on its mirror—can be leveraged to construct algebraic cycles whose regulators detect leading L-values of elliptic curves. Concretely, if $E/\mathbb{Q}$ is an elliptic curve, seek a mirror partner $\check{E}$ and a Lagrangian submanifold $\mathcal{L} \subset E(\mathbb{C})$ whose Floer-theoretic invariants encode the order of vanishing of $L(E, s)$ at $s = 1$.

**Tools needed.** Homological mirror symmetry (Kontsevich, 1994; Polishchuk–Zaslow), derived Fukaya categories, Floer homology, Bridgeland stability conditions, Beilinson–Bloch regulators, Chen–Ruan orbifold cohomology for curves with bad reduction.

**What's known.** Mirror symmetry for elliptic curves is well-understood: $D^b(\operatorname{Coh}(E)) \simeq D^b(\operatorname{Fuk}(\check{E}))$ is established for abelian varieties (Polishchuk–Zaslow). The SYZ fibration for elliptic curves is simply the dual fibration. Regulators from algebraic K-theory to Deligne cohomology are known to detect L-values (Beilinson's conjectures). However, no direct bridge from Floer-theoretic data to arithmetic L-values has been constructed.

**Main obstacle.** The Fukaya category over $\mathbb{C}$ is inherently a complex-geometric object, while BSD is arithmetic. The passage from $\mathbb{C}$-valued Floer invariants to $p$-adic or motivic information required for L-functions is not understood. There is no known mechanism to extract rank or Tate–Shafarevich group data from Lagrangian intersection Floer homology.

**BSD connection.** If Lagrangian correspondences between an elliptic curve and its mirror could be shown to generate the relevant motivic cohomology classes, mirror symmetry would provide a geometric construction of the regulator map, potentially yielding new proofs of rank bounds or formulas for the leading Taylor coefficient.

**Status.** Speculative; no concrete computational evidence connecting Floer data to L-values.

**Classification.** Speculative/Bridge

---

## J-002: Perfectoid Spaces and p-adic Hodge Theory for BSD

**Statement.** Develop the perfectoid approach to the $p$-adic BSD conjecture by establishing comparison isomorphisms between the Selmer group $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ and perfectoid cohomology groups of the tower of modular curves parametrizing $p$-power isogenies of $E$. Specifically, construct a perfectoid space $X_{p^\infty}$ over $\mathbb{Q}_p$ such that $H^1_{\mathrm{\acute{e}t}}(X_{p^\infty}, \mathbb{Z}_p(1))^{\Gamma}$ recovers $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ and study its relation to $p$-adic L-functions via the perfectoid Igusa tower.

**Tools needed.** Scholze's theory of perfectoid spaces, $p$-adic Hodge theory (Fontaine, Faltings, Scholze), the pro-étale topology, adic spaces (Huber), Emerton's completed cohomology, Hida theory and eigencurve geometry, $p$-adic Langlands for $\operatorname{GL}_2(\mathbb{Q}_p)$.

**What's known.** Perfectoid spaces have yielded breakthroughs in weight-monodromy (Scholze), Shimura varieties (Scholze–Weinstein), and the Langlands program (Fargues–Scholze). Completed cohomology of modular towers (Emerton) gives a perfectoid framework for Iwasawa theory. The Iwasawa main conjecture for modular forms is known (Wiles, Skinner–Urban). Besser's $p$-adic regulators and Coleman integration give $p$-adic Abel–Jacobi maps.

**Main obstacle.** The direct link between perfectoid cohomology of the infinite-level tower and the analytic rank is not established. The perfectoid Igusa tower encodes Galois representations but not obviously the Selmer group in a form amenable to rank computation. The local-global compatibility at supersingular primes and the behavior of $\Sigma$-Selmer groups in the perfectoid setting remain difficult.

**BSD connection.** A perfectoid construction of the Selmer group would provide a natural $p$-adic interpolation for the analytic rank, connecting directly to the $p$-adic BSD conjecture of Perrin-Riou and Mazur–Tate–Teitelbaum. This could establish $p$-adic BSD under weaker hypotheses than the classical conjecture.

**Status.** Active area; partial results exist via completed cohomology and eigencurves.

**Classification.** Active Research

---

## J-003: Categorification of the BSD Conjecture

**Statement.** Formulate a categorified version of BSD in which the Selmer group $\operatorname{Sel}(E/K)$ is replaced by a derived category $\mathcal{D}_{\mathrm{Sel}}(E/K)$ and the order of vanishing of $L(E, s)$ at $s=1$ is replaced by a categorical invariant (e.g., the Euler characteristic in a suitable Grothendieck group $K_0$). The categorified BSD conjecture would assert an equivalence of stable $\infty$-categories between the category of Selmer structures on $E$ and a category of motivic sheaves whose decategorification recovers the classical rank and leading coefficient.

**Tools needed.** Derived algebraic geometry (Lurie, Toën–Vezzosi), stable $\infty$-categories, motivic homotopy theory (Morel–Voevodsky), differential graded categories, Tamarkin's symplectic field theory as a model for categorification, higher algebraic K-theory, condensed mathematics (Clausen–Scholze).

**What's known.** Categorification has been powerful in topology (Khovanov homology categorifying the Jones polynomial) and representation theory (Kazhdan–Lusztig categorified). The motivic category $\mathbf{DM}(k)$ provides a natural home for categorical L-functions (Voevodsky). Jacob Lurie's work on higher algebra provides the $\infty$-categorical infrastructure. Galois cohomology has been studied in derived settings (Schnürer), but no categorification of Selmer groups exists.

**Main obstacle.** The Selmer group is a finite-dimensional vector space; categorifying it requires finding hidden homological structure that collapses to the classical invariant upon taking $K_0$. There is no known extra structure on $\operatorname{Sel}(E/K)$ beyond its group-theoretic one. The analytic rank side—categorifying the Taylor expansion of $L(E,s)$—is even less clear, as L-values have no known homological origin.

**BSD connection.** A categorified BSD would be strictly stronger than the classical conjecture: it would predict not just the rank and leading coefficient, but an equivalence of categories from which all arithmetic invariants of $E$ could be extracted. This could unify the various avatars of BSD ($p$-adic, equivariant, global) under a single framework.

**Status.** Conceptual; no formal formulation exists.

**Classification.** Speculative/Conceptual

---

## J-004: Kudla Program: Arithmetic Siegel–Weil Formula

**Statement.** Apply the arithmetic Siegel–Weil formula of Kudla, Kudla–Rapoport, and Kudla–Yang to express the central derivative $L'(E, 1)$ as an arithmetic intersection number on an integral model of a Shimura variety associated to $\operatorname{GU}(1,1)$. Concretely, for a Shimura curve $X$ parametrizing abelian surfaces with quaternionic multiplication, show that the arithmetic degree of the special cycle $\mathcal{Z}(m)$—the locus of CM points weighted by $m$—computes the $m$-th Fourier coefficient of the incoherent Eisenstein series, and that the generating series of these arithmetic degrees is a modular form whose central value is $L'(E, 1)$.

**Tools needed.** Arithmetic intersection theory (Gillet–Soulé, Kudla–Rapoport), Shimura varieties of orthogonal and unitary type, Eisenstein series and their Fourier coefficients, arithmetic geometry of integral models of Shimura varieties (Kisin, Pappas), metaplectic covers and Weil representations, local intersection formulas (Kudla–Rapoport–Yang, Liu), Borcherds products.

**What's known.** The Kudla program has been established in many cases: Kudla–Rapoport proved the arithmetic Siegel–Weil formula for unitary Shimura varieties (unramified case), Liu proved the local arithmetic Siegel–Weil formula, and Ichino–Ikeda and Kudla formulated global conjectures. Gross–Zagier's original theorem is a special case. Yuan–Zhang proved the averaged form of the arithmetic Gross–Zagier formula. Howard's work on CM cycles on Shimura curves connects to Heegner points.

**Main obstacle.** The full arithmetic Siegel–Weil formula for $\operatorname{GU}(1,1)$—the case directly relevant to elliptic curves of rank 1—remains open in the ramified case. The local intersection multiplicities at primes of bad reduction require delicate analysis of Rapoport–Zink spaces and integral models with parahoric level. The incoherent Eisenstein series associated to the quadratic space must be shown to match the generating series of arithmetic intersection numbers globally, including archimedean contributions via the arithmetic degree of the hermitian line bundle.

**BSD connection.** The arithmetic Siegel–Weil formula gives a direct geometric interpretation of $L'(E,1)$ as an intersection number. Combined with the standard Heegner point construction (Gross–Zagier), this provides the rank 1 case of BSD. Extensions to higher rank via higher-dimensional special cycles (Kudla's higher arithmetic Siegel–Weil) could address $L^{(r)}(E,1)$.

**Status.** Active; major cases proven, ramified case open.

**Classification.** Active Research

---

## J-005: Machine Learning Patterns in LMFDB Rank Data

**Statement.** Apply machine learning techniques to the LMFDB database of elliptic curves over $\mathbb{Q}$ (currently >300 million curves) to discover statistical patterns, conjectural formulas, and classification features for analytic rank distributions. Specifically: (1) train neural networks to predict $\operatorname{ord}_{s=1} L(E,s)$ from conductor, Tamagawa numbers, torsion, and local root numbers; (2) use symbolic regression (e.g., PySR, Eureqa) to discover closed-form relationships between arithmetic invariants and rank distributions; (3) apply dimensionality reduction (t-SNE, UMAP) to the trace formula coefficients to identify geometric clusters in rank strata.

**Tools needed.** LMFDB API and database dumps, PyTorch/TensorFlow for neural network architectures, symbolic regression libraries (PySR, AI Feynman), scikit-learn for ensemble methods, formal verification tools (Lean 4) to validate conjectured formulas, statistical hypothesis testing framework.

**What's known.** Heuristics of Katz–Sarnak predict rank distribution should follow a random matrix model: 50% rank 0, 50% rank 1, with ranks $\geq 2$ having density 0 (under Parity Conjecture). The conjecture that 100% of curves have rank $\leq 1$ (i.e., no rank $\geq 2$ asymptotically) is equivalent to a positive proportion having rank 0 and a positive proportion having rank 1. Bhargava–Shankar proved average rank is bounded. Existing computational data shows rank 2 curves are common, rank 3 rare, rank $\geq 4$ very rare. No closed-form formula relating rank to conductor-level invariants is known.

**Main obstacle.** Machine learning can identify correlations but not causal mathematical structure. The risk of overfitting to finite data is high, especially for rank $\geq 3$ where examples are sparse. Any ML-discovered "pattern" must be rigorously proven; the gap between statistical correlation and theorem is vast. Feature engineering—choosing which arithmetic invariants to feed—is itself a mathematical decision that constrains discoverable patterns.

**BSD connection.** Direct: if ML could reliably predict rank from explicit arithmetic data, it would suggest new formulations of BSD-type statements. Discovering that rank is predictable from local data (root numbers, Tamagawa numbers, torsion) would strengthen the heuristic case that rank is determined by local-to-global principles. Symbolic regression could surface formulas for the regulator or $|\Sha|$ in terms of other invariants.

**Status.** Preliminary; exploratory work exists (He–Lee, LMFDB-based studies) but no published ML results on rank prediction.

**Classification.** Computational/Exploratory

---

## J-006: Non-abelian Iwasawa Theory for GL(2)

**Statement.** Develop a non-abelian Iwasawa theory for the adjoint representation $\operatorname{Ad}(\rho_E)$ of the Galois representation $\rho_E: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{Z}_p)$ attached to an elliptic curve $E/\mathbb{Q}$, and prove a non-abelian main conjecture relating the characteristic ideal of the non-abelian Selmer group to the $p$-adic L-function of the symmetric square $\operatorname{Sym}^2 E$. This should yield a formula for the $p$-adic valuation of $|\Sha(E/\mathbb{Q})|$ in terms of special values of $L(\operatorname{Sym}^2 E, s)$.

**Tools needed.** Non-commutative Iwasawa theory (Coates–Fukaya–Kato–Sujatha–Venjakob), Galois deformation rings and pseudorepresentations, Greenberg's Selmer groups for non-ordinary primes, equivariant Tamagawa number conjecture (Burns–Flach, Burns–Kurihara–Sano), Hida's ordinary Hecke algebra, $\Lambda$-adic modular forms, $p$-adic Hodge theory for crystalline representations.

**What's known.** The abelian Iwasawa main conjecture for elliptic curves is known in many cases (Skinner–Urban, Wan). Non-abelian Iwasawa theory was developed by Coates–Fukaya–Kato–Sujatha–Venjakob for $\operatorname{GL}_2$ over imaginary quadratic fields, establishing the main conjecture for the "big" Selmer group over the $\operatorname{GL}_2$-extension. The equivariant Tamagawa number conjecture (ETNC) of Burns–Flach is the most general framework but remains open for $\operatorname{GL}_2$ over $\mathbb{Q}$.

**Main obstacle.** The main conjecture for the non-abelian $\operatorname{GL}_2$-extension of $\mathbb{Q}$ is wide open: one must construct the non-commutative $p$-adic L-function (a measure on $\operatorname{GL}_2(\mathbb{Z}_p)$), define the non-abelian Selmer group with the correct local conditions, and prove the equality of characteristic ideals. The non-commutative Fitting invariant—the replacement for the characteristic ideal in non-commutative Iwasawa theory—requires the theory of $\mu$-invariants for non-commutative $p$-adic Lie extensions, which is not well-developed.

**BSD connection.** The non-abelian main conjecture would control the $p$-part of $|\Sha|$ at all primes simultaneously and in all layers of the $\operatorname{GL}_2$-extension. Taking the limit and specializing to the trivial extension recovers the $p$-part of the classical Birch–Swinnerton-Dyer formula. The non-abelian structure captures the full symmetry of the problem, potentially yielding the exact $p$-adic valuation of $|\Sha|$ without assuming the $p$-part is trivial.

**Status.** Active research; main conjecture open for $\operatorname{GL}_2/\mathbb{Q}$.

**Classification.** Active Research

---

## J-007: Anabelian Geometry and BSD

**Statement.** Investigate whether the anabelian geometry of Grothendieck and Mochizuki—specifically the reconstruction of schemes from their étale fundamental groups—can be applied to the arithmetic of elliptic curves to extract BSD data. Precisely: determine whether the isomorphism class of the pro-$\ell$ étale fundamental group $\pi_1^{\mathrm{\acute{e}t}}(E_{\overline{\mathbb{Q}}}, \bar{b})$ and its outer Galois action, together with the geometry of the moduli of torsors under $E$, completely determines the Selmer group $\operatorname{Sel}(E/\mathbb{Q})$ and hence the rank.

**Tools needed.** Grothendieck's anabelian geometry (reconstruction theorems for hyperbolic curves), Mochizuki's inter-universal Teichmüller theory (IUT), étale fundamental groups and their Galois actions, the Section Conjecture of Grothendieck, birational anabelian geometry (Pop, Koenigsmann), non-abelian cohomology, anabelian lift of Chabauty–Kim method.

**What's known.** Grothendieck proved that hyperbolic curves over number fields are anabelian: they are determined by their étale fundamental group (with outer Galois action). Mochizuki's IUT claims bounds on Diophantine properties via the reconstruction of arithmetic schemes from fundamental groups. The Section Conjecture (for curves over number fields: sections of $\pi_1(X) \to G_\mathbb{Q}$ correspond to rational points) remains open but has been tested computationally. Kim's non-abelian Chabauty method uses quotients of $\pi_1$ to bound rational points on curves, with significant successes for curves of genus $\geq 2$.

**Main obstacle.** Anabelian geometry reconstructs the scheme, not its arithmetic properties like rank. There is no known mechanism to pass from the reconstructed scheme $E$ (or its fundamental group) to the Selmer group. The Section Conjecture, if true, would relate rational points to sections of the fundamental group exact sequence, but this addresses rational points, not the rank of $E$ (which is about rational points on the principal homogeneous space). The Selmer group parametrizes torsors, and while these are geometric objects, their relationship to the fundamental group is indirect.

**BSD connection.** If anabelian reconstruction could be made arithmetic—i.e., if the Selmer group could be read off from the outer Galois action on $\pi_1$—this would give a radically new approach to rank computation. The fundamental group already encodes the Tate module $T_\ell(E)$; the question is whether it encodes the full Selmer structure.

**Status.** Speculative; no concrete pathway from anabelian data to Selmer groups.

**Classification.** Speculative

---

## J-008: Arithmetic Topology: Knots and Elliptic Curves

**Statement.** Exploit the arithmetic topology dictionary—primes as knots, rings of integers as 3-manifolds, the analogy between $\operatorname{Spec}(\mathbb{Z})$ and $S^3$—to transfer techniques from 3-manifold topology (Thurston norm, Turaev torsion, Reidemeister torsion) to the study of Selmer groups and regulators of elliptic curves. Specifically: define a "Thurston norm" on $H^2(\operatorname{Spec}(\mathcal{O}_{E,\Sigma}), \partial)$ that bounds the rank of $E$ and show this bound is sharp.

**Tools needed.** Arithmetic topology (Mazur, Morishita), Alexander polynomial and its arithmetic analogs, Milnor torsion and its $\mathbb{Z}_p$-version (Iwasawa–Milnor $\mu$-invariant), Dehn surgery and $p$-descent, Thurston norm on 3-manifolds, knot concordance and Selmer group structure, Chern–Simons theory for number fields (unramified extensions as flat connections).

**What's known.** The analogy between primes and knots is classical (Mazur): linking numbers match Legendre symbols, Alexander polynomials correspond to cyclotomic polynomials, and Milnor $\mu$-invariants match Iwasawa $\mu$-invariants. Kapranov–Reznikov and Morishita have developed this extensively. The analog of the Thurston norm for number fields has been partially explored (Kurihara, Hiranouchi). Reznikov has studied Selmer groups via the lens of knot theory.

**Main obstacle.** The arithmetic topology dictionary is primarily combinatorial/homological and does not yet capture analytic objects like L-functions. The Thurston norm in 3-manifold topology uses $L^2$-Betti numbers and the LHS of the $L^2$-signature theorem; finding the arithmetic analog requires an "$L^2$-invariant" of $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$. The dictionary breaks down for higher-dimensional arithmetic schemes and does not naturally incorporate the analytic continuation of L-functions.

**BSD connection.** If the arithmetic Thurston norm on the Selmer complex equals $\operatorname{ord}_{s=1} L(E,s)$, this would give a topological proof of rank bounds. The Turaev torsion of the "arithmetic 3-manifold" $\operatorname{Spec}(\mathcal{O}_{E,\Sigma})$ could serve as the arithmetic regulator, matching the leading L-value coefficient to a Reidemeister-type torsion (as in the Cheeger–Müller theorem).

**Status.** Exploratory; the dictionary is developing but lacks application to BSD.

**Classification.** Exploratory/Bridge

---

## J-009: Derived Algebraic Geometry Approaches to Selmer Groups

**Statement.** Construct the Selmer group $\operatorname{Sel}(E/K)$ as the global sections $\mathbb{H}^0(K, \mathcal{S}\!\mathit{el}_E)$ of a sheaf $\mathcal{S}\!\mathit{el}_E$ on a derived site $\mathcal{X}_E = \operatorname{Spec}(K)^{\mathrm{der}}$ whose higher cohomology groups $\mathbb{H}^i(K, \mathcal{S}\!\mathit{el}_E)$ for $i > 0$ encode the obstruction to the vanishing of $\Sha(E/K)$ and whose Euler characteristic computes the order of vanishing of $L(E, s)$ at $s = 1$.

**Tools needed.** Derived algebraic geometry (Toën–Vezzosi, Lurie), simplicial presheaves and model topoi, cotangent complexes and their cohomology, derived de Rham cohomology, derived Selmer groups (analogous to derived functors of limit), condensed mathematics (Clausen–Scholze) for archimedean aspects.

**What's known.** Derived algebraic geometry has been applied to intersection theory (virtual fundamental classes), deformation theory (via cotangent complex), and motivic homotopy theory. The Selmer group naturally arises as an Ext group: $\operatorname{Sel}(E/K) \subset \operatorname{Ext}^1_{G_K}(1, E[p^n])$ for varying $n$. Derived completions (Lurie) provide a natural framework for $p$-adic Selmer groups. The "derived curve" $E^{\mathrm{der}}$ associated to the moduli of $E$-torsors has not been studied.

**Main obstacle.** Converting the derived Selmer complex into a single sheaf on a derived site requires choosing a site structure that captures both the Galois cohomological input and the local conditions defining Selmer groups. The higher cohomology groups $\mathbb{H}^i$ for $i > 0$ should relate to $H^i(G_K, E[n])$ and higher Massey products, but extracting $|\Sha|$ from these is not straightforward. The Euler characteristic of a derived Selmer complex on a non-proper site does not obviously equal the analytic rank.

**BSD connection.** The derived framework would make the Selmer group into a derived invariant with higher cohomological structure. If the Euler characteristic of this derived Selmer complex equals the analytic rank (a derived analog of the Nekovář–Niziol Euler characteristic formula), and if the higher terms control $|\Sha|$, this would give a unified derived formulation of BSD.

**Status.** Conceptual; no published derived Selmer construction exists.

**Classification.** Conceptual

---

## J-010: Quantum Invariants and Arithmetic

**Statement.** Explore the conjectural relationship between quantum group invariants of knots (Jones polynomial, HOMFLY-PT, colored Jones) and arithmetic L-functions, with the aim of applying quantum-topological techniques to study the order of vanishing and special values of $L(E, s)$. Specifically, investigate whether the quantum dilogarithm and its arithmetic realizations (as $p$-adic Gamma functions) can serve as a bridge between the Reshetikhin–Turaev invariant of an arithmetic 3-manifold and the $p$-adic L-function of $E$.

**Tools needed.** Quantum groups (Drinfeld, Jimbo), Reshetikhin–Turaev TQFT, Chern–Simons theory, quantum dilogarithm (Faddeev–Kashaev, Zagier), colored Jones polynomial and the Volume Conjecture (Kashaev, Murakami–Murakami), $p$-adic Gamma functions (Morita, Diamond), Bost–Connes systems, arithmetic quantum field theory.

**What's known.** The Volume Conjecture relates the asymptotic growth of the colored Jones polynomial of a knot to the hyperbolic volume of its complement. Quantum dilogarithms appear in both quantum topology (as R-matrix entries) and number theory (as $p$-adic special functions, polylogarithms). Zagier's work connects quantum dilogarithms to the Bloch group and regulator maps. The Bost–Connes system connects quantum statistical mechanics to class field theory. Kontsevich and Manin related Gromov–Witten invariants (closely related to quantum invariants) to motivic L-functions.

**Main obstacle.** The Volume Conjecture is proven only for very few knots, and the connection to number theory is entirely conjectural. The quantum invariants of the "arithmetic knot" associated to an elliptic curve (via the arithmetic topology dictionary) have not been computed. The passage from the analytic continuation of quantum invariants to the analytic continuation of L-functions requires a quantization of the number field, which is not understood.

**BSD connection.** If the Reshetikhin–Turaev invariant of the arithmetic 3-manifold $\operatorname{Spec}(\mathcal{O}_K) \setminus V(\mathfrak{p})$ (treating a prime as a knot complement) could be related to the local L-factor of $E$ at $\mathfrak{p}$, then the global RT invariant would be the L-function. The quantum dilogarithm would then play the role of the $p$-adic L-function, and the Volume Conjecture would be an arithmetic-geometric statement about BSD.

**Status.** Highly speculative; no concrete computation relating quantum invariants to L-values of elliptic curves.

**Classification.** Speculative/Bridge

---

## J-011: Higher Category Theory and Motives for Elliptic Curves

**Statement.** Construct an explicit $\mathbb{E}_\infty$-algebra of motivic cohomology $\mathcal{M}\!\mathit{ot}(E)$ in the $\infty$-category of motivic spectra $\mathbf{SH}(k)$ for an elliptic curve $E/\mathbb{Q}$, and prove that the motivic spectral sequence converging to the stable homotopy groups of the motivic spectrum $\mathrm{MGL} \wedge \Sigma^\infty_+ E$ degenerates at the $E_2$-page in a range determined by the rank. The goal is a motivic proof of rank bounds from the structure of $\mathcal{M}\!\mathit{ot}(E)$ as an $\mathbb{E}_\infty$-ring object.

**Tools needed.** Motivic homotopy theory (Morel–Voevodsky), stable motivic homotopy category $\mathbf{SH}(k)$, motivic spectra and Thom spectra ($\mathrm{MGL}$), $\mathbb{E}_\infty$-ring spectra in motivic homotopy (Röndigs–Østvær), motivic Adams spectral sequence, algebraic cobordism (Levine–Morel), slice filtration (Voevodsky, Pelaez), motivic cohomology operations, Beilinson motives ($\mathbf{DA}(k, \mathbb{Q})$).

**What's known.** The motivic category $\mathbf{SH}(k)$ is well-developed: $\mathrm{MGL}$ is the motivic Thom spectrum, and its coefficient ring is algebraic cobordism $\Omega_*(k)$. The motivic Adams spectral sequence converges to stable homotopy groups of motivic spectra. Röndigs–Østvær computed the first motivic stable stems. The derived category of motives $\mathbf{DA}(k, \mathbb{Q})$ contains the motive $h(E)$ of an elliptic curve, and its cohomology reproduces étale, de Rham, and Betti cohomology via realization functors. The Chow motive of $E$ decomposes as $\mathbb{1} \oplus h^1(E) \oplus \mathbb{L}$.

**Main obstacle.** The motivic spectral sequence is extremely difficult to compute beyond low degrees. The interaction between the multiplicative structure on $\mathrm{MGL}$ and the motivic cohomology of elliptic curves is not well-understood. There is no known mechanism by which the rank of $E$ controls the differentials in the motivic Adams spectral sequence. The passage from the motivic world (where $\mathrm{Hom}$-groups compute Chow groups, K-theory, etc.) to the analytic world (L-values) goes through regulator maps, and these are not captured by the $\mathbb{E}_\infty$-structure alone.

**BSD connection.** The motivic spectral sequence, if it degenerates in a rank-dependent way, would provide a homotopy-theoretic formulation of rank bounds. The $\mathbb{E}_\infty$-ring structure on $\mathcal{M}\!\mathit{ot}(E)$ encodes cup products and Massey products in motivic cohomology, which are related to higher regulators and hence to leading L-values. An $\mathbb{E}_\infty$ proof of rank bounds would be purely algebraic-topological and independent of analytic methods.

**Status.** Speculative; motivic homotopy theory is well-developed but its application to BSD is not.

**Classification.** Speculative/Homotopy-Theoretic

---

## J-012: Topological Modular Forms and Their L-functions

**Statement.** Investigate the L-function associated to the topological modular forms spectrum $\mathrm{tmf}$ and its relationship to classical modular forms and elliptic curves. Specifically: (1) define an L-function $L(\mathrm{tmf}, s)$ via the Adams–Novikov spectral sequence or the string orientation $\mathrm{MString} \to \mathrm{tmf}$; (2) show that for the elliptic curve $E$ corresponding to a modular form $f$, the L-function of $\mathrm{tmf}$ evaluated at the $E$-localization recovers $L(f, s)$; (3) use the chromatic filtration of $\mathrm{tmf}$ to construct a "chromatic BSD" relating the $\mathbb{F}_2$-rank of $\pi_*(\mathrm{L}_{K(2)} \mathrm{tmf})$ to arithmetic invariants of $E[2]$.

**Tools needed.** Topological modular forms (Hopkins–Mahowald, Behrens, Lawson), spectral algebraic geometry (Lurie), the moduli stack of elliptic curves $\mathcal{M}_{1,1}$ over $\mathbb{Z}$, sheaves of $\mathbb{E}_\infty$-ring spectra on $\mathcal{M}_{1,1}$, the Adams–Novikov spectral sequence, chromatic homotopy theory (Ravenel, Hopkins–Ravenel), the string orientation $\sigma: \mathrm{MString} \to \mathrm{tmf}$, Witten genus, equivariant elliptic cohomology.

**What's known.** $\mathrm{tmf}$ is a global section of a sheaf of $\mathbb{E}_\infty$-ring spectra on the moduli stack $\mathcal{M}_{1,1}$ (Goerss–Hopkins–Lurie). The coefficient ring $\pi_*(\mathrm{tmf})$ is known and connects to modular forms: the classical ring of modular forms embeds into $\pi_*(\mathrm{tmf})$ via the Witten genus. Chromatic localizations $\mathrm{L}_{K(n)} \mathrm{tmf}$ have been computed (Behrens, Meier). The connection between $\mathrm{tmf}$ and elliptic curves is structural: sections of the structure sheaf of $\mathcal{M}_{1,1}$ over Spec$(\mathbb{Z})$.

**Main obstacle.** The L-function of a spectrum like $\mathrm{tmf}$ is not defined in the classical sense. One must construct a zeta function for $\mathbb{E}_\infty$-ring spectra, likely via the trace map to topological Hochberg homology ($\mathrm{THH}$) and the Dennis trace to Hochschild homology. The Adams–Novikov spectral sequence converges to stable homotopy groups, not to L-values. The Witten genus connects $\mathrm{tmf}$ to modular forms but only at the level of generating functions (partitions), not at the level of L-functions. The chromatic filtration refines the structure but at height 2 and above, the arithmetic is of abelian surfaces, not elliptic curves.

**BSD connection.** If the L-function of $\mathrm{tmf}$ exists and recovers classical L-functions of modular forms (and hence elliptic curves via modularity), then chromatic homotopy theory provides a filtration of the L-function by height. The height 1 piece (classical modular forms) gives $L(E, s)$. The chromatic spectral sequence could organize the vanishing order of $L(E, s)$ in terms of the chromatic complexity of $\mathrm{tmf} \wedge \Sigma^\infty_+ E$. The string orientation could transfer BSD-relevant information from MString (which detects $\operatorname{Spin}$ bordism, related to index theory) to $\mathrm{tmf}$.

**Status.** Speculative; $\mathrm{tmf}$ is well-studied topologically but its arithmetic L-function is not defined.

**Classification.** Speculative/Topological

---
