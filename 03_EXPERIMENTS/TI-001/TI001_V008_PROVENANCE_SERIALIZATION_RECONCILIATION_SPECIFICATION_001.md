# TI-001 V008 Provenance and Serialization Reconciliation Specification 001

**Status:** DESIGN — RECONCILED, NOT YET PREFLIGHTED
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## 1. Resolution

The V008 fixture provenance requirement is reconciled without adding hidden or implicit fields to the canonical fixture JSON.

The exact top-level fixture serialization remains the five-field structure:

`fixture_id`, `schema_id`, `generator_id`, `seed`, `decision_units`.

The generator source blob SHA and schema specification blob SHA are provenance bindings of the fixture artifact and MUST be recorded in the accompanying fixture integrity manifest, not embedded as additional fixture JSON fields.

## 2. Canonical fixture JSON

The fixture JSON therefore remains exactly the structure already specified by the Decision Unit Schema Specification.

No additional top-level or Decision Unit fields may be introduced for provenance.

## 3. Integrity manifest binding

The V008 fixture integrity manifest MUST record:

- fixture_id;
- schema_id;
- generator_id;
- seed;
- canonical fixture SHA-256;
- exact schema specification Git blob SHA-1;
- exact generator source Git blob SHA-1;
- generation timestamp;
- generation environment identity sufficient for reproducibility;
- scientific_execution = NOT_PERFORMED for generation-stage records.

The integrity manifest is metadata external to the fixture JSON and does not alter the scientific Decision Unit schema.

## 4. Deterministic identity

The fixture identity is the canonical SHA-256 of the exact UTF-8 fixture JSON byte sequence, including its single final LF and excluding the external integrity manifest.

The integrity manifest binds that fixture SHA-256 to the exact schema and generator source blob SHAs.

## 5. Binding consequence

A fixture is considered canonically bound only when:

1. its serialized bytes conform to the approved schema;
2. its fixture SHA-256 is recorded;
3. the manifest records the exact schema blob SHA-1;
4. the manifest records the exact generator blob SHA-1;
5. the generator and schema identities match the approved V008 identities.

## 6. Scientific boundary

This reconciliation is a design/governance action only.

No fixture is generated.
No model/API call is performed.
No scientific result is produced.

`scientific_execution = NOT_PERFORMED`.

## 7. Next controlled action

Update the V008 Decision Unit Schema Specification to incorporate this reconciled provenance contract, then rerun the Schema Integrity Preflight. Generator implementation remains blocked until that preflight passes.