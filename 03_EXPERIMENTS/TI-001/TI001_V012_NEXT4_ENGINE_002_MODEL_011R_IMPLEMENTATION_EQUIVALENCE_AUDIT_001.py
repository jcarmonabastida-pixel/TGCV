"""Independent Engine-002 -> Model-011R reconciliation audit.

Deterministic only. No provider calls, no Monte Carlo, no fitted scientific
result. Verifies source binding, action-level design construction, reference
differencing, retained signal columns, and exact primary-contrast propagation.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
ENGINE_PATH = BASE / "TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py"
MODEL_PATH = BASE / "TI001_V012_NEXT4_TWO_SURFACE_MODEL_011R.py"
DGP_PATH = BASE / "TI001_V012_NEXT4_DGP_SPECIFICATION_002.json"
MODEL_COMMIT = "24e6b2067c5e038d30fabbc2761da6775e5de78f"
CANDIDATE_N = (1728, 2304, 3456, 5184, 6912)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def audit_one(engine, model, n):
    scenario = engine.Scenario("NULL", 0.0, n, 0, 410927)
    sets, rows = engine.generate_dataset(scenario)

    X_engine, active_cols, all_cols, X_full_engine = engine.build_model_matrix(
        sets, model, reference=0
    )

    X_canonical, canonical_cols = model.build_matrix(rows)
    if canonical_cols != all_cols:
        raise AssertionError("Engine column order differs from Model-011R")

    X4 = X_canonical.reshape(n, 4, len(all_cols))
    X_expected = X4 - X4[:, [0], :]
    active_expected = np.any(
        np.abs(X_expected[:, 1:, :]) > 0, axis=(0, 1)
    )
    expected_indices = np.flatnonzero(active_expected)
    X_expected_active = X_expected[:, :, expected_indices]
    expected_active_cols = [all_cols[i] for i in expected_indices]

    design_error = float(np.max(np.abs(X_engine - X_expected_active)))
    active_column_match = active_cols == expected_active_cols

    c_full = model.primary_contrast(all_cols)
    active_indices = np.flatnonzero(active_expected)
    c_active = c_full[active_indices]

    signal_names = (
        "future_reassigned_nonidentity_mapped_action",
        "future_reassigned_fixedpoint_mapped_action",
    )
    signal_indices = [all_cols.index(x) for x in signal_names]
    signal_active = [int(i in set(active_indices)) for i in signal_indices]

    return {
        "N": n,
        "choice_sets": len(sets),
        "action_rows": len(rows),
        "full_parameter_columns": len(all_cols),
        "active_parameter_columns": len(active_cols),
        "design_max_absolute_error": design_error,
        "active_column_order_match": active_column_match,
        "signal_columns_retained": all(signal_active),
        "primary_contrast_sha256": hashlib.sha256(c_full.tobytes()).hexdigest(),
        "active_contrast_nonzero": bool(np.any(np.abs(c_active) > 0)),
        "contrast_weights": {
            "nonidentity": float(
                c_full[all_cols.index(signal_names[0])]
            ),
            "fixedpoint": float(
                c_full[all_cols.index(signal_names[1])]
            ),
        },
        "model_matrix_sha256": hashlib.sha256(
            X_canonical.tobytes()
        ).hexdigest(),
    }


def audit():
    engine = load(ENGINE_PATH, "engine_002")
    model = load(MODEL_PATH, "model_011r")
    dgp = json.loads(DGP_PATH.read_text(encoding="utf-8"))

    source_binding = (
        engine.MODEL_PATH.name == MODEL_PATH.name
        and engine.MODEL_COMMIT == MODEL_COMMIT
        and dgp["artifact"] == "TI001_V012_NEXT4_DGP_SPECIFICATION_002"
    )

    rows = [audit_one(engine, model, n) for n in CANDIDATE_N]

    pass_design = all(
        x["design_max_absolute_error"] <= 0
        and x["active_column_order_match"]
        and x["signal_columns_retained"]
        and x["active_contrast_nonzero"]
        and x["contrast_weights"]["nonidentity"] == 0.75
        and x["contrast_weights"]["fixedpoint"] == 0.25
        for x in rows
    )

    return {
        "artifact": "TI001_V012_NEXT4_ENGINE_002_MODEL_011R_IMPLEMENTATION_EQUIVALENCE_AUDIT_001",
        "status": "PASS" if source_binding and pass_design else "FAIL",
        "scientific_execution_authorized": False,
        "monte_carlo": False,
        "provider_calls": False,
        "checks": {
            "engine_binds_model_011R": source_binding,
            "engine_reproduces_model_011R_reference_differencing": pass_design,
            "primary_contrast_weights": "0.75 / 0.25",
            "candidate_N_all_checked": True,
        },
        "candidate_results": rows,
        "conclusion": (
            "Engine-002 is reconciled to Model-011R at the deterministic "
            "design/contrast level."
            if source_binding and pass_design
            else "Engine-002 is not yet reconciled to Model-011R."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(audit(), sort_keys=True, indent=2))
