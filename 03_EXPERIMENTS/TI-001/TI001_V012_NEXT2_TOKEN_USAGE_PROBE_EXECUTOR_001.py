#!/usr/bin/env python3
"""
TI-001 V012 NEXT2 token-usage probe executor.

Purpose:
    Execute exactly one real NEXT2 cost-probe decision unit against the
    Responses API and persist the API-reported token decomposition.

This is a COST PROBE ONLY. It is not scientific execution and does not
generate or modify the NEXT2 scientific fixture.

Required environment:
    OPENAI_API_KEY

The executor reads the canonical probe input and system prompt from the
repository paths below. It verifies the system-prompt SHA-256 before making
the API request.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

try:
    from openai import OpenAI
except ImportError as exc:
    raise SystemExit("ERROR: install the OpenAI Python SDK before running the probe") from exc


REPO_ROOT = Path(__file__).resolve().parents[2]
TI001 = REPO_ROOT / "03_EXPERIMENTS" / "TI-001"

INPUT_PATH = TI001 / "TI001_V012_NEXT2_COST_PROBE_INPUT_001.json"
SYSTEM_PROMPT_PATH = TI001 / "TI001_V012_NEXT2_SYSTEM_PROMPT_001.txt"
OUTPUT_PATH = TI001 / "TI001_V012_NEXT2_TOKEN_USAGE_PROBE_RESULT_001.json"

EXPECTED_SYSTEM_PROMPT_SHA256 = (
    "660002f6506648fd0bfd703751f8996fae9fe0aaed3a48defbe78b2382c94122"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("ERROR: " + message)


def main() -> int:
    require(os.environ.get("OPENAI_API_KEY"), "OPENAI_API_KEY is not set")
    require(INPUT_PATH.is_file(), f"missing input: {INPUT_PATH}")
    require(SYSTEM_PROMPT_PATH.is_file(), f"missing system prompt: {SYSTEM_PROMPT_PATH}")

    system_prompt_sha256 = sha256_file(SYSTEM_PROMPT_PATH)
    require(
        system_prompt_sha256 == EXPECTED_SYSTEM_PROMPT_SHA256,
        "system prompt SHA-256 does not match the canonical binding",
    )

    with INPUT_PATH.open("r", encoding="utf-8") as handle:
        probe = json.load(handle)

    require(probe.get("status") == "COST_PROBE_ONLY", "input is not marked COST_PROBE_ONLY")
    require(probe.get("scientific_execution") is False, "probe input must not be scientific execution")
    require(probe.get("api_surface") == "Responses API", "unexpected API surface")
    require(probe.get("system_prompt_sha256") == system_prompt_sha256, "input/system-prompt hash mismatch")

    config = probe["generation_configuration"]
    unit = probe["decision_unit"]

    client = OpenAI()

    response = client.responses.create(
        model=probe["model_id"],
        instructions=SYSTEM_PROMPT_PATH.read_text(encoding="utf-8"),
        input=json.dumps(unit, ensure_ascii=False, separators=(",", ":")),
        max_output_tokens=config["max_output_tokens"],
        reasoning={"effort": config["reasoning_effort"]},
        store=config["store"],
        top_p=config["top_p"],
        tools=config["tools"],
    )

    usage = response.usage
    require(usage is not None, "API response did not contain usage")

    input_tokens = getattr(usage, "input_tokens", None)
    output_tokens = getattr(usage, "output_tokens", None)
    total_tokens = getattr(usage, "total_tokens", None)

    output_details = getattr(usage, "output_tokens_details", None)
    reasoning_tokens = getattr(output_details, "reasoning_tokens", None) if output_details else None

    input_details = getattr(usage, "input_tokens_details", None)
    cached_tokens = getattr(input_details, "cached_tokens", None) if input_details else None

    require(input_tokens is not None, "usage.input_tokens is missing")
    require(output_tokens is not None, "usage.output_tokens is missing")
    require(reasoning_tokens is not None, "usage.output_tokens_details.reasoning_tokens is missing")
    require(total_tokens is not None, "usage.total_tokens is missing")
    require(cached_tokens is not None, "usage.input_tokens_details.cached_tokens is missing")

    result = {
        "artifact_id": "TI001_V012_NEXT2_TOKEN_USAGE_PROBE_RESULT_001",
        "schema": "TI001_V012_NEXT2_TOKEN_USAGE_PROBE_RESULT_v001",
        "status": "TOKEN_USAGE_PROBE_COMPLETE",
        "scientific_execution": False,
        "source_input_artifact": probe["artifact_id"],
        "system_prompt_sha256": system_prompt_sha256,
        "instance_id": unit["instance_id"],
        "model_id": probe["model_id"],
        "api_surface": probe["api_surface"],
        "generation_configuration": config,
        "response_id": response.id,
        "usage": {
            "input_tokens": input_tokens,
            "input_tokens_details": {
                "cached_tokens": cached_tokens
            },
            "output_tokens": output_tokens,
            "output_tokens_details": {
                "reasoning_tokens": reasoning_tokens
            },
            "total_tokens": total_tokens
        },
        "accounting": {
            "reasoning_tokens_separate_from_visible_output": True,
            "input_plus_output_equals_total": (input_tokens + output_tokens == total_tokens),
            "output_tokens_include_reasoning_tokens": (reasoning_tokens <= output_tokens)
        }
    }

    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"RESULT_PATH={OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
