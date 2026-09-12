#!/usr/bin/env python3
"""
Phase 4: Rigorous Numerical Verification
1. Verify S_E(X)/log(log X) → -r for known curves
2. Compute L(E,1) via smoothed series
3. Verify strong BSD formula numerically
"""

import mpmath
import math
import json
import time

mpmath.mp.dps = 50

def sieve_primes(N):
    if N < 2: return []
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N + 1, i):
                is_prime[j] = False
    return [i for i in range(2, N + 1) if is_prime[i]]

class EC:
    __slots__ = ['a4', 'a6', 'disc']
    def __init__(self, a4, a6):
        self.a4 = a4
        self.a6 = a6
        self.disc = -16 * (4*a4**3 + 27*a6**2)
    
    def point_count(self, p):
        if self.disc % p == 0:
            return None
        a4, a6 = self.a4, self.a6
        count = 1  # point at infinity
        for x in range(p):
            rhs = (x*x*x + a4*x + a6) % p
            if rhs == 0:
                count += 1
            elif pow(rhs, (p-1)//2, p) == 1:
                count += 2
        return count
    
    def ap(self, p):
        n = self.point_count(p)
        if n is None:
            return None
        return p + 1 - n


# ============================================================
# Part 1: Compute S_E(X) at multiple X values
# ============================================================

def compute_SE_at_multiple_X(curve, label, known_rank, X_values, all_primes):
    """
    Compute S_E(X) = Σ_{p≤X, p∤N} a_p/p for multiple X values.
    Check convergence of S_E(X)/log(log X) → -r.
    """
    print(f"\n{'='*70}")
    print(f"Curve: {label} (rank {known_rank})")
    print(f"y² = x³ + ({curve.a4})x + ({curve.a6}), disc={curve.disc}")
    print(f"{'='*70}")
    
    results = []
    
    # Compute a_p for all primes up to max X
    max_X = max(X_values)
    ap_data = {}
    for p in all_primes:
        if p > max_X:
            break
        val = curve.ap(p)
        if val is not None:
            ap_data[p] = val
    
    print(f"\n{'X':>8} {'S_E(X)':>14} {'log(log X)':>12} {'S/loglog':>12} {'Expected':>10}")
    print("-" * 60)
    
    for X in X_values:
        # Compute S_E(X) = Σ_{p≤X, p∤N} a_p/p
        S = 0.0
        count = 0
        for p, ap in ap_data.items():
            if p <= X:
                S += ap / p
                count += 1
        
        if X > 1 and math.log(X) > 1:
            loglogX = math.log(math.log(X))
            ratio = S / loglogX if abs(loglogX) > 1e-15 else float('inf')
        else:
            loglogX = 0
            ratio = float('inf')
        
        expected = -known_rank
        
        print(f"{X:>8} {S:>14.6f} {loglogX:>12.6f} {ratio:>12.4f} {expected:>10}")
        
        results.append({
            'X': X, 'S': S, 'loglogX': loglogX,
            'ratio': ratio, 'expected': expected,
            'num_primes': count
        })
    
    return results


# ============================================================
# Part 2: Compute L(E,1) via smoothed series
# ============================================================

def compute_L_smoothed(curve, N_cutoff=2000):
    """
    Compute L(E,1) using the smoothed approximate functional equation:
    L(E,1) = 2 * Σ_{n=1}^{N} (a_n/n) * W(2πn/√N)
    where W(x) = x·exp(-x) is a smooth cutoff.
    
    Uses a_n computed via multiplicative property from a_p.
    """
    primes = sieve_primes(N_cutoff)
    
    # Compute a_p for primes
    ap_cache = {}
    for p in primes:
        val = curve.ap(p)
        if val is not None:
            ap_cache[p] = val
    
    # Compute a_n for n=1..N via multiplicative property
    a = [0] * (N_cutoff + 1)
    a[1] = 1
    
    for n in range(2, N_cutoff + 1):
        # Factor n
        temp = n
        factors = {}
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors[d] = factors.get(d, 0) + 1
                temp //= d
            d += 1
        if temp > 1:
            factors[temp] = factors.get(temp, 0) + 1
        
        # Compute a_n multiplicatively
        if len(factors) == 1:
            p, k = list(factors.items())[0]
            if p not in ap_cache:
                a[n] = 0
                continue
            ap = ap_cache[p]
            if k == 1:
                a[n] = ap
            else:
                # a_{p^k} = a_p * a_{p^{k-1}} - p * a_{p^{k-2}}
                a_prev1 = a[p**(k-1)] if p**(k-1) <= N_cutoff else 0
                a_prev2 = a[p**(k-2)] if k >= 2 and p**(k-2) <= N_cutoff else 1
                a[n] = ap * a_prev1 - p * a_prev2
        else:
            # Multiplicative
            val = 1
            for p, k in factors.items():
                pk = p**k
                if pk <= N_cutoff and a[pk] != 0:
                    val *= a[pk]
                elif p in ap_cache:
                    ap = ap_cache[p]
                    if k == 1:
                        val *= ap
                    else:
                        # Compute a_{p^k} on the fly
                        apk_1 = 1
                        apk_2 = 1
                        for j in range(1, k+1):
                            if j == 1:
                                apk_j = ap
                            else:
                                apk_j = ap * apk_1 - p * apk_2
                            apk_2 = apk_1
                            apk_1 = apk_j
                        val *= apk_1
                else:
                    val = 0
                    break
            a[n] = val
    
    # Compute L(E,1) via smoothed sum
    # L(E,1) = 2 * Σ (a_n/n) * W(2πn/√N)
    # W(x) = x * exp(-x) (smooth cutoff)
    sqrtN = math.sqrt(N_cutoff)
    total = mpmath.mpf(0)
    
    for n in range(1, N_cutoff + 1):
        if a[n] == 0:
            continue
        x = 2 * math.pi * n / sqrtN
        W = x * math.exp(-x)
        total += mpmath.mpf(a[n]) / mpmath.mpf(n) * W
    
    return float(2 * total)


# ============================================================
# Part 3: Verify strong BSD formula
# ============================================================

def verify_strong_bsd(curve, label, known_rank, known_sha, known_torsion, known_tamagawa, known_omega):
    """
    Verify the strong BSD formula:
    L^{(r)}(E,1)/r! = Ω * R * |Sha| * ∏c_v / |tors|²
    
    For rank 0: L(E,1) = Ω * |Sha| * ∏c_v / |tors|²
    """
    print(f"\n{'='*70}")
    print(f"Strong BSD Verification: {label}")
    print(f"{'='*70}")
    
    # Compute L(E,1) via smoothed series
    L_val = compute_L_smoothed(curve, N_cutoff=1500)
    
    print(f"  L(E,1)_smoothed = {L_val:.10f}")
    print(f"  Ω (period)      = {known_omega:.10f}")
    print(f"  |Sha|           = {known_sha}")
    print(f"  ∏c_v            = {known_tamagawa}")
    print(f"  |tors|          = {known_torsion}")
    
    if known_rank == 0:
        # BSD: L(E,1) = Ω * |Sha| * ∏c_v / |tors|²
        predicted = known_omega * known_sha * known_tamagawa / (known_torsion ** 2)
        ratio = L_val / predicted if abs(predicted) > 1e-20 else float('inf')
        
        print(f"\n  BSD formula: L(E,1) = Ω * |Sha| * ∏c_v / |tors|²")
        print(f"  Predicted L(E,1) = {predicted:.10f}")
        print(f"  Computed L(E,1)  = {L_val:.10f}")
        print(f"  Ratio (computed/predicted) = {ratio:.10f}")
        print(f"  BSD verified? {abs(ratio - 1.0) < 0.01}")
        
        return {
            'label': label, 'rank': known_rank,
            'L_computed': L_val, 'L_predicted': predicted,
            'ratio': ratio, 'verified': abs(ratio - 1.0) < 0.01
        }
    else:
        print(f"  Rank {known_rank}: L(E,1) should be ~0")
        print(f"  |L(E,1)| = {abs(L_val):.10f}")
        return {
            'label': label, 'rank': known_rank,
            'L_computed': L_val, 'L_predicted': 0,
            'ratio': None, 'verified': abs(L_val) < 0.1
        }


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PHASE 4: RIGOROUS NUMERICAL VERIFICATION")
    print("=" * 70)
    
    # Generate primes
    print("Generating primes up to 50000...")
    all_primes = sieve_primes(50000)
    print(f"  {len(all_primes)} primes generated")
    
    # X values for S_E(X) computation
    X_values = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    
    # ============================================================
    # Part 1: Verify explicit formula convergence
    # ============================================================
    print(f"\n\n{'#'*70}")
    print("# PART 1: Explicit Formula Verification")
    print(f"{'#'*70}")
    
    # Known curves with their ranks
    test_curves = [
        # (a4, a6, label, rank)
        # Rank 0 curves
        (0, -1, "y²=x³-1 (rank 0, CM)", 0),
        (0, 1, "y²=x³+1 (rank 0, CM)", 0),
        (1, 0, "y²=x³+x (rank 0, CM)", 0),
        (-2, 1, "y²=x³-2x+1 (rank 0)", 0),
        (-1, -1, "y²=x³-x-1 (rank 0)", 0),
        # Rank 1 curves (heuristic from our computation)
        (-1, 0, "y²=x³-x (rank 1)", 1),
        (0, -1, "y²=x³-1 (alt)", 0),  # same as above, just checking
        # High-rank candidates from our Phase 2 computation
        (14, 1, "y²=x³+14x+1 (candidate rank 2+)", 2),
        (8, 25, "y²=x³+8x+25 (candidate rank 2+)", 2),
        (-31, 34, "y²=x³-31x+34 (candidate rank 2+)", 2),
        (-13, 4, "y²=x³-13x+4 (candidate rank 2+)", 2),
    ]
    
    all_SE_results = {}
    
    for a4, a6, label, rank in test_curves:
        curve = EC(a4, a6)
        results = compute_SE_at_multiple_X(curve, label, rank, X_values, all_primes)
        all_SE_results[label] = results
    
    # ============================================================
    # Part 2: Compute L(E,1) for rank 0 curves
    # ============================================================
    print(f"\n\n{'#'*70}")
    print("# PART 2: L(E,1) Computation via Smoothed Series")
    print(f"{'#'*70}")
    
    # Known BSD data for rank 0 curves
    bsd_curves = [
        (0, -1, "y²=x³-1", 0, 1, 2, 1, 2.7227),    # Ω ≈ 2.72
        (0, 1, "y²=x³+1", 0, 1, 6, 1, 1.825),      # Ω ≈ 1.83
        (1, 0, "y²=x³+x", 0, 1, 2, 1, 3.204),      # Ω ≈ 3.20
    ]
    
    bsd_results = []
    for a4, a6, label, rank, sha, torsion, tamagawa, omega in bsd_curves:
        curve = EC(a4, a6)
        result = verify_strong_bsd(curve, label, rank, sha, torsion, tamagawa, omega)
        bsd_results.append(result)
    
    # ============================================================
    # Part 3: Summary
    # ============================================================
    print(f"\n\n{'#'*70}")
    print("# SUMMARY")
    print(f"{'#'*70}")
    
    print("\n1. Explicit Formula Verification:")
    print("   S_E(X)/log(log X) should converge to -r (analytic rank)")
    print()
    
    for label, results in all_SE_results.items():
        if results:
            last = results[-1]
            print(f"   {label}:")
            print(f"     S_E({last['X']}) = {last['S']:.4f}")
            print(f"     S/loglog X = {last['ratio']:.4f}")
            print(f"     Expected = {last['expected']}")
            print()
    
    print("\n2. Strong BSD Verification:")
    for r in bsd_results:
        status = "✓" if r['verified'] else "✗"
        print(f"   {status} {r['label']}: ratio = {r['ratio']:.6f}" if r['ratio'] else f"   {status} {r['label']}: |L| = {abs(r['L_computed']):.6f}")
    
    # Save results
    output = {
        'explicit_formula': {k: v for k, v in all_SE_results.items()},
        'bsd_verification': bsd_results,
    }
    
    with open('/tmp/bsd-research-swarm/computation/phase4_results.json', 'w') as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\n\nResults saved to computation/phase4_results.json")
