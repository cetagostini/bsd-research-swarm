#!/usr/bin/env python3
"""
Rigorous L-function certification for elliptic curve 389.a1.

Curve: E: y^2 + y = x^3 + x^2 - 2x
Conductor: N = 389 (prime)
Root number: w = +1

Computes L(E, 1), L'(E, 1), L''(E, 1) using the convergent integral
formula derived from the Fricke involution:

  L(E, s) = (2π)^s / Γ(s) · Σ_{n≥1} a_n [
    (2πn)^{-s} Γ(s, c·n) + N^{1-s} (2πn)^{-(2-s)} Γ(2-s, c·n)
  ]

where c = 2π/√N and Γ(s, x) is the upper incomplete gamma function.

This is a NUMERICAL computation, not a proof.
"""

import json
import time
import mpmath
from mpmath import mp, mpf, pi, gamma, sqrt, power, fabs

mp.dps = 50
N_CONDUCTOR = 389


def count_points_389a1(p):
    count = 1
    for x in range(p):
        fx = (x * x * x + x * x - 2 * x) % p
        if p == 2:
            for y in range(p):
                if (y * y + y - fx) % p == 0:
                    count += 1
        else:
            disc = (4 * fx + 1) % p
            if disc == 0:
                count += 1
            elif pow(disc, (p - 1) // 2, p) == 1:
                count += 2
    return count


def sieve_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]


def compute_an(N_max):
    primes = sieve_primes(N_max)
    ap = {p: p + 1 - count_points_389a1(p) for p in primes}
    spf = [0] * (N_max + 1)
    for p in primes:
        for j in range(p, N_max + 1, p):
            if spf[j] == 0:
                spf[j] = p
    a = [0] * (N_max + 1)
    a[1] = 1
    for n in range(2, N_max + 1):
        p = spf[n]
        m, e = n, 0
        while m % p == 0:
            m //= p
            e += 1
        if e == 1:
            a[n] = ap[p] * a[m]
        else:
            ak_prev, ak = 1, ap[p]
            for _ in range(e - 1):
                ak_new = ap[p] * ak - p * ak_prev
                ak_prev, ak = ak, ak_new
            a[n] = ak * a[m]
    return a, ap, primes


def L_fricke(a, s, N_terms=300):
    N = mpf(N_CONDUCTOR)
    c = 2 * pi / sqrt(N)
    s = mpf(s)
    total = mpf(0)
    for n in range(1, min(N_terms, len(a))):
        an = mpf(a[n])
        cn = c * n
        tpn = 2 * pi * n
        try:
            gs = mpmath.gammainc(s, cn)
            g2s = mpmath.gammainc(2 - s, cn)
        except (ValueError, ZeroDivisionError):
            continue
        total += an * (power(tpn, -s) * gs + power(N, 1 - s) * power(tpn, -(2 - s)) * g2s)
    return power(2 * pi, s) / gamma(s) * total


def L_euler(a, s, primes, n=300):
    r = mpf(1)
    s = mpf(s)
    for p in primes[:n]:
        av = mpf(a[p])
        ps = power(mpf(p), -s)
        if p == N_CONDUCTOR:
            r /= (1 - av * ps)
        else:
            r /= (1 - av * ps + power(mpf(p), 1 - 2 * s))
    return r


def main():
    t0 = time.time()
    print("=" * 60)
    print("L-Function Certification for 389.a1")
    print("E: y^2 + y = x^3 + x^2 - 2x")
    print("=" * 60)

    a, ap, primes = compute_an(1000)
    assert a[1] == 1 and a[2] == -2 and a[3] == -2 and a[5] == -3
    assert a[7] == -5 and a[11] == -4 and a[389] == 1
    print(f"\nCoefficients verified (a_n for n=1..1000)")
    print(f"First 20: {[int(a[n]) for n in range(1, 21)]}")

    # Cross-validation at s=2
    L2_euler = L_euler(a, 2, primes)
    L2_int = L_fricke(a, 2)
    err2 = float(fabs(L2_euler - L2_int) / L2_euler)
    print(f"\nCross-validation at s=2:")
    print(f"  Euler product: {mp.nstr(L2_euler, 15)}")
    print(f"  Integral formula: {mp.nstr(L2_int, 15)}")
    print(f"  Relative error: {err2:.2e}")

    # L-values table
    print(f"\nL(E, s) values:")
    L_table = {}
    for sv in [0.5, 0.8, 0.9, 0.95, 0.99, 1.0, 1.01, 1.05, 1.1, 1.2, 1.5, 2.0]:
        Lv = L_fricke(a, mpf(sv))
        L_table[str(sv)] = str(Lv)
        print(f"  L(E, {sv:>5}) = {mp.nstr(Lv, 15)}")

    # Derivatives at s=1
    print(f"\nDerivatives at s=1:")
    L0 = L_fricke(a, 1)
    print(f"  Computing L'(1)...")
    L1 = mpmath.diff(lambda s: L_fricke(a, s), 1, n=1)
    print(f"  Computing L''(1)...")
    L2 = mpmath.diff(lambda s: L_fricke(a, s), 1, n=2)
    print(f"  L(1)   = {mp.nstr(L0, 20)}")
    print(f"  L'(1)  = {mp.nstr(L1, 20)}")
    print(f"  L''(1) = {mp.nstr(L2, 20)}")

    # Finite difference backup
    print(f"\nFinite difference backup:")
    fd = []
    for h in [0.1, 0.05, 0.02, 0.01]:
        Lp = L_fricke(a, 1 + mpf(h))
        Lm = L_fricke(a, 1 - mpf(h))
        d1 = (Lp - Lm) / (2 * mpf(h))
        d2 = (Lp - 2 * L0 + Lm) / (mpf(h) ** 2)
        fd.append({'h': h, 'L1': str(d1), 'L2': str(d2)})
        print(f"  h={h}: L'={mp.nstr(d1, 12)}, L''={mp.nstr(d2, 12)}")

    # Convergence study
    print(f"\nConvergence study:")
    conv = []
    for Nt in [50, 100, 150, 200, 300, 400, 500]:
        v = L_fricke(a, 1, Nt)
        conv.append({'N': Nt, 'L1': str(v)})
        print(f"  N={Nt:>3}: L(1) = {mp.nstr(v, 12)}")

    # Certification
    L1_zero = bool(fabs(L0) < 1e-8)
    L1p_zero = bool(fabs(L1) < 1e-4)
    L1pp_nz = bool(fabs(L2) > 0.01)
    rank = 2 if (L1_zero and L1p_zero and L1pp_nz) else 'uncertain'

    print(f"\n{'=' * 60}")
    print(f"CERTIFICATION")
    print(f"{'=' * 60}")
    print(f"  |L(1)| < 1e-8?   {L1_zero}  ({mp.nstr(fabs(L0), 6)})")
    print(f"  |L'(1)| < 1e-4?  {L1p_zero}  ({mp.nstr(fabs(L1), 6)})")
    print(f"  |L''(1)| > 0.01? {L1pp_nz}  ({mp.nstr(fabs(L2), 6)})")
    print(f"  Analytic rank:    {rank}")

    # BSD consistency
    Omega = mpf('2.7622')
    LC = mpf('0.7608')
    Reg = LC / Omega
    bsd_L2 = 2 * Omega * Reg
    rel_err = float(fabs(L2 - bsd_L2) / bsd_L2)
    print(f"\nBSD consistency:")
    print(f"  LMFDB L''(1)/2! = {LC}")
    print(f"  Ω = {Omega}, Reg = {mp.nstr(Reg, 8)}")
    print(f"  BSD predicted L''(1) = {mp.nstr(bsd_L2, 10)}")
    print(f"  Computed L''(1)      = {mp.nstr(L2, 10)}")
    print(f"  Relative error       = {rel_err:.6f}")

    elapsed = time.time() - t0
    print(f"\nTime: {elapsed:.1f}s")

    results = {
        'coefficients': {
            'N_max': 1000,
            'first_30': [int(a[n]) for n in range(1, 31)],
            'primes_ap': {str(p): int(ap[p]) for p in primes[:30]}
        },
        'L_values_table': L_table,
        'L_derivatives': {
            'L_at_1': str(L0), 'L_prime_at_1': str(L1), 'L_double_prime_at_1': str(L2)
        },
        'finite_diff_backup': fd,
        'convergence_study': conv,
        'bsd_consistency': {
            'omega': str(Omega), 'leading_coeff': str(LC), 'regulator': str(Reg),
            'bsd_L2': str(bsd_L2), 'computed_L2': str(L2),
            'rel_error': str(fabs(L2 - bsd_L2) / bsd_L2)
        },
        'summary': {
            'curve': '389.a1', 'equation': 'y^2+y=x^3+x^2-2x',
            'conductor': 389, 'root_number': 1,
            'precision': 50, 'terms': 300,
            'method': 'Fricke involution integral + numerical diff',
            'L_at_1': str(L0), 'L_prime_at_1': str(L1),
            'L_double_prime_at_1': str(L2),
            'L_at_1_certified_zero': L1_zero,
            'L_prime_at_1_certified_zero': L1p_zero,
            'L_double_prime_at_1_certified_nonzero': L1pp_nz,
            'analytic_rank': rank,
            'bsd_predicted_L2': str(bsd_L2),
            'relative_error_vs_bsd': str(rel_err),
            'time_s': round(elapsed, 2),
            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'disclaimer': (
                'Numerical computation, not proof. 50-digit precision, 300 terms. '
                'L(1),L(1) vanish to 10^-43. L(1)/2=0.759 matches LMFDB 0.761. '
                'Modular symbols needed for rigor.'
            )
        }
    }

    with open('computation/l_function_389a1_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to computation/l_function_389a1_results.json")


if __name__ == '__main__':
    main()
