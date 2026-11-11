# TGCV — Rust Ω-Primary Local Controls Evidence Record 001

**Status:** PARTIAL EVIDENCE RECORD — REVIEW REQUIRED / DATASET ADMISSION NOT GRANTED  
**Evidence date:** 2026-10-09  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`  
**Purpose:** record the local checks performed interactively for the prospective admission review. This record does not grant dataset admission or authorize new processing.

## 1. Evidence provenance and limits

The values below were reported by the user from read-only PowerShell checks or explicitly declared by the user in conversation. The checks were not executed independently by the TGCV repository or by this assistant. No dataset contents were inspected or processed during these checks.

Do not add passwords, access tokens, private keys, personal account identifiers, or exact sensitive storage paths to public repository records.

## 2. Raw ZIP inventory

| Item | Observed value | Evidence status |
|---|---|---|
| Artifact class | Raw source ZIP | Reported from local check |
| Filename | `rust_repos_2022_09_07.zip` | Known artifact reference |
| Local storage class | Local disk, under the user's Downloads folder on `C:` | User declaration and local check |
| Exists | Yes | Reported from local check |
| Size | `6,047,715,996` bytes | Reported from local check; matches published artifact size |
| Published MD5 | `a6b9feffdc3dafc86fa80ec23de38c10` | Previously recorded comparison against Figshare metadata |
| Local MD5 verification | Previously reported as matching published MD5 | Prior evidence; not rerun as part of this record |
| Read-only attribute | False | Reported from local check |
| EFS encrypted attribute | False | Reported from local check |

A matching size and published MD5 support identification of the local file as the published artifact. MD5 is recorded for artifact matching, not as a modern collision-resistant security guarantee.

## 3. Local access-control observations

### 3.1 Raw ZIP ACL

The file ACL inventory returned three inherited `Allow FullControl` rules. Subsequent classification matched these rules to:
- `SYSTEM`;
- `BUILTIN_ADMINISTRATORS`;
- the current Windows account.

No explicit, non-inherited deny rule was reported. These observations do not constitute a complete effective-access audit, and they do not prove absence of every other access path.

### 3.2 Downloads folder ACL

The Downloads folder exists and its ACL inventory returned three inherited `Allow FullControl` rules, classified as:
- `SYSTEM`;
- `BUILTIN_ADMINISTRATORS`;
- the current Windows account.

### 3.3 User profile ACL

The profile ACL has inheritance disabled and four non-inherited rules:
- `SYSTEM`: `FullControl`;
- `BUILTIN_ADMINISTRATORS`: `FullControl`;
- current Windows account: `FullControl`;
- another special identity: `ExecuteFile, Synchronize`.

The final identity was not resolved beyond the broad category used in the local check. No conclusion is made about its exact principal or all effective access.

## 4. Storage protection and copies

| Control | Recorded state | Evidence type / limitation |
|---|---|---|
| BitLocker on system drive C: | Disabled | User checked Windows “Manage BitLocker” UI and reported the state |
| EFS on raw ZIP | Encrypted attribute false | Reported from local PowerShell check |
| Cloud sync / automatic backups for Downloads | User reports none known | User declaration; not independently verified |
| Storage boundary | Local disk on C: | User declaration and local checks |
| Public repository exposure | Bounded public-repository path-name check did not find the raw ZIP or an obvious full real-data U_t JSON | This was not a content scan, history scan, or audit of external stores |
| Transfers to third parties | Unknown | No evidence recorded |
| Backups or copies of existing U_t | Unknown | No evidence recorded |

The user has explicitly decided not to use BitLocker on this computer. No encryption setting or file permission was changed during the checks. The lack of BitLocker and EFS is recorded as a residual storage-protection limitation; it is not, by itself, evidence that the artifact is publicly exposed.

## 5. Purpose, accountability, and retention

| Decision item | Recorded value |
|---|---|
| Purpose | Use within the TGCV programme only; no other intended purpose |
| Accountable role | User-confirmed person responsible for preserving the original artifact for TGCV; no personal identity recorded here |
| Raw ZIP disposition | Retain for TGCV research/reproducibility, subject to periodic review |
| Review cadence | Every six months |
| Extraordinary review triggers | Change in purpose, storage location, or access conditions |
| Deletion | No automatic deletion; requires a separate explicit decision |
| External sharing | Not authorized by this record; separate approval required |
| Public row-level release | Not authorized by this record; separate approval required |

The six-month review cadence and extraordinary triggers were explicitly agreed in conversation on 2026-10-09. This record does not set a fixed deletion date.

## 6. Remaining unknowns and required follow-up

- Complete effective-access review for the raw ZIP and the storage boundary: **OPEN**.
- Exact identity and scope of the fourth user-profile ACL rule: **OPEN**.
- Location, access controls, and copies/backups of the existing U_t JSON: **UNKNOWN**.
- Transfer history and any external recipients: **UNKNOWN**.
- Formal residual-risk decision by the authorized TGCV decision-maker: **NOT RECORDED**.
- Independent linkage/privacy review, as applicable to the intended use: **OPEN**.
- Evidence review and prospective admission decision: **NOT COMPLETED**.

## 7. Gate state

- Dataset admission: **NOT GRANTED**.
- Privacy/identifiability clearance: **NOT GRANTED**.
- Existing U_t empirical reuse: **BLOCKED pending prospective admission decision**.
- Longitudinal absence/removal claims: **BLOCKED**; `UNKNOWN_MISSING` must not be interpreted as absence.
- New processing or scientific execution: **NOT AUTHORIZED by this record**.
- TGCV Core and Ω-primary canonical status: **UNCHANGED**.

No dataset bytes were opened, transformed, or scientifically processed for this record. No scientific code was executed. This record documents reported control evidence and explicit unknowns; it does not attest to controls that have not been verified.
