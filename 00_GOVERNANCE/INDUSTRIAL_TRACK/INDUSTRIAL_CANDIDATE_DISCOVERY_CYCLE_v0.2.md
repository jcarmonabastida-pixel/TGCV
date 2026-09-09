# TGCV — Industrial Candidate Discovery Cycle v0.2

**Date:** 2026-09-09  
**Status:** CURRENT / OPERATIVE — DOCUMENTARY DISCOVERY ONLY  
**Execution:** NOT AUTHORIZED  
**Origin:** EXT-UPD-4.9 Industrial Candidate Discovery Protocol v0.1

## Purpose

After ICD-01 and ICD-02 both failed IT-G1 on decision-time accessibility closure, this cycle tests whether documentary sources reveal a naturally bounded industrial candidate in which the accessible alternative set is independently specified rather than inferred from realized events.

The cycle does not execute datasets and does not admit a candidate to IT-G1. It applies the existing filters without relaxation.

## Search result

### ICD-06 — Road Traffic Fine Management

**Disposition: DISCARD at documentary screening.**

The documented real-life process from an Italian municipal police information system has a clear case unit and a normative process description, including an explicit choice between Payment and Send Fine. However, the published decision-mining analysis states that under the same observed condition (e.g. unpaid status) the choice may depend on an unavailable contextual factor. Therefore the normative process identifies alternatives but does not independently close the actual decision-time accessibility/admissibility conditions for every case.

This fails the mandatory accessibility filter. It is not retained for IT-G1.

### ICD-07 — Hospital Sepsis pathway

**Disposition: DISCARD at documentary screening.**

The public event log provides patient pathways, timestamps and clinical attributes, and is naturally case-bounded. However, clinical pathway branching is conditioned on evolving patient state and clinical judgement; the documentary sources do not provide an ex-ante, independently complete specification of all admissible alternative transformations at each decision time. The accessibility criterion therefore remains open.

This fails the mandatory accessibility filter. It is not retained for IT-G1.

### ICD-08 — BPI-2017 loan-application decision process

**Disposition: CONDITIONAL / NOT RETAINED.**

The BPI-2017 log contains substantial activity data and has been used for decision-model discovery. This supports analysis of observed decision structure, but documentary evidence reviewed in this cycle does not independently establish the complete ex-ante alternative set and admissibility conditions at each decision point. The candidate therefore cannot be promoted merely because decision-mining methods can infer rules from observed traces.

It remains a possible future discovery target only if an external normative decision specification can be identified independently of the event outcomes.

## Cycle conclusion

No new candidate satisfies all mandatory documentary filters sufficiently to justify retention for IT-G1.

The discovery problem has therefore become explicit:

> Public event logs can identify realized transformations and often support inferred decision models, but the present candidate pool does not provide an independently grounded ex-ante accessibility specification.

This is an evidence-availability result, not evidence that industrial accessibility is impossible in general.

## Governance consequence

- ICD-01: IT-G1 FAIL / NOT ADMITTED.
- ICD-02: IT-G1 FAIL / NOT ADMITTED.
- ICD-06: DISCARD at screening.
- ICD-07: DISCARD at screening.
- ICD-08: CONDITIONAL / NOT RETAINED.
- No candidate admitted to IT-G2.
- No dataset execution authorized.
- No partner evidential engagement authorized.
- No utility, causal or value assessment authorized.
- Scientific Core unchanged.
- C01–C16 unchanged.

## Non-retroactivity

No criterion was relaxed following the failures of ICD-01 or ICD-02. The accessibility requirement remains identical to the frozen Industrial Candidate Discovery Protocol.

## Next controlled decision

The Industrial Track has no currently admissible documentary candidate. Any continuation should therefore be a separately authorized discovery route that specifically searches for **normative or operational specifications of admissible alternatives**, not another generic event-log search.
