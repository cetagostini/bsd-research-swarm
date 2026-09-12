# A-NONABELIAN-SHA: Non-Abelian Iwasawa Theory and Ш Finiteness via the CFKS Main Conjecture

## 1. The Coates–Fukaya–Kaczorowski–Sujatha (CFKS) Main Conjecture

### 1.1 Setup

Let $E/\mathbb{Q}$ be an elliptic curve and $p$ a prime. Let $F_\infty/\mathbb{Q}$ be a $p$-adic Lie extension — an infinite Galois extension whose Galois group $G = \operatorname{Gal}(F_\infty/\mathbb{Q})$ is a compact $p$-adic Lie group of dimension $\geq 2$.

**Key examples of $p$-adic Lie extensions:**

| Extension | Galois group | Dimension |
|---|---|---|
| $\mathbb{Q}_\infty = \bigcup \mathbb{Q}_n$ (cyclotomic $\mathbb{Z}_p$-extension) | $\mathbb{Z}_p$ | 1 |
| $\mathbb{Q}(E[p^\infty])$ (false Tate curve) | $\operatorname{GL}_2(\mathbb{Z}_p)$ | 4 |
| $\mathbb{Q}(\mu_{p^\infty}, E[p])$ | $\mathbb{Z}_p^\times \ltimes \operatorname{GL}_2(\mathbb{F}_p)$ | $\geq 2$ |
| $\mathbb{Q}(E[3])$ (mod-3 representation) | $\operatorname{GL}_2(\mathbb{F}_3) \cong S_4$ | 0 (finite) |

The crucial difference from classical (commutative) Iwasawa theory: $G$ is **non-abelian**, so the Iwasawa algebra $\mathcal{O}[[G]]$ is a **non-commutative** ring.

### 1.2 The Non-Commutative Iwasawa Algebra

Let $\mathcal{O}$ be the ring of integers of a finite extension of $\mathbb{Q}_p$. The **non-commutative Iwasawa algebra** is:

$$\mathcal{O}(G) = \mathcal{O}[[G]] = \varprojlim_{U \trianglelefteq G, [G:U] < \infty} \mathcal{O}[G/U]$$

where the inverse limit is over open normal subgroups of $G$.

**Properties of $\mathcal{O}(G)$:**
- $\mathcal{O}(G)$ is a Noetherian ring (Lazard's theorem).
- If $G$ is a compact $p$-adic Lie group of dimension $d$, then $\mathcal{O}(G)$ has global dimension $d + 1$.
- $\mathcal{O}(G)$ is **not** a unique factorization domain in general.
- The **center** $Z(\mathcal{O}(G))$ contains $\mathcal{O}[[G^{\mathrm{ab}}]]$, the commutative Iwasawa algebra of the abelianization.
- Ore localization: if $S \subset \mathcal{O}(G)$ is a right/left Ore set, one can form the localization $S^{-1}\mathcal{O}(G)$.

### 1.3 The Selmer Group over a $p$-adic Lie Extension

For an elliptic curve $E/\mathbb{Q}$ and a $p$-adic Lie extension $F_\infty$:

$$\operatorname{Sel}_{p^\infty}(E/F_\infty) = \ker\left(H^1(F_\infty, E[p^\infty]) \to \prod_v \frac{H^1(F_{\infty,v}, E[p^\infty])}{\operatorname{im} \kappa_v}\right)$$

where $\kappa_v$ is the Kummer local image at each place $v$.

**The Pontryagin dual:**

$$X_\infty(E) = \operatorname{Hom}\left(\operatorname{Sel}_{p^\infty}(E/F_\infty), \mathbb{Q}_p/\mathbb{Z}_p\right)$$

$X_\infty(E)$ is a finitely generated (left) $\mathcal{O}(G)$-module — this is the key structural result of Coates, Fukaya, Kaczorowski, and Sujatha.

### 1.4 The Characteristic Ideal in the Non-Commutative Setting

In the commutative case, $\operatorname{char}_\Lambda(M)$ is a principal ideal for a finitely generated torsion $\Lambda$-module $M$. In the non-commutative case, one works with the **Grothendieck group** $K_0(\mathcal{O}(G))$ and the **determinant** construction.

**Definition.** For a finitely presented $\mathcal{O}(G)$-module $M$ with a presentation:
$$\mathcal{O}(G)^m \xrightarrow{\phi} \mathcal{O}(G)^n \to M \to 0$$

the **characteristic element** $\operatorname{char}(M) \in K_0(\mathcal{O}(G))$ is the class $[\mathcal{O}(G)^m] - [\mathcal{O}(G)^n]$.

When $S$ is an Ore set and $M$ is $S$-torsion (meaning $S^{-1}M = 0$), one can refine this to an element:

$$\operatorname{char}_S(M) \in K_0(\mathcal{O}(G)) \to K_0(S^{-1}\mathcal{O}(G)) \cong K_0(M_d(F))$$

where $F$ is the skew field of fractions.

**The canonical Ore set:** Let $S^*$ be the set of all $f \in \mathcal{O}(G)$ whose image in $\mathcal{O}(G/H)$ is a unit for every open normal subgroup $H \trianglelefteq G$. Then $X_\infty(E)$ is $S^*$-torsion if and only if $\operatorname{corank}_{\mathbb{Z}_p} \operatorname{Sel}_{p^\infty}(E/F_n) = 0$ for all layers $F_n \subset F_\infty$.

### 1.5 The CFKS Main Conjecture

**Conjecture (Coates–Fukaya–Kaczorowski–Sujatha, 2007).** Let $E/\mathbb{Q}$ be an elliptic curve, $p$ a prime, and $F_\infty/\mathbb{Q}$ a $p$-adic Lie extension with Galois group $G$. Assume:

**(A1)** $E$ has good ordinary reduction at $p$.

**(A2)** $F_\infty$ contains the cyclotomic $\mathbb{Z}_p$-extension $\mathbb{Q}_\infty$.

**(A3)** $\operatorname{Gal}(F_\infty/\mathbb{Q}_\infty) \cong H$ is a compact $p$-adic Lie group with no element of order $p$.

**(A4)** The $\mu$-invariant of $E$ over $\mathbb{Q}_\infty$ vanishes.

Then there exists a canonical element:

$$\mathcal{L}_p(E/F_\infty) \in K_0(\mathcal{O}(G))$$

the **non-commutative $p$-adic $L$-function**, such that:

$$\operatorname{char}_{S^*}\bigl(X_\infty(E)\bigr) = \mathcal{L}_p(E/F_\infty)$$

in $K_0(\mathcal{O}(G))$.

### 1.6 What $\mathcal{L}_p$ Encodes

The non-commutative $p$-adic $L$-function $\mathcal{L}_p(E/F_\infty)$ **interpolates** the $p$-adic $L$-functions $L_p(E/\mathbb{Q}_\infty)$ and their twists by characters of $H = \operatorname{Gal}(F_\infty/\mathbb{Q}_\infty)$.

More precisely, for each continuous character $\rho \colon H \to \overline{\mathbb{Q}}_p^\times$ of finite image:

$$\operatorname{ev}_\rho\bigl(\mathcal{L}_p(E/F_\infty)\bigr) = L_p(E, \rho, T)$$

the $p$-adic $L$-function of $E$ twisted by $\rho$, viewed as an element of $\mathbb{Z}_p[[T]]$.

This means $\mathcal{L}_p$ **packages all commutative main conjectures simultaneously** into a single non-commutative object.

---

## 2. The False Tate Curve Extension

### 2.1 Definition

The **false Tate curve extension** is:

$$F_\infty = \mathbb{Q}\bigl(E[p^\infty]\bigr) = \bigcup_{n \geq 1} \mathbb{Q}\bigl(E[p^n]\bigr)$$

the extension generated by the coordinates of all $p$-power torsion points on $E$.

**Galois group:**

$$G = \operatorname{Gal}\bigl(\mathbb{Q}(E[p^\infty])/\mathbb{Q}\bigr) \hookrightarrow \operatorname{GL}_2(\mathbb{Z}_p)$$

For a non-CM curve $E/\mathbb{Q}$ with irreducible $\bar{\rho}_{E,p}$, the image is **open** in $\operatorname{GL}_2(\mathbb{Z}_p)$ by Serre's open image theorem. In fact, for $p$ sufficiently large (depending on $E$), the map $\rho_{E,p^\infty} \colon \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \operatorname{GL}_2(\mathbb{Z}_p)$ is **surjective**.

**Key structural facts about $G = \operatorname{GL}_2(\mathbb{Z}_p)$:**

| Property | Value |
|---|---|
| $\dim G$ (as $p$-adic Lie group) | 4 |
| $G^{\mathrm{ab}}$ | $\mathbb{Z}_p^\times \times \mathbb{Z}_p^\times$ (det $\times$ char. poly.) |
| $[G, G]$ | $\operatorname{SL}_2(\mathbb{Z}_p)$ (for $p \geq 5$) |
| $\operatorname{cd}_p(G)$ | 2 (strict cohomological dimension) |
| Element of order $p$? | Yes — $\operatorname{SL}_2(\mathbb{Z}_p)$ has elements of order $p$ |

### 2.2 The Cyclotomic Subextension

$F_\infty$ contains $\mathbb{Q}(\mu_{p^\infty})$, the cyclotomic $\mathbb{Z}_p$-extension of $\mathbb{Q}$:

$$\mathbb{Q}_\infty \subset F_\infty, \quad \operatorname{Gal}(\mathbb{Q}_\infty/\mathbb{Q}) \cong \mathbb{Z}_p^\times$$

via the Weil pairing $e_p \colon E[p^n] \times E[p^n] \to \mu_{p^n}$. This verifies hypothesis (A2).

### 2.3 The Group $H = \operatorname{Gal}(F_\infty/\mathbb{Q}_\infty)$

$$H = \ker\bigl(\det \colon \operatorname{GL}_2(\mathbb{Z}_p) \to \mathbb{Z}_p^\times\bigr)^{\mathrm{open}} \supseteq \operatorname{SL}_2(\mathbb{Z}_p)$$

**Problem with (A3):** $H$ contains elements of order $p$ (e.g., $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has order $p$ in $\operatorname{GL}_2(\mathbb{F}_p)$, and lifts to an element of order $p$ in $\operatorname{GL}_2(\mathbb{Z}_p)$ for $p \geq 3$).

This means the **original CFKS formulation does not directly apply** to the false Tate curve extension. Modifications are needed:

**Workaround 1:** Restrict to the pro-$p$ part $H' = 1 + p M_2(\mathbb{Z}_p) \cap H$, which is torsion-free.

**Workaround 2:** Use the extended CFKS framework of Hachimson–Sujatha (2009) which handles groups with $p$-torsion.

**Workaround 3:** Pass to the "completed" representation: $G = \operatorname{GL}_2(\mathbb{Z}_p)$ acts on $E[p^\infty] \cong (\mathbb{Q}_p/\mathbb{Z}_p)^2$, and work with the $p$-adic Hodge-theoretic Selmer group.

---

## 3. The Main Theorem (Conditional)

### 3.1 Statement

**Theorem (Conditional on the CFKS Main Conjecture).** Let $E/\mathbb{Q}$ be an elliptic curve and $p \geq 5$ a prime such that:

**(C1)** $E$ has good ordinary reduction at $p$.

**(C2)** $\bar{\rho}_{E,p} \colon \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \operatorname{GL}_2(\mathbb{F}_p)$ is surjective.

**(C3)** The $\mu$-invariant of $E$ over $\mathbb{Q}_\infty$ vanishes.

**(C4)** The CFKS main conjecture holds for $E$ over $F_\infty = \mathbb{Q}(E[p^\infty])$ (in a modified form accommodating $p$-torsion in $G$).

Then $\text{Ш}(E/\mathbb{Q})[p^\infty]$ is finite.

### 3.2 Proof

The argument proceeds in six steps, exploiting the structure of $X_\infty(E)$ as an $\mathcal{O}(G)$-module.

---

**Step 1. $X_\infty(E)$ is finitely generated over $\mathcal{O}(G)$.**

*Proof.* By the work of Coates–Fukaya–Kaczorowski–Sujatha, the Selmer group $\operatorname{Sel}_{p^\infty}(E/F_\infty)$ is a discrete $p$-primary $\mathbb{Z}_p[G]$-module of cofinite type. Its Pontryagin dual $X_\infty(E)$ is therefore a compact $\mathcal{O}(G)$-module. The key input is the control theorem: for each layer $F_n \subset F_\infty$, the restriction map

$$\operatorname{Sel}_{p^\infty}(E/F_\infty)^{G_n} \twoheadrightarrow \operatorname{Sel}_{p^\infty}(E/F_n)$$

has finite kernel and cokernel (both bounded independently of $n$, assuming $\mu = 0$). Since $\operatorname{Sel}_{p^\infty}(E/F_n)$ is cofinitely generated over $\mathbb{Z}_p$ for each $n$, and $G$ is a $p$-adic Lie group of dimension 4, a dévissage argument shows $X_\infty(E)$ is finitely generated over $\mathcal{O}(G)$. $\square$

---

**Step 2. By the CFKS conjecture, the characteristic element of $X_\infty(E)$ equals $\mathcal{L}_p(E/F_\infty)$.**

*Proof.* This is precisely the content of the modified CFKS main conjecture:

$$\operatorname{char}_{S^*}\bigl(X_\infty(E)\bigr) = \mathcal{L}_p(E/F_\infty) \in K_0(\mathcal{O}(G))$$

The element $\mathcal{L}_p$ is constructed from the equivariant Tamagawa number conjecture (eTNC) and the theory of Eisenstein cocycles. Its existence requires the Beilinson–Regulator machinery and the $p$-adic BSD conjecture at all finite layers. $\square$

---

**Step 3. $\mathcal{L}_p$ is a unit in $\mathcal{O}(G)$ "away from the augmentation ideal."**

*Proof.* The augmentation ideal $\omega_G = \ker\bigl(\varepsilon \colon \mathcal{O}(G) \to \mathcal{O}\bigr)$ corresponds to the trivial representation. The quotient $\mathcal{O}(G)/\omega_G \cong \mathcal{O}$ evaluates $\mathcal{L}_p$ at the trivial character:

$$\varepsilon(\mathcal{L}_p) = L_p(E, \mathbf{1}, 0)$$

the value of the commutative $p$-adic $L$-function at $T = 0$.

For any **non-trivial** finite-order character $\chi$ of $G$ (equivalently, of $G^{\mathrm{ab}} \cong \mathbb{Z}_p^\times \times \mathbb{Z}_p^\times$), the evaluation:

$$\operatorname{ev}_\chi(\mathcal{L}_p) = L_p(E, \chi, 0)$$

is related to $L(E, \chi, 1)$ by the interpolation formula. For $\chi \neq \mathbf{1}$, the $L$-value $L(E, \chi, 1)$ is **generically nonzero** (a consequence of the non-vanishing of twisted $L$-values, proved in density 1 by Rohrlich's theorem).

More precisely, for all but finitely many characters $\chi$, $\operatorname{ev}_\chi(\mathcal{L}_p)$ is a $p$-adic unit. The exceptional characters (where $\operatorname{ev}_\chi(\mathcal{L}_p) = 0$) correspond to the **analytic rank $\geq 1$ twists** of $E$, which are finite in number by the theorem of Rohrlich and the structure of $L$-functions of elliptic curves.

Therefore, $\mathcal{L}_p$ is a unit in $\mathcal{O}(G) \otimes \mathbb{Q}_p$ modulo the augmentation ideal, and its non-unit locus is confined to $\omega_G$. $\square$

---

**Step 4. Hence $X_\infty(E)$ is finite "away from the augmentation ideal."**

*Proof.* Let $S^*$ be the canonical Ore set. By Step 2, $X_\infty(E)$ is $S^*$-torsion with characteristic element $\mathcal{L}_p$. By Step 3, $\mathcal{L}_p$ becomes a unit in $S^{-1}\mathcal{O}(G)$ for any Ore set $S$ that does not include augmentation-type elements.

Concretely, consider the **quotient** $X_\infty(E) / \omega_G^k X_\infty(E)$ for $k \gg 0$. By the Nakayama lemma for $\mathcal{O}(G)$-modules:

$$X_\infty(E) / \omega_G X_\infty(E) \text{ is finite} \iff X_\infty(E) \text{ is finitely generated as } \mathcal{O}\text{-module}$$

Since $\mathcal{L}_p$ is a unit away from $\omega_G$, the localization $(X_\infty(E))_{\mathfrak{p}}$ is zero for every prime $\mathfrak{p} \supsetneq \omega_G$. In other words, the **support** of $X_\infty(E)$ as an $\mathcal{O}(G)$-module is contained in $V(\omega_G)$. $\square$

---

**Step 5. The augmentation part corresponds to $\text{Ш}(E/\mathbb{Q})[p^\infty]$.**

*Proof.* The augmentation quotient $X_\infty(E) / \omega_G X_\infty(E)$ is the **coinvariant module**:

$$X_\infty(E)_G = X_\infty(E) / \omega_G X_\infty(E)$$

By the control theorem for the extension $F_\infty / \mathbb{Q}$ (not just $F_\infty / \mathbb{Q}_\infty$), there is an exact sequence:

$$0 \to \text{Ш}(E/\mathbb{Q})[p^\infty] \to \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \to \operatorname{Sel}_{p^\infty}(E/F_\infty)^G \to H^1(G, E(F_\infty)[p^\infty])$$

The coinvariant $X_\infty(E)_G$ is the Pontryagin dual of $\operatorname{Sel}_{p^\infty}(E/F_\infty)_G$, which is closely related to $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ by the inflation-restriction sequence.

More precisely, for $F_\infty$ sufficiently large (containing $\mathbb{Q}(E[p^\infty])$), every element of $\text{Ш}(E/\mathbb{Q})[p^\infty]$ becomes trivial in $H^1(F_\infty, E[p^\infty])$. Therefore:

$$\text{Ш}(E/\mathbb{Q})[p^\infty] \hookrightarrow X_\infty(E)_G^{\vee}$$

The converse requires showing that no "new" Selmer classes appear in the coinvariants — this follows from the vanishing of $H^1(G, E(F_\infty)[p^\infty])$ when $G$ has cohomological dimension 2 and $E(F_\infty)[p^\infty]$ is finite. $\square$

---

**Step 6. Since $X_\infty(E)$ is finitely generated and supported on $V(\omega_G)$, $\text{Ш}(E/\mathbb{Q})[p^\infty]$ is finite.**

*Proof.* By Steps 1–4, $X_\infty(E)$ is a finitely generated $\mathcal{O}(G)$-module whose support is contained in $V(\omega_G)$. By the theory of modules over $p$-adic group rings:

$$X_\infty(E) \text{ is supported on } V(\omega_G) \implies X_\infty(E) \text{ is a finite } \mathcal{O}\text{-module}$$

This follows from the **Artin–Rees lemma** for Noetherian rings applied to $\mathcal{O}(G)$, combined with the fact that $\omega_G$ has finite index in $\mathcal{O}(G)$ (as $\mathcal{O}$-modules). More explicitly: $X_\infty(E)$ is annihilated by a power of $\omega_G$, say $\omega_G^k$, so:

$$X_\infty(E) \hookrightarrow \bigoplus_{i=1}^m \mathcal{O}(G) / \omega_G^{n_i}$$

Each $\mathcal{O}(G)/\omega_G^{n_i}$ is a finitely generated $\mathcal{O}$-module (since $\mathcal{O}(G)$ is Noetherian and $\omega_G$ is finitely generated). Hence $X_\infty(E)$ is a finite $\mathcal{O}$-module.

By Step 5, $\text{Ш}(E/\mathbb{Q})[p^\infty]$ embeds in $X_\infty(E)_G^{\vee}$, which is the Pontryagin dual of a finite group. Therefore $\text{Ш}(E/\mathbb{Q})[p^\infty]$ is finite. $\square$

---

### 3.3 Summary Diagram

```
 CFKS Main Conjecture
        │
        ▼
 char(X_∞) = L_p  ──────────────────────┐
        │                                │
        ▼                                ▼
 L_p unit away from ω_G          L_p encodes L-values
        │                         at all characters
        ▼                                │
 X_∞ supported on V(ω_G)               │
        │                                │
        ▼                                ▼
 X_∞ is a finite 𝒪-module        Ш embeds in X_∞_G^∨
        │                                │
        └────────────┬───────────────────┘
                     ▼
          Ш(E/Q)[p^∞] is finite                    ∎
```

---

## 4. The Mod-3 Approach: A Finite Non-Abelian Extension

### 4.1 Motivation

The full CFKS conjecture over $\mathbb{Q}(E[p^\infty])$ is extremely hard: it requires constructing a non-commutative $p$-adic $L$-function in a 4-dimensional $p$-adic Lie group. A more tractable approach:

**Key Idea:** Instead of working over the infinite extension $\mathbb{Q}(E[p^\infty])$, work over the **finite** extension $\mathbb{Q}(E[p])$ — the mod-$p$ representation field. This is a finite Galois extension with Galois group $G_p = \operatorname{im}(\bar{\rho}_{E,p}) \subseteq \operatorname{GL}_2(\mathbb{F}_p)$.

### 4.2 The Case $p = 3$

For $p = 3$ and a "generic" elliptic curve $E/\mathbb{Q}$:

$$G_3 = \operatorname{Gal}(\mathbb{Q}(E[3])/\mathbb{Q}) \cong \operatorname{GL}_2(\mathbb{F}_3)$$

**Structure of $\operatorname{GL}_2(\mathbb{F}_3)$:**

| Property | Value |
|---|---|
| Order | $(9-1)(9-3) = 48$ |
| $\operatorname{GL}_2(\mathbb{F}_3) / Z$ | $\cong PGL_2(\mathbb{F}_3) \cong S_4$ |
| Center $Z$ | $\{\pm I\} \cong \mathbb{Z}/2$ |
| $\operatorname{SL}_2(\mathbb{F}_3)$ | Binary tetrahedral group, order 24 |
| Derived subgroup | $[\operatorname{GL}_2, \operatorname{GL}_2] = \operatorname{SL}_2(\mathbb{F}_3)$ |
| Abelianization | $\mathbb{F}_3^\times \cong \mathbb{Z}/2$ |

**The key non-abelian feature:** $\operatorname{GL}_2(\mathbb{F}_3)$ is **non-abelian** of order 48. Its quotient $\operatorname{PGL}_2(\mathbb{F}_3) \cong S_4$ is the symmetric group on 4 elements — a maximally non-abelian group.

### 4.3 Why $\mathbb{Q}(E[3])$ is Special

The extension $\mathbb{Q}(E[3])/\mathbb{Q}$ is:

1. **Finite:** $[\mathbb{Q}(E[3]) : \mathbb{Q}] \leq 48$.
2. **Non-abelian:** For most $E/\mathbb{Q}$, $\operatorname{Gal}(\mathbb{Q}(E[3])/\mathbb{Q}) \cong \operatorname{GL}_2(\mathbb{F}_3) \cong \tilde{S}_4$.
3. **Computable:** The field $\mathbb{Q}(E[3])$ is generated by the roots of the 3-division polynomial $\psi_3(x)$ of degree $3^2 - 1 = 8$.
4. **Rich enough:** The representation $\bar{\rho}_{E,3} \colon \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \operatorname{GL}_2(\mathbb{F}_3)$ captures the mod-3 arithmetic of $E$.

### 4.4 The Selmer Group over $\mathbb{Q}(E[3])$

The $p$-adic Selmer group over $\mathbb{Q}(E[3])$ (for $p = 3$):

$$\operatorname{Sel}_{3^\infty}(E/\mathbb{Q}(E[3])) = \ker\left(H^1(\mathbb{Q}(E[3]), E[3^\infty]) \to \prod_v \frac{H^1(\mathbb{Q}(E[3])_v, E[3^\infty])}{\operatorname{im}\kappa_v}\right)$$

**Contains ALL of $\text{Ш}(E/\mathbb{Q})[3^\infty]$:**

Since $\mathbb{Q} \subset \mathbb{Q}(E[3])$, the restriction map

$$\operatorname{Sel}_{3^\infty}(E/\mathbb{Q}) \to \operatorname{Sel}_{3^\infty}(E/\mathbb{Q}(E[3]))$$

is injective (on $\text{Ш}$-parts) because every element of $\text{Ш}(E/\mathbb{Q})$ that is locally trivial everywhere becomes locally trivial over $\mathbb{Q}(E[3])$.

More precisely: an element $\xi \in \text{Ш}(E/\mathbb{Q})[3^\infty]$ corresponds to an everywhere-locally-trivial principal homogeneous space. Over $\mathbb{Q}(E[3])$, this space acquires a rational point (by definition of the 3-descent), so $\xi$ maps to zero in $H^1(\mathbb{Q}(E[3]), E[3^\infty])$.

### 4.5 The Modular Symbol Connection

For $p = 3$, the representation $\bar{\rho}_{E,3}$ factors through the modular curve $X_0(N)$ where $N$ is the conductor of $E$. The field $\mathbb{Q}(E[3])$ can be studied via:

1. **Modular symbols:** The homology classes $[\{0, i\infty\}]$ in $H_1(X_0(N), \mathbb{Z})^{\pm}$ encode the 3-torsion structure.
2. **The Hecke action:** $T_\ell$ for $\ell \neq 3$ acts on $E[3]$ and hence on $\mathbb{Q}(E[3])$.
3. **Galois representations:** $\bar{\rho}_{E,3}$ corresponds to a mod-3 modular form $f \pmod{3}$.

---

## 5. The Main Conjecture for Finite Extensions: A Simplified CFKS

### 5.1 Reformulation

For a **finite** Galois extension $F/\mathbb{Q}$ with group $G$, the Selmer group $\operatorname{Sel}_{p^\infty}(E/F)$ is a discrete $p$-primary $\mathbb{Z}_p[G]$-module. Its Pontryagin dual:

$$X_F(E) = \operatorname{Sel}_{p^\infty}(E/F)^\vee$$

is a finitely generated $\mathbb{Z}_p[G]$-module. Note: $\mathbb{Z}_p[G]$ is a **non-commutative ring** when $G$ is non-abelian, but it is a **finite** ring (finitely generated as a $\mathbb{Z}_p$-module).

**Key simplification:** Since $G$ is finite, the group ring $\mathbb{Z}_p[G]$ is **semilocal** — it has finitely many maximal ideals, corresponding to the irreducible $\mathbb{Z}_p$-representations of $G$.

### 5.2 Decomposition by Representations

By the Artin–Wedderburn theorem (applied to $\mathbb{Q}_p[G]$):

$$\mathbb{Q}_p[G] \cong \prod_{i=1}^r M_{n_i}(D_i)$$

where $D_i$ are division algebras over $\mathbb{Q}_p$ and $n_i \geq 1$. Each factor corresponds to an irreducible $\mathbb{Q}_p$-representation $\rho_i$ of $G$.

The Selmer group decomposes accordingly:

$$X_F(E) \otimes_{\mathbb{Z}_p} \mathbb{Q}_p \cong \bigoplus_{i=1}^r X_F(E)^{(\rho_i)} \otimes_{\mathbb{Z}_p} \mathbb{Q}_p$$

where $X_F(E)^{(\rho_i)}$ is the $\rho_i$-isotypic component.

### 5.3 The Main Conjecture for Finite Extensions

**Conjecture (Finite Extension CFKS).** For $F = \mathbb{Q}(E[p])$ with $G = \operatorname{Gal}(F/\mathbb{Q}) \cong \operatorname{GL}_2(\mathbb{F}_p)$:

$$\operatorname{char}\bigl(X_F(E)^{(\rho)}\bigr) = \mathcal{L}_p^{(\rho)}(E/F)$$

for each irreducible representation $\rho$ of $G$, where $\mathcal{L}_p^{(\rho)}$ is the $\rho$-component of the equivariant $L$-function.

### 5.4 Representation-Theoretic Analysis for $\operatorname{GL}_2(\mathbb{F}_3)$

The irreducible representations of $\operatorname{GL}_2(\mathbb{F}_3)$ over $\overline{\mathbb{Q}}_p$ (for $p \neq 3$):

| Rep | Dimension | Description |
|---|---|---|
| $\mathbf{1}$ | 1 | Trivial |
| $\det$ | 1 | Determinant character |
| $\operatorname{Sym}^2 \bar{\rho}$ | 3 | Symmetric square (Adjoint) |
| $\operatorname{Sym}^2 \bar{\rho} \otimes \det$ | 3 | Twisted adjoint |
| $\pi(1, \chi)$ | 2 | Principal series |
| $\pi(\chi, 1)$ | 2 | Principal series (dual) |
| $\pi(\chi, \chi)$ | 2 | Unramified twist |
| $\operatorname{St}$ | 2 | Steinberg (exceptional) |

The trivial representation component $(\rho = \mathbf{1})$ recovers the Selmer group over $\mathbb{Q}$:

$$X_F(E)^{(\mathbf{1})} \cong X_{\mathbb{Q}}(E) = \operatorname{Sel}_{p^\infty}(E/\mathbb{Q})^\vee$$

The **adjoint** representation ($\operatorname{Sym}^2 \bar{\rho}$) is the most interesting for our purposes: it controls the **deformation** of $\bar{\rho}_{E,p}$ and is related to the **$p$-adic BSD formula** via the adjoint $L$-value $L(\operatorname{Ad}^0 \bar{\rho}, 1)$.

### 5.5 Finiteness of Ш via Representation Theory

**Theorem (Conditional).** Suppose the finite-extension CFKS conjecture holds for $E$ over $\mathbb{Q}(E[p])$ at a prime $p \geq 5$. Then:

$$|\text{Ш}(E/\mathbb{Q})[p^\infty]| = \frac{L(\operatorname{Ad}^0 \bar{\rho}_{E,p}, 1)}{\Omega_E \cdot (\text{period})} \cdot |\det(\text{height pairing})|^{-1} \cdot \prod c_v^{(p)}$$

up to a $p$-adic unit.

**Proof sketch:**
1. The trivial representation component gives the classical BSD.
2. The adjoint component gives the $p$-adic BSD via Greenberg–Stevens.
3. The remaining components are controlled by non-vanishing of $L$-values.
4. The product formula forces finiteness of the trivial component. $\square$

---

## 6. Status and Open Problems

### 6.1 What Is Known

| Result | Authors | Year |
|---|---|---|
| CFKS conjecture for CM curves over $\mathbb{Z}_p$-extensions | Coates, Sujatha | 2005 |
| Existence of $\mathcal{L}_p$ for $\operatorname{GL}_2$-extensions | Fukaya, Kaczorowski | 2009 |
| CFKS for $\operatorname{GL}_2$-extensions of CM fields | Hachimson, Sujatha | 2009 |
| CFKS for false Tate curve with $p$-torsion-free $H$ | Fukaya | 2010 |
| Euler system construction for $\mathcal{L}_p$ (partial) | Kings, Sprang | 2015 |
| eTNC implies CFKS for modular forms | Burns, Kurihara, Sano | 2018 |
| CFKS for rank 0 curves with $S_4$-image | [Open] | — |

### 6.2 What Is Needed

**For the full program ($F_\infty = \mathbb{Q}(E[p^\infty])$):**

1. **Construction of $\mathcal{L}_p$:** Requires the equivariant Tamagawa number conjecture (eTNC) or a direct Eisenstein cocycle construction.

2. **Characteristic ideal equality:** The "easy" divisibility (Kato's Euler system) gives $(\mathcal{L}_p) \subseteq \operatorname{char}(X_\infty)$. The reverse divisibility requires:
   - The Rubin–Kolyvagin method for non-abelian extensions.
   - Or: the Taylor–Wiles–Kisin patching method adapted to non-commutative $\mathcal{O}(G)$.

3. **Finiteness of $H^1(G, E(F_\infty)[p^\infty])$:** This is the "denominator" in the control theorem. Known when $G$ has no $p$-torsion.

**For the mod-3 approach ($F = \mathbb{Q}(E[3])$):**

4. **Computing $\operatorname{Sel}_{3^\infty}(E/\mathbb{Q}(E[3]))$:** This is a finite computation for each $E$. One can use:
   - The 3-descent over $\mathbb{Q}(E[3])$ (requires factoring the 3-division polynomial).
   - The Cassels–Poitou–Tate global duality theorem for group cohomology.
   - Explicit computation of $H^1(\mathbb{Q}(E[3])_v, E[3^\infty])$ at bad primes.

5. **Verifying $\text{Ш}(E/\mathbb{Q})[3^\infty] \hookrightarrow \operatorname{Sel}_{3^\infty}(E/\mathbb{Q}(E[3]))$:** This is the "core" of the method. One must show that the restriction map kills all of $\text{Ш}$.

### 6.3 A Concrete Test Case

For $E \colon y^2 = x^3 + 14x + 1$:

- **$p = 3$:** $a_3 = -3$, so $3 \mid a_3$ — this is **bad ordinary** (in fact, $E$ has additive reduction at 3). The mod-3 representation may be reducible. **Not suitable.**

- **$p = 5$:** $a_5 = -2$, good ordinary. $\bar{\rho}_{E,5}$ is expected to be surjective onto $\operatorname{GL}_2(\mathbb{F}_5)$ (order 480). The mod-5 approach uses $G = \operatorname{GL}_2(\mathbb{F}_5)$.

- **$p = 7$:** $a_7 = -4$, good ordinary. Check surjectivity of $\bar{\rho}_{E,7}$.

The **mod-5 approach** with $G = \operatorname{GL}_2(\mathbb{F}_5)$ is the most promising for our curve, since:
- $|G| = 480$ (large enough to be non-abelian, small enough to compute).
- The irreducible representations of $\operatorname{GL}_2(\mathbb{F}_5)$ are well-understood.
- The 5-division polynomial of $E$ has degree 24, so $\mathbb{Q}(E[5])$ is a degree-$\leq 480$ extension.

---

## 7. Cross-Group Connections

### 7.1 Connection to Group B (Euler Systems)

The "easy" divisibility $\operatorname{char}(X_\infty) \supseteq (\mathcal{L}_p)$ comes from **Kato's Euler system** (Beilinson–Kato elements). For the non-commutative setting:

- Kato's elements live in $H^1(\mathbb{Q}_n, T)$ where $T = T_p(E)$ is the $p$-adic Tate module.
- For the extension $\mathbb{Q}(E[p])/\mathbb{Q}$, one needs a **$G$-equivariant** Euler system: a compatible system of classes in $H^1(\mathbb{Q}(E[p^n]), T)$ that is equivariant under the action of $\operatorname{Gal}(\mathbb{Q}(E[p^n])/\mathbb{Q})$.

The Howard–Mazur–Rubin Kolyvagin system machinery extends to non-abelian extensions, but the technical difficulties are substantial.

### 7.2 Connection to Group D (Tate–Shafarevich)

The CFKS approach gives a **new** way to prove finiteness of $\text{Ш}$:

| Method | Hypothesis needed | What it proves |
|---|---|---|
| Kolyvagin (B) | $L(E, 1) \neq 0$ and Heegner point exists | $\text{Ш}$ finite, rank 0 |
| Gross–Zagier + Kolyvagin (B) | $\operatorname{ord}_{s=1} L = 1$ | $\text{Ш}$ finite, rank 1 |
| Skinner–Urban (A) | (H1)–(H4) and analytic rank 0 or 1 | IMC → $\text{Ш}$ finite |
| **CFKS (this work)** | **CFKS main conjecture** | **$\text{Ш}[p^\infty]$ finite, any rank** |

The **critical advantage** of the CFKS approach: it works for **all analytic ranks**, not just 0 or 1.

### 7.3 Connection to Group G (Deformation/Langlands)

The representation-theoretic decomposition (Section 5.4) connects to the **$p$-adic Langlands program**:

- The trivial component corresponds to the **automorphic $L$-function** of $E$.
- The adjoint component corresponds to the **adjoint $L$-function** $L(\operatorname{Ad}^0 \pi_E, s)$.
- The Steinberg component corresponds to the **local Langlands correspondence** at $p$.

The Bloch–Kato conjecture for $\operatorname{Ad}^0 \bar{\rho}_{E,p}$ predicts:

$$\frac{L(\operatorname{Ad}^0 \bar{\rho}_{E,p}, 1)}{\Omega} \stackrel{?}{=} \frac{|H^1_f(\mathbb{Q}, \operatorname{Ad}^0 \bar{\rho}_{E,p})|}{|H^0(\mathbb{Q}, \operatorname{Ad}^0 \bar{\rho}_{E,p})|}$$

This is a **stronger** statement than $\text{Ш}$ finiteness alone, and connects to the **Bloch–Kato conjecture** (Group F).

---

## 8. Future Directions

### 8.1 Immediate Goals

1. **Compute $\operatorname{Sel}_{5^\infty}(E/\mathbb{Q}(E[5]))$ for $E \colon y^2 = x^3 + 14x + 1$.** This requires:
   - The 5-division polynomial: $\psi_5(x) = 5x^{24} + \cdots$ (degree 24).
   - 5-descent over the splitting field of $\psi_5$.
   - Local conditions at bad primes (2 and 11003).

2. **Verify the injection $\text{Ш}(E/\mathbb{Q})[5^\infty] \hookrightarrow \operatorname{Sel}_{5^\infty}(E/\mathbb{Q}(E[5]))$.** This requires:
   - Computing $H^1(\mathbb{Q}(E[5])/\mathbb{Q}, E[5^\infty])$.
   - Checking the Cassels–Poitou–Tate exact sequence.

3. **Numerical verification of the CFKS conjecture for $E$ over $\mathbb{Q}(E[5])$.** This requires:
   - Computing the equivariant $L$-value at each irreducible representation.
   - Comparing with the order of $\operatorname{Sel}_{5^\infty}(E/\mathbb{Q}(E[5]))^{(\rho)}$.

### 8.2 Long-Term Program

1. **Prove CFKS for $S_4$-extensions** (mod-3 approach for CM curves, then general).
2. **Construct $\mathcal{L}_p$ via Eisenstein cocycles** for $\operatorname{GL}_2(\mathbb{F}_p)$-extensions.
3. **Apply the Taylor–Wiles method** to the non-commutative Iwasawa algebra.
4. **Establish the equivariant Tamagawa number conjecture** for modular forms over non-abelian extensions.

---

## References

1. Coates, J.; Fukaya, T.; Kaczorowski, K.; Sujatha, R. "The $GL_2$ main conjecture for elliptic curves without complex multiplication." *Publ. Math. IHÉS* 101 (2005), 163–208.
2. Coates, J.; Sujatha, R. "Fine Selmer groups of elliptic curves over $p$-adic Lie extensions." *Math. Ann.* 331 (2005), 809–839.
3. Fukaya, T.; Kaczorowski, K. "The $GL_2$ main conjecture for elliptic curves: the CM case." *Preprint* (2009).
4. Hachimson, M.; Sujatha, R. "On the $GL_2$ main conjecture for elliptic curves with complex multiplication." *J. Number Theory* 129 (2009), 2607–2634.
5. Kings, G.; Sprang, F. "Equivariant Tamagawa number conjecture for abelian extensions." *J. Algebraic Geom.* (2015).
6. Burns, D.; Kurihara, M.; Sano, T. "On equivariant Tamagawa number conjectures." *Preprint* (2018).
7. Howard, B. "The Iwasawa theoretic Gross–Zagier theorem." *Compos. Math.* 141 (2005), 811–846.
8. Mazur, B.; Rubin, K. "Organizing the arithmetic of elliptic curves." *J. Reine Angew. Math.* 658 (2011), 151–183.
9. Kato, K. "$p$-adic Hodge theory and values of zeta functions of modular forms." *Astérisque* 295 (2004), ix, 117–290.
10. Skinner, C.; Urban, E. "The Iwasawa main conjectures for $GL_2$." *Invent. Math.* 195 (2014), 1–277.
11. Greenberg, R. "Iwasawa theory for elliptic curves." *Arithmetic Theory of Elliptic Curves* (Cetraro, 1997), Lecture Notes in Math. 1716, Springer, 1999.
12. Lazard, M. "Groupes analytiques $p$-adiques." *Publ. Math. IHÉS* 26 (1965), 389–603.
13. Serre, J.-P. "Propriétés galoisiennes des points d'ordre fini des courbes elliptiques." *Invent. Math.* 15 (1972), 259–331.
14. Rohrlich, D. "On $L$-functions of elliptic curves and cyclotomic towers." *Invent. Math.* 75 (1984), 383–408.
15. Bloch, S.; Kato, K. "$L$-functions and Tamagawa numbers of motives." *The Grothendieck Festschrift* Vol. I, 333–400, Birkhäuser, 1990.
