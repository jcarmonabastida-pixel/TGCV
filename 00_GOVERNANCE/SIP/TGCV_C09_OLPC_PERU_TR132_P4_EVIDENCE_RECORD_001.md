# TGCV — C09 OLPC Peru TR-132 P4 Evidence Record 001

**Status:** `CLOSED — P4 PASS — BOUNDED TRANSFORMATIONAL-SPACE OPERATIONALISATION`
**Date:** 2026-09-14
**Candidate:** Beuermann, Cristia, Cueto, Malamud & Cruz-Aguayo — *One Laptop per Child at Home: Short-Term Impacts from a Randomized Experiment in Peru*
**Data package:** openICPSR 113587 V2
**Gate:** TR-132 P4 — bounded `U*`, `T_acc,0`, `T_acc,1`

## 1. Decision

**P4 = PASS — bounded transformational-space operationalisation.**

The audit does not claim reconstruction of the student's complete global transformation space. It establishes a finite, reproducible and study-bounded operationalisation restricted to transformations that the public OLPC study can observe or reconstruct.

## 2. Recovered operational definition

### `U*`

`U*` = domestic transformations dependent on having a computer/laptop in the home, within the classes of computer-related activity explicitly represented by the OLPC instruments.

The universe is deliberately bounded to the study-observable/reconstructible domain.

Excluded from `U*` as accessibility components:
- academic performance;
- cognitive skills;
- acquired XO skills;
- realized post-treatment use;
- economic or educational outcomes.

These remain trajectory/capability/outcome layers.

### `T_acc,0`

`T_acc,0` = transformations in `U*` accessible under pre-treatment domestic conditions.

The pre-treatment profile is supported by Round 1:
- P2 — computer/laptop at home;
- P3 — Internet at home;
- P4 — previous computer experience;
- P12* — declared computer capabilities.

These variables have explicit Yes/No coding in the inspected package. P5–P9 describe realized use/activities and are not substituted into the accessibility definition.

### `T_acc,1`

`T_acc,1` = transformations in the same `U*` accessible after XO assignment/provision, with the accessibility layer kept distinct from realized activity and acquired capability.

Round 2 provides the corresponding home-resource observations (P1 computer/laptop at home; P2 Internet at home; P3 previous computer experience). The public study documentation also identifies provision of XO laptops for home use as the intervention and reports increased home-computer access/use.

The operational definition therefore permits a bounded comparison of accessibility states without defining accessibility from post-treatment realized activity.

## 3. Causal separation

The preferred causal variable is:

`Z = won_lottery`

representing randomized lottery assignment.

`received_laptop` is retained as compliance/effective exposure information and is not substituted for randomized assignment.

`treatment_school` is a school-level treatment-condition variable and is not used as the individual randomized assignment variable in the causal definition.

The inspected data demonstrate that assignment, receipt and school treatment condition are not identical; this reinforces the required separation.

## 4. Information firewall

The following are explicitly excluded from `T_acc`:

- realized post-treatment laptop use;
- post-treatment activity measures;
- acquired XO skills/capability outcomes;
- academic or cognitive outcomes;
- aggregate treatment/control outcome statistics.

Outcome construction is independent. The frozen outcome definition is `Y = raven_r2`, based on 36 Raven items, with range `[0,36]`; it is not a component of `T_acc`.

## 5. Evidence chain

`baseline resources/capabilities → bounded U* → T_acc,0`

`randomized assignment Z → home-XO accessibility condition → T_acc,1`

`T_acc,0 / T_acc,1 → ΔT_acc → observed trajectory/use → capabilities/outcomes → Y`

The observed trajectory and outcomes are therefore downstream layers rather than definitions of accessibility.

## 6. Scope and limitations

This PASS is explicitly bounded. It does not establish a complete global `T_acc` for each student, nor does it claim that every domestic transformation becomes accessible after intervention. It establishes an admissible study-bounded operational layer sufficient for the TR-132 P4 gate.

No automatic upgrade of C09 claim strength, RMA, or TGCV Core follows from this record alone. Subsequent TR-132 gates remain subject to their own evidence requirements.

## 7. Provenance

This record consolidates the operational definition recovered from the prior OLPC/TR-132 analysis and cross-checked against the public V2 package structure and the already registered operational preflight.

Related canonical artifact:
`00_GOVERNANCE/SIP/TGCV_C09_OLPC_PERU_TR132_OPERATIONAL_PREFLIGHT_001.md`
