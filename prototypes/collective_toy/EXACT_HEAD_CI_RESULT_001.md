# Collective Toy — Exact-Head CI Result 001

**Date:** 2026-10-13
**Validated head:** `5cf209ff92e4a64d23501bb14939d8f82a067f7d`
**Branch:** `prototype/collective-toy-branch-audit-002-20261013`
**PR:** #56, open and draft; base remains `prototype/collective-toy-phase-instrumentation-001-20261013`.

## Results

Both push-triggered workflows completed successfully against the exact validated head:

- Synthetic engine tests — run [38326636566](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38326636566), conclusion `success`.
  - Compile engine and tests: success.
  - Run unit tests: success.
  - Replay full unit suite from clean source archive: success.
- Browser and cross-runtime tests — run [38326636553](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38326636553), conclusion `success`.
  - Browser/Python concordance test: success.
  - Replay browser and Python suite from clean source archive: success.

The test file at the validated head was re-fetched. Its blob remains `b62d9a05f8116d3c2da75d2bc39919af7680705f`, with 98 named `test_*` methods and the test `test_nonterminal_trajectory_cap_marks_omitted_terminal_path_truncated` present. The engine blob remains `f7816e325beb580779badfae1e35bcd8235cf5d4`.

## Interpretation

This is runtime validation of the synthetic engine suite and browser/Python concordance suite at this specific head, including clean-archive replay. It is not evidence of TGCV scientific validity, causality, or value claims. It does not authorize a merge, promotion, contract freeze, or scientific execution.

## Next bounded step

Continue the malformed-input exception-contract sweep using exact-head tests. Add a regression only if a concrete JSON-shaped malformed input produces an unexpected raw exception. Avoid a catch-all exception handler and avoid changing engine semantics without a reproduced defect.

`main` remains unchanged by this validation record. Scientific execution remains disabled.
