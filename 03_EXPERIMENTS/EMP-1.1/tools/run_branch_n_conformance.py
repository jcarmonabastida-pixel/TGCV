"""N-R2 conformance runner for Branch N transformation/R implementation.

This runner checks implementation invariants only. It does not execute any
scientific model, fit, outcome, or confirmatory EMP-1.1 analysis.
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


def assert_true(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"{name}: {detail}")
    return {"name": name, "status": "PASS"}


def main():
    checks = []

    s = mod.State.make(
        ["A1", "B1", "C1"],
        [("A1", "B1"), ("B1", "C1")],
        [1, 2, 3],
        "O07",
    )
    t = mod.enumerate_transformations(s)
    families = {x[0] for x in t}
    checks.append(assert_true("six_families_present", families == set(mod.FAMILIES), str(sorted(families))))
    checks.append(assert_true("canonical_transformation_order", t == tuple(sorted(t, key=lambda x: (mod.FAMILIES.index(x[0]), tuple((mod.COMPONENTS.index(p) if isinstance(p, str) else p) for p in x[1:]))))))

    add = next(x for x in t if x[0] == "ADD_COMPONENT")
    s_add = mod.apply_transformation(s, add)
    checks.append(assert_true("add_component_transition", len(s_add.components) == 4 and len(s_add.edges) == 2))

    rem = next(x for x in t if x[0] == "REMOVE_COMPONENT" and x[1] == "B1")
    s_rem = mod.apply_transformation(s, rem)
    checks.append(assert_true("remove_component_transition", s_rem.components == ("A1", "C1") and s_rem.edges == ()))

    add_edge = next(x for x in t if x[0] == "ADD_EDGE")
    s_ae = mod.apply_transformation(s, add_edge)
    checks.append(assert_true("add_edge_transition", len(s_ae.edges) == len(s.edges) + 1))

    rem_edge = next(x for x in t if x[0] == "REMOVE_EDGE")
    s_re = mod.apply_transformation(s, rem_edge)
    checks.append(assert_true("remove_edge_transition", len(s_re.edges) == len(s.edges) - 1))

    rw = next(x for x in t if x[0] == "REWIRE_EDGE")
    s_rw = mod.apply_transformation(s, rw)
    checks.append(assert_true("rewire_edge_transition", len(s_rw.edges) == len(s.edges) and s_rw.resources == s.resources and s_rw.objective == s.objective))

    mr = next(x for x in t if x[0] == "MODIFY_RESOURCE" and x[2] == +1)
    s_mr = mod.apply_transformation(s, mr)
    diffs = [b - a for a, b in zip(s.resources, s_mr.resources)]
    checks.append(assert_true("modify_resource_transition", sum(d != 0 for d in diffs) == 1 and sum(diffs) == 1 and s_mr.objective == s.objective and s_mr.edges == s.edges))

    for tau in t:
        s2 = mod.apply_transformation(s, tau)
        assert_true("global_transition_validity", len(s2.components) >= 1 and len(s2.components) <= 6)
        assert_true("objective_preserved", s2.objective == s.objective)
        assert_true("no_self_loops", all(u != v for u, v in s2.edges))
        assert_true("no_duplicate_edges", len(s2.edges) == len(set(s2.edges)))

    r1 = mod.encode_r(s, t)
    r2 = mod.encode_r(s, t)
    checks.append(assert_true("r_dimension_58", len(r1) == 58))
    checks.append(assert_true("same_state_determinism", r1 == r2))
    checks.append(assert_true("serialization_determinism", mod.canonical_serialization(r1) == mod.canonical_serialization(r2)))

    s_perm = mod.State.make(
        ["C1", "A1", "B1"],
        [("B1", "C1"), ("A1", "B1")],
        [1, 2, 3],
        "O07",
    )
    checks.append(assert_true("input_order_invariance", mod.encode_r(s_perm) == r1))

    r_empty = mod.encode_r(s, ())
    checks.append(assert_true("empty_tacc_all_zero", r_empty == (0,) * 58))

    checks.append(assert_true("no_noop_transformations", all(mod.apply_transformation(s, tau) != s for tau in t)))

    r2_counts = r1[6:12]
    expected_counts = tuple(sum(1 for tau in t if tau[0] == f) for f in mod.FAMILIES)
    checks.append(assert_true("family_count_completeness", r2_counts == expected_counts))

    s_obj = mod.State.make(s.components, s.edges, s.resources, "O08")
    checks.append(assert_true("objective_exogeneity", mod.encode_r(s_obj) == r1))

    blob = IMPL.read_bytes()
    result = {
        "runner": "BRANCH_N_CONFORMANCE_RUNNER_v0.1",
        "status": "PASS",
        "implementation_path": str(IMPL),
        "implementation_sha256": hashlib.sha256(blob).hexdigest(),
        "checks": checks,
        "r_dimension": len(r1),
        "t_acc_size_fixture": len(t),
        "scientific_execution": "NOT_PERFORMED",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
