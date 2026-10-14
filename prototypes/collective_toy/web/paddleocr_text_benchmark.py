import json
import os
import re
import time
from pathlib import Path

from paddleocr import PaddleOCR

ROOT = Path(__file__).resolve().parent
FIXTURE_DIR = Path(os.environ.get("TGCV_PADDLEOCR_FIXTURE_DIR", ROOT / "paddleocr-fixtures"))
OUTPUT = Path(os.environ.get("TGCV_PADDLEOCR_OUTPUT", ROOT / "paddleocr-result.json"))


def distance(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def normalize(text):
    return re.sub(r"[ \t]+", " ", text.replace("\r", "")).strip()


def cer(reference, actual):
    return distance(reference, actual) / len(reference) if reference else (0.0 if not actual else 1.0)


def wer(reference, actual):
    ref, hyp = reference.split(), actual.split()
    return distance(ref, hyp) / len(ref) if ref else (0.0 if not hyp else 1.0)


def main():
    expected = json.loads((FIXTURE_DIR / "expected.json").read_text(encoding="utf-8"))
    # All processing is local to the CI runner; no external OCR API receives fixture images.
    engine = PaddleOCR(use_angle_cls=False, lang="latin", show_log=False)
    results = []
    for fixture in expected:
        image = FIXTURE_DIR / (fixture["id"] + ".png")
        started = time.perf_counter()
        raw = engine.ocr(str(image), cls=False)
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
        words = []
        for page_result in (raw or []):
            for item in (page_result or []):
                if item and len(item) > 1 and item[1] and item[1][0]:
                    box, text = item[0], item[1][0]
                    y = sum(point[1] for point in box) / len(box)
                    x = sum(point[0] for point in box) / len(box)
                    words.append((y, x, text))
        # Reading order: top-to-bottom then left-to-right; preserve each detected region's text.
        words.sort(key=lambda row: (round(row[0] / 24), row[1]))
        recognized = normalize("\n".join(row[2] for row in words))
        reference = normalize("\n".join(fixture["lines"]))
        results.append({
            "id": fixture["id"],
            "expected": reference,
            "recognized": recognized,
            "cer": cer(reference, recognized),
            "wer": wer(reference, recognized),
            "elapsed_ms": elapsed_ms,
            "detected_regions": len(words),
            "fixture": image.name,
        })
    report = {
        "schema": "tgcv-paddleocr-text-benchmark-v1",
        "engine": "PaddleOCR (CPU; Latin recognition model)",
        "scope": "Text-only comparison on the same five synthetic fixtures as the Tesseract baseline; not a graph-structure evaluation.",
        "processing": "Local inference; no fixture images uploaded to an external OCR service.",
        "fixture_count": len(results),
        "mean_cer": sum(row["cer"] for row in results) / len(results),
        "mean_wer": sum(row["wer"] for row in results) / len(results),
        "results": results,
        "gate_pass": False,
        "gate_note": "No acceptance decision is made from this first comparison; compare against the recorded Tesseract report and expand fixtures before selecting an engine.",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
