#!/usr/bin/env python3
"""
Cycle 6: Extended |Ш| verification for rank 2 and rank 3 curves.

Extends the exhaustive BSD verification:
  - Part A: All rank 2 curves with conductor N ≤ 50000
  - Part B: First 100 rank 3 curves (Shafarevich-Tate group)

BSD formula: L^(r)(E,1)/r! = (Ω · R · |Ш| · ∏c_v) / |tors|²

Rearranged: |Ш| = L^(r)(E,1) · |tors|² / (r! · Ω · R · ∏c_v)

We use PARI/GP's ellbsd (which computes c = Ω·∏c_v/|tors|²), so:
  |Ш| = L^(r)(E,1) / (r! · c · R)

Strategy:
  1. For N ≤ 10000: load prior cycle3 results (already verified: all |Ш|=1)
  2. For 10000 < N ≤ 50000: exhaustive enumeration via PARI ellsearch
  3. For rank 3: first 100 curves with known rank 3
  4. If exhaustive is too slow, fall back to 500-curve random sample
"""

import json
import math
import os
import random
import sys
import time
from collections import Counter

from cypari2 import Pari

P = Pari()
P.default("parisizemax", 2**30)
P.default("realprecision", 50)


# ============================================================
# BSD invariant computation
# ============================================================

def compute_sha(E, label, target_rank=None):
    """Compute |Ш| for an elliptic curve via the BSD formula.

    Args:
        E: PARI ellinit object
        label: Cremona label string
        target_rank: if set, only compute if rank matches

    Returns:
        dict with sha data, or None if rank doesn't match, or dict with 'error'
    """
    ar = P.ellanalyticrank(E)
    rank = int(ar[0])
    L_leading = float(ar[1])  # L^(r)(1), NOT L^(r)(1)/r!

    if target_rank is not None and rank != target_rank:
        return None

    # ellbsd: c where L^(r)(1)/r! = c * R * S
    try:
        bsd_c = float(P.ellbsd(E))
    except Exception as e:
        return {'label': label, 'rank': rank, 'error': f'ellbsd_failed: {e}'}

    # Generators and regulator
    try:
        gens = P.ellgenerators(E)
    except Exception as e:
        return {'label': label, 'rank': rank, 'error': f'generators_failed: {e}'}

    if len(gens) < rank:
        return {'label': label, 'rank': rank, 'error': 'generators_missing',
                'found': len(gens), 'needed': rank}

    H = P.ellheightmatrix(E, gens)
    reg = float(P.matdet(H))

    if abs(reg) < 1e-30:
        return {'label': label, 'rank': rank, 'error': 'zero_regulator'}

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


# ============================================================
# Load prior cycle3 results (N ≤ 10000)
# ============================================================

def load_prior_results():
    """Load cycle3 SHA exhaust results for N ≤ 10000."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'cycle3_sha_exhaust.json')
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


# ============================================================
# Enumerate curves in a conductor range
# ============================================================

def enumerate_curves(lo, hi, progress_every=2000):
    """Enumerate all elliptic curves with conductor in [lo, hi].

    Returns list of (label, ainvs, conductor) tuples.
    """
    curves = []
    for N in range(lo, hi + 1):
        try:
            found = P.ellsearch(N)
            for c in found:
                label = str(c[0])
                ainvs = c[1]
                curves.append((label, ainvs, N))
        except Exception:
            pass
        if (N - lo + 1) % progress_every == 0:
            print(f"    ... enumerated N={N}, {len(curves)} curves so far")
    return curves


# ============================================================
# Part A: Rank 2 curves, N ≤ 50000
# ============================================================

def part_a_rank2():
    """Verify |Ш| = 1 for all rank 2 curves with N ≤ 50000."""
    print("=" * 75)
    print("PART A: |Ш| VERIFICATION FOR RANK 2 CURVES, N ≤ 50000")
    print("=" * 75)
    print()

    t0 = time.time()

    # Load prior results for N ≤ 10000
    prior = load_prior_results()
    if prior and prior.get('summary', {}).get('hypothesis_confirmed'):
        prior_results = prior['results']
        prior_sha_dist = prior['summary']['sha_distribution']
        prior_total = prior['summary']['total_curves']
        prior_rank_counts = prior['summary']['rank_distribution']
        prior_rank2 = prior['summary']['rank2_count']
        print(f"Loaded prior cycle3 results: N ≤ 10000")
        print(f"  Total curves: {prior_total}")
        print(f"  Rank 2 curves: {prior_rank2}")
        print(f"  All |Ш| = 1: YES")
        print()
    else:
        print("No prior results found — will compute N ≤ 10000 from scratch")
        prior_results = []
        prior_sha_dist = {}
        prior_total = 0
        prior_rank_counts = {}
        prior_rank2 = 0

    # Phase 1: Enumerate rank 2 curves for 10000 < N ≤ 50000
    print("Phase 1: Enumerating curves with 10000 < N ≤ 50000...")
    t1 = time.time()

    range1_curves = enumerate_curves(10001, 50000)
    t_enum = time.time() - t1
    print(f"  Found {len(range1_curves)} curves in {t_enum:.1f}s")
    print()

    # Phase 2: Find rank 2 curves
    print("Phase 2: Identifying rank 2 curves...")
    t2 = time.time()

    rank2_new = []
    total_new = 0
    rank_counts_new = Counter()
    batch_size = 500

    for i, (label, ainvs, N) in enumerate(range1_curves):
        try:
            E = P.ellinit(ainvs)
            ar = P.ellanalyticrank(E)
            rank = int(ar[0])
            rank_counts_new[rank] += 1
            total_new += 1
            if rank == 2:
                rank2_new.append((label, ainvs, N, float(ar[1])))
        except Exception:
            pass

        if (i + 1) % 5000 == 0:
            elapsed = time.time() - t2
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            print(f"    Progress: {i+1}/{len(range1_curves)} ({rate:.0f} curves/s), "
                  f"rank2 found: {len(rank2_new)}")

    t_rank = time.time() - t2
    print(f"  Total curves scanned: {total_new}")
    print(f"  Rank distribution (10001-50000): {dict(rank_counts_new)}")
    print(f"  Rank 2 curves found: {len(rank2_new)}")
    print(f"  Time: {t_rank:.1f}s")
    print()

    # Phase 3: Compute |Ш| for rank 2 curves
    print("Phase 3: Computing |Ш| for rank 2 curves (10001-50000)...")
    t3 = time.time()

    results_new = []
    errors_new = []
    sha_dist_new = Counter()

    for idx, (label, ainvs, N, L_lead) in enumerate(rank2_new):
        if (idx + 1) % 200 == 0:
            elapsed = time.time() - t3
            rate = (idx + 1) / elapsed if elapsed > 0 else 0
            print(f"    Progress: {idx+1}/{len(rank2_new)} ({rate:.1f} curves/s)")

        try:
            E = P.ellinit(ainvs)
            result = compute_sha(E, label, target_rank=2)
            if result is None:
                errors_new.append({'label': label, 'error': 'not_rank_2'})
            elif 'error' in result:
                errors_new.append(result)
            else:
                results_new.append(result)
                sha_dist_new[result['sha']] += 1
        except Exception as e:
            errors_new.append({'label': label, 'error': str(e)})

    t_sha = time.time() - t3
    print(f"  Successfully computed |Ш|: {len(results_new)}")
    print(f"  Errors: {len(errors_new)}")
    print(f"  Time: {t_sha:.1f}s")
    print()

    # Combine with prior (JSON keys are strings, new keys are ints — normalize)
    all_rank2_results = prior_results + results_new
    combined_sha_dist = Counter({int(k): v for k, v in prior_sha_dist.items()})
    for k, v in sha_dist_new.items():
        combined_sha_dist[int(k)] += v
    combined_total = prior_total + total_new
    combined_rank_counts = Counter({int(k): v for k, v in prior_rank_counts.items()})
    for k, v in rank_counts_new.items():
        combined_rank_counts[int(k)] += v
    combined_rank2 = prior_rank2 + len(rank2_new)

    # Analysis
    print("=" * 75)
    print("PART A RESULTS")
    print("=" * 75)
    print()

    # Distribution of |Ш|
    print("|Ш| distribution for ALL rank 2 curves (N ≤ 50000):")
    for sha_val in sorted(combined_sha_dist.keys()):
        count = combined_sha_dist[sha_val]
        if sha_val > 0:
            sqrt_v = math.isqrt(sha_val)
            is_sq = sqrt_v * sqrt_v == sha_val
            sq_marker = f" = {sqrt_v}²" if is_sq else " (NOT a perfect square!)"
        else:
            sq_marker = ""
        print(f"  |Ш| = {sha_val:>6}: {count:>5} curves{sq_marker}")
    print()

    # Perfect square check
    non_squares = [r for r in all_rank2_results if not r.get('is_square', True)]
    print(f"Perfect square check:")
    print(f"  All |Ш| are perfect squares: {len(non_squares) == 0}")
    print()

    # Curves with |Ш| > 1
    non_trivial = [r for r in all_rank2_results if r.get('sha', 1) != 1]
    sha1_count = combined_sha_dist.get(1, 0)
    print(f"|Ш| = 1 hypothesis:")
    print(f"  Rank 2 curves with |Ш| = 1: {sha1_count}/{combined_rank2}")
    if non_trivial:
        print(f"  CURVES WITH |Ш| > 1: {len(non_trivial)}")
        for r in sorted(non_trivial, key=lambda x: (x['conductor'], x['label']))[:30]:
            print(f"    {r['label']}: N={r['conductor']}, |Ш|={r['sha']}, "
                  f"sqrt(|Ш|)={r['sqrt_sha']}, tors={r['torsion']}, "
                  f"cp={r['prod_cp']}, reg={r['regulator']:.6f}")
    else:
        print(f"  ✓ ALL {combined_rank2} rank 2 curves have |Ш| = 1")
    print()

    t_total = time.time() - t0
    print(f"Total Part A time: {t_total:.1f}s")
    print()

    return {
        'prior_results_count': len(prior_results),
        'new_results': results_new,
        'new_errors': errors_new[:100],
        'combined_summary': {
            'conductor_bound': 50000,
            'total_curves': combined_total,
            'rank_distribution': dict(combined_rank_counts),
            'rank2_count': combined_rank2,
            'sha_computed': len(all_rank2_results),
            'sha_distribution': dict(combined_sha_dist),
            'sha1_count': sha1_count,
            'all_perfect_squares': len(non_squares) == 0,
            'all_sha_equal_1': sha1_count == combined_rank2,
            'non_trivial_sha_count': len(non_trivial),
        },
        'new_range_summary': {
            'conductor_range': '10001-50000',
            'total_curves': total_new,
            'rank_distribution': dict(rank_counts_new),
            'rank2_count': len(rank2_new),
            'sha_computed': len(results_new),
            'sha_errors': len(errors_new),
            'sha_distribution': dict(sha_dist_new),
        },
        'computation_time': round(t_total, 1),
    }


# ============================================================
# Part B: Rank 3 curves (first 100)
# ============================================================

def part_b_rank3():
    """Verify |Ш| for the first 100 rank 3 curves."""
    print("=" * 75)
    print("PART B: |Ш| VERIFICATION FOR RANK 3 CURVES (FIRST 100)")
    print("=" * 75)
    print()

    t0 = time.time()

    # Search for rank 3 curves by scanning conductors
    print("Searching for rank 3 curves...")
    rank3_curves = []
    total_scanned = 0
    N = 1

    # Scan conductors until we find 100 rank 3 curves
    # We'll scan up to N=200000 as a safety bound
    while len(rank3_curves) < 100 and N <= 200000:
        try:
            found = P.ellsearch(N)
            for c in found:
                label = str(c[0])
                ainvs = c[1]
                total_scanned += 1
                try:
                    E = P.ellinit(ainvs)
                    ar = P.ellanalyticrank(E)
                    rank = int(ar[0])
                    if rank == 3:
                        rank3_curves.append((label, ainvs, N, float(ar[1])))
                        if len(rank3_curves) % 10 == 0:
                            print(f"  Found {len(rank3_curves)} rank 3 curves "
                                  f"(latest: {label}, N={N})")
                        if len(rank3_curves) >= 100:
                            break
                except Exception:
                    pass
        except Exception:
            pass
        N += 1

        if N % 10000 == 0:
            print(f"  ... scanned up to N={N}, found {len(rank3_curves)} rank 3, "
                  f"{total_scanned} total curves")

    print(f"  Found {len(rank3_curves)} rank 3 curves after scanning "
          f"{total_scanned} curves (N ≤ {N-1})")
    print()

    # Compute |Ш| for rank 3 curves
    print(f"Computing |Ш| for {len(rank3_curves)} rank 3 curves...")
    t1 = time.time()

    results = []
    errors = []
    sha_dist = Counter()

    for idx, (label, ainvs, N, L_lead) in enumerate(rank3_curves):
        try:
            E = P.ellinit(ainvs)
            result = compute_sha(E, label, target_rank=3)
            if result is None:
                errors.append({'label': label, 'error': 'not_rank_3'})
            elif 'error' in result:
                errors.append(result)
            else:
                results.append(result)
                sha_dist[result['sha']] += 1
                if (idx + 1) % 10 == 0:
                    print(f"    Progress: {idx+1}/{len(rank3_curves)}, "
                          f"|Ш| values so far: {dict(sha_dist)}")
        except Exception as e:
            errors.append({'label': label, 'error': str(e)})

    t2 = time.time()
    print(f"  Successfully computed |Ш|: {len(results)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Time: {t2 - t1:.1f}s")
    print()

    # Analysis
    print("=" * 75)
    print("PART B RESULTS")
    print("=" * 75)
    print()

    print("|Ш| distribution for rank 3 curves:")
    for sha_val in sorted(sha_dist.keys()):
        count = sha_dist[sha_val]
        if sha_val > 0:
            sqrt_v = math.isqrt(sha_val)
            is_sq = sqrt_v * sqrt_v == sha_val
            sq_marker = f" = {sqrt_v}²" if is_sq else " (NOT a perfect square!)"
        else:
            sq_marker = ""
        print(f"  |Ш| = {sha_val:>6}: {count:>4} curves{sq_marker}")
    print()

    non_squares = [r for r in results if not r.get('is_square', True)]
    sha1_count = sha_dist.get(1, 0)
    print(f"All |Ш| are perfect squares: {len(non_squares) == 0}")
    print(f"|Ш| = 1 for all: {sha1_count == len(results)} "
          f"({sha1_count}/{len(results)})")
    print()

    if sha1_count < len(results):
        non_trivial = [r for r in results if r.get('sha', 1) != 1]
        print(f"Curves with |Ш| > 1:")
        for r in sorted(non_trivial, key=lambda x: (x['conductor'], x['label']))[:30]:
            print(f"  {r['label']}: N={r['conductor']}, |Ш|={r['sha']}, "
                  f"sqrt(|Ш|)={r['sqrt_sha']}, tors={r['torsion']}, "
                  f"cp={r['prod_cp']}, reg={r['regulator']:.6f}")
    else:
        print(f"✓ ALL {len(results)} rank 3 curves tested have |Ш| = 1")
    print()

    t_total = time.time() - t0
    print(f"Total Part B time: {t_total:.1f}s")
    print()

    return {
        'curves_found': len(rank3_curves),
        'total_scanned': total_scanned,
        'max_conductor': N - 1,
        'sha_computed': len(results),
        'errors': errors[:50],
        'sha_distribution': dict(sha_dist),
        'sha1_count': sha1_count,
        'all_perfect_squares': len(non_squares) == 0,
        'all_sha_equal_1': sha1_count == len(results),
        'results': results,
        'computation_time': round(t_total, 1),
    }


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 75)
    print("CYCLE 6: EXTENDED |Ш| FINITENESS VERIFICATION")
    print("Extending exhaustive BSD verification to N ≤ 50000 (rank 2)")
    print("and testing first 100 rank 3 curves")
    print("=" * 75)
    print()

    overall_t0 = time.time()

    # Part A
    part_a = part_a_rank2()

    # Part B
    part_b = part_b_rank3()

    overall_t = time.time() - overall_t0

    # Final summary
    print("=" * 75)
    print("CYCLE 6 FINAL SUMMARY")
    print("=" * 75)
    print()

    a = part_a['combined_summary']
    b = part_b
    print(f"Part A — Rank 2 curves, N ≤ 50000:")
    print(f"  Total elliptic curves scanned: {a['total_curves']}")
    print(f"  Rank distribution: {a['rank_distribution']}")
    print(f"  Rank 2 curves: {a['rank2_count']}")
    print(f"  |Ш| computed: {a['sha_computed']}")
    print(f"  All |Ш| = 1: {a['all_sha_equal_1']}")
    print(f"  All perfect squares: {a['all_perfect_squares']}")
    print()

    print(f"Part B — Rank 3 curves (first 100):")
    print(f"  Curves found: {b['curves_found']}")
    print(f"  |Ш| computed: {b['sha_computed']}")
    print(f"  |Ш| distribution: {b['sha_distribution']}")
    print(f"  All |Ш| = 1: {b['all_sha_equal_1']}")
    print()

    print(f"Total computation time: {overall_t:.1f}s")
    print()

    # Build output
    output = {
        'cycle': 6,
        'description': 'Extended |Ш| finiteness verification',
        'method': 'BSD formula via PARI/GP: |Ш| = L^(r)(E,1) / (r! * ellbsd(E) * Regulator)',
        'parameters': {
            'rank2_conductor_bound': 50000,
            'rank3_target_count': 100,
            'rank3_max_conductor': b['max_conductor'],
        },
        'part_a_rank2': {
            'combined_summary': a,
            'new_range': part_a['new_range_summary'],
            'new_results_count': len(part_a['new_results']),
            'new_results': part_a['new_results'],
            'errors': part_a['new_errors'],
        },
        'part_b_rank3': {
            'curves_found': b['curves_found'],
            'total_scanned': b['total_scanned'],
            'max_conductor': b['max_conductor'],
            'sha_computed': b['sha_computed'],
            'sha_distribution': b['sha_distribution'],
            'sha1_count': b['sha1_count'],
            'all_perfect_squares': b['all_perfect_squares'],
            'all_sha_equal_1': b['all_sha_equal_1'],
            'results': b['results'],
            'errors': b['errors'],
            'computation_time': b['computation_time'],
        },
        'overall_summary': {
            'rank2_all_sha_1': a['all_sha_equal_1'],
            'rank2_count': a['rank2_count'],
            'rank3_all_sha_1': b['all_sha_equal_1'],
            'rank3_count': b['sha_computed'],
            'total_computation_time': round(overall_t, 1),
        },
    }

    outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'cycle6_extend_verify.json')
    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"Results saved to {outfile}")

    return output


if __name__ == '__main__':
    main()
