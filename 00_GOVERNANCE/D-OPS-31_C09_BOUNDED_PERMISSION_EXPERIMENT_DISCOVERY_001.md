# D-OPS-31 — C09 Bounded Permission Experiment Discovery 001

**Status:** `CLOSED — DISCOVERY SHORTLISTED / PREFLIGHT REQUIRED`
**Date:** 2026-09-13
**Objective:** identify C09 candidates in which randomization changes an explicit executable capability/resource boundary and the post-intervention transformation space can plausibly satisfy TR-132.

## 1. Decision

D-OPS-30 showed that MTO fails because a human mobility trajectory cannot be safely compressed into a binary relocation profile without a TGCV-native sufficiency proof.

D-OPS-31 therefore narrows discovery to interventions where the accessible action space is itself explicit, finite or tightly bounded, and observable before subsequent outcomes.

No candidate is admitted to execution. All candidates require a dedicated TR-132 preflight.

## 2. Candidate D31-A — Inpatient portal function access

**Source:** McAlearney et al., *JAMA Network Open* (2022).

A randomized clinical trial with 2,892 inpatients compared access to **all portal functions** against access to a limited subset of functions, alongside a separate training comparison. The study measured portal use, patient satisfaction and involvement in care. citeturn0search13

### TGCV interpretation

`Z = randomized assignment to full vs limited portal functionality`

Candidate bounded space:

`U* = {available portal functions actually exposed by the trial}`

Potential accessibility transition:

`T_acc,0 = limited function set`

`T_acc,1 = expanded function set`

### Preliminary gate

- Stable decision-time unit: **PASS/PROMISING**
- Explicit intervention boundary: **PASS** — the treatment directly changes which portal functions are executable.
- Ex-ante randomization: **PASS**. citeturn0search13
- Bounded transformation vocabulary: **PROMISING** — function availability is explicitly configured.
- Longitudinal subsequent state: **PARTIAL/PROMISING** — portal-use trajectories are available, but the TGCV meaning of subsequent transformation must be established.
- TR-132 sufficiency: **OPEN**.

**Disposition:** `LEAD CANDIDATE FOR D-OPS-32`

## 3. Candidate D31-B — Generative-AI capability access

**Source:** Dillon, Jaffe, Immorlica & Stanton, Microsoft Research (2025), six-month randomized field experiment.

Approximately 6,000 knowledge workers participated; half received access to a generative-AI tool integrated into applications used for email, documents and meetings. The study reports changes in work patterns over six months. citeturn0search8

### TGCV interpretation

`Z = randomized access to AI capability`

Potential bounded domain:

`U* = task transformations executable with vs without the integrated AI capability`

### Preliminary gate

- Randomized access: **PASS/PROMISING**
- Capability boundary: **PASS/PROMISING** — access is materially changed.
- Stable task-level transformation identity: **OPEN**.
- Bounded `U*`: **OPEN**.
- Longitudinal trajectory: **PASS/PROMISING** — six-month behavioral/work-pattern data.
- TR-132 sufficiency: **OPEN — likely difficult** because the task space and human-AI workflow transformations are broad.

**Disposition:** `SECONDARY / DO NOT PREFLIGHT BEFORE D31-A`

## 4. Candidate D31-C — Digital appointment-system access

**Source:** *Journal of Public Economics* (2023), large-scale randomized experiment in Uruguay.

The experiment randomized 47,600 eligible women to invitations to use a government digital medical-appointment system versus usual local-clinic invitations, with outcomes over 16 weeks. citeturn0search4

### Preliminary gate

- Randomized intervention: **PASS**
- Resource/capability boundary: **PARTIAL** — treatment changes the transaction route and access cost, but may resemble the rejected channel/interface problem.
- Explicit finite transformation vocabulary: **OPEN**.
- Longitudinal trajectory: **PASS/PROMISING**.
- TR-132 sufficiency: **OPEN**.

**Disposition:** `SECONDARY / LIKELY REJECT IF ONLY CHANNEL ACCESS`

## 5. Candidate D31-D — Portal-integrated clinical decision-support access

A randomized study of 48 radiology residents compared access to the same clinical decision-support tool through a PACS-integrated portal versus a separate web interface; groups were switched halfway through a 10-month study. Use changed substantially when integrated access was added or removed. citeturn0search15

### Preliminary gate

- Longitudinal randomized/crossover structure: **PASS**
- Explicit access change: **PASS**
- Transformation identity: **FAIL/PROMISING depending on scope** — the intervention may again be an interface/access-route change rather than a change in executable capability.
- TR-132 sufficiency: **OPEN**.

**Disposition:** `SECONDARY / DO NOT PRIORITIZE`

## 6. Discovery result

The search establishes a materially better candidate class than MTO:

`randomized capability configuration → explicit finite executable function space → subsequent usage/state trajectory`

The strongest current candidate is **D31-A — inpatient portal full-vs-limited functionality**, because the intervention changes the function set itself rather than merely changing presentation or channel.

This distinction is now explicit:

- **Channel/interface access:** generally insufficient unless it changes executable transformations.
- **Information/incentive access:** generally insufficient unless it changes executable transformations.
- **Explicit function/capability availability:** potentially admissible.

## 7. Next operation

**D-OPS-32 — Inpatient Portal Full-vs-Limited Functionality TR-132 Preflight.**

The preflight must establish, from the published trial protocol and available outcome definitions:

1. exact `S0,C0`;
2. exact randomized treatment contrast;
3. exact finite `U*` of portal functions;
4. ex-ante `P_tau` for each relevant function;
5. whether full-vs-limited access creates a genuine `ΔT_acc` rather than a presentation difference;
6. whether subsequent portal-use/state transitions form an ordered trajectory;
7. whether omitted functions cannot alter the declared C09 estimand/conclusion;
8. provenance sufficient for independent reconstruction.

**Execution remains unauthorized.**
