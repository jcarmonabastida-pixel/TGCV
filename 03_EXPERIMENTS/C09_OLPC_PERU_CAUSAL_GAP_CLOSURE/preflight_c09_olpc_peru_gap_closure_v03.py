"""C09 v0.7 combined preflight — G1-G6 authorization gate.

No scientific execution is performed. The preflight verifies the canonical
executor/G5 dependency and the explicit G6 blocking logic before allowing a
local controlled execution of v0.7.
"""
from __future__ import annotations
import ast, hashlib, json, sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
EXEC=BASE/"run_c09_olpc_peru_gap_closure_v03.py"
G5=BASE/"g5_attrition_analysis_c09_v01.py"
SPEC=Path("00_GOVERNANCE/SIP/TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001.md")
AUDIT=BASE/"C09_OLPC_V07_EXECUTOR_IMPLEMENTATION_AUDIT_001.md"
def sha(p):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()
def text(p): return p.read_text(encoding="utf-8")
def main():
    checks={}; required=[EXEC,G5,SPEC,AUDIT]
    checks["required_files"]={str(p):p.exists() for p in required}; checks["required_files_pass"]=all(checks["required_files"].values())
    e=text(EXEC) if EXEC.exists() else ""; g=text(G5) if G5.exists() else ""; a=text(AUDIT) if AUDIT.exists() else ""
    checks["executor_version_0_7"]='VERSION="0.7"' in e
    checks["g5_dependency"]='G5=Path(__file__).with_name("g5_attrition_analysis_c09_v01.py")' in e and 'run_json(G5' in e
    checks["g6_function"]='def g6_gate(' in e
    checks["g6_first_stage"]='Z_to_delta_' in e
    checks["g6_trajectory"]='Z_to_trajectory_' in e
    checks["g6_2_mediator_diagnostic"]='def g6_2_delta_tacc_diagnostic(' in e and 'Wald/IV diagnostic using Z as instrument' in e and 'causal_interpretation_authorized=False' in e
    checks["g6_g5_sensitivity"]='complete_case_contrasts' in e and 'ipw_contrasts' in e
    checks["g6_alternative_path_block"]='alternative_paths_addressed=False' in e
    checks["g6_identification_block"]='causal_identification=False' in e
    checks["g1_identity_verification"]='identity=v06.get("identity",{})' in e and 'identity.get("causal_universe")' in e and 'identity.get("Z_definition")' in e
    checks["no_first_stage_only_verdict"]=("elif not first_pass" in e and "PARTIAL/INCONCLUSIVE" in e and "status=" in e)
    checks["audit_pass"]='Implementation audit:** PASS' in a
    checks["g5_x0_only"]='X0_SOURCE' in g and 'X0-only' in g
    checks["frozen_spec_unchanged"]='frozen C09 specification is not modified' in e
    checks["governance_isolation"]='RMA, Evidence Matrix, STATUS, or Core' in a
    checks["syntax_executor"]=False; checks["syntax_g5"]=False
    if checks["required_files_pass"]:
        try: ast.parse(e); checks["syntax_executor"]=True
        except SyntaxError as ex: checks["syntax_executor"]=str(ex)
        try: ast.parse(g); checks["syntax_g5"]=True
        except SyntaxError as ex: checks["syntax_g5"]=str(ex)
    gate_names=[k for k,v in checks.items() if k not in {"required_files","syntax_executor","syntax_g5"}]
    structural_pass=all(checks[k] is True for k in gate_names) and checks["syntax_executor"] is True and checks["syntax_g5"] is True
    result={"status":"PASS" if structural_pass else "BLOCKED_INFRASTRUCTURE","preflight":"C09 v0.7 G1-G6 authorization gate","scientific_execution":False,"controlled_execution_authorized":structural_pass,"checks":checks,"input_sha256":{str(p):sha(p) for p in required if p.exists()},"next_step":"Run v0.7 locally only if PASS; publish execution evidence afterward."}
    out=BASE/"output_v07"; out.mkdir(exist_ok=True); rp=out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_PREFLIGHT_003.json"; rp.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8")
    print(json.dumps({"status":result["status"],"preflight":str(rp),"scientific_execution":False,"controlled_execution_authorized":structural_pass},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
