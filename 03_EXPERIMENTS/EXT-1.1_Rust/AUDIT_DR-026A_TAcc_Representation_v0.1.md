# AUDIT DR-026A — EXT-1.1 Rust T_acc Representation v0.1

**Status:** PASS — STRUCTURAL AUDIT  
**Decision gate:** DR-026A  
**Implementation:** `src/audit_dr026a_tacc_representation_v01.py` (performance implementation v0.2)  
**Input:** `rust_repos_2022_09_07.zip`  
**Mode:** PRE-CONFIRMATORY / STRUCTURAL ONLY  
**Execution date:** 2026-09-06  

## 1. Scope

This audit evaluates whether the proposed primary representation

`TAcc_repr(v_o) = (A_rel(v_o), A_count(v_o))`

is deterministic, reconstructible, resolver-faithful, temporally valid, row-order invariant, capable of representing empty sets, and free of outcome/post-origin/model information, as required by DR-026A.

No outcome labels, model fitting, sampling, association, effect-size, or significance computation was performed.

## 2. Execution evidence

The user executed the performance-mode audit against the frozen Rust ZIP. The implementation streamed `package_dependencies.csv` once and stored the derived T_acc set in temporary SQLite storage rather than materializing the dependency CSV or loading the complete raw dataset into memory.

Observed progress reached 3,500,000 dependency rows, covering the complete dependency table of 3,618,523 rows.

## 3. Structural observations

- `PACKAGE_COUNT`: 91,437
- `VERSION_COUNT`: 607,498
- `DEPENDENCY_ROWS`: 3,618,523
- `ORIGIN_COUNT_REPRESENTED`: 607,498
- `TACC_TRANSFORMATION_COUNT`: 3,197,479
- `NONEMPTY_ORIGINS`: 492,872
- `EMPTY_ORIGINS`: 114,626
- `RESOLVED_EDGE_COUNT`: 3,197,479
- `UNRESOLVED_EDGE_COUNT`: 421,044
- `UNSUPPORTED_REQUIREMENT_EDGE_COUNT`: 0
- `DUPLICATE_CANONICAL_RELATIONS_COLLAPSED`: 0
- `FUTURE_TARGETS_IN_TACC`: 0
- `ORIGIN_VERSION_MISSING_FROM_INDEX`: 0
- `TARGET_PACKAGE_MISSING_FROM_INDEX`: 0

Canonical ordering rule:

`origin_id,target_package_id,target_version_id,target_version`

Canonical T_acc SHA-256:

`5c8aa157552434e385d735679b2b482d41a05abe262edef86d06ce7a582d4664`

## 4. Representation checks

All required structural representation checks passed:

- `TACC_RELATIONAL_REPRESENTATION`: `canonical_resolved_pairs`
- `TACC_CARDINALITY_DERIVED`: `True`
- `TACC_ORIGIN_PACKAGE_ID_AS_FEATURE`: `False`
- `OUTCOME_AS_INPUT`: `False`
- `POST_ORIGIN_DATA_AS_INPUT`: `False`
- `BASELINE_B_AS_INPUT`: `False`
- `ALTERNATE_RESOLVER_AS_INPUT`: `False`
- `TACC_SERIALIZATION_DETERMINISTIC`: `True`
- `TACC_ROW_ORDER_INVARIANT_BY_SET_SEMANTICS`: `True`
- `TACC_ROW_ORDER_PERMUTATION_SMOKE_TEST`: `True`
- `TACC_EMPTY_SET_VALID`: `True`
- `TACC_FUTURE_TARGET_EXCLUSION`: `True`
- `TACC_RESOLVER_FIDELITY_BY_NORMATIVE_IMPLEMENTATION`: `True`
- `TACC_PROVENANCE_TRACEABLE`: `True`

The row-order invariant is established by canonical set semantics and an explicit permutation smoke test rather than by a second full reverse-order traversal of the complete dependency table. This is an implementation optimization and does not alter the representation definition.

## 5. Accounting and protocol integrity

- `FULL_RAW_DATASET_LOADED_IN_MEMORY`: `False`
- `DEPENDENCY_CSV_MATERIALIZED_IN_MEMORY`: `False`
- `TEMPORARY_DERIVED_SET_ON_DISK`: `True`
- `CONFIRMATORY_ANALYSIS_STARTED`: `False`
- `OUTCOME_PREVALENCE_COMPUTED`: `False`
- `ASSOCIATIONS_COMPUTED`: `False`
- `EFFECT_SIZES_COMPUTED`: `False`
- `SIGNIFICANCE_COMPUTED`: `False`
- `MODEL_FITTED`: `False`
- `SAMPLING_PERFORMED`: `False`

## 6. Audit conclusion

The execution satisfies the DR-026A structural audit requirements. In particular, the resulting object is a canonical relational representation of the normative `T_acc^(R*)`, with cardinality as a derived summary; it preserves 114,626 empty origins; contains no future targets; is deterministic and row-order invariant; and uses neither outcome nor post-origin information.

**`DR026A_STRUCTURAL_AUDIT_PASS: True`**

The audit therefore supports acceptance of the DR-026A representation design.

This audit does **not** constitute a predictive result and does not authorize confirmatory execution. Model/evaluation specification remains a separate ex-ante gate under DR-026.
