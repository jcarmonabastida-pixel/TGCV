#!/usr/bin/env python3
"""TGCV TR-131 A6 Executor-1: PRISM leader_sync3_2 reconstruction.

Independent implementation. Reads the frozen PRISM fixture text, validates its
SHA-256, and reconstructs the bounded operational subgraph required by A6.
"""
from __future__ import annotations
import argparse, hashlib, json
from itertools import product
from pathlib import Path

EXPECTED_SHA = "8335ac3258dc457cb0d486fd8b774826799b87c81d65f15a5ae23696d7f2f43e"

def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def state(**kw):
    return tuple(sorted(kw.items()))

def acc(s):
    d = dict(s)
    out = []
    if d["s1"] == 0:
        out.append("pick")
    if d["s1"] == 1:
        out.append("read")
    if d["s1"] == 2:
        out.append("done" if (d["u1"] or d["u2"] or d["u3"]) else "retry")
    if d["s1"] == 3:
        out.append("loop")
    return tuple(sorted(set(out)))

def next_pick(s, bits):
    d = dict(s)
    for i, b in enumerate(bits, 1):
        d[f"s{i}"] = 1; d[f"p{i}"] = b; d[f"v{i}"] = b; d[f"u{i}"] = True
    return state(**d)

def next_read(s):
    d = dict(s)
    vals = [d["v2"], d["v3"], d["v1"]]
    for i, v in enumerate(vals, 1):
        d[f"u{i}"] = (d[f"p{i}"] != v)
        d[f"v{i}"] = v
    d["c"] = 2
    d["s1"] = d["s2"] = d["s3"] = 2
    d["v1"] = d["v2"] = d["v3"] = 0
    d["p1"] = d["p2"] = d["p3"] = 0
    return state(**d)

def apply_terminal(s, action):
    d = dict(s)
    if action == "retry":
        d.update(s1=0,s2=0,s3=0,u1=False,u2=False,u3=False,
                 v1=0,v2=0,v3=0,p1=0,p2=0,p3=0,c=1)
    else:
        d.update(s1=3,s2=3,s3=3,u1=False,u2=False,u3=False,
                 v1=0,v2=0,v3=0,p1=0,p2=0,p3=0)
    return state(**d)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fixture", type=Path)
    ap.add_argument("-o", "--output", type=Path, required=True)
    a = ap.parse_args()
    digest = sha256(a.fixture)
    if digest != EXPECTED_SHA:
        raise SystemExit(f"FIXTURE_SHA_MISMATCH expected={EXPECTED_SHA} actual={digest}")
    s0 = state(c=1, s1=0,s2=0,s3=0, u1=False,u2=False,u3=False,
               v1=0,v2=0,v3=0,p1=0,p2=0,p3=0)
    rows = [{"kind":"state","id":"S0","state":s0,"t_acc":acc(s0)}]
    for bits in product((0,1), repeat=3):
        s1 = next_pick(s0,bits)
        rows.append({"kind":"realization","source":"S0","transformation":"pick",
                     "realization":bits,"successor":s1,"t_acc":acc(s1)})
        s2 = next_read(s1)
        rows.append({"kind":"transition","source":s1,"transformation":"read",
                     "successor":s2,"t_acc":acc(s2)})
        branch = "done" if any(dict(s2)[f"u{i}"] for i in range(1,4)) else "retry"
        s3 = apply_terminal(s2,branch)
        rows.append({"kind":"transition","source":s2,"transformation":branch,
                     "successor":s3,"t_acc":acc(s3)})
    result = {"executor":"EXECUTOR_1","fixture_sha256":digest,"rows":rows}
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2),encoding="utf-8")
if __name__ == "__main__":
    main()
