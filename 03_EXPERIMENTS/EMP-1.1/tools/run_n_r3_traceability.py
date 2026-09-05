"""N-R3 independent feature-by-feature traceability runner.

Checks the prospective Branch N R encoding against independently derived
expected values for fixed fixtures. No scientific execution is performed.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
IMPL = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src" / "branch_n_r_v02.py"
spec = importlib.util.spec_from_file_location("branch_n_r_v02", IMPL)
if spec is None or spec.loader is None:
    raise RuntimeError("IMPORT_SPEC_FAILURE")
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)

COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")
FAMILIES = ("ADD_COMPONENT", "REMOVE_COMPONENT", "ADD_EDGE", "REMOVE_EDGE", "REWIRE_EDGE", "MODIFY_RESOURCE")


def expected_r(state, tacc):
    counts = {f: 0 for f in FAMILIES}
    for t in tacc:
        counts[t[0]] += 1
    r1 = tuple(int(counts[f] > 0) for f in FAMILIES)
    r2 = tuple(counts[f] for f in FAMILIES)
    if not tacc:
        return (0,) * 58

    r3 = []
    for v in COMPONENTS:
        r3.extend((
            sum(t[0] == "ADD_COMPONENT" and t[1] == v for t in tacc),
            sum(t[0] == "REMOVE_COMPONENT" and t[1] == v for t in tacc),
            sum(t[0] == "ADD_EDGE" and v in (t[1], t[2]) for t in tacc),
            sum(t[0] == "REMOVE_EDGE" and v in (t[1], t[2]) for t in tacc),
            sum(t[0] == "REWIRE_EDGE" and v in (t[1], t[2], t[3]) for t in tacc),
        ))

    successors = tuple(mod.apply_transformation(state, t) for t in tacc)
    cc = tuple(len(s.components) for s in successors)
    ec = tuple(len(s.edges) for s in successors)
    rv = tuple(s.resources for s in successors)
    sv = tuple((s.components, s.edges, s.resources, s.objective) for s in successors)
    r4 = (
        sum(t[0] == "ADD_COMPONENT" for t in tacc),
        sum(t[0] == "REMOVE_COMPONENT" for t in tacc),
        sum(t[0] == "ADD_EDGE" for t in tacc),
        sum(t[0] == "REMOVE_EDGE" for t in tacc),
        sum(t[0] == "REWIRE_EDGE" for t in tacc),
        sum(t[0] == "MODIFY_RESOURCE" and t[2] == +1 for t in tacc),
        sum(t[0] == "MODIFY_RESOURCE" and t[2] == -1 for t in tacc),
        sum(s == state for s in successors),
        len(set(cc)), len(set(ec)), len(set(rv)), len(set(sv)),
        max(cc), min(cc), max(ec), min(ec),
    )
    return tuple(r1 + r2 + tuple(r3) + r4)


def check_fixture(name, state, supplied_tacc=None):
    tacc = mod.enumerate_transformations(state) if supplied_tacc is None else supplied_tacc
    expected = expected_r(state, tacc)
    actual = mod.encode_r(state, tacc)
    mismatches = [
        {"index": i, "expected": expected[i], "actual": actual[i]}
        for i in range(58) if expected[i] != actual[i]
    ]
    if mismatches:
        raise AssertionError(f"{name}: feature mismatch {mismatches}")
    return {"name": name, "status": "PASS", "t_acc_size": len(tacc), "r_dimension": len(actual)}


def main():
    checks = []
    s1 = mod.State.make(
        ["A1", "B1", "C1"], [("A1", "B1"), ("B1", "C1")], [1, 2, 3], "O07"
    )
    s2 = mod.State.make(
        ["A1", "A2", "B1", "C1"], [("A1", "B1"), ("C1", "A2"), ("B1", "C1")], [0, 3, 1], "O12"
    )
    checks.append(check_fixture("fixture_1_feature_by_feature", s1))
    checks.append(check_fixture("fixture_2_feature_by_feature", s2))
    checks.append(check_fixture("fixture_empty_tacc", s1, ()))

    t1 = mod.enumerate_transformations(s1)
    s1_alt = mod.State.make(s1.components, s1.edges, s1.resources, "O08")
    checks.append({"name": "objective_exogeneity", "status": "PASS"} if mod.encode_r(s1, t1) == mod.encode_r(s1_alt, t1) else (_ for _ in ()).throw(AssertionError("objective_exogeneity")))

    checks.append({"name": "tacc_encoder_boundary", "status": "PASS"} if mod.encode_r(s1, ()) == (0,) * 58 else (_ for _ in ()).throw(AssertionError("empty_tacc")))

    digest = hashlib.sha256(IMPL.read_bytes()).hexdigest()
    print(json.dumps({
        "runner": "N_R3_TRACEABILITY_RUNNER_v0.1",
        "status": "PASS",
        "implementation_path": str(IMPL),
        "implementation_sha256": digest,
        "checks": checks,
        "scientific_execution": "NOT_PERFORMED",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
