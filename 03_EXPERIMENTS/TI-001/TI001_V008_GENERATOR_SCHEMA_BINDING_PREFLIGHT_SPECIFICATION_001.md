# TI-001 V008 Generator–Schema Binding Preflight Specification 001

**Status:** DESIGN — PREIMPLEMENTATION
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## Purpose

Define the integrity gate that must pass before the V008 generator may materialize the fixture.

## Required bindings

The preflight MUST bind:

- generator ID `TI001-V008-FIXTURE-GENERATOR-001`;
- generator implementation commit `ca2219420ffdab20c4bb4d98e116ab9eb3b989b3` only for the currently frozen blocked implementation;
- generator blob SHA `bcc86196060db50a62e512549c94a84c55561669` only for that implementation;
- approved schema ID `TI001-V008-DU-SCHEMA-001`;
- approved schema blob SHA `e0da4352f74a518f7e1bc7c9532a171bf5167735`.

## Implementation requirement

The current generator is intentionally blocked and does not yet materialize Decision Units. Therefore this preflight cannot authorize generation until an implementation conforming to the approved schema is committed and its new blob SHA is independently verified.

The implementation MUST preserve the already validated xorshift32/Fisher-Yates semantics, seed `20260925`, independent condition/presentation streams, and the six existing deterministic self-test vectors.

## Required materialization checks

The executable binding preflight MUST verify:

1. exact fixture top-level field order;
2. exact seven Decision Unit fields and order;
3. exact nested field order;
4. 210 pairs and 420 Decision Units;
5. 70/70/70 pair allocation;
6. paired I1_FIRST/I2_FIRST presentation;
7. pair-level condition consistency;
8. agent-facing versus hidden field boundary;
9. treatment/control/null future-structure mapping;
10. canonical Decision Unit ordering;
11. compact UTF-8 JSON with exactly one final LF and no BOM;
12. fixture SHA-256 calculated over the exact fixture bytes;
13. external integrity manifest binding fixture SHA-256, schema blob SHA-1, and generator blob SHA-1;
14. Executor-2 reconstruction independence.

## Scientific boundary

No model/API call is permitted. Fixture generation remains a pre-execution activity and must retain `scientific_execution = NOT_PERFORMED`.

## Gate rule

PASS permits the separate V008 Fixture Generation Gate to evaluate generation authorization. It does not itself authorize generation.