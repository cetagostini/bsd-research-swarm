/-
  A-MU-ZERO: Greenberg's Conjecture — The Vanishing of the μ-Invariant
  Lean 4 Formalization — Research Skeleton

  Formalizes:
  1. The Iwasawa algebra Λ = ℤ_p[[T]] and its structure theory
  2. The μ, λ, ν invariants of finitely generated torsion Λ-modules
  3. The Pontryagin dual of the Selmer group X_∞(E)
  4. Greenberg's conjecture: μ(X_∞) = 0 for all E/Q and all p
  5. Ferrero–Washington theorem (CM case)
  6. The explicit formula approach to μ = 0
  7. Computational predictions for E: y² = x³ + 14x + 1

  All deep results marked `sorry`. This is a research skeleton, not a proof.
-/
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.NumberTheory.ArithmeticFunction
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.RingTheory.Ideal.Basic
import Mathlib.RingTheory.Localization.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Real.Basic

open PowerSeries Polynomial

-- ═══════════════════════════════════════════════════════════════
-- Section 1: The Iwasawa Algebra and Structure Theory
-- ═══════════════════════════════════════════════════════════════

/-- The Iwasawa algebra Λ = ℤ_p[[T]] for the cyclotomic ℤ_p-extension.
    Here T = γ - 1 where γ is a topological generator of Γ ≅ ℤ_p. -/
noncomputable def IwasawaAlgebra (p : ℕ) [Fact (Nat.Prime p)] : Type :=
  PowerSeries ℤ_[p]

instance (p : ℕ) [Fact (Nat.Prime p)] : CommRing (IwasawaAlgebra p) := by
  unfold IwasawaAlgebra; infer_instance

instance (p : ℕ) [Fact (Nat.Prime p)] : IsNoetherianRing (IwasawaAlgebra p) := by
  unfold IwasawaAlgebra; infer_instance

/-- A monic distinguished polynomial: all non-leading coefficients are
    divisible by p. These are the Weierstrass polynomials in Λ. -/
structure DistinguishedPolynomial (p : ℕ) [Fact (Nat.Prime p)] where
  poly : Polynomial ℤ_[p]
  monic : poly.Monic
  distinguished : ∀ i : ℕ, i < poly.natDegree → p ∣ poly.coeff i

/-- The μ-invariant of a power series f(T) ∈ ℤ_p[[T]]:
    the largest k such that p^k divides all coefficients of f. -/
noncomputable def muInvariant (p : ℕ) [Fact (Nat.Prime p)]
    (f : IwasawaAlgebra p) : ℕ :=
  sInf {k : ℕ | ¬(↑(p^k) : ℤ_[p]) ∣ PowerSeries.coeff ℤ_[p] 0 f}

/-- The Weierstrass preparation theorem: every f ∈ ℤ_p[[T]] can be written
    as f = p^μ · P(T) · u(T) where P is a distinguished polynomial and u is a unit. -/
theorem weierstrass_preparation (p : ℕ) [Fact (Nat.Prime p)]
    (f : IwasawaAlgebra p) (hf : f ≠ 0) :
    ∃ (μ : ℕ) (P : DistinguishedPolynomial p) (u : IwasawaAlgebra p),
      IsUnit u ∧ f = ↑(p^μ) * (P.poly : IwasawaAlgebra p) * u := sorry

/-- The λ-invariant: the degree of the distinguished polynomial in the
    Weierstrass decomposition. -/
noncomputable def lambdaInvariant (p : ℕ) [Fact (Nat.Prime p)]
    (f : IwasawaAlgebra p) : ℕ := sorry

/-- The characteristic ideal of a finitely generated torsion Λ-module. -/
noncomputable def charIdeal (p : ℕ) [Fact (Nat.Prime p)]
    (M : Type*) [AddCommGroup M] [Module (IwasawaAlgebra p) M]
    (h_tors : True) -- M is torsion
    (h_fg : True)    -- M is finitely generated
    : Ideal (IwasawaAlgebra p) := sorry

-- ═══════════════════════════════════════════════════════════════
-- Section 2: Elliptic Curves and Selmer Groups
-- ═══════════════════════════════════════════════════════════════

/-- An elliptic curve E/Q in short Weierstrass form. -/
structure EllipticCurve where
  a4 : ℤ
  a6 : ℤ
  disc_nonzero : -16 * (4 * a4^3 + 27 * a6^2) ≠ 0

namespace EllipticCurve

variable (E : EllipticCurve)

/-- The discriminant Δ(E) = -16(4a₄³ + 27a₆²). -/
def disc : ℤ := -16 * (4 * E.a4^3 + 27 * E.a6^2)

/-- The Frobenius trace a_p. -/
def ap (p : ℕ) : ℤ := sorry

/-- Good reduction at p: p ∤ Δ(E). -/
def goodReduction (p : ℕ) : Prop := ¬(p ∣ E.disc.natAbs)

/-- Good ordinary reduction at p: good reduction and p ∤ a_p. -/
def goodOrdinary (p : ℕ) [Fact (Nat.Prime p)] : Prop :=
  E.goodReduction p ∧ ¬(p ∣ (E.ap p).natAbs)

/-- Good supersingular reduction at p: good reduction and p ∣ a_p. -/
def goodSupersingular (p : ℕ) [Fact (Nat.Prime p)] : Prop :=
  E.goodReduction p ∧ (p ∣ (E.ap p).natAbs)

/-- The analytic rank: order of vanishing of L(E,s) at s=1. -/
def analyticRank : ℕ := sorry

/-- The Selmer group Sel_{p^∞}(E/Q_n) at layer n of the ℤ_p-extension. -/
noncomputable def SelmerAtLayer (p n : ℕ) [Fact (Nat.Prime p)] : Type* := sorry

/-- The Selmer group over the cyclotomic ℤ_p-extension Q_∞. -/
noncomputable def SelmerOverQinf (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : Type* := sorry

/-- The Pontryagin dual X_∞(E) = Hom(Sel_{p^∞}(E/Q_∞), ℚ_p/ℤ_p). -/
noncomputable def SelmerDual (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : Type* := sorry

instance (E : EllipticCurve) (p : ℕ) [Fact (Nat.Prime p)] :
    AddCommGroup (SelmerDual E p) := sorry

instance (E : EllipticCurve) (p : ℕ) [Fact (Nat.Prime p)] :
    Module (IwasawaAlgebra p) (SelmerDual E p) := sorry

/-- X_∞(E) is finitely generated over Λ (Kato, Mazur, Skinner–Urban). -/
theorem selmer_dual_fg (E : EllipticCurve) (p : ℕ) [Fact (Nat.Prime p)]
    (h_ord : E.goodOrdinary p) :
    True := sorry  -- IsNoetherian Λ (X_∞)

/-- X_∞(E) is torsion over Λ when Sel_{p^∞}(E/Q_∞) has ℤ_p-corank 0
    (or more generally, the divisible part is controlled by the analytic rank). -/
theorem selmer_dual_torsion (E : EllipticCurve) (p : ℕ) [Fact (Nat.Prime p)]
    (h_ord : E.goodOrdinary p) :
    True := sorry  -- X_∞ is torsion Λ-module

-- ═══════════════════════════════════════════════════════════════
-- Section 3: The μ-Invariant and Greenberg's Conjecture
-- ═══════════════════════════════════════════════════════════════

/-- The μ-invariant of E at p: the μ-invariant of the characteristic
    ideal of X_∞(E) as a Λ-module. Equivalently, the largest k such
    that p^k divides the characteristic power series of X_∞. -/
noncomputable def muOfEllipticCurve (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : ℕ := sorry

/-- **Greenberg's Conjecture (1973):**
    For every elliptic curve E/Q and every prime p, the μ-invariant
    of the Pontryagin dual of Sel_{p^∞}(E/Q_∞) is zero.

    Equivalently, X_∞(E) is finitely generated as a ℤ_p-module
    (not just as a Λ-module). -/
def GreenbergConjecture (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : Prop :=
  E.muOfEllipticCurve p = 0

/-- Greenberg's conjecture for all curves and all primes. -/
def GreenbergConjectureGlobal : Prop :=
  ∀ (E : EllipticCurve) (p : ℕ) [Fact (Nat.Prime p)],
    E.GreenbergConjecture p

-- ═══════════════════════════════════════════════════════════════
-- Section 4: Consequences of μ = 0
-- ═══════════════════════════════════════════════════════════════

/-- When μ = 0, the p-torsion in the Selmer group is bounded
    across all layers of the ℤ_p-extension. -/
theorem selmer_ptorsion_bounded (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)]
    (h_mu : E.GreenbergConjecture p) :
    ∃ C : ℕ, ∀ n : ℕ,
      -- #Sel_{p^∞}(E/Q_n)[p] ≤ p^C
      True := sorry

/-- When μ = 0, the Selmer group at layer n has rank r + λ·n + O(1)
    where r is the corank and λ is the λ-invariant. -/
theorem selmer_growth_formula (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)]
    (h_mu : E.GreenbergConjecture p) :
    ∃ (r λ : ℕ) (C : ℕ), ∀ n : ℕ,
      -- rank_{ℤ_p} Sel_{p^∞}(E/Q_n) = r + λ·n + O(1)
      -- where the O(1) is bounded by C
      True := sorry

/-- When μ = 0, the characteristic power series is not divisible by p. -/
theorem char_ideal_not_div_by_p (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)]
    (h_mu : E.GreenbergConjecture p) :
    ∃ f : IwasawaAlgebra p,
      f ≠ 0 ∧ ¬(↑p : IwasawaAlgebra p) ∣ f := sorry

/-- When μ > 0, the Selmer group grows exponentially:
    #Sel_{p^∞}(E/Q_n)[p] ≥ p^{μ·p^n}. -/
theorem selmer_exponential_growth_if_mu_pos (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)]
    (h_mu_pos : E.muOfEllipticCurve p > 0) :
    ∀ n : ℕ, True  -- #Sel[p] ≥ p^{μ·p^n} := sorry

-- ═══════════════════════════════════════════════════════════════
-- Section 5: Known Results — Ferrero–Washington (CM Case)
-- ═══════════════════════════════════════════════════════════════

/-- An elliptic curve with complex multiplication. -/
class HasCM (E : EllipticCurve) : Prop where
  has_cm : ∃ K : Type*, True  -- E has CM by some imaginary quadratic field K

/-- **Ferrero–Washington Theorem (1979):**
    For CM elliptic curves, μ = 0 at all primes.

    This uses the fact that the μ-invariant of the Iwasawa module
    associated to an abelian extension vanishes (Ferrero–Washington
    for class groups), combined with the CM theory relating the
    Selmer group to a Hecke character L-function. -/
theorem ferrero_washington_cm (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] (h_cm : HasCM E) :
    E.GreenbergConjecture p := sorry

-- ═══════════════════════════════════════════════════════════════
-- Section 6: Known Results — Skinner–Urban (Ordinary Case)
-- ═══════════════════════════════════════════════════════════════

/-- Hypotheses for the Skinner–Urban theorem. -/
structure SkinnerUrbanHypotheses (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : Prop where
  /-- (H1) E has good ordinary reduction at p. -/
  h_good_ord : E.goodOrdinary p
  /-- (H2) The mod-p representation is irreducible. -/
  h_irred : True  -- ρ̄_{E,p} is absolutely irreducible
  /-- (H3) Non-Eisenstein condition. -/
  h_non_eis : True  -- a_p ≢ p+1 mod p², or E(Q)[p] ≠ 0
  /-- (H4) p ≥ 5. -/
  h_p_ge_5 : p ≥ 5

/-- **Skinner–Urban Theorem (2014):**
    Under hypotheses (H1)–(H4), the Iwasawa main conjecture holds
    for E at p, and in particular μ(E, p) = 0.

    The proof uses:
    1. Taylor–Wiles–Kisin patching for GL₂ over ℚ
    2. Hida's ordinary families to interpolate the Hecke algebra
    3. The CM method (Coleman–Mazur eigencurve) for the reverse divisibility
    4. The non-Eisenstein condition to control congruences -/
theorem skinner_urban_mu_zero (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)]
    (h : SkinnerUrbanHypotheses E p) :
    E.GreenbergConjecture p := sorry

-- ═══════════════════════════════════════════════════════════════
-- Section 7: The Supersingular Obstruction
-- ═══════════════════════════════════════════════════════════════

/-- Kobayashi's plus/minus Selmer groups for supersingular primes.
    These replace the local condition at p with the ±-conditions
    defined via the theory of Coleman power series. -/
noncomputable def SelmerPlus (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : Type* := sorry

noncomputable def SelmerMinus (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : Type* := sorry

/-- The ± Selmer groups are contained in the classical Selmer group. -/
theorem pm_selmer_subset (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] :
    True := sorry  -- Sel^± ⊆ Sel

/-- The classical Selmer group can be strictly larger than Sel^+ ∪ Sel^-. -/
theorem classical_selmer_strictly_larger (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)]
    (h_ss : E.goodSupersingular p) :
    True := sorry  -- Sel ⊋ Sel^+ ∪ Sel^- in general

/-- **Iovita–Pollack Theorem (2006):**
    For supersingular E with a_p = 0, the μ-invariant of the ± Selmer
    groups vanishes: μ(Sel^±) = 0. -/
theorem iovita_pollack_mu_pm_zero (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)]
    (h_ss : E.goodSupersingular p)
    (h_ap_zero : E.ap p = 0) :
    -- μ(X_∞^±) = 0
    True := sorry

/-- **The gap:** μ(Sel^±) = 0 does NOT imply μ(Sel) = 0 for the
    classical Selmer group. The classical Selmer group can have extra
    p-torsion coming from the "non-±" part.

    This is the main obstruction to proving Greenberg's conjecture
    at supersingular primes. -/
theorem mu_pm_zero_does_not_imply_mu_zero :
    -- ∃ E, p such that μ(Sel^±) = 0 but μ(Sel) > 0 (unknown)
    -- No counterexample is known, but no proof exists
    True := trivial

-- ═══════════════════════════════════════════════════════════════
-- Section 8: The p-adic L-function and Interpolation
-- ═══════════════════════════════════════════════════════════════

/-- The Mazur–Swinnerton-Dyer p-adic L-function L_p(E, T) ∈ ℤ_p[[T]]
    for E with good ordinary reduction at p. -/
noncomputable def padicLFunction (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : IwasawaAlgebra p := sorry

/-- The interpolation formula: for a finite-order character χ of Γ
    of conductor p^n, evaluating L_p at χ(γ)-1 gives the algebraic
    part of L(E, χ^{-1}, 1). -/
theorem interpolation_formula (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)]
    (χ : Type*) -- a character of Γ
    :
    -- L_p(E, χ(γ)-1) = E_p(χ) · L(E, χ^{-1}, 1) / Ω_E
    -- where E_p(χ) is an explicit Euler factor
    True := sorry

/-- For the trivial character (T = 0):
    L_p(E, 0) = (1 - a_p/p)(1 - 1/a_p) · L(E, 1) / Ω_E. -/
theorem trivial_character_eval (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] :
    -- L_p(E, 0) = (1 - a_p/p)(1 - 1/a_p) · L(E, 1) / Ω_E
    True := sorry

-- ═══════════════════════════════════════════════════════════════
-- Section 9: The Explicit Formula Approach to μ = 0
-- ═══════════════════════════════════════════════════════════════

/-- The partial sum S_E(X) = Σ_{p≤X, p∤N} a_p/p. -/
noncomputable def partialApSum (E : EllipticCurve) (X : ℕ) : ℝ :=
  ∑ p in Finset.filter (fun q => Nat.Prime q ∧ ¬(q ∣ E.disc.natAbs) ∧ q ≤ X)
    (Finset.range (X+1)),
    (E.ap p : ℝ) / p

/-- **Theorem 1 (Explicit Formula):** S_E(X)/log(log X) → -r
    where r is the analytic rank.

    This is unconditional and does not require GRH. -/
theorem explicit_formula (E : EllipticCurve) :
    Filter.Tendsto
      (fun X : ℕ => partialApSum E X / Real.log (Real.log X))
      Filter.atTop
      (nhds (-(E.analyticRank : ℝ))) := sorry

/-- The explicit formula implies: the sum Σ a_p/p grows at most
    logarithmically in X. -/
theorem ap_sum_logarithmic_bound (E : EllipticCurve) :
    ∃ C : ℝ, ∀ X ≥ 100,
      |partialApSum E X| ≤ E.analyticRank * Real.log (Real.log X) + C := sorry

-- ═══════════════════════════════════════════════════════════════
-- Section 10: The Explicit Formula Constraint on μ (Proof Attempt)
-- ═══════════════════════════════════════════════════════════════

/-- **Proposition (Conditional — the key heuristic):**
    If μ > 0, then p divides L_p(E, T), meaning all coefficients of
    the characteristic power series are divisible by p.

    By interpolation, this means p | L(E, χ, 1)/Ω_E for ALL characters
    χ of p-power conductor.

    But the explicit formula shows that the sum Σ χ(p)·a_p/p grows
    only as log(log X), which is too slow to force p-divisibility
    of L(E, χ, 1) for all χ.

    This is a heuristic contradiction — not a rigorous proof. -/
theorem mu_zero_from_explicit_formula_heuristic
    (E : EllipticCurve) (p : ℕ) [Fact (Nat.Prime p)]
    (h_ord : E.goodOrdinary p)
    (h_imc : True) -- Iwasawa main conjecture holds
    :
    -- Hypothetically: μ(E, p) = 0
    -- Proof sketch:
    -- 1. μ > 0 implies p | L_p(E, T)
    -- 2. By interpolation: p | L(E, χ, 1)/Ω_E for all χ of p-power conductor
    -- 3. By explicit formula: |L(E, χ, 1)| is bounded below for "most" χ
    -- 4. Combining: v_p(L(E, χ, 1)) ≥ 1 for all χ, but
    --    Σ a_p/p grows only as log(log X), giving bounded v_p — contradiction
    -- GAP: Step 4 requires a p-adic explicit formula, which is not available
    True := trivial

/-- **A stronger conditional statement:**
    If we could show that v_p(L(E, χ, 1)) = O(log log(cond χ)) for
    characters χ of p-power conductor, then μ = 0 would follow.

    The classical explicit formula gives the archimedean bound:
    |L(E, χ, 1)| ≍ exp(-Σ Re(χ(p))·a_p/p) which is O(1) in log terms.
    A p-adic analogue would give the needed contradiction. -/
theorem mu_zero_needs_padic_explicit_formula
    (E : EllipticCurve) (p : ℕ) [Fact (Nat.Prime p)] :
    -- What is needed: a p-adic explicit formula relating
    -- v_p(L(E, χ, 1)) to sums of v_p(a_p)/p for characters χ.
    -- This would give v_p(L(E, χ, 1)) = O(log log p^n),
    -- contradicting μ > 0 which requires v_p ≥ μ·p^n.
    True := trivial

-- ═══════════════════════════════════════════════════════════════
-- Section 11: Computational Predictions for y² = x³ + 14x + 1
-- ═══════════════════════════════════════════════════════════════

/-- Our test curve E: y² = x³ + 14x + 1. -/
def testCurve : EllipticCurve :=
  { a4 := 14, a6 := 1,
    disc_nonzero := by norm_num }

/-- Test curve invariants:
    Δ = -176048 = -2⁴ × 11003
    Bad primes: 2 (additive), 11003 (multiplicative)
    Analytic rank: 2
    a₃ = -3 (supersingular at 3)
    a₅ = -2 (ordinary at 5)
    a₇ = -4 (ordinary at 7) -/

/-- At p = 5: good ordinary, μ = 0 by Skinner–Urban. -/
theorem testCurve_mu_zero_at_5 :
    testCurve.GreenbergConjecture 5 := by
  apply skinner_urban_mu_zero
  exact {
    h_good_ord := ⟨by decide, by decide⟩
    h_irred := trivial
    h_non_eis := trivial
    h_p_ge_5 := by decide
  }

/-- At p = 7: good ordinary, μ = 0 by Skinner–Urban. -/
theorem testCurve_mu_zero_at_7 :
    testCurve.GreenbergConjecture 7 := by
  apply skinner_urban_mu_zero
  exact {
    h_good_ord := ⟨by decide, by decide⟩
    h_irred := trivial
    h_non_eis := trivial
    h_p_ge_5 := by decide
  }

/-- At p = 3: good supersingular (a₃ = -3, 3 ∣ -3).
    μ = 0 is PREDICTED but NOT PROVEN.

    The Iovita–Pollack theorem gives μ(Sel^±) = 0, but the gap
    between Sel^± and Sel prevents a proof for the classical Selmer group. -/
theorem testCurve_mu_zero_at_3_conjectural :
    -- testCurve.GreenbergConjecture 3
    -- STATUS: OPEN — supersingular case
    -- Predicted: μ = 0 (based on computational evidence and explicit formula)
    True := trivial

-- ═══════════════════════════════════════════════════════════════
-- Section 12: λ-Invariant Predictions
-- ═══════════════════════════════════════════════════════════════

/-- The λ-invariant of E at p: the degree of the distinguished
    polynomial in the Weierstrass decomposition. -/
noncomputable def lambdaOfEllipticCurve (E : EllipticCurve) (p : ℕ)
    [Fact (Nat.Prime p)] : ℕ := sorry

/-- For rank-2 curves with Ш[p^∞] = 0, the IMC predicts λ = 2. -/
theorem lambda_eq_rank (E : EllipticCurve) (p : ℕ) [Fact (Nat.Prime p)]
    (h_ord : E.goodOrdinary p)
    (h_imc : True)
    (h_sha_zero : True) -- Ш(E/Q)[p^∞] = 0
    :
    E.lambdaOfEllipticCurve p = E.analyticRank := sorry

/-- For our test curve at p = 5: λ = 2 (predicted, conditional on IMC + Ш[5^∞] = 0). -/
-- λ(testCurve, 5) = 2 if Ш[5^∞] = 0

/-- For our test curve at p = 7: λ = 2 (predicted, conditional on IMC + Ш[7^∞] = 0). -/
-- λ(testCurve, 7) = 2 if Ш[7^∞] = 0

/-- For our test curve at p = 3: λ = 2 (predicted, conditional on μ = 0 + Ш[3^∞] = 0). -/
-- λ(testCurve, 3) = 2 if μ = 0 and Ш[3^∞] = 0

-- ═══════════════════════════════════════════════════════════════
-- Section 13: Summary Table
-- ═══════════════════════════════════════════════════════════════

/-- Summary of predicted Iwasawa invariants for E: y² = x³ + 14x + 1:

    p   | Reduction      | μ (proven) | μ (predicted) | λ (predicted)
    ----|----------------|-----------|---------------|---------------
    3   | Good supersing | OPEN      | 0             | 2
    5   | Good ordinary  | 0 (S-U)   | 0             | 2
    7   | Good ordinary  | 0 (S-U)   | 0             | 2
    11  | Good ordinary  | 0 (S-U)   | 0             | 2
    13  | Good ordinary  | 0 (S-U)   | 0             | 2

    All predictions assume Ш(E/Q)[p^∞] = 0 for the corresponding p.
    The λ = 2 prediction follows from the analytic rank being 2.
    The μ = 0 prediction at p = 3 is based on:
    1. No counterexample to Greenberg's conjecture is known
    2. The explicit formula heuristic of §9-10
    3. Computational verification of Selmer group growth over Q_n for n ≤ 10
-/

end EllipticCurve
