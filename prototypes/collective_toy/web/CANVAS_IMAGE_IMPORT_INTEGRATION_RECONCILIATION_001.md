# Canvas image-import integration — reconciliation record 001

**Date:** 2026-10-20  
**Status:** RECONCILED — implementation port remains pending  
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
  - status: open draft; synthetic evaluation only.
- PR #81, editable graph review and export:
  - head branch: `prototype/image-import-review-guide-001-20261020`
  - head SHA: `4c7f5f8a192f59a40d8f289404420182c934ee3e`
  - base branch: `development/collective-toy-ocr-arrow-direction-001-20261014`
  - base SHA: `cbdc5bcae80dff050d073dfbe6c84f44cf4f4f56`
  - status: open draft; the documented image path still uses OCR text followed by text-to-graph parsing, not automatic pixel-level topology extraction.

## Reconciliation finding

Both PRs share the development base above, but neither is a clean integration branch based on current `main`. GitHub comparisons against `main` report both heads as diverged and 9 commits behind `main`; PR #80 is 289 commits ahead by history count and PR #81 is 242 commits ahead. Those counts describe history, not the amount of code needed to port.

The relevant detector files and UI files are absent from `main` at the queried paths. Therefore, merging either PR wholesale or using either head as the integration base would violate the intended clean, minimal integration approach. The next implementation step must port only the necessary detector/runtime pieces and the smallest UI adapter into this branch, then test the exact combined path.

## Required integration contract

1. Keep the existing detector algorithm unchanged during the first integration.
2. Do not require OCR output to create candidate nodes or connections.
3. Convert geometric candidates into a reviewable graph draft; do not mark it as an accepted execution package.
4. Preserve the source image, node/edge editability, and per-edge direction-review state.
5. Keep missing, ambiguous, or weak arrow evidence unresolved. Never auto-accept a direction.
6. Keep OCR optional and limited to provisional labels.
7. Add a regression for image → Canvas candidate extraction → editable graph draft → manual correction/review → review export.
8. Run CI on the exact branch head and report engineering results only; no scientific execution or TGCV scientific-validity claim.

## Current operation outcome

A clean branch was created from the verified current `main` commit above. This commit records the historical reconciliation and integration boundary only. It does not claim that Canvas has been integrated, and it does not modify `main`, merge a PR, or run tests.

## Next action

Inspect the exact detector and UI dependencies at the recorded PR heads, then port the smallest compatible set of files into this branch. Before writing the adapter, identify the actual browser-facing editor model and prove the mapping with a focused contract test. Do not add unrelated OCR benchmark files or copy either divergent branch wholesale.
