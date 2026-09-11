# TGCV — SWIM Observability / Identifiability Gate

**Date:** 2026-09-11  
**Status:** `BOUNDED PASS — PRE-OUTCOME RECONSTRUCTABILITY`  
**Execution:** `NOT PERFORMED`  

## 1. Objective

Determine the minimum observable pre-decision state/context required to reconstruct `Pτ(S_t,C_t)` and therefore `T_acc,t`, without using post-outcome information.

## 2. Canonical source inspection

The SWIM configuration records the adaptation period, server-pool bounds, dimmer configuration and other parameters needed to interpret candidate transformations. fileciteturn442file0

The reactive manager reads the current dimmer factor, active-server state, configured server count, maximum server count, utilization and average response time before constructing a tactic. fileciteturn450file0

The monitoring layer computes `avgResponseTime` from observed throughput/response-time components, confirming that this quantity is an observation available to the adaptation loop rather than an outcome of the candidate transformation being reconstructed. fileciteturn451file0

## 3. Minimum reconstruction schema

For a decision instant `t`, the minimum record required is:

### State / context

- `timestamp_t` or adaptation-loop index;
- `configured_servers_t` / server-pool count used by the execution model;
- `active_servers_t`;
- `servers_booting_t` or an equivalent reconstructable booting predicate;
- `max_servers_t`;
- `dimmer_factor_t`;
- `number_of_dimmer_levels_t` or equivalent discrete-level configuration;
- execution/configuration constraints relevant to the candidate transformation.

### Observations available before decision

- `utilization_t`;
- `avg_response_time_t` when required to distinguish native policy selection from accessibility;
- adaptation-loop configuration (`evaluationPeriod`, threshold and relevant model parameters).

### Candidate identity

- transformation type (`AddServer`, `RemoveServer`, `SetDimmer`);
- for `SetDimmer`, target factor `k`.

## 4. Derived fields

The following can be deterministically reconstructed from the minimum schema:

`booting_t = configured_servers_t > active_servers_t`

`P_add(S_t,C_t)` from booting state and server-pool upper bound.

`P_remove(S_t,C_t)` from booting state, lower server bound and concrete execution constraints.

`P_dimmer(k)(S_t,C_t)` from representability of `k` and current executable dimmer/brownout constraints.

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t)=1}`.

## 5. Identifiability boundary

The gate does **not** require reconstructing the entire SWIM state. It requires only the variables that affect candidate identity and pre-outcome accessibility.

If two pre-decision records are observationally equivalent on this schema, they must not be distinguished by TGCV accessibility unless an additional variable is shown to affect `Pτ`.

Conversely, if omission of one variable changes the truth value of any `Pτ`, that variable is mandatory for the reconstruction schema.

This yields an explicit falsification procedure for the observability claim rather than assuming that all simulator state is necessary.

## 6. Important separation

`avgResponseTime_t` and `utilization_t` may be needed to reconstruct the native **policy-selection** decision, but they are not automatically accessibility predicates. Accessibility remains defined by whether the transformation is executable/admissible from the pre-decision state and context.

This prevents outcome leakage and prevents native policy logic from being silently promoted into TGCV ontology.

## 7. Result

`PRE-DECISION STATE SCHEMA = IDENTIFIED`  
`CANDIDATE IDENTITY = IDENTIFIABLE`  
`Pτ RECONSTRUCTABILITY = PASS`  
`OUTCOME LEAKAGE = CONTROLLED`  
`MINIMUM-SCHEMA FALSIFIER = DEFINED`  
`EMPIRICAL EXECUTION = NOT PERFORMED`

## 8. Next operation

Construct a **trace-to-state reconstruction specification** mapping concrete SWIM result records/traces to the minimum schema above. This remains a G1 methodological operation. Only after that mapping is shown to be complete and non-ambiguous should an execution package be considered.
