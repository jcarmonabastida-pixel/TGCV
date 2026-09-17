# TGCV — WP2 TSTC Engine Implementation Specification 001

**Status:** FROZEN — IMPLEMENTATION SPECIFICATION; EXECUTION NOT STARTED
**Date:** 2026-09-17
**Upstream fixture freeze:** `TGCV_APPLICATION_FIT_WP2_TSTC_SYNTHETIC_FIXTURES_FREEZE_001.md`

## 1. Purpose

Define the deterministic software contract required to implement the TSTC minimum demonstrator against the already frozen synthetic fixtures C01/C03/C05.

This document specifies implementation and preflight only. It does not define or report a TSTC execution result.

## 2. Engine boundary

Input:

`fixture + frozen S0 + C0 + L + Uτ + Pτ + intervention + baseline`

Processing:

`validate → calculate T_acc,0 → apply declared transition → validate transition → calculate T_acc,1 → calculate ΔT_acc → record trajectory → reconstruct baseline → compare representations → validate invariants`

Output is a machine-readable preflight/execution object. The implementation MUST NOT read downstream outcomes, future activity, samples, or external datasets.

## 3. Required modules

1. `fixture_loader`
2. `schema_validator`
3. `admissibility_engine`
4. `tacc_calculator`
5. `transition_engine`
6. `trajectory_recorder`
7. `baseline_engine`
8. `cross_domain_propagator`
9. `invariant_checker`
10. `reproducibility_metadata`
11. `preflight_runner`

The modules may be implemented in one file initially, provided the logical boundaries remain explicit and testable.

## 4. Canonical data contract

Every fixture MUST serialise the following fields:

```text
fixture_id
fixture_version
connector_id
state
context
ruleset_version
transformation_universe
intervention
baseline
coupling_rules
```

Every transformation MUST have:

```text
transformation_id
domain
preconditions
affected_variables
transition_operator
```

Every admissibility evaluation MUST return:

```text
transformation_id
admissible
predicate_trace
```

`predicate_trace` MUST identify only declared state/context/rule inputs and MUST NOT contain outcome-derived information.

## 5. T_acc calculation

The canonical operation is:

`T_acc = { τ ∈ Uτ | Pτ(S,C,L)=1 }`

Requirements:

- `Uτ` is immutable during an evaluation;
- every returned transformation belongs to `Uτ`;
- every returned transformation evaluates true under its predicate;
- every excluded transformation evaluates false;
- ordering is canonical and deterministic;
- duplicate transformation identifiers fail closed.

## 6. Transition engine

A transition MUST identify:

```text
intervention_id
changed_variables
S_before
C_before
S_after
C_after
```

The engine MUST verify that every changed variable is explicitly listed in the intervention definition.

Undeclared mutations MUST cause preflight failure.

## 7. ΔT_acc

The engine MUST calculate:

```text
opened      = T_acc,1 − T_acc,0
closed      = T_acc,0 − T_acc,1
persistent  = T_acc,0 ∩ T_acc,1
changed     = T_acc,0 ≠ T_acc,1
```

No scalar score is permitted.

## 8. Trajectory

The trajectory recorder may contain only transformations that were admissible at the relevant decision point.

It MUST record:

```text
step
state_before
context_before
transformation_id
state_after
context_after
accessibility_basis
```

A trajectory containing an inadmissible transformation MUST fail the preflight.

## 9. Cross-domain propagation

Propagation MUST be explicit.

For each coupling edge:

```text
source_connector
source_condition
transition
 target_connector
target_condition
```

The engine MUST log the causal-by-design dependency as a fixture rule, but MUST NOT interpret it as empirical causality.

For the frozen minimum fixture:

`C01 security=restricted → C03 permission_repo=denied`

`C03 repo=changed → C05 mobility_requirement_A=urgent`

## 10. Baseline engine

The baseline receives the same frozen information available to the TGCV representation.

It MUST reconstruct feasible transformations without access to any additional variables.

Required baseline forms:

- C01: finite-state rule/feasible-action model;
- C03: capability/permission matrix + workflow state;
- C05: finite constrained-feasibility model;
- cross-domain: explicit dependency graph.

The comparison layer MUST report representational observations only. It MUST NOT compute a superiority score.

## 11. Negative controls

The preflight MUST execute the negative controls defined in the frozen fixture specification.

Expected invariant:

`ΔT_acc = ∅`

If a negative control produces a non-empty ΔT_acc, preflight status is `BLOCKED — NEGATIVE_CONTROL_VIOLATION`.

## 12. Reproducibility

The implementation MUST record:

```text
source_commit
fixture_id
fixture_version
ruleset_hash
transformation_universe_hash
intervention_id
configuration_hash
environment
random_seed
output_hash
```

`random_seed` MUST be `null` for the initial deterministic implementation.

## 13. Preflight checks

The preflight MUST verify, at minimum:

1. schema completeness;
2. deterministic serialization;
3. unique transformation identifiers;
4. `T_acc ⊆ Uτ`;
5. predicate determinism;
6. no outcome/future-activity access;
7. declared-variable-only transitions;
8. valid trajectory transformations;
9. negative-control invariants;
10. explicit cross-domain propagation;
11. baseline information parity;
12. reproducibility metadata completeness;
13. repeat execution byte-equivalence for the same fixture.

## 14. Fail-closed conditions

The engine MUST stop rather than repair silently if it detects:

- missing predicate;
- hidden mutation;
- duplicate transformation identifier;
- transformation outside `Uτ`;
- predicate depending on downstream outcome;
- undeclared cross-domain edge;
- baseline receiving extra information;
- non-deterministic output;
- unexplained negative-control ΔT_acc;
- trajectory containing an inaccessible transformation.

## 15. Preflight-only execution boundary

The first executable command MUST be a preflight/conformance command operating solely on the frozen synthetic fixtures.

It MUST NOT:

- load real datasets;
- contact external infrastructure;
- perform sampling;
- calculate predictive metrics;
- access downstream outcomes;
- generate scientific evidence;
- modify governance state automatically.

## 16. Preflight status vocabulary

Allowed statuses:

- `PREFLIGHT_PASS`
- `PREFLIGHT_BLOCKED_SCHEMA`
- `PREFLIGHT_BLOCKED_INVARIANT`
- `PREFLIGHT_BLOCKED_NEGATIVE_CONTROL`
- `PREFLIGHT_BLOCKED_REPRODUCIBILITY`
- `PREFLIGHT_BLOCKED_BASELINE_PARITY`

No other status may be introduced without a specification revision.

## 17. Execution gate after preflight

A `PREFLIGHT_PASS` does NOT authorize the TSTC experiment by itself.

After preflight, the next governance decision must separately authorize:

`TSTC EXECUTION`

Only that subsequent gate may permit the actual intervention/trajectory comparison.

## 18. Governance boundary

This implementation specification does not modify:

- TGCV Core;
- RMA v3.35;
- Evidence→Claim Matrix v1.12;
- C09/C10 scientific conclusions;
- VSL-44;
- industrial execution authorization.

**Next controlled action:** implement this contract and run preflight only.
