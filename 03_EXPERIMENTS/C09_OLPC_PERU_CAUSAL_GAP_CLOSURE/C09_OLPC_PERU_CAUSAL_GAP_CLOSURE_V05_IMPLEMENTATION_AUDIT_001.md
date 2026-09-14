# C09 OLPC Peru — v0.5 Implementation Audit 001

## Status
**OPEN — CORRECTION REQUIRED BEFORE C09 SCIENTIFIC CLOSURE**

## Purpose
Audit the executed C09 OLPC Peru causal-gap closure executor v0.5 against the frozen C09 specification and the pre-execution design record, without changing the frozen scientific acceptance criteria.

This audit does **not** close C09 and does **not** authorize creation of the C09 Evidence Record yet.

## Canonical inputs audited
- Frozen specification: `00_GOVERNANCE/SIP/TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001.md`
- Executor: `03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/run_c09_olpc_peru_gap_closure_v01.py`
- v0.5 execution result: `03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_RESULT_001.json`
- Pre-execution design context: the recovered OLPC causal-universe/attrition analysis from the preceding work session.

## Finding F1 — causal analysis universe is under-specified in v0.5

### Observed implementation
The v0.5 executor merges the student-level assignment table with R1/R2 observations and defines:

`Z = won_lottery`

It then computes every `Z` contrast over the full paired R1/R2 dataset. The implementation does **not** first restrict the causal comparison to students who participated in the individual lottery and who belonged to the treatment-school condition.

The relevant implementation sequence is:

1. merge `r1raw` with `listas_final.dta` assignment fields;
2. merge R2 accessibility, trajectory, capability and Raven variables;
3. set `d["Z"] = d["won_lottery"]`;
4. call `mean_diff(...)` directly on `d`.

There is no causal-universe filter between steps 3 and 4.

### Consequence
The v0.5 `Z=0` arm contains control-school observations that were not necessarily members of the individual lottery. The recorded v0.5 identity table demonstrates this directly:

- `Z=0, treatment_school=0`: 1,338 observations
- `Z=0, treatment_school=1`: 3,550 observations
- `Z=1, treatment_school=0`: 0 observations
- `Z=1, treatment_school=1`: 636 observations

Therefore the v0.5 `won_lottery=1` versus `won_lottery=0` contrasts are not yet a clean individual-lottery causal comparison.

### Required correction
Before any `Z` contrast is calculated, construct and explicitly record the individual-lottery causal universe:

`causal_universe = participated_in_lottery == 1 AND treatment_school == 1`

and, within that universe:

`Z = won_lottery`

The implementation must retain the original assignment variables and report exclusions/counts, rather than silently filtering.

### Scientific classification
**Material implementation defect.** This is not a change to the frozen scientific criterion. The frozen specification already requires assignment/linkage integrity, valid counterfactual identification, sample/exclusion accounting and assessment of alternative pathways. The correction restores those requirements at execution level.

## Finding F2 — assignment identity must be recomputed after the universe correction

The v0.5 receipt and school-condition cross-tabs are useful diagnostics but are not sufficient for causal-arm validation because the analysis universe is contaminated.

v0.6 must report at minimum:

- total `listas_final` N;
- `participated_in_lottery` counts;
- treatment-school counts within the lottery universe;
- `won_lottery` counts within the causal universe;
- receipt counts by Z within the causal universe;
- treatment-school counts after filtering;
- explicit count of excluded control-school observations;
- school-pair structural validity as a separate diagnostic.

The causal contrast must have no `treatment_school=0` observations in either Z arm.

## Finding F3 — bounded accessibility operationalisation remains unchanged

No change is authorized to the frozen operationalisation:

- `T_acc,0`: R1 P2/P3/P4/P12_A1–A8;
- `T_acc,1`: R2 P1/P2/P3;
- R2 P4–P7 remain trajectory/use observations;
- capabilities and Raven remain downstream outcomes/validation variables.

The v0.6 correction is therefore an **analysis-universe correction**, not an operationalisation change.

## Finding F4 — trajectory and capability reconstruction remains unchanged

The existing v0.5 mappings are retained:

- P4 duration → trajectory/use;
- P5 weekly use by place → trajectory/use;
- P6 use by activity → trajectory/use;
- P7 Internet use → trajectory/use;
- P91–P97 objective skills → capability/result;
- P10_A1–A11 self-reported skills → capability/result;
- Raven reconstructed from `matrices_g3-6_r2.dta` using the published 36-item key.

No redefinition of these variables is required for the universe correction.

## Finding F5 — attrition analysis must be rerun on the corrected causal universe

The prior design identified differential R2 observation between arms and rejected an unconditional MCAR assumption. That work is relevant to C09 but its numerical results must not be carried forward as final estimates because they were not established on the corrected individual-lottery universe.

v0.6 must therefore recompute, within the corrected causal universe and using pre-treatment X0 only:

1. observed versus not-observed R2 balance within each Z arm;
2. standardized differences for the pre-treatment covariates;
3. an observation model;
4. observation probabilities and inverse-probability weights;
5. effective sample size by arm;
6. brute complete-case estimate versus IPW estimate on the same corrected estimand/sample definition.

The previous numerical values are historical design context, not canonical C09 results.

## Finding F6 — causal bridge remains a separate gate

Even after correcting the causal universe, the following distinction remains mandatory:

`Z → ΔT_acc`

is not by itself equivalent to:

`ΔT_acc → subsequent trajectory`

with `ΔT_acc` established as the causal mediator.

v0.6 must therefore retain separate reporting of:

- assignment → accessibility change;
- assignment → downstream trajectory;
- evidence relevant to the bridge from accessibility change to subsequent trajectory;
- direct-treatment and alternative-pathway cautions.

The correction must not manufacture a mediation claim from treatment contrasts alone.

## v0.6 required execution gates

### G1 — Universe
`participated_in_lottery == 1 AND treatment_school == 1` is explicitly constructed and its counts are reported.

### G2 — Assignment
`Z = won_lottery` is evaluated only inside G1. No control-school observation may enter either causal arm.

### G3 — Accessibility
Recompute the frozen R1→R2 bounded accessibility transition without changing variable definitions.

### G4 — Trajectory
Recompute the frozen R2 P4–P7 trajectory variables.

### G5 — Attrition
Redo the X0-only observation/weighting analysis on the corrected causal universe.

### G6 — Causal bridge
Report the evidence for `Z → ΔT_acc` and downstream trajectory separately, and assess whether a defensible causal bridge is identified.

## Required v0.6 outputs

The corrected executor should produce a new versioned result, audit data and execution log. It must not overwrite the v0.5 outputs.

Recommended versioning:

- executor: v0.6;
- result: `...RESULT_002.json`;
- audit data: `...AUDIT_DATA_002.csv`;
- log: `...EXECUTION_LOG_002.txt`.

The v0.5 output remains immutable historical evidence of the defective execution and must not be relabeled as the corrected result.

## Governance constraints

- Do **not** modify `TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001.md`.
- Do **not** update RMA, Evidence Matrix, STATUS or TGCV Core from v0.5.
- Do **not** create the C09 Evidence Record until the corrected execution has passed its preflight and the resulting scientific verdict is independently assessed.
- Do **not** reuse the previous attrition point estimates as final C09 evidence.

## Audit verdict

**v0.5: NOT SCIENTIFICALLY CLOSABLE.**

Reason: the implementation computes the individual-lottery contrast over a universe that includes 1,338 control-school observations outside the intended lottery universe. This invalidates the current `Z` contrast as the final causal comparison.

**Next action: implement and preflight v0.6 with the corrected causal universe, then rerun the controlled C09 execution.**
