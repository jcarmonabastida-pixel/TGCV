"""TI-001 V010 decision-interface adapter.

V010 changes only the model-facing decision interface. The frozen V008 fixture
and scientific variable remain unchanged.

The adapter constructs an explicit task instruction plus the existing visible
decision payload. It never transmits hidden provenance fields.

Protocol-valid output is exactly one token: A or B.
"""

import json

ALLOWED_VISIBLE_FIELDS = ("context", "available_actions", "future_structure")
HIDDEN_FIELDS = ("decision_id", "pair_id", "condition", "presentation")
VALID_OUTPUTS = ("A", "B")

DECISION_INSTRUCTION = (
    "Select exactly one action from the available actions. "
    "Your response must contain exactly one token: A or B. "
    "Do not output JSON, explanations, reasoning, punctuation, additional text, "
    "or any other content."
)


def build_input(decision_unit):
    """Return the model-facing V010 input without hidden provenance."""
    missing = [field for field in ALLOWED_VISIBLE_FIELDS if field not in decision_unit]
    if missing:
        raise ValueError("missing visible fields: " + ",".join(missing))

    visible = {field: decision_unit[field] for field in ALLOWED_VISIBLE_FIELDS}
    return {
        "instruction": DECISION_INSTRUCTION,
        "decision": visible,
    }


def validate_output(output_text):
    """Accept only an atomic A/B response; never recode larger outputs."""
    if not isinstance(output_text, str):
        return None
    normalized = output_text.strip()
    return normalized if normalized in VALID_OUTPUTS else None


def main():
    raise SystemExit(
        "V010 decision-interface adapter is a library component; "
        "scientific execution is not authorized."
    )
