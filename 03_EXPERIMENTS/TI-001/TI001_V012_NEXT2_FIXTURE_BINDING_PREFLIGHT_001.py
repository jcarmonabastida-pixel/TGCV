#!/usr/bin/env python3
"""Binding preflight for TI-001 V012 NEXT2 regenerated fixture candidate."""

import hashlib
import json
import sys
from pathlib import Path

REPO = Path("/mnt/c/Users/pedri/TGCV")
CANDIDATE = Path("/tmp/TI001_V012_NEXT2_FIXTURE_REGENERATED_001")
REGISTER = REPO / "03_EXPERIMENTS/TI-001/TI001_V012_NEXT2_FIXTURE_REGENERATED_001_SHA256SUMS.json"
REQUIREMENTS = REPO / "03_EXPERIMENTS/TI-001/TI001_V012_NEXT2_FIXTURE_REQUIREMENTS_001.json"
SEMANTICS = REPO / "03_EXPERIMENTS/TI-001/TI001_V012_NEXT2_MAPPING_SEMANTICS_001.json"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def fail(msg):
    print("FIXTURE_BINDING_PREFLIGHT_FAIL")
    print(msg)
    raise SystemExit(1)

def main():
    for p in (CANDIDATE, REGISTER, REQUIREMENTS, SEMANTICS):
        if not p.exists():
            fail("MISSING: " + str(p))

    reg = load(REGISTER)
    man = load(CANDIDATE / "MANIFEST.json")
    req = load(REQUIREMENTS)
    sem = load(SEMANTICS)

    checks = {}

    checks["version"] = man.get("immutable_version") == reg["immutable_version"] == sem["immutable_version"] == req["immutable_version"]
    checks["requirements_hash"] = man.get("requirements_blob_sha256") == reg["requirements_blob_sha256"] == sha256(REQUIREMENTS)
    checks["semantics_hash"] = man.get("semantics_blob_sha256") == reg["semantics_blob_sha256"] == sha256(SEMANTICS)
    checks["unit_count"] = man.get("unit_count") == reg["unit_count"] == 23040
    checks["shard_count"] = man.get("shard_count") == reg["shard_count"] == 24
    checks["units_per_shard"] = man.get("units_per_shard") == reg["units_per_shard"] == 960
    checks["scientific_execution_false"] = man.get("status") == "GENERATED_NOT_FROZEN" and reg.get("scientific_execution") is False
    checks["freeze_not_authorized"] = reg.get("freeze_authorized") is False

    expected = reg["files_sha256"]
    actual = {}
    for name, digest in expected.items():
        path = CANDIDATE / name
        if not path.exists():
            fail("MISSING_CANDIDATE_FILE: " + name)
        actual[name] = sha256(path)
    checks["sha256_all_files"] = actual == expected

    shards = []
    for i in range(1, 25):
        data = load(CANDIDATE / f"SHARD_{i:03d}.json")
        if len(data) != 960:
            fail(f"SHARD_COUNT_FAIL: {i} has {len(data)}")
        shards.extend(data)

    checks["all_units_loaded"] = len(shards) == 23040
    ids = [u["id"] for u in shards]
    checks["ids_unique"] = len(set(ids)) == 23040
    checks["ids_sequential"] = ids == [f"N2-{i:05d}" for i in range(1, 23041)]

    if not all(checks.values()):
        for k, v in checks.items():
            print(f"{k}={v}")
        fail("one or more binding checks failed")

    print(json.dumps({
        "status": "FIXTURE_BINDING_PREFLIGHT_PASS",
        "checks": checks,
        "unit_count": 23040,
        "shard_count": 24,
        "scientific_execution": False,
        "freeze_authorized": False
    }, indent=2))

if __name__ == "__main__":
    main()
