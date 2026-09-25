#!/usr/bin/env python3
"""TI-001 V007 decision-agent provider.

Candidate runtime provider only. It binds the frozen V007 fixture to a bounded
A/B decision interface and never executes unless --execute is explicitly used.
No scientific execution is performed by preflight/import.
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
TOP_P = 0.98
MAX_OUTPUT_TOKENS = 64
REASONING = {"effort": "none"}
TOOLS = []
TOOL_CHOICE = "auto"
BACKGROUND = False
STORE = False
PROVIDER_VERSION = "TI001_DECISION_AGENT_PROVIDER_V007_001"
ALLOWED = {"A", "B"}
REQUIRED_CONDITIONS = {"control", "treatment", "null"}
EXPECTED_DECISIONS = 420


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_hash(obj: object) -> str:
    return sha256_bytes(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    )


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_fixture(fixture: dict) -> None:
    if fixture.get("fixture_id") != "TI001-v007-candidate-001":
        raise ValueError("unexpected V007 fixture_id")
    if fixture.get("version") != "v007-candidate-001":
        raise ValueError("unexpected V007 version")
    if fixture.get("status") not in {"CANDIDATE", "FROZEN"}:
        raise ValueError("V007 fixture is neither CANDIDATE nor FROZEN")
    if fixture.get("scientific_execution") != "NOT_AUTHORIZED":
        raise ValueError("fixture execution state changed unexpectedly")

    pairs = fixture.get("pairs", [])
    if len(pairs) != 210:
        raise ValueError("V007 fixture must contain exactly 210 pairs")

    counts = {c: 0 for c in REQUIRED_CONDITIONS}
    decision_count = 0
    for pair in pairs:
        condition = pair.get("condition")
        if condition not in REQUIRED_CONDITIONS:
            raise ValueError("invalid condition")
        counts[condition] += 1
        instances = pair.get("instances", [])
        if len(instances) != 2:
            raise ValueError("each pair must contain exactly I1 and I2")
        for inst in instances:
            decision_count += 1
            if set(inst.get("agent_view", {}).get("available_transformations", [])) != ALLOWED:
                raise ValueError("decision action space must be exactly A/B")
            if "condition" not in inst.get("agent_view", {}):
                pass
            if "pair_id" in inst.get("agent_view", {}) or "variant" in inst.get("agent_view", {}):
                raise ValueError("identity leakage in agent_view")
            if condition != "treatment" and "future_structure" in inst.get("agent_view", {}):
                raise ValueError("future structure leaked in non-treatment condition")
            if condition == "treatment" and "future_structure" not in inst.get("agent_view", {}):
                raise ValueError("treatment future structure missing")

    if counts != {"control": 70, "treatment": 70, "null": 70}:
        raise ValueError(f"condition balance mismatch: {counts}")
    if decision_count != EXPECTED_DECISIONS:
        raise ValueError("V007 fixture must contain exactly 420 decisions")


def validate_decision_units(units: list) -> None:
    if len(units) != EXPECTED_DECISIONS:
        raise ValueError("V007 requires exactly 420 decision units")
    for u in units:
        if not isinstance(u, dict):
            raise ValueError("decision unit must be an object")
        if u.get("condition") not in REQUIRED_CONDITIONS:
            raise ValueError("invalid condition in decision unit")
        if u.get("pair_id") is not None or u.get("variant") is not None:
            raise ValueError("decision unit must not expose identity to the provider input")


def build_decision_input(instance: dict) -> dict:
    view = instance["agent_view"]
    if any(k in view for k in ("condition", "pair_id", "variant")):
        raise ValueError("identity leakage in agent view")
    return {
        "state": view["state"],
        "available_transformations": list(view["available_transformations"]),
        "task": instance["task"],
        **({"future_structure": view["future_structure"]} if "future_structure" in view else {}),
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture")
    parser.add_argument("decision_units")
    parser.add_argument("prompt")
    parser.add_argument("output")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv[1:])

    fixture = load_json(Path(args.fixture))
    units_package = load_json(Path(args.decision_units))
    prompt = Path(args.prompt).read_text(encoding="utf-8")

    validate_fixture(fixture)
    validate_decision_units(units_package["decision_units"])

    fixture_hash = canonical_json_hash(fixture)
    prompt_hash = sha256_bytes(prompt.encode("utf-8"))

    if not args.execute:
        print(json.dumps({
            "status": "READY_NOT_EXECUTED",
            "provider_version": PROVIDER_VERSION,
            "fixture_sha256": fixture_hash,
            "base_prompt_sha256": prompt_hash,
            "decision_unit_count": len(units_package["decision_units"]),
            "reasoning": REASONING,
            "scientific_execution": "NOT_PERFORMED",
        }, indent=2, sort_keys=True))
        return 0

    client = OpenAI()
    decisions = {}

    for unit, instance in zip(units_package["decision_units"], units_package["instances"]):
        decision_input = build_decision_input(instance)
        input_hash = canonical_json_hash(decision_input)
        request_timestamp = datetime.now(timezone.utc).isoformat()

        response = client.responses.create(
            model=MODEL_ID,
            instructions=prompt,
            input=json.dumps(decision_input, sort_keys=True, separators=(",", ":"), ensure_ascii=False),
            top_p=TOP_P,
            max_output_tokens=MAX_OUTPUT_TOKENS,
            reasoning=REASONING,
            tools=TOOLS,
            tool_choice=TOOL_CHOICE,
            background=BACKGROUND,
            store=STORE,
        )

        selected = response.output_text.strip()
        if selected not in ALLOWED:
            raise ValueError(f"invalid model output: {selected!r}")

        key = unit["decision_id"]
        decisions[key] = {
            "decision_id": key,
            "selected_transformation": selected,
            "request_timestamp": request_timestamp,
            "decision_timestamp": datetime.now(timezone.utc).isoformat(),
            "response_id": response.id,
            "response_status": response.status,
            "model_id": getattr(response, "model", MODEL_ID),
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
            "decision_input_sha256": input_hash,
            "usage": response.usage.model_dump() if getattr(response, "usage", None) else None,
        }

    package = {
        "record_type": "TGCV_TI001_V007_DECISION_AGENT_OUTPUT",
        "provider_version": PROVIDER_VERSION,
        "fixture_sha256": fixture_hash,
        "base_prompt_sha256": prompt_hash,
        "model_id": MODEL_ID,
        "api_surface": "Responses API",
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
        "local_environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "openai_sdk": importlib.metadata.version("openai"),
        },
        "decision_count": len(decisions),
        "decisions": decisions,
        "scientific_execution": "PERFORMED",
    }

    Path(args.output).write_text(
        json.dumps(package, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "SCIENTIFIC_DECISIONS_WRITTEN",
        "decision_count": len(decisions),
        "fixture_sha256": fixture_hash,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
