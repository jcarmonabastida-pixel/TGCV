# TGCV — WP2 TSTC Execution Authorization Gate 002

**Status:** AUTHORIZATION GATE PASSED — FIXTURE-003 EXECUTION AUTHORIZED; NO TSTC RUN PERFORMED  
**Date:** 2026-09-17  
**Supersedes for Fixture-003 execution scope:** Gate 001 only insofar as its Fixture-001 references are concerned

## 1. Purpose

This record establishes explicit execution authorization for **TSTC Synthetic Fixture-003** after the successful deterministic Fixture-003 preflight.

Gate 001 remains historically valid for the scope it recorded. Because Fixture-003 supersedes Fixture-001 for execution purposes, a separate authorization record is required rather than silently extending Gate 001.

This gate does not constitute a TSTC execution result.

## 2. Preconditions

The following conditions are recorded as satisfied:

1. Minimum Demonstrator Specification 001 remains the governing methodological boundary.
2. Synthetic Fixture Freeze-003 is frozen and is the execution fixture for this run.
3. Engine `TSTC_FIXTURE_ENGINE_v003` is the implementation bound to Fixture-003.
4. Fixture-003 deterministic preflight returned `PREFLIGHT_PASS` for FX-C01, FX-C03 and FX-C05.
5. The previously recorded Freeze-001 / engine traceability discrepancy has been formally resolved by Freeze-003 rather than by silent modification.
6. `c03.modify_repo` is explicitly declared in Fixture-003 and its transition semantics are frozen.
7. The C01→C03 and C03→C05 propagation scenarios are required to remain distinct controlled transition records; execution must not claim that `c03.modify_repo` is accessible after `permission_repo=denied`.
8. No real-world data, external infrastructure, downstream outcomes, predictive modelling, or industrial deployment are part of the authorized scope.

## 3. Preflight evidence

```text
TSTC_FIXTURE_003_PREFLIGHT_STATUS=PREFLIGHT_PASS
FX-C01=PREFLIGHT_PASS
FX-C03=PREFLIGHT_PASS
FX-C05=PREFLIGHT_PASS
```

Recorded reproducibility hashes:

- FX-C01 ruleset: `fa60fd4ddcf272dd575d7ca48ea41fbc637937258687906e006761b0edf69f1c`
- FX-C01 output: `d7662e2da10b688660d721bf549d417260a2b35cd233ae4f5d4ad90be7d7ad57`
- FX-C03 ruleset: `3af1637a317ceb06dbbd34d246a06cf97572fd82e35784f8d504803d367eab0c`
- FX-C03 output: `28913b02799fb0b6d46cae538d014bfb841e27e21bff5fce321a16672158a7d3`
- FX-C05 ruleset: `0f2ac56493845b20baf8af013e68ae368389e94c39ed9605815fccbe3d47bd6a`
- FX-C05 output: `35f4c596747a857c280d1553716d48176f4e7c4bc5bffb4b1601fbc575afb530`

## 4. Authorization decision

**TSTC EXECUTION: AUTHORIZED within the frozen Fixture-003 synthetic boundary.**

Authorization covers only the controlled execution required by the Minimum Demonstrator Specification and Freeze-003.

It does not authorize:

- changes to Freeze-003 during execution;
- changes to TGCV Core, RMA, Evidence→Claim Matrix or scientific status;
- real-world datasets or external infrastructure;
- empirical causal claims;
- predictive modelling;
- value/ROI analysis;
- industrial deployment or validation;
- aggregate superiority scoring;
- introduction of undeclared variables, transformations, predicates, coupling edges or outcomes.

## 5. Mandatory execution boundary

Execution must remain within:

`frozen Fixture-003 → T_acc,0 → declared intervention → S1/C1 → T_acc,1 → ΔT_acc → bounded admissible trajectory → explicit cross-domain propagation → conventional baseline reconstruction → qualitative representation comparison`

The cross-domain path must preserve the two distinct controlled scenarios:

1. `C01 security=restricted → C03 permission_repo=denied`
2. `C03 repo=changed → C05 mobility_requirement_A=urgent`

No execution record may combine these into a single transition in a way that makes `c03.modify_repo` executable under denied repository permission.

## 6. Required execution outputs

The execution must produce the frozen machine-readable fields:

`fixture_id, fixture_version, connector_id, intervention_id, S0, C0, L_version, U_tau, T_acc_0, transition, S1, C1, T_acc_1, Delta_T_acc, trajectory, baseline_model, baseline_representation, baseline_reconstruction, comparison_observations, limitations, non_claims, execution_metadata`

Negative controls must remain negative controls and must produce the frozen expected structural result. Direct local effects and propagated cross-domain effects must remain separately recorded.

## 7. Mandatory stop conditions

Execution must stop and be classified blocked/inconclusive if:

- Fixture-003 differs from the frozen definition;
- an undeclared mutation occurs;
- `U_tau` changes silently;
- a trajectory uses an inaccessible transformation;
- cross-domain propagation is inferred rather than explicitly declared;
- the baseline receives information unavailable to the TGCV representation;
- a negative control changes `T_acc` unexpectedly;
- reproducibility metadata are incomplete;
- output cannot be reproduced from the frozen fixture and execution configuration;
- any implementation behaviour contradicts the Freeze-003 traceability constraints.

## 8. Interpretation boundary

Even a fully successful execution can establish only a bounded applicability observation for this synthetic demonstrator. It does not establish scientific validity, causal validity, superiority, generality, value creation, ROI, industrial applicability, or `ΔT_acc → ΔV`.

## 9. Governance disposition

**FIXTURE-003 EXECUTION AUTHORIZATION GATE: PASSED**  
**ACTUAL TSTC EXECUTION: NOT YET PERFORMED**  
**TGCV Core / RMA / Evidence→Claim Matrix: UNCHANGED**

The next step is implementation of the authorized execution path and controlled local TSTC execution against the frozen Fixture-003, with no fixture or governance mutation.
