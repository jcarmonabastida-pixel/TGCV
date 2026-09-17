# TGCV — Application Fit WP2 Cross-Case Discrimination Matrix 001

**Status:** BOUNDED SYNTHESIS — FIVE CASES SCREENED; NO SCIENTIFIC CLAIM UPGRADE
**Date:** 2026-09-17
**Scope:** C01, C03, C04, C05, C08
**Parent:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.14 / RMA traceability v3.35

## 1. Purpose

This matrix consolidates the five structurally distinct WP2 deep-screening cases. Its purpose is discrimination, not ranking. It asks whether the same TGCV candidate pattern can be reconstructed across domains and, more importantly, whether existing domain-specific representations already capture the relevant information.

The matrix does **not** score or rank candidates and does not establish scientific validity.

## 2. Common discrimination question

The common candidate pattern is:

`state/context transition → admissibility change → ΔT_acc → downstream trajectory`

The critical discrimination question is:

> Does explicitly representing the evolving accessible transformation space provide reusable information that is not equivalently represented by the strongest conventional model for the case?

A case is not considered discriminating merely because `T_acc` can be defined. A finite feasible/action set is already present in many established models.

## 3. Cross-case matrix

| Case | Structural mechanism | Candidate ΔT_acc reconstruction | Trajectory linkage | Strong conventional baseline | Main missing information | Current maturation route |
|---|---|---|---|---|---|---|
| **C01 ACROSS** | Federated network/compute/security orchestration; policy, resource and security changes propagate across domains | Conceptually strong; concrete frozen event sequence not yet independently reconstructable from public material | Candidate only; downstream trajectory not frozen | Network orchestration, policy automation, resource management, workflow/event models | Frozen S/C, finite Uτ, outcome-independent Pτ, controlled transition and post-transition trace | Applied Demonstration; scientific conditional |
| **C03 Sentinel** | Agent/tool/permission changes alter executable action space | Conceptually clear; permissions provide explicit admissibility conditions, but full transition trace remains incomplete | Candidate workflow trajectory; differential contribution unresolved | Access-control/capability/workflow/agent-tool models | Frozen action universe, permission transition, trajectory and baseline comparison | Applied Demonstration |
| **C04 Digital Twin** | Physical asset/diagnostic state changes maintenance action space | Potentially empirically reconstructable; public testbed/data exist, but admissibility contract is not frozen | Potentially observable; current source does not independently reconstruct action-space change | Predictive maintenance, diagnosis, digital-twin, workflow/control models | Frozen decision boundary, Uτ, outcome-independent Pτ, leakage controls, transition and trajectory | Applied Demonstration; scientific conditional |
| **C05 EV–Grid** | Shared physical resources and constraints propagate between mobility and energy | Structurally strong and finitely enumerable in a bounded system | Directly simulable/reconstructable once transitions are frozen | Constrained optimisation, scheduling, MPC, network capacity/control | Demonstration that transformation-space representation adds information beyond feasible-set representation | Applied Demonstration; scientific conditional |
| **C08 Public service / justice** | Institutional authority/procedural state changes another agency's action space | Conceptually reconstructable; legal, organisational and technical admissibility must be separated | Potentially traceable through case workflow; no frozen reconstruction yet | BPM, case management, RBAC, procedural/legal rules | De-identified case, authority rules, procedural transition, cross-agency trajectory | Applied Demonstration; possible Transfer/Scientific route |

## 4. Discrimination by mechanism class

### C01 — Federated technical orchestration

The candidate mechanism is cross-domain propagation through network, compute and security state. The strongest alternative explanation is conventional orchestration and policy/resource management. The unresolved issue is whether a transformation-space representation reveals a trajectory-relevant dependency not already explicit in those models.

### C03 — Agent/tool/permission

The candidate mechanism is capability/accessibility change caused by permission state. This is a particularly direct mapping to an action space, but access-control and capability models already define permitted actions. The discrimination burden is therefore whether TGCV adds trajectory-level information when permissions change dynamically.

### C04 — Physical asset/digital twin

The candidate mechanism is a physical/diagnostic transition changing maintenance options. Public data make empirical reconstruction more plausible than for the purely architectural cases. The critical baseline is predictive maintenance plus diagnosis/workflow/control; a future mapper must test what, if anything, is added by explicit `T_acc` tracking.

### C05 — Energy/mobility resource coupling

The candidate mechanism is shared capacity changing feasible actions across domains. This is the clearest physical resource-coupling case, but constrained optimisation already represents feasible action sets. Therefore the discriminating target is not feasibility itself but whether evolving accessibility provides a reusable trajectory-level abstraction across coupled domains.

### C08 — Institutional/procedural coupling

The candidate mechanism is authority and procedural state changing another organisation's admissible actions. Existing process, legal-rule and access-control models are strong alternatives. The key test is whether the same transformation-space abstraction crosses organisational boundaries in a way that preserves useful trajectory information without collapsing legal, organisational and technical admissibility into one variable.

## 5. What the five cases collectively establish at WP2 level

The screening supports the following bounded observations:

1. A common analytical pattern can be formulated across technically, physically and institutionally different application structures.
2. The pattern can be expressed in each case as a candidate relationship between state/context, admissibility, accessible transformations and subsequent trajectory.
3. The mechanism is not restricted to software/AI systems; C04 and C05 provide physical-resource contrasts, while C08 provides institutional/procedural coupling.
4. Each case has a strong domain-specific conventional representation capable of explaining substantial portions of the same phenomenon.
5. Therefore, cross-domain recurrence alone is insufficient to establish a distinct TGCV analytical contribution.

These are WP2 application-fit observations, not scientific claims about TGCV validity.

## 6. What remains unresolved

The following questions remain open across all five cases:

- whether `T_acc` provides information not already encoded by domain-specific feasible/action sets;
- whether explicit accessibility transitions improve reconstruction of downstream trajectories;
- whether the same representation can be operationalised without importing outcome information into `Pτ`;
- whether a single cross-domain abstraction can preserve domain-specific semantics sufficiently to be useful;
- whether any candidate reaches a maturation route beyond application-fit plausibility.

## 7. Minimum-proof selection logic

The next action should be selected by **information value**, not by an application preference or by an overall ranking.

A minimum demonstrator should satisfy four requirements:

1. finite and independently reconstructable `Uτ`;
2. outcome-independent admissibility predicates;
3. controlled or reproducible transition yielding a measurable accessibility change;
4. a strong conventional baseline whose represented information can be compared explicitly.

On the present screening record, **C05 is structurally the cleanest synthetic benchmark candidate** because a small bounded EV–grid system permits explicit enumeration of actions, controlled capacity transitions and a strong conventional optimisation baseline. This is a methodological selection for the next proof, not a ranking of applications or a claim that C05 is intrinsically superior.

C04 remains the principal candidate for a later empirical reconstruction because of its physical testbed/data substrate, subject to a frozen admissibility protocol. C01, C03 and C08 remain valuable structural contrasts and should not be discarded merely because their current public evidence is less directly executable.

## 8. Maturation-route separation

The five-case synthesis preserves the four independent WP2 maturation routes:

- **Scientific / SIP:** only if a discriminating research question survives baseline comparison.
- **Applied Demonstration:** bounded demonstrator showing that the representation can reconstruct a relevant cross-domain mechanism.
- **Transfer / Deployment:** integration into an operational environment if an appropriate partner/context emerges.
- **Value / Independent Evaluation:** remains a separate prospective route and is currently waiting on external responses.

No route is presumed to be the endpoint of Application Fit.

## 9. Governance effect

This matrix is an analytical WP2 synthesis only.

It does **not** authorize:

- scientific execution;
- causal claims;
- value/ROI evaluation;
- Core modification;
- RMA modification;
- Evidence→Claim Matrix claim-status upgrade;
- reopening of C09;
- rerunning TSTC or TR-132.

The existing scientific evidence state remains unchanged.

## 10. Next authorised operation

The next WP2 operation is to convert the selected **C05 minimum-proof concept** into a bounded demonstrator specification, while preserving C04 as the candidate for a later empirical branch.

That specification must define the finite transformation universe, state/context variables, admissibility predicates, transition matrix, trajectory observation, conventional baseline and non-claims before any execution is considered.
