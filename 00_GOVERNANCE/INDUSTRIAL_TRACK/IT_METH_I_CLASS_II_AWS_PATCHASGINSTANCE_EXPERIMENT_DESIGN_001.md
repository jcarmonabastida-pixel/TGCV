# IT-METH-I — Class II AWS-PatchAsgInstance Experimental Design 001

**Status:** `DESIGN FROZEN — NOT EXECUTED`
**Date:** 2026-09-10
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`
**Candidate:** `AWS-PatchAsgInstance`

## 1. Experimental question

Can a bounded representation of state-dependent transformations distinguish the accessibility conditions created by `AWS-PatchAsgInstance` from an ordinary patching path within the same reproducible fixture, without using post-decision outcomes to define the decision-time state?

The experiment is about the **fixture and representation**, not about industrial performance.

## 2. Experimental boundary

The unit is one EC2 instance associated with an Auto Scaling group and a frozen patch-management configuration.

The relevant state is the pre-decision state available before invocation of the patching transformation.

The candidate transformation is the governed invocation of `AWS-PatchAsgInstance` with frozen `InstanceId` and runbook parameters.

A comparator must represent an alternative patching transformation under the same initial state and evidence boundary, without importing information generated only after the decision.

## 3. Required frozen inputs

Before execution, the fixture package must freeze:

1. infrastructure/template version;
2. Auto Scaling group identity within the fixture;
3. target instance identity;
4. lifecycle and health/replacement configuration;
5. OS/image identity;
6. patch group and baseline identity/version;
7. pre-decision patch compliance state;
8. exact runbook identifier/version available to the fixture;
9. all runbook parameter values;
10. comparator definition;
11. accessibility predicates for candidate transformations;
12. temporal cutoff defining pre-decision evidence.

## 4. Primary measurements

The experiment will not infer value from the fact that a runbook exists.

Primary measurements are structural/representational:

- `T_acc`: transformations accessible from the frozen state;
- accessibility predicates and their observable variables;
- state transition representation;
- `ΔT_acc` after the governed transformation;
- downstream trajectory representation, where observable inside the fixture;
- reproducibility across independent executions/reconstructions.

## 5. Discriminative test

The central comparison is:

`ordinary patch path` versus `AWS-PatchAsgInstance`

under an identical frozen starting state.

A useful result requires that the representation identify a decision-relevant difference in accessible transformations or their enabling/limiting conditions **before relying on post-decision outcomes**.

A result that only distinguishes realized outcomes is not sufficient for the intended accessibility claim.

## 6. Non-claims

This Class II experiment cannot establish:

- industrial utility in a real organization;
- operational superiority in production;
- financial value;
- causal impact on industrial performance;
- universal/general applicability;
- superiority over existing industrial methods.

## 7. Execution gates

Execution is prohibited until a separate pre-execution record confirms:

- fixture bytes/version frozen;
- all mandatory inputs available;
- comparator operationalized;
- metric operationalized;
- effort convention frozen if effort is measured;
- two independent reconstruction paths defined;
- no post-decision leakage into pre-decision variables;
- evidence provenance recorded.

No IT-G1 or IT-G5 authorization is implied by this design.

## 8. Falsification conditions

The fixture experiment should be treated as negative/inconclusive if:

1. candidate and comparator cannot be distinguished from the same frozen pre-decision state;
2. accessibility requires post-decision outcomes;
3. required state variables cannot be independently reconstructed;
4. two reconstructions disagree materially without a resolvable cause;
5. the observed distinction is merely documentary naming rather than a transformation/accessibility difference;
6. the metric cannot discriminate the candidate from the comparator.

## 9. Expected methodological contribution

If executed successfully, the experiment can test whether a Class II fixture is sufficient to demonstrate **bounded structural/representational feasibility** of TGCV mechanisms without conflating that result with industrial evidence.

It therefore functions as a methodological bridge between pure conceptual feasibility and a future Class I industrial utility test.
