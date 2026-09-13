# D-OPS-27 — C09 Directed Access-Intervention Discovery 001

**Status:** `CLOSED — NEW CANDIDATE CLASS IDENTIFIED / PREFLIGHT REQUIRED`
**Date:** 2026-09-13
**Purpose:** identify a causal intervention in which randomized assignment changes access to an explicitly available transformation, rather than merely changing incentives for an unchanged transformation set.

## 1. Discovery boundary

This operation follows the EDR rejection and does not reopen unrestricted domain discovery. It searches only for interventions satisfying the newly sharpened criterion:

`Z → explicit access-rule/capability change → T_acc,1 ≠ T_acc,0 → longitudinal subsequent choices/trajectory`

The intervention must leave meaningful downstream choice to the unit and must have a credible randomized or quasi-randomized contrast.

## 2. Candidate screening

### Candidate D27-A — Randomized access to distance-learning streaming

**Source:** randomized experiment in higher education, Switzerland/University of Zurich context.

The experiment randomized access to a streaming platform across students and weeks of the term. The same student could have access in some weeks and not in others. Students were not forced to use streaming and could still attend in person. The study reports take-up, attendance and exam-performance outcomes and maps exam questions to the weeks in which the required material was covered.

**Why it is materially different from EDR:** assignment does not merely change an incentive attached to an unchanged household action. It changes whether the online attendance mode is available at that decision point. The transformation profile can therefore be bounded around attendance-mode choices:

`U_tau = {attend_in_person, attend_online}`

with the intervention potentially producing:

`T_acc,0 = {attend_in_person}`
`T_acc,1 = {attend_in_person, attend_online}`

provided the exact experimental access rule supports this interpretation.

**Preliminary gates:**
- randomized/exogenous `Z`: PASS at study-design level;
- repeated within-student treatment variation: PASS;
- explicit access contrast: PROMISING;
- finite candidate transformation universe: PROMISING, requires operational freeze;
- subsequent trajectory: PROMISING;
- independent public reconstruction/data availability: OPEN;
- exact `P_tau`: OPEN;
- no direct trajectory prescription: PASS at design level.

**Disposition:** `LEAD CANDIDATE — ADMIT TO CONTROLLED PREFLIGHT`

### Candidate D27-B — One Laptop per Child / technology access

Randomized provision of laptops clearly increases technology access and has longitudinal outcome evidence. However, the transformation universe is much broader and less naturally finite than D27-A, and the distinction between access to a device and accessibility of a bounded transformation is less clean.

**Disposition:** `SECONDARY — DO NOT PREFLIGHT YET`

### Candidate D27-C — Randomized access to digital health / clinical information

Several randomized studies provide users or clinicians with additional digital access. These establish causal access effects, but the accessible transformation universe is generally not explicit enough to satisfy the present TGCV rule-layer requirement without substantial analyst interpretation.

**Disposition:** `SECONDARY / LOW PRIORITY`

### Candidate D27-D — Platform feature-access experiments

Online field experiments frequently randomize access to new features. They are conceptually strong because feature availability can directly alter the action set, and long-horizon randomized feature experiments exist. However, most detailed assignment/exposure logs are proprietary, which makes independent reconstruction of `U_tau`, `P_tau`, and trajectories difficult for an external TGCV execution.

**Disposition:** `CONCEPTUALLY STRONG / EVIDENCE-PROVENANCE RISK`

## 3. Selection decision

D27-A is selected for the next controlled preflight because it combines the four properties currently missing from EDR more cleanly:

1. explicit randomized access assignment;
2. an identifiable access boundary;
3. a naturally bounded alternative-action profile;
4. repeated subsequent decisions and longitudinal outcomes.

The published experiment explicitly states that access to the streaming platform was randomized across students and weeks, while students retained the option to attend in person. This makes it a substantially stronger candidate for `Z → ΔT_acc` than an incentive-only demand-response intervention.

## 4. Critical caution

D27-A is **not yet admitted as C09 evidence**.

The key unresolved question is whether `attend_online` can legitimately be treated as a TGCV transformation whose accessibility is changed by `Z`, rather than merely as a channel/interface through which the same underlying educational transformation is performed.

The next preflight must therefore test the ontology of the transformation unit before any causal execution is considered.

## 5. Next controlled operation

Produce a candidate-specific admissibility preflight for D27-A covering:

`S0,C0,L,U_tau,P_tau,T_acc,0,T_acc,1,Z,Y`

with special gates:

- transformation identity;
- access-rule identity;
- completeness of `U_tau`;
- ex-ante `P_tau`;
- independence of `Y` from accessibility adjudication;
- availability of reconstructible longitudinal evidence.

No execution, new dataset acquisition, RUST/SWIM rerun, or C09 claim upgrade is authorized by this discovery record.

## 6. External evidence used for screening

- Distance Learning in Higher Education: Evidence from a Randomized Experiment, Journal of the European Economic Association. The experiment randomized platform access across students and weeks and allowed students to choose between online and in-person attendance.
- Technology and Child Development / One Laptop per Child randomized evaluation: evidence of randomized expansion of technology access, retained only as a secondary candidate because its transformation universe is less bounded.
- Randomized online field experiments and feature-access experiments: retained as a conceptual class, subject to proprietary-data provenance constraints.

## 7. Governance disposition

`C09 = H — NO CAUSAL IDENTIFICATION`

`D27-A = LEAD CANDIDATE — PREFLIGHT ONLY`

`EXECUTION AUTHORIZATION = NONE`

`NEW DATASET ACQUISITION = NONE`

`SWIM RERUN = NONE`

`RUST RERUN = NONE`

`CLAIM UPGRADE = NONE`
