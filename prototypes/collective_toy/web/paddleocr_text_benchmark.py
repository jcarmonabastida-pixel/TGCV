import hashlib
import json
import os
import re
import time
from pathlib import Path

from paddleocr import PaddleOCR

ROOT = Path(__file__).resolve().parent
FIXTURE_DIR = Path(os.environ.get("TGCV_PADDLEOCR_FIXTURE_DIR", ROOT / "paddleocr-fixtures"))
OUTPUT = Path(os.environ.get("TGCV_PADDLEOCR_OUTPUT", ROOT / "paddleocr-result.json"))
WARM_REPEATS = 3


def distance(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def normalize(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")).strip()


def cer(reference, actual):
    return distance(reference, actual) / len(reference) if reference else (0.0 if not actual else 1.0)


def wer(reference, actual):
    ref, hyp = reference.split(), actual.split()
    return distance(ref, hyp) / len(ref) if ref else (0.0 if not hyp else 1.0)


def recognize(engine, image):
    raw = engine.ocr(str(image), cls=False)
    regions = []
    for page_result in (raw or []):
        for item in (page_result or []):
            if item and len(item) > 1 and item[1] and item[1][0]:
                box, text = item[0], item[1][0]
                y = sum(point[1] for point in box) / len(box)
                x = sum(point[0] for point in box) / len(box)
                regions.append((y, x, text))
    regions.sort(key=lambda row: (round(row[0] / 24), row[1]))
    return normalize("\n".join(row[2] for row in regions)), len(regions)


def main():
    expected = json.loads((FIXTURE_DIR / "expected.json").read_text(encoding="utf-8"))
    manifest = json.loads((FIXTURE_DIR / "manifest.json").read_text(encoding="utf-8"))
    manifest_by_id = {item["id"]: item for item in manifest["fixtures"]}
    if len(expected) != 5 or len(manifest_by_id) != 5:
        raise RuntimeError("Expected exactly five frozen text fixtures.")
    if set(item["id"] for item in expected) != set(manifest_by_id):
        raise RuntimeError("Fixture IDs differ between expected.json and manifest.json.")

    for fixture in expected:
        entry = manifest_by_id[fixture["id"]]
        image = FIXTURE_DIR / entry["file"]
        digest = hashlib.sha256(image.read_bytes()).hexdigest()
        if digest != entry["sha256"]:
            raise RuntimeError("Fixture SHA-256 mismatch: " + fixture["id"])
        if image.name != fixture["id"] + ".png":
            raise RuntimeError("Unexpected fixture filename: " + fixture["id"])

    # Initialization is measured separately from first and warm inference.
    init_start = time.perf_counter()
    engine = PaddleOCR(use_angle_cls=False, lang="latin", show_log=False)
    engine_init_ms = round((time.perf_counter() - init_start) * 1000, 3)

    results = []
    for fixture in expected:
        image = FIXTURE_DIR / manifest_by_id[fixture["id"]]["file"]
        reference = normalize("\n".join(fixture["lines"]))
        first_start = time.perf_counter()
        first_text, detected_regions = recognize(engine, image)
        first_inference_ms = round((time.perf_counter() - first_start) * 1000, 3)
        warm_samples = []
        for _ in range(WARM_REPEATS):
            started = time.perf_counter()
            text, count = recognize(engine, image)
            elapsed = round((time.perf_counter() - started) * 1000, 3)
            warm_samples.append({"elapsed_ms": elapsed, "recognized": text})
            detected_regions = count
        recognized = warm_samples[-1]["recognized"]
        expected_lines = reference.split("\n")
        recognized_lines = recognized.split("\n")
        identifier_lines = [
            line for line in expected_lines
            if re.fullmatch(r"[A-Z]", line)
            or line.startswith("Nodo_")
            or line.startswith("Nodo-")
            or re.match(r"^T\d+:", line)
        ]
        identifier_exact = all(line in recognized_lines for line in identifier_lines)
        results.append({
            "id": fixture["id"],
            "expected": reference,
            "recognized_first_raw": first_text,
            "recognized": recognized,
            "cer": cer(reference, recognized),
            "wer": wer(reference, recognized),
            "first_inference_ms": first_inference_ms,
            "warm_inference_ms_samples": [sample["elapsed_ms"] for sample in warm_samples],
            "warm_inference_ms_mean": round(sum(sample["elapsed_ms"] for sample in warm_samples) / len(warm_samples), 3),
            "detected_regions": detected_regions,
            "fixture": image.name,
            "fixture_sha256": manifest_by_id[fixture["id"]]["sha256"],
            "identifier_lines_expected": identifier_lines,
            "identifier_exact": identifier_exact,
            "exact_lines": all(line in recognized_lines for line in expected_lines),
        })

    report = {
        "schema": "tgcv-paddleocr-text-benchmark-v2",
        "engine": "PaddleOCR (CPU; Latin recognition model)",
        "scope": "Text-only comparison on byte-identical synthetic fixtures; not a graph-structure evaluation.",
        "processing": "Local inference; no fixture images uploaded to an external OCR service.",
        "fixture_count": len(results),
        "fixture_manifest_sha256": hashlib.sha256((FIXTURE_DIR / "manifest.json").read_bytes()).hexdigest(),
        "engine_init_ms": engine_init_ms,
        "warm_repeats_per_fixture": WARM_REPEATS,
        "mean_cer": sum(row["cer"] for row in results) / len(results),
        "mean_wer": sum(row["wer"] for row in results) / len(results),
        "results": results,
        "gate_pass": False,
        "gate_note": "Comparison report only; acceptance remains closed pending paired audit, exact identifier checks, expanded fixtures, and predeclared thresholds."
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
