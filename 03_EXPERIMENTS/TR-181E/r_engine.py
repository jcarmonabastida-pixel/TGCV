"""TR-181E candidate R engine.

Design status: RECONSTRUCTED / NOT FROZEN.
This module is intentionally conservative: it computes accessibility from
explicit candidate records and a pre-outcome snapshot; it never consumes
trajectory or outcome fields.
"""

from collections import Counter
from math import log

CLASSES = (
    "ACTIVATE", "COMPOSE", "RECONFIGURE",
    "ACQUIRE", "LEARN", "RECOMBINE",
)


def _has(snapshot, key, value):
    return snapshot.get(key) == value


def candidate_accessible(snapshot, candidate):
    """Evaluate a fully explicit candidate against a snapshot.

    A candidate must declare a target and a list of boolean preconditions.
    Preconditions use the small predicate vocabulary below so that the
    operationalisation remains auditable and deterministic.
    """
    target = candidate.get("target")
    if not target:
        raise ValueError("candidate target is required")

    for predicate in candidate.get("pre", []):
        kind = predicate.get("kind")
        if kind == "component_exists":
            if predicate["value"] not in snapshot.get("components", []):
                return False
        elif kind == "resource_min":
            resources = snapshot.get("resources", {})
            if resources.get(predicate["name"], float("-inf")) < predicate["value"]:
                return False
        elif kind == "objective_is":
            if not _has(snapshot, "objective", predicate["value"]):
                return False
        elif kind == "flag_is":
            if not _has(snapshot, predicate["name"], predicate["value"]):
                return False
        elif kind == "component_pair":
            pair = predicate["value"]
            components = set(snapshot.get("components", []))
            if not set(pair).issubset(components):
                return False
        else:
            raise ValueError(f"unknown predicate kind: {kind}")
    return True


def accessible_transformations(snapshot, candidates):
    """Return deterministically ordered accessible candidates."""
    if not isinstance(snapshot, dict):
        raise TypeError("snapshot must be a mapping")
    if not isinstance(candidates, list):
        raise TypeError("candidates must be a list")
    if "outcome" in snapshot or "trajectory" in snapshot:
        # These fields may exist in sealed episode records, but the engine
        # deliberately ignores them. They are not read by any predicate.
        pass
    accessible = [c for c in candidates if candidate_accessible(snapshot, c)]
    return sorted(accessible, key=lambda c: str(c.get("id", "")))


def compute_r(snapshot, candidates):
    """Compute the candidate R vector from pre-outcome snapshot data."""
    if not isinstance(snapshot, dict):
        raise TypeError("snapshot must be a mapping")
    required = {"components", "resources", "objective"}
    missing = required.difference(snapshot)
    if missing:
        raise ValueError(f"missing snapshot fields: {sorted(missing)}")

    acc = accessible_transformations(snapshot, candidates)
    counts = Counter(c.get("type") for c in acc)
    type_counts = [counts.get(t, 0) for t in CLASSES]
    total = len(acc)

    nonzero = [n for n in type_counts if n]
    entropy = 0.0
    if total:
        entropy = -sum((n / total) * log(n / total) for n in nonzero)

    affected_components = set()
    affected_resources = set()
    for c in acc:
        target = c.get("target")
        if isinstance(target, list):
            affected_components.update(target)
        elif target is not None:
            affected_components.add(target)
        for r in c.get("resources", []):
            affected_resources.add(r)

    incidence = (total / len(affected_components)) if affected_components else 0.0

    return {
        "total_accessible": total,
        "type_counts": type_counts,
        "type_entropy": entropy,
        "affected_components": len(affected_components),
        "affected_resource_types": len(affected_resources),
        "candidate_component_incidence": incidence,
    }
