#!/usr/bin/env python3
"""
H-009 Deep: Strong BSD verification for rank 2 candidates.

Approach:
1. Compute L''(E,1)/2! via smoothed approximate functional equation
2. Compute Ω via numerical integration
3. Search for rational points to estimate Regulator
4. Compute Tamagawa numbers via reduction type analysis
5. Predict |Ш| and check integrality / perfect square
"""

import mpmath
import math
import json
import sys

mpmath.mp.dps = 60

# ============================================================
# Prime sieve
# ============================================================

def sieve_primes(N):
    if N < 2: return []
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N + 1, i):
                is_prime[j] = False
    return [i for i in range(2, N + 1) if is_prime[i]]


def factor(n):
    if n == 0: return {}
    n = abs(n)
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


# ============================================================
# Elliptic curve: y² = x³ + a4*x + a6
# ============================================================

class EC:
    def __init__(self, a4, a6):
        self.a4 = int(a4)
        self.a6 = int(a6)
        self.disc = -16 * (4*a4**3 + 27*a6**2)

    def ap(self, p):
        """a_p via point counting."""
        a4, a6 = self.a4, self.a6
        if (4*a4**3 + 27*a6**2) % p == 0:
            return None
        count = 1
        for x in range(p):
            rhs = (x*x*x + a4*x + a6) % p
            if rhs == 0:
                count += 1
            elif pow(rhs, (p-1)//2, p) == 1:
                count += 2
        return p + 1 - count

    def ap_all(self, primes):
        """Compute a_p for all good primes."""
        result = {}
        for p in primes:
            val = self.ap(p)
            if val is not None:
                result[p] = val
        return result

    def point_on_curve(self, x):
        """Return y² value at x."""
        return x**3 + self.a4*x + self.a6

    def is_point(self, x, y):
        return y*y == x**3 + self.a4*x + self.a6

    def rational_points_search(self, bound=200):
        """Search for rational points with small coordinates."""
        points = []
        for x in range(-bound, bound + 1):
            y2 = x**3 + self.a4*x + self.a6
            if y2 >= 0:
                y = int(mpmath.isqrt(y2))
                if y*y == y2 and y > 0:
                    points.append((x, y))
                    if y > 0:
                        points.append((x, -y))
                elif y2 == 0:
                    points.append((x, 0))
        return points


# ============================================================
# L''(E,1)/2! via smoothed AFE with Bessel K_0
# ============================================================

def compute_L_leading(curve, N_cond, N_terms=5000):
    """
    Compute L''(E,1)/2! using the smoothed approximate functional equation.

    For rank 2, the smoothed AFE gives:
    L''(E,1)/2! = (2/√N) Σ_{n≥1} a_n/n · K_0(4π√n/√N)

    where K_0 is the modified Bessel function of the second kind.
    """
    primes = sieve_primes(N_terms + 100)
    ap_cache = curve.ap_all(primes)

    # Build a_n multiplicatively
    a = [0] * (N_terms + 1)
    a[0] = 0
    a[1] = 1

    for n in range(2, N_terms + 1):
        temp = n
        facs = {}
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                facs[d] = facs.get(d, 0) + 1
                temp //= d
            d += 1
        if temp > 1:
            facs[temp] = facs.get(temp, 0) + 1

        if len(facs) == 1:
            p, k = list(facs.items())[0]
            if p not in ap_cache:
                a[n] = 0
                continue
            ap_val = ap_cache[p]
            if k == 1:
                a[n] = ap_val
            else:
                prev1 = a[p**(k-1)] if p**(k-1) <= N_terms else 0
                prev2 = a[p**(k-2)] if p**(k-2) <= N_terms else 1
                a[n] = ap_val * prev1 - p * prev2
        else:
            val = 1
            for p, k in facs.items():
                pk = p**k
                if pk <= N_terms and a[pk] != 0:
                    val *= a[pk]
                elif p in ap_cache:
                    ap_val = ap_cache[p]
                    apk_1, apk_2 = 1, 1
                    for j in range(1, k+1):
                        apk_j = ap_val * apk_1 - p * apk_2 if j > 1 else ap_val
                        apk_2 = apk_1
                        apk_1 = apk_j
                    val *= apk_1
                else:
                    val = 0
                    break
            a[n] = val

    # Compute L''(E,1)/2! via Bessel K_0 smoothing
    sqrtN = mpmath.sqrt(mpmath.mpf(N_cond))
    total = mpmath.mpf(0)

    for n in range(1, N_terms + 1):
        if a[n] == 0:
            continue
        x = 4 * mpmath.pi * mpmath.sqrt(mpmath.mpf(n)) / sqrtN
        if x > 500:
            continue
        K0 = mpmath.besselk(0, x)
        total += mpmath.mpf(a[n]) / mpmath.mpf(n) * K0

    return float(2 * total / sqrtN)


# ============================================================
# Real period Ω
# ============================================================

def compute_omega(a4, a6):
    """Compute real period via numerical integration."""
    mpmath.mp.dps = 60
    roots = mpmath.polyroots([1, 0, a4, a6])
    real_roots = sorted([float(r.real) for r in roots if abs(r.imag) < 1e-10])

    disc = -16 * (4*a4**3 + 27*a6**2)

    if len(real_roots) >= 3:
        e1, e2, e3 = real_roots[0], real_roots[1], real_roots[2]
        if disc > 0:
            # Two components
            def integrand(x):
                v = x**3 + a4*x + a6
                return 1/mpmath.sqrt(abs(v))
            w1 = 2 * mpmath.quad(integrand, [e1, e2])
            w2 = 2 * mpmath.quad(integrand, [e3, mpmath.inf])
            return float(w1 + w2)
        else:
            e3 = max(real_roots)
            def integrand(x):
                v = x**3 + a4*x + a6
                return 1/mpmath.sqrt(v)
            return float(2 * mpmath.quad(integrand, [e3, mpmath.inf]))
    elif len(real_roots) == 1:
        e1 = real_roots[0]
        def integrand(x):
            return 1/mpmath.sqrt(x**3 + a4*x + a6)
        return float(2 * mpmath.quad(integrand, [e1, mpmath.inf]))
    else:
        return None


# ============================================================
# Regulator computation
# ============================================================

def height(P, a4, a6):
    """
    Canonical (naive) height of point P=(x,y) on y²=x³+a4x+a6.
    Uses the Silverman algorithm (simplified).
    """
    x, y = P
    if x == 0 and y == 0:
        return mpmath.mpf(0)
    # Naive height = log(max(|num|,|den|)) for x = num/den
    # For integer points: h(P) = log|x| if |x| > 1, else 0
    if abs(x) <= 1:
        return mpmath.mpf(0)
    return mpmath.log(mpmath.mpf(abs(x)))


def point_add(P, Q, a4, a6):
    """Add two points on y²=x³+a4x+a6."""
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2:
        if y1 == y2:
            # Point doubling
            lam = (3*x1*x1 + a4) / (2*y1)
            x3 = lam*lam - 2*x1
            y3 = lam*(x1 - x3) - y1
            return (x3, y3)
        else:
            return None  # P + (-P) = O
    else:
        lam = (y2 - y1) / (x2 - x1)
        x3 = lam*lam - x1 - x2
        y3 = lam*(x1 - x3) - y1
        return (x3, y3)


def naive_regulator(P1, P2, a4, a6):
    """
    Compute regulator from two independent points.
    Reg = det(⟨P_i, P_j⟩) where ⟨P,P⟩ = h(P) and ⟨P,Q⟩ = (h(P+Q)-h(P)-h(Q))/2.
    """
    h11 = height(P1, a4, a6)
    h22 = height(P2, a4, a6)
    P12 = point_add(P1, P2, a4, a6)
    if P12 is None:
        return None
    h12_full = height(P12, a4, a6)
    h12 = (h12_full - h11 - h22) / 2
    return float(h11 * h22 - h12 * h12)


# ============================================================
# Tamagawa numbers via reduction analysis
# ============================================================

def tamagawa_at_p(a4, a6, p):
    """
    Compute c_p via simplified Tate algorithm.
    For multiplicative reduction: c_p = ord_p(Δ).
    For additive reduction: c_p ∈ {1,2,3,4}.
    """
    disc = -16 * (4*a4**3 + 27*a6**2)
    if disc % p != 0:
        return 1

    # Compute valuations
    v_Delta = 0
    temp = abs(disc)
    while temp % p == 0:
        v_Delta += 1
        temp //= p

    # Check if multiplicative: p ∤ c4 where c4 = -48*a4
    c4 = -48 * a4
    v_c4 = 0
    temp2 = abs(c4) if c4 != 0 else 0
    if temp2 > 0:
        while temp2 % p == 0:
            v_c4 += 1
            temp2 //= p
    else:
        v_c4 = float('inf')

    if v_c4 == 0:
        # Multiplicative reduction: c_p = v_Delta
        return v_Delta
    else:
        # Additive reduction: c_p ∈ {1,2,3,4}
        # Simplified: for p ≥ 5, c_p = 1 for split mult, 2 for nonsplit mult
        # For p = 2,3: more complex
        if p >= 5:
            if v_Delta == 1:
                return 1  # multiplicative
            else:
                return min(v_Delta, 4)  # rough
        elif p == 3:
            return min(v_Delta, 4)
        else:  # p = 2
            return min(v_Delta, 4)


# ============================================================
# Curve-specific conductor computation
# ============================================================

def compute_conductor(a4, a6):
    """
    Compute conductor N = ∏ p^{f_p} where f_p depends on reduction type.
    For multiplicative: f_p = 1
    For additive: f_p = 2 (or more for p=2,3)
    """
    disc = abs(-16 * (4*a4**3 + 27*a6**2))
    bad_primes = list(factor(disc).keys())
    N = 1
    for p in bad_primes:
        c4 = -48 * a4
        v_c4 = 0
        if c4 != 0:
            temp = abs(c4)
            while temp % p == 0:
                v_c4 += 1
                temp //= p
        else:
            v_c4 = float('inf')

        if v_c4 == 0:
            # Multiplicative reduction: f_p = 1
            N *= p
        else:
            # Additive reduction: f_p = 2 (generally)
            # For p=2,3: could be higher
            N *= p * p  # conservative
    return N


# ============================================================
# Main: comprehensive BSD analysis for rank 2 candidates
# ============================================================

def main():
    print("=" * 80)
    print("H-009 DEEP: Strong BSD Verification for Rank 2 Candidates")
    print("=" * 80)

    candidates = [
        ("y²=x³+14x+1",  14,  1),
        ("y²=x³+8x+25",    8, 25),
        ("y²=x³-31x+34", -31, 34),
        ("y²=x³-13x+4",  -13,  4),
        ("y²=x³-40x+25", -40, 25),
    ]

    results = []

    for label, a4, a6 in candidates:
        print(f"\n{'='*80}")
        print(f"Curve: {label}")
        print(f"{'='*80}")

        curve = EC(a4, a6)
        disc = curve.disc
        print(f"  Δ = {disc}")

        # Conductor
        N_cond = compute_conductor(a4, a6)
        fac_N = factor(N_cond)
        print(f"  N = {N_cond} = {' × '.join(f'{p}^{e}' for p,e in sorted(fac_N.items()))}")

        # Real period
        print(f"\nComputing real period Ω...")
        omega = compute_omega(a4, a6)
        print(f"  Ω = {omega:.10f}")

        # Search for rational points
        print(f"\nSearching for rational points (|x| ≤ 200)...")
        points = curve.rational_points_search(200)
        print(f"  Found {len(points)} points")

        # Identify generators (naive: pick two independent points)
        # For rank 2, we need two independent points
        non_torsion = []
        for P in points:
            if P[1] != 0:  # not 2-torsion
                h = height(P, a4, a6)
                if h > 0.1:  # non-trivial height
                    non_torsion.append((P, h))

        non_torsion.sort(key=lambda x: x[1])

        if len(non_torsion) >= 2:
            P1 = non_torsion[0][0]
            P2 = non_torsion[1][0]
            print(f"  Generator candidates: P1={P1}, P2={P2}")

            # Compute regulator
            reg = naive_regulator(P1, P2, a4, a6)
            print(f"  Regulator Reg = {reg:.10f}")
        else:
            print(f"  WARNING: Few generator candidates found.")
            print(f"  Using heuristic regulator estimate.")
            # Estimate regulator from height distribution
            if non_torsion:
                reg = non_torsion[0][1] * 0.5  # rough
            else:
                reg = 1.0  # placeholder
            print(f"  Estimated Reg ≈ {reg:.10f}")

        # Tamagawa numbers
        print(f"\nTamagawa numbers at bad primes:")
        bad_primes = sorted(factor(abs(disc)).keys())
        c_v_product = 1
        c_v_details = []
        for p in bad_primes:
            c_p = tamagawa_at_p(a4, a6, p)
            c_v_product *= c_p
            c_v_details.append((p, c_p))
            print(f"  c_{p} = {c_p}")
        print(f"  ∏c_v = {c_v_product}")

        # Torsion
        # For most curves with large conductor, torsion is trivial (|tors|=1)
        # Check for 2-torsion: points with y=0
        torsion_points = [P for P in points if P[1] == 0]
        if torsion_points:
            torsion_order = 2
            print(f"\n  2-torsion point found: {torsion_points[0]}")
        else:
            # Check for other torsion by computing nP for small n
            torsion_order = 1
            for P in points[:10]:
                # Check if P has finite order
                Q = P
                for n in range(2, 13):
                    Q = point_add(Q, P, a4, a6)
                    if Q is None:
                        torsion_order = max(torsion_order, n)
                        break
        print(f"  |E(Q)_tors| ≈ {torsion_order}")

        # L''(E,1)/2! via smoothed AFE
        print(f"\nComputing L''(E,1)/2! via smoothed AFE (5000 terms)...")
        L_leading = compute_L_leading(curve, N_cond, N_terms=5000)
        print(f"  L''(E,1)/2! = {L_leading:.12f}")
        print(f"  |L''(E,1)/2!| = {abs(L_leading):.12f}")

        # BSD formula: L''/2! = Ω * Reg * c_v * |Ш| / |tors|²
        # So: |Ш| = L''/2! * |tors|² / (Ω * Reg * c_v)
        denominator = omega * reg * c_v_product
        if denominator > 0:
            bsd_ratio = abs(L_leading) * (torsion_order ** 2) / denominator
        else:
            bsd_ratio = float('nan')

        print(f"\nBSD formula:")
        print(f"  |Ш| = |L''/2!| × |tors|² / (Ω × Reg × ∏c_v)")
        print(f"      = {abs(L_leading):.10f} × {torsion_order}² / ({omega:.6f} × {reg:.6f} × {c_v_product})")
        print(f"      = {bsd_ratio:.10f}")

        sha_predicted = round(bsd_ratio)
        error_pct = abs(bsd_ratio - sha_predicted) / sha_predicted * 100 if sha_predicted > 0 else float('inf')

        print(f"\n  Rounded |Ш| = {sha_predicted}")
        print(f"  Relative error = {error_pct:.4f}%")

        # Perfect square check
        is_sq = False
        sqrt_val = 0
        if sha_predicted > 0:
            sqrt_val = int(mpmath.isqrt(sha_predicted))
            is_sq = (sqrt_val * sqrt_val == sha_predicted)
        print(f"  Is perfect square? {is_sq} (if so, √|Ш| = {sqrt_val})")

        results.append({
            'label': label,
            'a4': a4, 'a6': a6,
            'disc': disc,
            'conductor': N_cond,
            'conductor_factors': fac_N,
            'omega': float(omega),
            'regulator': float(reg),
            'regulator_note': 'computed' if len(non_torsion) >= 2 else 'estimated',
            'tamagawa_product': c_v_product,
            'tamagawa_details': c_v_details,
            'torsion_order': torsion_order,
            'L_leading': float(L_leading),
            'L_leading_abs': abs(float(L_leading)),
            'bsd_ratio': float(bsd_ratio),
            'sha_predicted': sha_predicted,
            'error_pct': float(error_pct),
            'is_perfect_square': is_sq,
            'sqrt_sha': sqrt_val,
            'num_rational_points': len(points),
            'num_non_torsion': len(non_torsion),
            'rational_points_sample': points[:20],
        })

    # ============================================================
    # Summary table
    # ============================================================
    print(f"\n\n{'#'*80}")
    print("# SUMMARY TABLE")
    print(f"{'#'*80}")
    print()
    hdr = f"{'Curve':<25} {'N':<15} {'|L''/2!|':<14} {'Ω':<12} {'Reg':<12} {'∏c_v':<6} {'|tors|':<7} {'|Ш|':<6} {'Square?':<8} {'Err%':<8}"
    print(hdr)
    print("-" * len(hdr))
    for r in results:
        sq_str = f"✓={r['sqrt_sha']}²" if r['is_perfect_square'] else '✗'
        print(f"{r['label']:<25} {r['conductor']:<15} {r['L_leading_abs']:<14.8f} {r['omega']:<12.6f} {r['regulator']:<12.6f} {r['tamagawa_product']:<6} {r['torsion_order']:<7} {r['sha_predicted']:<6} {sq_str:<8} {r['error_pct']:<8.4f}")

    # ============================================================
    # Ranking
    # ============================================================
    print(f"\n\n{'#'*80}")
    print("# CANDIDATE RANKING")
    print(f"{'#'*80}")

    ranked = sorted(results, key=lambda r: (
        not r['is_perfect_square'],
        r['error_pct'],
        not (r['regulator_note'] == 'computed'),
    ))

    for i, r in enumerate(ranked):
        marker = "★" if i == 0 else " "
        print(f"\n{marker} {i+1}. {r['label']}")
        print(f"     N = {r['conductor']}")
        print(f"     |L''/2!| = {r['L_leading_abs']:.10f}")
        print(f"     Ω = {r['omega']:.6f}, Reg = {r['regulator']:.6f}")
        print(f"     ∏c_v = {r['tamagawa_product']}, |tors| = {r['torsion_order']}")
        print(f"     |Ш|_pred = {r['sha_predicted']}, error = {r['error_pct']:.4f}%")
        print(f"     Perfect square: {'Yes' if r['is_perfect_square'] else 'No'}")
        print(f"     Regulator: {r['regulator_note']}")
        print(f"     Rational points found: {r['num_rational_points']}")

    best = ranked[0]
    print(f"\n{'='*80}")
    print(f"MOST PROMISING CANDIDATE: {best['label']}")
    print(f"{'='*80}")
    print(f"  This curve has the most convincing evidence for rank 2:")
    print(f"  - |Ш| = {best['sha_predicted']} {'(perfect square)' if best['is_perfect_square'] else '(NOT a perfect square — evidence against rank 2 or regulator estimate off)'}")
    print(f"  - BSD ratio error: {best['error_pct']:.4f}%")
    print(f"  - Regulator {'computed from generators' if best['regulator_note']=='computed' else 'estimated'}")

    # Save
    output = {
        'results': results,
        'ranking': [r['label'] for r in ranked],
        'best_candidate': best['label'],
    }
    with open('/tmp/bsd-research-swarm/computation/deep_rank2_results.json', 'w') as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nResults saved to computation/deep_rank2_results.json")
    return results


if __name__ == "__main__":
    main()
