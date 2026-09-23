#!/usr/bin/env python3
"""TR-131 deterministic secondary-analysis runner v005."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
PROTOCOL="TR131_CROSS_DOMAIN_COMPARISON_PROTOCOL_FREEZE_001"
ALLOWED={"domain","record_id","S_t","T_acc_t","T_real_t","S_t1","T_acc_t1","trajectory_id","step"}
FORBIDDEN={"outcome","value","vsl","vsl_value","reward","performance","TI","transformational_intelligence","utility"}
def canon(v): return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def digest(v): return hashlib.sha256(canon(v).encode()).hexdigest()
def ids(x):
    out=[i if isinstance(i,str) else i["id"] for i in x]
    if len(out)!=len(set(out)): raise ValueError("DUPLICATE_TRANSFORMATION_IDENTITY")
    return tuple(sorted(out))
def derive(r):
    unknown=set(r)-ALLOWED
    if unknown:
        forbidden=unknown&FORBIDDEN
        if forbidden: raise ValueError("FORBIDDEN_OUTCOME_VALUE_FIELD:"+",".join(sorted(forbidden)))
        raise ValueError("UNAUTHORIZED_FIELD:"+",".join(sorted(unknown)))
    req=("domain","record_id","S_t","T_acc_t","T_real_t","S_t1","T_acc_t1")
    missing=[k for k in req if k not in r]
    if missing: raise ValueError("MISSING_REQUIRED_FIELDS:"+",".join(missing))
    a,b=set(ids(r["T_acc_t"])),set(ids(r["T_acc_t1"]))
    add,rem=sorted(b-a),sorted(a-b); keep=sorted(a&b)
    A,G,L,P=len(a),len(add),len(rem),len(keep)
    f=[]
    if G:f.append("EXPANSION")
    if L:f.append("CONTRACTION")
    if G or L:f.append("TURNOVER")
    if P:f.append("PERSISTENCE")
    if not G and not L:f.append("STABILITY")
    return {"domain":r["domain"],"record_id":r["record_id"],"S_t":r["S_t"],"T_acc_t":sorted(a),
            "T_real_t":r["T_real_t"],"S_t1":r["S_t1"],"T_acc_t1":sorted(b),
            "Delta_T_acc_t":{"Added":add,"Removed":rem},"H":[r["S_t"],r["T_real_t"],r["S_t1"]],
            "trajectory_id":r.get("trajectory_id"),"step":r.get("step"),"A_t":A,"A_t1":len(b),
            "G":G,"L":L,"P":P,"R":G+L,"D":len(b)-A,"Added":add,"Removed":rem,"Retained":keep,"FPE":f,
            "source_trace_hash":digest({"S_t":r["S_t"],"T_acc_t":sorted(a),"T_real_t":r["T_real_t"],"S_t1":r["S_t1"],"T_acc_t1":sorted(b)})}
def trajectory_analysis(rows):
    groups={}
    for r in rows:
        if r.get("trajectory_id") is not None: groups.setdefault((r["domain"],r["trajectory_id"]),[]).append(r)
    for v in groups.values(): v.sort(key=lambda x:(x.get("step") is None,x.get("step")))
    by_domain={}
    for (d,_),v in groups.items(): by_domain.setdefault(d,[]).append(v)
    out={}
    for d,ts in by_domain.items():
        branches=[v for v in ts if len(v)>=2]; out[d]={"trajectories":len(ts),"multi_step_trajectories":len(branches),"divergence":"NOT TESTABLE"}
        bg={}
        for v in branches: bg.setdefault(canon(v[0]["S_t"]),[]).append(v)
        div=False
        for vs in bg.values():
            if len(vs)>1:
                seq={tuple((x["A_t"],x["G"],x["L"],x["P"],x["R"],x["D"]) for x in v) for v in vs}
                if len(seq)>1: div=True
        if branches: out[d]["divergence"]="OBSERVED" if div else "NOT OBSERVED"
    return out
def utility_probe(rows,traj):
    def status(pred): return "OBSERVABLE" if any(pred(x) for x in rows) else ("NOT TESTABLE" if not rows else "NOT OBSERVABLE")
    vals=[v["divergence"] for v in traj.values()]
    div="OBSERVABLE" if "OBSERVED" in vals else ("NOT OBSERVABLE" if "NOT OBSERVED" in vals else "NOT TESTABLE") if vals else "NOT TESTABLE"
    return {"accessibility_expansion_contraction":status(lambda x:bool(x["G"] or x["L"])),
            "transformation_space_turnover":status(lambda x:x["R"]>0),"persistence":status(lambda x:x["P"]>0),
            "trajectory_divergence":div,
            "transformation_followed_by_future_accessibility_reconfiguration":status(lambda x:bool(x["T_real_t"]) and bool(x["G"] or x["L"]))}
def analyze(package,input_sha256=None,implementation_sha256=None):
    if package.get("protocol")!=PROTOCOL: raise ValueError("PROTOCOL_MISMATCH")
    records=package.get("records")
    if not isinstance(records,list) or not records: raise ValueError("NO_RECORDS")
    derived=[]; invalid=[]
    for i,r in enumerate(records):
        try: derived.append(derive(r))
        except ValueError as e: invalid.append({"index":i,"record_id":r.get("record_id"),"status":"NOT AVAILABLE","reason":str(e)})
    summaries={}
    for d in sorted({x["domain"] for x in derived}):
        z=[x for x in derived if x["domain"]==d]
        summaries[d]={"records":len(z),"mean_A_t":sum(x["A_t"] for x in z)/len(z),"mean_A_t1":sum(x["A_t1"] for x in z)/len(z),
        "expansion_records":sum("EXPANSION" in x["FPE"] for x in z),"contraction_records":sum("CONTRACTION" in x["FPE"] for x in z),
        "turnover_records":sum("TURNOVER" in x["FPE"] for x in z),"stability_records":sum("STABILITY" in x["FPE"] for x in z)}
    traj=trajectory_analysis(derived)
    result={"record_type":"TGCV_TR131_CROSS_DOMAIN_COMPARISON_ANALYSIS","protocol":PROTOCOL,"domains":sorted(summaries),
    "record_count":len(derived),"invalid_count":len(invalid),"derived":derived,"invalid_records":invalid,"summary":summaries,
    "trajectory_analysis":traj,"utility_probe":utility_probe(derived,traj),"input_sha256":input_sha256,"implementation_sha256":implementation_sha256}
    result["output_sha256"]=digest(result); return result
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input",type=Path); ap.add_argument("-o","--output",type=Path,required=True); a=ap.parse_args()
    raw=a.input.read_bytes(); res=analyze(json.loads(raw),hashlib.sha256(raw).hexdigest(),hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    a.output.write_text(json.dumps(res,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":"ANALYSIS_COMPLETED","records":res["record_count"],"invalid":res["invalid_count"],"output_sha256":res["output_sha256"]}))
if __name__=="__main__": main()
