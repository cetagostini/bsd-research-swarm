# G-002: Residually Reducible Galois Representations (Skinner-Wiles)

## Status Assessment
Active research. The ordinary case for GL₂/ℚ is essentially resolved (Skinner-Wiles 1999, Dasgupta-Kakde 2022). The crystalline case and extension to GL₂ over totally real fields remain partially open.

## Testable Conjecture

**Conjecture (Reducible Modularity).** Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at $\ell > 3$, and suppose $\bar\rho_{E,\ell}$ is reducible: $\bar\rho_{E,\ell} \sim \begin{pmatrix} \bar\varepsilon & * \\ 0 & 1 \end{pmatrix}$. If $\mathrm{Sel}_{\ell^\infty}(E/\mathbb{Q})$ is finite, then $E$ is modular.

**Lemma (Auxiliary Prime Irreducibility).** There exists a set of primes $S$ of positive density such that for $q \in S$ with $a_q(E) \not\equiv q+1 \pmod{\ell}$, the restriction $\bar\rho_{E,\ell}|_{G_{\mathbb{Q}(\mu_\ell)}}$ is absolutely irreducible.

## Approach Summary
1. Use the Skinner-Wiles auxiliary prime technique to force absolute irreducibility after restriction to $G_{\mathbb{Q}(\mu_\ell)}$.
2. Construct ordinary deformation rings $R_\ell^{\mathrm{ord}}$ parameterizing lifts with a specified filtration.
3. Apply Wiles's asymptotic formula $\#H^1_\Sigma / H^1_{\Sigma,\mathrm{str}} = \#\Phi$.
4. Use Ribet's lemma on raising the level to reduce to a known modularity result.
5. Alternatively, use Dasgupta-Kakde's Eisenstein cocycle approach.

## Computational Example
Consider $E = 11a1$ (Cremona label) at $\ell = 5$. The residual representation $\bar\rho_{E,5}$ is reducible: it sits in an exact sequence $0 \to \mathbb{F}_5(\bar\varepsilon) \to \bar\rho_{E,5} \to \mathbb{F}_5 \to 0$. The auxiliary prime $q = 7$ satisfies $a_7(E) = -2 \not\equiv 8 = 7+1 \pmod{5}$. The ordinary deformation ring $R_\ell^{\mathrm{ord}}$ at $\ell = 5$ has Krull dimension 2, and the congruence ideal $\eta_{\mathbb{T}}$ cuts out a codimension-1 subscheme. Selmer group $\mathrm{Sel}_{5^\infty}(E/\mathbb{Q}) = 0$ (verified via 2-descent).

## Obstacle Analysis
- **Primary**: The ordinary deformation ring $R_\ell^{\mathrm{ord}}$ in the reducible case is not a domain and has higher dimension than in the irreducible case.
- **Secondary**: The map $R_\ell^{\mathrm{ord}} \to \mathbb{T}$ need not be an isomorphism; one only shows $R_\ell^{\mathrm{ord}}/\eta \cong \mathbb{T}/\eta$.
- **Tertiary**: Controlling the cokernel requires vanishing of the dual Selmer group $H^1_{\Sigma^\perp}(F, \mathrm{ad}\,\bar\rho(1))$.

## Cross-Group Connections
- **G-007**: Eisenstein primes control the local structure of deformation rings in the reducible case.
- **G-008**: Deformation functor tangent space has dimension ≥ 2 in the reducible case.
- **G-001**: Taylor-Wiles patching is adapted to handle the reducible residual representation.
- **G-011**: p-adic Langlands provides alternative approach via Eisenstein families.

## Classification
Core techniques — essential for rank 0 and rank 1 cases of BSD.
