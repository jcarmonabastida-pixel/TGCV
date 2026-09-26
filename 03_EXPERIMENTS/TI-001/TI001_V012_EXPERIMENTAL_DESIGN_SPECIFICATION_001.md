# TI-001 V012 — Experimental Design Specification 001

**Date:** 2026-09-26  
**Status:** DESIGN — SCIENTIFIC EXECUTION NOT AUTHORIZED  
**Antecedents:** TI-001 V011 closed evidence; TI Discrimination Register 001; TI001 V012 Discrimination Mapping 001.

## 1. Purpose

V012 is the next experimental design derived from the six unresolved questions left by V011. Its purpose is to discriminate among the alternative explanations formalized in Q1–Q6. It is not a reproduction of V011.

## 2. Research question

Under matched present state and current accessible transformations, does access to explicitly action-conditioned information about future transformation-space structure alter present transformation selection in a way distinguishable from ordinary task information, presentation/order effects, baseline/null variability, fixture/task/model-specific effects, generic information processing, and post-hoc value interpretation?

## 3. V011 boundary

V011 remains immutable and closed. V012 must not rerun V011 merely to obtain additional observations, modify V011 artifacts, pool V011 with V012 observations, or use V011 results as a V012 outcome.

## 4. Core experimental structure

Each V012 decision unit contains a current state S_t, current accessible transformations T_acc,t = {a,b,c}, at least two admissible transformations, deterministic/reconstructable transitions, successor state, and successor accessibility for every candidate.

Control and treatment share the same present state, current action set, task, timing, execution environment, and decision mechanism. Treatment receives an action-conditioned description of future transformation-space consequences. The information describes consequences without evaluating them.

## 5. Experimental factors

### F1 — Future-space information
Control receives current task/state/action information only. Treatment receives identical information plus an explicit mapping a→F(a), b→F(b), c→F(c), where each F describes future transformation-space structure without recommendation, ranking, reward, value, utility, performance, or outcome-quality information.

### F2 — Presentation
At least two independently specified, semantically equivalent presentation encodings are used. Format/order is randomized or counterbalanced and recorded. Presentation must not reveal condition identity or preferred action.

### F3 — Null
The null preserves present state/action/task structure and comparable presentation burden while excluding future-space information and recommendation/outcome information. Control and null remain analytically separate.

### F4 — Mechanism perturbation
At least one mechanism-sensitive perturbation compares an intact action-to-future mapping with a structurally comparable mapping whose correspondence is removed or independently scrambled. Current state, action set, presentation burden, timing, and prohibited-information exclusions remain unchanged.

### F5 — Independent operationalisation
V012 contains multiple independently specified finite-state environments or transition structures. They must differ in successor-accessibility identity structure rather than merely duplicating one transition table.

## 6. Decision mechanism

The frozen TI-001 decision-mechanism specification remains the antecedent mechanism class. All conditions use the same model/runtime configuration and base decision protocol unless a separately authorized factor requires otherwise. No hand-coded treatment-to-action rule is permitted.

Before execution, model identifier/version, runtime identifier/version, generation configuration, base/system prompt hash, and output validation procedure must be frozen.

## 7. Temporal structure

1. Present state and current transformations become available.
2. Assigned information and presentation condition is shown.
3. The agent selects one current transformation.
4. The transformation is realised.
5. Successor state is reconstructed.
6. Successor accessible transformation space is reconstructed.
7. Future consequences are revealed only after the decision.

The agent cannot inspect realised future state/accessibility before choosing.

## 8. Q1 — Construct validity

V012 must distinguish future-transformation-space incorporation from ordinary task information, presentation artefacts, and simpler response heuristics.

Required controls are matched current state/action space, null condition, mechanism perturbation, presentation variation, and prohibition of preferred-action encoding.

Primary observable: transformation-selection difference specifically attributable to intact future-space information.

Non-discrimination: the same response difference persists when the action-conditioned mapping is removed or scrambled.

## 9. Q2 — Presentation dependence

V012 must determine whether the decision response is invariant to presentation/order.

Condition effects are reported separately by presentation variant and compared using pre-specified criteria.

Non-discrimination: an effect confined to one presentation/order without corresponding evidence across the independent presentation.

## 10. Q3 — Null/control behaviour

V012 must distinguish treatment sensitivity from baseline response variability.

Treatment must be interpreted alongside independently observed control/null behaviour. No pooling, recoding, retry, or imputation is permitted.

Non-discrimination: treatment variation is not distinguishable from pre-specified control/null baseline variation.

## 11. Q4 — Robustness

V012 must test persistence across independent operationalisations rather than merely repeating one fixture.

Required evidence: at least two independently specified environment/transition structures using the same abstract decision protocol.

Non-discrimination: the effect is confined to one environment, task construction, model, or encoding.

## 12. Q5 — Mechanism

V012 must distinguish use of action-conditioned future structure from generic information processing or association.

The mechanism contrast preserves current state, current action set, presentation complexity, timing, task, and decision mechanism while selectively preserving or perturbing action-to-future correspondence.

Mechanistic observable: change in transformation selection attributable to preserving versus perturbing the correspondence.

Non-discrimination: equivalent behaviour under intact and perturbed mappings, or an effect tracking generic information/presentation instead.

## 13. Q6 — Decision-to-T_acc bridge

V012 may establish a decision-to-transformation-space bridge but must not silently convert it into a value claim.

For every selected transformation independently reconstruct:
S_t → selected transformation → S_t+1 → T_acc,t+1.

Record selected transformation, successor state, successor accessible transformation set, change in accessible transformation structure, and correspondence between realised consequence and pre-decision descriptor.

No ΔV endpoint is part of primary V012 inference.

## 14. Primary estimands

No composite TI score is defined.

Primary behavioural estimand: pre-specified difference in transformation selection between matched information conditions.

Secondary estimands:
1. presentation-stratified condition contrast;
2. treatment/control/null contrast;
3. intact-versus-perturbed mapping contrast;
4. cross-operationalisation consistency;
5. decision-to-realised-T_acc correspondence.

All estimands must be frozen before inspecting outcomes.

## 15. Blocking and falsification criteria

Interpretation is blocked if current T_acc differs across matched conditions; treatment directly identifies a preferred transformation; prohibited reward/value/utility/performance/outcome-quality information is present; future state/accessibility is revealed before choice; presentation is confounded with treatment; mechanism perturbation changes current action availability; operationalisations are not independent; future mapping cannot be reconstructed; effects are equally present in null or mapping-perturbed conditions; or the decision-to-T_acc bridge cannot be independently reconstructed.

## 16. Independent reconstruction

Executor-2 must reconstruct the frozen package and verify state/action identity, condition isolation, presentation assignment, future mapping, mechanism perturbation, successor states, successor accessibility, and primary observables. Any unexplained deviation blocks interpretation.

## 17. Required freeze package

Before execution the package must contain the V012 specification, exact environments, action-conditioned descriptors, presentation encodings, null definition, mechanism perturbation, independent operationalisations, randomization, decision-agent configuration, executor, reconstruction procedure, estimands, integrity manifest, preflight result, and execution authorization.

## 18. Existing v005 work

TI001_REDESIGN_PREFLIGHT_SPECIFICATION_002, its checker, generator, and v005 candidate remain auxiliary methodological artifacts. They may inform V012 where explicitly traceable, but they are not V012 by identity.

The v004 fixture remains unchanged and historical.

## 19. Governance state

V011: CLOSED / IMMUTABLE.  
Q1–Q6: OPEN / FORMALIZED.  
V012 discrimination mapping: PERSISTED.  
V012 experimental design: DESIGN ONLY.  
V012 fixture: NOT GENERATED.  
V012 scientific execution: NOT AUTHORIZED.  
V012 claim status: NONE.  
TGCV Core: UNCHANGED.

## 20. Next gate

Before generating any V012 fixture or executable package, perform a dedicated V012 Design Audit / Requirements Gate verifying traceability from every V012 design element to Q1–Q6 and verifying that no inherited v005 constraint has silently become a scientific requirement.

Only a PASS permits construction of the V012 candidate fixture and dedicated preflight.


## 21. Detailed design closure conditions

### 21.1 Presentation factor — frozen design rule

V012 will use two semantically equivalent encodings of the same action-conditioned future-space mapping:

- **P1:** action-keyed tabular records, one row per action, with the same neutral descriptor fields for every action.
- **P2:** action-keyed ordered records using the same fields and values but a different presentation order determined by a frozen permutation.

The semantic mapping is invariant between P1 and P2. Presentation order is independent of condition assignment and is randomized at the decision-unit level using the frozen randomization seed. No presentation encoding may contain condition labels, preferred-action labels, rankings, or normative language.

The primary Q2 comparison is the treatment-versus-control contrast separately within P1 and P2, with the presentation-by-condition interaction as a secondary diagnostic. A condition effect that appears only under one presentation is not treated as presentation-invariant evidence.

### 21.2 Mechanism perturbation — frozen design rule

The mechanism test uses three information states within otherwise matched decision units:

- **INTACT:** each action is paired with its correct future-space descriptor F(u).
- **SCRAMBLED:** the same descriptor multiset, descriptor fields, information volume, and presentation structure are retained, but descriptors are independently permuted across action keys.
- **NULL:** no future-space mapping is supplied.

The scramble permutation is generated from the frozen seed and must be a derangement for the three-action case, so no action retains its original descriptor. The transition specification used for reconstruction remains the ground truth; the SCRAMBLED condition is an information perturbation, not a change to the environment.

This directly operationalises Q5: if behaviour depends on the action-to-future correspondence, INTact and SCRAMBLED should differ under the pre-specified analysis while current state, current T_acc, task, timing, descriptor inventory, and presentation burden remain matched. The result is not interpreted as mechanism proof by itself; it is a discrimination test between intact correspondence and a structurally matched perturbation.

### 21.3 Independent operationalisations — frozen minimum

V012 will contain **three** independently specified finite-state operationalisations, O1–O3. Each has S_t=S0 and current T_acc={a,b,c}, but distinct successor-accessibility identity structures:

- **O1:** a→{x,y}, b→{x,z}, c→{y,z}.
- **O2:** a→{p,q}, b→{p,r}, c→{q,s}.
- **O3:** a→{m,n}, b→{n,o}, c→{m,o}.

The abstract structure is held constant (two-element successor accessibility per action, at least two distinct future-space descriptors), while concrete transformation identities and the action-to-future mapping differ. No operationalisation may be derived by merely renaming one already generated fixture after observing outcomes; all three transition specifications are frozen before execution.

### 21.4 Experimental unit, sample size and randomization — frozen design rule

The primary unit is an independently generated decision instance within one operationalisation and one presentation/condition assignment. V012 will use **24 independent instances per operationalisation**, 72 instances total. Each instance is evaluated under one information condition and one presentation assignment. The allocation is balanced across the three information states INTact, SCRAMBLED, and NULL and across P1/P2 within each operationalisation, yielding 8 instances per information state and 12 per presentation per operationalisation.

The frozen randomization seed is **582031**. A deterministic assignment procedure will independently shuffle the 24 instance identifiers within each operationalisation, then assign condition and presentation using the pre-specified balanced allocation. Condition and presentation assignments are recorded in the frozen package and are not inferable from state/action identifiers.

No scientific execution is implied by this design closure. The exact generated instance identifiers, randomization manifest, and fixture bytes must be produced only after the V012 design requirements gate passes.

### 21.5 Closure status

The four conditions identified by the V012 Design Audit are now specified at the design level. They remain subject to machine-checking in the dedicated V012 Requirements/Preflight Gate before fixture generation.
