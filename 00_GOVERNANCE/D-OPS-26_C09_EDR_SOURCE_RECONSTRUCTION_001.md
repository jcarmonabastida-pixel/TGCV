# D-OPS-26 — C09 EDR Source Reconstruction 001

**Status:** `CLOSED — C09 CANDIDATE CAUSALLY INADMISSIBLE UNDER CURRENT TGCV OPERATIONALIZATION`
**Date:** 2026-09-13
**Candidate:** Southwestern-China randomized emergency demand-response (EDR), 2019

## 1. Source reconstruction scope

This operation is evidence-only. It does not execute the EDR study, acquire data, fit a new model, rerun SWIM/RUST, or upgrade C09.

The source describes six incentive-based EDR trials in southwestern China from July 18 to August 21, 2019, using clustered random assignment and 15-minute smart-meter data. The published causal estimand is the effect of randomized EDR assignment/incentive exposure on electricity use. The study reports 205,129 households and explicitly distinguishes assignment from subsequent confirmation/participation. [External source: Nature Communications / PMC, 2023.]

## 2. A1–A8 reconstruction

### A1 — Frozen decision-time unit

**Assessment: PASS at study-design level.**

Households are identifiable experimental units and assignment precedes response. The study describes random assignment of households/communities and subsequent EDR messaging/response. Baseline electricity data are available and the smart-meter series is collected at 15-minute intervals.

**Limitation:** exact TGCV frozen profile `S0,C0,L` and the complete variable list required by a TGCV accessibility predicate are not supplied by the published study at the level required for a controlled TGCV execution.

### A2 — Finite bounded transformation universe `U_tau`

**Assessment: FAIL / not demonstrated.**

The source provides electricity consumption measurements and an intervention programme, but it does not define a finite, exhaustive universe of transformations `U_tau` corresponding to household-level operational actions. The observed reduction behaviours cannot be promoted retrospectively to the complete transformation universe without circularity.

This is already sufficient to prevent C09 execution.

### A3 — Ex-ante accessibility predicate `P_tau`

**Assessment: FAIL / not demonstrated.**

The published intervention defines an incentive programme: households receiving assignment/messages may confirm participation and receive rebate coverage. This establishes treatment exposure, not a formal ex-ante rule that enumerates which transformations are accessible.

The source does not provide a non-circular `P_tau` mapping frozen state/context plus assignment to a finite `T_acc`.

### A4 — Accessibility manipulation `Z → ΔT_acc`

**Assessment: FAIL — CRITICAL.**

The randomized assignment changes exposure to an EDR incentive/message and thereby can causally change electricity consumption. The paper explicitly uses the assignment for ITT causal estimation of electricity reduction.

However, the intervention does **not** establish that assignment changes the set of physically/operationally accessible household transformations. The underlying household transformation opportunities (e.g. changing appliance use, shifting consumption, reducing load) remain available to both assigned and non-assigned households. What changes is the incentive/communication condition and consequently behaviour.

Therefore the evidence supports:

`Z → incentive/message exposure → behaviour/electricity-use outcome`

but does not establish:

`Z → T_acc,1 ≠ T_acc,0 → subsequent trajectory`

Under the current TGCV operationalization, this is an intervention on incentives/behaviour, not a demonstrated intervention on accessibility itself.

### A5 — Counterfactual integrity

**Assessment: PASS for conventional causal inference; insufficient for TGCV C09.**

Random assignment supplies a credible treatment/control contrast for the conventional EDR effect. The paper explicitly describes ITT estimation from assignment and also uses assignment as an instrument for treatment receipt in a noncompliance analysis.

This does not cure the A2–A4 TGCV accessibility gap.

### A6 — Independent trajectory outcome `Y`

**Assessment: PARTIAL / not sufficient.**

The source contains high-frequency electricity-use trajectories and defines response-period peak consumption outcomes. These can support conventional longitudinal outcome analysis.

But the TGCV requirement is a frozen trajectory outcome whose interpretation is downstream of an independently reconstructed accessibility change. Since `T_acc` cannot currently be independently reconstructed, A6 cannot establish the TGCV causal chain.

### A7 — Direct-path exclusion

**Assessment: PASS for the narrower TGCV design requirement.**

The assignment does not prescribe a particular future consumption sequence. Households retain discretion over their subsequent electricity use. Thus the intervention does not trivially encode the target trajectory.

This does not establish accessibility manipulation.

### A8 — Provenance / independent reconstruction

**Assessment: PARTIAL.**

The publication supplies study design, assignment description, timing, sample size and 15-minute metering methodology. It does not supply the complete formal rule layer and finite transformation universe needed to independently reconstruct `P_tau` and `T_acc` for TGCV.

## 3. Gate decision

| Gate | Result |
|---|---|
| A1 Frozen decision-time unit | PASS* |
| A2 Finite bounded `U_tau` | **FAIL** |
| A3 Ex-ante `P_tau` | **FAIL** |
| A4 `Z → ΔT_acc` | **FAIL — CRITICAL** |
| A5 Counterfactual integrity | PASS* |
| A6 Independent `Y` | PARTIAL* |
| A7 Direct-path exclusion | PASS* |
| A8 Provenance/reconstruction | PARTIAL |

`*` PASS applies only to the conventional causal-study property, not to full TGCV C09 admissibility.

## 4. Scientific disposition

**EDR is closed as a C09 execution candidate under the current operationalization.**

The candidate remains valuable as evidence that randomized interventions can causally modify subsequent behaviour/consumption, but that is not the same as evidence that an intervention causally modifies `T_acc`.

Consequently:

- C09 remains **H — no causal identification**.
- No EDR execution is authorized.
- No SWIM rerun is authorized.
- No RUST rerun is authorized.
- No new dataset acquisition is authorized from this candidate.
- No claim upgrade is authorized.

## 5. Non-redundancy conclusion

The failed EDR gate confirms that the missing C09 evidence is not more observational trajectory linkage. The missing object is specifically an **exogenous intervention whose treatment contrast changes accessibility itself** while leaving subsequent trajectory choice sufficiently open for a counterfactual test.

The next discovery operation, if C09 remains a programme priority, must therefore search for an intervention with an explicit permission/capability/access-rule change or equivalent mechanism, plus a reconstructible longitudinal transformation universe. A conventional incentive-only intervention is not sufficient.
