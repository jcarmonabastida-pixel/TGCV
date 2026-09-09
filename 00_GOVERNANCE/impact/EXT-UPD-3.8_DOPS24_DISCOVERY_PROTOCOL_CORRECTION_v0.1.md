# TGCV — EXT-UPD-3.8 D-OPS-24 Discovery Protocol Correction v0.1

**Status:** CLOSED / CONSISTENT  
**Date:** 2026-09-09  
**Trigger:** Protocol-budget nonconformance detected during initial D-OPS-24 documentary discovery  
**Predecessor:** EXT-UPD-3.7

## 1. Purpose

Regularize the D-OPS-24 documentary-discovery operation after the initial exploratory pass exceeded the query-family budget frozen in `D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.2.md`.

The correction preserves the deviation instead of retroactively treating the search as protocol-conformant.

## 2. Finding

The frozen protocol limited discovery to a maximum of three query families per source family. The initial discovery pass exceeded that bound for multiple source families.

Accordingly, the pass cannot be treated as a valid execution of v0.2.

## 3. Corrective decision

The nonconforming pass is closed as **exploratory / non-admissible**.

Its search observations may inform the design of a subsequent protocol, but they do not constitute candidate admissions, retained-domain evidence, or a valid bounded discovery result.

No candidate is selected from the pass.

## 4. Scientific-state protection

The correction changes no scientific object, claim, evidence level, empirical result, domain selection, conformance result or gate closure.

The following remain unchanged:

- Core `S`;
- analytical `T_acc` and `ΔT_acc`;
- downstream Reach / Trajectory / Outcome / Value distinction;
- current evidence state;
- Evidence-to-Claim Matrix;
- D-OPS-21, D-OPS-22 and D-OPS-23 boundaries;
- D-OPS-24 reconstruction and design;
- D-OPS-24 preflight controls;
- D-OPS-24 candidate-domain eligibility result;
- scientific-memory registry and from-scratch prohibition.

## 5. Treatment of observed search material

Observed documentary signals from the nonconforming pass are retained only as exploratory navigation material. They must not be represented as an outcome-blind, budget-conformant candidate screen.

No observed outcome, value, performance or favorable TGCV-like result was used to admit a candidate.

## 6. Corrective protocol requirement

A new versioned discovery protocol is required before further external-domain search.

The replacement protocol must:

1. preserve the frozen D-OPS-24 scientific question;
2. preserve the mandatory scientific-memory gate;
3. explicitly define the query-family unit so the budget is mechanically auditable;
4. impose a non-ambiguous maximum search budget per source family;
5. record every executed query family before search;
6. distinguish navigation queries from candidate-screening queries;
7. prohibit retroactive reclassification of queries to restore compliance;
8. preserve outcome-blind selection;
9. preserve the six-family scope unless separately versioned;
10. preserve the prohibition on dataset download, processing and empirical execution.

## 7. State transition

`D-OPS-24 DISCOVERY PROTOCOL v0.2` is no longer an executable discovery protocol for further search.

The next controlled state is **DISCOVERY PROTOCOL CORRECTION / v0.3 DESIGN**.

Further external discovery is **NOT AUTHORIZED** until v0.3 is frozen and its propagation/consistency closure is complete.

## 8. Governance propagation

Required propagation sequence:

`EXT-UPD-3.8 → RMA new immutable version → current pointer → STATUS → traceability → validator → CHANGELOG → consistency closure`

No current governance surface may claim that v0.2 produced a conformant discovery result.

## 9. Authorization boundary

External-domain search under v0.2: **NOT AUTHORIZED from this closure onward**.  
Dataset download: **NOT AUTHORIZED**.  
Dataset processing: **NOT AUTHORIZED**.  
Empirical execution: **NOT AUTHORIZED**.  
Outcome/model/value analysis: **NOT AUTHORIZED**.  
D-OPS-24 execution: **NOT AUTHORIZED**.

## 10. Non-claims

This correction is a governance regularisation only. It does not establish or weaken any scientific result beyond the procedural finding that the initial search pass was nonconforming to the frozen query budget.
