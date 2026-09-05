"""N-R5.2 predictor representation conformance runner.

Smoke-scale only. No learner, outcome, trajectory generation, network access,
or confirmatory inference.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
PRED_PATH = SRC / "branch_n_r5_predictor_v01.py"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


m = load("branch_n_r5_predictor_v01", PRED_PATH)


def snapshot(i: int, objective: str = "O01"):
    return {
        "episode_id": i,
        "components": ["A1", "B1", "C1"],
        "edges": [["A1", "B1"], ["B1", "C1"]],
        "resources": [0, 2, 3],
        "objective": objective,
    }


def check(name, ok, details=None):
    return {"name": name, "status": "PASS" if ok else "FAIL", **(details or {})}


def main():
    checks = []
    s = snapshot(7, "O04")
    p = m.encode_predictor(s)
    checks.append(check("B_dimension", len(p.B) == 16, {"dimension": len(p.B)}))
    checks.append(check("R_dimension", len(p.R) == 58, {"dimension": len(p.R)}))
    checks.append(check("BR_dimension", len(p.BR) == 74, {"dimension": len(p.BR)}))
    checks.append(check("B_layout", p.B[:4] == (3, 0, 2, 3) and p.B[4:8] == (0,0,0,1) and sum(p.B[4:]) == 1))
    checks.append(check("objective_one_hot", p.B[4 + 3] == 1 and all(x == 0 for x in p.B[4:7]) and all(x == 0 for x in p.B[8:])))
    checks.append(check("BR_concatenation", p.BR == p.B + p.R))
    checks.append(check("snapshot_traceability", len(p.initial_snapshot_sha256) == 64 and all(c in "0123456789abcdef" for c in p.initial_snapshot_sha256)))

    p2 = m.encode_predictor(s)
    checks.append(check("byte_determinism", m.canonical_predictor_bytes(p) == m.canonical_predictor_bytes(p2)))

    # episode_id is provenance/trace identity. It is included in the predictor record,
    # but must not alter the feature vectors or the snapshot content hash semantics.
    # The implementation currently hashes the complete snapshot record, including ID;
    # therefore the conformance criterion is that only trace fields change when ID changes.
    altered = dict(s)
    altered["episode_id"] = 8
    p3 = m.encode_predictor(altered)
    checks.append(check(
        "episode_identity_changes_trace_only",
        p3.B == p.B and p3.R == p.R and p3.BR == p.BR and p3.episode_id != p.episode_id
        and p3.initial_snapshot_sha256 != p.initial_snapshot_sha256,
    ))

    # Same S0 with hypothetical different post-snapshot fields: predictor has no such input.
    forbidden = {"trajectory": [], "outcome": 1, "terminal_reason": "SUCCESS", "steps": []}
    s_with_forbidden = {**s, **forbidden}
    p4 = m.encode_predictor(s_with_forbidden)
    checks.append(check("no_trajectory_outcome_dependency", p4.B == p.B and p4.R == p.R and p4.BR == p.BR))

    s2 = snapshot(7, "O05")
    p5 = m.encode_predictor(s2)
    # Objective is part of S0 and is explicitly encoded in B. R is structural and
    # objective-independent under the frozen Branch N transformation semantics.
    checks.append(check("objective_encoding_distinct", p5.B != p.B and p5.R == p.R and p5.BR != p.BR))

    source = PRED_PATH.read_text(encoding="utf-8").lower()
    forbidden_tokens = ["sklearn", "histgradientboosting", "randomforest", "logloss", "requests", "urllib", "httpx", "socket"]
    found = [t for t in forbidden_tokens if t in source]
    checks.append(check("no_learner_or_network_dependency", not found, {"forbidden_tokens_found": found}))

    checks.append(check("no_historical_result_literal", "0.07942359585000518" not in source))
    checks.append(check("no_trajectory_generation_dependency", "branch_n_r4b_trajectory" not in source))

    status = "PASS" if all(x["status"] == "PASS" for x in checks) else "FAIL"
    print(json.dumps({
        "runner": "N_R5_CONFORMANCE_RUNNER_v0.2",
        "checks": checks,
        "scientific_execution": "NOT_PERFORMED",
        "learner_execution": "NOT_PERFORMED",
        "confirmatory_inference": "NOT_PERFORMED",
        "status": status,
        "implementation_sha256": hashlib.sha256(PRED_PATH.read_bytes()).hexdigest(),
    }, indent=2))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
