"""N-R8-C2 vNext frozen matching key.

Pure state-derived implementation of the frozen C2-vNext key.
It MUST NOT inspect T_acc, R, O_T, transformations, or transformation-derived statistics.
"""
from __future__ import annotations

from branch_n_r8_operationalisation_v01 import State, b_vector


def degree_multiset(state: State) -> tuple[int, ...]:
    """Return sorted total degree (in + out) for every component."""
    indegree = {component: 0 for component in state.components}
    outdegree = {component: 0 for component in state.components}
    for source, target in state.edges:
        outdegree[source] += 1
        indegree[target] += 1
    return tuple(sorted(indegree[c] + outdegree[c] for c in state.components))


def c2_vnext_key(state: State) -> tuple:
    """Frozen K_C2_vNext = B + degree-multiset(V)."""
    return (b_vector(state), degree_multiset(state))
