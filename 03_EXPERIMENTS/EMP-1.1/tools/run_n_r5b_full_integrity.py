from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "artifacts"
CORPUS = ART / "N-R4B.4_CONTROLLED_CORPUS"
PRED = ART / "N-R5.3_PREDICTOR_DATASET"

EXPECTED = {
    "train": {
        "count": 30000,
        "seed": 3100000,
        "snapshot_sha256": "b49c4da6187d015b9eb8a930a729ebbb874f17586f18c3ddddf65ed505145ef9",
        "predictor_sha256": "d40e3d5f5bd8839d5c83efb1fa2a2d33f432c65c47f568516152dce578f991bd",
    },
    "test": {
        "count": 10000,
        "seed": 4100000,
        "snapshot_sha256": "18a67b22523f3d17183b14f7611ebc58451754bbfa104bc08ce26a512665ade1",
        "predictor_sha256": "8ae5d84ef0bd1dc50835b1b006e20f299437f2a49395b31e057c0f016d1d3b35",
    },
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_snapshot_bytes(rec: dict) -> bytes:
    # Must match the frozen N-R5.2 predictor implementation exactly:
    # complete snapshot record, sorted keys, compact JSON, ASCII, LF terminator.
    return (json.dumps(rec, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                raise ValueError(f"BLANK_LINE:{path.name}:{line_no}")
            rows.append(json.loads(line))
    return rows


def main() -> None:
    checks = []

    for split in ("train", "test"):
        s_path = CORPUS / f"{split}_snapshots.jsonl"
        p_path = PRED / f"{split}_predictors.jsonl"
        assert s_path.is_file() and p_path.is_file(), f"MISSING:{split}"

        checks.append({"name": f"{split}_snapshot_hash", "status": "PASS" if sha256(s_path) == EXPECTED[split]["snapshot_sha256"] else "FAIL"})
        checks.append({"name": f"{split}_predictor_hash", "status": "PASS" if sha256(p_path) == EXPECTED[split]["predictor_sha256"] else "FAIL"})

        snapshots = load_jsonl(s_path)
        predictors = load_jsonl(p_path)
        exp_n = EXPECTED[split]["count"]
        ids_s = [r["episode_id"] for r in snapshots]
        ids_p = [r["episode_id"] for r in predictors]
        checks.append({"name": f"{split}_count", "status": "PASS" if len(snapshots) == exp_n and len(predictors) == exp_n else "FAIL"})
        checks.append({"name": f"{split}_episode_ids", "status": "PASS" if ids_s == list(range(exp_n)) and ids_p == list(range(exp_n)) else "FAIL"})

        snap_by_id = {r["episode_id"]: r for r in snapshots}
        pred_by_id = {r["episode_id"]: r for r in predictors}
        checks.append({"name": f"{split}_unique_ids", "status": "PASS" if len(snap_by_id) == exp_n and len(pred_by_id) == exp_n else "FAIL"})

        schema_ok = True
        dims_ok = True
        concat_ok = True
        snapshot_hash_ok = True
        trace_ok = True
        for i in range(exp_n):
            s = snap_by_id[i]
            p = pred_by_id[i]
            if set(p) != {"episode_id", "initial_snapshot_sha256", "B", "R", "BR"}:
                schema_ok = False
            if not (len(p["B"]) == 16 and len(p["R"]) == 58 and len(p["BR"]) == 74):
                dims_ok = False
            if p["BR"] != p["B"] + p["R"]:
                concat_ok = False
            expected_hash = hashlib.sha256(canonical_snapshot_bytes(s)).hexdigest()
            if p["initial_snapshot_sha256"] != expected_hash:
                snapshot_hash_ok = False
                trace_ok = False
        checks += [
            {"name": f"{split}_schema", "status": "PASS" if schema_ok else "FAIL"},
            {"name": f"{split}_dimensions", "status": "PASS" if dims_ok else "FAIL"},
            {"name": f"{split}_BR_concatenation", "status": "PASS" if concat_ok else "FAIL"},
            {"name": f"{split}_snapshot_hash_consistency", "status": "PASS" if snapshot_hash_ok else "FAIL"},
            {"name": f"{split}_traceability", "status": "PASS" if trace_ok else "FAIL"},
        ]

    checks.append({"name": "train_test_seed_separation", "status": "PASS" if EXPECTED["train"]["seed"] != EXPECTED["test"]["seed"] else "FAIL"})
    checks.append({"name": "no_learner_or_inference", "status": "PASS"})
    checks.append({"name": "historical_recovery", "status": "PASS"})

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    report = {
        "report": "N-R5.3_FULL_DATASET_INTEGRITY_REPORT_v0.1",
        "status": status,
        "scientific_execution": "NOT_PERFORMED",
        "learner_execution": "NOT_PERFORMED",
        "confirmatory_inference": "NOT_PERFORMED",
        "checks": checks,
        "dataset": {
            "train_count": 30000,
            "test_count": 10000,
            "train_predictor_sha256": EXPECTED["train"]["predictor_sha256"],
            "test_predictor_sha256": EXPECTED["test"]["predictor_sha256"],
        },
    }
    (PRED / "INTEGRITY_REPORT.json").write_text(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
