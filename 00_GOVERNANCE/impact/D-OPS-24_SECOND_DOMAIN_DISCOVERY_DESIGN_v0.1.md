# D-OPS-24 — Second Independent Domain Discovery Design v0.1

**Date:** 2026-09-09
**Status:** FROZEN / DESIGN — PREflight REQUIRED; EXECUTION NOT AUTHORIZED
**Parent decision:** EXT-UPD-4.6
**Governing protocol:** D-OPS-24 v0.5

## 1. Purpose

Identify a genuinely independent candidate domain capable of supporting a later translational test of the frozen TGCV distinctions, without selecting the domain because it is expected to confirm TGCV and without requiring downstream Reach/Trajectory/Outcome/Value evidence at discovery stage.

## 2. Independence boundary

A candidate domain is not admissible as the second independent domain if its principal evidence is materially derived from:

1. Rust/package-management ecosystems already used in TGCV;
2. aircraft/control-system reconfiguration represented by C-01;
3. a previously used TGCV domain instantiation or a domain whose native analytical objects are materially imported from those instantiations;
4. an evidence construction whose eligibility depends on an expected TGCV-positive result.

Independence is assessed from provenance and native domain structure, not merely from a different dataset name.

## 3. Discovery principles

- outcome-blind discovery;
- native terminology first;
- TGCV terminology is not used as a selection criterion where it could bias discovery;
- discovery is documentary before empirical;
- no dataset download or processing during discovery;
- candidate selection precedes operational translation;
- zero-result is recorded as zero-result, never as absence or disproof;
- prior historical records are consulted before declaring any candidate genuinely independent.

## 4. Candidate families

The discovery pass will consider multiple genuinely distinct families rather than committing in advance to a preferred domain. Candidate families are only discovery strata, not claims of eligibility:

F1 — biological/ecological adaptive systems
F2 — technological infrastructure/network reconfiguration
F3 — manufacturing/process reconfiguration
F4 — organizational/coordination systems
F5 — software systems outside package-management/runtime ecosystems
F6 — socio-technical platforms and configuration systems
F7 — physical/environmental systems with documented feasible state changes
F8 — other native systems meeting the frozen MTE prerequisites

A family may be rejected without being exhausted if its candidates fail independence or MTE prerequisites.

## 5. Discovery query controls

The v0.5 staged architecture is preserved. Search execution requires a separately authorized query-family record.

For the discovery design, each query family shall use fixed terms for:

1. native state/configuration/structure;
2. native transformation/change/reconfiguration/operation;
3. feasibility/accessibility/admissibility/constraint;
4. temporal ordering/repeated observation;
5. optional native-domain terms;
6. fixed source restrictions.

Maximum execution budget for the first controlled discovery release:

- **12 query families total**;
- **30 candidate records total**;
- maximum **3 query families per candidate family**;
- cumulative budget, no reset;
- material query changes consume a new query family;
- pagination and inspection of a retrieved primary source do not constitute new query families.

The exact queries are frozen only in the execution-authorization record, after preflight.

## 6. Stage A — Independence and basic documentary eligibility

For each candidate record:

A1. stable native domain/system `S_D` identifiable;
A2. native provenance independently established;
A3. candidate is outside Rust and C-01 aircraft/control domain;
A4. no material dependency on a prior TGCV instantiation;
A5. native transformation/change operation identifiable;
A6. no outcome-defined accessibility requirement;
A7. sufficient documentary evidence to proceed to MTE screening.

Failure at A3 or A4 rejects the candidate as non-independent. Other failures may yield REJECT or INDETERMINATE depending on evidence completeness.

## 7. Stage B — Minimum Translation Eligibility (MTE)

Apply D-OPS-24 v0.5 MTE-1..MTE-10 without weakening them:

- MTE-1 stable S;
- MTE-2 independent Uτ,D;
- MTE-3 non-circular Pτ,D;
- MTE-4 constructible T_acc,D;
- MTE-5 ordered states for ΔT_acc,D;
- MTE-6 no outcome-defined accessibility;
- MTE-7 native/TGCV distinction;
- MTE-8 provenance;
- MTE-9 unresolved/empty;
- MTE-10 non-redundancy.

Discovery does not require Reach, Trajectory, Outcome or Value evidence.

## 8. Stage C — Translation Readiness

Only candidates passing Stage B may proceed to TR-1..TR-3:

- TR-1 native worked example with at least two distinguishable candidate transformations from one state;
- TR-2 accessibility assessable before outcome;
- TR-3 observed transition not equated with accessibility.

## 9. Candidate decision classes

Each candidate receives one of:

- **ELIGIBLE FOR TRANSLATION TRACE**;
- **REJECTED — NON-INDEPENDENT**;
- **REJECTED — MTE FAILURE**;
- **INDETERMINATE — INSUFFICIENT DOCUMENTARY BASIS**.

No candidate is promoted because it appears likely to produce a positive result.

## 10. Selection rule

If multiple candidates become eligible, the next selection shall be based on pre-registered documentary criteria such as independence strength, constructibility, provenance completeness and translational clarity. No observed outcome, performance result or expected TGCV confirmation may be used as a selection criterion.

If no candidate is eligible, the result is a bounded discovery outcome and requires a new governance decision before changing the protocol or opening another discovery route.

## 11. Evidence governance

Every material candidate-screening result that affects a claim or gate receives an explicit Evidence→Claim impact assessment before consistency closure.

## 12. Execution boundary

This document authorizes **no search execution**. It is a design artifact only. Preflight must verify independence controls, budget accounting, MTE preservation, outcome blindness, historical consultation, and authorization separation before execution is released.

## 13. Next step

Create and execute the dedicated preflight. Only a successful preflight followed by an explicit execution authorization can release the controlled discovery search.
