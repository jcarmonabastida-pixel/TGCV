"""C09 OLPC Peru causal-gap closure executor v0.7.

Controlled correction of v0.6:
- preserves the v0.6 corrected causal universe and reconstruction logic;
- integrates the canonical G5 attrition analysis as an execution dependency;
- implements an explicit G6 causal-bridge gate;
- never treats a positive first-stage contrast alone as scientific closure.

The frozen C09 specification is not modified by this executor.
"""
from __future__ import annotations
import argparse, json, platform, subprocess, sys
from pathlib import Path

VERSION="0.7"
SPEC="TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001"
DEFAULT_ROOT=Path(r"C:\Users\pedri\Downloads\openICPSR\113587-V2")
V06=Path(__file__).with_name("run_c09_olpc_peru_gap_closure_v02.py")
G5=Path(__file__).with_name("g5_attrition_analysis_c09_v01.py")


def run_json(script: Path, root: Path, out: Path):
    cmd=[sys.executable,str(script),"--data-root",str(root),"--output-dir",str(out)]
    p=subprocess.run(cmd,text=True,capture_output=True)
    if p.returncode!=0:
        raise RuntimeError(f"CHILD_EXECUTION_FAILED:{script.name}:\n{p.stdout}\n{p.stderr}")
    lines=[x.strip() for x in p.stdout.splitlines() if x.strip()]
    if not lines: raise RuntimeError(f"CHILD_NO_JSON:{script.name}")
    try: return json.loads(lines[-1]),p.stdout,p.stderr
    except json.JSONDecodeError as e: raise RuntimeError(f"CHILD_JSON_INVALID:{script.name}:{e}: {lines[-1]}")


def nonzero_contrast(v):
    return isinstance(v,dict) and v.get("diff") is not None and abs(float(v["diff"]))>0


def sign(v):
    if not isinstance(v,dict) or v.get("diff") is None: return None
    x=float(v["diff"]); return 1 if x>0 else (-1 if x<0 else 0)


def g6_gate(v06,g5):
    c=v06.get("contrasts",{})
    first={k:v for k,v in c.items() if k.startswith("Z_to_delta_")}
    traj={k:v for k,v in c.items() if k.startswith("Z_to_trajectory_")}
    first_available={k:v for k,v in first.items() if v.get("diff") is not None}
    traj_available={k:v for k,v in traj.items() if v.get("diff") is not None}
    first_pass=bool(first_available) and any(nonzero_contrast(v) for v in first_available.values())
    traj_pass=bool(traj_available) and any(nonzero_contrast(v) for v in traj_available.values())
    cc=g5.get("complete_case_contrasts",{})
    ipw=g5.get("ipw_contrasts",{})
    sensitivity={}
    for y,iv in ipw.items():
        cv=cc.get(y,{})
        cs=sign(cv); ins=sign(iv)
        sensitivity[y]={"complete_case_sign":cs,"ipw_sign":ins,"same_nonzero_sign":bool(cs is not None and ins is not None and cs==ins and cs!=0)}
    sensitivity_available=[x for x in sensitivity.values() if x["complete_case_sign"] is not None and x["ipw_sign"] is not None]
    g5_consistent=bool(sensitivity_available) and all(x["same_nonzero_sign"] for x in sensitivity_available)
    # The available C09 evidence does not identify exclusion/direct-path conditions.
    alternative_paths_addressed=False
    causal_identification=False
    if first_pass and traj_pass and g5_consistent and alternative_paths_addressed:
        status="PASS"
    elif not first_pass:
        status="FAIL"
    else:
        status="PARTIAL/INCONCLUSIVE"
    return {
        "status":status,
        "G6_1_Z_to_delta_T_acc":{"status":"PASS" if first_pass else "FAIL","available_contrasts":first_available},
        "G6_2_delta_T_acc_to_trajectory":{"status":"PASS" if traj_pass else "FAIL","available_contrasts":traj_available},
        "G6_3_G5_persistence":{"status":"PASS" if g5_consistent else "FAIL/INCONCLUSIVE","sensitivity":sensitivity},
        "G6_4_alternative_direct_pathways":{"status":"NOT_IDENTIFIED","addressed":alternative_paths_addressed,"note":"A treatment/accessibility contrast plus downstream association does not by itself identify an exclusive accessibility-mediated causal pathway."},
        "G6_5_identification_limit":{"status":"NOT_SATISFIED","causal_identification":causal_identification,"note":"No separate exclusion/mediation identification argument is encoded in the available C09 execution inputs."},
        "closure_authorized":False if status!="PASS" else True,
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--data-root",type=Path,default=DEFAULT_ROOT); ap.add_argument("--output-dir",type=Path,default=Path("03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output_v07")); args=ap.parse_args()
    root=args.data_root.resolve(); out=args.output_dir.resolve(); out.mkdir(parents=True,exist_ok=True)
    v06out=out/"v06_base"; g5out=out/"g5"
    v06,v06stdout,_=run_json(V06,root,v06out)
    g5,g5stdout,_=run_json(G5,root,g5out)
    g6=g6_gate(v06,g5)
    result={
        "spec":SPEC,"version":VERSION,"status":g6["status"],
        "scientific_closure_authorized":bool(g6["closure_authorized"]),
        "execution_dependency":{"v06_executor":"executed_as_historical_base_only","g5_executor":"integrated_as_execution_dependency","frozen_spec_unchanged":True},
        "G1_G5":{"G1_corrected_causal_universe": "PASS" if v06.get("causal_universe") else "NOT_VERIFIED","G2_assignment":"EXECUTED_IN_V06","G3_accessibility":"EXECUTED_IN_V06","G4_trajectory":"EXECUTED_IN_V06","G5_attrition":g5.get("g5","PASS_OPERATIONAL")},
        "G6":g6,
        "v06_base_status":v06.get("status"),
        "scientific_boundary":"A positive Z->delta_T_acc result is necessary but insufficient. Closure requires the explicit G6 bridge and identification conditions; this executor does not infer mediation from downstream contrasts.",
        "output_directories":{"v06_base":str(v06out),"g5":str(g5out),"result":str(out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_RESULT_003.json")},
        "environment":{"python":sys.version,"platform":platform.platform()},
    }
    rp=out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_RESULT_003.json"; rp.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8")
    (out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_EXECUTION_LOG_003.txt").write_text("\n".join([f"SPEC={SPEC}",f"VERSION={VERSION}",f"STATUS={result['status']}","G5=INTEGRATED","G6=EXPLICIT","SCIENTIFIC_CLOSURE_AUTHORIZED="+str(result["scientific_closure_authorized"]),"V06_BASE_STATUS="+str(v06.get("status"))]),encoding="utf-8")
    print(json.dumps({"status":result["status"],"result":str(rp),"g6_status":g6["status"],"scientific_closure_authorized":result["scientific_closure_authorized"]},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
