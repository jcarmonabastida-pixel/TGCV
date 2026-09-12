# D-OPS-21 — Regulated Allocation / Scheduling Rule-Layer C09 Discovery Audit v0.1

**Status:** `COMPLETED — PROMISING DOMAIN FAMILY / NO EXECUTION CANDIDATE ADMITTED`
**Date:** 2026-09-12
**Execution:** `NOT AUTHORIZED`
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories

## 1. Purpose

Test the strongest rule-layer-first family identified after D-OPS-20: regulated allocation and scheduling systems where an externally imposed procedural change can alter the transformations admissible to an actor, while historical operational records preserve subsequent trajectories.

## 2. Candidate family: Spanish electricity balancing / tertiary regulation

The Spanish electricity system provides an unusually explicit allocation rule layer. CNMC's operating procedures specify a tertiary-regulation offer-allocation algorithm, including the programming period, activation horizon, minimum-cost allocation criterion and security constraints. citeturn0search11turn0search15

A July 2026 CNMC resolution also specifies changes to system-operation procedures implementing 96 rounds of continuous intraday-market negotiation and requires publication of detailed allocation outcomes and prices. citeturn0search10

This is materially closer to the required TGCV architecture than generic transport/policy domains because the rule itself governs which offers can be selected/activated and how allocation occurs.

## 3. TGCV mapping

Candidate unit:

`U = one programming/activation decision for a defined balancing service and market period`.

Candidate state:

`S_t = pre-allocation market/system state`, including the frozen set of eligible offers, operational constraints and relevant system conditions.

Candidate transformation universe:

`U_tau = eligible offer/activation actions permitted by the governing operating procedure`.

Candidate admissibility:

`P_tau(S_t,C_t,L) = 1` iff the offer/action satisfies the applicable technical, temporal, security and market rules before allocation.

Candidate accessibility:

`T_acc,t = {τ : P_tau(S_t,C_t,L)=1}`.

Subsequent trajectory:

system state / dispatch evolution over a fixed post-allocation horizon.

## 4. Intervention candidate

The strongest intervention class is a **prospectively dated regulatory/procedural rule change** that modifies the allocation/scheduling rule while leaving some operational conditions and eligible units observable before and after the transition.

The 2026 CNMC change is recent and therefore unsuitable for a completed historical C09 execution today, but it demonstrates that the governing rule layer can be externally changed and precisely dated. citeturn0search10

Earlier operating-procedure changes provide the historical direction for a future longitudinal audit. The critical question is whether a past change can be isolated such that:

`Z → ΔT_acc`

without simultaneously changing the trajectory-generating mechanism in a way that makes C09 uninterpretable.

## 5. Identification risks

Three risks remain critical:

1. **Rule-change bundling:** regulatory changes may modify several market/system mechanisms simultaneously.
2. **Strategic adaptation:** market participants may alter offers in anticipation of or response to the new rule.
3. **Direct transition-function change:** if the rule changes dispatch itself rather than only admissibility, the intervention may affect trajectory directly.

Therefore the domain is not yet admitted.

## 6. Preliminary gate

| Requirement | Result |
|---|---|
| Governed formal rule layer | **PASS** |
| Versioned/dated rule changes | **PASS — prelim** |
| Longitudinal operational data | **PASS — prelim / retrieval audit required** |
| Stable decision unit | **PASS — bounded** |
| Pre-decision state reconstructible | **OPEN** |
| `U_tau` finite/operationally bounded | **PASS — bounded by eligible offers/actions** |
| `P_tau` independent of post-outcome data | **PASS — design-level** |
| Accessibility intervention changes `T_acc` | **OPEN — historical audit required** |
| No direct trajectory encoding | **OPEN — critical** |
| Credible counterfactual | **OPEN — critical** |
| C09 execution readiness | **NOT READY** |

## 7. Decision

**D-OPS-21 = CLOSED — PROMISING RULE-LAYER FAMILY, NO C09 EXECUTION CANDIDATE ADMITTED.**

This is the first post-Ethereum discovery family that satisfies the rule-layer requirement strongly enough to justify a dedicated feasibility audit.

It does not yet satisfy the intervention/counterfactual requirements.

## 8. Next operation

Perform a controlled historical audit of **one concrete Spanish electricity operating-procedure change**, selecting a change for which:

- the exact pre/post rule versions are recoverable;
- the affected eligibility/allocation predicate can be reconstructed;
- pre-treatment operational state is archived;
- unaffected comparison units or a credible quasi-experimental counterfactual exist;
- the intervention does not directly prescribe the measured post-treatment trajectory;
- all outcome variables are frozen before inspection.

No real-data execution or causal estimation is authorized by this document.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
