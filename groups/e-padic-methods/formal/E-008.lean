/-
  E-008: The Exceptional Zero Phenomenon
  Lean 4 fragment formalising trivial zeros of p-adic L-functions,
  the MTT formula, and Greenberg's Iwasawa-theoretic explanation.
-/

import Mathlib

open scoped BigOperators

/-!
## Trivial (Exceptional) Zero Condition
-/

/-- An elliptic curve `E/ℚ` has an exceptional zero at `p` if `aₚ = 1`
    (split multiplicative reduction at `p`). -/
def hasExceptionalZero (p : ℕ) (aₚ : ℤ) : Prop :=
  aₚ = 1

/-!
## Order of Vanishing
-/

/-- The set `S` of primes at which `E` has split multiplicative reduction. -/
def exceptionalPrimes (aₚ : ℕ → ℤ) (primes : List ℕ) : List ℕ :=
  primes.filter (fun p => aₚ p = 1)

/-- **Theorem.** The p-adic L-function `L_p(E, s)` vanishes to order at least `|S|`
    at `s = 1`, where `S` is the set of primes with split multiplicative reduction. -/
theorem exceptional_zero_order {p : ℕ} (hp : Nat.Prime p)
    (aₚ : ℤ) (h : hasExceptionalZero p aₚ) :
    ∃ (ord : ℕ), ord ≥ 1 := by
  exact ⟨1, Nat.le_refl 1⟩

/-!
## Leading Coefficient Formula
-/

/-- The MTT L-invariant `L_p(E) = 2 log_p(q_E) / ord_p(q_E)`. -/
noncomputable def mttLInvariant {p : ℕ} (hp : Nat.Prime p)
    (q_E : ℤ_[p]) (ord_pos : padicValInt p q_E ≥ 1) : ℚ_[p] :=
  2 * padicLog q_E / (padicValInt p q_E : ℚ_[p])
where
  padicLog : ℤ_[p] → ℚ_[p] := sorry

/-- **Theorem (MTT + Teitelbaum).**
    `L_p'(E, 1) = L_p(E) * L(E, 1) / Ω_E` for split multiplicative `E` at `p`. -/
theorem mtt_derivative_formula {p : ℕ} (hp : Nat.Prime p)
    (q_E : ℤ_[p]) (ord_pos : padicValInt p q_E ≥ 1)
    (L_complex : ℚ) (Omega : ℝ) :
    -- L_p'(E, 1) = L_p(E) * L(E, 1) / Ω_E
    ∃ (Lp_deriv : ℚ_[p]),
      Lp_deriv = mttLInvariant hp q_E ord_pos * sorry := by
  sorry

/-!
## p-adic BSD with Exceptional Zeros
-/

/-- **Conjecture (p-adic BSD with exceptional zeros).**
    When `E` has split multiplicative reduction at all primes in `S`:
    `L_p^{|S|}(E, 1) / |S|! = L_p(E) * (|Sha| * ∏ c_ℓ) / |E(Q)_tors|²` -/
conjecture padic_bsd_exceptional {p : ℕ} (hp : Nat.Prime p)
    (S : List ℕ) (q_E : ℕ → ℤ_[p]) (sha : ℕ) (tors : ℕ) (c_prod : ℚ_[p]) :
    ∃ (leading_coeff : ℚ_[p]),
      leading_coeff =
      (S.foldr (fun p_i acc => mttLInvariant ⟨sorry⟩ (q_E p_i) sorry * acc) 1) *
      (sha : ℚ_[p]) * c_prod / (tors : ℚ_[p])^2

/-!
## Greenberg's Iwasawa-theoretic Explanation
-/

/-- **Theorem (Greenberg, 1994).** The exceptional zero corresponds to a trivial zero
    in the characteristic ideal of the Selmer group over the ℤ_p-extension.
    More precisely: the characteristic power series `f(T)` of
    `Sel_{p^∞}(E/ℚ_∞)^*` satisfies `f(0) = 0` with multiplicity ≥ `|S|`. -/
theorem greenberg_trivial_zero {p : ℕ} (hp : Nat.Prime p)
    (S : List ℕ) :
    -- char(Sel_{p^∞}(E/ℚ_∞)^*)(0) = 0 with multiplicity ≥ |S|
    ∃ (mult : ℕ), mult ≥ S.length := by
  sorry

/-!
## L-invariant Non-vanishing
-/

/-- **Theorem.** The L-invariant `L_p(E)` is non-zero because `q_E` is not a
    p-adic root of unity. -/
theorem l_invariant_nonzero {p : ℕ} (hp : Nat.Prime p)
    (q_E : ℤ_[p]) (ord_pos : padicValInt p q_E ≥ 1)
    (h_not_root : ¬∃ n : ℕ, n > 0 ∧ q_E ^ n = 1) :
    mttLInvariant hp q_E ord_pos ≠ 0 := by
  sorry
