"""N-R4A conformance runner.

Checks the prospective snapshot generator only. Scientific execution is NOT performed.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
IMPL = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src" / "branch_n_r4a_generator_v01.py"


def load_module():
    spec = importlib.util.spec_from_file_location("branch_n_r4a_generator_v01", IMPL)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load implementation")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main():
    m = load_module()
    checks = []

    train = m.generate_dataset(100, 3100000)
    test = m.generate_dataset(100, 4100000)

    # Exact schema and domain checks.
    for records, label in ((train, "train"), (test, "test")):
        assert len(records) == 100
        for r in records:
            assert set(r) == {"episode_id", "components", "edges", "resources", "objective"}
            m.validate_record(r)
        checks.append({"name": f"{label}_schema_and_domain", "status": "PASS"})

    # Canonical representation and unique episode ids.
    assert [r["episode_id"] for r in train] == list(range(100))
    assert [r["episode_id"] for r in test] == list(range(100))
    checks.append({"name": "episode_id_canonical", "status": "PASS"})

    # Same-seed determinism.
    train2 = m.generate_dataset(100, 3100000)
    test2 = m.generate_dataset(100, 4100000)
    train_bytes = m.canonical_json_bytes(train)
    test_bytes = m.canonical_json_bytes(test)
    assert train_bytes == m.canonical_json_bytes(train2)
    assert test_bytes == m.canonical_json_bytes(test2)
    checks.append({"name": "same_seed_byte_identity", "status": "PASS"})

    # Split seed separation and corpus distinction.
    assert train_bytes != test_bytes
    checks.append({"name": "train_test_seed_separation", "status": "PASS"})

    # Rerun digest stability.
    assert digest(train_bytes) == digest(m.canonical_json_bytes(train2))
    assert digest(test_bytes) == digest(m.canonical_json_bytes(test2))
    checks.append({"name": "rerun_sha256_identity", "status": "PASS"})

    # No outcome/future fields at snapshot boundary.
    forbidden = {"outcome", "label", "success", "trajectory", "future_state", "future_transformations", "prediction"}
    for r in train + test:
        assert not (set(r) & forbidden)
    checks.append({"name": "snapshot_future_outcome_boundary", "status": "PASS"})

    # Generation is self-contained: no scientific learner or historical result.
    checks.append({"name": "scientific_execution", "status": "NOT_PERFORMED"})

    impl_bytes = IMPL.read_bytes()
    result = {
        "checks": checks,
        "implementation_path": str(IMPL),
        "implementation_sha256": digest(impl_bytes),
        "train_smoke_count": 100,
        "test_smoke_count": 100,
        "train_sha256": digest(train_bytes),
        "test_sha256": digest(test_bytes),
        "runner": "N_R4A_CONFORMANCE_RUNNER_v0.1",
        "scientific_execution": "NOT_PERFORMED",
        "status": "PASS"
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
