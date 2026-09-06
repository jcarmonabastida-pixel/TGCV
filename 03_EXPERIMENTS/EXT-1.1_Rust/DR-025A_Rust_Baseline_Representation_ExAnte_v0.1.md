# DR-025A — EXT-1.1 Rust Baseline B Representation Ex-Ante Design v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Scope:** Final representation of conventional baseline `B` for EXT-1.1 Rust  
**Depends on:** DR-019, DR-020, DR-021, DR-022, DR-023, DR-024, DR-025

## 1. Governing question

Can the candidate conventional baseline be represented in a fixed, deterministic and outcome-independent form that remains conventionally interpretable while avoiding reconstruction of `T_acc^(R*)`?

## 2. Frozen baseline object

For each eligible origin release `v_o = package@version`, at `t_o = created_at(v_o)`, the baseline representation is:

`B(v_o) = (V_o, H_o, A_o, D_o)`

where:

- `V_o` = origin release version representation;
- `H_o` = pre-origin package-history representation;
- `A_o` = raw dependency-declaration representation;
- `D_o` = origin release declared-dependency count.

No component is constructed from outcome, `T_acc`, `R*`, downstream observations, downloads, adoption or future records.

## 3. Version representation

`version_str` is retained as an observed release-state attribute.

For the primary baseline representation it is treated as a **categorical nominal field**, not as an ordinal numeric quantity. No ordering, distance, semantic-version arithmetic, or resolver operation is applied to it in construction of `B`.

The raw value is retained deterministically. Any later model encoding must be a fixed encoding specified before confirmatory analysis; no outcome-driven encoding or feature engineering is permitted.

Malformed or non-standard version strings are not manually corrected or excluded by substantive characteristics. If a downstream model cannot consume a value, handling must be specified ex ante and applied deterministically to the complete eligible frame.

## 4. Package identity

Canonical package identity is **not included as a predictive baseline feature**.

Package identity is retained only as observational metadata required to reconstruct the unit and its historical context. It must not be used to create package-specific target statistics, learned embeddings, outcome encodings, or equivalent identity-derived predictors.

This prevents the baseline from becoming an implicit package-history/outcome model while preserving deterministic reconstruction of the observational unit.

## 5. Historical representation

`H_o` consists of two fixed quantities:

1. `prior_release_count_o`: number of earlier releases of the same package with `created_at < t_o`;
2. `package_age_days_o`: elapsed time between the earliest observed release of the same package and `t_o`.

The primary definition uses strict precedence (`< t_o`) for prior releases. The origin itself is not counted as a prior release.

The earliest observed package release necessarily has timestamp `<= t_o`; no post-origin record may influence this quantity.

No other retrospective package-history feature is included in the primary baseline.

## 6. Dependency-declaration representation

`A_o` represents the dependency declarations attached to the origin release **without semantic resolution**.

The baseline does not call `R*`, enumerate admissible target releases, select maximal versions, construct candidate universes, or otherwise transform declarations into accessible transformations.

For the primary baseline feature vector, the raw declaration content is not expanded into target-release identities. Its presence is represented through the fixed scalar `D_o`, the number of dependency declaration rows attached to the origin release.

The declaration rows remain provenance available for audit/reconstruction but are not resolved into `T_acc`.

## 7. Dependency count

`D_o` is the deterministic count of dependency declaration rows attached to `v_o` in the frozen `package_dependencies` relation.

No filtering by dependency target, package popularity, outcome, dependency resolution success, or later activity is applied.

No SemVer parsing is required to construct `D_o`.

## 8. Primary feature vector

The primary numerical feature vector supplied to a later pre-specified model is conceptually:

`B_num(v_o) = encode(V_o) || prior_release_count_o || package_age_days_o || D_o`

with `encode(V_o)` fixed ex ante and independent of outcomes.

The exact model-compatible categorical encoding mechanism must be frozen in the confirmatory analysis specification before model fitting. The encoding must not use target statistics or future observations.

If a model family can natively consume a categorical field, the native representation is preferred over an outcome-derived encoding.

## 9. Deliberate exclusions

The primary baseline excludes:

- canonical package identity as a predictive feature;
- `T_acc^(R*)` and any derivative;
- `R*` and resolver outputs;
- candidate universe `T` as a feature;
- resolved dependency target versions;
- dependency-network centrality or downstream-network features;
- downloads, adoption, popularity and success measures;
- post-origin release counts or activity;
- future dependency declarations or future resolution;
- outcome-derived encodings;
- target encoding or other supervised encoding of package identity/version;
- feature selection based on outcome prevalence, association, effect size or significance;
- manually selected package classes or releases.

## 10. Why this is a conventional comparator

The baseline is intentionally limited to information ordinarily attached to a package release or its immediately observable release history: its own release-state version attribute, release-history maturity, and the size of its declared dependency surface.

The baseline does not attempt to infer which concrete target releases are accessible. That transformation is reserved for `T_acc^(R*)`.

Thus the scientific comparison is between:

`B(v_o)` = conventional release/state representation

and

`T_acc^(R*)(v_o)` = explicitly resolved accessible-transformation representation.

The experiment remains agnostic about which representation will contain more information about `Y_180`.

## 11. Determinism and temporal rule

For every feature:

- only frozen records with timestamp `<= t_o` may contribute;
- no future release may contribute;
- no post-origin dependency information may contribute;
- identical frozen inputs must produce identical values;
- package-history summaries use a deterministic timestamp rule;
- dependency count uses the fixed origin-release relation;
- version representation uses the stored release string without retrospective correction.

## 12. Finality boundary

This document freezes the **candidate primary representation**, but does not yet freeze:

- the statistical/model family;
- train/test or cross-validation protocol;
- hyperparameters;
- confirmatory metric or decision threshold;
- a model-specific categorical encoding if the chosen model does not natively consume categorical values.

Those belong to subsequent methodological decisions and must remain outcome-blind.

## 13. Acceptance conditions

DR-025A may be accepted only if review confirms:

1. the representation is reconstructible from the frozen dataset;
2. all primary features are pre-origin and outcome-independent;
3. no feature requires `T_acc` or `R*`;
4. package identity cannot leak outcome through target encoding or learned package-specific history;
5. the representation is sufficiently conventional to serve as a meaningful comparator;
6. no feature family was selected using confirmatory evidence;
7. downstream model encoding can be frozen without outcome-derived transformations.

No confirmatory execution is authorized by this design proposal alone.
