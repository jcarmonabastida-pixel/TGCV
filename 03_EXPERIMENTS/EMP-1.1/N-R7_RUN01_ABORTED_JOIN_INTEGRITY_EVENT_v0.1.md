# N-R7 Run 01 — Aborted Join Integrity Event v0.1

**Date:** 2026-09-05  
**Status:** ABORTED / PRE-LEARNER JOIN INTEGRITY FAILURE  
**Scientific execution:** NOT VALID / NO LEARNER FIT  
**Scope:** N-R7 controlled prospective reconstruction

## 1. Event

N-R7 Run 01 was launched under the frozen N-R7 execution specification and aborted during the mandatory label join, before any learner fitting, prediction, LogLoss calculation, sign-flip inference, or control execution.

Observed exception:

`MISSING_LABEL:train:(0, '618a5e9fbec132cfee8262eefabb2d1f72b7039e0081aaac9a927b9e32dcc8a4')`

## 2. Evidence

The first predictor record contained:

- `episode_id = 0`
- predictor-side `initial_snapshot_sha256 = 618a5e9fbec132cfee8262eefabb2d1f72b7039e0081aaac9a927b9e32dcc8a4`

The corresponding N-R4B.4 trajectory record contained:

- `episode_id = 0`
- outcome `Y = 1`
- outcome-side `initial_snapshot_sha256 = 6aeb0db9cea8796fc6a6a68b509e3c3dda212a383b9fdde595d39177aae03068`

The frozen N-R4B.4 trajectory artifacts themselves remained hash-consistent with their frozen corpus manifest:

- train trajectories: `08ED37B6B13A033EB47BB52E559B7A11DB3C8917B68BFF19AAD73F98AB836514`
- test trajectories: `1A5E9A21FA1F0F2AD756E7743045DC40835A7C3D5203C321F6B0427B32C2EAE8`

## 3. Root cause

The predictor implementation used a different hash definition from N-R4B.4.

N-R4B.4 hashes the semantic initial state consisting of:

`components + edges + objective + resources`

using sorted compact JSON, ASCII-safe encoding, UTF-8 bytes, and no newline. `episode_id` is excluded.

The prior N-R5 implementation hashed the complete snapshot record, including `episode_id`, and appended a newline. Therefore the same semantic `S_0` received different hashes across artifacts.

This is an integration defect in the predictor representation implementation/specification boundary. It is not a defect in the frozen N-R4B.4 corpus.

## 4. Scientific consequence

The join firewall correctly detected the inconsistency and prevented learner execution. The run produced no scientific result and must not be interpreted as a failed hypothesis test.

No historical EMP-1.1 result was used as a tuning target or acceptance criterion.

## 5. Corrective action

The repair is strictly limited to semantic identity consistency:

1. N-R4B.4 snapshots/corpus are unchanged.
2. B, R, and B+R definitions are unchanged.
3. N-R7 join key remains `episode_id + initial_snapshot_sha256`.
4. N-R5.1 is superseded by v0.2, which normatively defines the semantic `S_0` hash.
5. N-R5 predictor implementation is corrected accordingly.
6. N-R5.2 conformance is rerun.
7. N-R5.3 predictors are regenerated from the unchanged frozen N-R4B.4 snapshots.
8. N-R5.3 integrity/freeze is rerun.
9. N-R7 expected predictor hashes are updated only after the regenerated dataset is frozen.
10. N-R7 preflight is rerun before any scientific execution retry.

## 6. Integrity principle

The join must **not** be weakened by joining on `episode_id` alone or by ignoring hash mismatch. The mismatch is itself evidence that the two artifacts do not share a verified initial-state identity.

**Disposition:** preserve this event permanently as a reproducibility/integrity audit record; do not delete or overwrite it.
