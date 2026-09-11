from __future__ import annotations

import csv
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

ZENODO_RECORD = "https://zenodo.org/records/19462212"
EVENTS_URL = "https://zenodo.org/records/19462212/files/tmobile_combined_events.csv?download=1"
SPECTRUM_URL = "https://zenodo.org/records/19462212/files/tmobile_combined_spectrum.csv?download=1"
EXPECTED_EVENTS_MD5 = "f7f1eb72063ad5ab290817815c55f297"
EXPECTED_SPECTRUM_MD5 = "0796c64f3c8850e5b571ce49c556c50b"
OUT_DIR = Path("03_EXPERIMENTS/IT-NOSD-010_EVENT_INSPECTION")


def download(url: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as r, path.open("wb") as f:
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def detect_columns(fieldnames: list[str]) -> dict[str, str | None]:
    lower = {x.lower().strip(): x for x in fieldnames}
    event_candidates = [x for x in fieldnames if "event" in x.lower()]
    type_candidates = [x for x in fieldnames if any(k in x.lower() for k in ("type", "name", "category", "description"))]
    time_candidates = [x for x in fieldnames if any(k in x.lower() for k in ("time", "timestamp", "date"))]
    return {
        "event": event_candidates[0] if event_candidates else None,
        "type": type_candidates[0] if type_candidates else None,
        "time": time_candidates[0] if time_candidates else None,
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    events = OUT_DIR / "tmobile_combined_events.csv"
    spectrum = OUT_DIR / "tmobile_combined_spectrum.csv"

    if not events.exists():
        print(f"DOWNLOADING={EVENTS_URL}")
        download(EVENTS_URL, events)
    if not spectrum.exists():
        print(f"DOWNLOADING={SPECTRUM_URL}")
        download(SPECTRUM_URL, spectrum)

    events_md5 = md5(events)
    spectrum_md5 = md5(spectrum)
    print(f"EVENTS_MD5={events_md5}")
    print(f"SPECTRUM_MD5={spectrum_md5}")

    integrity = {
        "EVENTS_MD5_MATCH": events_md5 == EXPECTED_EVENTS_MD5,
        "SPECTRUM_MD5_MATCH": spectrum_md5 == EXPECTED_SPECTRUM_MD5,
    }
    if not all(integrity.values()):
        result = {"STATUS": "BLOCKED_INTEGRITY", "INTEGRITY": integrity}
        (OUT_DIR / "IT_NOSD_010_EVENT_INSPECTION_RESULT_001.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))
        return 2

    with events.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        columns = detect_columns(fields)
        matches = []
        for idx, row in enumerate(reader, start=2):
            text = " | ".join(str(v or "") for v in row.values()).lower()
            if "5g-to-5g" in text or "5g to 5g" in text or "5g-5g" in text or "handover" in text and "5g" in text:
                matches.append({"row_number": idx, "row": row})
                if len(matches) >= 25:
                    break

    result = {
        "STATUS": "EVENTS_LOCATED" if matches else "NO_MATCH",
        "ZENODO_RECORD": ZENODO_RECORD,
        "FILES": {
            "events": {"path": str(events), "md5": events_md5, "expected_md5": EXPECTED_EVENTS_MD5},
            "spectrum": {"path": str(spectrum), "md5": spectrum_md5, "expected_md5": EXPECTED_SPECTRUM_MD5},
        },
        "EVENT_COLUMNS": columns,
        "MATCH_COUNT_CAPTURED": len(matches),
        "CANDIDATE_EVENTS": matches,
        "OUTCOME_USED_FOR_SELECTION": False,
        "ACCESSIBILITY_CLOSED": False,
        "IT_G0": "NOT_STARTED",
        "IT_G1": "NOT_STARTED",
        "INDUSTRIAL_EXECUTION_AUTHORIZATION": "NONE",
    }
    out = OUT_DIR / "IT_NOSD_010_EVENT_INSPECTION_RESULT_001.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
