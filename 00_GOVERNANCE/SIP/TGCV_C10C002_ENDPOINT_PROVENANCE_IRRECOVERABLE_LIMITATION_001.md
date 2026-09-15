# TGCV — C10C-002 Endpoint Provenance Irrecoverable Limitation 001

**Status:** FROZEN — PROVENANCE LIMITATION FORMALLY RECORDED; EMPIRICAL EXECUTION NOT AUTHORIZED
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Purpose

Formally close the provenance-recovery attempt for the deposited real-estate endpoint using the admitted OpenICPSR 113705 V1 evidence, without inventing an upstream construction rule and without reopening the completed bounded causal experiment.

## 2. Evidence reviewed

The admitted evidence establishes:

- `real_estate_polygon_level.dta` is the deposited polygon-level real-estate file;
- `precios_diferencia_usd` is the dependent variable directly consumed by the deposited real-estate replication script;
- the published economic interpretation is change in professionally assessed real-estate price per square meter in real 2012 USD;
- 138 of 342 polygon observations contain the valuation endpoint;
- the replication script loads the endpoint as an existing field and does not construct `precios_diferencia` or `precios_diferencia_usd`;
- `precios_diferencia` is not equal to `valor_co_12 - valor_co_09`;
- recoverable Stata metadata inspected so far does not supply the missing construction formula.

## 3. Formal disposition

**B1 — ENDPOINT UPSTREAM CONSTRUCTION PROVENANCE: IRRECOVERABLE FROM ADMITTED V1 EVIDENCE REVIEWED SO FAR.**

This is an explicit provenance limitation, not an inferred reconstruction.

No formula for `precios_diferencia` or `precios_diferencia_usd` will be fabricated from observed values, correlations, conversion ratios, or the deposited level variables.

The constant empirical USD scaling relationship is retained only as an observed data property; it is not admitted as proof of the upstream construction procedure.

## 4. Consequence for C10-C

The endpoint remains **documented and identified**, but its upstream construction provenance is incomplete. Therefore:

- the candidate remains `PROMISING / EVIDENCE GAP REMAINS`;
- the endpoint may be referenced as the deposited study endpoint;
- no independently reconstructed endpoint formula is admissible;
- no causal execution is authorized on the basis of this record alone.

If future evidence from an admitted source recovers the provenance, it may be incorporated through a new controlled record. Such evidence must not be inferred from the outcome data themselves.

## 5. What this closes

This record closes the open-ended search for an endpoint formula within the currently admitted V1 script and recoverable file metadata.

It does **not** close the broader readiness gate, because the remaining conditions include endpoint field/time/missingness/aggregation specification, interference robustness, final script hash, and independent reproduction.

## 6. Governance boundaries

This record:

- does not modify the frozen C10C-002 causal design;
- does not reopen T17;
- does not repeat T10–T16-B;
- does not authorize a value regression;
- does not infer an endpoint formula;
- does not upgrade any TGCV claim.

## 7. Current state

**C10C-002: PROMISING / EVIDENCE GAP REMAINS.**

**B1: CLOSED AS AN IRRECOVERABLE PROVENANCE LIMITATION FROM ADMITTED V1 EVIDENCE.**

**EMPIRICAL CAUSAL EXECUTION: NOT AUTHORIZED.**

The next readiness work therefore moves to B2/B3/B4/B5 rather than repeating endpoint-formula reconstruction attempts.
