/-
  E-010: Greenberg's L-invariant and Its Variations
  Lean 4 fragment formalising the various definitions of L-invariants
  and their proven/proposed equivalences.
-/

import Mathlib

open scoped BigOperators

/-!
## MTT L-invariant (from E-003)
-/

noncomputable def mttLInvariant {p : ℕ} (hp : Nat.Prime p)
    (q_E : ℤ_[p]) : ℚ_[p] :=
  2 * padicLog q_E / (padicValRat p (q_E : ℚ) : ℚ_[p])
where
  padicLog : ℤ_[p] → ℚ_[p] := sorry

/-!
## Greenberg's L-invariant (Iwasawa-theoretic)
-/

/-- **Definition (Greenberg).** The L-invariant from the characteristic power series
    of the Selmer group: `L_p^Gr(E) = f'(0) / μ_p` where `f(T)` is the characteristic
    power series of `Sel_{p^∞}(E/ℚ_∞)^*`. -/
noncomputable def greenbergLInvariant {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) : ℚ_[p] :=
  -- f'(0) / μ where f(T) = char(Sel_{p^∞}(E/ℚ_∞)^*)
  sorry

/-- Greenberg's formula involving Frobenius eigenvalues at levels `p^n`:
    `L_p^Gr(E) = lim_{n→∞} (1/p^n) log_p(a_{p^{n+1}} / a_{p^n})` -/
noncomputable def greenbergLInvariantViaFrobenius {p : ℕ} (hp : Nat.Prime p)
    (frobTraces : ℕ → ℤ_[p]) : ℚ_[p] :=
  sorry  -- limit as n → ∞

/-!
## Colmez's L-invariant (p-adic representations)
-/

/-- **Definition (Colmez).** The L-invariant from `(φ, Γ)`-modules:
    `L_p^Col(V) = d/ds|_{s=0} log_p L_p(V(s))`. -/
noncomputable def colmezLInvariant {p : ℕ} (hp : Nat.Prime p)
    (V : Type*) : ℚ_[p] :=
  sorry  -- Derivative of the p-adic L-function of V at s=0

/-!
## Darmon's L-invariant (p-adic uniformisation)
-/

/-- **Definition (Darmon).** The L-invariant from p-adic uniformisation of
    Shimura curves: `L_p^Dar(E) = log_p(α) / ord_p(α)`. -/
noncomputable def darmonLInvariant {p : ℕ} (hp : Nat.Prime p)
    (alpha : ℤ_[p]) (hα : IsUnit alpha) : ℚ_[p] :=
  padicLog alpha / (padicValRat p (alpha : ℚ) : ℚ_[p])
where
  padicLog : ℤ_[p] → ℚ_[p] := sorry

/-!
## Equivalence Theorems
-/

/-- **Theorem (Colmez, 1990).** For split multiplicative reduction at `p`:
    MTT L-invariant = Colmez L-invariant. -/
theorem mtt_eq_colmez {p : ℕ} (hp : Nat.Prime p)
    (q_E : ℤ_[p]) (V : Type*) :
    mttLInvariant hp q_E = colmezLInvariant hp V := by
  sorry

/-- **Theorem (Sander).** For split multiplicative reduction at `p`:
    MTT L-invariant = Darmon L-invariant. -/
theorem mtt_eq_darmon {p : ℕ} (hp : Nat.Prime p)
    (q_E : ℤ_[p]) (alpha : ℤ_[p]) (hα : IsUnit alpha) :
    mttLInvariant hp q_E = darmonLInvariant hp alpha hα := by
  sorry

/-- **Theorem (Greenberg, 1994).** For split multiplicative reduction at `p`:
    MTT L-invariant = Greenberg L-invariant. -/
theorem mtt_eq_greenberg {p : ℕ} (hp : Nat.Prime p)
    (q_E : ℤ_[p]) (E : Type*) :
    mttLInvariant hp q_E = greenbergLInvariant hp E := by
  sorry

/-- **Conjecture.** All four L-invariants coincide for good ordinary reduction
    (proven only for split multiplicative). -/
conjecture all_l_invariants_coincide {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) (q_E : ℤ_[p]) (V : Type*) (alpha : ℤ_[p]) (hα : IsUnit alpha) :
    mttLInvariant hp q_E = greenbergLInvariant hp E ∧
    mttLInvariant hp q_E = colmezLInvariant hp V ∧
    mttLInvariant hp q_E = darmonLInvariant hp alpha hα

/-!
## Variation in Families
-/

/-- **Conjecture.** The L-invariant varies analytically in a Hida family. -/
conjecture l_invariant_analytic_variation {p : ℕ} (hp : Nat.Prime p)
    (weight : ℤ_[p] → Type*) :
    -- k ↦ L_p(E_k) is a p-adic analytic function on the weight space
    True

/-!
## Non-vanishing
-/

/-- **Conjecture (Non-vanishing).** The L-invariant is non-zero
    for all elliptic curves and all primes. -/
conjecture l_invariant_nonvanishing {p : ℕ} (hp : Nat.Prime p)
    (E : Type*) :
    greenbergLInvariant hp E ≠ 0
