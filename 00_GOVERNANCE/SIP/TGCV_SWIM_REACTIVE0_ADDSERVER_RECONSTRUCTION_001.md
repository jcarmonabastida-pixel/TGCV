# TGCV — SWIM Reactive-0 AddServer Reconstruction 001

**Status:** `BOUNDED PASS — PRE-OUTCOME RECONSTRUCTION`

**Date:** 2026-09-11

**Experiment:** `Reactive`

**Run:** `Reactive-0-20260911-17:49:20-1`

**Trace:** `traces/wc_day53-r0-105m-l70.delta`

**Latency:** `0`

**Repetition:** `0`

**Seedset:** `0`

## 1. Candidate transformation

`τ_add = AddServer`

The execution path creates the next server module and, with zero boot latency, completes activation immediately.

## 2. Operational accessibility

The inspected SWIM semantics impose two relevant execution-level conditions:

`¬isServerBooting(S_t) ∧ getServers(S_t) < maxServers(S_t)`

`Model::getServers()` accounts for a server currently booting by returning `activeServers + 1`; `Model::addServer()` also asserts that no server is already booting.

These conditions are evaluated before the new server is added and do not depend on its subsequent outcome.

## 3. Reconstructed events

### Event A — t = 3960

Vector evidence gives the pre-transition state as:

`activeServers = 1`

and the post-transition state as:

`activeServers = 2`.

Configuration gives:

`maxServers = 3`.

Therefore, before the decision:

`¬isServerBooting ∧ 1 < 3 → PASS`.

The observed transition is therefore reconstructable as:

`1 → AddServer → 2`.

### Event B — t = 4680

Vector evidence gives the pre-transition state as:

`activeServers = 2`

and the post-transition state as:

`activeServers = 3`.

Therefore, before the decision:

`¬isServerBooting ∧ 2 < 3 → PASS`.

The observed transition is therefore reconstructable as:

`2 → AddServer → 3`.

## 4. Boundary conditions

The periodic vectors begin after the configured 900 s warm-up period. The two AddServer events occur after warm-up, so their pre/post state evidence is directly observable in the periodic `activeServers` vector.

Duplicate vector entries at the same simulation time are treated as repeated writes of the same state, not as distinct transformations.

## 5. Result

- candidate identity: `τ_add` — unique
- pre-decision accessibility at t=3960: `PASS`
- pre-decision accessibility at t=4680: `PASS`
- target/outcome independence: `PASS`
- reconstruction: `BOUNDED PASS`

No rerun is required.
