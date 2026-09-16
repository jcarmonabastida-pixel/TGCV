# TGCV — MT5 Value Interpretation Reproducibility Protocol 001

**Date:** 2026-09-17  
**Status:** `FROZEN PROTOCOL — NOT EXECUTED`  
**Programme:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos

## 1. Purpose

Empirically test whether the Value Interpretation Layer `I_V` identified through MT5-07, instantiated in bounded form in MT5-08, reproduced methodologically across cases in MT5-09, and formalized as sufficiency conditions in MT5-10, can support independent reconstruction of a domain-bounded Value candidate `V*`.

This protocol tests reproducibility of the interpretation layer. It does **not** define a universal substantive Value, does not modify TGCV Core, and does not test the causal relation `ΔT_acc → ΔV`.

## 2. Case selection

**Primary case:** C09 / KGFS Rural Banking.

Selection basis: this case has the most complete currently closed bounded chain from randomized structural accessibility through downstream longitudinal outcomes, while preserving the separation between `T_acc` and downstream outcomes.

The protocol is single-case by design. Cross-case generalization is not inferred from this execution.

## 3. Frozen empirical evidence boundary

The independent analysts must receive only the frozen empirical evidence required to reconstruct the interpretation, together with the blank analysis worksheet. They must not receive prior MT5 interpretations, conclusions, candidate classifications, or coaching that could reveal the intended `I_V` or `V*`.

The frozen evidence package shall be composed from already-closed repository evidence, including:

- `00_GOVERNANCE/SIP/TGCV_C09_KGFS_D5A_CLOSURE_RECORD_001.md`
- `00_GOVERNANCE/SIP/TGCV_C09_KGFS_ACCESSIBILITY_TO_TRAJECTORY_BRIDGE_001.md`
- `00_GOVERNANCE/SIP/TGCV_C09_KGFS_TRAJECTORY_VARIABLE_AUDIT_001.md`
- the underlying frozen/provenance material necessary to identify the measured downstream outcomes and their temporal/reference structure.

The following are **protocol-development documents, not analyst-facing interpretation evidence** and must not be supplied to either analyst before their independent reconstruction:

- `TGCV_MT5_VALUE_INTERPRETATION_LAYER_CANDIDATE_001.md`
- `TGCV_MT5_VALUE_INTERPRETATION_INSTANTIATION_TEST_001.md`
- `TGCV_MT5_VALUE_INTERPRETATION_CROSS_CASE_REPRODUCIBILITY_TEST_001.md`
- `TGCV_MT5_VALUE_INTERPRETATION_SUFFICIENCY_GATE_001.md`

Before execution, the exact input bundle must be frozen and hashed.

## 4. Independent execution design

Two analysts, **Analyst 1** and **Analyst 2**, shall work independently.

Each analyst receives an equivalent frozen evidence package and an identical blank worksheet.

Constraints:

1. No communication between analysts during reconstruction.
2. No access to the other analyst's output before both outputs are frozen.
3. No coaching, hints, adjudication, or TGCV interpretation supplied during reconstruction.
4. No new evidence or new dataset may be introduced after the input bundle is frozen.
5. Analysts must reconstruct the interpretation from the supplied evidence, not from the protocol's expected result.
6. Each analyst must record unresolved ambiguities rather than silently resolving them through unstated assumptions.

## 5. Required analyst output

Each analyst must independently complete the following fields:

1. **Outcome `O`** — identify the downstream outcome actually measured.
2. **Reference entity** — identify the system, actor, household, beneficiary, population, or other entity to which the Value interpretation is attributed.
3. **Valuation objective** — state the substantive objective that makes the outcome Value-relevant.
4. **Direction** — specify the rule by which changes in the outcome are valued positively, negatively, or neutrally.
5. **Outcome-to-Value mapping `O → V*`** — specify how the measured outcome is interpreted as the Value candidate.
6. **Reference frame** — specify baseline/comparator, time horizon, population/domain frame, and any relevant counterfactual reference.
7. **Measurement rule** — specify the measurable estimand or rule used for the outcome and the proposed Value candidate.
8. **Non-circularity statement** — explain why the Value interpretation does not enter construction of `T_acc`.
9. **Domain-boundedness statement** — state the domain and why the interpretation is not being promoted to a universal TGCV primitive.
10. **Candidate `V*`** — provide the resulting domain-bounded Value candidate in the most explicit reproducible form supported by the evidence.

## 6. Reproducibility criterion

The comparison shall distinguish:

- **Exact agreement:** same substantive interpretation and materially equivalent representation.
- **Material agreement:** wording or representation differs, but reference entity, objective, direction, mapping, reference frame and measurement rule are substantively equivalent and lead to the same `V*`.
- **Material divergence:** analysts differ on one or more fields in a way that changes the resulting `V*`, its reference entity, valuation objective, direction, or mapping.
- **Underdetermination:** the supplied evidence does not permit an analyst to specify a field without importing an external or unstated normative assumption.

A structured or multidimensional `V*` is acceptable; reproducibility does not require a universal scalar or monetary measure.

## 7. Adjudication procedure

Adjudication begins only after both analyst outputs have been independently frozen.

The adjudication record shall:

1. compare all ten required fields;
2. identify exact, material, and divergent elements;
3. distinguish evidence-supported content from analyst-added assumptions;
4. identify whether any divergence is caused by incomplete frozen evidence;
5. determine whether both analysts recover the same domain-bounded `V*` without coaching.

No adjudication may rewrite either analyst's original output.

## 8. Decision classes

The execution shall terminate in one of four bounded classes:

- `PASS — REPRODUCIBLE DOMAIN-BOUNDED V*`
- `PARTIAL — RECONSTRUCTION DIVERGENCE`
- `FAIL — I_V INSUFFICIENT`
- `BLOCKED — INSUFFICIENT FROZEN EVIDENCE`

`PASS` requires independent reconstruction of materially equivalent `V*` together with adequate support for S1–S10.

`PARTIAL` applies where the interpretation architecture is recoverable but one or more material fields diverge.

`FAIL` applies where independent analysts cannot reconstruct a sufficiently explicit `V*` from the frozen specification without importing unresolved assumptions.

`BLOCKED` applies when the frozen evidence package itself is insufficient to perform the protocol as specified.

## 9. Governance boundary

This protocol is a **frozen experimental design only**. Its existence does not upgrade any TGCV claim.

Regardless of the execution result:

- no Core modification is authorized by this protocol alone;
- no RMA modification is authorized by this protocol alone;
- no Evidence→Claim Matrix upgrade is authorized by this protocol alone;
- no universal substantive definition of Value is authorized;
- no causal claim `ΔT_acc → ΔV` is authorized.

If `PASS` is obtained, the result supports bounded empirical reproducibility of a domain-specific Value interpretation procedure. It does not establish transversal substantive invariance of Value.

## 10. Execution sequence

**MT5-11a — Freeze input bundle and hashes.**  
Create the exact analyst-facing evidence package and record hashes.

**MT5-11b — Independent Analyst 1 execution.**  
Execute without access to Analyst 2 or prior MT5 interpretation artifacts.

**MT5-11c — Independent Analyst 2 execution.**  
Execute independently under the same evidence boundary.

**MT5-11d — Cross-output adjudication.**  
Compare frozen outputs only after both are complete.

**MT5-11e — Closure record.**  
Record the bounded result and governance disposition.

## 11. Current disposition

**`FROZEN PROTOCOL — NOT EXECUTED`.**

The next authorized operation is **MT5-11a: freeze the exact analyst-facing evidence bundle and record its hashes**.
