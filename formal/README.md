# Formal Verification — BSD Research Swarm

This directory contains Lean 4 files attempting to formalize aspects of the
Birch and Swinnerton-Dyer (BSD) conjecture.  **Only `OneSmallLemma.lean`
compiles.**  All other files are research skeletons: they declare definitions,
axioms, and theorem statements with `sorry` bodies, but have never been
compiled against Mathlib.

---

## Compilation Status

| File | Compiles? | Notes |
|------|-----------|-------|
| `OneSmallLemma.lean` | **Yes** | Self-contained lemma about element orders in finite groups. Uses `Mathlib.GroupTheory.OrderOfElement`. |
| All other `.lean` files | **No** | Never compiled. Contain `sorry`, vacuous definitions, and type errors against current Mathlib. |

---

## Files

### Core Definitions and Axioms

| File | Contents | Issues |
|------|----------|--------|
| `BSD_Core.lean` | Core definitions: elliptic curves over ℚ, L-function, analytic rank, BSD conjecture (weak + strong), arithmetic invariants (period, regulator, Tamagawa, Ш). | Every definition body is `sorry`. The `EllipticCurve` structure duplicates `Axioms_BSD.lean`. Never compiled. |
| `Axioms_BSD.lean` | Comprehensive axiom declarations for all deep results underpinning the BSD formalization: BCDT modularity, Mordell–Weil, Mazur torsion, Serre open image, Kolyvagin, Gross–Zagier, Cassels pairing, Selmer groups. | All axiom bodies are omitted (correct for Lean 4 axioms). The file is self-consistent in type signatures but was never compiled. Some types are `sorry` placeholders (e.g., `conductor`, `analyticRank`). |

### The One Proof That Works

| File | Contents | Issues |
|------|----------|--------|
| `OneSmallLemma.lean` | For a finite abelian group $G$, if $p > |G|$ then $G$ has no element of order $p$. Proof via Lagrange's theorem. | **Compiles and is correct.** This is the only verified proof in the repository. |

### Universal Visibility Proof (Research Skeleton)

| File | Contents | Issues |
|------|----------|--------|
| `Universal_Visibility_Proof.lean` | Main theorem: for every $E/\mathbb{Q}$ with rank ≥ 2, $K[p]^{G_\mathbb{Q}} = 0$ for all sufficiently large primes $p$. 4-step proof structure. | 6 axioms, all deep. Never compiled. Definitions duplicate `BSD_Core.lean`. |
| `Universal_Visibility_Proof_V2.lean` | Version 2: proper axioms (no `sorry` in definitions or axiom theorems). | Same 6 axioms. Never compiled. |
| `Universal_Visibility_Proof_V3.lean` | Version 3: axioms 1 and 2 proven (left-exactness + Lagrange). Axioms reduced from 6 to 4. | Never compiled. |
| `Universal_Visibility_Proof_V4.lean` | Version 4: axioms 1, 2, and 4 proven. Axioms reduced to 3. | Never compiled. |
| `Universal_Visibility_Proof_V5.lean` | Version 5: all 4 original axioms replaced by proofs or eliminated. Only 2 axioms remain (Serre's open image + visibility forcing Ш = 0). | Never compiled. The `injective_into_trivial` lemma is fully proven. |
| `PROOF_UNIVERSAL_VISIBILITY.lean` | Research skeleton with full 4-step proof structure, axioms for deep theorems (Skinner–Urban, Kobayashi, Poitou–Tate, Cassels). | All deep results are `sorry`. Never compiled. Imports Mathlib modules that may not exist in current Mathlib4. |

### Skinner–Urban Finiteness

| File | Contents | Issues |
|------|----------|--------|
| `SkinnerUrban.lean` | Case-analysis proof that Ш[$p^\infty$] is finite for all primes $p$ (semistable $E$). Dispatches: ordinary → Skinner–Urban; supersingular → Kobayashi; multiplicative → Mazur; small primes → Skinner–Wiles. | All deep results are axioms. The case-analysis proof (`sha_finite_all_primes`) is structurally complete but uses `sorry` axioms. Never compiled. |

### Ш Finiteness Proof

| File | Contents | Issues |
|------|----------|--------|
| `PROOF_SHA_FINITE.lean` | Finiteness of Ш for rank ≥ 2 curves. Three cases: visibility forces Ш = 0; non-existence of "bad" primes (Serre); general Ш[$p^\infty$] finite via IMC + μ = 0. | All definitions are `sorry`. Imports `Mathlib.AlgebraicGeometry.EllipticCurve.Weierstrass` which may not exist. Never compiled. |

### Supporting Theory

| File | Contents | Issues |
|------|----------|--------|
| `BSD_Rank01.lean` | BSD for rank ≤ 1: Gross–Zagier + Kolyvagin + Skinner–Urban. Strong BSD formula. | All theorems are `sorry`. Never compiled. |
| `GaloisCohomology.lean` | $H^0$, $H^1$, restriction, inflation, connecting homomorphisms, long exact sequences. | All definitions and theorems are `sorry`. Never compiled. |
| `SelmerGroups.lean` | Selmer groups, local conditions, Tate–Shafarevich group, visibility kernel, exact sequences. | All `sorry`. Never compiled. |
| `MazurVisibility.lean` | Mazur's visibility principle: $K[p]^{G_\mathbb{Q}} = 0 \Rightarrow \text{Ш}[p] = 0$. Long exact sequence in Galois cohomology. | All `sorry`. Never compiled. |
| `PoitouTate.lean` | The 9-term Poitou–Tate exact sequence for finite $G_\mathbb{Q}$-modules. | All `sorry`. Never compiled. |
| `CasselsTate.lean` | Cassels–Tate alternating pairing, perfect-square theorem, Skinner–Urban finiteness, Ш vanishing. | All `sorry`. Never compiled. |
| `ExplicitFormula.lean` | The explicit formula for $a_p$ bias detecting analytic rank. Phase 3 computational evidence formalization. | All `sorry`. Never compiled. |

### Axiom Replacement Proofs

These files attempt to replace axioms from the universal visibility proof with actual proofs:

| File | Contents | Issues |
|------|----------|--------|
| `Prove_Ax1.lean` | Left-exactness of the $G$-invariant functor: if $f: A \to B$ is injective, then $f^G: A^G \to B^G$ is injective. | Proof sketch present but never compiled against Mathlib. |
| `Prove_Ax2.lean` | Jacobian torsion triviality: if $p > |G|$ then $G[p] = 0$. Same as `OneSmallLemma.lean` but for multiplicative notation. | Proof present but never compiled. |
| `Prove_Ax4.lean` | Witness prime existence: for any $m$ and bound $B$, there exists a prime $p > B$ with $p \nmid m$. | Proof sketch present but never compiled. |
| `Prove_Axiom5.lean` | Ш vanishes from kernel: $K[p]^{G_\mathbb{Q}} = 0 \Rightarrow \text{Ш}[p] = 0$. Uses Poitou–Tate injectivity. | Depends on `poitou_tate_injective` axiom. Never compiled. |
| `Prove_Axiom6.lean` | Ш = 0 from $p$-vanishing: if $\text{Ш}[p] = 0$ for some $p$, then $\text{Ш} = 0$. Induction on element order. | Proof sketch present but never compiled. |
| `Prove_PoitouTate_Injective.lean` | Derives `poitou_tate_injective` from the Poitou–Tate exact sequence + inflation–restriction. | Depends on `PoitouTate.lean` (all `sorry`). Never compiled. |
| `Prove_ShaTorsion.lean` | Ш is torsion (Cassels 1962): every element has finite order. | Proof sketch present but never compiled. |

---

## Known Issues (All Files Except OneSmallLemma.lean)

1. **Nothing compiles.**  Every file except `OneSmallLemma.lean` contains
   `sorry` in definition bodies, uses `noncomputable section` throughout,
   and has never been type-checked against any version of Mathlib4.

2. **Vacuous definitions.**  Many core types (`EllipticCurve.conductor`,
   `analyticRank`, `MordellWeilGroup`, `TateShafarevich`, etc.) are defined
   as `sorry`, meaning they have no implementation.  Any theorem depending
   on them is vacuously true or uncheckable.

3. **Duplicate definitions.**  `EllipticCurve` is defined independently in
   `BSD_Core.lean`, `Axioms_BSD.lean`, `SkinnerUrban.lean`,
   `Universal_Visibility_Proof.lean`, and `PROOF_SHA_FINITE.lean` with
   incompatible field sets.  No shared import hierarchy exists.

4. **Stale Mathlib imports.**  Several files import modules that may not
   exist in current Mathlib4 (e.g.,
   `Mathlib.AlgebraicGeometry.EllipticCurve.Weierstrass`,
   `Mathlib.NumberTheory.LSeries.Elliptic`,
   `Mathlib.LinearAlgebra.SymplecticForm`).

5. **Axiom stacking.**  The "proofs" in `Prove_Ax*.lean` files replace one
   axiom with another (e.g., `poitou_tate_injective`) or depend on files
   that are entirely `sorry`.  The logical dependency chain is not resolved.

6. **No `lakefile.toml` at the right level.**  The repository root has a
   `lakefile.toml` but it may not match the import structure of the Lean
   files.  The `lean-toolchain` specifies a Lean 4 version that may be
   incompatible with the Mathlib4 imports used.

---

## Summary

The only verified result in this directory is `OneSmallLemma.lean` — a
self-contained application of Lagrange's theorem.  All other files are
**research scaffolding**: they sketch the logical structure of a BSD
formalization, declare the correct type signatures for deep theorems, and
outline proof strategies, but none of them compile or constitute a formal
proof.
