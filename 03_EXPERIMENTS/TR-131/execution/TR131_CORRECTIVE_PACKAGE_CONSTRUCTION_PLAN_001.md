# TGCV TR-131 — CORRECTIVE PACKAGE CONSTRUCTION PLAN 001

**Status:** PASS — CORRECTIVE DESIGN FROZEN
**Scientific execution:** NOT AUTHORIZED

## Purpose

Resolve the inventory audit blockers without relabeling preflight code as scientific execution.

## Decisions

### 1. Separate artifact classes

The exact-source package SHALL distinguish:

- SOURCE_LOCK: immutable provenance and fixture declaration.
- PREFLIGHT: deterministic integrity/traceability tests only.
- ADAPTER_SPEC: normative description of source transition semantics.
- EXECUTION_ADAPTER: executable mechanism that invokes or faithfully reproduces the pinned source transition semantics with auditable provenance.
- SCIENTIFIC_RUNNER: orchestrates A/B realization using the execution adapters.
- AUDIT_RECORD: evidence produced by preflight/reconstruction/freeze gates.

A PREFLIGHT file SHALL NOT be promoted to EXECUTION_ADAPTER merely by renaming it.

### 2. Source-runtime requirement

For VisitAll, the execution adapter must consume the pinned PDDL domain/problem semantics and apply the selected grounded action without inventing effects.

For Rainbow, the execution adapter must invoke the pinned Rainbow/SWIM tactic semantics, or use a separately frozen executable representation whose provenance is demonstrably derived from the pinned source revision.

If the original runtime cannot be invoked reproducibly, the package must record that limitation and remain blocked rather than substituting a hand-written semantic approximation.

### 3. Runner requirement

The scientific runner must:

1. load the exact-source candidate;
2. verify package hashes before execution;
3. reconstruct S0, C and T_acc;
4. verify T_acc invariance between A/B;
5. declare X_A/X_B before transition application;
6. select only members of T_acc;
7. call the domain execution adapter;
8. record S_t, C_t, T_acc_t, X_t, T_real_t and S_t+1;
9. derive H exclusively from the realized trace;
10. emit deterministic evidence for Executor-2 reconstruction.

The runner must fail closed on any package/hash/provenance mismatch.

### 4. Source-lock metadata

The stale status in TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json must be corrected in a new source-lock version rather than mutating v01 in place.

The new lock must state that fixture preflight passed, while preserving the distinction between fixture validation and scientific execution authorization.

### 5. No premature execution

Until the execution adapters and scientific runner pass their own traceability preflight, no A/B scientific run is authorized.

## Next gate

**SOURCE-RUNTIME EXECUTION ADAPTER AVAILABILITY AUDIT**

Determine whether the pinned VisitAll and Rainbow source artifacts provide a reproducible executable transition path. If yes, freeze the adapters and runner. If not, record the exact missing runtime dependency and keep the package blocked.
