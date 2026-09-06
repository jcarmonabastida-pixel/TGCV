# DR-026A — EXT-1.1 Rust T_acc Representation Ex-Ante Design v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Scope:** Computational representation of `T_acc^(R*)` for the EXT-1.1 Rust confirmatory comparison  
**Depends on:** DR-020, DR-021, DR-022, DR-023, DR-024, DR-025, DR-025A, DR-026  

## 1. Governing question

What is the minimum deterministic, reconstructible and outcome-independent representation of `T_acc^(R*)` that preserves information about accessible transformations without reducing that object prematurely to a generic scalar or introducing information not contained in the frozen resolver output?

The representation must permit a symmetric comparison against the frozen conventional baseline `B(v_o)` while preserving the distinction between:

`T(e)` → candidate universe  
`R*` → admissibility and selection  
`T_acc^(R*)` → resulting accessible transformation set.

No outcome, association, effect size, significance result, sampling result or model-fitting result may contribute to this design.

## 2. Frozen upstream object

For an origin release `v_o`, DR-020 defines the candidate universe for each dependency edge and DR-021 defines the resolver selection rule. DR-022 leaves the resource predicate inactive (`TRUE`).

Therefore the normative analytical object is:

`T_acc^(R*) (v_o) = { (v_o, p_d, v_d*) }`

where each `v_d*` is the maximal eligible target release satisfying the frozen supported constraint and temporal cutoff.

The representation defined here MUST be a deterministic function of that object and its frozen provenance. It MUST NOT re-resolve dependencies using a different policy.

## 3. Representation candidates considered ex ante

### 3.1 Cardinality representation

`A_count(v_o) = |T_acc^(R*)(v_o)|`

This is a valid scalar summary of the number of accessible dependency-target transformations.

It is not sufficient as the sole primary representation because two origins can have the same cardinality while having different accessible target identities and version states.

### 3.2 Structural profile representation

A deterministic profile may retain structural properties derivable from the resolved transformation collection, including:

- number of accessible transformations;
- number of distinct target packages;
- number of distinct target versions;
- resolved-to-declared dependency ratio, where the denominator is the frozen raw declaration count `D_o`;
- multiplicity/profile information over target packages or versions, when deterministically defined.

These summaries may be useful secondary representations, but any scalarization discards relational identity. They therefore do not constitute the normative representation by themselves.

### 3.3 Relational canonical representation

The primary representation candidate is the canonical resolved transformation collection itself:

`A_rel(v_o) = canonical_sort({(p_d, v_d*)})`

with tuples sorted deterministically by canonical target package identifier and target version identifier/string according to a frozen lexical serialization rule. The origin identifier is implicit from the observational unit and is not repeated as a predictive feature.

This representation preserves the identity of the accessible transformations without introducing outcome-derived information.

## 4. Proposed primary representation

The ex-ante primary representation is a **canonical relational object** with a deterministic scalar cardinality summary available as an explicitly derived feature:

`TAcc_repr(v_o) = (A_rel(v_o), A_count(v_o))`

where:

- `A_rel` is the canonical collection of resolved `(target_package, target_version)` pairs;
- `A_count = |A_rel|`;
- no outcome or future information is used;
- no package identity of the origin is used as a predictive feature;
- no downloads, adoption, popularity, downstream success or later releases are used;
- no alternative resolver or post-hoc resolution is permitted.

The pair is intentionally not collapsed at this design stage into a single scalar. The statistical encoding required to make this object consumable by the final model remains a separate DR-026 decision and must itself be frozen before confirmatory fitting.

## 5. Representation invariants

The accepted representation MUST satisfy all of the following:

**T1 — Determinism.** Identical frozen inputs produce identical representation and serialization.

**T2 — Resolver fidelity.** Every represented transformation is produced by the normative `R*` implementation and no non-normative resolver semantics are introduced.

**T3 — Temporal validity.** No target release later than the origin release is represented.

**T4 — No outcome leakage.** Representation construction does not inspect `Y_180` or any post-origin activity.

**T5 — No baseline leakage.** Construction does not depend on model features selected for `B` or on baseline performance.

**T6 — No adaptive compression.** Feature reduction, hashing, truncation, frequency filtering or manual selection based on the observed data or outcome is prohibited unless independently frozen ex ante.

**T7 — Permutation invariance.** Source row order cannot alter the representation.

**T8 — Empty-set validity.** Origins with zero accessible transformations have a valid representation (`A_rel = ∅`, `A_count = 0`) and are not silently removed.

**T9 — Provenance preservation.** The representation remains traceable to origin release, target package, target version and the frozen resolver rule.

**T10 — Separation of layers.** Candidate generation, resolution and representation remain independently auditable.

## 6. What is not frozen by DR-026A

This decision does **not** freeze:

- statistical model family;
- train/test or cross-validation scheme;
- hyperparameters;
- categorical/vector encoding implementation;
- vocabulary construction rules, if any structured encoding is ultimately required;
- primary scoring metric;
- comparison statistic;
- class-imbalance handling;
- sampling beyond DR-024;
- confirmatory execution.

Those decisions remain within DR-026 and subsequent gates.

## 7. Required audit

Before acceptance, an implementation audit MUST demonstrate:

1. reconstruction of `T_acc^(R*)` from the frozen Rust dataset and resolver;
2. deterministic canonical ordering;
3. equality of representation under source-row permutation;
4. correct cardinality;
5. preservation of empty accessible sets;
6. absence of future target releases;
7. absence of outcome, baseline-performance and post-origin inputs;
8. no alternate resolver semantics;
9. reproducible replay;
10. no confirmatory model fitting or outcome analysis.

The audit should stream the frozen dataset and must not require extraction of the full ZIP or loading the complete raw dataset into memory.

## 8. Falsification conditions

The design is rejected or revised if any of the following is demonstrated:

- the representation changes under source-row permutation;
- the representation contains a target release after the origin boundary;
- two identical resolver outputs serialize differently;
- an empty `T_acc` cannot be represented;
- representation requires outcome or post-origin information;
- representation cannot be reconstructed from frozen inputs;
- representation silently applies semantics outside normative `R*`;
- the proposed primary representation is shown to be merely a renamed scalar baseline feature rather than a representation of accessible transformations.

## 9. Decision boundary

DR-026A is an **ex-ante representation-design gate**, not an empirical result.

Acceptance of DR-026A would freeze the representation of `T_acc^(R*)` for the subsequent model/evaluation specification. It would not authorize confirmatory execution by itself.

The next gate after acceptance is the completion and audit of DR-026 model/evaluation specification, including the exact encoding of the accepted `T_acc` representation and the symmetric evaluation protocol against `B`.

**NO CONFIRMATORY EXECUTION IS AUTHORIZED BY THIS DOCUMENT ALONE.**
