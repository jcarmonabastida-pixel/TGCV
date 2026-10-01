# TGCV — O4/E3 Primitive Measurement Specification Review v0.1

**Status:** CLOSED — MEASUREMENT CLASS CONDITIONALLY SPECIFIED / NOT ADMITTED
**Date:** 2026-10-01
**Gate:** O4_E3_PRIMITIVE_MEASUREMENT_SPECIFICATION_REVIEW

## 1. Decision

E3 can be specified as an independently inspectable structural-compatibility observation, but its concrete measurement function remains source/environment specific. Therefore E3 is not yet admitted as an empirical Ω_T relation.

## 2. Frozen E3 contract

For two transformation identities u and v, define an observed relation record:

`e3 = (id(u), id(v), relation_type, evidence_ref, observation_time, provenance)`

`relation_type = COMPATIBLE` is admissible only when a pre-specified structural compatibility test returns PASS from the primitive structural record.

The test may not inspect T_acc, outcome, reward, value, future trajectory, success, or any variable derived from those quantities.

## 3. Measurement requirements

The source/environment-specific E3 test must:

1. be frozen before outcome observation;
2. operate on primitive structural fields that are independently recorded or measured;
3. produce an auditable evidence_ref pointing to those fields/observations;
4. be deterministic given the frozen primitive record and rule version;
5. define UNKNOWN/NOT-OBSERVABLE separately from INCOMPATIBLE;
6. preserve directionality if the underlying structural relation is directional;
7. preserve provenance across adjacent intervals;
8. avoid deriving the relation from co-accessibility, co-occurrence or future success.

## 4. Matched discrimination requirement

A synthetic environment intended to test architectural non-equivalence must permit matched observations with:

`A_1 = A_2`

while:

`E3_1 != E3_2`

and the difference must be supported by independently recorded primitive structural evidence.

If changing E3 necessarily changes A under the frozen A representation, the candidate is A-equivalent for that environment.

## 5. Raw observation requirement

A hidden relation in the generator is not sufficient.

The environment must emit the primitive evidence used by the E3 test, together with immutable provenance, before future trajectory execution.

This permits an auditor to recompute E3 from raw observations without access to the future outcome.

## 6. Longitudinal extension

For Ω_T dynamics, the same E3 measurement contract must be applied independently at adjacent intervals. Relation continuity/change must then be evaluated through π.

A single interval can establish an E3 candidate edge but cannot establish persistence, emergence, disappearance, replacement, split or merge.

## 7. Current disposition

E3 measurement class: **CONDITIONALLY SPECIFIED**.

Ω_T source admission: **NOT GRANTED**.

Concrete domain-specific E3 measurement: **NOT FROZEN**.

Scientific experiment: **NOT AUTHORIZED**.

## 8. Next gate

**O4_E3_A_RECONSTRUCTION_AND_NON_CIRCULARITY_AUDIT**

The next review must construct at least one candidate synthetic observation schema and determine, before any fixture freeze, whether E3 can differ while A remains matched and whether the E3 primitive evidence is genuinely independent of the outcome-generating mechanism.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.
