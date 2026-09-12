/-
  C-010: Arithmetic Statistics over Function Fields
  
  Lean 4 fragment: elliptic curves over 𝔽_q(t), function field BSD,
  Duke-Kowalski theorem, and Ulmer's high-rank examples.
-/

import Mathlib.Data.Real.Basic
import Mathlib.FieldTheory.Finite.Basic

/-! ## Elliptic curves over function fields -/

/-- An elliptic curve over 𝔽_q(t). -/
structure EllipticCurveFqT (q : ℕ) where
  (a₁ a₂ a₃ a₄ a₆ : Polynomial (ZMod q))
  (discriminant : Polynomial (ZMod q))
  (disc_ne_zero : discriminant ≠ 0)

/-- The conductor of E/𝔽_q(t) (a divisor of ℙ¹). -/
noncomputable def conductor {q : ℕ} (E : EllipticCurveFqT q) : ℕ := sorry
  -- degree of the conductor divisor

/-- The rank of E(𝔽_q(t)). -/
noncomputable def fqRank {q : ℕ} (E : EllipticCurveFqT q) : ℕ := sorry

/-! ## Function field BSD -/

/-- **Theorem (Kato-Trihan).** BSD holds for elliptic curves over 𝔽_q(t)
    for q = p^n with p > 2. -/
theorem bsd_function_field (q : ℕ) (hq : q > 2) (E : EllipticCurveFqT q) :
    sorry /* BSD equality */ := by
  sorry

/-- **Theorem (Tate).** Sha is finite for elliptic curves over
    global function fields. -/
theorem sha_finite_function_field (q : ℕ) (E : EllipticCurveFqT q) :
    ∃ n : ℕ, sorry /* |Sha(E/𝔽_q(t))| = n */ := by
  sorry

/-! ## Duke-Kowalski: function field Goldfeld -/

/-- The family of elliptic curves over 𝔽_q(t) with conductor degree ≤ d. -/
def FqTFamily (q d : ℕ) : Set (EllipticCurveFqT q) :=
  {E | conductor E ≤ d}

/-- **Theorem (Duke-Kowalski).** 100% of elliptic curves over 𝔽_q(t)
    have rank ≤ 1. -/
theorem duke_kowalski (q : ℕ) (hq : Nat.Prime q) :
    ∀ ε > 0, ∃ d₀ : ℕ, ∀ d > d₀,
      ({E ∈ FqTFamily q d | fqRank E ≥ 2}.ncard : ℝ) /
        (FqTFamily q d).ncard < ε := by
  sorry

/-! ## Ulmer's high-rank examples -/

/-- Ulmer's construction: for each r, an elliptic curve over 𝔽_q(t)
    with rank ≥ r. -/
theorem ulmer_high_rank (q : ℕ) (hq : Nat.Prime q) (r : ℕ) :
    ∃ E : EllipticCurveFqT q, fqRank E ≥ r := by
  sorry

/-- These high-rank curves have density 0. -/
theorem ulmer_density_zero (q : ℕ) (hq : Nat.Prime q) :
    ∀ ε > 0, ∃ d₀ : ℕ, ∀ d > d₀,
      ({E ∈ FqTFamily q d | fqRank E ≥ 2}.ncard : ℝ) /
        (FqTFamily q d).ncard < ε := by
  sorry

/-! ## Sato-Tate over function fields -/

/-- **Theorem (Deligne).** The Frobenius traces of E/𝔽_q(t) are
    equidistributed with respect to the Sato-Tate measure. -/
theorem sato_tate_function_field (q : ℕ) (E : EllipticCurveFqT q) :
    sorry /* equidistribution of a_v(E) */ := by
  sorry

/-! ## Moduli space counting -/

/-- The number of elliptic curves over 𝔽_q with conductor degree d
    grows as c · q^{5d/6}. -/
noncomputable def moduliCount (q d : ℕ) : ℝ :=
  sorry  -- ≈ c · q^{5d/6}

theorem moduli_growth (q : ℕ) (hq : q > 1) :
    ∃ c : ℝ, c > 0 ∧
      Filter.Tendsto
        (fun d => moduliCount q d / (q : ℝ) ^ (5 * d / 6))
        Filter.atTop (nhds c) := by
  sorry

/-! ## Uniformity in q -/

/-- **Conjecture (uniformity).** The Duke-Kowalski bound is
    uniform in q. -/
def UniformityConjecture : Prop :=
  ∃ C : ℝ, C > 0 ∧ ∀ q : ℕ, Nat.Prime q →
    ∀ d : ℕ, ({E ∈ FqTFamily q d | fqRank E ≥ 2}.ncard : ℝ) /
      (FqTFamily q d).ncard ≤ C * (q : ℝ) ^ (-(d : ℝ) / 2)
