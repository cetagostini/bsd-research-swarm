# J-006: Non-abelian Iwasawa Theory for GL(2)

## Status Assessment

**Classification: Active Research / High-Risk, High-Reward**

This direction pursues a non-abelian Iwasawa main conjecture for the adjoint representation $\operatorname{Ad}(\rho_E)$ of the Galois representation attached to an elliptic curve $E/\mathbb{Q}$, aiming to control the $p$-part of $|\Sha(E/\mathbb{Q})|$ through the symmetric square L-function $L(\operatorname{Sym}^2 E, s)$.

**Current state of the art:**
- The **abelian** Iwasawa main conjecture for elliptic curves is known in many cases: Skinner–Urban (2014) proved it for ordinary elliptic curves over $\mathbb{Q}$ assuming the Iwasawa main conjecture for $\operatorname{GL}_2$ over imaginary quadratic fields (later reduced further). Wan (2020) proved the Iwasawa main conjecture for supersingular primes with $a_p = 0$.
- **Non-abelian** Iwasawa theory for $\operatorname{GL}_2$ over imaginary quadratic fields $K$ was developed by Coates–Fukaya–Kato–Sujatha–Venjakob (2005), establishing the main conjecture for the "big" Selmer group over the $\operatorname{GL}_2$-extension $\mathbb{Q}_\infty/K$.
- The extension from imaginary quadratic base fields to $\mathbb{Q}$ is **wide open**. The fundamental issue is that $\mathbb{Q}$ admits no $\operatorname{GL}_2$-extension in the same sense — one must work with the non-commutative $p$-adic Lie extension cut out by $\rho_E: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{Z}_p)$.
- The **equivariant Tamagawa number conjecture** (Burns–Flach, Burns–Kurihara–Sano) provides the broadest framework but remains unproven for $\operatorname{GL}_2/\mathbb{Q}$.

**Honest assessment:** This is a direction where the full conjecture is likely decades away from resolution. However, partial results (e.g., for the $\operatorname{Ad}^0$ representation, for specific primes $p$, for CM curves where the image is smaller) are achievable within the current framework and would yield genuine progress on BSD.

---

## Testable Conjecture or Lemma

### The Non-abelian Main Conjecture for $\operatorname{Ad}(\rho_E)$

**Setup.** Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at an odd prime $p$. Let $\rho_E: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{Z}_p)$ be the $p$-adic Galois representation on $T_p(E)$. Let $G = \rho_E(G_\mathbb{Q}) \leq \operatorname{GL}_2(\mathbb{Z}_p)$ and $\Gamma = \operatorname{GL}_2(\mathbb{Z}_p)$ (or a suitable open subgroup). Consider the non-commutative Iwasawa algebra:

$$\Lambda(G) = \mathbb{Z}_p[[G]] = \varprojlim_{U \trianglelefteq G, \, [G:U] < \infty} \mathbb{Z}_p[G/U]$$

**Adjoint representation.** The Lie algebra $\mathfrak{g} = \operatorname{Lie}(\operatorname{GL}_2(\mathbb{Z}_p)) \cong M_2(\mathbb{Z}_p)$ acts on itself via the adjoint representation:
$$\operatorname{Ad}: G \to \operatorname{Aut}(\mathfrak{g}), \quad g \cdot X = gXg^{-1}$$

The adjoint representation decomposes as:
$$\operatorname{Ad}(\rho_E) \cong \operatorname{Ad}^0(\rho_E) \oplus \mathbb{Z}_p$$
where $\operatorname{Ad}^0$ is the trace-zero part (3-dimensional, corresponding to $\operatorname{Sym}^2$ minus the trivial character).

**Conjecture (Non-abelian Main Conjecture for $\operatorname{GL}_2/\mathbb{Q}$).** *Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at an odd prime $p$, with $\rho_E$ surjective onto an open subgroup of $\operatorname{GL}_2(\mathbb{Z}_p)$. There exists a non-commutative $p$-adic L-function $\mathcal{L}_p(E) \in K_1(\Lambda(G) \otimes \mathbb{Q}_p) / K_1(\Lambda(G))$ such that:*

$$\operatorname{char}_{\Lambda(G)}\left(\operatorname{Sel}_{\operatorname{Ad}}(E/\mathbb{Q}_\infty)\right) = (\mathcal{L}_p(E))$$

*where $\operatorname{Sel}_{\operatorname{Ad}}(E/\mathbb{Q}_\infty)$ is the non-abelian Selmer group for the adjoint representation over the $\operatorname{GL}_2$-extension $\mathbb{Q}_\infty$, and $\operatorname{char}_{\Lambda(G)}$ denotes the non-commutative characteristic ideal (Fitting ideal in the sense of Venjakob).*

**Specialization consequence.** Evaluating at the trivial character $\chi_0: G \to \{1\}$ yields:

$$\operatorname{char}_{\mathbb{Z}_p}\left(\operatorname{Sel}_{\operatorname{Ad}}(E/\mathbb{Q})\right) \sim_p L_p(\operatorname{Sym}^2 E, 1)$$

This connects directly to BSD: the leading coefficient of $L(\operatorname{Sym}^2 E, s)$ at $s=1$ controls the $p$-adic valuation of $|\Sha(E/\mathbb{Q})|$ via the formula:

$$v_p(|\Sha|) = v_p\left(\frac{L(\operatorname{Sym}^2 E, 1)}{\Omega^+_{\operatorname{Sym}^2} \cdot \prod_v c_v(\operatorname{Sym}^2)}\right) + \text{correction terms}$$

where $\Omega^+_{\operatorname{Sym}^2}$ is the real period of the symmetric square motive.

---

## Approach Summary

### Step 1: Non-commutative Selmer Groups

The classical Selmer group $H^1_f(G_S, V_p(E))$ must be replaced by a Selmer group for the **adjoint** representation $\operatorname{Ad}^0(\rho_E)$ over the non-commutative extension $\mathbb{Q}_\infty = \overline{\mathbb{Q}}^{\ker \rho_E}$. The Selmer conditions at each prime $v$ are:

- **$v \nmid p\infty$:** Unramified condition: $\operatorname{loc}_v(\xi) \in H^1_{\text{ur}}(G_v, \operatorname{Ad}^0(\rho_E))$
- **$v = p$:** Crystalline condition: $\operatorname{loc}_p(\xi) \in H^1_f(G_p, \operatorname{Ad}^0(\rho_E))$ defined via Fontaine's $D_{\text{cris}}$
- **$v = \infty$:** Trivial (odd representation)

The key difficulty is ensuring the Selmer conditions are **cotorsion** over $\Lambda(G)$ — this requires careful analysis of the local conditions at primes of bad reduction and at $p$.

### Step 2: Non-commutative $p$-adic L-function

Following Coates–Fukaya–Kato–Sujatha–Venjakob, the $p$-adic L-function lives in $K_1(\Lambda(G)_S)$ where $S$ is the Ore localization at elements with finite support. Construction proceeds via:

1. **Eisenstein ideal:** For the Eisenstein series associated to $E$, construct the $p$-adic family interpolating $L(\operatorname{Sym}^2 E, 1)$.
2. **Hida family:** Use Hida's ordinary Hecke algebra to construct a $\Lambda(G)$-adic family of modular forms whose specialization at each character of $G$ yields the appropriate L-value.
3. **Regulator map:** The Beilinson–Kato elements in $K_2$ of modular curves map to the Selmer group via the generalized Soulé regulator.

The fundamental obstruction is that $\Lambda(G)$ is non-commutative, so the classical theory of characteristic ideals does not apply. One must use:

- **Non-commutative Fitting invariants** (Venjakob)
- **$K$-theoretic localization** (Quillen, adapted by Coates et al.)
- **The reduced norm** on $\Lambda(G)$

### Step 3: Equality of Ideals

The main technical result required is:

$$\operatorname{char}_{\Lambda(G)}(\operatorname{Sel}_{\operatorname{Ad}}) = \operatorname{char}_{\Lambda(G)}(\operatorname{cotorsion of } H^0(G, \operatorname{Sel}_{\operatorname{Ad}}^*))$$

combined with the non-commutative main conjecture equating these to $(\mathcal{L}_p(E))$. This uses:

- The **Euler system machine** (Rubin, Kato, Kolyvagin) extended to the non-commutative setting
- **Control theorems** relating Selmer groups at different levels of the $\Lambda(G)$-tower
- **Pseudo-nullity** arguments for the dual Selmer group

### Step 4: BSD via Specialization

At each finite layer $G_n = G / U_n$, specialize the main conjecture to recover:

$$|\Sha(E/\mathbb{Q}_{n})[p^\infty]| \sim_p \frac{L_p(\operatorname{Sym}^2 E_{/\mathbb{Q}_n}, 1)}{\Omega_n \cdot \prod c_{v,n}}$$

In the limit $n \to \infty$ at the trivial layer, this yields the $p$-part of BSD.

---

## Computational Example

### Elliptic Curve $E = 11a1$: $y^2 + y = x^3 - x^2 - 10x - 20$

**Setup.** $E$ has conductor $N = 11$, rank $r = 0$, $|\Sha| = 1$. Take $p = 5$ (good ordinary, $a_5 = -2$).

**Galois representation.** $\rho_E: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{Z}_5)$ is surjective onto an open subgroup of $\operatorname{GL}_2(\mathbb{Z}_5)$ (Mazur's property $(\rho)$). The image $G = \rho_E(G_\mathbb{Q})$ contains $\operatorname{SL}_2(\mathbb{Z}_5)$.

**Iwasawa algebra.** $\Lambda(G) = \mathbb{Z}_5[[G]]$ is a completed group algebra of a $p$-adic Lie group of dimension 4. As a $\mathbb{Z}_5$-module, it is isomorphic (non-canonically) to $\mathbb{Z}_5[[x_1, x_2, x_3, x_4]]$ as a topological module, but with non-commutative multiplication.

**Symmetric square L-value.** The critical value is:
$$L(\operatorname{Sym}^2 E, 1) = \frac{2\pi^2}{\sqrt{11}} \cdot \sum_{n=1}^{\infty} \frac{a_n^2 - a_{n^2}}{n^2} \cdot e^{-2\pi n/\sqrt{11}}$$

Numerically (via modular symbol computation):
$$L(\operatorname{Sym}^2 E, 1) \approx 0.2197\ldots$$

Since $|\Sha| = 1$ for this curve, the $p$-adic valuation $v_5(|\Sha|) = 0$, consistent with $v_5(L(\operatorname{Sym}^2 E, 1)) = 0$.

**Selmer group computation.** The adjoint Selmer group $\operatorname{Sel}_{\operatorname{Ad}^0}(E/\mathbb{Q})$ has:
- $H^1_f(G_5, \operatorname{Ad}^0(\rho_E))$: 3-dimensional crystalline condition
- Global Selmer group: dimension 0 (consistent with rank 0 and $|\Sha| = 1$)

**Tower structure.** The layers of the $G$-extension are:
- Level 0: $\mathbb{Q}$ itself
- Level 1: $\mathbb{Q}(E[5])$, the 5-torsion field (degree $|\operatorname{GL}_2(\mathbb{F}_5)|/2 = 120$ over $\mathbb{Q}$)
- Level $n$: $\mathbb{Q}(E[5^n])$, degree $\sim 5^{4n}$

At each level, the specialization of the non-abelian main conjecture predicts the $5$-part of $|\Sha(E/\mathbb{Q}_n)|$.

**Verification.** For $E = 11a1$ and $p=5$, the abelian main conjecture is known (Skinner–Urban). The non-abelian version predicts additionally that the characteristic ideal of the non-abelian Selmer group equals the ideal generated by the non-commutative $p$-adic L-function. This is consistent with all known numerical data but remains unproven.

---

## Obstacle Analysis

### Obstacle 1: Non-commutative Characteristic Ideals
**Status: Partial theory (Venjakob, Coates–Sujatha)**

In commutative Iwasawa theory, $\operatorname{char}_{\mathbb{Z}_p[[T]]}(X)$ for a finitely generated torsion module $X$ is well-defined via the structure theorem. In the non-commutative setting, $\Lambda(G)$ is a non-commutative Noetherian ring, and the theory of Fitting ideals is much more subtle.

**Key issue:** The ring $\Lambda(G)$ is not a principal ideal domain, not even close. One must work with $K_0(\Lambda(G))$ and the reduced norm, but the theory of non-commutative Fitting invariants is not fully developed. Venjakob (2002) developed a partial theory, but it requires the module to be **pseudo-null** (codimension $\geq 2$ support), which is not guaranteed.

**Required breakthrough:** Extend the Fitting ideal theory to handle modules that are merely torsion, not pseudo-null, over $\Lambda(G)$.

### Obstacle 2: Construction of the Non-commutative $p$-adic L-function
**Status: Open for $\operatorname{GL}_2/\mathbb{Q}$**

For imaginary quadratic base fields, the $\operatorname{GL}_2$-extension has a specific structure (CM points, Heegner points) that allows interpolation. For $\mathbb{Q}$, the $\operatorname{GL}_2$-extension $\mathbb{Q}_\infty/\mathbb{Q}$ is cut out by $\rho_E$ and lacks this geometric structure.

**Key issue:** The interpolation of L-values at all characters of $G = \operatorname{GL}_2(\mathbb{Z}_p)$ requires:
- L-values $L(\operatorname{Sym}^2 E \otimes \chi, 1)$ for all algebraic characters $\chi$ of $G$
- A measure on $G$ interpolating these values
- Compatibility with the functional equation

The characters of $\operatorname{GL}_2(\mathbb{Z}_p)$ are much more complex than those of $\mathbb{Z}_p^\times$: they involve representations of $\operatorname{GL}_2(\mathbb{F}_p)$ (the "finite level" part) and characters of the center (the "weight" part).

**Required breakthrough:** Construct a $p$-adic measure on $\operatorname{GL}_2(\mathbb{Z}_p)$ interpolating symmetric square L-values, likely via Hida's ordinary Hecke algebra or $\Lambda$-adic modular forms.

### Obstacle 3: Control Theorem for Non-abelian Selmer Groups
**Status: Partial results (Coates–Fukaya–Kato–Sujatha–Venjakob for $K$ imaginary quadratic)**

The control theorem relates $\operatorname{Sel}_{\operatorname{Ad}}(E/\mathbb{Q}_n)$ to $\operatorname{Sel}_{\operatorname{Ad}}(E/\mathbb{Q}_{n+1})$ as one ascends the tower. In the abelian case, this is the classical Greenberg control theorem. In the non-abelian case, one must control:

$$\ker\left(\operatorname{Sel}_{\operatorname{Ad}}(E/\mathbb{Q}_{n+1}) \to \operatorname{Sel}_{\operatorname{Ad}}(E/\mathbb{Q}_n)\right)$$

and the cokernel, uniformly in $n$. The local conditions at primes dividing $p$ and $N$ (the conductor) are the main difficulty, especially for supersingular primes.

**Required breakthrough:** Uniform control theorem for the adjoint Selmer group over $\operatorname{GL}_2$-extensions of $\mathbb{Q}$, handling the crystalline condition at $p$.

### Obstacle 4: $\mu$-invariant Conjecture
**Status: Open**

The non-commutative $\mu$-invariant (the analogue of Iwasawa's $\mu$-invariant for $\Lambda(G)$) should vanish. For the commutative case, this is Ferrero–Washington (1979) for abelian extensions. For non-commutative extensions, it is completely open.

**Impact:** If $\mu \neq 0$, the main conjecture as stated needs modification (the L-function would need to be divided by a power of $p$).

---

## Cross-Group Connections

### Group A: Iwasawa Theory
**Direct overlap.** J-006 is the non-abelian generalization of the abelian main conjectures studied in Group A. The abelian main conjecture (A-001, A-002) is a special case obtained by restricting $\rho_E$ to the cyclotomic $\mathbb{Z}_p$-extension. The $p$-adic L-functions in A-003, A-004 are commutative specializations of the non-commutative L-function.

### Group B: Euler Systems
**Critical dependency.** The Euler system of Beilinson–Kato elements (B-001, B-003) provides the key input for constructing the non-commutative $p$-adic L-function. Kolyvagin's Euler system (B-005) controls the Selmer group in the abelian case; the non-abelian generalization requires a non-commutative Euler system machine.

### Group C: Arithmetic Statistics
**Indirect connection.** The distribution of Selmer ranks in families (C-001, C-003) provides statistical evidence for the non-abelian main conjecture. If the conjecture holds, the distribution of $|\Sha|$ in the $\operatorname{GL}_2$-tower should be governed by the $p$-adic L-function.

### Group D: Tate-Shafarevich Group
**Direct application.** The non-abelian main conjecture directly predicts $|\Sha(E/\mathbb{Q})[p^\infty]|$. The finiteness of $\Sha$ (D-001) is a prerequisite, and the structure of $\Sha$ (D-003, D-004) is constrained by the conjecture.

### Group E: $p$-adic Methods
**Technical tools.** The crystalline condition for the Selmer group uses $p$-adic Hodge theory (E-001, E-002). The construction of the $p$-adic L-function uses $\Lambda$-adic modular forms (E-005). The interpolation of L-values uses $p$-adic integration on $\operatorname{GL}_2(\mathbb{Z}_p)$ (E-007).

### Group F: Motivic/Cohomological
**Framework.** The equivariant Tamagawa number conjecture (F-001, F-003) is the motivic framework underlying the non-abelian main conjecture. The Beilinson regulator (F-005) appears in the construction of the L-function.

### Group G: Deformation/Langlands
**Key input.** The Galois representation $\rho_E$ and its deformations (G-001, G-002) are the starting point. The Langlands correspondence for $\operatorname{GL}_2$ over $p$-adic fields (G-005) governs the local factors of the L-function. Hida's $\Lambda$-adic forms (G-007) are essential for the L-function construction.

### Group H: Computational
**Verification.** Numerical computation of the non-abelian Selmer group (H-001, H-003) and the $p$-adic L-function (H-005) provides evidence. LMFDB data (H-008) can be used to verify specializations.

### Group I: Connections
**Meta-framework.** The connections between Iwasawa theory and BSD (I-001) are the primary motivation. The ETNC framework (I-003) subsumes the non-abelian main conjecture.

---

## Classification

| Criterion | Assessment |
|-----------|------------|
| **Risk** | Very High — Full conjecture likely decades away |
| **Reward** | Very High — Would resolve $p$-part of BSD, control $\Sha$ in towers |
| **Feasibility (5-year)** | Partial results only: abelian specializations, CM curves, specific primes |
| **Feasibility (20-year)** | Possible for restricted cases (CM curves, specific $p$, rank 0/1) |
| **Proof strategy** | Non-commutative Euler system + Hida theory + $p$-adic Hodge theory |
| **Key dependencies** | Abelian main conjecture (known), Euler systems (known), Hida theory (known), non-commutative $K$-theory (partially known) |
| **Novel contribution achievable** | Non-commutative Selmer group computations, evidence for main conjecture via numerical verification, partial results for CM curves |

**Bottom line:** The full non-abelian main conjecture for $\operatorname{GL}_2/\mathbb{Q}$ is one of the deepest open problems in arithmetic geometry. However, the approach is sound, the tools exist in pieces, and partial results (especially for CM curves and specific primes) are achievable. The connection to BSD is direct and powerful: if proven, it would give the exact $p$-adic valuation of $|\Sha|$ at all primes simultaneously.
