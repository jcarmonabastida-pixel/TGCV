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



## 6. Checkpointing, resource preflight and execution gates

### 6.1 Verified per-cell checkpoint/resume

The comparative runner now supports whole-cell checkpointing:

- Each completed cell is written atomically to its own JSON file.
- The checkpoint index binds protocol ID/version/hash, exact code commit, source SHA-256 inventory, seed-schedule ID, full cell manifests and K/B.
- A resumed run verifies the checkpoint configuration, every cell-file SHA-256, dataset count, dataset-ID uniqueness, protocol identity and cell identity before reuse.
- Any configuration mismatch or altered/missing cell file fails closed.
- An interrupted cell is recomputed from replicate zero; incomplete records are never merged.
- The final aggregate retains only cell summaries and record-file references/hashes in memory. Full per-dataset records remain in the per-cell files, limiting aggregate memory growth.

The deterministic tests cover exact resume reuse, configuration mismatch rejection, tamper rejection and disk-backed record retention.

### 6.2 Resource-only preflight implementation

Added `harness/run_c10s_nested_mr_comparative_resource_preflight.py` and its contract tests.

The bounded resource sample is deliberately limited to the two largest M/R cells, one per family:

- F1 Gaussian: M=30, R=20, K=1,000, C0 B=1,000.
- F5 beta-binomial: M=30, R=20, K=1,000, C0 B=1,000, C5 B=1,000.

It uses a separate deterministic seed namespace, retains candidate comparison objects only to reproduce the per-cell memory profile, records elapsed time and process peak RSS, and captures Python/NumPy/platform/workflow/dependency-lock provenance. It does not call `adjudicate_matched_datasets`, compute coverage, inspect interval success or emit method rankings. It is a resource sample, not the holdout and not scientific evidence.

### 6.3 Dedicated authorization gates

Two separate one-use workflows and validators are now present:

- `c10-s-nested-mr-comparative-resource-preflight.yml`: resource-preflight-only authorization; explicitly prohibits comparative holdout and C10 scientific execution.
- `c10-s-nested-mr-comparative-holdout.yml`: full eight-cell holdout authorization; exact protocol/code/workflow/source hashes, K/B, roster, profile exclusion, Tier B exclusion and primary/replay requirements are checked.

Each validator requires an APPROVED authorization file on a dedicated authorization branch, whose sole commit must have the exact approved research-code commit as its only parent and may change only the authorization JSON. The full holdout validator also binds the executor and validator hashes. No APPROVED authorization file or authorization branch has been created in this work.

## 7. Latest technical validation

GitHub Actions Run `44563560279`, commit `be11c07eac8849bc307c99e9f0c819136d6cfa6b`, completed **SUCCESS**:

- pinned Python 3.12.10 and hash-locked dependency installation: PASS;
- compilation of runner, preflight, executor and validators: PASS;
- comparator and runner/preflight/authorization contract suite: **60 tests, PASS**.

This is static/contract validation only. It does not validate the actual resource profile or authorize numerical execution.

## 8. Resource-only preflight (static assessment)

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

## 9. Next operation

1. Static workflow result inspected and passed for the runner/test code commit.
2. Resolve resource readiness: add verified per-cell checkpoint/resume and a dedicated authorization-gated workflow, then run a bounded resource-only performance/memory preflight (no coverage adjudication).
3. Freeze the resulting code/workflow identities and prepare the one-use numerical holdout authorization.
4. Execute the eight-cell independent C0/C1/C5 holdout only after explicit authorization.

No changes to `main`; no C10 scientific execution.


## 10. Resource-preflight authorization attempt — activation failure (2026-11-19)

The user explicitly approved one resource-only preflight attempt. A one-use authorization was created on the dedicated branch
`research/c10s-nested-mr-resource-preflight-auth-C10S-RES-PREFLIGHT-20261119-001`.

- Approved code commit: `15e758f92ac6aca2777154c2e24b8af0fe09f46b`.
- Authorization commit: `96950fb40ee09d1f9383de8f8d9b3369b5dbf979`.
- Authorization ID: `C10S-RES-PREFLIGHT-20261119-001`.
- Authorized scope: resource-only; two representative Tier A cells, K=1,000 each; C0 B=1,000 and F5 C5 B=1,000; no coverage adjudication, no comparative holdout, no Tier B, no C10 scientific execution.
- Authorization window: 2026-11-19 16:19:06Z through 17:49:06Z.

GitHub Actions created workflow-run records:
- Resource-only workflow: run `44564734347`, conclusion `failure`.
- Comparative holdout workflow: run `44564731876`, conclusion `failure`.

Both records report zero jobs. No validator, dependency installation, runner or preflight step ran; no datasets were generated; no resource measurement or scientific/coverage result exists. The resource-only workflow activation therefore failed before execution. The simultaneous holdout workflow record is an unexpected trigger and must be corrected so a resource-only authorization cannot activate the holdout workflow.

The one-use authorization is treated as consumed/closed after this failed activation attempt and must not be reused or replayed. No retry was made. A corrected trigger/registration and a new, separately approved one-use authorization are required before another attempt.

This is an orchestration/activation failure, not a preflight resource failure, not a C0/C1/C5 coverage result, and not a scientific C10 result.


## 11. Workflow isolation correction and second activation attempt (2026-11-19)

After the first failed activation, both workflow jobs were given fail-closed job-level guards:
- resource preflight requires the dedicated `research/c10s-nested-mr-resource-preflight-auth-*` ref and the resource-only authorization commit message;
- comparative holdout requires the distinct `research/c10s-nested-mr-comparative-auth-*` ref and the holdout-specific authorization commit message.

The corrected workflow sources were committed on the research branch:
- resource workflow guard commit: `0e874b1f2a33344cac316919cc366b118aa4dc98`;
- holdout workflow guard commit: `b079e6e7f0ce035629fd82c0d9a9af6266ae1da7`.

A fresh one-use authorization was then created (the first authorization was not reused):
- authorization ID: `C10S-RES-PREFLIGHT-20261119-002`;
- authorization branch: `research/c10s-nested-mr-resource-preflight-auth-C10S-RES-PREFLIGHT-20261119-002`;
- exact approved code commit: `b079e6e7f0ce035629fd82c0d9a9af6266ae1da7`;
- authorization commit: `d6ebde52c2b365c74bb9b8b548804fb552fd1b13`;
- scope remains resource-only, two Tier A cells, K=1,000 per cell, C0 B=1,000, C5 B=1,000; no coverage adjudication, holdout, Tier B or C10 scientific execution.

GitHub again created a workflow run for the **comparative holdout** workflow on the resource-only authorization branch:
- run `44565473766`;
- branch `research/c10s-nested-mr-resource-preflight-auth-C10S-RES-PREFLIGHT-20261119-002`;
- conclusion `failure`;
- zero jobs; no runner steps executed.

No resource-preflight workflow run was created for this second authorization. No datasets, timings, memory measurements or coverage outputs were generated. The resource preflight has therefore still not executed.

Important repository-state finding: both specialized workflow files are absent from `main` (404 when read from main) and exist only on the research branch. The GitHub Actions registration/activation behavior cannot be made reliable by research-branch job guards alone in the current state. Do not attempt further authorization pushes or reuse authorization 002. To activate these governed workflows reliably, their registration/trigger definitions must first be handled through the repository's canonical workflow governance (which may require an explicitly authorized main-branch promotion or another approved activation route). No main-branch change is made here.

This is a workflow-registration/activation blocker, not a resource-profile result and not a scientific result.


## 11. Workflow activation repair and current resource-preflight attempt (2026-11-19)

### 11.1 Diagnosed workflow activation failure

The GitHub Actions run pages exposed the exact parser error: both workflows had invalid YAML at line 63. The unquoted plain scalar
`run: python -m pip install --require-hashes --only-binary=:all: -r requirements-vcont-integrated.lock`
contains the YAML-sensitive `: ` sequence in `--only-binary=:all:`. The command is now a single-quoted YAML scalar in both workflows (`run: 'python -m pip install ...'`), avoiding the colon-space parse ambiguity.

Additional fail-closed job conditions now require the exact resource-preflight authorization branch prefix and its dedicated commit-message marker. The holdout job independently requires its own distinct authorization branch prefix and holdout-specific commit-message marker. A resource-only authorization therefore cannot execute the holdout job, even if GitHub creates a holdout workflow record.

### 11.2 Authorization attempts and exact dispositions

| Authorization | Approved code commit | Result | Disposition |
|---|---|---|---|
| `C10S-RES-PREFLIGHT-20261119-001` | `15e758f92ac6aca2777154c2e24b8af0fe09f46b` | Both workflow files rejected by YAML parser; zero jobs | Closed; no code ran |
| `C10S-RES-PREFLIGHT-20261119-002` | `b079e6e7f0ce035629fd82c0d9a9af6266ae1da7` | Same line-63 YAML parser error | Closed; no code ran |
| `C10S-RES-PREFLIGHT-20261119-003` | `2ace9f861fc6be0d69908094a744b24db9da9c6a` | Authorization validator rejected incorrect protocol digest | Closed; no benchmark ran |
| `C10S-RES-PREFLIGHT-20261119-004` | `2ace9f861fc6be0d69908094a744b24db9da9c6a` | Hash validation passed; workflow-output JSON parse failed because validator wrote literal backslash-n | Closed; no benchmark ran |
| `C10S-RES-PREFLIGHT-20261119-005` | `ec2754659d7237839a487fd855f26c4d4b551782` | Authorization, exact checkout and dependencies PASS; 2,000-dataset resource sample completed; artifact uploaded | Completed SUCCESS; one-use authorization consumed |

Attempt 003's digest values were incorrectly generated during orchestration and were rejected by the validator; they are not evidence of a repository defect. Attempt 004 exposed a real serialization defect in the validator, now corrected to write a newline character.

### 11.3 Current authorized run

- Run: `44566299402`
- URL: https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44566299402
- Authorization ID: `C10S-RES-PREFLIGHT-20261119-005`
- Authorization commit: `6bad48308ab4e3d9f725d9bd04a1294a16620fb6`
- Approved code commit: `ec2754659d7237839a487fd855f26c4d4b551782`
- Job ID: `135708842538`

Authorization validation, exact approved-code checkout and hash-locked dependency installation passed. The resource-only sample and artifact upload both completed successfully. It processed only the two authorized representative Tier A cells, 1,000 datasets each, with C0 B=1,000 and F5 C5 B=1,000.

No coverage adjudication, comparative holdout, Tier B or C10 scientific execution was performed. Authorization 005 is one-use and consumed; do not rerun or reuse it.

## 12. Completed resource-only preflight — measured result (2026-11-19)

### 12.1 Execution identity and integrity

- GitHub Actions run: `44566299402` — **SUCCESS**.
- Run URL: https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44566299402
- Job: `135708842538` — `resource-preflight`, **SUCCESS**.
- Authorization: `C10S-RES-PREFLIGHT-20261119-005`; authorization commit `6bad48308ab4e3d9f725d9bd04a1294a16620fb6`.
- Exact approved code commit: `ec2754659d7237839a487fd855f26c4d4b551782`.
- Environment: Python 3.12.10, NumPy 2.3.5, Ubuntu 24.04 runner; dependency-lock SHA-256 `4bdd6993cd8add430dab560f2e6eabb73028b4693e7f73e73999ecda4b2a30a9`.
- Artifact ID: `14552421343`; name `c10s-comparative-resource-preflight-C10S-RES-PREFLIGHT-20261119-005-ec2754659d7237839a487fd855f26c4d4b551782`.
- Artifact ZIP SHA-256: `86ba2d356a7da5ae4ac57c7e0e938cba12969dec1690051e610dccef9d55ca93`.
- Extracted `resource_preflight.json` SHA-256: `ef4cd86f9b9a99e09f04c1d87bb810d0e0af5f9f18f16bf030f2f5b94e5c6ffd`.
- Raw result persisted in this branch as `03_EXPERIMENTS/C10-S/diagnostics/C10S_NESTED_MR_COMPARATIVE_RESOURCE_PREFLIGHT_RESULT_001.json`.

### 12.2 Measurements

| Representative cell | Datasets | C0 B | Candidate B | Elapsed | Seconds/dataset | Peak RSS |
|---|---:|---:|---:|---:|---:|---:|
| F1 balanced, M=30/R=20 | 1,000 | 1,000 | C1 analytic | 18.283 s | 0.01828 s | 122,372,096 B (116.7 MiB) |
| F5 beta(2,2), M=30/R=20 | 1,000 | 1,000 | C5 B=1,000 | 229.321 s | 0.22932 s | 124,776,448 B (119.0 MiB) |

Total: **2,000 datasets**, 247.604 seconds of measured sample runtime. Both cells retained 1,000 comparison records during their memory sample. The observed peak process RSS was approximately 119 MiB.

### 12.3 Scope and interpretation

- `coverage_adjudication = NOT_RUN` in both cells and the aggregate.
- `adjudicate_matched_datasets_called = false` in both cells.
- `scientific_holdout_executed = false`.
- No interval coverage, method ranking, calibration result or scientific C10 evidence was produced.

For capacity planning only: the protocol has six F1 cells and two F5 cells. Applying the largest-M/R sample rate conservatively to all cells gives an indicative primary-pass runtime of about 9.5 minutes; a full clean-source replay of similar cost would put the two-pass runtime near 19 minutes, before workflow overhead. This is a rough planning estimate, not a measured full-holdout runtime. The measured memory sample is about 119 MiB; full-run memory must still be observed.

### 12.4 Disposition

**Resource readiness: PASS for proceeding to the separately authorized 8-cell Tier A comparative holdout.** The F5 cell dominates runtime; observed memory is modest. No reason emerged from this preflight to expand the numerical instrumentation or reopen F1/F5 method design.

The next operation is to freeze the exact final holdout code/workflow identities and obtain a new, separate one-use authorization for the full 8,000-dataset C0/C1/C5 Tier A holdout and its clean-source replay. This preflight authorization does not authorize that execution.

