# EXT-1.1 Dataset Audit v0.1

## Decision objective
Select a dataset that can support a falsifiable TGCV experiment on changes in the space of accessible transformations (`T_acc`) without relying on unverifiable historical joins or current-state leakage.

## Gate criteria
A candidate must satisfy all critical criteria (C1-C8). Non-critical criteria are scored for comparative selection.

| ID | Criterion | Rust / Schueller | npm-follower | Assessment |
|---|---|---:|---:|---|
| C1 | Stable entity identity | PASS | PASS | Both have package identity. |
| C2 | Stable version identity in source data | PASS* | PASS | Rust requires recovery of the original relational dataset; npm-follower archives published versions. |
| C3 | Historical timestamps | PASS | PASS | Both preserve publication history. |
| C4 | Dependencies + version constraints | PASS | PASS | Rust explicitly contains semver dependencies; npm metadata contains dependencies. |
| C5 | Reconstructable `T_acc(t)` | PASS* | PASS* | Requires a resolver whose historical semantics are pinned and audited. |
| C6 | Observable `ΔT_acc` | PASS* | PASS* | Derivable from adjacent historical states. |
| C7 | Outcome separable from structural inputs | PASS* | CONDITIONAL | Rust daily version downloads are explicit; npm-follower's core dataset is metadata/code, so a separate outcome source is needed unless the experiment is structural-only. |
| C8 | Public, reproducible acquisition path | UNRESOLVED | PASS* | Rust original 2022-09-07 DB has not been recovered; npm-follower has public dataset/infrastructure, but exact historical snapshot availability must be verified. |
| N1 | Historical deletion retention | UNKNOWN | PASS | npm-follower explicitly archives deleted versions. |
| N2 | Existing time-travelling resolver literature | PASS | PASS | Both have relevant prior work. |
| N3 | Minimal acquisition burden | LOW | MEDIUM | npm-follower data is large; Rust target is also potentially large. |
| N4 | Cross-domain replication potential | — | HIGH | Same dependency-space logic, independent ecosystem. |

`*` means conceptually supported but still requiring an executable validation gate before experimental freeze.

## Evidence

Rust's published data descriptor states that the Cargo source contains package names/creation dates, versions, semver dependency lists, and daily downloads per version, and that the resulting database includes `package_dependencies`, `package_version_downloads`, `package_versions`, and `packages`. The code can recreate SQLite or PostgreSQL databases. This makes Rust conceptually excellent, but the exact 2022-09-07 database artifact remains unrecovered in the current workflow.

npm-follower is explicitly designed to archive metadata and code for all package versions as they are published, including versions later deleted. The published work reports that collection began in July 2022 and that the dataset grows continuously. This gives it strong historical identity and deletion-retention properties, but the exact snapshot and an independent outcome series must be verified before substituting it for Rust.

## Decision rule

Do not switch domains merely because acquisition is easier. A candidate becomes the primary dataset only if it passes C1-C8 and an executable identifiability test on a small historical slice.

## Current decision

**Rust: PREFERRED / DATA-ACCESS GATE — not frozen.**

**npm-follower: ALTERNATIVE PRIORITY — requires a small-slice acquisition/identifiability test.**

No dataset is yet authorized for confirmatory analysis.

## Next gate

Run a minimal-slice audit for npm-follower and, in parallel, one final bounded attempt to resolve the Rust historical artifact. Whichever candidate first provides a verified historical identity + state + transformation-space reconstruction + independent outcome path becomes the experimental candidate. If both pass, prefer Rust for continuity and use npm as an independent replication candidate.
