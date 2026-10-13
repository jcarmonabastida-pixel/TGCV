# TGCV Collective Toy — OCR and graph evaluation protocol v0.1

- **Status:** proposed evaluation specification; not yet validated against a representative corpus.
- **Date:** 2026-10-13
- **Scope:** image-import OCR and conversion of recognized content into a candidate system graph.
- **Branch:** `development/collective-toy-ocr-preprocessing-001-20261013`
- **Normative boundary:** this protocol evaluates an implementation pipeline. It does not validate TGCV's scientific claims, establish causal relations, or prove that a human-reviewed graph is correct.
- **Threshold status:** all numeric acceptance thresholds below are provisional engineering gates. They must not be presented as empirically justified until a representative, independently annotated corpus supports them.

## 1. Relationship to existing assets

The repository already contains:
- `prototypes/collective_toy/web/ocr_quality_evaluation.html`: browser-based evaluator using five locally generated synthetic text images, Tesseract.js 5, `spa+eng`, CER/WER self-checks, segmentation and preprocessing diagnostics, and targeted character-confusion diagnostics.
- `prototypes/collective_toy/web/ocr_quality_ci_test.cjs`: CI harness that checks the synthetic OCR run and diagnostic report.
- `prototypes/collective_toy/web/ui_contract_test.cjs`: UI contract tests, including a stubbed OCR integration test.

This specification does **not** replace those files or duplicate their implementation. It defines the missing evaluation design for representative images, critical recognition errors, graph structure, and fair engine comparison. The current five-fixture synthetic corpus is useful for regression and instrumentation, but is insufficient to establish production-quality OCR or graph extraction.

## 2. Audit evidence and bounded conclusion

The supplied audit record identifies two failed gates:
- Execution 17: run [38434544909](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38434544909), commit `75abf6647a4c48a6435f2b23c0221ee67c498b01`, artifact `11832471600`, ZIP SHA-256 `ca1529330acf3c4c223a2074a577cdb8e7f638acd232005a9c16793dd42de290`.
- Execution 18: run [38434944535](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38434944535), commit `7cee19d969068595bd5d95192a87c578e4014b87`, artifact `11832960699`, ZIP SHA-256 `083bc6497cce85b76d13edbeb5ba8e53b8d14373b38917fe6b54f48899744614`.

Both are recorded as **gate not passed**. These identifiers and hashes are transcribed from the audit record supplied for this protocol; this document does not claim to have independently downloaded or re-hashed those artifacts.

## 3. Evaluation unit and corpus

The unit of evaluation is one source image plus its frozen annotation package. Each item must have a stable ID and include:
1. Original image bytes and SHA-256.
2. Source/provenance class and licence/permission status where applicable.
3. Image characteristics: dimensions, colour mode, scan/photo/screenshot, estimated skew/blur, contrast, compression and resolution.
4. Human-verified text transcription, preserving case, accents, punctuation, identifiers and mathematical/operator symbols.
5. Annotated entities/nodes and their exact labels.
6. Annotated directed/undirected edges, source and target node IDs, edge direction, relation label, and arrowhead location/meaning where visible.
7. Ambiguity/illegibility annotations, plus annotator and adjudication status.
8. Split assignment and reason for inclusion.

### Corpus matrix

| Stratum | Required examples | Primary risk covered | Status in current five synthetic fixtures |
|---|---|---|---|
| Clean printed labels | Short and long Spanish labels, accents | Baseline character recognition | Partial |
| Identifiers and punctuation | `Nodo_01`, hyphens, colons, decimal/number tokens | Token corruption and identifier mismatch | Partial |
| Critical symbols | `>`, `<`, `=`, arrows typed as text, 0/O, I/l/1, C/cc | Meaning-changing substitutions | Partial diagnostics only |
| Real screenshots/documents | Captures, exported diagrams, scans, photographed pages | Domain shift, compression, uneven contrast | Missing |
| Diagram topology | 2+ nodes with clear arrows and arrowheads | Node/edge omission or hallucination | Missing |
| Direction ambiguity | A→B vs B→A; bidirectional and crossing arrows | Direction reversal | Missing |
| Relation labels | Text near an edge, labels crossing/near lines | Wrong edge-to-label association | Missing |
| Dense/overlapping layouts | Many nodes, crossings, small text | Merged/split objects and spurious edges | Missing |
| Negative/ambiguous cases | No arrow, decorative line, illegible label, partial crop | False positive and overconfident extraction | Missing |
| Robustness variants | Controlled blur, scale, rotation, compression, lighting | Sensitivity to capture conditions | Missing |
| Multi-language / mixed notation | Spanish plus English, identifiers, formulas | Language and tokenisation failures | Partial |

Do not treat generated variants of the same base diagram as independent samples. Group by source diagram/document before assigning train/tuning/test partitions. Keep a locked test set that is not used to choose preprocessing or engine parameters.

### Minimum corpus release gate

Before any claim of representative quality:
- Include real-world images from at least three distinct source types (e.g. exported diagram, screenshot, scan/photo), with provenance documented.
- Include positive and negative examples for arrows, edge labels, direction, crossings and non-arrow lines.
- Have two independent annotations for all graph-critical fields and adjudicate disagreements.
- Publish counts per stratum, exclusion rules, class imbalance, and uncertainty/ambiguity rates.
- Keep the current synthetic fixtures as a regression suite, not as the sole quality benchmark.

No sample-size claim is made here: the necessary size should be decided from the intended deployment distribution and precision required for the critical-error rates.

## 4. Metric hierarchy

### 4.1 Primary textual metrics

Compute on the frozen reference and raw OCR output, before any semantic correction:
- **CER (Character Error Rate):** Levenshtein edit distance over characters divided by the number of reference characters.
- **WER (Word Error Rate):** word-level edit distance divided by reference word count.
- Report corpus micro-aggregates and per-image/per-stratum results. Also report median, 90th percentile, worst case, and confidence intervals where sample size permits.
- Publish the exact normalization and tokenization policy. Default normalization may standardize line endings and repeated whitespace only; it must not erase case, accents, punctuation, identifiers, numeric distinctions, operators or arrow direction.
- Report empty-reference cases separately; do not let them silently distort aggregate rates.

CER/WER measure transcription similarity only. Neither metric by itself certifies that a diagram's graph is correct.

### 4.2 Critical textual diagnostics (secondary; never silently folded into CER/WER)

Report separate counts/rates for:
- Directional/operator tokens: `->`, `<-`, `<->`, `>`, `<`, `=`.
- Confusable characters: 0/O, 1/l/I, C/cc, hyphen/underscore, colon/semicolon.
- Node IDs and relation identifiers: exact-match accuracy.
- Label truncation, line-order changes, merged lines, split tokens, omitted text and inserted hallucinated text.
- Unreadable/low-confidence output and abstention rate.
- Runtime, initialization time, failures, resource/version details.

Diagnostics explain failure modes. They are not independent success metrics and must not be used to override primary results post hoc.

## 5. Graph-structure evaluation

A reference graph must be annotated independently of OCR output. Compare the extracted candidate graph with that reference after only a documented, deterministic node-matching procedure. Do not manually repair the candidate before scoring.

Primary graph metrics:
- **Node precision, recall and F1**, using exact identity/label matching under the frozen matching policy.
- **Directed edge precision, recall and F1**, requiring correct source, target and direction.
- **Direction accuracy** among edges whose endpoints were matched.
- **Relation-label exact-match accuracy** for labelled edges.
- **Graph exact match**: fraction of images for which all required nodes and edges match the reference. Report as a strict metric, not the only metric.
- **Spurious-edge rate** and **missing-edge rate**, per image and per stratum.
- **Node-label exact match** separate from topology, so a correct topology cannot conceal corrupted labels.

If the system cannot confidently resolve a node or edge, record abstention/uncertainty rather than silently guessing. Define treatment of ambiguous annotations before evaluating.

## 6. Provisional release gates and critical rejection rules

The thresholds below are initial engineering safeguards, not validated standards. Keep them explicitly marked provisional until calibrated on a representative corpus.

| Gate | Provisional criterion | Failure consequence |
|---|---|---|
| Text aggregate | CER ≤ 5% and WER ≤ 10% on locked test set | Reject release candidate if exceeded |
| Critical identifiers | 100% exact match for graph-referenced node IDs in the accepted subset | Reject any affected image or require explicit user correction |
| Edge direction | 100% correct on unambiguous reference arrows in the accepted subset | Any reversal is a critical failure, irrespective of CER |
| Critical operator/token | 100% exact match for predesignated meaning-changing tokens | Any wrong token is a critical failure for that item |
| Graph edges | Directed edge F1 ≥ 0.95 on unambiguous cases | Reject if below threshold; report strata separately |
| Spurious edges | Zero unflagged spurious edges in the accepted subset | Critical rejection; uncertain cases must be surfaced |
| Abstention/error handling | Unreadable/ambiguous cases visibly flagged; no silent success | Any silent critical guess fails the gate |
| Reproducibility | Inputs, references, configuration, engine/resource versions and output hashes recorded | Results are not accepted as reproducible evidence |

A critical failure cannot be averaged away by a good CER/WER. Report both (a) end-to-end quality across all test images and (b) quality on the explicitly accepted subset. Never report only the accepted subset without its coverage/abstention rate.

## 7. Fair OCR-engine comparison protocol

When comparing engines:
1. Freeze and hash the same corpus, reference annotations, splits and evaluation code.
2. Use identical source images and identical eligibility rules for every engine.
3. Record engine name/version, language packs/model hashes where available, runtime/platform, configuration, preprocessing, confidence handling and resource-loading mode.
4. Start with a baseline run using original images and each engine's documented default configuration.
5. Compare preprocessing only as a separate, predeclared factorial/ablation experiment. Do not tune one engine more heavily than another and then call it a fair engine comparison.
6. Separate tuning/validation images from the locked test set. Select parameters on validation only; run the locked test after choices are frozen.
7. Preserve raw engine output. Any post-processing or normalization must be versioned and evaluated as a separate pipeline stage.
8. Run repeated measurements only when needed to characterize timing or nondeterminism; do not count repeats as independent images.
9. Report primary text metrics, graph metrics, critical error counts, coverage/abstention, per-stratum results, latency, failures and uncertainty.
10. Save machine-readable per-image results plus a summary; hash both. A missing artifact, missing stratum, changed reference, or incomparable configuration makes the comparison incomplete.
11. Apply critical rejection rules before ranking engines. If all candidates fail a critical rule, select none; do not choose the least bad engine as if it passed.

## 8. Human review and product boundary

Human review is a safety/approval step, not a correctness metric. Record separately:
- raw OCR transcription;
- proposed nodes/edges;
- uncertainty flags and highlighted source regions;
- edits made by the reviewer;
- final approved graph;
- reviewer identity/role and timestamp, where appropriate for the product's privacy policy.

Measure pre-review extraction against the frozen reference. Review acceptance, number of edits and time-to-review are usability outcomes, not proof that recognition was correct. Never label a graph as verified solely because a user clicked “accept”.

## 9. Machine-readable result contract

Each per-image record should include at minimum:
- `protocol_version`, `image_id`, `image_sha256`, `split`, `stratum`;
- `engine`, `engine_version`, `language_resources`, `preprocessing_id`, `configuration_hash`;
- `reference_text`, `raw_text`, `normalized_reference_text`, `normalized_raw_text`;
- `cer`, `wer`, critical-token diagnostics;
- `reference_graph` identifier/hash, extracted node/edge counts, node/edge metrics, direction errors, spurious/missing edges;
- `abstained`, `critical_failures`, `elapsed_ms`, error status;
- hashes/versions of the evaluator and output artifact.

Avoid embedding sensitive source images or personal data in public CI artifacts. Store a manifest and hashes when the corpus cannot be redistributed.

## 10. Decision and next gates

1. Keep the current synthetic Tesseract evaluator as a fast regression/instrumentation check.
2. Build and adjudicate the stratified image-and-graph corpus before engine selection.
3. Implement graph annotations and scoring independently from OCR.
4. Run a baseline with the current engine before changing engines or adding further preprocessing variants.
5. Review critical-error examples and per-stratum metrics; update provisional thresholds only with documented rationale.
6. Only after the protocol, corpus and evaluator are frozen should a controlled engine comparison be run.

**Current decision:** no engine change is justified by this protocol alone. The two audit runs remain failed gates. This document is a specification, not evidence of improved OCR quality; it does not authorize a new workflow run.
