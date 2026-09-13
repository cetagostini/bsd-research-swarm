# BSD Research Program — Restructured

**Date:** 2026-09-13
**Source:** Expert mathematical review (50 directions)

## Critical Corrections

### 1. Selmer computation is circular
`selmer_computation.py` assumes sha_order=1, then derives the expected Selmer dimension.
It does NOT perform a descent. The 433a1 coefficients also describe the wrong curve
(discriminant -675 vs correct -433).

### 2. Naïve diagonal on E³ vanishes
Gross–Schoen's Proposition 4.5 and equation (4.4) imply 6Δₑ=0 for a genus-one curve.
The cycle vanishes in the Chow group with rational coefficients. The viable program uses
modular/Shimura curves, projectors, auxiliary forms, and generalized classes.

### 3. Higher-rank machinery already exists
- Kim: higher-rank Selmer structure via Kurihara numbers
- Castella: rank-two implications with generalized Kato classes
- Burns–Sakamoto–Sano, Bullach–Burns: abstract Euler-system machinery

The missing input is NOT "invent all higher-rank theory." It is a particular arithmetic
class, nonvanishing statement, integral comparison, or specialization argument.

## Correct Benchmark

**Curve: 389.a1**
```
E: y² + y = x³ + x² - 2x
P = (0,0), Q = (1,0)
Δ_E = 389, #E(F₅) = 9, a₅ = -3
```
LMFDB records algebraic and analytic rank 2. This is a reproduction benchmark.

## Goal: One Complete Arithmetic Proof Package

### Deliverable 1: Certified 2-descent for 389.a1
- Independently compute the 2-Selmer group (actual descent, not assumed Sha)
- Prove the two-point rank lower bound (P,Q independent via canonical height)
- Retain local completeness certificates
- Deduce Sha(E/Q)[2^∞] = 0 from the exact sequence
- Resolve lattice index before using regulator

### Deliverable 2: Modern fixed-prime theorem at p=5
- Match 389.a1 to exact hypotheses of Kim's theorem
- Compute normalized Kurihara numbers
- Establish semilocal Selmer conclusion
- State precisely what's proved about 5-primary arithmetic

### Deliverable 3: One original lemma
Target: Direction 50 (effective local-solubility precision bound)
or Direction 26/27/44 (specialization/integer primitivity/hypothesis removal)

Gates:
- Precise statement (named objects, hypotheses, conclusion)
- Novelty (comparison with closest existing theorem)
- Proof (no assumed BSD/Sha conclusion in inputs)
- Consequence (named computation or theorem becomes stronger)

## The 50 Directions (organized by priority)

### Phase 1: Certified Arithmetic [Directions 1-10] — REPRODUCTION
Goal: Independently reproduce known rank-2 arithmetic for 389.a1

1. Certify curve identity and local invariants [K]
2. Perform actual full 2-descent [K]
3. Prove completeness of local tests [K]
4. Certify two independent rational points [K]
5. Prove rank and 2-primary Sha vanishing [K]
6. Certified nontrivial Sha control example [K]
7. Compute induced Cassels–Tate pairing [K]
8. Higher 4- or 8-descent [K]
9. Resolve odd-primary component [K]
10. Certify Mordell–Weil lattice index [K]

### Phase 2: Analytic/Rigorous [Directions 11-20] — REPRODUCTION + RESEARCH
Goal: Certify L-function and regulator computations

11. Certify central vanishing exactly [K]
12. Certify L″(E,1) ≠ 0 [K]
13. Compute certified real regulator [K]
14. Resolve BSD normalization factors [K]
15. Certify ordinary p-adic height determinant [K]
16. Certify cyclotomic p-adic leading term [K]
17. Treat exceptional zeros correctly [K]
18. Study degeneracy through derived heights [R]
19. Signed supersingular counterpart [R]
20. Determinant-line formula [R]

### Phase 3: Iwasawa/Euler Systems [Directions 21-30] — MODERN MACHINERY
Goal: Apply existing higher-rank theorems to 389.a1

21. Build fixed-(E,p) hypothesis matrix [K]
22. Compute exact Kurihara numbers [K]
23. Reconstruct Selmer info from semilocal data [K]
24. Reproduce generalized Kato-class theorem [K→R]
25. Extract higher Fitting-ideal information [K→R]
26. Control specialization at augmentation zero [R]
27. Prove integral primitivity of relevant class [R]
28. Construct concrete rank-two determinant class [F]
29. Establish required norm relations [R/F]
30. Prove sufficient Selmer control from classes [F]

### Phase 4: Geometric [Directions 31-40] — CORRECTED PROGRAM
Goal: Build correct geometric program (NOT naïve diagonal)

31. Close naïve genus-one diagonal route [K]
32. Compute correct motive and vanishing order [K]
33. Select useful auxiliary modular/theta forms [R]
34. Certify local signs and geometric hypotheses [K]
35. Construct projected cycle on correct variety [K→R]
36. Prove Abel–Jacobi image has required local conditions [R]
37. Prove precisely stated reciprocity formula [R/F]
38. Analyze quadratic base change correctly [K]
39. Identify correct anticyclotomic derived object [R]
40. Prove arithmetic nonvanishing beyond known cases [F]

### Phase 5: Missing Implications [Directions 41-50] — ORIGINAL WORK
Goal: Prove one new lemma or implication

41. Higher-rank p-converse in restricted setting [F]
42. Complex leading-term comparison [F]
43. Finite prime support for Sha [F]
44. Remove one hypothesis from one named theorem [R]
45. Transfer information across isogeny [K→R]
46. Parameterized descent theorem [R]
47. Restricted visibility result [R]
48. Family-level Selmer distribution [R]
49. Formalize sound arithmetic certificate checker [K→R]
50. Effective local-solubility precision bound [R]

## Starting Point

Benchmark curve: 389.a1
First task: Directions 2-5, 10 (certified 2-descent)
Second task: Directions 21-23 at p=5 (modern fixed-prime theorem)
Third task: Direction 50 or 26/27/44 (one original lemma)
