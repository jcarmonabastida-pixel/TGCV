# TGCV — Industrial Candidate Discovery Cycle v0.3

**Date:** 2026-09-11  
**Status:** CURRENT / OPERATIVE — DOCUMENTARY DISCOVERY ONLY  
**Supersedes:** `INDUSTRIAL_CANDIDATE_DISCOVERY_CYCLE_v0.2.md`  
**Normative dependency:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.2.md`; TR-132-MOD-1

## Purpose

Provide the current discovery-cycle framework after TR-132-MOD-1. Historical candidate outcomes remain immutable; this version corrects the screening criterion for future discovery.

## TR-132 propagation rule

The cycle **must not require complete ex-ante enumeration of the accessible transformation structure** as a prerequisite for candidate retention.

The relevant question is whether a concrete candidate transformation `τ_i` can be identified and its accessibility/admissibility assessed from pre-outcome `S_t,C_t`, independently of the subsequent outcome, with sufficient reconstruction of the resulting state transition.

Therefore:

- partial or unknown `T_acc(S_t)` is permissible;
- observed-transformation accessibility is the operative screening question;
- accessibility inferred from outcome remains invalid;
- transformation identity, temporal closure, evidence independence and downstream separation remain mandatory.

## Historical results

The results recorded in Cycle v0.2 are preserved as historical evidence. They are **not reclassified automatically** by this document. In particular, ICD-06, ICD-07 and ICD-08 are not silently reopened or promoted by this framework change.

The correction applies to future screening and to explicitly authorized re-screening of a candidate whose prior disposition depended materially on the now-superseded completeness requirement.

## Current discovery rule

For each new candidate, record:

1. natural unit and boundary;
2. pre-outcome state/context;
3. candidate transformation `τ_i`;
4. evidence supporting its accessibility/admissibility under that state/context;
5. whether alternative-space knowledge is complete, partial or unknown;
6. why any incompleteness does or does not affect the proposed test;
7. downstream outcome separation.

**A candidate must not be discarded solely because item 5 is partial or unknown.**

## Governance consequence

- No candidate is admitted by this update.
- No dataset execution is authorized.
- No industrial execution is authorized.
- No utility, causal or value assessment is authorized.
- Scientific Core remains unchanged.

## Next controlled decision

Re-screen, only where warranted, candidates previously rejected specifically because complete ex-ante alternative-space enumeration was treated as mandatory. Do not reopen candidates rejected for independent reasons.
