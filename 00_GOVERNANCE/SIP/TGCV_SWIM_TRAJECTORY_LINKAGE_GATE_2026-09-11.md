# TGCV — SWIM Trajectory Linkage Gate — 2026-09-11

**Status:** `PREPARED — NOT EXECUTED`

**Purpose:** define the next bounded falsifiable question after closure of SWIM Reactive-2, without reopening the Reactive-2 policy-independence gate and without implying causal or value evidence.

## Scientific question

Given a reconstructed change in accessible transformation space `ΔT_acc,t`, can the subsequent trajectory of selected/executed transformations and relevant system-state transitions be reconstructed sufficiently to determine whether the accessibility change is followed by a distinguishable trajectory change in the bounded SWIM exemplar?

The test is explicitly **trajectory-linkage**, not causal identification.

## TGCV chain under test

`S_t,C_t → Pτ(S_t,C_t) → T_acc,t → ΔT_acc,t → selected τ_t → S_{t+1},C_{t+1} → subsequent trajectory`

The gate does not test the final value layer.

## Reuse boundary

Use only the already frozen and executed SWIM evidence surface:

- SWIM Reactive-0 Run 0;
- SWIM Reactive2 Run 0 only where it provides non-comparative methodological support;
- existing frozen configuration and traces;
- existing `.sca/.vec` artifacts and reconstructed event records;
- existing source-semantics reconstructions already admitted by governance.

**No new dataset is authorized by this gate.**

**No additional Reactive-0 or Reactive2 execution is authorized by this gate.**

## Required reconstruction

For each admitted Reactive-0 trajectory point where `ΔT_acc` is already reconstructable:

1. identify the predecision `(S_t,C_t)` and `T_acc,t`;
2. identify the bounded change `ΔT_acc,t` without using downstream outcome to define accessibility;
3. identify the selected transformation `τ_t`, when observed;
4. reconstruct the immediate state transition `(S_t,C_t) → (S_{t+1},C_{t+1})` where evidence permits;
5. reconstruct a bounded postdecision trajectory window using only variables observable from the existing run;
6. distinguish transformation selection from accessibility itself;
7. record whether the observed trajectory differs across points with different `T_acc` states or `ΔT_acc` transitions.

## Candidate trajectory observables

Admitted observables are limited to variables already present in the frozen/executed evidence, including where available:

- ordered transformation events (`AddServer`, `RemoveServer`, `SetDimmer(k)`);
- active-server state;
- brownout/dimmer state;
- server-count transition timing;
- server-removal completion timing;
- utility-period vector only as a downstream trajectory/outcome-linked observable, never as an accessibility predicate.

## Acceptance criteria

- **T1 — Provenance:** all trajectory inputs trace to existing frozen/executed SWIM evidence.
- **T2 — Predecision separation:** `T_acc,t` and `ΔT_acc,t` are established independently of downstream trajectory/outcome.
- **T3 — Event identity:** selected transformation events are independently identifiable.
- **T4 — State transition:** at least one bounded pre/post state transition is reconstructable.
- **T5 — Trajectory window:** at least one bounded postdecision trajectory window is reconstructable without outcome leakage into the accessibility definition.
- **T6 — Linkage:** at least one bounded case shows a distinguishable subsequent trajectory pattern associated with a reconstructed accessibility-space change.
- **T7 — Boundary:** the result is explicitly classified as non-causal unless an independently identified causal design is present.

## Falsifiers / stop conditions

Stop and classify the gate `INCONCLUSIVE` if:

- `ΔT_acc` cannot be established before the downstream trajectory window;
- selected transformation identity cannot be separated from accessibility;
- state transitions cannot be reconstructed with sufficient temporal ordering;
- the available observables are insufficient to define a bounded trajectory window;
- apparent trajectory differences depend on outcome variables that were used to define accessibility;
- timestamp/event-ordering ambiguity prevents determining the transition sequence.

The gate does **not** treat absence of a trajectory difference as failure of TGCV. It is evidence against the specific bounded trajectory-linkage expectation only.

## Claim boundary

A PASS can provide bounded methodological evidence relevant to **C08** and potentially qualify the interpretation of the `ΔT_acc → trajectory` segment of C16.

A PASS does **not** by itself establish:

- C09 causal identification;
- C10 value creation/prediction;
- C11 transversal validity;
- C12 explanatory superiority;
- industrial utility;
- general validity across self-adaptive systems.

No C01–C16 upgrade is authorized by this preparation record.

## Execution authorization

`EXECUTION = NOT AUTHORIZED BY THIS RECORD`

Any execution requires a separate authorization record after this gate is reviewed for provenance, reconstruction feasibility, and non-redundancy.

## Routing

This gate is the proposed next scientific operation after:

- SWIM Reactive-0 closure;
- SWIM Reactive2 closure with A8 `NOT_COMPARABLE`;
- Evidence→Claim Matrix v1.2 propagation;
- IGRT governance reconciliation PASS.

The intended next action is **gate review**, not another Reactive2 run and not a claim upgrade.
