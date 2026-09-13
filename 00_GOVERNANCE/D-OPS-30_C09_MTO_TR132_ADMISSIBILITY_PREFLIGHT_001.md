# D-OPS-30 — C09 MTO TR-132 Admissibility Preflight 001

**Status:** `CLOSED — CANDIDATE REJECTED / TR-132 STATE-SUFFICIENCY FAIL`
**Date:** 2026-09-13
**Candidate:** Moving to Opportunity (MTO) randomized housing-mobility experiment

## 1. Decision

MTO is a strong randomized longitudinal experiment, but the current bounded relocation profile does **not** pass the TR-132 state-sufficiency requirement needed to establish a TGCV-specific accessibility intervention.

Therefore:

`D29-A MTO = REJECTED FOR C09 UNDER CURRENT OPERATIONALIZATION`

`C09 = H — NO CAUSAL IDENTIFICATION`

No execution, new data acquisition or claim upgrade is authorized.

## 2. Evidence reconstruction

MTO randomly assigned eligible volunteer families to a low-poverty voucher plus counseling, a geographically unrestricted Section 8 voucher, or a control condition. The experiment was conducted in five U.S. cities and followed families longitudinally, including a final 2008–2010 evaluation. citeturn0search2turn0search4turn0search14

The intervention clearly changes access to housing assistance and produces randomized differences in subsequent residential environments. citeturn0search0turn0search9

## 3. Proposed TGCV operationalization

The candidate was intentionally tested using a bounded profile:

`U* = {remain in origin housing state, relocate through qualifying voucher}`

with the intended causal chain:

`Z → voucher/resource eligibility → relocation accessibility → subsequent residential/social trajectory`

This is materially stronger than the rejected live-streaming candidate because the intervention changes a resource/eligibility condition rather than merely the delivery channel.

## 4. TR-132 gate

### G1 — decision-time state identity
**PASS at coarse level.** The experiment supplies a well-defined baseline household and assignment state before treatment.

### G2 — ex-ante intervention/access rule
**PASS.** Assignment to the treatment arms occurred before relocation and before subsequent outcomes. Voucher rules were specified independently of later outcomes. citeturn0search0turn0search2

### G3 — bounded transformation profile
**PASS descriptively.** A bounded relocation profile can be constructed for a declared housing-mobility scope.

### G4 — causal intervention on capability/resource feasibility
**PASS/PROMISING.** The voucher materially changes the feasibility of accessing private-market housing and, for the experimental arm, qualifying low-poverty neighbourhoods. citeturn0search1turn0search14

### G5 — state sufficiency / omitted-transformation closure
**FAIL — CRITICAL.** The proposed state is insufficient to guarantee that all omitted transformations are causally irrelevant to the subsequent trajectory. Residential mobility is not a single binary transformation: households can remain, move through different voucher mechanisms, move repeatedly, change neighbourhood characteristics, experience changes in household composition, employment, schooling, services and other state variables. The available MTO design does not supply a TGCV-native proof that the bounded `{remain, qualifying relocation}` profile is sufficient for the entire subsequent trajectory.

This is not a criticism of MTO's conventional causal identification. It is a failure of the **TGCV state-sufficiency gate**.

### G6 — independent trajectory
**PASS/PROMISING.** MTO has longitudinal residential and outcome observations extending from baseline through interim and final follow-up. citeturn0search2turn0search14

### G7 — no treatment-outcome leakage
**PASS.** Treatment assignment precedes subsequent residential and outcome observations.

### G8 — causal estimand integrity
**PASS conventionally / insufficient TGCV-wise.** ITT effects can be estimated from randomized assignment, but this does not by itself identify `Z → ΔT_acc → Y` under the proposed bounded transformation representation.

### G9 — provenance/reconstruction
**PROMISING.** The MTO data have substantial public documentation and longitudinal administrative/survey components, including residential histories. citeturn0search9turn0search14

## 5. Why TR-132 changes discovery but does not automatically admit MTO

The revised D-OPS-29 rule remains correct: **a globally exhaustive transformation universe is not required at discovery if TR-132 can prove sufficiency of a bounded operational state.**

MTO was selected precisely to test that possibility.

However, TR-132 does not mean that any arbitrarily narrow profile becomes sufficient. The bounded profile must preserve the relevant future transformation possibilities needed for the declared causal question.

MTO fails because the evidence available at this stage does not establish that the proposed binary relocation profile is sufficient to represent the relevant future state transitions.

Thus:

`TR-132 = admissibility mechanism, not automatic waiver of state completeness.`

## 6. Important consequence for future discovery

The next candidates should be prioritized where the intervention itself defines a **discrete, administratively or technically enforceable capability boundary**, and where the post-intervention state can remain finite and sufficient without reconstructing an entire human life-course transformation space.

Preferred structures now include:

- permission to execute a bounded technical operation;
- eligibility to access a specific resource with a finite action vocabulary;
- randomized authorization to use a constrained service/function;
- capability enable/disable experiments with machine-readable state;
- platform or organizational experiments where treatment changes an explicit executable permission rather than only incentives or information.

Human mobility cases remain conceptually useful but are lower priority when TR-132 sufficiency cannot be demonstrated from the frozen evidence.

## 7. C09 status

`C09 = H — NO CAUSAL IDENTIFICATION`

`D29-A MTO = CLOSED — TR-132 FAIL`

`D29 discovery principle = RETAINED`

`EXECUTION = NOT AUTHORIZED`

`NEW DATASET ACQUISITION = NOT AUTHORIZED`

`RUST/SWIM RERUN = NOT WARRANTED`

## 8. Next operation

**D-OPS-31 — Targeted discovery of bounded technical/organizational permission experiments.**

D-OPS-31 should search specifically for randomized or otherwise strongly identified interventions where:

`Z → explicit executable permission/capability/resource state → finite sufficient T_acc → longitudinal subsequent state`

The discovery should prioritize cases in which **TR-132 can be established from the published experimental protocol itself**, before any attempt to obtain proprietary or restricted data.
