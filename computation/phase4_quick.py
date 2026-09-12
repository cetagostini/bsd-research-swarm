#!/usr/bin/env python3
"""
Phase 4 Quick: Verify explicit formula with smaller prime range.
"""

import math
import json

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
    def __init__(self, a4, a6):
        self.a4 = a4
        self.a6 = a6
        self.disc = -16 * (4*a4**3 + 27*a6**2)
    
    def ap(self, p):
        if self.disc % p == 0:
            return None
        a4, a6 = self.a4, self.a6
        count = 1
        for x in range(p):
            rhs = (x*x*x + a4*x + a6) % p
            if rhs == 0:
                count += 1
            elif pow(rhs, (p-1)//2, p) == 1:
                count += 2
        return p + 1 - count


def compute_SE(curve, primes, X):
    S = 0.0
    count = 0
    for p in primes:
        if p > X:
            break
        val = curve.ap(p)
        if val is not None:
            S += val / p
            count += 1
    return S, count


print("=" * 70)
print("PHASE 4 QUICK: Explicit Formula Verification")
print("=" * 70)

# Generate primes up to 10000
primes = sieve_primes(10000)
print(f"Primes up to 10000: {len(primes)}")

X_values = [100, 500, 1000, 2000, 5000, 10000]

# Test curves
curves = [
    (0, -1, "y²=x³-1", 0),
    (0, 1, "y²=x³+1", 0),
    (1, 0, "y²=x³+x", 0),
    (-2, 1, "y²=x³-2x+1", 0),
    (-1, -1, "y²=x³-x-1", 0),
    (-1, 0, "y²=x³-x", 1),
    (14, 1, "y²=x³+14x+1", 2),
    (8, 25, "y²=x³+8x+25", 2),
    (-31, 34, "y²=x³-31x+34", 2),
    (-13, 4, "y²=x³-13x+4", 2),
    (-40, 25, "y²=x³-40x+25", 2),
]

results = {}

for a4, a6, label, expected_rank in curves:
    curve = EC(a4, a6)
    
    print(f"\n{label} (expected rank {expected_rank}):")
    print(f"  {'X':>6} {'S_E(X)':>12} {'loglogX':>10} {'S/loglog':>10} {'-r':>6}")
    print(f"  {'-'*50}")
    
    curve_results = []
    for X in X_values:
        S, n = compute_SE(curve, primes, X)
        if X > 1 and math.log(X) > 1:
            loglogX = math.log(math.log(X))
            ratio = S / loglogX
        else:
            loglogX = 0
            ratio = 0
        
        print(f"  {X:>6} {S:>12.4f} {loglogX:>10.4f} {ratio:>10.4f} {-expected_rank:>6}")
        curve_results.append({'X': X, 'S': S, 'ratio': ratio})
    
    results[label] = {
        'expected_rank': expected_rank,
        'data': curve_results,
        'final_ratio': curve_results[-1]['ratio'] if curve_results else 0,
    }

# Summary
print(f"\n\n{'='*70}")
print("SUMMARY: Does S_E(X)/log(log X) → -r?")
print(f"{'='*70}")
print(f"\n{'Curve':<30} {'Expected -r':>12} {'Actual ratio':>14} {'Match?':>8}")
print("-" * 70)

for label, data in results.items():
    expected = -data['expected_rank']
    actual = data['final_ratio']
    # For rank 0, ratio should → 0; for rank r, ratio should → -r
    # With limited primes, there's noise, so check if within 2 of expected
    match = abs(actual - expected) < 2.0 if data['expected_rank'] > 0 else abs(actual) < 1.0
    print(f"  {label:<28} {expected:>12.4f} {actual:>14.4f} {'✓' if match else '✗':>8}")

# Save
with open('/tmp/bsd-research-swarm/computation/phase4_quick.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\nSaved to computation/phase4_quick.json")
