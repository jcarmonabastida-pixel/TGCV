"""TR-181E minimal R engine.

STATUS: REVISED CANDIDATE / NOT FROZEN.
Canonical representation is the accessibility set/cardinality. Derived
summary statistics are intentionally excluded from canonical R until
separately justified.
"""


def candidate_accessible(snapshot, candidate):
    """Evaluate only pre-declared, pre-outcome predicates."""
    if not candidate.get("target"):
        raise ValueError("candidate target is required")
    for p in candidate.get("pre", []):
        kind = p.get("kind")
        if kind == "component_exists":
            if p["value"] not in snapshot["components"]:
                return False
        elif kind == "resource_min":
            if snapshot["resources"].get(p["name"], float("-inf")) < p["value"]:
                return False
        elif kind == "component_pair":
            if not set(p["value"]).issubset(set(snapshot["components"])):
                return False
        else:
            raise ValueError(f"non-canonical or unknown predicate: {kind}")
    return True


def accessible_transformations(snapshot, candidates):
    if not isinstance(snapshot, dict):
        raise TypeError("snapshot must be a mapping")
    if not isinstance(candidates, list):
        raise TypeError("candidates must be a list")
    return sorted((c for c in candidates if candidate_accessible(snapshot, c)),
                  key=lambda c: str(c.get("id", "")))


def compute_r(snapshot, candidates):
    """Return canonical R: the deterministic accessible-transformation set."""
    if not isinstance(snapshot, dict):
        raise TypeError("snapshot must be a mapping")
    required = {"components", "resources"}
    missing = required.difference(snapshot)
    if missing:
        raise ValueError(f"missing snapshot fields: {sorted(missing)}")
    acc = accessible_transformations(snapshot, candidates)
    ids = tuple(str(c["id"]) for c in acc)
    return {"accessible_ids": ids, "cardinality": len(ids)}
