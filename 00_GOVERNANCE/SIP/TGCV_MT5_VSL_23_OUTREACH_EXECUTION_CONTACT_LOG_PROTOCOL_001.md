# TGCV — MT5-VSL-23 Outreach Execution / Contact Log Protocol 001

**Date:** 2026-09-17  
**Status:** `FROZEN PROTOCOL — OUTREACH EXECUTION NOT YET RECORDED`

## 1. Purpose

Define the controlled procedure for executing MT5-VSL-22 first contacts and recording responses without converting interest, silence or preliminary discussion into scientific evidence.

The protocol governs only **context acquisition**. It does not execute a study, recruit participants, collect Value data or modify TGCV constructs.

## 2. Governing documents

- MT5-VSL-18 — Context Acquisition Specification / External Partner Target Definition
- MT5-VSL-20 — Context Acquisition Outreach Specification
- MT5-VSL-21 — Candidate Outreach Target List
- MT5-VSL-22 — First-Contact Outreach Package

## 3. Scientific boundary

The intended prospective architecture remains:

`system transformation → independently reconstructed ΔT_acc → subsequent trajectory → frozen external VSL → individual V*`

Outreach must not alter this architecture.

A recipient's agreement to discuss a study is not evidence for any TGCV claim.

## 4. Outreach unit

Each first contact receives a unique immutable identifier:

`MT5-VSL-23-[TARGET]-[DATE]-[SEQ]`

Required metadata:

- target identifier from MT5-VSL-21;
- organization/programme;
- contact role;
- contact channel;
- sender;
- date/time sent;
- outreach variant A/B/C/D;
- exact message version/hash;
- attachments, if any;
- response status;
- follow-up status.

No sensitive participant information is entered into this log.

## 5. Execution rule

Only the frozen MT5-VSL-22 text may be used for first contact unless a new version is explicitly created and frozen.

Permitted operational substitutions:

- recipient name;
- organization/programme name;
- contact-specific factual context that is independently documented;
- contact channel metadata.

Not permitted:

- adding claims about TGCV validity;
- promising causal findings;
- implying a partner has been selected;
- requesting participant data at first contact;
- selecting a Value endpoint because of expected treatment effects;
- changing the measurement specification informally during contact.

## 6. Response classes

### R0 — No response

No response after the predefined follow-up window.

**Scientific disposition:** no evidence of context qualification.

### R1 — Declines / incompatible

Recipient explicitly indicates that required prospective conditions cannot be met.

**Disposition:** `INCOMPATIBLE` if the incompatibility maps to a C1–C12 no-go condition; otherwise retain as `OPPORTUNITY ONLY` with reason recorded.

### R2 — General interest

Recipient expresses interest but supplies no concrete study/context evidence.

**Disposition:** `OPPORTUNITY ONLY`.

### R3 — Potential context

Recipient identifies a named programme/study and supplies partial C1–C12 information.

**Disposition:** `CONDITIONAL CONTEXT`; initiate controlled context audit.

### R4 — Evidence-bearing context

Recipient supplies documentary or formally confirmed evidence sufficient to assess C1–C12.

**Disposition:** perform candidate-context audit; do not automatically classify as qualified.

### R5 — Qualified context

All mandatory C1–C12 conditions are independently evidenced and the context can support a frozen material package.

**Disposition:** `QUALIFIED CONTEXT`; authorize the next methodological gate only through a new artifact.

## 7. Anti-coaching rule

The first contact must not teach the recipient how to satisfy C1–C12 by retrofitting an existing study after observing results.

If clarification is requested, provide only the frozen methodological boundary and ask for the context as it already exists or is prospectively planned.

Any substantive design change requested by the recipient is recorded as a proposed change, not silently incorporated.

## 8. Anti-selection rule

Do not select a target for advancement because it reports attractive outcomes, strong treatment effects, successful programme results or apparent TGCV compatibility.

Qualification is based on structural/methodological conditions:

- prospective timing;
- individual respondent unit;
- independently specified transformation;
- independently reconstructible `ΔT_acc`;
- frozen external VSL;
- item-level Value measurement;
- reproducibility;
- ethics/privacy/data governance.

## 9. Provenance rule

For every substantive response, preserve:

1. original received message/document;
2. date/time;
3. sender role and organization;
4. exact source location or attachment identifier where available;
5. extracted C1–C12 facts;
6. interpretation performed by TGCV;
7. unresolved items;
8. classification;
9. next authorized action.

Do not paraphrase away uncertainty. Distinguish explicitly between:

- documented fact;
- recipient assertion;
- TGCV interpretation;
- unresolved condition.

## 10. Contact log schema

| Field | Required | Rule |
|---|---|---|
| Contact ID | YES | immutable |
| Target ID | YES | MT5-VSL-21 identifier |
| Organization | YES | as documented |
| Role | YES | contact role only |
| Channel | YES | email/form/other |
| Date/time sent | YES | recorded at execution |
| Message version | YES | MT5-VSL-22 or later frozen version |
| Response date | CONDITIONAL | if response received |
| Response class | YES | R0–R5 |
| C1–C12 evidence | CONDITIONAL | only when supplied |
| Source/provenance | CONDITIONAL | required for substantive response |
| Qualification class | YES | opportunity/conditional/qualified/incompatible |
| Next action | YES | governed action only |
| Notes | YES | no participant-sensitive data |

## 11. Candidate admission gate

A responding context cannot become `QUALIFIED CONTEXT` merely through email discussion.

Before admission, independently verify:

- **C1** named prospective study;
- **C2** individual participants and recruitment frame;
- **C3** language, instrument and administration context;
- **C4** concrete system/service transformation;
- **C5** independent accessibility specification;
- **C6** prospective item-level Value measurement;
- **C7** frozen temporal structure;
- **C8** VSL independence from treatment results;
- **C9** data access and reproducibility;
- **C10** ethics/privacy/legal basis;
- **C11** independent executor;
- **C12** pre-analysis separation.

Any unresolved mandatory condition prevents `QUALIFIED CONTEXT` status.

## 12. Follow-up rule

One controlled follow-up may be sent after a reasonable interval if the recipient has not responded, using a short version of the same request.

A follow-up must not introduce new scientific claims or pressure the recipient to provide a positive answer.

Further contact is permitted only where there is a substantive response or an explicit invitation to continue.

## 13. Confidentiality and data minimization

First-contact activity must use the minimum information necessary to determine whether a prospective context exists.

Do not collect:

- participant names or identifiers;
- health information;
- financial account information;
- confidential business information;
- raw outcome data;
- treatment-effect estimates.

If a recipient voluntarily sends sensitive information, do not copy it into the governance log. Record only that sensitive material was received and route it through the applicable secure data-access process before any scientific use.

## 14. Version control

Every sent message must be reproducible from:

`Target ID + contact ID + frozen message version + recipient-specific substitutions + timestamp`.

If the outreach text changes substantively, create and freeze a new version before use.

## 15. Outreach execution status

At protocol creation:

- MT5-VSL-21 target list: CLOSED;
- MT5-VSL-22 message package: FROZEN;
- MT5-VSL-23 protocol: FROZEN;
- actual outreach execution: **NOT RECORDED IN THIS ARTIFACT**;
- qualified deployment context: NONE;
- pilot recruitment: NOT AUTHORIZED;
- Value measurement: NOT EXECUTED.

## 16. Governance boundary

This protocol does not authorize:

- participant recruitment;
- intervention deployment;
- pilot measurement;
- retrospective CFPB scoring;
- household-level CFPB aggregation;
- causal estimation of `ΔT_acc → ΔV*`;
- modification of `T_acc`;
- modification of TGCV Core;
- RMA/Evidence→Claim Matrix/STATUS/C09/M9 changes.

## 17. Decision

**`MT5-VSL-23 — FROZEN PROTOCOL — OUTREACH EXECUTION NOT YET RECORDED.`**

The protocol establishes a controlled path from first contact to candidate-context qualification while preserving the fail-closed scientific boundary.

## 18. Next authorized movement

**MT5-VSL-24 — Outreach Execution Record / Initial Contact Batch:** execute and record a bounded first-contact batch from the MT5-VSL-21 target list, using the frozen MT5-VSL-22 messages and this protocol. No candidate becomes qualified without the C1–C12 audit.
