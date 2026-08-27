# TR-181E — Semantic Audit v0.2

**Status:** PASS WITH REQUIRED REVISIONS — NO FREEZE
**Date:** 2026-08-28

## Scope

Audit of the candidate R engine against the Core-derived operationalisation. This is a semantic audit, not an empirical test.

## Findings

### 1. Accessibility is primary; summary statistics are secondary

The canonical object is `T_acc(S)`. Any R feature must be a declared representation of that object, not merely a convenient graph statistic.

### 2. Remove unjustified predicates

`objective_is` and generic `flag_is` are not retained as part of the minimal predicate vocabulary unless their ontological role in `(S,C,L)` is explicitly justified. They are implementation conveniences, not Core primitives.

### 3. Effects require explicit semantics

`eff` must be a typed description of the potential state transition. It does not determine accessibility by itself, but its schema must be valid and auditable. Recursive execution remains prohibited.

### 4. Candidate type labels are operational categories

The six labels may be used for controlled representation only if their predicates and effects are explicitly defined. They must never be presented as recovered historical EMP-1.1 families or as necessary TGCV ontological primitives.

### 5. Summary features require separate justification

`total_accessible` is the direct cardinality of `T_acc` and is therefore canonical. Class counts are admissible only after class semantics are frozen. Entropy, incidence density and other derived statistics are not automatically canonical and should be treated as optional sensitivity representations unless theoretically justified before freeze.

### 6. B/R separation

No claim of non-duplication can yet be certified because the exact B schema and the final candidate feature encoding have not been jointly frozen. This remains a mandatory gate.

## Revised freeze path

1. Freeze the candidate transformation schema and predicate vocabulary.
2. Define typed `eff` semantics without recursive execution.
3. Define canonical R as the minimal representation of `T_acc`.
4. Treat higher-order summaries as pre-declared sensitivity features, not silently canonical features.
5. Map every R feature against B and prove no accidental duplication.
6. Run deterministic unit and leakage tests.
7. Freeze executable R.

## Gate decision

**Semantic coherence:** PASS WITH REVISIONS

**R v1.0 freeze:** NO-GO

**Empirical execution:** BLOCKED

**Next action:** revise the candidate engine/specification to implement the minimal representation boundary above; do not add empirical tuning.
