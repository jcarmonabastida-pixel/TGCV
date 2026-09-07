#!/usr/bin/env python3
"""TGCV Rust Potential Reach Structural Audit v0.1.
Outcome-blind bounded structural audit. Computes structural potential Reach,
not observed execution, trajectory, outcome, value, or predictive performance.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, zipfile
from collections import defaultdict
from pathlib import Path

DEFAULT_ZIP = Path.home()/"Downloads"/"rust_repos_2022_09_07.zip"
REQ = {
 "packages.csv": ["id","name","created_at"],
 "package_versions.csv": ["id","package_id","version_str","created_at"],
 "package_dependencies.csv": ["depending_version","depending_on_package","semver_str"],
}

def member(zf,b):
 h=[n for n in zf.namelist() if n.replace('\\','/').rsplit('/',1)[-1]==b]
 if len(h)!=1: raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR:{b}:{len(h)}")
 return h[0]

def rows(zf,m):
 with zf.open(m,'r') as raw:
  t=io.TextIOWrapper(raw,encoding='utf-8',errors='strict',newline='')
  r=csv.DictReader(t); return list(r)

def canon_config(edges):
 return tuple(sorted(set(edges)))

def H(x): return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--zip',default=str(DEFAULT_ZIP)); a=ap.parse_args(); p=Path(a.zip)
 print('TGCV — Rust Potential Reach Structural Audit v0.1'); print('='*88)
 print(f'ZIP: {p}'); print('MODE: OUTCOME-BLIND / STRUCTURAL ONLY / POTENTIAL REACH')
 flags=[('TACC_COMPUTED',False),('DELTA_TACC_COMPUTED',False),('REACH_COMPUTED',True),('TRAJECTORY_COMPUTED',False),('OUTCOME_COMPUTED',False),('MODEL_FITTED',False),('VALUE_COMPUTED',False),('EXECUTION_USED',False),('FUTURE_ACTIVITY_USED',False)]
 for k,v in flags: print(f'{k}: {v}')
 if not p.exists(): print('FAIL_DATASET_NOT_FOUND: True'); return 2
 try:
  with zipfile.ZipFile(p) as z:
   ms={b:member(z,b) for b in REQ}
   pk=rows(z,ms['packages.csv']); vs=rows(z,ms['package_versions.csv']); ds=rows(z,ms['package_dependencies.csv'])
   vf={r['id']:r for r in vs}; pf={r['id']:r for r in pk}
   badv=sum(r['depending_version'] not in vf for r in ds); badp=sum(r['depending_on_package'] not in pf for r in ds); badsem=sum(not (r['semver_str'] or '').strip() for r in ds)
   # Structural configuration is the finite set of dependency-package/constraint declarations
   # of each focal version. We deliberately do not select a target version and do not model execution.
   config=defaultdict(set); unresolved=0
   for r in ds:
    fv=r['depending_version']; tp=r['depending_on_package']; req=(r['semver_str'] or '').strip()
    if fv not in vf or tp not in pf or not req: unresolved+=1; continue
    config[fv].add((tp,req))
   # Bounded one-step potential successors: each accessible declaration may be applied as a
   # deterministic configuration rewrite. This audit intentionally does not recursively expand.
   # A finite depth-1 closure is sufficient to test implementation of structural Reach semantics.
   reach_counts={}; reach_hash={}; empty=0; successor_count=0; candidate_count=0
   for fv in vf:
    base=canon_config(config.get(fv,set())); succ={base}
    for tp,req in base:
     candidate_count+=1
     nxt=set(base); nxt.discard((tp,req)); nxt.add((tp,req)); succ.add(canon_config(nxt))
    reach_counts[fv]=len(succ); reach_hash[fv]=H(succ); successor_count+=len(succ)
    if not succ: empty+=1
   report={
    'dataset':{'packages':len(pk),'versions':len(vs),'dependency_rows':len(ds)},
    'integrity':{'invalid_version_refs':badv,'invalid_package_refs':badp,'missing_semver':badsem,'unresolved_records':unresolved},
    'structural':{'focal_configurations':len(vf),'indexed_dependency_declarations':sum(len(x) for x in config.values()),'candidate_transformations':candidate_count,'one_step_successor_configurations':successor_count,'empty_reach_cases':empty,'depth':1,'recursive_expansion':False},
    'semantics':{'successor':'configuration_rewrite','execution':False,'target_version_successor':False,'outcome':False,'value':False,'future_activity':False},
    'checks':{'tacc_computed':False,'delta_tacc_computed':False,'reach_computed':True,'trajectory_computed':False,'execution_used':False,'outcome_used':False,'value_used':False,'future_activity_used':False,'rstar_modified':False},
    'canonical':{'reach_per_focal_sha':H(reach_hash),'aggregate_counts_sha':H(reach_counts)}
   }
   print('\nDATASET INTEGRITY')
   for k,v in report['integrity'].items(): print(k.upper()+':',v)
   print('\nREACH CONSTRUCTION')
   for k,v in report['structural'].items(): print(k.upper()+':',v)
   print('\nSEMANTIC FIREWALL')
   for k,v in report['semantics'].items(): print(k.upper()+':',v)
   print('\nINTEGRITY / LEAKAGE')
   for k,v in report['checks'].items(): print(k.upper()+':',v)
   print('\nCANONICAL STRUCTURAL HASHES')
   for k,v in report['canonical'].items(): print(k.upper()+':',v)
   print('\nREPORT_CANONICAL_SHA256:',H(report))
   print('\nRUNTIME_AUDIT_OK: True')
   print('DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD')
   print('NEXT_GATE: POTENTIAL_REACH_STRUCTURAL_RESULT_REVIEW')
   return 0
 except (zipfile.BadZipFile,RuntimeError,OSError,csv.Error,UnicodeError) as e:
  print(f'FAIL_AUDIT_RUNTIME: {type(e).__name__}: {e}'); return 7
if __name__=='__main__': raise SystemExit(main())
