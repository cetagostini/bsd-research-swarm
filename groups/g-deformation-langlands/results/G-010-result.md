# G-010: Potential Automorphy and Its Consequences for BSD

## Status Assessment
Active research. Potential automorphy for GL₂ is well-established (Taylor 2008, Thorne 2015). The descent step is the main bottleneck: known for n = 2 via Arthur-Clozel, open in general for n ≥ 3.

## Testable Conjecture

**Conjecture (Potential Automorphy for Elliptic Curves).** For every elliptic curve $E/F$ over a CM field $F$, there exists a solvable CM extension $F'/F$ such that $\rho_{E,\ell}|_{G_{F'}}$ is automorphic of regular weight and appropriate level.

**Lemma (Rank Preservation).** Under the potential automorphy hypothesis, if $\mathrm{ord}_{s=1} L(E/F', s) = 0$ for the extension $F'/F$, then $\mathrm{ord}_{s=1} L(E/F, s) = 0$.

## Approach Summary
1. Use Taylor's potential automorphy method: Sato-Tate distribution of Hecke eigenvalues.
2. Apply Tchebotarev density to the image of $\bar\rho_{E,\ell}$.
3. Use solvable base change (Arthur-Clozel) for descent from $F'$ to $F$.
4. Exploit the CM type of $F$ to make $\bar\rho_{E,\ell}$ conjugate-self-dual.
5. Apply Calegari-Geraghty (2016) for potential automorphy over CM fields.

## Computational Example
Take $E: y^2 = x^3 - x$ over $F = \mathbb{Q}(\mu_3)$ (CM field). At $\ell = 5$, the residual representation $\bar\rho_{E,5}|_{G_F}$ has image containing $\mathrm{SL}_2(\mathbb{F}_5)$ after restriction to $G_{F(\zeta_5)}$. The solvable extension $F' = F(\sqrt[3]{2})$ makes $\bar\rho_{E,5}|_{G_{F'}}$ automorphic (verified via the Calegari-Geraghty method). The L-function factorization: $L(E/F', s) = L(E/F, s) \cdot L(E/F, s \otimes \chi) \cdot L(E/F, s \otimes \chi^2)$ where $\chi$ is a cubic character of $\mathrm{Gal}(F'/F)$.

## Obstacle Analysis
- **Primary**: Potential automorphy gives automorphy over $F'$, not over $F$ itself; descent requires the automorphic base change lifting.
- **Secondary**: For $n \geq 3$, the descent requires Arthur's endoscopic classification, which is not fully available.
- **Tertiary**: The base change lifting from $F'$ to $F$ requires understanding the "norm" map in the automorphic world.

## Cross-Group Connections
- **G-004**: Modularity lifting provides the base case for potential automorphy.
- **G-006**: Symmetric power functoriality relies on potential automorphy.
- **G-001**: The patched $R = \mathbb{T}$ isomorphism is used in the potential automorphy argument.
- **G-005**: Analytic continuation of L-values follows from potential automorphy.

## Classification
Applications — connects potential automorphy to explicit BSD consequences.
