# IT-G1 — Case Identifiability Package

**Case:** `AWSSupport-ExecuteEC2Rescue`  
**Candidate:** `RETAINED CONDITIONALLY`  
**IT-G1:** `NOT STARTED`  
**Execution authorization:** `NONE`  
**Package status:** `PERSISTED — COMPLETENESS REVIEW IN PROGRESS`

## Purpose

Freeze the identifiability design for one inaccessible Windows EC2 instance at one pre-decision instant. This artifact is a governance package, not an execution authorization.

## 1. Unit and frozen instant

**Unit:** one EC2 instance + one pre-decision instant `t0`.

The identifiability decision may use only evidence available at or before `t0`. Post-execution observations are prohibited from the accessibility decision.

## 2. Operational state `S_t0`

The following fields are mandatory and must be represented as explicit values or `UNKNOWN`, with source and freeze timestamp:

| Field | Operational value | Required source | Decision relevance |
|---|---|---|---|
| `platform` | Windows / other / UNKNOWN | EC2 instance metadata or frozen case evidence | transformation applicability |
| `instance_state` | running / stopped / stopping / pending / terminated / UNKNOWN | EC2 state evidence | invocation/path applicability |
| `root_volume_id` | concrete volume ID / UNKNOWN | EC2/EBS evidence | rescue target identity |
| `root_volume_encryption` | encrypted / unencrypted / UNKNOWN | EBS evidence | runbook support constraint |
| `availability_zone` | concrete AZ / UNKNOWN | EC2 metadata | subnet compatibility |
| `subnet_id` | concrete subnet ID / UNKNOWN | EC2 metadata | helper-instance/network path |
| `ssm_managed` | true / false / UNKNOWN | SSM managed-node evidence | Systems Manager path |
| `iam_prerequisites` | satisfied / unsatisfied / UNKNOWN | frozen IAM/role evidence | automation authorization |
| `subnet_ssm_connectivity` | satisfied / unsatisfied / UNKNOWN | frozen networking evidence | helper/SSM execution path |
| `unreachable_instance_id` | concrete instance ID / UNKNOWN | frozen case evidence | target identity |
| `runbook_parameters` | frozen parameter tuple / UNKNOWN | package/evidence record | exact transformation identity |
| `rdp_context` | frozen observed RDP symptom/context | frozen case evidence | case characterization |

### State sufficiency rule

A state field is **decision-usable** only when its value is directly observable from a named source frozen at or before `t0`. `UNKNOWN` is not silently converted to a favorable value.

## 3. Transformation identity

**Analytical transformation:** `ExecuteEC2RescueRemediation`  
**Operational implementation:** `AWSSupport-ExecuteEC2Rescue`

The implementation name alone does not establish accessibility.

## 4. Pre-decision accessibility predicate

Define:

`A(t0) = P_platform ∧ P_instance ∧ P_target ∧ P_storage ∧ P_ssm ∧ P_iam ∧ P_network ∧ P_parameters ∧ P_case_evidence`

where each predicate is evaluated exclusively from the frozen `S_t0` and admitted evidence:

- `P_platform`: target is a supported Windows EC2 case;
- `P_instance`: required EC2 state/path prerequisites are satisfied;
- `P_target`: target instance identity and required rescue target are unambiguous;
- `P_storage`: root-volume condition satisfies the selected runbook path, including the documented encryption constraint;
- `P_ssm`: required Systems Manager prerequisites are satisfied;
- `P_iam`: required automation/IAM prerequisites are satisfied;
- `P_network`: required subnet/AZ and SSM connectivity prerequisites are satisfied;
- `P_parameters`: all required runbook parameters are frozen and valid;
- `P_case_evidence`: the case evidence is sufficient to establish the preceding predicates without post-execution information.

**Accessibility = TRUE iff `A(t0)=TRUE`.**

If any predicate is `FALSE` or `UNKNOWN`, accessibility is not established and execution authorization remains `NONE`.

## 5. Evidence freeze

The completeness gate requires two evidence classes:

1. **Authoritative AWS evidence:** fixed document identifiers/URLs plus retrieval/freeze date and, where available, document version or stable revision identifier.
2. **Case-specific evidence:** a manifest of the exact pre-decision evidence items, each with source identifier, timestamp and integrity hash.

The evidence manifest is not yet admitted by this package revision and must be persisted before `PACKAGE_COMPLETENESS=PASS`.

## 6. Comparator freeze

The comparator shall be one fixed manual troubleshooting route for the same case, selected before execution and based on the applicable AWS Windows/RDP troubleshooting guidance.

The frozen comparator record must specify:

- ordered diagnostic/repair steps;
- permitted observations;
- stopping/success/failure conditions;
- excluded alternative branches;
- equivalence boundary with `ExecuteEC2RescueRemediation`.

No comparative execution may begin before this record is persisted.

## 7. Effort convention

Effort is measured from a frozen **start event** (operator begins the prescribed procedure) to a frozen **stop event** (procedure reaches a predefined success/failure/stop condition).

The record must separately report:

- active operator effort;
- elapsed wall-clock time;
- automation/waiting time.

No retrospective adjustment is permitted using knowledge of outcomes.

## 8. Independent reconstruction rule

Two reconstructions are in agreement only if, using the same frozen package and evidence boundary, both independently produce:

1. the same target identity;
2. the same operational `S_t0` values for all decision-critical fields, or the same explicit `UNKNOWN` values;
3. the same accessibility result `A(t0)`;
4. the same transformation identity;
5. no use of post-decision information to establish accessibility.

Any disagreement on a decision-critical field or on `A(t0)` is `REPRODUCIBILITY=FAIL` pending adjudication under a separately frozen rule.

## 9. Integrity / provenance

Before completeness PASS, persist an integrity manifest containing at minimum:

- package path and package SHA/blob SHA;
- evidence manifest entries and hashes;
- comparator artifact identifier and hash;
- effort-convention artifact identifier and hash;
- reconstruction-rule identifier and hash;
- canonical Git commit containing the complete package set.

## 10. Completeness gate — current status

`PACKAGE_COMPLETENESS = FAIL / INCOMPLETE`

Remaining mandatory persistence items:

- frozen authoritative AWS evidence manifest;
- frozen case-specific evidence manifest;
- exact manual comparator artifact;
- final effort-convention artifact;
- final reconstruction-control artifact;
- integrity/provenance manifest over the complete package set.

### Governance decision

Until all mandatory items are persisted and independently checked:

`IT-G1 = NOT STARTED`  
`EXECUTION_AUTHORIZATION = NONE`  
`LOCAL_EXECUTION = NOT AUTHORIZED`

No pilot or outcome-based refinement is authorized by this package.