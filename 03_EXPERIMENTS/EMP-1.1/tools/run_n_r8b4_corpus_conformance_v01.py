"""N-R8.4 bounded conformance runner.

Conformance only. This runner MUST NOT construct the 5,000-pair corpora.
All corpus-related checks use tiny deterministic fixtures.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import branch_n_r8b4_corpus_v01 as m
import branch_n_r8_operationalisation_v01 as op
from branch_n_r8_operationalisation_v01 import b_vector
from branch_n_r_v02 import encode_r


def check(name, fn, failures):
    try:
        fn()
        print(f"PASS {name}")
    except Exception as exc:
        failures.append((name, repr(exc)))
        print(f"FAIL {name}: {exc}")


def fixture_states():
    a = m.canonical_state(("A1", "A2", "B1"), (("A1", "A2"),), (0, 1, 2), "O01")
    b = m.canonical_state(("A1", "A2", "B1"), (("A1", "B1"),), (0, 1, 2), "O01")
    return a, b


def find_c_fixture():
    """Enumerate only the 64 edge subsets of a 3-component graph.

    This is deliberately tiny and deterministic. It searches for two states
    with identical amended N-R8-C matching keys and different full 58-D R.
    """
    comps = ("A1", "A2", "B1")
    possible = tuple((u, v) for u in comps for v in comps if u != v)
    buckets = {}
    for mask in range(1 << len(possible)):
        edges = tuple(e for i, e in enumerate(possible) if mask & (1 << i))
        s = m.canonical_state(comps, edges, (0, 1, 2), "O01")
        key = m._c_match_key(s)
        r = tuple(encode_r(s))
        for prior_s, prior_r in buckets.get(key, []):
            if prior_r != r:
                return prior_s, s
        buckets.setdefault(key, []).append((s, r))
    raise AssertionError("NO_C_FIXTURE_FOUND_WITHIN_64_EDGE_SUBSETS")


def main():
    failures = []
    source = inspect.getsource(m)
    runner_source = inspect.getsource(sys.modules[__name__])

    check("constants", lambda: (
        m.PAIR_TARGET == 5000 and m.R8B_PAIR_BUDGET == 2_000_000 and
        m.R8C_PAIR_BUDGET == 5_000_000 and m.G2_SEED == 5_100_000 and
        m.R8B_SEED == 5_200_000 and m.R8C_SEED == 5_300_000
    ) or (_ for _ in ()).throw(AssertionError("CONSTANT_MISMATCH")), failures)
    check("no_learner_dependency", lambda: all(x not in source for x in ("sklearn", "fit(", "predict_proba", "log_loss")), failures)
    check("no_result_dependency", lambda: all(x not in source.lower() for x in ("primary_results", "trajectory", "y_a", "y_b", "n-r7_run01", "n-r7_run02")), failures)
    check("no_historical_result_literals", lambda: "0.2667941776817361" not in source and "0.18737058183173086" not in source, failures)
    check("runner_cannot_request_full_target", lambda: "target=5000" not in runner_source, failures)

    def g2_det():
        rng1 = m.random.Random(m.G2_SEED)
        rng2 = m.random.Random(m.G2_SEED)
        a = [m.generate_g2(rng1) for _ in range(10)]
        b = [m.generate_g2(rng2) for _ in range(10)]
        assert a == b
        assert all(len(s.components) in (3, 4, 5) for s in a)
        assert all(len(s.resources) == 3 for s in a)
        assert all(s.objective.startswith("O") for s in a)
    check("g2_determinism_bounded", g2_det, failures)

    def r58():
        a, _ = fixture_states()
        r = tuple(encode_r(a))
        assert len(r) == 58 and tuple(m._r_full(a)) == r
    check("full_r_dimension_and_authority", r58, failures)

    def b_fixture():
        a, b = fixture_states()
        assert tuple(b_vector(a)) == tuple(b_vector(b))
        assert m._b_key(a) == m._b_key(b)
        assert tuple(m.tacc(a)) != tuple(m.tacc(b))
        def rec(s):
            return {"state": m.asdict(s), "state_hash": m.state_hash(s), "B": list(m._b_key(s)), "T_acc": [list(t) for t in m.tacc(s)]}
        m.verify_b_pairs({"target": 1, "pairs": [{"pair_id": 0, "A": rec(a), "B": rec(b)}]})
    check("r8b_exact_matching_fixture", b_fixture, failures)

    def c_fixture():
        a, b = find_c_fixture()
        ra, rb = tuple(encode_r(a)), tuple(encode_r(b))
        assert len(ra) == len(rb) == 58
        assert m._c_match_key(a) == m._c_match_key(b)
        assert ra != rb
        def rec(s):
            return {"state": m.asdict(s), "state_hash": m.state_hash(s), "R": list(encode_r(s))}
        m.verify_c_pairs({"target": 1, "pairs": [{"pair_id": 0, "A": rec(a), "B": rec(b)}]})
    check("r8c_full_r_inequality_fixture", c_fixture, failures)

    def r2_fixture():
        a, _ = fixture_states(); vals = m.r2(a)
        assert len(vals) == 24 and all(isinstance(v, float) for v in vals)
    check("r2_dimension_and_finiteness", r2_fixture, failures)

    def empty_r2():
        a, _ = fixture_states()
        original = op.tacc
        try:
            op.tacc = lambda _s: []
            assert m.r2(a) == (0.0,) * 24
        finally:
            op.tacc = original
    check("r2_empty_zero", empty_r2, failures)

    def fail_closed():
        for fn in (m.build_matched_pairs_b, m.build_matched_pairs_c):
            try:
                fn(target=1, budget=0)
            except RuntimeError as exc:
                assert "TARGET_NOT_REACHED" in str(exc)
            else:
                raise AssertionError("NOT_FAIL_CLOSED")
    check("pair_search_fail_closed", fail_closed, failures)

    sha = hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest()
    print(json.dumps({"runner":"N_R8_CONFORMANCE_RUNNER_v0.4",
                      "implementation_sha256":sha,"failures":failures,
                      "status":"PASS" if not failures else "FAIL",
                      "scientific_execution":"NOT_PERFORMED",
                      "full_pair_corpus_generation":"NOT_PERFORMED"},
                     indent=2, sort_keys=True))
    return 0 if not failures else 1

if __name__ == "__main__":
    raise SystemExit(main())
