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
    route_component_truth: tuple[tuple[str, tuple[tuple[str, TruthState], ...]], ...]
    observed_route_component_truth: tuple[tuple[str, tuple[tuple[str, TruthState], ...]], ...]
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
    global_block_version: str
    global_block_provenance_ref: str
    observed_route_catalog_complete: bool
    route_catalog_version: str
    route_catalog_provenance_ref: str
    observed_route_catalog_provenance_ref: str
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
        if not all((self.global_block_version, self.global_block_provenance_ref,
                    self.route_catalog_version, self.route_catalog_provenance_ref,
                    self.observed_route_catalog_provenance_ref)):
            raise FocalAccessibilityContractError("global BLOCK and route-catalog versions/provenance are required")
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
    route_component_truth = tuple(
        (route.route_id, route.dependency_predicates) for route in source.routes
    )
    observed_route_component_truth = tuple(
        (
            route.route_id,
            route.observed_dependency_predicates if route.coverage == "COMPLETE"
            else tuple((name, "?") for name, _ in route.dependency_predicates),
        )
        for route in source.routes
    )
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
        "route_component_truth": route_component_truth,
        "observed_route_component_truth": observed_route_component_truth,
        "dep_truth": dep_truth,
        "global_block_truth": global_block,
        "observed_route_truth": tuple(zip((r.route_id for r in source.routes), observed_route_states)),
        "observed_global_block": observed_global_block,
        "global_block_version": source.global_block_version,
        "global_block_provenance_ref": source.global_block_provenance_ref,
        "route_catalog_version": source.route_catalog_version,
        "route_catalog_provenance_ref": source.route_catalog_provenance_ref,
        "observed_route_catalog_provenance_ref": source.observed_route_catalog_provenance_ref,
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
        route_component_truth, observed_route_component_truth,
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
    baseline_snapshot_version: str
    post_snapshot_id: str
    post_snapshot_version: str
    match_state: IdentityMatchState
    matching_contract_version: str
    adjudication_evidence_ref: str

    def validate(self) -> None:
        if self.match_state not in ("MATCHED", "NOT_MATCHED", "UNRESOLVED"):
            raise FocalAccessibilityContractError("semantic identity match state is invalid")
        if not all((self.unit_id, self.boundary_id, self.context_id,
                    self.baseline_transformation_id, self.baseline_transformation_version,
                    self.post_transformation_id, self.post_transformation_version,
                    self.baseline_snapshot_id, self.baseline_snapshot_version,
                    self.post_snapshot_id, self.post_snapshot_version,
                    self.matching_contract_version, self.adjudication_evidence_ref)):
            raise FocalAccessibilityContractError("semantic identity adjudication requires full provenance")


@dataclass(frozen=True)
class FocalOpeningResult:
    unit_id: str
    baseline_snapshot_id: str
    post_snapshot_id: str
    baseline_transformation_id: str
    baseline_transformation_version: str
    post_transformation_id: str
    post_transformation_version: str
    semantic_match_state: IdentityMatchState
    d_f_truth: OpeningState
    d_f_observed: OpeningState
    matching_contract_version: str
    adjudication_evidence_ref: str
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
            baseline.snapshot_id, baseline.snapshot_version,
            post.snapshot_id, post.snapshot_version) != (
        identity.baseline_transformation_id, identity.baseline_transformation_version,
        identity.post_transformation_id, identity.post_transformation_version,
        identity.baseline_snapshot_id, identity.baseline_snapshot_version,
        identity.post_snapshot_id, identity.post_snapshot_version
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
        "baseline_snapshot_version": baseline.snapshot_version,
        "post_snapshot_id": post.snapshot_id,
        "post_snapshot_version": post.snapshot_version,
        "baseline_transformation_id": baseline.transformation_id,
        "baseline_transformation_version": baseline.transformation_version,
        "post_transformation_id": post.transformation_id,
        "post_transformation_version": post.transformation_version,
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
        baseline.transformation_id, baseline.transformation_version,
        post.transformation_id, post.transformation_version,
        identity.match_state, truth, observed,
        identity.matching_contract_version, identity.adjudication_evidence_ref,
        _digest(payload),
    )


@dataclass(frozen=True)
class D2FocalAccessibilitySpecification:
    """Explicit D2 truth inputs for one unit's baseline and both Z potentials."""
    unit_id: str
    focal_route_id: str
    baseline: FocalAccessibilityInput
    post_by_z: tuple[tuple[int, FocalAccessibilityInput], ...]
    identity_matches_by_z: tuple[tuple[int, SemanticTransformationMatch], ...]
    specification_version: str
    provenance_ref: str

    def validate(self) -> None:
        if not all((self.unit_id, self.focal_route_id, self.specification_version, self.provenance_ref)):
            raise FocalAccessibilityContractError("D2 focal specification identity/version/provenance is required")
        if tuple(z for z, _ in self.post_by_z) != (0, 1):
            raise FocalAccessibilityContractError("D2 focal post inputs must preserve separate Z=0 and Z=1 potentials")
        if tuple(z for z, _ in self.identity_matches_by_z) != (0, 1):
            raise FocalAccessibilityContractError("D2 semantic identity adjudications must cover Z=0 and Z=1 exactly")
        if self.baseline.unit_id != self.unit_id:
            raise FocalAccessibilityContractError("D2 baseline focal input unit mismatch")
        self.baseline.validate()
        for z, source in self.post_by_z:
            if source.unit_id != self.unit_id:
                raise FocalAccessibilityContractError(f"D2 post-Z={z} focal input unit mismatch")
            source.validate()
        for source in (self.baseline, self.post_by_z[0][1], self.post_by_z[1][1]):
            if self.focal_route_id not in {route.route_id for route in source.routes}:
                raise FocalAccessibilityContractError(
                    f"declared focal route {self.focal_route_id} is absent from a D2 potential catalogue"
                )
        snapshot_ids = (
            self.baseline.snapshot_id,
            self.post_by_z[0][1].snapshot_id,
            self.post_by_z[1][1].snapshot_id,
        )
        if len(set(snapshot_ids)) != 3:
            raise FocalAccessibilityContractError(
                "D2 baseline, Z=0 and Z=1 require distinct potential snapshot identities"
            )
        for z, identity in self.identity_matches_by_z:
            identity.validate()
            post = self.post_by_z[z][1]
            if (
                identity.unit_id != self.unit_id
                or identity.baseline_snapshot_id != self.baseline.snapshot_id
                or identity.baseline_snapshot_version != self.baseline.snapshot_version
                or identity.post_snapshot_id != post.snapshot_id
                or identity.post_snapshot_version != post.snapshot_version
            ):
                raise FocalAccessibilityContractError(
                    f"D2 semantic identity adjudication does not bind exact baseline/Z={z} snapshots"
                )


@dataclass(frozen=True)
class D2FocalPotentialTruth:
    """Typed A_f*/D_f* truth for baseline and both potential policy worlds."""
    unit_id: str
    focal_route_id: str
    baseline: FocalAccessibilityResult
    post_by_z: tuple[tuple[int, FocalAccessibilityResult], ...]
    opening_by_z: tuple[tuple[int, FocalOpeningResult], ...]
    specification_version: str
    provenance_ref: str
    result_sha256: str

    def validate(self) -> None:
        if not all((self.unit_id, self.focal_route_id, self.specification_version, self.provenance_ref)):
            raise FocalAccessibilityContractError("D2 focal truth identity/version/provenance is required")
        if self.baseline.unit_id != self.unit_id:
            raise FocalAccessibilityContractError("D2 focal truth baseline unit mismatch")
        if self.baseline.accessibility_truth != "0" or self.baseline.dep_truth != "0":
            raise FocalAccessibilityContractError("D2 focal truth must retain the clean inaccessible baseline")
        if tuple(z for z, _ in self.post_by_z) != (0, 1):
            raise FocalAccessibilityContractError("D2 focal truth must preserve Z=0 and Z=1 post states")
        if tuple(z for z, _ in self.opening_by_z) != (0, 1):
            raise FocalAccessibilityContractError("D2 focal truth must preserve Z=0 and Z=1 opening states")
        if any(result.unit_id != self.unit_id for _, result in self.post_by_z):
            raise FocalAccessibilityContractError("D2 focal post-state unit mismatch")
        for state in (self.baseline, *(row for _, row in self.post_by_z)):
            component_map = dict(state.route_component_truth)
            if self.focal_route_id not in component_map:
                raise FocalAccessibilityContractError("D2 focal truth omits its declared focal route")
            if tuple(name for name, _ in component_map[self.focal_route_id]) != (
                "C_install", "C_integrity", "C_compat", "C_oper",
            ):
                raise FocalAccessibilityContractError("D2 focal truth has an invalid technical DEP component roster")
        if any(result.unit_id != self.unit_id for _, result in self.opening_by_z):
            raise FocalAccessibilityContractError("D2 focal opening unit mismatch")
        post_map = dict(self.post_by_z)
        for z, opening in self.opening_by_z:
            if (opening.baseline_snapshot_id != self.baseline.snapshot_id
                    or opening.post_snapshot_id != post_map[z].snapshot_id
                    or opening.baseline_transformation_id != self.baseline.transformation_id
                    or opening.baseline_transformation_version != self.baseline.transformation_version
                    or opening.post_transformation_id != post_map[z].transformation_id
                    or opening.post_transformation_version != post_map[z].transformation_version
                    or opening.semantic_match_state not in ("MATCHED", "NOT_MATCHED", "UNRESOLVED")
                    or not opening.matching_contract_version or not opening.adjudication_evidence_ref
                    or opening.d_f_truth not in ("1", "0", "?", "NOT_COMPARABLE")):
                raise FocalAccessibilityContractError(
                    f"D2 focal opening Z={z} is detached from its exact baseline/post snapshots"
                )
        payload = {
            "unit_id": self.unit_id,
            "focal_route_id": self.focal_route_id,
            "specification_version": self.specification_version,
            "provenance_ref": self.provenance_ref,
            "baseline_result_sha256": self.baseline.result_sha256,
            "post_result_sha256_by_z": tuple((z, row.result_sha256) for z, row in self.post_by_z),
            "opening_result_sha256_by_z": tuple((z, row.result_sha256) for z, row in self.opening_by_z),
        }
        if _digest(payload) != self.result_sha256:
            raise FocalAccessibilityContractError("D2 focal truth digest does not bind its component results")
        if len(self.result_sha256) != 64 or any(c not in "0123456789abcdef" for c in self.result_sha256):
            raise FocalAccessibilityContractError("D2 focal truth result digest must be lowercase SHA-256")


def _d2_non_dependency_signature(source: FocalAccessibilityInput) -> tuple:
    predicates = tuple(sorted(
        (row.role, row.truth_state, row.predicate_version)
        for row in source.predicates
    ))
    routes = tuple(sorted(
        (
            row.route_id,
            row.route_version,
            tuple(name for name, _ in row.dependency_predicates),
            row.local_block_state,
        )
        for row in source.routes
    ))
    return (
        predicates,
        source.global_block_state,
        source.global_block_version,
        source.global_block_scope,
        source.route_catalog_version,
        source.route_catalog_exhaustive,
        routes,
    )


def adjudicate_d2_focal_potentials(
    specification: D2FocalAccessibilitySpecification,
) -> D2FocalPotentialTruth:
    """Adjudicate D2 A_f*/D_f* without translating legacy stage fields.

    The clean D2 nucleus requires a structurally inaccessible baseline caused
    by DEP=0, with the other focal predicates true and basal authorization=1.
    Across baseline and both Z worlds, ID/REL/COND/AUTH/RES, universal/local
    blocks and the exhaustive route catalogue remain invariant. Only the
    named technical DEP components may differ by policy. Unknown post states
    remain unknown; they are never imputed from attempt, receipt or install.
    """
    specification.validate()
    sources = (
        specification.baseline,
        specification.post_by_z[0][1],
        specification.post_by_z[1][1],
    )
    baseline = specification.baseline
    baseline_result = adjudicate_focal_accessibility(baseline)
    baseline_predicates = {row.role: row.truth_state for row in baseline.predicates}

    if baseline_result.accessibility_truth != "0" or baseline_result.dep_truth != "0":
        raise FocalAccessibilityContractError(
            "D2 clean nucleus requires baseline A_f*=0 specifically through exhaustive DEP=0"
        )
    if not baseline.route_catalog_exhaustive:
        raise FocalAccessibilityContractError(
            "D2 clean baseline requires an exhaustive admissible-route catalogue"
        )
    if any(baseline_predicates.get(role) != "1" for role in ("ID", "REL", "COND", "AUTH", "RES")):
        raise FocalAccessibilityContractError(
            "D2 clean baseline requires ID/REL/COND/AUTH/RES=1, including C_auth,base=1"
        )
    if baseline.global_block_state != "0":
        raise FocalAccessibilityContractError(
            "D2 clean baseline requires no universal BLOCK; focal inaccessibility must arise through DEP"
        )

    reference_signature = _d2_non_dependency_signature(baseline)
    baseline_routes = {route.route_id: route for route in baseline.routes}
    for source in sources:
        if not source.routes:
            raise FocalAccessibilityContractError("D2 focal route catalogue must include the declared focal route")
        for route in source.routes:
            if tuple(name for name, _ in route.dependency_predicates) != (
                "C_install", "C_integrity", "C_compat", "C_oper",
            ):
                raise FocalAccessibilityContractError(
                    "D2 DEP route must preserve the four named C_dep* components exactly"
                )
    for source in sources[1:]:
        if source.contract_version != baseline.contract_version:
            raise FocalAccessibilityContractError("D2 focal contract version changes across baseline/Z potentials")
        if (source.boundary_id, source.context_id) != (baseline.boundary_id, baseline.context_id):
            raise FocalAccessibilityContractError("D2 focal boundary/context changes across potential worlds")
        if _d2_non_dependency_signature(source) != reference_signature:
            raise FocalAccessibilityContractError(
                "D2 isolation violation: non-DEP predicates, blocks or route catalogue differ across potential worlds"
            )
        for route in source.routes:
            if route.route_id != specification.focal_route_id:
                if route.dependency_predicates != baseline_routes[route.route_id].dependency_predicates:
                    raise FocalAccessibilityContractError(
                        "D2 isolation violation: a non-focal alternative route changed across policy potentials"
                    )
        values = {row.role: row.truth_state for row in source.predicates}
        if any(values.get(role) != "1" for role in ("ID", "REL", "COND", "AUTH", "RES")):
            raise FocalAccessibilityContractError(
                "D2 isolated policy contrast requires ID/REL/COND/AUTH/RES=1 in both potential worlds"
            )
        if source.global_block_state != "0":
            raise FocalAccessibilityContractError("D2 isolated policy contrast cannot introduce a universal BLOCK")

    post_results = []
    opening_results = []
    matches = dict(specification.identity_matches_by_z)
    for z, source in specification.post_by_z:
        post_result = adjudicate_focal_accessibility(source)
        opening = derive_focal_opening(
            baseline_result, post_result, matches[z],
        )
        post_results.append((z, post_result))
        opening_results.append((z, opening))

    payload = {
        "unit_id": specification.unit_id,
        "focal_route_id": specification.focal_route_id,
        "specification_version": specification.specification_version,
        "provenance_ref": specification.provenance_ref,
        "baseline_result_sha256": baseline_result.result_sha256,
        "post_result_sha256_by_z": tuple((z, row.result_sha256) for z, row in post_results),
        "opening_result_sha256_by_z": tuple((z, row.result_sha256) for z, row in opening_results),
    }
    result = D2FocalPotentialTruth(
        specification.unit_id, specification.focal_route_id, baseline_result, tuple(post_results),
        tuple(opening_results), specification.specification_version,
        specification.provenance_ref, _digest(payload),
    )
    result.validate()
    return result
