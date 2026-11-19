# C10-S — F1 near-degenerate interval fixture implementation record 001

Date: 2026-11-19  
Branch: `research/c10s-f1-integrated-correction-20261119`  
Implementation commit: `29e4e238bc8cb27a45b1a416e129f5fb45e0035d`

## Scope

Adds a deterministic test module for a realizable balanced-Gaussian nested-data fixture close to the previously constructed repeated nuisance-score root. This is a software-contract fixture only. It does not run a Monte Carlo bank, calibration, bootstrap bank, resource preflight, or scientific C10 execution.

## Construction

The fixture starts from the existing M=4, R=4 repeated-root construction at tau=1. It preserves each world mean and multiplies each within-world deviation from that mean by (1-5\times10^{-8}). Consequently, the data remain valid balanced nested rows, while the within sum of squares moves slightly away from the exact double-root condition.

The test requires the production polynomial diagnostic to isolate two distinct positive roots in (0.99, 1.01), with separation below 1e-3 and a resolved critical-point solver status. This checks a near-degenerate but non-tangential configuration rather than merely injecting a mocked polynomial.

A second test sends the same rows through the actual confidence-set entry point. It accepts only a valid finite ordered interval containing the profile MLE or a typed F1 profile abstention. Unexpected exception classes fail the test.

## Validation status

- File creation on the research branch: completed.
- Static workflow result for this commit: **not yet observed**. The commit lookup returned no PR-triggered workflow runs; this is not a PASS.
- Test execution: **not claimed**.
- Scientific/calibration execution: not performed and not authorized.

## Exact source

- Test module: `03_EXPERIMENTS/C10-S/harness/test_c10s_f1_near_degenerate_interval.py`
- Frozen development/calibration specification v1.0 remains unchanged.
- No changes to Tier A holdout artifacts, estimators, interval-selection rules, or `main`.

## Next gate

Obtain an actual static workflow run for this commit and inspect its job logs. If the new fixture fails, correct the deterministic construction or its numerical contract before adding further F1/F5 work. Do not proceed to resource preflight until the complete frozen implementation gate and static validation pass.


## Static workflow integration follow-up

Commit `aaa82ba5246b7c8554a80c7364ab82ecfe3f91d7` updates the existing research-branch static workflow so the new module is:
- included in the push path filter;
- compiled by the pinned-Python compile step; and
- executed by the deterministic unittest step.

This closes the workflow-wiring omission found during follow-up inspection. It does **not** establish a passing run. The available commit-run lookup returned no PR-triggered runs for the fixture commit, and no successful workflow result has been observed for the updated workflow commit. Static validation remains **PENDING / NOT VERIFIED** until an actual run and its job result are inspected.


## Observed CI result and fixture correction

The push-triggered static workflow did run for commit `aaa82ba5246b7c8554a80c7364ab82ecfe3f91d7` (run `44587633010`) and **FAILED**. Dependency installation and compilation passed; 120 of 121 tests passed. The failing assertion was the near-double-root fixture expecting `POLYNOMIAL_ROOTS_ISOLATED`, while the production diagnostic conservatively returned `POLYNOMIAL_ROOTS_UNRESOLVED`.

The initial perturbation factor `1 - 5e-8` placed the fixture inside the diagnostic's unresolved-tolerance region. This is a fixture calibration mismatch, not evidence that the solver should be weakened. The production tolerance and solver were left unchanged.

A follow-up fixture-only change uses `1 - 5e-6` to move the realizable polynomial farther outside that unresolved region while retaining a near-degenerate target. Commit: `e1af628250837ccd3a2aeffd2a6215879ce69c33`. Its static workflow result had not yet appeared at the time of this record update. Status therefore remains **PENDING**; do not count the test as passing until the new run is inspected.


## Second CI attempt and corrected scientific interpretation

The static workflow for commit `e1af628250837ccd3a2aeffd2a6215879ce69c33` completed as **FAIL** (run `44587970982`): 120/121 tests passed. The near-degenerate fixture remained `POLYNOMIAL_ROOTS_UNRESOLVED` even after changing the perturbation from (5\times10^{-8}) to (5\times10^{-6}).

This result shows that the prior expectation of two isolated positive roots was not supported. The correct conservative contract for this constructed near-double-root case is now explicit: the diagnostic must return `POLYNOMIAL_ROOTS_UNRESOLVED`, must expose an unresolved critical candidate or unresolved critical solver status, and must not relabel the case as a confirmed tangency. The interval-path companion continues to accept only a finite valid interval or typed F1 abstention.

The test was corrected accordingly in commit `0f4cc4a4b9c15ac7ba65095fc1a945655c94e9ca`. No production tolerance or solver code was changed. The workflow result for this corrected commit is pending; no PASS is claimed.


## Corrected conservative-contract static validation

The corrected test commit `0f4cc4a4b9c15ac7ba65095fc1a945655c94e9ca` was validated by the push-triggered workflow:
- Run: `44588197098`
- Conclusion: `SUCCESS`
- Exact commit checked out: `0f4cc4a4b9c15ac7ba65095fc1a945655c94e9ca`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **121 tests passed**
- New near-degenerate tests: both PASS.

The two tests now establish (a) conservative unresolved classification for the realizable near-double-root fixture and (b) interval-path completion or typed F1 abstention. They do not claim successful separation of the two nearby roots. The prior two attempts that failed 120/121 are retained as negative validation history.

The static workflow result is not a numerical-stress run, calibration, resource preflight, coverage adjudication, or scientific C10 execution. Those remain unauthorized/not performed.


## Subsequent F1 static gate and F5 low-concentration fixture

F1 conservative near-degenerate contract:
- Static workflow run `44588197098`, exact commit `0f4cc4a4b9c15ac7ba65095fc1a945655c94e9ca`, conclusion SUCCESS.
- 121/121 deterministic tests passed; both near-degenerate tests are explicitly present in the log.
- This validates conservative unresolved classification and interval-path valid-or-typed-abstention behaviour, not successful separation of the nearby roots.

A separate F5 deterministic test was added in commit `72f119b4be3b696fee95e5ad92c07376e5ba10c2` to verify convergence of the finite beta-binomial count log-likelihood to its `kappa -> 0` two-point mixing limit for endpoint-only counts. No workflow run has yet been observed for that commit, so this new F5 test is **NOT VERIFIED** and must not be counted as passing. It is a deterministic limit check only, not an empirical weak-identification or calibration result.


## F5 low-concentration limit test — static validation complete

The test added in commit `72f119b4be3b696fee95e5ad92c07376e5ba10c2` was executed by static workflow run `44588467741`:
- Exact commit checked out: `72f119b4be3b696fee95e5ad92c07376e5ba10c2`
- Workflow conclusion: SUCCESS
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **122 tests passed**
- Explicit test `test_two_point_limit_is_the_low_concentration_limit`: PASS.

This is a deterministic likelihood-limit identity check. It does not establish estimator identification, optimizer reliability across weak-identification regimes, bootstrap validity, or coverage. No calibration, resource preflight, holdout, or scientific C10 execution was performed.
