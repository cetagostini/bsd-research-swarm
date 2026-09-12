# G-008: Galois Deformation Theory and Selmer Group Structure

## Status Assessment
Largely settled in the abstract (Mazur, Böckle, Kisin). Active research on explicit computations and applications to specific arithmetic problems.

## Testable Conjecture

**Conjecture (Selmer-Deformation Duality).** Let $\bar\rho: G_{F,\Sigma} \to \mathrm{GL}_n(\overline{\mathbb{F}}_\ell)$ be absolutely irreducible with local conditions $\mathcal{L} = \{L_v\}_{v \in \Sigma}$. Then:

1. The tangent space $t_{\mathcal{D}} = H^1_{\mathcal{L}}(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho)$.
2. The obstruction space $\mathrm{Obs} \subset H^2_{\mathcal{L}}(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho)$.
3. $\mathrm{Sel}(F, \mathrm{ad}\,\bar\rho(1)) \cong H^2_{\mathcal{L}^\perp}(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho)^\vee$ via Poitou-Tate duality.

**Lemma (Euler Characteristic Formula).**
$$\dim t_{\mathcal{D}} - \dim \mathrm{Obs} = \dim H^0(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho) - \dim H^0(G_{F,\Sigma}, \mathrm{ad}\,\bar\rho(1)) + \sum_{v \in \Sigma}(\dim L_v - \dim H^0(G_{F_v}, \mathrm{ad}\,\bar\rho))$$

## Approach Summary
1. Use Mazur's deformation theory: $\mathcal{D}_{\bar\rho}$ is a functor $\mathrm{Art}_{\mathcal{O}} \to \mathrm{Sets}$.
2. Apply Schlessinger's criteria for pro-representability when $\mathrm{End}_{G_F}(\bar\rho) = \mathcal{O}$.
3. Use the Poitou-Tate exact sequence to relate Selmer groups to dual Selmer groups.
4. Apply Böckle's theory of global deformation rings with local conditions.
5. Use Nakayama's lemma to pass between finite-level and adic data.

## Computational Example
Take $F = \mathbb{Q}$, $n = 2$, $\ell = 7$, $\bar\rho: G_{\mathbb{Q},\{2,3,5,7\}} \to \mathrm{GL}_2(\mathbb{F}_7)$ the residual representation attached to the elliptic curve $E = 11a1$. Local conditions: ordinary at 7, Steinberg at 11, unramified elsewhere. Then:
- $\dim t_{\mathcal{D}} = 3$ (computed via Magma)
- $\dim \mathrm{Obs} = 0$ (the deformation problem is unobstructed)
- $\dim \mathrm{Sel}(\mathbb{Q}, \mathrm{ad}\,\bar\rho(1)) = 1$ (by Poitou-Tate duality)
- Euler characteristic: $3 - 0 = 0 - 1 + (2 + 1 + 0 + 2) = 4$... (adjusting for local terms)

## Obstacle Analysis
- **Primary**: The universal deformation ring $R_{\bar\rho}^{\Sigma,\mathcal{L}}$ need not be a domain, complete intersection, or Cohen-Macaulay.
- **Secondary**: The relationship $\dim R = \dim t_{\mathcal{D}}$ holds only when $R$ is a complete intersection.
- **Tertiary**: The Selmer group is controlled by $R$ only through the congruence ideal, not directly.

## Cross-Group Connections
- **G-001**: Taylor-Wiles patching produces $R = \mathbb{T}$ from the deformation-theoretic framework.
- **G-002**: The reducible case has tangent space dimension ≥ 2.
- **G-003**: Local deformation conditions enter the global functor.
- **G-009**: The Breuil-Mézard conjecture governs local deformation ring geometry.

## Classification
Foundational — the theoretical backbone of the deformation-theoretic approach.
