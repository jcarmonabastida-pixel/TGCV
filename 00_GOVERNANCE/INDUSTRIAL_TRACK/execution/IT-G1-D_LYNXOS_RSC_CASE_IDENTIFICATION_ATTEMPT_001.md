# IT-G1-D — LynxOS-178 RSC Case Identification Attempt 001

**Date:** 2026-09-09  
**Status:** CLOSED — IT-G1 PASS (BOUNDED PUBLIC CASE IDENTIFIED)  
**Candidate:** IT-NOSD-007 — FAA AC 20-148 Reusable Software Components

## 1. Case identified

The documentary closure operation established a bounded public case at the decision-object level: the **initial FAA RSC approval of LynxOS-178 in 2006**, associated with the Rockwell Collins Pro Line Fusion components **Adaptive Flight Display Runtime, Common Computing Runtime, and Data Concentration Module Runtime**. A contemporaneous historical report identifies the FAA AC 20-148 acceptance letter in March 2006, while later technical reporting explicitly states that the initial RSC approval in 2006 covered those three named components. citeturn1search1turn1search3

The exact acceptance-letter document identifier and exact day of FAA issuance were not recovered publicly. However, the IT-G1 criterion requires a bounded decision-time temporal frame, not necessarily a publicly recoverable day-level timestamp. The evidence closes the decision to **calendar year 2006**, with the public announcement of the acceptance dated 20 March 2006 and independent reporting on 23 March 2006. citeturn1search1turn1search0

The later 2012 approval for LynxOS-178 Version 2.2.2 is treated only as corroborative evidence of the same RSC mechanism and is **not used to define the 2006 case**. citeturn1search2turn1search3

## 2. IT-G1 frozen case definition

**Case identity:** Initial FAA AC 20-148 RSC approval of LynxOS-178, 2006.  
**Industrial decision object:** FAA acceptance of reusable software components for subsequent safety-critical avionics certification use.  
**Decision-time window:** Calendar year 2006; public announcement 20 March 2006.  
**Accepted component scope:** Adaptive Flight Display Runtime; Common Computing Runtime; Data Concentration Module Runtime.  
**Technology boundary:** LynxOS-178 RSC, PowerPC-family context as documented in subsequent technical material.  
**Decision mechanism:** FAA AC 20-148 RSC acceptance.  
**Outcome independence:** Case identity is the acceptance decision itself, not later aircraft deployment or certification outcome.

## 3. IT-G1 assessment

| Requirement | Status | Finding |
|---|---|---|
| Concrete industrial decision context | **PASS** | Specific FAA acceptance decision concerning a named safety-critical software component/product family |
| Explicit system boundary | **PASS** | LynxOS-178 RSC and three named Pro Line Fusion runtime components |
| Bounded reproducible unit | **PASS** | One identifiable initial RSC approval episode in 2006 with named accepted components |
| Decision-time temporal frame | **PASS** | Bounded to calendar year 2006; public announcement dated 20 March 2006 |
| Alternatives/constraints independently reconstructable | **PASS** | AC 20-148 predates the case and defines the RSC acceptance mechanism and its certification constraints |
| Outcome-independent case identity | **PASS** | Identity does not depend on later deployment or certification outcomes |

## 4. Closure judgement

**IT-G1-D = PASS — BOUNDED PUBLIC CASE IDENTIFIED.**

The missing day-level FAA acceptance-letter date and document identifier are recorded as documentary limitations, not silently inferred. They do not invalidate IT-G1 because the frozen protocol admits a bounded decision-time window and the case identity is independently anchored to the 2006 approval episode.

Importantly, the later Pro Line Fusion deployment is not used to establish case admissibility. It remains corroborative context only. The case is admitted on the basis of the contemporaneously reported FAA RSC acceptance and its named component scope.

## 5. Routing

**IT-G1 is CLOSED for this candidate.**

The next permissible gate is **IT-G2 — Variable Observability**. IT-G2 must independently determine whether the state/context, accessible transformations or enabling/limiting conditions, and required outcome variables can be observed or reconstructed without changing the frozen IT-G1 case definition.

No industrial execution, utility comparison, causal/value inference, partner/proprietary evidence, dataset execution, Rust/EXT-1.1 execution, O3, Stage-C/D, or Core modification is authorized by this record.
