# TGCV — C09 FOS Endpoint Resolution 001

Status: COMPLETED — ENDPOINT RESOLUTION FROZEN
Date: 2026-09-13
Candidate: HUD Family Options Study (FOS)
Endpoint: p37_composite_hl
Comparison: SUB vs UC
Execution authorization: NONE

## Frozen decision

Baseline SUB–UC comparison population: 1,139.
37-month linked observations: 896.
SUB: 501. UC: 395.
Assignment mismatch: 0.

Two observations in the complete 37-month adult file have p37_composite_hl=D:

- puf1_id=2926: PBTH, randsetgrp=2, w_nr_p37_su=Z. Outside the SUB–UC comparison.
- puf1_id=2506: SUB, randsetgrp=12, w_nr_p37_su=1.0526315789. Relevant to SUB–UC, but endpoint remains indeterminate.

For puf1_id=2506, the observable components are:
p37_hl_only=D; p37_hl_doubled=D; p37_doubled=0; p37_days_hl_only=D; p37_days_doubled=0; p37_days_hl_doub=D; p37_numplaces_6mo=2; p37_ownapt=1; p37_ownapt_noha=1; p37_ownapt_yesha=0.

These observations do not permit deterministic reconstruction of p37_composite_hl. No imputation or inference is permitted.

## Frozen analysis rule

For SUB–UC C09 analysis, use p37_composite_hl only when determinately observed as 0 or 1. Exclude D from outcome calculation, retain the excluded observation in the audit trail, and do not substitute take-up, programme use, housing-status proxies, or partial components for the endpoint. Apply the documented w_nr_p37_su non-response weight to the subsequent estimand calculation.

Resulting SUB–UC endpoint sample: 895 determinately observed outcomes, subject to the subsequent frozen causal-estimation specification.

## Scope

This is an endpoint-resolution PASS for bounded causal-design continuation. It is not a causal effect estimate and does not authorize model fitting or final C09 execution.

Next operation: controlled SUB–UC causal-identification specification, including estimand, treatment definition, weighting, endpoint coding, and exclusion accounting.
