#!/usr/bin/env python3
"""
Cycle 3: Exhaustive verification of |Ш| for all rank 2 elliptic curves
with conductor ≤ 10000.

BSD formula: L^(r)(E,1)/r! = c · R · S
  where c = ellbsd(E), R = regulator, S = |Ш|

So |Ш| = L^(r)(E,1) / (r! · c · R)

For each rank 2 curve:
  1. Compute L^(2)(E,1) via lfun(E,1,2)
  2. Compute c = ellbsd(E)
  3. Compute R = det(height matrix of generators)
  4. |Ш| = L^(2)(E,1) / (2! · c · R)
  5. Check |Ш| is a positive integer and perfect square
"""

import json
import math
import sys
import time
from collections import Counter

from cypari2 import Pari

P = Pari()


def compute_sha(E, label):
    """Compute |Ш| for a rank 2 elliptic curve."""
    # Analytic rank and L^(r)(1)
    ar = P.ellanalyticrank(E)
    rank = int(ar[0])
    L_leading = float(ar[1])  # This is L^(r)(1), NOT L^(r)(1)/r!

    if rank != 2:
        return None

    # ellbsd: c where L^(r)(1)/r! = c * R * S
    bsd_c = float(P.ellbsd(E))

    # Generators and regulator
    gens = P.ellgenerators(E)
    if len(gens) < rank:
        # Generators not found — can't compute regulator
        return {'error': 'generators_missing', 'rank': rank}

    H = P.ellheightmatrix(E, gens)
    reg = float(P.matdet(H))

    if abs(reg) < 1e-30:
        return {'error': 'zero_regulator', 'rank': rank}

    # |Ш| = L^(r)(1) / (r! · c · R)
    sha_float = L_leading / (math.factorial(rank) * bsd_c * reg)

    # Additional BSD data
    tors = P.elltors(E)
    gr = P.ellglobalred(E)
    conductor = int(gr[0])
    torsion_order = int(tors[0])
    prod_cp = int(gr[2])

    # Round to nearest integer
    sha_rounded = round(sha_float)
    error = abs(sha_float - sha_rounded)

    # Verify: is it a perfect square?
    if sha_rounded > 0:
        sqrt_sha = math.isqrt(sha_rounded)
        is_square = sqrt_sha * sqrt_sha == sha_rounded
    else:
        sqrt_sha = 0
        is_square = False

    return {
        'label': label,
        'conductor': conductor,
        'rank': rank,
        'torsion': torsion_order,
        'prod_cp': prod_cp,
        'regulator': round(reg, 12),
        'bsd_c': round(bsd_c, 12),
        'L_leading': round(L_leading, 12),
        'sha_float': round(sha_float, 10),
        'sha': sha_rounded,
        'sha_error': round(error, 10),
        'is_square': is_square,
        'sqrt_sha': sqrt_sha,
    }


def main():
    t0 = time.time()

    # Step 1: Find all rank 2 curves with conductor ≤ 10000
    print("=" * 70)
    print("EXHAUSTIVE |Ш| VERIFICATION FOR RANK 2 CURVES, N ≤ 10000")
    print("=" * 70)
    print()
    print("Phase 1: Enumerating all elliptic curves with conductor ≤ 10000...")

    rank2_curves = []
    total_curves = 0
    rank_counts = Counter()

    for N in range(1, 10001):
        try:
            curves = P.ellsearch(N)
            if len(curves) == 0:
                continue
            total_curves += len(curves)
            for i in range(len(curves)):
                c = curves[i]
                label = str(c[0])
                ainvs = c[1]
                E = P.ellinit(ainvs)
                ar = P.ellanalyticrank(E)
                rank = int(ar[0])
                rank_counts[rank] += 1
                if rank == 2:
                    rank2_curves.append((label, ainvs, float(ar[1])))
        except Exception:
            pass

    t1 = time.time()
    print(f"  Total curves found: {total_curves}")
    print(f"  Rank distribution: {dict(rank_counts)}")
    print(f"  Rank 2 curves: {len(rank2_curves)}")
    print(f"  Time: {t1 - t0:.1f}s")
    print()

    # Step 2: Compute |Ш| for each rank 2 curve
    print("Phase 2: Computing |Ш| for all rank 2 curves...")

    results = []
    errors = []
    sha_dist = Counter()

    for idx, (label, ainvs, L_leading) in enumerate(rank2_curves):
        if (idx + 1) % 100 == 0:
            elapsed = time.time() - t1
            rate = (idx + 1) / elapsed if elapsed > 0 else 0
            print(f"  Progress: {idx + 1}/{len(rank2_curves)} ({rate:.1f} curves/s)")

        try:
            E = P.ellinit(ainvs)
            result = compute_sha(E, label)
            if result is None:
                errors.append({'label': label, 'error': 'not_rank_2'})
            elif 'error' in result:
                errors.append(result)
            else:
                results.append(result)
                sha_dist[result['sha']] += 1
        except Exception as e:
            errors.append({'label': label, 'error': str(e)})

    t2 = time.time()
    print(f"  Successfully computed |Ш|: {len(results)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Time: {t2 - t1:.1f}s")
    print()

    # Step 3: Analyze results
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()

    # Distribution of |Ш|
    print("|Ш| distribution:")
    for sha_val in sorted(sha_dist.keys()):
        count = sha_dist[sha_val]
        sqrt_v = math.isqrt(sha_val) if sha_val > 0 else 0
        is_sq = sqrt_v * sqrt_v == sha_val if sha_val > 0 else False
        sq_marker = f" = {sqrt_v}²" if is_sq else " (NOT a perfect square!)"
        print(f"  |Ш| = {sha_val:>6}: {count:>4} curves{sq_marker}")
    print()

    # Perfect square check
    non_squares = [r for r in results if not r['is_square']]
    print(f"Perfect square check:")
    print(f"  Curves with |Ш| a perfect square: {len(results) - len(non_squares)}/{len(results)}")
    if non_squares:
        print(f"  CURVES WITH |Ш| NOT A PERFECT SQUARE: {len(non_squares)}")
        for r in non_squares[:10]:
            print(f"    {r['label']}: |Ш| = {r['sha']}")
    print()

    # Accuracy check
    bad_accuracy = [r for r in results if r['sha_error'] > 0.1]
    print(f"Numerical accuracy:")
    print(f"  Curves with |Ш| error < 0.1: {len(results) - len(bad_accuracy)}/{len(results)}")
    if bad_accuracy:
        print(f"  Curves with large error: {len(bad_accuracy)}")
        for r in bad_accuracy[:10]:
            print(f"    {r['label']}: |Ш|_float = {r['sha_float']}, rounded = {r['sha']}, error = {r['sha_error']:.4f}")
    print()

    # Specific curves from the assignment
    print("Specific curves from the problem statement:")
    known = {'571a1': None, '571b1': None, '681c1': None, '882a1': None, '990c1': None,
             '389a1': None, '563a1': None}
    for r in results:
        if r['label'] in known:
            known[r['label']] = r
    for label, r in known.items():
        if r:
            print(f"  {label}: N={r['conductor']}, |Ш|={r['sha']}, sqrt(|Ш|)={r['sqrt_sha']}, "
                  f"tors={r['torsion']}, cp={r['prod_cp']}, reg={r['regulator']:.6f}")
    print()

    # Hypothesis test: |Ш| = 1 for all rank 2 curves?
    sha1_count = sha_dist.get(1, 0)
    print("=" * 70)
    print("HYPOTHESIS TEST: |Ш| = 1 for all rank 2 curves with N ≤ 10000")
    print("=" * 70)
    print()
    if sha1_count == len(results):
        print(f"  ✓ HYPOTHESIS CONFIRMED: All {len(results)} rank 2 curves have |Ш| = 1")
    else:
        print(f"  ✗ HYPOTHESIS REFUTED: {sha1_count}/{len(results)} curves have |Ш| = 1")
        print(f"  Other values: {dict(Counter({k: v for k, v in sha_dist.items() if k != 1}))}")
        # Show curves with |Ш| > 1
        non_trivial = [r for r in results if r['sha'] != 1]
        print(f"  Curves with |Ш| > 1:")
        for r in sorted(non_trivial, key=lambda x: (x['conductor'], x['label']))[:30]:
            print(f"    {r['label']}: N={r['conductor']}, |Ш|={r['sha']}, "
                  f"tors={r['torsion']}, cp={r['prod_cp']}, reg={r['regulator']:.6f}")
    print()

    # Summary statistics
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"  Conductor bound: 10000")
    print(f"  Total elliptic curves: {total_curves}")
    print(f"  Rank 0 curves: {rank_counts[0]}")
    print(f"  Rank 1 curves: {rank_counts[1]}")
    print(f"  Rank 2 curves: {rank_counts[2]}")
    print(f"  Rank 3+ curves: {sum(v for k, v in rank_counts.items() if k >= 3)}")
    print(f"  Rank 2 curves with |Ш| computed: {len(results)}")
    print(f"  Rank 2 curves with |Ш| = 1: {sha1_count}")
    print(f"  All |Ш| perfect squares: {len(non_squares) == 0}")
    print(f"  Total computation time: {t2 - t0:.1f}s")
    print()

    # Save results
    output = {
        'parameters': {
            'conductor_bound': 10000,
            'target_rank': 2,
            'method': 'BSD formula via PARI/GP',
            'formula': "|Ш| = L^(r)(E,1) / (r! * ellbsd(E) * Regulator)",
        },
        'summary': {
            'total_curves': total_curves,
            'rank_distribution': dict(rank_counts),
            'rank2_count': len(rank2_curves),
            'sha_computed': len(results),
            'sha_errors': len(errors),
            'sha_distribution': dict(sha_dist),
            'sha1_count': sha1_count,
            'all_perfect_squares': len(non_squares) == 0,
            'hypothesis_confirmed': sha1_count == len(results),
            'computation_time_seconds': round(t2 - t0, 1),
        },
        'results': results,
        'errors': errors[:50],  # Cap errors for file size
    }

    outfile = 'computation/cycle3_sha_exhaust.json'
    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"Results saved to {outfile}")


if __name__ == '__main__':
    main()
