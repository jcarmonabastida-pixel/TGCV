# TR-131 — Cross-Domain Comparison Protocol Freeze 001

**Document ID:** TR131_CROSS_DOMAIN_COMPARISON_PROTOCOL_FREEZE_001  
**Status:** FROZEN — SCIENTIFIC EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-23  
**Repository:** jcarmonabastida-pixel/TGCV  
**Canonical source:** GitHub `origin/main`

## 1. Purpose

This protocol freezes the next TR-131 comparison before any interpretation of results.

The comparison uses only already-persisted evidence from:

- VisitAll `grid-5`, depth 2;
- PRISM Leader Sync `leader_sync3_2.pm`, bounded A6 reconstruction.

No new domain, fixture, source revision, or execution is introduced.

## 2. Scientific question

Can the same analytical procedure characterize transformation-space dynamics and future-possibility structure in two materially different domains, while preserving domain-specific semantics and without using outcomes or value to define accessibility?

The test is about cross-domain applicability of the analytical procedure, not representational superiority.

## 3. Frozen analytical record

Each reusable transition record is normalized only into these roles:

`S_t, T_acc,t, T_real,t, S_(t+1), T_acc,t+1, Delta_T_acc,t, H`

where:

`Delta_T_acc,t = (T_acc,t+1 \ T_acc,t, T_acc,t \ T_acc,t+1)`

and:

`H = (S_0,T_real,0,S_1,...,S_n)`

Domain-native semantics remain attached to every record.

## 4. Frozen descriptors

For every transition where both successive accessibility sets are available, calculate:

- `A_t = |T_acc,t|` — accessibility cardinality;
- `A_t+1 = |T_acc,t+1|`;
- `G_t = |T_acc,t+1 \ T_acc,t|` — newly accessible identities;
- `L_t = |T_acc,t \ T_acc,t+1|` — lost identities;
- `P_t = |T_acc,t ∩ T_acc,t+1|` — persistent identities;
- `R_t = G_t + L_t` — turnover;
- `D_t = A_t+1 - A_t` — net accessibility change.

These quantities are descriptive only. No sign or magnitude is assigned positive or negative value.

## 5. Identity rule

Raw transformation identities are not pooled across domains.

Within each domain, identity equality means equality under that domain's frozen transformation-identity rule. Set operations are performed only within a domain. Cross-domain comparison is performed on descriptor patterns and normalized structural relations, not on raw labels.

A VisitAll move is never declared equivalent to a PRISM action merely because both are labels.

## 6. Cross-domain comparison units

The primary comparison unit is the transition-space event:

`T_acc,t → T_real,t → S_(t+1) → T_acc,t+1`

The secondary unit is the trajectory segment.

The protocol compares:

1. whether each analytical role is instantiated;
2. whether accessibility changes can be represented;
3. whether realized transformations can be associated with subsequent accessibility changes;
4. whether alternative realizations can be represented as divergent future transformation-space trajectories;
5. whether the same descriptor grammar remains valid under both domain semantics.

## 7. Future-possibility endpoint

The primary non-outcome endpoint is **FPE — Future Possibility Exposure**.

For each admissible transition, record whether the realized transformation is followed by:

- expansion: `G_t > 0` and/or `D_t > 0`;
- contraction: `L_t > 0` and/or `D_t < 0`;
- turnover: `R_t > 0`;
- persistence: `P_t > 0`;
- stability: `G_t = L_t = 0`.

These descriptors are mutually non-exclusive. No descriptor is interpreted as beneficial.

## 8. Trajectory divergence

Where the frozen evidence contains multiple realizations from the same source state, compare their subsequent normalized descriptor sequences.

A divergence is recorded when two realizations from the same source state produce different subsequent transformation-space descriptor sequences.

The comparison does not require equal raw transformation labels across domains.

The endpoint is descriptive:

**trajectory-space divergence observed / not observed / not testable.**

## 9. Negative controls

Mandatory controls:

- **NC1 — VisitAll baseline reconstruction:** retain the known result that `T_acc` and `Delta_T_acc` are reconstructible from the native state/action baseline.
- **NC2 — Outcome independence:** no outcome, reward, VSL value, or downstream performance measure may enter construction of the analytical records or descriptors.
- **NC3 — Domain identity separation:** no cross-domain metric may depend on semantic equivalence between raw VisitAll and PRISM transformation labels.

## 10. Independence rule

This is a secondary analysis of frozen evidence, not a new executor experiment.

The analyst may transform persisted records mechanically according to this protocol but may not alter source semantics, transformation identities, select rows based on observed descriptors, introduce future outcomes, redefine accessibility after inspecting results, or omit contradictory records.

All inclusion/exclusion decisions must be made from frozen protocol scope, not from resulting values.

## 11. Utility probe

Record whether the common representation makes the following directly inspectable across both domains:

1. accessibility expansion/contraction;
2. transformation-space turnover;
3. persistence;
4. trajectory divergence;
5. transformation followed by reconfiguration of future accessibility.

The utility probe is not a subjective usefulness score. Results are **OBSERVABLE / NOT OBSERVABLE / NOT TESTABLE**.

## 12. Value/VSL separation

No VSL data are required for this protocol.

If independently available outcome/VSL evidence is later attached, it must remain downstream:

`transformation-space dynamics → trajectory → O → VSL → V*`

It may not be used retrospectively to alter accessibility or identity definitions.

The hypothesis `Delta_T_acc → Delta_Value` is outside this test.

## 13. Decision rule

**PASS — CROSS-DOMAIN ANALYTICAL APPLICABILITY** requires:

1. all core analytical roles operationally instantiated in both domains;
2. descriptors computed without semantic leakage;
3. at least one common structural analysis executable in both domains;
4. identity separation preserved;
5. no outcome/value leakage;
6. no protocol-dependent row selection.

**PASS WITH BOUNDARY:** same, with explicit domain-limited descriptors.

**FAIL:** the common procedure requires domain-specific semantic substitution that changes the analytical role.

**INCONCLUSIVE:** frozen evidence is insufficient.

**UTILITY NOT ESTABLISHED:** applicability is demonstrated but the utility probe yields no defensible cross-domain analytical use.

## 14. Interpretation boundary

A PASS does not establish representational superiority, ontological irreducibility, Transformational Intelligence as a new construct, causal `Delta_T_acc → Delta_Value`, predictive validity, value creation, value-guided optimal selection, or TGCV Core modification.

A negative result is equally admissible.

## 15. Execution authorization

**NOT AUTHORIZED by this document alone.**

Before analysis is run, the package must be checked against this frozen protocol for exact evidence-row availability and mechanical derivability.

The next gate is:

**CROSS-DOMAIN COMPARISON PACKAGE PREFLIGHT**

That preflight must establish that every required field and descriptor can be computed from already-frozen evidence without adding assumptions or reopening execution.

## 16. Governance

This protocol freezes the comparison specification. It does not modify VisitAll evidence, PRISM evidence, the PRISM fixture, Gate A decisions, TGCV Core, RMA, Evidence→Claim Matrix, or VSL.

No new scientific execution is authorized.
