# EXT-1.1 Rust — Dataset Schema & Temporal Audit v0.1

**Status:** CONDITIONAL PASS — source suitable in principle; exact empirical snapshot still must be downloaded and frozen.
**Date:** 2026-09-05

## 1. Audit target

Evaluate whether the official crates.io database/index ecosystem can supply the fields required by the EXT-1.1 `T_acc` protocol v0.3, while preserving temporal non-leakage and separation between candidate accessibility and realised transitions.

## 2. Evidence reviewed

### E1 — Official crates.io database schema

The current official crates.io schema contains `crates`, `versions`, and `dependencies` tables. The `dependencies` table contains, among other fields, `crate_id`, `version_id`, `req`, `kind`, `optional`, `target`, `default_features`, `features`, and related dependency identity fields. This is sufficient at schema level to represent the dependency declaration dimensions required by the EXT-1.1 scope filter. citeturn0search0turn1search5

### E2 — Official data-access policy

The crates.io project states that its index contains the information needed for Cargo dependency resolution and that a database dump is published every 24 hours. The project also explicitly warns that exact database table layouts are not guaranteed to remain stable. citeturn1search7

### E3 — Official Cargo semantics

Cargo documentation confirms that registry, git and path dependencies are distinct resolution locations and documents the dependency specification model. This supports the planned exclusion of non-registry/path/git dependency classes from the first confirmatory sample. citeturn0search3

### E4 — Historical dump limitation

The crates.io project has explicitly stated that old database dumps are not archived. Consequently, a current dump cannot be treated as a substitute for a previously intended historical snapshot. The exact acquired artifact must therefore be cryptographically frozen when obtained. citeturn1search9

### E5 — Download infrastructure

The official static archive infrastructure states that its version-download records use the `version_id` from the database's `versions` table and directs users to the latest database dump for the complete database snapshot. These download records are ancillary and are not required for the primary `T_acc` reconstruction. citeturn2search0

## 3. Gate results

| Gate | Result | Rationale |
|---|---|---|
| A — Identity | PASS | `versions` and `dependencies` expose stable relational IDs sufficient for joining declarations to package versions at schema level. |
| B — Temporal sufficiency | CONDITIONAL PASS | Publication/version timestamps can support temporal ordering, but exact temporal reconstruction must be tested on the acquired dump and cross-checked against the index/history representation. |
| C — Candidate-universe sufficiency | CONDITIONAL PASS | Dependency requirements and version records are present; the exact procedure for generating `U_t` must be validated against frozen historical context. |
| D — Accessibility compatibility | PASS | Required dependency declaration fields are represented; actual resolution remains an experimental operation under frozen `R`. |
| E — Realisation separation | CONDITIONAL PASS | Observed dependency declarations can be separated from counterfactual candidate generation, but the extraction implementation must enforce this separation. |
| F — Scope closure | PASS | Required filters map to explicit dependency fields (`kind`, `optional`, `target`, source/location information) subject to final schema inspection. |
| G — Reproducibility | CONDITIONAL PASS | The official dump is a concrete downloadable artifact, but the exact artifact, hash, schema snapshot and extraction code must still be frozen. |

## 4. Important methodological finding

The database dump is **not by itself the historical Cargo resolver context**. The dump provides structured registry/database state; the Cargo index is the authoritative resolution-oriented representation referenced by the crates.io policy. Therefore EXT-1.1 must not claim that a database dump alone proves historical resolver behaviour.

The correct architecture is:

`DB snapshot → historical package/version/declaration reconstruction`

plus

`historical index snapshot / frozen resolver context → accessibility test under R`.

The two evidence layers must remain distinct.

## 5. Schema-minimal dataset

The initial scientific extraction should use only the minimum tables necessary:

1. `crates` — package identity;
2. `versions` — version identity, publication/yank state and timestamps required by the reconstruction;
3. `dependencies` — dependency declarations and their linkage.

Additional tables are admitted only if a documented audit demonstrates that they are necessary for source identity, temporal reconstruction, or the frozen resolver context.

Download statistics, users, owners, categories, keywords and other metadata are **not** part of the primary `T_acc` dataset unless a later hypothesis explicitly requires them.

## 6. Temporal non-leakage decision

A current database dump contains the complete accumulated history available at acquisition time. That does **not** make it valid to use the entire dump when evaluating `U_t`.

The extraction layer MUST apply the historical cutoff before candidate generation. In particular:

- versions published after `t` cannot enter `C_t`;
- dependencies declared only after `t` cannot enter `C_t`;
- later index knowledge cannot enlarge `U_t`;
- realised later dependency additions may be used only after the prior accessibility computation has been materialised;
- all joins and filters used to build `U_t` must be reproducible from records available at `t`.

This is the critical anti-leakage control.

## 7. Current audit conclusion

**DATASET SOURCE GATE: CONDITIONAL PASS.**

The official crates.io database dump is technically suitable as the structured historical metadata layer for EXT-1.1. However, the experiment is **not yet dataset-frozen** because:

1. the exact dump artifact has not yet been acquired;
2. its SHA-256 and byte size have not yet been recorded;
3. the actual dump schema/version has not yet been captured;
4. the historical index/resolver context required for accessibility still has to be paired with the database layer;
5. the extraction implementation has not yet been frozen and tested for temporal non-leakage.

Therefore **do not begin scientific processing yet**.

## 8. Next gate

The next action is now narrowly defined:

**Acquire the current official database dump and inspect its manifest/schema before any scientific extraction. Then determine the exact historical index snapshots needed for the selected observation window, and freeze both evidence layers.**

No substitution with an unrecorded later dump is permitted after freeze.
