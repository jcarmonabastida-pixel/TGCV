"""Synthetic-only TGCV Collective Toy engine, profile 1.

This module implements a finite directed transition system. Relations are
descriptive metadata only; they have no execution semantics in profile 1.
It does not implement TGCV T_acc, value, causality, or empirical inference.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import hashlib
import json
from typing import Any


ENGINE_VERSION = "collective-toy-engine-001"
SUPPORTED_SCHEMA = "collective-toy-input-001"


class ModelValidationError(ValueError):
    """Raised when a model or scenario violates the input contract."""


def _reject_unknown_keys(value: dict[str, Any], allowed: set[str], context: str) -> None:
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise ModelValidationError(f"{context} contains unknown fields: {unknown}")


def canonical_json(value: Any) -> str:
    """Serialize JSON-compatible values deterministically for this engine."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Transition:
    id: str
    source: str
    target: str


def validate_model(model: dict[str, Any]) -> tuple[dict[str, str], dict[str, Transition]]:
    if not isinstance(model, dict):
        raise ModelValidationError("model must be a JSON object")
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
    if model.get("initial_state") not in set(states):
        raise ModelValidationError("initial_state must reference a declared state")

    profile = model.get("rule_profile")
    profile1 = {"type": "finite_deterministic_graph", "version": "1"}
    profile2 = {"type": "relation_guarded_graph", "version": "1"}
    if not isinstance(profile, dict):
        raise ModelValidationError("rule_profile must be an object")
    _reject_unknown_keys(profile, {"type", "version"}, "rule_profile")
    if profile not in (profile1, profile2):
        raise ModelValidationError("unsupported rule_profile; expected finite_deterministic_graph v1 or relation_guarded_graph v1")

    raw_transitions = model.get("transitions")
    if not isinstance(raw_transitions, list):
        raise ModelValidationError("transitions must be a list")
    transitions: dict[str, Transition] = {}
    for item in raw_transitions:
        if not isinstance(item, dict):
            raise ModelValidationError("each transition must be an object")
        _reject_unknown_keys(item, {"id", "source", "target"}, "transition")
        tid, source, target = item.get("id"), item.get("source"), item.get("target")
        if any(not isinstance(x, str) or not x for x in (tid, source, target)):
            raise ModelValidationError("transition id, source, and target must be non-empty strings")
        if tid in transitions:
            raise ModelValidationError(f"duplicate transition ID: {tid}")
        if source not in states or target not in states:
            raise ModelValidationError(f"transition {tid} references an unknown state")
        transitions[tid] = Transition(tid, source, target)

    relations = model.get("relations", [])
    if not isinstance(relations, list):
        raise ModelValidationError("relations must be a list")
    if profile == profile1:
        # Profile 1 preserves relations as inert descriptive metadata.
        pass
    else:
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
            if rtype != "requires_transition_enabled":
                raise ModelValidationError(f"unsupported relation type: {rtype!r}")
            if not isinstance(guarded, str) or not guarded or not isinstance(prerequisite, str) or not prerequisite:
                raise ModelValidationError("relation_guarded_graph relations require transition_id and requires_transition_id")
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


def _scenario_result(
    model: dict[str, Any], transitions: dict[str, Transition], scenario: dict[str, Any]
) -> dict[str, Any]:
    explicit_disabled = set(scenario.get("disabled_transitions", []))
    disabled = set(explicit_disabled)
    relation_effects: list[dict[str, str]] = []
    if model["rule_profile"] == {"type": "relation_guarded_graph", "version": "1"}:
        for relation in sorted(model.get("relations", []), key=lambda item: item["id"]):
            blocked = relation["requires_transition_id"] in explicit_disabled
            relation_effects.append({
                "relation_id": relation["id"],
                "type": relation["type"],
                "transition_id": relation["transition_id"],
                "requires_transition_id": relation["requires_transition_id"],
                "status": "BLOCKED" if blocked else "APPLIED",
                "reason": "prerequisite_transition_disabled" if blocked else "prerequisite_transition_not_disabled",
            })
            if blocked:
                disabled.add(relation["transition_id"])
    max_depth = model["exploration"]["max_depth"]
    max_trajectories = model["exploration"]["max_trajectories"]
    initial = model["initial_state"]
    adjacency: dict[str, list[Transition]] = {s: [] for s in model["states"]}
    for t in transitions.values():
        if t.id not in disabled:
            adjacency[t.source].append(t)
    for outgoing in adjacency.values():
        outgoing.sort(key=lambda t: t.id)

    # Reachability is graph search; cycles do not cause non-termination.
    reached = {initial}
    queue = deque([initial])
    while queue:
        state = queue.popleft()
        for transition in adjacency[state]:
            if transition.target not in reached:
                reached.add(transition.target)
                queue.append(transition.target)

    # Enumerate bounded finite walks, recording terminal paths and depth-limited paths; max_depth counts edges.
    trajectories: list[list[dict[str, str]]] = []
    truncated = False
    stack: list[tuple[str, list[dict[str, str]], int]] = [
        (initial, [{"state": initial}], 0)
    ]
    while stack:
        state, path, depth = stack.pop()
        if depth >= max_depth:
            if adjacency[state]:
                truncated = True
            if len(trajectories) < max_trajectories:
                trajectories.append(path)
            else:
                truncated = True
                break
            continue
        outgoing = adjacency[state]
        if not outgoing:
            if len(trajectories) < max_trajectories:
                trajectories.append(path)
            else:
                truncated = True
                break
            continue
        # Reverse push to make the resulting DFS lexicographic by transition ID.
        for transition in reversed(outgoing):
            next_path = path + [{"transition": transition.id, "state": transition.target}]
            stack.append((transition.target, next_path, depth + 1))
        # If pending work exceeds the output limit, stop only when output cap is hit.
        if len(trajectories) >= max_trajectories and stack:
            truncated = True
            break

    # Current-state enabled set is local and is not TGCV's system-level T_acc.
    enabled_at_initial = sorted(t.id for t in adjacency[initial])
    result = {
        "scenario_id": scenario["id"],
        "disabled_transitions": sorted(explicit_disabled),
        "enabled_transitions_at_initial_state": enabled_at_initial,
        "reachable_states": sorted(reached),
        "trajectories": trajectories,
        "truncated": truncated,
        "exploration_bounds": {"max_depth": max_depth, "max_trajectories": max_trajectories},
    }
    if model["rule_profile"] == {"type": "relation_guarded_graph", "version": "1"}:
        result["relation_effects"] = relation_effects
        result["effective_disabled_transitions"] = sorted(disabled)
    return result


def run_model(model: dict[str, Any]) -> dict[str, Any]:
    """Validate and evaluate every declared scenario; return a reproducible result."""
    _, transitions = validate_model(model)
    scenarios = sorted(model["scenarios"], key=lambda item: item["id"])
    results = {s["id"]: _scenario_result(model, transitions, s) for s in scenarios}
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
        "rule_profile": {"type": "finite_deterministic_graph", "version": "1"},
        "scenarios": [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "block_ac", "disabled_transitions": ["t_ac"]},
        ],
        "exploration": {"max_depth": 4, "max_trajectories": 1000},
    }


if __name__ == "__main__":
    print(json.dumps(export_run(demo_model()), indent=2, ensure_ascii=False, sort_keys=True))
