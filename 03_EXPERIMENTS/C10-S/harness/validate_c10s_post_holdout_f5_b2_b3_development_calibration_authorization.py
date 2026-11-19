"""Fail-closed one-use authorization validator for F5 B2/B3 development calibration."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

AUTH_PATH = "00_GOVERNANCE/authorizations/C10S_POST_HOLDOUT_F5_B2_B3_DEVELOPMENT_CALIBRATION_AUTHORIZATION.json"
BRANCH_PREFIX = "research/c10s-f1-f5-dev-cal-auth-"
SPEC_PATH = "03_EXPERIMENTS/C10-S/diagnostics/C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md"
RUNNER_PATH = "03_EXPERIMENTS/C10-S/harness/run_c10s_post_holdout_f5_b2_b3_development_calibration.py"
HOLDOUT_GENERATOR_PATH = "03_EXPERIMENTS/C10-S/harness/run_c10s_nested_mr_comparative_holdout.py"
FIXTURES_PATH = "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_fixtures.py"
ENGINE_PATH = "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py"
BOOTSTRAP_PATH = "03_EXPERIMENTS/C10-S/harness/c10s_fitted_beta_binomial_bootstrap.py"
DIAGNOSTICS_PATH = "03_EXPERIMENTS/C10-S/harness/c10s_f5_beta_binomial_likelihood_diagnostics.py"
INTERFACE_PATH = "03_EXPERIMENTS/C10-S/harness/c10s_variance_comparison_interface.py"
ORACLE_PATH = "03_EXPERIMENTS/C10-S/harness/c10s_beta_binomial_variance_oracles.py"
LOCK_PATH = "03_EXPERIMENTS/C10-S/harness/requirements-vcont-integrated.lock"
WORKFLOW_PATH = ".github/workflows/c10-s-post-holdout-f5-b2-b3-development-calibration.yml"
VALIDATOR_PATH = "03_EXPERIMENTS/C10-S/harness/validate_c10s_post_holdout_f5_b2_b3_development_calibration_authorization.py"
AUTH_SCHEMA = "TGCV-C10S-POST-HOLDOUT-F5-B2-B3-DEVELOPMENT-CALIBRATION-AUTH-001"
SPEC_ID = "C10S-POST-HOLDOUT-F1-F5-DEVELOPMENT-CALIBRATION-SPEC-001"
SEED_SCHEDULE_ID = "C10S_POST_HOLDOUT_F1_F5_DEV_CAL_SEEDS_1.0"
EXPECTED_CELLS = ["F5_beta22_M10_R5", "F5_beta22_M30_R20"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def validate(path: Path, root: Path, workflow_commit: str, branch: str) -> dict:
    if not branch.startswith(BRANCH_PREFIX):
        raise ValueError("dedicated F5 B2/B3 authorization branch required")
    auth = json.loads(path.read_text(encoding="utf-8"))
    if auth.get("schema") != AUTH_SCHEMA or auth.get("status") != "APPROVED":
        raise ValueError("authorization is absent, malformed or not APPROVED")
    authorization_id = auth.get("authorization_id")
    if not isinstance(authorization_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{7,63}", authorization_id):
        raise ValueError("invalid authorization_id")
    if branch != BRANCH_PREFIX + authorization_id:
        raise ValueError("branch does not encode authorization_id")
    if auth.get("authorization_branch") != branch:
        raise ValueError("authorization_branch mismatch")
    if auth.get("scope") != "C10S_F5_B2_B3_DEVELOPMENT_CALIBRATION_ONLY":
        raise ValueError("F5 B2/B3 authorization scope mismatch")
    flags = {
        "f5_b2_b3_authorized": True,
        "f1_a2_a3_authorized": False,
        "tier_b_authorized": False,
        "comparative_holdout_authorized": False,
        "c10_scientific_execution_authorized": False,
        "mcse_interval_construction_authorized": False,
    }
    for key, expected in flags.items():
        if auth.get(key) is not expected:
            raise ValueError(f"authorization scope flag mismatch: {key}")
    if auth.get("approved_by") != "USER_EXPLICIT_APPROVAL":
        raise ValueError("approved_by must record explicit user approval")
    approved = auth.get("approved_at_utc")
    expires = auth.get("expires_utc")
    if not isinstance(approved, str) or not isinstance(expires, str):
        raise ValueError("approval and expiry timestamps required")
    approved_at = datetime.fromisoformat(approved.replace("Z", "+00:00"))
    expires_at = datetime.fromisoformat(expires.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    if approved_at.tzinfo is None or expires_at.tzinfo is None or approved_at > now or expires_at <= now or expires_at <= approved_at:
        raise ValueError("invalid or expired UTC authorization window")
    if auth.get("spec_id") != SPEC_ID or auth.get("spec_version") != "1.0":
        raise ValueError("frozen development specification identity mismatch")
    if auth.get("seed_schedule_id") != SEED_SCHEDULE_ID:
        raise ValueError("frozen development seed schedule mismatch")
    exact_values = {
        "cells": EXPECTED_CELLS,
        "k_calibration_per_cell": 5000,
        "k_validation_per_cell": 5000,
        "c0_bootstrap_replicates": 1000,
        "c5_bootstrap_replicates": 1000,
        "b3_selected_per_cell": 250,
        "b3_bootstrap_b1000": 1000,
        "b3_bootstrap_b4000": 4000,
    }
    for key, expected in exact_values.items():
        if auth.get(key) != expected:
            raise ValueError(f"frozen F5 B2/B3 value mismatch: {key}")
    if auth.get("b3_selection_rule") != "SHA256(schedule_id|B3_SELECTION|cell_id|dataset_id), ascending, first 250":
        raise ValueError("B3 outcome-independent selection rule mismatch")
    code_commit = auth.get("approved_code_commit")
    if not isinstance(code_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", code_commit):
        raise ValueError("approved_code_commit must be a full SHA")
    if git("rev-parse", "HEAD") != workflow_commit:
        raise ValueError("authorization checkout differs from workflow commit")
    parents = git("rev-list", "--parents", "-n", "1", workflow_commit).split()
    if len(parents) != 2 or parents[1] != code_commit:
        raise ValueError("authorization commit must have approved code commit as sole parent")
    changed = git("diff-tree", "--no-commit-id", "--name-only", "-r", workflow_commit).splitlines()
    if changed != [AUTH_PATH]:
        raise ValueError("authorization commit may change only the authorization JSON")
    expected_hashes = {
        "spec_sha256": SPEC_PATH,
        "runner_sha256": RUNNER_PATH,
        "holdout_generator_sha256": HOLDOUT_GENERATOR_PATH,
        "fixtures_sha256": FIXTURES_PATH,
        "engine_sha256": ENGINE_PATH,
        "bootstrap_sha256": BOOTSTRAP_PATH,
        "diagnostics_sha256": DIAGNOSTICS_PATH,
        "interface_sha256": INTERFACE_PATH,
        "oracle_sha256": ORACLE_PATH,
        "dependency_lock_sha256": LOCK_PATH,
        "workflow_sha256": WORKFLOW_PATH,
        "validator_sha256": VALIDATOR_PATH,
    }
    for key, relative in expected_hashes.items():
        if auth.get(key) != sha256(root / relative):
            raise ValueError(f"{key} mismatch for {relative}")
    return {
        "validation_status": "PASS",
        "authorization_id": authorization_id,
        "authorization_commit": workflow_commit,
        "approved_code_commit": code_commit,
        "authorization_sha256": sha256(path),
        "scope": auth["scope"],
        "f5_b2_b3_authorized": True,
        "f1_a2_a3_authorized": False,
        "tier_b_authorized": False,
        "comparative_holdout_authorized": False,
        "c10_scientific_execution_authorized": False,
        "mcse_interval_construction_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authorization", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--workflow-commit", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    args = parser.parse_args()
    result = validate(args.authorization, args.root, args.workflow_commit, args.branch)
    args.output_json.write_text(json.dumps(result, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
