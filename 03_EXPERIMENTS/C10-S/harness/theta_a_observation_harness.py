"""Focal g_A observation evidence firewall for C10-S.

This module seals only passive S3 records linked to a realized, directly
assigned joint g_A policy. It does not estimate theta_A and does not expose
DGP truth, q_X target masses, potential outcomes, or latent states.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal
import hashlib
import json
from typing import Any, Sequence

from c10s_synthetic_components import ThetaAS3ObservationRecord, ContractError


SCHEMA = "C10S-THETA-A-S3-OBSERVATION-001"
ALLOWED_FIELDS = frozenset(ThetaAS3ObservationRecord.__dataclass_fields__)


def _plain(value: Any) -> Any:
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _plain(v) for k, v in sorted(value.items())}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    return value


def _hash(value: Any) -> str:
    raw = json.dumps(_plain(value), sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ThetaAEvidenceCandidate:
    run_id: str
    rows: tuple[dict[str, Any], ...]


@dataclass(frozen=True)
class SealedThetaAEvidence:
    run_id: str
    rows: tuple[dict[str, Any], ...]
    manifest: dict[str, Any]
    sha256: str


class ThetaASealer:
    """Strict allow-list, identity, timing, and assignment-consistency checks."""

    version = "c10s-theta-a-sealer-0.1"

    def seal(self, candidate: ThetaAEvidenceCandidate) -> SealedThetaAEvidence:
        if not candidate.run_id or not candidate.rows:
            raise ContractError("theta_A evidence requires run identity and non-empty rows")
        seen_observations: set[str] = set()
        unit_contracts: dict[str, tuple[Any, ...]] = {}
        normalised_rows: list[dict[str, Any]] = []
        for row in candidate.rows:
            if set(row) != ALLOWED_FIELDS:
                raise ContractError("theta_A row violates the S3 evidence allow-list")
            if row["run_id"] != candidate.run_id:
                raise ContractError("theta_A row run_id mismatch")
            required_strings = ("unit_id", "history_ref", "assignment_bundle_sha256",
                                "q_x_sha256", "assigned_vector_sha256",
                                "policy_fingerprint", "r_common_fingerprint", "history_id",
                                "observation_id", "profile_config_id", "profile_config_version",
                                "s3_config_id", "s3_config_version")
            if any(not isinstance(row[k], str) or not row[k] for k in required_strings):
                raise ContractError("theta_A evidence contains missing identity or version fields")
            if row["assigned_arm"] not in (0, 1):
                raise ContractError("theta_A assigned_arm must be 0 or 1")
            probability = row["assignment_probability"]
            if (not isinstance(probability, (int, float)) or isinstance(probability, bool)
                    or not 0.0 < probability <= 1.0):
                raise ContractError("theta_A assignment probability must be in (0,1]")
            if row["temporal_resolution"] != "POINT_SAMPLE":
                raise ContractError("unsupported temporal resolution in theta_A evidence")
            if row["enabled_status"] not in ("OBSERVED", "MISSING"):
                raise ContractError("invalid ENABLED missingness status")
            if row["admission_status"] not in ("OBSERVED", "MISSING"):
                raise ContractError("invalid admission missingness status")
            if row["profile_status"] not in ("OBSERVED", "MISSING"):
                raise ContractError("invalid PROFILE missingness status")
            for value, status, label in (
                (row["enabled_observed"], row["enabled_status"], "ENABLED"),
                (row["admission_behavior_observed"], row["admission_status"], "admission"),
                (row["profile_value_observed"], row["profile_status"], "PROFILE"),
            ):
                if (status == "MISSING") != (value is None):
                    raise ContractError(f"{label} value and missingness status disagree")
            times = (row["observation_time"], row["capture_time"], row["ingestion_time"])
            if any(not isinstance(t, Decimal) or not t.is_finite() for t in times):
                raise ContractError("theta_A observation timestamps must be finite Decimal values")
            if not times[0] <= times[1] <= times[2]:
                raise ContractError("theta_A observation/capture/ingestion times are not ordered")
            oid = row["observation_id"]
            if oid in seen_observations:
                raise ContractError("duplicate theta_A observation_id")
            seen_observations.add(oid)
            unit = row["unit_id"]
            assignment_contract = (row["assigned_arm"], row["assigned_vector_sha256"],
                                   row["policy_fingerprint"], row["r_common_fingerprint"],
                                   row["history_ref"], row["history_id"])
            if unit in unit_contracts and unit_contracts[unit] != assignment_contract:
                raise ContractError("inconsistent g_A assignment/history across a unit's observations")
            unit_contracts[unit] = assignment_contract
            normalised_rows.append(dict(row))
        arms = {contract[0] for contract in unit_contracts.values()}
        if arms != {0, 1}:
            raise ContractError("theta_A evidence must contain units assigned to both g_A arms")
        manifest = {"run_id": candidate.run_id, "schema": SCHEMA,
                    "sealer_version": self.version, "row_count": len(normalised_rows),
                    "unit_count": len(unit_contracts),
                    "temporal_resolution": "POINT_SAMPLE"}
        payload = {"manifest": manifest, "rows": normalised_rows}
        return SealedThetaAEvidence(candidate.run_id, tuple(normalised_rows),
                                    manifest, _hash(payload))


def candidate_from_s3_records(
    records: Sequence[ThetaAS3ObservationRecord],
) -> ThetaAEvidenceCandidate:
    if not records:
        raise ContractError("cannot construct theta_A evidence from empty S3 records")
    run_ids = {record.run_id for record in records}
    if len(run_ids) != 1:
        raise ContractError("theta_A S3 records contain multiple run identities")
    return ThetaAEvidenceCandidate(next(iter(run_ids)),
                                   tuple(asdict(record) for record in records))
