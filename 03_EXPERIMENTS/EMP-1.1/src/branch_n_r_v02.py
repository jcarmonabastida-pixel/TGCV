"""Branch N controlled reconstruction: transformation universe and R v0.2.

This module is a prospective reconstruction, NOT historical EMP-1.1 code.
It implements N-R1.2 and N-R1.3 v0.2 exactly and contains no learner,
training, outcome, or confirmatory-experiment logic.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from typing import Iterable, Tuple

COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")
FAMILIES = (
    "ADD_COMPONENT",
    "REMOVE_COMPONENT",
    "ADD_EDGE",
    "REMOVE_EDGE",
    "REWIRE_EDGE",
    "MODIFY_RESOURCE",
)
RESOURCE_VALUES = (0, 1, 2, 3)
OBJECTIVES = tuple(f"O{i:02d}" for i in range(1, 13))


@dataclass(frozen=True, order=True)
class State:
    """Canonical snapshot S=(V,E,q,o)."""
    components: Tuple[str, ...]
    edges: Tuple[Tuple[str, str], ...]
    resources: Tuple[int, int, int]
    objective: str

    def __post_init__(self) -> None:
        comps = tuple(sorted(set(self.components), key=COMPONENTS.index))
        if comps != self.components:
            raise ValueError("NON_CANONICAL_COMPONENT_ORDER")
        if not comps or len(comps) > 6 or any(c not in COMPONENTS for c in comps):
            raise ValueError("INVALID_COMPONENT_SET")
        if len(self.resources) != 3 or any(q not in RESOURCE_VALUES for q in self.resources):
            raise ValueError("INVALID_RESOURCE_VECTOR")
        if self.objective not in OBJECTIVES:
            raise ValueError("INVALID_OBJECTIVE")
        edge_set = set(self.edges)
        if len(edge_set) != len(self.edges):
            raise ValueError("DUPLICATE_EDGE")
        rank = {c: i for i, c in enumerate(COMPONENTS)}
        canonical_edges = tuple(sorted(edge_set, key=lambda e: (rank[e[0]], rank[e[1]])))
        if canonical_edges != self.edges:
            raise ValueError("NON_CANONICAL_EDGE_ORDER")
        if any(u == v or u not in comps or v not in comps for u, v in self.edges):
            raise ValueError("INVALID_EDGE")

    @staticmethod
    def make(components: Iterable[str], edges: Iterable[Tuple[str, str]],
             resources: Iterable[int], objective: str) -> "State":
        rank = {c: i for i, c in enumerate(COMPONENTS)}
        comps = tuple(sorted(set(components), key=lambda c: rank[c]))
        edge_set = set(edges)
        edges_c = tuple(sorted(edge_set, key=lambda e: (rank[e[0]], rank[e[1]])))
        return State(comps, edges_c, tuple(resources), objective)


def _replace_component_tuple(items: Iterable[str], remove: str | None = None,
                              add: str | None = None) -> Tuple[str, ...]:
    s = set(items)
    if remove is not None:
        s.remove(remove)
    if add is not None:
        s.add(add)
    return tuple(sorted(s, key=COMPONENTS.index))


def enumerate_transformations(state: State) -> Tuple[tuple, ...]:
    """Return complete deterministic T_acc under N-R1.2."""
    out: list[tuple] = []
    V = set(state.components)
    E = set(state.edges)

    # ADD_COMPONENT(v)
    if len(V) < 6:
        for v in COMPONENTS:
            if v not in V:
                out.append(("ADD_COMPONENT", v))

    # REMOVE_COMPONENT(v)
    if len(V) > 1:
        for v in state.components:
            out.append(("REMOVE_COMPONENT", v))

    # ADD_EDGE(u,v)
    for u, v in permutations(state.components, 2):
        if (u, v) not in E:
            out.append(("ADD_EDGE", u, v))

    # REMOVE_EDGE(u,v)
    for u, v in state.edges:
        out.append(("REMOVE_EDGE", u, v))

    # REWIRE_EDGE(u,v,w): preserve source u, replace target v by w.
    for u, v in state.edges:
        for w in state.components:
            if v != w and u != w and (u, w) not in E:
                out.append(("REWIRE_EDGE", u, v, w))

    # MODIFY_RESOURCE(i,d), i is 1-based; d is -1 or +1.
    for i, q in enumerate(state.resources, start=1):
        for d in (-1, +1):
            if q + d in RESOURCE_VALUES:
                out.append(("MODIFY_RESOURCE", i, d))

    family_rank = {f: i for i, f in enumerate(FAMILIES)}
    comp_rank = {c: i for i, c in enumerate(COMPONENTS)}

    def key(t: tuple):
        f = t[0]
        params = t[1:]
        converted = []
        for p in params:
            if isinstance(p, str):
                converted.append((0, comp_rank[p]))
            else:
                converted.append((1, p))
        return (family_rank[f], tuple(converted))

    return tuple(sorted(out, key=key))


def apply_transformation(state: State, tau: tuple) -> State:
    """Apply one valid Branch N transformation deterministically."""
    f = tau[0]
    V = set(state.components)
    E = set(state.edges)
    q = list(state.resources)

    if f == "ADD_COMPONENT":
        _, v = tau
        if v in V or len(V) >= 6:
            raise ValueError("INVALID_ADD_COMPONENT")
        return State.make(V | {v}, E, q, state.objective)

    if f == "REMOVE_COMPONENT":
        _, v = tau
        if v not in V or len(V) <= 1:
            raise ValueError("INVALID_REMOVE_COMPONENT")
        V.remove(v)
        E = {(u, w) for u, w in E if u != v and w != v}
        return State.make(V, E, q, state.objective)

    if f == "ADD_EDGE":
        _, u, v = tau
        if u not in V or v not in V or u == v or (u, v) in E:
            raise ValueError("INVALID_ADD_EDGE")
        E.add((u, v))
        return State.make(V, E, q, state.objective)

    if f == "REMOVE_EDGE":
        _, u, v = tau
        if (u, v) not in E:
            raise ValueError("INVALID_REMOVE_EDGE")
        E.remove((u, v))
        return State.make(V, E, q, state.objective)

    if f == "REWIRE_EDGE":
        _, u, v, w = tau
        if (u, v) not in E or u not in V or w not in V or v == w or u == w or (u, w) in E:
            raise ValueError("INVALID_REWIRE_EDGE")
        E.remove((u, v))
        E.add((u, w))
        return State.make(V, E, q, state.objective)

    if f == "MODIFY_RESOURCE":
        _, i, d = tau
        if i not in (1, 2, 3) or d not in (-1, +1):
            raise ValueError("INVALID_MODIFY_RESOURCE")
        q[i - 1] += d
        if q[i - 1] not in RESOURCE_VALUES:
            raise ValueError("RESOURCE_OUT_OF_RANGE")
        return State.make(V, E, q, state.objective)

    raise ValueError("UNKNOWN_FAMILY")


def _family(tau: tuple) -> str:
    return tau[0]


def encode_r(state: State, t_acc: Tuple[tuple, ...] | None = None) -> Tuple[int, ...]:
    """Encode exactly the 58 N-R1.3 v0.2 features."""
    if t_acc is None:
        t_acc = enumerate_transformations(state)

    # R1/R2
    counts = {f: 0 for f in FAMILIES}
    for tau in t_acc:
        if _family(tau) not in counts:
            raise ValueError("UNKNOWN_TRANSFORMATION_FAMILY")
        counts[_family(tau)] += 1
    r1 = tuple(int(counts[f] > 0) for f in FAMILIES)
    r2 = tuple(counts[f] for f in FAMILIES)

    # v0.2: empty T_acc is exactly 58 zeros.
    if not t_acc:
        return (0,) * 58

    # R3: five incidence summaries per canonical component.
    r3: list[int] = []
    for v in COMPONENTS:
        add_c = sum(1 for t in t_acc if t[0] == "ADD_COMPONENT" and t[1] == v)
        rem_c = sum(1 for t in t_acc if t[0] == "REMOVE_COMPONENT" and t[1] == v)
        add_e = sum(1 for t in t_acc if t[0] == "ADD_EDGE" and v in (t[1], t[2]))
        rem_e = sum(1 for t in t_acc if t[0] == "REMOVE_EDGE" and v in (t[1], t[2]))
        rew = sum(1 for t in t_acc if t[0] == "REWIRE_EDGE" and v in (t[1], t[2], t[3]))
        r3.extend((add_c, rem_c, add_e, rem_e, rew))

    # R4
    successors = tuple(apply_transformation(state, t) for t in t_acc)
    n_delta_components_add = sum(1 for t in t_acc if t[0] == "ADD_COMPONENT")
    n_delta_components_remove = sum(1 for t in t_acc if t[0] == "REMOVE_COMPONENT")
    n_delta_edges_add = sum(1 for t in t_acc if t[0] == "ADD_EDGE")
    n_delta_edges_remove = sum(1 for t in t_acc if t[0] == "REMOVE_EDGE")
    n_delta_edges_rewire = sum(1 for t in t_acc if t[0] == "REWIRE_EDGE")
    n_delta_resources_up = sum(1 for t in t_acc if t[0] == "MODIFY_RESOURCE" and t[2] == +1)
    n_delta_resources_down = sum(1 for t in t_acc if t[0] == "MODIFY_RESOURCE" and t[2] == -1)
    n_noop = sum(1 for s2 in successors if s2 == state)

    next_component_counts = tuple(len(s.components) for s in successors)
    next_edge_counts = tuple(len(s.edges) for s in successors)
    next_resource_vectors = tuple(s.resources for s in successors)
    next_states = tuple((s.components, s.edges, s.resources, s.objective) for s in successors)

    r4 = (
        n_delta_components_add,
        n_delta_components_remove,
        n_delta_edges_add,
        n_delta_edges_remove,
        n_delta_edges_rewire,
        n_delta_resources_up,
        n_delta_resources_down,
        n_noop,
        len(set(next_component_counts)),
        len(set(next_edge_counts)),
        len(set(next_resource_vectors)),
        len(set(next_states)),
        max(next_component_counts),
        min(next_component_counts),
        max(next_edge_counts),
        min(next_edge_counts),
    )
    r = tuple(r1 + r2 + tuple(r3) + r4)
    if len(r) != 58:
        raise AssertionError("R_DIMENSION_NOT_58")
    return r


def canonical_serialization(r: Tuple[int, ...]) -> bytes:
    if len(r) != 58 or any(not isinstance(x, int) or x < 0 for x in r):
        raise ValueError("INVALID_R_VECTOR")
    return ("[" + ",".join(str(x) for x in r) + "]\n").encode("ascii")
