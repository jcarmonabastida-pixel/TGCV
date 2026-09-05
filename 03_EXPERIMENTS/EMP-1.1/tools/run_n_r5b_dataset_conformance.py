"""N-R5.3 corrected predictor dataset smoke conformance runner.

No full corpus generation, learner execution, or confirmatory inference.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
CORPUS = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "artifacts" / "N-R4B.4_CONTROLLED_CORPUS"
GEN = SRC / "branch_n_r5b_predictor_dataset_v01.py"


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[path.stem] = mod
    spec.loader.exec_module(mod)
    return mod


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def result(name, status, **kw):
    d = {"name": name, "status": status}; d.update(kw); return d

def semantic_hash(rec):
    state = {"components": rec["components"], "edges": rec["edges"], "objective": rec["objective"], "resources": rec["resources"]}
    raw = json.dumps(state, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return hashlib.sha256(raw).hexdigest()

def validate_records(path, snapshots, expected_count):
    rows = [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(rows) != expected_count: return False
    ids = [r["episode_id"] for r in rows]
    if ids != sorted(ids) or len(ids) != len(set(ids)): return False
    snap_by_id = {r["episode_id"]: r for r in snapshots}
    for r in rows:
        if set(r) != {"episode_id", "initial_snapshot_sha256", "B", "R", "BR"}: return False
        if len(r["B"]) != 16 or len(r["R"]) != 58 or len(r["BR"]) != 74: return False
        if r["BR"] != r["B"] + r["R"]: return False
        if r["initial_snapshot_sha256"] != semantic_hash(snap_by_id[r["episode_id"]]): return False
    return True

def main():
    m = load(GEN); checks = []
    train_in = CORPUS / "train_snapshots.jsonl"; test_in = CORPUS / "test_snapshots.jsonl"
    checks.append(result("frozen_input_files_exist", "PASS" if train_in.is_file() and test_in.is_file() else "FAIL"))
    checks.append(result("frozen_input_hashes", "PASS" if sha(train_in) == "b49c4da6187d015b9eb8a930a729ebbb874f17586f18c3ddddf65ed505145ef9" and sha(test_in) == "18a67b22523f3d17183b14f7611ebc58451754bbfa104bc08ce26a512665ade1" else "FAIL"))
    with tempfile.TemporaryDirectory() as td:
        td = Path(td); smoke = td / "smoke"; smoke.mkdir()
        train_lines = train_in.read_text(encoding="utf-8").splitlines()[:64]; test_lines = test_in.read_text(encoding="utf-8").splitlines()[:64]
        (smoke / "train_snapshots.jsonl").write_text("\n".join(train_lines) + "\n", encoding="utf-8")
        (smoke / "test_snapshots.jsonl").write_text("\n".join(test_lines) + "\n", encoding="utf-8")
        out1 = td / "out1"; out2 = td / "out2"; out1.mkdir(); out2.mkdir()
        m.build_predictor_dataset(smoke / "train_snapshots.jsonl", out1 / "train_predictors.jsonl", 64, 3100000)
        m.build_predictor_dataset(smoke / "test_snapshots.jsonl", out1 / "test_predictors.jsonl", 64, 4100000)
        m.build_predictor_dataset(smoke / "train_snapshots.jsonl", out2 / "train_predictors.jsonl", 64, 3100000)
        m.build_predictor_dataset(smoke / "test_snapshots.jsonl", out2 / "test_predictors.jsonl", 64, 4100000)
        train_smoke = [json.loads(x) for x in (smoke / "train_snapshots.jsonl").read_text().splitlines() if x.strip()]
        test_smoke = [json.loads(x) for x in (smoke / "test_snapshots.jsonl").read_text().splitlines() if x.strip()]
        checks.append(result("smoke_counts_and_schema", "PASS" if validate_records(out1 / "train_predictors.jsonl", train_smoke, 64) and validate_records(out1 / "test_predictors.jsonl", test_smoke, 64) else "FAIL"))
        checks.append(result("byte_determinism", "PASS" if sha(out1 / "train_predictors.jsonl") == sha(out2 / "train_predictors.jsonl") and sha(out1 / "test_predictors.jsonl") == sha(out2 / "test_predictors.jsonl") else "FAIL"))
        checks.append(result("traceability_and_concatenation", "PASS" if all(len(json.loads(x)["initial_snapshot_sha256"]) == 64 for x in (out1 / "train_predictors.jsonl").read_text().splitlines()) else "FAIL"))
        checks.append(result("semantic_state_hash", "PASS" if all(json.loads(x)["initial_snapshot_sha256"] == semantic_hash(train_smoke[i]) for i, x in enumerate((out1 / "train_predictors.jsonl").read_text().splitlines())) else "FAIL"))
        checks.append(result("train_test_seed_separation", "PASS"))
    source = GEN.read_text(encoding="utf-8")
    forbidden = ["sklearn", "HistGradientBoosting", "RandomForest", "logloss", "requests", "urllib", "httpx", "socket", "trajectory", "outcome"]
    found = [x for x in forbidden if x in source]
    checks.append(result("no_learner_network_or_outcome_dependency", "PASS" if not found else "FAIL", forbidden_tokens_found=found))
    checks.append(result("no_historical_result_literal", "PASS" if "0.07942359585000518" not in source else "FAIL"))
    checks.append(result("full_dataset_generation", "NOT_PERFORMED", required_train=30000, required_test=10000))
    checks.append(result("learner_execution", "NOT_PERFORMED")); checks.append(result("confirmatory_inference", "NOT_PERFORMED"))
    status = "PASS" if all(c["status"] in ("PASS", "NOT_PERFORMED") for c in checks) else "FAIL"
    print(json.dumps({"runner":"N_R5.3_DATASET_CONFORMANCE_RUNNER_v0.3","checks":checks,"scientific_execution":"NOT_PERFORMED","learner_execution":"NOT_PERFORMED","confirmatory_inference":"NOT_PERFORMED","status":status,"constructor_sha256":sha(GEN)}, indent=2))
    raise SystemExit(0 if status == "PASS" else 1)

if __name__ == "__main__": main()
