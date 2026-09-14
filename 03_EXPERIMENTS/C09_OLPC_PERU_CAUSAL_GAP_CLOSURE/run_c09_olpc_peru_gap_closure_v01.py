"""C09 OLPC Peru causal-gap closure executor v0.5.

Evidence operation for the frozen C09 gap-closure specification; not a TR-132
proof/reproduction exercise. Trajectory transformations follow the published
openICPSR 113587 V2 input_r2.do, and Raven scoring uses its published 36-item key.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from pathlib import Path
import numpy as np, pandas as pd
import pyreadstat

SPEC = "TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001"
DEFAULT_ROOT = Path(r"C:\Users\pedri\Downloads\openICPSR\113587-V2")
RAVEN_KEY = [4,5,1,2,6,3,6,2,1,3,4,5,4,5,1,6,2,1,3,4,6,3,5,2,2,6,1,2,1,3,5,6,4,3,4,5]


def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()


def read_dta(path: Path): return pyreadstat.read_dta(str(path), encoding="latin1")


def locate(root: Path, filename: str) -> Path:
    hits=list(root.rglob(filename))
    if len(hits)!=1: raise RuntimeError(f"EXPECTED_ONE_FILE:{filename}:found={len(hits)}")
    return hits[0]


def resolve_col(df: pd.DataFrame, name: str) -> str:
    m={str(c).lower():str(c) for c in df.columns}
    if name.lower() not in m: raise RuntimeError(f"Required variable missing: {name}")
    return m[name.lower()]


def binary_yes(x):
    s=pd.to_numeric(x,errors="coerce")
    return s.where(s.isin([1,2])).map({1:1,2:0})


def binary_indicator(x, valid=(1,2)):
    s=pd.to_numeric(x,errors="coerce")
    return s.where(s.isin(valid)).map({1:1,2:0})


def mean_diff(df,y,z):
    a=df.loc[df[z]==1,y].dropna(); b=df.loc[df[z]==0,y].dropna()
    return {"n_z1":int(len(a)),"n_z0":int(len(b)),"mean_z1":None if a.empty else float(a.mean()),"mean_z0":None if b.empty else float(b.mean()),"diff":None if a.empty or b.empty else float(a.mean()-b.mean())}


def derive_trajectory(r2raw):
    cod=resolve_col(r2raw,"codest"); d=pd.DataFrame({"codest":r2raw[cod]}); duration=[]
    for i in range(1,6):
        a=pd.to_numeric(r2raw[resolve_col(r2raw,f"P4_A{i}")],errors="coerce"); b=pd.to_numeric(r2raw[resolve_col(r2raw,f"P4_B{i}")],errors="coerce")
        a=a.where(~a.isin([-9,-8,-7])); b=b.where(~b.isin([-9,-8,-7])); a=a.mask(a.isna()&b.notna(),0); b=b.mask(b.isna()&a.notna(),0)
        n=f"trajectory_P4_duration_{i}_minutes"; d[n]=a*60+b; duration.append(n)
    d["trajectory_P4_total_minutes"]=d[duration].sum(axis=1,min_count=1); d["trajectory_P4_used_yesterday"]=d["trajectory_P4_total_minutes"].gt(0).astype(float); d.loc[d[duration].notna().sum(axis=1).eq(0),"trajectory_P4_used_yesterday"]=np.nan
    weekly=[]
    for i in range(1,6):
        s=pd.to_numeric(r2raw[resolve_col(r2raw,f"P5_A{i}")],errors="coerce"); n=f"trajectory_P5_place_{i}"; d[n]=s.where(s.isin([1,2])).map({1:1,2:0}); weekly.append(n)
    d["trajectory_P5_used_week"]=d[weekly].max(axis=1,skipna=True); d.loc[d[weekly].notna().sum(axis=1).eq(0),"trajectory_P5_used_week"]=np.nan
    activities=[]
    for i in range(1,5):
        s=pd.to_numeric(r2raw[resolve_col(r2raw,f"P6_A{i}")],errors="coerce"); n=f"trajectory_P6_activity_{i}"; d[n]=s.where(s.isin([1,2])).map({1:1,2:0}); activities.append(n)
    d["trajectory_P6_any_activity"]=d[activities].max(axis=1,skipna=True); d.loc[d[activities].notna().sum(axis=1).eq(0),"trajectory_P6_any_activity"]=np.nan
    s=pd.to_numeric(r2raw[resolve_col(r2raw,"P7")],errors="coerce"); d["trajectory_P7_internet_use"]=s.where(s.isin([1,2])).map({1:1,2:0})
    return d,["trajectory_P4_used_yesterday","trajectory_P4_total_minutes","trajectory_P5_used_week","trajectory_P6_any_activity","trajectory_P7_internet_use"]


def build_capabilities(r2raw):
    cod=resolve_col(r2raw,"codest"); d=pd.DataFrame({"codest":r2raw[cod]})
    objective=[]
    for name,key in [("p91",3),("p92",1),("p93",1),("p94",2),("p95",3)]:
        s=pd.to_numeric(r2raw[resolve_col(r2raw,name)],errors="coerce")
        v=s.where(~s.isin([-9,-8,-7])); d[f"cap_{name}"]=(v==key).astype(float); d.loc[v.isna(),f"cap_{name}"]=np.nan; objective.append(f"cap_{name}")
    for i,key in [(1,2),(2,1),(3,2),(4,2)]:
        name=f"p96_a{i}"; s=pd.to_numeric(r2raw[resolve_col(r2raw,name)],errors="coerce"); v=s.where(~s.isin([-9,-8,-7])); d[f"cap_{name}"]=(v==key).astype(float); d.loc[v.isna(),f"cap_{name}"]=np.nan; objective.append(f"cap_{name}")
    for i,key in [(1,1),(2,2),(3,1),(4,1),(5,1)]:
        name=f"p97_a{i}"; s=pd.to_numeric(r2raw[resolve_col(r2raw,name)],errors="coerce"); v=s.where(~s.isin([-9,-8,-7])); d[f"cap_{name}"]=(v==key).astype(float); d.loc[v.isna(),f"cap_{name}"]=np.nan; objective.append(f"cap_{name}")
    d["cap_objective_pc_internet"]=d[objective].sum(axis=1,min_count=1)
    selfrep=[]
    for i in range(1,12):
        name=f"p10_a{i}"; s=pd.to_numeric(r2raw[resolve_col(r2raw,name)],errors="coerce"); v=s.where(~s.isin([-9,-8,-7])); d[f"cap_selfrep_{i}"]=(v==1).astype(float); d.loc[v.isna(),f"cap_selfrep_{i}"]=np.nan; selfrep.append(f"cap_selfrep_{i}")
    d["cap_selfreported_pc_internet"]=d[selfrep].sum(axis=1,min_count=1)
    return d,["cap_objective_pc_internet","cap_selfreported_pc_internet"]+objective+selfrep


def build_raven(root: Path):
    path=locate(root,"matrices_g3-6_r2.dta"); x,_=read_dta(path); cod=resolve_col(x,"codest")
    series=[*(f"serie_a_{i:02d}" for i in range(1,13)),*(f"serie_ab_{i:02d}" for i in range(1,13)),*(f"serie_b_{i:02d}" for i in range(1,13))]; cols=[resolve_col(x,n) for n in series]
    score=pd.Series(0.0,index=x.index); answered=pd.Series(0,index=x.index,dtype="int64")
    for col,key in zip(cols,RAVEN_KEY):
        v=pd.to_numeric(x[col],errors="coerce"); valid=v.notna() & ~v.isin([-9,-8,-7]); score += (v.eq(key)&valid).astype(float); answered += valid.astype("int64")
    score=score.where(answered.gt(0)); return pd.DataFrame({"codest":x[cod],"raven_r2":score}),path,"reconstructed_from_matrices_g3-6_r2_via_published_rename_and_key"


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--data-root",type=Path,default=DEFAULT_ROOT); ap.add_argument("--output-dir",type=Path,default=Path("03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output")); args=ap.parse_args()
    root,out=args.data_root.resolve(),args.output_dir.resolve(); out.mkdir(parents=True,exist_ok=True)
    if not root.exists(): raise RuntimeError(f"DATA_ROOT_NOT_FOUND:{root}")
    paths={n:locate(root,n) for n in ["listas_final.dta","school_pairs_final.dta","cestudiante_g3-6_p2_r1.dta","cestudiante_g3-6_p1_r2.dta","cestudiante_g3-6_p2_r2.dta","matrices_g3-6_r2.dta"]}; inventory=[{"file":n,"bytes":p.stat().st_size,"sha256":sha256_file(p)} for n,p in paths.items()]
    lists,_=read_dta(paths["listas_final.dta"]); pairs,_=read_dta(paths["school_pairs_final.dta"]); r1raw,_=read_dta(paths["cestudiante_g3-6_p2_r1.dta"]); r2raw,_=read_dta(paths["cestudiante_g3-6_p2_r2.dta"])
    lists=lists.rename(columns={resolve_col(lists,"codest"):"codest"}); r1raw=r1raw.rename(columns={resolve_col(r1raw,"codest"):"codest"}); r2raw=r2raw.rename(columns={resolve_col(r2raw,"codest"):"codest"})
    assignment=["codest","participated_in_lottery","won_lottery","received_laptop","treatment_school"]; [resolve_col(lists,c) for c in assignment[1:]]
    if any(x["codest"].duplicated().any() for x in [lists,r1raw,r2raw]): raise RuntimeError("NON_UNIQUE_STUDENT_KEY")
    r1=r1raw.merge(lists[assignment],on="codest",how="left",validate="one_to_one");
    if r1["won_lottery"].isna().any(): raise RuntimeError("ASSIGNMENT_LINK_FAIL")
    for c in ["P2","P3","P4"]+[f"P12_A{i}" for i in range(1,9)]: resolve_col(r1,c)
    for c,outc in [("P2","Tacc0_resource_computer"),("P3","Tacc0_resource_internet"),("P4","Tacc0_resource_prior_use")]: r1[outc]=binary_yes(r1[resolve_col(r1,c)])
    caps0=[]
    for i in range(1,9): n=f"Tacc0_cap_A{i}"; r1[n]=binary_yes(r1[resolve_col(r1,f"P12_A{i}")]); caps0.append(n)
    r1["Tacc0_capacity_count"]=r1[caps0].sum(axis=1,min_count=1)
    r2acc=r2raw[["codest",resolve_col(r2raw,"P1"),resolve_col(r2raw,"P2"),resolve_col(r2raw,"P3")]].copy(); r2acc.columns=["codest","P1","P2","P3"]
    for c,outc in [("P1","Tacc1_resource_computer"),("P2","Tacc1_resource_internet"),("P3","Tacc1_resource_prior_use")]: r2acc[outc]=binary_yes(r2acc[c])
    d=r1.merge(r2acc,on="codest",how="inner",validate="one_to_one")
    for c in ["won_lottery","received_laptop","treatment_school"]: d[c]=pd.to_numeric(d[c],errors="coerce")
    d["Z"]=d["won_lottery"].where(d["won_lottery"].isin([0,1]))
    for base,a,b in [("computer","Tacc1_resource_computer","Tacc0_resource_computer"),("internet","Tacc1_resource_internet","Tacc0_resource_internet"),("prior_use","Tacc1_resource_prior_use","Tacc0_resource_prior_use")]: d[f"delta_{base}"]=d[a]-d[b]
    d["delta_resource_count"]=d[["Tacc1_resource_computer","Tacc1_resource_internet","Tacc1_resource_prior_use"]].sum(axis=1,min_count=1)-d[["Tacc0_resource_computer","Tacc0_resource_internet","Tacc0_resource_prior_use"]].sum(axis=1,min_count=1)
    trajectory,trajectory_variables=derive_trajectory(r2raw); d=d.merge(trajectory,on="codest",how="inner",validate="one_to_one")
    capabilities,capability_variables=build_capabilities(r2raw); d=d.merge(capabilities,on="codest",how="inner",validate="one_to_one")
    raven,raven_path,raven_mode=build_raven(root); d=d.merge(raven,on="codest",how="left",validate="one_to_one")
    if d["raven_r2"].dropna().empty: raise RuntimeError("RAVEN_RECONSTRUCTION_EMPTY")
    if not bool(d["raven_r2"].dropna().between(0,36).all()): raise RuntimeError("RAVEN_OUT_OF_RANGE")
    contrasts={f"Z_to_{x}":mean_diff(d,x,"Z") for x in ["delta_computer","delta_internet","delta_prior_use","delta_resource_count"]+trajectory_variables+capability_variables[:2]+["raven_r2"]}
    pair=resolve_col(pairs,"pair"); pt=resolve_col(pairs,"treatment_school"); pc=pairs.groupby(pair)[pt].agg(["count","sum"]); pair_valid=bool((pc["count"]==2).all() and (pc["sum"]==1).all())
    school_cross=pd.crosstab(d["Z"],d["treatment_school"]).to_dict()
    receipt_cross=pd.crosstab(d["Z"],d["received_laptop"]).to_dict()
    identity={"Z_definition":"won_lottery","receipt_definition":"received_laptop","school_condition_definition":"treatment_school","Z_vs_receipt_crosstab":receipt_cross,"Z_vs_school_condition_crosstab":school_cross,"school_pair_structure_valid":pair_valid}
    first_stage=any(v["diff"] is not None and abs(v["diff"])>0 for k,v in contrasts.items() if k.startswith("Z_to_delta_")); trajectory_present=any(v["diff"] is not None and abs(v["diff"])>0 for k,v in contrasts.items() if k.startswith("Z_to_trajectory_")); verdict="FAIL" if not first_stage else "PARTIAL/INCONCLUSIVE"; note="No measurable bounded accessibility change was reconstructed from Z in the tested indicators." if not first_stage else "Bounded accessibility transition and downstream trajectory/capability contrasts are reconstructed, but no accessibility-mediated causal effect is inferred without an explicit identification/exclusion argument."
    result={"spec":SPEC,"version":"0.5","status":verdict,"causal_note":note,"data_root":str(root),"inventory":inventory,"environment":{"python":sys.version,"platform":platform.platform(),"pandas":pd.__version__,"pyreadstat":getattr(pyreadstat,"__version__","unknown")},"n":{"lists":len(lists),"r1":len(r1),"r2":len(r2raw),"paired_r1_r2":len(d)},"identity":identity,"trajectory_variables":trajectory_variables,"capability_variables":capability_variables,"capability_source_semantics":"Published input_r2.do section 13.6: objective PC/Internet test and self-reported PC/Internet skills","trajectory_source_semantics":"Published input_r2.do: P4 duration; P5 weekly use by place; P6 weekly use by activity; P7 Internet use","raven_source":str(raven_path),"raven_mode":raven_mode,"raven_key":RAVEN_KEY,"raven_definition":"sum of 36 keyed item indicators; missing/nonresponse not counted; score constrained to [0,36]","contrasts":contrasts,"first_stage_present":first_stage,"trajectory_contrast_present":trajectory_present,"output_schema":list(d.columns)}
    result_path=out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_RESULT_001.json"; result_path.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8")
    export=["codest","Z","received_laptop","treatment_school","Tacc0_capacity_count","Tacc0_resource_computer","Tacc0_resource_internet","Tacc0_resource_prior_use","Tacc1_resource_computer","Tacc1_resource_internet","Tacc1_resource_prior_use","delta_computer","delta_internet","delta_prior_use","delta_resource_count"]+trajectory_variables+capability_variables+["raven_r2"]; audit_path=out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_AUDIT_DATA_001.csv"; d[[c for c in export if c in d.columns]].to_csv(audit_path,index=False)
    log_path=out/"C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_EXECUTION_LOG_001.txt"; log_path.write_text(f"SPEC={SPEC}\nVERSION=0.5\nSTATUS={verdict}\nDATA_ROOT={root}\nRESULT={result_path}\nRESULT_SHA256={sha256_file(result_path)}\nAUDIT_DATA_SHA256={sha256_file(audit_path)}\n",encoding="utf-8")
    print(json.dumps({"status":verdict,"result":str(result_path),"audit_data":str(audit_path),"log":str(log_path)},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
