# IT-METH-I — FAA AMOC Blind Execution Package 001

**Status:** `CONTROLLED PACKAGE — READY FOR TRANSFER TO EXECUTOR-2`

**Case:** `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`

**Purpose:** provide a transfer-ready, blind execution container for reconstruction 002 while keeping reconstruction 001 outside the executor's information boundary.

## 1. Blindness objective

This package is designed so that EXECUTOR-2 can perform reconstruction 002 without access to:

- reconstruction 001;
- reconstruction 001 scores or answers;
- reconstruction 001 interpretation;
- reconstruction 001 effort measurement;
- any comparison between reconstructions 001 and 002.

The package does not contain any of those materials.

## 2. Package contents

The executor receives exactly the following controlled inputs:

1. this package;
2. the frozen evidence bundle identified in Section 4;
3. the reconstruction worksheet in Section 5, or an equivalent separately sealed worksheet generated from this package without changing its fields or rules.

No other TGCV execution result or comparison material may be provided before sealing.

## 3. Roles and information boundary

### EXECUTOR-2

Performs the reconstruction and records the result. EXECUTOR-2 must not have performed reconstruction 001 and must not have access to it before sealing reconstruction 002.

### CUSTODIAN

Transfers the frozen inputs, verifies package integrity, controls access to reconstruction 001, records timestamps, and receives the sealed result. The custodian must not coach EXECUTOR-2 toward agreement with reconstruction 001.

### COMPARATOR

Does not participate in reconstruction 002. Comparison starts only after the sealed 002 artifact is accepted by the custodian.

## 4. Frozen evidence bundle

The evidence boundary is inherited unchanged from the already frozen IT-METH-I package 002:

1. public EASA Safety Publications Tool record for `US-91-12-10`;
2. FAA AMOC approval letter, reference `7K0-18-00734`;
3. FAA AC 39-10, issued `2016-09-14`;
4. case-specific 2018 approval-process context admitted at IT-G1–IT-G4.

The custodian must provide the same frozen evidence set used by package 002 and record its integrity hash before transfer.

**No later operational outcome, safety event, maintenance cost, downtime, financial result, fleet-performance result, partner evidence, proprietary evidence, or new dataset may be supplied.**

## 5. Blind reconstruction worksheet

EXECUTOR-2 shall independently complete the following fields for both the TGCV condition and the conventional comparator.

| # | Field | TGCV condition | Conventional comparator | Evidence reference | Support / inference | Indeterminate? |
|---|---|---|---|---|---|---|
| 1 | Case identity | | | | | |
| 2 | System/product boundary | | | | | |
| 3 | Decision-time state/context | | | | | |
| 4 | Baseline AD requirement | | | | | |
| 5 | Alternative method | | | | | |
| 6 | Enabling conditions | | | | | |
| 7 | Limiting conditions | | | | | |
| 8 | Applicability restrictions | | | | | |
| 9 | Temporal conditions | | | | | |
| 10 | Resulting accessibility classification | | | | | |

For every entry:

- cite the evidence used;
- distinguish documentary support from inference;
- record uncertainty explicitly;
- do not infer missing technical conditions from the later outcome;
- do not consult reconstruction 001.

## 6. Case identification supplied to executor

Reconstruct only the following frozen case:

- AD: `US-91-12-10 — Wings — Spar Attachment — Modification`.
- AMOC reference: `7K0-18-00734`.
- FAA approval date: `2018-02-23`.
- Approval holder: `Textron Aviation Inc.`.
- Affected type-designation context: `Super King Air 200/B200/B200C/B200T and 300/300LW`.
- Use the serial-number applicability stated in the FAA approval letter.

These identifiers are case-routing information, not reconstruction results.

## 7. TGCV-side instruction

Construct the bounded TGCV representation from the frozen evidence only.

Identify the decision-defined accessibility conditions and the accessible transformation represented by the approved AMOC.

Do not use post-decision outcomes and do not evaluate comparative superiority.

## 8. Comparator-side instruction

Construct the conventional regulatory/engineering representation from the same frozen evidence boundary.

Use the AD-prescribed compliance requirement and documented alternative without importing TGCV constructs.

Do not evaluate comparative superiority.

## 9. Effort record

EXECUTOR-2 shall record:

- execution start timestamp;
- execution completion timestamp;
- elapsed effort under the frozen IT-G4 convention.

No comparison with reconstruction 001 is permitted while recording effort.

## 10. Seal protocol

At completion EXECUTOR-2 shall:

1. finish all worksheet fields;
2. identify all indeterminate fields;
3. confirm no access to reconstruction 001 occurred before completion;
4. record completion timestamp;
5. produce the reconstruction-002 artifact;
6. calculate and record the artifact integrity hash;
7. transfer the sealed artifact to the custodian.

After step 7, the custodian may release reconstruction 001 for a separate comparison operation.

## 11. Mandatory independence declaration

The sealed artifact must include the following machine-checkable statements:

`EXECUTOR_2_DISTINCT_FROM_EXECUTOR_1 = [PASS/FAIL]`

`RECONSTRUCTION_001_WITHHELD_UNTIL_SEAL = [PASS/FAIL]`

`FROZEN_INPUT_BOUNDARY_MAINTAINED = [PASS/FAIL]`

`COMPARISON_WITH_001_BEFORE_SEAL = [YES/NO]`

`INDEPENDENCE_STATUS = [PASS/FAIL]`

If any mandatory condition fails, `INDEPENDENCE_STATUS` must be `FAIL`.

## 12. Custodian control record

Before transfer:

- Package ID: `IT-METH-I-AMOC-BLIND-EXEC-001`
- Case ID: `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`
- Package version: `v0.1`
- Frozen evidence hash: `[TO BE RECORDED AT TRANSFER]`
- Executor-2 identity/control reference: `[TO BE RECORDED]`
- Transfer timestamp: `[TO BE RECORDED]`
- Execution context reference: `[TO BE RECORDED]`
- Reconstruction-001 access state: `WITHHELD`

After sealing:

- Execution start timestamp: `[TO BE RECORDED]`
- Seal timestamp: `[TO BE RECORDED]`
- Reconstruction-002 artifact hash: `[TO BE RECORDED]`
- Reconstruction-001 release timestamp: `[TO BE RECORDED ONLY AFTER SEAL]`
- Protocol deviations: `[NONE / DETAIL]`

## 13. Hard exclusions

The following invalidate the blind execution:

- EXECUTOR-2 sees reconstruction 001 before sealing;
- EXECUTOR-2 receives reconstruction 001 scores or interpretation before sealing;
- the frozen evidence boundary is changed without a new governed freeze;
- later outcomes are introduced into the reconstruction;
- the custodian coaches the executor using reconstruction 001;
- reconstruction 002 is altered after sealing;
- comparison is performed before sealing;
- the same executor performs both reconstructions.

## 14. Downstream routing

This package ends at the sealed reconstruction-002 artifact.

Only after sealing may a separate governed comparison operation evaluate:

- field-level reproducibility;
- analytical effort under the frozen IT-G4 definition;
- the existing IT-G4 decision rule.

This package does not itself establish utility, superiority, causality, value, prediction, scientific validation, or a change to the TGCV Core.

## 15. Current status

`BLIND_PACKAGE_STATUS = READY`

`EXECUTOR_2_STATUS = NOT_YET_ASSIGNED`

`INDEPENDENCE_STATUS = NOT_YET_DEMONSTRATED`

`RECONSTRUCTION_002_STATUS = NOT_EXECUTED`
