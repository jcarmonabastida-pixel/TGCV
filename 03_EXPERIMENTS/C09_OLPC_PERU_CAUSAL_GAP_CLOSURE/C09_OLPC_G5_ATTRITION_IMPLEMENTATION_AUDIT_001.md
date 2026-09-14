# C09 OLPC Peru — G5 Attrition Implementation Audit 001

Status: **CLOSED — G5 IMPLEMENTATION READY FOR INTEGRATION/PREFLIGHT**

## Purpose

Audit the G5 attrition component required by the C09 causal-gap closure execution, without modifying the frozen scientific specification and without treating attrition correction as proof of mediation.

## G5 universe

The observation analysis is restricted before model fitting to:

`participated_in_lottery == 1 AND treatment_school == 1`

with assignment:

`Z = won_lottery`

`received_laptop` remains implementation/compliance information and is not used to define the assignment arm.

## Observation definition

`observed_r2 = 1` iff the student's `codest` is present in the Round 2 `cestudiante_g3-6_p2_r2.dta` respondent file; otherwise `observed_r2 = 0`.

This separates the observation/attrition process from the downstream outcomes reconstructed from Round 2.

## Pre-treatment covariates X0

Only Round 1 variables are admitted to the observation model:

- P2: computer/laptop at home
- P3: Internet at home
- P4: prior computer use
- P12_A1–P12_A8: declared baseline computer capabilities

All are converted to binary Yes/No indicators using the documented `1=Yes, 2=No` coding; special nonresponse codes are treated as missing.

No Round 2 trajectory, capability, Raven, receipt, or other post-treatment variable enters the observation model.

## Estimation design

The implementation:

1. computes observed-vs-not-observed balance separately for Z=0 and Z=1;
2. reports standardized differences for each X0 variable;
3. fits separate logistic observation models within Z=0 and Z=1;
4. uses median imputation of X0 only for the observation-model design matrix, retaining the observed/not-observed indicator as the dependent variable;
5. clips predicted observation probabilities at 0.5 solely to prevent explosive inverse-probability weights;
6. computes IPW weights as `1/P_obs`;
7. reports P_obs range, maximum weight and P99 weight;
8. reports effective sample size by assignment arm;
9. compares complete-case and IPW contrasts for the prespecified downstream trajectory variables.

## Scientific boundary

G5 is an attrition robustness/sensitivity analysis under an X0-only MAR working model. It does **not** establish:

- absence of unmeasured attrition bias;
- mediation by ΔT_acc;
- exclusion of direct treatment pathways;
- causal identification of the full TGCV chain.

Those questions remain separate G6 causal-bridge questions.

## Versioning rule

G5 outputs are versioned independently and are intended to be integrated into C09 executor v0.6 outputs 002. No v0.5 artifact is overwritten and no Evidence-to-Claim Matrix, RMA, STATUS, or Core update is authorized by this audit.

## Verdict

**PASS — G5 implementation is operationally specified and ready for v0.6 preflight/integration.**

The next gate is a combined v0.6 preflight verifying G1–G5, followed only then by controlled execution.
