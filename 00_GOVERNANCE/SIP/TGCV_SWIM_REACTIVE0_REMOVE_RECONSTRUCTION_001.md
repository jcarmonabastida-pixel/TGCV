# TGCV — SWIM Reactive-0 RemoveServer Reconstruction 001

**Date:** 2026-09-11
**Status:** `BOUNDED PASS — PRE-OUTCOME RECONSTRUCTION`
**Run:** `Reactive-0-20260911-17:49:20-1`
**Experiment:** `Reactive`
**Trace:** `traces/wc_day53-r0-105m-l70.delta`
**Latency:** `0
**Repetition:** `0`
**Seedset:** `0`

## 1. Scope

Reconstruct the pre-decision records for the two observed `RemoveServer` decisions at `t=600s` and `t=660s`, using only evidence available at or before each decision boundary and the native SWIM execution semantics.

## 2. Candidate

`τ_remove = RemoveServer`

Native accessibility conditions established from `ExecutionManagerModBase::removeServer()`:

- `getServers() > 1`
- `serverRemoveInProgress == 0`

`isServerBeingRemoveEmpty()` is treated as a transformation-completion condition, not as a pre-decision accessibility predicate, because `RemoveServer` proceeds when the selected server is busy and completion is deferred until the server becomes empty.

## 3. Reconstruction

| time | pre-decision state | P_remove | selected transformation | pre-outcome basis |
|---:|---|---|---|---|
| 600s | `activeServers=3`; `getServers()=3`; no removal in progress | `PASS` | `RemoveServer → server3` | initial 3 completed additions; native predicate; observed RemoveServer event |
| 660s | `activeServers=2`; `getServers()=2`; no removal in progress | `PASS` | `RemoveServer → server2` | first removal completed sufficiently for second RemoveServer to execute; native predicate; observed RemoveServer event |

## 4. Temporal boundary

The run has `warmup-period=900s`; therefore periodic vectors begin at `t=900s`. The two RemoveServer decisions at `600s` and `660s` cannot be reconstructed from periodic `activeServers` samples. Their pre-decision states are reconstructed from the execution trace plus deterministic SWIM model/executor semantics.

## 5. Outcome firewall

The `activeServers=1` vector value at `t=900s` is retained only as downstream corroboration. It is not used to establish `P_remove` at `600s` or `660s`.

Likewise, post-removal server state and utility/performance observations are excluded from the accessibility predicate.

## 6. Result

`PRE-DECISION BOUNDARY = IDENTIFIABLE`

`P_remove @ 600s = PASS`

`P_remove @ 660s = PASS`

`CANDIDATE IDENTITY = UNIQUE`

`POST-OUTCOME DATA USED IN P_remove = NO`

`RECONSTRUCTION = BOUNDED PASS`
