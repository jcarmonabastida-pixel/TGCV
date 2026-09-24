#!/usr/bin/env python3
"""Independent TI-001 v005 Executor-2 reconstruction/preflight."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

EXPECTED_SHA='edd83fd2df3d39aad8911087569c19614c2264b7'
EXPECTED_ID='TI001-v005-candidate-001'
EXPECTED_VERSION='v005-candidate-001'
ACTIONS=['a','b','c']
FIELDS={'future_accessibility_class','identity_turnover_class','persistence_class','reconfiguration_class'}

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def sha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

def run(f):
    checks={}; reasons={}
    checks['fixture_identity_pass']=(f.get('fixture_id')==EXPECTED_ID and f.get('version')==EXPECTED_VERSION and f.get('status')=='FROZEN' and f.get('scientific_execution')=='NOT_AUTHORIZED')
    checks['condition_structure_pass']=set(f.get('conditions',{}))=={'control','treatment','null'}
    mappings=f['conditions']['treatment'].get('future_mapping',{})
    checks['treatment_mapping_pass']=set(mappings)==set(ACTIONS)
    checks['descriptor_schema_pass']=all(set(d)==FIELDS and all(isinstance(v,str) for v in d.values()) for d in mappings.values())
    checks['future_descriptor_distinction_pass']=len({json.dumps(mappings[a],sort_keys=True) for a in ACTIONS})>=2
    checks['temporal_separation_pass']=f.get('temporal_order')==['information_presentation','transformation_selection','successor_realisation','future_accessibility_reveal']
    checks['future_reveal_blocked']=f.get('successor_state_before_selection') is False and f.get('successor_accessibility_before_selection') is False
    n=f['conditions']['null']
    checks['null_validity_pass']=n.get('future_mapping') is None and n.get('future_signal') is None and n.get('recommendation') is None and n.get('format_compatible') is True
    w=f.get('divergence_witness',{})
    checks['divergence_witness_pass']=all([w.get('control_action')=='a',w.get('treatment_action')=='b',w.get('different') is True,w.get('depends_on_treatment_mapping') is True,w.get('same_state') is True,w.get('same_t_acc') is True,w.get('same_task') is True,w.get('same_timing') is True,w.get('same_decision_rule') is True,w.get('no_evaluation') is True,w.get('removing_mapping_removes_witness') is True])
    tr=f.get('transition_traceability',{})
    checks['traceability_pass']=set(tr)==set(ACTIONS) and all(tr[a].get('action_key')==a for a in ACTIONS)
    checks['canonical_hash_pass']=sha(f)==EXPECTED_SHA
    for k,v in checks.items():
        if not v: reasons[k]='v005 frozen contract mismatch'
    return {**checks,'overall_reconstruction_pass':all(checks.values()),'reasons':reasons}

def main(argv):
    p=argparse.ArgumentParser(); p.add_argument('fixture'); p.add_argument('output'); a=p.parse_args(argv[1:])
    result=run(load(a.fixture)); Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,sort_keys=True)); return 0 if result['overall_reconstruction_pass'] else 1

if __name__=='__main__': raise SystemExit(main(__import__('sys').argv))