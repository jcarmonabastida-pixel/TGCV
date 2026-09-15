# TGCV — C10C-002 Value Endpoint Documentary Freeze 001

**Status:** PARTIALLY FROZEN — DOCUMENTARY ENDPOINT ESTABLISHED; FILE-LEVEL VARIABLE MAPPING PENDING
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Documentary endpoint established

The study's published methodological record specifies the independent real-estate endpoint as professional assessments of **raw land value / price per square meter for unbuilt lots**, measured at baseline and follow-up.

The assessors were professional property assessors from INDAABIN, evaluated the same unbuilt lots at baseline and follow-up, and were blinded to treatment assignment. The published analysis uses polygon-level averages of the assessed price per square meter.

The reported dependent variable is the **change in real-estate price per square meter, in real 2012 US dollars**, based on professional assessments.

The study reports 138 polygons with valuation observations and 342 polygons in the broader baseline experiment universe.

## 2. Why this is admissible for TGCV design

This endpoint is independent of the six structural infrastructure variables used to construct `T_acc*` and is therefore not outcome-defined accessibility. It provides an externally measured value endpoint suitable in principle for the C10-C value-linkage design.

## 3. Remaining file-level freeze

The exact V1 variable mapping is still required before empirical execution:

- exact variable name(s) in `real_estate_polygon_level.dta`;
- baseline/follow-up field mapping;
- exact unit and scale;
- missing-value codes;
- exact polygon aggregation already represented in the file versus reconstruction required;
- deterministic `ΔV` construction and hash of the extraction procedure.

These items must be recovered from the admitted V1 real-estate file/script, not inferred from the published table.

## 4. No execution authorization

This record does not authorize causal estimation. The previous C10C-002 negative bounded `ΔT_acc` experiment remains closed and unchanged.

## 5. Documentary source

The OpenICPSR V1 deposit contains `Habitat_Real_Estate_Replication_170830.do` and `real_estate_polygon_level.dta`; the deposit is distributed as received from the depositor. The published study documents the endpoint described above.
