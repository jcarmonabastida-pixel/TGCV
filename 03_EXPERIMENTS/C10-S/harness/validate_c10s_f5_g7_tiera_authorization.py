"""Fail-closed one-use authorization validator for F5 G7 Tier-A calibration."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

AUTH_PATH = "00_GOVERNANCE/authorizations/C10S_F5_G7_TIERA_CALIBRATION_AUTHORIZATION.json"
BRANCH_PREFIX = "research/c10s-f5-g7-auth-"
PROTOCOL_PATH = "03_EXPERIMENTS/C10-S/design/C10S_F5_G7_TIERA_PROSPECTIVE_PROTOCOL_002.md"
RESOURCE_PROFILE_MANIFEST_PATH = "03_EXPERIMENTS/C10-S/fixtures/g7_resource_profile_v1_1/manifest.json"
from c10s_f5_g7_source_inventory import execution_source_hash_paths

SOURCE_HASH_PATHS = execution_source_hash_paths()

PROTOCOL_ID = "C10S-F5-G7-TIERA-PROSPECTIVE-001"
PROTOCOL_VERSION = "1.1"
AUTH_SCHEMA = "TGCV-C10S-F5-G7-TIERA-AUTH-002"
EXPECTED_CELLS = ("F5_beta22_M10_R5", "F5_beta22_M30_R20")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def validate(path: Path, root: Path, workflow_commit: str, branch: str) -> dict:
    if not branch.startswith(BRANCH_PREFIX):
        raise ValueError("dedicated F5 G7 authorization branch required")
    auth = json.loads(path.read_text(encoding="utf-8"))
    if auth.get("schema") != AUTH_SCHEMA or auth.get("status") != "APPROVED":
        raise ValueError("authorization absent, malformed or not APPROVED")
    authorization_id = auth.get("authorization_id")
    if not isinstance(authorization_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{7,63}", authorization_id):
        raise ValueError("invalid authorization_id")
    if branch != BRANCH_PREFIX + authorization_id or auth.get("authorization_branch") != branch:
        raise ValueError("authorization branch identity mismatch")
    if auth.get("scope") != "C10S_F5_G7_TIERA_PROSPECTIVE_CALIBRATION_ONLY":
        raise ValueError("G7 scope mismatch")
    if auth.get("g7_tiera_calibration_authorized") is not True:
        raise ValueError("explicit G7 calibration authorization required")
    if auth.get("approved_by") != "USER_EXPLICIT_APPROVAL":
        raise ValueError("approved_by must record explicit user approval")
    if auth.get("tier_b_authorized") is not False or auth.get("c10_scientific_execution_authorized") is not False:
        raise ValueError("Tier B and C10 causal execution must remain false")
    if auth.get("primary_replay_required") is not True:
        raise ValueError("primary/replay requirement missing")
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
        raise ValueError("G7 protocol identity mismatch")
    if auth.get("cells") != list(EXPECTED_CELLS):
        raise ValueError("G7 frozen F5 cell roster mismatch")
    if (auth.get("k_per_cell"), auth.get("c0_bootstrap_replicates"), auth.get("c5_bootstrap_replicates")) != (1000, 1000, 1000):
        raise ValueError("G7 frozen K/B mismatch")
    if auth.get("resource_preflight_k_per_cell") != 100:
        raise ValueError("G7 resource preflight K mismatch")
    if auth.get("execution_architecture_id") != "C10S-F5-G7-EXECUTION-ARCHITECTURE-002":
        raise ValueError("G7 staged execution architecture mismatch")
    if (auth.get("max_job_minutes"), auth.get("max_parallel_jobs")) != (150, 20):
        raise ValueError("G7 execution budget or parallelism mismatch")
    profile_manifest = json.loads((root / RESOURCE_PROFILE_MANIFEST_PATH).read_text(encoding="utf-8"))
    if profile_manifest.get("schema") != "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-002":
        raise ValueError("G7 resource profile manifest schema mismatch")
    if (
        auth.get("resource_profile_run_id") != profile_manifest.get("profile_run_id")
        or auth.get("resource_profile_artifact_id") != profile_manifest.get("profile_artifact_id")
        or auth.get("resource_profile_source_commit") != profile_manifest.get("profile_source_commit")
        or auth.get("resource_profile_artifact_archive_sha256") != profile_manifest.get("profile_artifact_archive_sha256")
        or auth.get("resource_profile_sha256") != profile_manifest.get("profile_json_sha256")
        or auth.get("resource_profile_scope") != "RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_TIMING_ONLY_NO_OUTCOME_INSPECTION_NO_COVERAGE_NO_HOLDOUT"
        or auth.get("resource_profile_seed_namespace") != "c10s_f5_g7_resource_v1_1"
    ):
        raise ValueError("G7 resource profile provenance mismatch")
    if auth.get("seed_schedule_id") != "C10S_F5_G7_TIERA_SEEDS_1.1":
        raise ValueError("G7 seed schedule mismatch")
    if auth.get("holdout_seed_namespace") != "c10s_f5_g7_holdout_v1_1" or auth.get("resource_seed_namespace") != "c10s_f5_g7_resource_v1_1":
        raise ValueError("G7 seed namespace mismatch")
    code_commit = auth.get("approved_code_commit")
    if not isinstance(code_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", code_commit):
        raise ValueError("approved_code_commit must be full SHA")
    if git("rev-parse", "HEAD") != workflow_commit:
        raise ValueError("authorization checkout differs from workflow commit")
    parents = git("rev-list", "--parents", "-n", "1", workflow_commit).split()
    if len(parents) != 2 or parents[1] != code_commit:
        raise ValueError("authorization commit must have approved code commit as sole parent")
    changed = git("diff-tree", "--no-commit-id", "--name-only", "-r", workflow_commit).splitlines()
    if changed != [AUTH_PATH]:
        raise ValueError("authorization commit may change only the G7 authorization JSON")
    for key, relative in SOURCE_HASH_PATHS.items():
        if auth.get(key) != sha256_file(root / relative):
            raise ValueError(f"{key} mismatch for {relative}")
    return {
        "authorization_id": authorization_id,
        "authorization_sha256": sha256_file(path),
        "approved_code_commit": code_commit,
        "protocol_sha256": auth["protocol_sha256"],
        "scope": auth["scope"],
        "k_per_cell": 1000,
        "c0_bootstrap_replicates": 1000,
        "c5_bootstrap_replicates": 1000,
        "resource_preflight_k_per_cell": 100,
        "execution_architecture_id": "C10S-F5-G7-EXECUTION-ARCHITECTURE-002",
        "resource_profile_run_id": auth["resource_profile_run_id"],
        "resource_profile_artifact_id": auth["resource_profile_artifact_id"],
        "resource_profile_source_commit": auth["resource_profile_source_commit"],
        "resource_profile_sha256": auth["resource_profile_sha256"],
        "resource_profile_artifact_archive_sha256": auth["resource_profile_artifact_archive_sha256"],
        "max_job_minutes": 150,
        "max_parallel_jobs": 20,
        "cells": list(EXPECTED_CELLS),
        "primary_replay_required": True,
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
