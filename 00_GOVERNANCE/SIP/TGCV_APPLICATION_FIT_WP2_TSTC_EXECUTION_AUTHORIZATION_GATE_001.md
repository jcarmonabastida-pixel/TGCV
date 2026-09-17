# TGCV — WP2 TSTC Execution Authorization Gate 001

**Status:** AUTHORIZATION GATE PASSED — EXECUTION MODE MAY NOW BE IMPLEMENTED; NO TSTC RUN PERFORMED
**Date:** 2026-09-17

## 1. Purpose

This record is the separate governance gate required after the successful deterministic preflight. It does not itself constitute a TSTC execution result.

## 2. Preconditions verified

The following frozen inputs remain unchanged:

- TSTC Minimum Demonstrator Specification 001;
- TSTC synthetic fixture freeze 001;
- TSTC Engine Implementation Specification 001;
- FX-C01, FX-C03 and FX-C05 definitions;
- declared interventions;
- declared negative controls;
- declared cross-domain coupling rules;
- conventional baseline definitions.

The local preflight returned:

```text
TSTC_PREFLIGHT_STATUS=PREFLIGHT_PASS
FX-C01=PREFLIGHT_PASS
FX-C03=PREFLIGHT_PASS
FX-C05=PREFLIGHT_PASS
```

The preflight closure was recorded in `TGCV_APPLICATION_FIT_WP2_TSTC_PREFLIGHT_CLOSURE_RECORD_001.md`.

## 3. Authorization decision

**TSTC EXECUTION: AUTHORIZED IN PRINCIPLE WITHIN THE FROZEN SYNTHETIC BOUNDARY.**

This authorization permits implementation and execution of the actual bounded TSTC comparison against the already frozen synthetic fixtures.

It does NOT authorize:

- real-world datasets;
- external infrastructure;
- empirical claims;
- downstream outcome access;
- predictive modelling;
- value analysis;
- deployment or industrial use;
- changes to the frozen fixtures;
- changes to TGCV Core, RMA, Evidence→Claim Matrix or scientific status.

## 4. Execution boundary

The authorized execution must remain strictly within:

`frozen fixture → T_acc,0 → declared intervention → S1/C1 → T_acc,1 → ΔT_acc → declared trajectory → explicit cross-domain propagation → conventional baseline reconstruction → qualitative comparison`

No additional variables, transformations, predicates, coupling edges or outcomes may be introduced during execution.

## 5. Required execution cases

### FX-C01

Execute the frozen positive intervention `I-C01` and its frozen negative control `N-C01`.

Expected structural behaviour is defined by the frozen fixture only; it must not be converted into an interpretation before execution.

### FX-C03

Execute the frozen positive intervention `I-C03` and its frozen negative control `N-C03`.

### FX-C05

Execute the frozen positive intervention `I-C05` and its frozen negative control `N-C05`.

### Cross-domain sequence

Execute only the explicitly frozen dependency chain:

`C01 security=restricted → C03 permission_repo=denied`

`C03 repo=changed → C05 mobility_requirement_A=urgent`

Direct local effects and propagated effects MUST remain separately recorded.

## 6. Required outputs

Each execution must produce the frozen machine-readable schema:

`fixture_id, fixture_version, connector_id, intervention_id, S0, C0, L_version, U_tau, T_acc_0, transition, S1, C1, T_acc_1, Delta_T_acc, trajectory, baseline_model, baseline_representation, baseline_reconstruction, comparison_observations, limitations, non_claims, execution_metadata`

No aggregate superiority score is permitted.

## 7. Execution stop conditions

Execution MUST stop and be classified as blocked/inconclusive if any of the following occurs:

- frozen fixture differs from the recorded version;
- undeclared mutation occurs;
- `U_tau` changes silently;
- admissibility depends on downstream outcome or future activity;
- trajectory uses an inaccessible transformation;
- cross-domain propagation is inferred rather than declared;
- baseline receives additional information;
- negative control changes `T_acc` unexpectedly;
- reproducibility metadata are incomplete;
- output is not reproducible from the frozen fixture.

## 8. Interpretation boundary

Even a successful TSTC execution may establish only a bounded applicability observation about the synthetic demonstrator.

It does not establish TGCV scientific validity, causality, generality, superiority, value creation, deployment readiness, ROI, or `ΔT_acc → ΔV`.

## 9. Current implementation status

The current engine has passed the preflight gate but is still explicitly a preflight implementation. Therefore **no TSTC execution is to be claimed from this authorization record**.

The next controlled implementation step is to add the execution path required by the frozen specification, without modifying the frozen fixture definitions, and then run the authorized synthetic TSTC execution locally.

## 10. Governance disposition

**AUTHORIZATION GATE: PASSED**

**ACTUAL TSTC EXECUTION: NOT YET PERFORMED**

No Core/RMA/Matrix/STATUS scientific change is authorized by this record.
