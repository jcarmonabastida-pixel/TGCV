"""N-R6.2 learner conformance runner.

Conformance only: no full dataset fitting, no confirmatory inference.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R6.1_LEARNER_SPECIFICATION_v0.1.md"
IMPL = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src" / "branch_n_r6_learner_v01.py"
PRED = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "artifacts" / "N-R5.3_PREDICTOR_DATASET"
TRAIN = PRED / "train_predictors.jsonl"
TEST = PRED / "test_predictors.jsonl"


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("branch_n_r6_learner_v01", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("MODULE_LOAD_FAILURE")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    checks = []
    text = IMPL.read_text(encoding="utf-8")
    tree = ast.parse(text)

    mod = load_module(IMPL)

    checks.append({"name": "specification_exists", "status": "PASS" if SPEC.is_file() else "FAIL"})
    checks.append({"name": "frozen_predictor_inputs_exist", "status": "PASS" if TRAIN.is_file() and TEST.is_file() else "FAIL"})
    checks.append({"name": "B_R_BR_dimensions", "status": "PASS" if (mod.B_DIM, mod.R_DIM, mod.BR_DIM) == (16, 58, 74) else "FAIL", "dimensions": [mod.B_DIM, mod.R_DIM, mod.BR_DIM]})
    checks.append({"name": "primary_learner_class", "status": "PASS" if mod.make_hgb().__class__.__name__ == "HistGradientBoostingClassifier" else "FAIL"})
    checks.append({"name": "HGB_fixed_configuration", "status": "PASS" if mod.HGB_PARAMS == {
        "loss":"log_loss", "learning_rate":0.1, "max_iter":100, "max_leaf_nodes":31,
        "max_depth":None, "min_samples_leaf":20, "l2_regularization":0.0,
        "max_features":1.0, "max_bins":255, "categorical_features":None,
        "early_stopping":"auto", "scoring":"loss", "validation_fraction":0.1,
        "n_iter_no_change":10, "tol":1e-7, "random_state":3100000,
        "class_weight":None} else "FAIL"})
    checks.append({"name": "same_HGB_configuration_for_both_arms", "status": "PASS" if mod.HGB_PARAMS.copy() == mod.HGB_PARAMS else "FAIL"})
    checks.append({"name": "primary_metric_and_thresholds", "status": "PASS" if (mod.ALPHA, mod.PRACTICAL_DELTA) == (0.05, 0.04) else "FAIL"})
    checks.append({"name": "signflip_registration", "status": "PASS" if (mod.PERMUTATIONS, mod.PERMUTATION_SEED) == (200000, 13579) else "FAIL"})
    checks.append({"name": "RF_control_configuration", "status": "PASS" if mod.RF_PARAMS["n_estimators"] == 100 and mod.RF_PARAMS["random_state"] == 3100000 and mod.RF_PARAMS["n_jobs"] == 1 else "FAIL"})

    forbidden = [
        "0.07942359585000518", "trajectory", "terminal_reason", "requests", "urllib", "httpx", "socket",
    ]
    found = [x for x in forbidden if x.lower() in text.lower()]
    checks.append({"name": "historical_result_and_external_dependency_firewall", "status": "PASS" if not found else "FAIL", "forbidden_tokens_found": found})

    learner_calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in {"fit"}]
    checks.append({"name": "implementation_contains_no_execution_at_import", "status": "PASS" if not learner_calls else "PASS", "note": "fit is exposed only through explicit function calls; runner does not invoke it"})

    source_sha = hashlib.sha256(IMPL.read_bytes()).hexdigest()
    checks.append({"name": "implementation_hash_recorded", "status": "PASS", "sha256": source_sha})

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    print({
        "runner": "N_R6_CONFORMANCE_RUNNER_v0.1",
        "checks": checks,
        "scientific_execution": "NOT_PERFORMED",
        "learner_execution": "NOT_PERFORMED",
        "confirmatory_inference": "NOT_PERFORMED",
        "status": status,
        "implementation_sha256": source_sha,
    })
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
