# EXT-1.1 Rust — CHR-MICRO-3 Historical Reconstruction Gate v0.1

**Date:** 2026-09-05  
**Status:** OPEN — NOT EXECUTED  
**Scientific execution:** NOT PERFORMED

## 1. Purpose

Close the specific blocker identified by CHR-MICRO-3: establish whether historical Cargo dependency resolution can be reconstructed reproducibly enough to define the empirical observation required by EXT-1.1, without current-state leakage or outcome leakage.

This gate concerns **data acquisition/reconstruction only**. It does not consume the frozen N-R8-C2 corpus and does not execute EXT-1.1.

## 2. Existing decision boundary

The Cargo-native route is an explicitly separate acquisition route; it is not silently substituted for the original replication artifact. The original Figshare reference remains identified but its physical artifact is not currently recovered. The Cargo-native route is therefore valid only if its own provenance and freeze are independently established.

## 3. Required historical reconstruction

For each selected historical release, establish all of the following:

### R1 — Release identity

`package@version` is uniquely identified and its historical release date is independently evidenced.

### R2 — Historical registry state

A registry/index state corresponding to the observation cutoff can be reconstructed from historical evidence. Current metadata must not be silently substituted for the historical state.

### R3 — Dependency metadata

The dependency declarations applicable to the focal release and candidate packages are recoverable from the historical state.

### R4 — Candidate universe

For every dependency resolution used in the observational unit, the candidate versions available at the cutoff are explicitly enumerable or reconstructible.

### R5 — Deterministic resolution

Given the reconstructed candidate universe, resolver inputs, semver constraints and cutoff rules, the resolution procedure is deterministic and independently rerunnable.

### R6 — Version identifier bridge

Each package/version used in the reconstructed dependency state can be joined unambiguously to the corresponding crates.io `version_id` required for the historical download series.

### R7 — Download archive bridge

The official historical version-download archive can be joined to the reconstructed version identifiers without using future information.

### R8 — Temporal censoring

Observation windows, left/right censoring, yanks, publication timing and other temporal boundary conditions are explicitly represented. Later facts must not retroactively alter the historical candidate universe.

### R9 — No outcome leakage

Download counts/success metrics are never used to construct, select, repair or infer dependency accessibility or candidate availability.

### R10 — T_acc operationalisation

The resulting empirical definition of `T_acc(t)` is computable from state/dependency information independently of the outcome variable and is auditable at the observational-unit level.

## 4. Pass criteria

The gate can PASS only if R1–R10 are all demonstrated with reproducible evidence.

A partial demonstration is not a PASS. In particular, proving release identity alone does not prove historical dependency resolution.

## 5. Failure conditions

The gate remains BLOCKED if any of the following occurs:

- historical candidate universe cannot be established;
- current registry state is used as a proxy without an explicit justified reconstruction;
- resolver output cannot be reproduced from recorded inputs;
- `package@version → version_id` is ambiguous or unverified;
- download observations cannot be temporally aligned;
- outcome data influence accessibility construction;
- censoring rules cannot be audited;
- `T_acc(t)` cannot be computed without hidden assumptions.

## 6. Evidence package to produce

If the gate is pursued, the minimum evidence package is:

1. acquisition/reconstruction provenance record;
2. exact source identifiers and retrieval dates;
3. historical registry/index snapshots or equivalent reconstructible evidence;
4. version/dependency reconstruction tables;
5. resolver configuration and deterministic reconstruction script;
6. package/version → `version_id` bridge evidence;
7. historical download archive artifact and SHA-256;
8. temporal coverage/censoring audit;
9. leakage audit;
10. observational-unit mapping to `T_acc(t)`;
11. final gate report with R1–R10 verdicts.

## 7. Separation from frozen N-R8-C2 corpus

This gate MUST NOT:

- read the N-R8-C2 production corpus to guide reconstruction;
- generate or modify corpus pairs;
- use corpus membership as a criterion for selecting Rust observations;
- write to or overwrite the frozen corpus or its manifest.

The corpus remains the independent frozen scientific input prepared before empirical dataset consumption.

## 8. Current verdict

```text
R1 Release identity                 OPEN / prior evidence available
R2 Historical registry state        OPEN
R3 Dependency metadata              OPEN
R4 Candidate universe               OPEN
R5 Deterministic resolution         OPEN
R6 version_id bridge                OPEN
R7 Download archive bridge          OPEN
R8 Temporal censoring               OPEN
R9 No outcome leakage               OPEN / methodological rule fixed
R10 T_acc operationalisation        OPEN

CHR-MICRO-3 RECONSTRUCTION GATE     BLOCKED / NOT EXECUTED
EXT-1.1 SCIENTIFIC EXECUTION        NOT PERFORMED
```

## 9. Next action

Acquire/reconstruct the minimum historical registry evidence needed to test R2–R7, beginning with one deliberately selected confirmatory historical case. Do not use downstream outcome to choose the case or infer missing resolution information.
