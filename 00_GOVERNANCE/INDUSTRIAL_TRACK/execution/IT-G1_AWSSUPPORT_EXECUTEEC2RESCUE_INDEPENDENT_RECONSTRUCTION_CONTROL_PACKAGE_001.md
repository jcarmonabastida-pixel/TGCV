# IT-G1 — AWSSupport-ExecuteEC2Rescue
## Independent Reconstruction / Control Package 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Stage:** `PRE-EXECUTION`
**Status:** `FROZEN — CONTROL PACKAGE`
**Execution authorization:** `NONE`
**Purpose:** independent reconstruction of the pre-decision state and accessibility decision before any comparative execution.

## 1. Independence requirement

Two reconstructions are required:

- `R001` — Reconstruction 001
- `R002` — Reconstruction 002

Each reconstruction must be performed independently from the frozen evidence package and this control package.

A reconstruction executor must not use the result of the other reconstruction, any later execution result, any post-decision evidence, or an interpretation derived from the other reconstruction.

## 2. Admitted evidence boundary

Only evidence frozen before the execution decision may be used:

1. the canonical IT-G1 Case Identifiability Package;
2. the canonical IT-G1 frozen Case Evidence Manifest;
3. the individual evidence objects listed by that manifest;
4. the canonical accessibility evaluation artifact;
5. this control package.

No new AWS observation is admitted during reconstruction unless a contradiction in the frozen evidence is discovered. If a contradiction is discovered, reconstruction stops and the contradiction is recorded; it does not silently update the case state.

## 3. Prohibited information

The reconstruction executor must not consult:

- any R001 or R002 result produced by another executor;
- any `AWSSupport-ExecuteEC2Rescue` execution result;
- any manual-comparator execution result;
- any post-decision AWS state;
- any newly collected dataset;
- any later governance interpretation not already part of the admitted evidence boundary.

## 4. Reconstruction task

Independently reconstruct the state at `t0` and determine:

### 4.1 Target identity

Confirm the frozen identity of the case target:

`i-0b0bf56b94733718c` in `eu-south-2`.

### 4.2 Decision-critical state

Reconstruct, without inference beyond the frozen evidence:

- platform;
- instance state;
- root volume identity and encryption state;
- Availability Zone;
- subnet;
- SSM managed/online state;
- IAM prerequisites;
- SSM network connectivity;
- unreachable-instance identity;
- frozen runbook parameter tuple;
- observed RDP symptom.

Every field must be classified as `EXPLICIT`, `UNKNOWN`, or `CONTRADICTED`.

### 4.3 Accessibility predicates

Independently evaluate:

`A(t0) = P_platform ∧ P_instance ∧ P_target ∧ P_storage ∧ P_ssm ∧ P_iam ∧ P_network ∧ P_parameters ∧ P_case_evidence`

No predicate may be promoted from UNKNOWN to TRUE by assumption.

### 4.4 Transformation identity

The reconstruction must distinguish:

- the observed pre-decision state;
- the manual comparator transformation, if later executed;
- the `AWSSupport-ExecuteEC2Rescue` transformation, if later executed.

The reconstruction must not infer a successful transformation merely because the automation is accessible or authorized.

## 5. Agreement criteria

`R001` and `R002` are considered concordant only if both independently agree on:

1. target identity;
2. every decision-critical `S_t0` field, or explicitly agree that the field is UNKNOWN;
3. every accessibility predicate;
4. the resulting `A(t0)` value;
5. execution authorization status;
6. the distinction between pre-decision state and future transformation;
7. the absence of post-decision information in the reconstruction.

Any disagreement is a control failure and requires adjudication before execution authorization.

## 6. Reconstruction output schema

Each executor must produce a reconstruction record containing:

```text
RECONSTRUCTION_ID=
EXECUTOR_ID=
CASE_ID=IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE
TARGET_ID=i-0b0bf56b94733718c
REGION=eu-south-2
STATE_RECONSTRUCTION=
P_PLATFORM=
P_INSTANCE=
P_TARGET=
P_STORAGE=
P_SSM=
P_IAM=
P_NETWORK=
P_PARAMETERS=
P_CASE_EVIDENCE=
A_T0=
EXECUTION_AUTHORIZATION=
POST_DECISION_INFORMATION_USED=FALSE
CONTRADICTION_DETECTED=
RECONSTRUCTION_RESULT=
```

The full evidence references supporting each field must accompany the record.

## 7. Control sequence

1. Freeze this package.
2. Transfer the package to `R001` without transmitting any R002 result.
3. Receive and seal R001 output.
4. Independently transfer the same admitted evidence boundary to `R002`.
5. Receive and seal R002 output.
6. Compare R001/R002 only after both are sealed.
7. If concordant, record `INDEPENDENT_RECONSTRUCTION_PASS`.
8. If discordant, record `INDEPENDENT_RECONSTRUCTION_FAIL` and stop.

No comparative execution is permitted between steps 3 and 7.

## 8. Relationship to execution authorization

This package does not authorize execution.

Even if both reconstructions independently return `A(t0)=TRUE`, execution remains prohibited until the final integrity/provenance manifest is complete and the explicit execution authorization gate is separately satisfied.

## 9. Current control state

```text
A(t0)                         = TRUE (canonical pre-decision evaluation)
COMPARATOR_FROZEN             = TRUE
EFFORT_CONVENTION_FROZEN      = TRUE
R001_STATUS                   = NOT EXECUTED
R002_STATUS                   = NOT EXECUTED
INDEPENDENT_RECONSTRUCTION    = PENDING
INDEPENDENT_RECONSTRUCTION_OK = NOT ESTABLISHED
INTEGRITY_MANIFEST            = PENDING
EXECUTION_AUTHORIZATION       = NONE
COMPARATOR_EXECUTED           = FALSE
AWSSUPPORT_EXECUTEEC2RESCUE_EXECUTED = FALSE
```

## 10. Authoritative-method note

AWS documents `AWSSupport-ExecuteEC2Rescue` as an automation that can stop the target instance, create a backup AMI, attach the root volume to a helper instance, run EC2Rescue, reattach the volume, restore the instance state, and clean up the temporary infrastructure. AWS also states that encrypted root volumes are unsupported and that a non-Elastic public IP can change when the instance is stopped. These are method-specific transformation effects and must not be conflated with the pre-decision accessibility predicate.
