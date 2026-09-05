"""N-R4B.3 controlled corpus-generator conformance runner.

Conformance only: smoke-scale generation, integrity, determinism and leakage
boundary checks. The 30k/10k scientific corpus and learner are NOT executed.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
IMPLEMENTATION = SRC / "branch_n_r4b3_corpus_v01.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"IMPORT_SPEC_FAILED:{path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def check(name, fn):
    try:
        ok, details = fn()
        return {"name": name, "status": "PASS" if ok else "FAIL", **details}
    except Exception as exc:
        return {"name": name, "status": "FAIL", "error": f"{type(exc).__name__}:{exc}"}


def canonical_hash(records, encoder):
    return hashlib.sha256(b"".join(encoder(r) for r in records)).hexdigest()


def main():
    m = load_module(IMPLEMENTATION, "branch_n_r4b3_corpus_v01")
    checks = []

    checks.append(check("registered_counts_and_seeds", lambda: (
        m.TRAIN_COUNT == 30000 and m.TEST_COUNT == 10000 and
        m.DATASET_SEEDS == {"train": 3100000, "test": 4100000},
        {"train_count": m.TRAIN_COUNT, "test_count": m.TEST_COUNT, "seeds": m.DATASET_SEEDS},
    )))

    train_a, traj_a = m.generate_partition("train", 64, 3100000)
    test_a, traj_test_a = m.generate_partition("test", 64, 4100000)
    train_b, traj_b = m.generate_partition("train", 64, 3100000)

    def snapshot_schema():
        required = {"episode_id", "components", "edges", "resources", "objective"}
        return all(set(r) == required for r in train_a + test_a), {"train": 64, "test": 64}
    checks.append(check("snapshot_schema", snapshot_schema))

    def snapshot_domains():
        for records in (train_a, test_a):
            for r in records:
                assert 0 <= r["episode_id"] < 64
                assert 3 <= len(r["components"]) <= 5
                assert len(set(r["components"])) == len(r["components"])
                assert all(0 <= q <= 3 for q in r["resources"])
                assert r["objective"] in m.r4a.OBJECTIVES
                m.r4a.validate_record(r)
        return True, {}
    checks.append(check("snapshot_domain_integrity", snapshot_domains))

    checks.append(check("canonical_episode_order", lambda: (
        [r["episode_id"] for r in train_a] == list(range(64)) and
        [r["episode_id"] for r in test_a] == list(range(64)), {},
    )))

    checks.append(check("same_seed_snapshot_byte_identity", lambda: (
        canonical_hash(train_a, m.canonical_snapshot_json) == canonical_hash(train_b, m.canonical_snapshot_json), {},
    )))

    checks.append(check("same_seed_trajectory_byte_identity", lambda: (
        b"".join(m.r4b.canonical_trajectory_json(r) for r in traj_a) ==
        b"".join(m.r4b.canonical_trajectory_json(r) for r in traj_b), {},
    )))

    checks.append(check("train_test_seed_separation", lambda: (
        canonical_hash(train_a, m.canonical_snapshot_json) != canonical_hash(test_a, m.canonical_snapshot_json), {},
    )))

    def trajectory_integrity():
        for snapshots, trajectories, split, seed in ((train_a, traj_a, "train", 3100000), (test_a, traj_test_a, "test", 4100000)):
            assert len(snapshots) == len(trajectories) == 64
            for s, t in zip(snapshots, trajectories):
                assert t.episode_id == s["episode_id"]
                assert t.dataset_split == split and t.dataset_seed == seed
                assert t.trajectory_seed == seed + t.episode_id
                assert t.initial_snapshot_sha256 == m.snapshot_sha256(s)
                assert 0 <= t.terminal_step <= 6
                assert len(t.steps) <= 6
                assert [x.step for x in t.steps] == list(range(len(t.steps)))
                if t.outcome == 1:
                    assert t.terminal_reason == "GOAL_REACHED"
                else:
                    assert t.terminal_reason in {"HORIZON_EXHAUSTED", "NO_ACCESSIBLE_TRANSFORMATION"}
                    if t.terminal_reason == "HORIZON_EXHAUSTED":
                        assert t.terminal_step == 6 and len(t.steps) == 6
                    if t.terminal_reason == "NO_ACCESSIBLE_TRANSFORMATION":
                        assert t.terminal_step == len(t.steps)
        return True, {}
    checks.append(check("trajectory_integrity", trajectory_integrity))

    def canonical_trajectory_schema():
        raw = json.loads(m.r4b.canonical_trajectory_json(traj_a[0]).decode("utf-8"))
        required = {"episode_id", "dataset_split", "dataset_seed", "trajectory_seed", "initial_snapshot_sha256", "objective", "horizon", "steps", "terminal_step", "terminal_reason", "outcome"}
        step_required = {"step", "state_sha256_before", "transformation_id", "state_sha256_after"}
        return set(raw) == required and all(set(x) == step_required for x in raw["steps"]), {}
    checks.append(check("trajectory_schema", canonical_trajectory_schema))

    def state_hash_boundary():
        for s, t in zip(train_a, traj_a):
            assert t.initial_snapshot_sha256 == m.snapshot_sha256(s)
        return True, {}
    checks.append(check("initial_snapshot_hash_consistency", state_hash_boundary))

    def no_learner_or_network_boundary():
        source = IMPLEMENTATION.read_text(encoding="utf-8").lower()
        forbidden = ("sklearn", "histgradientboosting", "randomforest", "logloss", "requests", "urllib", "httpx", "socket")
        hits = [x for x in forbidden if x in source]
        return not hits, {"forbidden_tokens_found": hits}
    checks.append(check("no_learner_or_network_dependency", no_learner_or_network_boundary))

    checks.append(check("historical_boundary", lambda: (
        "historical_recovery" in m.provenance(Path("."), [], IMPLEMENTATION, m.R4B_PATH) and
        m.provenance(Path("."), [], IMPLEMENTATION, m.R4B_PATH)["historical_recovery"] is False,
        {},
    )))

    checks.append({"name": "full_corpus_generation", "status": "NOT_PERFORMED", "required_train": 30000, "required_test": 10000})
    checks.append({"name": "learner_execution", "status": "NOT_PERFORMED"})
    checks.append({"name": "confirmatory_inference", "status": "NOT_PERFORMED"})

    failures = [x for x in checks if x["status"] == "FAIL"]
    output = {
        "checks": checks,
        "implementation_path": str(IMPLEMENTATION),
        "implementation_sha256": hashlib.sha256(IMPLEMENTATION.read_bytes()).hexdigest(),
        "runner": "N_R4B3_CORPUS_CONFORMANCE_RUNNER_v0.1",
        "smoke_train_count": 64,
        "smoke_test_count": 64,
        "scientific_execution": "NOT_PERFORMED",
        "status": "FAIL" if failures else "PASS",
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
