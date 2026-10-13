# Collective Toy — Exception Contract Sweep 001

**Status:** static source audit only; no runtime execution claimed.
**Engine blob reviewed:** `f7816e325beb580779badfae1e35bcd8235cf5d4`
**Test blob reviewed:** `b62d9a05f8116d3c2da75d2bc39919af7680705f`
**Review date:** 2026-10-13.

## Scope

Reviewed the canonical-domain validator, schema validation, relation/scenario validation, graph exploration guards, and exported-package verification paths for obvious `TypeError`/`KeyError` leakage from malformed external input. This is a source-level review, not a proof over all possible Python objects and not a substitute for running the suite.

## Findings

### 1. Validation order generally protects set/dictionary operations

- State IDs are type-checked before `set(states)`.
- Transition `id`, `source`, and `target` are type-checked before dictionary membership and lookup.
- Relation identifiers and references are type-checked before set membership / transition lookup.
- Scenario disabled-transition entries are checked as non-empty strings before `set(disabled)` and set difference.
- Exploration bounds reject booleans explicitly, avoiding Python's `bool`-is-an-`int` behavior.
- Export verification checks package/result containers and required fields before hash and replay operations.

No clear raw `TypeError`/`KeyError` leak was identified in these inspected paths for JSON-shaped malformed input. This is a bounded finding, not a guarantee for arbitrary non-JSON Python objects.

### 2. Existing malformed-input tests

The fetched test blob contains 98 named test methods and includes:
- a deterministic 19-case malformed-input mutation matrix expecting `ModelValidationError`;
- exact-message assertions for top-level model, schema version, model ID, container types, nested transition/relation/scenario objects, baseline, and relation reference errors;
- canonical-domain rejection for unsafe integers, non-finite/fractional numbers, unpaired Unicode surrogates, non-JSON values, and non-string object keys;
- package integrity and independent replay mismatch tests.

These are source-visible assertions. They are not runtime evidence for the current audit branch head.

## Remaining limitations

1. The 19-case mutation matrix is finite and does not cover every combination or every malformed nested field.
2. Tests should be run on the exact branch head after the trajectory-cap regression test was added.
3. Browser/Python concordance covers fixtures exercised, not universal equivalence.
4. This audit does not claim exception behavior for arbitrary custom Python objects; the intended external input domain is JSON-shaped data.

## Disposition

No engine change is justified by the reviewed evidence. Avoid adding a generic catch-all that masks programming errors as validation failures. If exact-head CI reveals a raw exception for a valid JSON-shaped malformed input, add a minimal regression test with an independent expected error and fix only that path.

No runtime tests were executed by this report. Scientific execution remains disabled; no promotion or merge is authorized.
