# TGCV — EXT-UPD-4.3 Evidence-to-Claim Propagation Governance Correction v0.1

**Status:** CLOSED / GOVERNANCE CORRECTION
**Date:** 2026-09-09
**Scope:** Evidence-bearing closures, RMA propagation, Evidence-to-Claim Matrix, and external-asset batching
**Scientific state change:** NONE

## 1. Purpose

Persist and formalize the two-speed governance model required to keep TGCV scientifically consistent without turning control propagation into a bottleneck.

The operating principle is:

1. **Fast scientific control:** every material evidence-bearing closure is reflected in the Evidence-to-Claim Matrix and current scientific control surfaces.
2. **Controlled external communication:** `05_ASSETS` is updated in deliberate batches/windows rather than after every closure.

This correction does not alter TGCV ontology, evidence status, claim strength, or any scientific result.

## 2. Material evidence

For governance purposes, **material evidence** includes, at minimum:

- empirical/computational evidence;
- documentary or primary-source evidence;
- formal/mathematical evidence;
- comparative/prior-art evidence;
- translational/cross-domain evidence;
- operational or methodological evidence when it changes the evidential basis of a claim;
- negative, contradictory, or null evidence when it materially affects a claim or its status.

A material evidence item is not required to be empirical to trigger Evidence-to-Claim control.

## 3. Mandatory Evidence → Claim impact control

Every material evidence-bearing gate, decision, result, or closure MUST include an explicit **Evidence → Claim impact assessment** before its consistency closure.

The assessment shall produce one of:

- **IMPACT — UPDATE REQUIRED:** one or more claims/evidential bases change;
- **NO MATERIAL IMPACT:** the evidence is recorded but does not alter the current claim matrix;
- **N/A — NON-CLAIM-BEARING:** the artifact has no material claim-bearing consequence.

Silence is not an admissible substitute for the assessment.

Where `IMPACT — UPDATE REQUIRED` applies, the current matrix MUST be updated before the consistency closure. Where `NO MATERIAL IMPACT` or `N/A` applies, that determination MUST itself be recorded in the propagation artifact.

## 4. Fast scientific propagation path

The canonical minimum propagation sequence is now:

`Evidence / Decision / Gate / Closure`
`→ Evidence → Claim impact assessment`
`→ Evidence-to-Claim Matrix current version`
`→ RMA current master / pointer`
`→ STATUS`
`→ Traceability`
`→ CHANGELOG`
`→ machine consistency validation`
`→ consistency closure`

The exact order may be optimized operationally when commits are batched, but no required control surface may be silently omitted.

The Evidence-to-Claim Matrix current version/pointer is part of the control state.

## 5. Epistemic safeguard

Updating the Evidence-to-Claim Matrix does **not** automatically upgrade a claim.

Evidence propagation must preserve the distinction among:

- evidence availability;
- claim status;
- epistemic strength;
- unresolved/indeterminate state;
- scientific closure.

New evidence cannot silently strengthen, broaden, or universalize an existing claim. Any such change requires an explicit scientific decision/gate.

## 6. Historical matrices

All historical Evidence-to-Claim Matrix artifacts remain immutable historical records.

The existence of several versioned matrix files in `00_GOVERNANCE/` is therefore not, by itself, a defect. They form a historical chain.

A single current pointer/control artifact is established separately so that historical versions are not overwritten or ambiguously treated as current.

## 7. External assets — controlled batching

External deliverables under `05_ASSETS/` are **not required to be updated at every scientific closure**.

They SHALL instead be refreshed through explicit controlled batches/windows when:

- accumulated scientific changes materially affect an external deliverable;
- an external submission/review/application requires a current version;
- a planned communication milestone is reached; or
- governance explicitly calls for a refresh.

The external-asset lag MUST remain explicit and traceable. A current scientific state may therefore coexist temporarily with older external deliverables without being treated as a consistency failure, provided the lag is recorded and no external asset is represented as current when it is not.

## 8. Batch-update rule

When an external-asset refresh is initiated, the batch SHALL begin from the current RMA/claim state and perform an impact analysis across affected assets. The batch then receives its own propagation and consistency closure.

This prevents communication maintenance from becoming a per-experiment bottleneck while preserving scientific traceability.

## 9. Application to C-01

C-01 is a material **translational/documentary evidence item** and therefore requires Evidence → Claim impact control despite not being a conventional empirical dataset result.

The current matrix shall record:

- Gate A: PASS;
- Gate B: PASS;
- Gate C: PASS, bounded/partial translation;
- Gate D: INDETERMINATE;
- bounded support for translation of TGCV Core distinctions into an external engineering domain;
- no established full downstream `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` chain;
- no causal, predictive, value, universal, originality, or superiority claim.

## 10. Governance decision

This correction is a control-surface refinement, not a scientific revision.

It becomes the governing rule for subsequent evidence-bearing closures unless superseded by a later explicit governance decision.

**Next controlled operation:** reconcile the historical matrix chain into a current pointer, register C-01 in the current matrix, and propagate the resulting control state before returning to the C-01 Gate-D operationalization audit.
