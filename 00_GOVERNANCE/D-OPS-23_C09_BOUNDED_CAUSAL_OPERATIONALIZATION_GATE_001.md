# D-OPS-23 — C09 Bounded Causal Operationalization Gate 001

**Status:** `OPEN — DESIGN GATE / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-12
**Candidate:** Southwestern-China randomized emergency demand-response (EDR), 2019

## 1. Purpose

Determine whether the bounded EDR candidate can instantiate the C09 causal design without conflating accessibility with incentives, realized behaviour or outcome trajectory.

C09 target relation:

`Z → ΔT_acc → subsequent trajectory`

The gate is bounded to the declared experimental population, event window, action profile and observation horizon. It does not require universal domain coverage.

## 2. Evidence baseline

The published EDR experiment randomly assigned permission to apply for the programme across 205,129 households, used 15-minute smart-meter observations, and conducted six trials between 18 July and 21 August 2019. The experimental design distinguishes assignment winners, targeted participants, no-reply participants and a no-notification comparison group. citeturn0search0turn0search1

## 3. Required frozen operationalization

### 3.1 Unit
One uniquely identified household-event observation with a reconstructible pre-event state `S0` and context `C0`.

### 3.2 Transformation universe
`U_tau` must be a finite, explicitly enumerated profile of controllable demand-response transformations available during the declared 90-minute event window.

The universe is required to be complete **within this frozen operational profile**, not complete over all physically possible household behaviours.

### 3.3 Accessibility rule
`P_tau(S0,C0,L)` must determine eligibility/access before observing the post-event trajectory.

Critical separation:

- `accessibility`: whether the household is permitted/exposed to the EDR transformation opportunity;
- `incentive`: rebate magnitude or economic motivation;
- `outcome`: realized consumption trajectory.

The operationalization fails if these are collapsed into one variable.

### 3.4 Intervention
`Z` is the randomized assignment affecting permission/access to apply for EDR.

For C09, admissibility requires showing:

`T_acc,1 = {tau in U_tau | P_tau(S0,C0,L,Z=1)=1}`

and

`T_acc,0 = {tau in U_tau | P_tau(S0,C0,L,Z=0)=1}`

with a demonstrable difference attributable to assignment rather than to the realized outcome.

The source study explicitly states that permission to apply was randomly assigned and that the assignment supports an ITT estimate. citeturn0search0

### 3.5 Outcome trajectory
`Y` must be reconstructed independently from the 15-minute consumption sequence after the intervention boundary. It must not enter the definition of `P_tau` or `T_acc`.

## 4. Gate tests

**G1 — unique unit identity:** PASS bounded.

**G2 — pre-treatment state/context:** PASS at design level; exact frozen variable list remains to be specified.

**G3 — bounded-complete U_tau:** OPEN. A concrete finite action profile must be enumerated and justified.

**G4 — ex-ante P_tau:** OPEN. Programme eligibility/access conditions must be translated into an explicit predicate without post-treatment variables.

**G5 — Z changes accessibility rather than merely outcome/incentive:** OPEN / CRITICAL. Random assignment to permission is strong evidence, but the TGCV mapping must demonstrate that the assigned permission corresponds to a difference in admissible transformations, not merely a change in motivation.

**G6 — counterfactual:** PASS at causal-design level because random assignment supplies treatment/control comparison. citeturn0search0turn0search1

**G7 — trajectory independent of accessibility adjudication:** PASS design requirement; must be enforced in the frozen implementation.

**G8 — no direct trajectory encoding:** PASS preliminary. Assignment does not prescribe the household's subsequent 15-minute consumption sequence. citeturn0search0

**G9 — temporal ordering:** PASS. Assignment precedes the 20:00–21:30 response window and subsequent observed consumption.

**G10 — provenance/reconstruction:** OPEN until the exact data fields, assignment records and protocol variables required for `U_tau`, `P_tau`, `T_acc` and `Y` are demonstrated as independently reconstructible.

## 5. Stop conditions

Stop and reject C09 execution if any of the following occurs:

1. `U_tau` cannot be made finite and complete for the frozen operational profile;
2. `P_tau` requires realized consumption or another post-treatment variable;
3. assignment changes only an incentive/outcome channel and cannot be represented as accessibility change;
4. the treatment/control boundary cannot be reconstructed independently;
5. the intervention directly specifies the subsequent trajectory;
6. the outcome trajectory cannot be independently reconstructed;
7. provenance is insufficient for independent reconstruction.

## 6. Current decision

**C09 BOUNDED CAUSAL OPERATIONALIZATION = OPEN.**

The candidate remains **promising and design-admissible**, but execution is not yet authorized because `U_tau`, `P_tau`, the exact accessibility-change mapping, and provenance have not yet been frozen at the required operational level.

This is deliberately narrower than D-OPS-23's bounded screening pass. No causal result is inferred from the published EDR outcome itself.

## 7. Next controlled operation

Produce the **C09 EDR operational specification/preflight** for one frozen event profile, limited to:

`U_tau → P_tau → T_acc,0/T_acc,1 → Z → Y`

and verify the information firewall before any empirical execution.

**No execution authorization. No new data acquisition. No model fitting. No AWS/Rust/SWIM execution.**
