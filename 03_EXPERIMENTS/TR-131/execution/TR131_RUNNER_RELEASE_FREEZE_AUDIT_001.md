# TR-131 — Runner Release/Frozen Audit 001

**Status:** FAIL — RELEASE BLOCKED / SCIENTIFIC EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-23  
**Canonical source:** GitHub `origin/main`

## Scope

Audit the actual V003 runner against the frozen protocol, the corrected construction requirements, and the successful 11-test execution.

## Verified

- V003 source exists in the canonical repository.
- V003 unit suite executed locally: **11/11 PASS, 0 errors, 0 failures**.
- Protocol identifier is the frozen `TR131_CROSS_DOMAIN_COMPARISON_PROTOCOL_FREEZE_001`.
- Input/implementation SHA-256 fields are emitted by the runner.
- Derived records preserve `S_t` and `S_t1`.
- Cross-domain raw transformation identities are not pooled.
- No VSL/value computation is performed by the derivation logic.
- Trajectory divergence is bounded to explicit trajectory groups and common source states.

## Release-blocking finding

### R1 — Allow-list is not actually enforced

The runner defines an analytical allow-list:

`ALLOWED={domain, record_id, S_t, T_acc_t, T_real_t, S_t1, T_acc_t1, trajectory_id, step}`

but its validation logic only rejects fields intersecting the explicit `FORBIDDEN` set.

Therefore an arbitrary unrecognized field not present in `FORBIDDEN` is silently accepted.

This does not satisfy the prior traceability requirement for an **explicit analytical-field allow-list** and leaves an avoidable data-ingress path.

The unit tests do not detect this because they test one explicitly forbidden field (`value`) rather than an arbitrary unrecognized field.

## Decision

**FAIL — RUNNER RELEASE BLOCKED.**

The 11/11 unit-test PASS remains valid as a test result, but it does not cure R1 because the frozen implementation requirement itself is stronger than the current tests.

No scientific evidence may be supplied to V003.

## Required correction

V004 must:

1. reject every input field outside `ALLOWED`;
2. distinguish `UNAUTHORIZED_FIELD` from `FORBIDDEN_OUTCOME_VALUE_FIELD`;
3. add a unit test containing an arbitrary unknown field (e.g. `foo`);
4. rerun the complete suite;
5. preserve all existing V003 behaviour.

No scientific evidence or protocol change is required.

## Next gate

**RUNNER V004 CORRECTION + COMPLETE UNIT-TEST EXECUTION.**

Only after that PASS can the runner be frozen for scientific analysis.
