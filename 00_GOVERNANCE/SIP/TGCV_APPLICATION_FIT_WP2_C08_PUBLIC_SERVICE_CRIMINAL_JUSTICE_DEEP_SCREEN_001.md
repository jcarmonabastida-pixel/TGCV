# TGCV — Application Fit WP2-C08 Cross-Agency Public-Service / Criminal-Justice Deep-Screen 001

**Status:** PROVISIONAL — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE
**Date:** 2026-09-17
**Parent screen:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Candidate register:** `TGCV_APPLICATION_FIT_WP2_CANDIDATE_REGISTER_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.14 / RMA traceability v3.35

## 1. Evidence boundary

C08 represents cross-agency public-service / criminal-justice digital coordination in which cases, records, permissions, procedural stages and decisions may cross organisational boundaries. The candidate is included because it provides a structural contrast to the technically coupled cases: the potentially decisive coupling is institutional, procedural and authority-dependent rather than primarily physical or software-architectural.

The present public candidate material supports the existence of cross-agency workflow and information dependencies, but it does not provide a frozen TGCV decision trace. It therefore cannot establish a scientific TGCV effect or differential value at this stage.

## 2. Decision-time boundary

A useful decision boundary is the point at which an agency or authorised actor must decide the next legally/procedurally admissible action on a case after receiving information or a state transition from another agency.

Relevant state/context variables include:

- case status and procedural stage;
- records and evidence available to the actor;
- authority/role of the actor;
- permissions and disclosure restrictions;
- outstanding actions by other agencies;
- statutory or procedural deadlines;
- court/agency decisions where applicable;
- inter-agency data availability;
- workload/resource constraints where operationally relevant.

The central issue is not merely information exchange, but whether a state change in one institutional domain changes the set of actions that another authorised actor may legitimately or operationally perform.

## 3. Candidate state representation

A bounded representation is:

`S_t = {case state, procedural stage, agency states, pending actions, available records}`

`C_t = {actor authority, permissions, disclosure conditions, deadlines, inter-agency dependencies, resource context}`

`L = {legal/procedural/organisational admissibility rules}`

This is an analytical reconstruction and must not be interpreted as a claim that any justice or public-service platform implements these constructs internally.

## 4. Candidate transformations

A finite action universe could include:

- request information from another agency;
- disclose an authorised record;
- verify identity or status;
- initiate an investigative/procedural action;
- refer or transfer a case;
- schedule a hearing or procedural step;
- approve/reject a defined request;
- close or advance a case stage;
- trigger a downstream agency action;
- suspend an action pending missing information or authority.

The admissibility of these actions depends strongly on authority, procedural state and cross-agency dependencies.

## 5. Accessibility/admissibility hypothesis

The C08 hypothesis is:

`institutional/procedural state change → admissibility of actions changes → another agency's accessible action space changes → subsequent case trajectory changes`

For example:

`agency A completes required verification`
→ `agency B's next procedural action becomes admissible`.

`disclosure authority is absent or expires`
→ `specific inter-agency information transfer becomes inadmissible`
→ dependent downstream actions remain closed.

`case stage advances`
→ previously unavailable procedural actions become accessible while earlier-stage actions close.

Formally:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`.

This is a plausible application-fit interpretation, not yet an empirically reconstructed transformation space.

## 6. Multidomain coexistence vs transformational coupling

### A. Conventional institutional-workflow explanation

The case can be represented by business-process models, access-control rules, case-management state machines, legal/procedural rules and inter-agency workflow dependencies. Such models already describe which actions are permitted at each procedural stage.

### B. Transformational-coupling explanation

The stronger interpretation is that a state transition in one institutional domain systematically changes the future transformation space of another:

`agency A state transition → agency B admissibility change → B action → new case state → agency A/B future options`.

This creates a cross-organisational trajectory rather than merely a data exchange.

The critical question remains whether explicitly representing the evolving transformation space adds information beyond conventional process, authority and case-management models.

## 7. Strong alternative explanations

C08 has particularly strong established baselines:

- business-process management;
- case-management state machines;
- role-based/access-control models;
- legal/procedural rule systems;
- workflow dependency graphs;
- inter-organisational process models;
- queueing/workload models where relevant.

Consequently, simply showing that an institutional event enables or blocks a later action would not distinguish TGCV from existing approaches.

## 8. What would make C08 discriminating

A meaningful TGCV test would require a bounded case in which:

1. multiple institutional domains have explicit action sets;
2. authority/procedure conditions are frozen;
3. one domain undergoes a controlled or historically reconstructable transition;
4. the transition changes admissibility in another domain;
5. `T_acc` before and after the transition can be independently reconstructed;
6. the downstream case trajectory can be observed;
7. a conventional process/authority baseline is reconstructed;
8. the comparison identifies whether TGCV exposes a reusable cross-domain property not represented equivalently by that baseline.

The test must also separate **legal admissibility**, **organisational permission**, and **technical availability**. They are not interchangeable.

## 9. Minimum next proof

**Cross-Agency Procedural Transformation Mapper — bounded synthetic or fully de-identified case reconstruction.**

Minimum structure:

- two agencies;
- one shared case;
- finite action universe;
- explicit authority and disclosure rules;
- finite procedural states;
- one controlled inter-agency transition;
- `T_acc,0` and `T_acc,1` reconstruction;
- downstream trajectory;
- conventional process/workflow baseline;
- explicit separation of legal, organisational and technical constraints.

A clean synthetic intervention would be:

`required verification: incomplete → complete`

with all other state variables frozen. The expected structural consequence is that a defined set of downstream actions becomes admissible without assuming that any particular outcome is produced.

No execution is authorized by this screen.

## 10. Maturation route

**Primary route: Applied Demonstration**, with possible Scientific or Transfer routes depending on whether a sufficiently de-identified operational setting can be established.

A real-world deployment route would require governance, legal, privacy and institutional controls that are outside the present WP2 screen. The Value route remains separate and prospective, pending external responses.

## 11. Current disposition

**WP2-C08 — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE.**

C08 successfully provides the intended institutional contrast: authority, procedural state and inter-organisational dependencies can plausibly alter another domain's future action space. However, conventional process, case-management, access-control and procedural-rule models provide strong alternative explanations. Current material does not establish differential TGCV information or scientific validity.

**No scientific claim upgrade.** No change to TGCV Core, RMA, Evidence→Claim Matrix, C09 or existing scientific evidence state.

## 12. WP2 bounded-subset synthesis

The selected deep-screen subset now covers five structurally distinct forms:

- **C01:** federated network/compute/security orchestration;
- **C03:** agent/tool/permission action space;
- **C04:** physical asset/diagnostic/maintenance coupling;
- **C05:** shared resource/energy–mobility constraint coupling;
- **C08:** institutional authority/procedural cross-agency coupling.

Across all five, the same candidate pattern can be reconstructed conceptually as:

`state/context transition → admissibility change → altered accessible transformations → downstream trajectory`.

The recurring pattern is therefore sufficiently broad to justify a **cross-case discrimination step**, but the screens do not yet establish that TGCV adds a representation or explanatory property not already available in established domain-specific models.

The next authorised WP2 operation should therefore not be another unrestricted candidate search. It should consolidate the five screens into a **bounded cross-case discrimination matrix**, explicitly comparing mechanism, `T_acc` reconstructability, trajectory linkage, conventional baseline, missing information, and appropriate maturation route. That matrix should determine which case, if any, merits a minimum demonstrator specification.
