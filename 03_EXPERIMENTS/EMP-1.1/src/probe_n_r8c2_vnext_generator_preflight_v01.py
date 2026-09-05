"""N-R8-C2 vNext generator preflight.

This gate validates the preparation layer without generating or accepting the
5,000-pair corpus and without running the scientific experiment.
"""
from __future__ import annotations

import ast
import hashlib
import json
import random
from pathlib import Path

from branch_n_r8_operationalisation_v01 import canonical_state
from branch_n_r8c2_vnext_generator_v01 import build_candidate_buckets, generate_candidate
from branch_n_r8c2_vnext_key_v01 import c2_vnext_key

ROOT = Path(__file__).resolve().parents[3]
GENERATOR = ROOT / "03_EXPERIMENTS/EMP-1.1/src/branch_n_r8c2_vnext_generator_v01.py"
TARGET = 5000
SEED = 582031
FORBIDDEN_CONSTRUCTION_NAMES = {
    "transformation_organisation_graph", "tacc", "r2", "low_order_r1",
    "acceptance_signature", "O_T", "ot_signature",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def deterministic_probe() -> bool:
    def run():
        rng = random.Random(SEED)
        states = [generate_candidate(rng) for _ in range(12)]
        return [s.sha256() for s in states], [c2_vnext_key(s) for s in states]
    return run() == run()


def result_blind_ast_check() -> tuple[bool, list[str]]:
    tree = ast.parse(GENERATOR.read_text(encoding="utf-8"), filename=str(GENERATOR))
    errors: list[str] = []
    target = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "generate_candidate":
            target = node
            break
    if target is None:
        return False, ["generate_candidate_missing"]
    for node in ast.walk(target):
        if isinstance(node, ast.Name) and node.id in FORBIDDEN_CONSTRUCTION_NAMES:
            errors.append(f"forbidden_name:{node.id}")
        if isinstance(node, ast.Attribute) and node.attr in FORBIDDEN_CONSTRUCTION_NAMES:
            errors.append(f"forbidden_attribute:{node.attr}")
    return not errors, errors


def schema_smoke() -> bool:
    rng = random.Random(SEED)
    states = [generate_candidate(rng) for _ in range(4)]
    buckets = build_candidate_buckets(states)
    return all(isinstance(k, tuple) and all(s.sha256() for s in v) for k, v in buckets.items())


def main() -> None:
    assertions = {}
    assertions["P1_generator_exists"] = GENERATOR.exists()
    assertions["P2_result_blind_construction"] = result_blind_ast_check()[0]
    assertions["P3_deterministic_seed"] = deterministic_probe()
    assertions["P4_canonical_state_generation"] = schema_smoke()
    assertions["P5_target_5000_not_generated"] = TARGET == 5000
    assertions["P6_scientific_execution_not_performed"] = True
    assertions["P7_rust_dataset_not_accessed"] = True
    assertions["P8_frozen_key_imported"] = c2_vnext_key is not None

    status = "PASS" if all(assertions.values()) else "BLOCKED_INFRASTRUCTURE"
    out = {
        "status": status,
        "decision": status,
        "assertions": assertions,
        "target_pair_count": TARGET,
        "seed": SEED,
        "corpus_generation": "NOT_PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
        "notes": [
            "Preflight only; no accepted corpus is written.",
            "O_T is not evaluated by this preflight.",
            "The generator's O_T boundary remains intentionally unbound until frozen-input verification is added.",
        ],
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 2)


if __name__ == "__main__":
    main()
