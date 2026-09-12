# Group G: Deformation Theory and Langlands Program

## Mission

Use deformation theory of Galois representations and Langlands functoriality to approach the Birch and Swinnerton-Dyer conjecture. This group investigates how the structure of Galois deformation rings, modularity lifting theorems, and automorphic L-functions constrain and determine the arithmetic of elliptic curves over number fields.

## Branch

`group-g-deformation-langlands`

## Assigned Directions

| ID | Title | Classification |
|----|-------|---------------|
| G-001 | Taylor-Wiles method extensions for higher-rank Selmer groups | Foundational |
| G-002 | Residually reducible Galois representations (Skinner-Wiles) | Core techniques |
| G-003 | Fontaine-Laffaille modules and local deformation rings | Local analysis |
| G-004 | Modularity lifting for higher-dimensional representations | Core techniques |
| G-005 | The Langlands-Weissman approach to L-values | New framework |
| G-006 | Functoriality and L-function special values (Langlands program) | Functoriality |
| G-007 | Deformation rings and Hecke algebras at Eisenstein primes | Core techniques |
| G-008 | Galois deformation theory and Selmer group structure | Foundational |
| G-009 | The Breuil-Mézard conjecture and local-global compatibility | Local analysis |
| G-010 | Potential automorphy and its consequences for BSD | Applications |
| G-011 | p-adic Langlands program and elliptic curves | p-adic methods |

## Overview

The Langlands program provides a bridge between Galois representations and automorphic forms. For elliptic curves over $\mathbb{Q}$, the modularity theorem establishes that the $\ell$-adic Galois representation $\rho_{E,\ell} \colon \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{GL}_2(\mathbb{Z}_\ell)$ arises from a weight-2 newform. Deformation theory studies how $\rho_{E,\ell}$ varies in families, and the Taylor-Wiles method proves that deformation rings are isomorphic to Hecke algebras, linking Galois-theoretic and automorphic data.

The BSD conjecture relates $L(E,1)$ (or the leading coefficient $L^*(E,1)$) to arithmetic invariants of $E$. The Galois-theoretic approach proceeds via:

1. **Selmer groups as deformation-theoretic objects**: The Selmer group $H^1_f(G_{\mathbb{Q}}, V_\ell(E))$ is cut out by local conditions at each prime, exactly paralleling the conditions defining a deformation ring.

2. **Waldspurger/Kolyvagin-style formulas**: The rank-part of BSD requires showing that the analytic rank equals the algebraic rank; deformation theory constrains the Selmer group rank through congruence ideals and $p$-adic L-functions.

3. **Automorphy and L-values**: If $\rho_{E,\ell}$ is modular, then $L(E,s)$ has analytic continuation and functional equation. The value $L^*(E,1)$ is then expressible via periods, Tamagawa numbers, and the regulator — exactly the BSD formula.

## Key Relationships

- **G-001 ↔ G-008**: Taylor-Wiles-Kisin patching controls Selmer group structure
- **G-002 ↔ G-007**: Residually reducible cases require Eisenstein prime analysis
- **G-003 ↔ G-009**: Local deformation rings encode Breuil-Mézard data
- **G-004 ↔ G-010**: Modularity lifting in higher dimensions feeds potential automorphy
- **G-005 ↔ G-006**: Langlands-Weissman framework is a specific instance of functoriality
- **G-011 ↔ G-001**: p-adic Langlands provides refined patching for $p$-adic families
