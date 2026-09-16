# TGCV MT4-6 — Independent Reproducibility Protocol 001

**Status:** ANALYSIS PROTOCOL — NOT GOVERNANCE-NORMATIVE  
**Date:** 2026-09-16

## Objective

Test whether an independent executor can reproduce the bounded MT4 technical translation from the frozen source without relying on prior output values or interpretations.

## Frozen input

`TGCV_MT4_energy_public-dataset_v2.zip`  
SHA256: `691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

## Frozen technical candidate rule

For each country-technology-year cell, construct the CORE6 record from:

1. Fuel_efficiency
2. LF_min
3. LF_max
4. Peak_contr
5. Ramp_rate
6. Resource

A cell is `CORE6_COMPLETE` only when all six fields are nonblank. `Resource` is categorical. Numeric parsing must use invariant culture. No imputation is permitted.

## Independent executor boundary

The executor must use only:

- the frozen ZIP;
- this protocol;
- the stated CORE6 rule;
- the local execution environment.

The executor must not use prior audit outputs, collision lists, prior interpretations, or coaching about expected counts.

## Required outputs

The executor must independently report:

- total country-technology-year cells;
- complete CORE6 cells;
- incomplete CORE6 cells;
- coverage percentage;
- missingness by CORE6 parameter;
- number of country-year groups with >=2 complete technologies;
- number of such groups with >=2 distinct CORE6 signatures;
- number of groups containing duplicate CORE6 signatures;
- SHA256 of the frozen source.

## Decision rule

`MT4-6 PASS` requires exact reproduction of the frozen source hash and agreement of all deterministic structural counts with the prior independent audit, subject to formatting differences only.

Any disagreement requires reconciliation before MT4-6 can be closed.

This test does not establish full `P_tau` sufficiency. It tests reproducibility of the bounded technical translation only.
