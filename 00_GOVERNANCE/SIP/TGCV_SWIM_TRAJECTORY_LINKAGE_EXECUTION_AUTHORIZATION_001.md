# TGCV — SWIM Trajectory Linkage Execution Authorization 001

**Status:** `AUTHORIZED — BOUNDED RECONSTRUCTION ONLY`

**Date:** 2026-09-12

## Authorization basis

This authorization follows the bounded feasibility/non-redundancy review:
`TGCV_SWIM_TRAJECTORY_LINKAGE_REVIEW_001.md`.

The underlying gate is:
`TGCV_SWIM_TRAJECTORY_LINKAGE_GATE_2026-09-11.md`.

## Scientific operation

Perform a bounded reconstruction of the downstream trajectory following already reconstructed Reactive-0 accessibility-space changes.

**This is not a new simulation.**

**This is not a causal-identification experiment.**

## Authorized inputs

Only existing canonical/frozen evidence may be used:

- SWIM Reactive-0 Run 0 artifacts and execution trace;
- existing Reactive-0 T_acc reconstruction;
- existing AddServer / RemoveServer / SetDimmer reconstructions;
- existing reconstruction consolidation;
- existing frozen SWIM configuration/traces and provenance;
- source-semantics evidence already admitted by governance.

Reactive2 Run 0 may be referenced only for the already established non-comparative methodological disposition. It must not be treated as a matched control or used to manufacture A8 comparability.

## Prohibited inputs / actions

- no new dataset;
- no new simulation run;
- no rerun of Reactive-0;
- no rerun of Reactive2;
- no external outcome data;
- no causal inference;
- no value prediction/creation inference;
- no claim upgrade;
- no reinterpretation of Reactive2 A8 `NOT_COMPARABLE`.

## Execution target

Construct at least one bounded trajectory window from existing Reactive-0 evidence in which:

1. the predecision state/context is identified;
2. `T_acc` is reconstructed independently of downstream outcome;
3. `ΔT_acc` is identified where the evidence supports it;
4. the selected transformation is identified;
5. the immediate state transition is reconstructed where temporally supportable;
6. subsequent ordered transformation/state events are reconstructed for a bounded window;
7. the linkage between accessibility-space change and subsequent trajectory is classified as observed, unsupported, or indeterminate.

## Temporal integrity rule

Same-timestamp observations are not sufficient by themselves to establish predecision equivalence. Event ordering and zero-latency effects must be respected. When ordering cannot establish whether a vector sample is pre- or post-action, that point must be marked indeterminate rather than inferred.

## Acceptance

The reconstruction may close with `PASS — BOUNDED TRAJECTORY LINKAGE` only if T1–T5 and at least one bounded T6 linkage case are satisfied.

If T1–T5 are satisfied but no distinguishable linkage is established, classify the result as bounded negative evidence against the specific linkage expectation, not as failure of TGCV overall.

If temporal/state reconstruction is insufficient, classify `INCONCLUSIVE`.

T7 boundary must always remain PASS: no causal interpretation without an independent causal design.

## Claim boundary

Any result is limited to methodological evidence relevant to C08 and qualification of the `ΔT_acc → trajectory` segment of C16. No upgrade to C09–C12, transversal validity, industrial utility, or value claims is authorized.

## Output governance

The executor must produce a reconstruction/disposition record in GitHub under `00_GOVERNANCE/SIP/`.

The record must contain:

- provenance of every admitted input;
- reconstructed trajectory table/window;
- temporal-ordering decisions;
- T1–T7 acceptance status;
- falsifier/stop-condition assessment;
- explicit claim boundary;
- final disposition.

## Authorization

`EXECUTION = AUTHORIZED`
`MODE = BOUNDED_RECONSTRUCTION_ONLY`
`SIMULATION = NOT_AUTHORIZED`
`NEW_DATASET = NOT_AUTHORIZED`
`CLAIM_UPGRADE = NOT_AUTHORIZED`
