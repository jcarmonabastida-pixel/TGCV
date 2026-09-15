# TGCV — C10C-002 Independent Reproduction Package Specification 001

**Status:** FROZEN — B4 PACKAGE SPECIFICATION; INDEPENDENT REPRODUCTION NOT YET COMPLETED; EMPIRICAL EXECUTION NOT AUTHORIZED
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Purpose

Define the minimum self-contained package that an independent executor must receive to reproduce the frozen C10-C value-linkage design without access to the prior bounded causal experiment, prior results, or outcome-driven choices.

## 2. Frozen source package

The independent package must use exactly OpenICPSR 113705 V1, identified by:

- ZIP: `113705-V1.zip`
- ZIP SHA-256: `D481DF2CCD6D677E81D1F0CD80AF27F24A111515BB6D1E9844D1DE6483A1DFC8`

Required deposited files and SHA-256:

- `Encuestas-2012.docx` — `CD3947BAE112CE83783C241B18C06783FE31D0101D2C50C155761A512EC1A6`
- `Habitat_Household_Analysis_Replication_170830.do` — `9C2F010725DCD60B090438137D155C8AC629D9AC185E3F22430C43DF46E4F3AF`
- `Habitat_Household_Data_for_Replication.dta` — `B080612908BDD45BD8B44B2A42F94E92CCAFCF776DE5379BD6DAB2B054469C55`
- `Habitat_Household_Data_for_Replication.xlsx` — `6E2E72DA1386F76DA7750CC0DCCCC73D9F74E0FF416C3178D85ABF9463E62B84`
- `Habitat_Real_Estate_Replication_170830.do` — `383531C1C9CC64D4AC772E4518E35B5DC66429369974A4CD1E23B0B08702B67D`
- `ReadMe.txt` — `AA2053E1745DE8CF1C04A6A49EECF7C642BA75468F24CDB3AA7FBB024CF8A443`
- `real_estate_polygon_level.dta` — `428560B2976F6F77CD7669F476262FA9AF9F6CD1B7C578D45E95456884B494`
- `real_estate_polygon_level.xlsx` — `5F962319AD9C22814C9C342E87237F5BFE5C191C38BD6D82451C5D1C82D58BE`

## 3. Governance inputs

The executor package must also contain the frozen candidate-specific governance records defining:

1. causal execution specification;
2. endpoint provenance limitation;
3. B2 endpoint field/unit/time/aggregation freeze;
4. B3 interference robustness rule;
5. proceed-without-undocumented-saturation disposition.

These documents define the admissible boundary and must be read before any execution.

## 4. Independent-executor boundary

The executor must not receive or use:

- the previous T17 result as an analytical input;
- prior treatment-effect estimates;
- prior regression outputs;
- outcome-driven specification choices;
- undocumented interpretations of `sat`, `sat_treat`, `r2` or `treat_r2`;
- any external dataset;
- any post-outcome model selection.

The executor may use only the frozen source package and the frozen governance specification.

## 5. Required reproduction checks

Before any causal estimation, the independent executor must reproduce at minimum:

- the 342-polygon admissible panel linkage universe;
- treatment `treat` and municipality identifier `cve_mun`;
- the six structural infrastructure dimensions;
- the 12 bounded opening/closure transformations;
- `T_acc,0`, `T_acc,1`, and `Delta T_acc` from structural inputs only;
- the deposited value endpoint `precios_diferencia_usd` exactly as represented, without inferred reconstruction;
- the 138/342 endpoint-observation coverage;
- exclusion of undocumented saturation fields from the primary estimand;
- municipality-clustered primary inference rule;
- the frozen primary ITT specification.

## 6. Reproduction acceptance

B4 is not closed by creation of this specification alone.

B4 closes only after an independent executor, operating under the defined boundary, demonstrates reproducibility of the frozen package and records:

- exact input hashes;
- environment/tool versions;
- extraction/transformation procedure hash;
- script/specification hash;
- deterministic structural reconstruction checks;
- endpoint linkage/coverage checks;
- confirmation that no prohibited inputs were used.

Any mismatch is a stop condition and must be resolved before causal execution.

## 7. Relationship to B5

The final executable analysis script/specification hash remains a separate B5 condition. This package specification must not be interpreted as the final execution hash.

B4 and B5 therefore remain jointly required before execution authorization.

## 8. Governance boundary

This record:

- does not authorize causal estimation;
- does not reopen T17;
- does not repeat T10–T16-B;
- does not infer the endpoint construction formula;
- does not infer undocumented saturation variables;
- does not upgrade C10C-002 beyond `PROMISING / EVIDENCE GAP REMAINS`.

**Current state: B4 SPECIFICATION FROZEN; REPRODUCTION TEST PENDING.**
**EMPIRICAL CAUSAL EXECUTION: NOT AUTHORIZED.**
