$ErrorActionPreference='Stop'
$repo='jcarmonabastida-pixel/TGCV'
$root=(Get-Location).Path
$raw='https://raw.githubusercontent.com/'+$repo+'/main/00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md'
$rawV12='https://raw.githubusercontent.com/'+$repo+'/main/00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.12.md'
$current=Invoke-RestMethod -Uri $raw
$v12=Invoke-RestMethod -Uri $rawV12
if($current -notmatch 'Current v1\.11'){ throw 'REMOTE_CURRENT_IS_NOT_V1.11' }
if($v12 -notmatch 'TGCV — Evidence-to-Claim Matrix — v1\.12'){ throw 'V12_ARTIFACT_NOT_FOUND_OR_INVALID' }
$mt4=$v12.Substring($v12.IndexOf('## v1.12 update — complete MT4 domain-transfer evidence'))
$mt4=$mt4.Substring(0,$mt4.IndexOf('## v1.12 methodological routing after MT4 closure'))
$out=$current
$out=$out -replace 'Evidence-to-Claim Matrix — Current v1\.11','Evidence-to-Claim Matrix — Current v1.12'
$out=$out -replace '\*\*Predecessor:\*\* v1\.10','**Predecessor:** v1.11'
$out=$out -replace '(\*\*Incremental governance update:\*\*).*',"**Incremental governance update:** v1.12 preserves the complete material evidentiary content and schema of v1.11 and adds the complete MT4 domain-transfer evidence layer. No prior evidence is deleted, collapsed, or downgraded. No claim-level status is upgraded by MT4 propagation."
$out=$out -replace '\+ C10C-004 \|','+ C10C-004 + MT4 |'
$out=$out -replace 'C10C-004 \| \n','C10C-004 + MT4 | \n'
$out=$out -replace 'C10C-004 \| No direct evidence contribution','C10C-004 + MT4 | No direct evidence contribution'
$out=$out -replace 'C10C-004 \| |','C10C-004 + MT4 | |'
$marker='## Claim boundary'
if($out.IndexOf('## Material evidence — MT4') -ge 0 -or $out.IndexOf('## v1.12 update — complete MT4') -ge 0){ throw 'MT4_ALREADY_PRESENT_IN_CURRENT' }
$pos=$out.IndexOf($marker)
if($pos -lt 0){ throw 'CLAIM_BOUNDARY_MARKER_NOT_FOUND' }
$out=$out.Substring(0,$pos)+"$mt4`n`n"+$out.Substring($pos)
$out=$out -replace 'v1\.11 adds C10C-004 bounded methodological evidence propagation','v1.11 adds C10C-004 bounded methodological evidence propagation, and v1.12 adds complete MT4 domain-transfer evidence propagation'
$path=Join-Path $root '00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md'
[IO.File]::WriteAllText($path,$out,(New-Object Text.UTF8Encoding($false)))
$check=Get-Content $path -Raw
if($check -notmatch 'Current v1\.12'){ throw 'LOCAL_CURRENT_HEADER_NOT_V1.12' }
if($check -notmatch 'MT4-8'){ throw 'MT4_COMPLETE_SECTION_NOT_PRESENT' }
if($check -notmatch 'MT4-6 independent reproducibility'){ throw 'MT4_REPRODUCIBILITY_SECTION_MISSING' }
if($check -notmatch 'MT4-7 downstream separation'){ throw 'MT4_DOWNSTREAM_SECTION_MISSING' }
if($check -notmatch 'MT4-8 value isolation'){ throw 'MT4_VALUE_SECTION_MISSING' }
git add -- 00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md
git commit -m 'Reconcile cumulative evidence matrix CURRENT to v1.12'
git push origin main
Write-Host 'MATRIX_CURRENT_V1_12_RECONCILED_AND_PUSHED'
git rev-parse HEAD
