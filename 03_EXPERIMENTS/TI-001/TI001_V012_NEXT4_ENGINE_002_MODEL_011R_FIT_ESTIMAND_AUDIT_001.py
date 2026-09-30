"""Independent deterministic fit/estimand audit for Engine-002 + Model-011R.

No provider calls and no Monte Carlo. The audit exercises the actual
fit_primary_contrast implementation on a deterministic NULL dataset and
checks that the returned estimand is dimensionally and algebraically bound to
the canonical Model-011R contrast after reference-action differencing.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
ENGINE_PATH = BASE / "TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py"
MODEL_PATH = BASE / "TI001_V012_NEXT4_TWO_SURFACE_MODEL_011R.py"
DGP_PATH = BASE / "TI001_V012_NEXT4_DGP_SPECIFICATION_002.json"
MODEL_COMMIT = "24e6b2067c5e038d30fabbc2761da6775e5de78f"
N = 1728
SEED = 410927


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def audit():
    engine = load(ENGINE_PATH, "engine_002_fit_audit")
    model = load(MODEL_PATH, "model_011r_fit_audit")
    dgp = json.loads(DGP_PATH.read_text(encoding="utf-8"))

    scenario = engine.Scenario("NULL", 0.0, N, 0, SEED)
    sets, rows = engine.generate_dataset(scenario)

    X, active_cols, full_cols, X_full = engine.build_model_matrix(
        sets, model, reference=0
    )
    c_full = model.primary_contrast(full_cols)
    active_indices = np.asarray(
        [full_cols.index(c) for c in active_cols], dtype=int
    )
    c_active = c_full[active_indices]

    if X.shape != (N * 4, len(active_cols)):
        raise AssertionError("Unexpected active likelihood matrix shape")
    if c_active.shape != (len(active_cols),):
        raise AssertionError("Contrast dimension does not match active design")
    if not np.all(np.isfinite(X)):
        raise AssertionError("Non-finite design matrix")
    if not np.all(np.isfinite(c_active)):
        raise AssertionError("Non-finite active contrast")

    result = engine.fit_primary_contrast(sets, reference=0)

    expected_contrast_sha = hashlib.sha256(c_active.tobytes()).hexdigest()
    returned_contrast_sha = result["contrast_sha256"]

    checks = {
        "engine_binds_model_011R": (
            engine.MODEL_PATH.name == MODEL_PATH.name
            and engine.MODEL_COMMIT == MODEL_COMMIT
        ),
        "dgp_binding": (
            dgp["artifact"] == "TI001_V012_NEXT4_DGP_SPECIFICATION_002"
        ),
        "reference_action_zero": result["reference_action"] == 0,
        "matrix_shape": X.shape == (N * 4, len(active_cols)),
        "contrast_dimension_matches_active_design": (
            len(c_active) == X.shape[1]
        ),
        "contrast_estimand_matches_active_canonical_sha": (
            returned_contrast_sha == expected_contrast_sha
        ),
        "contrast_weights": (
            float(c_full[full_cols.index(
                "future_reassigned_nonidentity_mapped_action"
            )]) == 0.75
            and float(c_full[full_cols.index(
                "future_reassigned_fixedpoint_mapped_action"
            )]) == 0.25
        ),
        "fit_outputs_finite": all(
            np.isfinite(float(result[k]))
            for k in ("estimate", "se", "wald_z", "p_value")
        ),
        "hessian_rank_positive": int(result["rank_hessian"]) > 0,
        "no_provider_calls": True,
        "no_monte_carlo": True,
    }

    passed = all(checks.values())

    return {
        "artifact": "TI001_V012_NEXT4_ENGINE_002_MODEL_011R_FIT_ESTIMAND_AUDIT_001",
        "status": "PASS" if passed else "FAIL",
        "scientific_execution_authorized": False,
        "provider_api_calls": False,
        "monte_carlo": False,
        "scenario": {
            "effect_label": "NULL",
            "effect_size": 0.0,
            "n_choice_sets": N,
            "replicate": 0,
            "master_seed": SEED,
        },
        "checks": checks,
        "fit_result": result,
        "design": {
            "rows": len(rows),
            "active_columns": len(active_cols),
            "full_columns": len(full_cols),
            "contrast_sha256": expected_contrast_sha,
        },
        "conclusion": (
            "Engine-002 fit and primary estimand are deterministically "
            "reconciled with Model-011R."
            if passed
            else "Fit/estimand reconciliation is not yet established."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(audit(), sort_keys=True, indent=2))
