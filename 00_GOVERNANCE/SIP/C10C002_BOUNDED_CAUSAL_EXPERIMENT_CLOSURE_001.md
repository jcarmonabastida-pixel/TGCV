# C10-C — C10C-002 Bounded Causal Experiment Closure 001

**Status:** CLOSED — NEGATIVE BOUNDED CAUSAL RESULT  
**Date:** 2026-09-15  
**Candidate:** C10C-002 — *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*  
**Study:** McIntosh, Alegría, Ordóñez & Zenteno (2018), AEJ Applied Economics  
**Replication:** OpenICPSR 113705, V1  
**Experiment boundary:** bounded empirical TGCV test of `Z → ΔT_acc*`  

## 1. Purpose

This record registers the complete controlled C10C-002 data-level reconstruction and first bounded causal test performed after the frozen C10-C admission specification and controlled acquisition/inspection authorization.

The experiment was designed to test whether randomized treatment assignment `Z` produces a causal change in a bounded, reproducibly reconstructed structural transformation space `T_acc*`. It was not designed to establish a general TGCV validation claim or to estimate the downstream value pathway.

## 2. Frozen provenance boundary

Source package: OpenICPSR 113705 V1.

Acquired ZIP:

`113705-V1.zip`

ZIP size: `96,046,289` bytes.  
ZIP SHA-256: `D481DF2CCD6D677E81D1F0CD80AF27F24A111515BB6D1E9844D1DE6483A1DFC8`

Extracted V1 materials inspected:

| File | Bytes | SHA-256 |
|---|---:|---|
| `Encuestas-2012.docx` | 6,240,809 | `CD3947BAE112CEBE83783C241B18C06783FE31D0101D2C50C155761A512EC1A6` |
| `Habitat_Household_Analysis_Replication_170830.do` | 35,412 | `9C2F010725DCD60B090438137D155C8AC629D9AC185E3F22430C43DF46E4F3AF` |
| `Habitat_Household_Data_for_Replication.dta` | 146,655,902 | `B080612908BDD45BD8B44B2A42F94E92CCAFCF776DE5379BD6DAB2B054469C55` |
| `Habitat_Household_Data_for_Replication.xlsx` | 73,474,355 | `6E2E72DA1386F76DA7750CC0DCCCC73D9F74E0FF416C3178D85ABF9463E62B84` |
| `Habitat_Real_Estate_Replication_170830.do` | 2,963 | `383531C1C9CC64D4AC772E4518E35B5DC66429369974A4CD1E23B0B08702B67D` |
| `ReadMe.txt` | 2,772 | `AA2053E1745DE8CF1C04A6A49EECF7C642BA75468F24CDB3AA7FBB024CF8A443` |
| `real_estate_polygon_level.dta` | 128,872 | `428560B2976F6FBB77CD7669F476262FA9AF9F6CD1B7C578D45E95456884B494` |
| `real_estate_polygon_level.xlsx` | 162,049 | `5F962319AD9C22814C9C342E87237F5BFE5C191C38BD6D82451C5D1C82D58BE` |

No non-V1 external dataset was introduced.

## 3. Structural reconstruction

The deposited household analysis code operationalizes seven infrastructure component variables plus the aggregate index. For the bounded TGCV reconstruction, the six dimensions selected for the structural state were:

`Disp_Agua`, `Disp_Drenaje`, `Disp_Luz`, `Disp_Guarniciones`, `Disp_Banquetas`, `Disp_Pavimento`.

The aggregate `Disp_Infra_Bas` was not treated as an elementary transformation dimension.

The canonical structural state was:

`S_t = (A_t, D_t, L_t, G_t, B_t, P_t)`

where each component is the weighted polygon-level proportion of sampled households exhibiting the corresponding structural availability.

The original replication aggregation was respected: `sample_PANEL==1`, grouped by `N_POLIGONO × round`, using `m_Factor_Corto_Vivienda`. The weight was complete for the relevant sample-panel observations in both rounds.

The 370 household polygons reduce to exactly 342 `sample_PANEL` polygons, and that set is exactly identical to the 342 polygons in the real-estate file.

All 342 polygons are observed in both rounds. Thus the structural longitudinal unit is 342 polygons × 2 rounds.

## 4. Structural change

Weighted R1 means:

- Agua: 0.8921
- Drenaje: 0.7551
- Luz: 0.9864
- Guarniciones: 0.4796
- Banquetas: 0.4626
- Pavimento: 0.5709

Weighted R2 means:

- Agua: 0.9107
- Drenaje: 0.7941
- Luz: 0.9915
- Guarniciones: 0.5316
- Banquetas: 0.5380
- Pavimento: 0.6468

Mean structural changes:

- Agua: +0.0187
- Drenaje: +0.0391
- Luz: +0.0051
- Guarniciones: +0.0520
- Banquetas: +0.0755
- Pavimento: +0.0759

All six dimensions exhibited both positive and negative changes across polygons. Structural transition was therefore non-trivial and heterogeneous.

## 5. Bounded transformation universe

No ex-post direction was used as an accessibility predicate. No arbitrary 0.5 threshold was imposed on the continuous polygon-level weighted proportions.

The minimum structural feasibility predicates were:

- `P(A+) = 1` iff `A_t < 1`
- `P(A-) = 1` iff `A_t > 0`
- analogous predicates for D, L, G, B and P.

The bounded universe was therefore:

`U_tau* = {A+, A-, D+, D-, L+, L-, G+, G-, B+, B-, P+, P-}`

with 12 elementary transformation families.

T10-3A: PASS for minimal structural feasibility; mechanistic ex-ante accessibility remains an evidence gap.  
T10-3B: PASS — structural change in `T_acc*` is non-trivial and reproducible.  
T10-4: PASS — `T_acc,0*`, `T_acc,1*` and changes reproducible in 342 polygons; 238 polygons have non-empty total `ΔT_acc*`; 157 openings and 238 closures were observed.  
T10-5: PASS — value endpoint variables were not used to construct accessibility.  
T10-6: PASS — treatment/state separation preserved.  
T10-7: PASS — deterministic, non-circular reconstruction; 64 unique Tacc0 signatures and 53 Tacc1 signatures.  
T10-8: EVIDENCE GAP — all 60 municipalities contain both treatment and control polygons; interference cannot be ruled out from assignment design.  
T10-9: EVIDENCE GAP — `sat`/`sat_treat` provenance is not recoverable from the deposited V1 `.do`; they were therefore excluded from `C_t` and `P_tau`.  
T10-10: PASS — structural reconstruction closure; 342 polygons, both rounds complete, bounded universe size 12, `T_acc,0*`, `T_acc,1*` and `ΔT_acc*` defined, 238 non-empty changes.

## 6. Value endpoint and attrition boundary

The real-estate file contains 342 polygon-level observations. Treatment is complete: 176 control and 166 treated.

Only 138/342 polygons have observed property-value endpoint fields (`any_precio=1`): 77 control and 61 treated. The remaining 204 are missing the endpoint.

The V1 deposited scripts recover the USD conversion rule `/13.12`, but do not recover the upstream construction of `precios_diferencia`, `any_precio`, `any_precio_hat`, `attrition_wgt` or `product_wgt`. Therefore the upstream endpoint-selection/attrition mechanism remains an evidence gap.

This gap did not enter the construction of `T_acc*` and does not alter the T16 bounded structural causal result.

## 7. Causal identification boundary

T11: `CONDITIONALLY_SUPPORTED` — treatment positivity, endpoint linkage and causal unit linkage established; interference unresolved.

T12/T12-B: `EVIDENCE_GAP` — no definition/provenance of `sat`, `sat_treat`, `r2`, `treat_r2` was found in the deposited `.do`.

T13: `CONDITIONAL_CAUSAL_IDENTIFICATION` — all 60 municipalities contain both treatment and control; treatment varies within municipality; an estimand without `sat` is possible, but causal interpretation remains conditioned by municipal saturation/interference.

No claim of absence of interference was made.

## 8. T14 — bounded TGCV causal estimand

T14: `PASS_BOUNDED_TGCV_ESTIMAND`.

The pre-specified first causal arrow is:

`Z → ΔT_acc*`

342/342 polygons have a defined structural transition object and treatment is binary. Value variables were external to the construction.

## 9. T15 — pre-regression freeze

Primary specification frozen before estimation:

`Y_i = alpha + beta Z_i + epsilon_i`

with:

- unit: polygon;
- N: 342;
- treatment: `treat`;
- outcome: scalar `DeltaTacc_net`;
- period: R1 → R2;
- primary estimator: ITT;
- standard errors: clustered by municipality;
- covariate adjustment: none;
- fixed effects: none in primary specification;
- `sat`, `sat_treat`, `r2`, `treat_r2`: excluded;
- value variables: excluded;
- post-treatment covariates: excluded.

## 10. T15-B — scalar outcome freeze

Because `ΔT_acc*` is a transformation-space object rather than a scalar, the pre-specified scalar outcome was frozen as:

`DeltaTacc_net = |T_acc,1*| - |T_acc,0*|`

Results:

- 342 polygons;
- `Tacc0_n` range: 6–12;
- `Tacc1_n` range: 6–12;
- 8 distinct values of `DeltaTacc_net`;
- range: −3 to +4;
- mean: −0.2368421;
- zero net change: 125 polygons;
- non-zero net change: 217 polygons.

The scalarization is structural-only and independent of the value endpoint.

## 11. T16 — primary bounded ITT

The primary causal estimate was executed without `statsmodels`, using direct OLS algebra and municipality-clustered variance with 60 clusters.

Results:

- N = 342
- municipalities = 60
- `beta_ITT = -0.031421139101862026`
- cluster SE = `0.1645865990128021`
- t = `-0.19090946219392982`
- normal-reference p = `0.848596526762317`
- normal-reference 95% CI = `[−0.3540108731669541, 0.2911685949632301]`

T16 status: `ESTIMATED_BOUNDED_ITT`.

## 12. T16-B — few-cluster robust inference

A Rademacher wild cluster bootstrap was executed under the null with municipality as the cluster and 9,999 bootstrap replications.

Results:

- beta ITT = `−0.031421139101862026`
- cluster SE = `0.1645865990128021`
- observed t = `−0.19090946219392982`
- wild-bootstrap p = `0.8354`
- 95% bootstrap critical value = `1.6846375446998223`
- 95% wild-bootstrap CI = `[−0.3086899031532831, 0.24584762494955906]`

T16-B status: `WILD_CLUSTER_BOOTSTRAP_COMPLETE`.

## 13. Causal result

The bounded causal test does **not** provide statistically detectable evidence that randomized treatment assignment changes the net number of accessible elementary transformations under the frozen `U_tau*` operationalization.

The result is a **negative/non-detectable bounded causal result**. It is not evidence that the true effect is exactly zero.

The interval remains compatible with both negative and positive effects of non-trivial magnitude.

## 14. TGCV claim boundary

This experiment establishes:

1. a reproducible bounded structural representation;
2. a non-trivial longitudinal structural transition;
3. a deterministic, value-independent `T_acc*` construction;
4. a pre-specified bounded causal estimand;
5. a causal estimate and few-cluster robust inference for that estimand.

It does **not** establish:

- positive bounded empirical causal support for `Z → ΔT_acc*`;
- general empirical support for TGCV;
- a refutation of TGCV;
- a causal effect on property value;
- a causal pathway `ΔT_acc → V`;
- absence of municipal/spatial interference.

No value regression was executed.

## 15. T17 closure

T17 status: `C10C002_CLOSED_NEGATIVE_BOUNDED_CAUSAL_RESULT`.

The candidate is closed for this empirical cycle. T10–T16-B must not be repeated merely to seek a positive result.

Any alternative TGCV outcome or alternative transformation universe must be separately justified and frozen before any future estimation; it cannot be selected post hoc because of the negative result.

## 16. Local execution artifacts

The following artifacts were produced during execution and remain in the local controlled package:

- `T10_elementary_transformations.csv`
- `T10-4_Tacc_reconstruction.csv`
- `T10-5_endpoint_separation_audit.csv`
- `T10-7_determinism_noncircularity.csv`
- `T10-10_structural_reconstruction_closure.csv`
- `T11_causal_execution_sufficiency_audit.csv`
- `T12-B_variable_origin_trace.txt`
- `T13_municipal_assignment_structure.csv`
- `T14_bounded_TGCV_estimand_audit.csv`
- `T15_pre_regression_ITT_specification.md`
- `T15-B_scalar_TGCV_outcome.csv`
- `T16_bounded_ITT_DeltaTacc_result.txt`
- `T16-B_wild_cluster_bootstrap_result.txt`
- `T17_C10C002_bounded_causal_closure.md`

The local source package path was:

`C:\Users\pedri\Downloads\openICPSR\C10C002_113705_V1`

## 17. Governance disposition

**Candidate:** C10C-002  
**Final experiment disposition:** CLOSED — NEGATIVE BOUNDED CAUSAL RESULT  
**Positive TGCV causal support:** NO  
**General TGCV validation:** NO  
**TGCV refutation:** NO  
**Value pathway estimated:** NO  
**Interference:** UNRESOLVED  
**Next action:** return to C10-C candidate routing and proceed to the next candidate; do not reopen C09.

## 18. Traceability

This closure is governed by:

- `TGCV_C10_C_CANDIDATE_C10C002_DATA_LEVEL_ADMISSION_PACKAGE_SPECIFICATION_001.md`
- `TGCV_C10_C_CANDIDATE_C10C002_CONTROLLED_ACQUISITION_INSPECTION_AUTHORIZATION_001.md`
- `TGCV_C10_METHODOLOGICAL_CRITERION_BOUNDED_EMPIRICAL_CAUSAL_SUPPORT_001.md`

This record is an experiment/closure register, not a claim-level TGCV validation record.
