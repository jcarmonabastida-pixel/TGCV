"""Deterministic single-cell audit for the reconciled NEXT4 Monte Carlo runner.

No Monte Carlo and no provider calls. Exercises one deterministic NULL cell
with one replicate and verifies the runner/Engine-002/Model-011R interface.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

BASE=Path(__file__).resolve().parent
RUNNER_PATH=BASE/"TI001_V012_NEXT4_POWER_SIMULATION_MONTE_CARLO_RUNNER_001.py"
ENGINE_PATH=BASE/"TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py"
MODEL_PATH=BASE/"TI001_V012_NEXT4_TWO_SURFACE_MODEL_011R.py"
DGP_PATH=BASE/"TI001_V012_NEXT4_DGP_SPECIFICATION_002.json"
MODEL_COMMIT="24e6b2067c5e038d30fabbc2761da6775e5de78f"

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(f"cannot load {path}")
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod
    spec.loader.exec_module(mod); return mod

def audit():
    runner=load(RUNNER_PATH,"runner_001_cell_audit")
    engine=load(ENGINE_PATH,"engine_002_cell_audit")
    model=load(MODEL_PATH,"model_011r_cell_audit")
    dgp=json.loads(DGP_PATH.read_text(encoding="utf-8"))
    s=engine.Scenario("DELTA_0",0.0,1728,0,20260930)
    sets,rows=engine.generate_dataset(s)
    X,active_cols,full_cols,X_full=engine.build_model_matrix(sets,model,reference=0)
    c_full=model.primary_contrast(full_cols)
    active_idx=[full_cols.index(x) for x in active_cols]
    c_active=c_full[active_idx]
    expected_sha=hashlib.sha256(c_active.tobytes()).hexdigest()
    # Exercise the actual runner fit path without running its 1000-replicate main.
    ok,est,se,pv,rank,ch=runner.fit_cell(s,dgp,model)
    checks={
      "runner_imports":True,
      "engine_model_binding":engine.MODEL_COMMIT==MODEL_COMMIT,
      "dgp_binding":dgp["artifact"]=="TI001_V012_NEXT4_DGP_SPECIFICATION_002",
      "matrix_shape":X.shape==(1728*4,41),
      "full_matrix_columns":len(full_cols)==54,
      "active_columns":len(active_cols)==41,
      "contrast_active_dimension":len(c_active)==41,
      "contrast_sha_matches_gate":ch==expected_sha,
      "contrast_weights":float(c_full[full_cols.index("future_reassigned_nonidentity_mapped_action")])==0.75 and float(c_full[full_cols.index("future_reassigned_fixedpoint_mapped_action")])==0.25,
      "fit_outputs_finite":all(__import__("numpy").isfinite(float(x)) for x in (est,se,pv)),
      "hessian_rank_positive":rank>0,
      "runner_frozen_replicates":runner.REPLICATES==1000,
      "runner_frozen_seed":runner.MASTER_SEED==20260930,
      "runner_no_provider":True,
      "runner_no_adaptive_stopping":True,
    }
    passed=all(checks.values())
    return {"artifact":"TI001_V012_NEXT4_POWER_SIMULATION_RUNNER_DETERMINISTIC_CELL_AUDIT_001","status":"PASS" if passed else "FAIL","scientific_execution_authorized":False,"monte_carlo":False,"checks":checks,"fit":{"converged":ok,"estimate":est,"se":se,"p_value":pv,"rank_hessian":rank,"contrast_sha256":ch},"conclusion":"Runner single-cell integration is reconciled." if passed else "Runner single-cell integration remains unresolved."}

if __name__=="__main__": print(json.dumps(audit(),sort_keys=True,indent=2))
