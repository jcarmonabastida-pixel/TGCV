# D-OPS-24 v0.5 — Execution Authorization v0.1

**Status:** AUTHORIZED / EXECUTION RELEASED
**Date:** 2026-09-09
**Protocol:** `D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.5.md`
**Preflight:** `D-OPS-24_PREFLIGHT_v0.5.md` — PASS
**Freeze/propagation:** `EXT-UPD-4.1_DOPS24_V05_FREEZE_PROPAGATION_v0.1.md` — CLOSED

## Authorization

Controlled broader documentary discovery under D-OPS-24 v0.5 is authorized.

This authorization releases **discovery and Minimum Translation Eligibility (MTE) screening only**. It does not authorize Translation Trace, Extended TGCV Conformance, dataset acquisition, empirical execution, outcome/value analysis or causal inference.

## Search budget

A new v0.5 budget is established independently of the exhausted v0.4 F2 budget.

- Query-family budget: **12 QF maximum** across the whole v0.5 discovery operation; cumulative and non-resettable.
- Candidate-record budget: **30 candidates maximum** for documentary screening/admission.
- Maximum 3 QFs per candidate family unless a new governance decision explicitly changes the budget.
- Query-family identity is exact and versioned. Material changes in semantic terms, Boolean structure or source restriction create a new QF and consume one budget unit.
- Pagination, opening/following a result, inspecting a cited primary source, or extracting evidence from an already retrieved candidate does not by itself create a new QF.

## Candidate-family strategy

Discovery may cover the following pre-registered families, in this order as operationally useful:

1. physical/engineering reconfiguration;
2. distributed/networked systems;
3. biological/ecological state-transition systems;
4. organizational/process systems;
5. manufacturing/production;
6. logistics/infrastructure;
7. software/hardware co-evolution, excluding the already operationalized Rust case;
8. control/cyber-physical systems;
9. scientific/experimental systems with repeated configuration changes.

Family order may be selected to maximize structural diversity, but every executed QF must be recorded before execution and remain within the global budget.

## Discovery / MTE boundary

A candidate is admitted for MTE screening only when documentary evidence permits assessment of:

- stable native system/state unit `S_D`;
- independently constructible native transformation universe/schema `Uτ,D`;
- non-circular, pre-outcome accessibility criterion `Pτ,D`;
- constructible `T_acc,D`;
- ordered observations sufficient to test `ΔT_acc,D`;
- accessibility not defined by downstream outcome;
- native/TGCV distinction without silent proxy equivalence;
- provenance and unresolved/empty cases;
- non-redundancy with existing TGCV operational domains.

Discovery does not require Reach, Trajectory, Outcome or Value evidence.

## Translation Readiness boundary

Only after MTE PASS may a candidate enter Translation Readiness. TR is documentary feasibility and requires the v0.5 TR-1/TR-2/TR-3 checks. It is not empirical validation.

Observed state transitions must not be treated automatically as the accessible transformation space.

## Outcome blindness

Candidate selection and MTE/TR screening must not depend on favorable downstream outcomes, performance, adoption, survival, reward, popularity, impact or value.

## Stop conditions

Stop and record a candidate as FAIL or INDETERMINATE when required native constructs, accessibility, provenance or semantic distinctions cannot be established. Stop the operation if a material protocol deviation occurs or if the authorized budget is exhausted.

## Authorization exclusions

Not authorized by this record:

- Q13 or any QF beyond the 12-unit budget;
- dataset download or processing;
- empirical experiment;
- causal identification;
- outcome/value optimization or analysis;
- Extended TGCV Conformance execution;
- claim inflation or cross-domain generalization claims.

## Required execution record

Each QF must record its exact formulation, date/channel, result set, candidate dispositions and budget consumption. Each admitted candidate must receive an auditable MTE record before any Translation Readiness decision.

## Next control

Execute the authorized v0.5 discovery, starting with the first controlled candidate-family QF, and record results in a dedicated execution log. No additional authorization is needed between QFs while the operation remains within this authorization and all controls are respected.
