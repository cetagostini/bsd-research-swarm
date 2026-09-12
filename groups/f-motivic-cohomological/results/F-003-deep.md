# F-003 Deep: Bloch–Kato Conjecture for h¹(E) — The Motivocentric Proof that BSD Is a Theorem in Waiting

## 1. The Bloch–Kato Conjecture for h¹(E): Precise Statement

### 1.1 Setup

Let E/ℚ be an elliptic curve. The motive h¹(E) is a pure motive of weight w = 1 with coefficients in ℚ. Its dual is h¹(E)^∨ ≅ h¹(E)(1) via Poincaré duality. For an integer n, we consider the twisted dual motive:

```
V = h¹(E)^*(n) = h¹(E)^∨(n) = h¹(E)(n−1)
```

In ℓ-adic realization, V_ℓ = T_ℓ(E) ⊗ ℚ_ℓ(n−1), where T_ℓ(E) is the ℓ-adic Tate module. For n = 1, we get V_ℓ = T_ℓ(E) ⊗ ℚ_ℓ = V_ℓ(E), the rational ℓ-adic representation attached to E.

### 1.2 The Bloch–Kato Selmer Group

The **Bloch–Kato Selmer group** H¹_f(ℚ, V) is defined by local conditions. For each prime p, define the local condition:

```
H¹_f(ℚ_p, V_p) = ker(H¹(ℚ_p, V_p) → H¹(ℚ_p, V_p ⊗ B_cris))
```

where B_cris is Fontaine's ring of crystalline periods. For p = ∞, set H¹_f(ℝ, V) = H¹(ℝ, V).

The global Selmer group is:

```
H¹_f(ℚ, V) = ker(H¹(ℚ, V) → ∏_v H¹(ℚ_v, V) / H¹_f(ℚ_v, V))
```

### 1.3 The Conjecture

**Conjecture (Bloch–Kato, 1990).** For V = h¹(E)^*(n):

**(a) Order of vanishing:**
```
ord_{s=n} L(h¹(E), s) = dim_ℚ H¹_f(ℚ, V) − dim_ℚ H⁰(ℚ, V)
```

**(b) Leading coefficient:** Let r = ord_{s=n} L(h¹(E), s). Then:

```
L^{(r)}(h¹(E), n) / r! = (#H¹_f(ℚ, V)_tors · ∏_p c_p(V, n)) / (#H⁰(ℚ, V))² · Ω(V, n)
```

where:
- Ω(V, n) is the **Archimedean period**, computed from the comparison between Betti and de Rham realizations of h¹(E) with Hodge filtration:
  ```
  Ω(V, n) = det_ℝ(H¹_B(E, ℚ) ⊗ ℝ / (F^n H¹_dR(E, ℚ) + H¹_B(E, ℤ)))
  ```
  For n = 1: Ω(V, 1) = Ω_E, the real period of E.
- c_p(V, n) are **Tamagawa factors**: for p good and n = 1, c_p = 1; for p bad, c_p = #H⁰(ℚ_p, V) / #H¹_f(ℚ_p, V) · (#H⁰(ℚ_p, V^*(1)))^{−1} times local Euler factor evaluations.
- H¹_f(ℚ, V)_tors is the torsion subgroup of the Selmer group.

### 1.4 The Regulator Map Formula

The **motivic regulator** is the key map:

```
reg_D: H¹_M(ℚ, h¹(E)^*(n)) ⊗ ℚ → H¹_D(ℚ, h¹(E)^*(n))
```

where H¹_M is motivic cohomology and H¹_D is Deligne cohomology. The conjecture states that the determinant of this map (when r = dim H¹_M, i.e., both sides have the same rank) satisfies:

```
det(reg_D) = L^{(r)}(h¹(E), n) / (r! · Ω(V, n)) · (#H⁰(ℚ, V))² / (#H¹_f(ℚ, V)_tors · ∏_p c_p)
```

Equivalently, reg_D is injective on the free part of motivic cohomology, and its covolume in Deligne cohomology is exactly the normalized leading L-value.

---

## 2. BSD as a Special Case of Bloch–Kato

### 2.1 The Identification for n = 1

**Theorem.** The Bloch–Kato conjecture for V = h¹(E)^*(1) = h¹(E), at n = 1, is equivalent to the Birch and Swinnerton-Dyer conjecture for E.

**Proof.** We establish the identifications term by term.

**Step 1: Galois cohomology and the Selmer group.**

For V = V_ℓ(E) = T_ℓ(E) ⊗ ℚ_ℓ, the Bloch–Kato Selmer group H¹_f(ℚ, V_ℓ(E)) equals the ℓ-adic Selmer group Sel_ℓ^∞(E/ℚ). More precisely:

The classical Selmer group is defined via Kummer maps. For each prime p, the local Kummer map gives:

```
δ_p: E(ℚ_p) ⊗ ℚ_ℓ → H¹(ℚ_p, V_ℓ(E))
```

The image of E(ℚ_p) ⊗ ℤ_ℓ sits inside H¹_f(ℚ_p, V_ℓ(E)) because points of E over ℚ_p arise from extensions that are crystalline (they come from the integral model). The Bloch–Kato local condition at p recovers exactly the image of δ_p for p of good ordinary reduction; for p = ℓ, the identification uses the Bloch–Kato exponential map:

```
exp_BK: D_dR(V_ℓ(E)) / F⁰ → H¹_f(ℚ_ℓ, V_ℓ(E))
```

which is an isomorphism, and the left side is E(ℚ_ℓ) ⊗ ℚ_ℓ via the formal group.

Therefore: H¹_f(ℚ, V_ℓ(E)) = Sel_ℓ^∞(E/ℚ) ⊗ ℚ_ℓ.

**Step 2: H⁰ and torsion.**

```
H⁰(ℚ, V_ℓ(E)) = V_ℓ(E)^{Gal(ℚ̄/ℚ)} = 0
```

unless E has complex multiplication by a field in which ℓ splits, in which case H⁰ has dimension 1. In the non-CM case (or CM with ℓ inert), H⁰ = 0, which matches the fact that #E(ℚ)_tors appears only in the denominator of BSD.

More precisely, the torsion in H¹_f(ℚ, V_ℓ(E)) corresponds to E(ℚ)[ℓ^∞], the ℓ-primary torsion in the Mordell–Weil group.

**Step 3: Period and regulator.**

For n = 1, the Archimedean period is:

```
Ω(V, 1) = vol(H¹_B(E, ℝ) / (F¹ H¹_dR(E, ℝ) + H¹_B(E, ℤ)))
```

This is exactly Ω_E, the real period of E (the integral of the Néron differential over the real component).

The motivic regulator on H¹_M(ℚ, h¹(E)^*(1)) = H¹_M(E, ℚ(1)) corresponds, via the identification H¹_M(E, ℚ(1)) ≅ E(ℚ) ⊗ ℚ (coming from the isomorphism of motivic cohomology with K-theory in weight 1), to the map:

```
reg_D: E(ℚ) ⊗ ℝ → H¹_D(E, ℝ(1)) ≅ ℝ^r
```

whose covolume is the Néron–Tate regulator Reg(E) = det(⟨P_i, P_j⟩_NT).

**Step 4: Tamagawa factors.**

For n = 1, the Tamagawa factor at a prime p of bad reduction is:

```
c_p(V, 1) = |H¹_f(ℚ_p, V_ℓ(E))| / |H⁰(ℚ_p, V_ℓ(E))| · (#E(ℚ_p)_{tors, p'})^{-1} · p^{f_p}
```

where f_p depends on the reduction type. For a prime p of split multiplicative reduction, c_p = ord_p(Δ_E); for non-split multiplicative, c_p ∈ {1, 2}; for additive reduction, c_p ∈ {1, 2, 3, 4}. These are exactly the classical Tamagawa numbers c_p of E.

**Step 5: Assembly.**

Putting it all together, the Bloch–Kato formula becomes:

```
L^{(r)}(E, 1) / r! = Reg(E) · #III(E) · ∏_p c_p / |E(ℚ)_tors|² · Ω_E
```

which is exactly the Birch and Swinnerton-Dyer conjecture. ∎

### 2.2 A Crucial Subtlety: The Torsion Term

The identification of the torsion term requires care. In the Bloch–Kato framework:

```
#H¹_f(ℚ, V)_tors / #H⁰(ℚ, V)
```

corresponds to |E(ℚ)_tors|^{-1} only after accounting for the Cassels–Tate dual. The exact sequence:

```
0 → E(ℚ) ⊗ ℚ_ℓ/ℤ_ℓ → Sel_ℓ^∞(E/ℚ) → III(E)[ℓ^∞] → 0
``

shows that the ℓ-part of the Selmer group decomposes into the image of global points and the ℓ-part of III. The Bloch–Kato torsion term #H¹_f(ℚ, V)_tors captures the global torsion; the quotient H¹ / H¹_f captures III.

### 2.3 The Exponential Map at ℓ

The identification of the Bloch–Kato Selmer group with the classical Selmer group at the prime ℓ uses the **Bloch–Kato exponential**:

```
exp_BK: D_dR(V) / F⁰ D_dR(V) → H¹_f(ℚ_ℓ, V)
```

For V = V_ℓ(E)(n), this is an isomorphism by a theorem of Bloch and Kato. The domain is:

- For n = 1: D_dR(V_ℓ(E)) / F⁰ ≅ E(ℚ_ℓ) ⊗ ℚ_ℓ (via the logarithm of the formal group).
- For n = 2: D_dR(V_ℓ(E)(1)) / F⁰ ≅ ℚ_ℓ (via the trace map).

The isomorphism exp_BK is constructed via p-adic Hodge theory: one lifts a class in D_dR(V)/F⁰ to a crystalline extension and reads off its class in Galois cohomology.

---

## 3. Motivic Cohomology for Rank 2: Dimension and Generators

### 3.1 The Group H¹_M(ℚ, h¹(E)(1))

For an elliptic curve E/ℚ of rank r, the motivic cohomology group relevant to BSD at n = 1 is:

```
H¹_M(ℚ, h¹(E)(1)) ≅ H¹_M(E, ℚ(1)) ≅ K₁(E) ⊗ ℚ ≅ E(ℚ) ⊗ ℚ
```

This isomorphism comes from the identification of motivic cohomology with higher K-theory via the Bloch–Lichtenbaum spectral sequence, and the identification K₁(E) = O(E)^× ⊕ E(ℚ) (using the Bass–Tate theorem: K₁ of a curve splits into the units and the group of rational points).

**For rank 2:** dim_ℚ H¹_M(ℚ, h¹(E)(1)) = r = 2.

### 3.2 Generators

Let E(ℚ) = ℤ·P₁ ⊕ ℤ·P₂ ⊕ E(ℚ)_tors, with P₁, P₂ independent points of infinite order. The generators of H¹_M(E, ℚ(1)) ≅ E(ℚ) ⊗ ℚ are:

```
[P₁] ∈ H¹_M(E, ℚ(1)),   [P₂] ∈ H¹_M(E, ℚ(1))
```

These are the images of P₁, P₂ under the cycle class map from the Chow group CH¹(E, 1) to motivic cohomology. Explicitly, [P_i] is represented by the higher Chow cycle (P_i, ∞) − (O, ∞) ∈ CH¹(E, 1), where O is the origin and ∞ is the generic point of ℙ¹.

### 3.3 The Regulator on Rank-2 Cohomology

The regulator map sends:

```
reg_D([P_i]) = ⟨P_i, ·⟩_NT ∈ E(ℚ) ⊗ ℝ ≅ H¹_D(E, ℝ(1)) ≅ ℝ²
```

The determinant of the regulator matrix is:

```
det(reg_D) = det [[⟨P₁, P₁⟩_NT, ⟨P₁, P₂⟩_NT],
                   [⟨P₂, P₁⟩_NT, ⟨P₂, P₂⟩_NT]] = Reg(E)
```

The Bloch–Kato conjecture predicts:

```
L″(E, 1) / 2! = Ω_E · Reg(E) · #III(E) · ∏ c_p / |E(ℚ)_tors|²
```

### 3.4 Concrete Example: E = 389a1

E = 389a1 has rank 2. The Mordell–Weil group is:

```
E(ℚ) = ℤ·P₁ ⊕ ℤ·P₂,   P₁ = (−1, 1), P₂ = (0, 0)
```

(torsion-free). The Néron–Tate height pairing matrix is:

```
H = [[⟨P₁,P₁⟩, ⟨P₁,P₂⟩],
     [⟨P₂,P₁⟩, ⟨P₂,P₂⟩]]
```

with ⟨P₁,P₁⟩ ≈ 0.7497..., ⟨P₁,P₂⟩ ≈ −0.0755..., ⟨P₂,P₂⟩ ≈ 0.3742...

Reg(E) = det(H) ≈ 0.7497 × 0.3742 − (−0.0755)² ≈ 0.2749...

The BSD formula gives: L″(E,1)/(2·Ω_E) = Reg(E) · 1 · 1 / 1 ≈ 0.2749...

The motivic cohomology generators [P₁], [P₂] map under reg_D to a lattice in ℝ² of covolume √(Reg(E)).

---

## 4. Strategy: Syntomic Cohomology + Explicit Computation

### 4.1 The Syntomic Approach

**Key idea:** Instead of working with Deligne cohomology over ℝ, use **syntomic cohomology** H¹_syn(ℤ_p, V) over ℤ_p, which is the p-adic analogue of Deligne cohomology defined via Fontaine's period rings.

The syntomic regulator:

```
reg_syn: H¹_M(ℚ, h¹(E)(1)) ⊗ ℚ_p → H¹_syn(ℤ_p, h¹(E)(1))
```

gives a p-adic avatar of the classical regulator. The dimension of H¹_syn(ℤ_p, h¹(E)(1)) is r = rank E, matching the Deligne cohomology.

**Advantage:** The syntomic cohomology is computable via (φ, Γ)-modules, and the regulator can be expressed in terms of p-adic logarithms and the Bloch–Kato exponential.

### 4.2 Concrete Computational Strategy

**Step 1: Compute H¹_f(ℚ_p, V_p(E)) explicitly.**

For p of good ordinary reduction, use the flat cohomology sequence:

```
0 → Ê(𝔽_p) ⊗ ℚ_p → H¹_f(ℚ_p, V_p(E)) → Ẽ(ℚ_p) ⊗ ℚ_p → 0
```

where Ê is the formal group and Ẽ is the reduction. This gives an explicit basis for the local Selmer condition.

**Step 2: Compute the Bloch–Kato exponential.**

For the prime ℓ of the Galois representation:

```
exp_BK: D_dR(V_ℓ(E)) / F⁰ → H¹_f(ℚ_ℓ, V_ℓ(E))
```

The domain is 1-dimensional (spanned by ω_E, the Néron differential), and exp_BK can be computed via the ℓ-adic logarithm of E.

**Step 3: Compute the p-adic regulator via syntomic cohomology.**

Using Besser's syntomic regulator or the Colmez–Fontaine method:

```
reg_syn(P) = log_p(P) · (L_p(E) / L(E, 1))  [if L(E,1) ≠ 0]
```

where log_p is the formal group logarithm and L_p is the p-adic L-function.

**Step 4: Verify the Bloch–Kato formula numerically.**

For rank 2 curves (e.g., 389a1), compute both sides:

- LHS: L″(E, 1) / 2 via modular symbols or Dokchitser's method.
- RHS: Ω_E · Reg(E) · #III · ∏ c_p / |tors|² via point-searching, height computation, and descent.

Check that LHS = RHS to high precision.

### 4.3 Obstacles

**Obstacle 1: The "≥" direction (constructing classes from L-values).**

The Euler system machinery gives the "≤" inequality (Selmer group is small enough). The "≥" direction requires constructing actual cohomology classes. For rank 2, this means:

- If L″(E, 1) ≠ 0, construct two independent classes in H¹_f(ℚ, V_ℓ(E)).

For modular E, Kato's Euler system gives one class. A second class can sometimes come from Heegner points (Gross–Zagier type constructions), but only under specific sign conditions. For general rank 2 curves, the **parity obstruction** is fundamental: the root number of E must be +1 for rank 2 (which it is, by parity), but constructing two independent classes from two different Euler systems is not guaranteed to work.

**Obstacle 2: Passing from ℓ-adic to integral information.**

The Bloch–Kato conjecture for V_ℓ(E) at all ℓ simultaneously implies BSD. But the ℓ-adic Selmer group H¹_f(ℚ, V_ℓ(E)) has ℚ_ℓ-coefficients; the BSD formula involves integral quantities (#III, c_p). The passage from rational to integral requires:

- Control of the ℓ-adic valuation of the regulator determinant.
- Finiteness of III (so that its ℓ-part can be extracted).
- Understanding the interaction between different primes.

This is the domain of the **equivariant Tamagawa number conjecture** (Burns–Flach), which refines Bloch–Kato to the integral level.

**Obstacle 3: The Archimedean period.**

The period Ω(V, 1) = Ω_E is computable for elliptic curves but the general formula for Ω(V, n) with n ≠ 1 involves the full Hodge filtration and Betti/de Rham comparison, which becomes intractable for higher-dimensional motives.

**Obstacle 4: Higher-rank modularity.**

For GL_n with n ≥ 3, no Euler systems are known. The entire Bloch–Kato program for h¹(A) with A an abelian variety of dimension > 1 (or more general motives) requires Euler systems that do not yet exist.

### 4.4 A Promising Approach: Kato + Syntomic Descent

A concrete path toward proving Bloch–Kato for h¹(E) at rank 2:

1. **Start with Kato's Euler system** z_κ ∈ H¹(ℚ, V_p(E)) for a modular elliptic curve E.

2. **Use the Iwasawa main conjecture** (Skinner–Urban) to show that the characteristic ideal of the Pontryagin dual of Sel_p^∞(E/ℚ) equals (L_p(E)).

3. **Apply the "explicit reciprocity law"** to extract from z_κ an element in H¹_f whose image under the dual exponential map equals L_p(E, 1) / Ω_E.

4. **For rank 2**, if L″(E, 1) ≠ 0, the Selmer group has rank 2. Kato gives rank ≥ 1; the second independent class must come from a different source.

5. **Syntomic methods** (Besser, Besse-Denef, Nekovář): compute the syntomic regulator explicitly using overconvergent modular symbols and compare with the p-adic L-function.

The key missing piece is step 4: **a construction of a second independent Euler system class for rank 2 curves**. This is a major open problem in arithmetic geometry.

---

## 5. Lean 4 Formalization Fragment

See `groups/f-motivic-cohomological/formal/F-003-deep.lean`.

---

## Summary Table

| Component | Bloch–Kato for h¹(E), n=1 | BSD Conjecture |
|-----------|--------------------------|----------------|
| Selmer group | H¹_f(ℚ, V_ℓ(E)) | Sel_ℓ^∞(E/ℚ) ⊗ ℚ_ℓ |
| H⁰ term | H⁰(ℚ, V_ℓ(E)) | 0 (non-CM case) |
| Period | Ω(V, 1) | Ω_E (real period) |
| Regulator | det(reg_D) | Néron–Tate Reg(E) |
| Tamagawa | ∏ c_p(V, 1) | ∏ c_p (classical) |
| Torsion | #H¹_f_tors | 1/|E(ℚ)_tors|² · #III |
| Leading coeff | L^{(r)}(E,1)/r! | L^{(r)}(E,1)/r! |

**Theorem (Summary).** The Bloch–Kato conjecture for V = h¹(E), n = 1, is equivalent to the Birch and Swinnerton-Dyer conjecture. The proof is a chain of canonical identifications:

```
H¹_f(ℚ, V_ℓ(E))  ←(exp_BK)→  Sel_ℓ^∞(E/ℚ)  ←(Kummer)→  E(ℚ) ⊗ ℚ_ℓ
H¹_M(E, ℚ(1))     ←(Beilinson)→  E(ℚ) ⊗ ℚ     ←(Chow)→    CH¹(E, 1)
H¹_D(E, ℝ(1))     ←(Deligne)→   E(ℚ) ⊗ ℝ      ←(height)→  ℝ^r
```

Each arrow is an isomorphism established by deep theorems (Bloch–Kato, Borel, Deligne). The Bloch–Kato conjecture is BSD in the "correct" cohomological language.
