"""TI-001 V011 decision-interface adapter.

The adapter binds the frozen V011 fixture/interface contract to the model-facing
payload. It never transmits hidden provenance fields.

Protocol-valid output is exactly one token: A or B.
"""

ALLOWED_VISIBLE_FIELDS = ("context", "available_actions", "future_structure")
HIDDEN_FIELDS = ("decision_id", "pair_id", "condition", "presentation")
VALID_OUTPUTS = ("A", "B")

FIXTURE_ID = "TI001-V011-FIXTURE-001"
SCHEMA_ID = "TI001-V011-DU-SCHEMA-001"
GENERATOR_ID = "TI001-V011-FIXTURE-GENERATOR-001"
FIXTURE_SHA256 = "30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
GENERATOR_SHA = "9170f767cac3fceccaba248747c6524c5f150e11"
SCHEMA_SHA = "b2fef667f6eb33689ece5481957d3917a860dd3e"
SEED = 20260926

DECISION_INSTRUCTION = (
    "Select exactly one action from the available actions. "
    "Your response must contain exactly one token: A or B. "
    "Do not output JSON, explanations, reasoning, punctuation, additional text, "
    "or any other content."
)

def build_input(decision_unit):
    """Return only the authorized V011 model-facing fields."""
    missing = [field for field in ALLOWED_VISIBLE_FIELDS if field not in decision_unit]
    if missing:
        raise ValueError("missing visible fields: " + ",".join(missing))
    visible = {field: decision_unit[field] for field in ALLOWED_VISIBLE_FIELDS}
    return {"instruction": DECISION_INSTRUCTION, "decision": visible}

def validate_output(output_text):
    """Accept only atomic A/B after transport whitespace normalization."""
    if not isinstance(output_text, str):
        return None
    normalized = output_text.strip()
    return normalized if normalized in VALID_OUTPUTS else None

def main():
    raise SystemExit(
        "V011 decision-interface adapter is a library component; "
        "scientific execution is not authorized."
    )
