# TGCV C10-C — C10C-002 Controlled Acquisition & Inspection Authorization 001

**Status:** AUTHORIZED — CONTROLLED DATA-LEVEL ACQUISITION AND INSPECTION ONLY
**Date:** 2026-09-14
**Candidate:** C10C-002 — *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*
**Replication:** OpenICPSR 113705, V1
**Governing specification:** `TGCV_C10_C_CANDIDATE_C10C002_DATA_LEVEL_ADMISSION_PACKAGE_SPECIFICATION_001.md`
**Methodological criterion:** `TGCV_C10_METHODOLOGICAL_CRITERION_BOUNDED_EMPIRICAL_CAUSAL_SUPPORT_001.md`

## 1. Authorization

This record authorizes the next controlled operation for C10C-002: acquisition and inspection of the exact OpenICPSR 113705 V1 materials listed in the frozen admission package, for the sole purpose of determining whether the candidate can support a reproducible, bounded TGCV structural reconstruction.

The authorization is limited to data/document inspection and provenance reconstruction. It does not authorize causal estimation or claim-level admission.

## 2. Authorized inputs

Only the following may be acquired/inspected:

1. V1 README / metadata documentation;
2. study questionnaire/codebook material included in the V1 package;
3. household analysis script;
4. real-estate analysis script;
5. principal household DTA identified by V1 metadata;
6. principal real-estate data file identified by V1 metadata;
7. explicitly documented companion data file required solely to decode variables in those principal datasets.

At acquisition, record exact filename, byte size and SHA-256 for every acquired file.

## 3. Required inspection objective

The operation must establish, without causal estimation:

- exact treatment/exposure variables and identifiers;
- exact variables for the six documented infrastructure dimensions;
- baseline/follow-up availability and native linkage;
- treatment versus realized structural state separation;
- value-endpoint variables and independent linkage;
- spatial/saturation information relevant to interference;
- a minimum sufficient bounded transformation universe `U_τ*`, if one can be justified;
- deterministic candidate predicates `P_τ` using only structural/context inputs;
- feasibility of constructing `T_acc,0`, `T_acc,1` and `ΔT_acc`.

## 4. Mandatory bounded-universe discipline

The inspection shall not attempt to enumerate the maximum conceivable universe of infrastructure-enabled transformations.

It shall first seek the **minimum sufficient `U_τ*`** satisfying the frozen methodological criterion: observable/reconstructible, endpoint-independent, explicit, non-trivial, causally connected and reproducible.

Selection of `U_τ*` must occur before any causal estimation and may not be informed by treatment-effect or value-result strength.

## 5. Prohibited operations

The following remain unauthorized:

- causal estimation;
- treatment-effect estimation;
- hypothesis selection based on value results;
- outcome-informed construction of `P_τ`;
- latent accessibility scores fitted to outcomes;
- post hoc transformation selection to strengthen an association;
- claim-level upgrade;
- modification of the frozen C10-C gate or admission package;
- use of datasets or files outside the frozen V1 boundary.

## 6. Stop conditions

Return **BLOCKED** immediately if provenance, variable identity, baseline/follow-up linkage, structural operationalization, endpoint separation, interference representation, or frozen-boundary compliance cannot be established without guessing or post hoc reconstruction.

A bounded universe that is too narrow to produce a substantive structural transition is not a valid PASS merely because it is easy to operationalize.

## 7. Required output

The operation shall produce a controlled inspection record containing:

1. acquired-file manifest and SHA-256 hashes;
2. variable-level provenance table;
3. six-dimension structural-state dictionary;
4. treatment/state separation record;
5. minimum sufficient `U_τ*` proposal or explicit failure disposition;
6. deterministic `P_τ` definitions or explicit failure disposition;
7. baseline/follow-up linkage assessment;
8. `T_acc,0` / `T_acc,1` / `ΔT_acc` construction feasibility;
9. value-endpoint linkage assessment;
10. spillover/interference assessment;
11. T1–T10 disposition;
12. recommendation for the next governance stage.

## 8. Decision boundary

The only permitted outcomes of this authorization are:

- **ADMISSIBLE FOR EMPIRICAL EXECUTION**;
- **PROMISING / EVIDENCE GAP REMAINS**;
- **BLOCKED**;
- **REJECTED FOR C10-C**.

No causal result may be reported as part of this operation.

## 9. Traceability

This authorization follows the frozen documentary audit and the frozen data-level admission package specification. It also operationalizes the C10 methodological criterion that empirical testing should begin from a minimum sufficient bounded transformation universe rather than maximum theoretical breadth.

**Authorization boundary:** acquire and inspect; do not estimate causality.
