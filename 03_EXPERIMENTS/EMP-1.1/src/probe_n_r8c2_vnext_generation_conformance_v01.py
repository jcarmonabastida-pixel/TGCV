"""N-R8-C2 vNext generation conformance / reproducibility gate."""
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


def _is_main_guard(node: ast.If) -> bool:
    test = node.test
    return (
        isinstance(test, ast.Compare)
        and len(test.ops) == 1
        and isinstance(test.ops[0], ast.Eq)
        and isinstance(test.left, ast.Name)
        and test.left.id == "__name__"
        and len(test.comparators) == 1
        and isinstance(test.comparators[0], ast.Constant)
        and test.comparators[0].value == "__main__"
    )


def static_no_generation_on_import() -> bool:
    """Verify the only top-level entry to generation is the main guard."""
    tree = ast.parse(GENERATOR_PATH.read_text(encoding="utf-8"))

    main_functions = {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "main"
    }
    if main_functions != {"main"}:
        return False

    guarded_main_calls: set[ast.AST] = set()
    for node in tree.body:
        if isinstance(node, ast.If) and _is_main_guard(node):
            for child in node.body:
                if isinstance(child, ast.Expr) and isinstance(child.value, ast.Call):
                    call = child.value
                    if isinstance(call.func, ast.Name) and call.func.id == "main":
                        guarded_main_calls.add(call)

    if len(guarded_main_calls) != 1:
        return False

    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)):
            continue
        if node.func.id != "run_generation":
            continue
        # run_generation must be called from main(), never at module scope.
        function_parent = None
        stack = [tree]
        while stack:
            parent = stack.pop()
            for child in ast.iter_child_nodes(parent):
                if child is node:
                    function_parent = parent
                    break
                stack.append(child)
            if function_parent is not None:
                break
        # The direct parent can be an Expr/Return; walk the tree structurally
        # through the enclosing function using a dedicated recursive check.
        found_in_main = False
        for fn in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "main"]:
            if any(x is node for x in ast.walk(fn)):
                found_in_main = True
                break
        if not found_in_main:
            return False
    return True


def state_from_record(record: dict):
    return generator.canonical_state(
        tuple(record["components"]),
        tuple(tuple(edge) for edge in record["edges"]),
        tuple(record["resources"]),
        record["objective"],
    )


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
        a_sha, b_sha = record["state_a_sha256"], record["state_b_sha256"]
        if not a_sha < b_sha:
            errors.append(f"pair state order is not canonical: {record['pair_id']}")
        expected_pid = hashlib.sha256(canonical_json(sorted((a_sha, b_sha))).encode("utf-8")).hexdigest()
        if record["pair_id"] != expected_pid:
            errors.append(f"pair_id formula mismatch: {record['pair_id']}")
        state_a = state_from_record(record["state_a"])
        state_b = state_from_record(record["state_b"])
        if state_a.sha256() != a_sha:
            errors.append(f"state_a SHA mismatch: {record['pair_id']}")
        if state_b.sha256() != b_sha:
            errors.append(f"state_b SHA mismatch: {record['pair_id']}")
        key_a, key_b = generator.c2_vnext_key(state_a), generator.c2_vnext_key(state_b)
        if list(key_a) != record["key_c2_vnext"] or list(key_b) != record["key_c2_vnext"]:
            errors.append(f"K reconstruction mismatch: {record['pair_id']}")
        if key_a != key_b:
            errors.append(f"K(A) != K(B): {record['pair_id']}")
        if record["o_t_a_signature"] == record["o_t_b_signature"]:
            errors.append(f"O_T equality accepted: {record['pair_id']}")
        if record["provenance"] != "DERIVED_RECONSTRUCTED":
            errors.append(f"unexpected provenance: {record['pair_id']}")
        if record["generator_version"] != "branch_n_r8c2_vnext_generator_v01":
            errors.append(f"unexpected generator version: {record['pair_id']}")
    return errors


def run_gate() -> dict:
    before_corpus = file_state(CORPUS_PATH)
    before_manifest = file_state(MANIFEST_PATH)
    frozen = generator.verify_frozen_inputs()
    if not all(frozen.values()):
        raise RuntimeError(f"frozen input verification failed: {frozen}")
    static_import_safe = static_no_generation_on_import()
    if not static_import_safe:
        raise RuntimeError("generator has an invalid generation entrypoint")
    first = generator._generation_core(target_pairs=SAMPLE_PAIRS, seed=SEED, dry_run=True)
    second = generator._generation_core(target_pairs=SAMPLE_PAIRS, seed=SEED, dry_run=True)
    first_bytes, second_bytes = canonical_result(first), canonical_result(second)
    if first_bytes != second_bytes:
        raise RuntimeError("two identical generation runs are not byte-for-byte identical")
    semantic_errors = semantic_checks(first)
    if semantic_errors:
        raise RuntimeError("semantic conformance failed: " + "; ".join(semantic_errors))
    if file_state(CORPUS_PATH) != before_corpus:
        raise RuntimeError("conformance gate modified the corpus artifact")
    if file_state(MANIFEST_PATH) != before_manifest:
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
        "byte_for_byte_reproducible": True,
        "semantic_conformance": True,
        "static_import_safe": True,
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
