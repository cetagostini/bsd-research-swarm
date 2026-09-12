/-
Prove_Ax1.lean — Left-Exactness of the G-Invariant Functor
Lean 4 / Mathlib4

Left-exactness of the fixed-point functor (·)^G:
  If f : A →+ B is an injective G-equivariant homomorphism,
  then f restricted to A^G →+ B^G is injective.

Corollary for short exact sequences of G-modules:
  0 → A → B  exact  ⟹  0 → A^G → B^G  exact
  (the rightmost map A^G → B^G → C^G need not be surjective).

Application to the universal visibility proof:
  Taking G_Q-invariants of 0 → K[p] → J₀(N)[p] → E[p] yields
    0 → K[p]^{G_Q} → J₀(N)[p]^{G_Q} → E[p]^{G_Q}
  Left-exactness ensures K[p]^{G_Q} ↪ J₀(N)[p]^{G_Q}.

This replaces the axiom `gqInvariants_injective` from Axioms_BSD.lean
with a proof for the general group-action setting.
-/

import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.GroupTheory.GroupAction.Basic

-- ═══════════════════════════════════════════════════════════════
-- § 1.  Fixed-point subgroup
-- ═══════════════════════════════════════════════════════════════

/-- The fixed-point additive subgroup A^G = {a : A | ∀ g : G, g • a = a}
    under a distributive multiplicative action of a monoid G on an
    additive commutative group A.

    When G = G_Q (the absolute Galois group), this recovers the
    G_Q-invariant submodule used in the universal visibility proof. -/
def fixedPoints (G A : Type*)
    [Monoid G] [AddCommGroup A] [DistribMulAction G A] :
    AddSubgroup A where
  carrier := {a | ∀ g : G, g • a = a}
  zero_mem' := smul_zero
  add_mem' {a b} ha hb g := by rw [smul_add, ha g, hb g]
  neg_mem' {a} ha g := by rw [smul_neg, ha g]

-- ═══════════════════════════════════════════════════════════════
-- § 2.  Restriction of equivariant maps to fixed points
-- ═══════════════════════════════════════════════════════════════

/-- If f : A →+ B is a G-equivariant additive monoid homomorphism,
    it restricts to a map A^G →+ B^G on fixed-point subgroups.

    Well-definedness: if a ∈ A^G then f(a) ∈ B^G because
      g • f(a) = f(g • a) = f(a)   (by equivariance and a being fixed). -/
def AddMonoidHom.restrictFixedPoints {G A B : Type*}
    [Monoid G] [AddCommGroup A] [AddCommGroup B]
    [DistribMulAction G A] [DistribMulAction G B]
    (f : A →+ B)
    (h_compat : ∀ (a : A) (g : G), f (g • a) = g • f a) :
    fixedPoints G A →+ fixedPoints G B where
  toFun a := ⟨f a.1, fun g => by rw [← h_compat a.1 g, a.2 g]⟩
  map_zero' := Subtype.ext (map_zero f)
  map_add' a b := Subtype.ext (map_add f a.1 b.1)

-- ═══════════════════════════════════════════════════════════════
-- § 3.  Left-exactness of the invariant functor
-- ═══════════════════════════════════════════════════════════════

/-- **Left-exactness of the G-invariant functor.**

    If f : A →+ B is an injective G-equivariant homomorphism,
    then f restricted to A^G →+ B^G is injective.

    This is the key property making (·)^{G_Q} left-exact:
    given a short exact sequence 0 → A → B → C of G-modules,
    taking G-invariants yields 0 → A^G → B^G → C^G
    (the last map need not be surjective; this is Galois cohomology).

    *Proof.* Trivially, if f(a) = f(b) in B then a = b by injectivity
    of f.  The content is that the restriction map is well-defined:
    equivariance ensures fixed points map to fixed points. -/
theorem invariant_injective {G A B : Type*}
    [Monoid G] [AddCommGroup A] [AddCommGroup B]
    [DistribMulAction G A] [DistribMulAction G B]
    (f : A →+ B) (hf : Function.Injective f)
    (h_compat : ∀ (a : A) (g : G), f (g • a) = g • f a) :
    Function.Injective (f.restrictFixedPoints h_compat) := by
  intro a b h
  apply Subtype.ext
  exact hf (Subtype.ext_iff.mp h)
