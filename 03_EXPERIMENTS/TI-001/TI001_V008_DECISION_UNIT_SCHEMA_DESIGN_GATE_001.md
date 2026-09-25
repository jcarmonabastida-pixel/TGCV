# TI-001 V008 Decision Unit Schema Design Gate 001

**Status:** OPEN — NEW SCHEMA DESIGN REQUIRED
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false
**Generation authorized:** true
**Design identity:** NEW V008 SCHEMA — NOT A RECOVERY OF V007

## Purpose

Open a controlled design gate for the exact materialized Decision Unit schema required by the V008 deterministic fixture.

Canonical recovery was attempted through the available GitHub repository search for TI-001/V005/V006/V007 identifiers, Decision Unit terms, fixture fields, and related TI metrics. No accessible canonical artifact defining the complete materialized schema was recovered.

Therefore no historical schema is being inferred or silently reused.

## Design boundary

The new schema must explicitly define, before fixture generation:

1. Decision Unit identity and stable ordering.
2. Pair identity and condition assignment.
3. Presentation variant and its relationship to I1/I2.
4. Action representation for A/B.
5. Exactly which information is exposed to the agent.
6. Exactly which information remains hidden.
7. Treatment-only future structure representation.
8. Absence of successor realization before the decision.
9. Absence of utility, reward, value, or performance feedback.
10. Field types, nullability, and allowed values.
11. Canonical record ordering.
12. Canonical JSON serialization, encoding, and newline convention.
13. Fixture metadata and provenance fields.
14. Binding to the deterministic generator and its source blob SHA.
15. Independent reconstruction requirements.

## Non-inference rule

The schema must not be justified as recovered V007 design unless a canonical V007 artifact is subsequently located.

Any element introduced here is a V008 design decision and must be traceable to the V008 experimental specification.

## Scientific boundary

Schema design is a pre-execution activity.

`scientific_execution = NOT_PERFORMED`

No model/API call, response collection, scientific scoring, or scientific execution is permitted during this gate.

## Generation constraint

The existing V008 generator remains blocked. The authorization recorded for deterministic generation does not authorize inventing or implicitly selecting an incomplete Decision Unit schema.

## Exit criteria

This gate may close only when:

- the complete V008 Decision Unit schema is explicitly specified;
- all exposed/hidden fields are defined;
- serialization is deterministic;
- schema decisions are traceable to the V008 design;
- the generator implementation is updated only if required by the approved schema;
- a schema-specific integrity preflight passes;
- source/blob bindings are updated and verified;
- independent reconstruction requirements are satisfied.

## Next action

Produce the explicit V008 Decision Unit Schema Specification as a separate design artifact. Do not generate the fixture until that specification and its integrity preflight pass.
