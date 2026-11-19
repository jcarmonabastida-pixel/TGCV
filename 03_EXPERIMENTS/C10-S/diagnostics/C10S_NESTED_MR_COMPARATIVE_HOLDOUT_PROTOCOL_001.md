# C10-S — Nested M/R comparative independent holdout protocol

**Record:** C10S-NESTED-MR-COMPARATIVE-HOLDOUT-PROTOCOL-001  
**Version:** 1.0  
**Status:** FROZEN RESEARCH PROTOCOL / COMPONENT INTERVAL COMPARISON ONLY / RUNNER INTEGRATION REQUIRED / NOT AUTHORIZED FOR EXECUTION  
**Date:** 2026-11-19  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Parent design:** `C10S_NESTED_MR_CALIBRATION_COMPARISON_DESIGN_001`  
**Comparator contract:** `C10S_NESTED_MR_COMPARATIVE_ENGINE_CONTRACT_001`  
**Historical baseline:** `C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001` v002; method `TGCV_NESTED_MR_BOOTSTRAP` 1.2  
**Historical Tier A:** Run `44449787220`, artifact `14495695421`; immutable development evidence, not holdout.

## 1. Purpose and scope

This protocol defines an independent, matched-data holdout comparison of the already implemented C0/C1/C5 interval procedures. It is a new comparative calibration study; it does not amend, repeat, overwrite or re-adjudicate protocol v002 or its original Tier A result.

The study asks whether the candidate interval procedures recover nominal 95% coverage for the two variance components under their declared fixture families:

- **F1:** balanced Gaussian random-intercept fixtures; C0 versus C1.
- **F5:** beta-binomial world-probability fixtures; C0 versus fitted C5.

The study is not C10 causal execution, not the C10 Generator/Analyzer/Evaluator, not Tier B, and not evidence of a TGCV causal or Value claim.

### Explicit target boundary

The confirmatory targets in this holdout are **within variance** and **untruncated raw between variance**.

- C0: frozen v002 two-stage nonparametric percentile bootstrap.
- C1: exact Gaussian within pivot and conservative Gaussian joint-pivot raw-between interval; F1 only.
- C5: fitted beta-binomial parametric percentile intervals for within and raw-between; F5 only.

**MCSE is diagnostic/non-confirmatory in v1.0.** The engine must retain and report MCSE point estimates, interval emission/abstention and profile diagnostics where requested, but:
- F5 C5 MCSE remains a typed abstention: `F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED`.
- No F5 MCSE coverage claim or method selection is permitted.
- F1 C1 MCSE projection may be recorded as exploratory diagnostic only; it is not a third confirmatory target.
- Do not condition MCSE scoring on positive raw-between draws or truncate raw estimates.

This exclusion is deliberate: the F5 boundary-aware MCSE profile method is specified separately but is not implemented or calibrated. v1.0 does not wait for it and does not imply it is solved.

## 2. Frozen cell roster and sample size

The holdout uses exactly the eight Tier A comparability-core cells, with the same population parameters and M/R designs but newly generated datasets:

| Cell | Family / parameters | M | R | K |
|---|---|---:|---:|---:|
| F1 balanced | Gaussian, within=1, between=1 | 10 | 5 | 1,000 |
| F1 balanced | Gaussian, within=1, between=1 | 30 | 20 | 1,000 |
| F1 high-between | Gaussian, within=0.25, between=2 | 10 | 5 | 1,000 |
| F1 high-between | Gaussian, within=0.25, between=2 | 30 | 20 | 1,000 |
| F1 low-between | Gaussian, within=1, between=0.05 | 10 | 5 | 1,000 |
| F1 low-between | Gaussian, within=1, between=0.05 | 30 | 20 | 1,000 |
| F5 beta22 | Beta(2,2), within=0.20, between=0.05 | 10 | 5 | 1,000 |
| F5 beta22 | Beta(2,2), within=0.20, between=0.05 | 30 | 20 | 1,000 |

Total: 8,000 independent datasets. No Tier B, F2, sparse/constant, additional stress or post-hoc cells are part of this holdout. They require a separately versioned design.

### K rationale

K=1,000 is retained from the v002 eight-cell comparability core, not selected after viewing holdout outcomes. At nominal coverage 0.95, the binomial Monte Carlo standard error is approximately 0.0069 and the expected 95% Wilson half-width is approximately 0.0135. This gives a prospective cell-level diagnostic capable of distinguishing gross deviations from the [0.93,0.97] acceptance band, while acknowledging that borderline cells may remain inconclusive. No pooling across cells is allowed.

K is fixed. It must not be increased, reduced or selectively extended after any holdout result is inspected.

## 3. Resampling counts and seed schedule

For every dataset:
- C0 uses B=1,000, preserving the frozen v002 resampling count and resampling law.
- F5 C5 uses B=1,000 fitted parametric bootstrap replicates.
- F1 C1 is analytic/pivotal and has no bootstrap B.
- F1/F5 profile/root diagnostics are disabled in the primary holdout pass; they are not required for the component interval targets and must not be run over all 8,000 datasets.

B=1,000 is fixed for v1.0 to retain direct comparability with C0 v002 and to avoid selecting B from holdout outcomes. The finite-B Monte Carlo error of C0/C5 interval endpoints is a declared limitation of v1.0: the primary adjudication reports the fixed-B intervals and does not claim endpoint-Monte-Carlo-error certification. A later B-sensitivity study, if needed, must use a separate development namespace and cannot modify this holdout after unblinding.

### Independent seed namespaces

The holdout must use a new seed-schedule version and namespace, distinct from:
- v002 Tier A/Tier B;
- all prior F1/F5 development and micro-simulation records;
- C0 baseline bootstrap streams;
- C5 parametric-bootstrap streams;
- any future profile-likelihood cutoff calibration.

Dataset generation is paired across methods: for a given dataset_id, C0 and its family-specific candidate receive the exact same immutable M×R observations and analytical truth. Method-specific bootstrap streams are independent of the dataset stream and of each other.

The runner must derive seeds deterministically from protocol version, namespace, cell_id and replicate index using a documented stable hash-to-unsigned-64 mapping. Dataset IDs must bind protocol, cell and replicate index. Duplicate IDs/seeds within a namespace are fatal. The exact seed-schedule identifier and hash implementation must be recorded in the run manifest before execution.

## 4. Candidate roster and matched adjudication

Per dataset, the exact expected roster is:

- F1: `C0_FROZEN_V002_NESTED_PERCENTILE_1.2` and `C1_F1_EXACT_PIVOTAL_1.0`.
- F5: `C0_FROZEN_V002_NESTED_PERCENTILE_1.2` and `F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0`.

C2, C3 and C4 remain explicitly unavailable. No fallback or surrogate method is permitted.

Use the existing `compare_dataset(..., include_profile_diagnostics=False)` API and `adjudicate_matched_datasets(...)` API. The same dataset_id, input design, target design, truth and immutable rows must be passed to all methods. Target design is fixed to the input cell's M/R pair in v1.0. Any change to target M*/R* requires a separate stratum and protocol amendment before execution.

Truth must come from the independent analytical fixture specification/oracle, not from candidate fits or candidate outputs. Preserve raw between estimates and interval endpoints, including negative values. Never clamp, truncate, filter, winsorize or condition on positive raw-between estimates.

## 5. Primary metrics and acceptance

For each cell × method × component (within, raw between), report:
- K completed datasets and point/interval emission rates;
- empirical conditional coverage among emitted intervals;
- unconditional cover rate over all K datasets (non-emission counts as not covered);
- 95% Wilson interval and coverage MCSE;
- lower-tail and upper-tail miss rates;
- point bias, RMSE and median absolute error;
- mean interval width;
- abstention/non-emission counts and typed reason frequencies;
- finite/non-finite and fit/convergence/boundary diagnostics;
- runtime and peak memory where available.

A component cell passes only when all are true:
1. empirical conditional coverage is within [0.93,0.97];
2. its two-sided 95% Wilson interval contains 0.95;
3. interval emission rate is at least 0.95;
4. all K datasets are accounted for exactly once and all expected method/truth pairings are present;
5. no invalid/non-finite interval is silently counted as emitted;
6. the raw-between target has not been truncated or filtered.

The unconditional cover rate is reported as a separate operational metric; it does not replace the stated conditional-coverage gate. The emission gate prevents a method from passing by abstaining selectively.

No averaging across cells, components or methods can rescue a failed cell. A family/method disposition is PASS only if every required component cell for that family/method passes. Otherwise report NOT_VALIDATED or INCONCLUSIVE according to whether a criterion failed or could not be evaluated. Do not select a winner solely by coverage: interval width, point error, emission, model scope and computation remain visible in the report.

## 6. F5 fitted-model safeguards

C5 must fit the beta-binomial model to each observed dataset using the implemented multi-start maximum-likelihood procedure. Oracle-known alpha/beta values may be used only to generate independent truth and diagnostics; they must never be passed into C5 fitting.

Record fitted alpha/beta, log-likelihood, optimizer/convergence status, boundary state, bootstrap seed and B. All-zero/all-one or boundary fits must retain the candidate's typed abstention; no fallback to oracle-known parameters, C0, or a Gaussian pivot.

C5 within/raw-between percentile intervals are exploratory fitted-model candidates under F5. Their holdout coverage is evaluated against the independent beta-binomial truth. A successful F5 result is bounded to the beta-binomial family and these two M/R designs.

## 7. Execution artifact, integrity and replay

The runner must emit:
- immutable protocol and code commit identities;
- authorization ID and manifest digest;
- branch/ref, workflow/run/attempt identifiers;
- Python, NumPy and dependency-lock identities;
- fixture-generator and seed-schedule versions;
- per-cell dataset and method counts;
- per-record dataset_id, truth, method IDs, estimates, intervals, diagnostics and seeds;
- per-cell/method/component summaries;
- source-file SHA-256 inventory;
- artifact SHA-256 inventory and a final run manifest.

The primary run must be followed by a clean-source replay under the same frozen code, inputs, protocol, authorization scope and deterministic seed schedule. Primary/replay record and summary hashes must match exactly. A replay mismatch is an integrity failure and blocks coverage adjudication.

Partial checkpoints may resume only when code commit, protocol hash, seed schedule, cell specification, K/B and record hashes all match. Otherwise discard the checkpoint and restart the affected cell under the same authorized run; never merge incompatible partial outputs.

## 8. Explicit exclusions and non-claims

This protocol does not:
- rerun or overwrite v002 Tier A;
- use v002 Tier A datasets as holdout;
- execute Tier B or any additional stress cells;
- implement or validate F5 MCSE intervals;
- calibrate profile-likelihood cutoffs or run Sturm/root diagnostics over the holdout;
- execute C10 Generator, Analyzer, Evaluator, causal DGP, calibration bank or scientific workflow;
- validate real-world M/R independence or the applicability of the nested sampling model;
- establish a general-purpose variance-component estimator;
- establish C10 causal contribution, ΔT_acc→Value, or any TGCV claim.

## 9. Implementation-readiness inspection and known blockers

The common comparator and its component methods already exist. The holdout must reuse them; it must not reimplement C0, C1, C5, the common result contract or adjudication.

The existing `run_c10s_nested_mr_validation.py` is **not reusable as the comparative holdout runner without substantive orchestration changes**. It:
- generates the legacy Tier A/Tier B records and calls the legacy single-method `analyze_fixture` path;
- does not dispatch `compare_dataset` or `adjudicate_matched_datasets`;
- uses the v002 seed schedule and K/B fixture specs;
- does not generate paired C0/C1/C5 records, candidate-specific seed streams or comparative summaries;
- has legacy authorization and manifest semantics.

Reusable parts:
- `generate_fixture` / `FixtureDataset` and analytical truth definitions, after a new holdout-specific seed schedule is introduced;
- the frozen C0 adapter inside the comparative engine;
- C1 and fitted C5 candidate functions;
- `compare_dataset` and `adjudicate_matched_datasets`;
- existing deterministic tests and dependency lock, subject to workflow path/branch correction.

A **thin comparative runner is required**, but it should be orchestration only: generate each dataset once, derive independent method seeds, call the existing engine with profile diagnostics disabled, construct `TruthTargets` from independent fixture truth, adjudicate by cell/family, and write the manifest/checksums/replay outputs. No inferential method or estimator redesign is authorized by this protocol.

### Readiness findings

- Comparator API: IMPLEMENTED; static contracts recorded as 39/39 in the existing engine contract.
- Matched adjudicator: IMPLEMENTED.
- Existing legacy runner: NOT REUSABLE AS-IS for comparative holdout.
- Comparative runner: NOT YET IMPLEMENTED.
- Static workflow: existing workflow path filter targets `research/c10s-nested-mr-calibration-design-20261119`, not this branch; its trigger/allowlist must be corrected in a separate implementation step before relying on CI on this branch.
- F5 MCSE: explicitly excluded; method design exists but is not implemented/calibrated.
- Resource benchmark: NOT YET RECORDED for 8,000 paired datasets with C0/C5 B=1,000. K/B are frozen as the scientific comparison design, but execution remains blocked until a non-scientific runtime/resource preflight demonstrates the runner fits the declared workflow budget. The preflight must not inspect coverage outcomes.
- No numerical calibration, holdout, Tier B or scientific C10 execution has been performed under this protocol.

## 10. Gate and authorization

Protocol v1.0 is frozen as a research design. Freezing it is not execution authorization.

Before numerical execution:
1. implement the thin comparative runner and correct the static workflow path filter;
2. add deterministic runner contract tests (seed separation, one generation per dataset, exact roster, truth pairing, complete denominators, resume integrity, checksums and replay identity);
3. run the static suite under a separately authorized technical-test operation;
4. perform a resource-only preflight with no coverage adjudication;
5. freeze the exact runner/code commit and workflow;
6. obtain a one-use numerical holdout authorization naming this protocol hash, code commit, workflow, K/B, cells, seed schedule, artifact destination, replay requirements and explicit exclusions.

This protocol grants no authorization. Tier B and scientific C10 execution remain separately unauthorized.

**Frozen decision:** execute the eight-cell independent comparative holdout only after the above gates; compare C0/C1 within F1 and C0/C5 within F5; score within and raw-between components; preserve explicit F5 MCSE abstention; never reuse v002 Tier A as holdout.
