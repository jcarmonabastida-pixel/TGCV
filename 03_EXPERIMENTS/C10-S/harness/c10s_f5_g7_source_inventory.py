"""Canonical typed source inventory shared by F5/G7 profile and authorization gates."""
from __future__ import annotations
import json
from pathlib import Path

INVENTORY_PATH = Path(__file__).with_name("c10s_f5_g7_source_inventory.json")

def load_inventory(path: Path = INVENTORY_PATH) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "TGCV-C10S-F5-G7-SOURCE-INVENTORY-001":
        raise ValueError("G7_SOURCE_INVENTORY_SCHEMA_MISMATCH")
    rows = data.get("paths")
    if not isinstance(rows, list) or not rows:
        raise ValueError("G7_SOURCE_INVENTORY_PATHS_REQUIRED")
    seen = set()
    keys = set()
    for row in rows:
        relative = row.get("path")
        roles = row.get("roles")
        if not isinstance(relative, str) or not relative or relative.startswith("/") or ".." in Path(relative).parts:
            raise ValueError("G7_SOURCE_INVENTORY_PATH_INVALID")
        if relative in seen:
            raise ValueError("G7_SOURCE_INVENTORY_DUPLICATE_PATH")
        seen.add(relative)
        if not isinstance(roles, list) or not roles or not set(roles) <= {"compute_path", "execution_source"}:
            raise ValueError("G7_SOURCE_INVENTORY_ROLE_INVALID")
        key = row.get("authorization_hash_key")
        if key is not None:
            if not isinstance(key, str) or key in keys or "execution_source" not in roles:
                raise ValueError("G7_SOURCE_INVENTORY_AUTH_KEY_INVALID")
            keys.add(key)
        if "execution_source" in roles and key is None:
            raise ValueError("G7_SOURCE_INVENTORY_AUTH_KEY_MISSING")
    return data

def compute_path_paths() -> tuple[str, ...]:
    data = load_inventory()
    return tuple(row["path"] for row in data["paths"] if "compute_path" in row["roles"])

def execution_source_hash_paths() -> dict[str, str]:
    data = load_inventory()
    return {row["authorization_hash_key"]: row["path"] for row in data["paths"] if "execution_source" in row["roles"]}

import hashlib
import subprocess

def _canonical_digest(payload: dict) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()

def build_manifests(root: Path, commit: str) -> dict:
    """Derive compute/execution identity manifests from immutable Git tree blobs."""
    if not isinstance(commit, str) or len(commit) != 40 or any(ch not in "0123456789abcdef" for ch in commit):
        raise ValueError("G7_SOURCE_INVENTORY_COMMIT_INVALID")
    data = load_inventory()
    tracked = set(subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", commit], cwd=root, text=True
    ).splitlines())
    result = {}
    for role, schema in (
        ("compute_path", "TGCV-C10S-F5-G7-COMPUTE-PATH-MANIFEST-001"),
        ("execution_source", "TGCV-C10S-F5-G7-EXECUTION-SOURCE-MANIFEST-001"),
    ):
        entries = []
        for row in sorted((item for item in data["paths"] if role in item["roles"]), key=lambda item: item["path"]):
            relative = row["path"]
            if relative not in tracked:
                raise ValueError(f"G7_SOURCE_INVENTORY_PATH_NOT_TRACKED:{relative}")
            blob = subprocess.check_output(["git", "show", f"{commit}:{relative}"], cwd=root)
            entries.append({"path": relative, "sha256": hashlib.sha256(blob).hexdigest()})
        manifest = {"schema": schema, "inventory_schema": data["schema"], "inventory_version": data["version"],
                    "git_commit": commit, "entries": entries}
        manifest["root_sha256"] = _canonical_digest(manifest)
        result[role] = manifest
    return result
