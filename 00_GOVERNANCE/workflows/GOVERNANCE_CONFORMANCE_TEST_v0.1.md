# TGCV — Governance Conformance Test v0.1

**Status:** FROZEN GOVERNANCE TEST  
**Date:** 2026-09-08  
**Purpose:** verify that the current governance mechanism detects incomplete propagation of a substantive accepted change without modifying production scientific state.

## 1. Test principle

The test uses a synthetic governance event. It does not represent a scientific result and must never modify the canonical RMA, claims, gates, experiments or architecture.

Synthetic event:

`TEST-CHANGE-001 = accepted substantive result that changes the status of one governed scientific asset.`

Expected propagation obligations:

- impact analysis required;
- RMA current state required;
- dependent current assets identified;
- STATUS reconciliation required;
- claim/evidence impact explicitly assessed;
- CHANGELOG entry required;
- structural validator required;
- human consistency closure required;
- next gate cannot be opened before closure.

## 2. Negative conformance case

A synthetic change is declared accepted but the impact analysis omits a dependent current asset and STATUS reconciliation.

Expected result: **FAIL / BLOCK PROGRESSION**.

The test passes if the governance validator identifies the missing propagation obligations.

## 3. Positive conformance case

The same synthetic change includes:

1. source Decision/Gate/Closure;
2. source commit;
3. impact analysis;
4. affected assets;
5. unaffected assets with reasons;
6. required version changes;
7. claim/evidence consequences;
8. gate consequences;
9. RMA update;
10. dependent current-asset updates;
11. STATUS update;
12. CHANGELOG entry;
13. machine validator PASS;
14. human consistency closure;
15. next gate state.

Expected result: **PASS / PROGRESSION PERMITTED**.

## 4. Required invariants

The test must demonstrate:

- historical artifacts remain immutable;
- current pointers may advance only to explicit versions;
- evidence levels do not change without evidential support;
- missing propagation blocks progression;
- an accepted change cannot be considered fully propagated merely because it is mentioned elsewhere;
- current RMA, STATUS, claim/evidence control and next gate must converge on one current state.

## 5. Governance conformance criterion

`GCT-1 PASS` iff both negative and positive cases produce their expected outcomes.

A passing test establishes **governance-process conformance**, not scientific validity.

## 6. Relationship to the normal workflow

This test validates the mechanism specified in:

`00_GOVERNANCE/workflows/CURRENT_STATE_PROPAGATION_AND_CONSISTENCY_WORKFLOW_v0.1.md`

It does not replace the mandatory impact analysis or human consistency closure for real changes.
