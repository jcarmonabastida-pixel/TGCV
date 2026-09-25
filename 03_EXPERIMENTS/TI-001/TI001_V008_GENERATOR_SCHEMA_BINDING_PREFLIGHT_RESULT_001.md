# TI-001 V008 Generator–Schema Binding Preflight Result 001

**Status:** PASS
**Preflight ID:** TI001-V008-GENERATOR-SCHEMA-BINDING-PREFLIGHT-001
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## Canonical bindings

- Generator blob SHA-1: `f345c41371a189c43b69b707b49b7eb17d140f55`
- Schema blob SHA-1: `d9539790452b047bc845a19bdcf50b8713a42b2a`

## Result

All 27 reported binding checks passed, including the reconciled presentation-order rule.

The committed generator is bound to the approved V008 Decision Unit Schema and its deterministic implementation requirements. The preflight confirms materialization structure, allocation, presentation pairing, reconciled presentation ordering, serialization, fixture SHA-256 calculation, external integrity-manifest binding, explicit generation binding, Executor-2 independence, and the scientific boundary.

## Interpretation

This PASS establishes generator/schema conformance. It does not itself authorize fixture generation.

`fixture_generated = false` and `scientific_execution = NOT_PERFORMED` remain in force.

## Next gate

The next controlled action is the V008 Fixture Generation Gate. Generation must remain a separately authorized operation.