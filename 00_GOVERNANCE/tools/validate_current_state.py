from pathlib import Path
import csv
import sys
ROOT=Path(__file__).resolve().parents[2]
R=ROOT/'00_GOVERNANCE'/'rma'; I=ROOT/'00_GOVERNANCE'/'impact'; S=ROOT/'02_EXTERNAL_SCIENCE'; A=ROOT/'05_ASSETS'
e=[]
def f(p,n):
    if not p.exists(): e.append(f'MISSING {n}: {p.as_posix()}')
def d(p,n):
    if not p.is_dir(): e.append(f'MISSING {n}: {p.as_posix()}')
for p,n in [(R/'TGCV_RMA_current.md','RMA pointer'),(ROOT/'STATUS.md','STATUS'),(ROOT/'CHANGELOG.md','CHANGELOG'),(ROOT/'00_GOVERNANCE'/'EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md','claim matrix'),(R/'TGCV_RMA_v1.8.md','RMA v1.8'),(R/'TGCV_RMA_traceability_v1.8.csv','traceability v1.8'),(R/'TGCV_RMA_v1.9.md','RMA v1.9'),(R/'TGCV_RMA_v2.0.md','RMA v2.0'),(R/'TGCV_RMA_v2.1.md','RMA v2.1'),(R/'TGCV_RMA_traceability_v2.1.csv','traceability v2.1'),(S/'SCIENTIFIC_ASSET_REGISTRY_v0.1.md','scientific registry'),(I/'D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.4.md','protocol v0.4'),(I/'D-OPS-24_PREFLIGHT_v0.4.md','preflight v0.4'),(I/'D-OPS-24_F2_Q1_EXECUTION_AUTHORIZATION_v0.1.md','Q1 auth'),(I/'D-OPS-24_F2_Q1_EXECUTION_LOG_v0.1.md','Q1 result'),(I/'D-OPS-24_F2_Q2_EXECUTION_AUTHORIZATION_v0.1.md','Q2 auth'),(I/'D-OPS-24_F2_Q2_EXECUTION_RESULT_v0.1.md','Q2 result'),(I/'D-OPS-24_F2_Q3_EXECUTION_AUTHORIZATION_v0.1.md','Q3 auth'),(I/'D-OPS-24_F2_Q3_EXECUTION_RESULT_v0.1.md','Q3 result'),(I/'EXT-UPD-4.0_F2_DISCOVERY_PROPAGATION_v0.1.md','F2 propagation')]: f(p,n)
for x in ('TCP','Vision_Paper','Research_Prospectus','ARM','RII','MOI'): d(A/x,f'asset family {x}')
if (R/'TGCV_RMA_current.md').exists():
 t=(R/'TGCV_RMA_current.md').read_text(encoding='utf-8')
 for x in ('TGCV_RMA_v2.1.md','D-OPS-24','v0.4','F2-Q1','F2-Q2','F2-Q3','3/3 consumed','0/10 admitted','No Q4','from-scratch'):
  if x not in t: e.append(f'RMA pointer missing {x}')
tr=R/'TGCV_RMA_traceability_v2.1.csv'
if tr.exists():
 with tr.open(encoding='utf-8-sig',newline='') as h: rows=list(csv.DictReader(h))
 ids={x.get('asset_id') for x in rows}; need={'D-OPS-24','DOPS24-DISCOVERY-PROTOCOL-v0.4','DOPS24-PREFLIGHT-v0.4','DOPS24-F2-Q1-AUTH','DOPS24-F2-Q1-RESULT','DOPS24-F2-Q2-AUTH','DOPS24-F2-Q2-RESULT','DOPS24-F2-Q3-AUTH','DOPS24-F2-Q3-RESULT','EXT-UPD-4.0-F2-PROPAGATION','RMA-v1.8','RMA-v1.9','RMA-v2.0','RMA-v2.1','RMA-current','STATUS','PROPAGATION-WORKFLOW','VALIDATOR','SCIENTIFIC-ASSET-REGISTRY'}
 e += [f'Traceability missing {x}' for x in sorted(need-ids)]
 for aid,st in {'RMA-v1.8':'HISTORICAL-SUPERSEDED','RMA-v1.9':'HISTORICAL-SUPERSEDED','RMA-v2.0':'HISTORICAL-SUPERSEDED','RMA-v2.1':'CURRENT','DOPS24-F2-Q1-RESULT':'CLOSED','DOPS24-F2-Q2-RESULT':'CLOSED','DOPS24-F2-Q3-RESULT':'CLOSED','EXT-UPD-4.0-F2-PROPAGATION':'CLOSED-CONSISTENT'}.items():
  m=[x for x in rows if x.get('asset_id')==aid]
  if m and m[0].get('status')!=st: e.append(f'Traceability status mismatch {aid}')
 m=[x for x in rows if x.get('asset_id')=='RMA-current']
 if m and m[0].get('depends_on')!='RMA-v2.1': e.append('Traceability current pointer mismatch')
if e:
 print('GOVERNANCE_CURRENT_STATE=FAIL'); print('\n'.join(e)); sys.exit(1)
print('GOVERNANCE_CURRENT_STATE=PASS'); print('RMA v2.1, pointer, traceability, STATUS and F2 closure structurally aligned.')