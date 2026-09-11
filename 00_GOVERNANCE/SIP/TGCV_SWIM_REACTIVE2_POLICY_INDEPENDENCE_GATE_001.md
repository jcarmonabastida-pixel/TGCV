# TGCV — SWIM Reactive2 Policy-Independence Validation Gate 001

**Date:** 2026-09-11

**Status:** `PREPARED — NOT EXECUTED`

**Purpose:** test whether the bounded TGCV accessibility reconstruction observed in Reactive-0 remains analytically separable from a different native policy-selection mechanism.

## 1. Why this is the next operation

Reactive-0 closed the current local operationalization surface. The next useful question is therefore not whether Reactive-0 can be repeated, but whether the separation

`candidate identity → accessibility → T_acc → policy selection`

survives a change in the adaptation policy.

SWIM already provides `Reactive2AdaptationManager`, making Reactive2 a low-cost, policy-differentiated validation surface without changing the underlying system domain.

## 2. Falsifiable question

**Does changing the native adaptation-manager policy alter the reconstructed accessibility predicate itself, or only the selection of transformations from an accessibility space that remains independently defined?**

### Supporting TGCV expectation

For comparable pre-decision states/contexts:

`Pτ(S_t,C_t)` should remain defined independently of which native adaptation manager selects a transformation.

The selected transformation may differ while the candidate accessibility relation remains reconstructable from state/context and execution constraints.

### Falsifier

The gate fails if accessibility cannot be defined independently of the Reactive2 selection policy, or if the purported `Pτ` predicate collapses into the policy's own selection rule.

## 3. Scope

Use the existing SWIM infrastructure and frozen inputs already established for the local surface. No new dataset is authorized by this gate.

Candidate universe remains bounded to the previously established families:

`Uτ = {AddServer, RemoveServer, SetDimmer(k)}`

Only transformation values actually observed/reconstructable in the execution should be represented; no exhaustive dimmer-domain claim is permitted.

## 4. Required reconstruction

For each usable Reactive2 decision point:

1. reconstruct `S_t,C_t` before the decision;
2. identify candidate transformation identity;
3. evaluate `Pτ(S_t,C_t)` independently of the selected action;
4. reconstruct the bounded `T_acc,t`;
5. record the native policy selection separately;
6. compare the accessibility representation with the Reactive-0 representation only where state/context are genuinely comparable;
7. keep outcome and post-decision information outside the accessibility predicate.

## 5. Acceptance criteria

`A1` Execution integrity PASS.

`A2` Frozen input provenance PASS.

`A3` At least one Reactive2 decision point with reconstructable pre-decision state/context PASS.

`A4` Candidate identity reconstructable independently of policy selection PASS.

`A5` Accessibility predicate reconstructable independently of selected action PASS.

`A6` At least one bounded `T_acc,t` snapshot reconstructed PASS.

`A7` Policy selection recorded as a distinct downstream layer PASS.

`A8` If comparable states exist, no contradiction between the accessibility representation and the Reactive-0 bounded representation PASS; otherwise report `NOT_COMPARABLE` without forcing equivalence.

## 6. Stop conditions

Stop without interpretation upgrade if:

- required pre-decision variables cannot be reconstructed;
- accessibility requires outcome information;
- candidate identity depends on knowing the selected action;
- Reactive2 changes the system semantics rather than only the adaptation policy;
- comparable state/context cannot be established.

## 7. Claim boundary

A PASS would strengthen bounded support for the methodological distinction between accessibility and policy selection, especially C02/C16, but would **not** upgrade any claim level automatically.

It would not establish:

- transversal validity;
- causal effects on trajectories;
- value generation;
- explanatory superiority;
- industrial utility;
- general validity across self-adaptive systems.

## 8. Execution authorization

`EXECUTION = NOT AUTHORIZED BY THIS RECORD`

This document is a gate specification only. Execution requires the normal preflight/authorization sequence and a separately recorded execution result.

## 9. Programme disposition

This gate is preferred to another Reactive-0 repetition because it changes the **policy-selection layer** while retaining the same controlled empirical domain. Its scientific purpose is therefore incremental and falsifiable rather than duplicative.
