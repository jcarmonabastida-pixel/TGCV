# TGCV — C10C-002 Controlled Data-Level Inspection Result 001

**Status:** COMPLETED — PROMISING / EVIDENCE GAP REMAINS
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico
**Source:** OpenICPSR 113705 V1
**Authorization:** `TGCV_C10_C_CANDIDATE_C10C002_CONTROLLED_ACQUISITION_INSPECTION_AUTHORIZATION_002.md`

## 1. Acquisition boundary

The previously acquired V1 package and acquisition manifest are retained as the controlled source. Archive SHA-256:

`D481DF2CCD6D677E81D1F0CD80AF27F24A111515BB6D1E9844D1DE6483A1DFC8`

Authorized files and SHA-256:

| File | SHA-256 |
|---|---|
| `Encuestas-2012.docx` | `CD3947BAE112CEBE83783C241B18C06783FE31D0101D2C50C155761A512EC1A6` |
| `Habitat_Household_Analysis_Replication_170830.do` | `9C2F010725DCD60B090438137D155C8AC629D9AC185E3F22430C43DF46E4F3AF` |
| `Habitat_Household_Data_for_Replication.dta` | `B080612908BDD45BD8B44B2A42F94E92CCAFCF776DE5379BD6DAB2B054469C55` |
| `Habitat_Household_Data_for_Replication.xlsx` | `6E2E72DA1386F76DA7750CC0DCCCC73D9F74E0FF416C3178D85ABF9463E62B84` |
| `Habitat_Real_Estate_Replication_170830.do` | `383531C1C9CC64D4AC772E4518E35B5DC66429369974A4CD1E23B0B08702B67D` |
| `ReadMe.txt` | `AA2053E1745DE8CF1C04A6A49EECF7C642BA75468F24CDB3AA7FBB024CF8A443` |
| `real_estate_polygon_level.dta` | `428560B2976F6F77CD7669F476262FA9AF9F6CD1B7C578D45E95456884B494` |
| `real_estate_polygon_level.xlsx` | `5F962319AD9C22814C9C342E87237F5BFE5C191C38BD6D82451C5D1C82D58BE` |

No external dataset or V2 material is admitted.

## 2. Structural state recovery

The deposited household replication code explicitly defines the infrastructure variable family as:

`Disp_Agua`, `Disp_Drenaje`, `Disp_Luz`, `Disp_Guarniciones`, `Disp_Banquetas`, `Disp_Pavimento`, plus the aggregate `Disp_Infra_Bas` and `Alumbrado_Siempre_Enc`.

For bounded TGCV reconstruction, the six elemental dimensions are admissible candidates; the aggregate is not an elemental transformation dimension. `Alumbrado_Siempre_Enc` is excluded from the minimum universe because of additional missingness.

The replication code also explicitly uses first differences such as `d_Disp_Agua` and `d_Disp_Drenaje`, while `treat` is used as an assignment variable. This supports treatment/state separation rather than equating treatment with realized state.

## 3. Unit and temporal linkage

The household replication structure identifies polygon `N_POLIGONO` and survey `round` and uses `sample_PANEL==1` for the panel population. The controlled reconstruction established 342 polygons with complete baseline/follow-up structural observations for the bounded inspection universe.

Treatment counts in the controlled reconstruction are 176 control and 166 treated polygons.

The real-estate polygon universe aligns with the 342 `sample_PANEL` polygons, providing a direct candidate linkage between structural transition and the independently measured property-value endpoint.

## 4. Bounded transformation universe

A minimum sufficient bounded universe of 12 elementary transformations is admissible for inspection:

`A+ A- D+ D- L+ L- G+ G- B+ B- P+ P-`

where each dimension has an opening and closure transformation.

Structural predicates are defined without value or downstream outcomes:

- opening: `P_{τ_j+}(S_t)=1` when `S_{j,t}<1`;
- closure: `P_{τ_j-}(S_t)=1` when `S_{j,t}>0`.

The controlled reconstruction produced nonempty `ΔT_acc` for 238 of 342 polygons. This demonstrates that the bounded universe is non-trivial and operationally reconstructible.

The reconstruction must remain independent of `treat`, real-estate value and downstream outcomes.

## 5. Value endpoint

The real-estate replication material provides a distinct property-value endpoint based on professional valuations of unbuilt lots at baseline/follow-up. The endpoint is therefore not definitionally part of the accessibility predicates.

The value layer is independently observable and temporally linked at the polygon level for the controlled 342-polygon universe.

## 5A. Endpoint variable and provenance update

Controlled inspection of `real_estate_polygon_level.dta` established the endpoint-related deposited variables:

`precios_diferencia`, `precios_diferencia_usd`, `valor_co_09`, `valor_co_09_usd`, `valor_co_12`, `lvalor_09`, `lvalor_12`, `lprecios_diferencia`, `any_precio`, and `any_precio_hat`.

The deposited `Habitat_Real_Estate_Replication_170830.do` directly uses **`precios_diferencia_usd`** as the dependent variable in the property-price/DID regressions and the Figure 2 CDF analysis. The script describes the endpoint as real-2012-dollar price increases per square meter and polygon-level averages.

The controlled data check found 138 observed endpoint records out of 342 polygons. It also established that `precios_diferencia` is **not** equal to `valor_co_12 - valor_co_09` for the observed records. Consequently, no direct subtraction of the deposited valuation-level fields is admitted as a reconstruction of the endpoint.

The V1 real-estate replication script loads the `.dta` and consumes these endpoint variables; it does not construct them. The exact upstream formula for `precios_diferencia` and `precios_diferencia_usd` was not recovered from the deposited script or from recoverable pandas/Stata metadata. `pandas.read_stata(..., convert_categoricals=False)` required a Latin-1 fallback for incompatible metadata strings and returned empty `d.attrs`; the stricter `pyreadstat` metadata read failed on an invalid UTF-8 metadata byte before yielding usable variable metadata.

Therefore the endpoint is **identified at the deposited-variable level**, while its upstream construction remains a documented provenance/reproducibility gap. No inferred formula is admitted.

The ratio `precios_diferencia_usd / precios_diferencia` is effectively constant at approximately `0.0762195125` over observed records, consistent with the USD representation, but this does not establish the upstream construction formula.

## 6. Identification and counterfactual

The intervention is randomized at polygon/municipality saturation structure, with treatment assignment available separately from realized infrastructure state. This supports a credible treatment/control counterfactual for the bounded causal design.

However, municipal saturation and spatial structure create a material interference/spillover question that must remain explicitly represented in any later causal execution.

## 7. Interference and context

The controlled inspection identifies 60 municipalities, all with mixed treatment/control assignment. Saturation variables are observed, but their provenance/definition is not sufficiently complete to treat interference as resolved at this stage.

Therefore:

**Interference status: UNRESOLVED / MATERIAL EVIDENCE GAP.**

This does not invalidate the candidate; it prevents premature execution authorization.

## 8. Reproducibility

The replication package contains the household and real-estate scripts and the corresponding data files. Variable-level provenance for the core infrastructure fields is sufficiently recoverable for the bounded reconstruction.

A separate trace identified undocumented/insufficiently documented saturation variables (`sat`, `r2` and related fields) in the deposited script. Their presence does not contaminate the structural `T_acc` predicates, but their interpretation must not be guessed.

The value-endpoint inspection adds a separate provenance limitation: the deposited endpoint variable is identifiable and directly consumed by the replication script, but its upstream construction is not documented in the V1 replication script or recoverable metadata inspected.

## 9. T1–T10 disposition

| Test | Result |
|---|---|
| T1 source identity | PASS |
| T2 structural variable recovery | PASS |
| T3 temporal linkage | PASS |
| T4 treatment/state separation | PASS |
| T5 transformation universe | PASS — bounded 12 transformations |
| T6 predicate integrity | PASS — structural only |
| T7 baseline/follow-up | PASS |
| T8 transition reconstruction | PASS |
| T9 reproducibility | PASS for core structural layer; saturation and endpoint-construction provenance gaps |
| T10 operational closure | PASS for bounded structural reconstruction; interference remains unresolved |

## 10. Admission decision

**C10C-002: PROMISING / EVIDENCE GAP REMAINS.**

The candidate passes the core structural and value-linkage admission requirements sufficiently to justify preparation of a separate causal-execution specification, but it is not yet authorized for causal estimation because interference/saturation interpretation remains unresolved and endpoint construction provenance remains incomplete.

## 11. Critical non-reopening rule

This inspection does not reopen or reinterpret the previously completed C10C-002 bounded causal experiment. Its negative result remains unchanged.

The present operation is a separate C10-C value-linkage admission audit.

## 12. Decision boundary

**Empirical causal execution: NOT AUTHORIZED.**

The existing candidate-specific causal-execution specification remains frozen and unchanged. The next governed action, if progression is desired, is to resolve or explicitly freeze the remaining provenance/interference conditions before any execution authorization.
