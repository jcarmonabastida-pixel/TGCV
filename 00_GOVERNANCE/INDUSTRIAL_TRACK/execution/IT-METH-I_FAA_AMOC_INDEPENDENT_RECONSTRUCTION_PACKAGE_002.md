# IT-METH-I — FAA AMOC Independent Reconstruction Package 002

**Date:** 2026-09-09  
**Status:** READY — INDEPENDENT RECONSTRUCTION PACKAGE 002  
**Case:** `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`  
**Methodological action:** `IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_ACTION_001.md`  
**Frozen protocol:** `IT-G4_I_FAA_AMOC_UTILITY_PROTOCOL_FREEZE_001.md`

## 1. Purpose

Provide a self-contained package for a second, genuinely independent reconstruction of the frozen FAA AMOC case.

This package is deliberately limited to the information necessary to reconstruct the mandatory worksheet. It does not reproduce, expose, or rely upon reconstruction 001 answers, scores, interpretations, or effort measurements.

## 2. Independence rule

The executor of reconstruction 002 must complete the worksheet before seeing reconstruction 001.

The following are prohibited before completion:

- consulting the IT-G4-I execution result 001;
- copying or adapting any field-level answer from reconstruction 001;
- comparing scores against reconstruction 001;
- using reconstruction 001's interpretation of TGCV or the comparator;
- using reconstruction 001's effort measurement.

After reconstruction 002 is frozen, a separate comparison operation may compare the two reconstructions.

## 3. Frozen case identity

Reconstruct only this case:

- AD: `US-91-12-10 — Wings — Spar Attachment — Modification`.
- AMOC reference: `7K0-18-00734`.
- FAA approval date: `2018-02-23`.
- Approval holder: `Textron Aviation Inc.`.
- Affected type-designation context: `Super King Air 200/B200/B200C/B200T and 300/300LW`.
- Use the serial-number applicability stated in the FAA approval letter.

## 4. Frozen evidence boundary

Use only the evidence package already admitted through IT-G1–IT-G4:

1. public EASA Safety Publications Tool record for `US-91-12-10`;
2. the attached FAA AMOC approval letter, reference `7K0-18-00734`;
3. FAA AC 39-10, issued `2016-09-14`;
4. the case-specific 2018 approval-process context already admitted at G1–G4.

Do not introduce later operational outcomes, safety events, maintenance costs, downtime, financial results, fleet performance, partner evidence, proprietary evidence, or a new dataset.

## 5. Required reconstruction worksheet

Complete the following fields independently for the TGCV condition and for the conventional comparator:

1. Case identity.
2. System/product boundary.
3. Decision-time state/context.
4. Baseline AD requirement.
5. Alternative method.
6. Enabling conditions.
7. Limiting conditions.
8. Applicability restrictions.
9. Temporal conditions.
10. Evidence source for each field.
11. Indeterminate fields, if any.
12. Resulting accessibility classification.

For every field, distinguish documentary support from inference. Unsupported inference must not be silently converted into a supported value.

## 6. TGCV condition

Construct the bounded TGCV representation from the frozen case and evidence boundary.

The reconstruction should identify the decision-defined accessibility conditions and the accessible transformation represented by the approved AMOC, without using post-decision outcomes.

Do not evaluate comparative superiority.

## 7. Conventional comparator condition

Construct the conventional regulatory/engineering representation from the same frozen evidence boundary.

Use the AD-prescribed compliance requirement and documented alternative without invoking TGCV constructs.

Do not evaluate comparative superiority.

## 8. Effort measurement

Record:

- start timestamp;
- completion timestamp;
- elapsed effort according to the frozen IT-G4 measurement convention.

The executor must use the same start/stop definition that will be applied to the other reconstruction. No comparison is made during this package execution.

## 9. Output requirements

The completed artifact must be stored separately as:

`IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_002.md`

It must contain the completed TGCV and comparator worksheets and the effort measurement, but no comparison against reconstruction 001.

The artifact must state that it was produced under `IT-METH-I` and that independence was maintained until completion.

## 10. Post-completion routing

After reconstruction 002 is complete and immutable:

1. preserve reconstruction 001 unchanged;
2. preserve reconstruction 002 unchanged;
3. create a separately governed comparison record;
4. calculate field-by-field reproducibility only from the two frozen reconstructions;
5. evaluate analytical effort only under the frozen IT-G4 definition;
6. apply the existing IT-G4 decision rule without changing thresholds or comparator.

No result may be upgraded merely because reconstruction 002 exists.

## 11. Authorization boundary

This package authorizes preparation of the independent reconstruction artifact only within the scope of `IT-METH-I`.

It does not authorize modification of IT-G4, modification of execution result 001, post-decision outcome analysis, causal inference, financial/value claims, Core modification, or execution of another industrial case.

**Package status: READY FOR INDEPENDENT RECONSTRUCTION 002.**
