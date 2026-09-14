# TGCV — C09 OLPC Peru Causal-Gap Closure Specification 001

**Status:** `FROZEN — C09 GAP CLOSURE / EXECUTION AUTHORIZED`
**Date:** 2026-09-14
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Case:** Beuermann, Cristia, Cueto, Malamud & Cruz-Aguayo — *One Laptop per Child at Home: Short-Term Impacts from a Randomized Experiment in Peru*
**Public package:** openICPSR 113587 V2

## 1. Purpose

This specification addresses the **remaining empirical gap of C09** using the OLPC Peru case and its public dataset.

The object of the operation is **not to prove TR-132**. TR-132 gates are used only as an audit scaffold for the empirical reconstruction. The scientific decision sought here is whether the OLPC Peru evidence can close the unresolved C09 causal link:

> Under a frozen decision-time state/context and an independently defined accessibility rule, does an exogenous change in accessibility conditions produce a distinguishable change in a subsequent trajectory relative to an appropriate counterfactual?

## 2. Existing evidence that is not to be repeated

The following are already established and must be treated as prior C09 evidence rather than re-tested unnecessarily:

- RUST-DYN-2: bounded structural empirical evidence distinguishing accessibility change from potential one-step Reach under H=1.
- SWIM: bounded observed trajectory linkage/reconstructability.
- FOS and related prior evidence already registered for C09.
- OLPC Peru P4: bounded transformational-space operationalisation.
- OLPC Peru P5: independent downstream trajectory/endpoint layer.
- OLPC Peru P6: randomized treatment/counterfactual structure.
- OLPC Peru P7: public reproducibility remains provisional until the targeted local reconstruction is executed.

This operation therefore targets the **causal bridge** that remains unresolved, not the already-covered descriptive or structural components.

## 3. Frozen bounded representation

### 3.1 Decision-time state

`S0 = (R0, K0, C0)`

where the observable baseline accessibility components are restricted to pre-treatment Round 1 variables:

- `R0`: R1 P2, P3, P4 — computer/laptop access, Internet access, prior computer use.
- `K0`: R1 P12_A1–P12_A8 — declared computer capabilities.
- `C0`: pre-treatment study context available from the public package, including school/pair linkage where required for the experimental design.

### 3.2 Bounded transformational domain

`U* = transformaciones domésticas dependientes de disponer de un ordenador/laptop en el hogar, dentro de las clases de actividad informática explícitamente representadas por los instrumentos OLPC.`

The analysis must not generalize beyond this bounded domain.

### 3.3 Accessibility change

`T_acc,0` is reconstructed from the frozen R1 baseline accessibility variables.

`T_acc,1` is reconstructed from R2 P1, P2 and P3 as post-intervention resource/access conditions.

`ΔT_acc` is the bounded change between these states, with missing/nonresponse handling made explicit in the execution record.

R2 P4–P7 remain trajectory/use observations and are not allowed to redefine accessibility.

R2 P9–P11 remain capability-result observations.

### 3.4 Treatment assignment

`Z = won_lottery`

`received_laptop` is implementation/compliance/effective exposure and must not replace `Z`.

`treatment_school` is a school-level condition and must not replace individual lottery assignment.

## 4. C09 causal closure test

The local execution must establish, from the public package, whether the randomized assignment generates an exogenous accessibility change and whether that accessibility change is associated with a subsequent trajectory under a defensible counterfactual comparison.

The primary causal chain under audit is:

`Z → ΔT_acc → subsequent trajectory`

The analysis must explicitly distinguish this from the weaker chain:

`Z → subsequent trajectory`

A treatment effect on an outcome alone does **not** close C09. The evidence must connect the experimentally induced accessibility change to the subsequent trajectory within the bounded `U*` representation.

## 5. Required local reconstruction

### A. Assignment and linkage

1. Verify `won_lottery` coding and its linkage to the student observations.
2. Verify the school/pair structure without substituting `treatment_school` for `Z`.
3. Record sample counts and exclusions transparently.

### B. Baseline accessibility

Reconstruct `T_acc,0` exclusively from frozen pre-treatment variables.

### C. Post-treatment accessibility

Reconstruct `T_acc,1` exclusively from R2 P1–P3.

### D. Accessibility change

Construct a reproducible bounded representation of `ΔT_acc`.

The execution record must state the exact coding and missing-data policy. No post-treatment use, skill, academic or cognitive variable may enter the accessibility classifier.

### E. Subsequent trajectory

Use pre-specified Round 2 downstream variables as trajectory/endpoint candidates. At minimum, retain the already frozen separation of:

- R2 P4–P7: trajectory/use;
- R2 P9–P11: capability-result;
- `Y = raven_r2 ∈ [0,36]`: independent endpoint from the 36 Raven items.

If the public package contains additional downstream outcome variables required by the published experimental analysis, they may be reported as outcomes, but they must remain outside `T_acc`.

### F. Causal bridge assessment

The execution must answer separately:

1. Does `Z` produce a measurable bounded change in accessibility?
2. Does `Z` produce a measurable subsequent trajectory difference?
3. Is the observed trajectory difference attributable to the accessibility change within the bounded causal design, or could it arise from direct treatment effects or other channels that the intervention also changes?
4. Does the evidence therefore satisfy the C09 causal requirement, or is the result only partial/inconclusive?

## 6. Direct-effect / mediation caution

Because the OLPC intervention is delivery of a laptop for home use, the analysis must not silently equate the treatment effect with an accessibility-mediated effect.

A finding that `Z` changes `T_acc` and that `Z` changes an outcome is **necessary but not by itself sufficient** to establish that `ΔT_acc` causally explains the subsequent trajectory.

Any stronger mediation statement requires explicit identification assumptions and observable support from the public data. If those assumptions cannot be defended, the correct C09 verdict is `PARTIAL / INCONCLUSIVE`, not PASS.

## 7. Information firewall

Forbidden substitutions:

- outcome → accessibility;
- realized use → accessibility;
- capability result → accessibility;
- laptop receipt → randomized assignment;
- school treatment → individual assignment;
- treatment effect → accessibility-mediated effect without identification support;
- public reproducibility → causal closure without execution evidence.

## 8. Acceptance criteria for C09 closure

### PASS — C09 GAP CLOSED

Only if all of the following hold:

1. Public-package inputs are reproducibly identified and integrity-checked.
2. `Z = won_lottery` is correctly reconstructed and linked.
3. `T_acc,0` and `T_acc,1` are reconstructed from the frozen bounded variables without post-treatment leakage.
4. A reproducible `ΔT_acc` is obtained.
5. A downstream trajectory is independently defined and reconstructed.
6. A valid counterfactual comparison is preserved.
7. The evidence supports a causal interpretation of the accessibility change on the subsequent trajectory within `U*`, rather than merely a treatment effect or association.
8. Direct treatment pathways and material alternative explanations are either excluded by design or explicitly addressed by the identification strategy.
9. Execution is independently reproducible from the public package with logs, environment and hashes.
10. The resulting evidence is sufficient to answer the C09 causal question affirmatively within the stated bounded scope.

### PARTIAL / INCONCLUSIVE

Use this verdict if accessibility change and/or trajectory effects are demonstrated but the accessibility-to-trajectory causal bridge cannot be separately identified from direct treatment effects or other channels.

### FAIL

Use this verdict if the required assignment, accessibility reconstruction, trajectory, or counterfactual cannot be established, or if the proposed causal bridge is contradicted by the reconstructed evidence.

### BLOCKED_INFRASTRUCTURE

Use only for an execution/environment/input failure that prevents the scientific test from being performed. Do not treat infrastructure failure as scientific failure.

## 9. Required outputs

The local execution must produce:

- frozen input inventory;
- input integrity hashes;
- environment record;
- assignment reconstruction summary;
- baseline accessibility reconstruction;
- post-treatment accessibility reconstruction;
- `ΔT_acc` construction and coding record;
- trajectory/outcome reconstruction;
- causal comparison results;
- direct-effect/alternative-explanation assessment;
- execution log;
- output hashes;
- final C09 verdict: `PASS`, `PARTIAL/INCONCLUSIVE`, `FAIL`, or `BLOCKED_INFRASTRUCTURE`.

## 10. Governance consequence

This execution is authorized to determine the **C09 evidence state only**.

A `PASS` does not automatically modify TGCV Core, C10–C13, value claims, industrial utility claims, or any unrelated Evidence-to-Claim Matrix entry. Those changes require a subsequent governance operation based on the resulting evidence record.

Likewise, a `PARTIAL/INCONCLUSIVE`, `FAIL`, or `BLOCKED_INFRASTRUCTURE` result must be registered without reinterpretation as a positive finding.

## 11. Immediate next action

Execute this frozen specification locally against the already available public package:

`C:\Users\pedri\Downloads\openICPSR\113587-V2`

The next artifact after execution is the **C09 OLPC Peru causal-gap closure evidence record**, not a generic TR-132 reproducibility record.
