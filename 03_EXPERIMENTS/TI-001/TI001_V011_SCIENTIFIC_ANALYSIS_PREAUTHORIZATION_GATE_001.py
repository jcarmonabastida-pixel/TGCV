#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; B=ROOT/'03_EXPERIMENTS'/'TI-001'
F=B/'TI001_V011_FIXTURE_001.json'; S=B/'TI001_V011_SCIENTIFIC_ANALYSIS_SPECIFICATION_001.md'
E1=B/'TI001_V011_E1R_SCIENTIFIC_EXECUTION_RESULT_001.json'; E2=B/'TI001_V011_E2R_SCIENTIFIC_EXECUTION_RESULT_001.json'
A1=B/'TI001_V011_E1R_PRIMARY_EXECUTION_AUDIT_RESULT_001.json'; A2=B/'TI001_V011_E2R_PRIMARY_EXECUTION_AUDIT_RESULT_001.json'
C=B/'TI001_V011_E1R_E2R_INDEPENDENT_EXECUTION_CONCORDANCE_AUDIT_RESULT_001.json'
EXPECTED='30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1'
def load(p):
 raw=p.read_text(encoding='utf-8')
 if raw.endswith('\\n'): raw=raw[:-2]
 return json.loads(raw)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 c={}; e1,e2,a1,a2,co=map(load,(E1,E2,A1,A2,C)); spec=S.read_text(encoding='utf-8'); f=load(F)
 c['A1_SPEC_EXISTS']=S.is_file(); c['A2_SPEC_NOT_AUTHORIZED']='NOT AUTHORIZED' in spec
 c['A3_FIXTURE_SHA_EXACT']=sha(F)==EXPECTED and e1.get('fixture_sha256')==EXPECTED and e2.get('fixture_sha256')==EXPECTED
 c['A4_E1R_AUDIT_PASS']=a1.get('status')=='PASS'; c['A5_E2R_AUDIT_PASS']=a2.get('status')=='PASS'; c['A6_CONCORDANCE_PASS']=co.get('status')=='PASS'
 c['A7_EACH_420_VALID']=len(e1.get('records',[]))==420 and len(e2.get('records',[]))==420 and all(x.get('valid') for x in e1['records']) and all(x.get('valid') for x in e2['records'])
 c['A8_SAME_FIXTURE_BINDING']=e1.get('fixture_sha256')==e2.get('fixture_sha256')==EXPECTED
 c['A9_RESPONSE_IDS_DISJOINT']=set(x.get('response_id') for x in e1['records']).isdisjoint(set(x.get('response_id') for x in e2['records']))
 def rz(e): return sum((((x.get('usage') or {}).get('output_tokens_details') or {}).get('reasoning_tokens') or 0) for x in e.get('records',[]))
 c['A10_REASONING_ZERO']=rz(e1)==0 and rz(e2)==0
 c['A11_NO_POOLING_SPEC']='MUST NOT pool' in spec or 'prohibits pooling' in spec
 c['A12_NO_RECODE_IMPUTATION_RETRY_FILTERING']=all(x in spec.lower() for x in ('recoding','imputation','retry','outcome-dependent filtering'))
 analysis_names=('TI001_V011_SCIENTIFIC_ANALYSIS_RESULT_001.json','TI001_V011_POOLED_RESULT_001.json')
 c['A13_NO_ANALYSIS_RESULT']=not any((B/n).exists() for n in analysis_names)
 c['A14_NO_ESTIMATION_BY_GATE']=True; c['A15_NO_AUTHORIZATION_BY_GATE']=True
 ok=all(c.values())
 out={'gate_id':'TI001-V011-SCIENTIFIC-ANALYSIS-PREAUTHORIZATION-GATE-001','status':'PASS' if ok else 'FAIL','checks':c,'scientific_analysis':'NOT_PERFORMED','authorization':'READY_FOR_EXPLICIT_AUTHORIZATION' if ok else 'NOT_AUTHORIZED'}
 print(json.dumps(out,indent=2,sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())