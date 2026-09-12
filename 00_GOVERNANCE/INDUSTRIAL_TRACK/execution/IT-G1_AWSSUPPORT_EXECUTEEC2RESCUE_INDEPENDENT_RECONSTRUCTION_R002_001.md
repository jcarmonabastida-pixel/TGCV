# IT-G1 — AWSSupport-ExecuteEC2Rescue
## Independent Reconstruction R002 — Sealed Record 001

**RECONSTRUCTION_ID:** `IT-G1-R002`
**EXECUTOR_ID:** `R002`
**CASE_ID:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Stage:** `PRE-EXECUTION`
**Status:** `SEALED — R002`
**Execution authorization:** `NONE`

## 1. Admitted evidence boundary

This reconstruction uses only the pre-decision evidence boundary specified by `INDEPENDENT_RECONSTRUCTION_TRANSFER_INSTRUCTIONS_002` and `INDEPENDENT_RECONSTRUCTION_CONTROL_PACKAGE_001`:

1. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_IDENTIFIABILITY_PACKAGE_001.md`
2. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_EVIDENCE_MANIFEST_FROZEN_002.md`
3. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ACCESSIBILITY_EVALUATION_001.md`
4. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_MANUAL_COMPARATOR_FREEZE_001.md`
5. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_EFFORT_CONVENTION_FREEZE_001.md`
6. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_INDEPENDENT_RECONSTRUCTION_CONTROL_PACKAGE_001.md`
7. The evidence objects referenced by `CASE_EVIDENCE_MANIFEST_FROZEN_002.md`.

No execution result, comparator execution result, post-decision state, new AWS observation, new dataset, or later governance interpretation was used.

## 2. Reconstruction record

```text
RECONSTRUCTION_ID=IT-G1-R002
EXECUTOR_ID=R002
CASE_ID=IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE
TARGET_ID=i-0b0bf56b94733718c
REGION=eu-south-2
STATE_RECONSTRUCTION=EXPLICIT PRE-DECISION STATE RECONSTRUCTED FROM FROZEN EVIDENCE
P_PLATFORM=TRUE
P_INSTANCE=TRUE
P_TARGET=TRUE
P_STORAGE=TRUE
P_SSM=TRUE
P_IAM=TRUE
P_NETWORK=TRUE
P_PARAMETERS=TRUE
P_CASE_EVIDENCE=TRUE
A_T0=TRUE
EXECUTION_AUTHORIZATION=NONE
POST_DECISION_INFORMATION_USED=FALSE
CONTRADICTION_DETECTED=FALSE
RECONSTRUCTION_RESULT=PASS
```

## 3. Decision-critical state

| Field | Classification | Reconstructed value | Primary frozen basis |
|---|---|---|---|
| `platform` | `EXPLICIT` | Windows Server 2025 Datacenter | `CASE-002`; SSM managed-node observed state |
| `instance_state` | `EXPLICIT` | `running` | `CASE-003`; case resource freeze |
| `root_volume_id` | `EXPLICIT` | `vol-003ff62dff6e449a4` | `CASE-004`; root-volume observed state |
| `root_volume_encryption` | `EXPLICIT` | `unencrypted` | `CASE-005`; root-volume encryption observed state |
| `availability_zone` | `EXPLICIT` | `eu-south-2b` | `CASE-006`; case resource freeze and root-volume evidence |
| `subnet_id` | `EXPLICIT` | `subnet-02b90b9a7f2a2966a` | `CASE-007`; case resource freeze |
| `ssm_managed` | `EXPLICIT` | `true / Online` | `CASE-008`; SSM managed-node observed state |
| `iam_prerequisites` | `EXPLICIT` | satisfied for evaluated automation action surface | `CASE-009`; frozen IAM/role/runbook authorization evidence and accessibility evaluation |
| `subnet_ssm_connectivity` | `EXPLICIT` | satisfied | `CASE-010`; SSM connectivity evidence and accessibility evaluation |
| `unreachable_instance_id` | `EXPLICIT` | `i-0b0bf56b94733718c` | `CASE-001`; case resource freeze |
| `runbook_parameters` | `EXPLICIT` | frozen valid parameter tuple including required `UnreachableInstanceId` | `CASE-011`; runbook parameter tuple and accessibility evaluation |
| `rdp_context` | `EXPLICIT` | TCP/3389 unreachable from operator observation point; `TermService` stopped; no TCP/3389 listener output | `CASE-012`; RDP symptom observed state |

No decision-critical field was promoted from `UNKNOWN` by assumption.

## 4. Accessibility reconstruction

The governing predicate is:

`A(t0) = P_platform ∧ P_instance ∧ P_target ∧ P_storage ∧ P_ssm ∧ P_iam ∧ P_network ∧ P_parameters ∧ P_case_evidence`

The nine predicates independently evaluate to TRUE from the frozen evidence boundary:

```text
P_platform=TRUE
P_instance=TRUE
P_target=TRUE
P_storage=TRUE
P_ssm=TRUE
P_iam=TRUE
P_network=TRUE
P_parameters=TRUE
P_case_evidence=TRUE
A_T0=TRUE
```

The result establishes pre-decision accessibility of the analytical transformation `ExecuteEC2RescueRemediation` through `AWSSupport-ExecuteEC2Rescue`. It does not establish execution, success, benefit, or authorization.

## 5. Transformation identity boundary

The reconstructed state is the frozen pre-decision state at `t0`.

- The manual comparator is a separate future diagnostic/repair transformation and is not executed.
- `AWSSupport-ExecuteEC2Rescue` is the operational implementation of `ExecuteEC2RescueRemediation` and is not executed.
- Accessibility of the transformation does not imply successful transformation.

## 6. Evidence references

- Case identity and state model: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_IDENTIFIABILITY_PACKAGE_001.md`
- Reconciled evidence membership and SHA-256 map: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_EVIDENCE_MANIFEST_FROZEN_002.md`
- Resource identity, instance state, AZ, subnet: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md`
- Platform and SSM managed/online state: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_MANAGED_NODE_OBSERVED_STATE_001.md`
- Root volume identity: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ROOT_VOLUME_OBSERVED_STATE_001.md`
- Root volume encryption: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ROOT_VOLUME_ENCRYPTION_OBSERVED_STATE_001.md`
- IAM/automation prerequisites: the five CASE-009 evidence objects listed by `CASE_EVIDENCE_MANIFEST_FROZEN_002.md`
- SSM network connectivity: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_CONNECTIVITY_OBSERVED_STATE_001.md`
- Runbook parameter tuple: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RUNBOOK_PARAMETER_TUPLE_001.md`
- RDP context: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RDP_SYMPTOM_OBSERVED_STATE_001.md`
- Predicate evaluation: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ACCESSIBILITY_EVALUATION_001.md`

## 7. Seal

`R002_STATUS=SEALED`
`INDEPENDENT_RECONSTRUCTION_OK=NOT ESTABLISHED`
`EXECUTION_AUTHORIZATION=NONE`
`COMPARATOR_EXECUTED=FALSE`
`AWSSUPPORT_EXECUTEEC2RESCUE_EXECUTED=FALSE`

This record is sealed as the R002 output. Comparison with the other sealed reconstruction is a separate subsequent control operation.
