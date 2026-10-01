def gs(sa, sb, representation):
    if representation=="S_raw":
        a=set(map(tuple,sa["predicates"])); b=set(map(tuple,sb["predicates"]))
    elif representation=="S_typed":
        a={tuple(x) for x in sa["predicates"]}; b={tuple(x) for x in sb["predicates"]}
    elif representation=="S_predicate_multiset":
        from collections import Counter
        a=Counter(x[0] for x in sa["predicates"]); b=Counter(x[0] for x in sb["predicates"])
    elif representation=="S_object_inventory":
        a={k:len(v) for k,v in sa["objects"].items()}; b={k:len(v) for k,v in sb["objects"].items()}
    else:
        return "NON_COMPARABLE"
    return "NO_STRUCTURAL_CHANGE" if a==b else "STRUCTURAL_CHANGE"
