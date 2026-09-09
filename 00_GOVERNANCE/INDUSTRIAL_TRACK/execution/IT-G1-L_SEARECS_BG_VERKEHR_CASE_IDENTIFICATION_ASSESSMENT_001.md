# IT-G1-L — Searecs / BG Verkehr Case Identification Assessment 001

**Date:** 2026-09-10  
**Status:** CLOSED — IT-G1 PASS (BOUNDED PUBLIC CASE IDENTIFIED)  
**Candidate:** `IT-NOSD-009` — ISO 21745:2019 / electronic record books  
**Gate:** IT-G1 — Case Identifiability

## 1. Purpose

Determine whether one concrete, outcome-independent industrial decision episode can be frozen from public evidence under the existing IT-G1 criteria, without treating the normative specification itself as the decision episode.

## 2. Frozen case

**Case ID:** `IT-G1-L-SEARECS-BGVERKEHR-2022-02-02`

**Decision object:** Product-level approval by BG Verkehr / Ship Safety Division of the electronic record-book software **Searecs**, manufactured by MARSIG, Rostock, for use on sea-going ships flying the German Flag.

**Decision date:** 2022-02-02.

**Approval scope publicly listed:** ship's logbook; engine logbook; MARPOL record book (MARPOL Annexes I, II, V, VI and NOx Technical Code); ballast water record book.

**Technical verification context:** BSH or a recognized organization performs the technical verification; the approval is issued by BG Verkehr / Ship Safety Division.

**Normative context:** ISO 21745:2019 and IMO Resolution MEPC.312(74), as identified by the German Flag's contemporaneous public announcement. The German Flag explicitly states that it relied on these international technical specifications rather than special German requirements.

## 3. IT-G1 assessment

| Requirement | Status | Finding |
|---|---|---|
| Concrete industrial decision context | **PASS** | A named maritime software product received a dated approval from a named competent authority. |
| Explicit system boundary | **PASS** | Product-level electronic record-book software Searecs and its publicly listed record-book scope are bounded. |
| Bounded reproducible unit | **PASS** | One approval episode, identifiable by product, manufacturer, authority and approval date. |
| Decision-time temporal frame | **PASS** | Approval date is explicitly listed as 02.02.2022. |
| Applicable normative version/context | **PASS** | ISO 21745:2019 was published in 2019 and is explicitly identified by the approving authority's public explanation; the IMO resolution is also identified. |
| Decision unit | **PASS** | Product-level approval by BG Verkehr / Ship Safety Division, distinct from later ship-specific approvals. |
| Outcome-independent identity | **PASS** | Case identity is the approval decision itself; subsequent ship use is not required. |

## 4. Critical unit-of-analysis distinction

The case is **not** defined as an individual ship's later deployment decision. The public German Flag material explicitly distinguishes the product-level approval from additional ship-specific approvals that shipping companies may request for particular MARPOL or ballast-water record books.

Therefore the frozen unit is the **2022 product approval of Searecs**, not any subsequent vessel-level installation or operational outcome.

This preserves the IT-G1 requirement that the decision episode be identifiable independently of later outcomes.

## 5. Documentary limitations

The public record does not, at this stage, establish the complete technical verification package, internal approval correspondence, full product configuration/version identifier, or every detailed acceptance condition that may have formed part of the underlying decision file.

Those limitations are intentionally not filled by inference. They belong to IT-G2 Variable Observability and must be assessed there if the case is advanced.

The existence of these documentary limitations does not prevent IT-G1 closure because IT-G1 concerns case identity and bounded decision unit, not complete reconstruction of all decision-time variables.

## 6. Decision

**IT-G1-L = PASS — BOUNDED PUBLIC CASE IDENTIFIED.**

The public evidence is sufficient to identify one concrete industrial approval episode without relying on subsequent operational outcomes and without collapsing the normative specification into the decision itself.

## 7. Routing

Next permissible operation: **IT-G2 — Variable Observability** for the frozen case `IT-G1-L-SEARECS-BGVERKEHR-2022-02-02`.

IT-G2 must independently assess whether decision-time state/context, accessible transformations, enabling/limiting conditions and the variables needed for the Industrial Track can be observed or reconstructed without changing the frozen case identity.

No industrial execution, utility comparison, causal/value inference, partner/proprietary evidence, new dataset execution, Rust/EXT-1.1 execution, O3, Stage-C/D, or Core modification is authorized by this record.

## 8. Public evidence references

1. German Flag / BG Verkehr, “List of electronic record books approved for the German Flag”: identifies MARSIG, Searecs, approval scope and approval date 02.02.2022.
2. German Flag / BG Verkehr, 2022 announcement: identifies Searecs as approved since 02.02.2022, identifies MARSIG, describes product-level approval, technical verification by BSH or recognized organization, and identifies ISO 21745 and IMO MEPC.312(74) as the technical basis.
3. ISO, ISO 21745:2019: identifies the international standard, publication in September 2019, and its purpose as specifying minimum technical and operational requirements for electronic record books on ships.
