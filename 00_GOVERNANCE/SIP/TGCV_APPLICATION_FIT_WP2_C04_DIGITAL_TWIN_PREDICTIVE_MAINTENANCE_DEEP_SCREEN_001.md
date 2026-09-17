# TGCV — WP2-C04 Digital Twin Predictive Maintenance Deep-Screen 001

**Status:** PROVISIONAL — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE
**Date:** 2026-09-17
**Parent screen:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Candidate register:** `TGCV_APPLICATION_FIT_WP2_CANDIDATE_REGISTER_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.12 / RMA traceability v3.35

## 1. Evidence boundary

Current industrial architectures show a recurring physical-digital-maintenance chain. AWS documents predictive-maintenance architectures in which sensor data are transmitted through MQTT/HTTP into IoT services, selected telemetry is sent to ML inference, rules trigger downstream processing, and maintenance notifications/orders are generated in SAP. citeturn0search1turn0search7

AWS also documents digital-twin architectures that bind industrial data sources such as IoT telemetry, historians, MES and ERP systems into virtual replicas, with ML capabilities for anomaly detection and predictive maintenance. citeturn0search6

Microsoft's Siemens Healthineers case describes digital twins of production facilities combined with IoT and machine learning to detect anomalies and support predictive maintenance. citeturn0search0 Enerjisa Üretim similarly reports real-time IoT asset monitoring, digital twins and predictive maintenance integrated with asset management and maintenance scheduling. citeturn0search3

These sources establish the existence of physical equipment, telemetry, digital representations, analytics and maintenance workflows interacting in industrial systems. They do **not** establish TGCV constructs, causal evidence for TGCV, or differential value.

## 2. Why C04 is structurally different from C01/C03

C01 was primarily federated technical orchestration.

C03 was agent action/tool accessibility.

C04 introduces a different structure:

`physical asset state → sensed/represented state → digital/analytical state → maintenance decision → physical intervention → subsequent asset state`

The potential coupling is therefore not merely between software domains. It crosses a physical system, sensing/communications, digital representation, analytics and human/organisational action.

This makes C04 useful for testing whether the TGCV accessibility concept remains meaningful when transformations include **physical interventions and maintenance actions**, not just digital operations.

## 3. Decision-time boundary

The most useful boundary is the maintenance decision immediately before a maintenance action is selected or authorised, for example after a new telemetry/prediction state becomes available but before the work order or intervention is executed.

Frozen variables should include:

- physical asset condition;
- relevant sensor/telemetry state;
- digital-twin state and model version;
- anomaly/RUL/prediction information available at decision time;
- available maintenance procedures;
- spare parts/material availability;
- technician skills and availability;
- production/operational constraints;
- safety constraints;
- current work orders and maintenance schedule;
- admissibility rules for interventions.

Public architecture descriptions show the components needed for such a representation, but do not provide a single frozen decision trace with enough detail for empirical reconstruction of `T_acc`.

## 4. Candidate state representation

A bounded TGCV screening representation is:

`S_t = {physical asset configuration/condition, relevant equipment state, current maintenance configuration}`

`C_t = {telemetry, digital-twin state, prediction/anomaly state, resource availability, production constraints, safety constraints}`

`L = {maintenance admissibility, safety, operational and organisational rules}`

Again, this is an analytical reconstruction for WP2 and not a claim about the internal ontology of any vendor platform.

## 5. Candidate transformations

A finite synthetic case could contain transformations such as:

- continue operation unchanged;
- inspect asset locally;
- perform a diagnostic test;
- replace a component;
- lubricate/adjust/calibrate;
- schedule preventive maintenance;
- perform corrective maintenance immediately;
- switch to an alternative operating configuration;
- reduce load or operating intensity;
- temporarily take the asset offline;
- substitute another asset/resource;
- defer intervention subject to safety/production conditions.

The purpose is not to enumerate every conceivable maintenance action. It is to define a bounded `Uτ` sufficient to test whether a concrete state transition changes which of these transformations remain admissible.

## 6. Accessibility hypothesis

C04 yields a natural mechanism-first hypothesis:

`physical/telemetry/digital/resource transition → maintenance transformation admissibility changes → T_acc changes`

For example:

`spare part unavailable`
→ `replace-component` becomes inadmissible
→ alternative inspection/defer/load-reduction transformations remain accessible.

Or:

`asset condition crosses safety threshold`
→ `continue-operation` becomes inadmissible
→ inspection/shutdown/corrective intervention options become admissible.

Formally:

`Pτ(S_t,C_t,L)=1`

and

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`.

A controlled transition can then produce:

`T_acc,t → T_acc,t+1`.

The important point is that the transition need not improve the maintenance outcome. It only needs to alter the **future set of admissible transformations**.

## 7. Multidomain coexistence vs transformational coupling

The architecture clearly contains multiple domains: physical equipment, IoT/telemetry, digital twin, ML/AI, maintenance management and human/operator workflows. citeturn0search1turn0search3

The stronger coupling interpretation requires more:

`change in physical state`
→ `change in represented/known state`
→ `change in admissible maintenance transformations`
→ `different subsequent physical/operational trajectory`.

This is more than coexistence if the intermediate state change systematically modifies the future transformation space.

However, conventional predictive-maintenance systems already contain condition monitoring, thresholding, rules, work-order generation, optimisation and control logic. Therefore the same alternative-explanation problem remains as in C01/C03.

## 8. Potential TGCV-specific contribution to test

The most informative question is not whether a digital twin can predict failure. It is whether a transformation-space representation adds a layer that is otherwise obscured by:

- condition monitoring;
- predictive maintenance models;
- maintenance decision rules;
- finite-state machine representations;
- scheduling/optimisation models;
- asset-management workflows.

A TGCV representation could potentially make explicit that the relevant object is not simply a predicted condition or selected maintenance action, but the **change in the set of future transformations accessible after a state transition**.

This distinction is testable.

## 9. Minimum next proof

**Physical-Digital Maintenance Transformation Mapper — synthetic bounded demonstrator.**

Minimum configuration:

1. one physical asset represented by a finite-state digital twin;
2. synthetic telemetry stream;
3. finite maintenance transformation catalogue;
4. explicit outcome-independent admissibility predicates;
5. `T_acc,0` reconstruction;
6. one controlled state transition, e.g. health degradation or spare-part unavailability;
7. `T_acc,1` reconstruction;
8. downstream trajectory simulation;
9. conventional predictive-maintenance/rule-based baseline;
10. comparison of what each representation makes explicit.

A particularly clean two-factor design would separate:

- **asset-state intervention:** healthy → degraded;
- **resource-state intervention:** spare available → unavailable.

This tests whether physical condition and operational resource constraints produce distinguishable changes in future transformation space.

## 10. Stronger demonstration variant

A second layer could introduce a digital-twin prediction that changes only the **information state**, while holding the physical asset state fixed.

This would allow separation of:

`physical-state change`
from
`knowledge/representation change`
from
`resource/constraint change`.

That separation is methodologically valuable because otherwise an observed change in maintenance actions could be attributed simply to the physical degradation itself.

The demonstrator should therefore preserve a strict decision-time boundary and avoid using later maintenance outcomes to define admissibility.

## 11. Alternative-explanation test

The baseline should include at least:

- threshold/rule-based predictive maintenance;
- finite-state maintenance workflow;
- conventional scheduling/optimisation representation;
- asset-management work-order logic.

The key comparison is whether TGCV provides a distinct representation of **future accessible transformations and their trajectory implications**, rather than simply renaming existing maintenance states or actions.

If the same structure is fully captured by the baseline, C04 remains an application/demonstration opportunity but does not support a differential TGCV claim.

## 12. Maturation route

**Primary route: Applied Demonstration.**

C04 is particularly compatible with a small synthetic demonstrator because digital-twin architectures already support simulated asset state, telemetry and maintenance workflows. AWS explicitly documents a predictive-digital-twin architecture using synthetic data and maintenance data, making this kind of bounded experimental setup technically plausible. citeturn0search8

A scientific route becomes appropriate only if the demonstrator identifies a non-trivial, reproducible transformation-space property not equivalently represented by the baseline.

## 13. Current disposition

**WP2-C04 — COUPLING-CANDIDATE.**

Reason: C04 exhibits a structurally stronger cross-boundary chain than C01/C03 because the candidate transformation space can include physical maintenance interventions and the resulting state trajectory. The architecture is well suited to a controlled synthetic demonstration. However, existing industrial architectures already provide strong conventional explanations through condition monitoring, prediction, rules and maintenance workflows.

Therefore this is **not evidence of differential TGCV value** and does not justify any scientific claim upgrade.

## 14. Cross-case observation after C01/C03/C04

The three candidates now instantiate the same screening hypothesis at increasingly different levels:

- **C01:** network/compute/security orchestration;
- **C03:** agent/tool/permission action space;
- **C04:** physical asset/digital twin/maintenance action space.

The recurring abstraction is potentially useful if it survives the baseline challenge: a state transition may alter the set of transformations accessible at the next decision point.

But the fact that the abstraction can be imposed on all three cases is not itself evidence that it is scientifically or operationally superior.

**Next case:** WP2-C05 — Energy–mobility / EV-grid coordination, focusing on resource coupling and constraint propagation.
