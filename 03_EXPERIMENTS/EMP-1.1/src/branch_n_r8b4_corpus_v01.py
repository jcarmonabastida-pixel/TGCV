"""N-R8.4 controlled corpus construction primitives.

Prospective Branch N corpus construction only. No learner, outcome, or
scientific-result dependency. Full corpus generation is intentionally kept
outside module import and requires an explicit caller.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict
import hashlib
import json
import random
from typing import Iterable

from branch_n_r8_operationalisation_v01 import (
    COMPONENTS,
    FAMILIES,
    State,
    canonical_state,
    b_vector,
    low_order_r1,
    r2,
    tacc,
)
from branch_n_r_v02 import encode_r as encode_r_full

G2_SEED = 5_100_000
R8B_SEED = 5_200_000
R8C_SEED = 5_300_000
TRAIN_COUNT = 30_000
TEST_COUNT = 10_000
PAIR_TARGET = 5_000
R8B_PAIR_BUDGET = 2_000_000
R8C_PAIR_BUDGET = 5_000_000


def semantic_state_bytes(state: State) -> bytes:
    obj = {
        "components": list(state.components),
        "edges": [list(e) for e in state.edges],
        "objective": state.objective,
        "resources": list(state.resources),
    }
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def state_hash(state: State) -> str:
    return hashlib.sha256(semantic_state_bytes(state)).hexdigest()


def generate_g2(rng: random.Random) -> State:
    n = rng.choices((3, 4, 5), weights=(0.10, 0.30, 0.60), k=1)[0]
    comps = tuple(sorted(rng.sample(COMPONENTS, n), key=COMPONENTS.index))
    m = n * (n - 1)
    d = rng.choices((0.20, 0.50, 0.80), weights=(0.50, 0.30, 0.20), k=1)[0]
    edge_count = int(d * m + 0.5)
    edge_count = max(0, min(m, edge_count))
    possible = [(u, v) for u in comps for v in comps if u != v]
    edges = tuple(sorted(rng.sample(possible, edge_count), key=lambda e: (COMPONENTS.index(e[0]), COMPONENTS.index(e[1]))))
    resources = tuple(rng.choices((0, 1, 2, 3), weights=(0.10, 0.20, 0.30, 0.40), k=3))
    objectives = tuple(f"O{i:02d}" for i in range(1, 13))
    weights = (0.10,) * 6 + (1 / 15,) * 6
    objective = rng.choices(objectives, weights=weights, k=1)[0]
    return canonical_state(comps, edges, resources, objective)


def make_g2_corpus() -> tuple[list[dict], list[dict]]:
    rng = random.Random(G2_SEED)
    train, test = [], []
    for i in range(TRAIN_COUNT + TEST_COUNT):
        rec = {
            "episode_id": i if i < TRAIN_COUNT else i - TRAIN_COUNT,
            "snapshot": asdict(generate_g2(rng)),
        }
        (train if i < TRAIN_COUNT else test).append(rec)
    return train, test


def _state_from_record(rec: dict) -> State:
    s = rec["snapshot"] if "snapshot" in rec else rec["state"]
    return canonical_state(s["components"], [tuple(e) for e in s["edges"]], s["resources"], s["objective"])


def _b_key(state: State) -> tuple:
    return tuple(b_vector(state))


def _tacc_key(state: State) -> tuple:
    return tuple(tacc(state))


def _r_full(state: State) -> tuple[int, ...]:
    """Authoritative N-R1.3 v0.2 full R: exactly 58 dimensions."""
    return tuple(encode_r_full(state))


def _c_match_key(state: State) -> tuple:
    """Exact N-R8-C amended matching key before the full-R inequality test.

    The first 42 dimensions of the authoritative 58-vector are R1+R2+R3:
    six family-availability indicators, six family cardinalities, and thirty
    component-incidence features. N-R8-C then additionally fixes |T_acc|,
    family count, component count, resources, and objective. Graph edge count
    is deliberately not part of the key under N-R8.2.3.
    """
    ts = tacc(state)
    rr = _r_full(state)
    return (
        _b_key(state),
        tuple(rr[:6]),
        tuple(rr[6:12]),
        tuple(rr[12:42]),
        len(ts),
        sum(1 for x in rr[:6] if x),
        len(state.components),
        tuple(state.resources),
        state.objective,
    )


def build_matched_pairs_b(target: int = PAIR_TARGET, budget: int = R8B_PAIR_BUDGET) -> dict:
    rng = random.Random(R8B_SEED)
    buckets: dict[tuple, list[dict]] = defaultdict(list)
    pairs = []
    evaluations = generated = 0
    while len(pairs) < target and evaluations < budget:
        state = generate_g2(rng)
        rec = {"state": asdict(state), "state_hash": state_hash(state), "B": list(_b_key(state)), "T_acc": [list(t) for t in tacc(state)]}
        key = _b_key(state)
        for prior in buckets[key]:
            evaluations += 1
            if _tacc_key(_state_from_record(prior)) != _tacc_key(state):
                pairs.append({"pair_id": len(pairs), "A": prior, "B": rec})
                if len(pairs) >= target:
                    break
            if evaluations >= budget:
                break
        buckets[key].append(rec)
        generated += 1
    if len(pairs) < target:
        raise RuntimeError(f"N_R8B_TARGET_NOT_REACHED:{len(pairs)}/{target}:evaluations={evaluations}:generated={generated}")
    return {"seed": R8B_SEED, "target": target, "budget": budget, "evaluations": evaluations, "generated_states": generated, "pairs": pairs}


def build_matched_pairs_c(target: int = PAIR_TARGET, budget: int = R8C_PAIR_BUDGET) -> dict:
    rng = random.Random(R8C_SEED)
    buckets: dict[tuple, list[dict]] = defaultdict(list)
    pairs = []
    evaluations = generated = 0
    while len(pairs) < target and evaluations < budget:
        state = generate_g2(rng)
        rec = {"state": asdict(state), "state_hash": state_hash(state), "R": list(_r_full(state))}
        key = _c_match_key(state)
        for prior in buckets[key]:
            evaluations += 1
            prior_state = _state_from_record(prior)
            if _r_full(prior_state) != _r_full(state):
                pairs.append({"pair_id": len(pairs), "A": prior, "B": rec})
                if len(pairs) >= target:
                    break
            if evaluations >= budget:
                break
        buckets[key].append(rec)
        generated += 1
    if len(pairs) < target:
        raise RuntimeError(f"N_R8C_TARGET_NOT_REACHED:{len(pairs)}/{target}:evaluations={evaluations}:generated={generated}")
    return {"seed": R8C_SEED, "target": target, "budget": budget, "evaluations": evaluations, "generated_states": generated, "pairs": pairs}


def build_r2_records(records: Iterable[dict]) -> list[dict]:
    out = []
    for rec in records:
        state = _state_from_record(rec)
        out.append({
            "episode_id": rec["episode_id"],
            "initial_snapshot_sha256": state_hash(state),
            "R2": list(r2(state)),
        })
    return out


def verify_b_pairs(obj: dict) -> None:
    if len(obj["pairs"]) != obj["target"]:
        raise AssertionError("R8B_TARGET")
    for pair in obj["pairs"]:
        a, b = _state_from_record(pair["A"]), _state_from_record(pair["B"])
        if _b_key(a) != _b_key(b): raise AssertionError("R8B_B_MISMATCH")
        if _tacc_key(a) == _tacc_key(b): raise AssertionError("R8B_TACC_NOT_DIFFERENT")


def verify_c_pairs(obj: dict) -> None:
    if len(obj["pairs"]) != obj["target"]:
        raise AssertionError("R8C_TARGET")
    for pair in obj["pairs"]:
        a, b = _state_from_record(pair["A"]), _state_from_record(pair["B"])
        if _c_match_key(a) != _c_match_key(b): raise AssertionError("R8C_MATCH_KEY_MISMATCH")
        if _r_full(a) == _r_full(b): raise AssertionError("R8C_FULL_R_NOT_DIFFERENT")
