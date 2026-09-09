# IT-G2 — LynxOS-178 RSC Variable Observability Assessment 001

**Date:** 2026-09-09  
**Status:** CLOSED — IT-G2 HOLD / NOT CLOSED  
**Candidate:** IT-NOSD-007 — FAA AC 20-148 / LynxOS-178 initial RSC case (2006)  
**Precondition:** IT-G1 PASS — bounded public case identified

## 1. Purpose

Assess whether the variables required for the next industrial-track stages can be observed or independently reconstructed for the frozen IT-G1 case, without changing the case identity and without using post-outcome information to define admissibility.

This is an observability assessment only. It is not an industrial experiment, utility test, causal analysis, value analysis, or validation of TGCV Core.

## 2. Frozen case

- **Decision:** initial FAA AC 20-148 RSC acceptance of LynxOS-178 in 2006.
- **Decision-time window:** calendar year 2006.
- **Accepted scope:** Adaptive Flight Display Runtime, Common Computing Runtime, Data Concentration Module Runtime.
- **Mechanism:** FAA AC 20-148 RSC acceptance.
- **Case identity:** the acceptance decision itself, independent of subsequent deployment/certification outcomes.

AC 20-148 defines an RSC as software together with supporting DO-178B life-cycle data and documentation considered for reuse, and distinguishes the RSC developer, RSC user, target computer/environment, software characteristics, and subsequent use. citeturn0search28turn0search0

## 3. Required observability domains

| Variable domain | Status | Evidence / limitation |
|---|---|---|
| Decision identity | **PASS** | Named LynxOS-178 RSC acceptance episode is publicly documented. |
| Decision-time normative context | **PASS** | AC 20-148 is publicly available and dated 2004-12-07; its RSC definitions and acceptance mechanism are explicit. citeturn0search0turn0search28 |
| Accepted component/product scope | **PASS** | Public reporting identifies the three initial Rockwell Collins runtime components. citeturn1search0turn1search2 |
| Technical state/context at decision time | **PARTIAL** | Public sources expose some architecture constraints: DO-178B Level A, ARINC 653, POSIX, partitioning, target processor family, and software-artifact structure. They do not expose the complete FAA acceptance basis, configuration data, margins, verification evidence, or integration context. citeturn0search25turn0search6turn0search28 |
| Accessible transformations / admissible reuse configurations | **PARTIAL** | AC 20-148 defines reusable-component acceptance and subsequent-use concepts; public technical material describes reuse across projects/platforms. However, the complete set of admissible configurations and constraints for the 2006 accepted component is not publicly reconstructable. citeturn0search28turn0search6 |
| Enabling / limiting conditions | **PARTIAL** | Public documentation identifies hardware families, partitioning, interfaces and certification-artifact conditions, but detailed acceptance constraints and configuration-specific conditions are incomplete. citeturn0search25turn0search10 |
| Subsequent realized uses | **PASS as documentary outcome context** | Public records identify later Pro Line Fusion deployment and certification contexts. These are retained only as outcome/context evidence, not as case-admission inputs. citeturn1search0turn1search6 |
| Outcome quality / utility | **NOT ESTABLISHED** | Public claims describe reduced time/cost/risk, but no independently frozen comparator and no auditable quantitative utility protocol are available from the current evidence. citeturn0search6turn1search0 |

## 4. Critical observability gap

The decisive limitation is not identification of the RSC itself. The limitation is reconstruction of the **decision-time transformational space** at sufficient granularity.

The public record establishes that AC 20-148 acceptance creates a reusable certification asset and that LynxOS-178 was accepted for named components. It does not provide the complete acceptance-basis data needed to enumerate, at decision time, all admissible configurations and their enabling/limiting conditions.

Therefore it would be methodologically unsafe to infer `T_acc` from later deployments, from marketing claims, or from the fact that the software was subsequently used on particular aircraft/platforms.

## 5. IT-G2 decision

**IT-G2 = HOLD / NOT CLOSED.**

The case passes documentary observability for identity, normative mechanism and broad component scope, but fails to close the full variable-observability requirement needed for a defensible industrial reconstruction of `S`, `T_acc` and the relevant enabling/limiting conditions.

This is **not a failure of the LynxOS-178 case at IT-G1**. IT-G1 remains PASS. It is a boundary on what can presently be reconstructed from public evidence.

## 6. Routing

No IT-G3, IT-G4 or IT-G5 entry is authorized for this case on the basis of the present evidence.

A future narrow operation may seek independent technical/certification evidence capable of closing the missing decision-time variables. Such evidence must be pre-existing and outcome-independent; it may not redefine the frozen IT-G1 case retrospectively.

No industrial execution, utility comparison, causal/value inference, proprietary/partner evidence, new dataset execution, Rust/EXT-1.1 execution, O3, Stage-C/D, or Core modification is authorized.
