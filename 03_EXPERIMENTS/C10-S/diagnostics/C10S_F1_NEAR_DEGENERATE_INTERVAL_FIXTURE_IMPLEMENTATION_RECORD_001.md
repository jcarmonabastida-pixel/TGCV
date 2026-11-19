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
