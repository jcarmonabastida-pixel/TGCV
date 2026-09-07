# TGCV — Rust Reach Non-Redundancy Structural Audit v0.1

**Date:** 2026-09-07  
**Dataset:** `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`  
**Mode:** OUTCOME-BLIND / STRUCTURAL ONLY / DEPTH-1 CONFIGURATION SUCCESSORS

## Execution status

- `TACC_COMPUTED`: True
- `DELTA_TACC_COMPUTED`: True
- `REACH_COMPUTED`: True
- `TRAJECTORY_COMPUTED`: False
- `OUTCOME_COMPUTED`: False
- `MODEL_FITTED`: False
- `VALUE_COMPUTED`: False
- `EXECUTION_USED`: False
- `FUTURE_ACTIVITY_USED`: False

## Dataset / temporal integrity

- `PACKAGE_COUNT`: 91437
- `VERSION_COUNT`: 607498
- `DEPENDENCY_ROWS_SCANNED`: 3618523
- `MALFORMED_ROWS`: 0
- `DUPLICATE_ROWS`: 0
- `PAIRED_FOCAL_VERSION_TRANSITIONS`: 516061
- `TERMINAL_FOCAL_VERSIONS`: 91437

## T_acc / Reach structure

- `TACC_T0_MEMBERSHIP_COUNT`: 26112590
- `TACC_T1_MEMBERSHIP_COUNT`: 27127368
- `TACC_ADD_MEMBERSHIP_COUNT`: 2490426
- `TACC_REM_MEMBERSHIP_COUNT`: 1475648
- `REACH1_T0_SUCCESSOR_CONFIGURATION_COUNT`: 26112590
- `REACH1_T1_SUCCESSOR_CONFIGURATION_COUNT`: 27127368
- `DELTA_TACC_ADDITIONS_WITH_REDUNDANT_SUCCESSOR`: 0
- `DELTA_TACC_ADDITIONS_WITH_NONREDUNDANT_SUCCESSOR`: 2490426
- `SAME_LOCAL_TACC_CARDINALITY_DIFFERENT_REACH_PAIRS`: 69890

## Firewall

- `CANDIDATE_IDENTITY_INCLUDES_DECLARATION`: False
- `SUCCESSOR_IDENTITY_EQUALS_TRANSFORMATION_IDENTITY`: False
- `EXECUTION_USED`: False
- `OUTCOME_USED`: False
- `VALUE_USED`: False
- `FUTURE_ACTIVITY_USED`: False
- `RSTAR_VERSION`: v0.2
- `TRAJECTORY_COMPUTED`: False

## Result

**DECISION STATUS:** PASS — REACH_NON_REDUNDANCY_RESULT_REVIEW

The audit provides structural evidence that, under the frozen Depth-1 successor-configuration representation, `Reach` contains information not reducible to mere local `T_acc` cardinality/membership. In particular, all 2,490,426 observed `Delta T_acc` additions had non-redundant successor configurations, while 69,890 pairs exhibited equal local `T_acc` cardinality but different `Reach`.

This result establishes **informational non-redundancy of the Reach representation relative to the tested T_acc representation**. It does **not** by itself establish that `Reach` must be promoted to a primitive of the TGCV Core; it remains a derived/analytical structure pending the broader core tests.

No execution, outcome, value, future-activity, or trajectory information was used.

## Provenance

- `RSTAR_VERSION`: v0.2
- `REPORT_CANONICAL_SHA256`: `276c0e7883b72804b5f094bbe12ce0f15b7e021c4791a77c8149c60293f8c418`
- `RUNTIME_AUDIT_OK`: True
- `NEXT_GATE`: downstream review after Reach non-redundancy; no outcome/value inference authorized by this audit.
