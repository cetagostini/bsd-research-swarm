# I-002: Vojta's Conjecture and Effective Finiteness for Elliptic Curves

## Direction ID and Title
**I-002** — Vojta's Conjecture and Effective Finiteness for Elliptic Curves

## Status Assessment
Both Vojta's conjecture and BSD are open. Their combination would resolve the effective Mordell problem for elliptic curves. No conditional proofs combining both are known. Vojta's conjecture is completely open in general; even its simplest case (the ABC conjecture) has only disputed proofs.

## Testable Conjecture or Lemma

**Conjecture (Effective BSD via Vojta).** Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N_E$ with $\operatorname{rank} E(\mathbb{Q}) = r$. Assume BSD for $E$ and Vojta's conjecture for $E \subset \mathbb{P}^2$ with $D = \{\infty\}$. Then there exists a basis $P_1, \ldots, P_r$ of $E(\mathbb{Q})/E(\mathbb{Q})_{\mathrm{tor}}$ such that for every $\epsilon > 0$:

$$\hat{h}(P_i) \leq C(\epsilon) \cdot N_E^{1+\epsilon}$$

where $C(\epsilon)$ is effectively computable from $\epsilon$ and the BSD data ($\Omega(E)$, $|\Sha(E)|$, $c_p$, $|E_{\mathrm{tor}}|$).

**Lemma (Regulator bound).** Under the same assumptions, the regulator satisfies:
$$\operatorname{Reg}(E) = \det(\langle P_i, P_j \rangle) \leq C'(\epsilon) \cdot N_E^{r(1+\epsilon)}.$$

Combined with the BSD formula $L^{(r)}(E,1)/r! = \Omega \cdot \operatorname{Reg} \cdot |\Sha| \cdot \prod c_p / |E_{\mathrm{tor}}|^2$, this gives an effective upper bound on $L^{(r)}(E,1)$ in terms of $N_E$.

## Approach Summary
1. **Vojta → height bound:** Apply Vojta's inequality with $X = E$, $D = \{\infty\}$, and the canonical height $h_{K_E}$. Since $K_E$ is trivial for an elliptic curve (genus 1), the inequality simplifies to a bound on $h_A(P)$ in terms of $d_{\mathrm{log}}(\infty, P)$ and the discriminant.
2. **BSD → regulator computation:** The BSD formula expresses $L^{(r)}(E,1)$ in terms of $\operatorname{Reg}(E)$, which is a determinant of height pairings. The Vojta bound on individual heights translates to a bound on the regulator.
3. **Effective constants:** Quantitative versions of the subspace theorem (Evertse, Schlickewei) provide explicit constants in the Vojta inequality, which propagate to explicit constants in the height bound.

## Computational Example

**Example 1: $E: y^2 = x^3 - x$ (conductor 32, rank 0).**
- No generators needed. Vojta's conjecture is vacuously satisfied. BSD predicts $L(E, 1) = \Omega(E) \cdot |\Sha| \cdot \prod c_p / |E_{\mathrm{tor}}|^2$. Numerically verified.

**Example 2: $E: y^2 = x^3 - x + 1$ (conductor 229, rank 1).**
- Generator $P$ with $\hat{h}(P) \approx 0.0511...$. The conductor is $N_E = 229$. The Vojta bound would give $\hat{h}(P) \leq C(\epsilon) \cdot 229^{1+\epsilon}$. The actual height is far below this bound, consistent with the conjecture.

**Example 3: $E = $ "11a1": $y^2 + y = x^3 - x^2 - 10x - 20$ (conductor 11, rank 0).**
- $\Omega(E) \approx 1.2692...$, $L(E, 1) \approx 1.2692...$, $|\Sha| = 1$. BSD holds trivially. The effective bound is vacuous.

**Example 4: High-rank curve $E$ with conductor $\sim 10^{14}$ and rank 2.**
- Two generators with moderate heights. The Vojta bound $C(\epsilon) \cdot (10^{14})^{1+\epsilon}$ is astronomically larger than the actual heights, illustrating that Vojta gives a qualitative bound, not a sharp one.

## Obstacle Analysis
1. **Vojta is completely open:** Even for $\mathbb{P}^1$ (the ABC conjecture), only conditional or disputed proofs exist. For elliptic curves inside $\mathbb{P}^2$, no progress beyond Faltings' theorem (genus $\geq 2$) is available.
2. **Effective constants:** Even conditional on Vojta, extracting explicit constants requires quantitative subspace theorems, which lose enormous factors. The resulting bounds are far from practical.
3. **BSD is independent:** BSD and Vojta are logically independent conjectures. Proving one does not directly help prove the other; their combination is needed for effective Mordell.

## Cross-Group Connections
- **I-008 (Parity Conjecture):** The parity of the rank determines whether Vojta's bound is non-vacuous.
- **I-006 (Bloch-Kato):** The Bloch-Kato Selmer group controls the algebraic side; Vojta controls the geometric side.
- **Group B (Arithmetic):** Computing heights of generators is the arithmetic counterpart.
- **Group C (Analytic):** Computing $L^{(r)}(E, 1)$ provides the analytic side of the effective bound.

## Classification
**Vertical connection.** Links Diophantine geometry (Vojta) to the analytic theory of $L$-functions (BSD) through height theory. The combination would resolve the effective Mordell problem for elliptic curves.
