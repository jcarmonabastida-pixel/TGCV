# TGCV — C10C-002 Value Endpoint Documentary Freeze 001

**Status:** PARTIALLY FROZEN — DOCUMENTARY ENDPOINT ESTABLISHED; DEPOSITED VARIABLE IDENTIFIED; UPSTREAM CONSTRUCTION PROVENANCE GAP REMAINS
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Documentary endpoint established

The study's published methodological record specifies the independent real-estate endpoint as professional assessments of **raw land value / price per square meter for unbuilt lots**, measured at baseline and follow-up.

The assessors were professional property assessors from INDAABIN, evaluated the same unbuilt lots at baseline and follow-up, and were blinded to treatment assignment. The published analysis uses polygon-level averages of the assessed price per square meter.

The reported dependent variable is the **change in real-estate price per square meter, in real 2012 US dollars**, based on professional assessments.

The study reports 138 polygons with valuation observations and 342 polygons in the broader baseline experiment universe.

## 2. V1 deposited endpoint variable identified

Controlled inspection of the exact OpenICPSR 113705 V1 package established that `real_estate_polygon_level.dta` contains the following endpoint-related variables:

- `precios_diferencia`
- `precios_diferencia_usd`
- `valor_co_09`
- `valor_co_09_usd`
- `valor_co_12`
- `lvalor_09`
- `lvalor_12`
- `lprecios_diferencia`
- `any_precio`
- `any_precio_hat`

The deposited replication script `Habitat_Real_Estate_Replication_170830.do` directly uses **`precios_diferencia_usd` as the dependent variable** in the reported DID/property-price regressions and in the Figure 2 CDF analysis. The script labels the analysis as real-2012-dollar price increases per square meter and polygon-level averages.

The controlled inspection found 138 observed endpoint records out of 342 polygons, consistent with the documented valuation-observation coverage.

## 3. Exact construction provenance: evidence gap

The V1 replication script **does not construct** `precios_diferencia` or `precios_diferencia_usd`; it loads `real_estate_polygon_level.dta` and consumes those variables as pre-existing fields. The same applies to the other endpoint-related fields listed above.

A direct data check established that:

`precios_diferencia != valor_co_12 - valor_co_09`

for the observed valuation records. Therefore the endpoint must **not** be reconstructed by naively subtracting the two deposited valuation-level fields.

`precios_diferencia_usd` has an effectively constant conversion ratio relative to `precios_diferencia`, consistent with the USD representation, but this does not establish the upstream formula that generated `precios_diferencia`.

The Stata file was readable with `pandas.read_stata(..., convert_categoricals=False)` using its Latin-1 fallback for incompatible metadata strings, but the resulting pandas attributes were empty (`d.attrs == {}`) and did not provide construction provenance. The stricter `pyreadstat` metadata read failed on an invalid UTF-8 metadata byte before yielding usable variable metadata. No construction formula has therefore been recovered from the V1 file metadata.

**Conclusion:** the deposited endpoint variable `precios_diferencia_usd` is identified and operationally usable as the authors' documented economic endpoint, but the exact upstream construction of `precios_diferencia` / `precios_diferencia_usd` is **not documented or recoverable from the V1 replication script and recoverable file metadata inspected so far**.

No inferred formula is admitted in its place.

## 4. Why this remains admissible for TGCV design

This endpoint is independent of the six structural infrastructure variables used to construct `T_acc*` and is therefore not outcome-defined accessibility. It provides an externally measured value endpoint suitable in principle for the C10-C value-linkage design.

The provenance gap is a reproducibility/documentation limitation, not evidence that the endpoint itself is invalid. Any future empirical execution must use the deposited endpoint exactly as represented in the admitted V1 file unless its upstream construction is independently documented and frozen.

## 5. Remaining file-level freeze

The following remain unresolved for full empirical-execution readiness:

- upstream construction formula for `precios_diferencia`;
- upstream construction/conversion provenance for `precios_diferencia_usd`;
- exact baseline/follow-up source-field mapping underlying the deposited endpoint;
- exact missing-value and attrition construction provenance where relevant;
- exact polygon aggregation provenance where not already documented;
- deterministic extraction procedure and hash for the final empirical package.

These items must be recovered from admitted V1 evidence or explicitly recorded as irrecoverable limitations. They must not be inferred from outcome values or reconstructed post hoc.

## 6. Governance boundary preserved

This update **does not modify** `TGCV_C10C002_CAUSAL_EXECUTION_SPECIFICATION_001.md`.

This update **does not reopen** the previously closed C10C-002 bounded causal experiment (`T17` / `C10C002_CLOSED_NEGATIVE_BOUNDED_CAUSAL_RESULT`).

The negative bounded causal result remains unchanged: no statistically detectable treatment effect on the frozen net-number-of-accessible-transformations outcome under that prior operationalization. No value regression is added to that experiment.

No causal estimation is authorized by this record.

## 7. Evidence record

Controlled V1 package:

- ZIP: `113705-V1.zip`
- ZIP SHA-256: `D481DF2CCD6D677E81D1F0CD80AF27F24A111515BB6D1E9844D1DE6483A1DFC8`
- `Habitat_Real_Estate_Replication_170830.do` SHA-256: `383531C1C9CC64D4AC772E4518E35B5DC66429369974A4CD1E23B0B08702B67D`
- `real_estate_polygon_level.dta` SHA-256: `428560B2976F6F77CD7669F476262FA9AF9F6CD1B7C578D45E95456884B494`

Inspection facts additionally established:

- `SHAPE = (342, 61)`;
- `any_precio = 1` for 138 polygons and `0` for 204;
- `precios_diferencia_usd / precios_diferencia` has an effectively constant ratio of approximately `0.0762195125` over observed records;
- the direct valuation-level difference does not reproduce `precios_diferencia`.

## 8. Status

**PARTIALLY FROZEN — DOCUMENTARY ENDPOINT ESTABLISHED; DEPOSITED VARIABLE IDENTIFIED; UPSTREAM CONSTRUCTION PROVENANCE GAP REMAINS.**

The appropriate next governed action is to preserve this limitation in the candidate-specific evidence record and, if empirical execution is later considered, resolve or explicitly freeze the remaining provenance conditions before authorization.
