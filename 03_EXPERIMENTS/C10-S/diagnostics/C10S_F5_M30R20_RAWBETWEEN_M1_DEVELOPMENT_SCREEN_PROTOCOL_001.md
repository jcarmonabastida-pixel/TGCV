# C10-S — F5 M30/R20 raw-between M1 development screen protocol 001

**Status:** CANCELLED — NO STATISTICAL RESULT — DEVELOPMENT-ONLY SCREEN — NOT TIER-A / NOT CONFIRMATORY  
**Date:** 2026-11-27  
**Branch:** `research/c10s-coverage-first-focus-20261127`

## 1. Deficit and rationale

The only primary target in this screen is **F5 M30/R20 raw-between**. Frozen C5 evidence is 93.08% (calibration) and 93.00% (disjoint development validation), with Wilson intervals [92.34%,93.75%] and [92.26%,93.67%], despite 100% emission. G7 v1.1 is 93.353%, Wilson [91.631%,94.742%], emission 99.3%. All fail the frozen Wilson requirement.

C5's bootstrap holds the fitted beta-binomial concentration parameters fixed in each bootstrap replicate. The existing M1-PCT procedure refits the beta-binomial model in every replicate and therefore directly addresses the plausible omitted-parameter-uncertainty mechanism. In the previous M1 pilot, M30/R20 emitted 50/50 and raw-between descriptive coverage was 94% (K=50, B=100). This is only a screening signal, not evidence of calibration.

The historical high-fitted-concentration tail has severe C5 raw-between undercoverage (35.6% calibration; 35.0% validation in the post-fit top decile), with directional upper-end misses. The tail is exploratory, not a new acceptance stratum.

## 2. Frozen method contract

Reuse unchanged:
- method: `F5_M1_FUNCTIONAL_REFIT_PARAMETRIC_BOOTSTRAP_PCT_1.0`;
- fit contract: `F5_M1_ANALYTIC_LBFGSB_BEST_SUCCESSFUL_START_1.0`;
- parametric bootstrap refits beta-binomial parameters in every replicate;
- percentile interval, NumPy linear quantiles, 95% confidence;
- every original/refit state is retained;
- any non-admissible original fit or bootstrap refit abstains the complete dataset; no failed replicate is dropped and no complete-case bootstrap is formed;
- no exact global-MLE certificate is invoked.

No fit-state, boundary, Hessian, or abstention rule is relaxed. The runner computes both W and B because they share the fit procedure, but raw-between is the only primary development target. Within is descriptive and cannot be used to select the method.

## 3. Bounded fresh-seed screen

- One cell only: F5 beta22 M30/R20.
- K=400 fresh datasets; B=100 refits per dataset.
- Dataset indices 50–449 under a new schedule and seed namespace; the seed audit also includes all seeds from the previous M1 pilot and the historical C0/C5/B2/B3/G7 schedules.
- No overlap with historical datasets or bootstrap streams.
- One workflow, one artifact, no parallel duplicate.
- The previous pilot-based estimate (approximately 84 minutes for K=400/B=100) proved operationally unreliable. Run `45976887796` was cancelled by the user after exceeding the agreed 30-minute development-run budget.
- The run completed setup, dependency installation and compilation; its primary calculation step was cancelled. No statistical result or usable coverage estimate was produced.
- No B escalation or additional numerical certification.

## 4. Reported outcomes

Primary:
- emission rate and all abstention classes;
- raw-between conditional coverage among emitted datasets;
- two-sided 95% Wilson interval for that coverage;
- directional lower/upper misses and interval width, retained per dataset in the artifact.

Secondary:
- Within coverage/emission descriptive only;
- exploratory post-fit top-decile concentration raw-between coverage and miss direction; not an acceptance stratum and not used for selection.

A promising screen requires raw-between point coverage within [93%,97%], Wilson interval containing 95%, and emission >=95%, with no unresolved numerical state. Because this is a development screen and K=400, a PASS-like result is **not Tier-A validation**; it only justifies designing a disjoint prospective validation. A failure ends this M1 route for this component unless a specific coverage result identifies a correctable cause without weakening the contract.

## 5. Runtime policy, stop rules and governance

- **For every future development run, hard timeout is 30 minutes.** Do not raise it to accommodate an oversized batch. Use a smaller diagnostic stage with explicit progress/checkpoints, then decide whether any further stage is justified.
- A small diagnostic sample cannot establish Tier-A coverage; label it only as a screen for gross failure modes and emission/fit-state behaviour. Any subsequent larger sample requires a separate MCSE/power justification and must still fit the 30-minute budget.

- No changes to estimand, DGP, frozen thresholds, interval construction, fit contract, or abstention semantics.
- No reuse of exposed historical data for tuning.
- No within component method selection.
- No Tier-A confirmatory, Tier-B, or C10 causal execution.
- No further Sturm, topology, global-certification, or generic interval work.
- Current run `45976887796` retains its original 165-minute workflow timeout as a one-off legacy exception; no automatic rerun, extension or duplicate. All future workflows must use `timeout-minutes: 30`.


## 6.1 Cancellation record — 2026-11-27

GitHub Actions job audit confirms run `45976887796` concluded `cancelled`. The calculation step was cancelled and artifact upload was skipped. This is an operational cancellation only, not a statistical failure or result. No replacement run has been launched.

## 7. Next operation and authorization boundary

The proposed next development screen remains K=30/B=25, one cell (F5 M30/R20 raw-between), one method (existing M1-PCT), with a hard 30-minute timeout, per-dataset checkpoints, and no changes to fit/refit or abstention semantics. However, the current canonical `main` bootstrap routes the next operation to C10 methodological recovery/consolidation and declares design/recovery only, with no execution authorization. Therefore this protocol is not dispatchable until that recovery is complete and the applicable authorization is confirmed. No run may be launched merely because this research-branch protocol proposes it.
