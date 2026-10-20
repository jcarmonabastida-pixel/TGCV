# Image import acceptance audit 002

- **Date:** 2026-10-20
- **Status:** implementation boundary reconciled; visual topology extraction remains pending
- **Branch:** `prototype/image-import-review-guide-001-20261020`
- **Related PR:** #81 — human direction review controls, review export and usage guide
- **Prior audit:** `OCR_IMAGE_TO_GRAPH_GAP_AUDIT_001.md` (2026-10-13)
- **Scope:** engineering acceptance only; no claim of scientific TGCV validity.

## Current verified behavior

| Contract area | Evidence/status | Boundary |
|---|---|---|
| Load PNG/JPEG/WebP as a visual reference | Implemented in the browser UI | The image remains a reference; this does not extract topology |
| Optional OCR text extraction | Implemented with Tesseract.js (`spa+eng`) | OCR output is text, not node/edge/direction detection |
| Convert text/connection notation into a graph draft | Implemented | The user must provide/correct connection notation; conversion is not pixel-level graph reconstruction |
| Edit graph and remove/create connections | Existing graph editor | Human review remains necessary |
| Invert an edge direction | Added in PR #81 | User must compare with the original image |
| Mark direction unresolved and confirm manually | Added in PR #81 | The unresolved marker is session-level UI state until exported |
| Export review snapshot and unresolved direction markers | Added in PR #81 | Separate sidecar; does not modify execution-package schema or embed the image |
| Browser/Python contract and clean-source replay | PASS, workflow run [39418150517](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39418150517), head `352b87ef2256b86af3a16ff09d6a35a0246066d6` | Confirms only automated tests in that workflow |

## Explicitly not implemented or not established

1. No committed, validated image-space pipeline that detects node regions, edge paths, crossings, bifurcations, convergences and arrowheads from pixels.
2. No spatial matching between detected edge endpoints and detected node regions.
3. No representative real-diagram benchmark or adjudicated real-image validation set.
4. No evidence that a clean OCR result implies a correct graph, or that a graph draft matches its source image.
5. No automatic acceptance of uncertain edge directions. Earlier synthetic adversarial evaluation failed the `no-arrow` control; do not tune the resolver from that evidence alone.

## Acceptance decision

**The current PR is acceptable as a manual-review and documentation increment, not as completion of image-to-graph topology import.** Keep it in draft until its owner reviews the scope; do not promote it to `main` automatically.

The product-level path currently is:

`image reference → optional OCR text → editable transcription/connection notation → graph draft → human structural review → execution`

It is not yet:

`image pixels → automatically extracted and spatially matched graph → human verification`

## Next minimal engineering gate

Avoid further isolated arrow-angle experiments. The next substantive implementation gate should be a **small user-guided visual graph authoring flow** or a bounded visual candidate detector, chosen only after reviewing the existing UI:

1. Keep the source image visible while the user edits the graph.
2. Allow the user to create/rename node candidates and add, reverse, or mark connections unresolved without losing the source reference.
3. Keep structural topology separate from OCR labels.
4. Preserve unresolved direction markers in the review sidecar and make the review artifact reproducible.
5. Add a tiny versioned synthetic raster fixture set only when there is an actual visual detector to evaluate; label it synthetic and separate its results from real-image validation.
6. Define real-diagram validation criteria before making any general accuracy claim.

## Governance boundaries

- No changes to `main` or promotion authorization.
- No scientific execution, real-data processing or TGCV Core change.
- The current PASS is software contract evidence, not scientific validation and not proof of image-level topology recovery.
