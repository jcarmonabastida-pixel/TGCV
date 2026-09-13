# TGCV — C09 Santiago Fare-Free Transit TR-132 Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-14
**Candidate:** Bull, Muñoz & Silva — Santiago fare-free public transport randomized controlled trial
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Gate:** TR-132 / C09 Domain Identification Gate 001

## 1. Candidate

The study randomly assigned 207 workers at 13 firms in Santiago, Chile to receive either a two-week unlimited fare-free public transport pass (`N=106`) or no pass (`N=101`). The published study reports effects on overall travel, off-peak travel and public-transport use.

Primary source: Bull, O., Muñoz, J.C., Silva, H.E. (2021), *The impact of fare-free public transport on travel behavior: Evidence from a randomized controlled trial*, Regional Science and Urban Economics 86, 103616. DOI: 10.1016/j.regsciurbeco.2020.103616.

## 2. TR-132 screening

| Gate | Result | Finding |
|---|---|---|
| P1 — identifiable unit | **PASS** | Individual worker enrolled in the randomized experiment. |
| P2 — reconstructible baseline | **PASS DESIGN / DATA ACCESS OPEN** | Application data and first-week trip diaries define baseline in the study. |
| P3 — intervention changes accessibility | **PASS CONCEPTUALLY** | Fare-free pass changes the cost/availability condition for public-transport travel during the treatment window. |
| P4 — bounded `U*` and `T_acc,0/T_acc,1` | **CONDITIONAL / DATA BLOCKER** | The study records trip modes/purposes and baseline information, but the underlying participant-level records needed to independently reconstruct a frozen bounded transformation universe and pre/post accessibility profile are not established as publicly downloadable. |
| P5 — independent trajectory | **PASS DESIGN** | Subsequent two weeks of trip-diary outcomes are temporally separated from the first-week baseline. |
| P6 — treatment/counterfactual identification | **PASS DESIGN** | Individual random assignment provides a credible counterfactual in the original experiment. |
| P7 — public independent reproducibility | **FAIL CURRENT PACKAGE** | No public unit-level experimental package containing the required application/assignment/diary records was located in the governed search. |
| P8 — execution authorization | **NOT ADMITTED** | P4/P7 prevent independent reconstruction of the required bounded causal representation. |

## 3. What the public evidence establishes

The published article establishes that the intervention was randomized and that application data plus trip diaries were used to construct baseline and subsequent outcomes. It therefore provides strong methodological evidence that the candidate has the required causal architecture in principle.

The public evidence does **not** establish that TGCV can independently reconstruct the participant-level `T_acc,0/T_acc,1` contrast from an unrestricted reproducible package.

The published results themselves cannot be substituted for the underlying treatment, accessibility and trajectory records. Doing so would violate the C09 information firewall.

## 4. Rejected substitutions

The following are explicitly rejected as substitutes for the missing public operational package:

- published treatment-effect estimates;
- aggregate trip counts or published tables;
- treatment assignment inferred from reported group totals;
- realized trips used as a proxy for pre-treatment `T_acc`;
- proximity to subway as a treatment/accessibility definition;
- the public description of the fare-free pass without participant-level assignment and baseline records;
- restricted smart-card or administrative records not independently downloadable under the candidate package.

## 5. Decision

**SANTIAGO RCT = STRONG METHODOLOGICAL CANDIDATE / CURRENT EXECUTION CANDIDATE CLOSED FOR PUBLIC-REPRODUCIBILITY PURPOSES.**

The candidate is not rejected because the causal design is weak. It is rejected because the current governed evidence does not establish the public, independently reproducible unit-level representation required by TR-132.

No causal model is fitted. No data are acquired from restricted sources. No treatment effect is re-estimated. No Matrix, RMA, Core or C09 claim status is changed.

## 6. Reopening condition

Santiago may be reopened only if a public, independently reproducible package is identified containing sufficient participant-level assignment, baseline and trajectory information to reconstruct the frozen bounded `U*`, `T_acc,0/T_acc,1` and `Y` without post-treatment leakage.

## 7. Sources checked

- ScienceDirect article: https://www.sciencedirect.com/science/article/pii/S016604622030301X
- PUC Chile working paper: https://www.economia.uc.cl/docs/doctra/dt-531.pdf
- PUC Chile publication record: https://www.ing.uc.cl/publicaciones/the-impact-of-fare-free-public-transport-on-travel-behavior-evidence-from-a-randomized-controlled-trial/

## 8. Governance disposition

`TR-132 = NOT PASSED FOR EXECUTION`

`EXECUTION AUTHORIZATION = NONE`

`C09 = OPEN — UNTESTED REAL-WORLD CAUSAL CLAIM`
