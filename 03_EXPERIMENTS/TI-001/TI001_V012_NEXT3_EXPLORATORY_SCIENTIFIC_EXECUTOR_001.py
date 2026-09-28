#!/usr/bin/env python3
"""TI-001 V012 NEXT3 exploratory scientific executor.

Consumes the frozen CANDIDATE_FIXTURE_003 only. Scientific execution requires
--execute explicitly. The decision input is projected strictly from pre-decision
fields; z and all post-decision realization fields remain hidden from the model.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

MODEL_ID = "gpt-5.6-luna"
TOP_P = 0.98
MAX_OUTPUT_TOKENS = 128
REASONING_EFFORT = "low"
TOOLS = []
STORE = False

FIXTURE_ARTIFACT = "TI001_V012_NEXT3_CANDIDATE_FIXTURE_003"
FIXTURE_VERSION = "NEXT3_v003"
FIXTURE_SHA256 = "0f16ebd02275ed32c481d34f92f704bb375dbe21e90d807483904ca73a9912d0"
UNIT_COUNT = 23040
REPLICATES = 3
PROMPT_BLOB_SHA1 = "c8abc3c5bbb2ec9d226b37c7e8c7cf872f8c35e4"
ALLOWED = ("A", "B", "C", "D")
PROFILE_KEYS = ("reachable_change_count", "constraint_count", "composition_depth", "dependency_count")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_fixture(path: Path) -> list[dict]:
    actual = sha256_file(path)
    if actual != FIXTURE_SHA256:
        raise ValueError(f"Fixture SHA-256 mismatch: expected {FIXTURE_SHA256}, got {actual}")

    package = json.loads(path.read_text(encoding="utf-8"))
    if package.get("fixture_id") != FIXTURE_ARTIFACT:
        raise ValueError("Fixture artifact mismatch")
    if package.get("version") != FIXTURE_VERSION:
        raise ValueError("Fixture version mismatch")
    if package.get("unit_count") != UNIT_COUNT:
        raise ValueError("Fixture unit count mismatch")
    if package.get("replicates_per_cell") != REPLICATES:
        raise ValueError("Fixture replicates mismatch")

    rows = package.get("rows")
    if not isinstance(rows, list) or len(rows) != UNIT_COUNT:
        raise ValueError("Fixture rows/cardinality mismatch")

    for row in rows:
        if row.get("version") != FIXTURE_VERSION:
            raise ValueError("Unit version mismatch")
        if row.get("replicate") not in (1, 2, 3):
            raise ValueError("Unexpected replicate")
        if row.get("actions") != list(ALLOWED):
            raise ValueError("Candidate action set mismatch")
        if not isinstance(row.get("S_t"), dict) or not isinstance(row.get("task_context"), dict):
            raise ValueError("Missing pre-decision state/context")
        if sha256_bytes(canonical(row["S_t"]).encode()) != row.get("S_t_sha256"):
            raise ValueError(f"S_t hash mismatch: {row.get('unit_id')}")
        if sha256_bytes(canonical(row["task_context"]).encode()) != row.get("task_context_sha256"):
            raise ValueError(f"task_context hash mismatch: {row.get('unit_id')}")
        if set(row.get("f", {})) != set(ALLOWED) or set(row.get("z", {})) != set(ALLOWED):
            raise ValueError(f"Mapping cardinality mismatch: {row.get('unit_id')}")
        if sorted(row["f"].values()) != ["slot_1", "slot_2", "slot_3", "slot_4"]:
            raise ValueError(f"f is not bijective: {row.get('unit_id')}")
        if sorted(row["z"].values()) != ["slot_1", "slot_2", "slot_3", "slot_4"]:
            raise ValueError(f"z is not bijective: {row.get('unit_id')}")
    return rows


def build_decision_input(row: dict) -> dict:
    profiles = {}
    for item in row["presented_profiles"]:
        profile = item["profile"]
        profiles[item["action"]] = {
            key: profile[i] for i, key in enumerate(PROFILE_KEYS)
        }
    return {
        "current_state": row["S_t"],
        "task_context": row["task_context"],
        "candidate_actions": list(ALLOWED),
        "presented_structural_transformation_profile_for_each_candidate": profiles,
    }


def classify_response(text: str) -> tuple[str, str | None]:
    raw = text.strip()
    if raw in ALLOWED:
        return "VALID", raw
    return "INVALID", None


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture")
    parser.add_argument("prompt")
    parser.add_argument("output")
    parser.add_argument("--raw-jsonl", default=None)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv[1:])

    fixture_path = Path(args.fixture)
    prompt_path = Path(args.prompt)
    output_path = Path(args.output)
    raw_path = Path(args.raw_jsonl) if args.raw_jsonl else output_path.with_suffix(".jsonl")

    rows = load_fixture(fixture_path)
    prompt_bytes = prompt_path.read_bytes()
    prompt_sha256 = sha256_bytes(prompt_bytes)
    prompt = prompt_bytes.decode("utf-8")

    if not args.execute:
        print(json.dumps({
            "status": "READY_NOT_EXECUTED",
            "executor_id": "TI001-V012-NEXT3-EXPLORATORY-SCIENTIFIC-EXECUTOR-001",
            "fixture_artifact": FIXTURE_ARTIFACT,
            "fixture_sha256": FIXTURE_SHA256,
            "unit_count": UNIT_COUNT,
            "replicates": REPLICATES,
            "system_prompt_blob_sha1": PROMPT_BLOB_SHA1,
            "system_prompt_sha256": prompt_sha256,
            "scientific_execution": False,
        }, indent=2, sort_keys=True))
        return 0

    client = OpenAI()
    decisions = []
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    with raw_path.open("w", encoding="utf-8") as raw_file:
        for index, row in enumerate(rows, start=1):
            decision_input = build_decision_input(row)
            # Guard: the serialized model input must not contain fixture-only/post-decision fields.
            serialized_input = canonical(decision_input)
            forbidden = ("mapping_condition_metadata", '" + "f" + "', '" + "z" + "', S_t_plus_1, realized_transformation, T_acc, reward, value, utility, performance, outcome")
            if any(token in serialized_input for token in ["mapping_condition_metadata", '"f":', '"z":', "S_t_plus_1", "realized_transformation", "T_acc", "reward", "value", "utility", "performance", "outcome"]):
                raise RuntimeError(f"Pre-decision projection violation at {row['unit_id']}")

            request_timestamp = datetime.now(timezone.utc).isoformat()
            response = client.responses.create(
                model=MODEL_ID,
                instructions=prompt,
                input=serialized_input,
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

            decision = {
                "unit_id": row["unit_id"],
                "domain": row["domain"],
                "operationalisation": row["operationalisation"],
                "presentation": row["presentation"],
                "permutation_index": row["permutation_index"],
                "replicate": row["replicate"],
                "decision_input_sha256": sha256_bytes(serialized_input.encode("utf-8")),
                "request_timestamp": request_timestamp,
                "response_timestamp": response_timestamp,
                "response_id": response.id,
                "response_status": response.status,
                "raw_output_text": raw_text,
                "parsed_action": parsed,
                "validity": validity,
                "model_id": getattr(response, "model", MODEL_ID),
                "usage": usage.model_dump() if usage is not None else None,
            }
            raw_file.write(json.dumps(decision, ensure_ascii=False, sort_keys=True) + "\n")
            raw_file.flush()
            decisions.append(decision)

            if index % 100 == 0:
                print(json.dumps({"progress": index, "total": UNIT_COUNT}), flush=True)

    package = {
        "record_type": "TGCV_TI001_V012_NEXT3_EXPLORATORY_SCIENTIFIC_EXECUTION_RESULT",
        "executor_id": "TI001-V012-NEXT3-EXPLORATORY-SCIENTIFIC-EXECUTOR-001",
        "fixture_artifact": FIXTURE_ARTIFACT,
        "fixture_version": FIXTURE_VERSION,
        "fixture_sha256": FIXTURE_SHA256,
        "system_prompt_blob_sha1": PROMPT_BLOB_SHA1,
        "system_prompt_sha256": prompt_sha256,
        "model_id": MODEL_ID,
        "api_surface": "Responses API",
        "generation_configuration": {
            "top_p": TOP_P,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "reasoning_effort": REASONING_EFFORT,
            "tools": TOOLS,
            "store": STORE,
            "retry": False,
        },
        "execution_environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "replicates": REPLICATES,
        "decision_count": len(decisions),
        "decisions": decisions,
        "scientific_execution": True,
        "exploratory_only": True,
        "confirmatory": False,
        "recoding": False,
        "substitution": False,
    }
    output_path.write_text(json.dumps(package, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "SCIENTIFIC_EXECUTION_COMPLETE", "decision_count": len(decisions), "output": str(output_path)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
