# Collective Toy OCR quality evaluation

Status: protocol and reference cases; no real-OCR accuracy result has been claimed yet.

## Purpose

Evaluate the OCR stage independently from graph/arrow interpretation. The current UI uses Tesseract.js in the browser. OCR output is only a transcription candidate and must not be treated as a validated graph.

## Reference cases

The fixture text below is the source of truth for expected OCR content. Generate the rendered image fixtures deterministically from these strings, with a plain white background, dark sans-serif text, no arrows crossing labels, and fixed dimensions. Keep a separate future set for arrows/diagram geometry; it must not be mixed into text OCR scoring.

| Case ID | Expected text | Difficulty |
|---|---|---|
| OCR-TXT-001 | `Estado A\nEstado B\nTransición` | Clear Spanish labels, large font |
| OCR-TXT-002 | `A\nB\nC\nInicio: A` | Short labels and punctuation |
| OCR-TXT-003 | `Estado inicial\nEstado final\nCondición: x > 0` | Accents and symbols |
| OCR-TXT-004 | `Nodo_01\nNodo-02\nT1: A -> B` | Underscore, hyphen, mixed notation |
| OCR-TXT-005 | `Sistema adaptable\nTransformación accesible\nRelación causal?` | Longer labels and punctuation |

## Procedure

1. Render every case as a PNG with a deterministic renderer and record the fixture SHA-256.
2. Run the same browser OCR version and language configuration (`spa+eng`) on every fixture.
3. Save the raw recognized text, normalized recognized text, elapsed milliseconds, browser/runtime version, and fixture hash.
4. Compute character error rate (CER) and word error rate (WER) against the expected text. Normalization may standardize line endings and repeated whitespace, but must not silently remove accents or punctuation from the primary score.
5. Report per-case values and macro-average values. Never report only the average; a failure on a short label can be consequential.
6. Repeat each case at least three times after a cold start and three times after the OCR worker is warm. Report cold-start separately from warm latency.
7. Inspect all cases manually and keep the raw output so scores can be reproduced.

## Acceptance criteria (provisional engineering gate)

These are proposed engineering thresholds, not scientific TGCV claims:
- 100% of fixtures produce a recorded result or an explicit error; no silent failures.
- Mean CER <= 5% and mean WER <= 10% on the clear/standard fixture set.
- Every state identifier in the fixtures is recovered exactly; otherwise mark that case as requiring manual correction regardless of aggregate score.
- Errors, empty OCR output, and cancellation leave the prior user-edited transcription intact.
- Arrow direction and graph connectivity are explicitly out of scope for this OCR score.

If these criteria are not met, do not tune the score by changing normalization after seeing results. Version any fixture, expected text, OCR engine, language data, and normalization change.

## Privacy and packaging

The current integration loads Tesseract.js and language data from a CDN. Although recognition runs in the browser, this is not a fully self-contained/offline bundle. Before describing the feature as offline-capable, vendor and pin the JavaScript bundle, worker, WASM assets, and Spanish/English trained data, then test with network access disabled. Do not send user images to a remote OCR service.

## Current evidence boundary

The deterministic UI test stubs `window.Tesseract.recognize`. It verifies that uploaded image data reaches the OCR interface and that transcription/error handling works. It does **not** measure Tesseract's real recognition quality or runtime. Those measurements must come from the fixture evaluation described above.
