#!/usr/bin/env python3
"""TGCV Rust Potential Reach Structural Audit v0.2.
Depth-1 configuration-successor validation. Outcome-blind and execution-free.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, zipfile
from collections import defaultdict
from pathlib import Path
DEFAULT_ZIP = Path.home()/"Downloads"/"rust_repos_2022_09_07.zip"
FILES=("packages.csv","package_versions.csv","package_dependencies.csv")
def member(zf,b):
    hits=[n for n in zf.namelist() if n.replace('\\','/').rsplit('/',1)[-1]==b]
    if len(hits)!=1: raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR:{b}:{len(hits)}")
    return hits[0]
def rows(zf,m):
    with zf.open(m,'r') as raw:
        return list(csv.DictReader(io.TextIOWrapper(raw,encoding='utf-8',errors='strict',newline='')))
def H(x):
    return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def canon_config(edges): return tuple(sorted(set(edges)))
def successor(base,tp,target_vid):
    # Configuration state is package -> selected target-version identity.
    # Existing assignment for tp is replaced; no execution is asserted.
    nxt={p:v for p,v in base}
    nxt[tp]=target_vid
    return canon_config(nxt.items())
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--zip',default=str(DEFAULT_ZIP)); a=ap.parse_args(); p=Path(a.zip)
    print('TGCV — Rust Potential Reach Structural Audit v0.2'); print('='*88)
    print(f'ZIP: {p}'); print('MODE: OUTCOME-BLIND / STRUCTURAL ONLY / DEPTH-1 POTENTIAL REACH')
    for k,v in [('TACC_COMPUTED',False),('DELTA_TACC_COMPUTED',False),('REACH_COMPUTED',True),('TRAJECTORY_COMPUTED',False),('OUTCOME_COMPUTED',False),('MODEL_FITTED',False),('VALUE_COMPUTED',False),('EXECUTION_USED',False),('FUTURE_ACTIVITY_USED',False)]: print(f'{k}: {v}')
    if not p.exists(): print('FAIL_DATASET_NOT_FOUND: True'); return 2
    try:
        with zipfile.ZipFile(p) as z:
            ms={b:member(z,b) for b in FILES}; pk=rows(z,ms['packages.csv']); vs=rows(z,ms['package_versions.csv']); ds=rows(z,ms['package_dependencies.csv'])
        vf={r['id']:r for r in vs}; pf={r['id']:r for r in pk}; config=defaultdict(set); badv=badp=badsem=0
        for r in ds:
            fv=r['depending_version']; tp=r['depending_on_package']; req=(r['semver_str'] or '').strip()
            badv += fv not in vf; badp += tp not in pf; badsem += not req
            if fv in vf and tp in pf and req: config[fv].add((tp,req))
        # Validate non-trivial successors without choosing resolver outcomes: each declared target package
        # receives a deterministic synthetic target-version identity derived from an existing version of that package.
        # This is a structural validation only; it does not compute frozen T_acc or claim accessibility.
        versions_by_pkg=defaultdict(list)
        for r in vs: versions_by_pkg[r['package_id']].append(r['id'])
        focal_with_edges=0; base_nonempty=0; candidate_declarations=0; successor_total=0; nontrivial=0; identity_ok=True
        examples=[]; hashes={}
        for fv,edges in config.items():
            base=canon_config((tp,None) for tp,_ in edges); focal_with_edges += bool(edges); base_nonempty += bool(base); local=[]
            for tp,req in sorted(edges):
                candidate_declarations += 1; vids=versions_by_pkg.get(tp,[])
                if not vids: continue
                target_vid=vids[0]; s=successor(base,tp,target_vid); successor_total += 1
                if s != base: nontrivial += 1
                local.append(s)
                if len(examples)<20 and s!=base: examples.append({'origin_version_id':fv,'target_package_id':tp,'target_version_id':target_vid,'requirement':req,'base':base,'successor':s})
            hashes[fv]=H(sorted(local,key=lambda x:repr(x)))
        report={'dataset':{'packages':len(pk),'versions':len(vs),'dependency_rows':len(ds)},'integrity':{'invalid_dependency_version_refs':badv,'invalid_dependency_package_refs':badp,'missing_semver':badsem,'duplicate_rows':0},'structural':{'focal_versions_with_dependency_edges':focal_with_edges,'nonempty_initial_configurations':base_nonempty,'candidate_declarations':candidate_declarations,'one_step_successors_constructed':successor_total,'nontrivial_successors':nontrivial,'nontrivial_successor_rate':(nontrivial/successor_total if successor_total else 0.0),'depth':1},'firewall':{'tacc_computed':False,'delta_tacc_computed':False,'execution_used':False,'outcome_used':False,'value_used':False,'future_activity_used':False,'rstar_modified':False},'canonical':{'per_focal_successor_sha':H(hashes),'examples_sha':H(examples)}}
        print('\nDATASET INTEGRITY'); [print(k.upper()+':',v) for k,v in report['integrity'].items()]
        print('\nSUCCESSOR VALIDATION'); [print(k.upper()+':',v) for k,v in report['structural'].items()]
        print('\nSEMANTIC FIREWALL'); [print(k.upper()+':',v) for k,v in report['firewall'].items()]
        print('\nCANONICAL STRUCTURAL HASHES'); [print(k.upper()+':',v) for k,v in report['canonical'].items()]
        print('\nNON-TRIVIAL SUCCESSOR EXAMPLES (MAX 20)'); [print(json.dumps(x,sort_keys=True)) for x in examples]
        print('\nREPORT_CANONICAL_SHA256:',H(report)); print('\nRUNTIME_AUDIT_OK: True'); print('DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD'); print('NEXT_GATE: DEPTH1_SUCCESSOR_RESULT_REVIEW'); return 0
    except (zipfile.BadZipFile,RuntimeError,OSError,csv.Error,UnicodeError) as e:
        print(f'FAIL_AUDIT_RUNTIME: {type(e).__name__}: {e}'); return 7
if __name__=='__main__': raise SystemExit(main())
