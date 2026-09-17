# TGCV — WP2 Cross-Case Synthesis C01/C03/C04/C05/C08 001

**Status:** FROZEN — CROSS-CASE DISCRIMINATION SYNTHESIS COMPLETED; NO APPLICATION QUALIFIED
**Date:** 2026-09-17
**Scope:** C01 / C03 / C04 / C05 / C08
**Protocol:** `TGCV_APPLICATION_FIT_WP2_EXPLORATION_PROTOCOL_001.md`
**Deep-screening basis:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.12 / RMA traceability v3.35

## 1. Purpose

This document closes the first bounded cross-case WP2 synthesis after deep-screening five structurally distinct candidates.

The purpose is not to rank applications or establish differential value. It is to determine whether the recurring TGCV representation survives comparison across substantially different system architectures and whether a common **minimum discriminator** can be formulated against established domain-specific representations.

The five cases are:

- **C01 — ACROSS:** federated network/cloud-edge/security orchestration;
- **C03 — Coupa Sentinel:** AI-agent/tool/permission action space;
- **C04 — Digital Twin / Predictive Maintenance:** physical-digital-maintenance coupling;
- **C05 — EV-Grid:** energy-mobility resource and constraint coupling;
- **C08 — Cross-Agency Criminal Justice:** institutional authority/inter-organisational case trajectories.

## 2. Cross-case instrument

The common analytical skeleton is:

`decision-time boundary → S_t/C_t → candidate transformations Uτ → admissibility Pτ → T_acc,t → controlled transition → T_acc,t+1 → downstream trajectory`

The recurring question is:

> Does a transition in state, context or governing conditions change the set of transformations that are accessible next, and does that change matter for the subsequent trajectory?

This formulation is portable across all five candidates.

Portability alone is **not** evidence of scientific validity or differential value.

## 3. Comparative structural matrix

| Case | Primary coupling | Main accessibility determinant | Downstream trajectory | Strong conventional baseline |
|---|---|---|---|---|
| C01 | technical domain orchestration | resources, policy, security/trust, service state | service/network reconfiguration | orchestration/control/policy automation |
| C03 | agent–tool–permission | tool availability, authorization, backend state | agent task execution | access control/workflow/capability models |
| C04 | physical–digital–maintenance | asset condition, knowledge state, resources, safety | maintenance/operational trajectory | predictive maintenance/rules/scheduling |
| C05 | energy–mobility resources | grid capacity, demand, charger/site state, mobility constraints | charging + mobility trajectory | constrained optimisation/control |
| C08 | institutional/inter-organisational | authority, procedural state, artefacts, interoperability | case trajectory across agencies | workflow/process/case-management/authorisation |

## 4. What survives across all five cases

### 4.1 Accessibility can be represented without making the mechanism primitive

In every case, the mechanism can remain an explanatory transition rather than an ontological primitive.

The analytical structure is compatible with:

`mechanism / condition change → state/context transition → admissibility change → ΔT_acc`.

This is consistent with the current TGCV boundary established by TR-130.

### 4.2 The state/context distinction remains useful

The cases repeatedly require separation between:

- system state `S`;
- context/conditions `C`;
- admissibility rules `L`;
- candidate transformations `Uτ`.

The distinction is especially important in C04 and C08, where physical state and institutional/procedural state respectively interact with information and resource conditions.

### 4.3 `T_acc` is analytically portable

A finite accessible transformation space can be formulated in every candidate without requiring exhaustive enumeration of every real-world action.

The practical unit is a bounded set of candidate transformations relevant to a defined decision-time boundary.

This reinforces the methodological position that TGCV operationalisation should be **case-bounded rather than universally exhaustive ex ante**.

### 4.4 The trajectory link is where the abstraction becomes more demanding

All five cases admit a simple `ΔT_acc` reconstruction hypothesis. The more difficult question is whether the change in accessible transformations has explanatory consequences for later trajectory that are not already encoded in the conventional model.

Therefore the cross-case discriminator should not stop at:

`T_acc,t ≠ T_acc,t+1`.

It should continue to:

`ΔT_acc → changed subsequent decision possibilities → trajectory divergence or constraint propagation`.

## 5. What does NOT survive as a differential claim

The synthesis does **not** establish that TGCV is superior to:

- orchestration models in C01;
- capability/access-control/workflow models in C03;
- predictive-maintenance and scheduling models in C04;
- optimisation/control models in C05;
- workflow/process/authorisation models in C08.

In every case, a conventional representation can potentially encode the same feasible-action information.

Consequently, the following implication is rejected as a WP2 conclusion:

`TGCV can represent T_acc → TGCV adds differential value`.

That implication requires a separate discriminator.

## 6. Minimum common discriminator

The smallest common discriminator identified is a **Transformation-Space Transition Comparison (TSTC)**.

### TSTC question

> Given the same frozen decision-time system, can a bounded TGCV representation identify a state transition that changes the accessible transformation space and its subsequent trajectory implications in a way that is not equivalently recoverable, with comparable information and assumptions, from the domain's conventional representation?

This is a comparative explanatory test, not a superiority score.

### Required components

1. frozen decision-time boundary;
2. frozen `S_t`, `C_t`, and `L`;
3. finite candidate transformation set `Uτ`;
4. explicit outcome-independent admissibility predicates `Pτ`;
5. reconstructed `T_acc,t`;
6. one controlled state/context transition;
7. reconstructed `T_acc,t+1`;
8. downstream trajectory representation;
9. conventional domain baseline;
10. matched comparison of information represented, assumptions required, and trajectory consequences.

## 7. Why the discriminator is not a generic "TGCV vs baseline" benchmark

A generic benchmark could become unfair because each domain has a different purpose and representational language.

The TSTC therefore should not ask which model predicts an arbitrary performance metric better.

Instead it should compare a narrower object:

**Can both representations reconstruct the same change in future transformation possibilities from the same frozen information?**

If both do so equivalently, there is no demonstrated differential explanatory contribution for that case.

If TGCV exposes a cross-domain relation that is difficult to express or compare in the conventional representation, that creates a **demonstration hypothesis**, not yet a scientific claim.

## 8. Cross-case common demonstrator

The synthesis identifies a candidate common artefact:

# TGCV Cross-Domain Transformation Mapper

A bounded synthetic environment containing multiple domain connectors, each with:

- domain state;
- context;
- admissibility rules;
- finite candidate transformations;
- accessible transformation space;
- transition operator;
- downstream trajectory.

The connectors can instantiate the five structural patterns without requiring realistic production infrastructure.

### Minimal architecture

`Domain A state/context`
→ `connector`
→ `TGCV transformation representation`
→ `cross-domain accessibility relation`
→ `connector`
→ `Domain B state/context`.

The mapper should make explicit when a transformation in one domain:

- opens another domain's transformation;
- closes another domain's transformation;
- changes its admissibility condition;
- changes cost/time without changing feasibility;
- propagates a constraint;
- changes a subsequent trajectory.

## 9. Minimum synthetic benchmark

The common demonstrator should not implement all five cases simultaneously at first.

A four-node synthetic benchmark is sufficient:

1. **technical orchestration node** — C01 pattern;
2. **agent/tool/permission node** — C03 pattern;
3. **resource/constraint node** — C05 pattern;
4. **institutional/procedural node** — C08 pattern.

C04 can supply the physical-digital pattern as an optional connector because it introduces an important distinction between:

`physical state change`
vs
`knowledge/representation change`
vs
`resource constraint change`.

### Controlled interventions

Each connector should support one clean intervention:

- capability/tool becomes available;
- permission changes;
- resource capacity becomes constrained;
- procedural authority becomes available;
- physical condition crosses a defined threshold.

Everything else remains frozen.

## 10. What would count as a useful applied result

The demonstrator would have practical applicability if it can show, in a reproducible bounded setting, that an analyst can:

1. specify a decision-time state;
2. identify candidate transformations;
3. state admissibility conditions;
4. reconstruct `T_acc`;
5. apply a controlled transition;
6. identify newly opened/closed transformations;
7. trace cross-domain consequences;
8. compare those consequences with a conventional representation.

This would support an **applicability-state update**.

It would not establish a scientific TGCV claim, causal validity, deployment readiness or value.

## 11. What would be required for a scientific route

A scientific route would require an empirical case in which:

- the decision-time state is reconstructible;
- the transformation candidates are identifiable;
- admissibility can be specified independently of outcome;
- a transition or intervention is observable;
- the subsequent trajectory is independently observable;
- an appropriate counterfactual or comparison exists where required;
- the conventional explanation can be reconstructed;
- the TGCV representation yields a falsifiable proposition not reducible to relabelling.

The current application-fit cases do not jointly satisfy these conditions.

Therefore the WP2 synthesis does **not** upgrade scientific status.

## 12. Differential-value hypothesis — current disposition

The cross-case work produces a sharper hypothesis but not evidence for it:

> TGCV may provide a common analytical layer for comparing how state/context transitions alter future transformation spaces across heterogeneous domains, particularly when transformations are distributed across domains and constraints propagate between them.

This is a **transfer/application hypothesis**.

It remains unverified whether this common layer produces information that is materially non-redundant with existing domain-specific representations.

## 13. Multidomain coupling finding

The strongest result of this WP2 pass is not that the candidates are validated. It is that **multidomain coupling can be operationalised more precisely**.

The relevant distinction is now:

`multidomain coexistence`

versus

`state-transition-mediated transformation-space coupling`.

The latter requires at least:

`transition in domain A`
→ `change in admissibility of transformation(s) in domain B`
→ `observable consequence for B's subsequent trajectory`.

This gives WP2 a sharper screening criterion than the original D0–D4 classification alone.

## 14. Proposed WP2 maturity state

The five deep-screened candidates should now be treated as:

| Candidate | Current state | Immediate route |
|---|---|---|
| C01 | coupling-candidate | applied mapper |
| C03 | coupling-candidate | applied mapper |
| C04 | coupling-candidate | applied mapper |
| C05 | coupling-candidate | applied mapper |
| C08 | coupling-candidate | applied mapper; scientific route conditional |

This is **not a ranking**.

The common state simply means that none has yet crossed the reconstruction/discrimination threshold.

## 15. WP2 decision

The first exploratory WP2 search and deep-screen sequence is now sufficiently informative to stop expanding the candidate list.

**Decision:** move from candidate discovery to **controlled Applied Demonstration design**.

The immediate next artefact should be a specification for the smallest common **TGCV Cross-Domain Transformation Mapper / TSTC demonstrator**.

The demonstrator should be designed so that failure to show non-redundant explanatory information is itself an informative outcome.

## 16. WP1 gate

WP1 remains paused during this step.

No automatic update to:

- Vision Paper;
- Research Prospectus;
- ARM;
- TCP;
- MOI;
- SIP

is authorised solely from this synthesis.

After the demonstrator specification is frozen, WP1 can receive a **controlled update limited to the application-fit/maturity architecture actually supported by WP2**.

## 17. Governance boundary

No change to:

- TGCV Core;
- RMA v3.35;
- Evidence→Claim Matrix v1.12;
- scientific claim status;
- C09/C10 evidence;
- VSL-44;
- standing industrial execution authorization.

**Next controlled step:** design and freeze `TGCV Cross-Domain Transformation Mapper / TSTC` minimum demonstrator specification.
