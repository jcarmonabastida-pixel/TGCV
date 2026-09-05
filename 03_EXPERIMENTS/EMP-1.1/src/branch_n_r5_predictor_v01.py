"""Prospective Branch N predictor representation B/R.

Implements N-R5.1 only. No learner, outcome, trajectory, or network access.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import hashlib
import json
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
R_PATH = ROOT / "branch_n_r_v02.py"
spec = importlib.util.spec_from_file_location("branch_n_r_v02", R_PATH)
rmod = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(rmod)
State = rmod.State
encode_r = rmod.encode_r
OBJECTIVES = rmod.OBJECTIVES

@dataclass(frozen=True)
class Predictor:
    episode_id: int
    initial_snapshot_sha256: str
    B: tuple[int, ...]
    R: tuple[int, ...]
    BR: tuple[int, ...]


def state_from_snapshot(rec: dict[str, Any]) -> State:
    return State.make(rec["components"], [tuple(e) for e in rec["edges"]], rec["resources"], rec["objective"])


def encode_b(rec: dict[str, Any]) -> tuple[int, ...]:
    if rec["objective"] not in OBJECTIVES:
        raise ValueError("INVALID_OBJECTIVE")
    one_hot = tuple(int(rec["objective"] == o) for o in OBJECTIVES)
    return (len(rec["components"]), *tuple(rec["resources"]), *one_hot)


def canonical_snapshot_bytes(rec: dict[str, Any]) -> bytes:
    return (json.dumps(rec, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def snapshot_sha256(rec: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_snapshot_bytes(rec)).hexdigest()


def encode_predictor(rec: dict[str, Any]) -> Predictor:
    state = state_from_snapshot(rec)
    b = encode_b(rec)
    r = encode_r(state)
    br = b + r
    if len(b) != 16 or len(r) != 58 or len(br) != 74:
        raise AssertionError("PREDICTOR_DIMENSION_ERROR")
    return Predictor(rec["episode_id"], snapshot_sha256(rec), b, r, br)


def canonical_predictor_bytes(p: Predictor) -> bytes:
    obj = {"episode_id": p.episode_id, "initial_snapshot_sha256": p.initial_snapshot_sha256,
           "B": list(p.B), "R": list(p.R), "BR": list(p.BR)}
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")
