# D-OPS-20 — Formal-to-Empirical Bridge Audit v0.1

**Status:** CLOSED — FORMAL-TO-EMPIRICAL BRIDGE DOES NOT CURRENTLY YIELD AN INDEPENDENT EXECUTION-READY DOMAIN
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Purpose

Determine whether a formal domain with a clean finite transformation universe can be legitimately connected to a public longitudinal empirical source without changing the TGCV unit of analysis or introducing circularity.

The immediate formal candidate is classical PDDL/planning. The audit asks whether public real-world robotics/planning datasets can supply longitudinal states while an independently governed PDDL rule layer supplies U_tau and P_tau.

## 2. Historical reconstruction

The current sequence is:

- Rust: E1 empirical evidence under frozen operationalization.
- Cross-domain literature reconstruction: PASS at bounded architectural level.
- Railway: blocked by historical public-state retrieval.
- Legal/regulatory: blocked by independent non-circular U_tau/P_tau.
- Ethereum: blocked by finite transformation-unit identifiability at empirical scale.
- D-OPS-19: PDDL retained as a clean formal candidate, but it lacked longitudinal real-state evidence.

D-OPS-20 therefore tests whether a formal-to-empirical bridge solves that missing dimension without silently replacing TGCV's transformation unit.

## 3. Formal side: PDDL

PDDL action schemas provide parameters, preconditions and effects. A grounded action can be independently enumerated from the declared objects/types, and applicability can be evaluated from the current symbolic state. Thus, for a frozen domain/problem:

`U_tau` = grounded action instances

`P_tau(S,C,L)` = action precondition satisfaction

`T_acc(S)` = applicable grounded actions

`Succ(S,tau)` = symbolic successor obtained from the declared effects.

This is a strong formal realization of the TGCV accessibility architecture. PDDL documentation explicitly distinguishes an action being possible from it actually being selected/applied.

## 4. Empirical bridge candidates

### A. UniDomain / real-robot demonstrations

UniDomain uses 12,393 manipulation videos to learn atomic PDDL domains and a unified symbolic domain. This demonstrates that real demonstrations can be translated into PDDL-like action/state representations.

However, the learned domain is itself derived from the demonstrations. Therefore using that learned domain as the independent rule layer and then measuring accessibility changes in the same demonstrations would introduce circularity.

**Result: FAIL as independent TGCV bridge.**

### B. PO-PDDL / demonstration-derived symbolic models

PO-PDDL similarly reconstructs latent symbolic trajectories and learns stochastic manipulation/observation models from demonstrations.

Again, the rule/model layer is learned from the same empirical behaviour that would be used to measure accessibility. It is therefore unsuitable as an independently governed P_tau for the present test.

**Result: FAIL as independent TGCV bridge.**

### C. Public robot trajectory datasets with externally fixed action semantics

Datasets such as BEHAVIOR and Open X-Embodiment provide large longitudinal trajectories of real robot states/actions. They establish that longitudinal empirical state/action streams are publicly available in principle.

But the audited public descriptions do not provide a single independently governed, externally frozen action admissibility rule system that is guaranteed to apply to the recorded trajectories. Robot actions are observations/control commands, not automatically the complete TGCV U_tau.

Defining P_tau from observed success, executed actions, reward, task completion or learned models would violate the firewall.

**Result: FAIL for current replication.**

## 5. Decisive methodological result

A formal PDDL domain solves the **finite transformational-unit problem** but not the **longitudinal empirical-state problem**.

Real-robot trajectory datasets solve the **longitudinal empirical-state problem** but, in the currently identified public resources, do not supply an independently governed transformation/admissibility layer.

Learning the PDDL domain from the same demonstrations does not solve the problem; it moves the rule layer inside the evidence-generating process and therefore breaks the independence requirement.

Consequently, the bridge cannot currently be closed without introducing one of three prohibited substitutions:

1. infer P_tau from observed behaviour;
2. infer U_tau from executed actions;
3. use a learned domain derived from the same trajectories as the supposedly independent rule layer.

## 6. Decision

**D-OPS-20 = CLOSED — NO VALID FORMAL-TO-EMPIRICAL BRIDGE CURRENTLY IDENTIFIED.**

This is not a falsification of TGCV and not a failure of the formal architecture. It is a closure of the present external-domain search under the project's independence and non-circularity requirements.

## 7. Scientific state after D-OPS-20

- Rust empirical evidence: **E1**, bounded to frozen Rust operationalization.
- Formal TGCV architecture: **E0/formally established**.
- Cross-domain architectural reconstruction: **PASS at bounded level**.
- Independent empirical replication: **OPEN**.
- Domain-independent validity: **H**.
- Causal claims: **H**.
- Predictive claims: **H**.
- Value claims: **H**.
- Universal originality: **OPEN**.

The absence of an execution-ready second domain is itself a methodological finding: the difficult component is not merely obtaining another dataset, but obtaining an independently governed transformation universe and admissibility predicate that can be connected to a genuine longitudinal state archive without leakage.

## 8. Governance consequence

**The external-domain discovery program is CLOSED for the current evidence base.**

No further candidate search should be initiated merely to obtain a second empirical domain. A new domain may only be reopened if an independently governed rule/constraint system plus a public longitudinal state archive becomes available and passes the same identifiability gate.

The project should now prioritize the highest-information open scientific question rather than continued domain hunting.

The next controlled operation should therefore be selected from the existing evidence matrix, with priority between:

- independent replication if a genuinely admissible domain emerges;
- stronger internal validation/robustness of the Rust result;
- originality/comparative architectural analysis;
- or explicit claim-boundary closure.

**REAL-DATA EXECUTION AUTHORIZED: NO.**

## 9. External evidence consulted

- PDDL domain/action semantics: planning.wiki / PDDL reference.
- Public PDDL benchmark repositories and API.
- UniDomain: real-world demonstrations translated into PDDL domains.
- PO-PDDL: demonstration-derived symbolic models.
- BEHAVIOR public robot trajectory datasets.
- Open X-Embodiment public robot trajectory corpus.
