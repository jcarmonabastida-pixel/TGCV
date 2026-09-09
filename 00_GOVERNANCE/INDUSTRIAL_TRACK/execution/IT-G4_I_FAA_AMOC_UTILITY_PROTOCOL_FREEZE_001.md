# IT-G4-I — FAA AMOC Utility Protocol Freeze 001

**Date:** 2026-09-09  
**Status:** CLOSED — IT-G4 PASS (PROTOCOL FROZEN)  
**Case:** IT-G1-I-AMOC-US-91-12-10-7K0-18-00734  
**Gate:** IT-G4 — Utility Protocol Freeze

## 1. Purpose

Freeze, before any comparative outcome assessment, the industrial utility question, comparator, metrics, decision horizon, and PASS/FAIL/INCONCLUSIVE rules for the bounded FAA AMOC case.

FAA describes an AMOC as an alternative way to address the unsafe condition specified by an AD, and notes that AMOCs may also accommodate product changes or business processes while maintaining an acceptable level of safety. citeturn0search2turn0search22

## 2. Decision task

The bounded analytical task is:

> Given the frozen AD/AMOC case and the independently closed accessibility conditions, can an analyst reconstruct the admissible compliance alternatives and their constraints sufficiently to support the compliance decision without relying on post-decision outcomes?

This is an analytical utility question. It is **not** a claim that TGCV is superior, causal, predictive, safer, cheaper, or value-generating.

## 3. Comparator freeze

**Primary comparator:** the conventional AD-prescribed compliance method as defined by AD 91-12-10, evaluated from the same frozen decision-time evidence boundary.

**TGCV condition:** representation of the case using the TGCV industrial-track chain, beginning with the reconstructed system/context and accessibility conditions and identifying the change in accessible transformations.

**Comparator condition:** conventional regulatory/engineering reconstruction using the AD requirement and documented compliance alternative without invoking TGCV constructs.

No post-decision operational outcome may be used to select, redefine, or strengthen either comparator.

## 4. Utility dimensions

The following dimensions are frozen:

1. **Decision-relevant coverage:** proportion of mandatory case constraints and admissible alternatives correctly represented.
2. **Reconstruction completeness:** proportion of pre-specified required decision variables recovered without unsupported inference.
3. **Constraint traceability:** proportion of represented constraints traceable to an identified authoritative source.
4. **Reproducibility:** independent analyst ability to reproduce the same accessibility classification and transformation representation from the frozen evidence package.
5. **Analytical effort:** documented analyst effort/time required to produce the representation.

`ΔT_acc` itself is **not** a utility metric. It is an analytical object whose correct reconstruction is evaluated separately from practical utility.

## 5. Measurement protocol

For each method, the analyst shall complete a fixed case worksheet containing the same mandatory fields:

- case identity;
- system/product boundary;
- decision-time state/context;
- baseline AD requirement;
- alternative method;
- enabling conditions;
- limiting conditions;
- applicability restrictions;
- temporal conditions;
- evidence source for each field;
- indeterminate fields, if any;
- resulting accessibility classification.

A field receives full credit only if its content is supported by the frozen evidence package or is explicitly marked indeterminate. Unsupported inference receives no credit.

## 6. Frozen scoring rules

For dimensions 1–3, score is:

`score = correctly supported mandatory fields / total mandatory fields`

For reproducibility, two independent reconstructions are compared field-by-field.

For analytical effort, record elapsed analyst time using the same start/stop definition for both methods. Effort is descriptive and is not sufficient alone to establish utility.

## 7. PASS / FAIL / INCONCLUSIVE

### PASS
A comparative utility PASS requires all of:

- no critical validity failure;
- decision-relevant coverage ≥ 0.90;
- reconstruction completeness ≥ 0.90;
- constraint traceability ≥ 0.90;
- reproducibility agreement ≥ 0.90;
- and at least one practically relevant improvement over the comparator without a compensating critical loss in another mandatory dimension.

### FAIL
A FAIL is permitted only if all validity conditions are satisfied and at least one pre-specified utility threshold is determinately missed.

### INCONCLUSIVE
INCONCLUSIVE is mandatory if a critical evidence dependency remains unresolved, the independent reconstructions cannot be validly compared, or any required metric cannot be measured under the frozen protocol.

No threshold may be relaxed after observing results.

## 8. Outcome boundary

Post-decision aircraft operation, safety events, maintenance cost, downtime, financial benefit, fleet performance or other downstream outcomes are **not** used to define the IT-G4 utility metric. If later examined, they belong to a separate outcome/value evidence class and cannot retroactively alter this protocol.

## 9. Execution status

This artifact freezes the protocol only. It does **not** authorize execution.

The Industrial Track governance specification requires IT-G5 authorization after IT-G0 through IT-G4 are closed. fileciteturn515file0

Current gate result:

**IT-G4-I = PASS — UTILITY PROTOCOL FROZEN.**

## 10. Routing

Next permissible operation: **IT-G5 Execution Authorization review**.

No comparative execution, utility result, causal inference, value claim, partner evidence, new dataset execution, Rust/EXT-1.1 execution, O3, Stage-C/D, or Core modification is authorized by this record.
