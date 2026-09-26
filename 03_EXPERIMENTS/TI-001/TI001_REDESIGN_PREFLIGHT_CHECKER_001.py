#!/usr/bin/env python3
"""
TGCV TI-001 redesign preflight checker 001.

Design-only checker. It validates a candidate specification/fixture against
R1-R14. It does not generate fixtures and never performs scientific execution.

Critical constraints:
- R8 is structural: neutral descriptor fields are allowlisted; lexical scan
  is diagnostic only and can NEVER establish R8 or overall preflight PASS.
- D6/R11 require a treatment-induced divergence witness, not arbitrary
  differing decision functions.
- v004 is outside this checker and must remain unchanged.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


ACTIONS = ("a", "b", "c")

# R8: only neutral, structural future-space descriptors are admissible.
# Values are deliberately restricted to categorical structural descriptors.
# Explicit governance marker: lexical scanning is auxiliary diagnostic data,
# never an R8 criterion and never an input to overall_preflight_pass.
LEXICAL_DIAGNOSTIC_ONLY = True

ALLOWED_DESCRIPTOR_FIELDS = frozenset({
    "future_accessibility_class",
    "identity_turnover_class",
    "persistence_class",
    "reconfiguration_class",
})

PROHIBITED_SEMANTIC_TOKENS = frozenset({
    "best", "preferred", "recommend", "recommended", "optimal", "choose",
    "avoid", "reward", "value", "utility", "performance", "outcome",
    "success", "failure", "score", "rank", "ranking",
})

REQUIRED_OUTPUT_KEYS = (
    "state_identity_pass",
    "current_tacc_identity_pass",
    "action_identity_pass",
    "temporal_separation_pass",
    "action_conditioned_mapping_complete",
    "future_descriptor_distinction_pass",
    "control_non_derivability_pass",
    "recommendation_schema_pass",
    "recommendation_lexical_diagnostic",
    "prohibited_information_absent",
    "choice_multiplicity_pass",
    "divergence_opportunity_pass",
    "null_validity_pass",
    "future_reveal_blocked",
    "traceability_pass",
    "overall_preflight_pass",
)


def _fail(reason: str) -> Tuple[bool, str]:
    return False, reason


def _pass(reason: str = "PASS") -> Tuple[bool, str]:
    return True, reason


def _same(x: Any, y: Any) -> bool:
    return x == y


def _descriptor_is_structurally_neutral(
    descriptor: Mapping[str, Any],
) -> Tuple[bool, str]:
    if not isinstance(descriptor, Mapping) or not descriptor:
        return _fail("descriptor must be a non-empty object")

    unknown = set(descriptor) - ALLOWED_DESCRIPTOR_FIELDS
    if unknown:
        return _fail(
            "descriptor contains non-allowlisted fields: "
            + ",".join(sorted(unknown))
        )

    if not set(descriptor) & ALLOWED_DESCRIPTOR_FIELDS:
        return _fail("descriptor has no allowlisted neutral structural field")

    for key, value in descriptor.items():
        if not isinstance(value, str):
            return _fail("descriptor field values must be categorical strings")
        lowered = value.lower()
        if any(token in lowered for token in PROHIBITED_SEMANTIC_TOKENS):
            return _fail(
                "descriptor field contains prohibited semantic token: "
                + key
            )

    return _pass()


def _lexical_diagnostic(value: Any) -> bool:
    """Auxiliary diagnostic only; NEVER establishes R8 or overall PASS."""
    blob = json.dumps(value, ensure_ascii=False, sort_keys=True).lower()
    return not any(re.search(r"\b" + re.escape(t) + r"\b", blob)
                   for t in PROHIBITED_SEMANTIC_TOKENS)


def _get_conditions(fixture: Mapping[str, Any]) -> Mapping[str, Any]:
    conditions = fixture.get("conditions")
    if not isinstance(conditions, Mapping):
        raise ValueError("fixture.conditions must be an object")
    return conditions


def check_r1_state_identity(conditions: Mapping[str, Any]) -> Tuple[bool, str]:
    states = [conditions[name].get("state") for name in ("control", "treatment", "null")]
    return (_pass() if all(_same(s, "S0") for s in states)
            else _fail("not all conditions have state S0"))


def check_r2_tacc_identity(conditions: Mapping[str, Any]) -> Tuple[bool, str]:
    expected = list(ACTIONS)
    values = [conditions[name].get("t_acc") for name in ("control", "treatment", "null")]
    return (_pass() if all(v == expected for v in values)
            else _fail("not all conditions expose T_acc=[a,b,c]"))


def check_r3_action_identity(conditions: Mapping[str, Any]) -> Tuple[bool, str]:
    values = [conditions[name].get("actions") for name in ("control", "treatment", "null")]
    return (_pass() if all(v == list(ACTIONS) for v in values)
            else _fail("action identity mismatch"))


def check_r4_temporal_separation(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    order = fixture.get("temporal_order")
    expected = [
        "information_presentation",
        "transformation_selection",
        "successor_realisation",
        "future_accessibility_reveal",
    ]
    return (_pass() if order == expected
            else _fail("temporal order does not match required sequence"))


def check_r5_mapping(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    mapping = fixture.get("conditions", {}).get("treatment", {}).get(
        "future_mapping"
    )
    if not isinstance(mapping, Mapping) or set(mapping) != set(ACTIONS):
        return _fail("treatment future_mapping is not exactly keyed by a,b,c")
    for action in ACTIONS:
        ok, reason = _descriptor_is_structurally_neutral(mapping[action])
        if not ok:
            return _fail("F(%s): %s" % (action, reason))
    return _pass()


def check_r6_distinction(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    mapping = fixture["conditions"]["treatment"]["future_mapping"]
    descriptors = [json.dumps(mapping[a], sort_keys=True) for a in ACTIONS]
    return (_pass() if len(set(descriptors)) >= 2
            else _fail("all future descriptors are identical"))


def check_r7_control_non_derivability(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    control = fixture["conditions"]["control"]
    mapping = fixture["conditions"]["treatment"]["future_mapping"]
    trace = fixture.get("transition_traceability")
    if "future_mapping" in control:
        return _fail("control explicitly contains future_mapping")
    if control.get("derivable_future_mapping") is True:
        return _fail("control declares future mapping derivable")
    if control.get("future_signal") is not None:
        return _fail("control contains future-space signal")
    if control.get("mapping_non_derivable") is not True:
        return _fail("missing explicit control non-derivability attestation")
    if not isinstance(trace, Mapping):
        return _fail("missing transition_traceability for non-derivability test")
    if set(mapping) != set(ACTIONS) or set(trace) != set(ACTIONS):
        return _fail("complete action-keyed treatment mapping/trace required")
    if any(k in control for k in ("future_descriptors", "action_future_mapping")):
        return _fail("control contains an action-keyed future descriptor field")
    return _pass("PASS: control payload excludes the treatment-only action-keyed future mapping")

def check_r8_schema(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    mapping = fixture["conditions"]["treatment"]["future_mapping"]
    for action in ACTIONS:
        ok, reason = _descriptor_is_structurally_neutral(mapping[action])
        if not ok:
            return _fail("R8 schema failure at %s: %s" % (action, reason))
    return _pass()


def check_r9_prohibited_absence(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    # Structural field prohibition across the condition payload.
    blob = json.dumps(fixture, ensure_ascii=False, sort_keys=True).lower()
    prohibited_patterns = (
        r'"(?:reward|value|utility|performance|outcome|score|ranking)"\s*:',
    )
    for pattern in prohibited_patterns:
        if re.search(pattern, blob):
            return _fail("prohibited evaluative field present")
    return _pass()


def check_r10_choice_multiplicity(conditions: Mapping[str, Any]) -> Tuple[bool, str]:
    treatment = conditions["treatment"]
    admissible = treatment.get("admissible_actions", list(ACTIONS))
    return (_pass() if len(set(admissible)) >= 2 and set(admissible) <= set(ACTIONS)
            else _fail("fewer than two admissible actions remain"))


def check_r11_d6_witness(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    witness = fixture.get("divergence_witness")
    if not isinstance(witness, Mapping):
        return _fail("missing divergence_witness")
    required = {
        "control_action", "treatment_action", "different",
        "depends_on_treatment_mapping", "same_state", "same_t_acc",
        "same_task", "same_timing", "same_decision_rule", "no_evaluation",
        "removing_mapping_removes_witness", "mapping_action_used",
        "mapping_descriptor_used", "control_without_mapping_action",
        "treatment_with_mapping_action", "mapping_removed_action",
    }
    missing = required - set(witness)
    if missing:
        return _fail("D6 witness missing fields: " + ",".join(sorted(missing)))
    if witness["different"] is not True:
        return _fail("D6 witness does not demonstrate different actions")
    if witness["control_action"] == witness["treatment_action"]:
        return _fail("D6 witness actions are identical")
    for key in (
        "depends_on_treatment_mapping", "same_state", "same_t_acc",
        "same_task", "same_timing", "same_decision_rule",
        "no_evaluation", "removing_mapping_removes_witness",
    ):
        if witness[key] is not True:
            return _fail("D6 witness condition false: " + key)
    mapping = fixture["conditions"]["treatment"]["future_mapping"]
    action_used = witness["mapping_action_used"]
    if action_used not in ACTIONS:
        return _fail("D6 mapping_action_used is not a current action")
    if witness["mapping_descriptor_used"] != mapping[action_used]:
        return _fail("D6 witness descriptor does not match the treatment mapping")
    if witness["control_without_mapping_action"] != witness["control_action"]:
        return _fail("D6 control action is not the stated no-mapping baseline")
    if witness["treatment_with_mapping_action"] != witness["treatment_action"]:
        return _fail("D6 treatment action is not the stated mapping-dependent action")
    if witness["mapping_removed_action"] != witness["control_action"]:
        return _fail("D6 removing the mapping does not restore the control action")
    if witness["mapping_removed_action"] == witness["treatment_action"]:
        return _fail("D6 witness remains divergent after mapping removal")
    return _pass("PASS: explicit treatment-mapping-dependent divergence witness")

def check_r12_null(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    null = fixture["conditions"]["null"]
    if null.get("future_mapping") is not None:
        return _fail("null contains future_mapping")
    if null.get("future_signal") is not None:
        return _fail("null contains future-space signal")
    if null.get("recommendation") is not None:
        return _fail("null contains recommendation")
    return (_pass() if null.get("format_compatible") is True
            else _fail("null format compatibility not attested"))


def check_r13_future_reveal(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    if fixture.get("successor_state_before_selection") is True:
        return _fail("successor state exposed before selection")
    if fixture.get("successor_accessibility_before_selection") is True:
        return _fail("successor accessibility exposed before selection")
    return _pass()


def check_r14_traceability(fixture: Mapping[str, Any]) -> Tuple[bool, str]:
    mapping = fixture["conditions"]["treatment"]["future_mapping"]
    trace = fixture.get("transition_traceability")
    if not isinstance(trace, Mapping):
        return _fail("missing transition_traceability")
    if set(trace) != set(ACTIONS):
        return _fail("transition_traceability must be exactly keyed by a,b,c")
    for action in ACTIONS:
        if action not in mapping:
            return _fail("missing treatment mapping for " + action)
        entry = trace[action]
        if not isinstance(entry, Mapping):
            return _fail("traceability entry is not an object for " + action)
        if entry.get("action") != action:
            return _fail("traceability action key mismatch for " + action)
        if entry.get("future_descriptor") != mapping[action]:
            return _fail("traceability descriptor mismatch for " + action)
        if not isinstance(entry.get("source_successor"), str):
            return _fail("missing source_successor for " + action)
        if not isinstance(entry.get("source_future_accessibility"), list):
            return _fail("missing source_future_accessibility for " + action)
    return _pass("PASS: each F(u) is linked to its explicit action and transition source")

def run_preflight(fixture: Mapping[str, Any]) -> Dict[str, Any]:
    conditions = _get_conditions(fixture)
    results: Dict[str, Tuple[bool, str]] = {}

    results["state_identity_pass"] = check_r1_state_identity(conditions)
    results["current_tacc_identity_pass"] = check_r2_tacc_identity(conditions)
    results["action_identity_pass"] = check_r3_action_identity(conditions)
    results["temporal_separation_pass"] = check_r4_temporal_separation(fixture)
    results["action_conditioned_mapping_complete"] = check_r5_mapping(fixture)
    results["future_descriptor_distinction_pass"] = check_r6_distinction(fixture)
    results["control_non_derivability_pass"] = check_r7_control_non_derivability(fixture)
    results["recommendation_schema_pass"] = check_r8_schema(fixture)
    results["recommendation_lexical_diagnostic"] = (
        _lexical_diagnostic(fixture["conditions"]["treatment"])
    )
    results["prohibited_information_absent"] = check_r9_prohibited_absence(fixture)
    results["choice_multiplicity_pass"] = check_r10_choice_multiplicity(conditions)
    results["divergence_opportunity_pass"] = check_r11_d6_witness(fixture)
    results["null_validity_pass"] = check_r12_null(fixture)
    results["future_reveal_blocked"] = check_r13_future_reveal(fixture)
    results["traceability_pass"] = check_r14_traceability(fixture)

    output = {
        key: value[0] if isinstance(value, tuple) else value
        for key, value in results.items()
    }
    reasons = {
        key: value[1] for key, value in results.items()
        if isinstance(value, tuple) and not value[0]
    }
    output["reasons"] = reasons
    output["overall_preflight_pass"] = (
        all(output[key] for key in REQUIRED_OUTPUT_KEYS if key != "overall_preflight_pass")
    )
    return output


def main(argv: Sequence[str]) -> int:
    if len(argv) != 2:
        print("usage: TI001_REDESIGN_PREFLIGHT_CHECKER_001.py <candidate.json>")
        return 2

    with open(argv[1], "r", encoding="utf-8") as handle:
        fixture = json.load(handle)

    result = run_preflight(fixture)
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if result["overall_preflight_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
