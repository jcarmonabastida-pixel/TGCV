# TI-001 V008 Fixture Generation Authorization 002

**Status:** AUTHORIZED — DETERMINISTIC GENERATION MAY PROCEED
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## Authorization

Explicit authorization is recorded to generate the deterministic V008 fixture defined by the approved schema and bound generator.

## Authorized scope

- V008 deterministic fixture generation only;
- seed `20260925`;
- approved schema blob SHA-1 `e0da4352f74a518f7e1bc7c9532a171bf5167735`;
- approved generator blob SHA-1 `f345c41371a189c43b69b707b49b7eb17d140f55`;
- generation of the canonical fixture JSON;
- calculation of the fixture SHA-256;
- generation of the external integrity manifest.

## Explicit exclusions

This authorization does NOT authorize model/API calls, scientific agent execution, scoring, value measurement, interpretation, or any change to the approved schema or generator semantics.

## Scientific boundary

Fixture generation is a deterministic pre-execution activity.
`scientific_execution = NOT_PERFORMED` remains mandatory.

## Required post-generation audit

After generation, verify fixture bytes, SHA-256, manifest bindings, 210 pairs, 420 Decision Units, 70/70/70 condition allocation, complementary presentation assignment, exact serialization, and absence of scientific execution before the fixture is accepted as canonical.