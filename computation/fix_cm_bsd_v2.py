#!/usr/bin/env python3
"""
Fix CM BSD computation: correct the normalization formula.

Per Mr. Genius's review:
- lfun(E,1,r) returns L^(r)(E,1) (raw derivative, NOT divided by r!)
- BSD formula: L^(r)(E,1)/r! = ellbsd(E) * Reg(E) * |Sha(E)|
- So BSD quotient = L^(r)(E,1) / (r! * ellbsd(E) * Reg(E))

Previous bug: raw_ratio = L_leading / (omega * regulator)
Missing: division by r! (factorial of rank)

NOTE: All "bsd_quotient" values are NUMERICAL estimates, NOT proven |Sha| orders.
"""
import json
import time
from math import factorial

try:
    from cypari2 import Pari
    HAS_PARI = True
except ImportError:
    HAS_PARI = False
    print("ERROR: cypari2 required")
    exit(1)


def safe_real(x):
    """Convert PARI value to float, handling complex numbers."""
    try:
        return float(x)
    except TypeError:
        # If complex, take real part
        return float(x.real())


def compute_bsd_ratio_correct(pari, ainvs):
    """
    Compute BSD quotient: L^(r)(E,1) / (r! * ellbsd(E) * Reg(E))
    
    This is the NUMERICAL BSD quotient, NOT a proven |Sha| value.
    Returns dict with all BSD components.
    """
    E = pari.ellinit(ainvs)
    
    # Get rank — check certification
    rank_data = pari.ellrank(E)
    rank_lower = int(rank_data[0])
    rank_upper = int(rank_data[1])
    if rank_lower != rank_upper:
        raise ValueError(f"Rank not certified: lower={rank_lower}, upper={rank_upper}")
    rank = rank_lower
    
    # Get L-function leading coefficient
    # lfun(E,1,r) returns L^(r)(E,1) (raw, not divided by r!)
    L_leading_raw = pari.lfun(E, 1, rank)
    L_leading = safe_real(L_leading_raw)
    
    # ellbsd(E) returns c where L^(r)(E,1)/r! = c * Reg(E) * |Sha(E)|
    ellbsd_raw = pari.ellbsd(E)
    ellbsd_val = safe_real(ellbsd_raw)
    
    # Get generators and regulator only when needed (rank > 0)
    # Rank 0: regulator = 1 unconditionally, no elldata dependency
    if rank > 0:
        gens = pari.ellgenerators(E)
        hmat = pari.ellheightmatrix(E, gens, precision=60)
        reg = safe_real(pari.matdet(hmat))
    else:
        reg = 1.0
    
    # Tamagawa product (for reporting)
    # Use ellglobalred for conductor, elllocalred for each bad prime
    globalred = pari.ellglobalred(E)
    N = int(globalred[0])
    
    # Get bad primes from conductor factorization
    tam = 1
    tam_details = []
    facN = pari.factor(N)
    for i in range(int(facN.matsize()[0])):
        p = int(facN[0][i])
        # elllocalred returns [conductor_exponent, kodaira_code, [c4,c6], tamagawa]
        lr = pari.elllocalred(E, p)
        kodaira = int(lr[1])
        cp = int(lr[3])
        tam *= cp
        tam_details.append({"p": p, "kodaira": kodaira, "tamagawa": cp})
    
    # Torsion
    tors = pari.elltors(E)
    tors_order = int(tors[0])
    tors_structure = [int(x) for x in tors[1]]
    
    # The correct formula:
    # |Sha| = L^(r)(E,1) / (r! * ellbsd(E) * Reg(E))
    denom = factorial(rank) * ellbsd_val * reg
    if abs(denom) < 1e-30:
        raise ValueError(f"Invalid regulator or ellbsd: denom={denom}")
    bsd_quotient = L_leading / denom
    
    return {
        "rank": rank,
        "L_leading": L_leading,
        "ellbsd": ellbsd_val,
        "regulator": reg,
        "bsd_quotient": bsd_quotient,  # L^(r)(1)/(r!*ellbsd*Reg); NOT proven |Sha|
        "conductor": N,
        "tamagawa_product": tam,
        "tam_details": tam_details,
        "torsion_order": tors_order,
        "torsion_structure": tors_structure
    }


def verify_controls(pari):
    """
    Verify the formula against Mr. Genius's control curves.
    """
    controls = [
        # (label, ainvs, expected_sha)
        # Verified with ellidentify: these are the correct Cremona labels
        ("11a1", [0, -1, 1, -10, -20], 1),  # NOT [0,-1,1,0,0] which is 11a3
        ("37a1", [0, 0, 1, -1, 0], 1),
        ("389a1", [0, 1, 1, -2, 0], 1),
    ]
    
    print("\n=== Control Verification ===")
    all_pass = True
    for label, ainvs, expected_sha in controls:
        result = compute_bsd_ratio_correct(pari, ainvs)
        sha_est = result["bsd_quotient"]
        ok = abs(sha_est - expected_sha) < 0.1
        status = "PASS" if ok else "FAIL"
        print(f"{label}: rank={result['rank']}, bsd_quotient={sha_est:.6f}, expected={expected_sha}, {status}")
        if not ok:
            all_pass = False
            print(f"  L_leading={result['L_leading']:.6f}, ellbsd={result['ellbsd']:.6f}, reg={result['regulator']:.6f}, r!={factorial(result['rank'])}")
    
    return all_pass


def compute_j1728_d68(pari):
    """
    Compute BSD data for j1728_d68: y^2 = x^3 + 68x
    Conductor 9248, Cremona 9248g2, CM by Q(i).
    
    NOTE: This is NOT the d=2 quadratic twist of 194040.cu1 (N1).
    N1 has ainvs [0,0,0,-1825528908,-30021416896912], conductor 1,552,320.
    This is the rank-2 CM curve for the Castella Track B audit.
    """
    print("\n=== j1728_d68: E: y^2 = x^3 + 68x (NOT the d=2 twist of N1) ===")
    # ainvs for y^2 = x^3 + 68x is [0, 0, 0, 68, 0]
    ainvs = [0, 0, 0, 68, 0]
    result = compute_bsd_ratio_correct(pari, ainvs)
    
    print(f"Conductor: {result['conductor']}")
    print(f"Rank: {result['rank']}")
    print(f"L^(r)(1): {result['L_leading']:.10f}")
    print(f"ellbsd(E): {result['ellbsd']:.10f}")
    print(f"Regulator: {result['regulator']:.10f}")
    print(f"BSD quotient (numerical): {result['bsd_quotient']:.6f}")
    print(f"Torsion order: {result['torsion_order']}")
    print(f"Tamagawa product: {result['tamagawa_product']}")
    
    # Per Mr. Genius: L''(1) = 9.59..., ellbsd = 2.58..., Reg = 1.85...
    # L''/(2*ellbsd*Reg) = 1
    print(f"\nVerification: L''(1) / (2! * ellbsd * Reg) = {result['L_leading'] / (2 * result['ellbsd'] * result['regulator']):.6f}")
    
    return result


def main():
    print("CM BSD Recomputation - Corrected Formula (v2)")
    print("=" * 50)
    
    pari = Pari()
    pari.default("parisizemax", 1 << 30)  # 1GB
    
    # First verify controls
    if not verify_controls(pari):
        print("\nERROR: Control verification failed!")
        return
    
    # Compute the key CM curve for Track B audit
    d68_result = compute_j1728_d68(pari)
    
    # Load CM curves
    curves_path = "computation/cm_rank2_curves.json"
    try:
        with open(curves_path) as f:
            curves = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: {curves_path} not found")
        return
    
    print(f"\nRecomputing BSD ratios for {len(curves)} CM curves...")
    
    results = []
    errors = []
    
    for i, curve in enumerate(curves):
        label = curve["label"]
        ainvs = curve["ainvs"]
        
        try:
            bsd = compute_bsd_ratio_correct(pari, ainvs)
            
            result = {
                "label": label,
                "cm_type": curve["cm_type"],
                "d": curve["d"],
                "conductor": bsd["conductor"],
                "ainvs": ainvs,
                "rank": bsd["rank"],
                "L_leading": round(bsd["L_leading"], 10),
                "ellbsd": round(bsd["ellbsd"], 10),
                "regulator": round(bsd["regulator"], 10),
                "tamagawa_product": bsd["tamagawa_product"],
                "tam_details": bsd["tam_details"],
                "torsion_order": bsd["torsion_order"],
                "torsion_structure": bsd["torsion_structure"],
                "bsd_quotient": round(bsd["bsd_quotient"], 6),
                "a5": curve.get("a5", 0),
                "ordinary_at_5": curve.get("ordinary_at_5", False)
            }
            
            results.append(result)
        except Exception as e:
            errors.append({"label": label, "error": str(e)})
        
        if (i + 1) % 20 == 0:
            print(f"  Processed {i + 1}/{len(curves)} curves...")
    
    # Save raw results
    raw_path = "computation/cm_bsd_raw_corrected.json"
    with open(raw_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved corrected raw data to {raw_path}")
    
    # Build candidates list for Track B: rank 2, ordinary at 5
    track_b_candidates = []
    for r in results:
        if r["rank"] == 2 and r["ordinary_at_5"]:
            track_b_candidates.append({
                "label": r["label"],
                "conductor": r["conductor"],
                "d": r["d"],
                "bsd_quotient": r["bsd_quotient"],
                "a5": r["a5"],
                "priority": "high" if r["conductor"] < 10000 else "medium"
            })
    
    # Sort by conductor
    track_b_candidates.sort(key=lambda x: x["conductor"])
    
    # Summary
    bsd_values = [r["bsd_quotient"] for r in results if r["rank"] == 2]
    rank_dist = {}
    for r in results:
        rank_dist[r["rank"]] = rank_dist.get(r["rank"], 0) + 1
    
    print(f"\n=== Summary ===")
    print(f"Total curves processed: {len(results)}")
    print(f"Errors: {len(errors)}")
    print(f"Rank distribution: {rank_dist}")
    if bsd_values:
        print(f"BSD quotients (rank 2): min={min(bsd_values):.4f}, max={max(bsd_values):.4f}, mean={sum(bsd_values)/len(bsd_values):.4f}")
    print(f"Track B candidates (rank 2, ordinary at 5): {len(track_b_candidates)}")
    
    if track_b_candidates:
        print("\nTop 5 Track B candidates:")
        for c in track_b_candidates[:5]:
            print(f"  {c['label']}: conductor={c['conductor']}, d={c['d']}, BSD quot~{c['bsd_quotient']:.2f}")
    
    # Save complete results
    complete_path = "computation/cm_bsd_complete_corrected.json"
    with open(complete_path, 'w') as f:
        json.dump({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_curves": len(results),
            "errors": len(errors),
            "rank_distribution": rank_dist,
            "track_b_candidates": track_b_candidates,
            "results": results,
            "error_details": errors
        }, f, indent=2)
    print(f"Saved complete results to {complete_path}")
    
    if errors:
        print(f"\nFirst 5 errors:")
        for e in errors[:5]:
            print(f"  {e['label']}: {e['error']}")
    
    print("\nDone!")


if __name__ == "__main__":
    main()
