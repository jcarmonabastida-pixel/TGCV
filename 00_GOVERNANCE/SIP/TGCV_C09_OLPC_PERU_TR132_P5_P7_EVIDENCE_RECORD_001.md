# TGCV — C09 OLPC Peru TR-132 P5–P7 Evidence Record 001

**Status:** `CLOSED — P5 PASS / P6 PASS / P7 PASS PROVISIONAL`
**Date:** 2026-09-14
**Candidate:** Beuermann, Cristia, Cueto, Malamud & Cruz-Aguayo — *One Laptop per Child at Home: Short-Term Impacts from a Randomized Experiment in Peru*
**Data package:** openICPSR 113587 V2
**Gates:** TR-132 P5, P6, P7

## 1. Decision

| Gate | Decision | Basis |
|---|---|---|
| P5 — independent trajectory / endpoint | **PASS** | Follow-up observations provide downstream trajectory and endpoint layers independently of the bounded accessibility definition. |
| P6 — treatment / counterfactual | **PASS** | Randomized lottery assignment supplies the causal counterfactual; assignment, receipt and school condition remain separated. |
| P7 — public independent reproducibility | **PASS PROVISIONAL** | Public V2 package is available with original data, follow-up data, instruments, code/materials and results; independent local execution has not yet been completed. |

P8 remains **NOT AUTHORIZED**.

## 2. P5 — independent trajectory / endpoint

P5 requires that the study expose a downstream trajectory and/or endpoint that is not simply reintroduced as the definition of `T_acc`.

This condition is satisfied.

The operational separation is:

`T_acc,0 → ΔT_acc → trajectory/use → capabilities/outcomes`

Round 2 contains explicit downstream observations. In the frozen operationalisation:

- R2 P4–P7 are treated as trajectory/use observations;
- R2 P9–P11 are treated as capability-result observations;
- the independent endpoint `Y = raven_r2 ∈ [0,36]` is constructed from 36 Raven items.

The outcome is therefore not used to define accessibility. The public study reports follow-up measurement of XO proficiency, academic effort, academic achievement and cognitive skills, confirming that post-intervention observations exist beyond the accessibility layer. The ICPSR catalogue describes the randomized trial and its follow-up findings, including the Raven cognitive endpoint. citeturn0search9

**P5 verdict: PASS.**

## 3. P6 — treatment / counterfactual

The causal assignment variable is:

`Z = won_lottery`

The bounded representation does not substitute either implementation receipt or school treatment condition for individual assignment.

- `won_lottery` = randomized lottery assignment;
- `received_laptop` = implementation/compliance/effective exposure;
- `treatment_school` = school-level experimental condition.

The previously inspected student-to-school linkage and school-pair structure establish that the school condition is not interchangeable with individual lottery assignment. The public study is explicitly described as a randomized controlled trial in which approximately 1,000 children were randomized to receive XO laptops for home use. citeturn0search9turn0search0

Therefore a credible treatment/counterfactual contrast exists for the bounded TR-132 representation.

**P6 verdict: PASS.**

## 4. P7 — public independent reproducibility

P7 is intentionally retained as **PROVISIONAL**, not promoted to unconditional PASS.

### Public availability

The V2 replication package is publicly listed by openICPSR and was published as Version V2 on 2024-03-28. The public package contains separate material for auxiliary data, instruments, original/follow-up data and results. citeturn0search0turn0search2turn0search3

The Round 1 public folder exposes the student files and other study data; the Round 2 folder exposes `cestudiante_g3-6_p1_r2.dta`, `cestudiante_g3-6_p2_r2.dta`, `matrices_g3-6_r2.dta`, `percepciondocente_g3-6_r2.dta`, and `xo_g3-6_r2.dta`. citeturn0search1turn0search4

The auxiliary folder publicly exposes `listas_final.dta` and `school_pairs_final.dta`, which are material to reconstructing the assignment/school linkage. citeturn0search2

### Why provisional

Public availability is established, but public availability is not equivalent to independent reproduction.

A complete P7 closure still requires an independent local executor to:

1. obtain the frozen V2 package without relying on the primary analysis execution;
2. verify package integrity and required inputs;
3. execute the frozen reconstruction/replication procedure;
4. record the execution environment and result hashes/logs;
5. demonstrate that the required bounded accessibility and treatment/counterfactual structures can be reconstructed from the public package without unpublished data or analyst intervention.

No such full independent execution is claimed by this record.

The repository itself states that the material is distributed exactly as received from the depositor and that ICPSR has not reviewed, checked, or processed it. This does not invalidate P7; it is precisely why the execution component must remain separately audited. citeturn0search0

**P7 verdict: PASS PROVISIONAL.**

## 5. Information firewall

P5–P7 do not authorize any of the following substitutions:

- outcome → accessibility;
- realized use → accessibility;
- laptop receipt → randomized assignment;
- school treatment condition → individual lottery assignment;
- public availability → completed independent reproduction.

These distinctions remain frozen for subsequent execution.

## 6. Relationship to P4

P4 is already closed by:

`TGCV_C09_OLPC_PERU_TR132_P4_EVIDENCE_RECORD_001.md`

P5–P7 build on that bounded construction but do not broaden `U*` or `T_acc`.

The resulting gate state is:

`P1 PASS`
`P2 PASS`
`P3 PASS`
`P4 PASS — bounded transformational-space operationalisation`
`P5 PASS`
`P6 PASS`
`P7 PASS PROVISIONAL`
`P8 NOT AUTHORIZED`

## 7. Required next action

The next operation is a **P7 independent reproducibility execution**, not a claim-matrix or RMA update.

Execution must be performed independently of the prior interpretive analysis, using only the frozen/public V2 package and the frozen execution specification. Its purpose is to convert P7 from provisional to definitive only if the reconstruction succeeds under the predefined acceptance criteria.

No C09 claim upgrade, RMA update, Evidence-to-Claim Matrix promotion, or TGCV Core change follows automatically from this record.
