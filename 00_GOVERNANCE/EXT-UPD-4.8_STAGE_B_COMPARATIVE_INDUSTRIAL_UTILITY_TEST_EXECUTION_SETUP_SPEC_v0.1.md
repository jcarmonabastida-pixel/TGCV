# EXT-UPD-4.8 — Stage B Comparative IUT — Execution Setup Specification v0.1

**Status:** FROZEN / EXECUTION SETUP SPECIFICATION  
**Purpose:** define the exact local execution artefact to be generated next.  
**Execution:** local PowerShell only; GitHub remains canonical gate/provenance surface.

## 1. Execution rule

The Stage-B scientific execution is not performed by the governance document itself. A versioned Python executor must be generated in GitHub, retrieved locally, and executed from PowerShell.

The executor must emit a machine-readable result and preserve sufficient hashes/provenance for the execution result to be committed back to GitHub.

## 2. Primary executor

Required path:

`03_EXPERIMENTS/IUT-A-01/src/execute_iut_a01_stage_b_v01.py`

The executor is the primary controlled execution artefact.

## 3. Input model

The first execution must use a **self-contained synthetic/bounded case fixture derived only from the frozen Stage-A specification**, unless the execution record establishes that an existing local fixture already corresponds exactly to the frozen case.

No external outcome dataset is required for the primary IUT comparison.

The fixture must contain only decision-time information and the frozen native alternatives O1/O2/O3.

## 4. Required executor assertions

Before producing a comparative result the executor must verify:

- frozen case identifier;
- frozen option universe `{O1,O2,O3}`;
- RF-01 rule;
- no outcome fields are consumed during primary construction;
- identical decision-time input is supplied to baseline and TGCV;
- baseline specification is frozen;
- TGCV output schema is frozen;
- decision-relevance rule is frozen;
- no arbitrary option generation occurs;
- no optimization/recommendation objective is invoked.

Any failed assertion must produce `EXECUTION_RESULT=INDETERMINATE` and must not produce a positive IUT classification.

## 5. Baseline arm

The baseline must represent the frozen incumbent fixed/linear process-plan decision representation and output only the options it can identify from the permitted decision-time information.

Its procedure must be deterministic and auditable.

## 6. TGCV arm

TGCV must represent the same bounded option universe and evaluate decision-time accessibility/structural conditions without using downstream outcomes.

The executor must explicitly distinguish candidate option existence from accessibility and from later outcome.

## 7. Comparison

Primary comparison is option-space identification, not recommendation quality.

The executor must calculate:

- baseline identified option set;
- TGCV identified accessible option set;
- set difference in both directions;
- structural explanation records;
- decision-relevance classification.

A richer textual description without differentiated decision capability cannot yield IUT-2.

## 8. Outcome blindness

The primary execution fixture must contain no downstream performance/outcome values required for construction or comparison.

If an outcome field is present for later descriptive use, it must be inaccessible to the primary construction functions until after the primary result has been frozen.

## 9. Result classes

The executor may emit only:

- `IUT-0`
- `IUT-1`
- `IUT-2`
- `INDETERMINATE`

No IUT-3/IUT-4 classification is permitted.

## 10. Reproducibility

The executor must report:

- Python/runtime version;
- executor SHA-256;
- fixture SHA-256;
- deterministic execution identifier;
- input/output hashes where applicable;
- exact classification;
- assertion results;
- provenance.

## 11. Local execution convention

Expected invocation pattern:

`python .\03_EXPERIMENTS\IUT-A-01\src\execute_iut_a01_stage_b_v01.py`

The user executes this locally in PowerShell and returns the complete stdout/result to the research conversation.

## 12. Governance boundary

This setup specification does not itself constitute the execution result. No scientific claim is upgraded until the local result is inspected, recorded, impact-assessed, propagated and consistency-closed.

## 13. Next controlled action

Generate and commit the primary Python executor at the required path. Do not execute it in GitHub or infer its result from source inspection.
