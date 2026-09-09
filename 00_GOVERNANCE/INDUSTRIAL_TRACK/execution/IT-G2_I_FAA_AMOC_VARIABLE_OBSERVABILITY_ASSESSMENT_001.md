# IT-G2-I — FAA AMOC Variable Observability Assessment 001

**Date:** 2026-09-09  
**Status:** CLOSED — IT-G2 PASS (PUBLIC OBSERVABILITY BOUNDED)  
**Case:** IT-G1-I-AMOC-US-91-12-10-7K0-18-00734  
**Gate:** IT-G2 — Variable Observability

## 1. Purpose

Assess whether the frozen FAA AMOC case identified at IT-G1 has sufficient independently observable decision-time variables to permit entry to IT-G3, without inferring missing variables from later outcomes.

## 2. Evidence closure

The EASA Safety Publications Tool exposes the AD identity, approval holder, affected type designations, service-document revisions and the attached FAA AMOC.

The attached FAA approval letter is unusually strong public evidence for this case. It identifies the requester (Textron Aviation), FAA event number 19880001, reference 7K0-18-00734, the AD, the proposal date (17 January 2018), and the approval decision. It also states the substantive change: the prior interim 15,000-hour TIS life limit was superseded after testing and analysis, and specifies the maintenance-manual Airworthiness Limitations used as the AMOC.

Crucially, the letter exposes concrete applicability restrictions: named aircraft models and explicit serial-number ranges, plus the required maintenance-manual revisions. It identifies the substantiating basis for acceptable safety and the transferability condition.

FAA Order 8110.103B independently confirms that these are the kinds of fields required in an AMOC approval response: AD and paragraphs, make/model or other limits, substantiating data, restrictions, service documents and transferability. It also states that public requests may disclose holder, approval date, applicable make/model and AD information, while technical specifics may be restricted.

## 3. IT-G2 assessment

| Variable class | Result | Assessment |
|---|---|---|
| Case identity | **PASS** | AD, AMOC reference, event number, requester and approval date are identified. |
| Normative context | **PASS** | AD 91-12-10 and FAA Order 8110.103B are identifiable; the case-specific letter states its governing conditions. |
| System/product boundary | **PASS** | Aircraft models and serial-number ranges are explicitly bounded. |
| Decision-time technical state | **PASS** | The letter identifies the interim life-limit condition, completed testing/analysis, and the applicable maintenance-manual revisions. |
| Accessible transformation / alternative | **PASS** | The alternative is explicitly represented by the post-1995 Airworthiness Limitations sections/revisions that replace the interim life-limit condition. |
| Enabling/limiting conditions | **PASS** | Serial-number applicability, manual revisions, remaining AD provisions, transferability and notification/use conditions are stated. |
| Independent reconstruction | **PASS** | The case can be reconstructed from the public EASA record plus the attached FAA approval letter without using later operational outcomes. |
| Outcome/utility | **NOT ASSESSED** | No utility, performance or value claim is made at IT-G2. |

## 4. Accessibility interpretation

This case does not require reconstruction of an unobservable proprietary proposal. The public approval letter contains enough decision-time information to identify the operative alternative and its applicability constraints. The proposal is referenced, but the decision boundary can be reconstructed from the approval itself and the cited maintenance documents.

The distinction is important: IT-G2 PASS means the variables required for bounded observability are publicly reconstructable. It does **not** mean that the case demonstrates TGCV, establishes causality, or establishes value.

## 5. Decision

**IT-G2-I = PASS — PUBLIC OBSERVABILITY BOUNDED.**

The case is eligible to proceed to **IT-G3 — Accessibility Closure**.

No utility comparison, causal inference, value inference, industrial experiment, new dataset execution, Rust/EXT-1.1 execution, O3, Stage-C/D or Core modification is authorized by this record.

## 6. Routing

Next permissible operation: **IT-G3 Accessibility Closure** for `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`.
