"""Execute an already validated comparative-holdout authorization, primary and replay."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from run_c10s_nested_mr_comparative_holdout import (
    PROTOCOL_PATH,
    run_holdout_checkpointed,
    verify_replay_identity,
    write_result_bundle,
)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def execute(authorization_path: Path, original_authorization_path: Path, code_commit: str, output_dir: Path, root: Path) -> dict:
    auth = json.loads(authorization_path.read_text(encoding="utf-8"))
    required = {
        "authorization_id", "approved_code_commit", "protocol_sha256",
        "authorization_sha256", "scope", "k_per_cell",
        "c0_bootstrap_replicates", "c5_bootstrap_replicates",
        "primary_replay_required",
    }
    if not required.issubset(auth):
        raise ValueError("validated authorization payload incomplete")
    if auth["approved_code_commit"] != code_commit:
        raise ValueError("approved code commit mismatch")
    if auth["scope"] != "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_ONLY":
        raise ValueError("authorization scope mismatch")
    if auth["primary_replay_required"] is not True:
        raise ValueError("primary/replay gate required")
    source_paths = (
        PROTOCOL_PATH,
        "03_EXPERIMENTS/C10-S/harness/run_c10s_nested_mr_comparative_holdout.py",
        "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py",
        "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_fixtures.py",
        "03_EXPERIMENTS/C10-S/harness/requirements-vcont-integrated.lock",
        "03_EXPERIMENTS/C10-S/harness/execute_c10s_nested_mr_comparative_holdout.py",
        "03_EXPERIMENTS/C10-S/harness/validate_c10s_nested_mr_comparative_holdout_authorization.py",
        ".github/workflows/c10-s-nested-mr-comparative-holdout.yml",
    )
    inventory = {name: file_sha256(root / name) for name in source_paths}
    if file_sha256(root / PROTOCOL_PATH) != auth["protocol_sha256"]:
        raise ValueError("protocol hash differs from validated authorization")
    if file_sha256(original_authorization_path) != auth["authorization_sha256"]:
        raise ValueError("validated authorization payload hash mismatch")
    primary_dir = output_dir / "primary"
    replay_dir = output_dir / "replay"
    common = {
        "code_commit": code_commit,
        "protocol_sha256": auth["protocol_sha256"],
        "source_inventory": inventory,
        "k": auth["k_per_cell"],
        "c0_b": auth["c0_bootstrap_replicates"],
        "c5_b": auth["c5_bootstrap_replicates"],
    }
    primary = run_holdout_checkpointed(primary_dir, **common)
    replay = run_holdout_checkpointed(replay_dir, **common)
    replay_digest = verify_replay_identity(primary, replay)
    primary["status"] = "EXECUTED_UNDER_APPROVED_AUTHORIZATION"
    primary["authorization_id"] = auth["authorization_id"]
    primary["authorization_sha256"] = auth["authorization_sha256"]
    primary["primary_replay_digest"] = replay_digest
    primary["replay_status"] = "EXACT_MATCH"
    hashes = write_result_bundle(primary, output_dir / "final")
    return {
        "authorization_id": auth["authorization_id"],
        "code_commit": code_commit,
        "protocol_sha256": auth["protocol_sha256"],
        "datasets": primary["total_datasets"],
        "cells": primary["cell_count"],
        "primary_replay_digest": replay_digest,
        "result_hashes": hashes,
        "status": primary["status"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validated-authorization", type=Path, required=True)
    parser.add_argument("--original-authorization", type=Path, required=True)
    parser.add_argument("--code-commit", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    result = execute(args.validated_authorization, args.original_authorization, args.code_commit, args.output_dir, args.root)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
