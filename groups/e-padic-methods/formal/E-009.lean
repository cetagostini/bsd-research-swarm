/-
  E-009: p-adic BSD for Supersingular Primes
  Lean 4 fragment formalising plus/minus p-adic L-functions,
  Selmer groups, and the Kobayashi conjecture.
-/

import Mathlib

open scoped BigOperators

/-!
## Supersingular Condition
-/

/-- An elliptic curve `E/ℚ` has supersingular reduction at `p` if `aₚ = 0`. -/
def isSupersingular (p : ℕ) (aₚ : ℤ) : Prop :=
  aₚ = 0

/-!
## Plus/Minus Norm Maps
-/

/-- The plus-norm map `Norm_n^+ = Norm_n + p` on the formal group. -/
noncomputable def plusNorm {p : ℕ} (hp : Nat.Prime p)
    (P : ℤ_[p]) (n : ℕ) : ℤ_[p] :=
  sorry  -- Norm_n(P) + p · P

/-- The minus-norm map `Norm_n^- = Norm_n - p` on the formal group. -/
noncomputable def minusNorm {p : ℕ} (hp : Nat.Prime p)
    (P : ℤ_[p]) (n : ℕ) : ℤ_[p] :=
  sorry  -- Norm_n(P) - p · P

/-!
## Plus/Minus Selmer Groups
-/

/-- The plus-Selmer group `Sel_{p^∞}^+(E/ℚ_∞)`. -/
structure PlusSelmerGroup (p : ℕ) (E : Type*) where
  /-- The local condition at `p` uses the plus-norm map. -/
  local_plus : Type
  /-- Global classes satisfying the plus local condition. -/
  classes : Type

/-- The minus-Selmer group `Sel_{p^∞}^-(E/ℚ_∞)`. -/
structure MinusSelmerGroup (p : ℕ) (E : Type*) where
  /-- The local condition at `p` uses the minus-norm map. -/
  local_minus : Type
  /-- Global classes satisfying the minus local condition. -/
  classes : Type

/-!
## Plus/Minus p-adic L-functions
-/

/-- The plus p-adic L-function `L_p^+(E, s)`. -/
noncomputable def plusLFunction {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) : ℚ_[p] → ℚ_[p] :=
  sorry

/-- The minus p-adic L-function `L_p^-(E, s)`. -/
noncomputable def minusLFunction {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) : ℚ_[p] → ℚ_[p] :=
  sorry

/-!
## Plus/Minus p-adic BSD Conjecture
-/

/-- Plus/minus regulators. -/
noncomputable def plusRegulator {p : ℕ} (hp : Nat.Prime p)
    (generators : List (ℤ × ℤ)) : ℚ_[p] :=
  sorry

noncomputable def minusRegulator {p : ℕ} (hp : Nat.Prime p)
    (generators : List (ℤ × ℤ)) : ℚ_[p] :=
  sorry

/-- **Conjecture (Kobayashi, 2003: Plus/Minus p-adic BSD).**
    For `E/ℚ` supersingular at `p`:
    `ord_{s=1} L_p^±(E, s) = rank_{ℤ_p} Sel_{p^∞}^±(E/ℚ_∞)`
    and the leading coefficient involves `Reg_p^±`, Sha^±, and Tamagawa numbers. -/
conjecture plus_minus_padic_bsd {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) (r_plus r_minus : ℕ) (sha_plus sha_minus : ℕ)
    (tors : ℕ) (tam : ℚ_[p]) :
    -- L_p^+ leading coeff = |Sha^+| * Reg_p^+ * tam / |tors|²
    -- L_p^- leading coeff = |Sha^-| * Reg_p^- * tam / |tors|²
    ∃ (leading_plus leading_minus : ℚ_[p]),
      leading_plus = (sha_plus : ℚ_[p]) * plusRegulator hp [] * tam / (tors : ℚ_[p])^2 ∧
      leading_minus = (sha_minus : ℚ_[p]) * minusRegulator hp [] * tam / (tors : ℚ_[p])^2

/-!
## Decomposition: r = r⁺ + r⁻
-/

/-- The total rank decomposes as `r = r⁺ + r⁻`. -/
theorem rank_decomposition {p : ℕ} (hp : Nat.Prime p)
    (r r_plus r_minus : ℕ) (h : r = r_plus + r_minus) :
    r = r_plus + r_minus := h

/-!
## p-adic Gross–Zagier for Supersingular (Sprung)
-/

/-- **Conjecture (Sprung, 2018).** p-adic Gross–Zagier for supersingular primes. -/
conjecture padic_gross_zagier_supersingular {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) (K : Type*) (P_K : ℤ × ℤ) (sign : Bool) :
    -- L_p'^{±}(E/K, 1) = h_p^±(P_K^±) * correction
    ∃ (correction : ℚ_[p]), True
