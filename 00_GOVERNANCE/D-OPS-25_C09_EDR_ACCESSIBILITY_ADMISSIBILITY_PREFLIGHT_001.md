# D-OPS-25 — C09 EDR Accessibility Admissibility Preflight 001

**Status:** `OPEN — PREFLIGHT / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Candidate:** Southwestern-China randomized emergency demand-response (EDR), 2019
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories

## 1. Purpose

Translate the already selected EDR candidate into the smallest pre-execution admissibility test needed to determine whether its randomized assignment can legitimately instantiate a TGCV accessibility intervention.

This preflight is deliberately narrower than the completed FOS/SWIM work. FOS/SWIM already establishes bounded reconstruction of accessibility-space change and its subsequent trajectory linkage, but not causal identification. The present preflight tests only whether the EDR intervention can supply the missing causal contrast.

## 2. Required causal mapping

The candidate must support, using information available before post-treatment trajectory observation:

`S0,C0,L,U_tau → P_tau(S0,C0,L,Z) → T_acc,0 / T_acc,1 → Z → Y`

with randomized `Z` providing the counterfactual contrast.

The critical scientific requirement is not merely that `Z` affects consumption. It is that `Z` changes the set/structure of transformations that are accessible under the frozen operational profile.

## 3. Preflight tests

### A1 — Frozen decision-time unit

**Requirement:** uniquely identified household-event unit with a reconstructible pre-treatment state/context sufficient to evaluate accessibility before treatment outcome.

**Pass condition:** every variable used by `P_tau` is determined no later than the intervention-assignment boundary.

**Fail:** any accessibility variable requires realized post-treatment consumption, programme response, or later information.

### A2 — Finite bounded transformation universe `U_tau`

**Requirement:** enumerate a finite transformation profile over the declared event window.

A defensible bounded profile may be expressed as prespecified controllable load-change actions or state-transition classes, but it must not be reverse-engineered from observed treatment trajectories.

**Pass condition:** completeness can be stated relative to a frozen operational profile and independently reconstructed for both assignment arms.

**Fail:** the universe is simply the set of behaviours observed after treatment, or completeness cannot be justified within the declared profile.

### A3 — Ex-ante accessibility predicate `P_tau`

**Requirement:** define a rule that maps frozen state/context and assignment to accessible transformations.

`T_acc,z = {τ ∈ U_tau | P_tau(S0,C0,L,z)=1}`

**Pass condition:** `P_tau` uses only pre-treatment programme rules/eligibility/access conditions and frozen state/context.

**Fail:** `P_tau` incorporates rebate realization, actual participation, realized consumption, or any other post-treatment variable.

### A4 — Accessibility manipulation test — CRITICAL

The randomized assignment must alter accessibility itself.

**Pass requires all three:**

1. `Z` changes a permission, eligibility or enabling condition that determines whether at least one member of `U_tau` is accessible;
2. the resulting `T_acc,1 ≠ T_acc,0` can be demonstrated without inspecting the subsequent consumption trajectory;
3. the intervention does not itself prescribe or select the downstream trajectory.

**Fail:** if assignment only changes incentive magnitude, information, or realized behaviour while `T_acc,1 = T_acc,0` under the frozen rule.

### A5 — Counterfactual integrity

**Requirement:** random assignment remains the treatment/control source for the causal comparison and is not conditioned on post-treatment participation or response.

**Pass:** intention-to-treat contrast can be defined at assignment level.

**Fail:** treatment is redefined as actual participation, successful response, or another post-assignment variable.

### A6 — Independent trajectory outcome `Y`

**Requirement:** define the subsequent trajectory from the post-boundary 15-minute consumption sequence independently of accessibility adjudication.

**Pass:** `Y` and its horizon/metric are frozen before inspecting treatment outcomes.

**Fail:** outcome definition is selected after observing which trajectories differ.

### A7 — Direct-path exclusion

The intervention must not directly force the target trajectory.

**Pass:** assignment creates/withdraws an accessible opportunity while households retain autonomous subsequent transformation choices.

**Fail:** assignment specifies the sequence, target load profile, or another mechanism equivalent to the outcome itself.

### A8 — Provenance and independent reconstruction

**Requirement:** the exact assignment variable, programme rules, event timing, baseline fields and post-event trajectory fields needed for A1–A7 are independently reconstructible from frozen public evidence.

**Pass:** another executor can reconstruct the same classification without analyst-supplied facts.

**Fail:** essential elements depend on undocumented interpretation or unavailable raw fields.

## 4. Decision logic

`PASS` requires A1–A8 all PASS, with special attention to A4.

If A1–A3, A5–A8 pass but A4 fails, the EDR candidate is **rejected for C09 causal execution** because the intervention does not instantiate the TGCV causal treatment of interest.

If A8 cannot be established, the candidate remains **inadmissible / unresolved** and no execution is authorized.

A successful preflight does not itself establish C09. It only permits a separately authorized causal execution.

## 5. Information firewall

Before any execution authorization, freeze:

- event profile and horizon;
- unit definition;
- `U_tau` and completeness boundary;
- `P_tau` and all inputs;
- treatment assignment definition `Z`;
- `T_acc,0` / `T_acc,1` reconstruction rule;
- trajectory outcome `Y`;
- primary estimand;
- exclusion/confounding rules;
- falsification and stop conditions.

No observed post-treatment trajectory may be used to repair `U_tau`, `P_tau`, treatment definition or eligibility.

## 6. Current gate status

| Gate | Status |
|---|---|
| A1 Frozen decision-time unit | OPEN — to verify from source evidence |
| A2 Finite bounded `U_tau` | OPEN |
| A3 Ex-ante `P_tau` | OPEN |
| A4 `Z → ΔT_acc` accessibility manipulation | OPEN — CRITICAL |
| A5 Counterfactual integrity | DESIGN PASS / source verification open |
| A6 Independent `Y` | DESIGN PASS / source verification open |
| A7 Direct-path exclusion | DESIGN PASS / source verification open |
| A8 Provenance/reconstruction | OPEN |

**Preflight result:** `NOT YET ADMISSIBLE`

## 7. Next controlled action

The next operation is an evidence-only source reconstruction of A1–A8 from the already selected EDR study/materials. No new domain search is justified and no FOS/SWIM/RUST execution is justified.

The reconstruction must stop at the first critical failure, especially A4. If A4 cannot be demonstrated from ex-ante intervention semantics, C09 execution is not authorized and the EDR candidate is closed as causally inadmissible.

## 8. Governance boundary

`EXECUTION AUTHORIZATION = NONE`

`NEW DATASET ACQUISITION = NONE`

`SWIM RERUN = NONE`

`RUST-DYN-2 RERUN = NONE`

`CLAIM UPGRADE = NONE`
