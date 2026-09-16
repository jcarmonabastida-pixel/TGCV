# TGCV MT4-6 — Independent Reproducibility Result 001

**Status:** CLOSED — PASS (BOUNDED TECHNICAL TRANSLATION REPRODUCED)  
**Date:** 2026-09-16

## Frozen source

`TGCV_MT4_energy_public-dataset_v2.zip`  
SHA256: `691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

The independent executor reproduced the frozen source hash exactly.

## Reproduced structural results

| Measure | Independent result |
|---|---:|
| Country-technology-year cells | 13,320 |
| Complete CORE6 cells | 12,331 |
| Incomplete CORE6 cells | 989 |
| CORE6 coverage | 92.58% |
| Missing Fuel_efficiency | 89 |
| Missing LF_min | 0 |
| Missing LF_max | 0 |
| Missing Peak_contr | 0 |
| Missing Ramp_rate | 900 |
| Missing Resource | 0 |
| Country-year groups with >=2 complete technologies | 930 |
| Groups with >=2 distinct CORE6 signatures | 930 |
| Groups with duplicate CORE6 signatures | 1 |

These values reproduce the prior deterministic structural audit exactly.

## MT4-6 decision

**MT4-6 = PASS.**

The bounded technical translation based on CORE6 is independently reproducible from the frozen source and protocol. No prior audit output was required by the executor.

## Scope limitation

This PASS establishes reproducibility of the specified technical representation. It does **not** establish that CORE6 is sufficient to define full `P_tau`, nor that the resulting technical layer captures legal, institutional, social, economic, or other accessibility conditions.

The previously established status therefore remains:

`P_TAU_TECHNICAL = PARTIALLY_FORMALIZED`  
`P_TAU_FULL = UNDETERMINED`

## Next authorized step

Proceed to MT4-7: independent downstream separation, preserving the distinction between accessibility/technical admissibility, realized transformation, subsequent trajectory, outcome, and value.
