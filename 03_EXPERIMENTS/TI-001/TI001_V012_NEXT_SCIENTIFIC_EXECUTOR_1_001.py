#!/usr/bin/env python3
"""TI-001 V012 NEXT scientific Executor-1.

Explicitly bound to the frozen NEXT_v001 fixture.
No scientific request is made unless --execute is explicitly supplied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

MODEL_ID = "gpt-5.6-luna"
TOP_P = 0.98
REASONING_EFFORT = "low"
MAX_OUTPUT_TOKENS = 128
TOOLS = []
STORE = False

FIXTURE_SHA256 = "7782e7652001ec8a64cd1f231c37e6c3c7cd065e672564140fdfa4626b185a5b"
FIXTURE_GIT_BLOB_SHA = "1886160849aecdbda2904a0d3b593975077e1914"
FIXTURE_SCHEMA = "TI001_V012_NEXT_FIXTURE_v001"
FIXTURE_VERSION = "NEXT_v001"
FIXTURE_SEED = 582031
PROMPT_SHA256 = "80d8f1555ce8d616f7609c2ff82d117189072caea3ad2a67d32fc54303484e04"
VALIDATION_SHA256 = "4e45c3ffb958425b1e2d72e22b41306f5d4ea6f3f3a9c22561c3739b9758856d"
ALLOWED = ("A", "B")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fixture_file_hash(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def build_decision_input(record: dict) -> dict:
    return {
        "current_state": record["state"],
        "current_task": record["task"],
        "available_actions": list(record["available_actions"]),
        "presentation": record["presentation"],
        "mapping_condition": record["mapping_condition"],
        "future_space_information": record["information"]["future_space_mapping"],
        "informative_correspondence_defined": record["information"]["informative_correspondence_defined"],
    }


def classify_response(text: str) -> tuple[str, str | None]:
    raw = text.strip()
    if raw in ALLOWED:
        return "VALID", raw
    return "INVALID", None


def usage_details(usage):
    if usage is None:
        return None
    data = usage.model_dump()
    details = data.get("output_tokens_details") or {}
    return {
        "input_tokens": data.get("input_tokens"),
        "output_tokens": data.get("output_tokens"),
        "reasoning_tokens": details.get("reasoning_tokens"),
        "total_tokens": data.get("total_tokens"),
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture")
    parser.add_argument("prompt")
    parser.add_argument("validation_procedure")
    parser.add_argument("output")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv[1:])

    fixture_path = Path(args.fixture)
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    validation = Path(args.validation_procedure).read_text(encoding="utf-8")

    if fixture_file_hash(fixture_path) != FIXTURE_SHA256:
        raise ValueError("NEXT fixture SHA-256 mismatch")
    if sha256_bytes(prompt.encode("utf-8")) != PROMPT_SHA256:
        raise ValueError("NEXT system prompt SHA-256 mismatch")
    if sha256_bytes(validation.encode("utf-8")) != VALIDATION_SHA256:
        raise ValueError("NEXT response-validation SHA-256 mismatch")
    if fixture.get("schema") != FIXTURE_SCHEMA:
        raise ValueError("NEXT fixture schema mismatch")
    if fixture.get("fixture_version") != FIXTURE_VERSION:
        raise ValueError("NEXT fixture version mismatch")
    if fixture.get("randomisation_seed") != FIXTURE_SEED:
        raise ValueError("NEXT fixture seed mismatch")
    if fixture.get("instance_count") != 72 or len(fixture.get("instances", [])) != 72:
        raise ValueError("NEXT fixture instance count mismatch")
    if fixture.get("scientific_execution") is not False:
        raise ValueError("NEXT fixture execution flag mismatch")

    executor_id = "TI001-V012-NEXT-SCIENTIFIC-EXECUTOR-1-001"

    if not args.execute:
        print(json.dumps({
            "status": "READY_NOT_EXECUTED",
            "executor_id": executor_id,
            "fixture_sha256": FIXTURE_SHA256,
            "fixture_git_blob_sha": FIXTURE_GIT_BLOB_SHA,
            "fixture_schema": FIXTURE_SCHEMA,
            "fixture_version": FIXTURE_VERSION,
            "prompt_sha256": PROMPT_SHA256,
            "validation_sha256": VALIDATION_SHA256,
            "model_id": MODEL_ID,
            "api_surface": "Responses API",
            "reasoning_effort": REASONING_EFFORT,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "instance_count": 72,
            "scientific_execution": False,
        }, indent=2, sort_keys=True))
        return 0

    client = OpenAI()
    decisions = []

    for record in fixture["instances"]:
        request_timestamp = datetime.now(timezone.utc).isoformat()
        decision_input = build_decision_input(record)
        response = client.responses.create(
            model=MODEL_ID,
            instructions=prompt,
            input=json.dumps(
                decision_input, sort_keys=True, separators=(",", ":"),
                ensure_ascii=False
            ),
            top_p=TOP_P,
            reasoning={"effort": REASONING_EFFORT},
            max_output_tokens=MAX_OUTPUT_TOKENS,
            tools=TOOLS,
            store=STORE,
        )
        response_timestamp = datetime.now(timezone.utc).isoformat()
        raw_text = response.output_text
        validity, parsed = classify_response(raw_text)
        usage = getattr(response, "usage", None)

        decisions.append({
            "instance_id": record["instance_id"],
            "operationalisation": record["operationalisation"],
            "mapping_condition": record["mapping_condition"],
            "informative_action": record["informative_action"],
            "presentation": record["presentation"],
            "request_timestamp": request_timestamp,
            "response_timestamp": response_timestamp,
            "response_id": response.id,
            "response_status": response.status,
            "incomplete_details": getattr(response, "incomplete_details", None),
            "raw_output_text": raw_text,
            "parsed_action": parsed,
            "validity": validity,
            "generation_configuration": {
                "top_p": TOP_P,
                "reasoning_effort": REASONING_EFFORT,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
                "tools": TOOLS,
                "previous_response_id": None,
                "conversation": None,
                "store": STORE,
            },
            "model_id": getattr(response, "model", MODEL_ID),
            "usage": usage_details(usage),
        })

    package = {
        "record_type": "TGCV_TI001_V012_NEXT_SCIENTIFIC_EXECUTION_RESULT",
        "executor_id": executor_id,
        "fixture_sha256": FIXTURE_SHA256,
        "fixture_git_blob_sha": FIXTURE_GIT_BLOB_SHA,
        "fixture_schema": FIXTURE_SCHEMA,
        "fixture_version": FIXTURE_VERSION,
        "system_prompt_sha256": PROMPT_SHA256,
        "validation_procedure_sha256": VALIDATION_SHA256,
        "model_id": MODEL_ID,
        "api_surface": "Responses API",
        "generation_configuration": {
            "top_p": TOP_P,
            "reasoning_effort": REASONING_EFFORT,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "tools": TOOLS,
            "previous_response_id": None,
            "conversation": None,
            "store": STORE,
        },
        "execution_environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "decision_count": len(decisions),
        "decisions": decisions,
        "scientific_execution": True,
        "retry": False,
        "recoding": False,
        "substitution": False,
    }
    Path(args.output).write_text(
        json.dumps(package, sort_keys=True, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "SCIENTIFIC_EXECUTION_COMPLETE",
        "decision_count": len(decisions),
        "fixture_sha256": FIXTURE_SHA256,
        "scientific_execution": True,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv))
