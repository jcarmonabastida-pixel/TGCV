"""Typed, trivalent focal accessibility adjudication for C10-S.

This module is deliberately separate from the legacy D2 stage generator. It
implements the current candidate predicate crosswalk without promoting it to
a frozen universal definition or silently changing legacy outputs.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Literal, Sequence

TruthState = Literal["1", "0", "?"]
PredicateRole = Literal["ID", "REL", "COND", "AUTH", "RES"]
CoverageState = Literal["COMPLETE", "INCOMPLETE"]


class FocalAccessibilityContractError(ValueError):
    pass


def _state(value: str, label: str) -> TruthState:
    if value not in ("1", "0", "?"):
        raise FocalAccessibilityContractError(f"{label} must be 1, 0 or ?")
    return value  # type: ignore[return-value]


def _and(values: Sequence[TruthState]) -> TruthState:
    if not values:
        raise FocalAccessibilityContractError("conjunction requires at least one predicate")
    if "0" in values:
        return "0"
    if "?" in values:
        return "?"
    return "1"


def _or(values: Sequence[TruthState], *, exhaustive: bool) -> TruthState:
    if "1" in values:
        return "1"
    if not exhaustive or not values or "?" in values:
        return "?"
    return "0"


def _not(value: TruthState) -> TruthState:
    return {"1": "0", "0": "1", "?": "?"}[value]


def _digest(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class FocalPredicateEvidence:
    """One predicate's DGP truth and observed/evidence state.

    Coverage is epistemic only: it never overwrites or changes truth_state.
    """
    role: PredicateRole
    truth_state: TruthState
    observed_state: TruthState
    coverage: CoverageState
    unit_id: str
    transformation_id: str
    boundary_id: str
    context_id: str
    snapshot_id: str
    predicate_version: str
    provenance_ref: str

    def validate(self) -> None:
        if self.role not in ("ID", "REL", "COND", "AUTH", "RES"):
            raise FocalAccessibilityContractError("unsupported focal predicate role")
        _state(self.truth_state, f"{self.role} truth")
        _state(self.observed_state, f"{self.role} observed")
        if self.coverage not in ("COMPLETE", "INCOMPLETE"):
            raise FocalAccessibilityContractError("coverage must be COMPLETE or INCOMPLETE")
        if not all((self.unit_id, self.transformation_id, self.boundary_id,
                    self.context_id, self.snapshot_id, self.predicate_version,
                    self.provenance_ref)):
            raise FocalAccessibilityContractError("predicate identity, version and provenance are required")


@dataclass(frozen=True)
class FocalDependencyRoute:
    """One admissible technical route for the same semantic transformation.

    dependency_state is the conjunction of named technical requirements for
    this route. local_block_state means 1=route blocked, 0=not blocked, ?=unknown.
    A local block does not imply a universal BLOCK_f*.
    """
    route_id: str
    route_version: str
    unit_id: str
    transformation_id: str
    boundary_id: str
    context_id: str
    snapshot_id: str
    dependency_state: TruthState
    local_block_state: TruthState
    observed_dependency_state: TruthState
    observed_local_block_state: TruthState
    coverage: CoverageState
    provenance_ref: str

    def validate(self) -> None:
        if not all((self.route_id, self.route_version, self.unit_id,
                    self.transformation_id, self.boundary_id, self.context_id,
                    self.snapshot_id, self.provenance_ref)):
            raise FocalAccessibilityContractError("route identity/version/provenance is required")
        _state(self.dependency_state, "route DEP")
        _state(self.local_block_state, "route-local BLOCK")
        _state(self.observed_dependency_state, "observed route DEP")
        _state(self.observed_local_block_state, "observed route-local BLOCK")
        if self.coverage not in ("COMPLETE", "INCOMPLETE"):
            raise FocalAccessibilityContractError("route coverage must be COMPLETE or INCOMPLETE")


@dataclass(frozen=True)
class FocalAccessibilityResult:
    unit_id: str
    transformation_id: str
    snapshot_id: str
    predicate_truth: tuple[tuple[str, TruthState], ...]
    route_truth: tuple[tuple[str, TruthState], ...]
    dep_truth: TruthState
    global_block_truth: TruthState
    accessibility_truth: TruthState
    observed_accessibility: TruthState
    observed_coverage_complete: bool
    result_sha256: str


@dataclass(frozen=True)
class FocalAccessibilityInput:
    unit_id: str
    transformation_id: str
    boundary_id: str
    context_id: str
    snapshot_id: str
    predicates: tuple[FocalPredicateEvidence, ...]
    routes: tuple[FocalDependencyRoute, ...]
    route_catalog_exhaustive: bool
    global_block_state: TruthState
    observed_global_block_state: TruthState
    global_block_coverage: CoverageState
    observed_route_catalog_complete: bool
    global_block_scope: Literal["ALL_ADMISSIBLE_ROUTES"]
    contract_version: str

    def validate(self) -> None:
        if not all((self.unit_id, self.transformation_id, self.boundary_id,
                    self.context_id, self.snapshot_id, self.contract_version)):
            raise FocalAccessibilityContractError("focal accessibility input identity/version is required")
        if self.global_block_scope != "ALL_ADMISSIBLE_ROUTES":
            raise FocalAccessibilityContractError(
                "BLOCK_f* must be explicitly scoped to all admissible routes"
            )
        _state(self.global_block_state, "global BLOCK")
        _state(self.observed_global_block_state, "observed global BLOCK")
        if self.global_block_coverage not in ("COMPLETE", "INCOMPLETE"):
            raise FocalAccessibilityContractError("global BLOCK coverage must be COMPLETE or INCOMPLETE")
        if type(self.observed_route_catalog_complete) is not bool:
            raise FocalAccessibilityContractError("observed route-catalog completeness must be explicit")
        roles = [p.role for p in self.predicates]
        if sorted(roles) != ["AUTH", "COND", "ID", "REL", "RES"]:
            raise FocalAccessibilityContractError(
                "exactly one ID, REL, COND, AUTH and RES predicate is required"
            )
        for predicate in self.predicates:
            predicate.validate()
            if (predicate.unit_id, predicate.transformation_id, predicate.boundary_id,
                    predicate.context_id, predicate.snapshot_id) != (
                self.unit_id, self.transformation_id, self.boundary_id,
                self.context_id, self.snapshot_id
            ):
                raise FocalAccessibilityContractError("predicate identity does not match focal snapshot")
        route_ids = [r.route_id for r in self.routes]
        if len(route_ids) != len(set(route_ids)):
            raise FocalAccessibilityContractError("route IDs must be unique")
        for route in self.routes:
            route.validate()
            if (route.unit_id, route.transformation_id, route.boundary_id,
                    route.context_id, route.snapshot_id) != (
                self.unit_id, self.transformation_id, self.boundary_id,
                self.context_id, self.snapshot_id
            ):
                raise FocalAccessibilityContractError("route identity does not match focal snapshot")


def adjudicate_focal_accessibility(
    source: FocalAccessibilityInput,
) -> FocalAccessibilityResult:
    """Evaluate A_f*=ID∧REL∧COND∧AUTH∧RES∧DEP∧¬BLOCK in strong Kleene logic.

    DEP is existential over the explicitly enumerated admissible routes.
    Structural zero requires an exhaustive route catalog. A local route block
    removes only that route; only the explicit all-routes BLOCK predicate is
    applied globally. Observed coverage is reported separately from DGP truth.
    """
    source.validate()
    predicates = {p.role: p for p in source.predicates}
    route_truth = []
    for route in source.routes:
        route_truth.append((
            route.route_id,
            _and((route.dependency_state, _not(route.local_block_state))),
        ))
    dep_truth = _or([state for _, state in route_truth],
                    exhaustive=source.route_catalog_exhaustive)
    global_block = _state(source.global_block_state, "global BLOCK")
    truth_terms = (
        predicates["ID"].truth_state,
        predicates["REL"].truth_state,
        predicates["COND"].truth_state,
        predicates["AUTH"].truth_state,
        predicates["RES"].truth_state,
        dep_truth,
        _not(global_block),
    )
    accessibility = _and(truth_terms)

    observed_predicates = [p.observed_state if p.coverage == "COMPLETE" else "?"
                           for p in source.predicates]
    observed_route_states = [
        _and((r.observed_dependency_state, _not(r.observed_local_block_state)))
        if r.coverage == "COMPLETE" else "?"
        for r in source.routes
    ]
    observed_dep = _or(observed_route_states, exhaustive=source.observed_route_catalog_complete)
    observed_global_block = (
        source.observed_global_block_state
        if source.global_block_coverage == "COMPLETE" else "?"
    )
    observed = _and((*observed_predicates, observed_dep, _not(observed_global_block)))
    coverage_complete = (
        all(p.coverage == "COMPLETE" for p in source.predicates)
        and all(r.coverage == "COMPLETE" for r in source.routes)
        and source.global_block_coverage == "COMPLETE"
        and source.observed_route_catalog_complete
    )
    payload = {
        "unit_id": source.unit_id,
        "transformation_id": source.transformation_id,
        "snapshot_id": source.snapshot_id,
        "predicate_truth": tuple((role, predicates[role].truth_state)
                                 for role in ("ID", "REL", "COND", "AUTH", "RES")),
        "route_truth": tuple(route_truth),
        "dep_truth": dep_truth,
        "global_block_truth": global_block,
        "observed_route_truth": tuple(zip((r.route_id for r in source.routes), observed_route_states)),
        "observed_global_block": observed_global_block,
        "accessibility_truth": accessibility,
        "observed_accessibility": observed,
        "observed_coverage_complete": coverage_complete,
        "contract_version": source.contract_version,
    }
    return FocalAccessibilityResult(
        source.unit_id, source.transformation_id, source.snapshot_id,
        payload["predicate_truth"], tuple(route_truth), dep_truth, global_block,
        accessibility, observed, coverage_complete, _digest(payload),
    )
