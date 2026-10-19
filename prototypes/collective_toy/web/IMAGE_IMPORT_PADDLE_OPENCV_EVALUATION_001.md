# Image import — PaddleOCR integration and OpenCV detector comparison 001

- **Status:** experimental evaluation protocol; implementation decision OPEN.
- **Branch:** `experiment/full-chain-image-import-paddle-opencv-001-20261020`.
- **Base:** `main` at `a1cf6ae6075ad57f2343e406eeb529b8722ef810`.
- **Scope:** optional image-to-editable-graph import for the Full Chain demonstrator.
- **Boundary:** no change to TGCV scientific Core, no scientific execution, no real-world inference, and no replacement of the current detector before comparative evidence.

## 1. Historical reconstruction and current baseline

Relevant prior work must be reused rather than recreated:

1. `prototypes/collective_toy/web/OCR_EVALUATION_PROTOCOL_v0.2.md` on `development/collective-toy-ocr-preprocessing-001-20261013` establishes the structure-first priority and separates topology metrics from text quality. It explicitly says the existing graph evaluator's stable-ID fixtures do not measure visual node detection or spatial matching.
2. PR [#64](https://github.com/jcarmonabastida-pixel/TGCV/pull/64) added a structural evaluator, evaluation fixtures and protocol revisions.
3. PR [#65](https://github.com/jcarmonabastida-pixel/TGCV/pull/65) added topology-first fixtures/guards, including branching and crossing diagrams, and UI regression protection against silently dropping transition conditions. These fixture passes do not establish real-image extraction quality.
4. The Full Chain distribution currently exposes image import as an experimental, collapsed section. It accepts externally generated OCR text or manual transcription; it does not run automatic OCR, and arrow direction must not be assumed to be detected.
5. Historical PaddleOCR text-only evaluation was previously recorded as CER 4.10% and WER 19.83% for OCR-TXT-004. This is a diagnostic result for that case, not a broad accuracy claim; it misses the provisional WER <=10% target and does not measure graph topology.

**Baseline decision:** preserve the existing structural detector and the text-only OCR benchmark as separate baselines. Do not remove either or combine their scores while the comparison is in progress.

## 2. Target user flow

1. User selects an image locally.
2. The image is processed locally or through an explicitly documented local runtime; no image is silently uploaded to a remote service.
3. PaddleOCR produces a transcription candidate with text, confidence and regions/coordinates when available.
4. A structure extractor proposes nodes, connections and direction separately from text recognition.
5. The application displays an editable draft graph and uncertainty indicators.
6. The user can add/delete/reconnect/reorient nodes and edges, rename labels and recover transition conditions.
7. The candidate remains a draft until the user explicitly validates it.
8. Only the user-validated graph may be passed to the normal Full Chain model validator/explorer.

Machine guesses must never be silently promoted to accepted input. If OCR or structural processing fails, is cancelled or returns empty data, preserve the user's previous model and edits.

## 3. Separate the two technical questions

### A. PaddleOCR text-recognition integration

Evaluate PaddleOCR as the text transcription component only. Record:
- engine/package/model version and language configuration;
- source image hash and dimensions;
- raw and normalized transcription;
- text-region coordinates/confidence when available;
- per-label exact match, node-label exact-match rate, edge/relation-label exact-match rate, CER and WER;
- cold-start and warm latency;
- local/offline packaging requirements, runtime dependencies and model size;
- explicit error/cancellation behavior.

Do not treat OCR confidence as confidence in topology, direction, or the correctness of a graph.

### B. Structural extraction: current detector vs OpenCV

Compare the existing custom detector, an OpenCV-based candidate, and a hybrid only if useful. Use the same images, annotation set, image preprocessing and matching protocol. OpenCV is a candidate library, not a presumed solution: its feasibility must be demonstrated for node regions, line/edge paths, arrowheads, crossings, convergences, colored nodes and arrow direction.

For each implementation, record:
- node detection precision/recall/F1 using annotated image regions and a declared spatial matching rule;
- edge endpoint/topology precision/recall/F1;
- directed-edge reversal count;
- missing, extra, duplicate and unresolved-endpoint nodes/edges;
- exact topology match per image;
- ambiguity/abstention rate;
- runtime, dependency footprint and reproducibility;
- human correction effort where measurable.

A graph-record evaluator that receives already-corresponded stable node IDs is not sufficient evidence of visual extraction accuracy. Image-level annotations and matching rules are required.

## 4. Corpus and adversarial cases

Reuse the historical synthetic image fixtures and annotations from the OCR development work where their exact blobs are recoverable:
- linear graph;
- branching graph;
- crossing/overlapping paths.

The comparison must explicitly include or add reviewed cases for:
- arrowheads and both edge directions;
- bifurcations and convergences;
- crossing lines that are not connected;
- a real node at or near a crossing;
- missing, faint, duplicated or spurious lines;
- colored nodes and low contrast;
- curved or touching edges where available;
- unreadable node labels and transition conditions;
- ambiguous direction, for which the safe output is unknown/needs review rather than an invented direction.

Record the image hashes and annotation version for every case. If the historical fixture blobs cannot be retrieved at the exact source commit, stop and recover them; do not recreate supposedly identical images without recording new identities.

## 5. Acceptance gates

### Structural gate (primary)

- Report per-image and aggregate node/edge precision, recall and F1; never report only an aggregate.
- Exact topology must match on every fixture designated as deterministic/clear.
- Any missing, spurious or duplicate edge, unresolved endpoint, or reversed directed edge is a structural failure for that image.
- Ambiguous direction must be explicitly marked unknown/for review; it must not be silently guessed.
- The candidate must not regress any currently passing structural fixture.
- The output must remain editable and require explicit human validation.

### Text gate (secondary)

Retain the historical provisional criteria from the OCR quality protocol:
- record a result or explicit error for every fixture; no silent failure;
- mean CER <= 5% and mean WER <= 10% on the declared clear/standard set;
- critical state identifiers must be exact or explicitly flagged for correction;
- preserve raw output and report per-case results.

The prior OCR-TXT-004 result (CER 4.10%, WER 19.83%) does not satisfy the WER target for that case. Do not claim acceptance from CER alone or modify normalization after observing results.

### Integration gate

- Browser import handles successful, empty, malformed, failed and cancelled OCR/extraction.
- Existing user model and edits survive any failed/cancelled import.
- OCR text and structural topology remain separately inspectable and correctable.
- Import does not discard labels/conditions without an explicit user choice.
- The imported graph is validated through the same Full Chain model contract before exploration/execution.
- Browser/cross-runtime checks and packaging/offline behavior are tested on the exact branch head.
- No image data leaves the local environment unless a separate explicit and documented architecture decision authorizes that.

## 6. Decision rule for replacing the custom detector

Do **not** replace the custom detector merely because OpenCV is a standard library or because it reduces code. Decide only after the same annotated image corpus has been run against both implementations.

- **Replace with OpenCV** only if it meets the structural gate, preserves all existing passes, handles arrow direction/ambiguity safely, and offers a clear maintenance or reliability advantage without unacceptable packaging/runtime cost.
- **Retain the custom detector** if it performs better or if OpenCV fails a critical topology/direction case.
- **Use a hybrid** if evidence shows OpenCV reliably handles specific geometric primitives while the custom detector is better for other parts; define the handoff and test the combined pipeline.
- **Defer the decision** if image-level annotations, direction cases or representative cases are missing. A fixture contract PASS is not enough.

No detector replacement may silently change the accepted graph semantics or user review gate.

## 7. Implementation order

1. Recover exact PaddleOCR benchmark code, configuration, model identity and outputs from the historical experiment branch; verify the reported result against retained evidence.
2. Recover the current custom detector and image-level fixtures/annotations by exact GitHub branch/commit, and identify which current tests only validate graph records rather than image extraction.
3. Add a small, reproducible head-to-head image-level benchmark harness without changing the Full Chain application.
4. Run current custom detector baseline and record per-image metrics.
5. Add OpenCV as a separate candidate implementation and run the identical corpus.
6. Compare metrics, failure cases, latency and packaging; only then choose custom/OpenCV/hybrid/defer.
7. Integrate PaddleOCR and the selected structural pipeline into an experimental image-import branch with human review and fail-closed behavior.
8. Validate browser behavior and the standalone package. Keep this optional feature isolated from Full Chain acceptance until it independently passes.

## 8. Explicit non-goals

- No scientific validation of TGCV or causal/value claims.
- No processing of the Rust dataset or other empirical research data.
- No automatic acceptance of OCR/extracted topology.
- No claim of offline capability until all runtime/model assets are pinned and verified with network access disabled.
- No removal of the current detector before comparative acceptance evidence exists.
