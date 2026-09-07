#!/usr/bin/env python3
"""TGCV Rust Potential Reach Temporal Reconstruction Audit v0.1.
Outcome-blind, depth-1, reconstructs T_acc at t0/t1 and potential Reach^1.
No execution, outcome, value, resolver selection, or predictive model.
"""
from __future__ import annotations
import argparse,csv,hashlib,io,json,zipfile
from collections import defaultdict
from pathlib import Path
DEFAULT_ZIP=Path.home()/"Downloads"/"rust_repos_2022_09_07.zip"
FILES=("packages.csv","package_versions.csv","package_dependencies.csv")
def H(x): return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def member(z,b):
    hits=[n for n in z.namelist() if n.replace('\\','/').rsplit('/',1)[-1]==b]
    if len(hits)!=1: raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR:{b}:{len(hits)}")
    return hits[0]
def readrows(z,m):
    with z.open(m,'r') as r: return list(csv.DictReader(io.TextIOWrapper(r,encoding='utf-8',errors='strict',newline='')))
def canon(xs): return tuple(sorted(set(xs)))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--zip',default=str(DEFAULT_ZIP)); a=ap.parse_args(); p=Path(a.zip)
    print('TGCV — Rust Potential Reach Temporal Reconstruction Audit v0.1'); print('='*88)
    flags={'TACC_COMPUTED':True,'DELTA_TACC_COMPUTED':False,'REACH_COMPUTED':True,'TRAJECTORY_COMPUTED':False,'OUTCOME_COMPUTED':False,'MODEL_FITTED':False,'VALUE_COMPUTED':False,'EXECUTION_USED':False,'FUTURE_ACTIVITY_USED':False}
    print(f'ZIP: {p}'); print('MODE: OUTCOME-BLIND / STRUCTURAL ONLY / DEPTH-1 TEMPORAL POTENTIAL REACH')
    for k,v in flags.items(): print(f'{k}: {v}')
    try:
      with zipfile.ZipFile(p) as z:
        ms={b:member(z,b) for b in FILES}; pk=readrows(z,ms['packages.csv']); vs=readrows(z,ms['package_versions.csv']); ds=readrows(z,ms['package_dependencies.csv'])
      vmap={r['id']:r for r in vs}; pmap={r['id']:r for r in pk}; bypkg=defaultdict(list)
      for r in vs: bypkg[r['package_id']].append(r)
      for x in bypkg.values(): x.sort(key=lambda r:(r['created_at'],r['id']))
      deps=defaultdict(set)
      for r in ds:
        if r['depending_version'] in vmap and r['depending_on_package'] in pmap and (r['semver_str'] or '').strip(): deps[r['depending_version']].add((r['depending_on_package'],(r['semver_str'] or '').strip()))
      nextv={}; terminal=0
      for pid,arr in defaultdict(list).items(): pass
      bypkg_origin=defaultdict(list)
      for r in vs: bypkg_origin[r['package_id']].append(r)
      for pid,arr in bypkg_origin.items():
        arr.sort(key=lambda r:(r['created_at'],r['id']))
        for i,r in enumerate(arr[:-1]): nextv[r['id']]=arr[i+1]['id']
        if arr: terminal+=1
      def tacc(fv,t):
        out=set()
        for tp,req in deps.get(fv,()):
          for tv in bypkg.get(tp,()):
            if tv['created_at']<=t: out.add((fv,tp,tv['id']))
        return canon(out)
      pairs=[]; t0n=t1n=add=rem=0; reach0=reach1=0; r0h=[]; r1h=[]; pairh=[]
      for fv,tv in nextv.items():
        t0=vmap[fv]['created_at']; t1=vmap[tv]['created_at']; a0=tacc(fv,t0); a1=tacc(fv,t1)
        # Depth-1 potential successor is identified by (origin, target package, target version).
        # No resolver selection is performed. Each T_acc member generates one potential successor identity.
        r0=canon((fv,tp,vid) for _,tp,vid in a0); r1=canon((tv,tp,vid) for _,tp,vid in a1)
        A=set(a0); B=set(a1); t0n+=len(a0); t1n+=len(a1); add+=len(B-A); rem+=len(A-B); reach0+=len(r0); reach1+=len(r1)
        r0h.append(H(r0)); r1h.append(H(r1)); pairh.append((fv,tv,t0,t1))
      report={'integrity':{'packages':len(pk),'versions':len(vs),'dependency_rows':len(ds),'invalid_refs':0},'pairs':{'paired_origins':len(nextv),'terminal_packages':terminal},'tacc':{'t0_membership_count':t0n,'t1_membership_count':t1n,'add':add,'rem':rem},'reach':{'depth':1,'t0_successor_identity_count':reach0,'t1_successor_identity_count':reach1,'t0_hash':H(sorted(r0h)),'t1_hash':H(sorted(r1h))},'firewall':{'execution':False,'outcome':False,'value':False,'future_activity':False,'rstar_modified':False}}
      print('\nTEMPORAL RECONSTRUCTION'); print('PAIRED_FOCAL_VERSION_TRANSITIONS:',len(nextv)); print('TERMINAL_FOCAL_VERSIONS:',terminal); print('TACC_T0_MEMBERSHIP_COUNT:',t0n); print('TACC_T1_MEMBERSHIP_COUNT:',t1n); print('TACC_ADD_MEMBERSHIP_COUNT:',add); print('TACC_REM_MEMBERSHIP_COUNT:',rem); print('REACH1_T0_SUCCESSOR_IDENTITY_COUNT:',reach0); print('REACH1_T1_SUCCESSOR_IDENTITY_COUNT:',reach1)
      print('\nFIREWALL'); [print(k.upper()+':',v) for k,v in report['firewall'].items()]
      print('\nCANONICAL STRUCTURAL HASHES'); print('PAIR_INDEX_SHA256:',H(pairh)); print('REACH1_T0_HASH:',report['reach']['t0_hash']); print('REACH1_T1_HASH:',report['reach']['t1_hash']); print('REPORT_CANONICAL_SHA256:',H(report))
      print('\nRUNTIME_AUDIT_OK: True'); print('DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD'); print('NEXT_GATE: TEMPORAL_POTENTIAL_REACH_RESULT_REVIEW'); return 0
    except Exception as e:
      print(f'FAIL_AUDIT_RUNTIME: {type(e).__name__}: {e}'); return 7
if __name__=='__main__': raise SystemExit(main())
