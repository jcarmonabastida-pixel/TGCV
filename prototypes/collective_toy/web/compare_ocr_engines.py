import json
import re
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TESSERACT_PATH = Path(os.environ.get("TGCV_TESSERACT_REPORT", ROOT / "ocr-quality-output" / "tgcv-ocr-quality-result.json"))
PADDLE_PATH = Path(os.environ.get("TGCV_PADDLEOCR_REPORT", ROOT / "paddleocr-result.json"))
OUTPUT = Path(os.environ.get("TGCV_OCR_PAIRED_OUTPUT", ROOT / "ocr-paired-comparison.json"))


def normalize(value):
    value = str(value or "").replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(re.sub(r"[ \t]+", " ", line).strip() for line in value.split("\n")).strip()


def edit_alignment(reference, actual):
    n, m = len(reference), len(actual)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i - 1][j - 1] + (reference[i - 1] != actual[j - 1]),
                           dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    ops = []
    i, j = n, m
    while i or j:
        if i and j and dp[i][j] == dp[i - 1][j - 1] + (reference[i - 1] != actual[j - 1]):
            kind = "match" if reference[i - 1] == actual[j - 1] else "substitution"
            ops.append((kind, reference[i - 1], actual[j - 1]))
            i -= 1
            j -= 1
        elif i and dp[i][j] == dp[i - 1][j] + 1:
            ops.append(("deletion", reference[i - 1], ""))
            i -= 1
        else:
            ops.append(("insertion", "", actual[j - 1]))
            j -= 1
    return list(reversed(ops))


def char_class(char):
    if not char:
        return "unknown"
    if char.isspace():
        return "whitespace"
    if char.isalnum() or char == "_":
        return "identifier"
    if char in "<>=→←↔-":
        return "symbol"
    if char in ":;,.?!()[]{}'\"":
        return "punctuation"
    return "other"


def class_errors(reference, actual):
    names = ("identifier", "symbol", "punctuation", "whitespace", "other", "unknown")
    summary = {name: {"substitutions": 0, "deletions": 0, "insertions": 0, "errors": 0} for name in names}
    keys = {"substitution": "substitutions", "deletion": "deletions", "insertion": "insertions"}
    for kind, expected, observed in edit_alignment(reference, actual):
        if kind == "match":
            continue
        target = expected if kind in ("substitution", "deletion") else observed
        category = char_class(target)
        summary[category][keys[kind]] += 1
        summary[category]["errors"] += 1
    return summary


def identifier_lines(expected):
    return [line for line in expected.split("\n")
            if re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", line) or re.match(r"^T\d+:", line)]


def engine_row(name, row, engine):
    if engine == "tesseract":
        expected = normalize(row.get("expected_normalized", row.get("expected", "")))
        recognized = normalize(row.get("recognized_normalized", row.get("recognized_raw", "")))
        first_ms = row.get("first_call_elapsed_ms")
        warm = row.get("warm_elapsed_ms_samples", [])
        digest = row.get("fixture_sha256")
    else:
        expected = normalize(row.get("expected", ""))
        recognized = normalize(row.get("recognized", ""))
        first_ms = row.get("first_inference_ms")
        warm = row.get("warm_inference_ms_samples", [])
        digest = row.get("fixture_sha256")
    ids = identifier_lines(expected)
    observed_lines = recognized.split("\n")
    exact_ids = all(identifier in observed_lines for identifier in ids)
    return {
        "engine": name, "expected": expected, "recognized": recognized,
        "cer": row.get("cer"), "wer": row.get("wer"), "fixture_sha256": digest,
        "identifier_lines_expected": ids, "identifier_exact": exact_ids,
        "identifier_lines_missing_or_changed": [identifier for identifier in ids if identifier not in observed_lines],
        "character_errors_by_class": class_errors(expected, recognized),
        "first_inference_ms": first_ms, "warm_inference_ms_samples": warm,
        "warm_inference_ms_mean": round(sum(warm) / len(warm), 3) if warm else None,
    }


def main():
    tess = json.loads(TESSERACT_PATH.read_text(encoding="utf-8"))
    paddle = json.loads(PADDLE_PATH.read_text(encoding="utf-8"))
    if tess.get("fixture_count") != 10 or paddle.get("fixture_count") != 10:
        raise RuntimeError("Paired comparison requires five baseline and five adversarial graph-text fixtures.")
    tess_rows = {row["id"]: row for row in tess["results"]}
    paddle_rows = {row["id"]: row for row in paddle["results"]}
    expected_ids = ["OCR-TXT-001", "OCR-TXT-002", "OCR-TXT-003", "OCR-TXT-004", "OCR-TXT-005", "OCR-GRAPH-006", "OCR-GRAPH-007", "OCR-GRAPH-008", "OCR-GRAPH-009", "OCR-GRAPH-010"]
    if sorted(tess_rows) != expected_ids or sorted(paddle_rows) != expected_ids:
        raise RuntimeError("Fixture IDs missing, duplicated, or unexpected; paired comparison blocked.")

    paired = []
    for fixture_id in expected_ids:
        t = engine_row("Tesseract.js", tess_rows[fixture_id], "tesseract")
        p = engine_row("PaddleOCR", paddle_rows[fixture_id], "paddle")
        if not t["fixture_sha256"] or t["fixture_sha256"] != p["fixture_sha256"]:
            raise RuntimeError("Byte-identical fixture hash mismatch for " + fixture_id)
        if t["expected"] != p["expected"]:
            raise RuntimeError("Expected text differs between engines for " + fixture_id)
        paired.append({
            "id": fixture_id, "fixture_sha256": t["fixture_sha256"], "expected": t["expected"],
            "tesseract": t, "paddleocr": p,
            "cer_delta_paddle_minus_tesseract": round(float(p["cer"]) - float(t["cer"]), 6),
            "wer_delta_paddle_minus_tesseract": round(float(p["wer"]) - float(t["wer"]), 6),
        })

    def mean(engine, metric):
        return sum(float(item[engine][metric]) for item in paired) / len(paired)

    per_engine = {}
    for engine in ("tesseract", "paddleocr"):
        mean_cer, mean_wer = mean(engine, "cer"), mean(engine, "wer")
        all_ids_exact = all(item[engine]["identifier_exact"] for item in paired)
        per_engine[engine] = {
            "mean_cer": round(mean_cer, 6), "mean_wer": round(mean_wer, 6),
            "all_significant_identifiers_exact": all_ids_exact,
            "provisional_thresholds_pass": mean_cer <= 0.05 and mean_wer <= 0.10 and all_ids_exact,
            "engine_initialization_ms": tess.get("worker_init_ms") if engine == "tesseract" else paddle.get("engine_init_ms"),
            "timing_note": "Initialization is separate; first inference and three warm inferences are recorded per fixture."
        }

    report = {
        "schema": "tgcv-ocr-paired-comparison-v1",
        "status": "PAIRED_COMPARISON_INTEGRITY_PASS_ACCEPTANCE_GATE_CLOSED",
        "scope": "Text recognition only. No structural detector, node reconstruction, edge reconstruction, or OpenCV geometry is evaluated or modified.",
        "fixture_count": len(paired), "fixture_ids": expected_ids,
        "timing_protocol": {
            "initialization": "Reported separately from inference.",
            "first_inference": "First recognition on each fixture, separately recorded.",
            "warm_inference": "Three repeated recognitions per fixture; raw samples and mean recorded.",
            "comparability_limit": "Latency is descriptive because engine runtimes and model loading differ."
        },
        "normalization": "Normalize CRLF to LF, trim line-edge whitespace, collapse horizontal whitespace; preserve case, accents, punctuation, symbols, underscores and hyphens.",
        "character_error_classes": ["identifier", "symbol", "punctuation", "whitespace", "other"],
        "provisional_thresholds": {"mean_cer_max": 0.05, "mean_wer_max": 0.10, "all_significant_identifiers_exact": True},
        "engines": per_engine, "acceptance_gate_pass": False,
        "acceptance_gate_note": "Kept closed: this is the first expanded ten-fixture comparison; thresholds, exact labels, arrows, edge-adjacent text and small-text cases require review before a separately governed acceptance gate.",
        "paired_results": paired
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
