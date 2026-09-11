# TGCV — SWIM Reactive-0 SetDimmer(k) Reconstruction 001

**Status:** `BOUNDED PASS — PRE-OUTCOME RECONSTRUCTION`

**Date:** 2026-09-11

**Experiment:** `Reactive`

**Run:** `Reactive-0-20260911-17:49:20-1`

**Trace:** `traces/wc_day53-r0-105m-l70.delta`

**Latency:** `0`

**Repetition:** `0`

**Seedset:** `0`

## 1. Candidate transformation

`τ_dimmer(k) = SetDimmer(k)`

The tactic identity is explicit in `SetDimmerTactic` and its execution maps directly to `ExecutionManager::setBrownout(1-k)`.

## 2. Operational semantics

`AdaptInterface::cmdSetDimmer(args)` converts the supplied value to a double and calls:

`setBrownout(1 - dimmer)`.

`SetDimmerTactic::execute()` performs the same mapping through the execution manager.

`ExecutionManagerModBase::setBrownout()` updates the model brownout factor and invokes the underlying brownout operation; no independent tactic-level guard was identified in the inspected execution path.

Therefore candidate identity, policy selection and execution outcome remain analytically distinct.

## 3. Configuration evidence

From `Reactive-0.sca` (`runParam`):

- `*.numberOfBrownoutLevels = 5`
- `*.dimmerMargin = 0.1`
- no `lowerDimmerMargin` entry was persisted in `runParam` for this run.

`ReactiveAdaptationManager` defines:

`dimmerStep = 1 / (numberOfDimmerLevels - 1) = 1 / 4 = 0.25`.

The observed tactic transitions therefore use native manager step size:

- `1.00 → 0.75`
- `0.75 → 1.00`

The `dimmerMargin` parameter does not invalidate these two observed values: the manager constructs the target directly by adding/subtracting `dimmerStep`, and the inspected `SetDimmerTactic` execution path does not impose a separate discrete-level guard.

## 4. Reconstructed events

### Event A — t = 4740

Observed execution event:

`SetDimmer(0.75)`

Pre-decision dimmer state reconstructed from the preceding brownout vector state:

`dimmer = 1.00`.

Manager step:

`1.00 - 0.25 = 0.75`.

Reconstruction:

- candidate identity: `τ_dimmer(0.75)` — unique
- target generation: `1.00 - dimmerStep = 0.75`
- pre-decision target representability: `PASS`
- outcome-independent accessibility: `PASS`
- post-outcome data used to define accessibility: `NO`

### Event B — t = 4800

Observed execution event:

`SetDimmer(1.00)`

Pre-decision dimmer state reconstructed from the preceding vector state:

`dimmer = 0.75`.

Manager step:

`0.75 + 0.25 = 1.00`.

Reconstruction:

- candidate identity: `τ_dimmer(1.00)` — unique
- target generation: `0.75 + dimmerStep = 1.00`
- pre-decision target representability: `PASS`
- outcome-independent accessibility: `PASS`
- post-outcome data used to define accessibility: `NO`

## 5. Policy-selection boundary

The Reactive manager additionally selects the direction of the dimmer change from its observed response-time branch and, for downward dimming, from the unavailability of `AddServer`.

These are **policy-selection conditions**, not retroactive definitions of the candidate transformation itself.

The reconstruction therefore preserves the TGCV distinction:

`candidate identity → accessibility → policy selection → execution → outcome`.

## 6. Result

`RECONSTRUCTION = BOUNDED PASS`

Both observed `SetDimmer(k)` transformations in Reactive-0 are reconstructable from pre-decision configuration/state and source semantics without using the post-decision outcome as an accessibility condition.

This closes the bounded reconstruction of `τ_dimmer(k)` for Reactive-0. No rerun is required.
