# D-OPS-14 — RINF Historical Access Route Audit v0.1

**Status:** CLOSED — BLOCKED FOR PUBLIC-ONLY LONGITUDINAL REPLICATION
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Purpose

Determine whether the governed public RINF access routes can recover a second historical ADIF dataset required to establish longitudinal state identity.

## 2. Routes audited

### A — Public Dataset Explorer

The current RINF Dataset Explorer provides direct access to the most recently published datasets and states that files are available exactly as submitted. It exposes Search, Map Explorer and SPARQL access. citeturn1search0

The current public listing contains an ADIF Spain record, organisation code 0071, file `RINF_ADIF_2026-03-20-17-46.xml`, published 20 March 2026. citeturn1search0

The explorer also contains older submissions from other infrastructure managers, reaching back to 2023/2024, but no second ADIF historical submission was recovered through the public listing/search evidence used in this audit. citeturn1search0

**Result: CONDITIONAL/FAIL for ADIF historical recovery.**

### B — Public SPARQL endpoint

The RINF endpoint is publicly reachable and exposes the RDF knowledge graph, including infrastructure-element classes and canonical URI properties. citeturn1search2

However, the endpoint exposes the currently queryable knowledge graph; the audit found no documented public mechanism proving that arbitrary withdrawn ADIF snapshots can be selected as historical graph versions. This matters because querying current data cannot reconstruct a past state without an immutable historical dataset.

**Result: PASS for current-state queryability; FAIL for demonstrated historical snapshot retrieval.**

### C — RINF API / documented historical access

The current RINF documentation describes dataset management, search and SPARQL access, while ERA states that the former relational API was switched off as RINF moved to a knowledge graph and a new SPARQL-based API is under development. citeturn1search12turn1search5

The historical RINF guide explicitly states that only the last submitted dataset is available through the application and previous datasets are retained for two years but are not available through the normal RINF application interface. citeturn1search13

Therefore the existence of retention does **not** establish public retrieval of historical ADIF datasets.

**Result: FAIL for the required public historical retrieval condition.**

### D — Versioned RINF ontology / technical annex

Historical ontology and technical-annex releases are publicly identifiable, including v3.3.1, v3.3.2 and v3.3.4. citeturn1search3turn1search4turn1search6

This confirms reproducible rule/schema history, but schema history cannot substitute for missing historical data snapshots.

**Result: PASS for rule/schema reconstruction; insufficient for state reconstruction.**

## 3. Decision matrix

| Access route | Current ADIF | Historical ADIF | Deterministic object mapping | Decision |
|---|---:|---:|---:|---|
| Dataset Explorer | PASS | NOT DEMONSTRATED | OPEN | Fail for replication |
| SPARQL endpoint | PASS | NOT DEMONSTRATED | OPEN | Fail for replication |
| Documented API/history route | PASS/CHANGED | FAIL | OPEN | Fail |
| Versioned ontology/annex | PASS | PASS | N/A | Supporting only |

## 4. Decisive conclusion

**D-OPS-14 = CLOSED — BLOCKED FOR PUBLIC-ONLY LONGITUDINAL REPLICATION.**

The railway path has now passed the independent-rule-layer requirement but failed the public historical-state recovery requirement needed to construct an auditable longitudinal `S_t → S_t+1` population.

This is a **data-access limitation, not a theoretical falsification** and not evidence that railway systems cannot instantiate TGCV.

The governance consequence is strict:

- no manual reconstruction of a second ADIF state;
- no inference of historical state from current RINF data;
- no substitution of another infrastructure manager merely for convenience;
- no execution using a synthetic or reconstructed historical state while claiming empirical replication;
- no upgrade of the TGCV claim matrix.

## 5. Railway route disposition

**Railway empirical replication = BLOCKED under the public-only reproducibility requirement.**

EULYNX/RINF remain valuable as prior-art, rule-layer and methodological evidence. They do not currently provide an execution-ready external empirical domain.

## 6. Next controlled operation

Return to cross-domain discovery, but preserve the methodological filter established in D-OPS-8:

> Find an independently governed rule layer first, then require a genuinely public, versioned longitudinal state archive before selecting a domain.

Open **D-OPS-15 — Cross-Domain Rule-Layer + Longitudinal-Archive Discovery III**.

Priority should be domains where both assets are public from the outset, rather than domains where one must be inferred or recovered indirectly.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
