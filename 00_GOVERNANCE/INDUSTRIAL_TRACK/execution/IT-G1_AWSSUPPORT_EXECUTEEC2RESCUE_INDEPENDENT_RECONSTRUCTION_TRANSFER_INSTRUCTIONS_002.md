# IT-G1 — AWSSupport-ExecuteEC2Rescue
## Independent Reconstruction Transfer Instructions 002

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Control package:** `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_INDEPENDENT_RECONSTRUCTION_CONTROL_PACKAGE_001.md`
**Status:** `TRANSFER-READY — RECONCILED REVISION 002`
**Execution authorization:** `NONE`
**Supersedes for transfer purposes:** `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_INDEPENDENT_RECONSTRUCTION_TRANSFER_INSTRUCTIONS_001.md`

## 1. Purpose

Provide a deterministic transfer procedure for obtaining `R001` and `R002` without cross-contamination between the two reconstructions, using the current reconciled frozen evidence manifest.

## 2. Executor boundary

The two executors must be independent. Each receives the same frozen evidence boundary and this control package, but must not receive the other executor's identity, output, interpretation, or status beyond the fact that a second reconstruction exists.

The executor must not execute:

- the manual comparator;
- `AWSSupport-ExecuteEC2Rescue`;
- any remediation;
- any new AWS observation;
- any action that changes the target state.

## 3. Input package

Transfer exactly these canonical artifacts:

1. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_IDENTIFIABILITY_PACKAGE_001.md`
2. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_EVIDENCE_MANIFEST_FROZEN_002.md`
3. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ACCESSIBILITY_EVALUATION_001.md`
4. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_MANUAL_COMPARATOR_FREEZE_001.md`
5. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_EFFORT_CONVENTION_FREEZE_001.md`
6. `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_INDEPENDENT_RECONSTRUCTION_CONTROL_PACKAGE_001.md`
7. The evidence objects referenced by the reconciled frozen case evidence manifest.

No other IT-G1 result is part of the reconstruction input.

## 4. Executor procedure

### R001

Assign executor identifier `R001` and provide only the input package above. Require the executor to return the exact reconstruction schema defined in the control package, including field classifications and evidence references.

Seal the result as `R001` before any transfer to `R002` occurs.

### R002

Assign executor identifier `R002` and provide the same frozen input package independently. Do not provide the R001 output, any R001 observations, or any comparison hints.

Seal the result as `R002` before comparison.

## 5. Acceptance gate

Only after both outputs are sealed may comparison occur.

Accept only if both independently agree on:

- target identity;
- all decision-critical `S_t0` fields or their `UNKNOWN` classification;
- all nine accessibility predicates;
- `A(t0)`;
- execution authorization status;
- pre-decision versus future transformation distinction;
- `POST_DECISION_INFORMATION_USED=FALSE`.

Any disagreement produces `INDEPENDENT_RECONSTRUCTION_FAIL` and blocks the next gate.

## 6. No-execution condition

The transfer and reconstruction process itself does not authorize either execution path.

Until an independent reconstruction PASS and final integrity/provenance closure are established:

```text
COMPARATOR_EXECUTED = FALSE
AWSSUPPORT_EXECUTEEC2RESCUE_EXECUTED = FALSE
EXECUTION_AUTHORIZATION = NONE
```

## 7. Expected handoff

The next canonical artifact after receiving both sealed outputs shall be a reconstruction comparison/control result. It must state explicitly whether `R001` and `R002` are concordant and whether the case may advance to integrity/provenance closure.

## 8. Reconciliation note

Revision 002 corrects the input-package reference from the historical `CASE_EVIDENCE_MANIFEST_FROZEN_001.md` to the current reconciled `CASE_EVIDENCE_MANIFEST_FROZEN_002.md`.

No evidence object, case state, accessibility result, comparator definition, effort convention, or execution authorization was changed by this revision.

`R001_STATUS = NOT EXECUTED`
`R002_STATUS = NOT EXECUTED`
`INDEPENDENT_RECONSTRUCTION_OK = NOT ESTABLISHED`
`EXECUTION_AUTHORIZATION = NONE`
