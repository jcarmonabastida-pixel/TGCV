"""TI-001 V012 NEXT4 power/sensitivity simulation.

DESIGN-STAGE ONLY. No provider/model API calls. No scientific fixture access.
This module intentionally stops at synthetic-data generation primitives until
the exact primary contrast/coding is frozen in a separate analysis specification.
"""

from __future__ import annotations
from dataclasses import dataclass
import hashlib
import json
from typing import Any

SPEC_ID = "TI001_V012_NEXT4_POWER_SENSITIVITY_ANALYSIS_SPECIFICATION_001"
IMPLEMENTATION_ID = "TI001_V012_NEXT4_POWER_SENSITIVITY_IMPLEMENTATION_001"
EFFECT_LABELS = ("NULL", "VERY_SMALL", "SMALL", "MODERATE", "OPTIMISTIC")
SAMPLE_SIZES = (1728, 2304, 3456, 5184, 6912)
CONDITIONS = ("STATIC_CONTROL", "FUTURE_REASSIGNED",
              "SURFACE_CONTROL", "UNINFORMATIVE_NULL")
PRESENTATIONS = ("order", "position", "orientation", "neutral")
DOMAINS = ("DOMAIN_01", "DOMAIN_02", "DOMAIN_03")
OPERATIONALISATIONS = ("OP_01", "OP_02")


@dataclass(frozen=True)
class SimulationConfig:
    master_seed: int
    effect_parameters: dict[str, float]
    n_replicates: int = 2000

    def canonical(self) -> str:
        return json.dumps({
            "implementation_id": IMPLEMENTATION_ID,
            "master_seed": self.master_seed,
            "effect_parameters": self.effect_parameters,
            "n_replicates": self.n_replicates,
            "sample_sizes": SAMPLE_SIZES,
            "conditions": CONDITIONS,
            "presentations": PRESENTATIONS,
            "domains": DOMAINS,
            "operationalisations": OPERATIONALISATIONS,
        }, sort_keys=True, separators=(",", ":"))

    def sha256(self) -> str:
        return hashlib.sha256(self.canonical().encode()).hexdigest()


def derive_seed(master_seed: int, scenario_id: str, n: int, replicate: int) -> int:
    payload = f"{master_seed}|{scenario_id}|{n}|{replicate}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def deterministic_mapping(permutation: tuple[int, ...]) -> dict[int, int]:
    if sorted(permutation) != [0, 1, 2, 3]:
        raise ValueError("Permutation must contain each profile/future index exactly once.")
    return dict(enumerate(permutation))


def validate_config(config: SimulationConfig) -> None:
    if config.n_replicates < 2000:
        raise ValueError("At least 2,000 Monte Carlo replicates are required.")
    if set(config.effect_parameters) != set(EFFECT_LABELS):
        raise ValueError("Effect grid must contain exactly the five declared labels.")
    if any(not isinstance(v, (int, float)) for v in config.effect_parameters.values()):
        raise TypeError("Effect parameters must be numeric.")
    if config.effect_parameters["NULL"] != 0.0:
        raise ValueError("NULL effect must be exactly zero.")


def implementation_manifest(config: SimulationConfig) -> dict[str, Any]:
    validate_config(config)
    return {
        "implementation_id": IMPLEMENTATION_ID,
        "spec_id": SPEC_ID,
        "config_sha256": config.sha256(),
        "provider_api_calls": False,
        "scientific_executor_calls": False,
        "scientific_fixture_reads": False,
        "next3_effect_coefficients_used": False,
        "effect_labels": EFFECT_LABELS,
        "sample_sizes": SAMPLE_SIZES,
        "n_replicates": config.n_replicates,
        "seed_derivation": "SHA256(master_seed|scenario_id|N|replicate)[:8]",
        "status": "IMPLEMENTATION_READY_FOR_AUDIT",
    }


if __name__ == "__main__":
    # Deliberately no simulation execution here.
    # This entry point only validates the frozen configuration contract.
    config = SimulationConfig(
        master_seed=410927,
        effect_parameters={
            "NULL": 0.0,
            "VERY_SMALL": 0.10,
            "SMALL": 0.25,
            "MODERATE": 0.50,
            "OPTIMISTIC": 0.80,
        },
    )
    print(json.dumps(implementation_manifest(config), indent=2, sort_keys=True))
