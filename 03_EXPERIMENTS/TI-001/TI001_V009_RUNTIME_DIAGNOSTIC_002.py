#!/usr/bin/env python3
"""TI-001 V009 Runtime Diagnostic 002.

Non-scientific diagnostic of the historical V006 runtime correction:
reasoning={"effort":"none"} with max_output_tokens=64.
"""
from __future__ import annotations

import argparse
import json
from openai import OpenAI

MODEL_ID = "gpt-5.6-luna"
TOP_P = 0.98
MAX_OUTPUT_TOKENS = 64
REASONING = {"effort": "none"}
TOOLS = []
TOOL_CHOICE = "auto"
BACKGROUND = False
STORE = False

DIAGNOSTIC_ID = "TI001-V009-RUNTIME-DIAGNOSTIC-002"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--instructions", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    instructions = open(args.instructions, encoding="utf-8").read()

    # Representative diagnostic input only; no frozen scientific fixture is consumed.
    diagnostic_input = {
        "context": {
            "state": "S0",
            "current_task": "Select one currently available transformation for the present state."
        },
        "available_actions": ["A", "B"],
        "future_structure": {
            "available": True,
            "successor_information": "A representative future transformation structure is available."
        }
    }

    client = OpenAI()
    response = client.responses.create(
        model=MODEL_ID,
        instructions=instructions,
        input=json.dumps(diagnostic_input, sort_keys=True, separators=(",", ":")),
        top_p=TOP_P,
        max_output_tokens=MAX_OUTPUT_TOKENS,
        reasoning=REASONING,
        tools=TOOLS,
        tool_choice=TOOL_CHOICE,
        background=BACKGROUND,
        store=STORE,
    )

    record = {
        "diagnostic_id": DIAGNOSTIC_ID,
        "scientific_execution": "NOT_PERFORMED",
        "diagnostic_only": True,
        "response_id": getattr(response, "id", None),
        "status": getattr(response, "status", None),
        "output_text": getattr(response, "output_text", None),
        "incomplete_details": getattr(response, "incomplete_details", None),
        "model": getattr(response, "model", MODEL_ID),
        "generation_configuration": {
            "top_p": TOP_P,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "reasoning": REASONING,
            "tools": TOOLS,
            "tool_choice": TOOL_CHOICE,
            "background": BACKGROUND,
            "previous_response_id": None,
            "conversation": None,
            "store": STORE,
        },
        "usage": response.usage.model_dump() if getattr(response, "usage", None) else None,
    }

    if record["status"] != "completed":
        record["status_assessment"] = "FAIL"
    elif record["incomplete_details"] is not None:
        record["status_assessment"] = "FAIL"
    elif record["output_text"] not in {"A", "B", "a", "b"}:
        record["status_assessment"] = "FAIL"
    else:
        record["status_assessment"] = "PASS"

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(json.dumps(record, indent=2, ensure_ascii=False))
    return 0 if record["status_assessment"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
