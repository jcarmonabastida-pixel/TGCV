"""Fail-closed one-use authorization validator for comparative C0/C1/C5 holdout."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

AUTH_PATH = "00_GOVERNANCE/authorizations/C10S_NESTED_MR_COMPARATIVE_HOLDOUT_AUTHORIZATION.json"
BRANCH_PREFIX = "research/c10s-nested-mr-comparative-auth-"
PROTOCOL_PATH = "03_EXPERIMENTS/C10-S/diagnostics/C10S_NESTED_MR_COMPARATIVE_HOLDOUT_PROTOCOL_001.md"
RUNNER_PATH = "03_EXPERIMENTS/C10-S/harness/run_c10s_nested_mr_comparative_holdout.py"
ENGINE_PATH = "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py"
FIXTURES_PATH = "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_fixtures.py"
LOCK_PATH = "03_EXPERIMENTS/C10-S/harness/requirements-vcont-integrated.lock"
WORKFLOW_PATH = ".github/workflows/c10-s-nested-mr-comparative-holdout.yml"
EXECUTOR_PATH = "03_EXPERIMENTS/C10-S/harness/execute_c10s_nested_mr_comparative_holdout.py"
VALIDATOR_PATH = "03_EXPERIMENTS/C10-S/harness/validate_c10s_nested_mr_comparative_holdout_authorization.py"
PROTOCOL_ID = "C10S-NESTED-MR-COMPARATIVE-HOLDOUT-PROTOCOL-001"
PROTOCOL_VERSION = "1.0"
AUTH_SCHEMA = "TGCV-C10S-COMPARATIVE-HOLDOUT-AUTH-001"
EXPECTED_CELLS = (
    "F1_balanced_M10_R5", "F1_balanced_M30_R20",
    "F1_high_between_M10_R5", "F1_high_between_M30_R20",
    "F1_low_between_M10_R5", "F1_low_between_M30_R20",
    "F5_beta22_M10_R5", "F5_beta22_M30_R20",
)


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
        raise ValueError("dedicated comparative authorization branch required")
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
    if auth.get("scope") != "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_ONLY":
        raise ValueError("authorization scope mismatch")
    if auth.get("comparative_holdout_authorized") is not True:
        raise ValueError("explicit comparative holdout approval required")
    if auth.get("c10_scientific_execution_authorized") is not False:
        raise ValueError("C10 scientific execution must remain false")
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
    if auth.get("protocol_id") != PROTOCOL_ID or auth.get("protocol_version") != PROTOCOL_VERSION:
        raise ValueError("protocol identity mismatch")
    if auth.get("k_per_cell") != 1000 or auth.get("c0_bootstrap_replicates") != 1000 or auth.get("c5_bootstrap_replicates") != 1000:
        raise ValueError("frozen K/B values mismatch")
    if auth.get("cells") != list(EXPECTED_CELLS):
        raise ValueError("frozen eight-cell roster mismatch")
    if auth.get("profile_diagnostics_enabled") is not False or auth.get("tier_b_authorized") is not False:
        raise ValueError("explicit exclusions missing")
    if auth.get("primary_replay_required") is not True:
        raise ValueError("primary/replay requirement missing")
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
    expected = {
        "protocol_sha256": PROTOCOL_PATH,
        "runner_sha256": RUNNER_PATH,
        "engine_sha256": ENGINE_PATH,
        "fixtures_sha256": FIXTURES_PATH,
        "dependency_lock_sha256": LOCK_PATH,
        "workflow_sha256": WORKFLOW_PATH,
        "executor_sha256": EXECUTOR_PATH,
        "validator_sha256": VALIDATOR_PATH,
    }
    for key, relative in expected.items():
        if auth.get(key) != sha256(root / relative):
            raise ValueError(f"{key} mismatch for {relative}")
    return {
        "authorization_id": authorization_id,
        "approved_code_commit": code_commit,
        "protocol_sha256": auth["protocol_sha256"],
        "scope": auth["scope"],
        "k_per_cell": auth["k_per_cell"],
        "c0_bootstrap_replicates": auth["c0_bootstrap_replicates"],
        "c5_bootstrap_replicates": auth["c5_bootstrap_replicates"],
        "cells": auth["cells"],
        "primary_replay_required": True,
        "authorization_sha256": sha256(path),
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
