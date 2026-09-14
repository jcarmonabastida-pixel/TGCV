#!/usr/bin/env python3
"""TGCV C09 — KGFS / D178 resumable acquisition wrapper.

Wraps the canonical D178 audit inventory without changing its scientific logic.
A per-file HTTP failure is recorded instead of aborting the complete 74-file
acquisition. Existing verified files are reused. If all 74 files are present
with the published sizes, the canonical metadata audit is then executed.
"""
from __future__ import annotations
import json, subprocess, sys, time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from RUN_KGFS_D178_AUDIT import (
    D178_HDL, EXPECTED_SIZES, BASE_URL, BASELINE, ENDLINE, OUTPUT,
    VERIFIED_FILE_ID, VERIFIED_FILE_LABEL, classify, load_cache, save_cache,
    resolve_file_id, sha256, main as canonical_main,
)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/139 Safari/537.36"


def download_resilient(file_id, destination):
    url = f"{BASE_URL}/api/access/datafile/{file_id}?format=original"
    destination.parent.mkdir(parents=True, exist_ok=True)
    last_error = None
    for attempt in range(1, 4):
        req = Request(url, headers={
            "User-Agent": UA,
            "Accept": "application/octet-stream,*/*;q=0.8",
            "Referer": "https://isps.yale.edu/research/data/d178",
            "Connection": "close",
        })
        try:
            with urlopen(req, timeout=600) as r, open(destination, "wb") as f:
                while True:
                    chunk = r.read(1024 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
            return destination.stat().st_size, "urllib"
        except Exception as e:
            last_error = e
            if isinstance(e, HTTPError) and e.code not in (403, 429, 500, 502, 503, 504):
                break
            time.sleep(2 * attempt)

    if sys.platform.startswith("win"):
        curl = [
            "curl.exe", "-L", "--http1.1", "--retry", "3", "--retry-delay", "2",
            "--retry-all-errors", "-A", UA,
            "-H", "Accept: application/octet-stream,*/*;q=0.8",
            "-H", "Referer: https://isps.yale.edu/research/data/d178",
            "-o", str(destination), url,
        ]
        try:
            subprocess.check_call(curl, timeout=900)
            return destination.stat().st_size, "curl"
        except Exception as e:
            last_error = e

    raise RuntimeError(str(last_error))


def main():
    needed = [f"D178F{i:02d}" for i in range(3, 77)]
    cache = load_cache()
    cache[VERIFIED_FILE_LABEL] = VERIFIED_FILE_ID
    save_cache(cache)
    statuses = []

    print("=== TGCV C09 — KGFS / D178 RESUMABLE ACQUISITION ===")
    print(f"Inventory: {len(needed)}/74 canonical files")

    for idx, label in enumerate(needed, 1):
        n = int(label[5:])
        category = classify(n)
        destination = (BASELINE if category == "BASELINE" else ENDLINE) / f"{label}.dta"
        expected = EXPECTED_SIZES[label]
        hdl = D178_HDL[label]

        try:
            if label in cache:
                file_id = int(cache[label])
                source = "cache"
            else:
                file_id, _ = resolve_file_id(hdl)
                cache[label] = file_id
                save_cache(cache)
                source = "resolved"

            if destination.exists() and destination.stat().st_size == expected:
                size = expected
                method = "reused"
            else:
                size, method = download_resilient(file_id, destination)

            if size != expected:
                raise RuntimeError(f"size={size}, expected={expected}")
            digest = sha256(destination)
            statuses.append({"file_name": label, "status": "PASS", "file_id": file_id,
                             "size_bytes": size, "expected_size_bytes": expected,
                             "sha256": digest, "source": source, "method": method})
            print(f"  {idx}/74 {label}: PASS", flush=True)
        except Exception as e:
            statuses.append({"file_name": label, "status": "BLOCKED", "file_id": cache.get(label),
                             "expected_size_bytes": expected, "error": str(e)})
            print(f"  {idx}/74 {label}: BLOCKED — {e}", flush=True)

    blocked = [x for x in statuses if x["status"] == "BLOCKED"]
    report = {
        "audit": "TGCV_C09_KGFS_D178_RESUMABLE_ACQUISITION",
        "file_count": 74,
        "passed": len(statuses) - len(blocked),
        "blocked": len(blocked),
        "scientific_claim_status": "NO_C09_UPGRADE",
        "statuses": statuses,
    }
    path = OUTPUT / "KGFS_D178_RESUMABLE_ACQUISITION_STATUS.json"
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nAcquisition result: PASS={report['passed']} BLOCKED={report['blocked']}")
    if blocked:
        print("Scientific status: NO C09 UPGRADE; acquisition remains technically open.")
        print(f"Blocked files: {', '.join(x['file_name'] for x in blocked)}")
        print(f"Status file: {path}")
        return 2

    print("All 74 files acquired and size-verified. Running canonical metadata audit...")
    canonical_main()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
