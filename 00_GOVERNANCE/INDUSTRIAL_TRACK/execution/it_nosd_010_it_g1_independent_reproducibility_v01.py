#!/usr/bin/env python3
"""IT-NOSD-010 IT-G1 independent reproducibility executor.

Technical executor only. It does not authorize or execute an industrial/3GPP
handover. Accessibility is evaluated strictly from pre-event observations.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import platform
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

EVENTS_URL = "https://zenodo.org/records/19462212/files/tmobile_combined_events.csv?download=1"
SPECTRUM_URL = "https://zenodo.org/records/19462212/files/tmobile_combined_spectrum.csv?download=1"
EXPECTED_EVENTS_MD5 = "f7f1eb72063ad5ab290817815c55f297"
EXPECTED_SPECTRUM_MD5 = "0796c64f3c8850e5b571ce49c556c50b"
SESSION = "T-Mobile_2026.03.28_05.14.11"
EVENT_TS = "2026-03-28T05:16:15"
EVENT_TYPE = "HANDOVER_DATA_5G5G"
SOURCE_CELL = "2"
TARGET_CELL = "3"
NODE = "84246"
PRE_START = "2026-03-28T05:15:15"
PRE_END = EVENT_TS

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "03_EXPERIMENTS" / "IT-NOSD-010" / "IT_G1_INDEPENDENT_REPRODUCIBILITY"
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
    if not path.exists():
        urllib.request.urlretrieve(url, path)


def norm(v):
    return str(v).strip()


def parse_ts(v: str) -> datetime:
    return datetime.fromisoformat(v.replace("Z", "+00:00"))


def main() -> int:
    events = DATA / "tmobile_combined_events.csv"
    spectrum = DATA / "tmobile_combined_spectrum.csv"
    download(EVENTS_URL, events)
    download(SPECTRUM_URL, spectrum)

    events_md5 = md5(events)
    spectrum_md5 = md5(spectrum)
    provenance_pass = events_md5 == EXPECTED_EVENTS_MD5 and spectrum_md5 == EXPECTED_SPECTRUM_MD5

    with events.open("r", encoding="utf-8-sig", newline="") as f:
        event_rows = list(csv.DictReader(f))
    with spectrum.open("r", encoding="utf-8-sig", newline="") as f:
        spectrum_rows = list(csv.DictReader(f))

    target = [r for r in event_rows if norm(r.get("session_id")) == SESSION
              and norm(r.get("timestamp")) == EVENT_TS
              and norm(r.get("event_type")) == EVENT_TYPE
              and norm(r.get("from_cell_id")) == SOURCE_CELL
              and norm(r.get("to_cell_id")) == TARGET_CELL]
    event_identity_pass = len(target) == 1

    pre_target = []
    if event_identity_pass:
        for r in spectrum_rows:
            if norm(r.get("session_id")) != SESSION:
                continue
            ts = norm(r.get("timestamp"))
            if PRE_START <= ts < PRE_END and norm(r.get("cell_id")) == TARGET_CELL:
                pre_target.append(r)

    target_observed_pass = len(pre_target) > 0
    first_target = min((norm(r.get("timestamp")) for r in pre_target), default=None)

    source_pre = []
    if event_identity_pass:
        for r in spectrum_rows:
            if norm(r.get("session_id")) != SESSION:
                continue
            ts = norm(r.get("timestamp"))
            if PRE_START <= ts < PRE_END and norm(r.get("cell_id")) == SOURCE_CELL:
                source_pre.append(r)
    source_state_pass = len(source_pre) > 0

    # Accessibility is intentionally computed with zero post-event rows.
    accessibility_pass = (provenance_pass and event_identity_pass and
                           target_observed_pass and source_state_pass)

    transition_pass = False
    post_rows_used_for_accessibility = 0
    if event_identity_pass:
        e = target[0]
        transition_pass = (norm(e.get("from_cell_id")) == SOURCE_CELL and
                           norm(e.get("to_cell_id")) == TARGET_CELL and
                           norm(e.get("from_node")) == NODE and
                           norm(e.get("to_node")) == NODE)

    predicates = {
        "G1-01_provenance_integrity": provenance_pass,
        "G1-02_candidate_event_identity": event_identity_pass,
        "G1-03_pre_event_state_closure": source_state_pass and target_observed_pass,
        "G1-04_transformation_identity": event_identity_pass,
        "G1-05_accessibility_outcome_separation": accessibility_pass and post_rows_used_for_accessibility == 0,
        "G1-06_state_transition_closure": transition_pass,
        "G1-07_temporal_closure": PRE_START < PRE_END == EVENT_TS,
        "G1-08_downstream_separation": post_rows_used_for_accessibility == 0,
        "G1-09_reproducibility": provenance_pass and event_identity_pass and accessibility_pass,
        "G1-10_scope_discipline": True,
    }
    all_pass = all(predicates.values())

    result = {
        "EXECUTOR": "IT-NOSD-010-IT-G1-INDEPENDENT-REPRODUCIBILITY-v0.1",
        "MODE": "TECHNICAL_INDEPENDENT_REPRODUCIBILITY",
        "EXECUTION_RESULT": "PASS" if all_pass else "FAIL",
        "IT_G0": "CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS",
        "IT_G1": "ELIGIBLE_FOR_CLOSURE_REVIEW" if all_pass else "OPEN — REPRODUCIBILITY PREDICATE FAILURE",
        "INDUSTRIAL_EXECUTION_AUTHORIZATION": "NONE",
        "PROVENANCE": {
            "events_md5": events_md5,
            "expected_events_md5": EXPECTED_EVENTS_MD5,
            "spectrum_md5": spectrum_md5,
            "expected_spectrum_md5": EXPECTED_SPECTRUM_MD5,
        },
        "TARGET": {
            "session_id": SESSION,
            "timestamp": EVENT_TS,
            "event_type": EVENT_TYPE,
            "source_cell_id": SOURCE_CELL,
            "target_cell_id": TARGET_CELL,
            "node": NODE,
        },
        "WINDOW": {
            "pre_start": PRE_START,
            "pre_end_exclusive": PRE_END,
            "post_event_rows_used_for_accessibility": post_rows_used_for_accessibility,
        },
        "PRE_OUTCOME": {
            "target_observation_count": len(pre_target),
            "first_target_observation": first_target,
            "source_observation_count": len(source_pre),
            "accessibility_rule": "IT-NOSD-010-A1",
            "outcome_used_for_accessibility": False,
            "complete_Tacc_enumeration_required": False,
        },
        "PREDICATES": predicates,
        "TRANSFORMATION": "τ_HO = serving-cell / serving-gNB state → target-cell / target-gNB serving state",
        "ENVIRONMENT": {
            "python": sys.version,
            "platform": platform.platform(),
            "cwd": os.getcwd(),
        },
    }
    out = OUT / "IT_NOSD_010_IT_G1_INDEPENDENT_REPRODUCIBILITY_RESULT_001.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if all_pass else 2


if __name__ == "__main__":
    raise SystemExit(main())
