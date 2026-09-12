# Group B: Euler Systems

## Mission

Develop and apply Euler system machinery — both classical and higher-rank — to bound Selmer groups, prove Iwasawa main conjectures, and establish new cases of the Birch and Swinnerton-Dyer conjecture. Euler systems provide the sharpest known unconditional upper bounds on Selmer groups of Galois representations. This group investigates their construction, computation, and arithmetic application to elliptic curves and modular forms, with the goal of pushing BSD results beyond rank 1.

## Assigned Directions

| ID    | Title                                                                              |
|-------|------------------------------------------------------------------------------------|
| B-001 | Kato's Euler System for Modular Forms — Generalization to Rank ≥ 2                |
| B-002 | Beilinson-Flach Elements for Rankin-Selberg Products                               |
| B-003 | Darmon Cycles and Stark-Heegner Points                                             |
| B-004 | Rubin's Euler System for CM Elliptic Curves                                       |
| B-005 | Higher-Rank Euler Systems (Nekovář, Schappacher)                                   |
| B-006 | Euler Systems for GL(n) — Discovery and Verification                              |
| B-007 | The BSD Formula via Euler System Bounds                                            |
| B-008 | p-adic L-functions from Euler Systems (Interpolation)                              |
| B-009 | Rubin's Method and Selmer Group Bounds                                             |
| B-010 | Euler Systems and Iwasawa Main Conjectures                                         |
| B-011 | Syntomic Regulators and Euler System Classes                                       |
| B-012 | Explicit Computation of Euler System Classes (SageMath/Magma)                      |

## Key Personnel

TBD

## Tools

- **Magma**: Arithmetic of modular curves, Heegner points, elliptic curve databases, computation of special values
- **SageMath**: Symbolic computation of L-functions, modular forms, Galois cohomology classes, regulator maps
- **Lean 4**: Formal verification of key structural results (Euler system norm relations, Selmer group exact sequences)
- **PARI/GP**: High-precision computation of p-adic L-functions, Heegner points, Stark-Heegner points

## Branch

`group-b-euler-systems`

## Scope

Each direction precisely identifies:
- The Galois cohomology classes defining the Euler system
- The regulator maps and Selmer conditions involved
- The exact connection to L-values and the BSD formula
- Current state of the art and main obstructions
- Concrete computational targets for verification

## Cross-Group Dependencies

- **Group A (Iwasawa Theory):** Euler systems are the primary tool for proving Iwasawa main conjectures; B-010 and A directions are deeply intertwined
- **Group D (Tate-Shafarevich):** Euler system bounds on Selmer groups imply finiteness results for III; B-007 feeds into D directions
- **Group E (p-adic Methods):** p-adic L-functions constructed from Euler systems (B-008) interact with the p-adic BSD conjecture
- **Group F (Motivic/Cohomological):** Syntomic regulators (B-011) and motivic cohomology provide the abstract framework for Euler system classes
- **Group H (Computational):** B-012 computational targets overlap with Group H's verification efforts
