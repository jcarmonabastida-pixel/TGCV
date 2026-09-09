# TGCV — D-OPS-24 Candidate-Pool Expansion / Empirical-Domain Discovery v0.3

**Status:** FROZEN / CORRECTED DISCOVERY PROTOCOL  
**Date:** 2026-09-09  
**Predecessor:** `D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.2.md`  
**Correction trigger:** EXT-UPD-3.8

## 1. Purpose

Provide a corrected, mechanically auditable protocol for the bounded documentary discovery of an independently observable empirical domain for D-OPS-24.

The v0.2 protocol is retained as historical protocol state. Its initial execution pass is non-admissible because its query-family budget was exceeded. v0.3 does not reinterpret that pass as compliant.

## 2. Scientific question

The frozen D-OPS-24 question remains unchanged:

> Can an independently specified domain translation be shown, by an ex-ante trace, to preserve the role and semantic distinctions of the frozen TGCV objects without importing outcome information, collapsing objects into native proxies, or silently changing operational meaning across the translation?

## 3. Mandatory scientific-memory gate

Before discovery, the operator must consult the current RMA/pointer, `02_EXTERNAL_SCIENCE/SCIENTIFIC_ASSET_REGISTRY_v0.1.md`, relevant `02_LITERATURE/` SLR history, D-OPS-24 reconstruction/design/preflight, candidate-domain eligibility audit, and the D1/D2/D3 prior-art boundaries.

No discovery may be represented as starting from scratch when relevant historical artifacts exist.

## 4. Scope

The same six source families are retained:

- F1 Organizational change / innovation systems
- F2 Physical/engineering reconfiguration systems
- F3 Biological/ecological adaptation or evolution
- F4 Scientific/technological design spaces outside software
- F5 Networked socio-technical systems outside software
- F6 Generative/design-production ecosystems outside software

Excluded unless reopened by a new versioned decision: software-package ecosystems substantially equivalent to Rust; MDE transformation frameworks already covered; self-adaptive/self-evolving software families already frozen as prior-art boundaries.

## 5. Query-family definition — corrected control

For v0.3, a **query family** is one pre-registered semantic search formulation for a source family, consisting of:

1. one fixed state-term set;
2. one fixed transformation-term set;
3. one fixed accessibility-term set;
4. one fixed temporal-term set;
5. optional native-domain terms explicitly listed before execution;
6. one fixed source-type restriction, if any.

Changing a term set, adding/removing a semantic group, changing the native-domain terms materially, or changing the source-type restriction creates a **new query family** and consumes one unit of the budget.

Pagination, opening results, following links, inspecting an identified primary source, and recording candidate evidence do **not** create new query families, provided the underlying query formulation is unchanged.

A query variant materially changing the formulation is a new query family even if it targets the same website or topic.

Every query family must be registered in the search log **before execution**, with a stable Q-ID.

## 6. Search budget

For each source family:

- maximum **3 pre-registered query families**;
- maximum **10 candidate records initially screened**;
- maximum 6 source families total.

The query-family budget is cumulative across the entire v0.3 execution. It cannot be reset per search engine, website, database, session or operator.

No retroactive reclassification may restore budget compliance.

## 7. Search execution order

For each source family:

1. register Q1, Q2 and Q3 formulations as applicable before execution;
2. execute Q1;
3. screen results until the candidate-screening budget is exhausted or a candidate reaches the documentary threshold;
4. proceed to Q2 only if required;
5. proceed to Q3 only if required;
6. stop the family once a candidate reaches the threshold or its budget is exhausted.

A query family may be omitted if prior results make it unnecessary. An omitted Q-ID remains unused.

## 8. Source hierarchy

Search may navigate peer-reviewed literature, established scholarly indexes, official dataset repositories/documentation, institutional repositories, authoritative project documentation and archival sources with stable provenance.

Candidate admission requires an inspectable primary or authoritative source whenever available. Snippets, secondary summaries, promotional material and rankings cannot alone admit a candidate.

## 9. Candidate admission threshold

A candidate may advance only when documentary evidence can potentially support:

1. stable unit;
2. longitudinal ordering;
3. independently constructible native `U_τ,D`;
4. non-circular accessibility;
5. `T_acc,D` membership;
6. `ΔT_acc,D` across states/time;
7. pre-outcome accessibility assessment;
8. explicit unresolved/empty cases;
9. Reach/Trajectory distinction;
10. Outcome separation;
11. provenance/reproducibility;
12. substantive non-redundancy;
13. potential C1–C5 auditability.

Failure of any mandatory condition prevents promotion.

## 10. Outcome-blind rule

Candidate selection cannot use Outcome, Value, performance, adoption, effect size, post-hoc TGCV conformance or convenience of a desired result.

Dataset availability may be recorded only as a feasibility attribute after the domain candidate is registered.

## 11. Hard exclusions

Exclude or hold candidates when accessibility is outcome-defined; longitudinal ordering is absent; transformations are not independently identifiable; `T_acc` collapses into a native possibility/adaptation/state-space construct; provenance is insufficient; the empirical representation is substantively redundant with TGCV work; admission depends on a favorable TGCV-like result; direct semantics are replaced by an impermissible proxy; the candidate belongs to a frozen prior-art family without a distinct question/representation; or dataset convenience is the principal selection reason.

## 12. Candidate records and provenance

Each screened candidate receives a stable ID and records source family, Q-ID, exact query formulation, timestamp, authoritative sources, native unit/state/transformation representation, temporal coverage, accessibility construction, `T_acc,D`, `ΔT_acc,D`, Reach/Trajectory, Outcome separation, provenance, DS-1–DS-14 preliminary status, C1–C5 preliminary status, leakage/collapse risks, mapping class, evidence gaps and decision reason.

## 13. Stopping rule

**A — RETAIN:** at least one candidate reaches the documentary threshold for a separate candidate-admission audit.

**B — NO ADMISSIBLE CANDIDATE:** all six families are screened within budget without a candidate reaching the threshold.

**C — GOVERNANCE STOP:** contradiction, prior-art, leakage, procedural nonconformance or other governance issue invalidates continuation.

If B or C occurs, no dataset acquisition or empirical execution follows. Any scope extension requires a new versioned scientific decision.

## 14. Required outputs

The operation must create in GitHub:

1. pre-registered search log;
2. candidate register;
3. candidate evidence matrix;
4. exclusion/prior-art record;
5. retained-candidate record, if any;
6. explicit stopping result;
7. next-gate recommendation.

## 15. Authorization boundary

Only documentary discovery is authorized under v0.3.

Dataset download: NOT AUTHORIZED.  
Dataset processing: NOT AUTHORIZED.  
Empirical execution: NOT AUTHORIZED.  
Outcome/model/value analysis: NOT AUTHORIZED.  
D-OPS-24 execution: NOT AUTHORIZED.

## 16. Non-claims

This protocol establishes no second-domain validation, cross-domain generalisation, translation conformance, causal or predictive validity, value linkage, originality or superiority.

It establishes only a corrected and auditable procedure for bounded candidate-domain discovery.
