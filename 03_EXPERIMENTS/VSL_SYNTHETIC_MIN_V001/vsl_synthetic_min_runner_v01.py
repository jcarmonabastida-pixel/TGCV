"""TGCV VSL Synthetic Minimum v0.1 — experimental runner.

The fixture defines the frozen numerical contract. This runner adds an
independent transformation/accessibility layer and evaluates the frozen
outcome/value functions only from the final state.

It is intentionally synthetic and non-causal: no real-world inference.
"""

from dataclasses import dataclass
from typing import Dict, Tuple

SPEC_VERSION = "VSL_SYNTHETIC_MIN_v0.1"
BASELINE = (10, 10)


@dataclass(frozen=True)
class State:
    q: int
    r: int


@dataclass(frozen=True)
class TransitionResult:
    case_id: str
    accessibility_changed: bool
    selected_transform: str
    final_state: State
    exogenous_factor: int = 0


# Independent transformation layer. The outcome function below does not
# receive this object or any accessibility/treatment variable.
TRANSFORMS = {
    "A": lambda s: State(s.q, s.r),
    "B": lambda s: State(s.q + 4, s.r),
}


def accessible_transforms(case_id: str) -> Tuple[str, ...]:
    if case_id in ("T2", "T3", "NC2"):
        return ("A", "B")
    return ("A",)


def select_transform(case_id: str, accessible: Tuple[str, ...]) -> str:
    if case_id == "T3":
        return "B"
    return "A"


def execute_transition(case_id: str) -> TransitionResult:
    s0 = State(*BASELINE)
    accessible = accessible_transforms(case_id)
    changed = accessible != ("A",)
    selected = select_transform(case_id, accessible)

    if selected not in accessible:
        raise AssertionError("selected transform is not accessible")

    if case_id == "T4":
        final_state = State(s0.q + 2, s0.r)
        exogenous_factor = 2
    else:
        final_state = TRANSFORMS[selected](s0)
        exogenous_factor = 0

    return TransitionResult(
        case_id=case_id,
        accessibility_changed=changed,
        selected_transform=selected,
        final_state=final_state,
        exogenous_factor=exogenous_factor,
    )


# Frozen VSL computational path: final state -> outcome -> value.
# No treatment/accessibility/case identifier is an input.
def outcome(state: State) -> float:
    return state.q + 0.5 * state.r


def value(outcome_value: float) -> float:
    return outcome_value


EXPECTED = {
    "T1": (False, "A", (10, 10), 0, 0.0),
    "T2": (True, "A", (10, 10), 0, 0.0),
    "T3": (True, "B", (14, 10), 0, 4.0),
    "T4": (False, "A", (12, 10), 2, 2.0),
    "NC1": (False, "A", (10, 10), 0, 0.0),
    "NC2": (True, "A", (10, 10), 0, 0.0),
}


def run_case(case_id: str) -> Dict:
    result = execute_transition(case_id)
    o0 = outcome(State(*BASELINE))
    o1 = outcome(result.final_state)
    v0 = value(o0)
    v1 = value(o1)

    return {
        "spec_version": SPEC_VERSION,
        "case_id": case_id,
        "baseline_state": {"q": BASELINE[0], "r": BASELINE[1]},
        "final_state": {"q": result.final_state.q, "r": result.final_state.r},
        "accessibility_changed": result.accessibility_changed,
        "selected_transform": result.selected_transform,
        "outcome_baseline": o0,
        "outcome_final": o1,
        "delta_outcome": o1 - o0,
        "value_baseline": v0,
        "value_final": v1,
        "delta_value": v1 - v0,
        "exogenous_factor": result.exogenous_factor,
    }


def validate_runner() -> None:
    assert outcome(State(*BASELINE)) == 15.0

    for case_id, expected in EXPECTED.items():
        observed = run_case(case_id)
        exp_access, exp_selected, exp_final, exp_factor, exp_delta = expected

        assert observed["accessibility_changed"] == exp_access
        assert observed["selected_transform"] == exp_selected
        assert (observed["final_state"]["q"], observed["final_state"]["r"]) == exp_final
        assert observed["exogenous_factor"] == exp_factor
        assert observed["delta_outcome"] == exp_delta
        assert observed["delta_value"] == exp_delta
        assert observed["outcome_baseline"] == 15.0
        assert observed["value_baseline"] == 15.0

    assert run_case("T2")["delta_value"] == 0.0
    assert run_case("T3")["delta_value"] == 4.0
    assert run_case("T4")["delta_value"] == 2.0
    assert run_case("NC2")["delta_value"] == 0.0


if __name__ == "__main__":
    validate_runner()
    for case_id in EXPECTED:
        print(run_case(case_id))
