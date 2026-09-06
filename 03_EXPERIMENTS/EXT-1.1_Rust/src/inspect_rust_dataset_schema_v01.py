from pathlib import Path
import zipfile
import csv
import io
import json
import sys

ZIP_PATH = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
MAX_PREVIEW_BYTES = 64 * 1024
MAX_FILES_TO_INSPECT = 50


def classify(name):
    n = name.lower()
    if n.endswith(".csv"):
        return "CSV"
    if n.endswith(".json"):
        return "JSON"
    if n.endswith(".jsonl"):
        return "JSONL"
    if n.endswith(".parquet"):
        return "PARQUET"
    if n.endswith(".tsv"):
        return "TSV"
    if n.endswith(".txt"):
        return "TEXT"
    return "OTHER"


def inspect_text(zf, info):
    raw = zf.open(info).read(MAX_PREVIEW_BYTES)
    text = raw.decode("utf-8", errors="replace")
    kind = classify(info.filename)
    print(f"\n--- {info.filename} [{kind}] ---")
    print(f"compressed={info.compress_size} bytes")
    print(f"uncompressed={info.file_size} bytes")

    if kind in ("CSV", "TSV"):
        delimiter = "\t" if kind == "TSV" else ","
        reader = csv.reader(io.StringIO(text), delimiter=delimiter)
        rows = []
        for i, row in enumerate(reader):
            rows.append(row)
            if i >= 3:
                break
        if rows:
            print("COLUMNS:")
            print(json.dumps(rows[0], ensure_ascii=False))
            print("SAMPLE_ROWS:")
            for row in rows[1:]:
                print(json.dumps(row, ensure_ascii=False))
    elif kind in ("JSON", "JSONL"):
        print("PREVIEW:")
        print(text[:4000])
    else:
        print("TEXT_PREVIEW:")
        print(text[:2000])


def main():
    print("TGCV EXT-1.1 — Rust dataset schema inspector v0.1")
    print("=" * 60)
    print(f"ZIP: {ZIP_PATH}")

    if not ZIP_PATH.exists():
        print("\nERROR: ZIP not found.")
        print("Expected:", ZIP_PATH)
        sys.exit(2)

    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        infos = zf.infolist()
        print(f"\nTOTAL ZIP ENTRIES: {len(infos)}")
        files = [x for x in infos if not x.is_dir()]
        print(f"TOTAL FILES: {len(files)}")

        print("\nFILE INVENTORY:")
        for info in files:
            print(f"{classify(info.filename):8} {info.file_size:14} bytes  {info.filename}")

        candidates = [x for x in files if classify(x.filename) in ("CSV", "TSV", "JSON", "JSONL", "TEXT")]
        print("\nCANDIDATE TEXT/DATA FILES:", len(candidates))
        for info in candidates[:MAX_FILES_TO_INSPECT]:
            inspect_text(zf, info)
        if len(candidates) > MAX_FILES_TO_INSPECT:
            print(f"\n[Only first {MAX_FILES_TO_INSPECT} candidate files inspected]")

    print("\nDONE.")
    print("No extraction was performed.")
    print("No complete dataset was loaded into memory.")


if __name__ == "__main__":
    main()
