from pathlib import Path
import csv,sys
ROOT=Path(__file__).resolve().parents[2]; R=ROOT/'00_GOVERNANCE'/'rma'; I=ROOT/'00_GOVERNANCE'/'impact'; S=ROOT/'02_EXTERNAL_SCIENCE'; A=ROOT/'05_ASSETS'; e=[]
def f(p,n):
    if not p.exists(): e.append(f'MISSING {n}: {p.as_posix()}')
def d(p,n):
    if not p.is_dir(): e.append(f'MISSING {n}: {p.as_posix()}')
for p,n in [(R/'TGCV_RMA_current.md','RMA pointer'),(R/'TGCV_RMA_v2.4.md','RMA v2.4'),(R/'TGCV_RMA_traceability_v2.4.csv','traceability v2.4'),(ROOT/'STATUS.md','STATUS'),(ROOT/'CHANGELOG.md','CHANGELOG'),(ROOT/'00_GOVERNANCE'/'EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md','current claim matrix'),(ROOT/'00_GOVERNANCE'/'EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md','current claim matrix pointer'),(S/'SCIENTIFIC_ASSET_REGISTRY_v0.1.md','scientific registry'),(I/'D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.5.md','protocol v0.5'),(I/'D-OPS-24_PREFLIGHT_v0.5.md','preflight v0.5'),(I/'EXT-UPD-4.1_DOPS24_V05_FREEZE_PROPAGATION_v0.1.md','freeze propagation'),(I/'EXT-UPD-4.2_C01_GATE_D_RESOLUTION_DECISION_v0.1.md','EXT-UPD-4.2'),(I/'EXT-UPD-4.3_EVIDENCE_CLAIM_PROPAGATION_GOVERNANCE_CORRECTION_v0.1.md','EXT-UPD-4.3'),(I/'D-OPS-24_V05_C01_GATE_D_OPERATIONALIZATION_DESIGN_v0.2.md','Gate-D design v0.2'),(I/'D-OPS-24_V05_C01_GATE_D_OPERATIONALIZATION_PREFLIGHT_v0.1.md','Gate-D preflight'),(I/'D-OPS-24_V05_C01_GATE_D_EXECUTION_AUTHORIZATION_v0.1.md','Gate-D authorization'),(I/'D-OPS-24_V05_C01_GATE_D_EXECUTION_RESULT_v0.1.md','Gate-D result'),(I/'EXT-UPD-4.4_C01_GATE_D_RESULT_PROPAGATION_v0.1.md','EXT-UPD-4.4')]: f(p,n)
for x in ('TCP','Vision_Paper','Research_Prospectus','ARM','RII','MOI'): d(A/x,f'asset family {x}')
p=R/'TGCV_RMA_current.md'
if p.exists():
 t=p.read_text(encoding='utf-8')
 for x in ('TGCV_RMA_v2.4.md','C-01','Gate D','INDETERMINATE','EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md','EXT-UPD-4.3','EXT-UPD-4.4','new explicit governance decision','from-scratch'):
  if x not in t: e.append(f'RMA pointer missing {x}')
tr=R/'TGCV_RMA_traceability_v2.4.csv'
if tr.exists():
 with tr.open(encoding='utf-8-sig',newline='') as h: rows=list(csv.DictReader(h))
 ids={r.get('asset_id') for r in rows}
 need={'D-OPS-24','DOPS24-DISCOVERY-PROTOCOL-v0.5','DOPS24-PREFLIGHT-v0.5','C-01','C01-GATED-EXEC','EXT-UPD-4.2','EXT-UPD-4.3','EXT-UPD-4.4','RMA-v2.4','RMA-current','STATUS','VALIDATOR','CLAIM-MATRIX','SCIENTIFIC-ASSET-REGISTRY'}
 e += [f'Traceability missing {x}' for x in sorted(need-ids)]
 checks={'D-OPS-24':'FROZEN-DESIGN','DOPS24-DISCOVERY-PROTOCOL-v0.5':'FROZEN','DOPS24-PREFLIGHT-v0.5':'CLOSED-PASS','C-01':'CLOSED-BOUNDED','C01-GATED-EXEC':'CLOSED-INDETERMINATE','EXT-UPD-4.2':'CLOSED','EXT-UPD-4.3':'CLOSED','EXT-UPD-4.4':'CLOSED-PROPAGATED','RMA-v2.3':'HISTORICAL-SUPERSEDED','RMA-v2.4':'CURRENT','RMA-current':'CURRENT','STATUS':'CURRENT','VALIDATOR':'CURRENT','CLAIM-MATRIX':'CURRENT'}
 for aid,st in checks.items():
  m=[r for r in rows if r.get('asset_id')==aid]
  if m and m[0].get('status')!=st: e.append(f'Traceability status mismatch {aid}: {m[0].get("status")}')
 m=[r for r in rows if r.get('asset_id')=='RMA-current']
 if m and m[0].get('depends_on')!='RMA-v2.4': e.append('Traceability current pointer mismatch')
 m=[r for r in rows if r.get('asset_id')=='CLAIM-MATRIX']
 if m and m[0].get('canonical_location')!='00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md': e.append('Traceability claim matrix pointer mismatch')
if e:
 print('GOVERNANCE_CURRENT_STATE=FAIL'); print('\n'.join(e)); sys.exit(1)
print('GOVERNANCE_CURRENT_STATE=PASS'); print('C-01 Gate D result propagation, current Evidence→Claim Matrix, RMA v2.4, pointer, traceability and STATUS aligned.')
