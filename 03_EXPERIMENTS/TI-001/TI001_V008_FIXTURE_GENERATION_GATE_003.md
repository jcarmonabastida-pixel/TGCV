# TI-001 V008 Fixture Generation Gate 003

**Status:** READY — GENERATION NOT AUTHORIZED BY THIS GATE
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## Revalidated bindings

- Generator blob SHA-1: `f345c41371a189c43b69b707b49b7eb17d140f55`
- Reconciled Decision Unit Schema blob SHA-1: `d9539790452b047bc845a19bdcf50b8713a42b2a`
- Generator–Schema Binding Preflight: PASS
- Binding result commit: `a35816bf0f8ca9e943ba48d3c08f87061fb811e7`
- Presentation-order reconciliation: approved and incorporated
- No V008 fixture generated
- No model/API/scientific execution performed

## Scope

This gate permits only the deterministic V008 fixture-generation operation after a generation authorization explicitly binds the current generator and reconciled schema hashes.

Generation may produce:
- the V008 fixture JSON;
- canonical fixture SHA-256;
- external integrity manifest;
- generation environment metadata.

Generation must retain `scientific_execution = NOT_PERFORMED`.

## Explicit exclusions

This gate does not authorize model/API calls, scientific execution, scoring, value measurement, interpretation, schema redesign, or generator semantic changes.

## Authorization state

The earlier V008 generation authorization was issued before the approved schema reconciliation. Therefore it is not treated as sufficient authorization for execution against the newly bound schema.

A fresh authorization must explicitly bind:

- generator SHA `f345c41371a189c43b69b707b49b7eb17d140f55`;
- schema SHA `d9539790452b047bc845a19bdcf50b8713a42b2a`;
- seed `20260925`;
- deterministic fixture generation only.

## Next controlled action

Obtain fresh explicit authorization for generation under these exact bindings. Until then, the generator MUST NOT be invoked.
