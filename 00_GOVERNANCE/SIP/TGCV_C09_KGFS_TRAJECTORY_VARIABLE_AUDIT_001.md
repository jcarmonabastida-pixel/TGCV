# TGCV C09 — KGFS Trajectory Variable Audit 001

**Date:** 2026-09-14
**Status:** PARTIAL PASS — STRUCTURAL/LONGITUDINAL AUDIT PASSED; EXACT TRAJECTORY-VARIABLE ENUMERATION/HASH CLOSURE PENDING
**Candidate:** KGFS Rural Banking

## 1. Audit objective

Verify that the KGFS evidence can support a reproducible downstream trajectory following the randomized structural accessibility intervention, without redefining accessibility using downstream realization variables.

## 2. Public-source verification

The Yale ISPS archive identifies the study as a field experiment with household-level observation, 4,184 households, service-area randomization, and treatment defined as expansion of banking services. It provides separate baseline and endline data files, baseline/endline codebooks, survey instruments and DDI metadata. Baseline files are D178F03–D178F40; endline files are D178F41–D178F76; codebooks are D178F77.1 and D178F78.1; metadata are D178F90. citeturn1view0

The Yale user reference gives the operational survey structure. Baseline surveys were administered before branch opening and endline surveys to the same households 18–24 months after branch opening. The experiment randomized which service area received the KGFS branch first within matched service-area pairs. citeturn7view0

The user reference also establishes exact core identifiers available in the public household data:

- `hhid` — main household identifier;
- `memid` — person number from the household roster;
- `cont_s_id` — composite location identifier that can identify district, block, gram panchayat and village and can identify treated/control village status. citeturn7view0

The public user reference specifies that the harmonized datasets are organized by section and observation level, including household, individual, woman, child, contact and section-specific levels. It also specifies that baseline I, baseline II, baseline III are harmonized together, as are the three endlines, and warns that the temporal order is **Baseline I → Baseline II → Endline I → Baseline III → Endline II → Endline III**. citeturn7view0

## 3. Trajectory-variable domain audit

The user reference confirms that the household survey contains the following relevant modules in both survey waves:

| TGCV trajectory dimension | Public survey section/domain | Structural/downstream classification | Status |
|---|---|---|---|
| Occupational state / non-agricultural self-employment | Section 2 roster + Section 4 existing self-employment + Section 6 labor | Downstream | PASS |
| Business activity / business income | Section 4 existing self-employment | Downstream | PASS |
| Wage employment / wage income | Section 6 labor | Downstream | PASS |
| Informal borrowing / financial state | Section 11 loans and lenders | Downstream financial state; not T_acc | PASS |
| Savings / insurance state | Section 12 savings and insurance | Downstream financial state; not T_acc | PASS |
| Poverty / wellbeing | Sections 9 consumption, 18 subjective wellbeing/aspirations; income/assets in household modules | Value-relevant downstream state/outcome | PASS |

The user reference describes Section 4 as identifying self-employed household members and recording business revenue and fixed/variable costs; Section 6 records labor type, payment frequency and salary; Section 11 records outstanding and repaid loans and their sources/purposes; Section 12 records savings and insurance; and Section 18 records subjective wellbeing and aspirations. citeturn7view0

The Yale EGC project page independently confirms that both baseline and endline include household income/assets, loans, savings, insurance, occupation/employment and business outcomes. citeturn0search4

## 4. Boundary check: T_acc versus trajectory

The following remain **outside** the definition of `T_acc`, even though they can be downstream consequences of the intervention:

- loan take-up;
- savings take-up;
- insurance take-up;
- business activity generated after treatment;
- employment generated after treatment;
- income;
- poverty;
- wellbeing.

The structural accessibility state remains represented by the intervention itself: the randomized early opening of KGFS banking infrastructure and the structural financial capabilities made available through that system. The user reference describes KGFS as offering formal loans, savings, insurance and tailored financial advice through local village branches. citeturn7view0

Thus the intended causal ordering remains:

`randomized structural branch expansion -> ΔT_acc -> subsequent financial/economic state trajectory -> value-relevant outcomes`

This is consistent with the study design: baseline before branches and endline 18–24 months after branch opening. citeturn7view0

## 5. Longitudinal reproducibility audit

The following elements are now independently established from the public documentation:

- stable household identifier: `hhid`;
- person/roster identifier: `memid`;
- geographic/service-area linkage support: `cont_s_id`;
- baseline and endline public `.dta` files;
- baseline and endline codebooks;
- explicit harmonization of survey rounds;
- explicit documentation of section-specific observation levels;
- explicit baseline/endline temporal ordering;
- explicit missing-value conventions;
- explicit warning that Stata extended missing values must be handled with `missing()` / `!missing()` rather than only `.`;
- explicit rules for added, dropped and modified variables in harmonized datasets. citeturn7view0

This materially strengthens the reproducibility case beyond the previous module-level audit.

## 6. Remaining technical gap

The exact variable names for the selected trajectory constructs have **not** been safely asserted in this audit, because the public archive page exposes the codebook files but the current retrieval path did not expose their binary contents to the execution environment. We therefore do not invent variable names from the section descriptions.

The remaining closure is strictly mechanical:

1. retrieve D178F77.1 and D178F78.1 and the relevant `.dta` files;
2. enumerate exact variable names and labels for the selected trajectory constructs;
3. verify `hhid` uniqueness/merge structure across the selected baseline/endline files;
4. verify `cont_s_id` and treatment/service-area linkage;
5. freeze recoding and extended-missing-value handling;
6. construct deterministic state/transition variables;
7. hash the source files;
8. archive the operationalisation manifest and reproducibility log.

No scientific reinterpretation is required for this step.

## 7. Gate decision

**KGFS C09 trajectory architecture: PASS.**

**KGFS longitudinal data/identifier architecture: PASS.**

**KGFS exact trajectory-variable reproducibility: OPEN — technical closure only.**

D5-A remains CLOSED. This audit does not upgrade C09 globally and does not modify TGCV Core, RMA, Evidence→Claim Matrix or STATUS.

## 8. Next authorized operation

Execute the exact `.dta`/codebook variable enumeration and reproducibility manifest. No additional candidate search is authorized before this technical closure unless the public KGFS files prove inaccessible or insufficient.
