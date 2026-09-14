# TGCV C09 — KGFS Trajectory Variable Audit 001

**Date:** 2026-09-14
**Status:** PARTIAL PASS — STRUCTURAL/LONGITUDINAL AUDIT PASSED; EXACT VARIABLE-NAME/HASH CLOSURE PENDING
**Candidate:** KGFS Rural Banking

## 1. Audit objective

Verify that the KGFS evidence can support a reproducible downstream trajectory following the randomized structural accessibility intervention, without redefining accessibility using downstream realization variables.

## 2. Public-source verification

The Yale ISPS archive identifies the study as a field experiment with household-level observation, 4,184 households, service-area randomization, and treatment defined as expansion of banking services. The archive provides separate baseline and endline household data files, codebooks and survey instruments. The archive lists baseline sections D178F03–D178F40 and endline sections D178F41–D178F76, plus baseline/endline codebooks and survey instruments.

The Yale Economic Growth Center states that the household dataset contains baseline and endline observations and that both rounds include modules covering household income/assets, loans, savings, insurance, occupation/employment and business outcomes. The project description states that baseline collection occurred in 2010–2014 and endline collection in 2013–2016, with the core analysis covering 4,160 households across 870 villages. citeturn1view0turn0search3

The evaluation report documents the randomized treatment as increased access to formal finance through opening a KGFS branch in a service area, with baseline surveys paralleling branch opening and endline surveys 18–24 months later. It reports downstream changes in self-employment, business income, household income and wages. citeturn4search24turn4search0

## 3. Trajectory audit matrix

| Trajectory | Baseline/endline availability | Causal ordering | TGCV admissibility | Status |
|---|---|---|---|---|
| Occupational state / non-agricultural self-employment | Yes | Post-intervention | Downstream of accessibility | PASS |
| Business activity / business income | Yes | Post-intervention | Downstream of accessibility | PASS |
| Wage employment / wage income | Yes | Post-intervention | Downstream of accessibility | PASS |
| Informal borrowing / financial state | Yes | Post-intervention | Downstream financial state; not T_acc | PASS |
| Poverty / wellbeing | Yes | Post-intervention | Value-relevant downstream outcome | PASS |

The public project description explicitly confirms that occupation/employment and business outcomes are measured in both baseline and endline rounds, while the archive lists loans, savings, employment, labour, consumption, insurance, wellbeing and related outcomes. citeturn0search3turn1view0

## 4. Boundary check

The following must remain outside the definition of `T_acc` even though they are observed as treatment responses:

- loan take-up;
- savings take-up;
- insurance take-up;
- business activity generated after treatment;
- employment generated after treatment;
- income;
- poverty;
- wellbeing.

This preserves the causal ordering:

`structural accessibility intervention -> subsequent financial/economic state -> value-relevant outcome`

The intervention is not reconstructed from the downstream response variables. The public evaluation itself distinguishes the randomized treatment from outcomes such as borrowing, savings, income and employment. citeturn4search24

## 5. What is closed

The audit establishes that KGFS has the required longitudinal architecture for a C09 trajectory bridge:

- stable household observational unit;
- baseline and endline measurements;
- randomized service-area intervention;
- structural intervention temporally preceding endline;
- multiple downstream state/trajectory dimensions;
- downstream variables separable conceptually from the structural accessibility definition.

Therefore the prior **KGFS accessibility-to-trajectory bridge remains PASS at the study-design and module level**.

## 6. What is not yet closed

This audit does **not** claim that the exact variable names, merge keys, recoding rules, missing-value treatment and file hashes have been independently reconstructed from the raw `.dta` files in this pass. The Yale archive exposes the required baseline/endline data files and codebooks, but the indexed public material available for this audit does not expose the full variable dictionaries inline. citeturn1view0

Accordingly, the remaining reproducibility closure is strictly technical:

1. obtain the public `.dta` files and codebooks;
2. enumerate exact variable names for the selected trajectory dimensions;
3. verify household and service-area linkage;
4. freeze baseline/endline recoding and missing-value rules;
5. compute deterministic trajectory variables;
6. record source-file hashes;
7. archive the resulting operationalisation manifest.

## 7. Gate decision

**KGFS C09 trajectory architecture: PASS.**

**KGFS exact variable-level reproducibility: OPEN — technical closure only.**

This does not reopen D5-A. D5-A remains CLOSED. It also does not upgrade the global C09 claim, TGCV Core, RMA, Evidence→Claim Matrix or STATUS.

## 8. Next authorized operation

Complete the exact `.dta` variable-level audit and reproducibility manifest. No additional candidate search is authorized before this technical closure unless the public KGFS files prove inaccessible or insufficient.
