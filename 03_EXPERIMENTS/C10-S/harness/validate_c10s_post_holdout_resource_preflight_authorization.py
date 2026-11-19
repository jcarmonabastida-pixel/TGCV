"""Fail-closed one-use authorization validator for the post-holdout F1/F5 preflight."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

AUTH_PATH = "00_GOVERNANCE/authorizations/C10S_POST_HOLDOUT_F1_F5_RESOURCE_PREFLIGHT_AUTHORIZATION.json"
BRANCH_PREFIX = "research/c10s-post-holdout-resource-preflight-auth-"
SPEC_PATH = "03_EXPERIMENTS/C10-S/diagnostics/C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md"
RUNNER_PATH = "03_EXPERIMENTS/C10-S/harness/run_c10s_post_holdout_f1_f5_resource_preflight.py"
TEST_PATH = "03_EXPERIMENTS/C10-S/harness/test_c10s_post_holdout_f1_f5_resource_preflight.py"
VALIDATOR_PATH = "03_EXPERIMENTS/C10-S/harness/validate_c10s_post_holdout_resource_preflight_authorization.py"
LOCK_PATH = "03_EXPERIMENTS/C10-S/harness/requirements-vcont-integrated.lock"
WORKFLOW_PATH = ".github/workflows/c10-s-post-holdout-f1-f5-resource-preflight.yml"
HASH_PATHS = {
    "spec_sha256": SPEC_PATH,
    "runner_sha256": RUNNER_PATH,
    "test_sha256": TEST_PATH,
    "validator_sha256": VALIDATOR_PATH,
    "dependency_lock_sha256": LOCK_PATH,
    "workflow_sha256": WORKFLOW_PATH,
    "fixtures_sha256": "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_fixtures.py",
    "holdout_generator_sha256": "03_EXPERIMENTS/C10-S/harness/run_c10s_nested_mr_comparative_holdout.py",
    "engine_sha256": "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py",
    "f1_profile_sha256": "03_EXPERIMENTS/C10-S/harness/c10s_f1_between_profile_likelihood.py",
    "f5_bootstrap_sha256": "03_EXPERIMENTS/C10-S/harness/c10s_fitted_beta_binomial_bootstrap.py",
    "f5_diagnostics_sha256": "03_EXPERIMENTS/C10-S/harness/c10s_f5_beta_binomial_likelihood_diagnostics.py",
}
AUTH_SCHEMA = "TGCV-C10S-POST-HOLDOUT-RESOURCE-PREFLIGHT-AUTH-001"
EXPECTED_CELLS = ["F1_balanced_M30_R20", "F5_beta22_M30_R20"]
EXPECTED_CUTOFF = 3.841458820694124

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()

def validate(auth_path: Path, root: Path, workflow_commit: str, branch: str) -> dict:
    if not branch.startswith(BRANCH_PREFIX):
        raise ValueError("dedicated post-holdout resource-preflight authorization branch required")
    auth = json.loads(auth_path.read_text(encoding="utf-8"))
    if auth.get("schema") != AUTH_SCHEMA or auth.get("status") != "APPROVED":
        raise ValueError("post-holdout resource-preflight authorization is not APPROVED")
    authorization_id = auth.get("authorization_id")
    if not isinstance(authorization_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{7,63}", authorization_id):
        raise ValueError("invalid authorization_id")
    if branch != BRANCH_PREFIX + authorization_id or auth.get("authorization_branch") != branch:
        raise ValueError("authorization branch identity mismatch")
    if auth.get("scope") != "C10S_POST_HOLDOUT_F1_F5_RESOURCE_PREFLIGHT_ONLY":
        raise ValueError("scope must be post-holdout F1/F5 resource-preflight-only")
    if auth.get("resource_preflight_authorized") is not True:
        raise ValueError("explicit resource-preflight approval required")
    for key in (
        "calibration_execution_authorized", "validation_execution_authorized",
        "comparative_holdout_authorized", "c10_scientific_execution_authorized",
        "tier_b_authorized",
    ):
        if auth.get(key) is not False:
            raise ValueError(f"{key} must remain false")
    if auth.get("approved_by") != "USER_EXPLICIT_APPROVAL":
        raise ValueError("explicit user approval record required")
    approved = auth.get("approved_at_utc")
    expires = auth.get("expires_utc")
    if not isinstance(approved, str) or not isinstance(expires, str):
        raise ValueError("approval and expiry timestamps required")
    approved_at = datetime.fromisoformat(approved.replace("Z", "+00:00"))
    expires_at = datetime.fromisoformat(expires.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    if (approved_at.tzinfo is None or expires_at.tzinfo is None
            or approved_at > now or expires_at <= now or expires_at <= approved_at):
        raise ValueError("invalid or expired UTC authorization window")
    if auth.get("spec_id") != "C10S-POST-HOLDOUT-F1-F5-DEVELOPMENT-CALIBRATION-SPEC-001" or auth.get("spec_version") != "1.0":
        raise ValueError("frozen development/calibration specification identity mismatch")
    if auth.get("representative_cells") != EXPECTED_CELLS:
        raise ValueError("representative cell roster mismatch")
    if auth.get("k_per_cell") != 100 or auth.get("c0_bootstrap_B") != 1000:
        raise ValueError("resource-preflight K/C0-B mismatch")
    if auth.get("c5_bootstrap_B_primary") != 1000 or auth.get("c5_bootstrap_B_sensitivity") != 4000:
        raise ValueError("resource-preflight C5 bootstrap counts mismatch")
    if auth.get("f1_profile_benchmark_cutoff") != EXPECTED_CUTOFF:
        raise ValueError("F1 benchmark-only cutoff mismatch")
    if auth.get("f1_profile_cutoff_use") != "COMPUTATIONAL_BENCHMARK_ONLY_NO_COVERAGE_OR_CALIBRATION":
        raise ValueError("F1 profile cutoff cannot be used for inferential adjudication")
    code_commit = auth.get("approved_code_commit")
    if not isinstance(code_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", code_commit):
        raise ValueError("approved_code_commit must be a full SHA")
    if git("rev-parse", "HEAD") != workflow_commit:
        raise ValueError("workflow checkout mismatch")
    parents = git("rev-list", "--parents", "-n", "1", workflow_commit).split()
    if len(parents) != 2 or parents[1] != code_commit:
        raise ValueError("authorization commit must have approved code commit as sole parent")
    changed = git("diff-tree", "--no-commit-id", "--name-only", "-r", workflow_commit).splitlines()
    if changed != [AUTH_PATH]:
        raise ValueError("authorization commit may change only its authorization file")
    for key, relative in HASH_PATHS.items():
        if auth.get(key) != sha256(root / relative):
            raise ValueError(f"{key} mismatch")
    return {
        "authorization_id": authorization_id,
        "approved_code_commit": code_commit,
        "authorization_sha256": sha256(auth_path),
        "spec_sha256": auth["spec_sha256"],
        "representative_cells": EXPECTED_CELLS,
        "k_per_cell": 100,
        "c0_bootstrap_B": 1000,
        "c5_bootstrap_B_primary": 1000,
        "c5_bootstrap_B_sensitivity": 4000,
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
