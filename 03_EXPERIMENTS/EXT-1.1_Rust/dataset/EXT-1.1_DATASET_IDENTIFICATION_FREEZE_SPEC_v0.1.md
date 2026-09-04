# EXT-1.1 Rust — Scientific Dataset Identification & Freeze Specification v0.1

**Status:** DRAFT — pre-download audit
**Purpose:** Identify and freeze the empirical source required for the confirmatory EXT-1.1 Rust experiment without yet performing scientific dataset processing.

## 1. Scientific role

The empirical object is the historical evolution of published Rust package versions and their normal registry dependency declarations. The dataset is used only after the `T_acc` identifiability protocol v0.3 and resolver policy `R` have passed their methodological gate.

The dataset MUST support reconstruction of package-version states and observed dependency-edge transitions without using future information to define prior accessibility.

## 2. Primary source candidate

The primary source candidate is the official crates.io data ecosystem, with the historical package/dependency metadata represented by the crates.io database/index infrastructure. The crates.io package index provides metadata required by Cargo to resolve dependencies, and Cargo documentation specifies dependency declarations, version requirements, target conditions, optionality and dependency kinds. citeturn1search1turn0search3

The crates.io database dump is preferred for bulk historical reconstruction because it provides structured relational records rather than requiring inference from current web pages. The exact dump artifact and release/access date MUST be frozen before use.

## 3. Required empirical fields

Minimum required evidence classes:

### 3.1 Package/version state

For each package version:

- package identifier/name;
- version identifier;
- semantic version;
- publication timestamp/date, if available in the authoritative source;
- yanked status, where available;
- any source/version identity needed to join dependencies unambiguously.

### 3.2 Dependency declaration

For each dependency declaration associated with a package version:

- source package identity/name;
- version requirement (`req`);
- dependency kind;
- optional flag;
- target condition;
- default-feature policy/features where available;
- registry/source identity where available;
- dependency-to-version linkage sufficient to reconstruct the declaration without relying on later observations.

Cargo's documented dependency model explicitly distinguishes registry, git and path dependencies and distinguishes normal, development and build dependencies; platform-specific and optional dependencies are also conditional. citeturn0search3

## 4. Confirmatory scope filter

For the first confirmatory EXT-1.1 analysis, retain only observations satisfying the already frozen minimal ontology:

- published package version as observational unit;
- normal dependency;
- registry dependency corresponding to crates.io;
- unconditional target;
- optional = false;
- no workspace inheritance requiring unavailable contextual reconstruction;
- candidate transformation represented canonically as one dependency-edge insertion;
- candidate version represented by exact `(name, version, requirement)` tuple where required by protocol.

Exclude from the confirmatory sample:

- path dependencies;
- git dependencies;
- dev dependencies;
- build dependencies;
- target-specific dependencies;
- optional/feature-conditional dependencies;
- observations whose required historical context cannot be reconstructed exactly.

These exclusions are methodological scope restrictions, not claims that the excluded phenomena are unimportant.

## 5. Temporal reconstruction rule

Let `S_t` denote the frozen package-version state at observation time `t` and `C_t` the contemporaneous historical registry context.

The empirical reconstruction MUST establish:

`S_t → S_t+1`

from observed historical package-version records.

The candidate universe `U_t` MUST be generated only from information available in `C_t` under the frozen temporal cutoff. Later package versions, later dependency declarations, later registry records, and realised transitions MUST NOT be used to enlarge or modify `U_t` retrospectively.

Observed later transitions are used only to construct `T_real,t` / subsequent realised states after the prior accessibility computation has been independently completed.

## 6. Snapshot and cutoff policy

Before scientific processing, record:

1. exact source/dump identifier;
2. source URL/provenance;
3. publication/release date of the dump, if supplied;
4. local acquisition timestamp;
5. SHA-256 of the complete downloaded artifact;
6. byte size;
7. extraction format and tool/version;
8. exact files/tables used;
9. exact schema/version information;
10. explicit historical cutoff used by EXT-1.1.

The acquired artifact becomes immutable experimental input. No silent replacement by a newer dump is permitted.

The existence of downloadable historical artifacts elsewhere in the crates.io data ecosystem does not substitute for freezing the exact empirical snapshot used by this experiment. For example, the official download-archive index identifies version IDs by their `versions` table IDs and points users to the latest database dump process. citeturn1search0

## 7. Schema audit before download/freeze

The following questions MUST receive PASS/FAIL answers before the dataset is frozen:

### A — Identity
Can package versions and dependency declarations be joined unambiguously?

### B — Temporal sufficiency
Can the historical state relevant to `t` be reconstructed without reading future records?

### C — Candidate-universe sufficiency
Can `U_t` be generated from contemporaneous registry information alone?

### D — Accessibility compatibility
Can the frozen records provide the inputs required by `R` for the exact Cargo resolution test?

### E — Realisation separation
Can observed dependency additions be reconstructed independently of prior accessibility?

### F — Scope closure
Can all included observations be classified by the v0.3 inclusion rules without hidden analyst choices?

### G — Reproducibility
Can another execution reproduce the same extracted input subset from the same frozen source and extraction specification?

Any FAIL blocks scientific processing.

## 8. Current source-status decision

**PROVISIONAL:** crates.io official database/index ecosystem is the preferred empirical source.

**NOT YET FROZEN:** exact dump artifact, cutoff, schema snapshot and extracted table subset.

No scientific Rust dataset processing is authorised until the source passes the schema/temporal audit and the exact source artifact is hashed and frozen.

## 9. Required freeze package

The final dataset freeze MUST contain:

- source provenance record;
- exact downloaded archive or formally documented external immutable identifier;
- SHA-256 and byte size;
- schema snapshot;
- extraction specification/code;
- field-level inclusion/exclusion map;
- temporal cutoff declaration;
- extracted-row counts;
- integrity checks;
- evidence that no live registry lookup entered the reconstruction;
- reproducibility record.

Large source datasets need not be committed directly to GitHub. GitHub should contain the immutable specification, provenance, hashes, extraction code, manifests and derived reproducibility records.

## 10. Gate

**DATASET PROCESSING GATE: CLOSED** until sections 7 and 8 are converted from provisional to PASS/FROZEN using the exact acquired source artifact.

The next action is therefore **source/schema audit and exact dump identification**, followed by download and cryptographic freeze only after the audit passes.
