#!/usr/bin/env python3
"""TGCV Canonical State Sync v3. Read-only manifest generation plus fail-closed apply/publish."""
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; GOV=ROOT/'00_GOVERNANCE'
FILES=[GOV/'CANONICAL_STATE.json',GOV/'EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md',GOV/'EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md',GOV/'EVIDENCE_TO_CLAIM_MATRIX_v1.5.md',GOV/'rma'/'TGCV_RMA_current.md',GOV/'rma'/'TGCV_RMA_traceability_current.csv',ROOT/'STATUS.md']
def rel(p): return p.relative_to(ROOT).as_posix()
def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  while True:
   b=f.read(1024*1024)
   if not b: break
   h.update(b)
 return h.hexdigest()
def tx(*a,check=True):
 r=subprocess.run(['git',*a],cwd=ROOT,text=True,capture_output=True,encoding='utf-8',errors='replace')
 if check and r.returncode: raise RuntimeError(r.stderr.strip() or r.stdout.strip())
 return r.stdout.strip()
def txt(p): return p.read_text(encoding='utf-8',errors='replace')
def claims(s): return [x.split('|')[1].strip() for x in s.splitlines() if x.startswith('| C') and '|' in x]
def cols(s):
 for x in s.splitlines():
  if x.startswith('| ID ') or x.startswith('|ID'): return [z.strip() for z in x.strip('|').split('|')]
 return []
def heads(s): return [x.strip('# ').strip() for x in s.splitlines() if x.startswith('#')]
def audit():
 e=[]; a=GOV/'EVIDENCE_TO_CLAIM_MATRIX_v1.4.md'; b=GOV/'EVIDENCE_TO_CLAIM_MATRIX_v1.5.md'; c=GOV/'EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md'
 if not b.exists() or not c.exists(): e.append('MATRIX_MISSING'); return e
 sa,sb=txt(a),txt(b)
 if len(sb.splitlines())<len(sa.splitlines()): e.append('SUCCESSOR_MATRIX_SHRINKS_IN_LINES')
 if not set(claims(sa))<=set(claims(sb)): e.append('SUCCESSOR_LOSES_CLAIMS')
 if cols(sa)!=cols(sb): e.append('SUCCESSOR_COLUMNS_CHANGED')
 if not set([h for h in heads(sa) if 'evidence' in h.lower()])<=set([h for h in heads(sb) if 'evidence' in h.lower()]): e.append('SUCCESSOR_LOSES_EVIDENCE_SECTIONS')
 if not set(['Claim boundary','Current methodological routing','Current scientific position','Gate state','Interpretation boundary'])<=set(heads(sb)): e.append('SUCCESSOR_LOSES_GOVERNANCE_BOUNDARIES')
 for bad in ['schema of v1.3','The v1.3 update is additive']:
  if bad in sb: e.append('STALE_V1.5_METADATA:'+bad)
 if 'FOS C09' not in sb: e.append('FOS_C09_MISSING')
 if '**Predecessor:** v1.4' not in sb: e.append('V1.5_PREDECESSOR_NOT_V1.4')
 if txt(c)!=sb: e.append('CURRENT_MATRIX_DIFFERS_FROM_V1.5')
 if 'v1.5' not in txt(GOV/'EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md'): e.append('CURRENT_POINTER_NOT_V1.5')
 if 'v1.5' not in txt(GOV/'CANONICAL_STATE.json'): e.append('CANONICAL_STATE_NOT_V1.5')
 return e
def snap(): return {rel(p):(sha(p) if p.exists() else None,p.stat().st_size if p.exists() else None) for p in FILES}
def manifest(args):
 e=audit(); head=tx('rev-parse','HEAD'); src=tx('rev-parse',f'{args.source_commit}^{{commit}}')
 return {'manifest_version':'1.0','status':'PREPARED_NOT_APPLIED' if not e else 'BLOCKED_VALIDATION','target_matrix_version':args.matrix_version,'source_commit':src,'source_commit_verified':src==head,'source_of_truth':'00_GOVERNANCE/CANONICAL_STATE.json','projections':['RMA','MATRIX','STATUS'],'validation':['MONOTONIC_EVIDENCE','CROSS_REFERENCE','VERSION_POINTER','STATUS'],'write_order':['BUILD','VALIDATE','WRITE','RE_READ','VERIFY'],'remote_policy':'COMMIT_PUSH_REMOTE_VERIFY','allowed_paths':[rel(p) for p in FILES],'files':[{'path':rel(p),'predecessor_sha256':sha(p) if p.exists() else None,'target_sha256':sha(p) if p.exists() else None,'target_source':'existing_local_current_state','authorized':True} for p in FILES],'validation_result':{'ok':not e,'errors':e}}
def main():
 ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
 sp.add_parser('check'); p=sp.add_parser('plan'); p.add_argument('--matrix-version',required=True); p.add_argument('--source-commit',required=True)
 sp.add_parser('verify'); p=sp.add_parser('manifest'); p.add_argument('--matrix-version',default='v1.5'); p.add_argument('--source-commit',default='HEAD'); p.add_argument('--output')
 p=sp.add_parser('apply'); p.add_argument('--transition-manifest',required=True); p.add_argument('--write',action='store_true')
 p=sp.add_parser('publish'); p.add_argument('--transition-manifest',required=True); p.add_argument('--commit',action='store_true'); p.add_argument('--push',action='store_true'); p.add_argument('--message',default='Governance: reconcile canonical state')
 a=ap.parse_args(); before=snap()
 if a.cmd=='manifest':
  m=manifest(a); out=json.dumps(m,ensure_ascii=False,indent=2); print(out); print('NO_FILES_WRITTEN='+str(before==snap()).upper()); print('MANIFEST_RESULT='+('PREPARED_READ_ONLY' if not m['validation_result']['errors'] else 'BLOCKED_READ_ONLY')); return 0
 if a.cmd=='verify':
  e=audit(); print('TGCV CANONICAL STATE SYNC'); print('MODE=VERIFY'); print('AUDIT_RESULT='+('PASS' if not e else 'FAIL')); print('ERRORS='+json.dumps(e,ensure_ascii=False)); print('NO_FILES_WRITTEN='+str(before==snap()).upper()); print('VERIFY_RESULT='+('PASS_READ_ONLY' if not e and before==snap() else 'FAIL_READ_ONLY')); return 0
 if a.cmd=='check': print('TGCV CANONICAL STATE SYNC'); print('MODE=CHECK'); print('ERRORS='+json.dumps(audit(),ensure_ascii=False)); print('NO_FILES_WRITTEN=TRUE'); return 0
 if a.cmd=='plan':
  src=tx('rev-parse',f'{a.source_commit}^{{commit}}'); print('TGCV CANONICAL STATE SYNC'); print('MODE=PLAN'); print('TARGET_MATRIX_VERSION='+a.matrix_version); print('SOURCE_COMMIT_RESOLVED='+src); print('SOURCE_COMMIT_VERIFIED='+str(src==tx('rev-parse','HEAD')).upper()); print('TARGET_MATRIX_PRESENT='+str((GOV/'EVIDENCE_TO_CLAIM_MATRIX_v1.5.md').exists()).upper()); print('TARGET_MATRIX_SHA256='+sha(GOV/'EVIDENCE_TO_CLAIM_MATRIX_v1.5.md')); print('SOURCE_OF_TRUTH=CANONICAL_STATE.json'); print('PROJECTIONS=RMA,MATRIX,STATUS'); print('VALIDATION=MONOTONIC_EVIDENCE,CROSS_REFERENCE,VERSION_POINTER,STATUS'); print('WRITE_ORDER=BUILD->VALIDATE->WRITE->RE_READ->VERIFY'); print('REMOTE_POLICY=COMMIT_PUSH_REMOTE_VERIFY'); print('NO_FILES_WRITTEN=TRUE'); print('PLAN_RESULT='+('READ_ONLY' if not audit() else 'FAIL')); return 0
 if a.cmd in ('apply','publish'):
  print('RESULT=FAIL_CLOSED'); print('REASON=V3_WRITE_PATH_REQUIRES_EXPLICIT_MANIFEST_TARGET_IMPLEMENTATION'); return 2
if __name__=='__main__': raise SystemExit(main())
