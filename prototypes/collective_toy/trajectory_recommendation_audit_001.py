"""Append-only, tamper-evident audit ledger for pre-execution trajectory recommendations.

This module is separate from the selector and execution flow. It does not execute trajectories
or claim storage-level immutability: the hash chain detects edits, deletions, and reordering
when verified, but a full rewrite can be recomputed unless an external checkpoint exists.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GENESIS_HASH = "0" * 64
EVENT_TYPE = "TRAJECTORY_HEURISTIC_RECOMMENDATION"
PHASE = "PRE_EXECUTION"


class RecommendationAuditError(ValueError):
    """Raised when an audit ledger violates its contract."""


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _read_events(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                raise RecommendationAuditError(f"blank ledger line at {line_number}")
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RecommendationAuditError(f"invalid JSON at ledger line {line_number}") from exc
            if not isinstance(event, dict):
                raise RecommendationAuditError(f"ledger line {line_number} must be an object")
            events.append(event)
    return events


def verify_ledger(path: str | os.PathLike[str]) -> dict[str, Any]:
    """Verify contiguous sequence numbers and the complete event hash chain."""
    events = _read_events(Path(path))
    previous_hash = GENESIS_HASH
    for expected_sequence, event in enumerate(events, 1):
        if event.get("event_sequence") != expected_sequence:
            raise RecommendationAuditError(f"event sequence mismatch at position {expected_sequence}")
        if event.get("previous_event_sha256") != previous_hash:
            raise RecommendationAuditError(f"previous-event hash mismatch at sequence {expected_sequence}")
        declared_hash = event.get("event_sha256")
        payload = dict(event)
        payload.pop("event_sha256", None)
        if not isinstance(declared_hash, str) or _digest(payload) != declared_hash:
            raise RecommendationAuditError(f"event hash mismatch at sequence {expected_sequence}")
        if event.get("event_type") != EVENT_TYPE or event.get("phase") != PHASE:
            raise RecommendationAuditError(f"invalid event type/phase at sequence {expected_sequence}")
        recommendation = event.get("recommendation")
        if not isinstance(recommendation, dict):
            raise RecommendationAuditError(f"recommendation payload missing at sequence {expected_sequence}")
        try:
            expected_recommendation_hash = _digest(recommendation)
        except (TypeError, ValueError) as exc:
            raise RecommendationAuditError(
                f"recommendation payload is not canonical JSON at sequence {expected_sequence}"
            ) from exc
        if event.get("recommendation_sha256") != expected_recommendation_hash:
            raise RecommendationAuditError(
                f"recommendation hash mismatch at sequence {expected_sequence}"
            )
        previous_hash = declared_hash
    return {
        "valid": True,
        "event_count": len(events),
        "last_event_sha256": previous_hash,
        "last_event_sequence": len(events),
    }


def append_recommendation(
    path: str | os.PathLike[str],
    recommendation: dict[str, Any],
    *,
    created_at: str | None = None,
) -> dict[str, Any]:
    """Append a recommendation snapshot before execution and return its audit event."""
    if not isinstance(recommendation, dict):
        raise RecommendationAuditError("recommendation must be an object")
    if recommendation.get("output_kind") != "HEURISTIC_RANKING_NOT_PREDICTION":
        raise RecommendationAuditError("recommendation output_kind is missing or unsupported")
    try:
        recommendation_sha256 = _digest(recommendation)
    except (TypeError, ValueError) as exc:
        raise RecommendationAuditError("recommendation is not canonical-JSON serializable") from exc

    ledger_path = Path(path)
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    state = verify_ledger(ledger_path)
    previous_hash = state["last_event_sha256"]
    timestamp = created_at or datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")
    if not isinstance(timestamp, str) or not timestamp.strip():
        raise RecommendationAuditError("created_at must be a non-empty timestamp string")

    event: dict[str, Any] = {
        "event_type": EVENT_TYPE,
        "phase": PHASE,
        "event_sequence": state["last_event_sequence"] + 1,
        "created_at": timestamp,
        "recommendation_sha256": recommendation_sha256,
        "recommendation": recommendation,
        "previous_event_sha256": previous_hash,
    }
    event["event_sha256"] = _digest(event)

    # O_APPEND opens in append mode; this is not an OS-level immutability guarantee.
    descriptor = os.open(ledger_path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    with os.fdopen(descriptor, "a", encoding="utf-8") as stream:
        stream.write(_canonical_json(event) + "\n")
        stream.flush()
        os.fsync(stream.fileno())

    verify_ledger(ledger_path)
    return event
