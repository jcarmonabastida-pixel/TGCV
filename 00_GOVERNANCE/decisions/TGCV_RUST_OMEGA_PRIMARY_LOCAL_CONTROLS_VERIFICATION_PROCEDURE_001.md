# TGCV — Rust Ω-Primary Local Controls Verification Procedure 001

**Status:** PROCEDURE PROPOSED — NOT EXECUTED — LOCAL CONTROLS UNKNOWN  
**Date:** 2026-10-09  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`  
**Purpose:** provide a read-only, privacy-conscious way to collect evidence about local storage of the raw ZIP and existing U_t before a prospective admission decision.

## 1. Safety boundary

Run these checks locally on the machine that stores the files. They are intended to read metadata/configuration only; they do not open, decompress, transform, hash, or process dataset contents. The ZIP MD5 identity check has already been separately performed by the user and is not repeated here.

Do not paste raw ACL output, usernames, account names, full local paths, serial numbers, or screenshots that expose personal or sensitive details into this public repository or chat. Report only the sanitised summaries described below.

This procedure does not itself grant permission to inspect row-level data or run scientific analysis. Do not run any command that uploads files, changes permissions, deletes data, or modifies the repository.

## 2. Check existence and file metadata

In PowerShell, set the known ZIP path and the actual local U_t JSON path if it exists:

```powershell
$zipPath = "C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip"
$utPath = Read-Host "Enter the local U_t JSON path (input remains in this PowerShell session)"
@($zipPath, $utPath) | ForEach-Object {
    if (Test-Path -LiteralPath $_ -PathType Leaf) {
        $f = Get-Item -LiteralPath $_
        [pscustomobject]@{
            ArtifactClass = if ($_.EndsWith("rust_repos_2022_09_07.zip")) { "RAW_ZIP" } else { "UT_JSON" }
            Exists = $true
            Bytes = $f.Length
            IsReadOnly = $f.IsReadOnly
            LastWriteTimePresent = ($null -ne $f.LastWriteTime)
        }
    } else {
        [pscustomobject]@{
            ArtifactClass = if ($_ -eq $zipPath) { "RAW_ZIP" } else { "UT_JSON" }
            Exists = $false
            Bytes = $null
            IsReadOnly = $null
            LastWriteTimePresent = $null
        }
    }
}
```

This intentionally does not print the supplied path. Do not report last-write timestamps unless they are needed for a specific audit question.

## 3. Check access-control configuration without disclosing identities

Run locally for each file:

```powershell
$paths = @($zipPath, $utPath)
foreach ($p in $paths) {
    if (Test-Path -LiteralPath $p -PathType Leaf) {
        $acl = Get-Acl -LiteralPath $p
        [pscustomobject]@{
            ArtifactClass = if ($p -eq $zipPath) { "RAW_ZIP" } else { "UT_JSON" }
            OwnerKnown = -not [string]::IsNullOrWhiteSpace($acl.Owner)
            AccessRuleCount = @($acl.Access).Count
            InheritanceDisabled = $acl.AreAccessRulesProtected
            HasExplicitDenyRule = @($acl.Access | Where-Object { $_.AccessControlType -eq "Deny" -and -not $_.IsInherited }).Count -gt 0
        }
    }
}
```

These fields are only an initial ACL inventory; they do not prove that access is appropriately restricted. Do not share the owner or identity strings. A reviewer must interpret the rules against the actual authorised-user scope before claiming access control is adequate.

## 4. Check Windows system-drive encryption status

This is a configuration query and may be unavailable without appropriate privileges:

```powershell
try {
    Get-BitLockerVolume -MountPoint $env:SystemDrive -ErrorAction Stop |
        Select-Object MountPoint, VolumeStatus, ProtectionStatus, EncryptionPercentage
} catch {
    "BITLOCKER_STATUS_UNAVAILABLE"
}
```

Report only the resulting status fields or `BITLOCKER_STATUS_UNAVAILABLE`. This checks the system drive only; if an artifact is on another volume, that volume must be assessed separately. Do not infer encryption from the presence of a Windows device or account password.

## 5. Cloud sync and backup

No single generic local command proves the absence of cloud-synced or backup copies. Check the configured storage location and any known sync/backup service through its ordinary settings UI. Record only:
- whether sync is enabled for the relevant folder;
- whether backup copies are known to exist;
- the storage/service category and access boundary;
- whether retention/deletion is controlled.

Do not share account names, folder paths, screenshots with personal details, or backup contents. If uncertain, record `UNKNOWN`.

## 6. What to return

Return a sanitised summary only:

| Item | Allowed response |
|---|---|
| Raw ZIP exists | YES / NO |
| U_t exists locally | YES / NO / UNKNOWN |
| File ACL inventory completed | YES / NO |
| Access scope understood and reviewed | YES / NO / UNKNOWN |
| System-drive encryption | ON / OFF / UNAVAILABLE |
| Artifact-volume encryption | ON / OFF / UNKNOWN / NOT APPLICABLE |
| Cloud sync for artifact folders | YES / NO / UNKNOWN |
| Backup copies | YES / NO / UNKNOWN |
| Retention owner and trigger defined | YES / NO / UNKNOWN |

Do not include full ACL output or identities. A `YES` for a check means the evidence was collected, not that the control is adequate.

## 7. Admission consequence

Until evidence is reviewed and the prospective decision is explicitly recorded:
- dataset admission remains **NOT GRANTED**;
- privacy/identifiability clearance remains **NOT GRANTED**;
- empirical reuse of existing U_t remains **BLOCKED**;
- no new data processing or scientific execution is authorised;
- TGCV Core and Ω-primary canonical status remain unchanged.

This procedure has not been run on the user's machine. It records a proposed read-only verification method, not findings about local controls.
