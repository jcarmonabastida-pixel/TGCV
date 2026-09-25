# TI-001 V008 Fixture Generation Gate 002

**Status:** READY — GENERATION NOT AUTHORIZED
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## Preconditions

1. V008 deterministic generator specification exists and its self-test has passed.
2. V008 Decision Unit Schema Integrity Preflight has passed against schema blob SHA `e0da4352f74a518f7e1bc7c9532a171bf5167735`.
3. V008 Generator–Schema Binding Preflight has passed against generator blob SHA `f345c41371a189c43b69b707b49b7eb17d140f55`.
4. The generator is constrained to require an explicit binding manifest.
5. No V008 fixture has been generated.
6. No model/API call is involved or authorized.

## Generation scope

If separately authorized, the operation may:

- materialize the deterministic V008 fixture;
- calculate the canonical fixture SHA-256;
- create the external integrity manifest binding fixture SHA-256, schema blob SHA-1, and generator blob SHA-1;
- record generation environment metadata;
- retain `scientific_execution = NOT_PERFORMED`.

## Explicit exclusions

This gate does NOT authorize:

- model/API calls;
- scientific agent execution;
- scoring;
- value measurement;
- interpretation;
- modification of the approved schema;
- modification of the deterministic PRNG semantics;
- substitution of another fixture.

## Authorization rule

Generation requires an explicit generation authorization recorded after this gate is READY.

Until that authorization exists, the generator MUST NOT be invoked with a binding manifest.

## Next controlled action

Obtain explicit authorization for deterministic V008 fixture generation, then execute only the generator with the approved binding manifest.