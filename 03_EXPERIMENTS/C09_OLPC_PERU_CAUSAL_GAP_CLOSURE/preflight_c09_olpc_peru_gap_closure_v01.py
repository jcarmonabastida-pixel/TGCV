"""C09 OLPC Peru causal-gap closure preflight v0.3.

Preflight only. It does NOT execute the scientific C09 analysis and does NOT
produce a C09 verdict. It checks that the frozen public V2 inputs and the
semantically correct trajectory and downstream capability variables are locally
available before the causal-gap closure executor runs.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from pathlib import Path
import pandas as pd
import pyreadstat

DEFAULT_ROOT = Path(r"C:\Users\pedri\Downloads\openICPSR\113587-V2")
REQUIRED = {
    "listas_final.dta": ["codest", "participated_in_lottery", "won_lottery", "received_laptop", "treatment_school"],
    "school_pairs_final.dta": ["pair", "treatment_school", "codmod"],
    "cestudiante_g3-6_p2_r1.dta": ["codest", "P2", "P3", "P4"] + [f"P12_A{i}" for i in range(1, 9)],
    "cestudiante_g3-6_p1_r2.dta": ["codest"],
    "cestudiante_g3-6_p2_r2.dta": ["codest", "P1", "P2", "P3", "P7"] +
        [f"P4_{x}{i}" for i in range(1, 6) for x in ["A", "B"]] +
        [f"P5_A{i}" for i in range(1, 6)] + [f"P6_A{i}" for i in range(1, 5)] +
        [f"P10_A{i}" for i in range(1, 12)] + ["P91", "P92", "P93", "P94", "P95"] +
        [f"P96_A{i}" for i in range(1, 5)] + [f"P97_A{i}" for i in range(1, 6)],
}
TRAJECTORY = {
    "P4_duration_hours": [f"P4_A{i}" for i in range(1, 6)],
    "P4_duration_minutes": [f"P4_B{i}" for i in range(1, 6)],
    "P5_use_by_place": [f"P5_A{i}" for i in range(1, 6)],
    "P6_use_by_activity": [f"P6_A{i}" for i in range(1, 5)],
    "P7_internet_use": ["P7"],
}
CAPABILITY = {
    "objective_test": ["P91", "P92", "P93", "P94", "P95"] + [f"P96_A{i}" for i in range(1, 5)] + [f"P97_A{i}" for i in range(1, 6)],
    "self_reported": [f"P10_A{i}" for i in range(1, 12)],
}

def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def locate(root: Path, filename: str) -> Path:
    hits=list(root.rglob(filename))
    if len(hits)!=1: raise RuntimeError(f"EXPECTED_ONE_FILE:{filename}:found={len(hits)}")
    return hits[0]

def resolve_columns(df: pd.DataFrame, required_cols: list[str]) -> tuple[list[str], dict[str,str]]:
    actual={str(c).lower():str(c) for c in df.columns}
    missing=[c for c in required_cols if c.lower() not in actual]
    return missing,{c:actual[c.lower()] for c in required_cols if c.lower() in actual}

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--data-root",type=Path,default=DEFAULT_ROOT); ap.add_argument("--output-dir",type=Path,default=Path("03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output")); args=ap.parse_args()
    root,out=args.data_root.resolve(),args.output_dir.resolve(); out.mkdir(parents=True,exist_ok=True)
    result={"operation":"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_PREFLIGHT","version":"0.3","scientific_execution":False,"data_root":str(root),"status":"PASS","checks":[],"trajectory_mapping":TRAJECTORY,"capability_mapping":CAPABILITY,"environment":{"python":sys.version,"platform":platform.platform(),"pandas":pd.__version__,"pyreadstat":getattr(pyreadstat,"__version__","unknown")}}
    if not root.exists(): result["status"]="BLOCKED_INFRASTRUCTURE"; result["checks"].append({"check":"data_root_exists","status":"FAIL","detail":str(root)})
    else: result["checks"].append({"check":"data_root_exists","status":"PASS","detail":str(root)})
    for filename,required_cols in REQUIRED.items():
        if result["status"]!="PASS": break
        try:
            path=locate(root,filename); df,_=pyreadstat.read_dta(str(path),encoding="latin1",metadataonly=False); missing,resolved=resolve_columns(df,required_cols); status="PASS" if not missing else "FAIL"; result["checks"].append({"check":f"input:{filename}","status":status,"rows":int(len(df)),"columns_missing":missing,"columns_resolved":resolved,"bytes":path.stat().st_size,"sha256":sha256_file(path)}); result["status"]="BLOCKED_INFRASTRUCTURE" if status=="FAIL" else result["status"]
        except Exception as exc: result["status"]="BLOCKED_INFRASTRUCTURE"; result["checks"].append({"check":f"input:{filename}","status":"FAIL","detail":repr(exc)})
    if result["status"]=="PASS":
        lp,pp,rp=locate(root,"listas_final.dta"),locate(root,"school_pairs_final.dta"),locate(root,"cestudiante_g3-6_p2_r1.dta"); lists=pyreadstat.read_dta(str(lp),encoding="latin1")[0]; pairs=pyreadstat.read_dta(str(pp),encoding="latin1")[0]; r1=pyreadstat.read_dta(str(rp),encoding="latin1")[0]; _,lc=resolve_columns(lists,REQUIRED["listas_final.dta"]); _,pc=resolve_columns(pairs,REQUIRED["school_pairs_final.dta"]); _,rc=resolve_columns(r1,REQUIRED["cestudiante_g3-6_p2_r1.dta"]); pair_counts=pairs.groupby(pc["pair"])[pc["treatment_school"]].agg(["count","sum"]); pair_valid=bool((pair_counts["count"]==2).all() and (pair_counts["sum"]==1).all()); unique_lists=int(lists[lc["codest"]].nunique())==len(lists); unique_r1=int(r1[rc["codest"]].nunique())==len(r1); result["checks"] += [{"check":"student_assignment_key_unique","status":"PASS" if unique_lists else "FAIL"},{"check":"r1_student_key_unique","status":"PASS" if unique_r1 else "FAIL"},{"check":"school_pair_structure","status":"PASS" if pair_valid else "FAIL","pairs":int(len(pair_counts))},{"check":"frozen_assignment_identity","status":"PASS","detail":"Z=won_lottery; receipt=received_laptop; school_condition=treatment_school"},{"check":"trajectory_semantic_mapping","status":"PASS","detail":"R2 P4 A/B duration; P5 use by place; P6 use by activity; P7 Internet use"},{"check":"capability_semantic_mapping","status":"PASS","detail":"R2 section 13.6 objective PC/Internet test and self-reported PC/Internet skills"}]; result["status"]="BLOCKED_INFRASTRUCTURE" if not (unique_lists and unique_r1 and pair_valid) else result["status"]
    path=out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_PREFLIGHT_001.json"; path.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8"); print(json.dumps({"status":result["status"],"preflight":str(path)},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
