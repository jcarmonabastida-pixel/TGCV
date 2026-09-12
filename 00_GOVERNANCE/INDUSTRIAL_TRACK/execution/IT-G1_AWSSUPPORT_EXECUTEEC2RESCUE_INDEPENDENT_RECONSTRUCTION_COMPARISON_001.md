# IT-G1 — AWSSupport-ExecuteEC2Rescue
## Independent Reconstruction Comparison 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Stage:** `PRE-EXECUTION`
**Status:** `SEALED — CONCORDANT INDEPENDENT RECONSTRUCTIONS`
**Execution authorization:** `NONE`
**Execution performed:** `FALSE`

## 1. Compared canonical records

- R001: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_INDEPENDENT_RECONSTRUCTION_R001_001.md`
  - Blob SHA: `9d1cbafbe9faf6093fe403b83a3c34d4b0631f09`
- R002: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_INDEPENDENT_RECONSTRUCTION_R002_001.md`
  - Blob SHA: `0611f1d88406ebd20d58ba347214eec783c99e7e`

Both records were independently sealed before this comparison. The comparison admits no execution result or post-decision information.

## 2. Agreement matrix

| Criterion | R001 | R002 | Agreement |
|---|---|---|---|
| Target identity | `i-0b0bf56b94733718c` | `i-0b0bf56b94733718c` | `TRUE` |
| Region | `eu-south-2` | `eu-south-2` | `TRUE` |
| `platform` | EXPLICIT — Windows Server 2025 Datacenter | EXPLICIT — Windows Server 2025 Datacenter | `TRUE` |
| `instance_state` | EXPLICIT — running | EXPLICIT — running | `TRUE` |
| `root_volume_id` | EXPLICIT — `vol-003ff62dff6e449a4` | EXPLICIT — `vol-003ff62dff6e449a4` | `TRUE` |
| `root_volume_encryption` | EXPLICIT — unencrypted | EXPLICIT — unencrypted | `TRUE` |
| `availability_zone` | EXPLICIT — `eu-south-2b` | EXPLICIT — `eu-south-2b` | `TRUE` |
| `subnet_id` | EXPLICIT — `subnet-02b90b9a7f2a2966a` | EXPLICIT — `subnet-02b90b9a7f2a2966a` | `TRUE` |
| `ssm_managed` | EXPLICIT — true / Online | EXPLICIT — true / Online | `TRUE` |
| `iam_prerequisites` | EXPLICIT — satisfied | EXPLICIT — satisfied | `TRUE` |
| `subnet_ssm_connectivity` | EXPLICIT — satisfied | EXPLICIT — satisfied | `TRUE` |
| `unreachable_instance_id` | EXPLICIT — target ID | EXPLICIT — target ID | `TRUE` |
| `runbook_parameters` | EXPLICIT — frozen valid tuple | EXPLICIT — frozen valid tuple | `TRUE` |
| `rdp_context` | EXPLICIT — TCP/3389 failed; TermService stopped; no listener | EXPLICIT — TCP/3389 failed; TermService stopped; no listener | `TRUE` |
| `P_platform` | TRUE | TRUE | `TRUE` |
| `P_instance` | TRUE | TRUE | `TRUE` |
| `P_target` | TRUE | TRUE | `TRUE` |
| `P_storage` | TRUE | TRUE | `TRUE` |
| `P_ssm` | TRUE | TRUE | `TRUE` |
| `P_iam` | TRUE | TRUE | `TRUE` |
| `P_network` | TRUE | TRUE | `TRUE` |
| `P_parameters` | TRUE | TRUE | `TRUE` |
| `P_case_evidence` | TRUE | TRUE | `TRUE` |
| `A(t0)` | TRUE | TRUE | `TRUE` |
| Transformation identity | `ExecuteEC2RescueRemediation` / `AWSSupport-ExecuteEC2Rescue` | same | `TRUE` |
| Post-decision information used | FALSE | FALSE | `TRUE` |
| Contradiction detected | FALSE | FALSE | `TRUE` |
| Execution authorization | NONE | NONE | `TRUE` |

## 3. Independent reconstruction result

All mandatory agreement criteria are concordant.

```text
TARGET_AGREEMENT=TRUE
STATE_AGREEMENT=TRUE
PREDICATE_AGREEMENT=TRUE
A_T0_AGREEMENT=TRUE
TRANSFORMATION_IDENTITY_AGREEMENT=TRUE
POST_DECISION_INFORMATION_EXCLUDED=TRUE
CONTRADICTION_DETECTED=FALSE
REPRODUCIBILITY=PASS
INDEPENDENT_RECONSTRUCTION_OK=TRUE
```

The independent reconstruction gate is therefore closed with `PASS`.

## 4. Governance boundary after comparison

The PASS establishes reproducibility of the pre-decision accessibility reconstruction. It does **not** authorize execution and does not establish expected or realized remediation benefit.

The following remain unchanged:

`EXECUTION_AUTHORIZATION=NONE`

`COMPARATOR_EXECUTED=FALSE`

`AWSSUPPORT_EXECUTEEC2RESCUE_EXECUTED=FALSE`

`LOCAL_EXECUTION=NOT AUTHORIZED`

No AWS remediation or target modification was performed by this comparison operation.

## 5. Next gate

The next governed operation is final integrity/provenance closure over the complete IT-G1 pre-execution package. Execution authorization remains prohibited until that closure and the explicit authorization decision are completed.
