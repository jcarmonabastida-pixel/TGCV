# D-OPS-19 — Ethereum C09 Intervention Identification Audit v0.1

**Status:** `COMPLETED — NO CAUSAL INTERVENTION ADMITTED`
**Date:** 2026-09-12
**Execution:** `NOT AUTHORIZED`
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories

## 1. Purpose

Audit whether Ethereum contains an intervention mechanism capable of changing `T_acc` independently of the subsequent trajectory, while preserving a credible counterfactual and the C09 information firewall.

This is an intervention-identification gate. It is not causal execution and does not upgrade C09.

## 2. Candidate intervention classes

### A. Protocol rule activation / hard fork

A protocol upgrade can change transaction admissibility. Current Ethereum proposals explicitly demonstrate this mechanism. EIP-7825, for example, introduces a transaction gas-limit cap and specifies that transactions above the cap are rejected during transaction validation. The proposal also reports an empirical impact analysis of historical transactions. citeturn0search0turn0search10

**Strength:** intervention is externally specified, timestamp/fork-bounded, and changes `P_tau` directly.

**Problem:** a hard fork may change multiple execution rules simultaneously. Even a narrowly specified rule change changes the governing transition function and potentially transaction behaviour, not merely accessibility. The intervention therefore risks violating the C09 requirement that the accessibility treatment be isolated from the target trajectory mechanism.

**Disposition:** `CANDIDATE — NOT ADMITTED`

### B. Gas-limit / resource-parameter changes

Ethereum has experienced protocol-level gas-limit changes; the Ethereum Foundation documented the move to a 45M mainnet gas limit and the broader scaling programme. EIP-8037 also explicitly describes how gas-limit changes alter state creation and transaction validation constraints. citeturn0search2turn0search3

**Strength:** the parameter change is externally observable and can alter the set of admissible transactions.

**Problem:** the parameter simultaneously changes execution capacity and economic/network behaviour. It is therefore not a clean intervention on `T_acc` alone. Treatment exposure is also heterogeneous and correlated with transaction resource demand.

**Disposition:** `REJECT FOR C09 ISOLATED-ACCESSIBILITY IDENTIFICATION`

### C. State manipulation of balances, nonces, permissions or contract state

A controlled state intervention can change `T_acc` because protocol validity is evaluated against the pre-state.

**Strength:** direct and potentially precise modification of accessibility.

**Problem:** in the historical mainnet archive, these state changes are endogenous to prior activity. A retrospective observational identification would therefore lack an independently assigned treatment. A synthetic or manually imposed state change would become a model-based counterfactual rather than observed causal evidence.

**Disposition:** `REJECT FOR HISTORICAL CAUSAL EXECUTION`

### D. Contract/code intervention

Changing contract code or account state can alter which transformations are admissible or executable.

**Problem:** code/state modification can directly determine the downstream trajectory. This violates the C09 requirement that the intervention change accessibility without directly encoding the target outcome.

**Disposition:** `REJECT`

## 3. Most promising specific mechanism: EIP-7825-style admissibility threshold

The cleanest available Ethereum example is a rule that changes validity for a sharply defined transaction profile: EIP-7825 caps transaction gas at `2^24`; transactions specifying a larger gas limit are rejected during transaction validation. citeturn0search0

This creates a strong structural contrast:

`pre-fork: τ ∈ T_acc`

`post-fork: τ ∉ T_acc`

for affected transaction profiles, while lower-gas transactions remain unaffected by that specific cap. The proposal's empirical report identifies a small affected subset in six months of Q1 2025 data. citeturn0search10

However, three identification problems remain:

1. **Treatment assignment is not random.** High-gas transactions are systematically different from low-gas transactions.
2. **Fork intervention changes protocol rules.** The post-fork world is not merely the pre-fork world with one accessibility bit changed; execution validity is governed by the new rule set.
3. **Observed downstream behaviour is adaptive.** Users/contracts can alter transactions in response to the rule, so observed post-fork trajectories combine accessibility effects with behavioural adaptation.

A threshold comparison around the gas cap could therefore be informative descriptively, but it is not sufficient by itself for C09 causal identification.

## 4. Counterfactual feasibility

Three possible counterfactuals were assessed:

| Counterfactual | C09 suitability |
|---|---|
| Historical pre-fork state replayed under post-fork rules | Strong structural counterfactual; model/specification evidence, not direct real-world causal evidence |
| Historical post-fork state replayed under pre-fork rules | Strong structural counterfactual; same limitation |
| Observed affected vs unaffected historical units | Weak causal counterfactual because treatment is endogenous |

The first two can establish what the protocol transition function implies under controlled rule intervention. They cannot, without additional identification assumptions, establish that an observed real-world trajectory changed causally because accessibility changed.

## 5. C09 firewall assessment

The intervention must satisfy:

`Z → ΔT_acc`

while excluding:

`Z → Y` directly,

and excluding common causes that determine both treatment and trajectory.

Protocol upgrades satisfy the first condition structurally better than endogenous state changes, but they do not cleanly satisfy the second because a protocol upgrade changes the execution environment itself. State/code interventions fail more strongly because the intervention can directly encode the successor trajectory.

**Firewall result: FAIL for an observational causal-execution design.**

## 6. Gate matrix

| Requirement | Result |
|---|---|
| Independently specified intervention mechanism | PASS — protocol upgrades |
| Direct change in `P_tau` / `T_acc` | PASS |
| Random/independent treatment assignment | FAIL |
| Treatment isolated from transition-rule changes | FAIL / unresolved |
| No direct trajectory encoding | FAIL for state/code interventions; unresolved for forks |
| Credible observed treatment/control counterfactual | FAIL |
| Structural counterfactual replay | PASS — bounded/model-based |
| C09 real-world causal identification | **NOT ADMITTED** |

## 7. Decision

**D-OPS-19 = CLOSED — NO ETHEREUM INTERVENTION ADMITTED FOR C09 CAUSAL EXECUTION.**

Ethereum remains scientifically valuable as an external domain for structural identifiability and counterfactual transition analysis, but the current audit does not establish an admissible real-world causal intervention satisfying the C09 information firewall.

This is a **negative feasibility result**, not a rejection of Ethereum as a scientific domain in general.

No C09 claim upgrade is permitted.

## 8. Consequence for the programme

The result sharpens the C09 requirement:

> A domain with a formally specified transition system and complete longitudinal state history is not sufficient. C09 additionally requires an intervention that changes accessibility while leaving the target trajectory mechanism identifiable and counterfactual treatment assignment credible.

This requirement is now a reusable screening criterion for subsequent domain discovery.

## 9. Next controlled operation

Do not execute Ethereum data.

Return to **controlled cross-domain intervention discovery**, but retain the newly strengthened filter:

`formal rule layer + public longitudinal state archive + stable identity + independently assigned accessibility intervention + credible counterfactual + no direct trajectory encoding`.

Any future candidate failing the intervention criterion is rejected before dataset acquisition or execution.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
