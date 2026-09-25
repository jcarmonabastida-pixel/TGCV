# TI-001 V008 Fixture Generation Authorization 003

**Status:** AUTHORIZED — DETERMINISTIC GENERATION MAY PROCEED

## Authorization

The user explicitly authorizes deterministic V008 fixture generation under the reconciled generator/schema bindings.

## Bound artifacts

- Generator blob SHA-1: `f345c41371a189c43b69b707b49b7eb17d140f55`
- Decision Unit Schema blob SHA-1: `d9539790452b047bc845a19bdcf50b8713a42b2a`
- Seed: `20260925`
- Presentation-order reconciliation: approved
- Generation gate: `TI001_V008_FIXTURE_GENERATION_GATE_003.md`

## Authorized scope

Only:
- deterministic fixture generation;
- canonical fixture SHA-256 calculation;
- external integrity manifest generation;
- generation environment metadata.

## Explicit exclusions

Not authorized:
- model/API calls;
- scientific agent execution;
- scoring;
- value measurement;
- interpretation;
- schema changes;
- generator semantic changes;
- substitution of another fixture.

`scientific_execution` MUST remain `NOT_PERFORMED` during this operation.
