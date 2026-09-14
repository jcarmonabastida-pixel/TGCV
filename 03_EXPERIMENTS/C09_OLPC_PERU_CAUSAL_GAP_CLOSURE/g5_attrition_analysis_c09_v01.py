"""C09 G5 attrition analysis for corrected individual-lottery universe.

G5 is restricted to pre-treatment X0 variables. Observation at R2 is modeled
separately within Z=0 and Z=1, so treatment assignment is never represented by
post-treatment variables and the observation model does not condition on
outcomes. Complete-case and IPW contrasts use the same corrected causal
universe and the same outcome-specific observed sample definition.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, sys
from pathlib import Path
import numpy as np
import pandas as pd
import pyreadstat

VERSION="0.1"
DEFAULT_ROOT=Path(r"C:\Users\pedri\Downloads\openICPSR\113587-V2")
X0_SOURCE=["P2","P3","P4"]+[f"P12_A{i}" for i in range(1,9)]


def read(path): return pyreadstat.read_dta(str(path), encoding="latin1")[0]
def col(df,n):
    m={str(c).lower():str(c) for c in df.columns}
    if n.lower() not in m: raise RuntimeError(f"MISSING:{n}")
    return m[n.lower()]
def sha(p):
    h=hashlib.sha256();
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()
def bin12(s):
    x=pd.to_numeric(s,errors="coerce"); return x.where(x.isin([1,2])).map({1:1,2:0})
def std_diff(a,b):
    a=a.dropna(); b=b.dropna()
    if len(a)<2 or len(b)<2: return None
    den=math.sqrt((a.var(ddof=1)+b.var(ddof=1))/2)
    return None if den==0 else float((a.mean()-b.mean())/den)

def fit_logit_irls(X,y):
    X=np.asarray(X,float); y=np.asarray(y,float)
    X=np.column_stack([np.ones(len(X)),X])
    beta=np.zeros(X.shape[1])
    for _ in range(100):
        eta=np.clip(X@beta,-30,30); p=1/(1+np.exp(-eta)); w=np.clip(p*(1-p),1e-8,None)
        z=eta+(y-p)/w; A=X.T@(w[:,None]*X)+1e-7*np.eye(X.shape[1]); b=X.T@(w*z)
        nb=np.linalg.solve(A,b)
        if np.max(np.abs(nb-beta))<1e-8: beta=nb; break
        beta=nb
    return beta

def predict(X,beta):
    X=np.asarray(X,float); X=np.column_stack([np.ones(len(X)),X]); return 1/(1+np.exp(-np.clip(X@beta,-30,30)))

def weighted_diff(df,y,w):
    q=df[[y,"Z",w]].dropna()
    if q.empty: return None
    out={}
    for z in [0,1]:
        g=q[q.Z==z]; out[f"n_z{z}"]=int(len(g)); out[f"ess_z{z}"]=float(g[w].sum()**2/(g[w]**2).sum()) if len(g) else None
        out[f"mean_z{z}"]=float(np.average(g[y],weights=g[w])) if len(g) else None
    out["diff"]=None if out.get("mean_z0") is None or out.get("mean_z1") is None else out["mean_z1"]-out["mean_z0"]
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--data-root",type=Path,default=DEFAULT_ROOT); ap.add_argument("--output-dir",type=Path,default=Path("03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output_v06")); args=ap.parse_args()
    root=args.data_root.resolve(); out=args.output_dir.resolve(); out.mkdir(parents=True,exist_ok=True)
    lp=next(root.rglob("listas_final.dta")); r1p=next(root.rglob("cestudiante_g3-6_p2_r1.dta")); r2p=next(root.rglob("cestudiante_g3-6_p2_r2.dta"))
    lists=read(lp); r1=read(r1p); r2=read(r2p)
    lists=lists.rename(columns={col(lists,"codest"):"codest"}); r1=r1.rename(columns={col(r1,"codest"):"codest"}); r2=r2.rename(columns={col(r2,"codest"):"codest"})
    for n in ["participated_in_lottery","won_lottery","received_laptop","treatment_school"]: col(lists,n)
    a=lists[["codest","participated_in_lottery","won_lottery","received_laptop","treatment_school"]].copy()
    for n in a.columns[1:]: a[n]=pd.to_numeric(a[n],errors="coerce")
    for n in X0_SOURCE: col(r1,n)
    b=r1[["codest"]+X0_SOURCE].copy()
    for n in X0_SOURCE: b[n]=bin12(b[col(b,n)])
    b=b.rename(columns={n:f"X0_{n}" for n in X0_SOURCE})
    base=a.merge(b,on="codest",how="inner",validate="one_to_one")
    base=base[(base.participated_in_lottery==1)&(base.treatment_school==1)&base.won_lottery.isin([0,1])].copy(); base["Z"]=base.won_lottery.astype(int)
    r2ids=set(r2.codest.tolist()); base["observed_r2"]=base.codest.isin(r2ids).astype(int)
    # Balance observed vs not observed within each arm, using X0 only.
    balance={}
    for z in [0,1]:
        g=base[base.Z==z]; balance[str(z)]={"n":int(len(g)),"observed":int(g.observed_r2.sum()),"not_observed":int((g.observed_r2==0).sum()),"x0":{}}
        for x in [f"X0_{n}" for n in X0_SOURCE]:
            balance[str(z)]["x0"][x]={"observed_mean":None if g.loc[g.observed_r2==1,x].dropna().empty else float(g.loc[g.observed_r2==1,x].mean()),"not_observed_mean":None if g.loc[g.observed_r2==0,x].dropna().empty else float(g.loc[g.observed_r2==0,x].mean()),"standardized_difference":std_diff(g.loc[g.observed_r2==1,x],g.loc[g.observed_r2==0,x])}
    # Separate X0-only observation models by arm.
    xcols=[f"X0_{n}" for n in X0_SOURCE]
    weights=np.full(len(base),np.nan); models={}
    for z in [0,1]:
        idx=base.Z.eq(z); m=base.loc[idx,xcols].copy(); med=m.median(); m=m.fillna(med); valid=m.notna().all(axis=1)
        yy=base.loc[idx,"observed_r2"].astype(float).to_numpy(); X=m.to_numpy(float)
        beta=fit_logit_irls(X,yy); ph=predict(X,beta); ph=np.clip(ph,0.5,1.0); weights[np.flatnonzero(idx.to_numpy())]=1/ph
        models[str(z)]={"variables":xcols,"beta":beta.tolist(),"p_obs_min":float(ph.min()),"p_obs_max":float(ph.max()),"weight_max":float((1/ph).max()),"weight_p99":float(np.quantile(1/ph,.99))}
    base["p_obs"]=np.where(np.isfinite(weights),1/weights,np.nan); base["ipw_weight"]=weights
    ess={str(z):float((base.loc[base.Z==z,"ipw_weight"].sum()**2)/(base.loc[base.Z==z,"ipw_weight"]**2).sum()) for z in [0,1]}
    # Attach downstream outcomes from R2. G5 does not redefine their semantics.
    obs=r2[["codest"]].copy()
    for n in ["P7"]+[f"P4_A{i}" for i in range(1,6)]+[f"P4_B{i}" for i in range(1,6)]+[f"P5_A{i}" for i in range(1,6)]+[f"P6_A{i}" for i in range(1,5)]: col(r2,n)
    for n in obs.columns[1:]: pass
    rr=r2[["codest"]+ [col(r2,n) for n in ["P7"]+[f"P4_A{i}" for i in range(1,6)]+[f"P4_B{i}" for i in range(1,6)]+[f"P5_A{i}" for i in range(1,6)]+[f"P6_A{i}" for i in range(1,5)]]].copy()
    rr.columns=["codest"]+[str(x) for x in rr.columns[1:]]
    p4=[]
    for i in range(1,6):
        aa=pd.to_numeric(rr[f"P4_A{i}"],errors="coerce"); bb=pd.to_numeric(rr[f"P4_B{i}"],errors="coerce"); aa=aa.where(~aa.isin([-9,-8,-7])); bb=bb.where(~bb.isin([-9,-8,-7])); aa=aa.mask(aa.isna()&bb.notna(),0); bb=bb.mask(bb.isna()&aa.notna(),0); rr[f"traj_p4_{i}"]=aa*60+bb; p4.append(f"traj_p4_{i}")
    rr["trajectory_P4_total_minutes"]=rr[p4].sum(axis=1,min_count=1); rr["trajectory_P4_used_yesterday"]=rr["trajectory_P4_total_minutes"].gt(0).astype(float)
    for i in range(1,6): rr[f"p5_{i}"]=bin12(rr[f"P5_A{i}"])
    rr["trajectory_P5_used_week"]=rr[[f"p5_{i}" for i in range(1,6)]].max(axis=1,skipna=True)
    for i in range(1,5): rr[f"p6_{i}"]=bin12(rr[f"P6_A{i}"])
    rr["trajectory_P6_any_activity"]=rr[[f"p6_{i}" for i in range(1,5)]].max(axis=1,skipna=True); rr["trajectory_P7_internet_use"]=bin12(rr["P7"])
    outcomes=["trajectory_P4_total_minutes","trajectory_P4_used_yesterday","trajectory_P5_used_week","trajectory_P6_any_activity","trajectory_P7_internet_use"]
    d=base.merge(rr[["codest"]+outcomes],on="codest",how="left",validate="one_to_one")
    cc={}; ipw={}
    for y in outcomes:
        q=d[["Z",y]].dropna(); cc[y]={"n":int(len(q)),"n_z0":int((q.Z==0).sum()),"n_z1":int((q.Z==1).sum()),"mean_z0":None if q[q.Z==0][y].empty else float(q[q.Z==0][y].mean()),"mean_z1":None if q[q.Z==1][y].empty else float(q[q.Z==1][y].mean())}; cc[y]["diff"]=None if cc[y]["mean_z0"] is None or cc[y]["mean_z1"] is None else cc[y]["mean_z1"]-cc[y]["mean_z0"]
        ipw[y]=weighted_diff(d,y,"ipw_weight")
    result={"spec":"TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE","g5":"PASS_OPERATIONAL","version":VERSION,"causal_universe":"participated_in_lottery==1 AND treatment_school==1","X0":X0_SOURCE,"observation_definition":"codest observed in Round 2 p2 respondent file","n":{"causal_universe":int(len(base)),"z0":int((base.Z==0).sum()),"z1":int((base.Z==1).sum()),"observed_r2":int(base.observed_r2.sum()),"not_observed_r2":int((base.observed_r2==0).sum())},"balance_observed_vs_not_observed":balance,"observation_models":models,"effective_sample_size":ess,"complete_case_contrasts":cc,"ipw_contrasts":ipw,"interpretation":"Observable attrition is assessed operationally under an X0-only MAR/IPW sensitivity framework. IPW does not establish mediation or remove unmeasured attrition bias."}
    rp=out/"C09_OLPC_PERU_G5_ATTRITION_RESULT_001.json"; rp.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8")
    audit=base[["codest","Z","observed_r2","p_obs","ipw_weight"]+xcols]; audit.to_csv(out/"C09_OLPC_PERU_G5_ATTRITION_AUDIT_DATA_001.csv",index=False)
    (out/"C09_OLPC_PERU_G5_ATTRITION_EXECUTION_LOG_001.txt").write_text(f"SPEC=TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE\nG5=PASS_OPERATIONAL\nVERSION={VERSION}\nCAUSAL_UNIVERSE=participated_in_lottery==1 AND treatment_school==1\nX0_ONLY={','.join(X0_SOURCE)}\nRESULT_SHA256={sha(rp)}\n",encoding="utf-8")
    print(json.dumps({"status":"PASS_OPERATIONAL","result":str(rp),"audit_data":str(out/"C09_OLPC_PERU_G5_ATTRITION_AUDIT_DATA_001.csv")},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
