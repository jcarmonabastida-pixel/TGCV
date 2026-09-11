"""IT-NOSD-010 bounded pre-outcome accessibility gate.

Technical local executor only. It does not authorize IT-G1 or industrial execution.
It evaluates one frozen candidate event using only records strictly earlier than the
candidate timestamp. The operational accessibility predicate is deliberately narrow:
for a candidate 5G->5G handover, the target cell must be independently observable in
pre-event spectrum data for the same session/operator/network, while the event record
identifies the source and target. No post-event row or handover outcome is used.
"""
from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "03_EXPERIMENTS" / "IT-NOSD-010_EVENT_INSPECTION"
EVENTS = DATA / "tmobile_combined_events.csv"
SPECTRUM = DATA / "tmobile_combined_spectrum.csv"
OUT = DATA / "IT_NOSD_010_ACCESSIBILITY_GATE_RESULT_001.json"

EXPECTED_EVENTS_MD5 = "f7f1eb72063ad5ab290817815c55f297"
EXPECTED_SPECTRUM_MD5 = "0796c64f3c8850e5b571ce49c556c50b"
TARGET_SESSION = "T-Mobile_2026.03.28_05.14.11"
TARGET_TS = datetime.fromisoformat("2026-03-28T05:16:15")
TARGET_SOURCE_CELL = "2"
TARGET_CELL = "3"


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("_", "T"))


def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    result = {
        "STATUS": "BLOCKED",
        "TARGET": {
            "session_id": TARGET_SESSION,
            "timestamp": TARGET_TS.isoformat(),
            "event_type": "HANDOVER_DATA_5G5G",
            "source_cell_id": TARGET_SOURCE_CELL,
            "target_cell_id": TARGET_CELL,
        },
        "FILES": {},
        "PRE_OUTCOME_RULE": {
            "rule_id": "IT-NOSD-010-A1",
            "definition": "Target cell is observable before the candidate event in spectrum data for the same session/operator/network; candidate source and target are explicitly identified by the event record.",
            "post_event_data_allowed": False,
            "event_occurrence_used_to_establish_accessibility": False,
            "complete_Tacc_enumeration_required": False,
        },
        "ASSESSMENT": {},
        "IT_G0": "NOT_STARTED",
        "IT_G1": "NOT_STARTED",
        "INDUSTRIAL_EXECUTION_AUTHORIZATION": "NONE",
    }

    if not EVENTS.exists() or not SPECTRUM.exists():
        result["STATUS"] = "BLOCKED_INPUT_MISSING"
        OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))
        return 2

    events_md5 = md5(EVENTS)
    spectrum_md5 = md5(SPECTRUM)
    result["FILES"] = {
        "events": {"path": str(EVENTS), "md5": events_md5, "expected_md5": EXPECTED_EVENTS_MD5},
        "spectrum": {"path": str(SPECTRUM), "md5": spectrum_md5, "expected_md5": EXPECTED_SPECTRUM_MD5},
    }
    if events_md5 != EXPECTED_EVENTS_MD5 or spectrum_md5 != EXPECTED_SPECTRUM_MD5:
        result["STATUS"] = "BLOCKED_INTEGRITY"
        OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))
        return 2

    events = read_csv(EVENTS)
    spectrum = read_csv(SPECTRUM)
    target_events = [r for r in events if r.get("session_id") == TARGET_SESSION and parse_ts(r.get("timestamp_iso", "")) == TARGET_TS and r.get("event_type") == "HANDOVER_DATA_5G5G"]
    if len(target_events) != 1:
        result["STATUS"] = "BLOCKED_TARGET_IDENTITY"
        result["ASSESSMENT"] = {"target_event_count": len(target_events)}
        OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))
        return 2

    ev = target_events[0]
    pre_start = TARGET_TS - timedelta(seconds=60)
    pre_rows = [r for r in spectrum if r.get("session_id") == TARGET_SESSION and parse_ts(r.get("timestamp_iso", "")) < TARGET_TS and parse_ts(r.get("timestamp_iso", "")) >= pre_start]
    target_observations = [r for r in pre_rows if r.get("operator_code") == "310260" and r.get("network_tech") == "5G" and r.get("cell_id") == TARGET_CELL]
    source_observations = [r for r in pre_rows if r.get("operator_code") == "310260" and r.get("network_tech") == "5G" and r.get("cell_id") == TARGET_SOURCE_CELL]

    source_ok = ev.get("from_cell_id") == TARGET_SOURCE_CELL
    target_ok = ev.get("to_cell_id") == TARGET_CELL
    identity_ok = ev.get("from_rat") == "5G" and ev.get("to_rat") == "5G" and ev.get("event_type") == "HANDOVER_DATA_5G5G"
    target_observable = len(target_observations) > 0
    preoutcome_ok = source_ok and target_ok and identity_ok and target_observable

    result["STATUS"] = "ACCESSIBILITY_GATE_PASS" if preoutcome_ok else "ACCESSIBILITY_GATE_FAIL"
    result["ASSESSMENT"] = {
        "candidate_event_identity": "PASS" if identity_ok else "FAIL",
        "source_state_identified_pre_outcome": "PASS" if (source_ok and len(source_observations) > 0) else "FAIL",
        "target_identifiable_pre_outcome": "PASS" if target_observable else "FAIL",
        "target_observation_count_pre_outcome": len(target_observations),
        "first_target_observation_pre_outcome": target_observations[0] if target_observations else None,
        "pre_window": {"start": pre_start.isoformat(), "end_exclusive": TARGET_TS.isoformat()},
        "accessibility_assessment": "PASS" if preoutcome_ok else "FAIL",
        "outcome_used_for_accessibility": False,
        "post_event_rows_considered": 0,
        "state_transition_reconstructable_from_frozen_event_and_pre_state": "PASS" if preoutcome_ok else "FAIL",
        "interpretation": "Bounded operational pre-outcome accessibility criterion satisfied." if preoutcome_ok else "Bounded operational pre-outcome accessibility criterion not satisfied.",
    }
    if preoutcome_ok:
        result["IT_G0"] = "ELIGIBLE_FOR_CLOSURE_REVIEW"

    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if preoutcome_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
