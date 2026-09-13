# D-OPS-28 — C09 D27-A Admissibility Preflight 001

**Status:** `CLOSED — CANDIDATE REJECTED / TRANSFORMATION-IDENTITY GATE FAIL`
**Date:** 2026-09-13
**Candidate:** randomized live-streaming access experiment, University of Geneva

## 1. Decision

D27-A is **not admissible as a TGCV C09 causal candidate** under the current operationalization.

The experiment has a strong randomized access intervention, but the intervention changes the **presentation/access channel** for an educational activity whose underlying transformation can remain the same. The evidence therefore does not establish that:

`Z → T_acc,1 ≠ T_acc,0`

at the required TGCV transformation-identity level.

## 2. Evidence reconstruction

The published experiment randomized access to a live-streaming platform across students and weeks. Students with access could watch lectures online, while physical attendance remained possible. Access was randomized both across students and over weeks; the same student could therefore have streaming access in some weeks and not others. The paper reports 1,459 students across the experimental semesters and combines administrative, streaming-server, exam and attendance-proxy data. citeturn0search0

The experimental contrast is consequently well identified as a conventional causal intervention on **availability of live streaming**. citeturn0search0

## 3. TGCV gates

### A1 — Stable decision unit
**PASS.** Student-course-week can be reconstructed at the experimental-design level.

### A2 — Finite bounded transformation universe
**PASS at descriptive action level, insufficient at TGCV level.** One can construct a small observed attendance-mode vocabulary, but this does not by itself establish that attendance modes are distinct TGCV transformations.

### A3 — Ex-ante accessibility rule
**PASS for platform access.** Assignment to streaming access is determined before weekly attendance behaviour and is randomized across students/weeks. citeturn0search0

### A4 — Transformation identity / `Z → ΔT_acc`
**FAIL — CRITICAL.** The experiment establishes that `Z` changes whether the streaming channel is available. It does not establish that `Z` changes the underlying transformation domain in the TGCV sense. A student may accomplish the same educational transformation through an alternative presentation mode. Treating `online attendance` as a distinct transformation would therefore be an analyst-imposed ontology unless a domain-specific transformation identity rule is independently fixed.

This is the decisive failure.

### A5 — Counterfactual integrity
**PASS.** Randomized assignment supports conventional counterfactual identification.

### A6 — Independent longitudinal outcome
**PASS/PROMISING.** Exam outcomes and attendance measures are observed independently of the TGCV accessibility adjudication. The paper also maps exam questions to weeks of instruction, providing temporal linkage. citeturn0search0

### A7 — No direct target-trajectory encoding
**PASS.** Treatment assignment does not prescribe the subsequent academic outcome.

### A8 — Provenance/reconstruction
**PARTIAL.** The published study provides substantial experimental and data-design information, but a complete independent TGCV reconstruction would still require the exact frozen transformation ontology and accessible raw/derived records.

## 4. Why this is not merely a data problem

The rejection is methodological rather than logistical.

The study has unusually strong causal identification for the conventional question. The problem is that the causal treatment is an **access-to-channel intervention**, whereas C09 requires a causal intervention on the **accessible transformation space itself**.

If TGCV simply declares every interface or delivery modality to be a distinct transformation, the operationalization becomes too permissive and risks converting ordinary treatment effects into apparent `ΔT_acc`. That would undermine the distinction established in the C09 non-redundancy audit.

## 5. Consequence for C09

D27-A does not close the causal gap.

`C09 = H — NO CAUSAL IDENTIFICATION`

No C09 claim upgrade is permitted.

No execution is authorized.

No new dataset acquisition is authorized on the basis of D27-A.

No RUST or SWIM rerun is warranted.

## 6. Scientific implication

The preflight identifies a sharper requirement for future causal discovery:

> The intervention must alter a transformation's **permission/capability/resource feasibility boundary**, not merely alter the interface, delivery channel, information available about the same transformation, or incentive to choose it.

Promising future candidates therefore need interventions such as:

- granting/revoking a formally defined capability;
- changing eligibility to perform a bounded operation;
- enabling/disabling a resource required for a distinct operation;
- changing an explicit permission or rule that determines whether an operation is executable;
- randomizing access to a genuinely distinct action with a separately identifiable post-intervention state.

## 7. Next operation

D-OPS-29 should perform **targeted discovery of capability/permission interventions**, excluding:

- incentive-only treatments;
- information treatments;
- interface/channel treatments;
- generic technology-access treatments;
- observational trajectory studies;
- repetitions of FOS/SWIM/RUST.

The next candidate should be admitted only if the intervention can be expressed independently as:

`Z → capability/permission/resource state → T_acc,1 ≠ T_acc,0 → subsequent trajectory Y`

with a finite or bounded-complete `U_tau` and ex-ante `P_tau`.
