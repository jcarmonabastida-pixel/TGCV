# C10-S — F5 pointwise LR development stress protocol 001

**Status:** PRE-EXECUTION DEVELOPMENT PROTOCOL — NOT CALIBRATION / NOT CONFIRMATORY  
**Branch:** `research/c10s-instrumental-autonomous-workpackage-20261126`  
**Purpose:** inspect the computational and numerical behaviour of the exact W/B profile-LR statistic on a small, fresh repeated-sampling sample from the frozen F5 beta22 DGP.

## 1. Scope and separation

This is a bounded development-only diagnostic of the already implemented exact constrained-profile maximum and LR-statistic enclosure. It is not:
- LR-cutoff selection or calibration;
- confidence-set inversion or topology certification;
- a coverage/emission adjudication;
- Tier-A, Tier-B, or causal C10-S execution;
- a change to any frozen acceptance threshold or historical result.

The known DGP values are used only to evaluate the pointwise LR statistic at the true functionals, as required for a later calibration study. They are not passed to the unrestricted global-MLE fit. No cutoff is applied and no IN/OUT decision is made.

## 2. Frozen DGP and targets

Use only the two existing Tier-A F5 beta22 fixture definitions:
- `F5_beta22_M10_R5`, (M=10,R=5,alpha=eta=2);
- `F5_beta22_M30_R20), (M=30,R=20,alpha=eta=2).

The exact population targets are (W=1/5) and (B=1/20). Generate complete independent world-count datasets using the existing `generate_holdout_dataset` implementation with an explicit fresh seed override. Do not filter or alter counts.

## 3. Sample size and seed schedule

- (K=3) datasets per cell; six datasets total.
- Dataset indices are 0, 1, 2 in each cell.
- Schedule ID: `C10S_F5_POINTWISE_LR_DEV_STRESS_SEEDS_1.0`.
- Namespace: `c10s_f5_pointwise_lr_dev_stress_v1`.
- Seed derivation: first unsigned 64 bits of SHA-256 over `schedule_id|namespace|dataset|cell_id|index`.
- Before generating data, audit all six new seeds against the reconstructed historical schedules used by the prior B2/B3/G7 and comparative-holdout work, plus all dataset/bootstrap/replicate seeds consumed by the executed 50-per-cell M1 pilot. Require global uniqueness and zero collisions. Abort before data generation on any collision.

This deliberately small K is a resource/behaviour probe, not adequate for calibration or coverage estimation.

## 4. Numerical procedure

For each generated dataset:
1. Convert its complete binary rows to the sufficient world-count histogram (x_min{0,ldots,R}).
2. Compute one existing exact unrestricted beta-binomial global-MLE certificate using the bounded configuration below; retain its typed result without overriding unresolved states.
3. At the exact true targets (W=1/5) and (B=1/20), evaluate the existing exact constrained profile maximum and LR-statistic enclosure, using root-isolation width (2^{-8}), maximum depth 140, maximum intervals 5,000 and 80 log-series terms.
4. Record exact rational LR bounds, global-certificate/profile states, root/candidate diagnostics, elapsed time, dataset hash and seed.
5. If the unrestricted certificate is unresolved, preserve the resulting unresolved profile states; do not retry with a different method or silently increase budgets.

The global certificate uses `max_refinements=1`, `projection_bits=12`, `max_projection_depth=40`, `max_lift_intervals=100`, `max_lift_depth=20`, and `max_mu_depth=10`. The source revision is the exact workflow commit.

## 5. Reporting

Report, separately by cell and component:
- completed profile evaluations and typed status counts;
- fraction with finite exact LR enclosures (descriptive only);
- LR enclosure bounds at the known truth (no cutoff);
- global-certificate status;
- runtime and root/candidate counts;
- seed audit and data fingerprints.

Do not label the fraction of enclosed LR statistics as emission under a confidence-interval procedure. Do not calculate coverage, Wilson intervals, acceptance rates, or confidence-set endpoints.

## 6. Stop/interpretation rules

Any missing dataset, seed collision, malformed exact enclosure, non-finite value or integrity failure blocks the run. A valid execution with unresolved numerical statuses is still reported as such and is not converted into PASS for the method.

The result can inform whether a larger, separately specified development calibration design is computationally plausible. It cannot establish that the method meets the frozen Tier-A gates. No Tier-A, Tier-B or causal C10-S execution is authorized by this protocol.
