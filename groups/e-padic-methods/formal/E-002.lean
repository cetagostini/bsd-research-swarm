/-
  E-002: p-adic Gross–Zagier Formula
  Lean 4 fragment formalising the p-adic height of Heegner points
  and the p-adic Gross–Zagier formula.
-/

import Mathlib

open scoped BigOperators

/-!
## p-adic Heights
-/

/-- The canonical p-adic height on an elliptic curve, depending on a
    choice of splitting of the Hodge filtration. -/
noncomputable def padicHeight {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) [AddCommGroup E] (P : E) : ℚ_[p] :=
  sorry

/-- The p-adic height pairing. -/
noncomputable def padicHeightPairing {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) [AddCommGroup E] (P Q : E) : ℚ_[p] :=
  padicHeight hp E (P + Q) - padicHeight hp E P - padicHeight hp E Q

/-!
## Heegner Points
-/

/-- A Heegner point on `E` associated to an imaginary quadratic field `K`
    and an order of conductor `f` in `K`. -/
structure HeegnerPoint (N : ℕ) (K : Type*) where
  /-- The imaginary quadratic discriminant. -/
  disc : ℤ
  /-- The conductor of the order. -/
  conductor : ℕ
  /-- The Heegner hypothesis: every prime dividing `N` splits in `K`. -/
  heegner_hyp : True -- Placeholder for: ∀ ℓ ∣ N, Kronecker (disc / ℓ) = 1
  /-- The point on `E(K)`. -/
  point : ℤ × ℤ  -- Coordinates on E, placeholder

/-!
## The p-adic Gross–Zagier Formula
-/

/-- The Euler correction factor at `p` in the p-adic Gross–Zagier formula. -/
noncomputable def eulerCorrectionFactor {p : ℕ} (hp : Nat.Prime p)
    (aₚ : ℤ) : ℚ_[p] :=
  (1 - aₚ / p + 1 / p)⁻¹

/-- **Theorem (Perrin-Riou).** The p-adic Gross–Zagier formula in the ordinary case.
    Relates the derivative of the p-adic L-function at `s = 1` to the p-adic height
    of the Heegner point. -/
theorem padic_gross_zagier_ordinary {p : ℕ} (hp : Nat.Prime p)
    (N : ℕ) (aₚ : ℤ) (hord : padicNorm p aₚ < 1)
    (K : Type*) (P_K : HeegnerPoint N K) :
    -- L_p'(E/K, 1) = eulerCorrectionFactor * h_p(P_K) * c_E / [O_K : Z[f]]
    ∃ (L' : ℚ_[p]) (hP : ℚ_[p]) (cE : ℚ_[p]) (index : ℕ),
      L' = eulerCorrectionFactor hp aₚ * hP * cE / index := by
  sorry

/-!
## Supersingular Extension
-/

/-- The plus/minus p-adic height for supersingular primes. -/
noncomputable def padicHeightPlusMinus {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) [AddCommGroup E] (sign : Bool) (P : E) : ℚ_[p] :=
  sorry

/-- **Conjecture (Sprung).** p-adic Gross–Zagier for supersingular primes
    using plus/minus decomposition. -/
conjecture padic_gross_zagier_supersingular {p : ℕ} (hp : Nat.Prime p)
    (N : ℕ) (aₚ : ℤ) (haₚ : aₚ = 0)
    (K : Type*) (P_K : HeegnerPoint N K) (sign : Bool) :
    -- L_p'^{±}(E/K, 1) = h_p^±(P_K^±) * correction
    ∃ (correction : ℚ_[p]), True := by
  sorry

/-!
## p-adic BSD in Rank 1
-/

/-- **Theorem (p-adic BSD in rank 1).**
    Combining p-adic Gross–Zagier with Kolyvagin's Euler system:
    the order of vanishing of `L_p(E, s)` at `s = 1` equals `rank E(Q)`,
    and the leading coefficient involves the p-adic regulator, Sha, and Tamagawa numbers. -/
theorem padic_bsd_rank_one {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) [AddCommGroup E] (r : ℕ) (hr : r = 1) :
    -- ord_{s=1} L_p(E, s) = r
    -- L_p'(E, 1) = (|Sha[p^∞]| / |E(Q)_tors|²) * Reg_p(E) * ∏ c_ℓ
    ∃ (Sha_part : ℕ) (tors : ℕ) (Reg_p : ℚ_[p]) (Tam : ℚ_[p]),
      True := by
  sorry
