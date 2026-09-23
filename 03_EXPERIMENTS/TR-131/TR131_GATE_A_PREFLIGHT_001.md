# TR-131 — Gate A Preflight Record 001

**Status:** FIXTURE REJECTED — INSUFFICIENT FOR FORWARD OPERATIONALISATION  
**Date:** 2026-09-23  
**Candidate:** Healthcare treatment process / CPN process execution  
**Gate:** A — Cross-domain operationalisation

## 1. Purpose

This preflight verifies whether the selected healthcare-treatment fixture contains the source artifacts required to instantiate and independently reconstruct:

`S_t → T_acc,t → T_real,t → S_(t+1) → T_acc,t+1`

without retrospective inference from observed outcomes or future events.

## 2. Source verification

The 4TU.ResearchData record for **Mozafari Mehr, Azadeh (2023), Healthcare treatment process (logs and CPN model)** was independently checked through the publisher/repository record.

Verified:

- Version: **1**
- Versioned DOI: **10.4121/8683fc1a-aca1-447b-aba4-8d7806a9977f.v1**
- Publisher: **4TU.ResearchData**
- Original publication date: **2023-03-28**
- Licence: **CC0**
- Format: **RAR**
- Dataset description: simulated healthcare treatment process using a Colored Petri Net (CPN) model
- Published experiment archives: **9**
- Total uncompressed size reported by repository: **25,833,041 bytes**

## 3. Fixture integrity

The version-1 download was retrieved and its container SHA-256 was verified:

`370AD1822FE6CEB245188DE2750DD6B59E0ED9358A861287D35435CF5435B46C`

All nine published RAR archives were extracted without modification and matched the repository-reported MD5 values.

Fixture integrity is therefore **PASS**.

## 4. Artifact inventory

Each experiment contains the expected process/data/log artifacts. The process model is `processModel.pnml` and is **8,936 bytes in all nine experiments**.

Experiment0 contains:

- `DataLog.xes`
- `DataModel.csv`
- `OrganisationalModel.CSV`
- `processLog.xes`
- `processModel.pnml`

No additional model/configuration/simulation artifact was found in the extracted Experiment0 fixture. The same process-model filename and size are present across Experiments1–8.

## 5. Process-model semantics verified

The PNML is a Yasper EPnml model:

- Yasper version: `1.2.4020.34351`
- 12 places: `pl1`–`pl12`
- 12 transitions: `tr1`–`tr12`
- explicit input/output arcs
- transition names identify healthcare activities and organizational roles
- no explicit `initialMarking` element was found
- no guard, condition or inscription semantics were found in the inspected PNML
- `<text>true</text>` occurrences are `tokenCaseSensitive` settings and are **not initial tokens**

The process log begins with observed events such as `Identify patient (ip)` and `Admission (ad)`, but these observations do not constitute an independent specification of the initial marking.

## 6. Critical missing operational artifact

The frozen fixture does **not** provide an independent representation of the initial state/marking `S_0`.

Consequently:

`S_t → T_acc,t`

cannot be reconstructed forward from the frozen fixture alone, because enabled transitions require the current marking/state.

Likewise, a formal reconstruction of:

`T_real,t → S_(t+1) → T_acc,t+1`

cannot be established without independently specified state/update semantics.

## 7. Retrospective reconstruction is explicitly rejected

The first observed event in `processLog.xes` must **not** be used to infer that its input place was initially marked.

Doing so would make accessibility partly a consequence of the observed realization rather than an independently determined property of the current state.

## 8. Gate A assessment

| Dimension | Result | Reason |
|---|---|---|
| A1 — State operationalisation | **FAIL** | No independent `S_0`/marking representation |
| A2 — Accessibility operationalisation | **FAIL** | `T_acc` cannot be derived without `S_t` |
| A3 — Realization identity | **PASS** | Process events are explicitly identifiable |
| A4 — Successor-state reconstruction | **FAIL** | No independently frozen state/update semantics |
| A5 — Transformation-space evolution | **FAIL** | Requires A1/A2/A4 |
| A6 — Independent reproducibility | **NOT AUTHORIZED** | No scientific execution authorized on an insufficient fixture |
| A7 — Domain-boundary disclosure | **PASS** | Boundary is explicitly identified |

## 9. Decision

**GATE A — FAIL / FIXTURE INSUFFICIENT FOR FORWARD OPERATIONALISATION**

This is a **fixture-level failure**, not a finding that healthcare is unsuitable as a domain and not a failure of TGCV.

The dataset demonstrates explicit healthcare-process transition structure and executable event traces, but the published fixture as frozen here does not contain the independent state information required to demonstrate the TGCV analytical grammar without retrospective inference.

No scientific execution is authorized from this fixture.

## 10. Scientific boundary

This result does not establish or test:

- cross-domain validity of TGCV;
- cross-domain usefulness;
- Transformational Intelligence;
- outcome linkage;
- value linkage;
- causal `ΔT_acc → ΔValue`;
- ontological consequences;
- TGCV Core modification.

The result only establishes the operational boundary of this candidate fixture for Gate A.

## 11. Next research action

The healthcare fixture is **not promoted to Gate A execution**.

The next action is to select a new second-domain fixture using these hard pre-screen requirements:

1. explicit source-defined state representation;
2. explicit initial state;
3. source-defined transformation identity;
4. forward-computable accessibility predicate;
5. deterministic or independently specified successor-state rule;
6. observable realized transformation;
7. observable/reconstructible subsequent transformation space;
8. stable primary provenance;
9. independent reconstruction possible before scientific results are inspected.

The candidate-selection protocol remains unchanged except that these conditions are now treated as **hard pre-screen requirements**, not merely post-selection preflight questions.

## 12. Governance

No TGCV Core, Evidence→Claim Matrix, SIP gate status, or scientific claim is upgraded or downgraded by this fixture-level failure.

The canonical methodological rule remains:

> **Evidence first → conceptual differentiation second → ontological review third → Core modification only if warranted by accumulated evidence.**
