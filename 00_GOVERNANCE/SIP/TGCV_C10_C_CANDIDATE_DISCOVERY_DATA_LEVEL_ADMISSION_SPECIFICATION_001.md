# TGCV — C10-C Candidate Discovery and Data-Level Admission Specification 001

**Status:** FROZEN — ADMISSION SPECIFICATION ONLY; NO CANDIDATE EXECUTION AUTHORIZED
**Date:** 2026-09-15
**Claim:** C10 — causal `ΔT_acc → ΔV`
**Parent gate:** `TGCV_C10_C_EMPIRICAL_DESIGN_GATE_001.md`

## 1. Purpose

Define the controlled filter for discovering and admitting a real-world candidate capable of testing the frozen C10-C causal design.

This specification is downstream of the frozen empirical design gate. It does not authorize acquisition, inspection, reconstruction or causal estimation of any candidate.

## 2. Candidate target

A candidate must permit the bounded causal architecture:

`Z → ΔS → ΔT_acc(U_τ*) → downstream path → V`

with an admissible counterfactual and independently defined value endpoint.

The search objective is therefore not to find a case with a positive result. It is to find a case in which the causal question is identifiable, reproducible and falsifiable before the result is known.

## 3. Mandatory candidate characteristics

A candidate is potentially admissible only if the available documentary record indicates all of the following can be reconstructed:

1. exact intervention/exposure identity;
2. causal unit and treatment assignment;
3. baseline structural state;
4. follow-up structural state or equivalent temporal state information;
5. a bounded, observable `U_τ*`;
6. deterministic accessibility predicates independent of value;
7. `T_acc,0`, `T_acc,1` and `ΔT_acc`;
8. an independently defined value endpoint `V`;
9. a credible counterfactual;
10. downstream outcome/value linkage;
11. interference or spillover structure;
12. sufficient provenance and reproducibility information.

## 4. Preferred evidence hierarchy

Candidates should be prioritized in this order:

1. randomized intervention with pre/post structural state and independent value endpoint;
2. strong quasi-experimental design with comparable structural and value measurements;
3. natural experiment with auditable identification assumptions;
4. other observational design only where confounding can be addressed without relying on post-treatment value information.

Synthetic-only cases, demonstrations, simulations and purely conceptual examples are not C10-C empirical candidates.

## 5. Minimum documentary pre-screen

Before any data acquisition, the public/documentary record must be sufficient to establish at least:

- source identity and version;
- intervention and unit of assignment;
- temporal structure;
- candidate structural variables;
- candidate value endpoint;
- causal identification design;
- existence of a counterfactual;
- enough information to judge whether `U_τ*` can be bounded.

If these cannot be established from documentary evidence, the candidate is not admitted to controlled acquisition.

## 6. Admission tests

### A — Provenance

Exact source, version, archive/deposit identity and reproducible acquisition route must be identifiable.

### B — Structural state

The candidate must contain observable variables that can define the relevant system state independently of downstream value.

### C — Accessibility reconstruction

A finite or operationally enumerable `U_τ*` must be definable before inspecting causal/value results. Every transformation must have a structural predicate and source mapping.

### D — Treatment/state separation

Treatment assignment must be distinguishable from realized structural state. Realized execution cannot be silently equated with accessibility.

### E — Value independence

The value endpoint must be independently defined and measured. It cannot be created by selecting variables because they respond favourably to the intervention.

### F — Causal identification

The candidate must support a defensible causal contrast, including an admissible counterfactual and explicit assumptions.

### G — Temporal ordering

The data must permit the ordering `baseline → intervention/state change → accessibility change → downstream observation → value` or a justified equivalent.

### H — Interference

Spatial, network, cluster or saturation spillovers must be identifiable sufficiently to determine whether the intended estimand remains valid.

### I — Reproducibility

Source files, code or computational definitions, variable provenance and environment information must be recoverable sufficiently for independent reconstruction.

## 7. Hard exclusion rules

Reject the candidate at pre-screen if any of the following is already evident:

- value is the definition of accessibility;
- `P_τ` would need outcome/value information;
- no structural state exists from which `T_acc` can be reconstructed;
- no credible treatment/intervention variation exists;
- no defensible counterfactual exists;
- value is only inferred retrospectively;
- causal identification depends on post-treatment adjustment that cannot be avoided;
- provenance is irreparably incomplete;
- the candidate is synthetic-only;
- the candidate is being selected because its reported result is positive;
- acquisition would require adding an external dataset not covered by the documented candidate design without a new admission decision.

## 8. Candidate scoring principle

No score may incorporate the observed sign or statistical significance of a causal/value estimate.

Prioritization should instead reflect:

- structural observability;
- accessibility reconstructibility;
- causal identification strength;
- value endpoint independence;
- counterfactual quality;
- temporal linkage;
- interference tractability;
- provenance completeness;
- reproducibility feasibility;
- boundedness of `U_τ*`.

A high-priority candidate is one with high identification and reconstruction feasibility, not one with a likely positive value effect.

## 9. Controlled acquisition boundary

Only after a candidate passes documentary pre-screen may a separate candidate-specific authorization permit acquisition/inspection.

That authorization must freeze:

- exact source/version;
- permitted files;
- acquisition hashes;
- inspection questions;
- prohibited operations;
- stop conditions;
- output contract.

No causal estimation is authorized by candidate-specific acquisition alone.

## 10. Candidate-level stop conditions

Stop and classify the candidate as `BLOCKED` or `REJECTED` if controlled inspection reveals:

- structural variables cannot be mapped reproducibly;
- `U_τ*` cannot be bounded without post-hoc selection;
- treatment and structural state cannot be separated;
- value endpoint is not independent;
- counterfactual assumptions fail;
- interference invalidates the stated estimand;
- missingness/attrition prevents valid linkage;
- provenance requires guessing;
- reproducibility cannot be demonstrated.

## 11. Decision states

| State | Meaning |
|---|---|
| `DISCOVERY-CANDIDATE` | Documentary record appears potentially compatible; no acquisition authorized. |
| `PRIORITY-CANDIDATE` | Strong documentary compatibility; candidate may be submitted for acquisition authorization. |
| `BLOCKED` | A required condition cannot currently be established without prohibited inference. |
| `REJECTED` | Candidate violates a hard admission condition. |
| `ADMITTED-FOR-CONTROLLED-INSPECTION` | Separate authorization has been issued; still no causal execution. |

## 12. Relation to previous C10 work

C10C-002 remains closed and cannot be reopened merely because future candidates are sought.

The methodological criterion of minimum-sufficient bounded `U_τ*` is binding: candidates should be evaluated for the smallest empirically sufficient transformation universe rather than maximum theoretical coverage.

C09 remains upstream evidence for accessibility-to-trajectory causality and must not be represented as evidence of causal value attribution.

## 13. No-execution boundary

This specification authorizes **neither**:

- broad dataset search as an empirical operation;
- data download;
- data inspection;
- variable extraction;
- reconstruction;
- causal estimation;
- claim upgrade.

It freezes the admission filter only. A subsequent governed operation may perform candidate discovery against this specification; acquisition requires a separate candidate-specific authorization.

## 14. Decision

**C10-C CANDIDATE DISCOVERY / DATA-LEVEL ADMISSION SPECIFICATION: FROZEN.**

The programme may now proceed to a governed candidate-discovery operation using this filter. No candidate has been admitted and no empirical execution has been authorized by this artifact.
