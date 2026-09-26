# TI-001 V011 Primary Execution Audit Specification 001

**Status:** GATE SPECIFICATION — E1 RESULT REQUIRES AUDIT BEFORE SCIENTIFIC ANALYSIS

## 1. Purpose

Audit the canonical Executor-1 E1 result for structural integrity, one-to-one coverage against the frozen fixture, response-validity consistency, traceability, and conformance with the frozen execution configuration.

The audit does not recode, repair, retry, impute, pool, or interpret scientific effects.

## 2. Canonical bindings

- Fixture ID: `TI001-V011-FIXTURE-001`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Executor version: `TI001-V011-SCIENTIFIC-EXECUTOR-001`
- Interface Git blob SHA: `8667b0ff70f58283c688f24c76f10db142655d14`
- Generator Git blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema Git blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Model: `gpt-5.6-luna`
- Population: 420 units / 210 pairs / 70 pairs per condition.

## 3. Required audit checks

The checker must verify:

1. E1 result exists and is valid JSON.
2. Result type is `TI001-V011-SCIENTIFIC-EXECUTION`.
3. Scientific execution status is `PERFORMED`.
4. Fixture, interface, generator, schema, executor version and model bindings are exact.
5. Declared decision count is 420 and exactly 420 records are present.
6. Decision IDs are unique and exactly match the fixture in serialized order.
7. For every decision ID, pair, condition, and presentation exactly match the frozen fixture.
8. Every pair occurs exactly twice.
9. Conditions and presentations retain the frozen population balances.
10. Response IDs are present and unique.
11. Response status, raw output representation, validity, and validated decision are internally consistent with the frozen A/B validator semantics.
12. `valid_count` is recomputed from records and matches the observed count.
13. Request/response timestamps are present and ordered.
14. Runtime metadata is present.
15. No prohibited scientific outcome fields were introduced as execution variables.
16. The recorded generation configuration matches the frozen configuration.
17. The audit reports observed reasoning-token usage separately; it must not silently equate `reasoning: null` in the declared configuration with zero effective reasoning. Any non-zero `reasoning_tokens` is recorded as a runtime configuration observation requiring reconciliation before interpreting E1 as conformant with a no-reasoning configuration.
18. No inference, repair, retry, recoding, or imputation is evidenced in the execution record.

## 4. Scientific boundary

The 175 invalid responses, if confirmed by the audit, remain part of E1 evidence. They are not removed or transformed.

The audit produces no TI-001 effect estimate.

## 5. Outcome

**PASS** only when all structural and traceability checks pass and no unresolved configuration deviation is present.

**FAIL** blocks scientific analysis and requires reconciliation of the identified execution-level deviation(s).
