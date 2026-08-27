# TGCV — Internal Programme Interfaces v0.1

**Date:** 2026-08-27  
**Status:** RECOVERED / WORKING — not a freeze

## Purpose

Record the interfaces between the internal programme-control components that can currently be established from recovered evidence. This is a bridge document, not a reconstructed original of any missing historical artefact.

## 1. Project Zero → Programme Governance

**Recovered status:** referenced by the RMA as an upstream dependency of PMO/SMO, but the standalone original has not yet been located.

**Working interface:** Project Zero appears to define the programme-level frame within which the research programme operates. Its exact rules, scope and terminology remain source-recovery targets.

## 2. Work Contract → PMO/SMO

**Recovered status:** referenced by the RMA as an upstream dependency of PMO/SMO; standalone original not yet located.

**Working interface:** the Work Contract is treated as the governing agreement for how the research collaboration/workflow is conducted. Exact clauses must not be invented until recovered.

## 3. PMO/SMO → RMA

**Confidence:** high at functional level.

PMO/SMO coordinates assets, gates, decisions, versions and dependencies. The RMA provides the formal registry of those assets and their states. Therefore the interface is:

`PMO/SMO control decisions → RMA state/version/dependency updates`

The RMA explicitly assigns PMO/SMO this role. fileciteturn64file0

## 4. SIP → Portfolio / Next Action

**Confidence:** high at functional level.

SIP is the research operating/prioritisation layer. Its intended role is to turn the current research/asset state into controlled next actions rather than allowing conversational drift to determine sequence. The RMA identifies SIP as a programme methodological asset. fileciteturn64file0

Working interface:

`RMA + current research state → SIP prioritisation → selected work → updated state`

## 5. Architecture Review → Core

**Confidence:** high at governance principle level.

Programme work may propose changes, but governance/execution mechanisms do not themselves modify the scientific Core. A scientific change requires an explicit evidence/gate decision.

Current safe scientific boundary remains the post-TR-140 state documented in the continuity package. fileciteturn68file0

## 6. SLR → Evidence → Claims

**Confidence:** high.

The RMA establishes a linked evidence subsystem:

`SLR dossiers → Evidence Bank → Fact Bank → Prior-Art Absorption Matrix → claim/originality assessment`

The purpose is not merely literature collection: SLR-1 is explicitly a falsification-oriented test of architectural originality.

## 7. Experiments → Scientific state

Experiments feed evidence into the scientific state through explicit test records and freezes. They do not automatically rewrite the Core or external assets. Changes propagate through governance and RMA.

## 8. Historical applied methodology → ARM/RII/MOI

The historical record contains a substantial value-construction methodology. Its correct current interface is downstream of the scientific Core: it may inform ARM/RII/MOI and applied methodology, but cannot be used to redefine the Core without explicit scientific justification. fileciteturn64file1

## 9. Provisional programme control loop

The strongest cross-source reconstruction currently supported is:

`Project Zero / Work Contract`
`        ↓`
`PMO / SMO`
`        ↓`
`RMA ↔ SIP`
`        ↓`
`Research / SLR / Experiment execution`
`        ↓`
`Evidence + decisions + updated assets`
`        ↓`
`Architecture / governance review`
`        ↺`

This loop is deliberately labelled **provisional** until the missing originals are recovered.

## 10. Recovery priority

The next source-recovery targets are not just the documents themselves but evidence describing the arrows in the loop:

1. Project Zero → PMO/SMO
2. Work Contract → PMO/SMO
3. SIP → RMA/portfolio selection
4. PMO/SMO → architecture review
5. ACTII → programme control loop
6. Flows/MOP → execution sequence
7. SLR → evidence/claim lifecycle

## 11. Integrity rule

No interface is promoted from `WORKING` to `FOUNDATIONAL` merely because it is elegant or operationally plausible. Promotion requires recovered source evidence or an explicit later decision.
