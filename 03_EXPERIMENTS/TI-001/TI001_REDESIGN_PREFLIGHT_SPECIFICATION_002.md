# TGCV — TI-001 Redesign / Preflight Specification
## Action-Conditioned Future Information — Specification 002

**Date:** 2026-09-25  
**Status:** DESIGN / PREFLIGHT SPECIFICATION — SCIENTIFIC EXECUTION NOT AUTHORIZED  
**Antecedent:** TI-001 Preflight Specification 001; TI-001 v004 execution record  
**Purpose:** redesign the treatment information so that future transformation-space information is explicitly conditioned on each currently executable transformation, while preserving the current state and current accessible transformation set.

## 1. Scientific boundary

This specification defines only the redesign and its machine-checkable preflight. It does not generate a new fixture and does not authorize scientific execution.

TI-001 v004 is retained unchanged as a prior, traceable execution. Its result is not invalidated. The redesign addresses an identified inferential limitation: v004 encoded a future-space pattern, but did not require the treatment representation itself to expose an explicit action-to-future-consequence mapping for all currently executable actions. Therefore v004 cannot by itself establish that the treatment supplied action-conditioned future information capable of supporting behavioral divergence.

## 2. Fixed current decision environment

Every redesigned instance MUST preserve:

- current state: S0;
- current accessible transformation set: T_acc = {a,b,c};
- current available transformations: exactly a,b,c;
- identical current state and current action set across control, treatment and null conditions.

No manipulation may modify the current state or the transformations executable at decision time.

## 3. Temporal separation

The manipulated information MUST refer only to consequences that become relevant after a transformation is selected.

The treatment MUST NOT modify S0, modify T_acc at decision time, reveal the successor state before the decision, or reveal realised successor accessibility before the decision.

The decision order is fixed as:

information presentation → transformation selection → successor realisation → future accessibility reveal.

## 4. Action-conditioned future representation

For every currently executable transformation u in {a,b,c}, the treatment MUST contain a structured future descriptor F(u).

The representation MUST therefore have the explicit form:

a → F(a), b → F(b), c → F(c)

where each F(u) describes a future transformation-space consequence, such as successor accessibility, identity turnover, persistence, or reconfiguration class.

The representation MUST be semantically neutral: it describes what follows from each action, not what the agent should choose.

A valid instance MUST contain at least two distinct future descriptors:

there exist u,v in T_acc such that F(u) != F(v).

For the canonical three-action design, all three mappings should be explicit and at least two should be distinct.

## 5. No recommendation / no normative encoding

The treatment MUST NOT contain preferred-action labels, rankings of actions, scores attached to actions, normative words equivalent to best/preferred/recommended/optimal/choose/avoid, reward/value/utility/performance information, outcome ranking, or a direct alias in which a treatment token uniquely denotes the action that should be selected.

This property MUST be enforced structurally, not only lexically. The treatment future-descriptor schema MUST define an allowlisted set of neutral structural fields (for example: future-accessibility class, identity-turnover class, persistence class, or reconfiguration class) and MUST reject any field whose semantics encode preference, evaluation, recommendation, ranking, reward, value, utility, performance, or outcome quality.

The checker MUST validate the descriptor schema and field semantics against this allowlist. A lexical scan may be an auxiliary diagnostic, but a lexical PASS alone MUST NOT establish R8.

A future descriptor may identify the consequence associated with an action, but must not evaluate that consequence.

## 6. No prohibited outcome information

The treatment, control and null information MUST exclude reward, value, utility, performance, outcome quality, success/failure labels, and any scalar or ordinal quantity that can function as an outcome ranking.

Future transformation-space structure is admissible. Outcome evaluation is not.

## 7. Divergence-opportunity criterion

The redesigned information must create a genuine structural opportunity for different decisions between conditions.

Define the treatment information as I_T and the control information as I_C.

The preflight MUST establish all of:

D1 — Action-conditioned observability: I_T contains reconstructable descriptors F(a), F(b), F(c).

D2 — Future-space non-equivalence: at least two currently executable transformations have different future descriptors.

D3 — Control non-derivability: the mapping u → F(u) is not reconstructable from I_C, S0, and T_acc alone.

D4 — Decision-time availability: I_T is available before selection and no realised future state is available.

D5 — Choice multiplicity: at least two transformations remain admissible after treatment information is received.

D6 — Treatment-induced divergence opportunity: there exist matched deterministic decision rules, identical with respect to S0, T_acc, task, timing and decision procedure, for which the treatment-exclusive mapping u → F(u) permits at least one admissible decision to differ from the corresponding control decision, with u != v, while no reward, value, utility, performance or outcome information is available.

The witness for D6 MUST therefore depend on the treatment-exclusive future mapping: the checker MUST demonstrate that removing that mapping while holding S0, T_acc, task, timing and decision rules fixed eliminates the specific information difference used to produce the divergent selection. Two arbitrary decision functions that merely happen to return different actions are insufficient.

D6 is an existence property, not a prediction that an experimental agent will diverge. It establishes that the treatment creates a real opportunity for condition-dependent behavioural divergence attributable to the treatment-exclusive information rather than to an unconstrained choice of decision function.

## 8. Structural equivalence constraint

Control and treatment MUST be identical with respect to S0, T_acc, action identities, task, decision timing, randomisation assignment, and execution environment.

The sole substantive difference is the availability of the future-space descriptor mapping in treatment.

## 9. Null condition

The null condition MUST preserve comparable structure/format while removing future-space signal.

It MUST satisfy: same S0; same T_acc; same action identities; same task; no future-space mapping; no recommendation; no reward/value/utility/performance/outcome information.

## 10. Machine-checkable preflight

A redesigned fixture MUST NOT be generated until all checks below PASS.

R1 — State identity: all conditions have S0.

R2 — Current-space identity: all conditions have T_acc={a,b,c}.

R3 — Action identity: all conditions expose exactly a,b,c.

R4 — Temporal separation: treatment information is available before selection and before future reveal.

R5 — Action-conditioned mapping completeness: treatment contains exactly one reconstructable future descriptor for each of a,b,c.

R6 — Future-space distinction: at least two of F(a), F(b), F(c) differ.

R7 — Control non-derivability: control cannot reconstruct the treatment-only mapping.

R8 — No recommendation: the treatment descriptor conforms to the allowlisted neutral structural schema and contains no normative/evaluative field; lexical scanning may supplement but cannot substitute for this structural check.

R9 — No prohibited quantities: reward/value/utility/performance/outcome information is absent.

R10 — Choice multiplicity: at least two actions remain admissible after treatment exposure.

R11 — Divergence opportunity: D6 is satisfied by an independent structural checker using an explicit treatment-induced divergence witness; arbitrary differing decision functions do not satisfy this check.

R12 — Null validity: null has comparable presentation structure but no future-space signal or recommendation.

R13 — No future reveal: successor state/accessibility are not exposed before selection.

R14 — Traceability: every future descriptor is reconstructable from the frozen transition specification and has an explicit action key.

Any failed R-check blocks fixture generation.

## 11. Required machine-checker outputs

The checker MUST return, at minimum:

- state_identity_pass
- current_tacc_identity_pass
- action_identity_pass
- temporal_separation_pass
- action_conditioned_mapping_complete
- future_descriptor_distinction_pass
- control_non_derivability_pass
- recommendation_schema_pass
- recommendation_lexical_diagnostic
- prohibited_information_absent
- choice_multiplicity_pass
- divergence_opportunity_pass
- null_validity_pass
- future_reveal_blocked
- traceability_pass
- overall_preflight_pass

For every failed check it MUST provide a machine-readable reason. No scientific execution result may be produced by this checker.

## 12. Fixture-generation boundary

Only after R1–R14 PASS may a new fixture be generated.

The new fixture MUST be a new version and MUST NOT overwrite, mutate, or delete v004 or its execution/audit records.

The v004 package remains a historical antecedent with its original hashes and status.

## 13. Scientific estimand boundary

The redesign does not introduce a composite TI score.

If later execution is authorized, the primary behavioural observable remains a condition difference in transformation selection/handling. No value, reward, utility, performance or outcome measure is part of the TI-001 primary inference.

## 14. Gate sequence

The required sequence is:

1. approve/fix this redesign specification;
2. run structural preflight against the specification itself, including review of the revised R8 schema constraint and D6 witness criterion;
3. only if PASS, implement/update the generator and checker;
4. run R1–R14 on the candidate design;
5. only if PASS, generate and freeze the new fixture;
6. perform the subsequent governance gate;
7. scientific execution remains separately authorized.

**Current execution status:** NOT AUTHORIZED.

**v004 status:** RETAINED / UNCHANGED / TRACEABLE.

**TGCV Core:** unchanged.
