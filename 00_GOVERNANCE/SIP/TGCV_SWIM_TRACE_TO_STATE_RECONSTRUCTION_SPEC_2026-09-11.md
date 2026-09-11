# TGCV — SWIM Trace-to-State Reconstruction Specification

**Date:** 2026-09-11  
**Status:** `BOUNDED PASS — RECONSTRUCTION SPECIFICATION`  
**Execution:** `NOT PERFORMED`  

## 1. Purpose

Define how concrete SWIM result traces can be mapped to the minimum pre-decision schema required to reconstruct `Pτ(S_t,C_t)` and `T_acc,t` without importing post-outcome information.

## 2. Trace evidence available in the canonical SWIM implementation

SWIM's result tooling explicitly reads time-series vectors for server state, active servers and brownout factor. fileciteturn452file0

The adaptation manager also exposes the pre-decision variables used by its control logic: dimmer factor, active servers, server-pool state, maximum server count, utilization, booting state and average response time. fileciteturn450file0

## 3. Reconstruction record

For each adaptation decision instant `t`, construct a record:

`R_t = (time_t, S_t, C_t, Uτ, Pτ, selection_t, outcome_t)`

with the strict temporal boundary:

`S_t,C_t,Uτ,Pτ` are reconstructed **before** the selected transformation's outcome is incorporated.

`selection_t` and `outcome_t` are stored separately and must never be used to manufacture `Pτ`.

## 4. Trace-to-field mapping

| Required field | Reconstruction source | Role |
|---|---|---|
| `time_t` | simulation timestamp / vector index | decision alignment |
| `active_servers_t` | `activeServers` vector | state |
| `dimmer_factor_t` | `brownoutFactor` vector, transformed according to SWIM convention | state |
| `configured_servers_t` | server-pool/model state or corresponding scalar/vector | execution context |
| `max_servers_t` | frozen simulation configuration | constraint |
| `number_of_dimmer_levels_t` | frozen simulation configuration | candidate domain |
| `booting_t` | reconstructed from configured vs active server state where valid | constraint |
| `utilization_t` | monitor/result observation corresponding to decision window | policy observation |
| `avg_response_time_t` | monitor/result observation corresponding to decision window | policy observation |
| `τ` | native tactic/event record where available; otherwise deterministic reconstruction from state + policy branch | candidate/selection identity |

## 5. Temporal alignment rule

A result record is admissible for TGCV reconstruction only when its timestamp/window can be associated with the corresponding adaptation evaluation instant.

If a trace contains only post-action state and no defensible pre-action boundary, it cannot be used to establish `Pτ` for that decision.

When vector sampling and adaptation evaluation periods differ, the reconstruction must use the last valid pre-decision observation, not the first observation after execution.

## 6. Missingness rule

Unknown fields are not silently imputed.

If a missing field can change the truth value of any `Pτ`, the corresponding `Pτ` is `unknown` and the decision record is not counted as identifiable for that candidate.

If a field is irrelevant to all candidate predicates for the bounded universe, its absence does not block reconstruction.

## 7. Selection/outcome firewall

The following are downstream and cannot be used to establish accessibility:

- post-action active-server count;
- post-action brownout/dimmer value;
- post-action response time;
- subsequent utility/performance outcome;
- any event whose timestamp is strictly after the transformation execution boundary.

They may be retained as `outcome_t+` for later trajectory/outcome analysis, but remain outside `Pτ` reconstruction.

## 8. Identifiability criterion

A decision instant is `RECONSTRUCTABLE` iff:

1. the pre-decision boundary is identifiable;
2. all variables required by the applicable `Pτ` predicates are observable or deterministically derivable;
3. candidate identity is uniquely determined for the bounded transformation representation;
4. no post-outcome variable is required to resolve the predicate;
5. configuration parameters governing the candidate domain are frozen and known.

Otherwise classify the decision as `UNKNOWN / NOT IDENTIFIABLE`, rather than forcing a binary value.

## 9. Gate result

`TRACE SOURCES IDENTIFIED = PASS`  
`PRE-DECISION TEMPORAL BOUNDARY = SPECIFIED`  
`FIELD-LEVEL MAPPING = PASS`  
`OUTCOME FIREWALL = PASS`  
`MISSINGNESS HANDLING = PASS`  
`RECONSTRUCTION CRITERION = PASS`  
`EMPIRICAL TRACE EXECUTION = NOT PERFORMED`

## 10. Consequence

The SWIM candidate has now passed the methodological chain required before execution-package construction:

`Uτ/Pτ formalization → local non-redundancy → observability/identifiability → trace-to-state reconstruction specification`.

This does **not** yet authorize empirical execution. The next controlled operation is a **preflight on an actual SWIM result bundle** to verify that the specified fields and temporal boundaries are present in practice. If the bundle is unavailable or incomplete, the candidate remains `METHOD READY / EMPIRICALLY UNVERIFIED` and no synthetic data are to be substituted.
