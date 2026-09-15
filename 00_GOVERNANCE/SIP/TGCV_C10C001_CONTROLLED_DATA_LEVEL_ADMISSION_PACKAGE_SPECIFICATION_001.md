# TGCV C10-C — C10C-001 Egypt Controlled Data-Level Admission Package Specification 001

## Status

`FROZEN — DATA-LEVEL ADMISSION PACKAGE SPECIFICATION ONLY; EMPIRICAL EXECUTION NOT AUTHORIZED`

## 1. Purpose

This specification freezes the evidence boundary and inspection protocol for the next controlled operation on C10C-001 (Egypt). It follows the documentary admission audit and is intended only to determine whether the public replication materials support a reproducible, bounded TGCV structural reconstruction.

It does **not** authorize causal estimation, replication of published estimates, or claim upgrade.

## 2. Candidate identity

Atkin, Khandelwal & Osman, *Exporting and Firm Performance: Evidence from a Randomized Experiment* (QJE 2017).

The experiment randomly assigned 219 eligible rug producers to an opportunity-to-export treatment (74) or comparison (145). The intervention involved access to export orders through Hamis Carpets and foreign buyers, with repeated firm-level observation over the study period.

## 3. Admitted evidence boundary

The controlled inspection may use only the exact public replication package associated with the study and its documented metadata/codebook/instructions.

At acquisition, the executor must record for every acquired artifact:

- exact filename;
- byte size;
- SHA-256;
- source/project identifier;
- acquisition timestamp;
- any documented version identifier.

No substituted, transformed, silently updated or externally supplemented file may enter the admitted package.

If the public route contains multiple releases, only the release explicitly corresponding to the study's replication materials may be admitted, with the exact version frozen before inspection.

## 4. Inspection domains

### A — Experimental intervention and unit

Recover the exact randomized treatment variable, experimental unit, assignment timing, comparison condition and any stratification/blocking variables.

Treatment assignment must remain distinct from:

- actual exporting;
- number/value of orders received;
- production decisions;
- buyer acceptance;
- post-treatment performance.

### B — Structural firm state

Identify observed pre/post variables that plausibly encode capabilities, constraints or conditions relevant to the firm's export-production transformation space.

Candidate variables must be admitted only when their definition, coding, unit, timing and provenance are documented independently of outcomes.

Do not infer structural state from treatment status, profit, productivity outcomes, export take-up or later buyer orders.

### C — Bounded transformation universe `U_τ*`

Construct the smallest sufficient candidate universe of transformations that can be supported directly by admitted structural variables.

For each candidate transformation record:

- identifier;
- textual definition;
- prerequisite state;
- post-transformation state;
- source variable(s);
- predicate `P_τ(S,C,L)`;
- time reference;
- admissible values;
- missing-value treatment;
- reason it is structural rather than outcome-derived.

No transformation may be selected because it produces a larger or more favorable value effect.

### D — Accessibility reconstruction

Determine whether `T_acc,0`, `T_acc,1` and `ΔT_acc` can be reconstructed reproducibly from `U_τ*`.

The inspection must explicitly test whether the public data support a deterministic mapping:

`source variables → S_t,C_t,L_t → P_τ → T_acc,t → ΔT_acc`.

If the mapping cannot be established without heuristic aggregation, outcome-informed thresholds, treatment substitution or undocumented assumptions, record an evidence limitation rather than repairing it heuristically.

### E — Independent value endpoint

Identify the exact economic endpoint used for the TGCV value linkage and document:

- variable name;
- conceptual definition;
- unit;
- currency/scale;
- time horizon;
- baseline/follow-up availability;
- missing-value codes;
- aggregation level;
- construction/derivation provenance;
- independence from structural accessibility variables.

Published treatment effects may be recorded as documentary context only; they must not be used to define or select the endpoint.

### F — Downstream pathway

Preserve the distinction among:

`randomized opportunity → realized exporting/take-up → buyer interaction → learning/quality/productivity → economic value`.

Post-treatment exporting or orders must not be relabeled as the initial accessibility state unless an explicit pre-treatment structural definition independently supports that interpretation.

### G — Interference and selection

Inspect documentary and data-level evidence for:

- geographic or market spillovers;
- treatment contamination;
- differential attrition;
- endogenous take-up;
- post-treatment selection;
- dependence among firms.

Non-random take-up must not be substituted for randomized treatment assignment.

### H — Reproducibility

Determine whether an independent executor can reproduce the structural reconstruction from the frozen inputs without access to prior TGCV results or outcome-informed decisions.

Record software/environment requirements and any deterministic extraction/transformation procedure needed for reproduction.

## 5. Mandatory admission tests

**T1** — source identity and version integrity.

**T2** — treatment assignment provenance and experimental-unit identity.

**T3** — pre/post structural-state provenance.

**T4** — treatment/state separation.

**T5** — bounded `U_τ*` is finite, explicit and outcome-independent.

**T6** — accessibility predicates are reproducible from admitted state/context variables.

**T7** — `T_acc,0`, `T_acc,1`, `ΔT_acc` are reconstructible without heuristic or outcome-informed aggregation.

**T8** — value endpoint is independently defined and linked to the same admissible observational unit/time horizon.

**T9** — downstream mechanisms and realized take-up are not conflated with accessibility.

**T10** — interference/selection and reproducibility conditions are sufficiently documented for a subsequent causal-design decision.

## 6. Hard stop conditions

Stop the operation and record the specific limitation if any of the following occurs:

- exact source/version cannot be frozen;
- treatment identity or experimental unit cannot be established;
- structural variables lack sufficient provenance;
- `U_τ*` requires outcome-informed selection;
- accessibility requires using treatment, take-up or value as a proxy;
- polygon/firm aggregation or thresholding requires an undocumented rule;
- value endpoint provenance cannot be established;
- structural and value variables cannot be separated;
- interference/selection materially changes identification and cannot be bounded;
- reproducibility requires prior TGCV interpretation or unavailable evidence;
- any new external dataset would be required.

## 7. Output contract

The controlled inspection must produce, at minimum:

1. immutable file manifest and SHA-256 record;
2. treatment/experimental-unit dictionary;
3. structural-state provenance table;
4. treatment-versus-state separation record;
5. candidate bounded `U_τ*` table, or explicit failure reason;
6. `P_τ` definitions, or explicit failure reason;
7. `T_acc,0`, `T_acc,1`, `ΔT_acc` feasibility result;
8. independent value-endpoint specification;
9. downstream pathway and take-up separation;
10. interference/selection assessment;
11. reproducibility/environment record;
12. T1–T10 disposition;
13. candidate admission decision.

## 8. Decision states

The controlled operation may conclude only with one of:

- `ADMISSIBLE FOR EMPIRICAL EXECUTION`;
- `PROMISING / EVIDENCE GAP REMAINS`;
- `BLOCKED`;
- `REJECTED FOR C10-C`.

A positive published treatment effect is not an admission criterion.

## 9. Authorization boundary

This specification authorizes **only the controlled acquisition and data-level inspection of the exact public replication materials once acquired under this frozen boundary**.

It does not authorize:

- causal estimation;
- reproduction of the published causal estimates as a result claim;
- value regression;
- mediation analysis;
- outcome-informed transformation selection;
- post-hoc model selection;
- use of undocumented variables;
- external/new datasets;
- claim upgrade;
- reopening C10C-002 or C09.

Any empirical execution requires a subsequent, explicit execution authorization after the admission decision.
