# Group D: Tate-Shafarevich Group (III)

## Mission

Attack the finiteness and structure of the Tate-Shafarevich group Sha(E/K), especially for elliptic curves of analytic rank ≥ 2.

The Tate-Shafarevich group measures the failure of the local-to-global principle for principal homogeneous spaces of an elliptic curve. Conjecturally finite, its structure encodes deep arithmetic information directly tied to the Birch and Swinnerton-Dyer conjecture: the order of Sha appears in the leading term of the L-function via the BSD formula

$$L^{(r)}(E/K, 1)/r! = \frac{\Omega_E \cdot R_E \cdot |\text{Sha}(E/K)| \cdot \prod c_v}{|E(K)_{\text{tors}}|^2}$$

Finiteness of Sha is the critical bridge between analytic data (L-values) and algebraic invariants (Selmer groups, heights, regulators).

## Scope

This group focuses on:
1. Proving or conditional finiteness of III via Euler systems, Iwasawa theory, and descent
2. Structural results: Cassels-Tate duality, p^n-torsion, p∞-Selmer control
3. Computational verification and bounding |III| for specific curves
4. Parity phenomena, visibility, and function-field analogues
5. Effective and explicit upper bounds for |III|

## Assigned Directions

| ID    | Title                                                     | Status       |
|-------|-----------------------------------------------------------|--------------|
| D-001 | Finiteness of III via Euler Systems (Kato)               | Speculative  |
| D-002 | Cassels-Tate Duality and III Structure                   | Established  |
| D-003 | Descent Methods for Bounding |III|                       | Active       |
| D-004 | p-adic Methods for III                                   | Active       |
| D-005 | Computational Bounds on |III| for Specific Curves        | Active       |
| D-006 | The Cassels-Tate Pairing and Non-degeneracy              | Established  |
| D-007 | Structure Constants: III[p^n] and p∞-Selmer Groups       | Active       |
| D-008 | Visibility Method for Elements of III                    | Active       |
| D-009 | III over Function Fields                                 | Active       |
| D-010 | The p-part of III and Iwasawa Theory                     | Active       |
| D-011 | Heuristics for |III| Distribution                        | Speculative  |
| D-012 | Effective Finiteness: Explicit Upper Bounds for |III|    | Open         |

## Branch

```
group-d-tate-shafarevich
```

## Dependencies

- Group A (Analytic): Rank computation, L-function vanishing orders
- Group B (Algebraic): Selmer groups, Galois cohomology inputs
- Group C (Heegner/Congruence): Heegner points provide rank-1 input to Euler systems

## Output Format

Each direction produces:
- Mathematical statement and precise conjecture
- Survey of known results with references
- Identification of main technical obstacles
- Concrete proposals for new approaches
- Computational data where applicable
