import csv
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path

BASE = Path("03_EXPERIMENTS/IT-NOSD-010_EVENT_INSPECTION")
EVENTS = BASE / "tmobile_combined_events.csv"
SPECTRUM = BASE / "tmobile_combined_spectrum.csv"
OUT = BASE / "IT_NOSD_010_CANDIDATE_PREOUTCOME_INSPECTION_RESULT_001.json"
TARGET_SESSION = "T-Mobile_2026.03.28_05.14.11"
TARGET_TIMESTAMP = "2026-03-28T05:16:15"
TARGET_EVENT_TYPE = "HANDOVER_DATA_5G5G"
PRE_WINDOW_SECONDS = 60
POST_WINDOW_SECONDS = 10

def md5(path):
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def parse_ts(value):
    if not value:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y.%m.%d_%H.%M.%S"):
        try:
            return datetime.strptime(value.strip(), fmt)
        except ValueError:
            pass
    return None

def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

result = {
    "STATUS": None,
    "TARGET": {"session_id": TARGET_SESSION, "timestamp": TARGET_TIMESTAMP,
               "event_type": TARGET_EVENT_TYPE, "pre_window_seconds": PRE_WINDOW_SECONDS,
               "post_window_seconds": POST_WINDOW_SECONDS},
    "FILES": {}, "CANDIDATE_EVENT": None, "PRE_EVENT_ROWS": [],
    "POST_EVENT_ROWS": [], "SPECTRUM_COLUMNS": [], "SPECTRUM_PRE_EVENT_ROWS": [],
    "ACCESSIBILITY_ASSESSMENT": "OPEN", "OUTCOME_USED_FOR_ACCESSIBILITY": False,
    "STATE_TRANSITION_ASSESSMENT": "OPEN", "IT_G0": "NOT_STARTED",
    "IT_G1": "NOT_STARTED", "INDUSTRIAL_EXECUTION_AUTHORIZATION": "NONE"
}

if not EVENTS.exists() or not SPECTRUM.exists():
    result["STATUS"] = "BLOCKED_INPUT_MISSING"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(2)

result["FILES"] = {"events": {"path": str(EVENTS), "md5": md5(EVENTS)},
                   "spectrum": {"path": str(SPECTRUM), "md5": md5(SPECTRUM)}}
events = read_csv(EVENTS)
spectrum = read_csv(SPECTRUM)
result["SPECTRUM_COLUMNS"] = list(spectrum[0].keys()) if spectrum else []
target = next((r for r in events if r.get("session_id") == TARGET_SESSION
               and r.get("timestamp_iso") == TARGET_TIMESTAMP
               and r.get("event_type") == TARGET_EVENT_TYPE), None)

if target is None:
    result["STATUS"] = "TARGET_NOT_FOUND"
else:
    result["CANDIDATE_EVENT"] = target
    t0 = parse_ts(TARGET_TIMESTAMP)
    pre0 = t0 - timedelta(seconds=PRE_WINDOW_SECONDS)
    post1 = t0 + timedelta(seconds=POST_WINDOW_SECONDS)
    for row in events:
        if row.get("session_id") != TARGET_SESSION:
            continue
        rt = parse_ts(row.get("timestamp_iso") or row.get("timestamp"))
        if rt is None:
            continue
        if pre0 <= rt <= t0:
            result["PRE_EVENT_ROWS"].append(row)
        elif t0 < rt <= post1:
            result["POST_EVENT_ROWS"].append(row)
    time_keys = [k for k in result["SPECTRUM_COLUMNS"]
                 if k.lower() in {"timestamp", "timestamp_iso", "time", "datetime", "date_time"}]
    session_keys = [k for k in result["SPECTRUM_COLUMNS"]
                    if k.lower() in {"session_id", "session", "campaign_session"}]
    for row in spectrum:
        if session_keys and not any(row.get(k) == TARGET_SESSION for k in session_keys):
            continue
        rt = next((parse_ts(row.get(k)) for k in time_keys if parse_ts(row.get(k)) is not None), None)
        if rt is not None and pre0 <= rt < t0:
            result["SPECTRUM_PRE_EVENT_ROWS"].append(row)
    result["STATUS"] = "CANDIDATE_PREOUTCOME_DATA_LOCATED"

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
