# D-OPS-8 — Rule-Layer Discovery / Engineering-Constraint Search v0.1

**Status:** CLOSED — RAILWAY ENGINEERING RULE LAYER RETAINED AS PRIMARY CANDIDATE
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Strategic change

This gate implements the methodological change established after D-OPS-7:

> Search first for an independently governed rule/constraint system capable of defining `Pτ`; only afterwards search for longitudinal data compatible with that rule layer.

The dataset is no longer the starting point of candidate selection.

## 2. Rule-layer candidates reviewed

### A — European railway engineering / signalling

Europe's Rail publicly describes automated railway asset planning based on **harmonised EU planning and engineering rules related to track layout**, with EULYNX data models and reference planning projects. citeturn1search0turn1search8

The EULYNX System Pillar publishes versioned requirement specifications, interface specifications, models, simulators and conformance test cases. Multiple Baseline Set releases are publicly documented. citeturn1search9turn1search10turn1search13

European railway infrastructure rules are also formally represented in the EU RINF regulatory framework, which defines common characteristics for publishing infrastructure data and includes infrastructure rules and restrictions. citeturn1search7

Formal-methods literature demonstrates that railway infrastructure designs can be verified against standard regulations, including explicit safety constraints. citeturn0search14turn0search9

**TGCV potential:**
- `S`: railway infrastructure configuration/topology at a defined engineering level;
- `Uτ`: permitted infrastructure/configuration modifications;
- `Pτ`: formal engineering, interoperability and safety constraints;
- `T_acc`: modifications satisfying those rules before implementation;
- `Reach`: successor infrastructure configurations;
- `ΔT_acc`: change in admissible engineering transformations as infrastructure/rules/context evolve.

This is the strongest candidate because the rule layer exists independently of observed operational success.

**Disposition: RETAIN — PRIMARY CANDIDATE.**

### B — Rail infrastructure public data (ADIF/RINF)

Spain's ADIF railway transport network dataset is publicly catalogued under INSPIRE, with a current version identified in July 2024. citeturn1search2turn1search4 The resource provides a potentially useful state representation, while RINF provides a standardised regulatory data model. citeturn1search7

However, the current evidence establishes public state data, not yet a longitudinal version history at the required semantic level.

**Disposition: SUPPORTING DATA CANDIDATE — NOT YET SELECTED.**

### C — Railway interlocking formalization

A public TU Delft dataset provides railway interlocking topology and logic in RailML, with schema and example database. citeturn1search20

Strength: explicit formal structural/logic representation.

Blocker: identified dataset is a single temporal coverage rather than a longitudinal evolution corpus.

**Disposition: SUPPORTING RULE/STATE RESOURCE — NOT SUFFICIENT ALONE.**

### D — Manufacturing/product configuration rules

Industrial configuration systems explicitly use dependencies and constraints to define allowed feature combinations and product variants. Public documentation describes configuration models, super-BOMs/super-routings and technical constraints. citeturn1search36

Systems-engineering literature also explicitly studies system configurations and changes over time. citeturn0search3turn0search13

However, this candidate is close to the software/configuration family already considered in D-OPS-3 and therefore has weaker cross-domain information gain.

**Disposition: RETAIN AS SECONDARY, NOT PRIMARY.**

### E — Formal data-conformance rules

CDISC CORE is an explicitly machine-executable rules framework intended to make conformance rules transparent and consistent across the study lifecycle. citeturn0search8

Strength: excellent independent rule layer.

Blocker: the natural transformation universe concerns data/conformance operations rather than a domain whose transformation-accessibility dynamics are clearly analogous to TGCV's target phenomenon. Longitudinal state and Reach semantics are also not yet identified.

**Disposition: REJECT FOR CURRENT EMPIRICAL REPLICATION; retain as methodological reference.**

## 3. Comparative decision

| Rule layer | Independent Pτ | Versioned/public rules | Potential longitudinal state | Cross-domain gain | Decision |
|---|---:|---:|---:|---:|---|
| Railway engineering / signalling | PASS/CONDITIONAL | PASS | CONDITIONAL | PASS | **PRIMARY** |
| ADIF/RINF infrastructure data | PASS/CONDITIONAL | PASS | CONDITIONAL | PASS | Supporting data |
| RailML interlocking | PASS | PASS | FAIL/CONDITIONAL | PASS | Supporting resource |
| Manufacturing configuration | PASS | PASS | CONDITIONAL | CONDITIONAL | Secondary |
| CDISC conformance | PASS | PASS | CONDITIONAL | LOW/UNCLEAR | Reject |

## 4. D-OPS-8 conclusion

The strategy change materially improves candidate identification.

The strongest remaining route is now **railway engineering**, not because railway data are abundant, but because a separately governed rule layer exists that can potentially define `Pτ` before observing whether a transformation is executed or successful.

This is still a candidate, not an empirical selection. The decisive remaining question is whether the rule layer and a public longitudinal infrastructure representation can be joined without introducing circularity or changing the meaning of `T_acc`.

## 5. Next controlled operation

Open **D-OPS-9 — Railway Rule-Layer / Longitudinal-State Compatibility Audit**.

D-OPS-9 must focus on one concrete rule family and one concrete public state resource, and determine:

1. exact `S` and temporal unit;
2. exact rule release/version;
3. independently enumerable `Uτ`;
4. canonical transformation identity;
5. non-trivial pre-execution `Pτ`;
6. exact construction of `T_acc`;
7. longitudinal comparability of `S_t`;
8. downstream successor/Reach semantics;
9. provenance and reproducibility;
10. whether the resulting experiment would provide information genuinely beyond Rust.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
