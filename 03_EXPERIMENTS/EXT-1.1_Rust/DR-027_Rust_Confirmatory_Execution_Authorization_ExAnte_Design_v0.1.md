# DR-027 — EXT-1.1 Rust Confirmatory Execution Authorization v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Date:** 2026-09-07  
**Scope:** Sole authorization gate for confirmatory execution of EXT-1.1 Rust  
**Depends on:** DR-023, DR-024, DR-025A, DR-026A, DR-026C, DR-026D

## Governing question

Are all scientific and computational conditions required to execute the frozen EXT-1.1 confirmatory comparison simultaneously satisfied, so that execution can begin without introducing a methodological choice after outcome information becomes available?

## 1. Authorization boundary

DR-027 is an execution gate, not a new scientific model-selection or hypothesis-selection decision.

Acceptance of DR-027 authorizes one confirmatory execution of the already frozen protocol. It does not authorize changes to outcome, horizon, population, baseline, T_acc representation, resolver semantics, preprocessing, temporal split, learner, seed, metric, or exclusions.

Any methodological change requires a new ex-ante decision and a new execution gate.

## 2. Normative inputs

The confirmatory run must use the accepted decisions:

- DR-023 — outcome `Y_180` and 180-day horizon;
- DR-024 — deterministic eligible population and census-first principle;
- DR-025A — baseline representation `B_num`;
- DR-026A — relational T_acc representation `(A_rel, A_count)`;
- DR-026C — primary learner, feature construction, split, preprocessing and metrics;
- DR-026D — deterministic runtime and dataset identity.

No proposal-stage alternative may enter the confirmatory run.

## 3. Dataset gate

Before scientific data construction begins, execution must:

1. locate the frozen Rust dataset;
2. compute its SHA-256;
3. require exact equality with:
   `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`;
4. fail closed on mismatch;
5. record dataset path, size and digest in the execution manifest.

No outcome or predictor construction may occur before this identity check passes.

## 4. Runtime gate

Execution must verify exact agreement with DR-026D:

- Python 3.14.7, CPython;
- Windows 11 10.0.26200-SP0;
- AMD64;
- scikit-learn 1.9.0;
- NumPy 2.5.2;
- SciPy 1.18.1;
- `random_state=0`.

A runtime mismatch is a hard failure. No package substitution or automatic environment modification is permitted.

## 5. Repository/code gate

The execution must begin from a clean Git checkout corresponding to the frozen execution commit identified in the manifest.

The manifest must identify every code artifact that participates in confirmatory execution, including normative resolver code and the confirmatory execution script.

Dirty or untracked implementation changes are a hard failure unless they are explicitly excluded as non-participating local artifacts by the repository execution policy and do not alter scientific code or evidence.

## 6. Protocol reconstruction gate

The execution implementation must reconstruct, in order:

1. the eligible origin population from DR-024;
2. `Y_180` only for eligible origins with complete follow-up;
3. `B_num` according to DR-025A;
4. `T_acc^(R*)` according to DR-020/DR-021/DR-022 and represent it according to DR-026A;
5. the exact DR-026C feature transformation;
6. the exact frozen temporal partition;
7. the exact frozen logistic-regression configuration;
8. test predictions and primary/secondary metrics.

The implementation must not introduce an alternate resolver, alternate outcome definition, adaptive feature selection, or post-origin predictor.

## 7. Symmetric comparison gate

B and T_acc must be evaluated on the same eligible origins, with:

- identical outcome labels;
- identical 180-day horizon;
- identical train/test partition;
- identical learner;
- identical regularization;
- identical preprocessing rules where applicable;
- identical primary metric;
- identical treatment of unrepresentable observations.

The comparison must remain paired at the test-origin level.

## 8. Primary estimand

The primary descriptive comparison is:

`ΔLogLoss = LogLoss(B) − LogLoss(T_acc)`

where positive values favor `T_acc`.

The primary reported metric is mean test log loss for each representation and their difference.

Secondary Brier score and ROC AUC may be reported only under the conditions already frozen in DR-026C. No new secondary metric may be introduced after execution begins.

## 9. No inferential adaptation

DR-026C did not freeze package-aware uncertainty estimation, confidence intervals or p-values. Therefore DR-027 does not authorize inferential claims beyond the frozen descriptive predictive estimand.

Any inferential procedure requires a separate ex-ante decision before it is computed.

## 10. Execution protocol

The confirmatory runner must emit an immutable execution manifest containing at least:

- execution timestamp;
- Git commit;
- runtime versions;
- dataset SHA-256;
- frozen decision identifiers;
- population counts;
- temporal boundary;
- feature-space/hash configuration;
- learner configuration;
- random seed;
- primary metric definition;
- replay identifier.

The runner must fail closed if any frozen identity or protocol check fails.

The runner must not print or expose outcome-derived diagnostics before all protocol gates have passed.

## 11. Replay requirement

After the primary execution, a second execution under the identical frozen environment, dataset and code must be performed as the reproducibility replay.

Required exact equality:

- population counts;
- eligibility classification;
- temporal split membership;
- T_acc structural counts/hashes;
- feature-space construction identifiers;
- predictions where deterministic exact equality is expected;
- discrete/count/hash outputs.

Floating-point outputs must satisfy the numerical reproducibility tolerance specified by the execution implementation.

The replay must not be used to select the more favorable result. If primary and replay disagree beyond the allowed tolerance, the confirmatory result is invalid pending investigation under a new gate.

## 12. Hard-stop conditions

Execution must stop and be marked invalid if any of the following occurs:

- dataset SHA mismatch;
- runtime mismatch;
- dirty scientific working tree;
- missing or ambiguous normative code identity;
- mismatch with an accepted decision;
- future information enters predictors;
- outcome information enters predictor construction;
- T_acc is constructed using post-origin information;
- resolver semantics differ from DR-021;
- B uses T_acc/R*/outcome/post-origin information;
- temporal split differs from DR-026C;
- learner configuration differs from DR-026C/DR-026D;
- adaptive feature/model/metric/exclusion choice is made after outcome construction;
- replay fails required reproducibility checks.

A hard stop does not authorize repair-and-rerun under the same gate when the repair changes the frozen protocol or scientific implementation. Such a change requires a new ex-ante decision and gate.

## 13. Prohibited activities before or during authorization

DR-027 acceptance must not be based on:

- outcome prevalence;
- observed T_acc distributions used to alter representation;
- predictive performance;
- model coefficients;
- significance results;
- subgroup results;
- alternative horizons;
- alternative baselines;
- alternative seeds;
- exploratory model comparisons.

The authorization decision must be made solely from structural compliance with the already accepted protocol.

## 14. Required pre-authorization audit

Before DR-027 can be accepted, a dedicated structural audit must verify:

1. all prerequisite decisions are present and accepted;
2. the exact dataset digest matches DR-026D;
3. the exact runtime matches DR-026D;
4. the repository/code identity is frozen and clean;
5. the confirmatory runner contains no mutable protocol overrides;
6. all required protocol parameters match DR-023 through DR-026D;
7. the runner can fail closed on identity/protocol mismatch;
8. no outcome labels are constructed by the audit;
9. no T_acc is constructed by the audit;
10. no model is fitted;
11. no predictions or performance metrics are computed;
12. no significance or inferential result is computed;
13. no result is inspected to determine authorization.

## 15. Acceptance boundary

Acceptance of DR-027 authorizes the confirmatory execution protocol exactly as frozen.

It does not authorize methodological modification, exploratory analysis, post-hoc optimization, inferential analysis not separately frozen, or replacement of the dataset/code/runtime.

## 16. Falsification

DR-027 must remain unaccepted if any required prerequisite is missing, inconsistent, mutable, or not operationally verifiable.

The experiment must be considered unsupported if the confirmatory runner cannot demonstrate that the observed comparison arose from the frozen protocol without post-outcome methodological choice.

**No confirmatory execution is authorized by this proposal.**
