# C10-S — Comparative holdout runner implementation record

**Record:** C10S-NESTED-MR-COMPARATIVE-HOLDOUT-RUNNER-IMPLEMENTATION-001  
**Date:** 2026-11-19  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Frozen protocol:** `C10S-NESTED-MR-COMPARATIVE-HOLDOUT-PROTOCOL-001 v1.0`  
**Scope:** implementation and deterministic contract tests only  
**Numerical holdout authorization:** NOT GRANTED

## 1. Mission boundary

This work operationalizes the already frozen C0/C1/C5 comparative holdout. It does not redesign F1/F5 estimators, change C0 v002, reopen the causal DGP/Analyzer/Evaluator, or execute the numerical holdout. Its purpose is to let the existing comparator answer the limited methodological question needed before the next C10-S calibration step: whether the corrected within/raw-between interval procedures meet their prespecified coverage and emission criteria on fresh independent datasets.

This is instrumental readiness work in service of C10-S, not scientific evidence about ΔT_acc → Value.

## 2. Implemented artifacts

- `harness/run_c10s_nested_mr_comparative_holdout.py`
  - holdout-only SHA-256 seed schedule with independent dataset, C0 bootstrap and C5 bootstrap namespaces;
  - exact eight-cell roster validation, including normalization to the frozen protocol order;
  - one dataset generation per replicate, using independent PCG64 child streams;
  - paired C0/C1 for F1 and C0/C5 for F5 through the existing `compare_dataset` API;
  - profile diagnostics disabled in the primary pass;
  - independent analytical truth construction;
  - exact dataset/design/method-roster checks and complete denominator enforcement;
  - existing `adjudicate_matched_datasets` reused for within and raw-between only;
  - MCSE excluded from coverage scoring; F5 C5 MCSE abstention retained in raw comparison records;
  - deterministic result digest and primary/replay identity check;
  - deterministic JSON result/manifest writer;
  - CLI fails closed and does not launch a numerical run without a separate authorization wrapper.

- `harness/test_c10s_nested_mr_comparative_holdout.py`
  - deterministic seed namespace separation;
  - fixture generation repeatability and frozen shapes;
  - roster rejection;
  - one-generation/one-comparison contract;
  - C0/C5 seed separation and B forwarding;
  - exact eight-cell roster ordering and duplicate/missing-cell rejection;
  - replay digest identity and mismatch rejection;
  - fail-closed CLI contract.

- `.github/workflows/c10-s-nested-mr-calibration-comparator-static.yml`
  - path filter now includes the active research branch and runner/tests;
  - pinned Python and hash-locked dependencies retained;
  - compile and unittest steps include the new runner/test module.

## 3. Reuse and non-duplication

The runner delegates all inference to the existing engine:
- `compare_dataset`
- `adjudicate_matched_datasets`

It does not copy C0 bootstrap logic, implement C1/C5 estimators, or run profile/root diagnostics over the 8,000-dataset holdout. The legacy v002 runner remains unchanged and is not used as the comparative runner.

## 4. Current evidence status

| Item | State |
|---|---|
| Protocol v1.0 | FROZEN |
| Comparative engine | IMPLEMENTED (pre-existing) |
| Thin comparative runner | IMPLEMENTED |
| Deterministic runner contract tests | IMPLEMENTED |
| Static workflow wiring | IMPLEMENTED |
| Static test execution | PASS — GitHub Actions Run `44560788541`, conclusion `success` |
| Resource-only preflight | NOT RUN |
| Numerical comparative holdout | NOT RUN |
| Primary/replay numerical identity | NOT RUN |
| Tier B | OUT OF SCOPE |
| Scientific C10-S execution | NOT AUTHORIZED |

The static workflow completed successfully on code commit `a7abb8936b57806d4f4f25df07a8c0ca16fb3251` (Run `44560788541`). Compile, dependency installation and the full configured comparator/runner unittest step all reported `success`. This establishes technical test conformance only; it does not establish numerical coverage or authorize the holdout.


## 6. Resource-only preflight (static assessment)

**Disposition: RESOURCE_PREFLIGHT_CONDITIONAL — capacity is not yet demonstrated for the new runner. No numerical benchmark or coverage computation was run.**

### Frozen workload arithmetic

- 8 cells × 1,000 datasets = **8,000 datasets**.
- C0: 1,000 bootstrap replicates for each of 8,000 datasets = **8,000,000 C0 bootstrap replicates**.
- C5: 1,000 parametric bootstrap replicates for each of the 2,000 F5 datasets = **2,000,000 C5 bootstrap replicates**.
- Across the eight cells, the sum of M×R per one-per-cell dataset is 2,600. At K=1,000 and B=1,000 this corresponds to approximately **2.6 billion C0 resampled observation positions**.
- F5 C5 adds approximately **650 million simulated Bernoulli observation positions** (2,000,000 replicates × the F5 M×R total of 650).
- Combined order of work: approximately **3.25 billion observation positions**, excluding fitting, array allocation, interval quantiles, serialization and Python orchestration.

### Relevant observed execution reference

Historical Tier A v002 Run `44449787220` completed successfully in approximately **141 seconds** (03:12:24–03:14:45 UTC) on GitHub-hosted Ubuntu. Its eight-cell K=1,000 / B=1,000 execution provides a useful empirical reference for the C0-like two-stage bootstrap workload, but it is not a benchmark of this new runner and contains no C5 parametric-bootstrap workload. It therefore cannot establish the new runner's end-to-end runtime.

The static comparator workflow Run `44560788541` took approximately 34 seconds; this is only static-test duration and is not relevant evidence for numerical capacity.

### Memory, checkpoint and workflow findings

- The runner retains all 8,000 serialized comparison records in memory until the final result bundle is written. Raw M×R datasets are not retained; only their hashes are recorded. Peak memory has not been measured.
- The runner currently writes the final result bundle only after all cells complete. It does **not** implement protocol-required verified per-cell checkpoints/resume. A late interruption could therefore waste completed work.
- The existing six-hour numerical workflow is bound to the legacy v002 authorization schema and invokes `run_c10s_nested_mr_validation.py`; it cannot execute this comparative runner. The ten-minute static workflow is not an execution workflow.
- No dedicated authorization-gated workflow exists yet for this frozen comparative protocol.

### Decision

The existing historical run suggests the C0 portion is operationally tractable, but it is not sufficient to claim that the combined C0/C1/C5 holdout fits the execution budget. Resource readiness remains **NOT DEMONSTRATED** until a bounded, non-adjudicating performance/memory preflight of the new runner is performed under a separately scoped technical authorization, or the runner gains safe per-cell checkpointing and the resource estimate is validated on the target GitHub runner.

No coverage, interval success, method ranking or scientific C10 result was computed. No numerical holdout was launched.

## 7. Next operation

1. Static workflow result inspected and passed for the runner/test code commit.
2. Resolve resource readiness: add verified per-cell checkpoint/resume and a dedicated authorization-gated workflow, then run a bounded resource-only performance/memory preflight (no coverage adjudication).
3. Freeze the resulting code/workflow identities and prepare the one-use numerical holdout authorization.
4. Execute the eight-cell independent C0/C1/C5 holdout only after explicit authorization.

No changes to `main`; no C10 scientific execution.
