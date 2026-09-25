# TI-001 V008 Fixture Canonical Freeze Authorization 001

**Status:** AUTHORIZATION PENDING — FREEZE NOT AUTHORIZED

## Authorization purpose

Authorize, when explicitly confirmed, only the canonical registration and freeze of the already generated and integrity-validated V008 fixture.

## Bound artifact

- Fixture ID: `TI001-V008-FIXTURE-001`
- Fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Generator ID: `TI001-V008-FIXTURE-GENERATOR-001`
- Generator blob SHA-1: `f345c41371a189c43b69b707b49b7eb17d140f55`
- Schema ID: `TI001-V008-DU-SCHEMA-001`
- Schema blob SHA-1: `d9539790452b047bc845a19bdcf50b8713a42b2a`
- Seed: `20260925`
- Scientific execution: `NOT_PERFORMED`

## Preconditions

- Generator/schema binding preflight: PASS.
- Provider–contract compatibility preflight: PASS.
- Fixture Integrity Preflight: PASS.
- Fixture has not been used for model/API execution.
- No scientific result is attached to the fixture.

## Authorized scope upon explicit confirmation

Only:

1. commit the exact generated fixture JSON to the canonical GitHub repository;
2. commit the corresponding generated integrity manifest;
3. verify their committed identities and bindings;
4. record the resulting canonical commit and freeze identity;
5. mark the fixture as frozen.

## Explicit exclusions

This authorization does not authorize:

- model/API calls;
- scientific execution;
- response generation or collection;
- scoring;
- value computation;
- statistical analysis;
- interpretation;
- provider execution;
- execution-contract activation;
- modification of the fixture contents;
- modification of the generator, schema, or provider.

Any change to the fixture bytes after authorization invalidates this authorization and requires a new freeze authorization.

## Required confirmation

The canonical freeze may proceed only after an explicit confirmation equivalent to:

**“Autorizo el Canonical Freeze V008 bajo estos bindings.”**

Until that confirmation is recorded, status remains:

**AUTHORIZATION PENDING — FREEZE NOT AUTHORIZED**

## Scientific status

`scientific_execution = NOT_PERFORMED`.
