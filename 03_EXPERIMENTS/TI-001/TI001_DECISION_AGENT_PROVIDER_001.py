#!/usr/bin/env python3
"""TI-001 Decision Agent Provider 001.

Generates the decision-provider evidence package by invoking the frozen
LLM decision mechanism once per fixture instance/condition.

This program is deliberately separate from the scientific execution harness.
It never reads successor state/accessibility or outcome/value information when
constructing the decision input.

No scientific API call is made unless --execute is explicitly supplied.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

MODEL_ID = "gpt-5.6-luna"
TEMPERATURE = 0.0
TOP_P = 0.98
MAX_OUTPUT_TOKENS = 16
TOOLS = []
TOOL_CHOICE = "auto"
BACKGROUND = False
STORE = False
PROVIDER_VERSION = "TI001_DECISION_AGENT_PROVIDER_001"

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def canonical_body_hash(fixture: dict) -> str:
    body = dict(fixture)
    body.pop("fixture_sha256", None)
    raw = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return sha256_bytes(raw)

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def decision_key(record: dict) -> str:
    return f"{record['pair_id']}::{record['condition']}"

def build_decision_input(record: dict) -> dict:
    # Only decision-time information is exposed. Identity, seeds, execution
    # slots, future alternatives, successors, outcomes, and estimands are excluded.
    info = {
        "state": record["S_t"],
        "currently_executable_transformations": list(record["available_transformations"]),
        "task": record["information_control"]["task"],
    }
    if record["condition"] == "treatment":
        info["future_transformation_space_information"] = record["information_treatment"]
    return info

def validate_output(text: str, allowed: list[str]) -> str:
    selected = text.strip()
    if selected not in allowed:
        raise ValueError(f"invalid model output: {selected!r}")
    return selected

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture")
    parser.add_argument("prompt")
    parser.add_argument("output")
    parser.add_argument("--execute", action="store_true",
                        help="perform the scientific decision calls")
    args = parser.parse_args(argv[1:])

    fixture_path = Path(args.fixture)
    prompt_path = Path(args.prompt)
    output_path = Path(args.output)

    fixture = load_json(fixture_path)
    prompt = load_text(prompt_path)
    expected_hash = fixture["fixture_sha256"]
    actual_hash = canonical_body_hash(fixture)
    if actual_hash != expected_hash:
        raise ValueError("fixture canonical body hash mismatch")

    prompt_hash = sha256_bytes(prompt.encode("utf-8"))
    if prompt_hash != "e451d2d89a353aa58030b3e59510837f5a664b186eb077662ae93376764f7006":
        raise ValueError("base prompt hash does not match frozen TI-001 prompt")

    if not args.execute:
        print(json.dumps({
            "status": "READY_NOT_EXECUTED",
            "provider_version": PROVIDER_VERSION,
            "fixture_sha256": expected_hash,
            "base_prompt_sha256": prompt_hash,
            "record_count": len(fixture["instances"]),
        }, indent=2, sort_keys=True))
        return 0

    client = OpenAI()
    decisions = {}

    for record in fixture["instances"]:
        key = decision_key(record)
        decision_input = build_decision_input(record)
        request_timestamp = datetime.now(timezone.utc).isoformat()

        response = client.responses.create(
            model=MODEL_ID,
            instructions=prompt,
            input=json.dumps(decision_input, sort_keys=True, separators=(",", ":"), ensure_ascii=False),
            temperature=TEMPERATURE,
            top_p=TOP_P,
            max_output_tokens=MAX_OUTPUT_TOKENS,
            tools=TOOLS,
            tool_choice=TOOL_CHOICE,
            background=BACKGROUND,
            store=STORE,
        )

        decision_timestamp = datetime.now(timezone.utc).isoformat()
        selected = validate_output(response.output_text, record["available_transformations"])

        usage = getattr(response, "usage", None)
        decisions[key] = {
            "pair_id": record["pair_id"],
            "instance_id": record["instance_id"],
            "condition": record["condition"],
            "selected_transformation": selected,
            "decision_timestamp": decision_timestamp,
            "request_timestamp": request_timestamp,
            "response_id": response.id,
            "response_status": response.status,
            "model_id": getattr(response, "model", MODEL_ID),
            "generation_configuration": {
                "temperature": TEMPERATURE,
                "top_p": TOP_P,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
                "tools": TOOLS,
                "tool_choice": TOOL_CHOICE,
                "background": BACKGROUND,
                "previous_response_id": None,
                "conversation": None,
                "reasoning": None,
                "store": STORE,
            },
            "usage": usage.model_dump() if usage is not None else None,
        }

    package = {
        "record_type": "TGCV_TI001_DECISION_AGENT_OUTPUT",
        "provider_version": PROVIDER_VERSION,
        "fixture_sha256": expected_hash,
        "base_prompt_sha256": prompt_hash,
        "model_id": MODEL_ID,
        "api_surface": "Responses API",
        "api_version": "not exposed by serving response",
        "model_version": "not exposed by serving response",
        "runtime_id": "not exposed by serving response",
        "runtime_version": "not exposed by serving response",
        "generation_configuration": {
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "tools": TOOLS,
            "tool_choice": TOOL_CHOICE,
            "background": BACKGROUND,
            "previous_response_id": None,
            "conversation": None,
            "reasoning": None,
            "store": STORE,
        },
        "local_environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "openai_sdk": importlib.metadata.version("openai"),
        },
        "decision_count": len(decisions),
        "decisions": decisions,
        "scientific_execution": "PERFORMED",
    }

    output_path.write_text(
        json.dumps(package, sort_keys=True, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "SCIENTIFIC_DECISIONS_WRITTEN",
        "output": str(output_path),
        "decision_count": len(decisions),
        "fixture_sha256": expected_hash,
    }, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
