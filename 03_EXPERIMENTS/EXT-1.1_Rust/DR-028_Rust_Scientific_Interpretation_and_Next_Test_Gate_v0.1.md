# DR-028 — Rust Scientific Interpretation and Next-Test Gate v0.1

**Status:** PROPOSED — EX-ANTE INTERPRETATION GATE, NO NEW EXECUTION AUTHORIZED
**Date:** 2026-09-07
**Scope:** EXT-1.1 Rust and its implications for TGCV

## 1. Purpose

Establish the ex-ante boundary between what EXT-1.1 directly establishes, what it does not establish, and what conditions must be satisfied before any new empirical test, robustness analysis, alternative outcome, alternative representation, or inferential analysis is authorized.

This decision does not modify, reopen, or normalize the closed DR-027 execution evidence.

## 2. Governing evidence

EXT-1.1 confirmatory execution was closed under DR-027C after successful primary execution, identical replay, and structural protocol/result verification.

Primary and replay critical results were exactly equal:

- Eligible origins: 507,279
- Train origins: 280,760
- Test origins: 226,519
- Resolved T_acc relations: 2,509,886
- Unresolved dependency edges: 355,475
- LogLoss(B): 0.40512255638027656
- LogLoss(T_acc): 0.41124528865339655
- Delta LogLoss(B - T_acc): -0.006122732273119991

The primary comparison was defined ex ante as `LogLoss(B) - LogLoss(T_acc)`, with positive values favoring T_acc.

Secondary descriptive metrics also favored B:

- Brier B: 0.12862999557185928
- Brier T_acc: 0.13123035232566702
- ROC AUC B: 0.7671989511641575
- ROC AUC T_acc: 0.759314009238935

No p-values, confidence intervals, significance tests, causal effects, or package-aware inferential quantities were authorized or computed.

## 3. Direct scientific finding

EXT-1.1 provides reproducible evidence that the frozen operational representation of `T_acc^(R*)` did not improve out-of-sample predictive performance relative to the frozen baseline `B` for the frozen outcome `Y_180` (subsequent release activity) in the Rust package-release population.

The observed primary result is unfavorable to the proposition that this operationalization of T_acc provides incremental predictive utility for this outcome under the frozen learner and evaluation protocol.

This is a localized empirical finding. It is not a general refutation of T_acc as a theoretical object.

## 4. What EXT-1.1 does not establish

EXT-1.1 does not establish any of the following:

1. that `T_acc` is ontologically unnecessary;
2. that the TGCV Core `(S, T_acc)` is false;
3. that accessible transformations have no causal, explanatory, or value-relevant role;
4. that T_acc can never contain information not contained in conventional state representations;
5. that the result generalizes to other domains, transformation families, outcomes, horizons, representations, resolvers, learners, or populations;
6. that the negative difference is statistically significant at the population level;
7. that B is causally superior to T_acc;
8. that a different post-hoc representation or outcome should be preferred because of the observed result.

## 5. Interpretation boundary

The experiment tests a predictive incremental-information proposition, not the full TGCV ontological proposition.

The evidence therefore supports the following bounded statement:

> In this Rust operationalization, explicit T_acc representation did not provide incremental predictive utility for subsequent release activity over the frozen baseline.

The evidence does not support the stronger statement:

> T_acc contains no analytically relevant information beyond state representation in general.

The latter would require an independently designed test targeting that proposition.

## 6. Candidate explanations retained without selection

The negative result is compatible with several logically distinct possibilities, including:

- T_acc may be redundant with information already present in B for this outcome;
- the chosen outcome may not be sensitive to the phenomenon TGCV seeks to represent;
- the frozen T_acc representation may not expose the relevant information for this outcome;
- the effect may be conditional on domain, transformation family, horizon, or state context;
- T_acc may be explanatory without yielding incremental predictive performance under this learner.

These are hypotheses only. None is accepted as an explanation by this decision, and none may be selected post hoc to rescue the hypothesis.

## 7. Consequence for TGCV

EXT-1.1 should be incorporated into TGCV as a negative/localized empirical result rather than as a theory-level refutation.

It places pressure on the stronger empirical claim that an explicit T_acc representation should automatically yield incremental predictive value for a downstream outcome. TGCV should therefore avoid treating predictive incrementalism as a universal consequence of representing T_acc.

The more fundamental TGCV proposition — that changes in the accessible transformation space constitute a potentially distinct analytical object — remains open after EXT-1.1.

## 8. Authorization boundary for future work

No new execution is authorized by DR-028 v0.1.

Any future work must first establish ex ante:

- the exact proposition being tested;
- the target outcome or non-predictive criterion;
- why that criterion is theoretically connected to the proposition;
- the population and observational unit;
- baseline representation, if a comparison is used;
- T_acc representation and resolver, if used;
- horizon and temporal protocol, where applicable;
- learner/evaluation method, where applicable;
- primary metric or decision criterion;
- exclusions and missing-data rules;
- reproducibility requirements;
- the exact falsification condition;
- separation from information revealed by EXT-1.1 results.

No alternative outcome, horizon, model, representation, or sampling rule may be selected merely because it is expected to reverse the EXT-1.1 result.

## 9. Decision options to be evaluated

A subsequent accepted gate may select one of the following paths, subject to independent ex-ante justification:

**A. Localized negative evidence:** retain EXT-1.1 as evidence against incremental predictive utility of the present T_acc operationalization for Y_180.

**B. Independent theoretical test:** test whether T_acc captures a property that is theoretically distinct from conventional state variables, without making predictive improvement the sole criterion.

**C. New predictive test:** test a theoretically justified outcome for which T_acc should have a direct relationship, with all choices frozen before inspecting new results.

**D. Theory revision:** revise the empirical scope of the TGCV hypothesis if subsequent evidence establishes that the predictive formulation was too strong.

These options are not selected by this decision.

## 10. Required next step

The immediate next step is methodological, not computational: review this gate against the TGCV Core and existing TR decisions, then decide whether DR-028 can be accepted as the governing interpretation boundary.

Only after acceptance may a new ex-ante research design be drafted, and only if a scientifically justified unresolved proposition remains.

## 11. Closure condition

DR-028 may be accepted when the interpretation boundary is reviewed and no contradiction with DR-023 through DR-027C, TR-130, TR-131, or the current TGCV Core is identified.

**DR-028 v0.1 is intentionally non-executive: it does not authorize computation or alteration of EXT-1.1 evidence.**
