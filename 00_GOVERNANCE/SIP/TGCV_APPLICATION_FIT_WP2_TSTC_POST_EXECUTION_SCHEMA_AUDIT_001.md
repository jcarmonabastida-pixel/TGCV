# TGCV — WP2 TSTC Post-Execution Schema Audit 001

**Status:** BLOCKED — OUTPUT CONTRACT NON-CONFORMANCE
**Date:** 2026-09-17
**Execution reviewed:** `TSTC_EXECUTION_v003`
**Fixture:** Freeze-003 / fixture version `003`
**Purpose:** post-execution audit against the frozen Minimum Demonstrator Specification 001

## 1. Audit boundary

This audit evaluates the machine-readable output contract of the already completed authorized Fixture-003 execution. It does **not** rerun the experiment and does not alter the frozen fixture, execution authorization, Core, RMA, Evidence→Claim Matrix, or STATUS.

The governing specification requires each run to contain at least:

`fixture_id, fixture_version, connector_id, intervention_id, S0, C0, L_version, U_tau, T_acc_0, transition, S1, C1, T_acc_1, Delta_T_acc, trajectory, baseline_model, baseline_representation, baseline_reconstruction, comparison_observations, limitations, non_claims, execution_metadata`.

## 2. Result

The completed execution demonstrates the intended bounded behavior in the supplied execution record, including local interventions, negative controls, explicit C01→C03 and C03→C05 propagation, and qualitative baseline comparison. However, the serialized output does not conform literally to the frozen minimum output schema.

### 2.1 Missing required top-level/per-run fields

The execution result does not expose the required schema fields as explicit run records:

- `fixture_id`
- `connector_id`
- `L_version`
- `U_tau`
- `transition`
- `baseline_model`
- `baseline_representation`
- `baseline_reconstruction`
- `comparison_observations`

`fixture_version`, `intervention_id`, `S0`, `C0`, `S1`, `C1`, `T_acc_0`, `T_acc_1`, `Delta_T_acc`, `trajectory`, `limitations`, `non_claims`, and `execution_metadata` are present either directly or nested under connector-specific structures, but the current serialization does not implement the specified per-run record contract.

## 3. Implementation finding

This is not only a field-renaming issue.

The current executor implements `_baseline_representation()` as a representation containing state, context and feasible actions, and `_baseline_compare()` compares only the before/after feasible-action sets. The frozen protocol, however, defines comparison dimensions covering:

- transformation identities;
- admissibility conditions;
- state/context dependencies;
- transition causing accessibility change;
- cross-domain dependency;
- trajectory consequence;
- assumptions;
- information omitted.

Therefore, a simple serialization wrapper or field renaming would not by itself establish full baseline-comparison conformance.

## 4. Additional traceability observation

The execution metadata reports a `source_commit`. This must remain the exact repository commit from which the executed v003 program was run. The reported value is retained as execution evidence and is not reinterpreted by this audit. A repository-level commit/tree check may be performed separately if required, but it is not necessary to establish the present schema non-conformance.

## 5. Scope of the finding

The finding is classified as **OUTPUT CONTRACT NON-CONFORMANCE**, not as a behavioral failure of the completed synthetic execution.

No evidence is admitted to TGCV scientific claims by this audit.

No conclusion is drawn about scientific validity, causality, superiority, generality, value creation, industrial validation, or `ΔT_acc → ΔV`.

## 6. Disposition

**TSTC execution result:** retained as historical execution evidence.

**Applicability closure:** BLOCKED pending output-contract correction.

**Experiment rerun:** NOT YET AUTHORIZED.

**Required next action:** implement a new execution/output-contract revision that explicitly materializes the frozen per-run schema and the complete qualitative baseline-comparison dimensions. Then perform a pre-execution/static audit of the revised implementation before deciding whether a fresh execution is required.

A corrected executor must not silently rewrite the already completed v003 result as though v003 had produced the missing fields.

**Core/RMA/Matrix/STATUS:** unchanged.
