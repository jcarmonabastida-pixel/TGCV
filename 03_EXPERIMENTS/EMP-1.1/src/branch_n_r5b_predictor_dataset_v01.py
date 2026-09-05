"""Prospective Branch N predictor-dataset constructor for N-R5.3.

Consumes only frozen N-R4B.4 initial snapshots and the N-R5.2 predictor
representation. Predictor construction does not read post-snapshot records,
learner state, network state, or external state.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import platform
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent
PRED_PATH = ROOT / "branch_n_r5_predictor_v01.py"
spec = importlib.util.spec_from_file_location("branch_n_r5_predictor_v01", PRED_PATH)
pmod = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules["branch_n_r5_predictor_v01"] = pmod
spec.loader.exec_module(pmod)
Predictor = pmod.Predictor
encode_predictor = pmod.encode_predictor

TRAIN_COUNT = 30000
TEST_COUNT = 10000
TRAIN_SEED = 3100000
TEST_SEED = 4100000


def canonical_jsonl(records: Iterable[dict]) -> bytes:
    return b"".join((json.dumps(r, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii") for r in records)


def predictor_record(p: Predictor) -> dict:
    return {"episode_id": p.episode_id,
            "initial_snapshot_sha256": p.initial_snapshot_sha256,
            "B": list(p.B), "R": list(p.R), "BR": list(p.BR)}


def build_predictor_dataset(snapshot_path: Path, output_path: Path, expected_count: int, expected_seed: int) -> dict:
    records = []
    seen = set()
    with snapshot_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec["episode_id"] in seen:
                raise ValueError("DUPLICATE_EPISODE_ID")
            seen.add(rec["episode_id"])
            p = encode_predictor(rec)
            records.append(predictor_record(p))
    if len(records) != expected_count:
        raise ValueError(f"COUNT_MISMATCH:{len(records)}:{expected_count}")
    records.sort(key=lambda x: x["episode_id"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(canonical_jsonl(records))
    return {"count": len(records), "sha256": hashlib.sha256(output_path.read_bytes()).hexdigest(),
            "first_episode_id": records[0]["episode_id"], "last_episode_id": records[-1]["episode_id"]}


def provenance(train_input: Path, test_input: Path, train_output: Path, test_output: Path) -> dict:
    return {"artifact": "N-R5.3_PREDICTOR_DATASET", "status": "CONTROLLED_GENERATION",
            "historical_recovery": False, "specification": "N-R5.3 v0.1",
            "train_input_sha256": hashlib.sha256(train_input.read_bytes()).hexdigest(),
            "test_input_sha256": hashlib.sha256(test_input.read_bytes()).hexdigest(),
            "train_output_sha256": hashlib.sha256(train_output.read_bytes()).hexdigest(),
            "test_output_sha256": hashlib.sha256(test_output.read_bytes()).hexdigest(),
            "train_count": TRAIN_COUNT, "test_count": TEST_COUNT,
            "train_seed": TRAIN_SEED, "test_seed": TEST_SEED,
            "predictor_implementation_sha256": hashlib.sha256(PRED_PATH.read_bytes()).hexdigest(),
            "constructor_implementation_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "python_version": platform.python_version(), "python_implementation": platform.python_implementation(),
            "platform": platform.platform(), "learner_executed": False,
            "confirmatory_inference_executed": False, "historical_result_used_as_tuning_target": False}


def generate_predictor_dataset(corpus_dir: Path, output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    train_in = corpus_dir / "train_snapshots.jsonl"
    test_in = corpus_dir / "test_snapshots.jsonl"
    train_out = output_dir / "train_predictors.jsonl"
    test_out = output_dir / "test_predictors.jsonl"
    train = build_predictor_dataset(train_in, train_out, TRAIN_COUNT, TRAIN_SEED)
    test = build_predictor_dataset(test_in, test_out, TEST_COUNT, TEST_SEED)
    prov = provenance(train_in, test_in, train_out, test_out)
    (output_dir / "PROVENANCE.json").write_text(json.dumps(prov, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return {"train": train, "test": test, "provenance": prov}
