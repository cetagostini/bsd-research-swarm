#!/usr/bin/env python3
"""Unconditional 2-descent (PARI ellrank) over the rank-2 analytic-|Ш|=4 pool.

For each curve: [r1, r2, s, pts] = ellrank(E, effort).
  - r1 == r2 certifies the rank (PARI doc: r1=r2 never holds if Ш has 4-torsion)
  - C = dim 2-Selmer = r2 + T + s  (T = dim E(Q)[2])
  - dim Ш[2] = C - T - r1 when rank certified
Prediction (CT + BSD-analytic-|Ш|=4): every curve gives r1==r2==2, s=2,
i.e. Ш[2] ~= (Z/2)^2 and no class lifts to Ш[4] (no 2-divisible classes).
Control: rank-0 curves with analytic |Ш|=4 must also give s=2 (Ш[2]=(Z/2)^2).
"""
import json, sys, time
from cypari2 import Pari

def gen_triples(rows):
    for row in rows:
        a = row["ainvs"]
        yield row["lmfdb_label"], row["conductor"], a

def main(path, limit, control):
    rows = json.load(open(path))
    if control:
        start = 0
    else:
        start = 0
    results = []
    pari = Pari()
    n = 0
    for lbl, cond, a in gen_triples(rows):
        if n >= limit: break
        n += 1
        t0 = time.time()
        rec = {"label": lbl, "conductor": cond, "ainvs": a}
        try:
            E = pari.ellinit(a)
            R = pari.ellrank(E, 3)
            rec["ellrank"] = [int(x) for x in (R[0], R[1], R[2])]
            rec["rank_certified"] = (int(R[0]) == int(R[1]))
            # T = dim E(Q)[2]: torsion structure from LMFDB not passed; compute via elltors
            tors = pari.elltors(E)[0]
            rec["torsion_order"] = int(tors)
            rec["ellapsed"] = round(time.time()-t0, 1)
        except Exception as e:
            rec["error"] = str(e)[:200]
            rec["ellapsed"] = round(time.time()-t0, 1)
        results.append(rec)
        print(f"{n:3d} {lbl:14s} {rec.get('ellrank','ERR')}", flush=True)
    out = {"pool": "rank2_sha4" if not control else "rank0_sha4",
           "n": len(results), "results": results}
    json.dump(out, open(sys.argv[3] if len(sys.argv)>3 else "/tmp/pool_descent_out.json","w"), indent=1)
    print("WROTE", len(results))

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), False)
