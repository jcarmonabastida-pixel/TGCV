# DEC-C10-093 — Acceptance of C10-S AB working specialization baseline

**Status:** ACCEPTED WORKING DESIGN BASE — NOT DESIGN FREEZE  
**Date:** 2026-11-09  
**Scope:** C10-S, research branch research/c10-s-consolidation-draft

## 1. Decision

The user accepts the integrated proposal in C10-S master §217 as the working specialization baseline for Package AB, subject to the explicit reservations in §3 below.

This acceptance is intended to stop reopening already settled conceptual choices and to let the remaining AB specification be completed as one coordinated package. It does not convert every proposed material detail into a frozen or empirically validated fact.

## 2. Accepted working baseline

The following are accepted as the working basis, within the scope of existing decisions DEC-C10-068/069 and without modifying them:

1. The synthetic logical service instance already identified by DEC-C10-069 remains the reference instance: contract C10S-SVC-REQUEST-PROCESSOR v1.0.0, instance C10S-SVC-REQUEST-PROCESSOR-001 rev. 1, CMP anchor CMP-SERVICE-LOGIC-001.
2. The constitutive functional nucleus is the two accepted parameters PAR-SVC-ENABLED and PAR-SVC-PROFILE and the accepted REQUIRE rule from DEC-C10-068. The proposed base and adversarial truth states in §217.2 may be used as candidate stipulated DGP cases, not as empirical observations or prevalence assumptions.
3. C10-S will specify both the focal path F1/F2 and the baseline alternative path A1/A2 against one common non-compensatory functional acceptance criterion F*.
4. The semantic source/destination/mapping proposal in §217.3 is the working mapping candidate. The proposed ENUM correspondence is total and injective at the semantic level; physical serialization, AST representation and canonicalization remain open.
5. B remains a technical provisioning intervention under D2 and is not the actor that transforms, applies or functionally validates the configuration. ARCH-B1 remains a candidate architecture, not an approved implementation.
6. FP-01…FP-07 remain the proposed functional acceptance profile; FP-08 remains a separate evidence/provenance gate. No compensatory averaging is introduced.
7. The AB-01…AB-09 closure work is to be completed as one integrated specification package on this baseline, rather than through repeated standalone conceptual audits.

## 3. Explicit reservations — remain OPEN

This decision does not decide or freeze:

- whether the two rule operand bindings are separate REF records or represented solely in the approved AST/grammar;
- the physical C_src/C_dst/M namespaces, serialization, AST syntax, canonicalization or hashes;
- final IAM roster and snapshot-scoped coverage/cardinality;
- final FP-05 security profile and its operational evidence;
- the material scope of G and complete C0 contents;
- the common temporal horizon H;
- the D2 operational probability model: receipt, compliance, attempt, partial failure, retry, rollback, background provision and crossover;
- the joint distribution of installation, integrity, compatibility and operability; no s=.80 or historical .20/.80 is approved;
- MD-C1/MD-C4 isolation and non-affectation of A1/A2;
- population eligibility, q_X*, positivity, unit, support and interference;
- the independent oracle, blinding, adjudication procedure and truth/observed separation;
- statistical identification, power, sensitivity, sample size or any Value conclusion.

These are not reasons to reopen the accepted baseline. They are material specifications to resolve within the remaining AB package, or to transfer to the appropriate subsequent package where explicitly designated.

## 4. Governance and implementation boundary

This is a working-design acceptance, not Design Freeze, not an implementation contract, and not authorization to generate executable fixtures, code, validators, parsers, simulations or experiments.

scientific_execution=false; execution_authorized=false.

The work remains on the research branch. No change to main and no PR promotion is authorized.

## 5. Traceability

- Accepted proposal: 00_GOVERNANCE/SIP/C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md, §217.
- Closure plan: 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_004.md, §16.95.
- Closure control: 00_GOVERNANCE/SIP/C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md, §113.
- Governing prior decisions: DEC-C10-068 and DEC-C10-069, whose explicit exclusions remain in force except where this decision accepts a working design baseline without claiming freeze or implementation.
