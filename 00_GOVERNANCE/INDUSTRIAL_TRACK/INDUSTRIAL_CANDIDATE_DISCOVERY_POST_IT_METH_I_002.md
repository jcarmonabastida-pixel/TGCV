# TGCV — Post-IT-METH-I Industrial Candidate Discovery 002

**Date:** 2026-09-11  
**Status:** `CURRENT CORRECTION — SCREENING FRAMEWORK UPDATE; NO IT-G1 AUTHORIZATION`  
**Supersedes screening interpretation only; historical 001 record remains immutable**  
**Filter:** `INDUSTRIAL_DISCOVERY_FILTER_POST_IT_METH_I_v0.2`  
**Normative dependency:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.2.md`; TR-132-MOD-1

## 1. Purpose

Propagate TR-132-MOD-1 into post-IT-METH-I industrial candidate discovery and prevent inadvertent reintroduction of a requirement for exhaustive ex-ante reconstruction of the complete accessible transformation structure.

No experiment is authorized by this record. The FAA AMOC experiment remains closed and is not reopened.

## 2. Corrected screening principle

The post-IT-METH-I filter shall not require a complete ex-ante enumeration of `T_acc(S_t)`.

A candidate may remain viable when the alternative space is only partially known or unknown, provided that:

- the concrete candidate transformation `τ_i` is independently identifiable;
- the relevant pre-outcome state/context is reconstructable;
- accessibility/admissibility of `τ_i` can be assessed from that pre-outcome information;
- the accessibility assessment is independent of the subsequent outcome;
- the resulting state transition and downstream separation remain reconstructable.

## 3. Effect on prior discovery findings

The prior 001 record is preserved unchanged. Its conclusion that cloud/runbook automation was the most promising direction remains unaffected.

The prior rejection logic for any candidate that depended **only** on absence of complete alternative-space enumeration is no longer sufficient for discard.

This creates a controlled re-screening eligibility class; it does not constitute promotion.

## 4. Candidate routing after correction

### AWS / cloud runbook family

`RETAIN FOR CASE-SPECIFIC SCREENING` remains valid. Screening must focus on the concrete event/unit and pre-action accessibility of the selected transformation, not on exhaustive enumeration of every possible remediation path.

### IT-NOSD-010 — ETSI TS 23.502 / 3GPP 5GS

`ELIGIBLE FOR RE-SCREENING`.

The previous rejection rationale based on inability to establish a complete public alternative space is superseded. A concrete public/reproducible procedure instance must now be sought and assessed under the corrected TR-132 rule.

### ICD-08 — BPI-2017 decision process

`ELIGIBLE FOR RE-SCREENING` because its previous non-retention explicitly relied on incomplete ex-ante alternative-space evidence. Re-screening is not automatic and must test whether the realized transformation and its pre-outcome accessibility can be independently reconstructed.

### ICD-06 / ICD-07

No automatic reopening. Their prior problems included contextual/evolving-state limitations beyond mere alternative-space completeness.

## 5. Current governance state

`CANDIDATE_ADMISSION = NOT YET GRANTED`

`IT-G1 = NOT STARTED`

`EXECUTION_AUTHORIZATION = NONE`

`GOVERNANCE_PATCH_TO_CANONICAL_STATE = NONE`

`SCIENTIFIC_CORE = UNCHANGED`

## 6. Next controlled operation

Re-screen one eligible candidate at a time under the TR-132-corrected criterion, beginning with the candidate that offers the strongest combination of natural unit, state reconstructability, transformation identity and outcome-independent accessibility evidence.
