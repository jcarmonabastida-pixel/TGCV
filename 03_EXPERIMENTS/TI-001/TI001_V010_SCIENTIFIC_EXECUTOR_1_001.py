#!/usr/bin/env python3
"""TI-001 V010 scientific Executor-1.

V010 changes the model-facing decision interface only. The frozen V008
scientific fixture and Transformational Intelligence object remain unchanged.

This runner is an execution component. It does not authorize execution,
perform analysis, retry, or recode invalid outputs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

from TI001_V010_DECISION_INTERFACE_001 import (
    build_input,
    validate_output,
)

EXECUTOR_ID = "TI001-V010-SCIENTIFIC-EXECUTOR-1-001"
FIXTURE_ID = "TI001-V008-FIXTURE-001"
FIXTURE_SHA256 = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
INTERFACE_ID = "TI001-V010-DECISION-INTERFACE-001"
INTERFACE_SHA256 = "e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c"
MODEL_ID = "gpt-5.6-luna"
API_SURFACE = "Responses API"
TOP_P = 0.98
MAX_OUTPUT_TOKENS = 64
REASONING = {"effort": "none"}
VALID_OUTPUTS = {"A", "B"}


def load_fixture(path: Path):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != FIXTURE_SHA256:
        raise SystemExit("fixture SHA-256 mismatch")
    return json.loads(raw)


def authorization_ok(auth):
    return (
        auth.get("scientific_execution") == "AUTHORIZED"
        and auth.get("executor_id") == EXECUTOR_ID
        and auth.get("fixture_id") == FIXTURE_ID
        and auth.get("fixture_sha256") == FIXTURE_SHA256
        and auth.get("interface_id") == INTERFACE_ID
        and auth.get("interface_sha256") == INTERFACE_SHA256
        and auth.get("model_id") == MODEL_ID
        and auth.get("api_surface") == API_SURFACE
        and auth.get("top_p") == TOP_P
        and auth.get("max_output_tokens") == MAX_OUTPUT_TOKENS
        and auth.get("reasoning") == REASONING
        and auth.get("temperature") is None
        and auth.get("tools") == []
        and auth.get("tool_choice") == "auto"
        and auth.get("background") is False
        and auth.get("previous_response_id") is None
        and auth.get("conversation") is None
        and auth.get("store") is False
    )


def dump_response(response):
    if hasattr(response, "model_dump"):
        return response.model_dump()
    if hasattr(response, "to_dict"):
        return response.to_dict()
    return {"repr": repr(response)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--authorization", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    fixture = load_fixture(Path(args.fixture))
    authorization = json.loads(
        Path(args.authorization).read_text(encoding="utf-8")
    )

    if not authorization_ok(authorization):
        raise SystemExit("authorization does not match exact V010 runner binding")

    units = fixture.get("decision_units", [])
    if len(units) != 420:
        raise SystemExit("fixture must contain exactly 420 decision units")

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required")

    client = OpenAI()
    records = []
    started = datetime.now(timezone.utc).isoformat()

    for unit in units:
        visible_input = build_input(unit)
        record = {
            "decision_id": unit["decision_id"],
            "pair_id": unit["pair_id"],
            "condition": unit["condition"],
            "presentation": unit["presentation"],
            "request": {
                "model": MODEL_ID,
                "api_surface": API_SURFACE,
                "temperature": None,
                "top_p": TOP_P,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
                "reasoning": REASONING,
                "tools": [],
                "tool_choice": "auto",
                "background": False,
                "previous_response_id": None,
                "conversation": None,
                "store": False,
                "input_visible_to_model": visible_input,
            },
        }

        try:
            response = client.responses.create(
                model=MODEL_ID,
                input=json.dumps(
                    visible_input,
                    ensure_ascii=False,
                    separators=(",", ":"),
                ),
                top_p=TOP_P,
                max_output_tokens=MAX_OUTPUT_TOKENS,
                reasoning=REASONING,
                tools=[],
                tool_choice="auto",
                background=False,
                store=False,
            )
            output_text = getattr(response, "output_text", "")
            selected = validate_output(output_text)
            record.update(
                {
                    "response_id": getattr(response, "id", None),
                    "response_status": getattr(response, "status", None),
                    "output_text": output_text,
                    "raw_response": dump_response(response),
                    "parsed_response": selected,
                    "validity": "VALID" if selected in VALID_OUTPUTS else "INVALID",
                }
            )
            if selected not in VALID_OUTPUTS:
                record["validation_error"] = "invalid model output"
        except Exception as exc:
            record.update(
                {
                    "response_id": None,
                    "response_status": None,
                    "output_text": None,
                    "parsed_response": None,
                    "validity": "RUNTIME_ERROR",
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                }
            )

        records.append(record)

    result = {
        "executor_id": EXECUTOR_ID,
        "fixture_id": FIXTURE_ID,
        "fixture_sha256": FIXTURE_SHA256,
        "interface_id": INTERFACE_ID,
        "interface_sha256": INTERFACE_SHA256,
        "model_id": MODEL_ID,
        "api_surface": API_SURFACE,
        "runtime": {
            "temperature": None,
            "top_p": TOP_P,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "reasoning": REASONING,
            "tools": [],
            "tool_choice": "auto",
            "background": False,
            "previous_response_id": None,
            "conversation": None,
            "store": False,
        },
        "started_at": started,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "decision_count": len(records),
        "scientific_execution": "PERFORMED",
        "analysis_performed": False,
        "records": records,
    }

    Path(args.output).write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
