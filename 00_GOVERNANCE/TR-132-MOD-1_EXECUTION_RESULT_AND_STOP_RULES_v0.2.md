# TR-132-MOD-1 — Execution Result and Stop Rules v0.2

**Status:** FROZEN PRE-EXECUTION TEMPLATE
**Fixture:** `MOD1-FX-001`
**Execution:** NOT AUTHORIZED

## Required result fields
`EXECUTION_ID`, `PROTOCOL_VERSION`, `PACKAGE_VERSION`, `FIXTURE_MANIFEST_HASH`, `FREEZE_ID`, `TIMEPOINTS`, `CANDIDATE_UNIVERSE_HASH`, `PREDICATE_VERSION`, `EVIDENCE_MANIFEST_HASH`, `ADJUDICATION_HASH`, `CERTIFIED_TACC_PLUS_T0`, `CERTIFIED_TACC_PLUS_T1`, `OBSERVED_T0`, `OBSERVED_T1`, `ACHIEVED_LEVEL`, `NON_CIRCULARITY_STATUS`, `REPRODUCIBILITY_STATUS`, `DEVIATIONS`, `DECISION`, `BOUNDED_INTERPRETATION`.

## Pre-declared L3 target
The frozen target is to demonstrate a non-empty symmetric difference between certified bounded accessible sets at `t0` and `t1` under invariant candidate universe, identity, predicate and evidence rules.

Expected control classifications are stored separately and are not an execution result.

## Stop rules
- Any post-freeze definition change: `INVALID`.
- Any use of realization to establish accessibility: `INVALID`.
- Any missing mandatory evidence treated as accessibility: `INVALID`.
- Any candidate-universe change after adjudication: `INVALID`.
- Failure to demonstrate the pre-declared minimum level: `FAIL` or `INCONCLUSIVE` under the protocol.
- Conforming bounded L3 demonstration: `BOUNDED PASS`.

No result may be interpreted as full real-world `T_acc` closure, causal evidence, value evidence, industrial utility, or Core validation.
