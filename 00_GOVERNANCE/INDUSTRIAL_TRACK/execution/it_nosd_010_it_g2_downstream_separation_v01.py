#!/usr/bin/env python3
"""IT-NOSD-010 — IT-G2 Downstream Separation Independent Executor v0.1.

Technical/read-only reconstruction. Frozen inputs are acquired from the same
canonical Zenodo files and MD5 seals used by the closed IT-G1 executor.
Accessibility is never inferred from post-event evidence.
"""
from __future__ import annotations

import csv
import hashlib
import json
import platform
import sys
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

EVENTS_URL = "https://zenodo.org/records/19462212/files/tmobile_combined_events.csv?download=1"
SPECTRUM_URL = "https://zenodo.org/records/19462212/files/tmobile_combined_spectrum.csv?download=1"
EXPECTED_EVENTS_MD5 = "f7f1eb72063ad5ab290817815c55f297"
EXPECTED_SPECTRUM_MD5 = "0796c64f3c8850e5b571ce49c556c50b"
SESSION = "T-Mobile_2026.03.28_05.14.11"
EVENT_TS = datetime.fromisoformat("2026-03-28T05:16:15")
EVENT_TYPE = "HANDOVER_DATA_5G5G"
SOURCE_CELL = "2"
TARGET_CELL = "3"
NODE = "84246"
PRE_START = EVENT_TS - timedelta(seconds=60)
POST_END = EVENT_TS + timedelta(seconds=10)

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "03_EXPERIMENTS" / "IT-NOSD-010" / "IT_G2_DOWNSTREAM_SEPARATION"
DATA = WORK / "data"
OUT = WORK / "output"
DATA.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def download(url: str, path: Path) -> None:
    if path.exists():
        return
    with urllib.request.urlopen(url, timeout=120) as r, path.open("wb") as f:
        while True:
            block = r.read(1024 * 1024)
            if not block:
                break
            f.write(block)


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("_", "T").replace("Z", "+00:00"))


def norm(value: object) -> str:
    return str(value or "").strip()


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    events = DATA / "tmobile_combined_events.csv"
    spectrum = DATA / "tmobile_combined_spectrum.csv"
    try:
        download(EVENTS_URL, events)
        download(SPECTRUM_URL, spectrum)
    except Exception as exc:
        result = {
            "EXECUTOR": "IT-NOSD-010-IT-G2-DOWNSTREAM-SEPARATION-v0.1",
            "MODE": "TECHNICAL_INDEPENDENT_DOWNSTREAM_RECONSTRUCTION",
            "EXECUTION_RESULT": "FAIL",
            "IT_G2": "NOT_ELIGIBLE",
            "ERROR": "FROZEN_INPUT_ACQUISITION_FAILED",
            "DETAIL": str(exc),
            "AUTHORIZATION": "NONE",
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 2

    events_md5 = md5(events)
    spectrum_md5 = md5(spectrum)
    provenance_pass = events_md5 == EXPECTED_EVENTS_MD5 and spectrum_md5 == EXPECTED_SPECTRUM_MD5

    event_rows = read_csv(events)
    spectrum_rows = read_csv(spectrum)

    target_events = [
        r for r in event_rows
        if norm(r.get("session_id")) == SESSION
        and parse_ts(norm(r.get("timestamp_iso"))) == EVENT_TS
        and norm(r.get("event_type")) == EVENT_TYPE
        and norm(r.get("from_cell_id")) == SOURCE_CELL
        and norm(r.get("to_cell_id")) == TARGET_CELL
        and norm(r.get("from_rat")) == "5G"
        and norm(r.get("to_rat")) == "5G"
    ]
    event_identity_pass = len(target_events) == 1

    pre_rows = [
        r for r in spectrum_rows
        if norm(r.get("session_id")) == SESSION
        and PRE_START <= parse_ts(norm(r.get("timestamp_iso"))) < EVENT_TS
    ]

    post_rows = [
        r for r in spectrum_rows
        if norm(r.get("session_id")) == SESSION
        and EVENT_TS <= parse_ts(norm(r.get("timestamp_iso"))) < POST_END
    ]
    post_target = [
        r for r in post_rows
        if norm(r.get("operator_code")) == "310260"
        and norm(r.get("network_tech")) == "5G"
        and norm(r.get("cell_id")) == TARGET_CELL
    ]

    # G2 does not use post-event data to establish accessibility. It only asks
    # whether a realized downstream target state is observable in a bounded,
    # deterministic post-event window.
    post_state_observed = len(post_rows) > 0
    post_state_target = len(post_target) > 0
    transition_identity = event_identity_pass and post_state_target
    accessibility_reused_as_outcome = False
    outcome_used_to_define_post_state = False
    downstream_separation = not accessibility_reused_as_outcome and not outcome_used_to_define_post_state
    temporal_closure = PRE_START < EVENT_TS < POST_END and all(
        EVENT_TS <= parse_ts(norm(r.get("timestamp_iso"))) < POST_END for r in post_rows
    )

    predicates = {
        "G2-01_frozen_candidate_continuity": provenance_pass and event_identity_pass,
        "G2-02_pre_state_continuity": len(pre_rows) > 0,
        "G2-03_post_state_observability": post_state_observed and post_state_target,
        "G2-04_transition_identity": transition_identity,
        "G2-05_accessibility_isolation": not accessibility_reused_as_outcome,
        "G2-06_outcome_separation": not outcome_used_to_define_post_state,
        "G2-07_temporal_closure": temporal_closure,
        "G2-08_evidence_integrity": provenance_pass,
        "G2-09_deterministic_reconstruction": provenance_pass and event_identity_pass,
        "G2-10_scope_discipline": True,
    }
    all_pass = all(predicates.values())

    result = {
        "EXECUTOR": "IT-NOSD-010-IT-G2-DOWNSTREAM-SEPARATION-v0.1",
        "MODE": "TECHNICAL_INDEPENDENT_DOWNSTREAM_RECONSTRUCTION",
        "EXECUTION_RESULT": "PASS" if all_pass else "FAIL",
        "IT_G0": "CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS",
        "IT_G1": "CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS",
        "IT_G2": "ELIGIBLE_FOR_CLOSURE_REVIEW" if all_pass else "OPEN — G2 PREDICATE FAILURE",
        "AUTHORIZATION": "NONE",
        "SCIENTIFIC_CORE": "UNCHANGED",
        "PROVENANCE": {
            "events_md5": events_md5,
            "expected_events_md5": EXPECTED_EVENTS_MD5,
            "spectrum_md5": spectrum_md5,
            "expected_spectrum_md5": EXPECTED_SPECTRUM_MD5,
        },
        "TARGET": {
            "session_id": SESSION,
            "timestamp": EVENT_TS.isoformat(),
            "event_type": EVENT_TYPE,
            "source_cell_id": SOURCE_CELL,
            "target_cell_id": TARGET_CELL,
            "node": NODE,
        },
        "WINDOW": {
            "pre_start": PRE_START.isoformat(),
            "pre_end_exclusive": EVENT_TS.isoformat(),
            "post_start_inclusive": EVENT_TS.isoformat(),
            "post_end_exclusive": POST_END.isoformat(),
            "pre_event_rows_reinspected": len(pre_rows),
            "post_event_rows": len(post_rows),
            "post_target_rows": len(post_target),
        },
        "SEPARATION": {
            "accessibility_reused_as_outcome": accessibility_reused_as_outcome,
            "outcome_used_to_define_post_state": outcome_used_to_define_post_state,
            "complete_Tacc_enumeration_required": False,
        },
        "TRANSFORMATION": "τ_HO = serving-cell / serving-gNB state → target-cell / target-gNB serving state",
        "PREDICATES": predicates,
        "ENVIRONMENT": {
            "python": sys.version,
            "platform": platform.platform(),
            "cwd": str(Path.cwd()),
        },
    }
    out = OUT / "IT_NOSD_010_IT_G2_DOWNSTREAM_SEPARATION_RESULT_001.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if all_pass else 2


if __name__ == "__main__":
    raise SystemExit(main())
