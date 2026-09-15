# TGCV — C10C-002 B2 Endpoint Field / Unit / Time / Aggregation Freeze 001

**Status:** FROZEN — B2 DOCUMENTARY SPECIFICATION; EMPIRICAL EXECUTION NOT AUTHORIZED
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Purpose

Freeze the portion of the value endpoint definition that is directly supported by admitted V1 evidence, while explicitly preserving the irrecoverable upstream-construction limitation recorded in the endpoint provenance disposition.

## 2. Endpoint field

The primary deposited endpoint field is:

`precios_diferencia_usd`

It is the field directly consumed by the deposited real-estate replication script as the dependent variable in the property-price impact regressions and CDF analysis.

## 3. Economic unit

The documented economic interpretation is:

**change in professional real-estate price per square meter, expressed in real 2012 US dollars, at polygon level.**

The underlying professional assessments concern unbuilt lots and are attributed to INDAABIN professional assessors.

## 4. Time dimension

The documented study design compares professional assessments at baseline and follow-up, corresponding to the study's 2009 and 2012 valuation waves.

The deposited endpoint is therefore treated as a change endpoint spanning the baseline-to-follow-up period.

The exact upstream source-field construction of this change remains unresolved and is not inferred here.

## 5. Observation and linkage rule

The controlled V1 inspection established:

- total polygon panel universe: 342;
- polygons with observed valuation endpoint: 138;
- `any_precio=1`: 138;
- `any_precio=0`: 204.

The 138 observed endpoint polygons are the admissible endpoint-observation subset for any future execution using the deposited endpoint.

No imputation or outcome-derived completion rule is authorized.

## 6. Aggregation

The published methodological description identifies polygon-level averages of professional assessed price per square meter as the analysis unit.

The deposited `real_estate_polygon_level.dta` is therefore admitted as the polygon-level endpoint file.

Any additional aggregation or weighting operation must be frozen separately before execution; this record does not authorize one.

## 7. Explicit provenance limitation

This freeze does **not** establish the upstream formula for `precios_diferencia` or `precios_diferencia_usd`.

The prior controlled inspection established that:

`precios_diferencia != valor_co_12 - valor_co_09`

and that the replication script consumes rather than constructs the endpoint.

Consequently, the following remain non-admitted:

- inferred difference formulas;
- inferred deflators beyond documented interpretation;
- reconstructed missing values;
- post-hoc transformations of the endpoint.

## 8. Readiness disposition

**B2 is CLOSED for the directly documented field/unit/time/observation definition, with the upstream-construction limitation carried forward as an explicit constraint.**

This does not by itself satisfy full empirical-execution readiness.

Remaining readiness conditions are:

- B3 — interference/robustness rule;
- B4 — independent reproduction package;
- B5 — final script/specification hash.

The endpoint provenance limitation remains part of the admissibility record and must not be silently removed.

## 9. Governance boundary

This record:

- does not authorize causal estimation;
- does not reopen T17;
- does not repeat T10–T16-B;
- does not modify the frozen causal design;
- does not infer the endpoint construction formula;
- does not upgrade the C10C-002 candidate beyond `PROMISING / EVIDENCE GAP REMAINS`.

**Current candidate state: PROMISING / EVIDENCE GAP REMAINS.**
**Empirical causal execution: NOT AUTHORIZED.**
