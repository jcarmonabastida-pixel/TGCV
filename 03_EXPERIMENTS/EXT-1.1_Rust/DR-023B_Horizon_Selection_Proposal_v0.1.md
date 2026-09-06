# EXT-1.1 Rust — DR-023B Ex-Ante Horizon Selection Proposal v0.1

**Status:** PROPOSED — AWAITING GOVERNANCE ACCEPTANCE
**Prerequisites:** DR-023 structural PASS; DR-023A design analysis; horizon-feasibility audit PASS

## 1. Evidence available before confirmatory analysis

The frozen Rust snapshot contains 607,498 package-version observations with complete `created_at` timestamps. The observed release timestamp span is 2,857.061 days.

For the pre-declared design grid:

| Horizon | Complete-follow-up origins | Coverage |
|---:|---:|---:|
| 30 days | 589,846 | 97.0943% |
| 90 days | 555,636 | 91.4630% |
| 180 days | 507,279 | 83.5030% |
| 365 days | 416,112 | 68.4960% |

All four horizons are structurally feasible. No outcome label, outcome prevalence, `T_acc`, association, effect size, significance test, or sampling result was computed.

## 2. Primary horizon proposal

**Proposed primary horizon: H = 180 elapsed days.**

The proposal is based exclusively on pre-confirmatory design criteria:

1. **Local-trajectory requirement.** The outcome is intended to represent a subsequent package trajectory after an origin release, not merely an immediate next-event window and not an effectively annual lifecycle measure.
2. **Temporal exposure requirement.** 180 days provides a substantially longer observation window than 30 or 90 days while remaining substantially shorter than one year.
3. **Coverage requirement.** 180 days retains complete follow-up for 83.5030% of all package-version observations. The 365-day candidate falls below the pre-specified 80% coverage floor and is therefore rejected for the primary horizon.
4. **Non-optimization requirement.** The choice is not based on any outcome, predictor, association, effect size, or significance result.
5. **Single-horizon requirement.** 30, 90 and 365 days are not searched as alternative confirmatory models. They are design-grid candidates evaluated only against the frozen structural criteria.

## 3. Coverage floor

For this design stage, **80% complete-follow-up coverage** is adopted as the minimum structural-coverage criterion for a primary horizon candidate.

This criterion is applied to observation opportunity only. It is not an outcome inclusion criterion and does not inspect whether a package subsequently released.

Under the observed snapshot:

- 30 days: PASS;
- 90 days: PASS;
- 180 days: PASS;
- 365 days: FAIL primary-coverage criterion.

Among candidates satisfying the floor, 180 days is the longest pre-declared horizon and therefore the proposal preserves the longest local trajectory without requiring excessive right-censoring.

## 4. Outcome and censoring definition linked to H

If accepted, the primary outcome will be:

`Y_180(v_o) = 1` iff at least one later release of the same package occurs strictly after `created_at(v_o)` and no later than `created_at(v_o) + 180 days`.

`Y_180(v_o) = 0` iff no such later release is observed, **and only when complete 180-day follow-up is available**.

Origins without complete 180-day follow-up are excluded from the primary outcome analysis and are not coded as zero.

## 5. Governance state

This document does **not** accept DR-023. It records a concrete ex-ante proposal so that the governance decision can be explicit and auditable.

Acceptance should occur only after review that:

- the 80% structural-coverage floor is methodologically acceptable;
- H=180 days is accepted as the single primary horizon;
- the linked outcome/censoring definition is accepted;
- no alternative horizon will replace H=180 after confirmatory results are observed.

After acceptance, the horizon becomes frozen and cannot be changed based on experimental results. Any additional horizons, if scientifically useful, must be declared secondary/exploratory before confirmatory execution.

## 6. External methodological context

Empirical research on package ecosystems shows that package releases and dependency-network evolution occur on materially different time scales and that update frequency varies across packages and ecosystems. This supports treating the horizon as an explicit design parameter rather than assuming a universal release cadence. The present proposal therefore does not derive H from observed release frequency or from the outcome itself.

## 7. Explicit non-claims

This proposal does not claim that 180 days is universally optimal for software ecosystems. It claims only that, under the frozen EXT-1.1 design criteria, it is a defensible primary horizon candidate: long enough to represent a medium-term local trajectory, short enough to avoid an annual interpretation, and supported by >80% complete observation coverage in the frozen snapshot.
