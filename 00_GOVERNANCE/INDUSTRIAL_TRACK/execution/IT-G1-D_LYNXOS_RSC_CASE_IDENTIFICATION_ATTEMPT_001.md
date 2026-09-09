# IT-G1-D — LynxOS-178 RSC Case Identification Attempt 001

**Date:** 2026-09-09  
**Status:** CLOSED — BOUNDED DOCUMENTARY IDENTIFICATION ATTEMPT  
**Candidate:** IT-NOSD-007 — FAA AC 20-148 Reusable Software Components

## 1. Case located

A substantially stronger public case has been identified than in the previous attempts: FAA approval of **LynxOS-178 as a Reusable Software Component (RSC)**.

FAA AC 20-148 defines the RSC mechanism as an acceptable means by which a reusable software component can obtain FAA acceptance and reuse credit in subsequent certification projects. citeturn0search2turn0search36

Public historical reporting identifies LynuxWorks as the first embedded-OS vendor to receive an AC 20-148 acceptance letter from FAA for LynxOS-178 in March 2006. citeturn2search13turn3search2

A later public record identifies a specific second RSC approval for **LynxOS-178 Version 2.2.2**, dated 12 March 2012, and states that the RSC approval applied to the PowerPC family and could support reuse in avionics certification projects. citeturn2search0turn2search12

Public material also links the RSC to concrete Rockwell Collins Pro Line Fusion components: Adaptive Flight Display Runtime, Common Computing Runtime, Data Concentration Module Runtime and Synthetic Vision Module Runtime. citeturn2search8turn3search9

## 2. IT-G1 assessment

| Requirement | Status | Finding |
|---|---|---|
| Concrete industrial decision context | **PASS** | Specific FAA RSC approval of a named safety-critical software component/product family |
| Explicit system boundary | **PASS / bounded** | LynxOS-178 RSC, defined component scope, PowerPC family; public material identifies concrete avionics runtimes in Pro Line Fusion |
| Bounded reproducible unit | **PASS at product-case level** | Named product/version and RSC approval episode; second approval explicitly identifies Version 2.2.2 |
| Decision-time temporal frame | **PARTIAL** | 12 March 2012 is the public announcement date of the second approval, but the exact FAA acceptance-letter date is not independently established in the sources located |
| Alternatives/constraints independently reconstructable | **PASS** | AC 20-148 provides the pre-existing RSC acceptance mechanism and constraints; the approval is not defined from its later deployment outcome |
| Outcome-independent case identity | **PASS** | Case identity is the FAA RSC approval itself, not a success/failure outcome of later aircraft deployment |

## 3. Critical limitation

This is the first candidate in the current sequence that closes the **industrial decision object** and a reproducible product-level unit strongly enough to justify further work. However, the exact decision date of the FAA acceptance letter must be distinguished from the date of the public announcement.

The evidence therefore does **not yet justify unconditional IT-G1 PASS**.

The case should not be reconstructed from the later Pro Line Fusion deployment. The deployment is corroborative context only; it must not define the identity or admissibility of the RSC approval case.

## 4. Decision

**IT-G1-D = PROVISIONAL CANDIDATE — DATE-CLOSURE REQUIRED.**

This is materially stronger than the FAA AMOC, ERA and AESA cases because the decision object itself is publicly identified: a specific FAA RSC approval for a named software component/product family, with public documentation of the governing mechanism and subsequent public references to the accepted component.

Formal IT-G1 remains **HOLD / NOT CLOSED** pending independent closure of the decision-time identifier/date and confirmation that the exact acceptance record can be reconstructed without relying on post-decision deployment evidence.

## 5. Next operation

Perform one narrow documentary closure operation on the LynxOS-178 RSC case:

1. identify the exact FAA acceptance-letter/document identifier if publicly recoverable;
2. establish the exact effective/decision date separately from the press-release date;
3. freeze the accepted product/version and component scope at that date;
4. freeze AC 20-148 as the decision-time normative mechanism;
5. verify that no post-outcome deployment fact is required to establish admissibility.

If these fields close, IT-G1 can be formally re-evaluated. If the acceptance record/date remains unrecoverable, this candidate will remain provisional rather than being upgraded by inference.

No IT-G2, industrial execution, utility, causal/value analysis, partner/proprietary evidence, or Core modification is authorized.
