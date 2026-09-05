"""N-R8.4 corpus-construction conformance runner.

Smoke/conformance only. It must not promote artifacts to scientific use and
must not invoke a learner or consume outcomes/results.
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


def check(name, fn, failures):
    try:
        fn()
        print(f"PASS {name}")
    except Exception as exc:
        failures.append((name, repr(exc)))
        print(f"FAIL {name}: {exc}")


def main():
    failures = []
    source = inspect.getsource(m)

    check("constants", lambda: (
        m.PAIR_TARGET == 5000 and m.R8B_PAIR_BUDGET == 2_000_000 and
        m.R8C_PAIR_BUDGET == 5_000_000 and m.G2_SEED == 5_100_000 and
        m.R8B_SEED == 5_200_000 and m.R8C_SEED == 5_300_000
    ) or (_ for _ in ()).throw(AssertionError("CONSTANT_MISMATCH")), failures)

    check("no_learner_dependency", lambda: all(x not in source for x in ("sklearn", "fit(", "predict_proba", "log_loss")), failures)
    check("no_outcome_dependency", lambda: all(x not in source.lower() for x in ("primary_results", "trajectory", "Y_A", "Y_B")), failures)
    check("no_historical_result_literals", lambda: "0.2667941776817361" not in source and "0.18737058183173086" not in source, failures)

    def g2_det():
        a, b = m.make_g2_corpus()
        c, d = m.make_g2_corpus()
        assert a == c and b == d
        assert len(a) == 30000 and len(b) == 10000
        assert [x["episode_id"] for x in a[:3]] == [0, 1, 2]
        assert [x["episode_id"] for x in b[:3]] == [0, 1, 2]
    check("g2_determinism_and_counts", g2_det, failures)

    def state_hash_det():
        train, _ = m.make_g2_corpus()
        s = m._state_from_record(train[0])
        assert m.state_hash(s) == m.state_hash(s)
        assert len(m.state_hash(s)) == 64
        assert m.semantic_state_bytes(s).endswith(b"}")
    check("semantic_state_hash", state_hash_det, failures)

    def b_smoke():
        # Small target proves exact matching mechanics without constructing the full 5k corpus.
        obj = m.build_matched_pairs_b(target=25, budget=10000)
        m.verify_b_pairs(obj)
        for p in obj["pairs"]:
            assert p["A"]["B"] == p["B"]["B"]
            assert p["A"]["T_acc"] != p["B"]["T_acc"]
    check("r8b_exact_matching_smoke", b_smoke, failures)

    def c_smoke():
        obj = m.build_matched_pairs_c(target=25, budget=100000)
        m.verify_c_pairs(obj)
        for p in obj["pairs"]:
            a = m._state_from_record(p["A"])
            b = m._state_from_record(p["B"])
            assert m._c_match_key(a) == m._c_match_key(b)
            assert m._r1_full(a) != m._r1_full(b)
    check("r8c_full_r_inequality_smoke", c_smoke, failures)

    def r2_smoke():
        train, _ = m.make_g2_corpus()
        rows = m.build_r2_records(train[:10])
        assert len(rows) == 10
        assert all(len(x["R2"]) == 24 for x in rows)
        assert all(all(isinstance(v, (int, float)) for v in x["R2"]) for x in rows)
    check("r2_dimension_and_finiteness_smoke", r2_smoke, failures)

    def fail_closed():
        try:
            m.build_matched_pairs_b(target=1, budget=0)
        except RuntimeError as exc:
            assert "TARGET_NOT_REACHED" in str(exc)
        else:
            raise AssertionError("B_NOT_FAIL_CLOSED")
        try:
            m.build_matched_pairs_c(target=1, budget=0)
        except RuntimeError as exc:
            assert "TARGET_NOT_REACHED" in str(exc)
        else:
            raise AssertionError("C_NOT_FAIL_CLOSED")
    check("pair_search_fail_closed", fail_closed, failures)

    def source_separation():
        forbidden = ("primary_results.json", "PROVENANCE.json", "N-R7_RUN01", "N-R7_RUN02")
        assert not any(x in source for x in forbidden)
    check("result_artifact_separation", source_separation, failures)

    sha = hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest()
    print(json.dumps({
        "runner": "N_R8_CONFORMANCE_RUNNER_v0.1",
        "implementation_sha256": sha,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
        "scientific_execution": "NOT_PERFORMED",
    }, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
