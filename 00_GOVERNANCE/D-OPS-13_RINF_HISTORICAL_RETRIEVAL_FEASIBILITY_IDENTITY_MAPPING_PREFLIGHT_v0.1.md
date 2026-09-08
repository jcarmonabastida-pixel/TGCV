# D-OPS-13 — RINF Historical Retrieval Feasibility / Identity Mapping Preflight v0.1

**Status:** CLOSED — CONDITIONAL / HISTORICAL RETRIEVAL NOT DEMONSTRATED FOR ADIF
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Purpose

Determine whether the public RINF interface currently permits deterministic recovery of at least two historical Spain/ADIF datasets suitable for longitudinal TGCV state reconstruction, without executing or downloading an experiment dataset.

## 2. Evidence

The current official RINF Dataset Explorer exposes datasets exactly as submitted by Infrastructure Managers and provides country, Infrastructure Manager, organisation code, file name, size and publishing date. It also exposes Search, Map Explorer and a SPARQL endpoint. citeturn0search1

The current explorer visibly contains an ADIF Spain record:
- Infrastructure Manager: Administrador de Infraestructuras Ferroviarias
- Organisation code: 0071
- File: `RINF_ADIF_2026-03-20-17-46.xml`
- Size: 48.28 MiB
- Publishing date: 20 March 2026. citeturn0search1

The same explorer also contains historical submissions from other Infrastructure Managers reaching back to 2023/2024, demonstrating that the public explorer can expose older retained files in some cases. However, the visible ADIF record recovered in this audit is a 2026 submission; no second historical ADIF submission was independently established from the public explorer/search evidence used here. citeturn1search0

The governing RINF regulation requires the system to retain the complete historical record of infrastructure-manager data for two years from withdrawal and to provide search/retrieval functionality, timestamped exports and an API/open querying endpoint. citeturn0search0turn0search2

The historical RINF application guide also states that previous datasets are stored for two years but are not available through the normal RINF application interface, which creates an important distinction between **governed retention** and **currently public historical retrieval**. citeturn0search24

## 3. Identity mapping assessment

| Criterion | Result | Finding |
|---|---|---|
| D13-1 Current ADIF record recoverable | PASS | Organisation 0071 and a concrete 2026 dataset are publicly exposed. |
| D13-2 Second historical ADIF record publicly recoverable | FAIL / NOT DEMONSTRATED | Current public evidence did not establish a second ADIF submission sufficiently close in time and with retrievable file identity. |
| D13-3 Historical retention exists by governance | PASS | Retention is explicitly required for two years after withdrawal. |
| D13-4 Historical retrieval currently demonstrated | CONDITIONAL | Regulation requires retrieval/API capability, but the current public explorer evidence does not demonstrate arbitrary historical ADIF retrieval. |
| D13-5 Stable object identity | OPEN | Cannot be tested without at least two recoverable ADIF datasets. |
| D13-6 Deterministic cross-version mapping | OPEN | Depends on D13-5. |
| D13-7 Schema/version compatibility | PASS/CONDITIONAL | Current RINF ontology and technical annex are versioned and historical releases are public. citeturn0search3turn0search5turn0search6 |
| D13-8 Non-circular Pτ | CONDITIONAL | Rule layer remains independently definable through RINF/EULYNX; no empirical execution performed. |
| D13-9 Reproducibility | CONDITIONAL | Current dataset provenance is strong; historical ADIF byte-level provenance remains unproven. |
| D13-10 Information gain beyond Rust | PASS | External engineering/regulatory domain remains distinct. |

## 4. Decision

**D-OPS-13 = CLOSED — CONDITIONAL / HISTORICAL RETRIEVAL BLOCKER.**

The audit establishes that:

1. RINF is a genuinely governed longitudinal register.
2. The public system currently exposes an ADIF dataset with stable Infrastructure Manager identity (0071).
3. Public historical retrieval is not yet demonstrated for a second ADIF state.
4. Therefore object-identity continuity and exact longitudinal `ΔT_acc` remain untestable at this stage.

This is **not** a failure of RINF as a conceptual rule/state architecture. It is a failure to establish the minimum public historical retrieval condition required for empirical execution.

No operational specification is frozen and no execution is authorized.

## 5. Next controlled operation

Open **D-OPS-14 — RINF Historical Access Route Audit**.

The next step should investigate only the governed access routes already specified by RINF: public search/query, SPARQL/API, timestamped exports, and any documented historical-data access mechanism. The objective is to determine whether a second ADIF historical record can be retrieved without relying on web-search indexing or undocumented URLs.

If a second ADIF historical record cannot be recovered through the governed interface, the railway empirical path should be marked **BLOCKED FOR PUBLIC-ONLY REPLICATION** and the project should return to cross-domain discovery rather than inventing or manually reconstructing a historical state.

**REAL-DATA EXPERIMENT EXECUTION AUTHORIZED: NO.**
