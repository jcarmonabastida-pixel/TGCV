# TGCV Application Fit WP2 — TSTC Synthetic Fixture 002 Specification 001

**Status:** `SPECIFICATION ONLY — NOT FROZEN; FIXTURE 001 UNCHANGED; EXECUTION NOT AUTHORIZED`

## 1. Purpose

Define the controlled requirements for a new synthetic fixture version (`Fixture 002`) that makes executable transition semantics explicit without silently modifying or reinterpreting frozen Fixture 001.

Fixture 002 is intended to resolve the operationalisation gap identified by the Fixture-001 transition-semantics provenance audit while preserving the scientific question, intervention structure, negative controls, and C01→C03→C05 coupling architecture.

This document is a specification for review. It is **not** the Fixture 002 data itself and does not authorize execution.

## 2. Non-negotiable boundary

Fixture 001 remains immutable at version `001`.

No implementation adapter may infer missing transition semantics into Fixture 001.

Fixture 002 must be created as a new version and explicitly frozen only after its complete contents have been reviewed for semantic traceability.

## 3. Scientific identity to preserve

Unless a formal change is explicitly justified and separately authorized, Fixture 002 must preserve:

- the same connector domains C01, C03 and C05;
- the same initial state and context values;
- the same transformation identities;
- the same admissibility predicates;
- the same positive interventions;
- the same negative controls;
- the same two cross-domain coupling rules;
- the same bounded TSTC question;
- the same baseline-information boundary;
- the same scientific non-claims.

The purpose of version 002 is to make transition semantics explicit, not to redesign the experiment.

## 4. Required transition schema

Every transformation retained in Fixture 002 must explicitly define:

- `transformation_id`
- `domain`
- `preconditions`
- `affected_variables`
- `transition_operator`
- `transition_postcondition`
- `semantic_provenance`

`semantic_provenance` must identify whether the transition is:

- `EXPLICITLY_DEFINED_FOR_FIXTURE_002`
- `DERIVED_FROM_EXPLICIT_FIXTURE_002_RULE`

No `INFERRED_FROM_IMPLEMENTATION` category is permitted.

## 5. Transition completeness requirement

For every transformation used in a trajectory, the operator must define a deterministic mapping:

`(S_before, C_before) -> (S_after, C_after)`

Only declared affected variables may change.

Any undeclared mutation must fail closed.

A transformation may remain in the transformation universe without an executable operator only if it is explicitly marked `NON_TRAJECTORY / NOT_EXECUTED` and the demonstrator does not require it. Otherwise the fixture is incomplete and cannot be frozen.

## 6. C01 requirements

Fixture 002 must explicitly specify executable semantics for the C01 transformations required by the demonstrator.

At minimum:

- `c01.restrict_security`: `security normal -> restricted`
- `c01.restore_security`: `security restricted -> normal`

For trajectory completeness, the deploy and routing transformations must also receive explicit deterministic operators if they remain eligible for trajectory use.

Their operators must be specified from the fixture scenario itself, not copied into the scientific specification merely because an implementation currently performs them.

## 7. C03 requirements and critical decision

The C03 domain requires explicit semantics for the transformation that produces the repository-state transition needed by the frozen coupling sequence.

The required state change is:

`repo: clean -> changed`

Fixture 002 must **not** assign this effect arbitrarily to `c03.inspect_repo`, `c03.open_pr`, or `c03.complete_task`.

Instead, the Fixture-002 design must introduce or identify an explicit transformation whose declared meaning is that a repository-changing action occurs and whose transition operator deterministically produces `repo=changed`.

If the scientific scenario cannot justify such a transformation without changing the intended experiment, then the C03→C05 coupling rule must remain non-executable and the fixture must not be frozen as a complete end-to-end demonstrator.

Any new transformation identity constitutes a scientific fixture change and must be explicitly documented as such rather than presented as a repair of Fixture 001.

## 8. C05 requirements

Fixture 002 must explicitly specify deterministic operators for the C05 transformations required for trajectory recording.

At minimum, the operators must respect the declared state variables and must not mutate variables outside their `affected_variables` declaration.

The positive intervention remains:

`grid_capacity: high -> low`

The negative control remains identity-preserving and must continue to yield:

`Delta_T_acc = ∅`

## 9. Cross-domain coupling

The following coupling rules remain frozen in conceptual form:

1. `C01 security=restricted -> C03 permission_repo=denied`
2. `C03 repo=changed -> C05 mobility_requirement_A=urgent`

Fixture 002 must make the transition producing `repo=changed` explicit before the second coupling can be executed.

Propagation must be recorded separately from local effects.

No additional cross-domain dependencies may be introduced merely to obtain a successful result.

## 10. Interventions and controls

The positive interventions remain unchanged:

- C01: `trust_B trusted -> untrusted`
- C03: `permission_repo granted -> denied`
- C05: `grid_capacity high -> low`

The negative controls remain unchanged:

- C01: `routing A -> B` with no predicate dependency initially
- C03: identity-preserving `tool_query available -> available`
- C05: identity-preserving `mobility_requirement_A normal -> normal`

Fixture 002 must preserve the expected negative-control property:

`Delta_T_acc = ∅`

No negative control may be weakened or redesigned to accommodate the transition operators.

## 11. Accessibility predicates

Predicates remain outcome-independent and deterministic.

Fixture 002 must not add future activity, downstream outcomes, realized trajectory information, value, or baseline performance information to any admissibility predicate.

`T_acc` remains a subset of the declared finite transformation universe.

## 12. Baseline compatibility

Fixture 002 must retain sufficient frozen information to reconstruct the conventional baseline under the same information boundary as TSTC.

No baseline may receive additional information unavailable to the TSTC representation.

No aggregate superiority score is permitted.

## 13. Reproducibility

A frozen Fixture 002 must have deterministic canonical serialization and hashes for:

- fixture definition;
- ruleset;
- transformation universe;
- coupling rules;
- configuration;
- intervention set;
- negative-control set.

The frozen record must include fixture version and complete provenance.

## 14. Required validation before freezing

Fixture 002 cannot be frozen until all of the following pass:

1. schema completeness;
2. unique transformation IDs;
3. explicit affected-variable declarations;
4. deterministic transition operators;
5. operator mutation boundary;
6. deterministic admissibility predicates;
7. trajectory completeness for every executed transformation;
8. explicit C01→C03 propagation;
9. explicit C03→C05 propagation;
10. explicit provenance for `repo: clean -> changed`;
11. negative controls produce `Delta_T_acc = ∅`;
12. baseline information parity;
13. deterministic serialization and hashes;
14. byte-equivalent reconstruction.

## 15. Freeze gate

The specification does **not** authorize execution.

Before freezing Fixture 002, a review record must establish that every newly added transition semantic is either explicitly defined by the new fixture scenario or is a transparent derivation from an explicit Fixture-002 rule.

If any transition remains implementation-derived or ambiguous, freezing must fail closed.

## 16. Expected execution sequence after separate authorization

Only after Fixture 002 is separately frozen and execution is separately authorized may the following sequence be considered:

1. preflight/conformance;
2. C01 positive and negative control;
3. C03 positive and negative control;
4. C05 positive and negative control;
5. C01→C03→C05 cross-domain sequence;
6. trajectory recording;
7. baseline reconstruction;
8. invariant checks;
9. byte-equivalence rerun.

A preflight pass does not itself authorize execution.

## 17. Scientific boundary

Even a successful Fixture-002 TSTC execution would establish only a bounded synthetic applicability observation under the frozen scenario.

It would not establish:

- scientific validity of TGCV as a general theory;
- empirical causality;
- superiority over conventional approaches;
- generality across domains;
- value creation;
- `Delta_T_acc -> Delta_V`;
- deployment readiness;
- industrial authorization.

## 18. Decision

**Fixture 002 specification prepared for controlled review.**

No Fixture-002 data has been frozen.

Fixture 001 remains unchanged.

No TSTC execution has been performed under this specification.
