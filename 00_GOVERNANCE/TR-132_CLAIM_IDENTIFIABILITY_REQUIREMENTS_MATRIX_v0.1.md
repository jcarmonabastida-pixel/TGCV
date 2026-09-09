# TR-132 — Claim Identifiability Requirements Matrix v0.1

**Status:** CURRENT / OPERATIVE — DESIGN-ONLY  
**Date:** 2026-09-09  
**Scientific result:** NONE  
**Execution:** NOT AUTHORIZED  
**Origin:** TR-132 — T_acc Operational Identifiability Test v0.1

## Purpose

Determine the minimum empirically identifiable representation of `T_acc` required to test each current claim without changing that claim's meaning. This matrix is a methodological design control for TR-132; it does not upgrade, downgrade, close or reopen any scientific claim.

## Governing distinction

The matrix distinguishes four objects:

- `T_poss(S,C,L)`: technically/physically possible transformations.
- `T_adm(S,C,L)`: transformations admissible under independently specified rules/constraints.
- `T_acc(S,C,L,E)`: transformations effectively accessible under decision-time conditions `E`.
- `T_obs`: transformations actually observed as realized.

`T_obs` is never treated as a substitute for `T_acc`. Non-observation is never treated as inaccessibility.

## Identifiability levels

| Level | Representation | Meaning | Permitted use |
|---|---|---|---|
| L0 | Formal object only | `T_acc` is defined but not empirically identified | Conceptual/formal claims only |
| L1 | Single certified candidate `τ ∈ T_acc^+` | One transformation is independently shown accessible under frozen criteria | Bounded existence/accessibility propositions |
| L2 | Certified bounded subset `T_acc^+` | A non-arbitrarily defined subset/lower representation is identified | Bounded comparisons and bounded `ΔT_acc^+` propositions |
| L3 | Pairwise bounded change `ΔT_acc^+` | Same frozen universe/criteria establish change in a certified subset across `t` | Bounded temporal-change propositions |
| L4 | Closed/full `T_acc` | Candidate universe and all relevant accessibility conditions are independently closed | Full-space propositions |

A higher level is not required merely because it is theoretically possible. The required level is the lowest level that preserves the literal meaning and inferential scope of the claim being tested.

## Claim-by-claim requirements

| Claim | Current status | Minimum representation that can test the claim without semantic weakening | Minimum evidence | Critical prohibitions |
|---|---|---|---|---|
| **C02** Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | **L1** for a bounded empirical test of the representation; **L4** only if the claim is interpreted as exhaustive characterization of the whole accessible set | Ex-ante candidate transformation; frozen predicate; independently evidenced admissibility/accessibility conditions; evidence independent of realized outcome | Do not infer accessibility from realization; do not define predicate from observed success; do not narrow candidate universe after observing result |
| **C03** `T_acc` is analytically distinct from downstream Reach in bounded Rust | E1 | **L2** bounded certified accessibility representation sufficient to show `T_acc` and Reach are different analytical objects | Independently identified candidate accessibility set/subset plus separately defined Reach representation | Do not collapse accessible transformations into realized/reachable outcomes; do not use cardinality as sole identity criterion |
| **C04** `ΔT_acc` can occur without `ΔReach¹_pot` | E1 | **L3** bounded pairwise `ΔT_acc^+ ≠ 0` with `ΔReach¹_pot = 0` under frozen criteria | Same candidate universe, accessibility rule and evidence protocol at both times; independent Reach calculation | No post-hoc candidate selection, threshold changes, or use of non-observation as inaccessibility |
| **C05** `ΔT_acc` can occur with `ΔReach¹_pot` change | E1 | **L3** bounded pairwise `ΔT_acc^+ ≠ 0` with independently observed/derived `ΔReach¹_pot ≠ 0` | Same as C04, with independently reconstructed downstream Reach | No causal inference; no claim that the accessibility change caused the Reach change |
| **C06** Reach identity is not characterized by cardinality alone | E1 | **L2** is sufficient because this is a downstream representation test; `T_acc` need not be fully closed | Same-state or matched-state Reach representations with equal/near-equal cardinality but non-equivalent identity/structure | Do not introduce `T_acc` requirements not needed by the claim; do not equate cardinality with structural identity |
| **C07** Accessible transformation spaces change over time in Rust | E1 | **L3** for the current bounded empirical interpretation. **L4** would be required only for a literal exhaustive claim that the entire `T_acc` space changed | Two time-indexed certified bounded accessibility representations using frozen candidate universe/criteria and independently evidenced change | Do not silently convert a bounded subset change into a full-space claim; do not change universe, predicate or evidence threshold between times |
| **C11** TGCV is domain-independent / transversal | H | **L2/L3 per domain** is sufficient for a bounded transversal translation proposition; **L4 per domain plus broader domain coverage** would be required for full conformance/generalization | Same semantic distinction map across domains; independently reconstructed bounded accessibility object/change; explicit domain-specific operational mapping | Do not infer full domain-independence from one bounded example; do not fill missing accessibility conditions analytically and count them as evidence |
| **C16** TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | **L1/L2 per tested domain**, provided every required distinction is operationally instantiated and preservation is auditable; downstream claims need not be empirically closed for the protocol claim itself | Frozen translation schema; explicit mapping for each distinction; bounded independently supported accessibility representation; audit trail showing no category collapse | Do not substitute formal labels for evidence; do not claim downstream empirical validity from protocol conformance alone |

## Key methodological conclusion

For the current claim set, **full-space identification of `T_acc` is not uniformly required**. Several claims can be tested at a bounded level if their inferential scope is explicitly bounded and the bounded object is certified independently under frozen criteria.

However, a bounded representation is not automatically sufficient for every wording. In particular, a literal full-space reading of C07 would require L4. The current E1 evidence must therefore remain interpreted as bounded rather than silently upgraded to exhaustive temporal change.

Likewise, C11 and C16 can receive meaningful bounded transversal evidence without requiring exhaustive closure of `T_acc` in every domain, but such evidence cannot establish full domain-independence or universal conformance.

## Operational consequence for TR-132

The next executable protocol should test, in order:

1. whether at least L1 can be achieved non-circularly;
2. whether a reproducible L2 bounded subset can be defined without outcome-dependent selection;
3. whether L3 pairwise change can be demonstrated under frozen criteria;
4. whether any current claim actually requires L4;
5. whether failure at L4 leaves a valid bounded proposition rather than invalidating the whole analytical programme.

## Non-retroactivity

This matrix does not alter the Evidence→Claim Matrix v0.6, current epistemic states, falsification criteria, Core, or gate states. If execution later demonstrates that a current claim's existing wording exceeds its empirically identifiable scope, that impact must be adjudicated separately before any claim text is changed.

## Authorization boundary

This artifact authorizes no experiment, dataset execution, industrial case execution, O3 reassessment, Stage C/D activity, causal inference, value assessment, partner evidential engagement, Core modification, threshold relaxation or claim upgrade.
