# IT-G1 — Case Identifiability Package

**Case:** `AWSSupport-ExecuteEC2Rescue`  
**Candidate:** `RETAINED CONDITIONALLY`  
**IT-G1:** `NOT STARTED`  
**Execution authorization:** `NONE`  
**Package status:** `DESIGNED / PERSISTED — PENDING COMPLETENESS REVIEW`

## Purpose

Freeze the identifiability design for a single Windows EC2 instance that is inaccessible because of an RDP-related problem. This package is a pre-execution governance artifact. It does not admit the case to IT-G1 and does not authorize execution.

## 1. Case

A Windows EC2 instance is inaccessible / presents an RDP connectivity problem. The candidate transformation is the AWS Systems Manager Automation runbook `AWSSupport-ExecuteEC2Rescue` represented analytically as `ExecuteEC2RescueRemediation`.

## 2. Unit of analysis

One EC2 instance at one explicitly frozen **pre-decision instant** `t`.

The identifiability decision must be made from information available at or before `t`. No post-execution outcome may be used to establish pre-decision accessibility.

## 3. Pre-decision state `S_t`

`S_t` shall contain, to the extent observable and frozen before execution:

- platform / operating-system identity;
- EC2 instance state;
- root-volume identity and encryption state;
- Availability Zone and subnet;
- Systems Manager / SSM management state;
- IAM / execution-role prerequisites relevant to the automation;
- connectivity context relevant to the RDP problem;
- runbook parameters and prerequisites that determine whether the transformation can be invoked.

Each field used for the identifiability decision must have an observable source and a frozen representation.

## 4. Transformation

Analytical transformation identity:

`ExecuteEC2RescueRemediation`

Operational implementation:

`AWSSupport-ExecuteEC2Rescue`

The operational implementation is not itself evidence of accessibility. Accessibility must be established from pre-decision observable conditions.

## 5. Accessibility criterion

The transformation is accessible at `t` only if all conditions required to invoke and execute the selected runbook path are observable and satisfied in `S_t`, including applicable parameter, IAM, SSM, networking/subnet, instance and storage prerequisites.

Any condition whose truth can only be established after execution is excluded from the pre-decision identifiability predicate.

The final Boolean predicate and field-level evidence mapping remain a required item of the completeness review.

## 6. Observation window

The frozen analytical window is:

`pre-decision state → authorized execution → immediate post-execution state`

The post-execution state is retained for transition/reproducibility analysis only. It must not leak backward into the accessibility decision.

## 7. Independent evidence

Required evidence classes:

1. authoritative AWS documentation for `AWSSupport-ExecuteEC2Rescue` and applicable prerequisites;
2. frozen case-specific evidence available at the pre-decision instant.

The package must record stable identifiers, retrieval/freeze metadata and integrity information for the evidence used in the final gate.

## 8. Comparator

The comparator is a manually executed, technically equivalent Windows EC2/RDP troubleshooting route based on the applicable AWS troubleshooting guidance.

The exact manual path, scope and stopping conditions must be frozen before any comparative execution. The comparator must not be retrospectively optimized using knowledge of the automation outcome.

## 9. Effort convention

An effort convention must be frozen before execution. It must define the included activities, start/stop boundaries, personnel/tooling assumptions, and treatment of waiting or automated elapsed time.

No effort result is admitted until this convention is frozen.

## 10. Reproducibility rule

Reproducibility must be assessed by independent reconstructions using the same frozen package and evidence boundary.

The agreement rule, including what constitutes the same identified state, transformation accessibility result and relevant derived measurements, must be frozen before execution.

## Completeness gate

This package is **not yet complete for IT-G1 admission**. The following items remain mandatory for the completeness review:

- field-level operational definition of `S_t`;
- executable pre-decision accessibility predicate;
- frozen AWS evidence identifiers/version or retrieval metadata;
- frozen case-evidence manifest and integrity data;
- exact manual comparator procedure and stopping conditions;
- frozen effort convention;
- explicit independent-reconstruction agreement rule;
- package/evidence integrity manifest.

### Governance decision

Until the completeness review returns `PASS`:

`IT-G1 = NOT STARTED`  
`EXECUTION_AUTHORIZATION = NONE`

No execution, pilot, or outcome-based refinement is authorized by this artifact.
