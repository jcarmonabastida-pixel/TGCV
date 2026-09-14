# TGCV C10-C — C10C-002 Data-Level Admission Package Specification 001

**Status:** FROZEN — DATA-LEVEL AUDIT PACKAGE SPECIFICATION ONLY
**Date:** 2026-09-14
**Candidate:** C10C-002 — *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*
**Study:** McIntosh, Alegría, Ordóñez & Zenteno (2018), AEJ Applied Economics
**Replication:** OpenICPSR 113705, V1
**Predecessor:** `TGCV_C10_C_CANDIDATE_C10C002_MEXICO_DOCUMENTARY_VARIABLE_AUDIT_001.md`

## 1. Purpose

This document freezes the candidate-specific admission contract for the next **controlled data-level variable audit** of C10C-002.

It does not authorize dataset acquisition, empirical reconstruction, causal estimation, or claim-level admission. It defines exactly what a later authorization may inspect, what must be established, which derived quantities are admissible, and when the operation must stop.

The frozen C10-C design is unchanged. The audit remains a test of whether the candidate can operationalize:

`Z → structural state change → T_acc,0/T_acc,1 → ΔT_acc → downstream pathway → V`

## 2. Admission question

The data-level audit shall answer one question:

> Can the documented infrastructure intervention be reconstructed from the replication materials as a reproducible structural state transition that yields a defensible `T_acc,0`, `T_acc,1`, and `ΔT_acc`, while preserving causal exposure, downstream outcomes, value measurement, and interference as distinct objects?

A positive answer is necessary for empirical C10-C admission. It is not sufficient for a TGCV claim upgrade or causal result.

## 3. Frozen input boundary

The next controlled operation may inspect only the following OpenICPSR 113705 V1 materials, once a separate acquisition/inspection authorization exists:

### 3.1 Documentation materials

1. Replication-package README / metadata documentation.
2. Study questionnaire or codebook material included in the public replication deposit.
3. Household analysis script.
4. Real-estate analysis script.

### 3.2 Data materials

5. Household dataset identified by the V1 replication metadata as the principal household DTA.
6. Real-estate dataset identified by the V1 replication metadata as the principal property-value data file.
7. Any explicitly documented companion data file required solely to decode variables in those two principal datasets.

### 3.3 Acquisition rule

The exact filenames, byte sizes, and SHA-256 hashes shall be recorded at acquisition time. No filename substitution, undocumented companion file, newer replication version, transformed download, or externally sourced dataset is admissible without a new package revision.

The documentary audit reported a household DTA of approximately 139.9 MB and a real-estate DTA of approximately 125.9 KB, and also identified an approximately 70.1 MB XLSX in the prior audit scope. These reported sizes are provenance clues, not frozen acceptance criteria; the V1 package metadata and acquired file hashes are authoritative.

## 4. Excluded inputs

The following are outside the frozen admission boundary unless a new package is issued:

- any non-V1 replication version;
- newly constructed or externally downloaded datasets;
- data from other studies;
- variables obtained from outcome tables rather than source data;
- post-treatment variables used to define structural accessibility;
- property-value, rent, private-investment, social-capital, crime, satisfaction, or other downstream outcomes used inside `P_τ`;
- any researcher-created coding that changes source-variable meaning;
- any causal estimates generated before the admission audit is closed.

## 5. Audit units and provenance

The audit shall preserve the study's native hierarchy and establish explicit linkage among:

- municipality;
- randomized polygon;
- block / household observation, where applicable;
- professionally valued unbuilt lot;
- baseline 2009;
- follow-up 2012.

For every variable admitted into the structural reconstruction, record:

`source_file → variable_name → label/definition → coding → admissible values → missing codes → unit → time → geographic/unit level → transformation rule`

No variable is admitted merely because it appears correlated with treatment or value.

## 6. Variable audit domains

### A. Treatment / exposure

Audit exact variables and coding for:

- randomized treatment assignment `Z`;
- municipality saturation / assignment strata;
- polygon identifier;
- treatment-control linkage;
- any documented actual implementation / infrastructure realization measure.

The audit must determine whether actual realization is an observed component of `S_1`, while randomized assignment remains the causal exposure `Z`. These concepts must not be conflated.

### B. Structural infrastructure state

Audit the six infrastructure dimensions documented in the pre-analysis plan:

1. electricity;
2. piped water;
3. sewerage;
4. paved streets;
5. streetlights;
6. sidewalks / medians.

For each dimension determine:

- exact variable name(s);
- baseline and follow-up availability;
- coding and admissible values;
- missing-value conventions;
- unit of observation;
- spatial aggregation;
- whether the variable measures availability, quality, completion, exposure, or another construct;
- whether it is pre-treatment, post-treatment, or potentially affected by implementation;
- whether the documented infrastructure index can be reproduced exactly.

### C. Structural context

Audit only context variables required to define the structural state or interpret spatial/temporal linkage. Context variables must not be promoted into accessibility merely because they predict value.

### D. Value endpoint

Audit exact professional property-value variables, including:

- variable name(s);
- units and scale;
- valuation date / wave;
- lot identifier;
- baseline/follow-up linkage;
- treatment/control linkage;
- aggregation rule;
- missingness and exclusions;
- evidence that the endpoint remains independently defined from the TGCV accessibility construction.

The preferred endpoint remains change in professionally assessed raw land value for the relevant linked lots/aggregation, with the exact estimand frozen before any causal estimation.

### E. Downstream pathway variables

Private housing investment, rents and other downstream variables may be audited only to establish a non-circular pathway after `ΔT_acc` is constructed. They cannot be used to define `P_τ`.

## 7. Frozen TGCV representation test

The candidate structural state shall be represented as:

`S_t = (infrastructure state at the admissible native unit, context)`

and accessibility as:

`T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`

where `U_τ` is an explicitly enumerated operational universe of transformation families.

The audit must produce an auditable finite representation of `U_τ`. A vague statement that infrastructure enables "more opportunities" is insufficient.

### 7.1 Admissible transformation families

A candidate `τ` may represent an activity, service access, movement, connection, use, or other transformation that can be justified directly from the observed structural infrastructure and context.

Each admitted transformation must have:

- identifier;
- verbal definition;
- structural prerequisites;
- context prerequisites, if any;
- source-variable mapping;
- baseline/follow-up applicability;
- predicate `P_τ`;
- reason it is not itself a downstream outcome.

### 7.2 Prohibited construction

The following may not be used to define `T_acc` or `P_τ`:

- land/property value;
- rents;
- private housing investment;
- social capital;
- crime;
- satisfaction;
- income changes caused by treatment;
- treatment-effect estimates;
- any variable whose definition already incorporates the value endpoint.

## 8. Derived-variable rules

Derived variables are admissible only when they are deterministic functions of admitted source variables and their rule is frozen before execution.

### 8.1 Allowed

- harmonization of documented coding schemes;
- deterministic recoding of documented missing values;
- documented unit conversion;
- baseline/follow-up linkage using native identifiers;
- reproducible infrastructure index reconstruction when its published rule can be recovered;
- deterministic structural indicators;
- `T_acc,0`, `T_acc,1` and `ΔT_acc` derived solely from admissible structural/context inputs;
- explicitly documented spatial exposure measures required to represent saturation/interference, provided they do not encode outcomes.

### 8.2 Not allowed

- outcome-informed thresholds;
- thresholds chosen after inspecting treatment effects;
- latent accessibility scores fitted to property value;
- machine-learned accessibility definitions trained on outcomes;
- post hoc selection of transformations because they strengthen the value result;
- imputation rules that use downstream outcomes;
- redefining source variables to obtain a PASS.

## 9. T_acc construction test

The data-level audit shall execute the following sequence.

### T1 — Source identity
All source files are V1 and hashes are recorded.

### T2 — Structural variable recovery
All six documented infrastructure dimensions are either recovered at variable level or each exception is explicitly documented.

### T3 — Temporal linkage
Baseline and follow-up structural observations can be linked at a defensible native unit, with missingness and attrition explicitly characterized.

### T4 — Treatment/state separation
`Z` is retained as causal assignment/exposure. Actual infrastructure realization, if observed, is represented separately as structural state information rather than silently replacing `Z`.

### T5 — Transformation universe
`U_τ` is finite or operationally enumerable and each candidate transformation has a documented predicate.

### T6 — Predicate integrity
Every `P_τ` uses only admissible structural/context inputs and no downstream value information.

### T7 — Baseline/follow-up construction
`T_acc,0` and `T_acc,1` can be generated deterministically from the frozen rules.

### T8 — Transition
`ΔT_acc` can be computed or otherwise represented without introducing outcome information.

### T9 — Reproducibility
An independent rerun using the same frozen inputs and rules yields the same structural accessibility representation.

### T10 — Endpoint separation
The value endpoint can be linked independently of the accessibility construction and its baseline/follow-up definition is explicit.

**Admission requirement:** T1–T10 must PASS, or a failure must be shown to be non-material and explicitly dispositioned by governance. A material FAIL or unresolved BLOCKED condition prevents data-level admission.

## 10. Spillover and interference gate

Because assignment includes municipality-level saturation and the intervention has spatial structure, the audit must identify:

- native spatial identifiers;
- treatment saturation variables;
- plausible neighboring exposure measures, if directly constructible;
- the unit at which interference could operate;
- whether the intended causal estimand requires treatment saturation or spatial exposure terms.

No assumption of no interference may be inserted merely for convenience.

## 11. Reach and Trajectory gate

`Reach` and `Trajectory` are secondary constructs and must not be manufactured from value outcomes.

A candidate representation is admissible only if it is derived from structural states, accessible transformations, temporal linkage, or explicitly documented non-outcome mechanisms.

If no non-circular operational representation can be justified from the frozen data, the audit shall record **D6 unresolved for TGCV pathway construction** rather than inventing a proxy.

## 12. Stop conditions

The controlled operation must stop immediately and return **BLOCKED** if any of the following occurs:

1. The acquired package is not demonstrably OpenICPSR 113705 V1.
2. A required file cannot be provenance-linked.
3. Required structural variables cannot be identified without guessing.
4. Baseline/follow-up linkage cannot be established at a defensible unit.
5. The six infrastructure dimensions cannot be operationalized without outcome information.
6. `U_τ` cannot be made finite/operational without post hoc interpretation.
7. `P_τ` requires downstream value or outcome variables.
8. Treatment assignment and realized infrastructure cannot be separated sufficiently for the proposed reconstruction.
9. Missingness/attrition makes the structural transition non-reproducible and no pre-specified defensible handling exists.
10. Property-value linkage cannot be independently established.
11. Spillover/interference changes the causal estimand but cannot be represented or bounded.
12. Any proposed derived variable changes the semantic meaning of a source variable.
13. Any analysis begins to estimate treatment effects before the admission gate is closed.
14. Any evidence outside the frozen input boundary is introduced.

## 13. Output contract

The controlled data-level audit shall produce, at minimum:

1. variable-level provenance table;
2. structural-state dictionary;
3. treatment/state separation record;
4. `T_acc` transformation-universe specification;
5. deterministic `P_τ` definitions;
6. `T_acc,0` / `T_acc,1` construction record;
7. `ΔT_acc` result or explicit failure disposition;
8. value-endpoint linkage record;
9. spillover/interference assessment;
10. reproducibility/hash record;
11. PASS / FAIL / BLOCKED disposition for T1–T10;
12. candidate admission recommendation.

No causal estimate is part of this output contract.

## 14. Authorization boundary

**This specification is FROZEN.**

It does **not** authorize:

- downloading the replication data;
- inspecting the data files;
- executing replication code;
- constructing treatment effects;
- estimating causal effects;
- upgrading C10C-002 from B — PROMISING / EVIDENCE GAP;
- making a TGCV claim-level conclusion.

A separate authorization record may now permit the controlled acquisition and inspection of the exact V1 materials listed in Section 3.

## 15. Expected disposition after the next operation

The next controlled operation must return exactly one of:

- **ADMISSIBLE FOR EMPIRICAL EXECUTION** — T1–T10 PASS and no material unresolved gate remains;
- **PROMISING / EVIDENCE GAP REMAINS** — candidate remains B and a bounded additional audit is justified;
- **BLOCKED** — a frozen stop condition prevents valid reconstruction;
- **REJECTED FOR C10-C** — the candidate fails a material frozen requirement.

The package itself does not pre-judge which disposition will result.

## 16. Traceability

This specification operationalizes the next step explicitly required by:

`TGCV_C10_C_CANDIDATE_C10C002_MEXICO_DOCUMENTARY_VARIABLE_AUDIT_001.md`

The predecessor documentary audit established documentary PASS for study identity, causal design, value endpoint and replication provenance, while leaving the decisive TGCV-specific `ΔT_acc` reconstruction pending variable-level inspection.

**Frozen decision:** proceed to a separately authorized controlled data-level variable audit; do not redesign C10-C and do not perform empirical reconstruction or causal estimation at this stage.
