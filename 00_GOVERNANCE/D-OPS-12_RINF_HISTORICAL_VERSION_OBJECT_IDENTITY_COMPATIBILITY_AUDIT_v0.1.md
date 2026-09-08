# D-OPS-12 — RINF Historical Version / Object Identity Compatibility Audit v0.1

**Status:** CLOSED — RINF RETAINED AS A STRONG ARCHIVAL CANDIDATE; EMPIRICAL SELECTION STILL BLOCKED
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Scope

This audit tests the decisive remaining question from D-OPS-11: whether RINF can provide an auditable longitudinal state identity for the same Spanish infrastructure manager, and whether that representation can support a bounded TGCV transformation universe without semantic leakage.

No RINF dataset was downloaded or executed.

## 2. Evidence recovered

### 2.1 Historical retention is explicitly part of RINF

The consolidated RINF regulation states that the central RINF database makes infrastructure-manager data publicly available without modification and that the RINF application **retains the complete historical record of data made available by infrastructure managers**, with records stored for two years from withdrawal. It also requires timestamped exports and provides an API/open querying endpoint. citeturn1search3turn1search38

This is materially stronger than the evidence available at D-OPS-10: historical retention is not an accidental archival property; it is part of the governed RINF system.

### 2.2 Infrastructure objects have explicit identities and validity semantics

The ERA RINF Application Guide defines infrastructure elements as managed railway features including tracks, signals, switches, operational points, tunnels and sections of line. citeturn0search1turn0search24

The guide specifies URI generation for infrastructure elements using a hash derived from the object identifier, object type, track identifier and **validity dates**. citeturn0search25

This is important but creates a precise limitation: the RINF URI is not automatically a permanent object identifier independent of temporal validity. A change in the validity interval can produce a different URI even when the physical asset is conceptually the same.

### 2.3 The schema itself is versioned

RINF/ERA ontology releases are explicitly versioned. The current public ontology is v3.3.4, while v3.2.1 and v3.3.1 are separately browsable historical releases. The RINF application guide also exposes previous versions including v1.6.1. citeturn0search0turn0search1turn0search10

The older RINF guide remains publicly available, establishing that the rule/schema layer is historically reconstructible at least at specification level. citeturn0search26turn0search6

### 2.4 Infrastructure-manager identity is independently governed

RINF defines a four-character organisation code allocated by ERA for the infrastructure manager and states that it is a unique identifier verified nationally. citeturn1search0

Therefore a Spanish infrastructure-manager population can, in principle, be isolated without inferring identity from observed operations.

## 3. Compatibility assessment

| Criterion | Result | Finding |
|---|---|---|
| D12-1 Historical record existence | **PASS** | Historical retention is explicitly mandated by RINF. |
| D12-2 Public recoverability of historical records | **CONDITIONAL** | The legal/system specification requires retention, API/query access and public availability, but current public evidence does not demonstrate that arbitrary historical Spain/ADIF snapshots can be retrieved today beyond the retention window. |
| D12-3 Versioned ontology/schema | **PASS** | Multiple RINF/ERA ontology and guide versions are publicly identifiable. |
| D12-4 Infrastructure-manager identity | **PASS** | ERA-assigned organisation code provides governed IM identity. |
| D12-5 Object identity independent of outcome | **CONDITIONAL** | RINF defines object URIs, but URI construction incorporates validity dates; persistent physical-object identity across changing validity intervals is therefore not guaranteed by URI equality. |
| D12-6 Stable longitudinal object identity | **OPEN / NOT ESTABLISHED** | A cross-version identity relation must be reconstructed from the underlying object identifiers and semantics; it cannot be assumed from URI equality. |
| D12-7 State comparison | **CONDITIONAL** | Exact comparison is conceptually possible if historical records and an identity mapping are recovered. |
| D12-8 Independent `Uτ` | **CONDITIONAL** | RINF supplies a rich infrastructure object vocabulary, but the transformation universe must be independently frozen; it cannot simply be “all observed changes”. |
| D12-9 Non-trivial `Pτ` | **PASS/CONDITIONAL** | RINF contains technical characteristics and restrictions, including rules/restrictions documents; a bounded admissibility predicate can potentially be derived, but its exact scope must be frozen with EULYNX/engineering rules. citeturn1search1turn1search2 |
| D12-10 Reach separability | **CONDITIONAL** | Successor infrastructure configurations can be represented structurally once object identity and transformation scope are frozen. |
| D12-11 Reproducibility | **CONDITIONAL** | Specifications are strongly reproducible; historical data bytes remain the unresolved reproducibility component. |
| D12-12 Information gain beyond Rust | **PASS** | Railway infrastructure is an external engineering domain with a governed rule and regulatory layer. |

## 4. Decisive finding

D-OPS-12 changes the assessment of RINF materially:

> **RINF is not merely a current-state dataset. It is a governed, versioned infrastructure register with an explicitly retained historical record and machine-readable infrastructure semantics.**

This removes the previous assumption that longitudinality is unavailable in principle.

However, the decisive empirical requirement remains unresolved:

> **Can historical Spanish/ADIF RINF records actually be recovered now, and can their object identifiers be mapped across versions without retrospective manual interpretation?**

The validity-date-based URI construction makes this a real identity problem rather than a simple key lookup.

## 5. Decision

**D-OPS-12 = CLOSED — RINF RETAINED / NOT YET EXECUTION-READY.**

The railway path remains active because:
- independent rule layer: strong;
- governed longitudinal retention: confirmed;
- versioned schema: confirmed;
- infrastructure-manager identity: confirmed;
- historical object identity: unresolved;
- current historical data recoverability: unresolved.

No operational specification is frozen and no execution is authorized.

## 6. Next controlled operation

Open **D-OPS-13 — RINF Historical Retrieval Feasibility / Identity Mapping Preflight**.

This must be a **read-only feasibility audit**, not an experiment. It should determine whether the public RINF API/query interface or archived public exports permit retrieval of at least two historical Spain/ADIF records within the governed retention window, and whether their object identifiers/validity intervals permit deterministic identity mapping.

Required outcome is one of:
- **PASS:** two or more recoverable historical states with deterministic object identity;
- **CONDITIONAL:** historical states recoverable but identity mapping requires an explicitly frozen deterministic rule;
- **FAIL:** historical state recovery or identity mapping cannot be established.

Only a PASS/acceptable CONDITIONAL may justify a subsequent operational specification.

**REAL-DATA EXPERIMENT EXECUTION AUTHORIZED: NO.**
