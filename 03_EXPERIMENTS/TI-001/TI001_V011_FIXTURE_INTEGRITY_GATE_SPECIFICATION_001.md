# TI-001 V011 Fixture Integrity Gate Specification 001

**Status:** GATE SPECIFICATION — FIXTURE GENERATED / INTEGRITY NOT YET VERIFIED

## 1. Purpose

Verify that the generated V011 fixture is exactly the deterministic fixture specified by the frozen generator, schema, and serialization contract.

This gate does not authorize scientific model execution.

## 2. Bound inputs

- Fixture: `TI001-V011-FIXTURE-001`
- Expected decision units: 420
- Expected pairs: 210
- Seed: 20260926
- Generator SHA-256: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema SHA-256: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Generated fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`

## 3. Required checks

1. Fixture exists and is valid UTF-8 JSON.
2. Exact fixture identity fields match the frozen contract.
3. Exact SHA-256 of the fixture bytes matches the generated hash above.
4. Exact 420 decision units and 210 unique pairs.
5. Exactly two units per pair, one `I1_FIRST` and one `I2_FIRST`.
6. Exactly 70 pairs and 140 units per condition.
7. Exactly 210 units per presentation.
8. Exactly 35 first-orientation pairs per condition for each orientation.
9. Exact decision-unit field order and nested field order.
10. Exact A/B action set and future-structure semantics.
11. No utility, reward, value, performance, task-success, outcome, response, or scientific-score fields.
12. No duplicate decision IDs or pair IDs.
13. Generator and schema source hashes match the frozen identities.
14. Deterministic reconstruction reproduces the same fixture bytes.

## 4. Disposition

PASS requires every check to be true.

FAIL blocks fixture canonicalization and all scientific execution.

`scientific_execution` must remain `NOT_PERFORMED` for this gate.

## 5. Output

The gate result must record all individual checks, the verified fixture SHA-256, generator SHA-256, schema SHA-256, seed, decision count, and scientific execution status.
