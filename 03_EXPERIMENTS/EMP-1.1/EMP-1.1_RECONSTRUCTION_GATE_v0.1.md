# EMP-1.1 — Reconstruction Gate v0.1

**Date:** 2026-08-27
**Status:** GATE OPEN — IMPLEMENTATION NOT YET VERIFIED

## Finding

The Library search has recovered the frozen EMP-1.1 protocol and the sealed confirmatory episode dataset/result record. The protocol fixes the representation-level hypothesis, baseline scope, confirmatory sample sizes, seeds, learner family, permutation procedure and controls.

The recovered episode records expose snapshots containing components, directed edges, resources, objectives, trajectories and outcomes. Therefore the empirical input record is substantially recoverable.

## Critical unresolved boundary

The recovered artifacts still do not provide an unambiguous executable definition of every transformation family and transition rule used to generate the historical episodes, nor a complete source implementation of the feature construction `snapshot -> T_acc -> R`.

The earlier TR-180E document also contains a historical statement that the pilot should use a family-level split. The completed EMP-1.1 record, however, does not expose enough information in the currently recovered artifacts to certify that this exact split rule was used for the recorded result. This must therefore remain OPEN rather than being silently assumed.

## Consequence

We can reconstruct and verify the **evaluation layer** against the sealed dataset only when the exact feature construction is recovered or explicitly labelled as reconstructed.

We cannot yet claim exact historical re-execution of EMP-1.1.

## Next controlled action

1. Recover or reconstruct `snapshot -> T_acc -> R` with provenance labels.
2. Recover exact model hyperparameters and encoding.
3. Implement a clean-room evaluation harness against the sealed test episodes.
4. Run unit/smoke tests without using the recorded result for tuning.
5. Compare against the frozen result only after the implementation is frozen.
6. Record all discrepancies.
7. Only then decide whether EMP-1.1 achieves `REPRODUCIBLE` status.

## Scientific integrity rule

The recorded result remains immutable. A failure to reproduce it is evidence requiring investigation; it is not permission to alter the specification retrospectively.

**Current status:**

`EMP-1.1 SCIENTIFIC RECORD = FROZEN`

`EMP-1.1 COMPUTATIONAL SPECIFICATION = SUBSTANTIALLY RECOVERED`

`EMP-1.1 EXECUTABLE REPRODUCTION = OPEN`

`TR-181E EXECUTION = BLOCKED`
