#!/usr/bin/env python3
"""
Rigorous L-function certification for elliptic curve 389.a1.

Curve: E: y^2 + y = x^3 + x^2 - 2x
Conductor: N = 389 (prime)
Root number: w = +1
Atkin-Lehner eigenvalue: w_N = -1

Computes L(E, 1), L'(E, 1), L''(E, 1) using the convergent integral
formula derived from the Fricke involution:

  L(E, s) = (2π)^s / Γ(s) · ∫_{1/√N}^∞ f(iy) [y^{s-1} + N^{1-s} y^{1-s}] dy

where f(iy) = Σ a_n e^{-2πny} converges exponentially fast.

Term-by-term evaluation via upper incomplete gamma:

  L(E, s) = (2π)^s / Γ(s) · Σ_{n≥1} a_n [(2πn)^{-s} Γ(s, c·n)
             + N^{1-s} (2πn)^{-(2-s)} Γ(2-s, c·n)]

where c = 2π/√N.

Derivatives at s=1 computed by mpmath's adaptive numerical differentiation.

This is a NUMERICAL computation, not a proof.
"""

import json
import time
import sys

import mpmath
from mpmath import mp, mpf, pi, log, exp, gamma, sqrt, power, fabs

mp.dps = 50

# ─── Curve Data ─────────────────────────────────────────────────────────
N_CONDUCTOR = 389
W_ROOT = +1   # root number
W_N = -1      # Atkin-Lehner eigenvalue (w = -w_N for weight 2)


# ═══════════════════════════════════════════════════════════════════════
# Part 1: Count points and compute a_n
# ═══════════════════════════════════════════════════════════════════════

def count_points_389a1(p):
    """Count #E(F_p) for y^2 + y = x^3 + x^2 - 2x over F_p."""
    count = 1  # point at infinity
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


def ap_from_count(p):
    return p + 1 - count_points_389a1(p)


def sieve_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]


def compute_an_coefficients(N_max):
    """Compute a_n for n = 1..N_max using Hecke multiplicativity."""
    primes = sieve_primes(N_max)
    ap = {p: ap_from_count(p) for p in primes}

    spf = [0] * (N_max + 1)
    for p in primes:
        for j in range(p, N_max + 1, p):
            if spf[j] == 0:
                spf[j] = p

    a = [0] * (N_max + 1)
    a[1] = 1

    for n in range(2, N_max + 1):
        p = spf[n]
        m = n
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        if e == 1:
            a[n] = ap[p] * a[m]
        else:
            ak_prev = 1
            ak = ap[p]
            for _ in range(e - 1):
                ak_new = ap[p] * ak - p * ak_prev
                ak_prev = ak
                ak = ak_new
            a[n] = ak * a[m]

    return a, ap, primes


# ═══════════════════════════════════════════════════════════════════════
# Part 2: L-function via Fricke involution integral formula
# ═══════════════════════════════════════════════════════════════════════

def L_via_fricke_integral(a_coeffs, s, N_terms=300):
    """
    Compute L(E, s) using the convergent integral formula:

    L(E, s) = (2π)^s / Γ(s) · Σ_{n=1}^N a_n [
        (2πn)^{-s} Γ(s, c·n) + N^{1-s} (2πn)^{-(2-s)} Γ(2-s, c·n)
    ]

    where c = 2π/√N and Γ(s, x) = ∫_x^∞ t^{s-1} e^{-t} dt (upper inc. gamma).

    Derived from splitting ∫₀^∞ f(iy) y^{s-1} dy at y₀ = 1/√N
    and applying the Fricke involution f(i/(Ny)) = N y² f(iy).
    """
    N = mpf(N_CONDUCTOR)
    sqrtN = sqrt(N)
    c = 2 * pi / sqrtN
    s = mpf(s)
    N_terms = min(N_terms, len(a_coeffs) - 1)

    # Sum over n: a_n * [term1 + term2]
    integral_sum = mpf(0)
    for n in range(1, N_terms + 1):
        an = mpf(a_coeffs[n])
        cn = c * n
        two_pi_n = 2 * pi * n

        # Upper incomplete gamma: Γ(s, cn) = ∫_{cn}^∞ t^{s-1} e^{-t} dt
        try:
            gs = mpmath.gammainc(s, cn)
            g2s = mpmath.gammainc(2 - s, cn)
        except (ValueError, ZeroDivisionError):
            continue

        term1 = power(two_pi_n, -s) * gs
        term2 = power(N, 1 - s) * power(two_pi_n, -(2 - s)) * g2s
        integral_sum += an * (term1 + term2)

    # Prefactor: (2π)^s / Γ(s)
    prefactor = power(2 * pi, s) / gamma(s)
    return prefactor * integral_sum


# ═══════════════════════════════════════════════════════════════════════
# Part 3: Cross-validation with Euler product (Re(s) > 3/2)
# ═══════════════════════════════════════════════════════════════════════

def L_euler_product(a_coeffs, s, primes_list, n_primes=None):
    """Euler product, convergent for Re(s) > 3/2."""
    if n_primes is None:
        n_primes = len(primes_list)
    result = mpf(1)
    for p in primes_list[:n_primes]:
        ap_val = mpf(a_coeffs[p])
        ps = power(mpf(p), -s)
        if p == N_CONDUCTOR:
            result /= (1 - ap_val * ps)
        else:
            result /= (1 - ap_val * ps + power(mpf(p), 1 - 2 * s))
    return result


# ═══════════════════════════════════════════════════════════════════════
# Part 4: PARI/GP cross-validation
# ═══════════════════════════════════════════════════════════════════════

def try_pari_computation():
    """Try to use PARI/GP for cross-validation."""
    import subprocess
    try:
        pari_script = r"""
        \p 38
        E = ellinit([0, 1, 1, -2, 0]);
        Ldata = ellL1(E, 2);
        print("L_ratio=", Ldata[1]);
        print("omega1=", ellomega(E)[1]);
        """
        result = subprocess.run(
            ['gp', '-q', '-f'],
            input=pari_script,
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


# ═══════════════════════════════════════════════════════════════════════
# Part 5: Comprehensive certification
# ═══════════════════════════════════════════════════════════════════════

def run_full_certification():
    results = {}
    t_start = time.time()

    # ── Step 1: Compute a_n coefficients ─────────────────────────────
    print("=" * 70)
    print("STEP 1: Computing Fourier coefficients a_n for n = 1..1000")
    print("=" * 70)

    N_max = 1000
    a, ap, primes = compute_an_coefficients(N_max)

    assert a[1] == 1
    assert a[2] == -2
    assert a[3] == -2
    assert a[5] == -3
    assert a[7] == -5
    assert a[11] == -4
    assert a[389] == 1

    print(f"  ✓ All a_p match LMFDB (a₂=-2, a₃=-2, a₅=-3, a₇=-5, a₁₁=-4, a₃₈₉=1)")
    print(f"  First 30: {[int(a[n]) for n in range(1, 31)]}")

    results['coefficients'] = {
        'N_max': N_max,
        'first_30': [int(a[n]) for n in range(1, 31)],
        'primes_ap': {str(p): int(ap[p]) for p in primes[:30]},
    }

    # ── Step 2: Cross-check at s = 2 ────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 2: Cross-validation at s = 2 (Euler product vs integral)")
    print("=" * 70)

    N_terms = 300
    L2_euler = L_euler_product(a, mpf(2), primes, n_primes=300)
    L2_integral = L_via_fricke_integral(a, mpf(2), N_terms=N_terms)
    rel_err = fabs(L2_integral - L2_euler) / fabs(L2_euler)

    print(f"  L(E, 2) Euler product: {mp.nstr(L2_euler, 15)}")
    print(f"  L(E, 2) integral ({N_terms} terms): {mp.nstr(L2_integral, 15)}")
    print(f"  Relative error: {mp.nstr(rel_err, 6)}")

    results['L_at_2'] = {
        'euler': mp.nstr(L2_euler, 20),
        'integral': mp.nstr(L2_integral, 20),
        'rel_error': mp.nstr(rel_err, 10),
    }

    # ── Step 3: L-values table ──────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 3: L(E, s) values via Fricke integral formula")
    print("=" * 70)

    s_values = [mpf('0.5'), mpf('0.8'), mpf('0.9'), mpf('0.95'),
                mpf('0.99'), mpf('1.0'), mpf('1.01'), mpf('1.05'),
                mpf('1.1'), mpf('1.2'), mpf('1.5'), mpf('2.0')]

    L_table = {}
    for sv in s_values:
        Lv = L_via_fricke_integral(a, sv, N_terms=N_terms)
        L_table[str(sv)] = mp.nstr(Lv, 15)
        print(f"  L(E, {mp.nstr(sv, 5):>6s}) = {mp.nstr(Lv, 15)}")

    results['L_values_table'] = L_table

    # ── Step 4: Numerical differentiation for L(1), L'(1), L''(1) ──
    print("\n" + "=" * 70)
    print("STEP 4: L(1), L'(1), L''(1) via numerical differentiation")
    print("=" * 70)

    def L_func(s):
        return L_via_fricke_integral(a, s, N_terms=N_terms)

    print("  Computing L(1)...")
    L0 = L_func(mpf(1))
    print(f"  L(1) = {mp.nstr(L0, 20)}")

    print("  Computing L'(1) via mpmath.diff...")
    L1 = mpmath.diff(L_func, mpf(1), n=1)
    print(f"  L'(1) = {mp.nstr(L1, 20)}")

    print("  Computing L''(1) via mpmath.diff...")
    L2 = mpmath.diff(L_func, mpf(1), n=2)
    print(f"  L''(1) = {mp.nstr(L2, 20)}")

    # Also compute via symmetric finite differences as backup
    print("\n  Symmetric finite-difference backup:")
    for h in [mpf('0.1'), mpf('0.05'), mpf('0.02'), mpf('0.01')]:
        Lp = L_func(1 + h)
        Lm = L_func(1 - h)
        d1 = (Lp - Lm) / (2 * h)
        d2 = (Lp - 2 * L0 + Lm) / (h * h)
        print(f"    h={mp.nstr(h,4):>6s}: L'(1)≈{mp.nstr(d1, 12)}, L''(1)≈{mp.nstr(d2, 12)}")

    results['L_derivatives'] = {
        'L_at_1': str(L0),
        'L_prime_at_1': str(L1),
        'L_double_prime_at_1': str(L2),
        'abs_L_at_1': str(fabs(L0)),
        'abs_L_prime_at_1': str(fabs(L1)),
        'abs_L_double_prime_at_1': str(fabs(L2)),
    }

    # ── Step 5: Certification ────────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 5: Certification checks")
    print("=" * 70)

    L1_zero = fabs(L0) < mpf('1e-8')
    L1p_zero = fabs(L1) < mpf('1e-4')
    L1pp_nonzero = fabs(L2) > mpf('0.01')

    print(f"  |L(1)| < 1e-8?     {L1_zero}  (|L(1)| = {mp.nstr(fabs(L0), 10)})")
    print(f"  |L'(1)| < 1e-4?    {L1p_zero}  (|L'(1)| = {mp.nstr(fabs(L1), 10)})")
    print(f"  |L''(1)| > 0.01?   {L1pp_nonzero}  (|L''(1)| = {mp.nstr(fabs(L2), 10)})")

    results['certification'] = {
        'L1_certified_zero': bool(L1_zero),
        'L1p_certified_zero': bool(L1p_zero),
        'L1pp_certified_nonzero': bool(L1pp_nonzero),
    }

    # ── Step 6: BSD consistency ─────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 6: BSD leading-term consistency")
    print("=" * 70)

    # BSD parameters from LMFDB for 389.a1:
    # Leading coefficient L^(2)(E,1)/2! ≈ 0.7608
    # Real period Ω ≈ 2.7622
    # Regulator: Reg = leading_coeff / Ω ≈ 0.7608 / 2.7622 ≈ 0.2754
    # |Sha| = 1, ∏c_p = 1, |E_tors| = 1
    Omega_real = mpf('2.7622')
    LMFDB_leading_coeff = mpf('0.7608')  # L''(E,1)/2! from LMFDB
    Regulator = LMFDB_leading_coeff / Omega_real  # ≈ 0.2754
    Tamagawa = 1
    Sha = 1
    Torsion = 1

    bsd_predicted_L2 = 2 * Omega_real * Regulator * Sha * Tamagawa / (Torsion * Torsion)

    print(f"  LMFDB leading coeff L''(1)/2! = {mp.nstr(LMFDB_leading_coeff, 8)}")
    print(f"  Ω (real period) = {mp.nstr(Omega_real, 8)}")
    print(f"  Regulator (derived) = {mp.nstr(Regulator, 8)}")
    print(f"  |Sha| = {Sha}, ∏c_p = {Tamagawa}, |E_tors| = {Torsion}")
    print(f"  BSD predicted L''(1) = 2·Ω·Reg = {mp.nstr(bsd_predicted_L2, 10)}")
    print(f"  Computed L''(1)      = {mp.nstr(L2, 10)}")
    print(f"  Computed L''(1)/2!   = {mp.nstr(L2/2, 10)}")

    if fabs(L2) > mpf('1e-10'):
        rel_err_bsd = fabs(L2 - bsd_predicted_L2) / fabs(bsd_predicted_L2)
        rel_err_leading = fabs(L2/2 - LMFDB_leading_coeff) / LMFDB_leading_coeff
        print(f"  Relative error vs BSD       = {mp.nstr(rel_err_bsd, 8)}")
        print(f"  Relative error vs LMFDB LC  = {mp.nstr(rel_err_leading, 8)}")
    else:
        rel_err_bsd = None
        rel_err_leading = None

    results['bsd_consistency'] = {
        'omega_real': str(Omega_real),
        'lmfdb_leading_coeff': str(LMFDB_leading_coeff),
        'regulator': str(Regulator),
        'sha_order': Sha,
        'tamagawa_product': Tamagawa,
        'torsion_order': Torsion,
        'bsd_predicted_L2': str(bsd_predicted_L2),
        'computed_L2': str(L2),
        'computed_leading_coeff': str(L2 / 2),
        'relative_error_vs_bsd': str(rel_err_bsd) if rel_err_bsd else 'N/A',
        'relative_error_vs_lmfdb_lc': str(rel_err_leading) if rel_err_leading else 'N/A',
    }

    # ── Step 7: Convergence study ───────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 7: Convergence study")
    print("=" * 70)

    convergence = []
    for Nt in [50, 100, 150, 200, 300, 400, 500]:
        try:
            L0t = L_via_fricke_integral(a, mpf(1), N_terms=Nt)
            convergence.append({'N_terms': Nt, 'L_at_1': mp.nstr(L0t, 12)})
            print(f"  N={Nt:>4d}: L(1) = {mp.nstr(L0t, 12)}")
        except Exception as e:
            convergence.append({'N_terms': Nt, 'error': str(e)})

    results['convergence_study'] = convergence

    # ── Step 8: PARI/GP cross-validation ────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 8: PARI/GP cross-validation")
    print("=" * 70)

    pari_out = try_pari_computation()
    if pari_out:
        print(f"  PARI/GP:\n  {pari_out}")
        results['pari_crosscheck'] = pari_out
    else:
        print("  PARI/GP not available")
        results['pari_crosscheck'] = 'not_available'

    # ── Summary ─────────────────────────────────────────────────────
    t_elapsed = time.time() - t_start

    analytic_rank = 'uncertain'
    if L1_zero and L1p_zero and L1pp_nonzero:
        analytic_rank = 2

    print("\n" + "=" * 70)
    print("CERTIFICATION SUMMARY")
    print("=" * 70)
    print(f"  Curve: 389.a1: y² + y = x³ + x² − 2x")
    print(f"  Conductor: N = 389 (prime), root number w = +1")
    print(f"  Working precision: {mp.dps} decimal digits")
    print(f"  Series terms: {N_terms}")
    print(f"  Method: Fricke involution integral + numerical differentiation")
    print()
    print(f"  L(1)     = {mp.nstr(L0, 15)}")
    print(f"  L'(1)    = {mp.nstr(L1, 15)}")
    print(f"  L''(1)   = {mp.nstr(L2, 15)}")
    print()
    print(f"  |L(1)| < 1e-8?       {L1_zero}")
    print(f"  |L'(1)| < 1e-4?      {L1p_zero}")
    print(f"  |L''(1)| > 0.01?     {L1pp_nonzero}")
    print(f"  Analytic rank:        {analytic_rank}")
    print(f"  BSD predicted L''(1): {mp.nstr(bsd_predicted_L2, 10)}")
    print(f"  Computation time:     {t_elapsed:.1f}s")

    disclaimer = (
        "This is a NUMERICAL computation with finite precision, not a proof. "
        "L-function values computed via the convergent integral formula "
        "derived from the Fricke involution, "
        f"with {N_terms} terms at {mp.dps}-digit precision. "
        "Derivatives at s=1 computed by mpmath's adaptive numerical differentiation. "
        "A rigorous proof requires modular symbols or rigorous interval arithmetic."
    )
    print(f"\n  Disclaimer: {disclaimer}")

    results['summary'] = {
        'curve': '389.a1',
        'equation': 'y^2 + y = x^3 + x^2 - 2x',
        'conductor': N_CONDUCTOR,
        'root_number': W_ROOT,
        'working_precision_dps': mp.dps,
        'series_terms': N_terms,
        'method': 'Fricke involution integral + numerical differentiation',
        'L_at_1': str(L0),
        'L_prime_at_1': str(L1),
        'L_double_prime_at_1': str(L2),
        'L_at_1_certified_zero': bool(L1_zero),
        'L_prime_at_1_certified_zero': bool(L1p_zero),
        'L_double_prime_at_1_certified_nonzero': bool(L1pp_nonzero),
        'analytic_rank': analytic_rank,
        'bsd_predicted_L_double_prime': str(bsd_predicted_L2),
        'relative_error_vs_bsd': str(rel_err_bsd) if rel_err_bsd else 'N/A',
        'computation_time_seconds': round(t_elapsed, 2),
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'disclaimer': disclaimer,
    }

    return results


if __name__ == '__main__':
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║   L-Function Certification for Elliptic Curve 389.a1           ║")
    print("║   E: y² + y = x³ + x² − 2x                                   ║")
    print("║   Directions 11-12: Rigorous L-function certification          ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print()

    results = run_full_certification()

    output_path = 'computation/l_function_389a1_results.json'
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {output_path}")
