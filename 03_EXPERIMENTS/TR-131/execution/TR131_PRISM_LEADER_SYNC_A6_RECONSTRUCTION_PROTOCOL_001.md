# TR-131 — PRISM leader_sync — A6 Independent Reconstruction Protocol v0.1

**Document ID:** TR131_PRISM_LEADER_SYNC_A6_RECONSTRUCTION_PROTOCOL_001
**Status:** FROZEN RECONSTRUCTION PROTOCOL — SCIENTIFIC EXECUTION NOT YET AUTHORIZED
**Date:** 2026-09-23
**Repository:** jcarmonabastida-pixel/TGCV

## 1. Purpose

This package freezes the independent-reconstruction protocol for Gate A, criterion A6, using the PRISM Benchmark Suite `leader_sync3_2.pm` as the second-domain fixture.

A6 asks whether two independent executors can reconstruct the same operational transformation-space structure from identical frozen inputs without using one another's outputs or prior scientific interpretation.

This protocol does not evaluate Transformational Intelligence, usefulness, outcomes, value, causal `ΔT_acc → ΔValue`, or ontology.

## 2. Frozen domain fixture

Primary fixture:

- Repository: `prismmodelchecker/prism-benchmarks`
- Ref: `59ee49c031dbdfdb1e606edcdd643410de32192b`
- Path: `models/dtmcs/leader_sync/leader_sync3_2.pm`
- GitHub blob SHA: `bf96477357435e16a41c904bd91b63660246fd2f`

The fixture is a DTMC with `N=3` and `K=2`.

The PRISM model defines the global state from the local variables of all modules and guarded commands whose updates define transitions. Action labels impose synchronization between modules. These semantics are frozen as the source-defined execution semantics; no TGCV-specific interpretation may alter them.

## 3. Initial-state rule

The reconstruction shall obtain the initial state from the PRISM language semantics, not from comments, event traces, or scientific expectations.

For variables without an explicit initialization, the PRISM default initialization rule is used.

The expected initial valuation to be independently reconstructed is:

```
c = 1
s1=s2=s3 = 0
u1=u2=u3 = false
v1=v2=v3 = 0
p1=p2=p3 = 0
```

This valuation is an input-derived expectation to be verified independently by each executor, not a result to be assumed.

## 4. Frozen operational grammar

The common analytical grammar is:

`S_t → T_acc,t → T_real,t → S_(t+1) → T_acc,t+1`

### 4.1 State

`S_t` is the complete valuation of all model variables relevant to the PRISM global state.

### 4.2 Transformation identity

A transformation is identified by its PRISM action label at the global composed-model level:

- `pick`
- `read`
- `done`
- `retry`
- `loop`

The label, not an executor-invented semantic name, is the canonical transformation identity.

### 4.3 Accessibility

`T_acc(S)` is the set of globally enabled action-labelled transformations in state `S`, after applying PRISM guard evaluation and synchronization semantics.

Unlabelled local commands are not assigned a TGCV transformation identity in this protocol.

### 4.4 Realization

For a transformation whose command contains multiple probabilistic updates, a realization is the concrete global successor selected by one synchronized combination of enabled updates.

The protocol must preserve the distinction:

`T_real ⊆ realization`

conceptually as transformation identity versus concrete realized successor; it must not count probabilistic alternatives as distinct transformation identities.

### 4.5 Successor

`S_(t+1)` is the complete global valuation produced by the selected synchronized update combination.

### 4.6 Transformation-space evolution

`T_acc,t+1` is recomputed from the reconstructed successor state using the same frozen accessibility rule.

## 5. Frozen reconstruction scope

Both executors must reconstruct at minimum:

1. `S0`;
2. `T_acc(S0)`;
3. every global realization of `pick` from `S0`;
4. the corresponding `S1` states;
5. `T_acc(S1)` for every distinct `S1`;
6. every global realization of `read` from each required `S1`;
7. the corresponding `S2` states;
8. `T_acc(S2)`;
9. the enabled `done` or `retry` branch;
10. the corresponding successor state;
11. `T_acc(S3)` where reached.

The reconstruction terminates after the first stable terminal/self-loop state on the `done` branch and after the first return to the canonical `S0` on the `retry` branch.

No deeper exploration is required for A6.

## 6. Independence conditions

Executor-1 and Executor-2 must:

- receive the same frozen fixture and semantics;
- use independently written reconstruction logic;
- not inspect the other executor's output;
- not use previous manually reconstructed tables as execution input;
- not use downstream outcome properties;
- not alter transformation identity after seeing results;
- produce machine-comparable canonical output.

Scientific interpretation is prohibited during reconstruction.

## 7. Canonical output

Each executor shall emit a canonical representation containing:

- fixture identifier and blob SHA;
- initial state;
- ordered transformation identities;
- realization identifiers;
- source-state hash;
- successor-state hash;
- accessible-transformation set;
- transformation-space delta;
- reconstruction depth;
- executor identifier.

Ordering rules must be deterministic:

1. states ordered by canonical serialized state;
2. transformations lexicographically by action label;
3. realizations lexicographically by canonical update valuation;
4. sets represented in sorted order.

## 8. Comparison audit

The comparison audit shall compare Executor-1 and Executor-2 outputs on:

- fixture identity;
- initial state;
- transformation identities;
- realization cardinalities;
- successor states;
- state-to-transformation relations;
- transformation-to-successor relations;
- `T_acc` sets;
- `ΔT_acc` sets;
- terminal/self-loop classification.

Any discrepancy is a deviation and must be classified before any scientific evaluation.

### A6 decision

**PASS** only if deviations = 0.

**FAIL** if any material reconstruction discrepancy remains after checking implementation-independent serialization.

A tooling/implementation defect is not converted into a scientific PASS.

## 9. Source-semantics boundary

PRISM's official semantics are authoritative for:

- global-state construction;
- guard evaluation;
- command updates;
- action synchronization;
- probabilistic update semantics.

TGCV supplies only the analytical extraction layer:

`state → accessible transformation → realization → successor state → accessible transformation`.

This boundary is frozen to prevent semantic back-fitting.

## 10. Scientific exclusions

A6 does not establish:

- that `T_acc` is ontologically primitive;
- that transformation-space dynamics are causally related to value;
- Transformational Intelligence;
- practical usefulness;
- outcome superiority;
- value-guided navigation;
- representational superiority.

## 11. Authorization state

**FROZEN PROTOCOL.**

Scientific execution is not authorized until:

1. both executor implementations are independently prepared;
2. the fixture is verified against the frozen SHA;
3. executor inputs are frozen;
4. execution artifacts are persisted;
5. comparison is performed without cross-contamination.

## 12. Provenance

PRISM manual version referenced: 4.10.1.

Relevant official semantic statements are documented in the PRISM Manual sections covering modules, commands, model type, and synchronization.

This document is a protocol artifact only. It does not contain scientific execution results.
