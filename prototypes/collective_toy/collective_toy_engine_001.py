"""Synthetic-only TGCV Collective Toy engine, temporal profile 3 only.

This module executes temporal prerequisite graphs over synthetic data. It does
not implement TGCV T_acc, value, causality, or empirical inference.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import hashlib
import json
import copy
import math
import uuid
from typing import Any


ENGINE_VERSION = "collective-toy-engine-001"
SUPPORTED_SCHEMA = "collective-toy-input-001"


class ModelValidationError(ValueError):
    """Raised when a model or scenario violates the input contract."""


def _reject_unknown_keys(value: dict[str, Any], allowed: set[str], context: str) -> None:
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise ModelValidationError(f"{context} contains unknown fields: {unknown}")


MAX_SAFE_JSON_INTEGER = 9_007_199_254_740_991


def _validate_canonical_domain(value: Any, path: str = "$") -> None:
    """Limit inputs to a JSON domain with matching Python/JavaScript number and string behavior."""
    if value is None or isinstance(value, bool):
        return
    if isinstance(value, int):
        if abs(value) > MAX_SAFE_JSON_INTEGER:
            raise ModelValidationError(f"{path} contains an integer outside JavaScript's safe integer range")
        return
    if isinstance(value, float):
        if not math.isfinite(value) or not value.is_integer() or abs(value) > MAX_SAFE_JSON_INTEGER:
            raise ModelValidationError(f"{path} contains a number that is not a finite safe integer")
        return
    if isinstance(value, str):
        if any(0xD800 <= ord(char) <= 0xDFFF for char in value):
            raise ModelValidationError(f"{path} contains an unpaired Unicode surrogate")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_canonical_domain(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ModelValidationError(f"{path} contains a non-string object key")
            _validate_canonical_domain(key, f"{path}.<key>")
            _validate_canonical_domain(item, f"{path}.{key}")
        return
    raise ModelValidationError(f"{path} contains a non-JSON value")


def _normalize_integral_floats(value: Any) -> Any:
    if isinstance(value, float):
        return int(value)
    if isinstance(value, list):
        return [_normalize_integral_floats(item) for item in value]
    if isinstance(value, dict):
        return {key: _normalize_integral_floats(item) for key, item in value.items()}
    return value


def canonical_json(value: Any) -> str:
    """Serialize the supported JSON domain deterministically across Python and JavaScript."""
    _validate_canonical_domain(value)
    return json.dumps(
        _normalize_integral_floats(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


SEMANTIC_IDENTITY_VERSION = "collective-toy-semantic-identity-001"


def semantic_result_projection(output: dict[str, Any]) -> dict[str, Any]:
    """Project result semantics while excluding provenance and normalizing known unordered lists.

    This is deliberately schema-aware: trajectory and temporal step order is preserved.
    """
    projected = json.loads(canonical_json(output))
    projected.pop("delta_reach", None)
    projected.pop("engine_version", None)  # provenance, not model/result semantics
    projected.pop("input_sha256", None)
    projected.pop("result_sha256", None)
    projected.pop("semantic_sha256", None)
    projected.pop("semantic_identity_version", None)
    for scenario in projected.get("scenario_results", {}).values():
        if isinstance(scenario.get("disabled_transitions"), list):
            scenario["disabled_transitions"].sort()
    for comparison in projected.get("comparisons_to_baseline", {}).values():
        intervention = comparison.get("intervention", {})
        if isinstance(intervention.get("disabled_transitions"), list):
            intervention["disabled_transitions"].sort()
    return projected


@dataclass(frozen=True)
class Transition:
    id: str
    source: str
    target: str
    condition: str | None = None


def validate_model(model: dict[str, Any]) -> tuple[dict[str, str], dict[str, Transition]]:
    if not isinstance(model, dict):
        raise ModelValidationError("model must be a JSON object")
    _validate_canonical_domain(model)
    _reject_unknown_keys(model, {"schema_version", "model_id", "initial_state", "states", "transitions", "relations", "rule_profile", "scenarios", "exploration"}, "model")
    if model.get("schema_version") != SUPPORTED_SCHEMA:
        raise ModelValidationError(f"schema_version must be {SUPPORTED_SCHEMA!r}")
    if not isinstance(model.get("model_id"), str) or not model["model_id"].strip():
        raise ModelValidationError("model_id must be a non-empty string")
    states = model.get("states")
    if not isinstance(states, list) or not states:
        raise ModelValidationError("states must be a non-empty list")
    if any(not isinstance(s, str) or not s for s in states):
        raise ModelValidationError("each state ID must be a non-empty string")
    if len(set(states)) != len(states):
        raise ModelValidationError("duplicate state IDs")
    initial_state = model.get("initial_state")
    if not isinstance(initial_state, str) or initial_state not in set(states):
        raise ModelValidationError("initial_state must be a state ID string referencing a declared state")

    profile = model.get("rule_profile")
    profile3 = {"type": "temporal_prerequisite_graph", "version": "1"}
    if not isinstance(profile, dict):
        raise ModelValidationError("rule_profile must be an object")
    _reject_unknown_keys(profile, {"type", "version"}, "rule_profile")
    if profile != profile3:
        raise ModelValidationError("unsupported rule_profile; only temporal_prerequisite_graph v1 is supported")

    raw_transitions = model.get("transitions")
    if not isinstance(raw_transitions, list):
        raise ModelValidationError("transitions must be a list")
    transitions: dict[str, Transition] = {}
    for item in raw_transitions:
        if not isinstance(item, dict):
            raise ModelValidationError("each transition must be an object")
        _reject_unknown_keys(item, {"id", "source", "target", "condition"}, "transition")
        tid, source, target = item.get("id"), item.get("source"), item.get("target")
        if any(not isinstance(x, str) or not x for x in (tid, source, target)):
            raise ModelValidationError("transition id, source, and target must be non-empty strings")
        if tid in transitions:
            raise ModelValidationError(f"duplicate transition ID: {tid}")
        if source not in states or target not in states:
            raise ModelValidationError(f"transition {tid} references an unknown state")
        condition = item.get("condition")
        if condition is not None and (not isinstance(condition, str) or not condition.strip()):
            raise ModelValidationError(f"transition {tid} condition must be a non-empty string when provided")
        transitions[tid] = Transition(tid, source, target, condition.strip() if condition is not None else None)

    relations = model.get("relations", [])
    if not isinstance(relations, list):
        raise ModelValidationError("relations must be a list")
    relation_ids: set[str] = set()
    for relation in relations:
        if not isinstance(relation, dict):
            raise ModelValidationError("each relation must be an object")
        _reject_unknown_keys(relation, {"id", "type", "transition_id", "requires_transition_id"}, "relation")
        rid, rtype = relation.get("id"), relation.get("type")
        guarded, prerequisite = relation.get("transition_id"), relation.get("requires_transition_id")
        if not isinstance(rid, str) or not rid:
            raise ModelValidationError("relation id must be a non-empty string")
        if rid in relation_ids:
            raise ModelValidationError(f"duplicate relation ID: {rid}")
        relation_ids.add(rid)
        expected_type = "requires_prior_execution"
        if rtype != expected_type:
            raise ModelValidationError(f"unsupported relation type for {profile['type']}: {rtype!r}; expected {expected_type!r}")
        if not isinstance(guarded, str) or not guarded or not isinstance(prerequisite, str) or not prerequisite:
            raise ModelValidationError(f"{profile['type']} relations require transition_id and requires_transition_id")
        if guarded not in transitions:
            raise ModelValidationError(f"relation {rid} references unknown guarded transition: {guarded}")
        if prerequisite not in transitions:
            raise ModelValidationError(f"relation {rid} references unknown prerequisite transition: {prerequisite}")
        if guarded == prerequisite:
            raise ModelValidationError(f"relation {rid} cannot require a transition to enable itself")
    scenarios = model.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise ModelValidationError("scenarios must be a non-empty list")
    scenario_ids: set[str] = set()
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            raise ModelValidationError("each scenario must be an object")
        _reject_unknown_keys(scenario, {"id", "disabled_transitions"}, "scenario")
        sid = scenario.get("id")
        if not isinstance(sid, str) or not sid:
            raise ModelValidationError("scenario id must be a non-empty string")
        if sid in scenario_ids:
            raise ModelValidationError(f"duplicate scenario ID: {sid}")
        scenario_ids.add(sid)
        disabled = scenario.get("disabled_transitions", [])
        if not isinstance(disabled, list):
            raise ModelValidationError(f"disabled_transitions for {sid} must be a list")
        if any(not isinstance(tid, str) or not tid for tid in disabled):
            raise ModelValidationError(
                f"disabled_transitions for {sid} must contain non-empty transition ID strings"
            )
        unknown = set(disabled) - set(transitions)
        if unknown:
            raise ModelValidationError(f"scenario {sid} references unknown transitions: {sorted(unknown)}")
        if len(disabled) != len(set(disabled)):
            raise ModelValidationError(f"scenario {sid} repeats a disabled transition")
    if "baseline" not in scenario_ids:
        raise ModelValidationError("a scenario with id 'baseline' is required")

    exploration = model.get("exploration")
    if not isinstance(exploration, dict):
        raise ModelValidationError("exploration must be an object")
    _reject_unknown_keys(exploration, {"max_depth", "max_trajectories"}, "exploration")
    max_depth, max_trajectories = exploration.get("max_depth"), exploration.get("max_trajectories")
    if not isinstance(max_depth, int) or isinstance(max_depth, bool) or max_depth < 0:
        raise ModelValidationError("max_depth must be a non-negative integer")
    if not isinstance(max_trajectories, int) or isinstance(max_trajectories, bool) or max_trajectories < 1:
        raise ModelValidationError("max_trajectories must be a positive integer")
    # Keep Python's accepted domain identical to the browser UI's documented resource caps.
    if len(states) > 500 or len(transitions) > 2000:
        raise ModelValidationError("model exceeds limits: at most 500 states and 2000 transitions")
    if max_depth > 100 or max_trajectories > 10000:
        raise ModelValidationError("exploration exceeds limits: max_depth <= 100 and max_trajectories <= 10000")
    return {s: s for s in states}, transitions


def _temporal_scenario_result(
    model: dict[str, Any], transitions: dict[str, Transition], scenario: dict[str, Any]
) -> dict[str, Any]:
    """Explore paths while carrying path-local temporal prerequisite history."""
    explicit_disabled = set(scenario.get("disabled_transitions", []))
    prerequisites: dict[str, set[str]] = {}
    for relation in model.get("relations", []):
        prerequisites.setdefault(relation["transition_id"], set()).add(relation["requires_transition_id"])
    adjacency: dict[str, list[Transition]] = {s: [] for s in model["states"]}
    for transition in transitions.values():
        # Conditions are preserved in the model but never evaluated by this engine.
        # Therefore conditional transitions are not traversable in reachability or trajectories.
        if transition.condition is None:
            adjacency[transition.source].append(transition)
    for outgoing in adjacency.values():
        outgoing.sort(key=lambda item: item.id)

    initial = model["initial_state"]
    max_depth = model["exploration"]["max_depth"]
    max_trajectories = model["exploration"]["max_trajectories"]

    # Compute reachability independently from bounded trajectory enumeration.
    # Temporal applicability depends on the set of transitions already executed,
    # so the search state is (graph state, executed-transition set). This finite
    # configuration search does not consume the user-facing depth/trajectory caps.
    reached = {initial}
    # Only execution of transitions that are prerequisites for another transition
    # can affect future applicability. Discard all other history from the search
    # key; this avoids exponential configuration growth on cyclic graphs without
    # temporal relations (including the engineering benchmark fixtures).
    prerequisite_ids = frozenset(
        prerequisite
        for required in prerequisites.values()
        for prerequisite in required
    )
    pending_configs: list[tuple[str, frozenset[str]]] = [(initial, frozenset())]
    visited_configs: set[tuple[str, frozenset[str]]] = set()
    while pending_configs:
        config_state, executed = pending_configs.pop()
        config = (config_state, executed)
        if config in visited_configs:
            continue
        visited_configs.add(config)
        for transition in adjacency[config_state]:
            if transition.id in explicit_disabled:
                continue
            if not prerequisites.get(transition.id, set()).issubset(executed):
                continue
            reached.add(transition.target)
            next_executed = (executed | {transition.id}) & prerequisite_ids
            next_config = (transition.target, next_executed)
            if next_config not in visited_configs:
                pending_configs.append(next_config)

    trajectories: list[list[dict[str, str]]] = []
    truncated = False
    stack: list[tuple[str, list[dict[str, str]], tuple[str, ...], int]] = [
        (initial, [{"state": initial}], tuple(), 0)
    ]
    while stack:
        state, path, history, depth = stack.pop()
        available = [
            transition for transition in adjacency[state]
            if transition.id not in explicit_disabled
            and prerequisites.get(transition.id, set()).issubset(set(history))
        ]
        if depth >= max_depth:
            if available:
                truncated = True
            if len(trajectories) < max_trajectories:
                trajectories.append(path)
            else:
                truncated = True
                break
            continue
        if not available:
            if len(trajectories) < max_trajectories:
                trajectories.append(path)
            else:
                truncated = True
                break
            continue
        for transition in reversed(available):
            next_path = path + [{"transition": transition.id, "state": transition.target}]
            next_history = history + (transition.id,)
            reached.add(transition.target)
            stack.append((transition.target, next_path, next_history, depth + 1))
        if len(trajectories) >= max_trajectories and stack:
            truncated = True
            break

    enabled_at_initial = sorted(
        transition.id for transition in adjacency[initial]
        if transition.id not in explicit_disabled
        and prerequisites.get(transition.id, set()).issubset(set())
    )
    return {
        "scenario_id": scenario["id"],
        "disabled_transitions": sorted(explicit_disabled),
        "enabled_transitions_at_initial_state": enabled_at_initial,
        "reachable_states": sorted(reached),
        "trajectories": trajectories,
        "truncated": truncated,
        "exploration_bounds": {"max_depth": max_depth, "max_trajectories": max_trajectories},
        "temporal_prerequisites": [
            {"transition_id": transition_id, "requires_transition_ids": sorted(required)}
            for transition_id, required in sorted(prerequisites.items())
        ],
    }


def execute_sequence(
    model: dict[str, Any], scenario_id: str, transition_ids: list[str]
) -> dict[str, Any]:
    """Execute one concrete ordered sequence and retain immutable replay provenance."""
    _, transitions = validate_model(model)
    profile = model["rule_profile"]
    scenarios = {scenario["id"]: scenario for scenario in model["scenarios"]}
    if scenario_id not in scenarios:
        raise ModelValidationError(f"unknown scenario ID: {scenario_id}")
    if not isinstance(transition_ids, list) or any(not isinstance(item, str) for item in transition_ids):
        raise ModelValidationError("transition_ids must be a list of transition ID strings")
    scenario = scenarios[scenario_id]
    disabled = set(scenario.get("disabled_transitions", []))
    prerequisites: dict[str, set[str]] = {}
    for relation in model.get("relations", []):
        prerequisites.setdefault(relation["transition_id"], set()).add(relation["requires_transition_id"])

    configuration = {
        "model": copy.deepcopy(model),
        "scenario_id": scenario_id,
        "rule_profile": copy.deepcopy(profile),
        "initial_state": model["initial_state"],
        "exploration": copy.deepcopy(model["exploration"]),
        "engine_version": ENGINE_VERSION,
    }
    configuration_hash = sha256_json(configuration)
    current = model["initial_state"]
    history: list[str] = []
    steps: list[dict[str, Any]] = []
    blocked: dict[str, Any] | None = None
    for index, transition_id in enumerate(transition_ids, start=1):
        transition = transitions.get(transition_id)
        reason: str | None = None
        required_id: str | None = None
        if transition is None:
            reason = "unknown_transition"
        elif transition.condition is not None:
            reason = "condition_not_evaluated"
        elif transition_id in disabled:
            reason = "transition_disabled_by_scenario"
        elif transition.source != current:
            reason = "transition_source_mismatch"
        else:
            missing = sorted(prerequisites.get(transition_id, set()) - set(history))
            if missing:
                reason = "temporal_prerequisite_not_satisfied"
                required_id = missing[0]
        if reason:
            blocked = {"index": index, "transition_id": transition_id, "reason": reason}
            if required_id is not None:
                blocked["required_transition_id"] = required_id
            break
        assert transition is not None
        steps.append({
            "index": index,
            "transition_id": transition_id,
            "state_before": current,
            "state_after": transition.target,
        })
        current = transition.target
        history.append(transition_id)

    payload = {
        "configuration_sha256": configuration_hash,
        "scenario_id": scenario_id,
        "status": "BLOCKED" if blocked else "PASS",
        "steps": steps,
        "final_state": current,
        "blocked_step": blocked,
    }
    return {
        "execution_id": str(uuid.uuid4()),
        **payload,
        "configuration": configuration,
        "configuration_sha256": configuration_hash,
        "trace_sha256": sha256_json(payload),
    }


def run_model(model: dict[str, Any]) -> dict[str, Any]:
    """Validate and evaluate every declared scenario; return a reproducible result."""
    _, transitions = validate_model(model)
    scenarios = sorted(model["scenarios"], key=lambda item: item["id"])
    results = {s["id"]: _temporal_scenario_result(model, transitions, s) for s in scenarios}
    baseline = results["baseline"]
    comparisons: dict[str, Any] = {}
    for sid, result in results.items():
        if sid == "baseline":
            continue
        base_paths = {canonical_json(p) for p in baseline["trajectories"]}
        scenario_paths = {canonical_json(p) for p in result["trajectories"]}
        comparisons[sid] = {
            "intervention": {"disabled_transitions": result["disabled_transitions"]},
            "enabled_at_initial_added": sorted(set(result["enabled_transitions_at_initial_state"]) - set(baseline["enabled_transitions_at_initial_state"])),
            "enabled_at_initial_removed": sorted(set(baseline["enabled_transitions_at_initial_state"]) - set(result["enabled_transitions_at_initial_state"])),
            "reachable_states_added": sorted(set(result["reachable_states"]) - set(baseline["reachable_states"])),
            "reachable_states_removed": sorted(set(baseline["reachable_states"]) - set(result["reachable_states"])),
            "trajectories_added": [p for p in result["trajectories"] if canonical_json(p) not in base_paths],
            "trajectories_removed": [p for p in baseline["trajectories"] if canonical_json(p) not in scenario_paths],
            "truncated": baseline["truncated"] or result["truncated"],
        }
    # Keep the auditable baseline/intervention reachability delta in parity with the browser runtime.
    common_source = {
        "schema_version": model["schema_version"],
        "model_id": model["model_id"],
        "initial_state": model["initial_state"],
        "states": model["states"],
        "transitions": model["transitions"],
        "relations": model.get("relations", []),
        "rule_profile": model["rule_profile"],
        "exploration": model.get("exploration", {}),
    }
    baseline_scenario = next((item for item in model.get("scenarios", []) if item.get("id") == "baseline"), None)
    if baseline_scenario is None:
        raise ModelValidationError("Cannot calculate delta_reach without a baseline scenario")
    baseline_source_hash = sha256_json({**common_source, "scenario": baseline_scenario})
    delta_reach: dict[str, Any] = {}
    for sid in sorted(results):
        if sid == "baseline":
            continue
        scenario = next((item for item in model.get("scenarios", []) if item.get("id") == sid), None)
        if scenario is None:
            raise ModelValidationError(f"Cannot identify intervention source {sid}")
        intervention_source_hash = sha256_json({**common_source, "scenario": scenario})
        result = results[sid]
        comparison = comparisons[sid]
        delta_reach[sid] = {
            "baseline_source_sha256": baseline_source_hash,
            "intervention_source_sha256": intervention_source_hash,
            "reachable_states_added": comparison["reachable_states_added"],
            "reachable_states_removed": comparison["reachable_states_removed"],
            "enabled_at_initial_added": comparison["enabled_at_initial_added"],
            "enabled_at_initial_removed": comparison["enabled_at_initial_removed"],
            "trajectories_added": comparison["trajectories_added"],
            "trajectories_removed": comparison["trajectories_removed"],
            "truncated": bool(baseline["truncated"] or result["truncated"]),
            "baseline_truncated": bool(baseline["truncated"]),
            "intervention_truncated": bool(result["truncated"]),
        }
    output = {
        "engine_version": ENGINE_VERSION,
        "schema_version": model["schema_version"],
        "model_id": model["model_id"],
        "rule_profile": model["rule_profile"],
        "validation": "PASS",
        "scenario_results": results,
        "comparisons_to_baseline": comparisons,
        "scientific_interpretation": "NONE: synthetic model execution only; no empirical or TGCV validity claim.",
    }
    # Provenance hashes identify exact source serializations; they must not redefine
    # semantic result identity. Keep the legacy output shape when no intervention exists.
    if delta_reach:
        output["delta_reach"] = delta_reach
    # Semantic identity is separate from exact result integrity. Only the
    # versioned projection normalizes declared unordered dimensions.
    output["semantic_identity_version"] = SEMANTIC_IDENTITY_VERSION
    output["semantic_sha256"] = sha256_json(semantic_result_projection(output))
    return {
        **output,
        "input_sha256": sha256_json(model),
        "result_sha256": sha256_json(output),
    }


def export_run(model: dict[str, Any]) -> dict[str, Any]:
    """Package exact input plus result and their hashes for repeat execution."""
    result = run_model(model)
    package = {
        "package_version": "collective-toy-run-package-001",
        "engine_version": ENGINE_VERSION,
        "input": model,
        "result": result,
    }
    package["package_sha256"] = sha256_json(package)
    return package



def verify_exported_package_integrity(package: dict[str, Any]) -> bool:
    """Verify a known package format's hashes without claiming engine replay compatibility.

    This permits inspection of a package whose engine version is unavailable, while
    still rejecting unknown package formats and any integrity mismatch.
    """
    required = {"package_version", "engine_version", "input", "result", "package_sha256"}
    if not isinstance(package, dict) or not required.issubset(package):
        raise ModelValidationError("Exported package is missing required fields")
    if package["package_version"] != "collective-toy-run-package-001":
        raise ModelValidationError("Unsupported exported package version")
    if not isinstance(package["engine_version"], str) or not package["engine_version"]:
        raise ModelValidationError("Exported package engine_version must be a non-empty string")
    if not isinstance(package["input"], dict) or not isinstance(package["result"], dict):
        raise ModelValidationError("Exported package input and result must be objects")

    package_payload = dict(package)
    del package_payload["package_sha256"]
    if sha256_json(package_payload) != package["package_sha256"]:
        raise ModelValidationError("Exported package SHA-256 does not verify")

    result = package["result"]
    if not {"input_sha256", "result_sha256"}.issubset(result):
        raise ModelValidationError("Exported result is missing required hashes")
    if sha256_json(package["input"]) != result["input_sha256"]:
        raise ModelValidationError("Exported input SHA-256 does not verify")
    result_payload = dict(result)
    del result_payload["input_sha256"]
    expected_result_sha256 = result_payload.pop("result_sha256")
    if sha256_json(result_payload) != expected_result_sha256:
        raise ModelValidationError("Exported result SHA-256 does not verify")
    semantic_version = result.get("semantic_identity_version")
    if semantic_version is not None:
        if semantic_version != SEMANTIC_IDENTITY_VERSION:
            raise ModelValidationError("Unsupported semantic identity version")
        semantic_hash = result.get("semantic_sha256")
        if not isinstance(semantic_hash, str) or sha256_json(semantic_result_projection(result)) != semantic_hash:
            raise ModelValidationError("Exported semantic identity does not verify")
    elif "semantic_sha256" in result:
        raise ModelValidationError("semantic_sha256 requires a semantic identity version")
    return True


def assess_exported_package_integrity(package: dict[str, Any]) -> dict[str, Any]:
    """Return the integrity-only lifecycle state for a known, hash-valid package."""
    verify_exported_package_integrity(package)
    return {
        "status": "integrity-verified",
        "integrity_verified": True,
        "replay_verified": False,
        "reason": None,
    }


def assess_exported_package(package: dict[str, Any]) -> dict[str, Any]:
    """Return an explicit lifecycle status without conflating integrity and replay.

    Unknown package formats or integrity failures raise ModelValidationError.
    A known, intact package with an unavailable engine is inspect-only: its data
    may be inspected, but this function does not claim replay compatibility.
    """
    integrity = assess_exported_package_integrity(package)
    if package["engine_version"] != ENGINE_VERSION:
        return {
            "status": "inspect-only/replay-unavailable",
            "integrity_verified": integrity["integrity_verified"],
            "replay_verified": False,
            "reason": "Unsupported exported package engine version",
        }
    replayed = run_model(package["input"])
    exported = package["result"]
    if "semantic_identity_version" not in exported:
        # Legacy packages keep their original bytes and hashes. Compare only the
        # legacy result contract, omitting fields introduced by newer engines,
        # then independently recompute the legacy result hash.
        legacy_replay = dict(replayed)
        legacy_replay.pop("delta_reach", None)
        legacy_replay.pop("semantic_identity_version", None)
        legacy_replay.pop("semantic_sha256", None)
        legacy_replay.pop("input_sha256", None)
        legacy_replay.pop("result_sha256", None)
        legacy_replay["input_sha256"] = sha256_json(package["input"])
        legacy_replay["result_sha256"] = sha256_json({
            key: value for key, value in legacy_replay.items()
            if key != "input_sha256"
        })
        if legacy_replay != exported:
            raise ModelValidationError("Legacy exported result does not match compatible replay")
    elif replayed != exported:
        raise ModelValidationError("Exported result does not match independent replay")
    return {
        "status": "replay-verified",
        "integrity_verified": True,
        "replay_verified": True,
        "reason": None,
    }


def verify_exported_package(package: dict[str, Any]) -> bool:
    """Strict boolean verifier retained for callers requiring successful replay."""
    assessment = assess_exported_package(package)
    if assessment["status"] != "replay-verified":
        raise ModelValidationError(assessment["reason"] or "Exported package is not replay-verified")
    return True


def demo_model() -> dict[str, Any]:
    """The hand-checkable diamond fixture from the contract."""
    return {
        "schema_version": SUPPORTED_SCHEMA,
        "model_id": "toy-diamond-001",
        "initial_state": "A",
        "states": ["A", "B", "C", "D"],
        "transitions": [
            {"id": "t_ab", "source": "A", "target": "B"},
            {"id": "t_ac", "source": "A", "target": "C"},
            {"id": "t_bd", "source": "B", "target": "D"},
            {"id": "t_cd", "source": "C", "target": "D"},
        ],
        "relations": [],
        "rule_profile": {"type": "temporal_prerequisite_graph", "version": "1"},
        "scenarios": [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "block_ac", "disabled_transitions": ["t_ac"]},
        ],
        "exploration": {"max_depth": 4, "max_trajectories": 1000},
    }


if __name__ == "__main__":
    print(json.dumps(export_run(demo_model()), indent=2, ensure_ascii=False, sort_keys=True))
