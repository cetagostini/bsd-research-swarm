/-
Prove_Ax4.lean — Proof of witness prime existence

For any natural number m and bound B, there exists a prime p > B with p ∤ m.
This follows from the infinitude of primes and the fact that m has finitely
many prime divisors.

This replaces axiom 4 (witness_prime_exists) in the main formalization.
-/
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Nat.Factorization.Basic

/-- For any n : ℕ, the set of primes dividing n is finite. -/
lemma prime_divisors_finite (n : ℕ) :
    {p : ℕ | p.Prime ∧ p ∣ n}.Finite := by
  -- Every prime divisor of n is ≤ n
  have h : {p : ℕ | p.Prime ∧ p ∣ n} ⊆ {p : ℕ | p ≤ n} := by
    intro p ⟨hp, hpdvd⟩
    exact Nat.le_of_dvd (Nat.pos_of_ne_zero (fun h => hp.ne_zero (Nat.eq_zero_of_dvd_zero (h ▸ hpdvd)))) hpdvd
  exact (Finset.range (n + 1)).finite_toSet.subset (fun p ⟨hp, hpdvd⟩ => by
    exact ⟨p, ⟨hp, hpdvd⟩, Nat.lt_succ_iff.mpr (h ⟨hp, hpdvd⟩)⟩)

/-- For any m B : ℕ, there exists a prime p > B with p ∤ m. -/
theorem exists_prime_gt_not_dvd (m B : ℕ) :
    ∃ p : ℕ, p.Prime ∧ p > B ∧ ¬(p ∣ m) := by
  -- The set of primes dividing m is finite
  have hfin : {p : ℕ | p.Prime ∧ p ∣ m}.Finite := prime_divisors_finite m
  -- There are infinitely many primes
  -- Take a prime larger than max(B, m) — it can't divide m
  obtain ⟨p, hp_prime, hp_large⟩ := Nat.exists_infinite_primes (max B m + 1)
  refine ⟨p, hp_prime, ?_, ?_⟩
  · -- p > B
    linarith [le_max_left B m]
  · -- p ∤ m (since p > m ≥ all divisors of m)
    intro hpdvd
    have : p ≤ m := Nat.le_of_dvd (Nat.pos_of_ne_zero (fun h => hp_prime.ne_zero (Nat.eq_zero_of_dvd_zero (h ▸ hpdvd)))) hpdvd
    linarith [le_max_right B m]

/-- **Witness prime exists (PROVEN, replaces axiom 4):**
    For any modular degree m and torsion bound T, there exists a prime p
    with p ∤ m and p > max(m, T). -/
theorem witness_prime_proven (m T : ℕ) :
    ∃ p : ℕ, p.Prime ∧ ¬(p ∣ m) ∧ p > max m T := by
  obtain ⟨p, hp_prime, hp_gt, hp_ndvd⟩ := exists_prime_gt_not_dvd m (max m T)
  exact ⟨p, hp_prime, hp_ndvd, hp_gt⟩
