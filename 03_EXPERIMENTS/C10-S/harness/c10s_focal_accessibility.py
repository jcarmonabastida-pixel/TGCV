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
    if not exhaustive or "?" in values:
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
    transformation_version: str
    boundary_id: str
    context_id: str
    snapshot_id: str
    snapshot_version: str
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
                    self.transformation_version, self.context_id, self.snapshot_id,
                    self.snapshot_version, self.predicate_version,
                    self.provenance_ref)):
            raise FocalAccessibilityContractError("predicate identity, version and provenance are required")


@dataclass(frozen=True)
class FocalDependencyRoute:
    """One admissible technical route for the same semantic transformation.

    Named dependency predicates are retained separately. local_block_state means
    1=route blocked, 0=not blocked, ?=unknown.
    A local block does not imply a universal BLOCK_f*.
    """
    route_id: str
    route_version: str
    unit_id: str
    transformation_id: str
    transformation_version: str
    boundary_id: str
    context_id: str
    snapshot_id: str
    snapshot_version: str
    dependency_predicates: tuple[tuple[str, TruthState], ...]
    local_block_state: TruthState
    observed_dependency_predicates: tuple[tuple[str, TruthState], ...]
    observed_local_block_state: TruthState
    coverage: CoverageState
    provenance_ref: str

    def validate(self) -> None:
        if not all((self.route_id, self.route_version, self.unit_id,
                    self.transformation_id, self.transformation_version,
                    self.boundary_id, self.context_id, self.snapshot_id,
                    self.snapshot_version, self.provenance_ref)):
            raise FocalAccessibilityContractError("route identity/version/provenance is required")
        if not self.dependency_predicates or not self.observed_dependency_predicates:
            raise FocalAccessibilityContractError("route must expose named DEP components and observed states")
        names = [name for name, _ in self.dependency_predicates]
        observed_names = [name for name, _ in self.observed_dependency_predicates]
        if any(not name for name in names) or len(names) != len(set(names)):
            raise FocalAccessibilityContractError("route DEP component names must be nonempty and unique")
        if observed_names != names:
            raise FocalAccessibilityContractError("observed DEP components must match the truth component roster/order")
        for name, value in self.dependency_predicates:
            _state(value, f"route DEP component {name}")
        for name, value in self.observed_dependency_predicates:
            _state(value, f"observed route DEP component {name}")
        _state(self.local_block_state, "route-local BLOCK")
        _state(self.observed_local_block_state, "observed route-local BLOCK")
        if self.coverage not in ("COMPLETE", "INCOMPLETE"):
            raise FocalAccessibilityContractError("route coverage must be COMPLETE or INCOMPLETE")


@dataclass(frozen=True)
class FocalAccessibilityResult:
    unit_id: str
    transformation_id: str
    transformation_version: str
    boundary_id: str
    context_id: str
    snapshot_id: str
    snapshot_version: str
    contract_version: str
    predicate_truth: tuple[tuple[str, TruthState], ...]
    route_truth: tuple[tuple[str, TruthState], ...]
    observed_route_truth: tuple[tuple[str, TruthState], ...]
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
    transformation_version: str
    boundary_id: str
    context_id: str
    snapshot_id: str
    snapshot_version: str
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
        if not all((self.unit_id, self.transformation_id, self.transformation_version,
                    self.boundary_id, self.context_id, self.snapshot_id,
                    self.snapshot_version, self.contract_version)):
            raise FocalAccessibilityContractError("focal accessibility input identity/version is required")
        if self.global_block_scope != "ALL_ADMISSIBLE_ROUTES":
            raise FocalAccessibilityContractError(
                "BLOCK_f* must be explicitly scoped to all admissible routes"
            )
        _state(self.global_block_state, "global BLOCK")
        _state(self.observed_global_block_state, "observed global BLOCK")
        if self.global_block_coverage not in ("COMPLETE", "INCOMPLETE"):
            raise FocalAccessibilityContractError("global BLOCK coverage must be COMPLETE or INCOMPLETE")
        if type(self.observed_route_catalog_complete) is not bool or type(self.route_catalog_exhaustive) is not bool:
            raise FocalAccessibilityContractError("truth and observed route-catalog completeness must be explicit")
        roles = [p.role for p in self.predicates]
        if sorted(roles) != ["AUTH", "COND", "ID", "REL", "RES"]:
            raise FocalAccessibilityContractError(
                "exactly one ID, REL, COND, AUTH and RES predicate is required"
            )
        for predicate in self.predicates:
            predicate.validate()
            if (predicate.unit_id, predicate.transformation_id, predicate.transformation_version,
                    predicate.boundary_id, predicate.context_id, predicate.snapshot_id,
                    predicate.snapshot_version) != (
                self.unit_id, self.transformation_id, self.transformation_version,
                self.boundary_id, self.context_id, self.snapshot_id, self.snapshot_version
            ):
                raise FocalAccessibilityContractError("predicate identity does not match focal snapshot")
        route_ids = [r.route_id for r in self.routes]
        if len(route_ids) != len(set(route_ids)):
            raise FocalAccessibilityContractError("route IDs must be unique")
        for route in self.routes:
            route.validate()
            if (route.unit_id, route.transformation_id, route.transformation_version,
                    route.boundary_id, route.context_id, route.snapshot_id,
                    route.snapshot_version) != (
                self.unit_id, self.transformation_id, self.transformation_version,
                self.boundary_id, self.context_id, self.snapshot_id, self.snapshot_version
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
            _and((*[value for _, value in route.dependency_predicates], _not(route.local_block_state))),
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
        _and((*[value for _, value in r.observed_dependency_predicates], _not(r.observed_local_block_state)))
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
        "transformation_version": source.transformation_version,
        "boundary_id": source.boundary_id,
        "context_id": source.context_id,
        "snapshot_id": source.snapshot_id,
        "snapshot_version": source.snapshot_version,
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
        source.unit_id, source.transformation_id, source.transformation_version,
        source.boundary_id, source.context_id, source.snapshot_id,
        source.snapshot_version, source.contract_version,
        payload["predicate_truth"], tuple(route_truth),
        tuple(zip((r.route_id for r in source.routes), observed_route_states)),
        dep_truth, global_block, accessibility, observed, coverage_complete, _digest(payload),
    )


IdentityMatchState = Literal["MATCHED", "NOT_MATCHED", "UNRESOLVED"]
OpeningState = Literal["1", "0", "?", "NOT_COMPARABLE"]


@dataclass(frozen=True)
class SemanticTransformationMatch:
    """Independent semantic-identity adjudication for the same focal tau2."""
    unit_id: str
    boundary_id: str
    context_id: str
    baseline_transformation_id: str
    baseline_transformation_version: str
    post_transformation_id: str
    post_transformation_version: str
    baseline_snapshot_id: str
    post_snapshot_id: str
    match_state: IdentityMatchState
    matching_contract_version: str
    adjudication_evidence_ref: str

    def validate(self) -> None:
        if self.match_state not in ("MATCHED", "NOT_MATCHED", "UNRESOLVED"):
            raise FocalAccessibilityContractError("semantic identity match state is invalid")
        if not all((self.unit_id, self.boundary_id, self.context_id,
                    self.baseline_transformation_id, self.baseline_transformation_version,
                    self.post_transformation_id, self.post_transformation_version,
                    self.baseline_snapshot_id, self.post_snapshot_id,
                    self.matching_contract_version, self.adjudication_evidence_ref)):
            raise FocalAccessibilityContractError("semantic identity adjudication requires full provenance")


@dataclass(frozen=True)
class FocalOpeningResult:
    unit_id: str
    baseline_snapshot_id: str
    post_snapshot_id: str
    semantic_match_state: IdentityMatchState
    d_f_truth: OpeningState
    d_f_observed: OpeningState
    matching_contract_version: str
    result_sha256: str


def derive_focal_opening(
    baseline: FocalAccessibilityResult,
    post: FocalAccessibilityResult,
    identity: SemanticTransformationMatch,
) -> FocalOpeningResult:
    """Derive D_f*=I(A_f*(t0)=0 AND A_f*(t1)=1) only for the same matched tau2.

    Semantic matching is an explicit independently evidenced input. Different
    identifiers/versions are never auto-merged, and a changed evidence hash is
    not used as a semantic identity decision.
    """
    identity.validate()
    if baseline.unit_id != post.unit_id or baseline.unit_id != identity.unit_id:
        raise FocalAccessibilityContractError("baseline/post focal unit identity mismatch")
    if (baseline.boundary_id, baseline.context_id) != (post.boundary_id, post.context_id):
        raise FocalAccessibilityContractError("baseline/post boundary or context is not comparable")
    if baseline.contract_version != post.contract_version:
        raise FocalAccessibilityContractError("baseline/post focal predicate contracts are not version-comparable")
    if (baseline.boundary_id, baseline.context_id) != (identity.boundary_id, identity.context_id):
        raise FocalAccessibilityContractError("identity adjudication boundary/context mismatch")
    if baseline.snapshot_id == post.snapshot_id:
        raise FocalAccessibilityContractError("D_f* requires distinct baseline and post snapshots")
    if (baseline.transformation_id, baseline.transformation_version,
            post.transformation_id, post.transformation_version,
            baseline.snapshot_id, post.snapshot_id) != (
        identity.baseline_transformation_id, identity.baseline_transformation_version,
        identity.post_transformation_id, identity.post_transformation_version,
        identity.baseline_snapshot_id, identity.post_snapshot_id
    ):
        raise FocalAccessibilityContractError("semantic identity adjudication does not bind exact focal inputs")

    if identity.match_state == "NOT_MATCHED":
        truth: OpeningState = "NOT_COMPARABLE"
        observed: OpeningState = "NOT_COMPARABLE"
    elif identity.match_state == "UNRESOLVED":
        truth = "?"
        observed = "?"
    else:
        before, after = baseline.accessibility_truth, post.accessibility_truth
        if "?" in (before, after):
            truth = "?"
        else:
            truth = "1" if (before, after) == ("0", "1") else "0"
        observed_before, observed_after = (
            baseline.observed_accessibility, post.observed_accessibility
        )
        if "?" in (observed_before, observed_after):
            observed = "?"
        else:
            observed = "1" if (observed_before, observed_after) == ("0", "1") else "0"

    payload = {
        "unit_id": baseline.unit_id,
        "baseline_snapshot_id": baseline.snapshot_id,
        "post_snapshot_id": post.snapshot_id,
        "semantic_match_state": identity.match_state,
        "d_f_truth": truth,
        "d_f_observed": observed,
        "matching_contract_version": identity.matching_contract_version,
        "adjudication_evidence_ref": identity.adjudication_evidence_ref,
        "baseline_accessibility_sha256": baseline.result_sha256,
        "post_accessibility_sha256": post.result_sha256,
    }
    return FocalOpeningResult(
        baseline.unit_id, baseline.snapshot_id, post.snapshot_id,
        identity.match_state, truth, observed,
        identity.matching_contract_version, _digest(payload),
    )
