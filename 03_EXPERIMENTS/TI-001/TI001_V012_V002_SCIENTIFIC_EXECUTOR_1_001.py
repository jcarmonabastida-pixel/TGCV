#!/usr/bin/env python3
"""TI-001 V012 V002 scientific Executor-1.

Canonical scientific executor for the frozen V002 package. No scientific
request is made unless --execute is explicitly supplied.
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
MAX_OUTPUT_TOKENS = 16
TOOLS = []
STORE = False
FIXTURE_SHA256 = "065ffa5f51fb69b5c9cca8f958bd424375b47b3e2e4e4b5cdb48f4259794a04d"
PROMPT_SHA256 = "162fe16e59a4a748e82381ce45dea67992c3e2568ea9ae064494d7b7bd8fa360"
VALIDATION_SHA256 = "44f31ddc1173f4b69d8302b97ed6dc96e4fd559c8865a86b5aaf921cefd43374"
ALLOWED = ("a", "b", "c")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_fixture_hash(fixture: dict) -> str:
    body = dict(fixture)
    body.pop("fixture_sha256", None)
    raw = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return sha256_bytes(raw)


def build_decision_input(record: dict) -> dict:
    info = {
        "current_task": record["information"]["current_task"],
        "available_transformations": list(record["available_transformations"]),
    }
    if record["condition"] != "NULL":
        rep = record["presentation_representation"]
        key = "p1_records" if record["presentation"] == "P1" else "p2_records"
        info["future_space_information"] = rep[key]
    return info


def classify_response(text: str) -> tuple[str, str | None]:
    raw = text.strip()
    if raw in ALLOWED:
        return "VALID", raw
    return "INVALID", None


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture")
    parser.add_argument("prompt")
    parser.add_argument("validation_procedure")
    parser.add_argument("output")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv[1:])

    fixture = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    validation = Path(args.validation_procedure).read_text(encoding="utf-8")

    actual_fixture_hash = canonical_fixture_hash(fixture)
    if actual_fixture_hash != FIXTURE_SHA256:
        raise ValueError("V002 fixture canonical hash mismatch")
    if sha256_bytes(prompt.encode("utf-8")) != PROMPT_SHA256:
        raise ValueError("V002 system prompt hash mismatch")
    if sha256_bytes(validation.encode("utf-8")) != VALIDATION_SHA256:
        raise ValueError("V002 response-validation procedure hash mismatch")
    if fixture.get("instance_count") != 72 or len(fixture.get("instances", [])) != 72:
        raise ValueError("V002 fixture instance count mismatch")

    if not args.execute:
        print(json.dumps({
            "status": "READY_NOT_EXECUTED",
            "executor_id": "TI001-V012-V002-SCIENTIFIC-EXECUTOR-1-001",
            "fixture_sha256": FIXTURE_SHA256,
            "prompt_sha256": PROMPT_SHA256,
            "validation_sha256": VALIDATION_SHA256,
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
            "condition": record["condition"],
            "presentation": record["presentation"],
            "request_timestamp": request_timestamp,
            "response_timestamp": response_timestamp,
            "response_id": response.id,
            "response_status": response.status,
            "raw_output_text": raw_text,
            "parsed_action": parsed,
            "validity": validity,
            "generation_configuration": {
                "top_p": TOP_P,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
                "tools": TOOLS,
                "previous_response_id": None,
                "conversation": None,
                "store": STORE,
            },
            "model_id": getattr(response, "model", MODEL_ID),
            "usage": usage.model_dump() if usage is not None else None,
        })

    package = {
        "record_type": "TGCV_TI001_V012_V002_SCIENTIFIC_EXECUTION_RESULT",
        "executor_id": "TI001-V012-V002-SCIENTIFIC-EXECUTOR-1-001",
        "fixture_sha256": FIXTURE_SHA256,
        "system_prompt_sha256": PROMPT_SHA256,
        "validation_procedure_sha256": VALIDATION_SHA256,
        "model_id": MODEL_ID,
        "api_surface": "Responses API",
        "generation_configuration": {
            "top_p": TOP_P,
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
