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
| Static test execution | PENDING workflow result |
| Resource-only preflight | NOT RUN |
| Numerical comparative holdout | NOT RUN |
| Primary/replay numerical identity | NOT RUN |
| Tier B | OUT OF SCOPE |
| Scientific C10-S execution | NOT AUTHORIZED |

A successful static workflow will establish only technical conformance of the runner contracts. It will not establish numerical coverage or authorize the holdout.

## 5. Next operation

1. Inspect the static workflow result for the exact commit containing these changes.
2. Resolve any runner/test defects without changing the frozen protocol or inference methods.
3. Perform a resource-only preflight without coverage adjudication.
4. Freeze the resulting code/workflow identities and prepare the one-use numerical holdout authorization.
5. Execute the eight-cell independent C0/C1/C5 holdout only after explicit authorization.

No changes to `main`; no C10 scientific execution.
