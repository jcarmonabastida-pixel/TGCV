# OCR image-to-graph gap audit 001

- **Date:** 2026-10-13
- **Status:** VERIFIED IMPLEMENTATION GAP; engineering audit only
- **Branch:** `development/collective-toy-ocr-topology-first-001-20261013`
- **Source under inspection:** `prototypes/collective_toy/web/index.html`, blob `53758d1f81dbfb206eefa456e03a80b6559848b1`
- **Related contract:** `OCR_EVALUATION_PROTOCOL_v0.2.md`, blob `2d9c095cd1b3c1f0506dc71680c18bb250929b97`
- **Scope boundary:** This audit makes no claim about OCR accuracy or TGCV scientific validity.

## Findings

1. The image input currently accepts PNG, JPEG, and WebP.
2. The OCR action calls Tesseract `recognize(preview.src, "spa+eng", ...)` and obtains text.
3. The next import step parses the resulting transcription into a graph draft.
4. The current path does not expose a visual node detector, edge-path detector, arrowhead detector, node bounding-box annotations, or a spatial matching stage.
5. The repository currently contains no committed raster image fixtures for an image-to-graph benchmark. The existing graph fixtures are structured JSON cases and test evaluator contracts, not visual extraction.
6. Therefore, the recent PASS results establish browser/cross-runtime and graph-evaluator contract behavior only. They do not establish image-to-graph topology recovery.

## Engineering consequence

Do not describe the current pipeline as a visual graph recognizer. It is currently an **image-to-text OCR step followed by text-to-graph parsing**. This distinction matters because a diagram may have clear geometric connections whose textual representation is not recognized by OCR.

## Next minimal implementation gate

Before tuning image preprocessing or claiming image-level metrics:

1. Add a small, versioned raster fixture set with independent node-region and edge/direction annotations. Include at least a linear graph, a branch/convergence, and an ambiguous crossing; use synthetic fixtures first and keep them explicitly separate from real-world validation images.
2. Record each image's SHA-256, provenance/source type, split, and annotation status using `ocr_graph_reference.schema.json`.
3. Define a candidate-detection interface that emits node regions and candidate edge endpoints/direction with uncertainty, independently of recognized labels.
4. Add deterministic annotation-matching tests for node regions, edge endpoints, direction, crossings, and unresolved cases.
5. Only then evaluate an actual visual extraction method. Report structural metrics separately from OCR label metrics.

## Release/authorization boundary

- No change to `main` is authorized or made by this audit.
- No representative corpus or real-image quality claim is established.
- Synthetic fixture PASS must not be presented as evidence of general OCR quality.
- Preserve explicit user review and validation before accepting an imported graph.
