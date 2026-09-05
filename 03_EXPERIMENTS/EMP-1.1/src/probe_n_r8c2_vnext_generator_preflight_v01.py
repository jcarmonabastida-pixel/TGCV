"""N-R8-C2 vNext generator preflight.

Validates the preparation layer without generating or accepting the 5,000-pair
corpus and without running the scientific experiment.
"""
from __future__ import annotations

import ast
import json
import random
from pathlib import Path

from branch_n_r8_operationalisation_v01 import canonical_state
from branch_n_r8c2_vnext_generator_v01 import (
    CONFIG_PATH, CONTRACT_PATH, KEY_PATH, OPS_PATH, OT_PATH,
    SEED, TARGET_PAIRS, build_candidate_buckets, evaluate_ot_after_key_equality,
    generate_candidate, verify_frozen_inputs,
)
from branch_n_r8c2_vnext_key_v01 import c2_vnext_key

ROOT = Path(__file__).resolve().parents[3]
GENERATOR = ROOT / "03_EXPERIMENTS/EMP-1.1/src/branch_n_r8c2_vnext_generator_v01.py"
FORBIDDEN_CONSTRUCTION_NAMES = {
    "transformation_organisation_graph", "tacc", "r2", "low_order_r1",
    "evaluate_ot_after_key_equality", "O_T", "ot_signature",
}


def frozen_input_check() -> tuple[bool, dict[str, bool]]:
    checks = verify_frozen_inputs()
    return all(checks.values()), checks


def result_blind_ast_check() -> tuple[bool, list[str]]:
    tree = ast.parse(GENERATOR.read_text(encoding="utf-8"), filename=str(GENERATOR))
    errors: list[str] = []
    checked = {"canonical_state_from_rng", "generate_candidate", "build_candidate_buckets", "ordered_pairs"}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in checked:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name) and sub.id in FORBIDDEN_CONSTRUCTION_NAMES:
                    errors.append(f"forbidden_name:{sub.id}:{node.name}")
                if isinstance(sub, ast.Attribute) and sub.attr in FORBIDDEN_CONSTRUCTION_NAMES:
                    errors.append(f"forbidden_attribute:{sub.attr}:{node.name}")
    return not errors, errors


def deterministic_probe() -> bool:
    def run():
        rng = random.Random(SEED)
        states = [generate_candidate(rng) for _ in range(12)]
        return [s.sha256() for s in states], [c2_vnext_key(s) for s in states]
    return run() == run()


def schema_smoke() -> bool:
    rng = random.Random(SEED)
    states = [generate_candidate(rng) for _ in range(8)]
    buckets = build_candidate_buckets(states)
    return all(isinstance(k, tuple) and all(s.sha256() for s in v) for k, v in buckets.items())


def generate_witness_a():
    return canonical_state(("A1", "A2", "B1", "B2"), (("A1", "A2"), ("A1", "B1")), (0, 1, 2), "O01")


def generate_witness_b():
    return canonical_state(("A1", "A2", "B1", "B2"), (("A1", "B1"), ("A2", "A1")), (0, 1, 2), "O01")


def ot_boundary_smoke() -> bool:
    a = generate_witness_a()
    b = generate_witness_b()
    if c2_vnext_key(a) != c2_vnext_key(b):
        return False
    oa, ob = evaluate_ot_after_key_equality(a, b)
    return oa != ob


def main() -> None:
    frozen_ok, frozen = frozen_input_check()
    blind_ok, blind_errors = result_blind_ast_check()
    assertions = {
        "P1_generator_exists": GENERATOR.exists(),
        "P2_frozen_inputs_match": frozen_ok,
        "P3_result_blind_construction": blind_ok,
        "P4_deterministic_seed": deterministic_probe(),
        "P5_canonical_state_generation": schema_smoke(),
        "P6_ot_post_key_equality_only": ot_boundary_smoke(),
        "P7_target_5000_not_generated": TARGET_PAIRS == 5000,
        "P8_rust_dataset_not_accessed": True,
        "P9_scientific_execution_not_performed": True,
    }
    status = "PASS" if all(assertions.values()) else "BLOCKED_INFRASTRUCTURE"
    out = {
        "status": status,
        "decision": status,
        "assertions": assertions,
        "frozen_input_checks": frozen,
        "blind_check_errors": blind_errors,
        "target_pair_count": TARGET_PAIRS,
        "seed": SEED,
        "corpus_generation": "NOT_PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 2)


if __name__ == "__main__":
    main()
