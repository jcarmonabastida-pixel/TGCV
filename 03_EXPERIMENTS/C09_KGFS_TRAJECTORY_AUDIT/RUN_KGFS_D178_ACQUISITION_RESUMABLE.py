#!/usr/bin/env python3
"""TGCV C09 — KGFS / D178 resumable acquisition wrapper.

Wraps the canonical D178 audit inventory without changing its scientific logic.
A per-file HTTP failure is recorded instead of aborting the complete 74-file
acquisition. Existing verified files are reused. Truncated downloads are
recovered with bounded HTTP Range requests against the same canonical
Dataverse endpoint. If all 74 files are present with the published sizes, the
canonical metadata audit is then executed.
"""
from __future__ import annotations
import json, subprocess, sys, time
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from RUN_KGFS_D178_AUDIT import (
    D178_HDL, EXPECTED_SIZES, BASE_URL, BASELINE, ENDLINE, OUTPUT,
    VERIFIED_FILE_ID, VERIFIED_FILE_LABEL, classify, load_cache, save_cache,
    resolve_file_id, sha256, main as canonical_main,
)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/139 Safari/537.36"


def _request_headers():
    return {
        "User-Agent": UA,
        "Accept": "application/octet-stream,*/*;q=0.8",
        "Referer": "https://isps.yale.edu/research/data/d178",
        "Connection": "close",
    }


def download_range(file_id, destination, expected_size):
    """Download the exact expected byte range in bounded chunks.

    This is a transport recovery only: same fileId, same Dataverse endpoint,
    same published byte count. The assembled file must equal expected_size.
    """
    url = f"{BASE_URL}/api/access/datafile/{file_id}?format=original"
    chunk_size = 1024 * 1024
    tmp = destination.with_suffix(destination.suffix + ".range.tmp")
    if tmp.exists():
        tmp.unlink()
    with open(tmp, "wb") as out:
        start = 0
        while start < expected_size:
            end = min(start + chunk_size - 1, expected_size - 1)
            req = Request(url, headers={**_request_headers(), "Range": f"bytes={start}-{end}"})
            last_error = None
            for attempt in range(1, 4):
                try:
                    with urlopen(req, timeout=600) as r:
                        status = getattr(r, "status", r.getcode())
                        if status not in (200, 206):
                            raise RuntimeError(f"unexpected HTTP status {status} for range {start}-{end}")
                        data = r.read(end - start + 1)
                        if len(data) != end - start + 1:
                            raise RuntimeError(f"range {start}-{end}: received {len(data)} bytes")
                        out.write(data)
                        last_error = None
                        break
                except Exception as e:
                    last_error = e
                    time.sleep(2 * attempt)
            if last_error is not None:
                tmp.unlink(missing_ok=True)
                raise last_error
            start = end + 1
    actual = tmp.stat().st_size
    if actual != expected_size:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"range assembled size={actual}, expected={expected_size}")
    tmp.replace(destination)
    return actual, "http-range"


def download_resilient(file_id, destination, expected_size):
    url = f"{BASE_URL}/api/access/datafile/{file_id}?format=original"
    destination.parent.mkdir(parents=True, exist_ok=True)
    last_error = None
    for attempt in range(1, 4):
        destination.unlink(missing_ok=True)
        req = Request(url, headers=_request_headers())
        try:
            with urlopen(req, timeout=600) as r, open(destination, "wb") as f:
                while True:
                    chunk = r.read(1024 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
            size = destination.stat().st_size
            if size == expected_size:
                return size, "urllib"
            last_error = RuntimeError(f"truncated download size={size}, expected={expected_size}")
        except Exception as e:
            last_error = e
        time.sleep(2 * attempt)

    if sys.platform.startswith("win"):
        destination.unlink(missing_ok=True)
        curl = [
            "curl.exe", "-L", "--http1.1", "--retry", "3", "--retry-delay", "2",
            "--retry-all-errors", "-A", UA,
            "-H", "Accept: application/octet-stream,*/*;q=0.8",
            "-H", "Referer: https://isps.yale.edu/research/data/d178",
            "-o", str(destination), url,
        ]
        try:
            subprocess.check_call(curl, timeout=900)
            size = destination.stat().st_size
            if size == expected_size:
                return size, "curl"
            last_error = RuntimeError(f"curl truncated download size={size}, expected={expected_size}")
        except Exception as e:
            last_error = e

    # Final bounded recovery for deterministic truncation/connection cutoff.
    try:
        return download_range(file_id, destination, expected_size)
    except Exception as range_error:
        raise RuntimeError(f"full/range download failed; last_full_error={last_error}; range_error={range_error}") from range_error


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
                size, method = download_resilient(file_id, destination, expected)

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
