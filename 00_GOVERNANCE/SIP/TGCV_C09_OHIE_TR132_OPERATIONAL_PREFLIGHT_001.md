# TGCV — C09 OHIE TR-132 Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Oregon Health Insurance Experiment (OHIE)
**Parent:** `TGCV_C09_RETROSPECTIVE_TR132_CANDIDATE_REVIEW_001.md`
**Execution authorization:** `NONE`

## 1. Candidate definition

OHIE randomly selected uninsured low-income adults in Oregon in 2008 for the opportunity to apply for Medicaid. Lottery selection increased insurance coverage by about 25 percentage points in the first year and generated randomized contrasts in health-care use, financial strain and health outcomes. citeturn0search1turn0search6

NBER currently provides public-use OHIE data and replication code for several major study papers. citeturn0search0turn0search14

## 2. Proposed bounded C09 representation

`U* = medically necessary health-care access transformations available to an eligible lottery participant during the frozen post-lottery observation window.`

Intervention: randomized lottery selection / opportunity to apply for Medicaid.

Accessibility representation must distinguish the relevant insurance-mediated access conditions rather than equating lottery assignment, enrollment or realized utilization with `T_acc`.

## 3. Operational gates

### P1 — Randomized intervention

**PASS.**

Lottery selection provides the randomized treatment/control contrast. citeturn0search1turn0search6

### P2 — Decision-time unit and baseline state

**PASS — DESIGN LEVEL.**

The study was built around low-income uninsured adults before lottery selection, with prespecified analyses and survey instruments publicly archived. citeturn0search6turn0search14

### P3 — Accessibility intervention

**CONDITIONAL PASS.**

Medicaid eligibility/coverage plausibly changes the admissibility of health-care transformations by changing insurance-mediated financial access. The randomized design is therefore relevant to C09. However, TGCV requires an explicit bounded transformation universe and accessibility predicates, not simply an insurance-status indicator.

### P4 — Unit-level `T_acc,0/T_acc,1`

**FAIL — CURRENT PUBLIC OPERATIONALIZATION.**

Although OHIE public-use data are available, the public release is not established as containing a reconstructible unit-level health-care transformation universe together with ex-ante accessibility predicates under Medicaid versus control for each randomized participant. The study's scientific evidence also draws on rich administrative data, including hospital and emergency-department records. citeturn0search0turn0search6

A treatment indicator, Medicaid coverage, health-care utilization, or observed claims cannot be substituted for `T_acc` without changing the TGCV construct.

### P5 — Independent trajectory endpoint

**PASS — SCIENTIFICALLY / CONDITIONAL OPERATIONALLY.**

OHIE has independently measured downstream health, financial and utilization outcomes; the first-year study explicitly evaluates health-care use, out-of-pocket expenditure/medical debt and self-reported physical and mental health. citeturn0search1

The remaining issue is whether one such endpoint can be reconstructed together with the required unit-level accessibility contrast using only the admissible public package.

### P6 — Public reproducibility

**CONDITIONAL / INSUFFICIENT FOR C09 EXECUTION.**

Public-use data and replication code are genuinely available, which is stronger than several previous candidates. citeturn0search0turn0search14

However, public availability of study data does not by itself establish the specific TGCV operational variables `T_acc,0` and `T_acc,1`. The available public documentation does not establish that a unit-level bounded transformation-space representation satisfying TR-132 can be reconstructed without importing additional restricted administrative data.

### P7 — TR-132 omitted-path sufficiency

**NOT ADMITTED.**

The causal lottery is strong, but the accessibility representation remains under-specified at unit level. Without a demonstrable `T_acc,0/T_acc,1` contrast, omitted-path sufficiency cannot be certified. The existence of a public-use dataset therefore does not override the TR-132 gate.

## 4. Decision

**OHIE = PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED.**

OHIE is a stronger data-access candidate than several previously rejected cases because public-use data and replication code are explicitly provided. citeturn0search0turn0search14

Nevertheless, the present public package is not sufficient to demonstrate the required unit-level bounded accessibility representation. The candidate therefore does not enter C09 causal execution.

No inference from lottery selection to `T_acc`.
No substitution of Medicaid coverage or utilization for accessibility.
No restricted-data request.
No causal execution.
No matrix upgrade.
No Core change.
No execution authorization.

## 5. Candidate disposition

Retain OHIE as a **strong methodological reference / conditional C09 candidate**. A future reopening is justified only if an admissible public-use or otherwise governed dataset package can explicitly reconstruct the bounded `T_acc,0/T_acc,1` representation required by TR-132.

**Next operation:** evaluate **Charlotte-Mecklenburg School-Choice Lottery** under the controlled TR-132 operational-preflight gate.
