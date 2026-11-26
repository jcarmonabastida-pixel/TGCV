# C10-S — F1 raw-between profile-likelihood reconciliation 002

**Date:** 2026-11-26  
**Status:** STATIC RECONCILIATION COMPLETE / CANDIDATE NOT CALIBRATED / NOT READY FOR TIER-A  
**Branch:** `research/c10s-instrumental-autonomous-workpackage-20261126`  
**Branch head reviewed:** `3be47b6f86e5a625b23fda7e878651cc08731cdc`  
**Source:** `harness/c10s_f1_between_profile_likelihood.py`, blob `eded4e1de5ab3a4a346b7a4ec2834be60d5257d4`  
**Tests:** `harness/test_c10s_f1_between_profile_likelihood.py`, blob `225dcaeddf1c2d5997c235ca3fe31f7fc62458dc`  
**Static test run:** GitHub Actions `45816013597`, exact tested commit `3be47b6f86e5a625b23fda7e878651cc08731cdc`, SUCCESS (211 tests across the C10-S comparator test suite).

## 1. Purpose and relationship to the earlier review

This note reconciles the 2026-11-19 static review `C10S_F1_PROFILE_LIKELIHOOD_STATIC_REVIEW_001.md` against the current source. The earlier review accurately described the code at that time, but findings F1-PL-01 through F1-PL-03 are no longer fully current: the interval path and API have since been strengthened. This note does not alter the frozen Tier-A protocol, choose an LR cutoff, or claim coverage.

## 2. Reconciliation of the prior findings

### F1-PL-01 — nuisance maximum and interval-path diagnostics

**Current disposition: IMPLEMENTATION GATE ADDED; NUMERICAL GLOBALITY REMAINS CONDITIONAL.**

At every evaluated between-variance value, `f1_profile_between_confidence_set()` now calls `f1_profile_nuisance_optimizer_diagnostic()` and `f1_score_polynomial_diagnostic()`. It fails closed unless:
- bounded-optimizer and stationary-root likelihood values are both finite;
- their absolute log-likelihood difference is at most the existing numerical tolerance (10^{-7});
- the score-polynomial diagnostic reports isolated roots and no unresolved critical/tangential candidates;
- the independent stationary solution is not search-boundary-sensitive and no optimizer error is present;
- at least one positive stationary root is found;
- exactly one local nuisance maximum is classified and no stationary-root type remains unresolved;
- the polynomial numerator and the independently evaluated likelihood score have matching signs at the probes bracketing each isolated root.

This closes the earlier omission in which the interval inversion could call the bounded optimizer without enforcing the nuisance diagnostics. It is a fail-closed numerical gate, not a formal proof that every floating-point operation is exact.

The finite log-score scan remains supplementary. A proposed hard veto on its aggregate `polynomial_scan_discordant` flag was tested and reverted: the constructed, resolved repeated-root fixture can produce a finite-scan discordance even though the polynomial root diagnostic, direct score-sign checks and bounded/stationary likelihood comparison resolve the tangency. Treating that flag as an unconditional veto would incorrectly reject a specifically tested admissible tangency. The current interval gate therefore relies on the polynomial stationary-root path and direct score checks, while retaining the scan as a diagnostic rather than silently promoting its finite grid to a root certificate.

### F1-PL-02 — connectedness of the outer likelihood-ratio set

**Current disposition: ANALYTIC ARGUMENT ADDED; VALID ONLY UNDER THE DECLARED F1 MODEL AND UNIQUE-NUISANCE-MAXIMUM GATE.**

The current function documents the envelope derivative for the balanced Gaussian random-intercept likelihood. Writing (s) for the within variance, (	au) for the between variance, and (q^*=	au+s^*/R) at the profiled nuisance maximum:

[
\frac{d\ell_p(\tau)}{d\tau}
=\frac{df_B}{2}\frac{S^2_{\bar Y}-q^*}{(q^*)^2}.
]

An interior stationary point of the outer profile requires (q^*=S^2_{\bar Y}). Substitution into the nuisance score equation gives (s^*=SSW/df_W=MSW), and hence the only possible stationary location is

[
\tau^*=S^2_{\bar Y}-MSW/R.
]

Thus there can be at most one interior stationary point on (	au>0). Together with the likelihood's decay at infinity and the per-(	au) unique nuisance-maximum gate, the LR acceptance set is connected for the declared nondegenerate F1 likelihood. The interval implementation can therefore bracket one lower and one upper endpoint rather than assuming connectedness without an argument.

This is an internal mathematical derivation embedded in the implementation. It is not an external proof review, and its assumptions must remain explicit: balanced Gaussian F1 likelihood, positive within residual information, finite sufficient statistics, and successful nuisance certification at every profile evaluation.

### F1-PL-03 — explicit family guard

**Current disposition: CLOSED AT THE CALLABLE INTERVAL API.**

The confidence-set API now requires `family="F1"` and rejects any other family label. It also requires a finite positive caller-supplied LR cutoff. The function remains F1-specific; it is not a generic F1–F5 interval routine.

### F1-PL-04 — boundary and numerical domain

**Current disposition: DETERMINISTICALLY TESTED IN THE CURRENT FIXTURE DOMAIN; BROADER CALIBRATION OPEN.**

The test suite includes:
- deterministic fixtures for all six frozen F1 design/regime combinations;
- a constructed repeated/tangential nuisance-score root;
- typed abstention for unresolved tangencies and unresolved polynomial critical points;
- scale and endpoint checks;
- invalid family/cutoff and bracketing/error paths.

The six-cell test checks that the implementation returns a valid interval or a typed abstention; it is not an empirical coverage test. Zero within residual sum of squares and other unsupported boundary cases remain explicit abstention territory.

### F1-PL-05 — LR cutoff calibration

**Current disposition: OPEN / BLOCKING FOR TIER-A.**

The LR cutoff remains caller-supplied. The familiar chi-square value used in unit fixtures is only a numerical inversion fixture, not an accepted calibration rule. No cutoff has been selected, calibrated, or evaluated on a fresh development bank. The exposed historical Tier-A data are not eligible for cutoff tuning.

## 3. Current F1 component disposition

| Component | Current method | Disposition |
|---|---|---|
| F1 within | Existing exact chi-square pivot | Retain unchanged; prior six-cell calibration evidence remains the basis |
| F1 raw-between | Profile-likelihood candidate with caller-supplied LR cutoff | Static implementation gate improved; cutoff calibration and fresh development comparison remain open |
| Conservative joint-pivot raw-between | Existing comparator | Retain as benchmark/guard; historical overcoverage remains a failure against the frozen upper bound |

The profile-likelihood candidate is not yet eligible for a prospective Tier-A freeze. Do not change the F1 within pivot to address the separate raw-between problem.

## 4. Verification evidence and limits

The read-only static workflow completed successfully on exact commit `3be47b6f86e5a625b23fda7e878651cc08731cdc`:
- dependency installation: PASS;
- Python compilation: PASS;
- 211 deterministic tests across the C10-S comparator suite: PASS;
- G7 resource-profile compatibility steps: SKIPPED on this autonomous branch because the historical immutable resource manifest/artifact pair belongs to a separate G7 resource-validation path and has a schema mismatch with the later validator. Those steps remain enabled on the original G7 research branch. No G7 resource manifest, artifact, result, authorization or scientific data was changed.

The tests establish code-path behaviour on deterministic fixtures. They do not establish profile-LR coverage, calibrated cutoffs, or readiness for Tier-A.

## 5. Decision

**F1 raw-between profile-likelihood candidate: RETAIN FOR BOUNDED DEVELOPMENT; NOT CALIBRATED; NOT READY FOR TIER-A.**

Next admissible work is a prospectively specified, bounded development calibration of the caller-supplied LR cutoff over the six frozen F1 cells, using a fresh development seed namespace and retaining the existing acceptance band/Wilson/emission gates. The calibration design must specify whether one common cutoff or design-cell-specific cutoffs are scientifically admissible before generating development outcomes. No historical exposed Tier-A data may be used for selection.

No source change to the profile candidate is required solely to satisfy the earlier F1-PL-01 to F1-PL-03 review findings. Further complexity, including integrating the exact Sturm root adjudicator into every LR evaluation, should be added only if a deterministic adversarial counterexample shows the current polynomial/score/optimizer gate is insufficient.

No coverage claim, Tier-A PASS, Tier-B readiness, C10 causal result, or `\Delta T_{acc}\rightarrow Value` claim is made.
