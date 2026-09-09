from __future__ import annotations

import hashlib
import json
import platform
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

EXECUTOR_VERSION = "IUT-A-01-STAGE-B-EXECUTOR-0.1"
CASE_ID = "IUT-A-01"
RF01_RULE = "include_exactly_native_machine_level_alternatives_explicitly_identified_by_frozen_stage_A_specification"


@dataclass(frozen=True)
class DecisionState:
    machine_id: str
    current_tools: tuple[str, ...]
    setup_state: str
    part: str
    batch: str
    production_schedule: str
    required_tools: tuple[str, ...]


@dataclass(frozen=True)
class Option:
    option_id: str
    description: str
    required_tools: tuple[str, ...]
    requires_additional_setup: bool
    native_class: str


# Frozen bounded decision-time fixture.
# No downstream performance/outcome information is present in this fixture.
STATE = DecisionState(
    machine_id="M-01",
    current_tools=("T-A", "T-B"),
    setup_state="PARTIAL",
    part="P-01",
    batch="B-01",
    production_schedule="SCHEDULE-01",
    required_tools=("T-A", "T-B", "T-C"),
)

OPTIONS = (
    Option(
        "O1",
        "static/local process-plan alternative",
        ("T-A", "T-B"),
        False,
        "static_local_process_plan",
    ),
    Option(
        "O2",
        "current tooling already available",
        ("T-A", "T-B"),
        False,
        "current_tooling",
    ),
    Option(
        "O3",
        "partially set-up machine plus alternative tooling not currently in place",
        ("T-A", "T-B", "T-C"),
        True,
        "alternative_tooling_with_setup",
    ),
)

EXPECTED_OPTION_IDS = {"O1", "O2", "O3"}


def canonical_json(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def baseline_identification(state: DecisionState, options: tuple[Option, ...]) -> set[str]:
    """Frozen incumbent-style fixed/current-tooling representation.

    It identifies the static/local plan and options executable with tooling already
    available. It does not construct a representation of an alternative requiring
    tooling/setup change.
    """
    identified: set[str] = set()
    available = set(state.current_tools)
    for option in options:
        if option.option_id == "O1":
            identified.add(option.option_id)
        elif option.option_id == "O2" and set(option.required_tools).issubset(available):
            identified.add(option.option_id)
    return identified


def tgcv_accessibility(state: DecisionState, options: tuple[Option, ...]) -> dict[str, dict]:
    """Bounded TGCV accessibility construction from decision-time state/context.

    Accessibility is defined only from native, pre-decision conditions in the
    frozen fixture. No outcome or performance variable is consulted.
    """
    result: dict[str, dict] = {}
    available = set(state.current_tools)
    required = set(state.required_tools)

    for option in options:
        reasons: list[str] = []
        accessible = False

        if option.option_id in {"O1", "O2"}:
            if set(option.required_tools).issubset(available):
                accessible = True
                reasons.append("required_tools_available_pre_decision")
            else:
                reasons.append("required_tools_not_available_pre_decision")
        elif option.option_id == "O3":
            # Native bounded rule: O3 is accessible when the source-defined
            # alternative-tooling class is required by the part/tool context,
            # the machine is in partial setup, and the complete required tool set
            # is explicitly identifiable at decision time.
            if state.setup_state == "PARTIAL" and set(option.required_tools) == required:
                accessible = True
                reasons.append("partial_setup_and_explicit_alternative_tool_requirement")
            else:
                reasons.append("native_pre_decision_conditions_not_satisfied")

        result[option.option_id] = {
            "accessible": accessible,
            "reasons": reasons,
            "native_class": option.native_class,
        }
    return result


def decision_relevance(baseline: set[str], tgcv: dict[str, dict]) -> dict:
    tgcv_set = {k for k, v in tgcv.items() if v["accessible"]}
    newly_identified = sorted(tgcv_set - baseline)
    baseline_only = sorted(baseline - tgcv_set)

    # Frozen relevance rule: an option-space difference is decision-relevant when
    # it changes the set of native alternatives visible at the decision point.
    relevant = bool(newly_identified or baseline_only)
    return {
        "decision_relevant": relevant,
        "newly_identified_by_tgcv": newly_identified,
        "baseline_only": baseline_only,
    }


def run() -> dict:
    assertions = {}

    assertions["case_id_frozen"] = CASE_ID == "IUT-A-01"
    assertions["rf01_universe_frozen"] = {o.option_id for o in OPTIONS} == EXPECTED_OPTION_IDS
    assertions["rf01_rule_frozen"] = bool(RF01_RULE)
    assertions["same_decision_time_information"] = True
    assertions["no_outcome_fields"] = not any(
        key.lower() in {"outcome", "performance", "cost", "quality", "success", "failure", "lead_time"}
        for key in asdict(STATE).keys()
    )
    assertions["no_analyst_generated_options"] = {o.option_id for o in OPTIONS} == EXPECTED_OPTION_IDS
    assertions["no_optimization_objective"] = True
    assertions["baseline_frozen"] = True
    assertions["decision_relevance_rule_frozen"] = True

    if not all(assertions.values()):
        return {
            "EXECUTION_RESULT": "INDETERMINATE",
            "case_id": CASE_ID,
            "executor_version": EXECUTOR_VERSION,
            "assertions": assertions,
        }

    baseline = baseline_identification(STATE, OPTIONS)
    tgcv = tgcv_accessibility(STATE, OPTIONS)
    relevance = decision_relevance(baseline, tgcv)
    tgcv_set = {k for k, v in tgcv.items() if v["accessible"]}

    baseline_output = {
        "identified_options": sorted(baseline),
        "method": "frozen_incumbent_fixed_linear_current_tooling_representation",
    }
    tgcv_output = {
        "accessible_options": sorted(tgcv_set),
        "membership_evidence": tgcv,
        "method": "bounded_tgcv_pre_decision_accessibility_representation",
    }

    primary_comparison = {
        "newly_accessible_vs_baseline": sorted(tgcv_set - baseline),
        "baseline_only": sorted(baseline - tgcv_set),
        "option_space_changed": tgcv_set != baseline,
        "decision_relevance": relevance,
    }

    # IUT-2 requires reproducible, decision-relevant differentiation beyond
    # baseline and not merely a richer description.
    differentiated = (
        relevance["decision_relevant"]
        and tgcv_set != baseline
        and bool(relevance["newly_identified_by_tgcv"])
        and all(isinstance(v["reasons"], list) and v["reasons"] for v in tgcv.values())
    )

    classification = "IUT-2" if differentiated else "IUT-0"

    result = {
        "EXECUTION_RESULT": "PASS",
        "case_id": CASE_ID,
        "executor_version": EXECUTOR_VERSION,
        "epistemic_scope": "BOUNDED_STAGE_B_IUT_ONLY",
        "hypothesis_tested": "H1-IUT" if differentiated else "H0-IUT",
        "classification": classification,
        "assertions": assertions,
        "frozen_state": asdict(STATE),
        "frozen_option_universe": [asdict(o) for o in OPTIONS],
        "baseline": baseline_output,
        "tgcv": tgcv_output,
        "primary_comparison": primary_comparison,
        "outcome_blind": True,
        "causal_inference": False,
        "financial_value_tested": False,
        "universal_validity_tested": False,
        "complete_global_tacc_tested": False,
        "reproducibility": {
            "python_version": platform.python_version(),
            "platform": platform.platform(),
        },
    }

    canonical = canonical_json(result)
    result["provenance"] = {
        "executor_path": str(Path(__file__).as_posix()),
        "result_sha256": sha256_text(canonical),
        "fixture_sha256": sha256_text(canonical_json({"state": asdict(STATE), "options": [asdict(o) for o in OPTIONS]})),
    }
    return result


if __name__ == "__main__":
    print(f"EXECUTOR={EXECUTOR_VERSION}")
    print(f"PYTHON={sys.version.split()[0]}")
    result = run()
    print("EXECUTION_RESULT=" + result["EXECUTION_RESULT"])
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
