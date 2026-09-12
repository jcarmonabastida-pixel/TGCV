# D-OPS-18 — Ethereum Transaction Universe / Pre-Execution Admissibility Identifiability Audit v0.1

**Status:** `COMPLETED — PRIMARY CANDIDATE RETAINED / CAUSAL EXECUTION NOT ADMITTED`
**Date:** 2026-09-12
**Execution:** `NOT AUTHORIZED`
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories

## 1. Purpose

Determine whether Ethereum can provide a concrete, reproducible operationalization of `U_tau`, canonical state identity, pre-execution admissibility `P_tau`, `T_acc`, and successor/Reach semantics without using observed downstream outcomes or historical transaction inclusion.

This audit is an identifiability/design gate only. It does not constitute C09 causal evidence.

## 2. Reused canonical discovery

D-OPS-15 selected Ethereum as the primary external-domain candidate because it combines an independently specified state-transition rule system with a public longitudinal history of states. This audit therefore reuses that selection and does not reopen cross-domain discovery.

## 3. Evidence reviewed

The Ethereum Execution Layer Specifications (EELS) provide an executable Python reference implementation of execution-layer consensus behaviour and associated tests. The specification is maintained against network upgrades. citeturn1search1

The execution test ecosystem publishes versioned fixtures covering transaction validity and state-transition behaviour across forks. Current releases have moved the maintained testing infrastructure into `ethereum/execution-specs`, while the former `execution-spec-tests` repository is archived. citeturn1search2turn1search5

Ethereum archive nodes provide access to historical states, while full nodes retain the historical blockchain journal and can regenerate older states by replaying transactions. This establishes a reproducible longitudinal state source, subject to declaring the exact block/fork boundary. citeturn1search0turn1search3

## 4. Canonical state identity

### Candidate definition

`S_t = canonical execution state at a declared block boundary b_t under fork F_t`.

The boundary must be frozen before analysis. The state identifier is the canonical state root associated with the selected block/fork context, supplemented by the block number/hash and fork specification required to interpret the state.

### Assessment

**PASS — bounded**, provided fork and block boundary are explicit.

Potential ambiguity from protocol upgrades is not a blocker: it becomes part of `C_t/L` and must not be silently mixed across forks.

## 5. Transaction/operation universe `U_tau`

A key requirement is that `U_tau` cannot be defined as the transactions historically observed on-chain, because that would condition accessibility on realised historical behaviour.

A valid construction is a frozen **transaction-profile universe** generated from the protocol grammar/types and explicit parameter domains. The profile must specify, before execution:

- transaction type(s) admitted;
- sender/account identity domain;
- recipient/contract identity domain;
- nonce domain;
- value domain;
- gas-limit domain;
- fee fields/domain;
- calldata/authorization/blob-related fields where applicable;
- fork-specific validity rules.

### Critical computational issue

The unrestricted Ethereum transaction space is effectively enormous because calldata, addresses, values and contract behaviour create a combinatorial space. Therefore the unrestricted universe cannot be enumerated directly.

A finite `U_tau` is nevertheless technically possible through a frozen bounded profile. The bound must be justified independently of observed outcomes and fixed before execution. A convenience-driven arbitrary truncation would weaken the scientific interpretation and could make the result profile-dependent.

### Assessment

**CONDITIONAL PASS — finite bounded profile is feasible; unrestricted universe is NOT executable.**

This is a central pre-execution control, not a minor implementation detail.

## 6. Pre-execution admissibility `P_tau`

`P_tau(S_t,C_t,L)` must use only information available immediately before the candidate transformation is applied.

Admissibility can include protocol-defined conditions such as transaction encoding/type validity, signature validity, nonce validity, sender constraints, gas/fee constraints and other fork-specific validity predicates. The maintained execution specifications and tests explicitly cover transaction-validity behaviour. citeturn1search1turn1search2

### Forbidden inputs

The following must not enter `P_tau`:

- historical inclusion in a block;
- transaction receipt/result;
- post-execution balances or storage;
- realised gas usage;
- logs/events generated after execution;
- downstream trajectory;
- outcome variables selected after treatment;
- historical frequency of a candidate transaction as a proxy for admissibility.

### Assessment

**PASS — design-level.**

The protocol supplies an independent pre-execution validity layer. The remaining requirement is to freeze the exact fork-specific predicate implementation used in any future execution.

## 7. Construction of `T_acc`

For a frozen state/profile:

`T_acc,t = { τ ∈ U_tau | P_tau(S_t,C_t,L) = 1 }`.

This differs explicitly from the observed transaction set in the historical blockchain.

A transaction can therefore belong to `T_acc,t` without ever having been submitted or included. This is essential because observed inclusion is downstream evidence and cannot define accessibility.

### Assessment

**PASS — design-level.**

The construct is operationally distinguishable from realised transaction history.

## 8. Successor and Reach construction

For a candidate `τ ∈ T_acc,t`, define a deterministic successor execution state under the declared fork semantics:

`S_{t+1} = τ_exec(S_t, τ, C_t)`.

`Reach_H(S_t)` is the bounded set of successor states generated by the frozen profile over horizon `H`.

The key distinction is:

`T_acc,t` = transformations admissible before execution;

`Reach_H` = states generated after applying admissible transformations.

The historical blockchain must not be used as the definition of Reach, because that would collapse potential reachability into observed trajectory.

### Assessment

**PASS — design-level / bounded**, subject to the same finite-profile constraint as `U_tau`.

## 9. Information-firewall audit

| Information | Allowed in pre-execution `T_acc`? |
|---|---:|
| State root / pre-state | YES |
| Fork/protocol rules | YES |
| Transaction grammar | YES |
| Pre-state account nonce/balance/storage | YES |
| Historical transaction inclusion | **NO** |
| Receipt/result | **NO** |
| Post-state | **NO** |
| Future block contents | **NO** |
| Observed future trajectory | **NO** |
| Outcome/value variable | **NO** |

**Firewall result: PASS — designable and auditable.**

## 10. C09 intervention problem

The audit identifies a stronger issue that prevents immediate causal execution admission.

Ethereum provides an excellent separation between admissibility and realised execution, but a C09 causal intervention still has to change accessibility independently of the subsequent trajectory.

Possible intervention classes include:

1. **Protocol-rule intervention:** a fork changes validity rules. This changes `L/P_tau` but also changes the governing rule system itself, creating a substantial interpretation problem for C09.
2. **State intervention:** a controlled change to balances, nonce, permissions or contract state can alter `T_acc`. In historical observational data, however, such changes are generally endogenous to preceding activity.
3. **Account/contract intervention:** changing state or code may directly encode or constrain the downstream trajectory and therefore risks violating the C09 intervention boundary.

Consequently, the existence of a clean `T_acc` construct does **not** itself supply an admissible causal treatment.

### Assessment

**OPEN — CRITICAL C09 IDENTIFICATION ISSUE.**

## 11. Overall gate matrix

| Requirement | Result |
|---|---|
| Independent domain | PASS |
| Canonical longitudinal state archive | PASS |
| Stable/fork-aware state identity | PASS — bounded |
| Independently defined `U_tau` | CONDITIONAL PASS |
| Finite executable profile | CONDITIONAL PASS |
| Non-circular `P_tau` | PASS — design-level |
| Pre-execution `T_acc` | PASS — design-level |
| `Reach` distinct from observed history | PASS — bounded/design-level |
| Information firewall | PASS — designable |
| Independent accessibility intervention | **OPEN — CRITICAL** |
| C09 causal identification | **NOT ADMITTED** |

## 12. Decision

**D-OPS-18 = PASS AS IDENTIFIABILITY / DESIGN FEASIBILITY, WITH C09 TREATMENT GATE OPEN.**

Ethereum remains the **primary external-domain candidate**.

The audit establishes that the domain can support a clean, non-circular distinction between:

`protocol/state → admissible transformations (T_acc) → generated successor states (Reach) → trajectories`.

It does not establish that an admissible causal intervention on `T_acc` is available.

## 13. Required next operation

Before any dataset execution, the next controlled operation must audit **candidate intervention mechanisms** capable of changing `T_acc` while:

- being independently assigned/reconstructible;
- preceding the measured trajectory;
- not encoding the trajectory outcome directly;
- preserving a credible treatment/control or counterfactual;
- keeping the `T_acc` rule frozen and pre-treatment;
- remaining computationally bounded.

If no such intervention exists in Ethereum, the domain must be rejected for C09 causal execution despite its excellent state-transition identifiability.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
