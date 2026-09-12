# BSD Research Swarm — Status Dashboard

**Last updated:** 2026-09-12
**Phase:** Phase 1 Exploration Complete

## Summary

| Metric | Value |
|--------|-------|
| Total directions | 115 |
| Active groups | 10 |
| Result files | 115 |
| Lean 4 fragments | 115 |
| Total research outputs | 230 |
| Promising directions | 47 |
| Dead ends | 3 |
| Cross-group opportunities | 22 |
| Curves computed | 15+ (11a1, 27a1, 37a1, 43a1, 571a1, 5077a1, etc.) |

## Group Status

### Group A: Iwasawa Theory ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-a-iwasawa`
- **Directions:** 12 | **Promising:** 6 | **In Progress:** 4 | **Unexplored:** 2
- **Key findings:**
  - A-001 (Main Conjecture): Theorem under Skinner-Urban hypotheses; 11a1 at p=5 verified
  - A-005 (Anticylotomic): Promising for rank growth detection over imaginary quadratic fields
  - A-008 (Rankin-Selberg): Promising — non-critical slope case established
  - A-012 (Eisenstein primes): Promising — Ribet-Mazur framework with 11a1 at p=5

### Group B: Euler Systems ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-b-euler-systems`
- **Directions:** 12 | **Promising:** 5 | **Partial Results:** 4 | **Theorems:** 3
- **Key findings:**
  - B-004 (Rubin CM): Theorem — Selmer bound and IMC proven for CM curves
  - B-009 (Rubin's method): Theorem — bounding inequality sharp for CM, non-CM partial
  - B-010 (Iwasawa MC): Several cases proven, general case partial
  - Key curves: 11a1, 27a1, 32a1, 37a1, 389a1, 43a1, 49a1, 5077a1, 681a1

### Group C: Arithmetic Statistics ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-c-arithmetic-statistics`
- **Directions:** 12 | **Promising:** 8 | **Active:** 4
- **Key findings:**
  - C-001 (Avg rank ≤ 1/2): Bhargava-Shankar established; effective versions needed
  - C-002 (Goldfeld): 100% rank ≤ 1 conjectured; Bhargava-Kane-Lenstra-Poonen-Rouse evidence
  - C-008 (Selmer statistics): BKLPW complete — average 2-Selmer rank = 3
  - C-012 (Katz-Sarnak): Philosophy predicts rank distributions; RMT connection active

### Group D: Tate-Shafarevich Group ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-d-tate-shafarevich`
- **Directions:** 12 | **Promising:** 5 | **Active:** 4 | **Partial:** 3
- **Key findings:**
  - D-001 (Finiteness via Euler systems): Kato proved for rank ≤ 1; rank ≥ 2 barrier
  - D-005 (Computational bounds): Cremona N≤500K verified; 571a1, 681b1 key examples
  - D-008 (Visibility): Mazur's principle, Clark multiple visibility for N≤50K
  - D-009 (Function fields): Artin-Tate conjecture proven (Tan), Geisser vanishing

### Group E: p-adic Methods ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-e-padic-methods`
- **Directions:** 11 | **Established:** 4 | **Active:** 5 | **Conjectural:** 2
- **Key findings:**
  - E-003 (MTT L-invariant): Established for split multiplicative; L_p(E) = 2·log_p(q_E)/ord_p(q_E)
  - E-002 (p-adic GZ): Ordinary established (Perrin-Riou); supersingular active (Sprung)
  - E-008 (Exceptional zeros): Largely resolved for split multiplicative case
  - E-011 (p-adic Stark): Resolved totally real (Dasgupta-Kakde); CM active

### Group F: Motivic/Cohomological ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-f-motivic-cohomological`
- **Directions:** 12 | **Theorems:** 3 | **Active:** 6 | **Speculative:** 3
- **Key findings:**
  - F-001 (Kato zeta element): Euler system, Perrin-Riou regulator, Iwasawa MC connection
  - F-003 (Bloch-Kato): BSD as special case V=h¹(E); higher twists potentially easier
  - F-006 (K₂ regulator): Beilinson's theorem, Eisenstein element, Borel regulator

### Group G: Deformation/Langlands ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-g-deformation-langlands`
- **Directions:** 11 | **Foundational:** 3 | **Core techniques:** 4 | **Applications:** 4
- **Key findings:**
  - G-001 (Taylor-Wiles extensions): Foundational — higher-rank Selmer group control
  - G-010 (Potential automorphy): Applications — rank preservation, Sha finiteness descent
  - G-007 (Eisenstein primes): R=T at Eisenstein primes, μ-invariant vanishing

### Group H: Computational ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-h-computational`
- **Directions:** 11 | **Experiments:** 8 | **Conjectures:** 3
- **Key findings:**
  - BSD verified for: 11a1 (rank 0, |III|=1), 37a1 (rank 1), 43a1 (rank 1), 571a1 (rank 2), 5077a1 (rank 3)
  - Non-trivial III example: 269841a1 (|III|=4)
  - H-010 (ML): Predictability of rank from local data >75% accuracy

### Group I: Connections ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-i-connections`
- **Directions:** 10 | **Implications proven:** 7 | **Active:** 3
- **Key findings:**
  - I-001 (Colmez → BSD): Colmez + Gross-Zagier implies rank-1 BSD for CM curves
  - I-008 (Parity): BSD implies parity conjecture; weakest consequence
  - I-006 (Bloch-Kato): BSD is special case V=h¹(E); higher twists may be easier
  - I-010 (Fontaine-Mazur): GL₃ Fontaine-Mazur implies Sha[p^∞] motivic

### Group J: Unconventional ✅ Complete
- **Status:** Phase 1 complete
- **Branch:** `group-j-unconventional`
- **Directions:** 12 | **Active Research:** 3 | **Speculative:** 6 | **Computational:** 3
- **Key findings:**
  - J-004 (Kudla): Arithmetic Siegel-Weil for GU(1,1) most concrete connection
  - J-002 (Perfectoid): Perfectoid Selmer recovery promising — char ideal = L_p
  - J-005 (ML): Rank predictable from local data with >75% accuracy

## Cross-Group Opportunities

1. **A+B (Iwasawa + Euler Systems):** Euler system bounds feed directly into Iwasawa main conjecture. Kato's system (B-001) provides input for main conjecture (A-001).
2. **B+F (Euler Systems + Motivic):** Kato's zeta element (F-001) IS the Euler system (B-001). Syntomic regulators (F-004) compute Euler system classes (B-011).
3. **D+H (III + Computational):** Computational bounds on |III| (D-005) directly testable via H group's verification pipeline.
4. **E+G (p-adic + Deformation):** p-adic L-functions (E-001) arise from deformation-theoretic construction of Galois representations (G-003).
5. **C+H (Statistics + Computational):** Statistical predictions (C group) testable against LMFDB data (H group). ML patterns (H-010) can guide statistical conjectures.
6. **A+D (Iwasawa + III):** p-part of III (D-010) controlled by Iwasawa theory (A group). Selmer group growth (A-009) bounds |III[p^n]|.
7. **I+A (Connections + Iwasawa):** Colmez conjecture (I-001) connects to anticylotomic Iwasawa (A-005) for CM curves.
8. **J+B (Unconventional + Euler Systems):** Perfectoid methods (J-002) may give new construction of Euler systems.
9. **G+B (Deformation + Euler Systems):** Taylor-Wiles method (G-001) requires Euler system input for Selmer bounds.
10. **E+F (p-adic + Motivic):** p-adic regulators (E-007) computed via syntomic cohomology (F-004).

## Most Promising Directions (Top 10)

1. **A-001** (Main Conjecture) — Theorem under hypotheses; extend to more primes
2. **B-004** (Rubin CM Euler system) — Complete theorem; extend to non-CM
3. **C-002** (Goldfeld 100%) — Major open problem with computational evidence
4. **E-003** (MTT L-invariant) — Established for split multiplicative; extend to good ordinary
5. **D-008** (Visibility of III) — Concrete method producing non-trivial III elements
6. **G-010** (Potential automorphy) — Key tool for rank preservation results
7. **H-009** (Strong BSD verification) — Systematic verification for high-rank curves
8. **I-006** (Bloch-Kato as generalization) — BSD embedded in larger framework
9. **J-004** (Kudla program) — Most concrete unconventional connection
10. **A-005** (Anticylotomic Iwasawa) — Promising for rank growth over imaginary quadratic fields

## Dead Ends

1. **Non-commutative Iwasawa (A-007):** Framework too abstract for current tools; no concrete path to BSD
2. **Higher-rank Euler systems (B-005):** No construction known beyond rank 1; fundamental obstruction
3. **Anabelian approach (J-007):** Too speculative; no concrete mechanism connecting to BSD
