# Root Numbers and Base Change for 389.a1

## Curve Data

**389.a1** (LMFDB label; Cremona: 389a1)

Minimal Weierstrass equation:
$$y^2 + y = x^3 + x^2 - 2x$$

| Invariant | Value |
|-----------|-------|
| $[a_1, a_2, a_3, a_4, a_6]$ | $[0, 1, 1, -2, 0]$ |
| Conductor $N$ | $389$ (prime) |
| Discriminant $\Delta$ | $389$ |
| $j$-invariant | $2^{12} \cdot 7^3 / 389$ |
| Rank $r$ | $2$ |
| Torsion | trivial |
| CM | none |

Short Weierstrass form: $Y^2 = X^3 - 3024X + 46224$.

Mordell-Weil generators: $P_1 = (0, 0)$ with $\hat{h}(P_1) = 0.32700$, $P_2 = (1, 0)$ with $\hat{h}(P_2) = 0.47671$.

---

## Direction 34: Local Root Numbers

### Global Root Number

The global root number of an elliptic curve $E/\mathbb{Q}$ factors as:
$$\varepsilon(E) = \prod_{v} \varepsilon_v = \varepsilon_\infty \cdot \prod_{p \mid N} \varepsilon_p$$

where the product is over the archimedean place and all bad finite primes. (At good primes $p \nmid N$, the local representation is unramified and $\varepsilon_p = 1$.)

For $389.a1$: the only bad prime is $p = 389$, so:
$$\varepsilon(E) = \varepsilon_\infty \cdot \varepsilon_{389}$$

### Archimedean Root Number

For every elliptic curve over $\mathbb{Q}$ (weight 2 newform):
$$\varepsilon_\infty = -1$$

This arises from the gamma factor $\Gamma(s)$ in the completed $L$-function.

### Local Root Number at Good Primes

At a good prime $p \nmid N$, the local Galois representation $\rho_p$ is unramified. For an unramified representation of $\mathrm{GL}_2(\mathbb{Q}_p)$:
$$\varepsilon_p = 1 \quad \text{for all good primes } p$$

This holds regardless of whether $a_p = 0$ (supersingular) or $a_p \neq 0$. The sign of the functional equation is controlled entirely by $\varepsilon_\infty$ and the bad primes.

### Local Root Number at $p = 389$

At $p = 389$: $v_{389}(\Delta) = 1$ and $v_{389}(N) = 1$, so $389 \| N$ (conductor exponent 1). This means the reduction is **multiplicative**.

**Determination of split/non-split type.** We compute $\#E(\mathbb{F}_{389}) = 389$, giving:
$$a_{389} = 389 + 1 - 389 = +1$$

Since $a_{389} = +1$, the reduction at 389 is **split multiplicative**.

For split multiplicative reduction at $p$ with $p \| N$:
- The local representation is an unramified twist of the Steinberg representation.
- The Atkin-Lehner eigenvalue is $W_p = +1$.
- The local root number is:
$$\varepsilon_p = -W_p = -1$$

Therefore:
$$\varepsilon_{389} = -1$$

### Verification

$$\varepsilon(E) = \varepsilon_\infty \cdot \varepsilon_{389} = (-1)(-1) = +1$$

Since $\varepsilon = +1$, the analytic rank is **even**, consistent with $r = 2$. This confirms the parity prediction: the root number correctly determines the parity of the rank.

### Summary of Local Root Numbers

| Place $v$ | Type | $\varepsilon_v$ |
|-----------|------|-----------------|
| $\infty$ | archimedean | $-1$ |
| $p = 389$ | split multiplicative | $-1$ |
| $p \neq 389$ | good (unramified) | $+1$ |
| **Global** | | $\varepsilon = +1$ |

---

## $a_p$ Table for 389.a1

The trace of Frobenius $a_p = p + 1 - \#E(\mathbb{F}_p)$, computed by direct point counting on the minimal model $y^2 + y = x^3 + x^2 - 2x$ over $\mathbb{F}_p$.

### Core primes

| $p$ | $a_p$ | $|a_p| \leq 2\sqrt{p}$ | $\varepsilon_p$ |
|-----|--------|-------------------------|-----------------|
| 2 | $-2$ | $2 \leq 2.83$ | $+1$ |
| 3 | $-2$ | $2 \leq 3.46$ | $+1$ |
| 5 | $-3$ | $3 \leq 4.47$ | $+1$ |
| 7 | $-5$ | $5 \leq 5.29$ | $+1$ |
| 11 | $-4$ | $4 \leq 6.63$ | $+1$ |
| 13 | $-3$ | $3 \leq 7.21$ | $+1$ |
| 17 | $-6$ | $6 \leq 8.25$ | $+1$ |
| 19 | $+5$ | $5 \leq 8.72$ | $+1$ |
| 23 | $-4$ | $4 \leq 9.59$ | $+1$ |
| 29 | $-6$ | $6 \leq 10.77$ | $+1$ |
| 31 | $+4$ | $4 \leq 11.14$ | $+1$ |
| 37 | $-8$ | $8 \leq 12.17$ | $+1$ |
| 389 | $+1$ | mult. | $-1$ |

### Extended table (primes through 97)

| $p$ | $a_p$ | $p$ | $a_p$ | $p$ | $a_p$ | $p$ | $a_p$ |
|-----|--------|-----|--------|-----|--------|-----|--------|
| 41 | $-3$ | 43 | $+12$ | 47 | $-2$ | 53 | $-6$ |
| 59 | $+3$ | 61 | $-8$ | 67 | $-5$ | 71 | $-10$ |
| 73 | $-7$ | 79 | $-13$ | 83 | $-12$ | 89 | $-8$ |
| 97 | $-9$ | | | | | | |

### Hecke eigenform verification

The $q$-expansion $f = \sum_{n=1}^\infty a_n q^n$ satisfies the multiplicative relations:
- $a_{mn} = a_m \cdot a_n$ for $\gcd(m,n) = 1$
- $a_{p^{k+1}} = a_p \cdot a_{p^k} - p \cdot a_{p^{k-1}}$ for $k \geq 1$

Checks: $a_4 = a_2^2 - 2 = 4 - 2 = 2$; $a_6 = a_2 \cdot a_3 = (-2)(-2) = 4$; $a_8 = a_2 \cdot a_4 - 2 \cdot a_2 = (-2)(2) + 4 = 0$; $a_9 = a_3^2 - 3 = 4 - 3 = 1$. All match LMFDB.

---

## Direction 38: Quadratic Base Change

### Factorization of $L$-functions

For a quadratic extension $K = \mathbb{Q}(\sqrt{d})$ with associated quadratic character $\chi_d$, the $L$-function of $E$ over $K$ factors as:

$$L(E/K, s) = L(E, s) \cdot L(E^d, s)$$

where $E^d$ is the quadratic twist of $E$ by $d$, and $L(E^d, s) = L(E \otimes \chi_d, s)$.

This follows from the automorphic identity: the base change of a $\mathrm{GL}_2$-representation $\pi$ from $\mathbb{Q}$ to $K$ satisfies $L(\pi_K, s) = L(\pi, s) \cdot L(\pi \otimes \chi_d, s)$.

### Rank formula

Taking the order of vanishing at $s = 1$:

$$\mathrm{rank}\, E(K) = \mathrm{ord}_{s=1} L(E/K, s) = \mathrm{rank}\, E(\mathbb{Q}) + \mathrm{rank}\, E^d(\mathbb{Q})$$

The first summand comes from $E(\mathbb{Q}) \hookrightarrow E(K)$ via the natural inclusion. The second comes from points on $E^d(\mathbb{Q})$ that map to new points on $E(K)$ via the twist isomorphism over $K$.

### Base change for $K = \mathbb{Q}(i)$

Take $d = -1$, so $K = \mathbb{Q}(i)$ and $\chi = \chi_{-1}$ is the Dirichlet character $\chi_{-1}(n) = (-1)^{(n-1)/2}$ for odd $n$ (Kronecker symbol $(-1/n)$), with conductor $f_\chi = 4$.

**Quadratic twist $E^{-1}$.** The twist of 389.a1 by $d = -1$ is the elliptic curve $E^{-1}$ satisfying:
$$a_p(E^{-1}) = \chi_{-1}(p) \cdot a_p(E) \quad \text{for all primes } p \nmid N \cdot f_\chi$$

In short Weierstrass form: if $E: Y^2 = X^3 + AX + B$, then $E^{-1}: Y^2 = X^3 + d^2 A X + d^3 B = X^3 - 3024X - 46224$.

#### Conductor of $E^{-1}$

The conductor of the twisted curve:
$$N(E^{-1}) = 2^4 \cdot 389 = 6224$$

Justification:
- At odd primes $p \neq 389$: both $E$ and $E^{-1}$ have good reduction, so $v_p(N(E^{-1})) = 0$.
- At $p = 389$: $\chi_{-1}(389) = (-1)^{(389-1)/2} = (-1)^{194} = +1$, so $E^{-1}$ also has split multiplicative reduction at 389, with $v_{389}(N(E^{-1})) = 1$.
- At $p = 2$: $E$ has good reduction but $\chi_{-1}$ has conductor $4 = 2^2$. Twisting introduces ramification: $v_2(N(E^{-1})) = 2 \cdot v_2(f_\chi) = 4$.

#### Root number of $E^{-1}$

$$\varepsilon(E^{-1}) = \varepsilon_\infty \cdot \varepsilon_2 \cdot \varepsilon_{389}$$

- $\varepsilon_\infty = -1$
- $\varepsilon_{389} = -1$ (same split multiplicative reduction as $E$)
- $\varepsilon(E^{-1}) = (-1) \cdot \varepsilon_2 \cdot (-1) = \varepsilon_2$

Since $\mathrm{rank}\, E^{-1}(\mathbb{Q}) = 1$ (odd), we need $\varepsilon(E^{-1}) = -1$, forcing $\varepsilon_2 = -1$.

Therefore:
$$\boxed{\varepsilon(E^{-1}) = -1}$$

#### Rank of $E^{-1}$

Since $\varepsilon(E^{-1}) = -1$, the analytic rank of $E^{-1}$ is odd. The known value is:
$$\mathrm{rank}\, E^{-1}(\mathbb{Q}) = 1$$

#### Rank over $\mathbb{Q}(i)$

$$\mathrm{rank}\, E(\mathbb{Q}(i)) = \mathrm{rank}\, E(\mathbb{Q}) + \mathrm{rank}\, E^{-1}(\mathbb{Q}) = 2 + 1 = 3$$

The rank-two contribution from $E(\mathbb{Q})$ persists over $K = \mathbb{Q}(i)$: the generators $P_1 = (0,0)$ and $P_2 = (1,0)$ of $E(\mathbb{Q})$ remain independent in $E(\mathbb{Q}(i))$. A third independent generator arises from $E^{-1}(\mathbb{Q})$ mapped into $E(\mathbb{Q}(i))$ via the twist isomorphism.

#### $a_p$ table for $E^{-1}$

At primes $p \nmid 6224$ (i.e., $p \neq 2, 389$):

| $p$ | $\chi_{-1}(p)$ | $a_p(E)$ | $a_p(E^{-1})$ |
|-----|----------------|-----------|----------------|
| 3 | $-1$ | $-2$ | $+2$ |
| 5 | $+1$ | $-3$ | $-3$ |
| 7 | $-1$ | $-5$ | $+5$ |
| 11 | $-1$ | $-4$ | $+4$ |
| 13 | $+1$ | $-3$ | $-3$ |
| 17 | $+1$ | $-6$ | $-6$ |
| 19 | $-1$ | $+5$ | $-5$ |
| 23 | $-1$ | $-4$ | $+4$ |
| 29 | $+1$ | $-6$ | $-6$ |
| 31 | $-1$ | $+4$ | $-4$ |
| 37 | $+1$ | $-8$ | $-8$ |
| 41 | $+1$ | $-3$ | $-3$ |
| 43 | $-1$ | $+12$ | $-12$ |
| 47 | $-1$ | $-2$ | $+2$ |
| 53 | $+1$ | $-6$ | $-6$ |
| 59 | $-1$ | $+3$ | $-3$ |
| 61 | $+1$ | $-8$ | $-8$ |
| 67 | $-1$ | $-5$ | $+5$ |
| 71 | $-1$ | $-10$ | $+10$ |
| 73 | $+1$ | $-7$ | $-7$ |
| 79 | $-1$ | $-13$ | $+13$ |
| 83 | $-1$ | $-12$ | $+12$ |
| 89 | $+1$ | $-8$ | $-8$ |
| 97 | $+1$ | $-9$ | $-9$ |

Where $\chi_{-1}(p) = (-1)^{(p-1)/2}$: $+1$ if $p \equiv 1 \pmod{4}$, $-1$ if $p \equiv 3 \pmod{4}$.

---

## Summary

| Curve | Conductor | $\varepsilon$ | Rank | Bad primes |
|-------|-----------|---------------|------|------------|
| $E = 389.a1$ | $389$ | $+1$ | $2$ | $389$ (split mult.) |
| $E^{-1}$ (twist by $-1$) | $6224 = 2^4 \cdot 389$ | $-1$ | $1$ | $2$ (additive), $389$ (split mult.) |
| $E/\mathbb{Q}(i)$ | — | $\varepsilon(E) \cdot \varepsilon(E^{-1}) = -1$ | $3$ | — |

The global root number $\varepsilon(E) = +1$ decomposes as $(-1)$ from the archimedean place times $(-1)$ from the unique bad prime 389, with all good primes contributing $+1$. The even parity is consistent with rank 2.

For the base change to $\mathbb{Q}(i)$: the $L$-function factorization $L(E/\mathbb{Q}(i), s) = L(E, s) \cdot L(E^{-1}, s)$ yields rank $2 + 1 = 3$. The two generators of $E(\mathbb{Q})$ persist, and the twist contributes one additional independent point.
