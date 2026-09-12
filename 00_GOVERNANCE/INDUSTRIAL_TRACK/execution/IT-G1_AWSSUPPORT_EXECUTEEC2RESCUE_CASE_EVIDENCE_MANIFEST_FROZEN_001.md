# IT-G1 — AWSSupport-ExecuteEC2Rescue
## Final Frozen Case Evidence Manifest 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Decision stage:** `PRE-DECISION`
**Evidence scope:** `CASE-001 … CASE-012`
**Manifest status:** `FROZEN — PRE-DECISION EVIDENCE`
**Execution authorization:** `NONE`
**Local execution:** `NOT AUTHORIZED`

## 1. Freeze rule

This manifest records the canonical pre-decision evidence representations used for the twelve decision-critical fields defined by the IT-G1 Case Identifiability Package and Evidence Freeze governance.

Git blob SHA values are not used as the evidence integrity value. The SHA-256 values below are the SHA-256 values calculated locally over the exact canonical UTF-8 Markdown files after synchronization with `origin/main`.

No `AWSSupport-ExecuteEC2Rescue` remediation or target modification has been authorized or executed by this manifest.

## 2. Frozen evidence map

| Evidence ID | Decision field | Canonical evidence representation | SHA-256 |
|---|---|---|---|
| CASE-001 | `unreachable_instance_id` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md` | `6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359` |
| CASE-002 | `platform` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md`; `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_MANAGED_NODE_OBSERVED_STATE_001.md` | `6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359`; `EC6901A36B66FD50634AD31A251C888E8920C771B45A4EE3F48243A97959FEC3` |
| CASE-003 | `instance_state` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md` | `6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359` |
| CASE-004 | `root_volume_id` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ROOT_VOLUME_OBSERVED_STATE_001.md` | `E4206B7A1B33944BEA2D38F702E2E6EE463F13F40684DCB2BAB889B75084BA3F` |
| CASE-005 | `root_volume_encryption` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ROOT_VOLUME_ENCRYPTION_OBSERVED_STATE_001.md` | `617F97003B1E940F9A39E75C04E1A9C06ACE5BBC110376143FFED2A215F8231C` |
| CASE-006 | `availability_zone` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md` | `6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359` |
| CASE-007 | `subnet_id` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md` | `6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359` |
| CASE-008 | `ssm_managed` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_MANAGED_NODE_OBSERVED_STATE_001.md` | `EC6901A36B66FD50634AD31A251C888E8920C771B45A4EE3F48243A97959FEC3` |
| CASE-009 | `iam_prerequisites` | IAM/EC2/SSM authorization evidence set: `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CALLER_IAM_SUPPORT_ACTION_AUTHORIZATION_SIMULATION_001.md`; `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CALLER_EC2_MATERIAL_ACTION_AUTHORIZATION_SIMULATION_001.md`; `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CALLER_SSM_EXECUTION_AUTHORIZATION_SIMULATION_001.md`; `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_INSTANCE_ROLE_SSM_POLICY_VERSION_002_OBSERVED_STATE_001.md`; `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RUNBOOK_ASSUMEROLE_AND_NESTED_WORKFLOW_OBSERVED_STATE_001.md` | `C701DE80F96D2913B5AC84099AABC08AF0A3CF3F039A4099D127EC11821D05AF`; `5CFFFA6390764275D4EE52FF527E2944501B6954841ADDD406DA4BE75A5D457E`; `C88058399B575EF98DE42CDA72804B8A46E3FC97F0AFDF8C4EA15A25AA7EE1CB`; `E5C71F383EDEBD46612983596D96C75511A06102FD31B9BDC9BA7BA0FAE130A2`; `08F505295F09E196E1EC203325115DA035F20A13AEE7F92A5C112A2A5AA8D606` |
| CASE-010 | `subnet_ssm_connectivity` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_CONNECTIVITY_OBSERVED_STATE_001.md` | `09C1D188341C899FFA0657658016E01EC3AFC5D07301D051E9B691202F1B2871` |
| CASE-011 | `runbook_parameters` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RUNBOOK_PARAMETER_TUPLE_001.md` | `142EDF5FD735A423C6784CD7CFD8FF38DD4CEF9664312047BEA91761D886F362` |
| CASE-012 | `rdp_context` | `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RDP_SYMPTOM_OBSERVED_STATE_001.md` | `BD7CD1C5D8DCE0747DDCECCD853612EB7570A2EA3F80E65FAE03005545B6B5BB` |

## 3. Integrity basis

The SHA-256 values were obtained from the synchronized local `main` working tree using `Get-FileHash -Algorithm SHA256` over the exact canonical files listed above.

The evidence representation is therefore bound to the canonical repository content at the synchronized working-tree state. Any subsequent modification of an evidence file invalidates the corresponding SHA-256 entry and requires a new manifest revision.

## 4. Freeze determination

`CASE_EVIDENCE_OBJECTS_PRESENT = TRUE`

`CASE_EVIDENCE_SHA256_COMPLETENESS = TRUE`

`CASE_EVIDENCE_MANIFEST_SCHEMA_RECONCILED = TRUE`

`EVIDENCE_FREEZE_COMPLETENESS = PASS`

`A(t0) = NOT YET ESTABLISHED`

The PASS above is limited to the completeness and integrity freeze of the case-specific evidence manifest. It is not a PASS for the accessibility predicate. Evaluation of `A(t0)` remains a separate governed operation requiring the frozen predicate inputs and all applicable authorization/comparator/effort/integrity gates.

## 5. Execution boundary

`IT-G1 = NOT STARTED`

`EXECUTION_AUTHORIZATION = NONE`

`LOCAL_EXECUTION = NOT AUTHORIZED`

`AWSSUPPORT_EXECUTEEC2RESCUE_EXECUTED = FALSE`

This manifest does not authorize, imply, or record execution of the AWS Support Automation.

## 6. Next governed operation

With the case-specific evidence freeze complete, the next admissible operation is the formal evaluation of `A(t0)` against the frozen twelve-field state and the remaining IT-G1 gates. No remediation execution is admissible before that evaluation and the subsequent governed authorization step.
