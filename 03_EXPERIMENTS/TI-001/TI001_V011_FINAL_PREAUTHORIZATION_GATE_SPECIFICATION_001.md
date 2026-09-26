# TI-001 V011 Final Preauthorization Gate Specification 001

**Status:** GATE SPECIFICATION — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Purpose

Verify that the frozen V011 fixture, decision interface, compatibility preflight, and scientific execution contract are mutually bound and that no scientific execution has occurred before explicit authorization.

## Required PASS conditions

1. Canonical fixture exists and SHA-256 is `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`.
2. Fixture contains exactly 420 decision units and 210 pairs.
3. Generator Git blob SHA is `9170f767cac3fceccaba248747c6524c5f150e11`.
4. Schema Git blob SHA is `b2fef667f6eb33689ece5481957d3917a860dd3e`.
5. Decision-interface implementation Git blob SHA is `8667b0ff70f58283c688f24c76f10db142655d14`.
6. Decision-interface compatibility preflight result exists and has status `PASS`.
7. Compatibility preflight binds the same fixture, generator, and schema hashes.
8. Scientific execution contract exists and binds the same fixture, generator, schema, and interface hashes.
9. Contract status is `NOT AUTHORIZED`.
10. No V011 scientific execution result is accepted as evidence by this gate.
11. No authorization token or authorization record is created by this gate.

## Authorization rule

PASS means **READY FOR EXPLICIT AUTHORIZATION**. It does not itself authorize execution.

Scientific execution remains prohibited until the user explicitly authorizes it after this gate passes.

## Failure rule

Any failed condition blocks scientific execution. The fixture and scientific artifacts must not be modified merely to make this gate pass.

## Output

The gate result shall report:
- gate ID;
- PASS/FAIL;
- all checks;
- canonical bindings;
- scientific execution status;
- authorization status.

Expected state before explicit authorization:
- `scientific_execution = NOT_PERFORMED`
- `authorization = NOT_AUTHORIZED`
