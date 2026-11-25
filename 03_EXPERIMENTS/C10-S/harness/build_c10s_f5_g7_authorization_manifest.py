"""Build G7 authorization hash bindings from the canonical immutable Git manifests.

The tool can emit a sidecar and, optionally, a new DRAFT authorization from a
DRAFT template. It never approves, dispatches, or consumes an authorization.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from c10s_f5_g7_source_inventory import build_manifests, execution_source_hash_paths

BINDINGS_SCHEMA = "TGCV-C10S-F5-G7-AUTHORIZATION-MANIFEST-BINDINGS-001"


def build_authorization_manifest_bindings(root: Path, approved_code_commit: str) -> dict:
    """Derive every authorization hash field from the validator's canonical manifests."""
    manifests = build_manifests(root, approved_code_commit)
    execution = manifests["execution_source"]
    compute = manifests["compute_path"]

    path_hashes = {entry["path"]: entry["sha256"] for entry in execution["entries"]}
    key_to_path = execution_source_hash_paths()
    if set(path_hashes) != set(key_to_path.values()):
        raise ValueError("G7_AUTHORIZATION_BINDINGS_EXECUTION_PATH_SET_MISMATCH")

    source_hashes = {
        key: path_hashes[relative]
        for key, relative in sorted(key_to_path.items())
    }
    if len(source_hashes) != len(key_to_path):
        raise ValueError("G7_AUTHORIZATION_BINDINGS_HASH_KEY_COLLISION")

    return {
        "schema": BINDINGS_SCHEMA,
        "approved_code_commit": approved_code_commit,
        "execution_source_manifest_sha256": execution["root_sha256"],
        "compute_path_content_sha256": compute["content_sha256"],
        "source_hashes": source_hashes,
    }


def build_draft_authorization(template: dict, bindings: dict) -> dict:
    """Apply canonical bindings to a DRAFT template; never approve or consume it."""
    if template.get("status") != "DRAFT":
        raise ValueError("G7_AUTHORIZATION_TEMPLATE_MUST_BE_DRAFT")
    if bindings.get("schema") != BINDINGS_SCHEMA:
        raise ValueError("G7_AUTHORIZATION_BINDINGS_SCHEMA_MISMATCH")
    source_hashes = bindings.get("source_hashes")
    if not isinstance(source_hashes, dict):
        raise ValueError("G7_AUTHORIZATION_BINDINGS_SOURCE_HASHES_INVALID")

    draft = dict(template)
    draft["approved_code_commit"] = bindings["approved_code_commit"]
    draft["execution_source_manifest_sha256"] = bindings["execution_source_manifest_sha256"]
    draft["compute_path_content_sha256"] = bindings["compute_path_content_sha256"]
    draft.update(source_hashes)
    draft["status"] = "DRAFT"
    return draft


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build canonical G7 manifest bindings and optionally a DRAFT authorization."
    )
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--approved-code-commit", required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--draft-template", type=Path)
    parser.add_argument("--output-draft-authorization", type=Path)
    args = parser.parse_args()
    if bool(args.draft_template) != bool(args.output_draft_authorization):
        parser.error("--draft-template and --output-draft-authorization must be supplied together")

    bindings = build_authorization_manifest_bindings(args.root, args.approved_code_commit)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(bindings, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    if args.draft_template:
        template = json.loads(args.draft_template.read_text(encoding="utf-8"))
        draft = build_draft_authorization(template, bindings)
        args.output_draft_authorization.parent.mkdir(parents=True, exist_ok=True)
        args.output_draft_authorization.write_text(
            json.dumps(draft, sort_keys=True, indent=2, allow_nan=False) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
