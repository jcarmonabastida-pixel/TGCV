# TGCV — VSL Experimental Protocol Integrity Audit 001

**Date:** 2026-09-19  
**Status:** CLOSED — PROTOCOLS NOT FROZEN / INTEGRITY CONDITIONS SATISFIED FOR FURTHER SPECIFICATION  
**Protocols:** A — Built Assets / Infrastructure LCC; B — Petroleum / Petrochemical / Natural-Gas LCC

## 1. Audit result

Both draft protocols preserve the required analytical separation and contain no detected circular dependency in their current architecture.

| Gate | A | B |
|---|---|---|
| Frozen VSL referenced | PASS | PASS |
| Value before outcome | PASS | PASS |
| Outcome independent of V* | PASS | PASS |
| T_acc independent of Outcome/V* | PASS | PASS |
| Reference before results | PASS | PASS |
| Trajectory rule independent of Value | PASS | PASS |
| Direction inherited from frozen VSL | PASS | PASS |
| Independent reconstruction required | PASS | PASS |
| Claim boundary preserved | PASS | PASS |
| Complete executable specification | BLOCKED | BLOCKED |

## 2. Interpretation

The audit does **not** authorize freezing or execution. The conceptual architecture is clean, but both protocols remain materially under-specified.

## 3. Mandatory unresolved fields

For both A and B, the following must be frozen before protocol approval:

- exact intervention/treatment;
- experimental population/context and unit-selection rule;
- admissibility predicate and operational construction of `T_acc`;
- assignment/randomization or deterministic assignment rule;
- sample/scenario generation and size/coverage rationale;
- exact control/null condition;
- exact trajectory-selection/execution mechanism;
- measurable Outcome construction;
- statistical/structural metrics and decision thresholds;
- missingness and uncertainty implementation;
- executable package and integrity hashes;
- independent Executor-2 reconstruction package;
- stopping/failure rules in operational form.

## 4. Important methodological finding

No Value circularity has been detected. Therefore the current blocker is **experimental identifiability/executability**, not Value-layer compatibility.

The frozen VSLs A and B can remain unchanged while the experimental protocol is completed.

## 5. Governance consequence

No changes to TGCV Core, C09, RMA, Evidence-to-Claim Matrix, VSL-SPEC-01, VSL-EXP-01 or the frozen domain-specific VSLs.

No experiment is authorized.

## 6. Next operation

Complete the unresolved operational fields for A and B, then run a second integrity audit against the fully executable bundles. Only a clean audit may lead to protocol freeze and execution authorization.