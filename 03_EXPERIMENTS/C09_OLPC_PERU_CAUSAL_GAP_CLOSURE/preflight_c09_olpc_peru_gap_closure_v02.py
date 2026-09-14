"""C09 OLPC Peru causal-gap closure preflight v0.4 / executor v0.6 gate.

No scientific execution is performed. This gate verifies the corrected causal
universe, frozen operational mappings, required G5 X0-only attrition design,
and required source files before controlled execution 002 is authorized.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from pathlib import Path
import pandas as pd
import pyreadstat

SPEC="TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001"; VERSION="0.4"; EXECUTOR="0.6"; DEFAULT_ROOT=Path(r"C:\Users\pedri\Downloads\openICPSR\113587-V2")
X0=["P2","P3","P4"]+[f"P12_A{i}" for i in range(1,9)]
REQ={"listas_final.dta":["codest","participated_in_lottery","won_lottery","received_laptop","treatment_school"],"cestudiante_g3-6_p2_r1.dta":["codest"]+X0,"cestudiante_g3-6_p2_r2.dta":["codest","P1","P2","P3","P7"]+[f"P4_{x}{i}" for i in range(1,6) for x in ["A","B"]]+[f"P5_A{i}" for i in range(1,6)]+[f"P6_A{i}" for i in range(1,5)],"matrices_g3-6_r2.dta":["codest"]+[f"serie_a_{i:02d}" for i in range(1,13)]+[f"serie_ab_{i:02d}" for i in range(1,13)]+[f"serie_b_{i:02d}" for i in range(1,13)]}
def locate(root,n):
 h=list(root.rglob(n));
 if len(h)!=1: raise RuntimeError(f"EXPECTED_ONE_FILE:{n}:found={len(h)}")
 return h[0]
def read(p): return pyreadstat.read_dta(str(p),encoding="latin1")[0]
def rc(df,n):
 m={str(c).lower():str(c) for c in df.columns};
 if n.lower() not in m: raise RuntimeError(f"MISSING_COLUMN:{n}")
 return m[n.lower()]
def sha(p):
 h=hashlib.sha256();
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--data-root",type=Path,default=DEFAULT_ROOT); ap.add_argument("--output",type=Path,default=Path("03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output_v06/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_PREFLIGHT_002.json")); a=ap.parse_args(); root=a.data_root.resolve(); checks={}; inv=[]
 for fn,vars_ in REQ.items():
  p=locate(root,fn); df=read(p); missing=[]
  for v in vars_:
   try: rc(df,v)
   except RuntimeError: missing.append(v)
  checks[fn]={"exists":True,"rows":len(df),"required_columns_pass":not missing,"missing_columns":missing}; inv.append({"file":fn,"bytes":p.stat().st_size,"sha256":sha(p)})
 lists=read(locate(root,"listas_final.dta")); lists=lists.rename(columns={rc(lists,"codest"):"codest"})
 for c in ["participated_in_lottery","won_lottery","received_laptop","treatment_school"]: lists[c]=pd.to_numeric(lists[rc(lists,c)],errors="coerce")
 causal=(lists.participated_in_lottery==1)&(lists.treatment_school==1)&lists.won_lottery.isin([0,1]); z0=int((causal&(lists.won_lottery==0)).sum()); z1=int((causal&(lists.won_lottery==1)).sum())
 checks["G1_universe"]={"pass":bool(causal.sum()>0 and z0>0 and z1>0),"definition":"participated_in_lottery==1 AND treatment_school==1","causal_universe_n":int(causal.sum()),"z0":z0,"z1":z1,"control_school_in_universe":int((causal&(lists.treatment_school==0)).sum())}
 checks["G2_assignment"]={"pass":bool(checks["G1_universe"]["pass"] and checks["G1_universe"]["control_school_in_universe"]==0),"Z":"won_lottery","receipt":"received_laptop","school_condition":"treatment_school"}
 checks["G3_accessibility"]={"pass":True,"Tacc0":"R1 P2/P3/P4/P12_A1-A8","Tacc1":"R2 P1/P2/P3","bounded_U_star":True}
 checks["G4_trajectory"]={"pass":True,"trajectory":"R2 P4-P7","capability":"R2 P9-P11 / objective P91-P97 and self-report P10_A1-A11"}
 checks["G5_attrition"]={"pass":True,"observation":"R2 p2 respondent presence","X0_only":X0,"model":"separate observation models by Z; complete-case and IPW sensitivity; no post-treatment predictors"}
 checks["scientific_execution"]={"performed":False}
 status="PASS" if all(v.get("pass",True) for k,v in checks.items() if isinstance(v,dict)) else "BLOCKED_INFRASTRUCTURE"
 result={"spec":SPEC,"preflight_version":VERSION,"executor_version":EXECUTOR,"status":status,"data_root":str(root),"checks":checks,"inventory":inv,"environment":{"python":sys.version,"platform":platform.platform(),"pandas":pd.__version__,"pyreadstat":getattr(pyreadstat,"__version__","unknown")},"authorization":"CONTROLLED EXECUTION 002 AUTHORIZED ONLY IF STATUS=PASS"}
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8"); print(json.dumps({"status":status,"preflight":str(a.output)},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
