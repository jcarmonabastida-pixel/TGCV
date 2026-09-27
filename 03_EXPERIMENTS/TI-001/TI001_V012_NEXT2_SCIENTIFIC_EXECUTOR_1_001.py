#!/usr/bin/env python3
"""TI-001 V012 NEXT2 scientific Executor-1.

Canonical executor for frozen NEXT2_v001. The executor consumes only
pre-decision fields from each fixture unit and never exposes realized z
to the model. Scientific execution requires --execute explicitly.
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
MAX_OUTPUT_TOKENS = 128
REASONING_EFFORT = "low"
TOOLS = []
STORE = False

FIXTURE_VERSION = "NEXT2_v001"
FIXTURE_ARTIFACT = "TI001_V012_NEXT2_FIXTURE_REGENERATED_001"
UNIT_COUNT = 23040
SHARD_COUNT = 24
UNITS_PER_SHARD = 960

REQUIREMENTS_SHA256 = "c9e55982188e4242124adbe196a6d98211bec2fe"
SEMANTICS_SHA256 = "b0801bfc7e7614f5fc7ca6304fb305c0d77d9252"
SCHEMA_SHA256 = "6c6f72435039bcab594829a629c7828b39d83305"
PROMPT_SHA256 = "660002f6506648fd0bfd703751f8996fae9fe0aaed3a48defbe78b2382c94122"

ALLOWED = ("A", "B", "C", "D")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_fixture(fixture_dir: Path, register_path: Path) -> list[dict]:
    manifest = json.loads((fixture_dir / "MANIFEST.json").read_text(encoding="utf-8"))
    register = json.loads(register_path.read_text(encoding="utf-8"))

    if manifest["immutable_version"] != FIXTURE_VERSION:
        raise ValueError("NEXT2 immutable version mismatch")
    if manifest["unit_count"] != UNIT_COUNT or manifest["shard_count"] != SHARD_COUNT:
        raise ValueError("NEXT2 fixture dimensions mismatch")
    if manifest["units_per_shard"] != UNITS_PER_SHARD:
        raise ValueError("NEXT2 units_per_shard mismatch")
    if manifest["status"] != "GENERATED_NOT_FROZEN":
        raise ValueError("Fixture manifest must remain the canonical generated manifest")
    if register["immutable_version"] != FIXTURE_VERSION:
        raise ValueError("NEXT2 integrity register version mismatch")
    if register["unit_count"] != UNIT_COUNT or register["shard_count"] != SHARD_COUNT:
        raise ValueError("NEXT2 integrity register dimensions mismatch")
    if register["scientific_execution"] is not False:
        raise ValueError("Integrity register scientific_execution must remain false")
    if register["freeze_authorized"] is not False:
        raise ValueError("Integrity register freeze_authorized must remain false")

    for name, expected in register["files_sha256"].items():
        actual = sha256_file(fixture_dir / name)
        if actual != expected:
            raise ValueError(f"Fixture hash mismatch: {name}")

    rows: list[dict] = []
    for i in range(1, SHARD_COUNT + 1):
        rows.extend(json.loads((fixture_dir / f"SHARD_{i:03d}.json").read_text(encoding="utf-8")))

    if len(rows) != UNIT_COUNT:
        raise ValueError("NEXT2 unit count mismatch")
    ids = [row["id"] for row in rows]
    if ids != [f"N2-{i:05d}" for i in range(1, UNIT_COUNT + 1)]:
        raise ValueError("NEXT2 unit ordering mismatch")
    return rows


def build_decision_input(record: dict) -> dict:
    return {
        "current_task": "select_one_current_transformation",
        "available_transformations": list(ALLOWED),
        "domain": f"D{record['d']}",
        "future_space_operationalisation": f"O{record['o']}",
        "mapping_condition": record["m"],
        "presentation": f"P{record['p']}",
        "action_mapping_permutation_index": record["k"],
        "state": {
            "state_id": record["s"],
            "T_acc": list(ALLOWED),
        },
        "future_space_information": {
            "presented_action_to_future_slot": dict(record["f"])
        },
        "decision_boundary": {
            "decision_before_future_reveal": True,
            "realized_successor_visible_at_decision": False,
            "realized_T_acc_visible_at_decision": False,
        },
    }


def classify_response(text: str) -> tuple[str, str | None]:
    raw = text.strip()
    if raw in ALLOWED:
        return "VALID", raw
    return "INVALID", None


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture_dir")
    parser.add_argument("integrity_register")
    parser.add_argument("prompt")
    parser.add_argument("output")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv[1:])

    fixture_dir = Path(args.fixture_dir)
    register_path = Path(args.integrity_register)
    prompt_path = Path(args.prompt)

    rows = load_fixture(fixture_dir, register_path)
    prompt = prompt_path.read_text(encoding="utf-8")
    if sha256_bytes(prompt.encode("utf-8")) != PROMPT_SHA256:
        raise ValueError("NEXT2 system prompt hash mismatch")

    if not args.execute:
        print(json.dumps({
            "status": "READY_NOT_EXECUTED",
            "executor_id": "TI001-V012-NEXT2-SCIENTIFIC-EXECUTOR-1-001",
            "fixture_artifact": FIXTURE_ARTIFACT,
            "immutable_version": FIXTURE_VERSION,
            "unit_count": len(rows),
            "system_prompt_sha256": PROMPT_SHA256,
            "scientific_execution": False,
        }, indent=2, sort_keys=True))
        return 0

    client = OpenAI()
    decisions = []

    for record in rows:
        request_timestamp = datetime.now(timezone.utc).isoformat()
        decision_input = build_decision_input(record)
        response = client.responses.create(
            model=MODEL_ID,
            instructions=prompt,
            input=json.dumps(
                decision_input, sort_keys=True, separators=(",", ":"),
                ensure_ascii=False
            ),
            reasoning={"effort": REASONING_EFFORT},
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
            "unit_id": record["id"],
            "d": record["d"],
            "o": record["o"],
            "mapping_condition": record["m"],
            "presentation": record["p"],
            "permutation_index": record["k"],
            "replicate": record["r"],
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
                "reasoning_effort": REASONING_EFFORT,
                "tools": TOOLS,
                "previous_response_id": None,
                "conversation": None,
                "store": STORE,
            },
            "model_id": getattr(response, "model", MODEL_ID),
            "usage": usage.model_dump() if usage is not None else None,
        })

    package = {
        "record_type": "TGCV_TI001_V012_NEXT2_SCIENTIFIC_EXECUTION_RESULT",
        "executor_id": "TI001-V012-NEXT2-SCIENTIFIC-EXECUTOR-1-001",
        "fixture_artifact": FIXTURE_ARTIFACT,
        "immutable_version": FIXTURE_VERSION,
        "system_prompt_sha256": PROMPT_SHA256,
        "requirements_sha256": REQUIREMENTS_SHA256,
        "semantics_sha256": SEMANTICS_SHA256,
        "schema_sha256": SCHEMA_SHA256,
        "model_id": MODEL_ID,
        "api_surface": "Responses API",
        "generation_configuration": {
            "top_p": TOP_P,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "reasoning_effort": REASONING_EFFORT,
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
        "fixture_artifact": FIXTURE_ARTIFACT,
        "immutable_version": FIXTURE_VERSION,
        "scientific_execution": True,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv))
