-- D-009: III over Function Fields
-- Lean 4 fragment: Sha over F_q(t) and the Artin-Tate conjecture

import Mathlib.AlgebraicGeometry.EllipticCurve.Weierstrass
import Mathlib.NumberTheory.FunctionField

/-! # D-009: The Tate-Shafarevich Group over Function Fields

    For E/F_q(t) with non-constant j-invariant, Sha is finite
    and satisfies the function-field BSD formula (Tan, 2021).
-/

namespace BSD.TateShafarevich.D009

variable {F : Type*} [Field F] [Fintype F]

/-- An elliptic curve E over F_q(t). -/
def EllipticCurveFF (F : Type*) [Field F] [Fintype F] : Type := sorry

/-- The function field F_q(t). -/
def FunctionField (F : Type*) [Field F] : Type := sorry

/-- Sha(E/F_q(t)). -/
def TateShafarevichFF (E : Type*) : Type := sorry

/-- The Artin-Tate conjecture: for E/F_q(t) with non-constant j,
    Sha is finite and satisfies BSD. -/
theorem artin_tate_conjecture (E : Type*) [EllipticCurveFF F E]
    (h_nonconst : sorry) -- non-constant j-invariant
    : Finite (TateShafarevichFF E) := sorry

/-- The Goss L-function L(E/F_q(t), s). -/
def GossLFunction (E : Type*) : Type := sorry

/-- The function-field BSD formula:
    L(E/F_q(t), 1) = |Sha| · ∏ c_v · deg(ĥ) / |E(F_q(t))_tors|² -/
theorem function_field_bsd (E : Type*) [EllipticCurveFF F E]
    (h_nonconst : sorry) (h_fin : Finite (TateShafarevichFF E)) :
    sorry := sorry

/-- Geisser (2004): Sha[p] = 0 for p ≠ char(F_q). -/
theorem geisser_vanishing (E : Type*) [EllipticCurveFF F E]
    (p : ℕ) [Fact (Nat.Prime p)]
    (h_p : p ≠ Fintype.card F) : -- p ≠ char
    TateShafarevichFF E = sorry := sorry

/-- The Artin-Tate duality for Sha over function fields. -/
def ArtinTateDuality (E : Type*) : Type := sorry

/-- The Néron-Severi group of the associated surface S. -/
def NeronSeveri (E : Type*) : Type := sorry

/-- |Sha| = |det(intersection matrix on NS)| / (∏ c_v · |tors|²). -/
theorem sha_from_neron_severi (E : Type*) [EllipticCurveFF F E] :
    sorry := sorry

/-- Ulmer's construction: E/F_q(t) with arbitrarily large rank. -/
def UlmerCurve (F : Type*) [Field F] [Fintype F] (n : ℕ) : Type := sorry

/-- The Brauer group of S. -/
def BrauerGroup (E : Type*) : Type := sorry

/-- The exact sequence relating Sha and the Brauer group. -/
theorem sha_brauer_exact (E : Type*) :
    ∃ (f : TateShafarevichFF E → BrauerGroup E),
      sorry := sorry

/-- The Tate conjecture for surfaces over finite fields
    (proved by Tate for abelian varieties). -/
theorem tate_conjecture_surfaces (S : Type*) :
    sorry := sorry

/-- The Weil conjectures give rationality and functional equation
    of the zeta function of S. -/
theorem weil_conjectures (S : Type*) :
    sorry := sorry

/-- For E/Q(t), finiteness of Sha is open. -/
theorem number_field_base_open (E : Type*) :
    sorry := sorry -- open problem

end BSD.TateShafarevich.D009
