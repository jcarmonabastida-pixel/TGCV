# TGCV Collective Toy — Structure-first graph extraction evaluation protocol v0.2

- **Status:** proposed engineering specification; not validated against a representative image corpus.
- **Date:** 2026-10-13
- **Supersedes for new structural-priority work:** the evaluation priorities in v0.1 only; v0.1 remains historical and unchanged.
- **Scope:** image import, candidate graph extraction, user correction, and validation.
- **Scientific boundary:** this protocol evaluates the software pipeline only. It does not validate TGCV scientific claims or prove the correctness of a user-approved graph.

## 1. Decision: separate structure from text

The primary engineering objective is to recover the graph topology, not to transcribe every character perfectly.

Priority order:
1. Detect each node and preserve its identity through review.
2. Recover every edge, its endpoints, and its direction (directed, undirected, or bidirectional).
3. Detect missing, extra, duplicated, or ambiguous nodes/edges and make uncertainty visible.
4. Recover node labels and edge/relation labels as a separate text-quality layer.
5. Allow a user to edit the candidate graph and explicitly validate it before it becomes the accepted input.

When a node label is absent or unreadable, the UI may assign a provisional label such as A, B, C or S1, S2, S3. The provisional label must not be represented as OCR-recognized source text. It must remain editable and must not change node identity or topology.

Text errors must not conceal structural errors. Conversely, a text-label mismatch alone must not fail the topology score. Edge labels and mathematical/condition text can be semantically important; preserve them when legible and mark uncertain or missing text for review rather than silently inventing it.

## 2. Metrics and gates

Report at least two independent result groups:

### Structural metrics (primary)
- Node detection precision, recall, and F1.
- Edge topology precision, recall, and F1.
- Directed-edge reversal count.
- Missing and extra nodes/edges.
- Duplicate edges and edges with unresolved endpoints.
- Exact topology match.

### Text metrics (secondary)
- Node-label exact-match rate among matched nodes.
- Edge/relation-label exact-match rate among matched edges.
- Optional CER/WER for verbatim OCR, reported separately.
- Count of missing, unreadable, or provisional labels.

Do not collapse structural and text metrics into one average score. A high OCR character score cannot compensate for a wrong graph. A wrong state name alone cannot compensate for, or disguise, a correct topology.

### Status semantics
- `STRUCTURE_PASS`: the evaluated topology matches exactly, regardless of label text.
- `STRUCTURE_FAIL`: a node/edge is missing or extra, direction differs, or duplicate topology is present.
- `CRITICAL_FAIL`: the graph is malformed, an edge references a missing node, or a directed edge is reversed.
- Text discrepancies are reported separately and require review according to the UI's uncertainty policy; they do not change structural status by themselves.

## 3. Identity and current evaluator limitation

The deterministic contract fixtures use stable node IDs to represent correspondence between a reference node and the candidate node. In a real image pipeline, those IDs must be grounded in node detections (for example, stable candidate IDs linked to image regions/bounding boxes) and the reference/candidate correspondence must be established independently of OCR labels.

**The current fixture evaluator does not yet measure visual node detection or spatial matching.** Passing these tests proves only the intended scoring contract for already-corresponded graph records. It is not evidence that image-to-graph extraction works.

The next image-level gate must add annotated node regions, edge paths/arrowheads, ambiguity regions, and a documented matching rule (including how crossings and overlapping nodes are handled) before reporting image-level topology precision/recall.

## 4. Human-in-the-loop contract

The import flow should:
1. Create a candidate graph and mark uncertain detections/labels.
2. Use provisional node labels only when source labels are absent/unreadable.
3. Show nodes and directed/undirected edges in an editable graph view.
4. Let the user add, remove, reconnect, reorient, rename, and annotate elements.
5. Distinguish machine-proposed content, provisional labels, and user edits in the UI.
6. Require an explicit user validation action before the graph is accepted as input to TGCV.
7. Preserve an audit record of the accepted graph and its corrections, without implying that user validation proves the source image was unambiguous.

## 5. Regression fixtures and corpus

Keep v0.1 fixtures unchanged. The v0.2 contract fixtures cover: exact topology, label mismatch with topology preserved, reversed arrow, missing edge, extra edge, duplicate edge, missing node, unknown endpoint, undirected edge equivalence, and edge-label mismatch.

These are synthetic contract cases, not a representative OCR benchmark. Before any claim of real-world quality, use real images from multiple source types, independent annotations for graph-critical fields, adjudication, provenance, and a locked test set. Keep all thresholds provisional until justified by representative data.

## 6. Acceptance boundary

A passing structural contract is necessary but not sufficient for release. It does not establish:
- visual node/edge detection accuracy;
- robustness to image quality, crossings, dense layouts, or skew;
- OCR quality on real images;
- usability or effectiveness of the correction UI;
- scientific validity of the resulting graph or any TGCV claim.
