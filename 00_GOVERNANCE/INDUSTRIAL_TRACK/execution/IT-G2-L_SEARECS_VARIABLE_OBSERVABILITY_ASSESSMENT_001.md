# IT-G2-L — Searecs / BG Verkehr Variable Observability Assessment 001

**Date:** 2026-09-10  
**Status:** CLOSED — IT-G2 HOLD / NOT CLOSED  
**Case:** `IT-G1-L-SEARECS-BGVERKEHR-2022-02-02`  
**Gate:** IT-G2 — Variable Observability

## 1. Purpose

Assess whether the frozen Searecs product-approval case has sufficient public evidence to observe or reconstruct the decision-time variables required for Industrial Track analysis, without using later outcomes to fill missing decision-time information.

## 2. Evidence boundary

Frozen public evidence consists of the German Flag/BG Verkehr approval list and contemporaneous German Flag announcement, supplemented only for cross-checking product identity and technical scope by public MARSIG material and later public approval material. Later approvals are not treated as decision-time evidence for the 2022 German approval.

## 3. Variable assessment

| Variable class | Status | Finding |
|---|---|---|
| Case / decision identity | **PASS** | Product Searecs, manufacturer MARSIG, approving authority BG Verkehr/Ship Safety Division and approval date 02.02.2022 are independently identifiable. |
| Normative context | **PASS** | German Flag explicitly identifies ISO 21745 and IMO MEPC.312(74) as the technical basis; MARSIG also identifies ISO 21745:2019 and MEPC.312(74). |
| Product / system boundary | **PASS** | Electronic record-book product and approved record-book categories are publicly bounded. |
| Decision-time product version/configuration | **PARTIAL** | Public German Flag material identifies the product but does not expose a complete version/configuration identifier for the 02.02.2022 decision. A later Liberian approval identifies Searecs Version 2.2.x.y, but this cannot be retroactively assigned to the German decision. |
| Technical state at decision time | **PARTIAL** | Public sources establish that technical verification occurred and identify the standards used, but do not expose the complete 2022 conformance/test package, configuration baseline, verification measurements or acceptance evidence. |
| Accessible transformations / admissible configurations | **PARTIAL** | Public approval scope establishes which record-book functions/categories were admissible, but does not provide a complete decision-time configuration space or all conditional alternatives available within the approved product. |
| Enabling conditions | **PARTIAL** | Public sources establish German-flagged sea-going ships as the use context and identify technical verification, but do not expose the complete installation, training, onboard documentation and technical acceptance conditions for the 2022 product approval. |
| Limiting conditions / restrictions | **PARTIAL** | Public scope and the distinction between product approval and ship-specific approval are clear, but the complete restriction/condition set in the underlying approval file is not public. |
| Subsequent outcomes | **NOT USED** | Later use, flag-state approvals and deployments are excluded from reconstruction of the 2022 decision-time variables. |

## 4. Critical finding

The case remains strongly identifiable, but public evidence does **not** close the decision-time variable layer required to reconstruct a sufficiently complete `S/C/T_acc` representation for Industrial Track purposes.

In particular, the missing product-version/configuration baseline and the inaccessible underlying technical verification/acceptance package prevent a defensible claim that the complete set of admissible transformations and their enabling/limiting conditions can be reconstructed independently from the public record.

The later public Liberian approval provides an explicit example of a versioned Searecs decision (Version 2.2.x.y), but it is a different authority, date and decision episode and therefore cannot be used to fill the German 2022 decision-time state.

## 5. Decision

**IT-G2-L = HOLD / NOT CLOSED.**

The case does not fail because the product approval is unidentifiable. Rather, G2 cannot be closed because the publicly recoverable decision-time variable set is incomplete.

No G3 accessibility closure is entered for this case.

## 6. Routing

The Searecs case is retained as a bounded documentary candidate with **G1 PASS / G2 HOLD**.

Further work would require a separately governed public evidence source that exposes the missing decision-time technical/configuration variables, or another admissible case with stronger public observability. The present record must not be repeatedly mined without new evidence.

No industrial execution, utility comparison, causal/value inference, partner/proprietary evidence, new dataset execution, Rust/EXT-1.1 execution, O3, Stage-C/D, or Core modification is authorized by this record.

## 7. Evidence references

- Deutsche Flagge/BG Verkehr, “Record books”: Searecs, MARSIG, approved scope and approval date 02.02.2022.
- Deutsche Flagge/BG Verkehr, “German Flag issues approvals for electronic record books”: approval authority, technical-verification arrangement, normative basis and distinction between product-level and ship-specific approvals.
- MARSIG public Searecs material: product modules and compliance standards.
- MARSIG 2022 public approval notice: BSH approval/testing and ISO 21745 basis.
- Later Liberia Maritime Authority approval: explicit Searecs Version 2.2.x.y, used only as a demonstration that versioned approval evidence exists in another later episode; not used to reconstruct the 2022 German case.
