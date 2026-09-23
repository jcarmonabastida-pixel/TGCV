#!/usr/bin/env python3
"""TR-131 deterministic secondary analysis runner.

This runner does not reconstruct source-domain semantics. It consumes a frozen,
normalized evidence package and derives only the descriptors frozen by the
Cross-Domain Comparison Protocol.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

PROTOCOL = "TR131_CROSS_DOMAIN_COMPARISON_PROTOCOL_FREEZE_001"
REQUIRED = ("domain","record_id","S_t","T_acc_t","T_real_t","S_t1","T_acc_t1")

def canonical(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256(v):
    return hashlib.sha256(canonical(v).encode("utf-8")).hexdigest()

def ids(tacc):
    out = []
    for item in tacc:
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, dict) and "id" in item:
            out.append(item["id"])
        else:
            raise ValueError("invalid transformation identity")
    if len(out) != len(set(out)):
        raise ValueError("duplicate transformation identity")
    return tuple(sorted(out))

def derive(record):
    missing = [k for k in REQUIRED if k not in record]
    if missing:
        raise ValueError("MISSING_REQUIRED_FIELDS:" + ",".join(missing))
    t0, t1 = set(ids(record["T_acc_t"])), set(ids(record["T_acc_t1"]))
    added, removed = sorted(t1-t0), sorted(t0-t1)
    retained = sorted(t0&t1)
    a0, a1 = len(t0), len(t1)
    g, l, p = len(added), len(removed), len(retained)
    assert a1 == p + g
    assert a0 == p + l
    assert a1-a0 == g-l
    classes = []
    if g: classes.append("EXPANSION")
    if l: classes.append("CONTRACTION")
    if g or l: classes.append("TURNOVER")
    if p: classes.append("PERSISTENCE")
    if not g and not l: classes.append("STABILITY")
    return {
        "domain": record["domain"], "record_id": record["record_id"],
        "A_t": a0, "A_t1": a1, "G": g, "L": l, "P": p, "R": g+l, "D": a1-a0,
        "Added": added, "Removed": removed, "Retained": retained,
        "FPE": classes, "T_real_t": record["T_real_t"],
        "source_trace_hash": sha256({
            "S_t":record["S_t"],"T_acc_t":ids(record["T_acc_t"]),
            "T_real_t":record["T_real_t"],"S_t1":record["S_t1"],
            "T_acc_t1":ids(record["T_acc_t1"])
        })
    }

def analyze(package):
    if package.get("protocol") != PROTOCOL:
        raise ValueError("PROTOCOL_MISMATCH")
    records = package.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("NO_RECORDS")
    derived = [derive(r) for r in records]
    domains = sorted({r["domain"] for r in derived})
    summary = {}
    for d in domains:
        rows = [r for r in derived if r["domain"] == d]
        summary[d] = {
            "records": len(rows),
            "mean_A_t": sum(r["A_t"] for r in rows)/len(rows),
            "mean_A_t1": sum(r["A_t1"] for r in rows)/len(rows),
            "expansion_records": sum("EXPANSION" in r["FPE"] for r in rows),
            "contraction_records": sum("CONTRACTION" in r["FPE"] for r in rows),
            "turnover_records": sum("TURNOVER" in r["FPE"] for r in rows),
            "stability_records": sum("STABILITY" in r["FPE"] for r in rows),
        }
    result = {
        "record_type":"TGCV_TR131_CROSS_DOMAIN_COMPARISON_ANALYSIS",
        "protocol":PROTOCOL, "domains":domains,
        "record_count":len(derived), "derived":derived, "summary":summary,
        "output_sha256":sha256(derived)
    }
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input",type=Path)
    ap.add_argument("-o","--output",type=Path,required=True)
    args=ap.parse_args()
    package=json.loads(args.input.read_text(encoding="utf-8"))
    result=analyze(package)
    args.output.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":"ANALYSIS_COMPLETED","record_count":result["record_count"],"output_sha256":result["output_sha256"]}))
if __name__=="__main__":
    main()
