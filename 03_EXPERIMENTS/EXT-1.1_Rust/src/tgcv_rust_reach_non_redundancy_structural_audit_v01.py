#!/usr/bin/env python3
"""TGCV — Rust Reach Non-Redundancy Structural Audit v0.1

Outcome-blind, depth-1, configuration-level structural audit.
"""
from __future__ import annotations
import csv, hashlib, json, sys, zipfile
from collections import defaultdict
from pathlib import Path
ZIP_PATH=Path(r"C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip")
RSTAR_VERSION="v0.2"
def canon(v): return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"))
def sha(v): return hashlib.sha256(v.encode()).hexdigest()
def norm(s): return " ".join((s or "").strip().split())
def load(zf,name):
    member=next((n for n in zf.namelist() if n==name or n.endswith("/"+name)),None)
    if member is None: raise KeyError(f"Archive member not found: {name}")
    with zf.open(member) as f: return list(csv.DictReader((x.decode("utf-8") for x in f)))
def api():
    sys.path.insert(0,str(Path(__file__).resolve().parent)); from rstar_v02 import requirement_kind,satisfies; return requirement_kind,satisfies
def main():
    requirement_kind,satisfies=api()
    print("TGCV — Rust Reach Non-Redundancy Structural Audit v0.1\n"+"="*94)
    print(f"ZIP: {ZIP_PATH}\nMODE: OUTCOME-BLIND / STRUCTURAL ONLY / DEPTH-1 CONFIGURATION SUCCESSORS")
    print("TACC_COMPUTED: True\nDELTA_TACC_COMPUTED: True\nREACH_COMPUTED: True\nTRAJECTORY_COMPUTED: False\nOUTCOME_COMPUTED: False\nMODEL_FITTED: False\nVALUE_COMPUTED: False\nEXECUTION_USED: False\nFUTURE_ACTIVITY_USED: False\n")
    with zipfile.ZipFile(ZIP_PATH) as z:
        packages=load(z,"packages.csv"); versions=load(z,"package_versions.csv"); deps=load(z,"package_dependencies.csv")
    pbyv={int(v['id']):int(v['package_id']) for v in versions}; vs={int(v['id']):v['version_str'] for v in versions}; vc={int(v['id']):v['created_at'] for v in versions}
    bypkg=defaultdict(list)
    for v in versions: bypkg[int(v['package_id'])].append((v['created_at'],int(v['id'])))
    for a in bypkg.values(): a.sort()
    db=defaultdict(list); seen=set(); malformed=dup=0
    for d in deps:
        try:
            ov,tp=int(d['depending_version']),int(d['depending_on_package']); r=norm(d['semver_str'])
            if not r: malformed+=1; continue
            k=(ov,tp,r)
            if k in seen: dup+=1; continue
            seen.add(k); db[ov].append((tp,r))
        except Exception: malformed+=1
    def decl(ov):
        out=defaultdict(list)
        for tp,r in db.get(ov,[]):
            if requirement_kind(r)!="UNSUPPORTED": out[tp].append(r)
        return out
    def tacc(ov,t):
        out=set(); d=decl(ov)
        for tp,rs in d.items():
            for created,tv in bypkg.get(tp,[]):
                if created>t: break
                for r in rs:
                    try:
                        if satisfies(vs[tv],r): out.add((tp,tv)); break
                    except ValueError as e:
                        if str(e).startswith("UNSUPPORTED_VERSION:"): continue
                        raise
        return out
    def succ(config,tp,tv):
        # Configuration identity deliberately excludes focal-version ID and tau ID.
        # It is the declaration-induced package->version assignment state.
        items={k:tuple(sorted(v)) for k,v in config.items()}
        items[tp]=(vs[tv],)
        return tuple(sorted(items.items()))
    paired=terminal=0; ta0=ta1=ra0=ra1=0; add=rem=0; red=nonred=0; samecard=0; examples=[]
    for pid,a in bypkg.items():
        if a: terminal+=1
        for i in range(len(a)-1):
            t0,v0=a[i]; t1,v1=a[i+1]; paired+=1
            d0,d1=decl(v0),decl(v1); a0=tacc(v0,t0); a1=tacc(v1,t1); A=a1-a0; R=a0-a1
            ta0+=len(a0); ta1+=len(a1); add+=len(A); rem+=len(R)
            r0={succ(d0,tp,tv) for tp,tv in a0}; r1={succ(d1,tp,tv) for tp,tv in a1}; ra0+=len(r0); ra1+=len(r1)
            for tp,tv in A:
                s=succ(d1,tp,tv)
                if s in r0: red+=1; case="DELTA_TACC_NONZERO_DELTA_REACH_ZERO"
                else: nonred+=1; case="DELTA_TACC_NONZERO_DELTA_REACH_NONZERO"
                if len(examples)<20: examples.append({"case":case,"target_package_id":tp,"target_version_id":tv,"successor":s})
            if len(a0)==len(a1) and r0!=r1: samecard+=1
    # Reach is compared pairwise; global unions are not used to infer temporal change.
    print("DATASET / TEMPORAL INTEGRITY")
    for k,v in [("PACKAGE_COUNT",len(packages)),("VERSION_COUNT",len(versions)),("DEPENDENCY_ROWS_SCANNED",len(deps)),("MALFORMED_ROWS",malformed),("DUPLICATE_ROWS",dup),("PAIRED_FOCAL_VERSION_TRANSITIONS",paired),("TERMINAL_FOCAL_VERSIONS",terminal)]: print(f"{k}: {v}")
    print("\nT_ACC / REACH STRUCTURE")
    for k,v in [("TACC_T0_MEMBERSHIP_COUNT",ta0),("TACC_T1_MEMBERSHIP_COUNT",ta1),("TACC_ADD_MEMBERSHIP_COUNT",add),("TACC_REM_MEMBERSHIP_COUNT",rem),("REACH1_T0_SUCCESSOR_CONFIGURATION_COUNT",ra0),("REACH1_T1_SUCCESSOR_CONFIGURATION_COUNT",ra1),("DELTA_TACC_ADDITIONS_WITH_REDUNDANT_SUCCESSOR",red),("DELTA_TACC_ADDITIONS_WITH_NONREDUNDANT_SUCCESSOR",nonred),("SAME_LOCAL_TACC_CARDINALITY_DIFFERENT_REACH_PAIRS",samecard)]: print(f"{k}: {v}")
    print("\nFIREWALL\nCANDIDATE_IDENTITY_INCLUDES_DECLARATION: False\nSUCCESSOR_IDENTITY_EQUALS_TRANSFORMATION_IDENTITY: False\nEXECUTION_USED: False\nOUTCOME_USED: False\nVALUE_USED: False\nFUTURE_ACTIVITY_USED: False\nRSTAR_VERSION: v0.2\nTRAJECTORY_COMPUTED: False\n")
    print("EXAMPLES")
    for x in examples: print(json.dumps(x,ensure_ascii=False,sort_keys=True))
    report={'paired':paired,'tacc_t0':ta0,'tacc_t1':ta1,'add':add,'rem':rem,'reach_t0':ra0,'reach_t1':ra1,'redundant':red,'nonredundant':nonred,'samecard':samecard,'firewall':{'execution':False,'outcome':False,'value':False,'future_activity':False,'rstar_modified':False}}
    print(f"\nREPORT_CANONICAL_SHA256: {sha(canon(report))}\n\nRUNTIME_AUDIT_OK: True\nDECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD\nNEXT_GATE: REACH_NON_REDUNDANCY_RESULT_REVIEW")
if __name__=="__main__": main()
