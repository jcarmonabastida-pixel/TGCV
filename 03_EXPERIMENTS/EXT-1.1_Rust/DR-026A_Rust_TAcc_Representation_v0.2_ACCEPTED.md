# DR-026A — EXT-1.1 Rust T_acc Representation v0.2

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION  
**Scope:** Computational representation of `T_acc^(R*)` for EXT-1.1 Rust  
**Audit:** `AUDIT_DR-026A_TAcc_Representation_v0.1.md`  

## Decision

The primary representation of the frozen accessible-transformation object is accepted as:

`TAcc_repr(v_o) = (A_rel(v_o), A_count(v_o))`

where:

`A_rel(v_o) = canonical_sort({(p_d, v_d*)})`

and

`A_count(v_o) = |A_rel(v_o)|`.

`A_rel` is the canonical relational collection of resolved target package/version pairs produced by the normative `R*` implementation. `A_count` is a derived cardinality summary and does not replace the relational object at the representation layer.

## Acceptance basis

The DR-026A structural audit passed on the frozen Rust dataset:

- 91,437 packages
- 607,498 package versions
- 3,618,523 dependency declarations
- 3,197,479 resolved T_acc transformations
- 492,872 origins with nonempty T_acc
- 114,626 origins with empty T_acc
- 0 duplicate canonical relations collapsed
- 0 future targets in T_acc
- 0 missing origin versions
- 0 missing target packages
- 0 unsupported requirement edges in the audited input

Canonical T_acc serialization:

`origin_id,target_package_id,target_version_id,target_version`

Audit SHA-256:

`5c8aa157552434e385d735679b2b482d41a05abe262edef86d06ce7a582d4664`

The audit established deterministic serialization, row-order invariance by set semantics plus permutation smoke test, empty-set validity, temporal validity, normative resolver fidelity, and provenance traceability.

The audit also confirmed that outcome labels, post-origin data, baseline B, alternate resolver semantics, model fitting, sampling, associations, effect sizes, and significance were not used.

## Normative constraints

1. `T_acc^(R*)` MUST be reconstructed only from the frozen DR-020/DR-021/DR-022 semantics.
2. `A_rel` MUST preserve the identity of accessible target package/version pairs and use deterministic canonical ordering.
3. `A_count` MUST equal the cardinality of `A_rel`.
4. Empty `T_acc` MUST remain representable as an empty relational object with cardinality zero.
5. No future target release may enter the representation.
6. No outcome, post-origin activity, downloads, adoption, downstream success, or other future information may enter the representation.
7. No alternative resolver semantics may be substituted.
8. No adaptive hashing, truncation, frequency filtering, manual feature selection, or other compression is permitted unless independently frozen ex ante under the DR-026 model/evaluation gate.
9. Origin package identity remains excluded as a predictive feature; the relational representation concerns accessible target transformations.
10. Provenance MUST remain traceable to origin release, target package, target version, and the normative resolver.

## Scope boundary

Acceptance freezes the representation of `T_acc^(R*)` for the subsequent model/evaluation specification. It does **not** freeze:

- statistical model family;
- train/test or cross-validation scheme;
- hyperparameters;
- model-compatible encoding/vectorization of the relational object;
- vocabulary construction, hashing or other representation compression if later independently justified;
- primary or secondary metrics;
- comparison statistic or decision rule;
- class-imbalance handling;
- confirmatory execution.

Those decisions remain open under DR-026 and its subsequent ex-ante gates.

## Governance boundary

This acceptance is methodological, not empirical. It establishes that the selected `T_acc` representation can be reconstructed deterministically and audited independently of the subsequent outcome and model comparison.

**NO CONFIRMATORY EXECUTION IS AUTHORIZED BY DR-026A ALONE.**
