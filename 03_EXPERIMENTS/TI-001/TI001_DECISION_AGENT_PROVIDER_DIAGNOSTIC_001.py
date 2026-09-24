#!/usr/bin/env python3
"""Non-scientific diagnostic for a single TI-001 provider response.

This diagnostic does not use TI-001 fixture records and must not be used as
scientific evidence. It sends a minimal diagnostic prompt and prints the raw
serving-response structure needed to diagnose empty output_text.
"""

from __future__ import annotations

import json
from openai import OpenAI

MODEL_ID = "gpt-5.6-luna"

def main() -> int:
    client = OpenAI()
    response = client.responses.create(
        model=MODEL_ID,
        instructions="Return exactly one token: a",
        input="Diagnostic only. Return exactly one token: a",
        top_p=0.98,
        max_output_tokens=64,
        tools=[],
        tool_choice="auto",
        background=False,
        store=False,
    )

    print(json.dumps({
        "scientific_execution": "NOT_PERFORMED",
        "diagnostic_only": True,
        "response_id": getattr(response, "id", None),
        "status": getattr(response, "status", None),
        "output_text": getattr(response, "output_text", None),
        "incomplete_details": getattr(response, "incomplete_details", None),
        "output": getattr(response, "output", None),
        "usage": getattr(response, "usage", None),
        "model": getattr(response, "model", None),
    }, default=lambda x: x.model_dump() if hasattr(x, "model_dump") else str(x),
       indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
