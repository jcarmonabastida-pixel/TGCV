# Canvas image-import integration — reconciliation record 001

**Date:** 2026-10-20  
**Status:** INTEGRATION IMPLEMENTED IN PR #82; conservative browser direction proposals and synthetic topology characterization pass engineering CI on code head `09eb24d44fe20c47c926a8d5704ea30cf281acff`  
**Base:** `main` at `5768fe937fc6453098779101a0df5119e07dffbe`  
**Branch:** `experiment/canvas-image-import-integration-reconciliation-001-20261020`

## Decision already established

Canvas remains the primary detector candidate. OpenCV remains a secondary experiment. Do not restart detector comparison or continue tuning OpenCV's arrow-direction discriminator as part of this integration step.

Canvas direction proposals remain provisional and require human review. Unresolved directions must not silently become accepted directed transitions.

## Historical artifacts and exact identities

- PR #80, Canvas arrow-tip localization:
  - head branch: `experiment/canvas-arrow-tip-localization-001-20261020`
  - head SHA: `b7a37e134cb1f7cffa806d49c81f2fc5d565e872`
  - base branch: `development/collective-toy-ocr-arrow-direction-001-20261014`
  - base SHA: `cbdc5bcae80dff050d073dfbe6c84f44cf4f4f56`
  - status at reconciliation: open draft; synthetic evaluation only.
- PR #81, editable graph review and export:
  - head branch: `prototype/image-import-review-guide-001-20261020`
  - head SHA: `4c7f5f8a192f59a40d8f289404420182c934ee3e`
  - base branch: `development/collective-toy-ocr-arrow-direction-001-20261014`
  - base SHA: `cbdc5bcae80dff050d073dfbe6c84f44cf4f4f56`
  - status at reconciliation: open draft; its documented image path used OCR text followed by text-to-graph parsing, not automatic pixel-level topology extraction.

## Reconciliation finding

Both historical PRs shared the development base above, but neither was a clean integration branch based on current `main`. The integration therefore ports the required detector/runtime and adapter pieces onto a clean branch based on the verified `main` commit rather than merging either divergent branch wholesale.

## Integration contract

1. Keep Canvas as the primary detector candidate; do not use OCR to create nodes, edges, or topology.
2. Convert geometric candidates into an editable review draft, not an accepted execution package.
3. Preserve the source image and editable node/edge model.
4. Keep every imported edge direction subject to explicit human review, including directions proposed by the detector.
5. Block scenario execution while any edge direction remains unresolved.
6. Export a review-draft JSON with source image and explicit review state.
7. Keep OCR optional and limited to provisional labels; OCR quality metrics are separate from topology correctness.
8. Report engineering conformance only; no scientific execution or TGCV scientific-validity claim.

## Current implementation and verification

The integration is implemented in PR #82. The browser UI path is covered by a Playwright regression that selects a local image, creates an editable draft, blocks execution while edge directions are unresolved, allows manual reversal and confirmation, and exports review JSON preserving the source image and review state.

The UI end-to-end test uses a controlled detector stub to isolate integration wiring. The actual browser Canvas detector is now also exercised on generated synthetic linear and branch diagrams. At code head `09eb24d44fe20c47c926a8d5704ea30cf281acff`, it found the expected 3 node candidates and 2 edge candidates in each probe, with expected topology and node centers. The conservative post-processing adapter now uses the existing geometric evidence thresholds to propose direction when supported; proposals remain unresolved until explicit human confirmation. The branch probe proposed A→B and A→C, and the linear probe proposed A→B and B→C.

This is a **small synthetic regression set**, not representative real-image validation. The current browser detector test does not establish general accuracy on scans, screenshots, colored nodes, varied line styles, complex crossings, or missing/spurious connections. Arrow-direction proposal quality remains provisional and must be measured separately from topology.

On code head `09eb24d44fe20c47c926a8d5704ea30cf281acff`, all four GitHub Actions workflows completed successfully on 2026-10-20:
- Collective Toy browser and cross-runtime tests — run `39444524861`.
- Collective Toy browser performance benchmark — run `39444524763`.
- Collective Toy synthetic engine tests — run `39444524785`.
- TGCV governance current-state consistency — run `39444524725`.

This evidence is engineering conformance for the exact code head above, not scientific execution or a TGCV scientific-validity claim. The subsequent documentation-only update must also have its own exact-head CI checked before the branch is considered reconciled.

## Next acceptance step

Evaluate the real Canvas detector against the agreed representative image set, recording topology separately from OCR labels and arrow direction. Retain human review for every direction. Keep PR #82 draft and `main` unchanged until that acceptance evidence and the exact-head CI status have been reconciled.
