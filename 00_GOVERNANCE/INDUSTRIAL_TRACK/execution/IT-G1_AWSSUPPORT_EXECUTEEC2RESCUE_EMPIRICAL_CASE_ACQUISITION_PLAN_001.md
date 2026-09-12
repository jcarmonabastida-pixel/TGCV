# IT-G1 — AWSSupport-ExecuteEC2Rescue — Empirical Case Acquisition Plan 001

**Date:** 2026-09-12  
**Status:** `PREPARATION ONLY — NO AWS MUTATION AUTHORIZED`  
**Case candidate:** `AWSSupport-ExecuteEC2Rescue`  
**Scenario:** `UNREACHABLE EC2 INSTANCE / WINDOWS RDP CONNECTIVITY`

## 1. Purpose

Convert the existing documentary scenario into a genuine empirical IT-G1 case without treating the documentary template as empirical evidence.

This artifact authorizes planning and evidence-structure preparation only. It does **not** authorize creation, modification, stopping, restarting, deletion, or remediation of any AWS resource.

## 2. Current boundary

The existing IT-G1 screening, identifiability package, and evidence-freeze design establish that:

- the candidate transformation is `ExecuteEC2RescueRemediation`;
- the natural unit is one Windows EC2 instance at one frozen pre-decision instant `t0`;
- no concrete `unreachable_instance_id` is currently frozen;
- case-specific evidence is missing;
- `A(t0)` is therefore not established;
- execution authorization remains `NONE`.

The two currently observed `eu-south-2` Linux instances are explicitly excluded from this case.

## 3. Empirical-case acquisition requirement

A future empirical case may be admitted only if a controlled Windows EC2 target exists and all decision-critical pre-execution fields can be independently evidenced and frozen:

`platform, instance_state, root_volume_id, root_volume_encryption, availability_zone, subnet_id, ssm_managed, iam_prerequisites, subnet_ssm_connectivity, unreachable_instance_id, runbook_parameters, rdp_context`.

The case must represent an actual pre-decision accessibility problem, not a retrospectively constructed failure.

## 4. Required sequence

1. Identify or provision, under explicit user control, a Windows EC2 target suitable for the case.
2. Establish the target identity and document the intended case boundary.
3. Establish the pre-decision state `S_t0` and the case-specific evidence manifest.
4. Freeze all decision-critical evidence with timestamps, provenance, and SHA-256 integrity records.
5. Freeze the manual comparator and effort convention before intervention.
6. Evaluate `A(t0)`.
7. Only if all governance gates pass, separately issue execution authorization.
8. Execute the remediation as a controlled experimental operation.
9. Preserve post-execution evidence separately from pre-decision evidence.

## 5. Prohibitions

Until a separate execution authorization exists:

- no `AWSSupport-ExecuteEC2Rescue` execution;
- no stopping or restarting the target;
- no EC2Rescue intervention;
- no modification of networking, IAM, storage, or instance configuration for the purpose of obtaining a desired outcome;
- no use of post-execution observations to establish `A(t0)`.

## 6. Admission rule

`A(t0) = P_platform ∧ P_instance ∧ P_target ∧ P_storage ∧ P_ssm ∧ P_iam ∧ P_network ∧ P_parameters ∧ P_case_evidence`

Any `FALSE` or `UNKNOWN` component keeps the case at `NOT ESTABLISHED` and execution authorization at `NONE`.

## 7. Next operation

The next operation is **case-resource identification/acquisition planning only**. No AWS mutation is implied by this plan. Once a concrete controlled Windows target is identified, the evidence-freeze package shall be populated before any remediation is considered.
