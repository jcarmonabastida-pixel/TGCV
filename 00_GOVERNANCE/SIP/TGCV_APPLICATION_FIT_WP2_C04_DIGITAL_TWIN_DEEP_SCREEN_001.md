# TGCV — Application Fit WP2-C04 Cross-Domain Digital Twin Deep-Screen 001

**Status:** PROVISIONAL — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE
**Date:** 2026-09-17
**Parent screen:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Candidate register:** `TGCV_APPLICATION_FIT_WP2_CANDIDATE_REGISTER_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.14 / RMA traceability v3.35

## 1. Evidence boundary

The selected C04 case is the 2026 cross-domain digital-twin architecture for predictive maintenance reported in *Computers & Industrial Engineering* (Vol. 215, article 111914). The study integrates physical equipment sensing, MQTT data transport, machine-learning fault classification, edge/cloud computation, an LLM guidance component and AR/web operator interfaces. The paper describes an end-to-end loop from sensor data through fault prediction to maintenance guidance and reports testbed-based implementation. citeturn1search0

The associated public dataset repository contains vibration and temperature monitoring data from a test-bed motor under baseline and faulty conditions, with two motors of the same model and two monitoring platforms, enabling cross-platform comparison/fusion. citeturn1search12

These facts establish a materially cross-domain physical–digital–operational architecture and provide a stronger empirical substrate than the public descriptions used for C01 and C03. They do not, by themselves, establish a TGCV `T_acc`, `ΔT_acc`, or a causal effect of accessibility on maintenance outcomes.

## 2. Decision-time boundary

The most informative boundary is a maintenance decision point after a physical/telemetry state has been observed and fault information has been generated, but before a concrete maintenance action is selected.

Relevant state/context variables can include:

- physical equipment condition;
- sensor observations and telemetry state;
- inferred fault class / diagnostic state;
- digital-twin state;
- available maintenance procedures and work instructions;
- operator/interface state;
- spare-part/tool/resource availability where represented;
- applicable safety and operational constraints.

The study provides enough architectural information to define this boundary conceptually, but the published material does not expose a complete frozen decision instance containing all candidate actions and outcome-independent admissibility predicates.

## 3. Candidate state representation

A bounded TGCV screening representation is:

`S_t = {physical asset state, detected condition/fault state, digital-twin state, maintenance status}`

`C_t = {sensor/telemetry context, available procedures, operator context, resource constraints, safety/operational constraints}`

`L = {maintenance and safety admissibility rules}`

This is an analytical reconstruction, not a claim that the source system uses TGCV terminology or ontology.

## 4. Candidate transformations

Potential transformations suggested by the architecture include:

- continue monitoring;
- inspect a component;
- initiate a maintenance procedure;
- change operating conditions;
- replace or service a component;
- issue or follow a maintenance work instruction;
- alter the maintenance plan in response to a detected fault;
- return the asset to service after an admissible intervention.

The source demonstrates the sensing-to-guidance pathway, but does not provide a complete finite transformation universe with explicit preconditions for each action. Therefore these remain candidate transformations.

## 5. Accessibility/admissibility hypothesis

The C04 TGCV hypothesis is stronger than simply saying that physical, data and AI layers interact:

`physical/diagnostic state change → admissibility of maintenance transformations changes → operator/maintenance action space changes → subsequent asset trajectory changes`

For example, detection of a particular fault class could make a specialised inspection or maintenance action admissible while making continued operation inadmissible under a given safety policy. Conversely, a healthy state could leave a larger set of operating transformations accessible.

The target reconstruction is:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

followed by a controlled state transition and reconstruction of `T_acc,t+1`.

## 6. What the current evidence supports

The paper provides an actual end-to-end physical-to-digital-to-guidance pipeline, rather than merely a conceptual architecture. It also reports testbed data and fault-classification experiments. citeturn1search0turn1search12

This makes the C04 mechanism structurally plausible and potentially more amenable to empirical reconstruction than C01/C03. However, prediction of a fault and generation of guidance are not equivalent to demonstrating that the system's transformation space changed. The published material reviewed here does not yet specify the pre/post admissibility conditions for a fixed action universe or independently reconstructable downstream trajectory under a controlled state transition.

## 7. Multidomain coexistence vs transformational coupling

### A. Conventional predictive-maintenance explanation

The case can be represented as a conventional pipeline:

`physical sensing → data transport → fault classification → maintenance recommendation`

The digital twin, ML model and LLM can be treated as successive information-processing components without requiring a separate transformation-space construct.

### B. Transformational-coupling explanation

A stronger interpretation becomes justified if a change in physical/diagnostic state changes which maintenance or operational transformations are admissible, and that altered action space subsequently changes the asset trajectory:

`asset state → diagnostic state → admissible maintenance actions → selected intervention → new asset state`

The discriminating issue is therefore whether the cross-domain chain changes the **set of future transformations**, rather than merely improving information about the current state.

## 8. Alternative-explanation test

Relevant baselines include:

- conventional condition-based/predictive maintenance state machines;
- fault-diagnosis decision trees;
- maintenance workflow models;
- rule-based safety and admissibility systems;
- digital-twin state-transition models;
- standard optimisation or scheduling representations where applicable.

If these baselines represent the same state-dependent action changes with equivalent clarity, the case remains an important multidomain application but does not demonstrate a distinct TGCV contribution.

## 9. Strongest current opportunity

C04 differs materially from C01 and C03 because a public empirical dataset exists and the source reports physical testbed operation. citeturn1search12

That makes a future bounded mapper potentially empirical rather than purely synthetic. However, the dataset should not be treated as an authorised execution input merely because it exists publicly. A separate frozen protocol would first need to specify:

1. decision-time boundary;
2. finite transformation catalogue;
3. admissibility predicates independent of later outcome;
4. state/context variables available before action selection;
5. intervention or transition definition;
6. trajectory observation window;
7. baseline representation;
8. handling of fault labels and information leakage;
9. reproducibility and data provenance;
10. non-claims concerning causal effects and value.

## 10. Minimum next proof

**Physical–Digital Maintenance Transformation Mapper — bounded case reconstruction.**

The smallest useful next proof is not a general predictive-maintenance benchmark. It is a bounded reconstruction of one or a small number of fault-state transitions in which:

1. `S0,C0` is frozen;
2. a finite candidate action universe `Uτ` is defined;
3. `Pτ(S,C,L)` is specified independently of the later result;
4. `T_acc,0` is reconstructed;
5. a defined physical/diagnostic transition occurs;
6. `T_acc,1` is reconstructed;
7. transformations opened/closed/reordered are identified;
8. a subsequent maintenance trajectory is observed or reconstructed;
9. a conventional maintenance/digital-twin baseline is reconstructed;
10. the additional information, if any, supplied by the transformation-space representation is explicitly tested.

No execution is authorized by this screen.

## 11. Maturation route

**Primary candidate route: Applied Demonstration, with a possible later Scientific route.**

The existence of public empirical data makes a bounded scientific study conceivable, but only after the accessibility and decision-time contract has been made explicit. The immediate WP2 result remains structural/application-fit screening rather than scientific validation.

The separate Value route remains prospective and pending external responses; it does not alter this WP2 disposition.

## 12. Current disposition

**WP2-C04 — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE.**

Reason: C04 provides a concrete physical–digital–operational chain and public empirical substrate that make state-dependent transformation accessibility plausible. The current published evidence does not yet reconstruct a controlled `ΔT_acc` instance or establish that the transformation-space representation adds information beyond conventional predictive-maintenance, workflow, diagnostic or control models.

**No scientific claim upgrade.** No change to TGCV Core, RMA, Evidence→Claim Matrix, or existing scientific evidence state.

## 13. Cross-case observation after C01–C04

The WP2 mechanism is now visible across three structurally distinct forms:

- C01: federated network/compute/security orchestration;
- C03: agent/tool/permission action space;
- C04: physical asset/diagnostic/maintenance action space.

In all three, the central unresolved question is the same: whether state-dependent changes in future accessible transformations provide information that conventional orchestration, capability, workflow, diagnostic or control representations do not already capture equivalently.

The next structural contrast is **WP2-C05 — Energy–mobility / EV-grid coordination**, where resource and constraint coupling should test whether the same reconstruction survives outside software/AI-centric architectures.
