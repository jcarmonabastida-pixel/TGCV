# Collective Toy — Malformed-Input Contract Sweep 002

**Date:** 2026-10-13
**Audited branch:** `prototype/collective-toy-branch-audit-002-20261013`
**Source blobs inspected:**
- Engine `collective_toy_engine_001.py`: `f7816e325beb580779badfae1e35bcd8235cf5d4`
- Tests `test_collective_toy_engine_001.py`: `b62d9a05f8116d3c2da75d2bc39919af7680705f`

## Scope

Static review of the Python model-validation order and the existing malformed-input regression coverage. No engine or test code was changed in this sweep.

## Findings

The current validation path checks the top-level model type before recursive canonical-domain validation, rejects non-JSON values and unsafe/non-finite numbers, validates state IDs before constructing the state set, validates transition containers and identifiers before using IDs as mapping keys, validates relation references in the relation-guarded profile, and validates disabled-transition IDs before set subtraction.

The existing suite includes targeted tests for malformed top-level/nested containers, invalid state/transition/relation/scenario identifiers, unknown references, duplicate identifiers, unknown nested fields, invalid exploration bounds, non-JSON values, unsafe numbers, unpaired surrogates, package tampering, and trajectory truncation boundaries.

**No concrete reproducible defect was established by this static pass.** This is not a claim that every malformed input has been executed or that all exceptions are impossible. In particular, the suite's existence and prior CI results do not substitute for a new run against a newly changed code head.

## Decision

- Do not add a broad exception handler.
- Do not alter engine semantics without a reproduced failure.
- Do not add a speculative test merely to increase the test count.
- Continue by checking the browser/Python CI run and, if a specific untested malformed-input boundary is identified, add a narrow regression that asserts the exact contract.

## Status

This is a static audit record only. It does not claim a fresh CI result, scientific validity, causality, or value claims. `main` remains untouched; PR #56 remains a draft; scientific execution remains disabled.
