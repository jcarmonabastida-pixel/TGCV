# C10-S V_cont — scenario–estimand coverage matrix

**Status:** DRAFT — persisted with Gate 143–144 source alignment; static review pending.  
**Branch:** research/c10-s-consolidation-draft  
**Scope:** 13 benchmark scenarios × 4 assignment estimands = 52 coverage records.  
**Scenario version:** VCONT-SYNTH-001.  
**Estimand version:** 001 (proposed stable IDs).

This is a coverage contract, not an executed benchmark result. DEFINED describes DGP potential-outcome truth; it does not imply identification from observed evidence. Numeric tolerances remain open. theta_A is outside this assignment-contrast benchmark.

| scenario_id | estimand_id | evaluation_class | truth_status | DGP truth field | Analyzer output | identification expectation | abstention | tolerance_id | reason |
|---|---|---|---|---|---|---|---|---|---|
| R0_FOCAL_POSITIVE | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R0_FOCAL_POSITIVE | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R0_FOCAL_POSITIVE | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R0_FOCAL_POSITIVE | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R0_FOCAL_NULL | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R0_FOCAL_NULL | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R0_FOCAL_NULL | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R0_FOCAL_NULL | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R0_FOCAL_ADVERSE | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R0_FOCAL_ADVERSE | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R0_FOCAL_ADVERSE | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R0_FOCAL_ADVERSE | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R0_DIRECT_G | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R0_DIRECT_G | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R0_DIRECT_G | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R0_DIRECT_G | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R0_DIRECT_Z | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R0_DIRECT_Z | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R0_DIRECT_Z | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R0_DIRECT_Z | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R1_ALTERNATIVE_BASELINE | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R1_ALTERNATIVE_BASELINE | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R1_ALTERNATIVE_BASELINE | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R1_ALTERNATIVE_BASELINE | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R2_ALTERNATIVE_AFFECTED | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R2_ALTERNATIVE_AFFECTED | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R2_ALTERNATIVE_AFFECTED | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R2_ALTERNATIVE_AFFECTED | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R3_PROVISION_FAILURE | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R3_PROVISION_FAILURE | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R3_PROVISION_FAILURE | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R3_PROVISION_FAILURE | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R0_MEASUREMENT_ADVERSE | ITT_Z_RUN_CONDITIONAL_VCONT | STATUS_ONLY | DEFINED | itt_z_run_truth | — | INDETERMINATE | true | N/A | MEASUREMENT_NOT_IDENTIFIED |
| R0_MEASUREMENT_ADVERSE | ITT_Z_MECHANISM_MARGINAL_VCONT | STATUS_ONLY | DEFINED | itt_z_mechanism_truth | — | INDETERMINATE | true | N/A | MEASUREMENT_NOT_IDENTIFIED |
| R0_MEASUREMENT_ADVERSE | ITT_Z_REFERENCE_REGIME_VCONT | STATUS_ONLY | DEFINED | itt_z_reference_truth | — | INDETERMINATE | true | N/A | MEASUREMENT_NOT_IDENTIFIED |
| R0_MEASUREMENT_ADVERSE | ITT_G_Z0_VCONT | STATUS_ONLY | DEFINED | itt_g_z0_truth | — | INDETERMINATE | true | N/A | MEASUREMENT_NOT_IDENTIFIED |
| R0_INTERFERENCE | ITT_Z_RUN_CONDITIONAL_VCONT | STATUS_ONLY | DEFINED | itt_z_run_truth | — | INDETERMINATE | true | N/A | UNIT_INTERFERENCE |
| R0_INTERFERENCE | ITT_Z_MECHANISM_MARGINAL_VCONT | STATUS_ONLY | DEFINED | itt_z_mechanism_truth | — | INDETERMINATE | true | N/A | UNIT_INTERFERENCE |
| R0_INTERFERENCE | ITT_Z_REFERENCE_REGIME_VCONT | STATUS_ONLY | DEFINED | itt_z_reference_truth | — | INDETERMINATE | true | N/A | UNIT_INTERFERENCE |
| R0_INTERFERENCE | ITT_G_Z0_VCONT | STATUS_ONLY | DEFINED | itt_g_z0_truth | — | INDETERMINATE | true | N/A | UNIT_INTERFERENCE |
| R0_SUPPORT_FAILURE | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R0_SUPPORT_FAILURE | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R0_SUPPORT_FAILURE | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_TRANSPORTABILITY_R0 |
| R0_SUPPORT_FAILURE | ITT_G_Z0_VCONT | NOT_IDENTIFIABLE | DEFINED | itt_g_z0_truth | — | NOT_IDENTIFIED | true | N/A | G_NO_COMMON_SUPPORT |
| R0_HETEROGENEITY | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R0_HETEROGENEITY | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R0_HETEROGENEITY | ITT_Z_REFERENCE_REGIME_VCONT | EVALUABLE | DEFINED | itt_z_reference_truth | reference_regime_itt | IDENTIFIED | false | OPEN_UNASSIGNED | REFERENCE_COMMON_SUPPORT |
| R0_HETEROGENEITY | ITT_G_Z0_VCONT | EVALUABLE | DEFINED | itt_g_z0_truth | g_assignment_effect | IDENTIFIED | false | OPEN_UNASSIGNED | G_COMMON_SUPPORT |
| R2_SUPPORT_FAILURE_ZG_INTERACTION | ITT_Z_RUN_CONDITIONAL_VCONT | EVALUABLE | DEFINED | itt_z_run_truth | package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_REALIZED |
| R2_SUPPORT_FAILURE_ZG_INTERACTION | ITT_Z_MECHANISM_MARGINAL_VCONT | EVALUABLE | DEFINED | itt_z_mechanism_truth | mean_package_itt | IDENTIFIED | false | OPEN_UNASSIGNED | Z_RANDOMIZED_G_MECHANISM |
| R2_SUPPORT_FAILURE_ZG_INTERACTION | ITT_Z_REFERENCE_REGIME_VCONT | NOT_IDENTIFIABLE | DEFINED | itt_z_reference_truth | — | NOT_IDENTIFIED | true | N/A | REFERENCE_NO_TRANSPORTABILITY |
| R2_SUPPORT_FAILURE_ZG_INTERACTION | ITT_G_Z0_VCONT | NOT_IDENTIFIABLE | DEFINED | itt_g_z0_truth | — | NOT_IDENTIFIED | true | N/A | G_NO_COMMON_SUPPORT |

## Interpretation

- Run-conditional ITT-Z is evaluated per assignment replicate against the realized G-vector truth.
- Mechanism-marginal ITT-Z is the repeated-assignment mean under the actual G assignment mechanism.
- Reference-regime ITT-Z is separately evaluated across repeated assignments against itt_z_reference_truth; its numeric output is absent when reference identification fails.
- ITT-G under Z=0 requires common support; lack of support is NOT_IDENTIFIABLE, not a zero effect.
- Measurement adversity and unit interference are STATUS_ONLY for current unit-level estimands because the Analyzer abstains.
- R0 support failure permits reference evaluation only under the declared, scope-matched DGP invariance restriction; ITT-G remains NOT_IDENTIFIABLE.
- R2 support failure with Z×G interaction blocks reference transportability and ITT-G common support.
- Null truth is never interpreted as zero; truth comes only from TruthBundle.
- STATUS_ONLY and NOT_IDENTIFIABLE remain in coverage/identification reporting but do not enter numeric MCSE/recovery selection.

Versioned key: (scenario_id, scenario_version, estimand_id, estimand_version).
