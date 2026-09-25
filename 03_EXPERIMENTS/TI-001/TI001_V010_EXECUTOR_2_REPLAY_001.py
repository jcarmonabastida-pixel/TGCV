#!/usr/bin/env python3
"""TI-001 V010 independent Executor-2 replay reconstruction.

This component is intentionally independent of Executor-1. It may consume
only the frozen fixture, replay contract, authorization and its own source.
It must not import or consume Executor-1 source or result.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

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
EXECUTOR_ID = "TI001-V010-EXECUTOR-2-REPLAY-001"


def load_fixture(path: Path):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != FIXTURE_SHA256:
        raise SystemExit("fixture SHA-256 mismatch")
    fixture = json.loads(raw)
    units = fixture.get("decision_units", [])
    if len(units) != 420:
        raise SystemExit("fixture must contain exactly 420 decision units")
    return units


def authorization_ok(auth):
    return (
        auth.get("scientific_execution") == "AUTHORIZED"
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--authorization", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    units = load_fixture(Path(args.fixture))
    authorization = json.loads(Path(args.authorization).read_text(encoding="utf-8"))

    if not authorization_ok(authorization):
        raise SystemExit("authorization does not match exact V010 replay binding")

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
            "store": False
        },
        "decision_count": len(units),
        "scientific_execution": "NOT_PERFORMED",
        "analysis_performed": False,
        "replay_implementation_ready": True
    }

    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
