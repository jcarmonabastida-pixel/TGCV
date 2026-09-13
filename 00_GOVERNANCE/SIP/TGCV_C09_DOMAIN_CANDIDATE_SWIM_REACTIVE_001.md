# TGCV — C09 Domain Candidate 001 — SWIM Reactive

**Status:** `CANDIDATE — PRE-EXECUTION AUDIT / NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent gate:** `TGCV_C09_PRE_EXECUTION_DOMAIN_IDENTIFICATION_GATE_001.md`

## 1. Candidate selection rationale

`SWIM Reactive-0` is selected as the first concrete C09 domain candidate because the canonical evidence already contains, in one bounded exemplar:

`S_t,C_t → Pτ(S_t,C_t) → T_acc,t → ΔT_acc,t → selected τ_t → S_{t+1},C_{t+1}`.

The existing evidence reconstructs multiple accessibility-space changes and ordered subsequent transformations/state transitions, while explicitly stopping short of a causal claim. This makes SWIM the closest existing domain to the C09 causal-design requirement without requiring a new scientific domain to be introduced prematurely.

This selection is a design choice, not evidence of C09 causality.

## 2. Existing evidence basis

The current evidence matrix records SWIM Reactive-0 as bounded operational evidence for changing `T_acc`, and the SWIM trajectory-linkage reconstruction as bounded evidence for ordered subsequent selected transformations and state transitions. Both explicitly exclude causal interpretation. fileciteturn22file0L2-L2

Reactive2 additionally provides bounded methodological separation between candidate/accessibility representation and native policy selection, while its A8 comparison remains `NOT_COMPARABLE`. This is useful for design but does not establish policy-independent accessibility under identical matched state/context. fileciteturn22file0L2-L2

## 3. Proposed C09 unit

**Unit:** a frozen SWIM decision point `(S0,C0)` immediately before an accessibility-changing condition is introduced, with:

- candidate transformation universe frozen;
- accessibility semantics frozen;
- pre-treatment `T_acc,0` reconstructed;
- intervention assigned before subsequent trajectory observation;
- subsequent native adaptation trajectory observed over fixed horizon `H`.

The exact decision-point sampling rule remains to be specified in the execution protocol.

## 4. Candidate intervention concept

The candidate intervention would alter an enabling condition that changes which transformations satisfy the frozen accessibility predicate, while leaving the candidate transformation identity and trajectory scoring rule unchanged.

The principal design candidate is a controlled perturbation of a resource/condition governing transformation admissibility in SWIM, followed by observation of the native adaptation trajectory rather than forced execution of a target transformation.

**Critical unresolved issue:** a resource/condition perturbation may itself alter system state or native policy inputs independently of `T_acc`. Therefore this candidate cannot yet be treated as a valid C09 intervention.

## 5. Direct-effect exclusion test

Required condition:

`intervention → ΔT_acc`

must be distinguishable from:

`intervention → direct change in trajectory mechanism`.

For the present candidate, this condition is **NOT YET DEMONSTRATED**.

A valid design must show that the manipulated condition changes accessibility while any independent change to the trajectory mechanism is either absent, held constant, or separately identifiable.

## 6. Counterfactual candidate

Preferred construction is a matched treatment/control pair or randomized assignment over otherwise frozen decision points, using the same accessibility rule, trajectory definition and observation horizon.

A simple comparison of existing Reactive-0 and Reactive2 runs is explicitly rejected as a causal counterfactual because their predecision states/histories are not established as identical.

## 7. Candidate-domain screening

| Criterion | Current disposition |
|---|---|
| State/context freeze | `PASS — conceptually supported` |
| Accessibility observability | `PASS — bounded existing reconstruction` |
| Accessibility manipulation | `OPEN — intervention not yet validated` |
| Outcome independence | `OPEN — direct-effect separation not yet demonstrated` |
| Counterfactual | `OPEN — new controlled construction required` |
| Temporal ordering | `PASS — designable` |
| Confounding | `OPEN — protocol-specific identification required` |
| Reconstruction | `PASS — existing infrastructure supports bounded reconstruction` |
| Scope | `PASS — bounded SWIM exemplar only` |

## 8. Decision

**SWIM Reactive is an admissible C09 candidate domain for further design, but it does not pass the Pre-Execution Domain / Identification Gate yet.**

The unresolved blockers are specifically:

1. demonstrate an intervention that changes `T_acc`;
2. demonstrate that the intervention does not directly encode the target trajectory;
3. define and justify the treatment/control or counterfactual construction;
4. freeze the concrete decision unit, horizon and trajectory criterion.

## 9. Authorization boundary

`EXECUTION AUTHORIZATION = NONE`

No new SWIM execution, dataset acquisition, rerun or claim upgrade is authorized by this artifact.

**Next operation:** develop the concrete SWIM intervention/counterfactual design and audit the direct-effect exclusion condition before any execution protocol is drafted.
