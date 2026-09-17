# TGCV — C05 EV–Grid Minimum Demonstrator Fixture 001

**Status:** FROZEN FIXTURE — PRE-FLIGHT READY — EXECUTION NOT AUTHORIZED
**Date:** 2026-09-17
**Specification:** `TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_MINIMUM_DEMONSTRATOR_SPEC_001.md`

## 1. Fixed numerical system

- Site A charging capacity: 11 kW
- Site B charging capacity: 11 kW
- Shared grid capacity at baseline: 22 kW
- Constrained shared grid capacity T1: 8 kW
- EV1 initial energy: 20 kWh
- EV2 initial energy: 20 kWh
- EV1 required departure energy: 24 kWh
- EV2 required departure energy: 24 kWh
- Standard charging power: 4 kW per active EV
- Reduced charging power: 2 kW per active EV
- V1G/V2G discharge power: 2 kW
- Decision horizon: 3 discrete decision steps
- No stochastic inputs.

## 2. Initial state S0

```text
site_assignment = {EV1:A, EV2:B}
charging_state = {EV1:idle, EV2:idle}
grid_capacity_state = high
active_power = {A:0, B:0}
EV_energy_state = {EV1:20, EV2:20}
```

## 3. Initial context C0

```text
departure_requirement = {EV1:24, EV2:24}
mobility_requirement = {EV1:required, EV2:required}
site_capacity = {A:11, B:11}
grid_limit = 22
charging_policy = standard_then_reduced
V1G_V2G_capability = {EV1:available, EV2:unavailable}
```

## 4. Transformation universe U_tau

Exactly the following 12 transformations are evaluated:

```text
accept_A
accept_B
defer
reduce_power
shift_window
redirect_A_to_B
redirect_B_to_A
reserve_capacity
release_capacity
v1g_discharge
v2g_discharge
reject
```

## 5. Frozen admissibility predicates

All predicates are Boolean and use only S_t, C_t and L.

- `accept_A`: A has available capacity, selected EV can charge, and resulting grid load does not exceed grid limit.
- `accept_B`: B has available capacity, selected EV can charge, and resulting grid load does not exceed grid limit.
- `defer`: always admissible while an unmet departure requirement remains.
- `reduce_power`: admissible when at least one EV can charge at 2 kW without violating site/grid limits.
- `shift_window`: admissible when the affected EV has an unmet departure requirement and the policy permits temporal shifting.
- `redirect_A_to_B`: admissible when EV at A can be assigned to B, B has capacity, mobility constraints permit the move, and resulting grid load is within limit.
- `redirect_B_to_A`: symmetric condition for B→A.
- `reserve_capacity`: admissible when unused site/grid capacity exists and reservation does not exceed the grid limit.
- `release_capacity`: admissible when previously reserved capacity exists.
- `v1g_discharge`: admissible only for an EV explicitly having V1G capability and sufficient stored energy above its required departure energy floor.
- `v2g_discharge`: admissible only for an EV explicitly having V2G capability and sufficient stored energy above its required departure energy floor.
- `reject`: admissible only as a terminal refusal action when no charging transformation satisfying the current requirement is admissible.

No predicate references downstream outcome, trajectory after the decision, monetary value, or performance measurement.

## 6. Controlled transitions

### T1 — Grid capacity contraction

`grid_limit: 22 kW → 8 kW`.

All other variables remain fixed.

### T2 — EV demand increase

`departure_requirement: {24,24} → {28,28}`.

All other variables remain fixed.

### T3 — Site B unavailable

`site_capacity.B: 11 kW → 0 kW`.

All other variables remain fixed.

### T4 — Departure requirement tightens

`departure_requirement: {24,24} → {26,26}`.

All other variables remain fixed.

### T5 — V1G/V2G capability transition

`V1G_V2G_capability.EV2: unavailable → available`.

All other variables remain fixed.

### T6 — Combined cross-domain transition

Apply T1 and T4 simultaneously:

`grid_limit: 22 → 8 kW`

and

`departure_requirement: {24,24} → {26,26}`.

## 7. Negative controls

### NC1 — Irrelevant descriptive change

`telemetry_label = normal → recalibrated`.

This variable is not referenced by any admissibility predicate.

Expected:

`Delta_T_acc = empty`.

### NC2 — Routing-only change

Change the deterministic scheduling tie-break order while keeping S, C and L unchanged.

Expected:

`Delta_T_acc = empty`.

This control tests separation between accessibility and selection among already accessible transformations.

## 8. Deterministic trajectory policy

Before execution, use this fixed priority only among transformations already in `T_acc`:

1. satisfy an unmet departure requirement;
2. prefer local charging over redirection;
3. prefer standard power over reduced power;
4. prefer earlier decision-step execution;
5. break remaining ties by lexical transformation identifier.

The policy cannot alter `T_acc` and cannot inspect future outcomes.

## 9. Conventional baseline fixture

The baseline receives exactly:

- S_t;
- C_t;
- L;
- U_tau;
- the same transition;
- the same deterministic selection policy.

It computes a conventional feasible-action set by evaluating the same constraints. It has no future-outcome information.

## 10. Runtime contract

Expected execution environment:

- Windows 10/11 compatible host;
- Python 3.8.10;
- UTF-8 text I/O;
- deterministic execution;
- no network access required;
- no external datasets;
- no random seed required.

The actual runtime version and platform fingerprint must be recorded at execution and must match this contract before authorization.

## 11. Fixture non-claims

This fixture is synthetic and bounded. It does not represent a real EV-grid deployment, does not estimate operational performance, and does not establish causal or value effects.
