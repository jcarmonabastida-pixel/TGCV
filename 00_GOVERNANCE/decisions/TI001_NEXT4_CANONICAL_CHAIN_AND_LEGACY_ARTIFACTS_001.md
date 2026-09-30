# TI-001 NEXT4 — Canonical chain and legacy artifacts

**Status:** GOVERNANCE MARKER — ACTIVE  
**Date:** 2026-10-01

## Purpose

This file prevents historical NEXT4 design artifacts from being treated as the current scientific contract.

## Current canonical NEXT4 chain

The current scientific chain is:

1. **DGP-002** — `TI001_V012_NEXT4_DGP_SPECIFICATION_002.json`
2. **Engine-002** — `TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py`
3. **Model-011R** — `TI001_V012_NEXT4_TWO_SURFACE_MODEL_011R.py`
4. **Execution Spec-002** — `TI001_V012_NEXT4_POWER_SIMULATION_EXECUTION_SPECIFICATION_002.json`
5. Monte Carlo execution and its canonical 40-cell aggregation/audits
6. Subsequent reconciliation/audit artifacts that explicitly reference Engine-002 + Model-011R

These artifacts supersede earlier NEXT4 statistical/DGP/model specifications where the newer artifact explicitly declares supersession.

## Historical / non-current artifacts

The following must **not** be used as the current NEXT4 scientific contract:

- `TI001_V012_NEXT4_DGP_SPECIFICATION_001.json`
- `TI001_V012_NEXT4_POWER_SIMULATION_DGP_SPECIFICATION_001.md`
- `TI001_V012_NEXT4_POWER_SIMULATION_EXECUTION_SPECIFICATION_001.json`
- `TI001_V012_NEXT4_PRIMARY_ESTIMAND_MODEL_010_SPECIFICATION_001.md`
- `TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_001.py`
- `TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py` **only where an artifact explicitly supersedes it with the current Engine-002 chain; do not infer Model-010 equivalence from historical audits**
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_008.py`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_009.py`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_010.py`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_011.py`
- `TI001_V012_NEXT4_ACTION_PROFILE_SURFACE_CONTRAST_MODEL_006.py`
- `TI001_V012_NEXT4_ACTION_PROFILE_SURFACE_CONTRAST_MODEL_007.py`
- `TI001_V012_NEXT4_ACTION_PROFILE_SURFACE_CONTRAST_AUDIT_006.json`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_008_AUDIT_001.json`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_009_AUDIT_001.json`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_009_IDENTIFIABILITY_AUDIT_001.json`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_009_NUMERICAL_AUDIT_001.json`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_010_IDENTIFIABILITY_AUDIT_001.json`
- `TI001_V012_NEXT4_TWO_SURFACE_MODEL_011_IDENTIFIABILITY_AUDIT_001.json`
- `TI001_V012_NEXT4_ENGINE_002_POWER_SIMULATION_MODEL_010_IMPLEMENTATION_EQUIVALENCE_AUDIT_001.json`
- `TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002_MODEL_010_IMPLEMENTATION_EQUIVALENCE_AUDIT_002.json`

The following early empirical-design specifications are also historical and must not be treated as the implementation contract for the current Spec-002/Model-011R chain:

- `TI001_V012_NEXT4_EXPERIMENTAL_SPECIFICATION_001.md`
- `TI001_V012_NEXT4_FIXTURE_ARCHITECTURE_AND_ANALYSIS_SPECIFICATION_001.md`
- `TI001_V012_NEXT4_FUTURE_STRUCTURE_GENERATOR_NULL_CONTROL_SPECIFICATION_001.md`
- `TI001_V012_NEXT4_FUTURE_STRUCTURE_SCHEMA_AND_PERMUTATION_PLAN_001.md`
- `TI001_V012_NEXT4_FUTURE_STRUCTURE_SEMANTIC_CONTROL_SPECIFICATION_001.md`
- `TI001_V012_NEXT4_MAPPING_SIGNAL_AND_PRIMARY_CONTRAST_IMPLEMENTATION_001.py`
- `TI001_V012_NEXT4_BALANCED_ALLOCATION_001.py`
- `TI001_V012_NEXT4_DESIGN_MATRIX_AND_PRIMARY_CONTRAST_001.py`
- `TI001_V012_NEXT4_DGP_AUDIT_001.py`

## Interpretation rule

A historical artifact may be retained for provenance, comparison, or audit lineage, but it must **never be selected as the operative NEXT4 specification merely because its filename appears newer than another historical artifact**.

For scientific execution, the operative contract must be traced explicitly to **DGP-002 + Engine-002 + Model-011R + Execution Spec-002**.

## Important distinction

This marker does **not** delete or rewrite historical artifacts. It records their status so provenance is preserved while preventing accidental reuse.
