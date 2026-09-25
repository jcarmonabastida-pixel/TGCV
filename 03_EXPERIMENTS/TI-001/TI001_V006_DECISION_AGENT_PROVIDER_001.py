#!/usr/bin/env python3
"""TI-001 V006 decision-agent provider.

Runtime-only correction of V005: the Responses API request explicitly sends
reasoning={"effort":"none"}. Scientific design, fixture, prompt, estimand,
decision units, and isolation boundary are unchanged.
"""
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json, platform, sys
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
PROVIDER_VERSION = "TI001_DECISION_AGENT_PROVIDER_V006_001"
ALLOWED = {"a", "b", "c"}
REQUIRED_CONDITIONS = {"control", "treatment", "null"}

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def canonical_json_hash(obj: dict) -> str:
    return sha256_bytes(json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def validate_fixture(fixture: dict) -> None:
    if fixture.get("fixture_id") != "TI001-v005-candidate-001":
        raise ValueError("unexpected v005 fixture_id")
    if fixture.get("version") != "v005-candidate-001":
        raise ValueError("unexpected v005 version")
    if fixture.get("status") != "FROZEN":
        raise ValueError("v005 fixture is not FROZEN")
    if fixture.get("scientific_execution") != "NOT_AUTHORIZED":
        raise ValueError("v005 fixture execution state changed unexpectedly")
    conditions = fixture.get("conditions", {})
    if set(conditions) != REQUIRED_CONDITIONS:
        raise ValueError("v005 condition set mismatch")
    for name in REQUIRED_CONDITIONS:
        c = conditions[name]
        if c.get("state") != "S0" or c.get("t_acc") != ["a", "b", "c"]:
            raise ValueError(f"{name}: current decision environment mismatch")
        if c.get("actions") != ["a", "b", "c"]:
            raise ValueError(f"{name}: action identity mismatch")

def build_decision_input(fixture: dict, condition: str) -> dict:
    c = fixture["conditions"][condition]
    info = {
        "state": c["state"],
        "currently_executable_transformations": list(c["t_acc"]),
        "task": fixture["task"],
    }
    if condition == "treatment":
        info["future_transformation_space_information"] = c["future_mapping"]
    return info

def validate_decision_units(units: list) -> None:
    if not units:
        raise ValueError("decision_units must not be empty")
    for u in units:
        if not isinstance(u, dict):
            raise ValueError("decision unit must be an object")
        if not isinstance(u.get("pair_id"), str) or not u["pair_id"]:
            raise ValueError("missing pair_id")
        if u.get("condition") not in REQUIRED_CONDITIONS:
            raise ValueError("invalid condition")
        if u.get("condition") == "treatment" and "future_mapping" in u:
            raise ValueError("decision unit must not duplicate treatment mapping")
        if u.get("condition") != "treatment" and "future_mapping" in u:
            raise ValueError("non-treatment unit contains future mapping")

def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("fixture")
    p.add_argument("decision_units")
    p.add_argument("prompt")
    p.add_argument("output")
    p.add_argument("--execute", action="store_true")
    args = p.parse_args(argv[1:])

    fixture = load_json(Path(args.fixture))
    units = load_json(Path(args.decision_units))
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    validate_fixture(fixture)
    fixture_hash = canonical_json_hash(fixture)
    validate_decision_units(units["decision_units"])
    prompt_hash = sha256_bytes(prompt.encode())
    expected_prompt_hash = "e451d2d89a353aa58030b3e59510837f5a664b186eb077662ae93376764f7006"
    if prompt_hash != expected_prompt_hash:
        raise ValueError("base prompt hash does not match frozen TI-001 prompt")

    if not args.execute:
        print(json.dumps({
            "status": "READY_NOT_EXECUTED",
            "provider_version": PROVIDER_VERSION,
            "fixture_sha256": fixture_hash,
            "base_prompt_sha256": prompt_hash,
            "decision_unit_count": len(units["decision_units"]),
            "reasoning": REASONING,
        }, indent=2, sort_keys=True))
        return 0

    client = OpenAI()
    decisions = {}
    for unit in units["decision_units"]:
        condition = unit["condition"]
        decision_input = build_decision_input(fixture, condition)
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
            diagnostic = {
                "event": "INVALID_MODEL_OUTPUT",
                "pair_id": unit["pair_id"],
                "condition": condition,
                "response_id": getattr(response, "id", None),
                "response_status": getattr(response, "status", None),
                "output_text_repr": repr(getattr(response, "output_text", "")),
                "incomplete_details": getattr(response, "incomplete_details", None),
                "usage": response.usage.model_dump() if getattr(response, "usage", None) else None,
                "output_structure": [
                    {
                        "id": getattr(item, "id", None),
                        "type": getattr(item, "type", None),
                        "status": getattr(item, "status", None),
                        "role": getattr(item, "role", None),
                        "phase": getattr(item, "phase", None),
                        "content_types": [getattr(part, "type", None) for part in (getattr(item, "content", None) or [])],
                    }
                    for item in (getattr(response, "output", None) or [])
                ],
            }
            print(json.dumps(diagnostic, indent=2, sort_keys=True, default=str), file=sys.stderr)
            raise ValueError(f"invalid model output: {selected!r}")
        key = f"{unit['pair_id']}::{condition}"
        decisions[key] = {
            "pair_id": unit["pair_id"],
            "condition": condition,
            "selected_transformation": selected,
            "request_timestamp": request_timestamp,
            "decision_timestamp": datetime.now(timezone.utc).isoformat(),
            "response_id": response.id,
            "response_status": response.status,
            "model_id": getattr(response, "model", MODEL_ID),
            "generation_configuration": {
                "top_p": TOP_P, "max_output_tokens": MAX_OUTPUT_TOKENS,
                "reasoning": REASONING, "tools": TOOLS, "tool_choice": TOOL_CHOICE,
                "background": BACKGROUND, "previous_response_id": None,
                "conversation": None, "store": STORE
            },
            "decision_input_sha256": input_hash,
            "usage": response.usage.model_dump() if getattr(response, "usage", None) else None,
        }

    package = {
        "record_type": "TGCV_TI001_V006_DECISION_AGENT_OUTPUT",
        "provider_version": PROVIDER_VERSION,
        "fixture_sha256": fixture_hash,
        "base_prompt_sha256": prompt_hash,
        "model_id": MODEL_ID,
        "api_surface": "Responses API",
        "generation_configuration": {
            "top_p": TOP_P, "max_output_tokens": MAX_OUTPUT_TOKENS,
            "reasoning": REASONING, "tools": TOOLS, "tool_choice": TOOL_CHOICE,
            "background": BACKGROUND, "previous_response_id": None,
            "conversation": None, "store": STORE
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
    Path(args.output).write_text(json.dumps(package, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    print(json.dumps({"status":"SCIENTIFIC_DECISIONS_WRITTEN","decision_count":len(decisions),"fixture_sha256":fixture_hash},indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
