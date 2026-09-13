# TGCV — C09 Controlled Execution Protocol 001

**Status:** `PROTOCOL FROZEN — EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent:** `TGCV_C09_CONTROLLED_DOMAIN_CANDIDATE_SELECTION_AUDIT_001.md`

## 1. Scientific question

Test the bounded causal proposition:

`exogenous accessibility intervention → ΔT_acc → subsequent trajectory`

The protocol does not test value, industrial utility, predictive superiority, universality, or transversal validity.

## 2. Frozen domain

Finite candidate universe:

`U = {A,B,C}`

Frozen decision-time state/context:

`S0,C0`

Accessibility resource:

`R1`

Accessibility rule:

- `A` accessible in both arms;
- `C` accessible in both arms;
- `B` accessible iff `R1=true`.

Therefore the design-validation fixture has:

`T_acc,0={A,C}`
`T_acc,1={A,B,C}`

The intervention is `Z ∈ {0,1}`, with `Z=1` enabling `R1`.

## 3. Randomization and unit

Unit = independently seeded replica of the same frozen system.

After all pre-treatment inputs are sealed, assign replicas to treatment/control using a predeclared deterministic seeded randomization procedure.

No assignment may depend on any generated trajectory, transformation identity, or post-assignment observation.

Eligibility, exclusions and seed allocation are frozen before execution.

## 4. Execution sequence

For every replica:

1. load frozen package;
2. verify package/hash integrity;
3. seal `S0,C0,U,L,G,P,objective,metric,H`;
4. assign `Z`;
5. derive `T_acc,Z`;
6. verify accessibility-set hash;
7. execute exactly one decision/transition step (`H=1`);
8. record the resulting trajectory endpoint `Y`;
9. record all canonical hashes and execution metadata;
10. terminate without adaptive parameter changes.

No exploratory reruns may modify the frozen protocol.

## 5. Invariant trajectory mechanism

The following artefacts are identical in treatment and control:

- transformation definitions;
- transition function `G`;
- decision policy `P(S,C,T_acc)`;
- objective/scoring rule;
- execution engine;
- observation procedure;
- trajectory metric;
- randomization algorithm after assignment.

`Z` may be consumed only by the accessibility calculation through `R1`.

Any other dependency is a protocol violation and stops the experiment.

## 6. Primary endpoint

`Y` is the prespecified one-step trajectory endpoint: the canonical next-state/selected-transformation record generated after accessibility has been evaluated.

Primary causal contrast:

`τ = E[Y(1)-Y(0)]`

The endpoint is evaluated using the frozen metric defined before execution. No metric may be selected or changed after seeing outcomes.

## 7. Secondary structural checks

Report separately:

1. `ΔT_acc` between arms;
2. trajectory endpoint difference;
3. treatment/control execution counts;
4. protocol/hash violations;
5. null-intervention results;
6. independent reconstruction agreement.

Structural checks must never be substituted for the primary causal endpoint.

## 8. Null-intervention control

A predeclared null arm uses an intervention token that does not alter `R1` or any accessibility predicate.

Expected:

`T_acc,null = T_acc,baseline`

and no systematic treatment-induced trajectory contrast attributable to the intervention token.

Failure blocks causal interpretation until diagnosed.

## 9. Falsification and stopping rules

Stop and classify `BLOCKED` or `INCONCLUSIVE` if:

- frozen hashes differ unexpectedly;
- `Z` reaches `G`, objective, policy except through `T_acc`, execution or observation code;
- `T_acc,0=T_acc,1` when the declared intervention is applied;
- accessibility uses post-treatment information;
- randomization or eligibility depends on outcomes;
- trajectory endpoint or metric is altered post hoc;
- independent reconstruction disagrees with the primary execution;
- null control exhibits an unexplained accessibility or trajectory effect;
- any unregistered input affects execution.

A successful execution requires all integrity checks to pass; statistical/causal inference is then performed only within the declared finite domain and H=1 scope.

## 10. Independent reconstruction

Executor-2 receives only the frozen protocol, frozen package and declared execution bundle. It must not receive Executor-1 outcomes before producing its own reconstruction.

Executor-2 independently reconstructs:

`S0,C0,U,L,T_acc,0,T_acc,1,G,P,Y`

and compares canonical hashes and endpoint records after its own execution.

Any disagreement is recorded before adjudication. The two executions are not silently merged.

## 11. Evidence firewall

The following are prohibited from entering the frozen protocol after execution begins:

- observed outcomes;
- exploratory runs;
- later candidate results;
- value analyses;
- changes to TGCV Core;
- changes to RMA or claim matrix intended to influence execution;
- external coaching concerning the expected outcome.

## 12. Claim boundary

Even if the primary causal contrast is positive, the result may support only a bounded statement that, in this controlled finite domain and under the frozen intervention and H=1 protocol, changing accessibility conditions causally changes the subsequent trajectory endpoint.

It does not establish general C09 universality or value creation.

## 13. Authorization

`EXECUTION AUTHORIZATION = NONE`

This document freezes the protocol. A separate **C09 Controlled Execution Protocol Audit 001** must verify internal consistency and independence boundaries before an explicit execution authorization can be issued.

Next sequence:

`protocol audit → explicit authorization → Executor-1 controlled execution → Executor-2 independent reconstruction → adjudication → C09 assessment`
