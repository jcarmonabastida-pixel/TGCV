# TR-132-MOD-1 — Evidence Manifest v0.1

**Fixture:** `MOD1-FX-001`
**Status:** FROZEN PRE-EXECUTION
**Role:** Package-integrity / provenance manifest
**Execution:** NOT AUTHORIZED

## Purpose

Freeze the provenance and semantic role of every evidence reference used by the pre-execution accessibility adjudication. These records are methodological inputs and controls; they are not empirical observations and must not be treated as execution results.

## Evidence records

| evidence_id | timepoint | candidate | evidence_class | role | source | status |
|---|---|---|---|---|---|---|
| E-A-t0 | t0 | TA | MATERIAL_SETUP | accessibility condition | FIXTURE_CONTROLLED | FROZEN |
| E-A-t1 | t1 | TA | MATERIAL_SETUP | accessibility condition | FIXTURE_CONTROLLED | FROZEN |
| E-B-t0 | t0 | TB | MATERIAL_SETUP | accessibility condition | FIXTURE_CONTROLLED | FROZEN |
| E-B-t1 | t1 | TB | MATERIAL_SETUP | accessibility condition | FIXTURE_CONTROLLED | FROZEN |
| E-C-t0 | t0 | TC | ADMISSIBILITY | exclusion control | FIXTURE_CONTROLLED | FROZEN |
| E-C-t1 | t1 | TC | ADMISSIBILITY | exclusion control | FIXTURE_CONTROLLED | FROZEN |
| E-D-t0 | t0 | TD | RESOURCE | accessibility condition | FIXTURE_CONTROLLED | FROZEN |
| E-D-t1 | t1 | TD | RESOURCE | accessibility condition | FIXTURE_CONTROLLED | FROZEN |
| E-E-t0 | t0 | TE | EVIDENCE | accessibility condition | FIXTURE_CONTROLLED | FROZEN |
| E-E-t1 | t1 | TE | EVIDENCE | accessibility condition | FIXTURE_CONTROLLED | FROZEN |

## Provenance rule

`FIXTURE_CONTROLLED` means the evidence record is instantiated from the frozen methodological fixture itself. It is not derived from transformation realization, downstream outcome, utility, or result inspection.

## Completeness rule

Every evidence reference appearing in the frozen accessibility adjudication must resolve to exactly one record in this manifest. No unlisted evidence reference may be introduced during execution.

## Non-circularity rule

Evidence records are fixed before empirical execution and before inspection of any execution result. Realization records are maintained separately and cannot establish accessibility.

## Integrity

This manifest is part of the frozen package and must be included in the immutable execution input manifest before any empirical result is generated.
