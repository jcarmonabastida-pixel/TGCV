def G_S(state_a, state_b, representation):
    if representation == "S_raw":
        return sorted(state_a.get("initial_state", [])) == sorted(state_b.get("initial_state", []))
    if representation == "S_typed":
        return sorted(tuple(x) for x in state_a.get("initial_state", [])) == sorted(tuple(x) for x in state_b.get("initial_state", []))
    if representation == "S_predicate_multiset":
        from collections import Counter
        return Counter(x[0] for x in state_a.get("initial_state", [])) == Counter(x[0] for x in state_b.get("initial_state", []))
    if representation == "S_object_inventory":
        return {k:len(v) for k,v in state_a.get("objects",{}).items()} == {k:len(v) for k,v in state_b.get("objects",{}).items()}
    return "NON_COMPARABLE"
