# TR-131 — Analysis Implementation Traceability Audit 001

**Document ID:** TR131_ANALYSIS_IMPLEMENTATION_TRACEABILITY_AUDIT_001  
**Status:** PASS WITH BOUNDARY — IMPLEMENTATION SPECIFICATION AUDITED / EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-23  
**Canonical source:** GitHub `origin/main`

## 1. Purpose

Audit the deterministic secondary-analysis implementation required by the frozen Cross-Domain Comparison Protocol before any result is generated.

The implementation must consume only already-persisted VisitAll and PRISM evidence and mechanically derive the frozen descriptors. It must not become a second scientific executor or alter source semantics.

## 2. Traceability chain

Every output field must trace to:

`frozen evidence → normalized analytical record → deterministic descriptor → audit output`

No output may trace to:

- outcome/value;
- post hoc row selection;
- analyst interpretation;
- a new domain assumption;
- a changed transformation identity.

## 3. Frozen inputs

### VisitAll

Input scope is the already closed `grid-5`, depth-2 scientific-evaluation evidence.

No rerun is permitted.

### PRISM

Input scope is the already persisted bounded A6 reconstruction for `leader_sync3_2.pm`.

No A6 rerun is permitted.

## 4. Required implementation stages

The implementation shall contain four logically separated stages:

1. **LOAD** — read frozen evidence records without mutation.
2. **NORMALIZE** — map source-specific fields into `S_t, T_acc,t, T_real,t, S_(t+1), T_acc,t+1`.
3. **DERIVE** — mechanically compute `A,G,L,P,R,D`, FPE class and trajectory descriptors.
4. **AUDIT** — emit counts, missing-field conditions, provenance identifiers, and deterministic checksums.

No stage may use downstream outcome/value information.

## 5. Normalization constraints

Normalization may rename an existing source field into an analytical role, but may not:

- invent a transformation;
- merge distinct source identities;
- split one frozen identity into multiple identities;
- infer accessibility from the successor state;
- infer accessibility from outcome;
- infer a missing state from a later record.

Any unavailable required field must be reported as **NOT AVAILABLE**, not reconstructed by assumption.

## 6. Descriptor implementation

For records with both successive accessibility sets:

- `A_t = cardinality(T_acc,t)`
- `A_t+1 = cardinality(T_acc,t+1)`
- `G_t = cardinality(T_acc,t+1 - T_acc,t)`
- `L_t = cardinality(T_acc,t - T_acc,t+1)`
- `P_t = cardinality(T_acc,t ∩ T_acc,t+1)`
- `R_t = G_t + L_t`
- `D_t = A_t+1 - A_t`

The implementation must assert:

`A_t+1 = P_t + G_t`

`A_t = P_t + L_t`

and therefore:

`D_t = G_t - L_t`

These are internal consistency checks, not scientific hypotheses.

## 7. FPE implementation

FPE classification is derived only from `G,L,D,P`.

Permitted labels:

- EXPANSION
- CONTRACTION
- TURNOVER
- PERSISTENCE
- STABILITY
- combinations where criteria overlap.

The implementation must preserve the underlying numeric descriptors so labels cannot conceal ambiguity.

## 8. Trajectory implementation

Trajectory descriptors must be generated from the frozen ordered transition records.

A trajectory divergence is only testable where the frozen evidence contains multiple realizations from a common source state and sufficient subsequent records.

If those conditions are absent, output **NOT TESTABLE**.

The implementation must never manufacture paired trajectories by matching unrelated records.

## 9. Cross-domain comparison rule

Cross-domain comparison operates on descriptor structures and analytical-role presence.

It must not:

- compute set intersections between VisitAll and PRISM transformation identities;
- assign semantic equivalence to raw labels;
- pool raw `|T_acc|` into a capability score;
- rank domains.

Within-domain set operations remain domain-local.

## 10. Negative-control enforcement

The implementation must preserve the known VisitAll negative representational result.

It must additionally verify:

- no outcome/VSL field is read by the derivation functions;
- no row is selected according to its resulting descriptor;
- all records inside the frozen scope are processed;
- missing/invalid records are surfaced rather than silently dropped.

## 11. Determinism

Given identical frozen inputs and implementation version, the analysis output must be byte-stable or accompanied by a deterministic canonical serialization and SHA-256 digest.

The implementation must record:

- input artifact identifiers/hashes where available;
- implementation file hash;
- protocol identifier;
- output hash;
- record counts;
- excluded records and explicit reasons.

## 12. Independent implementation requirement

Because this is a secondary analysis rather than a new executor reconstruction, a second scientific executor is not required.

However, before scientific execution, the implementation must pass a mechanical audit against hand-checkable fixture cases covering:

1. unchanged accessibility;
2. pure addition;
3. pure loss;
4. simultaneous addition/loss;
5. trajectory with insufficient continuation;
6. duplicate identity;
7. missing required field.

Expected outputs for these unit cases must be frozen before analysis.

## 13. Scientific-result firewall

The implementation must not contain:

- thresholds chosen after seeing data;
- outcome-dependent branches;
- value-dependent classifications;
- TI labels used as inputs;
- utility judgments embedded in code;
- domain-specific semantic substitutions not present in the frozen protocol.

The runner may calculate descriptors. It may not decide what they mean scientifically.

## 14. Audit decision

| Criterion | Status |
|---|---|
| Frozen protocol traceability | PASS |
| Frozen domain scope | PASS |
| No new execution | PASS |
| Deterministic derivation specified | PASS |
| Cross-domain identity separation | PASS |
| Outcome/value firewall | PASS |
| Selection-bias control | PASS |
| Missing-data handling | PASS |
| Determinism/hash requirements | PASS |
| Unit-test cases specified | PASS |
| Actual implementation file audited | **NOT YET** |
| Scientific execution authorized | **NO** |

### Determination

**PASS WITH BOUNDARY — IMPLEMENTATION SPECIFICATION AUDITED.**

The implementation requirements are sufficiently constrained to proceed to construction, but the actual runner has not yet been audited because it does not yet exist.

## 15. Next gate

**DETERMINISTIC ANALYSIS RUNNER CONSTRUCTION + UNIT-TEST FREEZE**

The next action is to build the runner and its hand-checkable unit tests from this audit. After construction, the actual implementation and test outputs must be audited before the frozen VisitAll/PRISM evidence is processed.

No scientific interpretation is authorized at the construction stage.
