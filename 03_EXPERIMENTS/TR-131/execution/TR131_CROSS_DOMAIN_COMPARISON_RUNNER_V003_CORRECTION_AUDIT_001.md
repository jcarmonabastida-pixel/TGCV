# TR-131 — V002 Unit-Test Failure and V003 Correction Audit

**Status:** CORRECTIVE ACTION REQUIRED — SCIENTIFIC EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-23  
**Canonical source:** GitHub `origin/main`

## Observed result
Local execution of V002 produced **11 tests: 10 passed, 1 error**. The failing test was `test_trajectory_divergence`, with `KeyError: 'S_t'`.

## Diagnosis
V002 used `S_t` and `S_t1` for provenance hashing but did not preserve them in derived records. The trajectory procedure requires the source state to group explicit branches, so the implementation failed at the trajectory-analysis boundary.

This is an implementation defect, not a scientific finding.

## Correction
V003 preserves `S_t` and `S_t1` in derived records. The complete 11-test suite is reproduced against V003.

No VisitAll or PRISM evidence is touched.

## Decision
**V002 UNIT TEST EXECUTION: FAIL — IMPLEMENTATION ERROR.**

**V003 CORRECTION: CONSTRUCTED; UNIT-TEST EXECUTION PENDING.**

Scientific execution remains prohibited until V003 passes the complete unit-test suite.

## Next gate
Run only:
`py .\03_EXPERIMENTS\TR-131\execution\TR131_CROSS_DOMAIN_COMPARISON_RUNNER_003_TEST.py`
