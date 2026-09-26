#!/usr/bin/env python3
"""TI-001 V012 V003 scientific Executor-1.

Instrumentation-amended executor. No scientific request is made unless
--execute is explicitly supplied.
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
FIXTURE_SHA256 = "065ffa5f51fb69b5c9cca8f958bd424375b47b3e2e4e4b5cdb48f4259794a04d"
PROMPT_SHA256 = "7c5453f19d87c3f6737eca2d35fac27c784beef6cde66be352f1cf354359384b"
VALIDATION_SHA256 = "14934b507a774b9b354ed2005d5903790dfcabafa40486c72467336393daec53"
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

    fixture = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    validation = Path(args.validation_procedure).read_text(encoding="utf-8")

    actual_fixture_hash = canonical_fixture_hash(fixture)
    if actual_fixture_hash != FIXTURE_SHA256:
        raise ValueError("V003 fixture canonical hash mismatch")
    if sha256_bytes(prompt.encode("utf-8")) != PROMPT_SHA256:
        raise ValueError("V003 system prompt hash mismatch")
    if sha256_bytes(validation.encode("utf-8")) != VALIDATION_SHA256:
        raise ValueError("V003 response-validation procedure hash mismatch")
    if fixture.get("instance_count") != 72 or len(fixture.get("instances", [])) != 72:
        raise ValueError("V003 fixture instance count mismatch")

    if not args.execute:
        print(json.dumps({
            "status": "READY_NOT_EXECUTED",
            "executor_id": "TI001-V012-V003-SCIENTIFIC-EXECUTOR-1-001",
            "fixture_sha256": FIXTURE_SHA256,
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
            "condition": record["condition"],
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
        "record_type": "TGCV_TI001_V012_V003_SCIENTIFIC_EXECUTION_RESULT",
        "executor_id": "TI001-V012-V003-SCIENTIFIC-EXECUTOR-1-001",
        "fixture_sha256": FIXTURE_SHA256,
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
