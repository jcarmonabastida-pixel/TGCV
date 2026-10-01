def G_S(state_a, state_b, representation):
    if representation == "S_raw":
        same = sorted(state_a.get("initial_state", [])) == sorted(state_b.get("initial_state", []))
    elif representation == "S_typed":
        same = sorted(tuple(x) for x in state_a.get("initial_state", [])) == sorted(tuple(x) for x in state_b.get("initial_state", []))
    elif representation == "S_predicate_multiset":
        from collections import Counter
        same = Counter(x[0] for x in state_a.get("initial_state", [])) == Counter(x[0] for x in state_b.get("initial_state", []))
    elif representation == "S_object_inventory":
        same = {k: len(v) for k, v in state_a.get("objects", {}).items()} == {k: len(v) for k, v in state_b.get("objects", {}).items()}
    else:
        return "NON_COMPARABLE"
    return "NO_STRUCTURAL_CHANGE" if same else "STRUCTURAL_CHANGE"
