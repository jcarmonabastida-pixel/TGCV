# Collective Toy — Cross-Runtime Invalid-Input Assertion Gap 001

**Date:** 2026-10-13  
**Branch:** `prototype/collective-toy-branch-audit-002-20261013`  
**Inspected test blobs:**
- Python engine tests `test_collective_toy_engine_001.py`: `b62d9a05f8116d3c2da75d2bc39919af7680705f`
- Browser/cross-runtime test `web/cross_runtime_test.cjs`: `9f50b37c1a9bfdb70d3aad1c5266ff60da1e6c5a`

## Concrete finding

The browser test's `pythonRejects(engineDir, model)` helper treats any non-zero Python subprocess exit status as rejection. It does not distinguish the expected `ModelValidationError` from an unexpected implementation exception, import failure, or runtime error.

The browser loop also asserts that the UI reaches the generic “No se ha podido ejecutar” state for each invalid fixture. That confirms the user-facing rejection path, but not that Python rejected each fixture through the intended validation contract. The dedicated Python unit tests do assert `ModelValidationError` for selected malformed-input cases, but that narrower contract is not enforced by the cross-runtime invalid-fixture loop.

## Risk and scope

This is a **test-oracle precision gap**, not a demonstrated engine semantic defect or a proven Python/JavaScript result mismatch. No engine change is warranted on this evidence.

## Bounded follow-up

Make a test-only change in a development branch: change the Python subprocess probe to report whether the failure is specifically `ModelValidationError`, then assert that contract for all cross-runtime invalid fixtures. Keep the browser UI rejection assertion. Include a deliberate probe/control case demonstrating that an unrelated Python exception is not counted as a valid schema rejection. Run the engine suite and browser/cross-runtime suite, including clean-archive replay, before treating the improvement as validated.

Do not change the production engine, canonical JSON, hashes, or scientific execution gate as part of this correction.

## CI state at time of review

- Engine workflow for documentation head `cfb0766fd2c194fcb38c4fc2060dde8e9d4b312e`: PASS, run [38327347258](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38327347258).
- Browser workflow for that head: still `in_progress`, run [38327347304](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38327347304); the concordance step had not finished and clean-archive replay was pending when inspected.

`main` remains untouched. PR #56 remains open and draft. Scientific execution remains disabled.
