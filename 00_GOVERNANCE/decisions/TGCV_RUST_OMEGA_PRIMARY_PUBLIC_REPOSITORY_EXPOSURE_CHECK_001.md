# TGCV — Rust Ω-Primary Public Repository Exposure Check 001

**Status:** LIMITED REPOSITORY-PATH CHECK COMPLETE / LOCAL AND EXTERNAL STORAGE UNKNOWN  
**Date:** 2026-10-09  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`  
**Scope:** Public GitHub repository tree at the reviewed branch commit

## 1. Purpose and limits

This check addresses one narrow question from the operational controls evidence template: whether the raw Rust source ZIP or an obvious generated U_t data artifact is tracked in the public TGCV repository under recognisable names.

It is not a complete secret scan, DLP audit, repository-history audit, local-device audit, cloud-sync audit, or proof that no copy exists elsewhere. It does not verify filesystem permissions, encryption, backups, access logs, or retention.

## 2. Repository facts checked

- Repository: `jcarmonabastida-pixel/TGCV`
- Repository visibility: **PUBLIC**
- Default branch: `main`
- Reviewed branch: `governance/rust-omega-raw-data-admission-firewall-audit-20261009`
- Reviewed branch commit: `4aa82e7c8d7a0e7e9074cc2761611196e0854dfb`
- Git tree response: not truncated; 3,206 tree entries were returned.
- Path-name search covered obvious names/patterns for `rust_repos_2022_09_07.zip`, Rust dataset ZIP/CSV/JSON, `package_versions.csv`, `package_dependencies.csv`, and U_t/Ω-U artifacts.

## 3. Bounded result

The reviewed tree contains the U_t constructor, runner, preflight, tests, synthetic fixture, workflows, and EXT-1.1 Rust result artifacts. The path-name search did **not** return the original `rust_repos_2022_09_07.zip`, `package_versions.csv`, `package_dependencies.csv`, or an obvious full real-data U_t JSON artifact.

This supports only the narrow statement that these expected data artifacts were not found under the searched path names in the returned tree for the reviewed branch. It does not establish that all tracked files are free of row-level data or sensitive content, and it does not establish anything about local or external copies.

## 4. Evidence status by control

| Control | Result | Status |
|---|---|---|
| Repository visibility | GitHub API reports repository as public | **VERIFIED** |
| Obvious raw ZIP path in reviewed tree | Not found by bounded path-name search | **NOT FOUND IN THIS CHECK** |
| Obvious full real-data U_t JSON path | Not found by bounded path-name search | **NOT FOUND IN THIS CHECK** |
| Entire repository content / history reviewed for data exposure | Not performed | **UNKNOWN** |
| Local ZIP and U_t storage location and permissions | Not inspected | **UNKNOWN** |
| Disk encryption | Not inspected | **UNKNOWN** |
| Cloud sync / backup copies | Not inspected | **UNKNOWN** |
| Retention and accountable role | No decision evidence | **UNKNOWN** |
| Row-level data exposure in every tracked artifact | Not established by path names | **UNKNOWN** |

## 5. Required follow-up

1. Keep the raw ZIP and existing full U_t outside public repository commits unless a separate, explicit disclosure decision approves publication.
2. If a stronger repository exposure assessment is required, perform a separately scoped content/history scan with explicit authorization and record its method and exact commit range. Do not treat this path-name check as a substitute.
3. Verify local storage/access, encryption, sync/backups, retention, and accountability from non-sensitive configuration evidence.
4. Keep the prospective empirical-use gate blocked until those items and the linkage-risk assessment are resolved.

## 6. Gate effect

This check provides one limited piece of evidence about the current public repository tree; it does not grant privacy clearance or dataset admission.

- Dataset admission: **NOT GRANTED**.
- Privacy/identifiability clearance: **NOT GRANTED**.
- Existing U_t empirical reuse: **BLOCKED**.
- New data processing or scientific execution: **NOT AUTHORIZED**.
- TGCV Core and Ω-primary canonical status: **UNCHANGED**.

No dataset bytes were downloaded, opened, or processed. No scientific code was executed. No repository content was changed except this governance record.
