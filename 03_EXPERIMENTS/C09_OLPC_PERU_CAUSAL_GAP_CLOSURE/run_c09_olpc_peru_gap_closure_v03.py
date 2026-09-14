"""C09 OLPC Peru causal-gap closure executor v0.7.

Controlled correction of v0.6:
- preserves the v0.6 corrected causal universe and reconstruction logic;
- integrates the canonical G5 attrition analysis as an execution dependency;
- implements an explicit G6 causal-bridge gate;
- never treats a positive first-stage contrast alone as scientific closure.

The frozen C09 specification is not modified by this executor.
"""
from __future__ import annotations
import argparse,json,platform,re,subprocess,sys
from pathlib import Path
VERSION="0.7"
SPEC="TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001"
DEFAULT_ROOT=Path(r"C:\Users\pedri\Downloads\openICPSR\113587-V2")
V06=Path(__file__).with_name("run_c09_olpc_peru_gap_closure_v02.py")
G5=Path(__file__).with_name("g5_attrition_analysis_c09_v01.py")

def _child_root_json(stdout, required_keys, fallback_result=None):
    decoder=json.JSONDecoder(); candidates=[]
    for i,ch in enumerate(stdout):
        if ch!="{": continue
        try:
            obj,end=decoder.raw_decode(stdout[i:])
            if isinstance(obj,dict) and all(k in obj for k in required_keys): candidates.append(obj)
        except json.JSONDecodeError: pass
    if candidates: return candidates[-1]
    if fallback_result and fallback_result.exists():
        obj=json.loads(fallback_result.read_text(encoding="utf-8"))
        if isinstance(obj,dict) and all(k in obj for k in required_keys): return obj
    raise ValueError(f"no JSON object containing required keys {required_keys}")

def _result_path(stdout):
    m=re.search(r'"result"\s*:\s*"([^"]+)"',stdout)
    return Path(m.group(1)) if m else None

def run_json(script,root,out,required_keys):
    p=subprocess.run([sys.executable,str(script),"--data-root",str(root),"--output-dir",str(out)],text=True,capture_output=True)
    if p.returncode!=0: raise RuntimeError(f"CHILD_EXECUTION_FAILED:{script.name}:\n{p.stdout}\n{p.stderr}")
    try:
        return _child_root_json(p.stdout,required_keys,_result_path(p.stdout)),p.stdout,p.stderr
    except ValueError as e: raise RuntimeError(f"CHILD_JSON_INVALID:{script.name}:{e}:\n{p.stdout}") from e

def nonzero(v): return isinstance(v,dict) and v.get("diff") is not None and abs(float(v["diff"]))>0
def sign(v):
    if not isinstance(v,dict) or v.get("diff") is None:return None
    x=float(v["diff"]);return 1 if x>0 else (-1 if x<0 else 0)
def g6_gate(v06,g5):
    c=v06.get("contrasts",{}); first={k:v for k,v in c.items() if k.startswith("Z_to_delta_")}; traj={k:v for k,v in c.items() if k.startswith("Z_to_trajectory_")}
    first_available={k:v for k,v in first.items() if v.get("diff") is not None}; traj_available={k:v for k,v in traj.items() if v.get("diff") is not None}
    first_pass=bool(first_available) and any(nonzero(v) for v in first_available.values()); traj_pass=bool(traj_available) and any(nonzero(v) for v in traj_available.values())
    cc=g5.get("complete_case_contrasts",{}); ipw=g5.get("ipw_contrasts",{}); sensitivity={}
    for y,iv in ipw.items():
        cs=sign(cc.get(y,{})); ins=sign(iv); sensitivity[y]={"complete_case_sign":cs,"ipw_sign":ins,"same_nonzero_sign":bool(cs is not None and ins is not None and cs==ins and cs!=0)}
    av=[x for x in sensitivity.values() if x["complete_case_sign"] is not None and x["ipw_sign"] is not None]; g5_consistent=bool(av) and all(x["same_nonzero_sign"] for x in av)
    alternative_paths_addressed=False; causal_identification=False
    if first_pass and traj_pass and g5_consistent and alternative_paths_addressed:
        status="PASS"
    elif not first_pass:
        status="FAIL"
    else:
        status="PARTIAL/INCONCLUSIVE"
    return {"status":status,"G6_1_Z_to_delta_T_acc":{"status":"PASS" if first_pass else "FAIL","available_contrasts":first_available},"G6_2_delta_T_acc_to_trajectory":{"status":"PASS" if traj_pass else "FAIL","available_contrasts":traj_available},"G6_3_G5_persistence":{"status":"PASS" if g5_consistent else "FAIL/INCONCLUSIVE","sensitivity":sensitivity},"G6_4_alternative_direct_pathways":{"status":"NOT_IDENTIFIED","addressed":alternative_paths_addressed},"G6_5_identification_limit":{"status":"NOT_SATISFIED","causal_identification":causal_identification},"closure_authorized":status=="PASS"}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--data-root",type=Path,default=DEFAULT_ROOT);ap.add_argument("--output-dir",type=Path,default=Path("03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output_v07"));a=ap.parse_args();root=a.data_root.resolve();out=a.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    v06,v06stdout,_=run_json(V06,root,out/"v06_base",["contrasts","status","version"]);g5,g5stdout,_=run_json(G5,root,out/"g5",["complete_case_contrasts","ipw_contrasts"]);g6=g6_gate(v06,g5)
    result={"spec":SPEC,"version":VERSION,"status":g6["status"],"scientific_closure_authorized":g6["closure_authorized"],"execution_dependency":{"v06_executor":"executed_as_historical_base_only","g5_executor":"integrated_as_execution_dependency","frozen_spec_unchanged":True},"G1_G5":{"G1_corrected_causal_universe":"PASS" if v06.get("causal_universe") else "NOT_VERIFIED","G2_assignment":"EXECUTED_IN_V06","G3_accessibility":"EXECUTED_IN_V06","G4_trajectory":"EXECUTED_IN_V06","G5_attrition":g5.get("g5","PASS_OPERATIONAL")},"G6":g6,"v06_base_status":v06.get("status"),"scientific_boundary":"A positive Z->delta_T_acc result is necessary but insufficient; closure requires the explicit G6 bridge and identification conditions."}
    rp=out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_RESULT_003.json";rp.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8");(out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_EXECUTION_LOG_003.txt").write_text(f"SPEC={SPEC}\nVERSION={VERSION}\nSTATUS={result['status']}\nG5=INTEGRATED\nG6=EXPLICIT\nSCIENTIFIC_CLOSURE_AUTHORIZED={result['scientific_closure_authorized']}\nV06_BASE_STATUS={v06.get('status')}\n",encoding="utf-8");print(json.dumps({"status":result["status"],"result":str(rp),"g6_status":g6["status"],"scientific_closure_authorized":result["scientific_closure_authorized"]},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
