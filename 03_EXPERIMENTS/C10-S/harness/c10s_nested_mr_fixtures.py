"""Deterministic analytical fixture generator for C10-S nested M/R validation.

This module creates scalar q_mr fixtures only. It does not invoke the C10-S
Generator, Analyzer, Evaluator, DGP, calibration banks, or scientific workflows.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
from typing import Any

import numpy as np

SEED_SCHEDULE_VERSION = "C10S_NESTED_MR_SEED_SCHEDULE_1.0"
FIXTURE_GENERATOR_VERSION = "C10S_NESTED_MR_FIXTURES_1.1"
OUTER_CONTRACT_VERSION = "1.0"
INNER_CONTRACT_VERSION = "1.0"

OUTER_INDEPENDENCE_BASIS = (
    "Fixture truth: outer-world latent states are generated from an independent "
    "PCG64 child stream spawned from the dataset seed."
)
INNER_INDEPENDENCE_BASIS = (
    "Fixture truth: each world receives its own independent PCG64 child stream "
    "for R draws, conditional on that world state."
)


@dataclass(frozen=True)
class FixtureSpec:
    tier: str
    cell_id: str
    family: str
    distribution: str
    m: int
    r: int
    k: int
    b: int
    true_within: float
    true_between: float
    parameters: tuple[tuple[str, float | int | str], ...]
    stochastic: bool = True

    def manifest(self) -> dict[str, Any]:
        value = asdict(self)
        value["parameters"] = dict(self.parameters)
        value["seed_schedule_version"] = SEED_SCHEDULE_VERSION
        value["fixture_generator_version"] = FIXTURE_GENERATOR_VERSION
        value["outer_contract"] = {
            "id": f"C10S-FIXTURE-M-{self.cell_id}",
            "version": OUTER_CONTRACT_VERSION,
            "mode": "DECLARED_IID_PSEUDORANDOM",
            "independence_basis": OUTER_INDEPENDENCE_BASIS,
        }
        value["inner_contract"] = {
            "id": f"C10S-FIXTURE-R-{self.cell_id}",
            "version": INNER_CONTRACT_VERSION,
            "mode": "DECLARED_IID_PSEUDORANDOM",
            "independence_basis": INNER_INDEPENDENCE_BASIS,
        }
        return value


@dataclass(frozen=True)
class FixtureDataset:
    spec: FixtureSpec
    rows: tuple[tuple[float, ...], ...]
    dataset_seed: int
    bootstrap_seed: int

    @property
    def metric(self) -> str:
        return "point_rmse" if self.spec.family == "F6" else "fixture_scalar"

    @property
    def world_ids(self) -> tuple[str, ...]:
        return tuple(f"{self.spec.cell_id}-M{index:04d}" for index in range(self.spec.m))


def derive_seed(namespace: str, cell_id: str, replicate_index: int) -> int:
    """Stable unsigned 64-bit seed with independent dataset/bootstrap namespaces."""
    if namespace not in {"fixture_dataset", "bootstrap"}:
        raise ValueError("unsupported seed namespace")
    if not isinstance(cell_id, str) or not cell_id:
        raise ValueError("cell_id is required")
    if type(replicate_index) is not int or replicate_index < 0:
        raise ValueError("replicate_index must be a nonnegative integer")
    payload = (
        f"{SEED_SCHEDULE_VERSION}|{namespace}|{cell_id}|{replicate_index}"
    ).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big", signed=False)


def _spec(
    tier: str, cell_id: str, family: str, distribution: str, m: int, r: int,
    k: int, b: int, within: float, between: float,
    parameters: dict[str, float | int | str], stochastic: bool = True,
) -> FixtureSpec:
    return FixtureSpec(
        tier=tier, cell_id=cell_id, family=family, distribution=distribution,
        m=m, r=r, k=k, b=b, true_within=within, true_between=between,
        parameters=tuple(sorted(parameters.items())), stochastic=stochastic,
    )


def tier_a_specs() -> tuple[FixtureSpec, ...]:
    """The eight frozen Tier A cells: four parameter cells × two designs."""
    designs = ((10, 5), (30, 20))
    gaussian = (
        ("balanced", 1.0, 1.0),
        ("low_between", 1.0, 0.05),
        ("high_between", 0.25, 2.0),
    )
    specs: list[FixtureSpec] = []
    for label, within, between in gaussian:
        for m, r in designs:
            specs.append(_spec(
                "A", f"F1_{label}_M{m}_R{r}", "F1", "gaussian_random_intercept",
                m, r, 1000, 1000, within, between,
                {"sigma2_within": within, "sigma2_between": between},
            ))
    for m, r in designs:
        specs.append(_spec(
            "A", f"F5_beta22_M{m}_R{r}", "F5", "beta_binomial_world_probability",
            m, r, 1000, 1000, 0.20, 0.05,
            {"alpha": 2, "beta": 2},
        ))
    return tuple(specs)


def tier_b_specs() -> tuple[FixtureSpec, ...]:
    """The frozen stochastic Tier B diagnostics: 20 cells."""
    specs: list[FixtureSpec] = []
    for label, within, between in (("balanced", 1.0, 1.0), ("low_between", 1.0, 0.05)):
        for m, r in ((3, 2), (10, 5), (2, 2)):
            specs.append(_spec(
                "B", f"F1_{label}_M{m}_R{r}", "F1", "gaussian_random_intercept",
                m, r, 500, 500, within, between,
                {"sigma2_within": within, "sigma2_between": between},
            ))
    for label, between in (("exact_zero", 0.0), ("near_zero", 0.01)):
        for m, r in ((3, 2), (10, 5)):
            specs.append(_spec(
                "B", f"F2_{label}_M{m}_R{r}", "F2", "gaussian_random_intercept",
                m, r, 500, 500, 1.0, between,
                {"sigma2_within": 1.0, "sigma2_between": between},
            ))
    for m, r in ((3, 2), (10, 5)):
        specs.append(_spec(
            "B", f"F3_within_zero_M{m}_R{r}", "F3", "gaussian_world_only",
            m, r, 500, 500, 0.0, 1.0,
            {"sigma2_within": 0.0, "sigma2_between": 1.0},
        ))
    for label, probability in (("p050", 0.5), ("p001", 0.01)):
        for m, r in ((3, 2), (10, 5)):
            specs.append(_spec(
                "B", f"F5_{label}_M{m}_R{r}", "F5", "bernoulli_constant_probability",
                m, r, 500, 500, probability * (1.0 - probability), 0.0,
                {"p": probability},
            ))
    for label, scale in (("unit_mse", 1.0), ("small_scale_mse", 1e-8)):
        for m, r in ((3, 2), (10, 5)):
            specs.append(_spec(
                "B", f"F6_{label}_M{m}_R{r}", "F6", "squared_normal_error",
                m, r, 500, 500, 2.0 * scale * scale, 0.0,
                {"mse_scale": scale},
            ))
    return tuple(specs)


def deterministic_guard_specs() -> tuple[FixtureSpec, ...]:
    """Exact deterministic controls, checked once rather than assigned K/B."""
    return (
        _spec("B", "F4_all_zero", "F4", "fully_degenerate", 3, 2, 0, 0,
              0.0, 0.0, {"value": 0.0}, stochastic=False),
        _spec("B", "F5_p_zero", "F5", "bernoulli_degenerate", 3, 2, 0, 0,
              0.0, 0.0, {"p": 0.0}, stochastic=False),
        _spec("B", "F5_p_one", "F5", "bernoulli_degenerate", 3, 2, 0, 0,
              0.0, 0.0, {"p": 1.0}, stochastic=False),
        _spec("B", "F6_exact_zero_mse", "F6", "exact_zero_squared_error", 3, 2, 0, 0,
              0.0, 0.0, {"mse_scale": 0.0}, stochastic=False),
    )


def generate_fixture(spec: FixtureSpec, replicate_index: int) -> FixtureDataset:
    if not spec.stochastic:
        raise ValueError("deterministic guard specs are generated by generate_deterministic_guard")
    dataset_seed = derive_seed("fixture_dataset", spec.cell_id, replicate_index)
    bootstrap_seed = derive_seed("bootstrap", spec.cell_id, replicate_index)
    outer_sequence, inner_sequence = np.random.SeedSequence(dataset_seed).spawn(2)
    outer_rng = np.random.Generator(np.random.PCG64(outer_sequence))
    inner_sequences = inner_sequence.spawn(spec.m)
    inner_rngs = [
        np.random.Generator(np.random.PCG64(sequence))
        for sequence in inner_sequences
    ]
    params = dict(spec.parameters)
    m, r = spec.m, spec.r

    if spec.family in {"F1", "F2"}:
        u = outer_rng.normal(0.0, np.sqrt(spec.true_between), size=m)
        eps = np.vstack([
            inner_rngs[index].normal(0.0, np.sqrt(spec.true_within), size=r)
            for index in range(m)
        ])
        values = u[:, None] + eps
    elif spec.family == "F3":
        u = outer_rng.normal(0.0, np.sqrt(spec.true_between), size=m)
        values = np.repeat(u[:, None], r, axis=1)
    elif spec.family == "F5" and spec.distribution == "beta_binomial_world_probability":
        p_world = outer_rng.beta(float(params["alpha"]), float(params["beta"]), size=m)
        values = np.vstack([
            inner_rngs[index].binomial(1, p_world[index], size=r)
            for index in range(m)
        ])
    elif spec.family == "F5":
        p = float(params["p"])
        values = np.vstack([inner_rngs[index].binomial(1, p, size=r) for index in range(m)])
    elif spec.family == "F6":
        scale = float(params["mse_scale"])
        errors = np.vstack([
            inner_rngs[index].normal(0.0, np.sqrt(scale), size=r)
            for index in range(m)
        ])
        values = errors * errors
    else:
        raise ValueError(f"unsupported fixture family/distribution: {spec.family}/{spec.distribution}")

    return FixtureDataset(
        spec=spec,
        rows=tuple(tuple(float(value) for value in row) for row in values),
        dataset_seed=dataset_seed,
        bootstrap_seed=bootstrap_seed,
    )


def generate_deterministic_guard(spec: FixtureSpec) -> FixtureDataset:
    if spec.stochastic:
        raise ValueError("expected a deterministic guard spec")
    params = dict(spec.parameters)
    if spec.family == "F4" or spec.family == "F6":
        value = 0.0
    elif spec.family == "F5":
        value = float(params["p"])
    else:
        raise ValueError("unsupported deterministic guard")
    rows = tuple(tuple(value for _ in range(spec.r)) for _ in range(spec.m))
    return FixtureDataset(
        spec=spec,
        rows=rows,
        dataset_seed=derive_seed("fixture_dataset", spec.cell_id, 0),
        bootstrap_seed=derive_seed("bootstrap", spec.cell_id, 0),
    )
