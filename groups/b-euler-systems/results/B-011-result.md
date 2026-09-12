# B-011: Syntomic Regulators and Euler System Classes

## Direction ID and Title
B-011 — Syntomic Regulators and Euler System Classes

## Status Assessment
The syntomic regulator $\operatorname{reg}_{\mathrm{syn}}: H^{2r-k}_{\mathcal{M}}(X, \mathbb{Q}(r)) \to H^r_{\mathrm{syn}}(X/\mathbb{Z}_p, k)$ provides the bridge between motivic cohomology (where Euler system classes live geometrically) and $p$-adic L-functions. For Beilinson-Flach elements on $X_0(N_f) \times X_0(N_g)$, Kings and Loeffler-Zerbes computed $\operatorname{reg}_{\mathrm{syn}}$ explicitly and showed it matches the Perrin-Riou regulator, yielding $\operatorname{reg}_{\mathrm{syn}}(\mathrm{BF}_{f,g}) = \mathcal{L}_p(f,g)$. For general Euler system classes (especially higher-rank ones), the syntomic regulator is not well-understood.

## Testable Conjecture or Lemma

**Conjecture B-011.** Let $E/\mathbb{Q}$ be an elliptic curve with good ordinary reduction at $p$, and let $z^{(p)} \in H^1(\mathbb{Q}, V_p(E))$ be Kato's zeta element. Then:

(a) **Lift to syntomic cohomology:** There exists a class $\tilde{z} \in H^1_{\mathrm{syn}}(\operatorname{Spec}(\mathbb{Z}_p), T_p(E))$ lifting $z^{(p)}$ such that the crystalline condition is satisfied:
$$\mathrm{loc}_p(\tilde{z}) \in H^1_f(\mathbb{Q}_p, V_p(E)) = \ker\left(H^1(\mathbb{Q}_p, V_p(E)) \to H^1(\mathbb{Q}_p, B_{\mathrm{dR}} \otimes V_p(E))\right)$$

(b) **Regulator identity:** The syntomic regulator of $\tilde{z}$ equals the Perrin-Riou regulator:
$$\operatorname{reg}_{\mathrm{syn}}(\tilde{z}) = \mathcal{L}_{\mathrm{PR}}(\operatorname{loc}_p(z^{(p)})) = \mathcal{L}_p^{\mathrm{Kato}} \in \Lambda$$

(c) **Injectivity on the relevant subspace:** The syntomic regulator is injective on the image of motivic cohomology in $H^1_{\mathrm{syn}}$:
$$\ker\left(\operatorname{reg}_{\mathrm{syn}}: H^1_{\mathcal{M}}(X_0(N), \mathbb{Q}(2)) \to H^1_{\mathrm{syn}}(X_0(N)/\mathbb{Z}_p, 2)\right) = 0$$

(d) **Higher-rank analogue:** For $r \geq 2$, the syntomic regulator on $H^r_{\mathcal{M}}(\operatorname{Spec}(\mathbb{Q}), \operatorname{Sym}^{r-1} V_E \otimes \mathbb{Q}(r))$ factors through Besser's extended syntomic cohomology and the target $H^r_{\mathrm{syn}}$ has dimension $r$, consistent with the expected rank of the Euler system.

## Approach Summary

Besser's syntomic cohomology $H^r_{\mathrm{syn}}(X/W, k)$ for smooth proper $X$ over the Witt vectors $W = W(\mathbb{F})$ is defined as the hypercohomology of the syntomic complex:
$$\mathrm{Fil}^r B_{\mathrm{dR}} \otimes \mathcal{O}_X \xrightarrow{d} \Omega^1_X \otimes B_{\mathrm{dR}} / \mathrm{Fil}^{r-1}$$
This sits in an exact sequence $0 \to H^{r-1}_{\mathrm{dR}}(X/F) / \mathrm{Fil}^r \to H^r_{\mathrm{syn}}(X/W, r) \to H^r_{\mathrm{crys}}(X_0/W)^{\varphi = p^r} \to 0$ where $\varphi$ is the Frobenius.

For modular curves $X = X_0(N)$, the de Rham cohomology $H^1_{\mathrm{dR}}(X_0(N)/\mathbb{Q}_p)$ decomposes under the Hecke action into eigenspaces corresponding to newforms $f$. On the $f$-eigenspace, the Hodge filtration has $\mathrm{Fil}^1 = \mathbb{Q}_p \cdot \omega_f$ (the space spanned by the newform differential) and $H^1_{\mathrm{dR}} / \mathrm{Fil}^1 \cong \mathbb{Q}_p \cdot \eta_f$ (the dual differential). The syntomic regulator maps Kato's class to the $p$-adic L-function via the Perrin-Riou interpolation.

For Beilinson-Flach elements on $X_0(N_f) \times X_0(N_g)$, the product structure allows the syntomic regulator to be computed as a tensor product of single-variable regulators, and the result matches the two-variable $p$-adic L-function.

## Computational Example

- **$X = X_0(11)$**: $H^1_{\mathrm{dR}}(X_0(11)/\mathbb{Q}_3)$ is 3-dimensional. The 11a1 eigenspace is 2-dimensional with $\mathrm{Fil}^1 = \mathbb{Q}_3 \cdot \omega_{11a1}$. The syntomic regulator on $H^1_{\mathcal{M}}(X_0(11), \mathbb{Q}(2))$ should map to $\mathcal{L}_3^{\mathrm{Kato}}(11a1)$ computed via modular symbols.
- **$X = X_0(37)$**: The syntomic regulator of the Beilinson element in $K_2(X_0(37))$ should recover $L'(E, 1) / \Omega_E$ for $E = $ 37a1. Compute via Besser's algorithm at $p = 3$.
- **$X_0(11) \times X_0(37)$**: The Beilinson-Flach element $\mathrm{BF}_{11a1, 37a1}^{(1)}$ has syntomic regulator equal to $\mathcal{L}_3(11a1, 37a1)$, computed via the Rankin-Selberg method.

## Obstacle Analysis

The injectivity of the syntomic regulator (conjecture (c)) is the fundamental open problem. The kernel of $\operatorname{reg}_{\mathrm{syn}}$ is related to extensions in the category of syntomic sheaves that are non-trivial motivically but trivial in $p$-adic cohomology. For $r = 1$, the regulator on $K_2$ of modular curves is expected to be injective on the "interesting" part (the newform eigenspace), but this has not been proven in general. For $r \geq 2$, the target $H^r_{\mathrm{syn}}$ may have smaller dimension than the source motivic cohomology, making injectivity impossible. The computation of $\operatorname{reg}_{\mathrm{syn}}$ for non-Eisenstein cycles on modular curves requires $p$-adic analytic continuation of the $p$-adic polylogarithm, which is algorithmically difficult.

## Cross-Group Connections
- **Group A (BSD Formula)**: The regulator identity (b) connects motivic classes to the $p$-adic L-function encoding BSD.
- **Group B-008 (p-adic L-functions)**: The Perrin-Riou regulator equals the syntomic regulator for Kato's class.
- **Group E (p-adic Heights)**: The $p$-adic height is related to the syntomic regulator via the $p$-adic cycle class map.

## Classification
Theorem (for BF elements); Conjecture (injectivity and higher-rank analogue)
