# TGCV — C09 Controlled Domain Pre-Execution Package 001

**Status:** `DESIGN / CONTROLLED / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent:** `TGCV_C09_CANDIDATE_CLASS_DECISION_GATE_001.md`

## 1. Purpose

Define the minimum controlled domain needed to close the remaining causal gap without depending on restricted external datasets.

The experiment is designed to test only:

`exogenous accessibility intervention → ΔT_acc → subsequent trajectory`

It does not test value generation, industrial utility, predictive superiority, originality or transversal validity.

## 2. Domain architecture

Use a finite, fully reproducible synthetic transformation system with:

- frozen initial state `S0`;
- frozen context `C0`;
- finite candidate transformation universe `U`;
- deterministic accessibility rule `L`;
- exogenous binary intervention `Z`;
- invariant trajectory-generating rule `G`;
- fixed observation horizon `H`;
- independently reconstructed trajectory `Y`.

Define:

`T_acc,z = {u ∈ U : L(S0,C0,u,z)=1}`

and require:

`T_acc,0 ≠ T_acc,1`.

The intervention must modify only the accessibility predicate. It must not modify `G`, the objective/scoring rule, state-transition equations, execution capacity, or observation procedure.

## 3. Minimal intervention design

Construct paired worlds from identical frozen `(S0,C0,U)`:

- **Control:** `Z=0`, baseline accessibility rule.
- **Treatment:** `Z=1`, one predeclared enabling condition changes accessibility for a known subset of `U`.

The intervention must be exogenous to the subsequent trajectory and must not encode which transformation will actually be selected.

A valid manipulation therefore has the form:

`L_0 ≠ L_1` while `G_0 = G_1`.

A manipulation is invalid if it changes the transition rule, objective, scoring, random seed after assignment, observation mechanism, or directly forces a target transformation.

## 4. Trajectory definition

For each paired world, the system generates a trajectory under the same invariant decision/transition mechanism. The primary trajectory endpoint is a prespecified ordered sequence of post-decision transformations/states over horizon `H`.

Primary causal estimand:

`τ = E[Y(1) − Y(0)]`

with `Y` defined before execution and independent of the accessibility classification.

H=1 may be used for the first minimal experiment, but its scope must remain explicitly one-step. Any claim concerning H>1 requires separate evidence.

## 5. Information firewall

Before any outcome is generated, freeze and hash:

1. `S0` and `C0`;
2. candidate universe `U`;
3. accessibility rules `L0,L1`;
4. intervention assignment mechanism;
5. invariant trajectory rule `G`;
6. objective/scoring rule;
7. horizon `H`;
8. primary estimand and trajectory metric;
9. confounder/alternative register;
10. falsification and stopping criteria.

No future trajectory, outcome, value metric or exploratory result may alter any frozen input.

## 6. Required design-validation tests before execution

### DV1 — Accessibility manipulation

On a frozen fixture, independently verify `T_acc,0 ≠ T_acc,1`.

### DV2 — Trajectory-rule invariance

Verify byte-level/canonical equality of `G0` and `G1` and all transition/scoring parameters except the declared accessibility intervention.

### DV3 — No target encoding

Verify that the intervention does not contain the identity of the transformation that will subsequently occur.

### DV4 — State/context identity

Verify identical `S0,C0,U` across paired worlds.

### DV5 — Independent reconstruction

A second execution path must reconstruct `T_acc,0`, `T_acc,1` and `Y` from the frozen package without access to the first outcome.

### DV6 — Null intervention control

Include a predeclared null intervention in which accessibility is unchanged. This checks that the measurement pipeline does not manufacture `ΔT_acc` or trajectory differences.

## 7. Falsification / stop criteria

The experiment is INCONCLUSIVE/BLOCKED if any of the following occurs:

- `T_acc,0 = T_acc,1`;
- intervention changes `G` or another direct trajectory mechanism;
- treatment assignment leaks the target trajectory;
- `S0,C0,U` differ between paired worlds;
- trajectory cannot be independently reconstructed;
- accessibility classification uses post-treatment information;
- outcome metric changes after seeing results;
- null intervention produces unexplained accessibility change;
- reproducibility/hash checks fail.

A causal PASS requires verified accessibility change, invariant trajectory mechanism, independent reconstruction, prespecified trajectory contrast and successful falsification checks.

## 8. Scope of inference

A PASS establishes only a bounded causal demonstration within the controlled domain:

`Z → ΔT_acc → Y`.

It does not establish universality, cross-domain validity, value creation, industrial superiority or that accessibility is the only mechanism relevant to trajectories outside the controlled system.

## 9. Execution boundary

`EXECUTION AUTHORIZATION = NONE`

This package is design-only. No scientific execution is authorized until a separate design audit confirms that the intervention changes accessibility independently of the trajectory-generating mechanism and that the complete frozen/reconstruction protocol is internally consistent.

## 10. Next operation

Perform the **C09 Controlled Domain Design Audit 001**. The audit must inspect the concrete intervention, formal accessibility rule, trajectory rule, information firewall, reconstruction architecture and falsification criteria. Only a PASS at that audit may open an execution-package construction stage.
