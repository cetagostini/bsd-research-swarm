#!/usr/bin/env python3
"""PhdMath advisory search: rank-2 curves in the Cremona database (PARI elldata)
whose *analytic* |Ш| is integral and >= 9 (and in particular ODD).

Motivation: SHA_LIFT_RESEARCH.md / SHA_LIFT_REVIEW.md assert that "no rank-2
curve with analytic |Ш| >= 9 exists in LMFDB", hence no empirical testbed for
the p^4 dichotomy branch or the odd-primary direction. This script tests that
claim against the OFFLINE Cremona database (PARI elldata, conductors <= ~400k),
which needs no network access at all.

Method (all PARI, no network):
  - forell over conductor chunks; forell binds E to [label, ainvs, ...]
  - ellrootno == 1 (parity => even analytic rank)
  - ellrank(E,2): keep curves with r2 == 2 and r1 == r2 (certified rank 2)
  - ellanalyticrank(E) == [2, L'']; ellbsd(E) = c with L''(1)/2! = c*Reg*|Ш|_an
  - |Ш|_an = ar[2]/2/(c*Reg); keep if integral; record >= 9 separately
Output: computation/phdmath_oddsha_search.json
"""
import json
import sys
import time

from cypari2 import Pari

CHUNK = 25_000
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 400_000

GP = r"""
proc(E, ~st) =
{
  my(Ei = ellinit(E[2]), r, ar, c, Rg, sha, s);
  if(ellrootno(Ei) != 1, return);
  r = ellrank(Ei, 2);
  if(r[2] != 2, return);
  st[1] = st[1] + 1;
  if(r[1] != 2, return);
  st[2] = st[2] + 1;
  ar = ellanalyticrank(Ei);
  if(ar[1] != 2, return);
  c = ellbsd(Ei);
  Rg = matdet(ellheightmatrix(Ei, r[4]));
  sha = ar[2]/2/(c*Rg);
  if(abs(sha - round(sha)) > 0.0001, return);
  st[3] = st[3] + 1;
  s = round(sha);
  st[4] = concat(st[4], [Str(E[1]), Str(s)]);
};
"""


def main() -> None:
    pari = Pari()
    pari.allocatemem(512 * 10**6)
    pari(GP)
    n2 = ncert = nint = 0
    hist: dict[int, int] = {}
    ge9: list = []
    t0 = time.time()
    lo = 2
    while lo <= LIMIT:
        hi = min(lo + CHUNK - 1, LIMIT)
        out = pari(f"st=[0,0,0,[]]; forell(E,{lo},{hi}, proc(E,st)); st")
        n2 += int(str(out[0]))
        ncert += int(str(out[1]))
        nint += int(str(out[2]))
        flat = [str(x) for x in out[3]]
        for i in range(0, len(flat), 2):
            lab, s = flat[i], int(flat[i + 1])
            hist[s] = hist.get(s, 0) + 1
            if s >= 9:
                ge9.append([lab, s])
        print(f"[{time.time()-t0:6.0f}s] {lo}-{hi}: n2={n2} cert={ncert} "
              f"integral={nint} ge9={len(ge9)}", flush=True)
        lo = hi + 1

    result = {
        "note": ("Cremona elldata via PARI forell; conductors 2..%d; certified "
                 "rank 2 (r1=r2=2); |Ш|_an = L''(1)/2!/(ellbsd*Reg); only "
                 "integral values recorded" % LIMIT),
        "n_r2_2": n2,
        "n_certified": ncert,
        "n_integral_sha": nint,
        "hist": sorted(hist.items()),
        "ge9": ge9,
        "ge9_odd": [p for p in ge9 if p[1] % 2 == 1],
    }
    with open("computation/phdmath_oddsha_search.json", "w") as f:
        json.dump(result, f, indent=1)
    print("WROTE computation/phdmath_oddsha_search.json")
    print(json.dumps({k: result[k] for k in
                      ("n_r2_2", "n_certified", "n_integral_sha", "hist")}))
    print("ge9 count:", len(ge9), " odd:", len(result["ge9_odd"]))


if __name__ == "__main__":
    main()
