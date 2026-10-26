"""Deterministic, isolated heuristic ranking over already-enumerated TGCV toy trajectories.

This module does not enumerate paths, evaluate conditions, execute paths, predict outcomes,
or infer contextual value. It consumes one scenario result produced by the existing engine.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from typing import Any

SELECTOR_VERSION = "trajectory-selector-001"
CONTRACT_VERSION = "trajectory-selector-contract-001"
OUTPUT_KIND = "HEURISTIC_RANKING_NOT_PREDICTION"
PROVENANCE_STATUS = "DECLARED_NOT_INDEPENDENTLY_VERIFIED"
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class SelectorInputError(ValueError):
    """Raised when the selector input violates its explicit data contract."""


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def _sha256_json(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _validate_sha256(value: Any, name: str) -> str:
    if not isinstance(value, str) or not _SHA256_RE.fullmatch(value):
        raise SelectorInputError(f"{name} must be a lowercase 64-character SHA-256 hex digest")
    return value


def _path_transitions(path: Any) -> list[str]:
    if not isinstance(path, list) or not path:
        raise SelectorInputError("each trajectory must be a non-empty list of steps")
    transitions: list[str] = []
    for index, step in enumerate(path):
        if not isinstance(step, dict) or not isinstance(step.get("state"), str):
            raise SelectorInputError(f"trajectory step {index} must contain a string state")
        if index == 0:
            if "transition" in step:
                raise SelectorInputError("initial trajectory step must not contain a transition")
        else:
            transition_id = step.get("transition")
            if not isinstance(transition_id, str) or not transition_id:
                raise SelectorInputError(f"trajectory step {index} must contain a transition id")
            transitions.append(transition_id)
    return transitions


def _criterion_value(criterion: dict[str, Any], path: list[dict[str, Any]], transitions: list[str]) -> Any:
    source = criterion.get("source")
    if source == "step_count":
        return len(path) - 1
    if source == "transition_present":
        transition_id = criterion.get("transition_id")
        if not isinstance(transition_id, str) or not transition_id:
            raise SelectorInputError("transition_present criteria require transition_id")
        return transition_id in transitions
    raise SelectorInputError(f"unsupported criterion source: {source!r}")


def _validate_config(config: Any) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if not isinstance(config, dict) or set(config) - {"config_id", "version", "criteria", "restrictions"}:
        raise SelectorInputError("criteria_config must be an object with only documented fields")
    config_id = config.get("config_id")
    if not isinstance(config_id, str) or not config_id.strip():
        raise SelectorInputError("criteria_config.config_id is required")
    version = config.get("version")
    if not isinstance(version, str) or not version.strip():
        raise SelectorInputError("criteria_config.version is required")
    criteria = config.get("criteria")
    restrictions = config.get("restrictions")
    if not isinstance(criteria, list) or not isinstance(restrictions, list):
        raise SelectorInputError("criteria and restrictions must be lists")
    if not criteria and not restrictions:
        raise SelectorInputError("at least one criterion or restriction must be configured")

    seen: set[str] = set()
    clean_criteria: list[dict[str, Any]] = []
    for criterion in criteria:
        if not isinstance(criterion, dict) or set(criterion) - {
            "id", "direction", "source", "transition_id", "unit", "missing_policy"
        }:
            raise SelectorInputError("criterion has unknown fields or is not an object")
        criterion_id = criterion.get("id")
        if not isinstance(criterion_id, str) or not criterion_id.strip() or criterion_id in seen:
            raise SelectorInputError("criterion ids must be non-empty and unique across criteria/restrictions")
        seen.add(criterion_id)
        if criterion.get("direction") not in {"minimize", "maximize"}:
            raise SelectorInputError(f"criterion {criterion_id!r} direction must be minimize or maximize")
        if criterion.get("source") not in {"step_count", "transition_present"}:
            raise SelectorInputError(f"criterion {criterion_id!r} has unsupported source")
        if criterion.get("missing_policy", "abstain") != "abstain":
            raise SelectorInputError("v1 supports only missing_policy='abstain'")
        if "unit" in criterion and not isinstance(criterion["unit"], str):
            raise SelectorInputError(f"criterion {criterion_id!r} unit must be a string")
        clean_criteria.append(copy.deepcopy(criterion))

    clean_restrictions: list[dict[str, Any]] = []
    for restriction in restrictions:
        if not isinstance(restriction, dict) or set(restriction) - {"id", "source", "transition_id", "must_be_present"}:
            raise SelectorInputError("restriction has unknown fields or is not an object")
        restriction_id = restriction.get("id")
        if not isinstance(restriction_id, str) or not restriction_id.strip() or restriction_id in seen:
            raise SelectorInputError("criterion ids must be non-empty and unique across criteria/restrictions")
        seen.add(restriction_id)
        if restriction.get("source") != "transition_present":
            raise SelectorInputError(f"restriction {restriction_id!r} has unsupported source")
        if not isinstance(restriction.get("transition_id"), str) or not restriction["transition_id"]:
            raise SelectorInputError(f"restriction {restriction_id!r} requires transition_id")
        if not isinstance(restriction.get("must_be_present"), bool):
            raise SelectorInputError(f"restriction {restriction_id!r} requires boolean must_be_present")
        clean_restrictions.append(copy.deepcopy(restriction))
    return clean_criteria, clean_restrictions


def select_trajectories(
    scenario_result: dict[str, Any],
    criteria_config: dict[str, Any],
    *,
    scenario_id: str,
    model_sha256: str,
    result_sha256: str,
) -> dict[str, Any]:
    """Return an auditable lexicographic ranking without modifying inputs.

    Supported v1 preference sources are step count and presence of a named transition.
    Supported restrictions require or forbid a named transition. Unsupported or missing
    data causes explicit abstention; no defaults, weights, costs, or values are inferred.
    """
    if not isinstance(scenario_id, str) or not scenario_id.strip():
        raise SelectorInputError("scenario_id is required")
    model_hash = _validate_sha256(model_sha256, "model_sha256")
    result_hash = _validate_sha256(result_sha256, "result_sha256")
    if not isinstance(scenario_result, dict):
        raise SelectorInputError("scenario_result must be an object")
    required = {
        "scenario_id", "disabled_transitions", "enabled_transitions_at_initial_state",
        "reachable_states", "trajectories", "truncated", "exploration_bounds",
        "temporal_prerequisites",
    }
    if not required.issubset(scenario_result):
        raise SelectorInputError(f"scenario_result missing fields: {sorted(required - set(scenario_result))}")
    if scenario_result["scenario_id"] != scenario_id:
        raise SelectorInputError("scenario_id does not match scenario_result")
    if not isinstance(scenario_result["truncated"], bool):
        raise SelectorInputError("truncated must be boolean")
    if not isinstance(scenario_result["trajectories"], list):
        raise SelectorInputError("trajectories must be a list")
    if not isinstance(scenario_result["exploration_bounds"], dict):
        raise SelectorInputError("exploration_bounds must be an object")
    if not isinstance(scenario_result["temporal_prerequisites"], list):
        raise SelectorInputError("temporal_prerequisites must be a list")

    criteria, restrictions = _validate_config(criteria_config)
    snapshot = {
        "scenario_id": scenario_id,
        "scenario_result": copy.deepcopy(scenario_result),
        "criteria_config": copy.deepcopy(criteria_config),
        "model_sha256": model_hash,
        "result_sha256": result_hash,
    }
    input_sha256 = _sha256_json(snapshot)
    warnings: list[str] = [
        "PROVENANCE_NOT_INDEPENDENTLY_VERIFIED: supplied model/result hashes are format-checked and recorded, not recomputed from source artifacts"
    ]
    if scenario_result["truncated"]:
        warnings.append("EXPLORATION_TRUNCATED: ranking covers observed trajectories only; global optimality is not established")

    paths = scenario_result["trajectories"]
    if not paths:
        return {
            "contract_version": CONTRACT_VERSION,
            "selector_version": SELECTOR_VERSION,
            "output_kind": OUTPUT_KIND,
            "status": "ABSTAINED",
            "reason": "NO_TRAJECTORIES",
            "scenario_id": scenario_id,
            "input_sha256": input_sha256,
            "model_sha256": model_hash,
            "result_sha256": result_hash,
            "provenance_status": PROVENANCE_STATUS,
            "config_sha256": _sha256_json(criteria_config),
            "criteria_config": copy.deepcopy(criteria_config),
            "exploration": {
                "truncated": scenario_result["truncated"],
                "exploration_bounds": copy.deepcopy(scenario_result["exploration_bounds"]),
            },
            "ranked_trajectories": [],
            "warnings": warnings,
        }

    records: list[dict[str, Any]] = []
    for index, path in enumerate(paths):
        transitions = _path_transitions(path)
        trajectory_sha = _sha256_json(path)
        restriction_results = []
        for restriction in restrictions:
            present = restriction["transition_id"] in transitions
            satisfied = present is restriction["must_be_present"]
            restriction_results.append({
                "id": restriction["id"],
                "transition_id": restriction["transition_id"],
                "must_be_present": restriction["must_be_present"],
                "actual_present": present,
                "satisfied": satisfied,
            })
        eligible = all(item["satisfied"] for item in restriction_results)
        values = []
        sort_key = []
        for criterion in criteria:
            value = _criterion_value(criterion, path, transitions)
            values.append({
                "id": criterion["id"],
                "source": criterion["source"],
                "direction": criterion["direction"],
                "unit": criterion.get("unit"),
                "value": value,
            })
            # Bool is a supported categorical value for transition presence. Invert it
            # for maximize/minimize into a numeric sort key without mixing units.
            if isinstance(value, bool):
                ordered_value = int(value)
                sort_key.append(-ordered_value if criterion["direction"] == "maximize" else ordered_value)
            else:
                sort_key.append(-value if criterion["direction"] == "maximize" else value)
        explanation_parts = [str(item["id"]) + "=" + repr(item["value"]) + " (" + item["direction"] + ")" for item in values]
        restriction_summary = ("all configured restrictions satisfied" if eligible else "ineligible: " + ", ".join(item["id"] for item in restriction_results if not item["satisfied"]))
        records.append({
            "trajectory_id": f"trajectory-{trajectory_sha[:16]}",
            "trajectory_sha256": trajectory_sha,
            "source_index": index,
            "eligible": eligible,
            "status": "ELIGIBLE" if eligible else "INELIGIBLE",
            "criteria": values,
            "restrictions": restriction_results,
            "position_explanation": ("Lexicographic criteria: " + "; ".join(explanation_parts) + ". " if explanation_parts else "No preference criteria configured. ") + restriction_summary + ".",
            "_sort_key": tuple(sort_key),
        })

    eligible_records = [record for record in records if record["eligible"]]
    if not eligible_records:
        return {
            "contract_version": CONTRACT_VERSION,
            "selector_version": SELECTOR_VERSION,
            "output_kind": OUTPUT_KIND,
            "status": "ABSTAINED",
            "reason": "NO_ADMISSIBLE_TRAJECTORIES",
            "scenario_id": scenario_id,
            "input_sha256": input_sha256,
            "model_sha256": model_hash,
            "result_sha256": result_hash,
            "provenance_status": PROVENANCE_STATUS,
            "config_sha256": _sha256_json(criteria_config),
            "criteria_config": copy.deepcopy(criteria_config),
            "exploration": {
                "truncated": scenario_result["truncated"],
                "exploration_bounds": copy.deepcopy(scenario_result["exploration_bounds"]),
            },
            "ranked_trajectories": [
                {key: value for key, value in record.items() if key != "_sort_key"}
                for record in records
            ],
            "warnings": warnings,
        }

    # If an active preference cannot be evaluated, v1 abstains rather than silently
    # assigning zero/favorability. The supported sources above are fully path-derived.
    eligible_records.sort(key=lambda record: (record["_sort_key"], record["trajectory_sha256"]))
    ranked = []
    previous_key = None
    rank = 0
    for record in eligible_records:
        if record["_sort_key"] != previous_key:
            rank += 1
            previous_key = record["_sort_key"]
        public = {key: value for key, value in record.items() if key != "_sort_key"}
        public["rank"] = rank
        public["tie_group"] = f"tie-{rank}"
        public["tie_note"] = "equal substantive criteria; trajectory hash is used only for stable presentation"
        ranked.append(public)
    ranked.extend(
        {key: value for key, value in record.items() if key != "_sort_key"}
        for record in records if not record["eligible"]
    )
    return {
        "contract_version": CONTRACT_VERSION,
        "selector_version": SELECTOR_VERSION,
        "output_kind": OUTPUT_KIND,
        "status": "PARTIAL_TRUNCATED" if scenario_result["truncated"] else "RANKED",
        "reason": "EXPLORATION_TRUNCATED" if scenario_result["truncated"] else None,
        "scenario_id": scenario_id,
        "input_sha256": input_sha256,
        "model_sha256": model_hash,
        "result_sha256": result_hash,
        "provenance_status": PROVENANCE_STATUS,
        "config_sha256": _sha256_json(criteria_config),
        "criteria_config": copy.deepcopy(criteria_config),
        "exploration": {
            "truncated": scenario_result["truncated"],
            "exploration_bounds": copy.deepcopy(scenario_result["exploration_bounds"]),
            "temporal_prerequisites": copy.deepcopy(scenario_result["temporal_prerequisites"]),
        },
        "ranked_trajectories": ranked,
        "warnings": warnings,
    }
