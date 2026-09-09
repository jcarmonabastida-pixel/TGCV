# IT-G2-D — LynxOS-178 RSC Observability Closure Attempt 001

**Date:** 2026-09-09  
**Status:** CLOSED — IT-G2 REMAINS HOLD / NOT CLOSED  
**Candidate:** IT-NOSD-007 — FAA AC 20-148 / LynxOS-178 initial RSC case (2006)  
**Prior status:** IT-G1 PASS; IT-G2 HOLD / NOT CLOSED

## 1. Purpose

Conduct the single narrow documentary closure operation authorized after IT-G2, using only independent pre-existing public evidence, to determine whether the missing decision-time variables can be closed without redefining the frozen IT-G1 case.

## 2. New documentary evidence

The FAA's official AC 20-148 states that an RSC acceptance letter is issued only after the FAA grants the relevant certification or authorization for a product or equipment using the RSC. The AC also specifies that unchanged RSC software may be reused without additional FAA review only when it remains within the limitations of the acceptance letter and no relevant safety, installation, operational, functional, or performance concerns arise in subsequent use. citeturn0search34turn0search8

The same official AC establishes that RSC acceptance is embedded in a concrete approval context such as a type certificate, supplemental type certificate, amended certificate, or TSO authorization. This confirms that the RSC decision cannot be treated as an isolated software-only state: its admissibility depends on installation/integration context and the acceptance-letter limitations. citeturn0search34

Independent public material confirms that the initial 2006 LynxOS-178 RSC approval concerned the Rockwell Collins Adaptive Flight Display Runtime, Common Computing Runtime and Data Concentration Module Runtime for Pro Line Fusion. citeturn1search2turn1search0

Public technical documentation also exposes a substantial portion of the RSC structure: time/space/resource partitioning, timing-margin analysis, requirements/design/test/coverage evidence, target-hardware-independent reusable components, PowerPC family scope, and application/API boundaries. citeturn0search2turn0search3

## 3. Closure assessment

| Missing IT-G2 domain | Closure result | Reason |
|---|---|---|
| Decision-time normative context | **CLOSED** | Official AC 20-148 is explicit and dated 2004-12-07. |
| Accepted component scope | **CLOSED** | Three named Pro Line Fusion runtime components are independently identified. |
| Broad technical state/context | **PARTIAL** | Public documentation exposes partitioning, interfaces, timing/resource concepts and processor-family scope, but not the complete acceptance basis. |
| Exact acceptance-letter limitations | **NOT CLOSED** | The FAA AC explicitly makes these limitations decision-critical, but the actual 2006 acceptance letter is not publicly recovered. |
| Full installation/integration context | **NOT CLOSED** | AC 20-148 ties acceptance to the approving product/equipment and installation context; the public record does not expose the complete configuration. |
| Complete accessible transformation space | **NOT CLOSED** | Later public descriptions establish reusable configurations in principle but cannot enumerate the complete 2006 admissible configuration space without the acceptance-letter limitations and integration data. |
| Enabling/limiting conditions | **PARTIAL / NOT CLOSED** | General RSC constraints are observable, but case-specific constraints remain inaccessible. |

## 4. Decisive finding

The closure attempt strengthens IT-G2 substantially but does **not** close it.

The key reason is structural: the official FAA procedure makes the **acceptance-letter limitations and installation/approval context part of the decision boundary itself**. Those data are not optional explanatory details. Without them, reconstructing the case's complete `T_acc` would require inference from later uses or generic AC 20-148 provisions.

That inference would violate the frozen protocol and would risk converting the observed outcome/deployment history into the definition of the accessible transformation space.

## 5. Decision

**IT-G2-D = INSUFFICIENT FOR CLOSURE.**

**Overall IT-G2 = HOLD / NOT CLOSED.**

No downgrade of IT-G1 is warranted. The public case remains validly identified at IT-G1; it is simply not sufficiently observable for the next industrial-track gate on public documentary evidence alone.

## 6. Routing

Do **not** enter IT-G3 for LynxOS-178 on the current public evidence.

The only legitimate future route for this candidate would require independently accessible, decision-time evidence of the 2006 acceptance-letter limitations and the associated approving product/equipment configuration. Such evidence must be pre-existing and must not be selected or interpreted from later deployment success.

Otherwise the case is frozen at IT-G2 HOLD and the programme should screen the next retained industrial candidate rather than repeatedly mining the same insufficient public record.

No industrial execution, utility comparison, causal/value inference, proprietary/partner evidence, new dataset execution, Rust/EXT-1.1 execution, O3, Stage-C/D, or Core modification is authorized.
