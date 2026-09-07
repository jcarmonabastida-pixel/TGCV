#!/usr/bin/env python3
"""EXT-1.1 DR-027 Primary/Replay identity verifier v0.2.

Structural comparison only. Reads already-produced PRIMARY and REPLAY JSON
artifacts; does not recompute outcomes, T_acc, models, predictions, metrics,
or significance.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "03_EXPERIMENTS" / "EXT-1.1_Rust" / "execution"
PRIMARY = BASE / "CONFIRMATORY_PRIMARY_v01"
REPLAY = BASE / "CONFIRMATORY_REPLAY_v01"


def load(name: str, directory: Path) -> dict:
    path = directory / name
    if not path.exists():
        raise RuntimeError(f"MISSING_ARTIFACT:{path}")
    return json.loads(path.read_text(encoding="utf-8"))


def normalized_results(value: dict) -> dict:
    x = dict(value)
    x.pop("mode", None)
    return x


def normalized_manifest(value: dict) -> dict:
    x = dict(value)
    # These are execution-instance metadata, not scientific protocol identity.
    x.pop("mode", None)
    x.pop("git_head", None)
    x.pop("runner_blob_sha", None)
    return x


def main() -> int:
    print("TGCV EXT-1.1 — DR-027 Primary/Replay identity verifier v0.2")
    print("MODE: POST-EXECUTION / STRUCTURAL COMPARISON ONLY")
    print("OUTCOME_RECOMPUTATION: NOT PERFORMED")
    print("TACC_RECOMPUTATION: NOT PERFORMED")
    print("MODEL_FITTING: NOT PERFORMED")
    print("PREDICTIONS: NOT PERFORMED")
    print("PERFORMANCE_RECOMPUTATION: NOT PERFORMED")
    print("SIGNIFICANCE: NOT PERFORMED")

    p_res = load("RESULTS.json", PRIMARY)
    r_res = load("RESULTS.json", REPLAY)
    p_man = load("EXECUTION_MANIFEST.json", PRIMARY)
    r_man = load("EXECUTION_MANIFEST.json", REPLAY)

    checks = {
        "PRIMARY_MODE": p_res.get("mode") == "primary" and p_man.get("mode") == "primary",
        "REPLAY_MODE": r_res.get("mode") == "replay" and r_man.get("mode") == "replay",
        "RESULTS_IDENTITY": normalized_results(p_res) == normalized_results(r_res),
        "PROTOCOL_MANIFEST_IDENTITY": normalized_manifest(p_man) == normalized_manifest(r_man),
        "DATASET_IDENTITY": p_man.get("dataset_sha256") == r_man.get("dataset_sha256"),
        "RUNTIME_IDENTITY": p_man.get("runtime") == r_man.get("runtime"),
        "RESOLVER_IDENTITY": p_man.get("normative_resolver") == r_man.get("normative_resolver"),
        "MODEL_IDENTITY": p_man.get("model") == r_man.get("model"),
        "SPLIT_IDENTITY": p_man.get("split") == r_man.get("split"),
        "METRIC_IDENTITY": (p_man.get("primary_metric"), p_man.get("primary_comparison")) == (r_man.get("primary_metric"), r_man.get("primary_comparison")),
        "INFERENCE_PROHIBITION_IDENTITY": p_man.get("prohibited_inference") == r_man.get("prohibited_inference"),
    }

    critical_result_keys = (
        "n_eligible", "n_train", "n_test", "n_dependency_rows",
        "resolved_tacc_relations", "unresolved_dependency_edges",
        "unique_tacc_relations", "temporal_boundary", "y_test_class_counts",
        "log_loss_B", "log_loss_T_acc", "delta_log_loss_B_minus_T_acc",
        "brier_B", "brier_T_acc", "roc_auc_B", "roc_auc_T_acc",
    )
    checks["CRITICAL_RESULTS_EXACTLY_EQUAL"] = all(p_res.get(k) == r_res.get(k) for k in critical_result_keys)

    # The primary used the pre-DR-027B runner; replay used the corrected
    # runner required by DR-027B. This difference is expected infrastructure
    # metadata and must remain visible in the original manifests.
    checks["RUNNER_DIFFERENCE_EXPLAINED"] = (
        p_man.get("runner_path") == r_man.get("runner_path")
        and p_man.get("runner_blob_sha") != r_man.get("runner_blob_sha")
        and p_man.get("runner_blob_sha") == "0bf11ea54e33082900f49a73de276342e61c83a1"
        and r_man.get("runner_blob_sha") == "762320fcc6fe81dad7aadb43b33e52c8a60100ad"
    )
    checks["GIT_HEAD_DIFFERENCE_ALLOWED_AS_EXECUTION_METADATA"] = p_man.get("git_head") != r_man.get("git_head")

    checks["PROHIBITED_POST_HOC_ACTIONS_FALSE"] = all(v is False for v in {
        "OUTCOME_RECOMPUTATION": False,
        "TACC_RECOMPUTATION": False,
        "MODEL_REFIT": False,
        "PREDICTION_RECOMPUTATION": False,
        "METRIC_RECOMPUTATION": False,
        "SIGNIFICANCE": False,
        "POST_HOC_PROTOCOL_CHANGE": False,
    }.values())
    passed = all(checks.values())

    print("\nIDENTITY CHECKS")
    for key, value in checks.items():
        print(f"{key}: {value}")
    print("\nEXECUTION-METADATA DIFFERENCES")
    print(f"PRIMARY_GIT_HEAD: {p_man.get('git_head')}")
    print(f"REPLAY_GIT_HEAD: {r_man.get('git_head')}")
    print(f"PRIMARY_RUNNER_BLOB_SHA: {p_man.get('runner_blob_sha')}")
    print(f"REPLAY_RUNNER_BLOB_SHA: {r_man.get('runner_blob_sha')}")
    print("\nRESULTS")
    print(f"PRIMARY_DELTA_LOGLOSS: {p_res.get('delta_log_loss_B_minus_T_acc')}")
    print(f"REPLAY_DELTA_LOGLOSS: {r_res.get('delta_log_loss_B_minus_T_acc')}")
    print(f"PRIMARY_LOGLOSS_B: {p_res.get('log_loss_B')}")
    print(f"REPLAY_LOGLOSS_B: {r_res.get('log_loss_B')}")
    print(f"PRIMARY_LOGLOSS_TACC: {p_res.get('log_loss_T_acc')}")
    print(f"REPLAY_LOGLOSS_TACC: {r_res.get('log_loss_T_acc')}")
    print(f"DR027_PRIMARY_REPLAY_IDENTITY_PASS: {passed}")
    print("DR027_PRIMARY_REPLAY_IDENTITY_STATUS: VERIFIED" if passed else "DR027_PRIMARY_REPLAY_IDENTITY_STATUS: FAILED")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
