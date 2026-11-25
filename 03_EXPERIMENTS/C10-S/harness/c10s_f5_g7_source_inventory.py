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
