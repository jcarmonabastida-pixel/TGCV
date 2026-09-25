#!/usr/bin/env python3
"""TI-001 V008 decision-agent provider boundary implementation."""

PROVIDER_ID = "TI001-V008-DECISION-AGENT-PROVIDER-001"
SCHEMA_ID = "TI001-V008-DU-SCHEMA-001"
SCHEMA_BLOB_SHA1 = "d9539790452b047bc845a19bdcf50b8713a42b2a"
ALLOWED_ACTIONS = ("A", "B")
HIDDEN_FIELDS = frozenset(("decision_id", "pair_id", "condition", "presentation"))
VISIBLE_FIELDS = frozenset(("context", "available_actions", "future_structure"))


def build_model_input(unit):
    if set(unit) != HIDDEN_FIELDS | VISIBLE_FIELDS:
        raise ValueError("V008 decision-unit field boundary mismatch")
    if unit["available_actions"] != ["A", "B"]:
        raise ValueError("V008 action space must be exactly A/B")
    context = unit["context"]
    if set(context) != {"items", "item_count"}:
        raise ValueError("V008 context schema mismatch")
    if context["item_count"] != len(context["items"]):
        raise ValueError("V008 context item_count mismatch")
    future = unit["future_structure"]
    if set(future) != {"successor_realized", "future_structure_available"}:
        raise ValueError("V008 future_structure schema mismatch")
    if future["successor_realized"]:
        raise ValueError("successor must not be realized before decision")
    return {
        "context": {
            "items": list(context["items"]),
            "item_count": context["item_count"],
        },
        "available_actions": ["A", "B"],
        "future_structure": {
            "successor_realized": False,
            "future_structure_available": bool(future["future_structure_available"]),
        },
    }


def validate_output(text):
    selected = text.strip()
    if selected not in ALLOWED_ACTIONS:
        raise ValueError("invalid model output")
    return selected


if __name__ == "__main__":
    raise SystemExit(
        "V008 provider implementation present; scientific execution requires its dedicated execution gate."
    )
