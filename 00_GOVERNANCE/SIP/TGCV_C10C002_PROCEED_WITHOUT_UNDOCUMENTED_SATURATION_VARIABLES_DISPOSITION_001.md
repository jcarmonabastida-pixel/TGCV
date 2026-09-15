# TGCV — C10C-002 Proceed-Without-Undocumented-Saturation-Variables Disposition 001

**Status:** FROZEN — METHODOLOGICAL DISPOSITION; EMPIRICAL EXECUTION NOT AUTHORIZED
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Purpose

Resolve the remaining methodological choice concerning the undocumented deposited saturation fields `sat`, `sat_treat` and `r2` without modifying the frozen causal design and without reopening the completed T17 bounded causal experiment.

## 2. Evidence basis

The controlled V1 inspection establishes:

- 342 admissible polygon observations in the panel universe;
- 60 municipalities;
- treatment variation within municipalities;
- `treat` is directly observed and admitted as the randomized assignment variable;
- the deposited analysis script uses `cve_mun` and saturation-related fields;
- the exact provenance/definition of `sat`, `sat_treat` and `r2` is not recoverable from the deposited V1 script/documentation without inference.

The published methodological record independently establishes that the experiment used a randomized saturation design and explicitly considered municipal spillovers. This resolves the existence and methodological relevance of interference, but does not establish the file-level provenance of the deposited saturation fields.

## 3. Disposition

**PROCEED WITHOUT THE UNDOCUMENTED DEPOSITED SATURATION VARIABLES** for the primary C10-C estimand, subject to the remaining pre-execution freeze conditions.

This is a methodological disposition, not an execution authorization.

The primary estimand therefore remains the ITT effect of randomized `treat` assignment on the independently measured polygon-level change in professional real-estate value. No undocumented saturation field is required as an input to the primary treatment contrast.

## 4. Interference interpretation

The absence of `sat`/`r2` from the primary analysis must not be interpreted as assuming away interference.

Instead:

1. randomized saturation is treated as a documented feature of the original design;
2. municipal treatment variation and possible spillovers remain an identification consideration;
3. the primary estimand is defined on randomized assignment, without conditioning on undocumented deposited saturation variables;
4. any interference/saturation robustness analysis must be specified from documented quantities before execution;
5. no post-outcome choice of saturation adjustment is permitted.

A municipal treatment share computed deterministically from admitted `treat` values may be used only if separately frozen as a design descriptor or robustness quantity. It is not automatically a causal adjustment variable.

## 5. What this disposition closes

This disposition closes the decision question:

> “Must the primary C10-C estimand use the undocumented deposited saturation fields?”

**Answer: NO.**

It does **not** close the separate data-provenance question of what those deposited fields were intended to represent.

The undocumented fields remain preserved as source data but are excluded from the primary estimand unless provenance is subsequently established.

## 6. What remains open before execution

The following independent conditions remain mandatory:

1. exact professional-value variable and file-level mapping;
2. exact unit and monetary scale;
3. baseline/follow-up valuation mapping;
4. missing-value and endpoint-linkage rule;
5. polygon aggregation rule;
6. final documented treatment-randomization reference;
7. pre-specified interference/robustness rule using only admissible documented quantities;
8. final statistical script/specification hash;
9. independent executor package and reproducibility test.

No condition above is satisfied merely by this disposition.

## 7. Non-reopening and non-upgrade rules

This record:

- does not reopen T17;
- does not repeat T10–T16-B;
- does not alter the negative bounded causal result;
- does not modify the frozen C10C-002 causal design;
- does not authorize causal estimation;
- does not upgrade any TGCV claim;
- does not infer the meaning of undocumented saturation variables.

## 8. Relationship to frozen causal specification

This disposition is subordinate to and consistent with `TGCV_C10C002_CAUSAL_EXECUTION_SPECIFICATION_001.md`.

The specification's rule that undocumented `sat`, `sat_treat` and `r2` are inadmissible remains unchanged. This record supplies the formally justified disposition permitted by that specification: the primary estimand can proceed conceptually without those undocumented fields, while interference remains explicitly treated as a design/identification issue.

## 9. Decision state

**C10C-002: PROMISING / EVIDENCE GAP REMAINS.**

**Causal execution: NOT AUTHORIZED.**

The next authorization gate is therefore determined by the remaining value-endpoint provenance and independent reproducibility conditions, together with the final pre-specified interference robustness rule.
