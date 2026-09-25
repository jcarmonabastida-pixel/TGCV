# TI-001 V008 Fixture Schema & Serialization Completeness Gate 001

**Status:** OPEN — SPECIFICATION COMPLETION REQUIRED  
**Scientific execution:** NOT_PERFORMED  
**Fixture generated:** false  
**Generation authorized:** true

## Purpose

Establish the technical completeness gate that must be passed before the authorized V008 fixture-generation implementation can be completed.

This gate does not alter the scientific design and does not generate a fixture.

## Required specification elements

The V008 specification MUST define, unambiguously and reproducibly:

1. exact fixture schema;
2. exact fields for each decision unit;
3. field types and allowed values;
4. exact ordering of the 420 decision records;
5. exact mapping from the 210 pair IDs to the two decision instances per pair;
6. exact materialization of condition and presentation variant;
7. exact hidden-versus-exposed field boundary;
8. exact canonical JSON serialization;
9. encoding and newline rules;
10. fixture-level metadata and provenance fields;
11. deterministic fixture identity/hash calculation;
12. reconstruction requirements sufficient for Executor-2 to reproduce the fixture without reading the generated fixture.

## Scientific boundary

This gate is a design/integrity gate only.

It MUST preserve:

`scientific_execution = NOT_PERFORMED`

No model/API call, agent response, scientific outcome, or value measurement is permitted.

## Current finding

The deterministic PRNG and Fisher-Yates semantics are already specified and preflighted. However, the current V008 specification does not yet fully define the materialized fixture schema and canonical serialization needed for an independently reproducible generated artifact.

Therefore fixture generation remains blocked despite the explicit generation authorization.

## Gate decision

**NOT YET PASSABLE.**

The next action is to amend the V008 Generator Specification 001 with the missing fixture-schema and serialization definitions, then run a dedicated completeness preflight before modifying the generator.

## Non-regression constraint

The following MUST remain unchanged unless separately authorized as a scientific design change:

- 210 pairs;
- 70 control / 70 treatment / 70 null;
- 420 decision instances;
- 105 I1_FIRST / 105 I2_FIRST;
- seed `20260925`;
- xorshift32 semantics;
- independent condition and presentation streams;
- Fisher-Yates semantics;
- scientific execution boundary.
