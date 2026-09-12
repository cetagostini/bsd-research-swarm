# I-010: BSD and the Fontaine-Mazur Conjecture

## Direction ID and Title
**I-010** — BSD and the Fontaine-Mazur Conjecture

## Status Assessment
The Fontaine-Mazur conjecture is proven for $\operatorname{GL}_2$ over $\mathbb{Q}$ (Kisin 2003, 2006). The relevant case for BSD involves $\operatorname{GL}_3$ extensions (the Selmer group classifies extensions $0 \to V_p(E) \to W \to \mathbb{Q}_p(1) \to 0$), which is open. The connection to BSD is well-understood conceptually: Fontaine-Mazur for the relevant representations would complete the motivic foundation for the $p$-adic BSD conjecture.

## Testable Conjecture or Lemma

**Conjecture (Fontaine-Mazur for Selmer Extensions).** Let $E/\mathbb{Q}$ be an elliptic curve. The Fontaine-Mazur conjecture for the extension:
$$0 \to V_p(E) \to W \to \mathbb{Q}_p(1) \to 0$$
asserts that every such extension that is de Rham at $p$ and unramified at almost all primes is geometric (arises from a motive).

**Lemma (Fontaine-Mazur Implies Motivic Sha).** Assume the Fontaine-Mazur conjecture for $\operatorname{GL}_3$ representations over $\mathbb{Q}$. Then every element of $\Sha(E)[p^\infty]$ is motivic: it arises from an actual global point on a related variety (not a "phantom" element).

*Proof sketch:* An element of $\Sha(E)[p^\infty]$ corresponds to an extension $0 \to V_p(E) \to W \to \mathbb{Q}_p(1) \to 0$ that is flat at all primes (i.e., in the Bloch-Kato Selmer group $H^1_f$) and locally trivial (i.e., maps to 0 in $H^1(\mathbb{Q}_v, V_p(E))$ for all $v$). The Fontaine-Mazur conjecture predicts $W$ is geometric, hence arises from the étale cohomology of a variety. This gives the extension a motivic interpretation. $\square$

**Lemma (BSD Implies Fontaine-Mazur for the Extension).** If BSD holds for $E$ and $\Sha(E)$ is finite, then every element of $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ is geometric.

*Proof sketch:* If $\Sha(E)$ is finite, then $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ is finitely generated over $\mathbb{Z}_p$. Every element comes from an actual point $P \in E(\mathbb{Q}) \otimes \mathbb{Z}_p$. The extension corresponding to $P$ is automatically geometric (it arises from the Tate module of $E$ twisted by the point $P$). $\square$

## Approach Summary
1. **Selmer group as extensions:** $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ classifies extensions $0 \to V_p(E) \to W \to \mathbb{Q}_p(1) \to 0$ that are flat at all primes. These are 3-dimensional $p$-adic representations.
2. **Fontaine-Mazur prediction:** The conjecture predicts that every such $W$ is geometric: de Rham at $p$, unramified almost everywhere, and arising from a motive. This is the $\operatorname{GL}_3$ case of Fontaine-Mazur.
3. **Kisin's theorem (GL_2):** Kisin proved Fontaine-Mazur for 2-dimensional representations. The 3-dimensional case (extensions of 2-dimensional by 1-dimensional) is open but expected to follow from similar techniques.
4. **BSD consequence:** If Fontaine-Mazur holds for these extensions, then $\Sha(E)[p^\infty]$ has a clean motivic interpretation, the $p$-adic BSD formula (Perrin-Riou) is well-posed, and the deformation-theoretic approach to BSD (via universal deformation rings) has a solid foundation.

## Computational Example

**Example 1: $E: y^2 + y = x^3 - x^2 - 10x - 20$ (conductor 11, rank 0, $|\Sha| = 1$).**
- $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) = 0$ for all $p$ (since rank 0 and $\Sha = 1$). The Fontaine-Mazur conjecture is vacuously satisfied: there are no non-trivial extensions. ✓

**Example 2: $E$ with rank 0 and $|\Sha| = p^2$.**
- $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \cong (\mathbb{Z}/p)^2$ (from $\Sha[p]$). Each element corresponds to an extension $W$. Fontaine-Mazur predicts each $W$ is geometric. If true, these extensions arise from actual algebraic cycles on a related variety.

**Example 3: $E$ with rank 1.**
- $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \cong \mathbb{Z}_p \oplus \Sha[p^\infty]$. The $\mathbb{Z}_p$ part comes from the point of infinite order and is automatically geometric. The $\Sha[p^\infty]$ part is the Fontaine-Mazur content.

**Example 4: Deformation ring perspective.**
- The universal deformation ring $R$ of $\bar\rho_E: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{F}_p)$ parametrizes all lifts. The "BSD locus" (representations from the Selmer group) is a subspace of the "geometric locus" (Fontaine-Mazur). If the geometric locus contains the BSD locus, this gives a structural proof of the arithmetic constraints.

## Obstacle Analysis
1. **$\operatorname{GL}_3$ is open:** Kisin's proof for $\operatorname{GL}_2$ uses the theory of $(\varphi, \Gamma)$-modules and Kisin modules, which do not directly generalize to $\operatorname{GL}_3$. New ideas are needed.
2. **Extensions are harder than representations:** The representation $V_p(E)$ is known to be geometric (by modularity). But extensions of geometric representations need not be geometric in general. The Fontaine-Mazur conjecture predicts they are, but this is unproven.
3. **Motivic interpretation:** Even if Fontaine-Mazur holds, identifying the specific motive that gives rise to the extension requires additional work (e.g., finding the algebraic cycle or variety).

## Cross-Group Connections
- **I-006 (Bloch-Kato):** The Bloch-Kato Selmer group is defined in terms of Galois representations; Fontaine-Mazur ensures these are geometric.
- **I-009 (Greenberg's Conjecture):** Fontaine-Mazur for extensions would imply constraints on the $\mu$-invariant.
- **I-008 (Parity Conjecture):** The Cassels-Tate pairing on $\Sha[p^\infty]$ is related to the Galois structure of the extensions; Fontaine-Mazur would give a motivic interpretation.
- **Group A (Galois Representations):** Computing the deformation ring and its geometric locus provides numerical evidence.
- **Group D ($p$-adic BSD):** The $p$-adic BSD conjecture (Perrin-Riou) is the endpoint; Fontaine-Mazur provides the framework.

## Classification
**Structural prerequisite.** The Fontaine-Mazur conjecture provides the $p$-adic Hodge-theoretic framework within which the $p$-adic BSD conjecture is naturally formulated. Proving it for the relevant $\operatorname{GL}_3$ representations would complete the motivic foundation for BSD and ensure that all Selmer group elements have a geometric origin.
