"""TGCV VSL Synthetic Minimum v0.1 — executable fixture.

This module implements only the frozen fixture contract.
It does not execute the experiment or infer causality.
"""

from dataclasses import dataclass
from typing import Dict, Tuple


SPEC_VERSION = "VSL_SYNTHETIC_MIN_v0.1"
BASELINE: Tuple[int, int] = (10, 10)


@dataclass(frozen=True)
class State:
    q: int
    r: int


@dataclass(frozen=True)
class Case:
    case_id: str
    accessibility_changed: bool
    final_state: State
    exogenous_factor: int = 0


CASES: Dict[str, Case] = {
    "T1": Case("T1", False, State(10, 10)),
    "T2": Case("T2", True, State(10, 10)),
    "T3": Case("T3", True, State(14, 10)),
    "T4": Case("T4", False, State(12, 10), exogenous_factor=2),
    "NC1": Case("NC1", False, State(10, 10)),
    "NC2": Case("NC2", True, State(10, 10)),
}


def outcome(state: State) -> float:
    """Compute downstream outcome from final state only."""
    return state.q + 0.5 * state.r


def value(outcome_value: float) -> float:
    """Frozen synthetic VSL mapping O -> V*."""
    return outcome_value


def accessibility_delta(case: Case) -> bool:
    """Fixture-level accessibility delta indicator."""
    return case.accessibility_changed


def evaluate(case_id: str) -> dict:
    case = CASES[case_id]
    baseline = State(*BASELINE)
    o0 = outcome(baseline)
    o1 = outcome(case.final_state)
    delta_o = o1 - o0
    v0 = value(o0)
    v1 = value(o1)
    delta_v = v1 - v0

    return {
        "spec_version": SPEC_VERSION,
        "case_id": case.case_id,
        "baseline_state": {"q": baseline.q, "r": baseline.r},
        "final_state": {"q": case.final_state.q, "r": case.final_state.r},
        "accessibility_changed": accessibility_delta(case),
        "outcome_baseline": o0,
        "outcome_final": o1,
        "delta_outcome": delta_o,
        "value_baseline": v0,
        "value_final": v1,
        "delta_value": delta_v,
        "exogenous_factor": case.exogenous_factor,
    }


def validate_fixture() -> None:
    assert BASELINE == (10, 10)
    assert outcome(State(10, 10)) == 15.0

    expected = {
        "T1": (False, 0.0, 0.0),
        "T2": (True, 0.0, 0.0),
        "T3": (True, 4.0, 4.0),
        "T4": (False, 2.0, 2.0),
        "NC1": (False, 0.0, 0.0),
        "NC2": (True, 0.0, 0.0),
    }

    for case_id, (access_changed, delta_o, delta_v) in expected.items():
        result = evaluate(case_id)
        assert result["accessibility_changed"] == access_changed
        assert result["delta_outcome"] == delta_o
        assert result["delta_value"] == delta_v

    # Non-circularity: outcome is a pure function of final q,r.
    assert outcome(State(14, 10)) == 19.0
    assert outcome(State(12, 10)) == 17.0

    # T4's exogenous factor is not consumed by outcome/value calculation.
    assert evaluate("T4")["exogenous_factor"] == 2
    assert evaluate("T4")["delta_outcome"] == 2.0

    # Required contrasts.
    assert evaluate("T2")["accessibility_changed"] and evaluate("T2")["delta_value"] == 0.0
    assert not evaluate("T4")["accessibility_changed"] and evaluate("T4")["delta_value"] > 0.0


if __name__ == "__main__":
    validate_fixture()
    for case_id in CASES:
        print(evaluate(case_id))
