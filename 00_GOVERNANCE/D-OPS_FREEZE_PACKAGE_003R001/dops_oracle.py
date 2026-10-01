import json

def _canon(value):
    if isinstance(value, dict):
        return {k: _canon(value[k]) for k in sorted(value)}
    if isinstance(value, list):
        values = [_canon(v) for v in value]
        return sorted(values, key=lambda v: json.dumps(v, sort_keys=True, separators=(",", ":")))
    return value

def oracle_canonicalize(fixture, r3):
    """Independent oracle-side canonicalization; does not import the SUT."""
    U = [t["id"] for t in fixture["transformations"]]
    R1 = []
    R2 = []
    for t in fixture["transformations"]:
        tid = t["id"]
        for p in t["preconditions"]:
            R1.append([tid, p])
        for a in t["add_effects"]:
            R2.append([tid, "ADD", a])
        for d in t["delete_effects"]:
            R2.append([tid, "DELETE", d])
    return {
        "U": sorted(U),
        "equivalence": [],
        "R1": _canon(R1),
        "R2": _canon(R2),
        "R3": sorted([list(edge) for edge in r3["edges"]], key=lambda e: json.dumps(e, separators=(",", ":"))),
    }

def classify(old, new):
    if old is None or new is None:
        return "NON_COMPARABLE"
    au = set(new["U"]) - set(old["U"])
    ru = set(old["U"]) - set(new["U"])
    if au and not ru:
        return "EXPANSION"
    if ru and not au:
        return "CONTRACTION"
    if au and ru:
        return "OTHER_STRUCTURAL_CHANGE"
    if all(old[k] == new[k] for k in ("equivalence", "R1", "R2", "R3")):
        return "PERSISTENCE"
    dr3_old = set(map(tuple, old["R3"]))
    dr3_new = set(map(tuple, new["R3"]))
    if (
        old["equivalence"] == new["equivalence"]
        and old["R1"] == new["R1"]
        and old["R2"] == new["R2"]
        and len(dr3_old - dr3_new) == 1
        and len(dr3_new - dr3_old) == 1
    ):
        return "RECONFIGURATION_ONLY"
    return "OTHER_STRUCTURAL_CHANGE"

def expected():
    return {
        "persistence": "PERSISTENCE",
        "expansion": "EXPANSION",
        "contraction": "CONTRACTION",
        "reconfiguration": "RECONFIGURATION_ONLY",
        "mixed_identity_change": "OTHER_STRUCTURAL_CHANGE",
    }
