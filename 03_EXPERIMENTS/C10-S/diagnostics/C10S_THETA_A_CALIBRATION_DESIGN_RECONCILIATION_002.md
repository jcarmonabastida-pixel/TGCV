# C10-S — Direct theta_A calibration design reconciliation 002

**Date:** 2026-11-27  
**Status:** STATIC RECONCILIATION / DECISIONS PROPOSED / EXECUTION NOT AUTHORIZED  
**Branch:** `research/c10s-m1-engine12-source-only-20261127`  
**Scope:** Denominators, within-world replication assumptions, and MCSE governance  
**Authorization:** No code changes, tests, seed-bank generation, calibration, simulation, workflow dispatch, or scientific execution.

## 1. Purpose and historical basis

This addendum resolves the three design questions left open by `C10S_THETA_A_CALIBRATION_PROTOCOL_STATIC_DESIGN_REVIEW_001.md`. It reuses the existing direct theta_A calibration protocol, seed-bank derivation, nested M/R precision module, and their current contracts. It does not introduce a new Analyzer, Evaluator, estimand, DGP family, or experiment.

The historical static review remains the parent design record. This addendum is a reconciliation, not a replacement.

## 2. Denominator decision: retain strict all-R evaluability

**Decision: retain the existing fail-closed denominator rules as primary. Do not relax them in code.**

For each outer world M:

- Identification, abstention, availability, and abstention-cause rates retain all planned R as their denominator.
- Point bias, MAE, RMSE, and point-recovery remain NOT_EVALUABLE for that world if any planned R is not identified.
- Inferential interval coverage and width remain NOT_EVALUABLE for that world if any planned R lacks an inferential interval.

This avoids silently changing the estimand through complete-case deletion. A missing interval or an abstention is itself relevant evidence for the calibration objectives and must not disappear from the denominator.

Conditional diagnostics may be reported separately:
- coverage conditional on an emitted interval, with the exact emitted-interval denominator;
- point-error metrics conditional on identified outputs, with the exact identified denominator.

Every such diagnostic must be paired with all-R interval availability or identification/false-abstention rates, respectively. It cannot replace the strict primary metric or be described as unconditional coverage/recovery.

This decision preserves the existing metric registry and aggregation semantics.

## 3. Within-world R: what is established and what is not

The seed-bank implementation establishes the following source-level facts:

- The same world identity, roster, DGP identity, and world seed are fixed across R within each M.
- Each R has a distinct joint-policy randomization salt.
- Each R has a distinct S3 measurement seed.
- Assignment and S3 streams are domain-separated; the S3 seed is expanded deterministically to unit-specific monitor seeds.
- The calibration runner verifies that actual assignment and S3 provenance matches the planned R-specific material.

Therefore, R is a repeat of the **joint assignment-and-observation pipeline** conditional on a fixed outer world. It is not assignment-only replication.

However, unique, domain-separated deterministic seeds do not, by themselves, establish an inferential IID sampling contract. The current `ThetaACalibrationDesign` versions the outer-world sampling contract but has no corresponding first-class within-world sampling-contract field. The nested precision function accepts a separate within-world declaration, but the existence of that parameter does not itself supply its scientific basis.

**Decision for the first bounded calibration design:** do not claim inferential IID-within-R or use nested M/R projections as acceptance evidence yet. Keep the nested module's within-world mode `UNVERIFIED`; its variance components and projections remain descriptive. The existing per-R seed/provenance checks remain valid operational controls, not proof of an IID model.

A later versioned within-world contract may declare `DECLARED_IID_PSEUDORANDOM` only after it explicitly states:
1. the conditional target distribution of joint-policy assignments within a fixed world;
2. the S3 observation-randomness distribution and its relation to assignment randomness;
3. the domain-separated seed-stream construction and generator identity/version;
4. why R replicates are modeled as independent draws conditional on the fixed world;
5. the limits of that assumption (synthetic design only; no claim about real-world independence).

That declaration should reuse the existing randomization and S3 seed contracts and should not require new randomization machinery. Until then, distinct seeds must not be used as a shortcut to an IID claim.

## 4. MCSE governance: one observed criterion, nested projection as planning diagnostic

The current aggregator computes each metric's observed calibration summary across the M outer-world contributions. Under `DECLARED_IID_PSEUDORANDOM` outer-world sampling, it reports the across-M MCSE and compares it with the versioned target. Without that declaration, it suppresses inferential MCSE.

The nested M/R module reconstructs the same observed outer-world summary and checks reconciliation against the aggregator. For non-RMSE metrics, its observed MCSE is explicitly the same across-M quantity. For RMSE, it carries forward the aggregator's delta-method MCSE. Its additional contribution is variance decomposition and bootstrap projection to candidate M/R designs.

**Decision:**
- The aggregator's observed across-M MCSE is the sole primary observed-precision acceptance criterion for the current design.
- The nested module is not a second, independent observed-MCSE test and must not create a duplicate PASS/FAIL.
- Nested variance components and candidate M/R projections are planning diagnostics only while within-world IID remains UNVERIFIED.
- If a valid within-world contract is later approved, nested projections may inform candidate M/R selection, but the aggregator's observed MCSE remains the criterion used to assess the realized calibration design.
- All MCSE conclusions remain conditional on the declared outer-world sampling model. `PASS_PRECISION` does not certify coverage, identification, causal attribution, or external validity.

## 5. Primary metric set for the four objectives

Retain the exhaustive registry for auditability, but use the following as the primary decision set, reported by scenario and N:

| Objective | Primary metrics |
|---|---|
| Causal point recovery | point_bias, point_mae, point_rmse; point_recovery_rate only if its tolerance is explicitly approved |
| Inferential calibration | interval_coverage, interval_availability_rate, interval_width |
| Monte Carlo precision | aggregator MCSE for each predeclared primary metric with a versioned target |
| Identification and abstention | identification_rate, false_abstention_rate, correct_abstention_rate, wrong_cause_abstention_rate, false_identification_rate |

Partial-identification rate and evaluator audit metrics remain supporting diagnostics/integrity checks. Do not expand the scenario roster. The positive, null, negative, alternative-pathway-zero, and target-support-failure cases remain distinct.

No numerical confidence level, point-recovery tolerance, MCSE target, coverage band, availability floor, width limit, or stopping threshold is selected here. Those remain explicit pre-calibration design inputs.

## 6. Consequence for the next operation

The three design questions are reconciled as follows:

1. **Denominators:** strict all-R evaluability remains primary; conditional diagnostics are supplementary and paired with availability/identification.
2. **Within-R sampling:** the current seed plan proves fixed-world and stream-provenance structure, not IID by itself. Keep inferential within-R projections descriptive until a versioned conditional sampling contract is justified.
3. **MCSE:** the aggregator governs observed precision; nested M/R is a planning diagnostic, not a second acceptance gate.

The next useful operation is to draft the small development-calibration design and run budget using these constraints, without generating seeds or executing anything. Before calibration, the numerical acceptance targets and stopping rule must be frozen, and the evaluation bank must remain disjoint and unopened.

## 7. Execution boundary

Static design reconciliation only. No tests, seed generation, calibration, simulation, benchmark, holdout, workflow dispatch, or scientific execution were performed or authorized.

`scientific_execution=false`  
`execution_authorized=false`
