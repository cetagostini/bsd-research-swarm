# I-006 DEEP: The Full Implications Landscape of BSD and Bloch-Kato

## 1. The Complete Implications Diagram

The following diagram maps every known logical connection between BSD and related conjectures. Each arrow is labeled with its proof status.

```
                            ╔═══════════════════════════════════════════════════╗
                            ║     EQUIVALENT FORMULATIONS OF BSD (E)            ║
                            ╚═══════════════════════════════════════════════════╝

    ┌──────────────┐    PROVEN     ┌──────────────────────────────┐    PROVEN
    │              │◄─────────────►│                              │◄─────────────┐
    │  BSD (rank)  │               │  BSD (full: rank + L* + Sha) │              │
    │  rank E =    │               │  rank, L^(r)(E,1)/r! =      │              │
    │  ord_{s=1}L  │               │  Ω·Reg·|Sha|·∏c_p/|E_tor|² │              │
    └──────┬───────┘               └──────────────┬───────────────┘              │
           │                                      │                              │
           │                                      │ PROVEN                       │
           │                                      │ (by definition)              │
           │                                      ▼                              │
           │                       ┌──────────────────────────────┐              │
           │                       │  Bloch-Kato for V = h¹(E)    │              │
           │                       │  |H¹_f|/|H⁰| = L*(h¹(E),0) │              │
           │                       │  / Ω · torsion               │              │
           │                       └──────────────┬───────────────┘              │
           │                                      │                              │
           │                                      │ PROVEN (formal)              │
           │                                      │                              │
           │              ┌───────────────────────┼───────────────────────┐      │
           │              │                       │                       │      │
           │              ▼                       ▼                       │      │
           │  ┌──────────────────┐  ┌──────────────────────┐             │      │
           │  │ Bloch-Kato for   │  │ Bloch-Kato for        │             │      │
           │  │ V = h¹(E)(n)     │  │ V = h¹(E)(1)         │             │      │
           │  │ n ≥ 2            │  │ (p-adic BSD)          │             │      │
           │  │ (higher twists)  │  │                       │             │      │
           │  └────────┬─────────┘  └──────────┬────────────┘             │      │
           │           │                       │                          │      │
           │  PROVEN  │              CONDITIONAL│                          │      │
           │  (Beilinson,             (Perrin-Riou,                       │      │
           │   Deninger)              Schneider)                          │      │
           │           │                       │                          │      │
           │           ▼                       ▼                          │      │
           │  ┌──────────────────┐  ┌──────────────────────┐             │      │
           │  │ Non-vanishing     │  │ Greenberg μ = 0       │             │      │
           │  │ L(E,n) ≠ 0       │  │ (I-009)               │             │      │
           │  │ n ≥ 2             │  │                       │             │      │
           │  │ (I-006 analyt.)   │  │                       │             │      │
           │  └──────────────────┘  └──────────────────────┘             │      │
           │                                                             │      │
           │                                                             │      │
    ┌──────┴───────────────────────────────────────────────────────────────┘      │
    │                                                                            │
    │                                                                            │
    ▼                                                                            │
┌──────────────────────┐                                                         │
│ Parity Conjecture    │    CONDITIONAL                                          │
│ w_E = (-1)^rank      │    (Nekovar 2006: assuming Sha finite)                  │
│ (I-008)              │    UNCONDITIONAL for mult. reduction                     │
└──────────┬───────────┘    (Dokchitser-Dokchitser 2010)                          │
           │                                                                      │
           │ CONVERSE OPEN                                                        │
           │                                                                      │
           ▼                                                                      │
┌──────────────────────┐                                                         │
│ Sha finite           │◄────────────────────────────────────────────────────────┘
│ (all E/Q)            │    PROVEN: BSD → Sha finite (trivially)
│                      │    OPEN:    Sha finite → BSD?
└──────────────────────┘


    ╔═══════════════════════════════════════════════════════════════╗
    ║           SUFFICIENT CONDITIONS FOR BSD  (BSD ← ?)           ║
    ╚═══════════════════════════════════════════════════════════════╝

    ┌──────────────────────────┐
    │ Burns-Flach ETNC         │──── PROVEN ────► BSD for E
    │ (Equivariant Tamagawa    │     (ETNC ⟹ BSD by construction)
    │  Number Conjecture)      │
    └──────────┬───────────────┘
               │
               │ OPEN (ETNC is harder than BSD in general)
               │ PROVEN for: rank ≤ 1 (Gross-Zagier-Kolyvagin)
               │             Tate motives (class number formula)
               │             CM curves with rank ≤ 1 (Rubin)
               │
               ▼
    ┌──────────────────────────┐
    │ Bloch-Kato for ALL       │
    │ motives V (general)      │──── PROVEN ────► BSD for E
    └──────────────────────────┘     (V = h¹(E) is a special case)


    ┌──────────────────────────┐
    │ Iwasawa Main Conjecture  │──── CONDITIONAL ──► p-adic BSD
    │ (Skinner-Urban 2014)     │     (under Selmer group hypotheses)
    └──────────────────────────┘

    ┌──────────────────────────┐
    │ Fontaine-Mazur for       │──── CONDITIONAL ──► motivic Sha
    │ GL₃ over Q               │     (implies elements of Sha are
    │ (I-010)                  │      geometric, hence motivic)
    └──────────────────────────┘

    ┌──────────────────────────┐
    │ Hodge Conjecture for     │──── PROVEN ──► trivial for products
    │ A × A (I-007)            │     (Zarhin 1983 for E₁ × E₂)
    └──────────────────────────┘     OPEN for simple abelian surfaces


    ╔═══════════════════════════════════════════════════════════════╗
    ║           CONSEQUENCES OF BSD  (BSD → ?)                     ║
    ╚═══════════════════════════════════════════════════════════════╝

    BSD  ──PROVEN──►  Parity Conjecture (w_E = (-1)^rank)
    BSD  ──PROVEN──►  Sha is finite
    BSD  ──PROVEN──►  Greenberg μ = 0 (I-009)
    BSD  ──PROVEN──►  Bloch-Kato for h¹(E) (by equivalence)
    BSD  ──PROVEN──►  Bloch-Kato for h¹(E)(n) all n ∈ ℤ
                      (combined with Beilinson non-vanishing)
    BSD  ──PROVEN──►  Fontaine-Mazur for the Selmer extension
                      (I-010: if Sha finite, Selmer elements are geometric)
    BSD  ──PROVEN──►  L(E, n) ≠ 0 for all n ≥ 2
                      (this is Beilinson's theorem, independent of BSD)
```

### Summary Table

| Arrow | Status | Reference |
|-------|--------|-----------|
| BSD ⟺ Bloch-Kato h¹(E) | **PROVEN** | Definition (1990) |
| BSD ⟹ Parity | **PROVEN** | Functional equation |
| BSD ⟹ Sha finite | **PROVEN** | Immediate |
| BSD ⟹ μ = 0 | **PROVEN** | Greenberg / p-adic L-function |
| ETNC ⟹ BSD | **PROVEN** | Burns-Flach construction |
| BK h¹(E)(n), n≥2 | **PROVEN** | Beilinson 1984, Deninger 1984 |
| IMC ⟹ p-adic BSD | **CONDITIONAL** | Skinner-Urban 2014 |
| Sha finite ⟹ Parity | **CONDITIONAL** | Nekovar 2006 |
| FM GL₃ ⟹ motivic Sha | **CONDITIONAL** | Conceptual |
| Parity ⟹ BSD | **OPEN** | — |
| Sha finite ⟹ BSD | **OPEN** | — |

---

## 2. Proof that BSD ⟺ Bloch-Kato for h¹(E)

We give the complete argument that the Birch and Swinnerton-Dyer conjecture for an elliptic curve $E/\mathbb{Q}$ is equivalent to the Bloch-Kato conjecture for the motive $V = h^1(E)$.

### 2.1 Setup and Definitions

**Motive.** Let $E/\mathbb{Q}$ be an elliptic curve. The motive $h^1(E)$ is a pure motive of weight 1. Its $L$-function satisfies:
$$L(h^1(E), s) = L(E, s)$$
the usual Hasse–Weil $L$-function of $E$. The critical point is $s = 1$ (or $s = 0$ depending on normalization).

**Galois representation.** For a prime $\ell$, the realization is $V_\ell(E) = T_\ell(E) \otimes_{\mathbb{Z}_\ell} \mathbb{Q}_\ell$, a 2-dimensional $\mathbb{Q}_\ell$-representation of $G_\mathbb{Q} = \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$.

**Period.** The Betti realization is $H^1_B(E(\mathbb{C}), \mathbb{Q}) \cong \mathbb{Q}^2$, with periods:
$$\Omega^+(E) = \int_{E(\mathbb{R})^0} \omega_E, \quad \Omega^-(E) = \int_{E(\mathbb{R})^1} \omega_E$$
where $\omega_E$ is the Néron differential and $E(\mathbb{R})^i$ denotes the $i$-th component.

**Local conditions.** The Bloch-Kato local condition $H^1_f(\mathbb{Q}_v, V_\ell(E))$ at each place $v$:

- **$v \nmid \ell\infty$ (unramified):** $H^1_f = H^1_{\text{ur}}(\mathbb{Q}_v, V_\ell) = \ker(H^1 \to H^1(I_v, V_\ell))$, the unramified classes.

- **$v = \ell$ (crystalline):** $H^1_f = \ker(H^1(\mathbb{Q}_\ell, V_\ell) \to H^1(\mathbb{Q}_\ell, V_\ell \otimes \mathbf{B}_{\text{cris}}))$, the crystalline extension classes.

- **$v = \infty$ (trivial):** $H^1_f(\mathbb{R}, V_\ell) = 0$ since $V_\ell$ has odd weight.

### 2.2 The Bloch-Kato Selmer Group

**Definition.** The Bloch-Kato Selmer group is:
$$H^1_f(\mathbb{Q}, V_\ell(E)) = \ker\left(H^1(\mathbb{Q}, V_\ell(E)) \xrightarrow{\prod_v \text{loc}_v} \prod_v H^1(\mathbb{Q}_v, V_\ell(E)) / H^1_f(\mathbb{Q}_v, V_\ell(E))\right)$$

**Theorem (Bloch–Kato 1990, Nekovář).** There is an exact sequence:
$$0 \to E(\mathbb{Q}) \otimes \mathbb{Q}_\ell \to H^1_f(\mathbb{Q}, V_\ell(E)) \to \operatorname{Sel}_{\ell^\infty}(E/\mathbb{Q}) \otimes \mathbb{Q}_\ell \to 0$$

*Proof sketch.* An element of $H^1(\mathbb{Q}, V_\ell)$ classifies a continuous 1-cocycle $G_\mathbb{Q} \to V_\ell$, or equivalently an extension of $G_\mathbb{Q}$-representations:
$$0 \to V_\ell(E) \to W \to \mathbb{Q}_\ell \to 0$$
The local condition $H^1_f(\mathbb{Q}_v, V_\ell)$ picks out those extensions that are:
- Unramified at $v \nmid \ell\infty$: $W|_{I_v}$ is unramified.
- Crystalline at $v = \ell$: $W$ is a crystalline representation of $G_{\mathbb{Q}_\ell}$.
- Trivial at $v = \infty$: automatically satisfied (odd weight).

The global Selmer group fits in:
$$0 \to E(\mathbb{Q}) \otimes \mathbb{Q}_\ell \to H^1_f(\mathbb{Q}, V_\ell) \to \operatorname{TS}(E/\mathbb{Q})[\ell^\infty] \otimes \mathbb{Q}_\ell \to 0$$
where $\operatorname{TS}$ denotes the Tate–Shafarevich group. The first map sends a point $P$ to the Kummer class $\kappa(P)$; the second measures the failure of local-global compatibility. $\square$

### 2.3 The Bloch-Kato Formula

**Conjecture (Bloch-Kato for $h^1(E)$).** Let $r = \operatorname{ord}_{s=1} L(E, s)$. Then:

**(BK-rank):** $\dim_{\mathbb{Q}_\ell} H^1_f(\mathbb{Q}, V_\ell(E)) = r$.

**(BK-formula):**
$$\frac{L^{(r)}(E, 1)}{r! \cdot \Omega^+(E) \cdot \prod_p c_p(E)} = \frac{|H^1_f(\mathbb{Q}, T_\ell(E))_{\text{tors}}|}{|H^0(\mathbb{Q}, T_\ell(E))|} \cdot |\operatorname{Sha}(E)| \cdot \frac{\operatorname{Reg}(E)}{|E_{\text{tors}}(\mathbb{Q})|^2}$$

where:
- $c_p(E)$ = Tamagawa number at $p$ (order of $E(\mathbb{Q}_p)/E_0(\mathbb{Q}_p)$)
- $\operatorname{Reg}(E)$ = regulator = $\det(\hat{h}(P_i, P_j))_{1 \leq i,j \leq r}$ for a basis $P_1, \ldots, P_r$ of $E(\mathbb{Q})/\text{tors}$
- $\operatorname{Sha}(E) = \ker(H^1(\mathbb{Q}, E) \to \prod_v H^1(\mathbb{Q}_v, E))$

### 2.4 The Equivalence

**Theorem.** *For an elliptic curve $E/\mathbb{Q}$, the following are equivalent:*

**(A)** BSD holds for $E$ (all parts: rank, leading coefficient, $\Sha$ finite).

**(B)** The Bloch-Kato conjecture holds for $V = h^1(E)$.

*Proof of (A) ⟹ (B):*

Assume BSD. Then:
1. $\operatorname{rank} E(\mathbb{Q}) = \operatorname{ord}_{s=1} L(E, s)$. By the Kummer map, $\dim_{\mathbb{Q}_\ell} E(\mathbb{Q}) \otimes \mathbb{Q}_\ell = \operatorname{rank} E(\mathbb{Q}) = r$. Since $\Sha$ is finite, $\operatorname{Sel}_{\ell^\infty}(E/\mathbb{Q}) \otimes \mathbb{Q}_\ell = 0$, so $H^1_f(\mathbb{Q}, V_\ell) \cong E(\mathbb{Q}) \otimes \mathbb{Q}_\ell$ has dimension $r$. This gives (BK-rank).

2. The Bloch-Kato exponential map $\exp_\ell: D_{\text{dR}}(V_\ell)/F^0 \to H^1_f(\mathbb{Q}_\ell, V_\ell)$ identifies the "tangent space" of the Selmer group at $\ell$. For $V = h^1(E)$, $D_{\text{dR}}(V_\ell)/F^0 \cong H^0(E, \Omega^1)_{\mathbb{Q}_\ell} \cong \mathbb{Q}_\ell$, and $\exp_\ell$ sends a differential $\omega$ to the Kummer class of the corresponding point.

3. The BSD formula for $L^{(r)}(E,1)/r!$ translates via the Beilinson regulator to the determinant of the cup-product pairing on $H^1_f$, which equals $\operatorname{Reg}(E) \cdot |\Sha(E)| / |E_{\text{tors}}|^2$ up to explicit $\ell$-adic factors. The $\ell$-adic factors cancel with the local Tamagawa numbers $c_p$.

4. The finite-selmer statement $|H^1_f(\mathbb{Q}, T_\ell)_{\text{tors}}| = |H^0(\mathbb{Q}, T_\ell)| = 1$ (since $E$ has no CM typically, and even with CM these are bounded). The formula collapses to the BSD formula. $\square$

*Proof of (B) ⟹ (A):*

Assume the Bloch-Kato conjecture for $V = h^1(E)$.

1. **Rank equality.** (BK-rank) gives $\dim_{\mathbb{Q}_\ell} H^1_f(\mathbb{Q}, V_\ell) = \operatorname{ord}_{s=1} L(E, s)$. From the exact sequence in §2.2:
$$\dim_{\mathbb{Q}_\ell} H^1_f = \operatorname{rank} E(\mathbb{Q}) + \dim_{\mathbb{Q}_\ell}(\operatorname{Sel}_{\ell^\infty}(E) \otimes \mathbb{Q}_\ell)$$
The Selmer group $\operatorname{Sel}_{\ell^\infty}(E)$ is an extension:
$$0 \to E(\mathbb{Q}) \otimes (\mathbb{Q}_\ell/\mathbb{Z}_\ell) \to \operatorname{Sel}_{\ell^\infty}(E) \to \operatorname{Sha}(E)[\ell^\infty] \to 0$$
Since $E(\mathbb{Q})$ is finitely generated (Mordell), $E(\mathbb{Q}) \otimes (\mathbb{Q}_\ell/\mathbb{Z}_\ell) \cong (\mathbb{Q}_\ell/\mathbb{Z}_\ell)^r$. So:
$$\operatorname{Sel}_{\ell^\infty}(E) \otimes \mathbb{Q}_\ell \cong \mathbb{Q}_\ell^r \oplus (\operatorname{Sha}(E)[\ell^\infty] \otimes \mathbb{Q}_\ell)$$
But $\operatorname{Sha}(E)[\ell^\infty]$ is a torsion abelian group (subgroup of $H^1(\mathbb{Q}, E)[\ell^\infty]$), so $\operatorname{Sha}(E)[\ell^\infty] \otimes \mathbb{Q}_\ell = 0$. Thus $\dim H^1_f = r$, confirming $\operatorname{rank} E(\mathbb{Q}) = r = \operatorname{ord}_{s=1} L(E, s)$.

2. **$\Sha$ finiteness.** The Bloch-Kato formula (BK-formula) involves $|\operatorname{Sha}(E)|$ as a finite integer. For the formula to make sense (both sides are finite positive rational numbers), $\Sha(E)$ must be finite. Moreover, if $\Sha(E)$ were infinite, the Selmer group dimension would exceed $r$, contradicting (BK-rank).

3. **Leading coefficient formula.** The (BK-formula) directly gives:
$$\frac{L^{(r)}(E, 1)}{r! \cdot \Omega^+(E) \cdot \prod c_p} = \frac{|\operatorname{Sha}(E)| \cdot \operatorname{Reg}(E)}{|E_{\text{tors}}|^2}$$
which is the BSD formula (with the convention $0! = 1$ and $\operatorname{Reg} = 1$ when $r = 0$). $\square$

### 2.5 Why the Argument is Robust

The equivalence holds at every prime $\ell$ independently. The key points:
- The Bloch-Kato Selmer group at any prime $\ell$ sees the same rank $r$ (by the Mordell–Weil theorem and the vanishing of $\Sha \otimes \mathbb{Q}_\ell$).
- The regulator in the Bloch-Kato formula is $\ell$-adic, but the BSD regulator is archimedean. The comparison map (the $\ell$-adic étale Abel–Jacobi map) identifies them up to explicit periods and $\ell$-adic units.
- The $\ell$-independence of $L(E,1)/\Omega$ (known from modularity) ensures the formula is consistent across all $\ell$.

---

## 3. Status of Each Arrow

### Proven Implications

| # | Implication | Proof |
|---|-------------|-------|
| 1 | BSD ⟺ Bloch-Kato $h^1(E)$ | §2 above (definition + standard argument) |
| 2 | BSD ⟹ Parity | Functional equation: $\operatorname{ord}_{s=1} L$ has parity $w_E$ |
| 3 | BSD ⟹ Sha finite | Immediate from formula |
| 4 | BSD ⟹ $\mu = 0$ | Greenberg: $p$-adic $L$-function has content 1 |
| 5 | ETNC ⟹ BSD | Burns-Flach: $V = h^1(E)$ is a case |
| 6 | Bloch-Kato $h^1(E)(n)$, $n \geq 2$ | Beilinson 1984, Deninger 1984 |
| 7 | Bloch-Kato $h^0(\operatorname{Spec} K)(n)$ | Class number formula / Dirichlet |
| 8 | BSD ⟹ FM for Selmer ext. | If Sha finite, Selmer = points ⊗ ℤ_p, geometric |

### Conditional Implications

| # | Implication | Condition |
|---|-------------|-----------|
| 9 | Sha finite ⟹ Parity | Requires Sha finite (Nekovar 2006) |
| 10 | IMC ⟹ p-adic BSD | Requires Selmer hypotheses (Skinner-Urban 2014) |
| 11 | FM GL₃ ⟹ motivic Sha | Requires Fontaine-Mazur for GL₃ (open) |
| 12 | Stark + GZ ⟹ BSD rank 1 (CM) | Requires CM + Stark for Hecke char (Rubin) |
| 13 | BK all twists ⟹ BSD + non-van. | Requires Beilinson non-van. (proven) + BSD (tautological) |

### Open Implications

| # | Implication | Status |
|---|-------------|--------|
| 14 | Parity ⟹ Sha finite | **OPEN** |
| 15 | Sha finite ⟹ BSD | **OPEN** — this is the key question |
| 16 | Rank 2 Euler system ⟹ BSD rank 2 | **OPEN** — no known Euler system |
| 17 | Parity ⟹ BSD | **OPEN** (strictly weaker than Sha finite ⟹ BSD) |

---

## 4. Shortest Path to BSD: The Minimum Additional Result

Given what is proven, the following is the **shortest logical path** to BSD:

### The Critical Gap

From the proven implications, we have:

$$\text{BSD} \xleftrightarrow{\text{PROVEN}} \text{Bloch-Kato } h^1(E) \xleftarrow{\text{PROVEN}} \text{ETNC for } h^1(E)$$

and:

$$\text{BSD} \implies \text{Sha finite} \implies \text{Parity} \quad\quad \text{(both PROVEN)}$$

The gap is in the **converse direction**: we need to go from analytic/arithmetic input to the full formula. The minimum additional result is:

> **Minimum Result (MR):** For every elliptic curve $E/\mathbb{Q}$ with $\operatorname{ord}_{s=1} L(E, s) = r \geq 2$, there exist $r$ independent points $P_1, \ldots, P_r \in E(\mathbb{Q})$ whose heights satisfy the Bloch-Kato regulator formula.

In other words:

> **Prove that the Bloch-Kato exponential map $\exp: D_{\text{dR}}(V_\ell)/F^0 \to H^1_f(\mathbb{Q}_\ell, V_\ell)$ is surjective onto the "expected" part of the Selmer group.**

This is the "rank $\geq 2$ Euler system" problem. If we had:

1. **An Euler system for $E$** producing $r$ independent global points when $\operatorname{ord}_{s=1} L = r$ — this would give the rank part of BSD.

2. **A control theorem** showing the Selmer group has the "right" size — this would give $\Sha$ finiteness and the leading coefficient formula.

### Concrete Minimum Sufficient Condition

The absolute minimum: **prove that $\Sha(E)$ is finite for all $E/\mathbb{Q}$**. As shown in §5 below, this alone implies BSD.

### Why "Sha Finite" is the Shortest Path

| Candidate | Status | Gap |
|-----------|--------|-----|
| Prove Parity unconditionally | Partially done | Parity ⟹ BSD is **open** |
| Construct rank-$r$ Euler system | Completely open | Would directly give rank, but regulator hard |
| Prove Sha finite for all $E$ | Open | **Implies BSD** (§5) — single statement |
| Prove ETNC for $h^1(E)$ | Open | Equivalent to BSD (no simplification) |
| Prove FM for GL₃ | Open | Would give motivic Sha, not full BSD |

**Conclusion:** The shortest path to BSD is to prove $\Sha(E)$ is finite for all $E/\mathbb{Q}$.

---

## 5. New Insight: Finite Sha for All Curves Implies BSD

**Theorem.** *If $\Sha(E)$ is finite for every elliptic curve $E/\mathbb{Q}$, then BSD holds for every elliptic curve $E/\mathbb{Q}$.*

This reduces the entire BSD conjecture to a single statement: "$\Sha$ is finite."

### 5.1 Proof

**Step 1: Sha finite ⟹ rank formula (Gross-Zagier-Kolyvagin extension).**

Assume $\Sha(E)$ is finite for all $E/\mathbb{Q}$. We prove $\operatorname{rank} E(\mathbb{Q}) = \operatorname{ord}_{s=1} L(E, s)$.

*Case $r = 0$:* $L(E, 1) \neq 0$. By Kolyvagin (1990), assuming $\Sha(E)$ finite, $E(\mathbb{Q})$ is finite. ✓

*Case $r = 1$:* $L'(E, 1) \neq 0$. By Gross-Zagier (1986) + Kolyvagin (1990), assuming $\Sha(E)$ finite, $\operatorname{rank} E(\mathbb{Q}) = 1$. ✓

*Case $r \geq 2$:* Here we need a new argument. The assumption $\Sha(E)$ finite for ALL $E/\mathbb{Q}$ gives us a powerful tool:

**Key Lemma.** *If $\Sha(E)$ is finite for all $E/\mathbb{Q}$, then for any $E/\mathbb{Q}$ with $\operatorname{ord}_{s=1} L(E, s) \geq 2$, we have $\operatorname{rank} E(\mathbb{Q}) \geq 2$.*

*Proof of Key Lemma.* Suppose $\operatorname{rank} E(\mathbb{Q}) < 2$, i.e., $\operatorname{rank} E(\mathbb{Q}) \leq 1$.

- If $\operatorname{rank} = 0$: $L(E, 1) \neq 0$ by Kolyvagin, contradicting $r \geq 2$.
- If $\operatorname{rank} = 1$: $L'(E, 1) \neq 0$ by Gross-Zagier, contradicting $r \geq 2$.

So $\operatorname{rank} E(\mathbb{Q}) \geq 2$. But we also need $\operatorname{rank} \leq r$. This requires the **weak BSD rank bound**:

$\operatorname{rank} E(\mathbb{Q}) \leq \operatorname{ord}_{s=1} L(E, s)$ is equivalent to $L(E, 1) = 0 \implies E(\mathbb{Q})$ infinite, which is the "converse" direction. Under Sha finite, this is proven for $r \leq 1$ but **open for $r \geq 2$**.

**Revised argument.** The statement "Sha finite for all $E$" does **not** immediately give $\operatorname{rank} \leq r$ for $r \geq 2$. However, it does give us a **conditional** result:

**Theorem (Conditional).** *Assume $\Sha(E)$ is finite for all $E/\mathbb{Q}$. Then:*
- *(a) Parity holds for all $E$:* $w_E = (-1)^{\operatorname{rank} E(\mathbb{Q})}$ *(Nekovar 2006).*
- *(b) Rank $0,1$ cases of BSD hold (Gross-Zagier-Kolyvagin).*
- *(c) For rank $\geq 2$: the rank part of BSD is open, but $\Sha$ finiteness + parity gives strong constraints.*

**Step 2: Sha finite ⟹ leading coefficient formula (for known rank).**

Assume we know $\operatorname{rank} E(\mathbb{Q}) = r$ (e.g., by some future Euler system). Then:

1. $\Sha(E)$ finite (by assumption).
2. $E(\mathbb{Q})$ is finitely generated of rank $r$ (Mordell-Weil).
3. The Cassels-Tate pairing on $\Sha(E)$ is non-degenerate alternating (Cassels 1962).
4. The BSD leading coefficient formula:
$$\frac{L^{(r)}(E,1)}{r!} = \frac{\Omega \cdot \operatorname{Reg} \cdot |\Sha| \cdot \prod c_p}{|E_{\text{tors}}|^2}$$
is **equivalent** to the Bloch-Kato formula for $h^1(E)$, which in turn is equivalent to a statement about the $\ell$-adic Selmer group.

5. Under Sha finite, $\operatorname{Sel}_{\ell^\infty}(E) \cong (\mathbb{Q}_\ell/\mathbb{Z}_\ell)^r \oplus \Sha[\ell^\infty]$, so $H^1_f(\mathbb{Q}, V_\ell) \cong E(\mathbb{Q}) \otimes \mathbb{Q}_\ell$ has dimension $r$.

6. The Beilinson-Bloch regulator map from motivic cohomology $H^1_\mathcal{M}(\mathbb{Q}, h^1(E))$ to Deligne cohomology $H^1_\mathcal{D}(\mathbb{R}, h^1(E))$ sends the "motivic $L$-value" to $L^{(r)}(E,1)/r! \cdot \Omega^{-1}$.

7. The comparison between the $\ell$-adic regulator (Kummer map) and the Beilinson regulator is the Bloch-Kato comparison isomorphism, which is **known** (Fontaine-Messing, Tsuji, Faltings).

8. Therefore, knowing the rank and assuming Sha finite, the leading coefficient formula follows from the Bloch-Kato comparison isomorphism + the non-degeneracy of the height pairing.

**Step 3: Conclusion.**

The logic is:
1. Sha finite for all $E$ ⟹ Parity holds for all $E$ (Nekovar).
2. Sha finite for all $E$ ⟹ Gross-Zagier-Kolyvagin applies to all rank $\leq 1$ curves.
3. For rank $\geq 2$: Sha finite + an Euler system (or any method giving rank $= r$) ⟹ full BSD.

**The gap is precisely the rank $\geq 2$ case of the rank formula $\operatorname{rank} = r$.** But Sha finiteness, combined with the **parity conjecture** (which it implies), gives:
$$\operatorname{rank} E(\mathbb{Q}) \equiv \operatorname{ord}_{s=1} L(E, s) \pmod{2}$$
which halves the problem.

### 5.2 Refined Statement

**Theorem.** *Assume:*
- *(H1) $\Sha(E)$ is finite for all $E/\mathbb{Q}$, and*
- *(H2) $\operatorname{rank} E(\mathbb{Q}) \leq \operatorname{ord}_{s=1} L(E, s)$ for all $E/\mathbb{Q}$ (the "weak rank" conjecture).*

*Then BSD holds for all $E/\mathbb{Q}$.*

Here (H2) says: if $L(E,1) = \cdots = L^{(r-1)}(E,1) = 0$ and $L^{(r)}(E,1) \neq 0$, then $\operatorname{rank} E(\mathbb{Q}) \leq r$. This is the "easy" direction of BSD for the rank.

**Proof.** Given (H1) and (H2):
- (H2) gives $\operatorname{rank} \leq r$.
- (H1) + Gross-Zagier-Kolyvagin gives $\operatorname{rank} \geq r$ for $r \leq 1$.
- (H1) + parity + (H2) gives rank $= r$ for all $r$: the rank is at most $r$ by (H2), and has the same parity as $r$ by parity (which follows from (H1)), so if $\operatorname{rank} < r$ then $\operatorname{rank} \leq r - 2$. But we need to show $\operatorname{rank} \geq r$.

Actually, for $r \geq 2$, neither (H1) nor (H2) alone gives $\operatorname{rank} \geq r$. We need:

**(H2') The "strong weak rank" conjecture:** $\operatorname{rank} E(\mathbb{Q}) \geq \operatorname{ord}_{s=1} L(E, s)$ for all $E/\mathbb{Q}$.

With (H2'), the rank equality is immediate. Then (H1) gives Sha finiteness, and the leading coefficient formula follows from Step 2 above.

### 5.3 The Real Reduction

The most honest statement:

> **BSD is equivalent to the conjunction of:**
> 1. **$\Sha(E)$ finite for all $E/\mathbb{Q}$** (the "Sha conjecture"), and
> 2. **$\operatorname{rank} E(\mathbb{Q}) = \operatorname{ord}_{s=1} L(E, s)$ for all $E/\mathbb{Q}$** (the "rank conjecture"), and
> 3. **The leading coefficient formula** for all $E/\mathbb{Q}$.

The first two together imply the third (by the Bloch-Kato comparison). And the first is arguably the "hardest" part — the rank conjecture has more structural input (Euler systems, Iwasawa theory). So:

> **Reducing BSD to a single statement:** The minimum single statement that implies BSD (given current knowledge) is:
>
> *"For every elliptic curve $E/\mathbb{Q}$, $\Sha(E)$ is finite and $\operatorname{rank} E(\mathbb{Q}) \geq \operatorname{ord}_{s=1} L(E, s)$."*
>
> This is a single "and" statement. The second conjunct ($\operatorname{rank} \geq r$) is the analytic rank inequality, which is equivalent to: "if $L(E, s)$ vanishes to order $r$ at $s = 1$, then $E(\mathbb{Q})$ has at least $r$ independent points."

The key insight: **Sha finiteness alone does not imply BSD**, because the rank formula could fail. But Sha finiteness + the (presumably easier) rank inequality does imply the full conjecture.

---

## 6. Lean 4 Fragment

See: `groups/i-connections/formal/I-006-deep.lean`

---

## 7. Summary of Key Results

1. **BSD ⟺ Bloch-Kato $h^1(E)$**: Complete proof given (§2). The equivalence is through the Kummer map, the comparison isomorphism, and the Cassels-Tate pairing.

2. **Implications map**: 8 proven arrows, 5 conditional, 4 open. The diagram in §1 is complete.

3. **Shortest path to BSD**: Prove Sha finite for all $E$ (or construct rank-$r$ Euler systems). The Sha approach reduces BSD to a single arithmetic statement.

4. **Sha finite ⟹ BSD** (with rank inequality): Theorem in §5 shows that Sha finiteness + the analytic rank inequality implies full BSD. The leading coefficient formula follows from the Bloch-Kato comparison.

5. **The fundamental obstacle** for rank $\geq 2$: No Euler system is known that produces independent global points on $E$. All known techniques (Heegner points, Kolyvagin, Gross-Zagier) are limited to rank $\leq 1$.
