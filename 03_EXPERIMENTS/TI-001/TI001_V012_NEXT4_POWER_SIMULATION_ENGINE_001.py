"""NEXT4 design-stage Monte Carlo engine.

No provider calls. No scientific fixture. Synthetic responses only.
The engine implements a deterministic four-action multinomial-style choice
generator and records the mapping-alignment ground truth.

This is an implementation component, not an execution authorization.
"""

from __future__ import annotations
from dataclasses import dataclass
import hashlib
import json
import math
import random
from itertools import permutations
from typing import Any

ACTIONS = (0, 1, 2, 3)
PROFILES = (0, 1, 2, 3)
DOMAINS = (0, 1, 2)
OPS = (0, 1)
PRESENTATIONS = (0, 1, 2, 3)
CONDITIONS = ("STATIC_CONTROL", "FUTURE_REASSIGNED",
              "SURFACE_CONTROL", "UNINFORMATIVE_NULL")
PERMUTATIONS = tuple(permutations(ACTIONS))


@dataclass(frozen=True)
class SimulationScenario:
    effect_label: str
    effect_size: float
    n_units: int
    replicate: int
    seed: int


def stable_seed(master_seed: int, effect_label: str, n_units: int, replicate: int) -> int:
    raw = f"{master_seed}|{effect_label}|{n_units}|{replicate}".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    ex = [math.exp(x - m) for x in logits]
    s = sum(ex)
    return [x / s for x in ex]


def mapping_signal(permutation: tuple[int, ...], profile: int, future: int) -> int:
    if sorted(permutation) != list(ACTIONS):
        raise ValueError("Invalid permutation")
    return int(permutation[profile] == future)


def choose(probs: list[float], rng: random.Random) -> int:
    u = rng.random()
    c = 0.0
    for i, p in enumerate(probs):
        c += p
        if u <= c:
            return i
    return len(probs) - 1


def generate_unit(s: SimulationScenario, unit_id: int) -> dict[str, Any]:
    rng = random.Random(stable_seed(s.seed, s.effect_label, s.n_units, unit_id))

    domain = unit_id % len(DOMAINS)
    op = (unit_id // len(DOMAINS)) % len(OPS)
    presentation = (unit_id // (len(DOMAINS) * len(OPS))) % len(PRESENTATIONS)
    permutation = PERMUTATIONS[unit_id % len(PERMUTATIONS)]

    condition = CONDITIONS[(unit_id // len(PERMUTATIONS)) % len(CONDITIONS)]
    profile = unit_id % 4
    future = permutation[profile]

    # Synthetic mapping-following signal. The nuisance terms are deliberately
    # deterministic and independent of the generated response.
    logits = []
    for action in ACTIONS:
        baseline = 0.05 * action + 0.03 * domain + 0.02 * op
        profile_term = 0.04 * ((action + profile) % 4)
        alignment = mapping_signal(permutation, profile, future)
        signal = s.effect_size * (1.0 if action == future else 0.0) * alignment
        logits.append(baseline + profile_term + signal)

    choice = choose(softmax(logits), rng)

    return {
        "unit_id": unit_id,
        "domain": domain,
        "operationalisation": op,
        "presentation": presentation,
        "condition": condition,
        "permutation": permutation,
        "profile": profile,
        "future": future,
        "mapping_signal": mapping_signal(permutation, profile, future),
        "choice": choice,
        "effect_label": s.effect_label,
        "effect_size": s.effect_size,
    }


def generate_dataset(s: SimulationScenario) -> list[dict[str, Any]]:
    return [generate_unit(s, i) for i in range(s.n_units)]


def dataset_sha256(rows: list[dict[str, Any]]) -> str:
    raw = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


if __name__ == "__main__":
    scenario = SimulationScenario(
        effect_label="NULL", effect_size=0.0, n_units=1728,
        replicate=0, seed=410927
    )
    rows = generate_dataset(scenario)
    print(json.dumps({
        "status": "SYNTHETIC_GENERATOR_READY",
        "units": len(rows),
        "dataset_sha256": dataset_sha256(rows),
        "provider_api_calls": False,
        "scientific_executor_calls": False,
    }, sort_keys=True))
