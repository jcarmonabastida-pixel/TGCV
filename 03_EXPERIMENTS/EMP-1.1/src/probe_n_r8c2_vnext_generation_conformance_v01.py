"""N-R8-C2 vNext generation conformance / reproducibility gate.

This gate validates the deterministic generation core before the contracted
5,000-pair corpus is allowed to be generated. It never writes corpus or
manifest artifacts and never runs scientific EXT-1.1 execution.

The gate runs the same small accepted-pair generation twice with the frozen
seed and compares the canonical in-memory result byte-for-byte. It also checks
pair semantics, ordering, provenance, duplicate pair IDs, and the absence of
corpus/manifest side effects.
"""
from __future__ import annotations

import ast
import hashlib
import json
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
ROOT = SRC.parents[3]
OUTPUT_DIR = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "execution"
CORPUS_PATH = OUTPUT_DIR / "N-R8-C2_vNEXT_CORPUS_v0.1.jsonl"
MANIFEST_PATH = OUTPUT_DIR / "N-R8-C2_vNEXT_CORPUS_MANIFEST_v0.1.json"
GENERATOR_PATH = SRC / "branch_n_r8c2_vnext_generator_v01.py"

SAMPLE_PAIRS = 3
SEED = 582031

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import branch_n_r8c2_vnext_generator_v01 as generator  # noqa: E402


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def canonical_result(result: dict) -> bytes:
    """Stable serialization of the deterministic generation-core result."""
    payload = {
        "records": result["records"],
        "candidate_count": result["candidate_count"],
        "equal_key_pairs_examined": result["equal_key_pairs_examined"],
        "rejected_equal_ot": result["rejected_equal_ot"],
        "frozen_input_checks": result["frozen_input_checks"],
    }
    return (canonical_json(payload) + "\n").encode("utf-8")


def file_state(path: Path) -> tuple[bool, str | None]:
    if not path.exists():
        return False, None
    return True, hashlib.sha256(path.read_bytes()).hexdigest()


def static_no_generation_on_import() -> bool:
    tree = ast.parse(GENERATOR_PATH.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "run_generation":
                parent = getattr(node, "parent", None)
                if isinstance(parent, ast.If):
                    continue
                return False
    return True


def attach_parents(tree: ast.AST) -> None:
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            child.parent = parent  # type: ignore[attr-defined]


def semantic_checks(result: dict) -> list[str]:
    errors: list[str] = []
    records = result["records"]

    if len(records) != SAMPLE_PAIRS:
        errors.append(f"accepted_pair_count={len(records)} != {SAMPLE_PAIRS}")

    pair_ids = [r["pair_id"] for r in records]
    if len(pair_ids) != len(set(pair_ids)):
        errors.append("duplicate pair_id detected")

    ordering = [(r["state_a_sha256"], r["state_b_sha256"]) for r in records]
    if ordering != sorted(ordering):
        errors.append("accepted records are not ordered lexicographically by state hashes")

    for record in records:
        a_sha = record["state_a_sha256"]
        b_sha = record["state_b_sha256"]
        if not a_sha < b_sha:
            errors.append(f"pair state order is not canonical: {record['pair_id']}")

        expected_pid = hashlib.sha256(
            canonical_json(sorted((a_sha, b_sha))).encode("utf-8")
        ).hexdigest()
        if record["pair_id"] != expected_pid:
            errors.append(f"pair_id formula mismatch: {record['pair_id']}")

        if record["key_c2_vnext"] != list(generator.c2_vnext_key_from_record(record["state_a"])):
            errors.append(f"state_a key mismatch: {record['pair_id']}")
        if record["key_c2_vnext"] != list(generator.c2_vnext_key_from_record(record["state_b"])):
            errors.append(f"state_b key mismatch: {record['pair_id']}")

        if record["o_t_a_signature"] == record["o_t_b_signature"]:
            errors.append(f"O_T equality accepted: {record['pair_id']}")
        if record["provenance"] != "DERIVED_RECONSTRUCTED":
            errors.append(f"unexpected provenance: {record['pair_id']}")
        if record["generator_version"] != "branch_n_r8c2_vnext_generator_v01":
            errors.append(f"unexpected generator version: {record['pair_id']}")

    return errors


def record_key_from_record(record: dict):
    """Reconstruct a state using only serialized state fields for key checking."""
    return generator.c2_vnext_key_from_record(record)


def run_gate() -> dict:
    attach_parents(ast.parse(GENERATOR_PATH.read_text(encoding="utf-8")))

    before_corpus = file_state(CORPUS_PATH)
    before_manifest = file_state(MANIFEST_PATH)

    frozen = generator.verify_frozen_inputs()
    if not all(frozen.values()):
        raise RuntimeError(f"frozen input verification failed: {frozen}")

    static_import_safe = static_no_generation_on_import()
    if not static_import_safe:
        raise RuntimeError("generator contains an unexpected import-time run_generation call")

    first = generator._generation_core(target_pairs=SAMPLE_PAIRS, seed=SEED, dry_run=True)
    second = generator._generation_core(target_pairs=SAMPLE_PAIRS, seed=SEED, dry_run=True)

    first_bytes = canonical_result(first)
    second_bytes = canonical_result(second)
    byte_identical = first_bytes == second_bytes
    if not byte_identical:
        raise RuntimeError("two identical generation runs are not byte-for-byte identical")

    semantic_errors = semantic_checks(first)
    if semantic_errors:
        raise RuntimeError("semantic conformance failed: " + "; ".join(semantic_errors))

    after_corpus = file_state(CORPUS_PATH)
    after_manifest = file_state(MANIFEST_PATH)
    if before_corpus != after_corpus:
        raise RuntimeError("conformance gate modified the corpus artifact")
    if before_manifest != after_manifest:
        raise RuntimeError("conformance gate modified the manifest artifact")

    return {
        "status": "PASS",
        "gate": "N-R8-C2_vNEXT_GENERATION_CONFORMANCE_v0.1",
        "sample_pair_count": SAMPLE_PAIRS,
        "seed": SEED,
        "run_1_candidate_count": first["candidate_count"],
        "run_2_candidate_count": second["candidate_count"],
        "run_1_equal_key_pairs_examined": first["equal_key_pairs_examined"],
        "run_2_equal_key_pairs_examined": second["equal_key_pairs_examined"],
        "run_1_rejected_equal_ot": first["rejected_equal_ot"],
        "run_2_rejected_equal_ot": second["rejected_equal_ot"],
        "canonical_result_sha256": hashlib.sha256(first_bytes).hexdigest(),
        "byte_for_byte_reproducible": byte_identical,
        "semantic_conformance": True,
        "static_import_safe": static_import_safe,
        "corpus_artifact_side_effect": False,
        "manifest_artifact_side_effect": False,
        "frozen_input_checks": frozen,
        "corpus_generation": "NOT_PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
        "decision": "PASS",
    }


def main() -> None:
    print(json.dumps(run_gate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
