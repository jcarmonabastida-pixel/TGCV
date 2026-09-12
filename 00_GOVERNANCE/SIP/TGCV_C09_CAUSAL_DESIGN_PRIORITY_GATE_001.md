# TGCV — C09 Causal Design Priority Gate 001

**Status:** `PRIORITY NEXT — DESIGN ONLY / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-12
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories

## 1. Trigger
RUST-DYN-2 is closed as a bounded structural empirical pass, distinguishing `ΔT_acc` from potential one-step Reach under H=1. SWIM trajectory linkage is closed as bounded observed association/reconstructability. These results leave the causal link unresolved and explicitly prevent treating association as causality.

## 2. Why C09 is next
C09 is the immediate unresolved causal link after the bounded C08 evidence. It has high falsification value, directly tests the mechanism-to-trajectory segment, and prevents downstream Value work from being built on an untested causal assumption. C10, C11, C12 and C13 remain open parallel claims; none is closed by this gate.

## 3. Required causal question
Under a frozen decision-time state/context and an independently defined accessibility rule, does an exogenous change in accessibility conditions produce a distinguishable change in subsequent trajectory relative to an appropriate counterfactual or controlled comparison?

## 4. Minimum design requirements
- decision-time state/context frozen before treatment;
- accessibility rule defined independently of subsequent outcome/trajectory;
- intervention changes accessibility conditions without directly encoding the target trajectory outcome;
- explicit treatment/control or counterfactual construction;
- trajectory criterion fixed ex ante;
- post-treatment observation window fixed ex ante;
- no leakage from future events into accessibility classification;
- treatment assignment or equivalent identification strategy justified;
- confounders and alternative explanations specified;
- stopping/falsification criteria fixed before result inspection;
- reproducible reconstruction of `T_acc`, accessibility change and trajectory;
- separate treatment of causal effect, association, execution and value.

## 5. Falsifiers / stop conditions
The design must stop or classify as inconclusive if accessibility cannot be independently manipulated/identified, treatment and counterfactual states cannot be distinguished, trajectory is not independently defined, post-treatment information leaks into accessibility, or observed differences can be explained by direct intervention effects/confounding rather than accessibility change.

## 6. Explicit exclusions
This gate does not authorize execution, dataset acquisition, AWS mutation, SWIM rerun, RUST-DYN-2 rerun, value analysis, industrial utility claims, or claim upgrade.

## 7. Decision
**C09 is the current next scientific priority.** The immediate next operation is to develop and audit the causal-design specification against this gate before any execution authorization is considered.
