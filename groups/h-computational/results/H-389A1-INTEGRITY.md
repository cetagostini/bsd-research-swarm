# H-389A1-INTEGRITY: Certified Local Invariants for 389.a1

## Curve Identity

**LMFDB label:** 389.a1
**Equation:** $y^2 + y = x^3 + x^2 - 2x$

**General Weierstrass coefficients:** $[a_1, a_2, a_3, a_4, a_6] = [0, 1, 1, -2, 0]$

---

## 1. Short Weierstrass Form

Starting from $y^2 + y = x^3 + x^2 - 2x$:

### Step 1: Complete the square

$$y^2 + y = \left(y + \tfrac{1}{2}\right)^2 - \tfrac{1}{4}$$

Substituting $Y = y + \tfrac{1}{2}$:

$$Y^2 = x^3 + x^2 - 2x + \tfrac{1}{4}$$

### Step 2: Eliminate $x^2$

Substitute $x = X - \tfrac{1}{3}$:

$$\left(X - \tfrac{1}{3}\right)^3 = X^3 - X^2 + \tfrac{1}{3}X - \tfrac{1}{27}$$
$$\left(X - \tfrac{1}{3}\right)^2 = X^2 - \tfrac{2}{3}X + \tfrac{1}{9}$$
$$-2\left(X - \tfrac{1}{3}\right) = -2X + \tfrac{2}{3}$$

Summing all terms:

$$X^3 + \underbrace{(-1 + 1)}_{=\,0}X^2 + \left(\tfrac{1}{3} - \tfrac{2}{3} - 2\right)X + \left(-\tfrac{1}{27} + \tfrac{1}{9} + \tfrac{2}{3} + \tfrac{1}{4}\right)$$

**Coefficient of $X$:**

$$\frac{1}{3} - \frac{2}{3} - 2 = -\frac{1}{3} - 2 = -\frac{7}{3}$$

**Constant term:**

$$-\frac{1}{27} + \frac{1}{9} + \frac{2}{3} + \frac{1}{4} = \frac{-4 + 12 + 72 + 27}{108} = \frac{107}{108}$$

So the short Weierstrass form over $\mathbb{Q}$ is:

$$\boxed{Y^2 = X^3 - \frac{7}{3}X + \frac{107}{108}}$$

### Step 3: Integer model

Clear denominators with $U = 36X$, $V = 216Y$ (i.e., $X = U/36$, $Y = V/216$):

$$\frac{V^2}{46656} = \frac{U^3}{46656} - \frac{7}{3}\cdot\frac{U}{36} + \frac{107}{108}$$

$$V^2 = U^3 - \frac{7 \times 46656}{108}\,U + \frac{107 \times 46656}{108} = U^3 - 3024\,U + 46224$$

$$\boxed{V^2 = U^3 - 3024\,U + 46224}$$

---

## 2. Discriminant Computation

### From the original model

Using the standard invariants for $[a_1, a_2, a_3, a_4, a_6] = [0, 1, 1, -2, 0]$:

**$b$-invariants:**

| Invariant | Formula | Value |
|-----------|---------|-------|
| $b_2$ | $a_1^2 + 4a_2$ | $0 + 4 = 4$ |
| $b_4$ | $a_1 a_3 + 2a_4$ | $0 - 4 = -4$ |
| $b_6$ | $a_3^2 + 4a_6$ | $1 + 0 = 1$ |
| $b_8$ | $a_1^2 a_6 + 4a_2 a_6 - a_1 a_3 a_5 + a_2 a_3^2 - a_4^2$ | $0 + 0 - 0 + 1 - 4 = -3$ |

**$c$-invariants:**

| Invariant | Formula | Value |
|-----------|---------|-------|
| $c_4$ | $b_2^2 - 24 b_4$ | $16 + 96 = 112$ |
| $c_6$ | $-b_2^3 + 36 b_2 b_4 - 216 b_6$ | $-64 - 576 - 216 = -856$ |

**Discriminant:**

$$\Delta = -b_2^2 b_8 - 8b_4^3 - 27b_6^2 + 9b_2 b_4 b_6$$

$$= -(16)(-3) - 8(-64) - 27(1) + 9(4)(-4)(1)$$

$$= 48 + 512 - 27 - 144 = \boxed{389}$$

**Cross-check via $c_4, c_6$:**

$$c_4^3 - c_6^2 = 112^3 - (-856)^2 = 1{,}404{,}928 - 732{,}736 = 672{,}192 = 1728 \times 389 \;\checkmark$$

### From the short Weierstrass form

For $V^2 = U^3 + aU + b$ with $a = -3024$, $b = 46224$:

$$\Delta_{\mathrm{short}} = -16\left(4a^3 + 27b^2\right)$$

**Factorizations:**

$$4a^3 = 4 \cdot (-3024)^3 = 4 \cdot \left(-(2^4 \cdot 3^3 \cdot 7)^3\right) = -2^{14} \cdot 3^9 \cdot 7^3$$

$$27b^2 = 27 \cdot (46224)^2 = 3^3 \cdot (2^4 \cdot 3^3 \cdot 107)^2 = 2^8 \cdot 3^9 \cdot 107^2$$

$$4a^3 + 27b^2 = 2^8 \cdot 3^9 \cdot \left(-2^6 \cdot 7^3 + 107^2\right) = 2^8 \cdot 3^9 \cdot \left(-21952 + 11449\right) = 2^8 \cdot 3^9 \cdot (-10503)$$

Since $10503 = 3^3 \times 389$:

$$4a^3 + 27b^2 = -2^8 \cdot 3^{12} \cdot 389$$

$$\Delta_{\mathrm{short}} = -16 \times \left(-2^8 \cdot 3^{12} \cdot 389\right) = 2^4 \cdot 2^8 \cdot 3^{12} \cdot 389 = 2^{12} \cdot 3^{12} \cdot 389 = 6^{12} \cdot 389$$

$$\boxed{\Delta_{\mathrm{short}} = 6^{12} \times 389 = 846{,}768{,}328{,}704}$$

The factor $6^{12} = d^{12}$ arises from the coordinate substitution clearing denominators ($d = 6$). The minimal discriminant is:

$$\boxed{\Delta_{\min} = 389}$$

**$j$-invariant:**

$$j = \frac{c_4^3}{\Delta} = \frac{112^3}{389} = \frac{1{,}404{,}928}{389} \approx 3611.64$$

---

## 3. Conductor

**Claim:** $N = 389$ (prime).

**Proof:** The conductor factors as $N = \prod_p p^{f_p}$ where $f_p = \operatorname{ord}_p(\Delta) + \delta_p - 1$ for bad primes, with $\delta_p \geq 0$ the wild conductor (Swan conductor).

Since $\Delta = 389$ is prime, the only prime of bad reduction is $p = 389$.

At $p = 389$:
- $v_{389}(\Delta) = 1$
- $c_4 = 112 \not\equiv 0 \pmod{389}$

When $p \mid \Delta$ but $p \nmid c_4$, the reduction is **multiplicative** (not additive). For multiplicative reduction, the conductor exponent is $f_p = 1$ and $\delta_p = 0$.

Therefore $N = 389^1 = 389$, consistent with the discriminant factorization. $\square$

---

## 4. Torsion Structure

**Claim:** $E(\mathbb{Q})_{\mathrm{tors}} = \{O\}$ (trivial).

**Proof:**

**(a) No 2-torsion.** A point $P = (x, y)$ satisfies $2P = O$ if and only if $y = -y - a_1 x - a_3$, i.e., $2y + a_1 x + a_3 = 0$. With $a_1 = 0$, $a_3 = 1$: $2y + 1 = 0 \Rightarrow y = -1/2 \notin \mathbb{Z}$. By the Nagell-Lutz theorem (generalized for minimal integral models), torsion points have integer coordinates. Since $y = -1/2$ is not integral, there is no rational 2-torsion.

**(b) Torsion points have integer coordinates.** For a minimal Weierstrass model over $\mathbb{Z}$, any torsion point $P = (x, y) \in E(\mathbb{Q})$ has $x, y \in \mathbb{Z}$ (Silverman, *The Arithmetic of Elliptic Curves*, Theorem VIII.7.1).

**(c) Nagell-Lutz divisibility.** For a torsion point $P = (x, y)$ with $P \neq -P$ (i.e., $2y + 1 \neq 0$), the quantity $(2y + a_1 x + a_3)^2 = (2y + 1)^2$ must divide $4\Delta = 4 \times 389 = 1556$. Since $389$ is prime:

$$1556 = 2^2 \times 389$$

The divisors of $1556$ that are perfect squares are: $1$ and $4$.

- $(2y+1)^2 = 1 \Rightarrow 2y + 1 = \pm 1 \Rightarrow y \in \{0, -1\}$
- $(2y+1)^2 = 4 \Rightarrow 2y + 1 = \pm 2 \Rightarrow y \in \{1/2, -3/2\}$ (not integers)

So torsion points can only have $y = 0$ or $y = -1$.

**(d) Exhaustive search.** We enumerate all integer points with $y \in \{0, -1\}$:
- $y = 0$: $0 = x^3 + x^2 - 2x = x(x-1)(x+2) \Rightarrow x \in \{0, 1, -2\}$, giving $(0,0)$, $(1,0)$, $(-2,0)$.
- $y = -1$: $1 - 1 = 0 = x^3 + x^2 - 2x \Rightarrow x \in \{0, 1, -2\}$, giving $(0,-1)$, $(1,-1)$, $(-2,-1)$.

Each of these 6 points and the broader set of all integer points (14 total, found by checking $|x| \leq 20$) were tested for torsion by computing multiples up to $14P$. **None returned to $O$** within 14 multiples.

**(e) Mazur's theorem.** The only possible torsion orders for $E(\mathbb{Q})$ are $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12\}$. Since we checked up to order 14 with no torsion found, and there is no 2-torsion, the torsion subgroup is trivial:

$$\boxed{E(\mathbb{Q})_{\mathrm{tors}} = \{O\}}$$

---

## 5. Reduction Types

### At $p = 389$ (bad prime)

| Criterion | Value | Implication |
|-----------|-------|-------------|
| $389 \mid \Delta$ | Yes ($\Delta = 389$) | Bad reduction |
| $389 \mid c_4$ | No ($c_4 = 112$) | **Multiplicative** (not additive) |
| $v_{389}(\Delta)$ | 1 | Kodaira type $\mathrm{I}_1$ |
| $a_{389}$ | $+1$ | Split multiplicative |
| Tamagawa $c_{389}$ | 1 | Néron model fiber has 1 component |
| Conductor exponent $f_{389}$ | 1 | $N = 389$ |

**Note:** The problem statement suggested additive reduction at 389. This is **incorrect**. Additive reduction requires $p \mid c_4$ in addition to $p \mid \Delta$. Since $112 \not\equiv 0 \pmod{389}$, the reduction is multiplicative of type $\mathrm{I}_1$.

### At primes $p \neq 389$

Since $\Delta = 389$ is prime, $p \nmid \Delta$ for all $p \neq 389$, so $E$ has **good reduction** at all other primes. $\square$

### Trace of Frobenius $a_p$

For each prime $p$, $a_p = p + 1 - \#E(\mathbb{F}_p)$, computed by exhaustive enumeration of $\mathbb{F}_p$-points on $y^2 + y \equiv x^3 + x^2 - 2x \pmod{p}$:

| $p$ | $\#E(\mathbb{F}_p)$ | $a_p$ | $|a_p| \leq 2\sqrt{p}$ |
|-----|----------------------|-------|-------------------------|
| 2 | 5 | $-2$ | $2 \leq 2.83$ ✓ |
| 3 | 6 | $-2$ | $2 \leq 3.46$ ✓ |
| **5** | **9** | $\mathbf{-3}$ | $3 \leq 4.47$ **✓** |
| 7 | 13 | $-5$ | $5 \leq 5.29$ ✓ |
| 11 | 16 | $-4$ | $4 \leq 6.63$ ✓ |
| 13 | 17 | $-3$ | $3 \leq 7.21$ ✓ |
| 17 | 24 | $-6$ | $6 \leq 8.25$ ✓ |
| 19 | 15 | $5$ | $5 \leq 8.72$ ✓ |
| 23 | 28 | $-4$ | $4 \leq 9.59$ ✓ |
| 29 | 36 | $-6$ | $6 \leq 10.77$ ✓ |
| 31 | 28 | $4$ | $4 \leq 11.14$ ✓ |
| 37 | 46 | $-8$ | $8 \leq 12.17$ ✓ |
| 41 | 45 | $-3$ | $3 \leq 12.81$ ✓ |
| 43 | 32 | $12$ | $12 \leq 13.11$ ✓ |
| 389 | 389 | $1$ | $1 \leq 39.45$ ✓ |

**Verification of $a_5 = -3$:** Over $\mathbb{F}_5$, the points are:

| $x$ | $x^3 + x^2 - 2x \pmod{5}$ | Solutions $y$ to $y^2 + y \equiv$ RHS |
|-----|---------------------------|---------------------------------------|
| 0 | 0 | $y \in \{0, 4\}$ (2 pts) |
| 1 | 0 | $y \in \{0, 4\}$ (2 pts) |
| 2 | 3 | none (disc $= 13 \equiv 3$, not a QR mod 5) |
| 3 | 0 | $y \in \{0, 4\}$ (2 pts) |
| 4 | 2 | $y \in \{1, 3\}$ (2 pts) |

Total: $8 + 1(O) = 9$ points, giving $a_5 = 5 + 1 - 9 = -3$. $\checkmark$

---

## 6. Point Verification

### $P = (0, 0)$

$$0^2 + 0 = 0 = 0^3 + 0^2 - 2(0) = 0 \quad\checkmark$$

### $Q = (1, 0)$

$$0^2 + 0 = 0 = 1^3 + 1^2 - 2(1) = 1 + 1 - 2 = 0 \quad\checkmark$$

### $2P = (3, 5)$

Using the doubling formula for $y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6$:

$$\lambda = \frac{3x_P^2 + 2a_2 x_P + a_4}{2y_P + a_1 x_P + a_3} = \frac{0 + 0 - 2}{0 + 0 + 1} = -2$$

$$x_{2P} = \lambda^2 + a_1\lambda - a_2 - 2x_P = 4 + 0 - 1 - 0 = 3$$

$$y_{2P} = -\lambda(x_{2P} - x_P) - y_P - a_1 x_{2P} - a_3 = 2(3) - 0 - 0 - 1 = 5$$

**On curve:** $5^2 + 5 = 30 = 27 + 9 - 6 = 3^3 + 3^2 - 2(3)$ $\checkmark$

### $2Q = (6, -16)$

$$\lambda = \frac{3(1) + 2(1) - 2}{0 + 0 + 1} = 3$$

$$x_{2Q} = 9 - 1 - 2 = 6$$

$$y_{2Q} = -3(6 - 1) - 0 - 1 = -15 - 1 = -16$$

**On curve:** $(-16)^2 + (-16) = 240 = 216 + 36 - 12 = 6^3 + 6^2 - 2(6)$ $\checkmark$

### $P + Q = (-2, -1)$

$$\lambda = \frac{y_Q - y_P}{x_Q - x_P} = \frac{0 - 0}{1 - 0} = 0$$

$$x_{P+Q} = 0 - 1 - 0 - 1 = -2$$

$$y_{P+Q} = 0 \cdot (-2 - 0) - 0 - 1 = -1$$

**On curve:** $(-1)^2 + (-1) = 0 = -8 + 4 + 4 = (-2)^3 + (-2)^2 - 2(-2)$ $\checkmark$

### $3P = \left(-\frac{11}{9}, \frac{28}{27}\right)$

$$2P + P = (3, 5) + (0, 0): \quad \lambda = \frac{0 - 5}{0 - 3} = \frac{5}{3}$$

$$x_{3P} = \frac{25}{9} - 1 - 3 = \frac{25 - 9 - 27}{9} = -\frac{11}{9}$$

$$y_{3P} = -\frac{5}{3}\left(-\frac{11}{9} - 3\right) - 5 - 1 = -\frac{5}{3}\left(-\frac{38}{9}\right) - 6 = \frac{190}{27} - \frac{162}{27} = \frac{28}{27}$$

**On curve:** $\left(\frac{28}{27}\right)^2 + \frac{28}{27} = \frac{784 + 756}{729} = \frac{1540}{729}$

$$\left(-\frac{11}{9}\right)^3 + \left(-\frac{11}{9}\right)^2 - 2\left(-\frac{11}{9}\right) = \frac{-1331 + 1089 + 1782}{729} = \frac{1540}{729} \quad\checkmark$$

### $3Q = \left(\frac{56}{25}, \frac{371}{125}\right)$

$$2Q + Q = (6, -16) + (1, 0): \quad \lambda = \frac{0 + 16}{1 - 6} = -\frac{16}{5}$$

$$x_{3Q} = \frac{256}{25} - 1 - 6 = \frac{256 - 175}{25} = \frac{81}{25}$$

Wait — let me recompute. $x_{3Q} = \lambda^2 - a_2 - x_{2Q} - x_Q = \frac{256}{25} - 1 - 6 - 1 = \frac{256 - 200}{25} = \frac{56}{25}$.

$$y_{3Q} = -\lambda(x_{3Q} - x_Q) - y_Q - 1 = \frac{16}{5}\left(\frac{56}{25} - 1\right) - 0 - 1 = \frac{16}{5} \cdot \frac{31}{25} - 1 = \frac{496}{125} - \frac{125}{125} = \frac{371}{125}$$

**On curve:** $\left(\frac{371}{125}\right)^2 + \frac{371}{125} = \frac{137641 + 46375}{15625} = \frac{184016}{15625}$

$$\left(\frac{56}{25}\right)^3 + \left(\frac{56}{25}\right)^2 - 2\left(\frac{56}{25}\right) = \frac{175616 + 78400 - 35000}{15625} = \frac{184016}{15625} \quad\checkmark$$

---

## 7. Independence Check

### Naive heights

The **naive (logarithmic) height** of $P = (x_P, y_P)$ is $h(P) = \log\max(|a|, |b|)$ where $x_P = a/b$ in lowest terms.

| Point | $x$-coordinate | $h$ |
|-------|---------------|-----|
| $P$ | $0$ | $\log 1 = 0$ |
| $Q$ | $1$ | $\log 1 = 0$ |
| $P + Q$ | $-2$ | $\log 2 \approx 0.6931$ |
| $P - Q$ | $-1$ | $\log 1 = 0$ |

The naive heights of $P$ and $Q$ are both $0$, so $h$ alone cannot distinguish them. We need the **canonical height** $\hat{h}$.

### Canonical heights via Silverman's algorithm

The canonical height is computed as $\hat{h}(P) = \lim_{n \to \infty} h(2^n P) / 4^n$ using exact rational arithmetic on the $x$-coordinate doubling:

$$x(2P) = \frac{x^4 - b_4 x^2 - 2b_6 x - b_8}{4x^3 + b_2 x^2 + 2b_4 x + b_6}$$

with $b_2 = 4$, $b_4 = -4$, $b_6 = 1$, $b_8 = -3$.

Computed to $\sim 10^{-6}$ precision (convergence at iteration $n = 9$):

| Quantity | Value |
|----------|-------|
| $\hat{h}(P)$ | $0.326999$ |
| $\hat{h}(Q)$ | $0.476712$ |
| $\hat{h}(P + Q)$ | $0.920755$ |
| $\hat{h}(P - Q)$ | $0.686665$ |

### Height pairing matrix

The bilinear height pairing is:

$$\langle P, Q \rangle = \frac{\hat{h}(P+Q) - \hat{h}(P) - \hat{h}(Q)}{2} = \frac{0.920755 - 0.326999 - 0.476712}{2} \approx 0.058522$$

The **height pairing matrix** is:

$$\mathcal{H} = \begin{pmatrix} \hat{h}(P) & \langle P, Q \rangle \\ \langle P, Q \rangle & \hat{h}(Q) \end{pmatrix} = \begin{pmatrix} 0.326999 & 0.058522 \\ 0.058522 & 0.476712 \end{pmatrix}$$

**Determinant:**

$$\det(\mathcal{H}) = 0.326999 \times 0.476712 - 0.058522^2 = 0.155926 - 0.003425 = 0.152501$$

$$\boxed{\det(\mathcal{H}) \approx 0.1525 > 0}$$

Since the height pairing matrix has **positive determinant**, the points $P$ and $Q$ are **linearly independent** over $\mathbb{Z}$.

This confirms: $\operatorname{rank} E(\mathbb{Q}) \geq 2$ with $\{P, Q\}$ as independent generators.

The regulator is $\operatorname{Reg}(E) = \det(\mathcal{H}) \approx 0.1525$.

---

## Summary of Certified Invariants

| Invariant | Value | Method |
|-----------|-------|--------|
| $\Delta$ | $389$ | Direct computation from $b$-invariants |
| $c_4$ | $112$ | $b_2^2 - 24b_4$ |
| $c_6$ | $-856$ | $-b_2^3 + 36b_2 b_4 - 216b_6$ |
| $j$ | $1404928/389$ | $c_4^3/\Delta$ |
| $N$ (conductor) | $389$ | Prime, from Tate's algorithm |
| Kodaira at 389 | $\mathrm{I}_1$ | Multiplicative, split |
| $c_{389}$ (Tamagawa) | $1$ | $1$ component |
| $E(\mathbb{Q})_{\mathrm{tors}}$ | $\{O\}$ | Nagell-Lutz + Mazur |
| $a_5$ | $-3$ | $\#E(\mathbb{F}_5) = 9$ |
| $\operatorname{rank}$ | $\geq 2$ | $\det(\mathcal{H}) > 0$ |
| $\operatorname{Reg}$ | $\approx 0.1525$ | Height pairing matrix |
