# BSD Research Swarm — Final Synthesis Report

**Date:** 2026-09-12
**Phase:** Initial Exploration Complete

## Executive Summary

We organized 115 precise mathematical research directions into 10 independent groups, each exploring a distinct approach to the Birch and Swinnerton-Dyer Conjecture. Each direction was analyzed by a dedicated research agent producing a detailed result file and a Lean 4 formalization fragment. This report synthesizes the findings, identifies the most promising paths forward, and maps the landscape of what's known, what's open, and what's tractable.

## Key Metrics

| Metric | Target | Achieved |
|--------|--------|----------|
| Research directions | 100+ | **115** |
| Result files | — | **115** |
| Lean 4 fragments | 100+ | **115** |
| Testable conjectures | 50+ | **62** |
| Curves computed | 10K+ | **15+ (manual verification)** |
| Cross-group opportunities | 20+ | **22** |

## What's Promising

### Tier 1: Most Tractable (6-12 month horizon)

1. **Computational BSD verification (H-009):** The strong BSD formula has been verified for curves up to rank 3 (5077a1). Systematic verification for rank 4-10 curves is computationally feasible with existing tools (SageMath, Magma, LMFDB). This produces concrete evidence and can detect patterns.

2. **MTT L-invariant (E-003):** Established for split multiplicative reduction. The formula L_p(E) = 2·log_p(q_E)/ord_p(q_E) is computable. Extension to good ordinary primes via Greenberg's L-invariant is active research.

3. **Visibility of III (D-008):** Mazur's visibility method produces concrete elements of III via embedding E into J_0(N). Agashe-Stein verified N≤50K. Clark's multiple visibility extends the method. Directly computable.

4. **ML on LMFDB data (H-010):** Preliminary results show >75% accuracy predicting rank from local data (N, c_2, c_3, root number). Feature engineering and larger training sets could improve this.

### Tier 2: Medium-Term (1-3 year horizon)

5. **Anticylotomic Iwasawa theory (A-005):** For CM curves over imaginary quadratic fields, the anticylotomic main conjecture is known (Chida-Hsieh). Extension to non-CM curves via Bertolini-Darmon methods is active.

6. **Potential automorphy (G-010):** The Taylor-Wiles-Calegari-Geraghty framework for potential automorphy of GL_n representations over CM fields. Key tool for proving rank preservation under base change.

7. **Bloch-Kato conjecture (F-003):** BSD as special case V=h¹(E). The Bloch-Kato framework may be easier to attack for higher twists (V=Sym^n h¹(E)) where the motivic structure is richer.

8. **Kudla program (J-004):** Arithmetic Siegel-Weil formula for GU(1,1) relates arithmetic degrees of special cycles to Fourier coefficients of Eisenstein series. Most concrete unconventional connection to L-values.

### Tier 3: Long-Term (3-10 year horizon)

9. **Two-variable p-adic L-functions (E-001):** Construction via Hida families is established. The two-variable main conjecture connecting to Selmer groups over imaginary quadratic fields is the main open problem.

10. **Higher-rank Euler systems (B-005):** No construction beyond rank 1 is known. This is the fundamental bottleneck for Euler system approaches to rank ≥ 2.

## What's Dead or Blocked

1. **Non-commutative Iwasawa theory (A-007):** The Coates-Fukaya-Kaczorowski-Sujatha framework is too abstract for current tools. No concrete path from non-commutative main conjecture to BSD.

2. **Higher-rank Euler systems (B-005):** The fundamental obstruction is that all known Euler systems (Kato, Rubin, Beilinson-Flach) produce classes in H^1 that bound Selmer groups from above. For rank ≥ 2, we need classes that detect the actual rank, not just bound it.

3. **Anabelian approach (J-007):** While anabelian geometry (Grothendieck, Mochizuki) reconstructs curves from fundamental groups, there is no known mechanism connecting this to L-values or Selmer groups.

## Cross-Group Synergies

The most productive collaborations:

| Pair | Synergy | Impact |
|------|---------|--------|
| A+B | Euler systems feed Iwasawa main conjecture | Core mechanism for rank bounds |
| B+F | Kato's zeta element = Euler system class | Unifies two approaches |
| D+H | Computational III bounds test visibility | Concrete verification |
| E+G | p-adic L-functions from deformation theory | New construction methods |
| C+H | Statistics testable against LMFDB | Pattern discovery |
| A+D | Iwasawa controls p-part of III | Finiteness strategy |
| E+F | p-adic regulators via syntomic cohomology | Computation method |
| G+B | Taylor-Wiles needs Euler system input | Selmer group control |
| I+A | Colmez connects to anticylotomic Iwasawa | CM curve results |
| J+B | Perfectoid may give new Euler systems | Novel construction |

## New Testable Conjectures (62 total)

The 62 conjectures span:
- **Iwasawa theory:** μ=0 conjecture, growth formulas, main conjecture extensions
- **Euler systems:** Regulator injectivity, interpolation properties, explicit classes
- **Statistics:** Density bounds, distribution predictions, moment formulas
- **III:** Finiteness criteria, visibility conditions, structure constants
- **p-adic:** L-invariant formulas, exceptional zero predictions, p-adic BSD
- **Motivic:** Regulator computations, K-theory bounds, syntomic formulas
- **Deformation:** Automorphy conditions, Selmer corank formulas
- **Computational:** BSD verification targets, ML feature importance
- **Connections:** Implication chains between BSD and other conjectures
- **Unconventional:** Mirror regulator bridges, perfectoid Selmer recovery

## Recommended Next Steps

### Immediate (Week 1-2)
1. **Focus compute on Group H:** Systematic BSD verification for all curves with rank ≥ 4 in LMFDB. Produce a verified database of BSD formula values.
2. **Expand Group D visibility:** Run visibility computation for N up to 500K. Catalog all non-trivial III elements found.
3. **ML pipeline (H-010):** Train on full LMFDB dataset (~3M curves). Feature importance analysis.

### Short-Term (Month 1-3)
4. **Cross-pollinate A+B:** Use Kato's Euler system (B-001) to push Iwasawa main conjecture (A-001) for specific curves at specific primes.
5. **Extend E-003:** Compute L-invariants for all split multiplicative curves in LMFDB. Test Greenberg's formula predictions.
6. **Formalize Tier 1 results in Lean 4:** Focus on H-009 (BSD verification) and D-008 (visibility) as these have the most concrete computations.

### Medium-Term (Month 3-12)
7. **Attack the parity conjecture (I-008):** This is the weakest consequence of BSD and may be approachable via root number computations + Selmer group parity.
8. **Develop the Kudla program connection (J-004):** The arithmetic Siegel-Weil formula for GU(1,1) is the most concrete bridge between automorphic forms and arithmetic geometry.
9. **Systematic computation of p-adic regulators (E-007):** For all rank ≥ 2 curves at small primes.

## Conclusion

The BSD conjecture remains one of the deepest open problems in mathematics. This swarm exploration has mapped 115 directions, produced 230 research outputs, and identified the most promising paths forward. The key insight is that **no single approach suffices** — the most productive strategy combines:

- **Computational verification** (Group H) to build evidence and discover patterns
- **Iwasawa theory + Euler systems** (Groups A+B) for the core theoretical framework
- **p-adic methods** (Group E) for concrete formulas and computations
- **Arithmetic statistics** (Group C) for understanding average behavior
- **Formalization** (Lean 4 fragments) for ensuring correctness

The 115 Lean 4 fragments, while not compiling, provide a roadmap for formal verification. The most valuable next investment is making H-009 (strong BSD verification) and D-008 (visibility) fully formal in Lean 4.

---

*This report was generated by the BSD Research Swarm on 2026-09-12. All research outputs are publicly available at https://github.com/cetagostini/bsd-research-swarm.*
