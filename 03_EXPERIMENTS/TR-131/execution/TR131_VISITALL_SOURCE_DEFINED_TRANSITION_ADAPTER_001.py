#!/usr/bin/env python3
"""TR-131 VisitAll source-defined transition adapter.

Deterministic adapter for the pinned VisitAll PDDL semantics.
No planner search, goal selection, optimization, or TGCV-specific
transition semantics are implemented here.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Move:
    cur: str
    nxt: str

    @property
    def identity(self) -> str:
        return f"move:{self.cur}->{self.nxt}"


def applicable_moves(state: dict, connected: set[tuple[str, str]]) -> tuple[Move, ...]:
    cur = state["at-robot"]
    moves = [
        Move(cur, nxt)
        for a, nxt in sorted(connected)
        if a == cur
    ]
    return tuple(moves)


def apply_move(
    state: dict,
    action: Move,
    connected: set[tuple[str, str]],
) -> dict:
    if (action.cur, action.nxt) not in connected:
        raise ValueError("selected move is not source-defined connected")
    if state["at-robot"] != action.cur:
        raise ValueError("selected move violates at-robot precondition")

    if action not in applicable_moves(state, connected):
        raise ValueError("selected move is not in T_acc")

    out = dict(state)
    out["at-robot"] = action.nxt
    out["visited"] = sorted(set(state.get("visited", ())) | {action.nxt})
    return out


def transition_record(
    state: dict,
    action: Move,
    connected: set[tuple[str, str]],
) -> tuple[dict, dict]:
    t_acc = applicable_moves(state, connected)
    if action not in t_acc:
        raise ValueError("T_real must belong to T_acc")

    successor = apply_move(state, action, connected)
    record = {
        "S_t": state,
        "T_acc_t": [m.identity for m in t_acc],
        "T_real_t": action.identity,
        "S_t1": successor,
    }
    return successor, record
