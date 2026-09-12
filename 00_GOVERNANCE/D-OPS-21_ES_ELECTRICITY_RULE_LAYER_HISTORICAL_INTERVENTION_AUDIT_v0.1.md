# D-OPS-21 — ES Electricity Rule-Layer Historical Intervention Audit v0.1

**Status:** `COMPLETED — CANDIDATE NOT ADMITTED FOR C09 CAUSAL EXECUTION`
**Date:** 2026-09-12
**Execution:** `NOT AUTHORIZED`

## 1. Candidate

Spanish electricity-system regulated allocation / operation procedures, with particular attention to P.O. 7.5 and subsequent modifications.

The candidate is attractive because CNMC formally approves market rules and system-operation procedures, while REE publishes the operating procedures and a historical consultation archive. CNMC records multiple recent rule changes, including P.O. 7.5 in May 2026. The BOE describes P.O. 7.5 as regulating the active demand-response balancing service, including offer allocation by auction. [External evidence: CNMC/BOE/REE sources reviewed in discovery pass.]

## 2. Formal rule-layer assessment

**PASS — bounded.**

The P.O. 7.5 documentation defines admissible offers and an allocation algorithm. The 2025 rule specifies ordering and allocation constraints, including price ordering, divisibility, power and sequence criteria, and an aggregate ±5% requirement. The 2026 modification changes the allocation process and introduces a tolerance sensitive to cost gradient.

This supports a non-circular pre-execution representation of candidate transformations as offer/allocation actions and an admissibility predicate based on the published rule.

## 3. Historical intervention assessment

**PASS — documentary rule change.**

A pre/post rule boundary is clearly identifiable: P.O. 7.5 was approved in 2025 and modified by CNMC resolution of 11 May 2026. The modification explicitly states that it changes the allocation process and reinforces competition in future auctions.

## 4. C09 identification gate

### 4.1 Independent intervention assignment

**FAIL / NOT DEMONSTRATED.**

The rule change is externally imposed and institutionally governed, but it is a system-wide regulatory intervention rather than an independently assigned treatment across otherwise comparable decision units. Therefore it does not by itself provide the treatment/control structure required for a clean C09 causal estimand.

### 4.2 Intervention isolated to accessibility

**FAIL / NOT DEMONSTRATED.**

The 2026 modification changes allocation mechanics and associated tolerance/price-curve handling. It may change not only the admissible transformation space but also allocation outcomes, incentives and prices. The intervention therefore cannot presently be treated as a pure `Z → ΔT_acc` intervention with all other transition mechanisms held fixed.

### 4.3 Credible counterfactual

**OPEN — insufficient.**

A pre/post replay under frozen alternative rules could provide a structural counterfactual, but that would be a model/specification counterfactual rather than an observed causal counterfactual. A credible empirical control group has not been demonstrated.

### 4.4 Outcome leakage

**PASS — designable, not sufficient.**

The published rule can be specified from pre-decision variables without defining it from the subsequent trajectory. This preserves the information firewall at the rule-definition level, but does not solve treatment identification.

## 5. Decision

**D-OPS-21 = CLOSED — NO C09 EXECUTION CANDIDATE ADMITTED.**

The Spanish electricity rule-layer family is a strong demonstration of the missing formal component and may remain a methodological reference. It does not currently satisfy the complete C09 intervention-identification gate.

No C09 claim upgrade follows.

## 6. Refined discovery implication

The next search must require not merely an externally imposed rule change, but a setting in which exposure to the accessibility-changing rule can be independently determined across units, or where a credible quasi-experimental assignment exists, while the formal rule layer remains fixed enough to isolate `Z → ΔT_acc`.

Preferred next candidates should therefore have:

`versioned formal rule layer + longitudinal state + unit-level intervention assignment + unchanged transition environment + independent trajectory outcome`.

No empirical execution, data acquisition, model fitting, AWS mutation, Rust rerun or SWIM rerun is authorized.
