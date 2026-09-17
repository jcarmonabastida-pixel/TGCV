# TGCV — WP2 TSTC Execution Conformance Audit 001

**Status:** BLOCKED — IMPLEMENTATION CONFORMANCE GAPS IDENTIFIED
**Date:** 2026-09-17
**Scope:** `TSTC_EXECUTION_v001` against frozen Fixture 001 + Engine Implementation Specification 001

## 1. Purpose

This audit compares the first authorized synthetic execution output with the frozen implementation contract before any further execution is attempted.

The audit is fail-closed: missing implementation elements are recorded rather than silently inferred or repaired.

## 2. Confirmed executed component

The first execution correctly demonstrated the local synthetic accessibility calculation for the three positive interventions and the three negative controls.

Observed positive closures:

- C01: `c01.deploy_B`
- C03: `c03.inspect_repo`, `c03.open_pr`
- C05: `c05.start_A`, `c05.start_B`

All three negative controls produced `ΔT_acc = ∅`.

## 3. Conformance gaps

### G1 — Transformation transition contract

The current fixture engine stores empty `affected_variables` for the candidate transformations.

The frozen implementation contract requires every transformation to expose `affected_variables` and a transition operator, and requires undeclared mutations to fail closed.

The execution runner did not execute transformation trajectories, so this latent gap was not exercised by the first run.

**Disposition:** BLOCKED for trajectory execution until resolved without modifying Fixture Freeze 001.

### G2 — C03 state transition required by cross-domain sequence

The frozen cross-domain sequence requires a C03 state transition resulting in `repo=changed`, followed by propagation to C05.

The current C03 implementation assigns `_noop` as the transition operator for all C03 transformations. Therefore no current C03 transformation can produce `repo=changed`.

The first execution returned an empty trajectory and consequently did not reach this condition.

**Disposition:** BLOCKED for cross-domain execution until a deterministic transition operator consistent with the frozen fixture definition is explicitly operationalised.

### G3 — Explicit coupling metadata

The frozen fixture defines two coupling rules:

`C01 security=restricted → C03 permission_repo=denied`

`C03 repo=changed → C05 mobility_requirement_A=urgent`

The current `Fixture` dataclass does not carry these coupling rules. The execution runner therefore cannot yet provide the required explicit propagation record from fixture data.

**Disposition:** BLOCKED for cross-domain execution until coupling metadata is represented explicitly without changing the frozen fixture definitions.

### G4 — Baseline reconstruction

The first execution output contains no baseline representation or reconstruction.

The implementation contract requires parity-controlled baseline reconstruction for C01, C03, C05 and the cross-domain dependency graph.

**Disposition:** BLOCKED for final TSTC completion.

### G5 — Complete machine-readable output contract

The first execution output omits required fields including, at minimum:

- `L_version` / ruleset version;
- explicit `U_tau` representation;
- transition record;
- complete trajectory record;
- baseline representation/reconstruction;
- comparison observations;
- complete reproducibility hashes.

**Disposition:** BLOCKED for final TSTC completion.

### G6 — Reproducibility metadata

The first output contains Python/platform/random-seed/source metadata but not the full required reproducibility tuple:

`source_commit, fixture_id, fixture_version, ruleset_hash, transformation_universe_hash, intervention_id, configuration_hash, environment, random_seed, output_hash`.

**Disposition:** BLOCKED for final TSTC completion.

## 4. Important interpretation boundary

The positive `ΔT_acc` observations from Execution 001 remain valid as observations produced by the implemented local accessibility calculation. They are not discarded.

They are insufficient, however, to classify the complete TSTC minimum demonstrator as successfully executed because the missing modules concern trajectory, propagation, baseline parity and reproducibility rather than the already observed local `T_acc` calculation.

## 5. Frozen-fixture protection

No modification to Fixture Freeze 001 is authorised by this audit.

In particular, the missing C03 transition and coupling metadata must not be solved by silently changing the frozen transformation identities, predicates, interventions or coupling rules.

Any genuinely changed fixture definition requires a new fixture version and a new authorization path.

## 6. Required next implementation action

Create a new execution implementation revision, preferably `TSTC_EXECUTION_v002`, that adds an explicit adapter/operationalisation layer for the frozen fixture definitions and implements, fail-closed:

1. explicit transformation affected-variable declarations;
2. deterministic transition operators;
3. explicit coupling-rule representation;
4. C01 → C03 propagation;
5. C03 → C05 propagation;
6. local versus propagated effect logging;
7. baseline reconstruction with identical information;
8. complete output schema;
9. complete reproducibility metadata;
10. invariant checks and byte-equivalence rerun.

The new implementation MUST be reviewed against the frozen specification before another local execution is requested.

## 7. Governance boundary

This audit changes no scientific claim status and does not modify:

- TGCV Core;
- RMA v3.35;
- Evidence→Claim Matrix v1.12;
- C09;
- C10;
- VSL-44;
- industrial execution authorization.
