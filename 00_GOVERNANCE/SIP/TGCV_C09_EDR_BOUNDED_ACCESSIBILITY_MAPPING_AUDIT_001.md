# TGCV — C09 EDR Bounded Accessibility-Mapping Audit 001

**Status:** `CLOSED — CANDIDATE REJECTED FOR C09 CAUSAL EXECUTION`
**Date:** 2026-09-13
**Candidate:** Southwestern-China EDR 2019
**Parent:** `TGCV_C09_EDR_BOUNDED_CAUSAL_PREFLIGHT_001.md`
**Execution authorization:** `NONE`

## 1. Objective

Determine whether the randomized EDR intervention can be mapped, without post-hoc construction, to the TGCV causal relation:

`Z → ΔT_acc → subsequent trajectory`

The audit is bounded to the declared household-event profile. It does not assess universal demand-response coverage.

## 2. Accessibility mapping

The documented intervention changes whether/how households are invited, notified, permitted and financially rewarded for participating in EDR. The published causal analysis then measures changes in electricity consumption.

For TGCV C09, that is insufficient by itself. A valid mapping requires a pre-treatment transformation universe `U_tau`, an ex-ante predicate `P_tau`, and evidence that random assignment changes the resulting accessible transformation space:

`T_acc(Z=1) ≠ T_acc(Z=0)`.

The available published evidence does not provide such a transformation-level enumeration and predicate. It documents programme access and behavioral response, not a separately identifiable set of transformations whose admissibility changes under assignment.

## 3. Alternative representations tested

### A. Access-to-programme interpretation

`Z → eligibility/notification/participation access → incentive exposure → consumption trajectory`

This is consistent with the documented experiment but does not establish `ΔT_acc` in the TGCV sense.

**Disposition:** insufficient for C09.

### B. Monetary-incentive interpretation

`Z → rebate opportunity → economic incentive → consumption trajectory`

Under this representation, the underlying household transformation space may remain unchanged while the payoff structure changes.

**Disposition:** fails the critical accessibility-change requirement.

### C. Information/notification interpretation

`Z → information about EDR → behavioral choice → trajectory`

Information can affect realized behavior without necessarily changing which transformations are structurally accessible.

**Disposition:** insufficient unless an ex-ante accessibility predicate demonstrates a genuine change in `T_acc`.

### D. Programme eligibility interpretation

If eligibility itself is defined as accessibility, the audit still requires a transformation-level `U_tau` and `P_tau` showing which transformations become accessible under eligibility. The available evidence does not independently provide this mapping.

**Disposition:** not demonstrated.

## 4. Firewall assessment

The audit preserves the required firewall:

- assignment `Z` is pre-treatment;
- outcome trajectory is downstream;
- no post-treatment consumption is used to define accessibility;
- no observed outcome is used to construct `U_tau`.

However, preserving the firewall does not solve the identification problem. The missing element is the independent transformation-level definition of `T_acc`.

## 5. Decision

**Critical gate `Z → ΔT_acc`: FAIL.**

The EDR experiment is therefore **not admissible for C09 causal execution** under the current TGCV operational definition.

This is not a rejection of the published EDR causal result. The experiment can support causal conclusions about demand-response effects under its own outcome definitions. The negative disposition concerns only the stronger TGCV claim that an accessibility-space change causes a subsequent trajectory change.

## 6. Consequence for TGCV

No C09 claim upgrade.

No execution package should be generated from this candidate.

No dataset acquisition, model fitting, causal estimation, AWS mutation, Rust rerun or SWIM rerun is authorized.

The candidate may remain registered as a **causal-design reference** because randomized access assignment and longitudinal outcome measurement are methodologically valuable, but it is removed from the C09 execution-candidate queue.

## 7. Gate closure

The sequence is now:

`D-OPS-22 = promising candidate`

→ `D-OPS-23 = bounded screening PASS`

→ `C09 operational specification = frozen`

→ `bounded preflight = BLOCKED`

→ `accessibility-mapping audit = REJECTED for C09 execution`

The decisive unresolved C09 requirement remains:

> an independently specified, bounded and complete `U_tau` plus ex-ante `P_tau` such that an independently assigned intervention demonstrably changes `T_acc` without directly encoding the downstream trajectory.

**Final disposition:** `EDR CLOSED FOR C09 EXECUTION — RETAINED AS CAUSAL-DESIGN REFERENCE`.
