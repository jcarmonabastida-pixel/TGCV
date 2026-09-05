"""N-R8-C2 vNext full-corpus deterministic rerun gate.

This gate re-runs the corrected generator core in memory and compares the
canonical corpus bytes against the already-generated production corpus.
It NEVER overwrites the production corpus or manifest and NEVER performs
scientific EXT-1.1 execution or Rust dataset consumption.

The manifest comparison deliberately excludes wall-clock timestamps and the
self-referential final-manifest hash. Those fields are execution metadata, not
deterministic generation output. All deterministic generation fields,
including the corpus SHA and frozen input SHAs, are compared exactly.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
EXECUTION = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "execution"
CORPUS = EXECUTION / "N-R8-C2_vNEXT_CORPUS_v0.1.jsonl"
MANIFEST = EXECUTION / "N-R8-C2_vNEXT_CORPUS_MANIFEST_v0.1.json"
GENERATOR = SRC / "branch_n_r8c2_vnext_generator_v01.py"

EXPECTED = {
    "corpus_sha256": "795bfb12b11be49dc08f4dbe568141cd0a2f7e776c7a10cc8aa9122befb408af",
    "accepted_pair_count": 5000,
    "candidate_count": 27318,
    "equal_key_pairs_examined": 12317,
    "rejected_equal_ot": 7317,
    "seed": 582031,
    "target_pair_count": 5000,
    "generator_version": "branch_n_r8c2_vnext_generator_v01",
    "contract_version": "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1",
    "scientific_execution": "NOT_PERFORMED",
}
EXPECTED_INPUT_SHAS = {
    "config": "48c00a16fb50d2258e50920b3bd283810c60d149",
    "contract": "62e0ad9b5b075276af4a8716f8ac824e14a47021",
    "generator": "652ffeebab1f43095494a93a5cae04d18656d51d",
    "key": "40a8cfa6c74cbdf253285b3073372e6c42d262e3",
    "operationalisation": "0cc01c7afb051b44f010a798a1b8a256dff286c9",
    "ot": "095cff6c69adfba19b1722a5a355b58f7e2cbe1a",
}


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def load_generator():
    src_dir = str(SRC)
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    spec = importlib.util.spec_from_file_location("tgcv_r8c2_vnext_generator_gate", GENERATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load generator: {GENERATOR}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def corpus_bytes(records: list[dict]) -> bytes:
    return ("".join(canonical_json(record) + "\n" for record in records)).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def deterministic_manifest_projection(payload: dict) -> dict:
    ignored = {"start_utc", "end_utc", "deterministic_rerun_result", "final_manifest_sha256"}
    return {key: value for key, value in payload.items() if key not in ignored}


def main() -> None:
    if not CORPUS.exists() or not MANIFEST.exists():
        raise RuntimeError("production corpus/manifest missing; deterministic rerun gate requires the existing production artifacts")

    generator = load_generator()
    result = generator._generation_core(target_pairs=generator.TARGET_PAIRS, seed=generator.SEED)
    records = result["records"]
    rerun_bytes = corpus_bytes(records)
    rerun_sha = sha256_bytes(rerun_bytes)
    production_bytes = CORPUS.read_bytes()
    production_sha = sha256_bytes(production_bytes)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    observed_core = {
        "corpus_sha256": rerun_sha,
        "accepted_pair_count": len(records),
        "candidate_count": result["candidate_count"],
        "equal_key_pairs_examined": result["equal_key_pairs_examined"],
        "rejected_equal_ot": result["rejected_equal_ot"],
        "seed": generator.SEED,
        "target_pair_count": generator.TARGET_PAIRS,
        "generator_version": "branch_n_r8c2_vnext_generator_v01",
        "contract_version": "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1",
        "scientific_execution": "NOT_PERFORMED",
    }

    manifest_core = deterministic_manifest_projection(manifest)
    expected_manifest_core = {
        "accepted_pair_count": EXPECTED["accepted_pair_count"],
        "candidate_count": EXPECTED["candidate_count"],
        "contract_version": EXPECTED["contract_version"],
        "corpus_generation": "PERFORMED",
        "corpus_sha256": EXPECTED["corpus_sha256"],
        "frozen_input_shas": EXPECTED_INPUT_SHAS,
        "generator_version": EXPECTED["generator_version"],
        "equal_key_pairs_examined": EXPECTED["equal_key_pairs_examined"],
        "rejected_equal_ot": EXPECTED["rejected_equal_ot"],
        "scientific_execution": "NOT_PERFORMED",
        "seed": EXPECTED["seed"],
        "status": "PASS",
        "target_pair_count": EXPECTED["target_pair_count"],
    }

    checks = {
        "production_corpus_exists": CORPUS.exists(),
        "production_manifest_exists": MANIFEST.exists(),
        "rerun_corpus_sha_matches_expected": rerun_sha == EXPECTED["corpus_sha256"],
        "rerun_corpus_sha_matches_production": rerun_sha == production_sha,
        "rerun_corpus_bytes_match_production": rerun_bytes == production_bytes,
        "generation_core_metrics_match_expected": observed_core == EXPECTED,
        "manifest_deterministic_projection_matches_expected": manifest_core == expected_manifest_core,
        "manifest_records_match_rerun": all(manifest.get(k) == v for k, v in observed_core.items()),
        "scientific_execution_not_performed": manifest.get("scientific_execution") == "NOT_PERFORMED",
        "rust_dataset_not_consumed": True,
    }

    if not all(checks.values()):
        raise RuntimeError(json.dumps({"status": "FAIL", "checks": checks, "observed_core": observed_core, "manifest_core": manifest_core}, indent=2, sort_keys=True))

    print(json.dumps({
        "status": "PASS",
        "decision": "DETERMINISTIC_RERUN_CONFIRMED",
        "gate": "N-R8-C2_vNEXT_DETERMINISTIC_RERUN_v0.1",
        "rerun_corpus_sha256": rerun_sha,
        "production_corpus_sha256": production_sha,
        "byte_for_byte_match": True,
        "accepted_pair_count": len(records),
        "candidate_count": result["candidate_count"],
        "equal_key_pairs_examined": result["equal_key_pairs_examined"],
        "rejected_equal_ot": result["rejected_equal_ot"],
        "seed": generator.SEED,
        "frozen_input_shas": EXPECTED_INPUT_SHAS,
        "scientific_execution": "NOT_PERFORMED",
        "rust_dataset_consumption": "NOT_PERFORMED",
        "production_artifacts_modified": False,
        "checks": checks,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
