# TGCV — TR-181E Integrity Review v0.1

**Status:** INTEGRITY REVIEW — FREEZE BLOCKED
**Date:** 2026-08-28

## 1. Review objective

Determine whether the existing TR-181E protocol can be frozen and executed as the independent post-EMP-1.1 replication/stability operation without contaminating the historical confirmatory experiment.

## 2. Source protocols reviewed

- `TGCV-EMP-1.1_PROTOCOL.json` — frozen before confirmatory model fit.
- `TR-181E_PROTOCOL_v1.0.md` — draft, pending freeze.
- `TR-181E_NEXT.md` — prior operational planning note.

## 3. Verified invariants

The historical protocol fixes the core representation, hypothesis, primary metric, alpha, historical delta, sample sizes, seeds, learner family and controls. EMP-1.1 also explicitly prohibits retrospective alteration of Core, MVE, R, outcome, delta, dataset or model-selection rule.

TR-181E correctly preserves the following:

- EMP-1.1 remains sealed historical evidence;
- the Core is not re-optimised;
- the frozen `R` is reused rather than selected anew;
- new data are generated independently;
- evaluation remains out-of-sample;
- baseline and TGCV arms use matched procedures;
- cardinality and structural/null controls are retained;
- negative results remain valid results.

## 4. Integrity finding — threshold inconsistency

Two historical documents encode different roles for `delta = 0.04`.

`TGCV-EMP-1.1_PROTOCOL.json` freezes `delta = 0.04` as part of the historical confirmatory protocol.

`TR-181E_PROTOCOL_v1.0.md` retains `0.04` as the historical threshold but states that TR-181E should report the effect and planning information for a future external replication.

`TR-181E_NEXT.md`, however, states that the pilot should determine `delta`, `N*` and `alpha` before confirmatory execution.

Therefore `0.04` must be treated as a **historical EMP-1.1 parameter**, not automatically as a confirmatory decision threshold for TR-181E.

## 5. Freeze decision

**TR-181E must not be frozen yet.**

The protocol should first be amended so that its role is unambiguous:

> TR-181E is an independent predictive/stability pilot. It estimates reproducibility and effect-size variability. It does not inherit EMP-1.1's confirmatory threshold as its own decision rule and does not itself constitute the final external confirmation of TGCV.

If a subsequent confirmatory experiment is planned from TR-181E, its alpha, minimum effect, sample size and decision rule must be pre-specified from the pilot without accessing the sealed historical confirmatory dataset.

## 6. Additional freeze blockers

The following items remain unverified from the currently inspected repository material:

1. exact recoverable definition of frozen `R`;
2. exact MVE-1.0 implementation;
3. independently generated dataset specification;
4. pilot episode/sample count;
5. generation seed and generator version;
6. exact model hyperparameters for TR-181E;
7. exact resampling/split scheme;
8. exact number of sign-flips or other inferential procedure;
9. missing-data and exclusion rules;
10. protocol hash at freeze time.

These are not defects in the historical EMP-1.1 result. They are outstanding certification items for TR-181E.

## 7. Required action

Create a corrected TR-181E protocol revision and a machine-readable freeze manifest after all outstanding fields have been independently verified.

Do not execute confirmatory inference before the freeze manifest is complete.

## 8. Scientific consequence

This review does not weaken EMP-1.1. It strengthens the programme's epistemic separation:

`EMP-1.1 = historical confirmatory evidence`

`TR-181E = independent stability / reproducibility pilot`

`future external replication = separate confirmatory gate`

This separation is preferable to retrospectively turning TR-181E into a second confirmatory experiment.
