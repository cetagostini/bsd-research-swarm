/-
OneSmallLemma.lean — A small lemma about element orders in finite groups

For a finite abelian group G, if p > |G| then G has no element of order p.

This is an immediate consequence of Lagrange's theorem: the order of any
element divides the group order, so an element of order p requires p | |G|,
which contradicts p > |G| when |G| > 0.
-/

import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Data.Fintype.Basic

/-- For a finite abelian group G, if p > |G| then G has no element of order p. -/
theorem no_element_of_large_prime_order
    (G : Type*) [AddCommGroup G] [Fintype G]
    (p : ℕ) (hp : Nat.Prime p)
    (h : p > Fintype.card G) (g : G) (hg : addOrderOf g = p) : False := by
  -- By Lagrange's theorem, addOrderOf g ∣ Fintype.card G
  have h_dvd : addOrderOf g ∣ Fintype.card G := addOrderOf_dvd_card_univ
  -- Substituting the hypothesis addOrderOf g = p
  rw [hg] at h_dvd
  -- Since |G| > 0 (G is nonempty as it contains 0), p | |G| implies p ≤ |G|
  have h_pos : 0 < Fintype.card G := Fintype.card_pos_iff.mpr ⟨0⟩
  -- Contradiction: p ≤ |G| but p > |G|
  exact absurd (Nat.le_of_dvd h_pos h_dvd) (not_le.mpr h)
