# D-OPS-11 — Longitudinal State Archive Discovery / Railway Historical Data Recovery Audit v0.1

**Status:** CLOSED — HISTORICAL STATE CANDIDATE FOUND, BUT TGCV LONGITUDINAL IDENTITY REMAINS UNPROVEN
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Purpose

D-OPS-11 searches specifically for immutable or versioned historical railway-state resources that could close the longitudinal-state gap identified in D-OPS-10.

The search does not modify the EULYNX rule layer and does not authorize dataset download, parsing or experiment execution.

## 2. New historical resource identified

A public research dataset, **Railways of Spain GIS (1848–2023)**, provides six GIS files covering Spanish railway lines and stations across the historical period 1848–2023. It is version 1.0, published in 2023, open access under CC BY 4.0, with DOI `10.34810/DATA917`. citeturn0search8turn0search14

This is materially different from the ADIF catalogue snapshots: it is explicitly designed as a longitudinal historical GIS reconstruction rather than merely the current version of an infrastructure catalogue.

However, its temporal resolution and object semantics are historical-network reconstruction semantics, not necessarily the same infrastructure object model required by EULYNX signalling/interlocking.

## 3. Other archival evidence

The official ADIF catalogue confirms a 2018 version and a current July 2024 version of the INSPIRE railway transport network dataset. citeturn0search2turn0search0

The ADIF catalogue states temporal coverage from 2010-01-01 to 2024-01-31 for the current resource, while the 2018 catalogue entry identifies the April 2018 version. citeturn0search0turn0search2

The European Union Agency for Railways' RINF dataset explorer is stronger from a provenance perspective: it exposes datasets exactly as submitted by infrastructure managers, preserving traceability, and currently lists an ADIF RINF file for Spain. citeturn0search1

RINF also has a versioned technical application guide and ontology releases, with the current 2026 release explicitly identifying previous versions. citeturn0search12

## 4. Compatibility assessment

| Resource | Historical depth | Stable railway objects | Compatible with EULYNX signalling state | Potential TGCV use |
|---|---:|---:|---:|---|
| Railways of Spain GIS (1848–2023) | PASS | CONDITIONAL | FAIL/OPEN | Historical context / candidate longitudinal topology |
| ADIF 2018 + 2024 INSPIRE | CONDITIONAL | OPEN | CONDITIONAL | Candidate infrastructure snapshots |
| ERA RINF submitted datasets | PASS in provenance/versioning | CONDITIONAL | CONDITIONAL/PASS at infrastructure-attribute level | Strong archival candidate |

## 5. Critical result

D-OPS-11 improves the evidence base substantially, but it does **not** yet close the TGCV gate.

The key discovery is that historical railway state archives exist at multiple semantic layers:

1. historical network reconstruction (Railways of Spain GIS);
2. ADIF infrastructure network snapshots;
3. regulator-facing RINF infrastructure datasets with strong provenance/versioning.

The remaining problem is now precisely identifiable:

> Can one of these resources provide a **stable canonical state identity at the signalling/interlocking level** that can be evaluated under a frozen EULYNX rule subset at more than one time point?

The historical GIS dataset is too coarse/semantically different to answer this directly. ADIF INSPIRE is promising but object continuity is unresolved. RINF has the strongest provenance and version structure, but its current public explorer does not by itself establish the required historical multi-version series for the same Spanish infrastructure manager at the relevant semantic level.

## 6. Decision

**D-OPS-11 = CLOSED — NO EMPIRICAL SELECTION.**

Decision status:
- Historical longitudinal resources: **FOUND**;
- Immutable/versioned provenance: **PARTIALLY FOUND / strongest in RINF**;
- Stable signalling-level object identity across time: **NOT ESTABLISHED**;
- EULYNX-compatible longitudinal state: **NOT ESTABLISHED**;
- `ΔT_acc` empirical identifiability: **OPEN**;
- implementation: **NOT AUTHORIZED**;
- execution: **NOT AUTHORIZED**.

No scientific claim is upgraded.

## 7. Strategic consequence

The railway path should not be abandoned yet, because the rule-layer problem is substantially solved and the archival problem now has concrete candidate resources.

But the next operation must be narrower still: rather than another broad archive search, test whether **RINF's versioned infrastructure representation itself can supply a stable longitudinal state identity** for Spain, and whether a bounded EULYNX-compatible transformation universe can be mapped onto it without changing semantics.

## 8. Next controlled operation

Open **D-OPS-12 — RINF Historical Version / Object Identity Compatibility Audit**.

Focus:
1. identify historical RINF submissions for the same Spanish infrastructure manager;
2. determine whether multiple immutable submissions are publicly recoverable;
3. compare their schema/ontology versions;
4. identify persistent infrastructure object identifiers;
5. test whether those identifiers support exact state comparison;
6. determine whether a bounded EULYNX signalling/interlocking rule subset can operate on the resulting state representation;
7. only if all pass, define the minimum operational specification.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
