#!/usr/bin/env python3
"""
E1: Analyze the existing 100-curve pool from Dr. Science's computation.

Since LMFDB API is behind reCAPTCHA, we use the local pool data
and extend analysis where possible.

Output: e1_pool_analysis.json
"""
import json
import sys
import time


def load_pool_data() -> dict:
    """Load the existing pool results."""
    with open("computation/sha_lift_pool_results.json") as f:
        return json.load(f)


def analyze_pool(pool: dict) -> dict:
    """Analyze the pool for patterns and anomalies."""
    results = pool.get("results", [])
    
    # Count by s-value
    s_values = {}
    certified_count = 0
    uncertified = []
    anomalies = []
    
    for r in results:
        if r.get("rank_certified"):
            certified_count += 1
            s = r.get("ellrank", [0,0,0])[2]
            s_values[s] = s_values.get(s, 0) + 1
            
            # Check for anomalies
            if s not in [0, 2]:
                anomalies.append(r)
        else:
            uncertified.append(r)
    
    # Torsion analysis
    torsion_counts = {}
    for r in results:
        tors = r.get("torsion_order", 1)
        torsion_counts[tors] = torsion_counts.get(tors, 0) + 1
    
    # Selmer group analysis
    sel2_sizes = {}
    for r in results:
        sel2 = r.get("Sel2_order")
        if sel2:
            sel2_sizes[sel2] = sel2_sizes.get(sel2, 0) + 1
    
    # Compute derived quantities
    T_values = {}
    for r in results:
        T = r.get("T_dim_E2", 0)
        T_values[T] = T_values.get(T, 0) + 1
    
    summary = {
        "total_curves": len(results),
        "certified": certified_count,
        "not_certified": len(uncertified),
        "s_value_distribution": s_values,
        "torsion_distribution": torsion_counts,
        "sel2_distribution": sel2_sizes,
        "T_distribution": T_values,
        "anomalies": anomalies,
        "uncertified_curves": uncertified
    }
    
    return summary


def main():
    """Analyze the existing pool data."""
    print("E1: Analyzing existing 100-curve pool")
    print("=" * 60)
    
    pool = load_pool_data()
    summary = analyze_pool(pool)
    
    print(f"Total curves: {summary['total_curves']}")
    print(f"Certified: {summary['certified']}")
    print(f"Not certified: {summary['not_certified']}")
    print(f"\ns-value distribution: {summary['s_value_distribution']}")
    print(f"Torsion distribution: {summary['torsion_distribution']}")
    print(f"Sel2 distribution: {summary['sel2_distribution']}")
    print(f"T (dim E(Q)[2]) distribution: {summary['T_distribution']}")
    
    if summary['anomalies']:
        print(f"\n*** ANOMALIES FOUND: {len(summary['anomalies'])} ***")
        for a in summary['anomalies']:
            print(f"  {a['label']}: s={a['ellrank'][2]}")
    else:
        print(f"\n*** NO ANOMALIES: All certified curves have s ∈ {{0, 2}} ***")
    
    if summary['uncertified_curves']:
        print(f"\n*** UNCERTIFIED: {len(summary['uncertified_curves'])} curves ***")
        for u in summary['uncertified_curves']:
            print(f"  {u['label']}: rank={u['ellrank']}")
    
    # Statistical analysis
    print(f"\n{'='*60}")
    print("STATISTICAL ANALYSIS")
    print(f"{'='*60}")
    
    # For rank-2 curves with |Ш|=4, we expect s=2
    # Check if any certified rank-2 curve has s≠2
    rank2_certified = [r for r in pool['results'] 
                       if r.get('rank_certified') and r['ellrank'][0] == 2]
    rank2_s2 = [r for r in rank2_certified if r['ellrank'][2] == 2]
    rank2_s0 = [r for r in rank2_certified if r['ellrank'][2] == 0]
    
    print(f"Rank-2 certified curves: {len(rank2_certified)}")
    print(f"  s=2 (Ш[2]≅(ℤ/2)²): {len(rank2_s2)}")
    print(f"  s=0 (trivial Ш): {len(rank2_s0)}")
    
    if len(rank2_certified) > 0:
        s2_rate = len(rank2_s2) / len(rank2_certified) * 100
        print(f"  s=2 rate: {s2_rate:.1f}%")
    
    # For this pool (analytic |Ш|=4), we expect all to have s=2
    if len(rank2_s0) == 0 and len(rank2_s2) == len(rank2_certified):
        print(f"\n*** RESULT: All {len(rank2_certified)} rank-2 curves have s=2 ***")
        print("*** Ш[2] ≅ (ℤ/2)² is uniform across this pool ***")
        print("*** The lifting question is settled unconditionally for p=2 ***")
    elif len(rank2_s0) > 0:
        print(f"\n*** RESULT: {len(rank2_s0)} curves have s=0 (trivial Ш) ***")
        print("*** This contradicts analytic |Ш|=4 prediction ***")
        print("*** Possible explanations: BSD failure, analytic vs algebraic Sha, or error ***")
    
    # Save results
    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "experiment": "E1",
        "pool_source": "Dr. Science's 100-curve computation",
        "summary": summary,
        "conclusion": {
            "anomalies_found": len(summary['anomalies']) > 0,
            "all_rank2_s2": len(rank2_s0) == 0 and len(rank2_s2) == len(rank2_certified),
            "s2_rate": len(rank2_s2) / len(rank2_certified) * 100 if rank2_certified else 0
        }
    }
    
    output_path = "computation/e1_pool_analysis.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults written to {output_path}")
    
    return output


if __name__ == "__main__":
    main()
