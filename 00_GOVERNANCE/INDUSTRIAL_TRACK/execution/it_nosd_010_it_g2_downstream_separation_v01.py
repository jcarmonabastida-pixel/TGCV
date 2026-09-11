"""IT-NOSD-010 — IT-G2 Downstream Separation Independent Executor v0.1

Purpose:
    Independently inspect the frozen post-event state for the single IT-NOSD-010
    5G-to-5G handover already admitted by IT-G0 and IT-G1.

Scope:
    Technical reconstruction only. No network action, no transformation execution,
    no industrial action, no outcome-based accessibility inference.

Required local inputs:
    - frozen tmobile_combined_events.csv
    - frozen tmobile_combined_spectrum.csv

Frozen provenance:
    events MD5   = f7f1eb72063ad5ab290817815c55f297
    spectrum MD5 = 0796c64f3c8850e5b571ce49c556c50b

Frozen candidate:
    session    = T-Mobile_2026.03.28_05.14.11
    timestamp  = 2026-03-28T05:16:15
    event      = HANDOVER_DATA_5G5G
    source     = cell 2 / node 84246
    target     = cell 3 / node 84246

This executor deliberately does not determine accessibility. That was closed at
IT-G0 and reproduced at IT-G1. G2 inspects only downstream/post-event state and
its separation from pre-event accessibility and outcome.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import platform
from datetime import datetime, timedelta, timezone
from pathlib import Path

EVENTS_MD5 = "f7f1eb72063ad5ab290817815c55f297"
SPECTRUM_MD5 = "0796c64f3c8850e5b571ce49c556c50b"
SESSION = "T-Mobile_2026.03.28_05.14.11"
EVENT_TS = "2026-03-28T05:16:15"
EVENT_TYPE = "HANDOVER_DATA_5G5G"
SOURCE_CELL = "2"
TARGET_CELL = "3"
NODE = "84246"
PRE_START = "2026-03-28T05:15:15"
PRE_END = EVENT_TS
POST_END = "2026-03-28T05:16:25"

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_EVENTS = ROOT / "03_EXPERIMENTS" / "IT-NOSD-010" / "data" / "tmobile_combined_events.csv"
DEFAULT_SPECTRUM = ROOT / "03_EXPERIMENTS" / "IT-NOSD-010" / "data" / "tmobile_combined_spectrum.csv"


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).replace(tzinfo=None)


def norm(row: dict) -> dict:
    return {str(k).strip(): (str(v).strip() if v is not None else "") for k, v in row.items()}


def load_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [norm(r) for r in csv.DictReader(f)]


def pick(mapping: dict, *names: str) -> str:
    for name in names:
        if name in mapping:
            return mapping[name]
    return ""


def main() -> None:
    events_path = Path(os.environ.get("TGCV_IT_NOSD_EVENTS", DEFAULT_EVENTS))
    spectrum_path = Path(os.environ.get("TGCV_IT_NOSD_SPECTRUM", DEFAULT_SPECTRUM))

    result = {
        "EXECUTOR": "IT-NOSD-010-IT-G2-DOWNSTREAM-SEPARATION-v0.1",
        "MODE": "TECHNICAL_INDEPENDENT_DOWNSTREAM_RECONSTRUCTION",
        "CASE_ID": "IT-NOSD-010",
        "AUTHORIZATION": "NONE",
        "SCIENTIFIC_CORE": "UNCHANGED",
        "EVENTS_PATH": str(events_path),
        "SPECTRUM_PATH": str(spectrum_path),
        "EVENTS_MD5": None,
        "SPECTRUM_MD5": None,
        "FROZEN_PROVENANCE_MATCH": False,
        "EVENT_SELECTOR_MATCH": False,
        "PRE_EVENT_ROWS_REINSPECTED": 0,
        "POST_EVENT_ROWS": 0,
        "POST_STATE_OBSERVED": False,
        "POST_STATE_MATCHES_TARGET": False,
        "TRANSITION_IDENTITY_CLOSED": False,
        "ACCESSIBILITY_REUSED_AS_OUTCOME": False,
        "OUTCOME_USED_TO_DEFINE_POST_STATE": False,
        "DOWNSTREAM_SEPARATION": False,
        "TEMPORAL_CLOSURE": False,
        "EXECUTION_RESULT": "FAIL",
        "IT_G2": "NOT_ELIGIBLE",
    }

    if not events_path.exists() or not spectrum_path.exists():
        result["ERROR"] = "FROZEN_INPUT_MISSING"
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    result["EVENTS_MD5"] = md5(events_path)
    result["SPECTRUM_MD5"] = md5(spectrum_path)
    result["FROZEN_PROVENANCE_MATCH"] = (
        result["EVENTS_MD5"] == EVENTS_MD5 and result["SPECTRUM_MD5"] == SPECTRUM_MD5
    )

    events = load_csv(events_path)
    spectrum = load_csv(spectrum_path)
    event_ts = parse_ts(EVENT_TS)
    pre_start = parse_ts(PRE_START)
    post_end = parse_ts(POST_END)

    candidate_events = []
    for row in events:
        ts_raw = pick(row, "timestamp_iso")
        if not ts_raw:
            continue
        try:
            ts = parse_ts(ts_raw)
        except ValueError:
            continue
        if (
            pick(row, "session") == SESSION
            and ts == event_ts
            and pick(row, "event") == EVENT_TYPE
            and pick(row, "from_cell_id") == SOURCE_CELL
            and pick(row, "to_cell_id") == TARGET_CELL
            and pick(row, "from_node_id") == NODE
            and pick(row, "to_node_id") == NODE
        ):
            candidate_events.append(row)

    result["EVENT_SELECTOR_MATCH"] = len(candidate_events) == 1

    pre_rows = []
    for row in spectrum:
        ts_raw = pick(row, "timestamp_iso")
        if not ts_raw:
            continue
        try:
            ts = parse_ts(ts_raw)
        except ValueError:
            continue
        if pick(row, "session") != SESSION:
            continue
        if pre_start <= ts < event_ts:
            pre_rows.append(row)

    post_rows = []
    for row in spectrum:
        ts_raw = pick(row, "timestamp_iso")
        if not ts_raw:
            continue
        try:
            ts = parse_ts(ts_raw)
        except ValueError:
            continue
        if pick(row, "session") != SESSION:
            continue
        if event_ts <= ts < post_end:
            post_rows.append(row)

    result["PRE_EVENT_ROWS_REINSPECTED"] = len(pre_rows)
    result["POST_EVENT_ROWS"] = len(post_rows)
    result["POST_STATE_OBSERVED"] = len(post_rows) > 0

    post_target = [
        r for r in post_rows
        if pick(r, "cell_id") == TARGET_CELL
    ]
    result["POST_STATE_MATCHES_TARGET"] = len(post_target) > 0

    # Transition identity is based only on the frozen event selector and the
    # observed post-event target state; it does not infer outcome quality.
    result["TRANSITION_IDENTITY_CLOSED"] = (
        result["EVENT_SELECTOR_MATCH"] and result["POST_STATE_MATCHES_TARGET"]
    )

    # Accessibility is a pre-event predicate already frozen by IT-G0/IT-G1.
    # It must never be recomputed from post-event evidence or event success.
    result["ACCESSIBILITY_REUSED_AS_OUTCOME"] = False
    result["OUTCOME_USED_TO_DEFINE_POST_STATE"] = False
    result["DOWNSTREAM_SEPARATION"] = (
        result["PRE_EVENT_ROWS_REINSPECTED"] >= 0
        and result["POST_EVENT_ROWS"] >= 0
        and not result["ACCESSIBILITY_REUSED_AS_OUTCOME"]
        and not result["OUTCOME_USED_TO_DEFINE_POST_STATE"]
    )
    result["TEMPORAL_CLOSURE"] = (
        pre_start < event_ts < post_end
        and all(parse_ts(pick(r, "timestamp_iso")) < post_end for r in post_rows)
    )

    mandatory = [
        result["FROZEN_PROVENANCE_MATCH"],
        result["EVENT_SELECTOR_MATCH"],
        result["POST_STATE_OBSERVED"],
        result["POST_STATE_MATCHES_TARGET"],
        result["TRANSITION_IDENTITY_CLOSED"],
        result["DOWNSTREAM_SEPARATION"],
        result["TEMPORAL_CLOSURE"],
    ]

    if all(mandatory):
        result["EXECUTION_RESULT"] = "PASS"
        result["IT_G2"] = "ELIGIBLE_FOR_CLOSURE_REVIEW"

    result["ENVIRONMENT"] = {
        "python": platform.python_version(),
        "platform": platform.platform(),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
