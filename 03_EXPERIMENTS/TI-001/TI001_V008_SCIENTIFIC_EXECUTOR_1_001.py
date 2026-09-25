#!/usr/bin/env python3
"""TI-001 V008 Executor-1 scientific runner.

This runner performs scientific execution only when a separate authorization
record explicitly authorizes the exact executor and bindings. It never retries
or recodes an invalid response and performs no scientific analysis.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

PROVIDER_ID = "TI001-V008-DECISION-AGENT-PROVIDER-001"
PROVIDER_BLOB_SHA1 = "c7d066de3481143d878f06bb2c1d791cb7dc54e1"
FIXTURE_ID = "TI001-V008-FIXTURE-001"
FIXTURE_SHA256 = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
SCHEMA_ID = "TI001-V008-DU-SCHEMA-001"
MODEL_ID = "gpt-5.6-luna"
API_SURFACE = "Responses API"
EXECUTOR_ID = "TI001-V008-SCIENTIFIC-EXECUTOR-1-001"
TOP_P = 0.98
MAX_OUTPUT_TOKENS = 16
VALID_OUTPUTS = {"A", "B"}

def load_fixture(path: Path):
    raw = path.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != FIXTURE_SHA256:
        raise SystemExit(f"fixture SHA-256 mismatch: {actual}")
    return json.loads(raw)

def model_input(unit):
    if set(unit) != {
        "decision_id", "pair_id", "condition", "presentation",
        "context", "available_actions", "future_structure"
    }:
        raise ValueError("V008 decision-unit schema mismatch")
    if unit["available_actions"] != ["A", "B"]:
        raise ValueError("V008 action space must be exactly A/B")
    if unit["future_structure"]["successor_realized"] is not False:
        raise ValueError("successor must not be realized before decision")
    return {
        "context": unit["context"],
        "available_actions": ["A", "B"],
        "future_structure": {
            "successor_realized": False,
            "future_structure_available":
                bool(unit["future_structure"]["future_structure_available"]),
        },
    }

def authorization_ok(record):
    return (
        record.get("scientific_execution") == "AUTHORIZED"
        and record.get("executor_id") == EXECUTOR_ID
        and record.get("fixture_id") == FIXTURE_ID
        and record.get("fixture_sha256") == FIXTURE_SHA256
        and record.get("provider_id") == PROVIDER_ID
        and record.get("provider_blob_sha1") == PROVIDER_BLOB_SHA1
        and record.get("model_id") == MODEL_ID
        and record.get("api_surface") == API_SURFACE
        and record.get("top_p") == TOP_P
        and record.get("max_output_tokens") == MAX_OUTPUT_TOKENS
        and record.get("temperature") is None
        and record.get("tools") == []
        and record.get("conversation") is None
        and record.get("previous_response_id") is None
        and record.get("store") is False
    )

def response_dump(response):
    if hasattr(response, "model_dump"):
        return response.model_dump()
    if hasattr(response, "to_dict"):
        return response.to_dict()
    return {"repr": repr(response)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", required=True)
    ap.add_argument("--authorization", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    fixture = load_fixture(Path(args.fixture))
    auth = json.loads(Path(args.authorization).read_text(encoding="utf-8"))

    if not authorization_ok(auth):
        raise SystemExit("authorization record does not match exact V008 scientific runner binding")

    units = fixture.get("decision_units", [])
    if len(units) != 420:
        raise SystemExit("fixture must contain exactly 420 decision units")

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required for scientific execution")

    client = OpenAI()
    started = datetime.now(timezone.utc).isoformat()
    records = []

    for unit in units:
        visible = model_input(unit)
        request_payload = json.dumps(
            visible, ensure_ascii=False, separators=(",", ":")
        )

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
                "tools": [],
                "tool_choice": "auto",
                "background": False,
                "previous_response_id": None,
                "conversation": None,
                "reasoning": None,
                "store": False,
                "input_visible_to_model": visible,
            },
        }

        try:
            response = client.responses.create(
                model=MODEL_ID,
                input=request_payload,
                top_p=TOP_P,
                max_output_tokens=MAX_OUTPUT_TOKENS,
                tools=[],
                tool_choice="auto",
                background=False,
                store=False,
            )
            raw = response_dump(response)
            text = getattr(response, "output_text", "")
            record["response_id"] = getattr(response, "id", None)
            record["response_status"] = getattr(response, "status", None)
            record["output_text"] = text
            record["raw_response"] = raw
            try:
                selected = text.strip()
                if selected not in VALID_OUTPUTS:
                    raise ValueError("invalid model output")
                record["parsed_response"] = selected
                record["validity"] = "VALID"
            except ValueError as exc:
                record["parsed_response"] = None
                record["validity"] = "INVALID"
                record["validation_error"] = str(exc)
        except Exception as exc:
            record["response_id"] = None
            record["response_status"] = None
            record["output_text"] = None
            record["parsed_response"] = None
            record["validity"] = "RUNTIME_ERROR"
            record["error_type"] = type(exc).__name__
            record["error_message"] = str(exc)

        records.append(record)

    result = {
        "executor_id": EXECUTOR_ID,
        "fixture_id": FIXTURE_ID,
        "fixture_sha256": FIXTURE_SHA256,
        "schema_id": SCHEMA_ID,
        "provider_id": PROVIDER_ID,
        "provider_blob_sha1": PROVIDER_BLOB_SHA1,
        "model_id": MODEL_ID,
        "api_surface": API_SURFACE,
        "runtime": {
            "temperature": None,
            "top_p": TOP_P,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "tools": [],
            "tool_choice": "auto",
            "background": False,
            "previous_response_id": None,
            "conversation": None,
            "reasoning": None,
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
