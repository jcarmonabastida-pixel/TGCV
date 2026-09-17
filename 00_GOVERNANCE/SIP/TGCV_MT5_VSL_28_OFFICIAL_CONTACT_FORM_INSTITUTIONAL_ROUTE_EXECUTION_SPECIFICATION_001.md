# TGCV — MT5-VSL-28 Official Contact-Form / Institutional Route Execution Specification 001

**Date:** 2026-09-17  
**Status:** `FROZEN ROUTE SPECIFICATION — NO MESSAGE SUBMITTED`

## 1. Purpose

Define a controlled way to execute MT5-VSL-22 first contact when a current direct personal email is unavailable, using only an official institutional contact form or official enquiry mechanism.

This step resolves an operational channel only. It does not qualify a partner or study context.

## 2. Current route basis

The current MSCA official contact page explicitly directs prospective applicants and participating organizations to MSCA National Contact Points for country-specific help and to the Research Enquiry Service for future/current fellows, universities, research organizations, public institutions and businesses. citeturn0search5

EURAXESS also maintains current national/contact-point infrastructure and country resources for Spain. citeturn0search0turn0search1

For ECOBAS, the current USC research portal identifies ECOBAS as an active inter-university research centre and exposes an official `Contactar` route. citeturn0search11turn0search18

These routes establish legitimate institutional channels, not recipient willingness or scientific qualification.

## 3. Route priority

### R28-1 — MSCA / Spain NCP or Research Enquiry Service

**Target:** T21-06.

**Route:** official MSCA contact/NCP mechanism.

**Purpose:** ask whether a concrete doctoral/applied-research context or partner network can host a prospective TGCV-compatible measurement deployment.

**Message:** Variant D from MT5-VSL-22, with only recipient-specific institutional wording permitted.

**Required record:** exact route used, URL, timestamp, submitted text version/hash, acknowledgement if any.

### R28-2 — ECOBAS official Contactar route

**Target:** T21-04.

**Route:** official USC/ECOBAS `Contactar` mechanism.

**Purpose:** identify whether an existing or planned prospective applied study could support the seven-question screening.

**Message:** Variant A from MT5-VSL-22.

**Required record:** exact official route, timestamp, submitted text version/hash, acknowledgement if any.

### R28-3 — CFPB Project Catalyst

**Target:** T21-01.

**Route:** only a current CFPB official enquiry mechanism if its present page explicitly accepts Project Catalyst/research-collaboration enquiries.

The historical Project Catalyst email remains excluded from automatic execution because current status was not independently confirmed.

### R28-4 — European Commission financial-literacy programme

**Target:** T21-05.

**Route:** only the current official programme enquiry/contact mechanism explicitly applicable to stakeholder/research enquiries.

Do not redirect the message to an unrelated DG FISMA unit merely because its published email is current.

## 4. Submission controls

Before submitting any message, freeze:

1. target ID;
2. route ID;
3. official destination URL or mechanism;
4. message variant/version;
5. recipient-specific substitutions;
6. submission timestamp;
7. sender identity;
8. attachment list;
9. confirmation/acknowledgement identifier, if supplied.

No message is considered sent merely because an official contact page exists.

## 5. Message integrity

The submitted content must remain within MT5-VSL-22.

Allowed substitutions:

- recipient/institution name;
- route-specific salutation;
- factual context about the target, if documented.

No additions may:

- claim TGCV validation;
- imply an existing partnership;
- promise causal results;
- request participant data;
- alter the Value specification;
- alter the C1–C12 criteria.

## 6. Response handling

Any acknowledgement is recorded separately from substantive response.

Response classes remain those frozen in MT5-VSL-23:

- R0 No response
- R1 Declines/incompatible
- R2 General interest
- R3 Potential context
- R4 Evidence-bearing context
- R5 Qualified context

An acknowledgement alone cannot move a target beyond `OPPORTUNITY ONLY`.

## 7. Provenance record

For every submitted contact-form message preserve:

- official destination URL;
- route ID;
- date/time;
- exact message version/hash;
- exact submitted text;
- confirmation/reference number where provided;
- any response;
- subsequent C1–C12 evidence separately.

Do not place participant-sensitive information into the route log.

## 8. Fail-closed rules

Stop before submission if:

- route purpose is ambiguous;
- destination is not official/current;
- message requires unverified recipient identity;
- form requests data that cannot be lawfully/appropriately supplied at this stage;
- message would need substantive modification to fit the route;
- submission would imply partner selection or scientific validation.

## 9. Execution status

MT5-VSL-28 defines the route but does **not** itself submit any message.

Current status:

- MT5-VSL-21 target list: CLOSED;
- MT5-VSL-22 outreach package: FROZEN;
- MT5-VSL-23 execution protocol: FROZEN;
- MT5-VSL-24 initial batch: BLOCKED / NOT SENT;
- MT5-VSL-25 endpoint resolution: CLOSED;
- MT5-VSL-26 verification: CLOSED;
- MT5-VSL-27 direct-contact resolution: CLOSED;
- MT5-VSL-28 institutional route specification: FROZEN;
- actual outbound submission: **NOT RECORDED**.

## 10. Governance boundary

No recruitment, intervention, Value measurement, causal estimation, or modification of TGCV Core/RMA/Evidence→Claim Matrix/STATUS/C09/M9 is authorized.

## 11. Decision

**`MT5-VSL-28 — FROZEN ROUTE SPECIFICATION — NO MESSAGE SUBMITTED.`**

## 12. Next authorized movement

**MT5-VSL-29 — Institutional Contact-Form Execution Record:** execute one bounded institutional route, beginning with the highest-relevance current official route, and record the exact submission or a fail-closed inability to submit. No scientific qualification follows from submission itself.