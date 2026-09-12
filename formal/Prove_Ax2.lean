/-
Prove_Ax2.lean — Proof of Jacobian Torsion Triviality
Lean 4 / Mathlib4

For a finite abelian group G of order n, and a prime p > n,
the p-torsion G[p] = 0.

Mathematical proof:
  1. G is a finite group of order n
  2. By Lagrange's theorem, the order of every element divides n
  3. If g ∈ G[p], then p • g = 0 and the order of g divides p
  4. Since p is prime, ord(g) = 1 or ord(g) = p
  5. If ord(g) = p, then p | n (by Lagrange), contradicting p > n
  6. So ord(g) = 1, meaning g = 0

This result is the key lemma behind the axiom `jacobian_ptorsion_rational_bound`
in Axioms_BSD.lean: for J₀(N)(Q) a finite abelian group of order T,
any prime p > T yields J₀(N)[p]^{G_Q} = 0.
-/

import Mathlib.GroupTheory.Torsion
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.GroupTheory.OrderOfElement

/-- **Jacobian torsion triviality.**
    For a finite abelian group G, if p > |G| is prime, then G has no
    nonzero p-torsion element: p • g = 0 implies g = 0.

    *Proof.* The additive order of g divides p (since p • g = 0) and
    divides |G| (Lagrange).  Since p is prime, ord(g) ∈ {1, p}.
    If ord(g) = p then p | |G|, contradicting p > |G|.
    So ord(g) = 1, hence g = 0. -/
theorem jacobian_torsion_trivial
    (G : Type*) [AddCommGroup G] [Fintype G]
    (p : ℕ) (hp : Nat.Prime p)
    (h_large : p > Fintype.card G) :
    ∀ g : G, p • g = 0 → g = 0 := by
  intro g hg
  -- The order of g divides p (since p • g = 0)
  have h_ord_dvd : addOrderOf g ∣ p :=
    addOrderOf_dvd_of_nsmul_eq_zero hg
  -- The order of g divides |G| (Lagrange's theorem)
  have h_ord_dvd_card : addOrderOf g ∣ Fintype.card G :=
    addOrderOf_dvd_card_univ
  -- Since p is prime, addOrderOf g = 1 or addOrderOf g = p
  have h_eq_one : addOrderOf g = 1 := by
    rcases (Nat.dvd_prime hp).mp h_ord_dvd with h | h
    · exact h  -- addOrderOf g = 1
    · -- addOrderOf g = p, contradiction with p > |G|
      exfalso
      have : p ∣ Fintype.card G := h ▸ h_ord_dvd_card
      have hpos : 0 < Fintype.card G := Fintype.card_pos_iff.mpr ⟨0⟩
      linarith [Nat.le_of_dvd hpos this]
  -- addOrderOf g = 1 implies g = 0
  exact addOrderOf_eq_one_iff.mp h_eq_one
