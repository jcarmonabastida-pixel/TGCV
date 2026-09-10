# IT-METH-I — FAA AMOC Governed Comparison 001

**Date:** 2026-09-10  
**Status:** `CLOSED — INCONCLUSIVE`  
**Case:** `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`  
**Protocol:** `IT-G4_I_FAA_AMOC_UTILITY_PROTOCOL_FREEZE_001.md`  
**Independence resolution:** `IT-METH-I_FAA_AMOC_EXECUTOR_2_INDEPENDENCE_GATE_RESOLUTION_002.md`

## 1. Purpose

Apply the frozen IT-G4 comparative utility protocol to Reconstruction 001 (R001) and the sealed Reconstruction 002 (R002), after the bounded blind-execution independence gate was closed.

This record does not alter either reconstruction, does not relax any threshold, and does not introduce post-decision outcomes, external evidence, new datasets, or TGCV Core modifications.

## 2. Inputs admitted to comparison

- R001: `IT-G4_I_FAA_AMOC_UTILITY_EXECUTION_RESULT_001.md` — prior execution result, status `CLOSED — INCONCLUSIVE`.
- R002: `IT-METH-I_FAA_AMOC_RECONSTRUCTION_002.md` — sealed artifact, exact artifact SHA-256 `FFE8D944F870B1DF2D6C9C5FA6A2D2FF67EA595E74520598929E12F43E4D5FD8`.
- Frozen IT-G4 protocol: `IT-G4_I_FAA_AMOC_UTILITY_PROTOCOL_FREEZE_001.md`.
- Bounded independence resolution: `IT-METH-I_FAA_AMOC_EXECUTOR_2_INDEPENDENCE_GATE_RESOLUTION_002.md`.
- R002 sealed-artifact audit: `IT-METH-I_FAA_AMOC_R002_SEALED_ARTIFACT_AUDIT_001.md`.

No modification was made to the sealed R002 artifact or to the historical R001 execution result.

## 3. Independence and contamination gate

The bounded blind-execution independence resolution establishes the operative independence criterion for this experiment as execution-context and information-state separation sufficient to prevent R001 contamination before R002 sealing.

Established conditions:

- distinct execution context: PASS;
- R001 withheld until R002 sealing: PASS;
- frozen input boundary: PASS;
- TGCV repository withheld during R002: PASS;
- no coaching or pre-seal comparison: PASS;
- no later outcomes, external sources, or new dataset: PASS;
- R002 sealed before R001 release: PASS.

The stronger human-operator identity distinction remains not demonstrated and is not claimed. The sealed R002 declaration `EXECUTOR_2_DISTINCT_FROM_EXECUTOR_1 = FAIL` is retained unchanged.

**BOUNDED_COMPARISON_INDEPENDENCE = PASS**

## 4. Field-level reconstruction comparison

| Frozen mandatory field | R001 TGCV | R002 TGCV | Comparison |
|---|---|---|---|
| Case identity | Supported | Supported | Substantive agreement; approval-date anchor differs |
| System/product boundary | Supported | Supported | Agreement |
| Decision-time state/context | Supported | Supported | Agreement at bounded documentary level |
| Baseline AD requirement | Supported | Supported | Agreement |
| Alternative method | Supported | Supported | Agreement |
| Enabling conditions | Supported | Supported | Agreement |
| Limiting conditions | Supported | Supported | Agreement |
| Applicability restrictions | Supported | Supported | Agreement |
| Temporal conditions | Supported | Supported | Documentary date anchor differs; aircraft-specific timing indeterminate in R002 |
| Evidence source for each field | Supported | Supported | Agreement in bounded source basis |
| Indeterminate fields | None required at R001 bounded level | Explicit aircraft-specific indeterminacy | Difference in explicitness, not contradiction of documentary scope |
| Resulting accessibility classification | ACCESSIBLE / ADMISSIBLE under G3 conditions | Documented conditional accessibility | Substantive agreement |

The two reconstructions independently recover the same bounded transformation structure: the AD-prescribed baseline compliance path and the documented Airworthiness-Limitations-based AMOC alternative, subject to explicit applicability and procedural constraints.

## 5. Frozen dimensions 1–3

The frozen protocol defines dimensions 1–3 as correctly supported mandatory fields divided by total mandatory fields.

R001 reports:

- decision-relevant coverage = `1.00`;
- reconstruction completeness = `1.00`;
- constraint traceability = `1.00`.

R002 contains all mandatory fields with evidence references and explicit documentary-versus-analytical distinction, with indeterminacy explicitly marked where aircraft-specific facts are absent. On the same bounded worksheet basis, no mandatory field is unsupported.

Therefore the comparison records:

- decision-relevant coverage: `1.00` R001 / `1.00` R002;
- reconstruction completeness: `1.00` R001 / `1.00` R002;
- constraint traceability: `1.00` R001 / `1.00` R002.

These results do not establish superiority.

## 6. Reproducibility

The frozen protocol requires independent reconstructions to be compared field-by-field.

R001 and R002 recover the same accessibility classification and the same bounded alternative transformation. The principal documentary inconsistency is the approval-date anchor:

- R001: `2018-02-23`;
- R002: `2018-02-13`.

This discrepancy is retained as an unresolved documentary issue. It is not silently corrected in R002.

At the level of the 10 substantive reconstruction fields, the comparison therefore establishes substantive agreement on the reconstructed accessibility/transformation structure, while Field 9 contains a date-anchor discrepancy. The evidence does not justify converting that discrepancy into a resolved factual value within this comparison.

**REPRODUCIBILITY_STATUS = SUBSTANTIVE AGREEMENT WITH DOCUMENTARY DISCREPANCY**

**REPRODUCIBILITY_AGREEMENT = NOT DETERMINATELY SCORABLE AS A CLEAN 10/10 FIELD MATCH**

No favorable numerical score is substituted for the unresolved discrepancy.

## 7. Analytical effort

R001 previously recorded analytical effort as not validly comparable under its execution condition.

R002 records wall-clock execution of approximately `0.009` seconds but explicitly marks `IT-G4_EFFORT = INDETERMINATE` because the frozen IT-G4 effort convention was not included in the admitted R002 package.

Therefore:

**EFFORT_COMPARISON = NOT VALIDLY COMPARABLE**

The 0.009-second wall-clock value is not used as an IT-G4 effort score.

## 8. Comparative improvement over conventional comparator

The frozen PASS rule requires at least one practically relevant improvement over the conventional comparator without compensating critical loss.

Both R001 and R002 reconstruct the conventional compliance alternative from the same documentary boundary. The conventional comparator already identifies the same approved AMOC path and its conditions.

The comparison therefore establishes:

**PRACTICALLY_RELEVANT_IMPROVEMENT_OVER_COMPARATOR = NOT ESTABLISHED**

The bounded TGCV representation provides an explicit accessibility/transformation framing, but the present case does not supply a frozen metric showing that this framing is practically superior to the conventional representation. No superiority inference is permitted.

## 9. Validity and outcome decision

Frozen IT-G4 requirements considered:

- critical validity failure: none established for bounded comparison;
- coverage ≥ 0.90: satisfied by both reconstructions;
- completeness ≥ 0.90: satisfied by both reconstructions;
- traceability ≥ 0.90: satisfied by both reconstructions;
- reproducibility agreement ≥ 0.90: **not determinately scorable as a clean field-match result because of the unresolved documentary date discrepancy**;
- practically relevant improvement over comparator: **not established**;
- analytical effort: **not validly comparable**.

Under the frozen rule, INCONCLUSIVE is mandatory where a required metric cannot be measured under the frozen protocol. In addition, the practical comparative-improvement requirement is not established.

**IT-METH-I GOVERNED COMPARISON RESULT = INCONCLUSIVE**

## 10. Interpretation

This is a determinate application of the frozen decision rule, not a judgment that TGCV is ineffective.

The result means that this single industrial case does not establish a comparative utility PASS or FAIL under the pre-specified protocol.

Established by this comparison:

- bounded reconstruction agreement: substantially established;
- decision-relevant coverage: 1.00 / 1.00;
- reconstruction completeness: 1.00 / 1.00;
- constraint traceability: 1.00 / 1.00;
- clean reproducibility metric: not determinately established;
- analytical effort comparison: not validly comparable;
- practically relevant superiority over conventional representation: not established.

The comparison does not establish causality, predictive validity, safety improvement, cost reduction, financial value, or value creation.

## 11. Open documentary issue

The approval-date discrepancy remains explicitly recorded:

`R001 = 2018-02-23`  
`R002 = 2018-02-13`

This comparison does not use external evidence to resolve the discrepancy because the comparison is bounded by the frozen experiment and must preserve the sealed R002 record as-is.

A later documentary reconciliation, if desired, must be a separate governed action and cannot retroactively alter R002 or this comparison result.

## 12. Closure

**STATUS = CLOSED — INCONCLUSIVE**

The frozen IT-G4 protocol was applied without threshold relaxation or favorable inference. No reconstruction rerun is required by this result.

`INDUSTRIAL_UTILITY = UNPROVEN / OPEN`

`COMPARATIVE_SUPERIORITY = NOT_ESTABLISHED`

`CAUSALITY = NOT_ASSESSED`

`FINANCIAL_VALUE_EFFECT = NOT_ASSESSED`

`TGCV_CORE = UNCHANGED`
