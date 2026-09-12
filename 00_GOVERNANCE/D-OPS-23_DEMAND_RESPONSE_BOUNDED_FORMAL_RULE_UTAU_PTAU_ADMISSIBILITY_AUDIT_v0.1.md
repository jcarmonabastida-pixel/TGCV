# D-OPS-23 — Demand Response Bounded Formal Rule / U_tau / P_tau Admissibility Audit v0.1

**Status:** `CLOSED — BOUNDED SCREENING PASS / C09 EXECUTION NOT ADMITTED`
**Date:** 2026-09-12
**Execution:** `NOT AUTHORIZED`

## 1. Scope correction

This audit does **not** require demonstration over the complete electricity-demand-response universe, nor universal external validity.

The gate is evaluated over an explicitly bounded candidate domain, unit population, event window, transformation profile and decision horizon. The relevant requirement is **bounded completeness**: `U_tau` must be complete and enumerable for the frozen scope of the candidate case, while `P_tau` must be determined ex ante and independently of the realized trajectory.

Universal/transversal validity remains outside this gate and outside C09 execution admission.

## 2. Candidate

The southwestern-China emergency demand-response experiment is retained as the bounded candidate. The published experiment randomly assigned permission to apply for EDR, used 15-minute smart-meter observations, and conducted six trials between 18 July and 21 August 2019. The final study population contained 205,129 households. citeturn1search0turn1search1

## 3. Bounded representation

For a frozen event window and household unit:

- `S_t`: observable household/system state immediately before the response decision;
- `C_t`: frozen event/context variables, including declared peak window and applicable programme conditions;
- `U_tau`: finite candidate response-action profile defined for the event window, e.g. bounded controllable demand-response actions available to the participating household under the experimental protocol;
- `P_tau(S_t,C_t,L)`: ex-ante programme eligibility/admissibility rule;
- `T_acc,t = {tau in U_tau | P_tau(S_t,C_t,L)=1}`;
- `Z`: randomized assignment to EDR access/notification condition;
- `Y`: subsequent electricity-consumption trajectory over the frozen observation window.

The published design establishes a concrete event horizon (20:00–21:30), a benchmark-day comparison, eligibility for monetary rebate conditional on the stated reduction requirement, and randomized assignment to notification/access groups. citeturn1search0

## 4. Gate assessment

### G1 — bounded unit/state identity
**PASS.** Household identity and 15-minute consumption observations provide a bounded longitudinal state representation. citeturn1search0

### G2 — bounded candidate transformation universe
**CONDITIONAL PASS.** A finite `U_tau` can be defined for the frozen event window by an explicit action profile rather than by observed consumption traces. The public experiment does not itself enumerate every physically possible household action; therefore completeness is valid only for the declared operational action profile, not for all conceivable demand changes.

### G3 — ex-ante accessibility rule
**PASS — bounded.** Programme conditions and response-window requirements are specified before observing the realized trajectory; the published protocol distinguishes invitation, confirmation, non-response and no-notification groups. citeturn1search0turn1search1

### G4 — intervention changes access
**PASS — bounded causal-design candidate.** Randomized permission/notification changes whether the household is exposed to the EDR participation opportunity. The study explicitly treats the assignment as a randomized design for identifying the ITT effect of EDR access. citeturn1search0

### G5 — no direct encoding of trajectory
**PASS — preliminary.** Assignment determines access/notification and programme eligibility; it does not prescribe the household's subsequent 15-minute consumption sequence. The realized trajectory remains an outcome. This must be preserved in any future frozen execution specification.

### G6 — counterfactual
**PASS — bounded.** Random assignment provides treated/untreated comparison within the experimental population. This supports internal causal identification within the bounded study population; it does not establish external validity beyond that population. citeturn0search0turn0search1

### G7 — transition environment unchanged
**CONDITIONAL PASS.** The intervention operates through access/notification and incentive exposure within the same underlying electricity-use environment. However, the intervention may alter household behaviour and therefore the realized state transition; that is the intended treatment effect, not a change to the underlying transition law. This distinction must be frozen explicitly before execution.

### G8 — information firewall
**PASS — designable.** `P_tau` may be constructed from pre-event programme conditions and state/context variables. Post-event consumption, realized savings, rebates earned and downstream trajectory must be excluded from accessibility adjudication.

## 5. Decision

**D-OPS-23 = CLOSED — BOUNDED SCREENING PASS / C09 EXECUTION NOT ADMITTED.**

The candidate clears the **bounded discovery/admissibility screen** after correcting the previous over-stringent requirement for whole-domain formal-system equivalence.

This does **not** establish:

- universal `U_tau` completeness;
- cross-domain validity;
- general causal validity outside the bounded study population;
- causal identification of TGCV's `ΔT_acc → trajectory` relation;
- predictive superiority;
- industrial value;
- any C09 claim upgrade.

## 6. Remaining C09 gate

The next gate is no longer broad discovery. It is a **bounded causal operationalization gate**:

> Freeze one concrete event/unit profile in which `U_tau`, `P_tau`, `T_acc,0`, randomized accessibility intervention `Z`, and subsequent trajectory `Y` can all be independently reconstructed without post-treatment leakage, and demonstrate that `Z` changes `T_acc` rather than merely changing an incentive/outcome variable.

Only after that gate passes can a separate execution authorization be considered.

No real-data execution, model fitting, AWS mutation, Rust rerun or SWIM rerun is authorized.
