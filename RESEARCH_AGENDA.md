# BSD Research Agenda — Based on Expert Review

**Date:** 2026-09-13
**Source:** DeepSeek v4 Flash review + external critique

## The 5 Missing Mathematical Results

### 1. Rank Inequality for rank ≥ 2
**What:** Prove rank E(Q) ≤ ord_{s=1} L(E,s) for r ≥ 2
**Status:** OPEN. Only r ≤ 1 proven (Gross-Zagier/Kolyvagin)
**Tools needed:** Higher-derivative Gross-Zagier, diagonal cycles, p-adic methods
**Key papers:** Bertolini-Darmon, Yuan-Zhang-Zhang, Kings-Loeffler-Zerbes

### 2. Ш Finiteness for rank ≥ 2
**What:** Prove corank Sel_{p^∞}(E/Q) = rank E(Q) for all p
**Status:** OPEN. All existing machines cap at r ≤ 1
**Tools needed:** Rank-r Euler systems or substitute
**Key papers:** Kato, Kolyvagin, Skinner-Urban (all r ≤ 1)

### 3. Rank-r Euler System
**What:** r norm-compatible independent cohomology classes in H^1
**Status:** OPEN. No explicit classes known for r ≥ 2
**Tools needed:** New construction (diagonal cycles, Beilinson-Flach, etc.)
**Key papers:** Nekovář (Ext^k program — no explicit classes)

### 4. Unconditional μ=0 and Full IMC
**What:** Prove μ=0 and Iwasawa Main Conjecture at ALL primes
**Status:** Partially known. Skinner-Urban covers good ordinary p ≥ 5 under hypotheses
**Tools needed:** Supersingular (±-Selmer), additive primes, small primes
**Key papers:** Skinner-Urban, Kobayashi, Pollack-Weston, Skinner-Wiles

### 5. Higher-derivative Gross-Zagier
**What:** Arithmetic cycle whose regulator computes L^{(r)}(E,1) for r ≥ 2
**Status:** ACTIVE RESEARCH. Diagonal cycles on E×E×E, anticylotomic p-adic L-functions
**Key papers:** Bertolini-Darmon-Longo, Yuan-Zhang-Zhang, GKS (Gross-Kudla-Schoen)

## 3 New Approaches (from review)

### Approach A: Diagonal Cycles (E×E×E)
The Gross-Kudla-Schoen diagonal cycle on E×E×E has a height that relates to L'''(E×E×E, s) at s=0. This is the triple product L-function, and its central derivative involves L(E,s) data. For rank 2 curves, this could provide the missing algebraic cycle.

### Approach B: Anticylotomic p-adic Methods
For E over an imaginary quadratic field K, the anticylotomic p-adic L-function has a derivative that computes Heegner point heights. For rank 2, the second derivative might compute a "higher Heegner point" via Bertolini-Darmon's construction.

### Approach C: Selmer Group Computational Approach
Instead of proving Ш finite theoretically, compute Sel_{p^∞}(E/Q) explicitly for specific curves using p-descent. If we can show corank = rank for specific rank 2 curves, that's a genuine result.

## 5-Step Research Program

### Step 1: Fix the computational pipeline
- Cross-validate against LMFDB including 194040.cu1 (|Ш|=4)
- Compute Selmer groups for specific rank 2 curves
- Produce honest numerical evidence

### Step 2: Study diagonal cycles on E×E×E
- For rank 2 curves, compute the Gross-Kudla-Schoen cycle
- Relate its height to L'''(E×E×E, 0)
- Check if this gives rank equality for specific curves

### Step 3: Develop anticylotomic p-adic methods
- For E over imaginary quadratic K, study the anticylotomic p-adic L-function
- Compute its second derivative at s=0
- Relate to "higher Heegner points"

### Step 4: Prove one honest theorem
- Target: For a specific rank 2 curve E and prime p, prove Sel_p(E/Q) has dimension 2
- Method: Explicit 2-descent + Cassels-Tate pairing
- This would prove Ш[p] = 0 for that specific curve

### Step 5: Formalize in Lean 4
- Formalize the one honest theorem
- Build around genuine objects (not axioms)
- Target: one compiling, sorry-free proof of a non-trivial arithmetic statement
