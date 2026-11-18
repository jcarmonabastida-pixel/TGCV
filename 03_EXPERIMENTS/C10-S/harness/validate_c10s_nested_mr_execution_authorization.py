"""Fail-closed validation of a separately committed numerical-run authorization."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from typing import Any

AUTH_SCHEMA = "TGCV-C10S-NESTED-MR-EXECUTION-AUTH-001"
AUTH_PATH = "00_GOVERNANCE/authorizations/C10S_NESTED_MR_NUMERICAL_EXECUTION_AUTHORIZATION.json"
PROTOCOL_PATH = "00_GOVERNANCE/SIP/C10_S_NESTED_MR_BOOTSTRAP_NUMERICAL_VALIDATION_PROTOCOL_DRAFT_001.md"
PROTOCOL_ID = "C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001"
PROTOCOL_VERSION = "002"
METHOD_ID = "TGCV_NESTED_MR_BOOTSTRAP"
METHOD_VERSION = "1.2"
SEED_SCHEDULE_VERSION = "C10S_NESTED_MR_SEED_SCHEDULE_1.0"
AUTH_BRANCH_PREFIX = "research/c10s-nested-mr-auth-"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def validate_authorization(
    authorization_path: Path,
    root: Path,
    workflow_commit: str,
    branch: str,
) -> dict[str, Any]:
    if branch is None or not branch.startswith(AUTH_BRANCH_PREFIX):
        raise ValueError("authorization must be committed on a dedicated numerical-auth branch")
    auth = json.loads(authorization_path.read_text(encoding="utf-8"))
    if auth.get("schema") != AUTH_SCHEMA or auth.get("status") != "APPROVED":
        raise ValueError("authorization record is absent, malformed or not APPROVED")
    if not isinstance(auth.get("authorization_id"), str) or not auth["authorization_id"].strip():
        raise ValueError("authorization_id is required")
    if auth.get("protocol_id") != PROTOCOL_ID or auth.get("protocol_version") != PROTOCOL_VERSION:
        raise ValueError("authorization must bind frozen protocol version 002")
    if auth.get("method_id") != METHOD_ID or auth.get("method_version") != METHOD_VERSION:
        raise ValueError("authorization must bind nested M/R method version 1.2")
    if auth.get("seed_schedule_version") != SEED_SCHEDULE_VERSION:
        raise ValueError("authorization seed schedule does not match")
    tier = auth.get("tier")
    if tier not in {"A", "B"}:
        raise ValueError("authorization tier must be A or B")
    expected_k, expected_b = (1000, 1000) if tier == "A" else (500, 500)
    if auth.get("k_per_cell") != expected_k or auth.get("b_per_dataset") != expected_b:
        raise ValueError("authorization K/B differ from frozen tier values")
    code_commit = auth.get("approved_code_commit")
    if not isinstance(code_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", code_commit):
        raise ValueError("approved_code_commit must be a full 40-character SHA")
    if git("rev-parse", "HEAD") != workflow_commit:
        raise ValueError("workflow checkout does not match triggering authorization commit")
    parents = git("rev-list", "--parents", "-n", "1", workflow_commit).split()
    if len(parents) != 2 or parents[1] != code_commit:
        raise ValueError("authorization commit must have the exact approved code commit as its sole parent")
    changed = git("diff-tree", "--no-commit-id", "--name-only", "-r", workflow_commit).splitlines()
    if changed != [AUTH_PATH]:
        raise ValueError("authorization commit may change only the authorization manifest")
    protocol = root / PROTOCOL_PATH
    if sha256(protocol) != auth.get("protocol_sha256"):
        raise ValueError("authorization protocol SHA-256 does not match frozen protocol bytes")
    if auth.get("authorization_branch") != branch:
        raise ValueError("authorization branch identity mismatch")
    expires = auth.get("expires_utc")
    if not isinstance(expires, str):
        raise ValueError("expires_utc is required")
    expiry = datetime.fromisoformat(expires.replace("Z", "+00:00"))
    if expiry.tzinfo is None or expiry <= datetime.now(timezone.utc):
        raise ValueError("authorization is expired or lacks an explicit UTC offset")
    resume = auth.get("resume_from_run_id")
    if resume is not None and (type(resume) is not int or resume <= 0):
        raise ValueError("resume_from_run_id must be a positive workflow run ID or null")
    return auth


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authorization", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--workflow-commit", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    args = parser.parse_args()
    auth = validate_authorization(
        args.authorization, args.root, args.workflow_commit, args.branch
    )
    output = {
        "authorization_id": auth["authorization_id"],
        "approved_code_commit": auth["approved_code_commit"],
        "tier": auth["tier"],
        "resume_from_run_id": auth.get("resume_from_run_id"),
    }
    args.output_json.write_text(json.dumps(output, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
