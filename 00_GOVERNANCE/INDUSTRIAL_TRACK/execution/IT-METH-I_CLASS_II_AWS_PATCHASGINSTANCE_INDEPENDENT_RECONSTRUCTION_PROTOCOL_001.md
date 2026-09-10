# IT-METH-I — Class II AWS-PatchAsgInstance Independent Reconstruction Protocol 001

**Date:** 2026-09-11  
**Status:** `DESIGN FROZEN — INDEPENDENT RECONSTRUCTION GATE DEFINED`  
**Candidate:** `AWS-PatchAsgInstance`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`  
**Case / fixture:** `IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE`  
**Parent contract:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PREDECISION_STATE_AND_COMPARATOR_CONTRACT_001.md`  
**Parent build specification:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_CONTROLLED_FIXTURE_BUILD_SPECIFICATION_001.md`

## 1. Purpose

Define the minimum independently reproducible procedure required to establish that the frozen pre-decision fixture state for the Class II AWS-PatchAsgInstance experiment can be reconstructed through a second, non-conditioned reconstruction path.

This protocol is methodological only. It does not authorize execution of `AWS-PatchAsgInstance`, comparator execution, utility scoring, industrial execution, or any modification to TGCV Core.

## 2. Reconstruction object

The reconstruction object is the pre-decision state representation required by the frozen contract:

- ASG identity and source/reference;
- target EC2 instance identity;
- ASG capacity;
- launch-template identity/version;
- effective AMI/image identity;
- OS identity;
- target instance health;
- ASG lifecycle state and lifecycle hooks;
- health-check and replacement/termination behavior;
- Patch Group state;
- effective patch baseline and assignment;
- pre-decision patch compliance state;
- Systems Manager managed-instance state;
- candidate/comparator eligibility predicates;
- observation cutoff;
- evidence provenance and integrity information.

The reconstruction must reproduce the same semantic state represented at the primary Phase-A freeze boundary. It must not infer missing values from the primary reconstruction artifact itself.

## 3. Independence definition

For this fixture, `INDEPENDENT_RECONSTRUCTION = PASS` only when all mandatory conditions below are satisfied:

1. **Frozen-input separation** — reconstruction 002 consumes only the frozen public-source package, frozen fixture contract, frozen reconstruction instructions, and the independently accessible runtime state/evidence explicitly admitted by the protocol.
2. **Primary-result exclusion** — the primary Phase-A freeze record, its derived interpretation, predicate vector, and any downstream analysis are not used as reconstruction inputs.
3. **Procedure separation** — reconstruction 002 follows an independently executed observation/reconstruction path rather than copying field values from reconstruction 001.
4. **Common target/state boundary** — the reconstruction refers to the same frozen fixture target or an equivalently identified target that is demonstrably the same decision-time state.
5. **Common temporal boundary** — the reconstructed values are tied to the same pre-decision observation window/cutoff semantics required by the frozen contract.
6. **Provenance preservation** — each reconstructed field is linked to its underlying observable evidence or to an explicitly permitted deterministic derivation from that evidence.
7. **No post-decision leakage** — information created by candidate/comparator execution, or any other post-decision event, cannot be used to populate the pre-decision state.
8. **Separate artifact** — reconstruction 002 is written as a distinct artifact with its own timestamp and hash.
9. **Sealing before comparison** — reconstruction 002 is frozen before any field-level comparison with reconstruction 001 occurs.

This protocol does not require a second human identity. Independence here is a property of the **reconstruction path and information boundary**. A same-operator technical execution is admissible only if the primary reconstruction outputs are excluded from the reconstruction-002 input path and the procedure is demonstrably separate.

## 4. Permitted inputs

Reconstruction 002 may consume:

- frozen Class II source files and their frozen integrity hashes;
- frozen composition/build/pre-decision contracts;
- the concrete fixture runtime resources that are observable at the reconstruction boundary;
- read-only AWS observations required to reconstruct the frozen state;
- the reconstruction-002 protocol/instructions;
- deterministic normalization rules frozen before comparison.

It must not consume:

- `PHASE_A_PREDECISION_FREEZE_RECORD_001.json` as a source of field values;
- any primary worksheet or interpretation;
- any candidate/comparator execution result;
- utility or superiority conclusions;
- later outcome data;
- newly discovered industrial evidence;
- modified governance rules.

## 5. Required reconstruction procedure

The required sequence is:

`LOAD FROZEN CONTRACT → IDENTIFY TARGET FROM ADMITTED RUNTIME BOUNDARY → OBSERVE READ-ONLY STATE → NORMALIZE VALUES → EVALUATE FROZEN PREDICATES → RECORD PROVENANCE → RECORD CUTOFF → HASH ARTIFACT → SEAL 002 → ONLY THEN RELEASE FOR COMPARISON`

The reconstruction procedure must not invoke `AWS-PatchAsgInstance` and must not invoke the comparator transformation.

## 6. Mandatory reconstructed predicates

The independent artifact must explicitly evaluate the same mandatory predicates used by the Phase-A accessibility gate:

- `target_member_of_asg`;
- `instance_in_service`;
- `ssm_registered`;
- `patch_group_app`;
- `effective_baseline_resolved`;
- `patch_state_resolved`.

A predicate must be evaluated from the reconstruction-002 observations, not copied from reconstruction 001.

## 7. Agreement requirements

After sealing reconstruction 002, a separate comparison operation may compare reconstruction 001 and 002.

Agreement must be assessed at least for:

- target and ASG identity;
- all mandatory state variables;
- effective AMI and OS identity;
- health/lifecycle/replacement state;
- Patch Group and effective baseline;
- pre-decision compliance state;
- SSM state;
- mandatory accessibility predicates;
- observation cutoff semantics;
- evidence provenance.

Differences must be classified as one of:

- `EXACT_AGREEMENT` — same value/identity where exact agreement is required;
- `SEMANTIC_AGREEMENT` — equivalent normalized representation where exact textual equality is not required;
- `RECONSTRUCTION_DISAGREEMENT` — material difference affecting the experimental state or accessibility classification;
- `UNRESOLVED` — evidence insufficient to determine agreement.

No disagreement may be silently repaired by altering the frozen contract or by importing a primary result into reconstruction 002.

## 8. Effort measurement

Analytical effort may be measured only under a separately frozen convention.

This protocol does not define or infer effort from elapsed wall-clock time unless such a convention has already been frozen elsewhere.

No effort comparison may be performed before both reconstructions are sealed.

## 9. Failure rules

The independent reconstruction gate is `FAIL` or `BLOCKED` when any of the following occurs:

- primary reconstruction values are used as inputs;
- post-decision information is used to define the pre-decision state;
- target identity cannot be established;
- mandatory state variables cannot be observed or independently reconstructed;
- mandatory predicates cannot be evaluated;
- provenance cannot be established;
- temporal cutoff cannot be established;
- reconstruction 002 is not sealed before comparison;
- the procedure materially deviates from this protocol without a governed amendment.

A failed reconstruction gate is not evidence against TGCV. It is a failure to establish the required experimental precondition.

## 10. Artifact requirements

The sealed reconstruction-002 artifact must contain at minimum:

- schema/version identifier;
- fixture identity;
- target identity;
- observation start/cutoff timestamps;
- reconstructed state variables;
- accessibility predicate vector;
- field-level evidence/provenance references;
- explicit indeterminate values where applicable;
- reconstruction procedure identifier/version;
- execution-context identifier;
- artifact SHA-256;
- confirmation that primary reconstruction outputs were excluded from the input boundary.

## 11. Downstream comparison boundary

Only after the reconstruction-002 artifact is sealed may a separately governed comparison operation inspect reconstruction 001.

The comparison operation is responsible for:

- field-by-field agreement;
- classification of discrepancies;
- any frozen effort comparison;
- determination of whether the independent reconstruction condition was satisfied.

This protocol itself does not establish reproducibility, utility, superiority, causality, financial value, prediction, industrial benefit, or generalization.

## 12. Governance constraints

This protocol explicitly prohibits:

- execution of `AWS-PatchAsgInstance`;
- comparator execution;
- industrial-case claims;
- production deployment;
- post-decision reconstruction;
- threshold relaxation;
- modification of the TGCV Core;
- promotion of a Class II fixture to a Class I industrial case;
- use of the FAA AMOC independence protocol as a substitute;
- use of reconstruction 001 as a convenience template for field values.

## 13. Current gate

`PHASE_A_PRIMARY_FREEZE = READY`

`INDEPENDENT_RECONSTRUCTION_PROTOCOL = FROZEN`

`INDEPENDENT_RECONSTRUCTION_EXECUTION = NOT YET PERFORMED`

`CANDIDATE_TRANSFORMATION = NOT AUTHORIZED`

`COMPARATOR_TRANSFORMATION = NOT AUTHORIZED`

`UTILITY_SCORING = NOT AUTHORIZED`

## 14. Next routing

The next permissible operation is to establish the **independent reconstruction-002 executable/procedure** from this frozen protocol and the frozen Class II contract, then execute reconstruction 002 without access to the primary freeze artifact values and seal it before comparison.
