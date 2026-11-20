"""Execute one validated F5 G7 authorization: resource preflight, primary and replay."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from run_c10s_f5_g7_tiera_calibration import execute_g7
from validate_c10s_f5_g7_tiera_authorization import (
    AUTH_PATH,
    SOURCE_HASH_PATHS,
    sha256_file,
)


def execute(validated_path: Path, original_authorization_path: Path,
            code_commit: str, output_dir: Path, root: Path) -> dict:
    validated = json.loads(validated_path.read_text(encoding="utf-8"))
    original = json.loads(original_authorization_path.read_text(encoding="utf-8"))
    required = {
        "authorization_id", "authorization_sha256", "approved_code_commit",
        "protocol_sha256", "scope", "primary_replay_required",
    }
    if not required.issubset(validated):
        raise ValueError("validated G7 authorization payload incomplete")
    if validated["approved_code_commit"] != code_commit:
        raise ValueError("G7 approved code commit mismatch")
    if validated["scope"] != "C10S_F5_G7_TIERA_PROSPECTIVE_CALIBRATION_ONLY":
        raise ValueError("G7 scope mismatch")
    if validated["primary_replay_required"] is not True:
        raise ValueError("G7 primary/replay requirement missing")
    if original.get("authorization_id") != validated["authorization_id"]:
        raise ValueError("original/validated authorization ID mismatch")
    if sha256_file(original_authorization_path) != validated["authorization_sha256"]:
        raise ValueError("original G7 authorization digest mismatch")
    for key, relative in SOURCE_HASH_PATHS.items():
        if original.get(key) != sha256_file(root / relative):
            raise ValueError(f"G7 source inventory mismatch: {relative}")
    if original.get("protocol_sha256") != validated["protocol_sha256"]:
        raise ValueError("G7 protocol digest mismatch")

    result = execute_g7(output_dir, code_commit=code_commit)
    result_path = output_dir / "g7_result.json"
    final = json.loads(result_path.read_text(encoding="utf-8"))
    final["authorization_id"] = validated["authorization_id"]
    final["authorization_sha256"] = validated["authorization_sha256"]
    final["protocol_sha256"] = validated["protocol_sha256"]
    result_bytes = json.dumps(final, sort_keys=True, indent=2, allow_nan=False) + "\n"
    result_path.write_text(result_bytes, encoding="utf-8")
    result_digest = hashlib.sha256(result_bytes.encode("utf-8")).hexdigest()
    files = {}
    for path in sorted(output_dir.rglob("*")):
        if path.is_file() and path.name != "run_manifest.json":
            files[str(path.relative_to(output_dir))] = sha256_file(path)
    manifest = {
        "schema": "TGCV-C10S-F5-G7-AUTHORIZED-MANIFEST-001",
        "authorization_id": validated["authorization_id"],
        "authorization_sha256": validated["authorization_sha256"],
        "protocol_sha256": validated["protocol_sha256"],
        "code_commit": code_commit,
        "status": final["status"],
        "primary_replay_digest": final["primary_replay_digest"],
        "result_sha256": result_digest,
        "artifact_files_sha256": files,
        "resource_preflight": final["resource_preflight"],
    }
    (output_dir / "run_manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    return {
        "authorization_id": validated["authorization_id"],
        "code_commit": code_commit,
        "status": final["status"],
        "primary_replay_digest": final["primary_replay_digest"],
        "result_sha256": result_digest,
        "artifact_files": len(files),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validated-authorization", type=Path, required=True)
    parser.add_argument("--original-authorization", type=Path, required=True)
    parser.add_argument("--code-commit", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    print(json.dumps(execute(
        args.validated_authorization, args.original_authorization,
        args.code_commit, args.output_dir, args.root,
    ), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
