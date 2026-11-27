# C10-S — Historical runtime evidence reconciliation for direct theta_A calibration

**Record:** C10S-THETA-A-HISTORICAL-RUNTIME-RECONCILIATION-001  
**Date:** 2026-11-27  
**Status:** STATIC HISTORICAL AUDIT — DIRECT theta_A RUNTIME NOT ESTABLISHED  
**Branch:** `research/c10s-m1-engine12-source-only-20261127`  
**Scope:** Recover existing runtime/resource evidence before proposing a direct theta_A development calibration schedule.  
**Execution:** No workflow, test, benchmark, simulation, seed generation, or scientific execution was initiated.

## 1. Finding

The historical GitHub Actions evidence does **not** currently establish the runtime cost of the direct theta_A calibration pipeline.

There is useful measured resource evidence for other C10-S workloads (F5/G7, P178 Analyzer Monte Carlo, static integrated contract tests). These workloads differ in estimator, data path, repetition structure and/or purpose. They may inform operational caution, but their runtimes must not be extrapolated to direct theta_A calibration.

The direct theta_A modules and protocol exist on the research branch, and the integrated harness workflow has included compile/contract-test coverage for them. The recovered workflow inventory does not contain a dedicated direct theta_A calibration execution workflow. No completed direct theta_A calibration run or measured per-replicate runtime was identified in the inspected records.

**Consequence:** no evidence-based N/M/R schedule, block size, or per-run duration can yet be specified. The <=3-hour user preference remains a hard planning constraint, not a demonstrated runtime capability.

## 2. Recovered runtime evidence — explicitly non-transferable

### 2.1 F5/G7 resource-only profile

Canonical manifest on main:
`03_EXPERIMENTS/C10-S/diagnostics/C10S_F5_G7_RESOURCE_PROFILE_MANIFEST_001.json`

- Profile run ID: `44926453920`
- Profile source commit: `469ecdd6f17639d10b9142158c527727e9add303`
- Scope: `RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_NO_COVERAGE_NO_HOLDOUT`
- Wall elapsed: 2,469.19 s (about 41.2 min)
- Process CPU: 2,636.46 s
- Peak RSS: 251,028 KiB
- F5 `M10/R5`: mean 0.444 s per dataset; p95 0.864 s; max 1.005 s.
- F5 `M30/R20`: mean 24.246 s per dataset; p95 36.014 s; p99 40.423 s; max 42.551 s.

These are measurements of the F5/G7 resource-only namespace and its own computational path. The manifest explicitly excludes coverage adjudication and holdout. They are **not** direct theta_A timings and cannot be used to calculate theta_A throughput.

### 2.2 F5/G7 execution examples

- Run `45453940984`, F5 deterministic certification (partitioned): 5 min 33 s elapsed, successful compile and deterministic test partitions. This is a software certification/test workflow, not a calibration.
- Run `45911630439`, F5 M30/R20 W stage profile: 16 min 24 s elapsed, successful F5 stage-profile job.
- Run `45911630605`, F5 M30/R20 robustness smoke: 18 min 27 s elapsed, successful F5 robustness fixture.
- Run `45976887796`, F5 M30/R20 raw-between M1 development screen: cancelled after 41 min 40 s. Its cancellation is not a statistical result or a completed runtime benchmark.

All four are F5-specific. Their runtimes cannot be attributed to direct theta_A.

### 2.3 P178 Analyzer Monte Carlo

- Run `43083651875`, P178 Analyzer Monte Carlo validation, was cancelled after 47 min 33 s.
- The workflow specification describes 27 cells × 10,000 replications and a clean replay, but the retrieved run record is cancelled. It is not a completed full calibration result and not a direct theta_A calibration.
- P178's N=700 reference artefact is a historical P178 input, not a scientifically justified N choice for the direct theta_A DGP.

No P178 runtime is transferred to the direct theta_A design.

## 3. Direct theta_A implementation/workflow inventory

The research branch contains the direct theta_A protocol, DGP factory, observation harness, Analyzer, independent Evaluator, nested M/R precision module and tests. The integrated synthetic contract workflow includes these modules in its source allowlist and compiles/tests the relevant contracts.

However:
- the integrated workflow's role is contract/test validation; it does not invoke a direct theta_A calibration over an N×M×R seed bank;
- the F5/G7, P178 and nested-comparator workflows target other workloads or static/numerical contract checks;
- the current direct theta_A runner iterates the supplied seed assignments sequentially;
- the current runner does not itself provide checkpoint/resume, sharding, concurrency, timeout enforcement or partial-result persistence;
- no dedicated direct theta_A calibration workflow or completed direct theta_A calibration run was identified in the inspected branch workflow inventory and Actions history.

Therefore the previous proposed 25-block schedule and 3-hour per-run claim have no verified implementation or runtime basis.

## 4. What can be reused now

Reuse is possible at the component level, not by importing F5 execution plans:

1. Direct theta_A Analyzer, Evaluator, DGP and calibration protocol already present on the research branch.
2. Existing sealed-evidence and truth-separation architecture.
3. Existing seed-bank planning/provenance and fail-closed aggregator contracts.
4. Existing integrated contract-test workflow as evidence of prior software-level validation, where the exact run/commit is recovered and its scope is respected.
5. Existing F5 resource measurements only as a warning that solver workload can change runtime sharply with configuration; not as a theta_A cost model.

No second Analyzer, new statistical engine, new DGP family, or duplicate seed system is justified by this audit.

## 5. Minimum missing evidence before a runtime proposal

The next operation should first recover the exact integrated contract-test run(s) and commit provenance for the direct theta_A modules. Then determine whether an already existing, authorized, bounded direct theta_A execution record contains any usable per-world or per-replicate timing. If not, record that no such timing exists.

Only after an explicit authorization for a technical-only resource preflight could a measured resource profile be considered. It must be isolated from scientific calibration, use a frozen small workload, and have a strict ceiling. This document does not authorize that preflight.

The runtime profile must measure at least:
- fixed-world construction cost;
- one complete R replicate, including assignment and S3 observation;
- Analyzer and Evaluator cost separately;
- aggregation/provenance overhead;
- peak memory and wall/CPU time;
- repeatability of timing across a small number of technical repetitions, without interpreting them as scientific replicates.

The measurement must use the exact direct theta_A code/dependency closure and a predeclared small technical fixture. It must not be used to tune scientific outcomes or to claim statistical performance.

## 6. Current disposition

**Direct theta_A runtime:** NOT MEASURED / NOT ESTABLISHED.  
**N grid:** NOT JUSTIFIED.  
**M/R values:** NOT JUSTIFIED.  
**Execution sharding/checkpoint plan:** NOT IMPLEMENTED / NOT VERIFIED.  
**<=3-hour constraint:** retained as a planning ceiling, not a proven feasible block size.  
**Scientific execution:** `false`.  
**Execution authorization:** `false`.

The correct next step is a historical provenance recovery of the integrated contract-test executions and any exact direct theta_A timing artefacts. If no such runtime evidence exists, the only honest conclusion is that a separately authorized technical-only resource preflight would be needed before any calibration schedule can be costed. No new runner or orchestration layer should be built at this stage.


## 7. Exact recovery of the prior integrated theta_A contract-suite execution

The historical run that had not been located in the earlier pass has now been recovered.

**Run:** [45044946102 — C10-S integrated synthetic contract suite](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45044946102)  
**Commit:** `78c2b17c6305f2a77c2f48695cae5a73f0f1de83`  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Result:** SUCCESS  
**Run wall duration:** 58 seconds (16:38:12Z–16:39:10Z)  
**Job:** explicitly authorized integrated synthetic contract suite; successful.

The workflow executed:
- pinned CPython 3.12.10 and hash-locked EP-02 dependencies;
- exact source materialization for primary and clean replay;
- compile of the integrated source/test allowlist;
- primary run of the exact 17 test modules;
- clean replay of the same 17 modules;
- runtime identity and materialization manifest capture.

The test module allowlist explicitly included:
- `test_theta_a_calibration_protocol`
- `test_theta_a_interval_observation`
- `test_theta_a_observation_harness`
- `test_theta_a_analyzer`
- `test_theta_a_evaluator`
- `test_c10s_world_pipeline_integration`

The primary suite completed **356 tests in 12.436 seconds**. The clean replay completed **356 tests in 12.408 seconds**. Both succeeded. The job also completed dependency installation, materialization, compilation, integrity checks and artifact upload. The two artifacts remain available:
- payload artifact ID `14762722989`;
- manifest artifact ID `14762538366`.

This is strong historical evidence that the integrated **contract/test suite** (including direct theta_A module tests) ran and replayed successfully in under one minute on that hosted runner and commit.

**It is not a direct theta_A calibration runtime measurement.** The workflow did not build and execute an N×M×R calibration seed bank, run repeated DGP worlds, or time a complete joint assignment + S3 observation + Analyzer + Evaluator replicate. The 12.4-second test-suite duration must not be divided into or extrapolated as per-replicate cost.

Two earlier trigger attempts on the same workflow failed before the successful run:
- `45044488530` — failure, 24 seconds;
- `45044609635` — failure, 43 seconds.
The subsequent successful run `45044946102` included the missing nested-precision source and passed primary plus replay. A later run `45045271710` was skipped after the one-shot trigger marker had been rotated; it is not an execution result.

### Revised evidence classification

- Direct theta_A module compile and integrated contract tests: **EXECUTED / PASS**, with exact primary/replay provenance.
- Direct theta_A N×M×R calibration: **NOT EXECUTED** in this recovered run.
- Direct theta_A per-replicate runtime: **NOT MEASURED**.
- Resource preflight for direct theta_A: **NOT EXECUTED**.
- No new execution is authorized by this historical recovery.

This closes the historical search for the prior integrated contract-suite execution. It does not remove the need for a separately authorized technical-only runtime preflight if a defensible N/M/R cost estimate is still required.


## 8. Static preflight-path recovery — 2026-11-27

The current research branch workflow inventory and direct theta_A source were inspected without dispatching a workflow, generating a seed bank, running tests, or invoking the DGP.

### 8.1 Existing workflow suitability

No existing workflow on `research/c10s-m1-engine12-source-only-20261127` is a reusable direct-theta_A single-replicate resource preflight:

- `c10-s-focal-harness-tests.yml` is the historical integrated contract-test suite. Its manual-dispatch branch guard does not include this current research branch, and its job runs the contract suite/replay rather than one complete calibration replicate.
- `c10-s-analyzer-monte-carlo.yml`, `c10-s-analyzer-mc-replay.yml`, `c10-s-analyzer-mc-performance-diagnostic.yml` and `c10-s-analyzer-t-cache-probe.yml` are P178/legacy Analyzer workloads, tied to other branch/source identities. They do not execute the direct theta_A DGP and must not be repurposed as its runtime proxy.
- `c10-s-f1-profile-static-tests.yml` tests the separate F1 profile-likelihood component and is not a direct theta_A pipeline runner.
- The remaining listed C10-S workflows target F5/G7, nested-M/R comparator, V_cont package, or other distinct workloads. Their resource measurements are not transferable to direct theta_A.

### 8.2 Existing direct pipeline entrypoints

The source already provides the necessary components; no second engine is justified:

- `build_theta_a_candidate_scenario_roster()` declares the five candidate scenarios.
- `build_theta_a_seed_bank()` creates the declared N×M×R seed assignments but does not invoke a Generator or DGP.
- `ThetaACalibrationDGPFactory.execute_calibration_scenario()` builds the scenario fixture and calls the complete-world pipeline.
- `run_theta_a_calibration_replicates()` orchestrates supplied assignments through a caller-provided world-executor callback and requires `execution_authorized=True`; it captures the actual Analyzer/Evaluator outputs.
- The DGP path reaches `materialize_c10s_complete_world_from_dgp()`, including assignment, S3 observation, sealing, Analyzer and Evaluator.

The orchestrator is a reusable library function, not a standalone CLI or a ready-to-dispatch GitHub Actions workflow. No existing workflow currently binds the callback to a bounded one-replicate technical invocation and captures stage-level resource measurements.

### 8.3 Disposition and minimum next action

**PREFLIGHT EXECUTION PATH: BLOCKED — NO REUSABLE WORKFLOW.** The historical contract-test workflow cannot be treated as a preflight because it does not time the required pipeline; P178/F5/nested-M/R workflows cannot be substituted because they execute different workloads or estimands.

A valid technical-only preflight would need a narrowly scoped execution wrapper that:

1. materializes exactly one explicitly identified technical seed assignment in a separate technical namespace;
2. executes one complete direct theta_A replicate using the existing DGP factory and orchestrator callback (no new Analyzer, DGP, or statistical engine);
3. records wall time, CPU time and peak memory for world construction, assignment/S3 observation, Analyzer, Evaluator and capture/aggregation overhead where separable;
4. marks all outputs as technical diagnostics, not calibration/evaluation-bank records or scientific evidence; and
5. has a hard runtime ceiling and no automatic retry or subsequent dispatch.

The current branch has no workflow implementing those steps. Creating or modifying a workflow would be a new executable path and is not authorized by the present design/recovery scope. Therefore no code or workflow was changed and no execution is proposed for immediate dispatch. Before seeking execution authorization, the smallest design decision is whether to authorize creation of this one-purpose technical wrapper, with its exact N/fixture, seed namespace, time ceiling and artifact outputs specified in advance.

No numerical N/M/R calibration choice is made here. The default 32-unit fixture in the DGP factory is a software default, not an adopted scientific N. The earlier N=700/M=5/R=4/25-block/3-hour proposal remains withdrawn.

**Current state:** direct theta_A pipeline components IMPLEMENTED; historical integrated contract suite EXECUTED/PASS; direct single-replicate runtime NOT MEASURED; reusable preflight workflow NOT IMPLEMENTED; scientific execution `false`; execution authorization `false`.
