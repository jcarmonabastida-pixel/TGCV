"""Final pre-generation gate for the N-R8-C2 vNext 5,000-pair corpus.

This gate is deliberately preparation-only: it never calls run_generation and
therefore cannot create the production corpus. It verifies that the exact
inputs and generator that passed the conformance gate are still frozen, that
the contracted target/seed remain unchanged, that production output paths are
clear, and that the scientific EXT-1.1 execution boundary remains untouched.
"""
from __future__ import annotations

import ast
import hashlib
import json
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
ROOT = SRC.parents[2]
EMP = ROOT / "03_EXPERIMENTS" / "EMP-1.1"
EXECUTION = EMP / "execution"
GENERATOR = SRC / "branch_n_r8c2_vnext_generator_v01.py"
CONFORMANCE = SRC / "probe_n_r8c2_vnext_generation_conformance_v01.py"
CONFIG = EMP / "N-R8-C2_vNEXT_GENERATION_CONFIG_v0.1.json"
CONTRACT = EMP / "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1.md"
CORPUS = EXECUTION / "N-R8-C2_vNEXT_CORPUS_v0.1.jsonl"
MANIFEST = EXECUTION / "N-R8-C2_vNEXT_CORPUS_MANIFEST_v0.1.json"

EXPECTED = {
    "operationalisation": "0cc01c7afb051b44f010a798a1b8a256dff286c9",
    "key": "40a8cfa6c74cbdf253285b3073372e6c42d262e3",
    "ot": "095cff6c69adfba19b1722a5a355b58f7e2cbe1a",
    "config": "48c00a16fb50d2258e50920b3bd283810c60d149",
    "contract": "62e0ad9b5b075276af4a8716f8ac824e14a47021",
    "generator": "1cbffad8f14cb004b81e5ef1613e1f288d7962d1",
    "conformance": "7745a8defa239ab489f92d4cbe301381156202fa",
}
EXPECTED_CONFORMANCE_RESULT_SHA256 = "1e16758c8609cd27c8540cd60827ecef5fb162966e68995bbd91000150f8ad2c"
EXPECTED_SEED = 582031
EXPECTED_TARGET = 5000


def git_blob_sha(path: Path) -> str:
    result = subprocess.run(
        ["git", "hash-object", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def static_no_production_generation() -> bool:
    """Ensure this gate itself has no path to the production entrypoint."""
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    forbidden_calls = {"run_generation"}
    return not any(
        isinstance(n, ast.Call)
        and isinstance(n.func, ast.Name)
        and n.func.id in forbidden_calls
        for n in ast.walk(tree)
    )


def static_generator_boundary() -> bool:
    """Verify production generation remains behind the explicit main guard."""
    tree = ast.parse(GENERATOR.read_text(encoding="utf-8"))
    main_nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main"]
    if len(main_nodes) != 1:
        return False
    main = main_nodes[0]
    if not any(
        isinstance(n, ast.Call)
        and isinstance(n.func, ast.Name)
        and n.func.id == "run_generation"
        for n in ast.walk(main)
    ):
        return False
    guards = [
        n for n in tree.body
        if isinstance(n, ast.If)
        and isinstance(n.test, ast.Compare)
        and isinstance(n.test.left, ast.Name)
        and n.test.left.id == "__name__"
        and len(n.test.comparators) == 1
        and isinstance(n.test.comparators[0], ast.Constant)
        and n.test.comparators[0].value == "__main__"
    ]
    return len(guards) == 1 and any(
        isinstance(n, ast.Expr)
        and isinstance(n.value, ast.Call)
        and isinstance(n.value.func, ast.Name)
        and n.value.func.id == "main"
        for n in guards[0].body
    )


def verify_config() -> tuple[bool, str]:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    checks = (
        cfg.get("status") == "FROZEN_PRE_GENERATION",
        cfg.get("target_pair_count") == EXPECTED_TARGET,
        cfg.get("seed") == EXPECTED_SEED,
        cfg.get("corpus_output") == CORPUS.name,
        cfg.get("manifest_output") == MANIFEST.name,
        cfg.get("scientific_execution") == "NOT_PERFORMED",
    )
    return all(checks), "PASS" if all(checks) else "CONFIG_MISMATCH"


def run_gate() -> dict:
    required_paths = [CONFIG, CONTRACT, GENERATOR, CONFORMANCE]
    if not all(path.exists() for path in required_paths):
        raise RuntimeError("required frozen/pre-generation file is missing")

    blob_checks = {
        "operationalisation": git_blob_sha(SRC / "branch_n_r8_operationalisation_v01.py") == EXPECTED["operationalisation"],
        "key": git_blob_sha(SRC / "branch_n_r8c2_vnext_key_v01.py") == EXPECTED["key"],
        "ot": git_blob_sha(SRC / "probe_n_r8c2_vnext_identifiability_v01.py") == EXPECTED["ot"],
        "config": git_blob_sha(CONFIG) == EXPECTED["config"],
        "contract": git_blob_sha(CONTRACT) == EXPECTED["contract"],
        "generator": git_blob_sha(GENERATOR) == EXPECTED["generator"],
        "conformance": git_blob_sha(CONFORMANCE) == EXPECTED["conformance"],
    }
    if not all(blob_checks.values()):
        raise RuntimeError(f"frozen blob verification failed: {blob_checks}")

    config_ok, config_state = verify_config()
    if not config_ok:
        raise RuntimeError(f"frozen configuration mismatch: {config_state}")
    if not static_no_production_generation():
        raise RuntimeError("pre-generation gate contains a production run_generation call")
    if not static_generator_boundary():
        raise RuntimeError("generator production entrypoint is not safely main-guarded")

    # These output paths must be absent: generation must never silently overwrite
    # an earlier corpus or manifest.
    if CORPUS.exists() or MANIFEST.exists():
        raise RuntimeError("production corpus/manifest already exists; refusing overwrite")

    # The generator is explicitly preparation-only with respect to scientific
    # execution and must not consume a Rust dataset during corpus construction.
    generator_text = GENERATOR.read_text(encoding="utf-8").lower()
    forbidden_dataset_markers = ("rust_dataset", "rust dataset", "dataset_path", "logloss", "model.train", "model.fit")
    if any(marker in generator_text for marker in forbidden_dataset_markers):
        raise RuntimeError("generator contains a forbidden scientific/dataset execution marker")

    return {
        "status": "PASS",
        "gate": "N-R8-C2_vNEXT_PRE_GENERATION_v0.1",
        "decision": "AUTHORIZED_FOR_EXPLICIT_PRODUCTION_GENERATION",
        "target_pair_count": EXPECTED_TARGET,
        "seed": EXPECTED_SEED,
        "frozen_blob_checks": blob_checks,
        "config_check": config_state,
        "production_entrypoint_safe": True,
        "production_generation": "NOT_PERFORMED",
        "corpus_artifact_exists": False,
        "manifest_artifact_exists": False,
        "scientific_execution": "NOT_PERFORMED",
        "rust_dataset_consumption": "NOT_PERFORMED",
        "conformance_evidence": {
            "gate_blob_sha": EXPECTED["conformance"],
            "canonical_result_sha256": EXPECTED_CONFORMANCE_RESULT_SHA256,
            "status": "PASS",
        },
    }


def main() -> None:
    print(json.dumps(run_gate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
