# C10-S — Tier-A coverage ledger 001

**Status:** HISTORICAL RECONCILIATION — NO NEW SIMULATION / NO METHOD CHANGE  
**Date:** 2026-11-27  
**Branch:** `research/c10s-coverage-first-focus-20261127`  
**Purpose:** establish one compact, source-traceable view of the actual Tier-A coverage and interval-emission deficits. This ledger is a routing aid; historical adjudications remain immutable.

## 1. Frozen acceptance rules

For each cell × target component, independently:
- conditional coverage [93%,97%];
- two-sided 95% Wilson interval contains 95%;
- interval emission >=95%;
- complete accounting, finite ordered endpoints, correct raw-between values, no unresolved numerical state;
- no pooling/averaging across cells or components.

A component only passes when every applicable condition passes. Coverage without adequate interval emission is not accepted as calibrated conditional coverage.

## 2. Component status ledger

### 2.1 Original frozen v002 percentile bootstrap (C0; K=1,000/B=1,000 per cell)

| Family/cell | Within coverage | Raw-between coverage | MCSE availability | Coverage reading |
|---|---:|---:|---:|---|
| F1 balanced M10/R5 | 84.0% | 93.8% | 24.4% | Within under; between point inside band |
| F1 balanced M30/R20 | 94.9% | 90.7% | 100.0% | Within point inside; between under |
| F1 high-between M10/R5 | 84.3% | 80.1% | 91.6% | Both under |
| F1 high-between M30/R20 | 93.8% | 86.5% | 100.0% | Within point inside; between under |
| F1 low-between M10/R5 | 79.9% | 98.2% | 0.0% | Within under; between over |
| F1 low-between M30/R20 | 95.5% | 87.8% | 57.8% | Within point inside; between under |
| F5 beta22 M10/R5 | 94.2% | 98.7% | 1.7% | Within point inside; between over |
| F5 beta22 M30/R20 | 91.8% | 95.4% | 99.7% | Within under; between point inside |

Source: `C10S_F1_F5_INTEGRATED_SIMPLIFICATION_AUDIT_001.md` §3.1. The source summary reports within passed 4/8 and raw-between 2/8; only one cell met the original MCSE availability and coverage/Wilson conditions. Wilson endpoints are not reproduced in that summary; do not infer them from point coverage. C0 remains a frozen comparator, not a fallback.

### 2.2 F1 exact within pivot and conservative raw-between candidate

| Component | Independent comparative holdout result | Emission | Wilson criterion | Disposition |
|---|---:|---:|---|---|
| F1 within, six Gaussian cells | 94.9–95.5% | 100% | All six contain 95% | PASS within declared balanced Gaussian random-intercept family |
| F1 raw-between, six Gaussian cells | 96.7–99.4% | 100% | All six Wilson intervals above 95% | FAIL — conservative overcoverage |

Source: `C10S_F1_F5_INTEGRATED_SIMPLIFICATION_AUDIT_001.md` §§3.2, 4–5 and `C10S_TIER_A_POST_HOLDOUT_METHOD_DIAGNOSIS_001.md` §§3.1–3.2. Exact per-cell C1 coverages/Wilson endpoints are not transcribed in the summary sources reviewed for this ledger; preserve the aggregate range and all-six Wilson disposition only. Existing F1 profile-likelihood candidate is implemented and deterministic-tested, but its LR cutoff is uncalibrated.

### 2.3 F5 C5 comparative holdout

| Cell | Target | Coverage | Wilson 95% | Emission | Disposition |
|---|---|---:|---:|---:|---|
| M10/R5 | Within | 98.37% | Not reproduced in post-holdout summary | 98.4% | FAIL — overcoverage |
| M10/R5 | Raw-between | 98.88% | Not reproduced in post-holdout summary | 98.4% | FAIL — overcoverage |
| M30/R20 | Within | 93.5% | Not reproduced in post-holdout summary | 100% | FAIL — Wilson condition |
| M30/R20 | Raw-between | 92.7% | Not reproduced in post-holdout summary | 100% | FAIL — undercoverage |

Source: `C10S_TIER_A_POST_HOLDOUT_METHOD_DIAGNOSIS_001.md` §3.3. This was an 8,000-dataset exposed/unblinded comparative holdout; it is development evidence only and must not be reused for tuning as a fresh confirmatory holdout. The report notes 16 M10/R5 non-emissions (15 MLE non-convergences, one upper-bound concentration fit). The aggregate emission shown above is 98.4%.

### 2.4 F5 C5 B2/B3 development calibration and disjoint development validation

| Cell/bank | Target | Coverage | Wilson 95% | Emission | Disposition |
|---|---|---:|---:|---:|---|
| M10/R5 calibration | Within | 97.74% | [97.29%,98.12%] | 98.22% | FAIL |
| M10/R5 calibration | Raw-between | 98.33% | [97.93%,98.65%] | 98.22% | FAIL |
| M10/R5 validation | Within | 98.02% | [97.59%,98.38%] | 98.10% | FAIL |
| M10/R5 validation | Raw-between | 98.70% | [98.34%,98.98%] | 98.10% | FAIL |
| M30/R20 calibration | Within | 94.04% | [93.35%,94.66%] | 100% | FAIL |
| M30/R20 calibration | Raw-between | 93.08% | [92.34%,93.75%] | 100% | FAIL |
| M30/R20 validation | Within | 93.96% | [93.27%,94.59%] | 100% | FAIL |
| M30/R20 validation | Raw-between | 93.00% | [92.26%,93.67%] | 100% | FAIL |

Source: `C10S_F5_B2_B3_DEVELOPMENT_CALIBRATION_RESULT_AUDIT_001.md` §3. Each bank had K=5,000 per cell. C5 fails 0/8 complete component gates. B3 endpoint sensitivity B=1,000 versus 4,000 showed modest shifts on selected datasets; it did not repair the coverage pattern. All B2/B3 data are development-only and cannot be used as fresh confirmatory holdout.

### 2.5 F5 G7 Tier-A v1.1

| Cell | Target | Coverage | Wilson 95% | Emission | Disposition |
|---|---|---:|---:|---:|---|
| M10/R5 | Within | 98.644% | [97.645%,99.223%] | 88.5% | FAIL — coverage and emission |
| M10/R5 | Raw-between | 99.661% | [99.008%,99.885%] | 88.5% | FAIL — coverage and emission |
| M30/R20 | Within | 94.260% | [92.635%,95.543%] | 99.3% | PASS |
| M30/R20 | Raw-between | 93.353% | [91.631%,94.742%] | 99.3% | FAIL — Wilson interval does not contain 95% |

Source: `C10S_F1_F5_INTEGRATED_SIMPLIFICATION_AUDIT_001.md` §3.4 and G7 v1.1 adjudication. K=1,000 per cell. Overall 1/4 components passed. Primary/replay records matched exactly. G7 is NOT_VALIDATED and exposed; not a holdout for future tuning or confirmation.

### 2.6 F5 M1-PCT refitted-bootstrap pilot

| Cell | Datasets | Emitted | Emission | Descriptive within / raw-between | Disposition |
|---|---:|---:|---:|---:|---|
| M10/R5 | 50 | 2 | 4% | 100% / 100% (only 2 emitted) | FAIL emission; not calibrated |
| M30/R20 | 50 | 50 | 100% | 98% / 94% | Descriptive only; no formal coverage adjudication |

Source: `C10S_F5_M1_PCT_DEVELOPMENT_PILOT_RESULT_001.md`. M10/R5 had 846/4,500 non-admissible bootstrap refits among 45 original fits; strict fail-closed handling caused 43/45 bootstrap abstentions. This candidate is rejected under its current contract. Do not drop failed replicates or relax abstention.

## 3. What the ledger says — the actual deficits

1. **F1 within is solved within the declared Gaussian family.** Keep it unchanged.
2. **F1 raw-between overcovers under the conservative joint-pivot method.** Existing profile-likelihood candidate is the only next F1 method to inspect; no new solver.
3. **F5 M10/R5 has both overcoverage and insufficient emission.** G7's exact MLE certificate did not fix either. M1-PCT's current refit contract collapses emission to 4%; simply dropping failed refits is invalid.
4. **F5 M30/R20 raw-between is a distinct, marginal undercoverage/Wilson failure.** Preserve the within PASS; do not treat M10/R5's weak-identification issue as the same mechanism.
5. **The F5 coverage problem is not a simple increase-B problem.** Existing B3 sensitivity is modest and does not address uncertainty/approximation in the fitted concentration distribution.

## 4. Data-use and evidence limits

- All historical banks in this ledger are exposed/unblinded development evidence or previously adjudicated evidence. They are useful for diagnosis and candidate design only.
- No historical data may be relabelled as fresh confirmatory Tier-A.
- The ledger does not calculate missing Wilson intervals, infer missing per-cell results, or change any prior adjudication.
- F5 MCSE is excluded: it is not the within/raw-between coverage target.
- No new execution, calibration, code change or method selection was performed to create this ledger.

## 5. Next coverage-directed action

**F5 M10/R5 first:** perform a compact, data-grounded reconciliation of the observed high-concentration/near-binomial ridge, production-versus-analytic fit divergence, and the M1-PCT abstention classes. The decision output must identify one minimum candidate interval construction that directly addresses both coverage and emission, or state that no valid candidate is currently supported. Only then consider one bounded development-only comparison on fresh disjoint seeds.

Do not extend F5 M2 profile inversion, Sturm precision or global-certificate machinery by default. Any escalation must be justified by a named coverage/emission failure and a demonstrated inability of a simpler candidate to address it.
