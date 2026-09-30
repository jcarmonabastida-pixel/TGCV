"""NEXT4 mapping signal and primary contrast implementation.

Design-stage only. No provider calls and no scientific execution.
The mapping signal is a deterministic function of the frozen permutation.
"""

from __future__ import annotations
from dataclasses import dataclass
import hashlib
import json
from itertools import permutations

IMPLEMENTATION_ID = "TI001_V012_NEXT4_MAPPING_SIGNAL_AND_PRIMARY_CONTRAST_IMPLEMENTATION_001"
N_ACTIONS = 4
IDENTITY = (0, 1, 2, 3)
ALL_PERMUTATIONS = tuple(permutations(IDENTITY))


@dataclass(frozen=True)
class MappingRecord:
    profile_id: int
    future_structure_id: int
    permutation_id: int

    @property
    def aligned(self) -> int:
        return int(self.future_structure_id == self.profile_id)


def validate_permutation(p):
    p = tuple(p)
    if sorted(p) != list(IDENTITY):
        raise ValueError("Invalid four-element permutation.")
    return p


def mapping_table(permutation):
    p = validate_permutation(permutation)
    return tuple(MappingRecord(i, p[i], ALL_PERMUTATIONS.index(p))
                 for i in IDENTITY)


def mapping_signal(permutation, profile_id, future_structure_id):
    p = validate_permutation(permutation)
    if profile_id not in IDENTITY or future_structure_id not in IDENTITY:
        raise ValueError("Profile/future identifiers must be 0..3.")
    # Semantic alignment is defined solely by the frozen permutation.
    return int(p[profile_id] == future_structure_id)


def alignment_vector(permutation):
    return tuple(mapping_signal(permutation, p, permutation[p]) for p in IDENTITY)


def contrast_definition():
    return {
        "type": "mapping_alignment",
        "primary_comparison": ["STATIC_CONTROL", "FUTURE_REASSIGNED"],
        "estimand": "change in action×profile association aligned with imposed profile→future permutation",
        "direction": "positive alignment according to frozen mapping_signal",
        "two_sided_alpha": 0.05,
        "not_primary": "generic STATIC_CONTROL minus FUTURE_REASSIGNED condition effect",
        "response_independent": True,
    }


def canonical_manifest():
    payload = {
        "implementation_id": IMPLEMENTATION_ID,
        "n_actions": N_ACTIONS,
        "permutation_count": len(ALL_PERMUTATIONS),
        "contrast": contrast_definition(),
        "provider_api_calls": False,
        "scientific_executor_calls": False,
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["sha256"] = hashlib.sha256(raw.encode()).hexdigest()
    return payload


if __name__ == "__main__":
    assert len(ALL_PERMUTATIONS) == 24
    for p in ALL_PERMUTATIONS:
        assert len(mapping_table(p)) == 4
    print(json.dumps(canonical_manifest(), indent=2, sort_keys=True))
