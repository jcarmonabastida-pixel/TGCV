param(
    [string]$TransferRoot = 'C:\R002_TRANSFER',
    [string]$OutputRoot = 'C:\R002_OUTPUT'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$Package = Join-Path $TransferRoot 'IT-METH-I_FAA_AMOC_BLIND_EXECUTION_PACKAGE_001.md'
$EvidenceZip = Join-Path $TransferRoot 'IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_001.zip'
$OutputEvidence = Join-Path $OutputRoot 'FROZEN_EVIDENCE_EXTRACTED'
$ManifestPath = Join-Path $OutputRoot 'executor_2_pdf_intake_manifest.json'

$ExpectedZipSha256 = '829A301215FB13EC619EE478DA45FDE4DABF0A3206B7D14F8ECADBF1660EDCBA'
$ExpectedFiles = @(
    @{ Name='EASA_AD_US-91-12-10_1.pdf'; Sha256='136C9458701AD63402C966694CB30A773D53E2A4C3FF7FA5CDE101B90379FFFE'; Length=1308719 },
    @{ Name='EASA_AD_US-91-12-10_2.pdf'; Sha256='1C7D810B9CC905EB0FF456A0515E3B86EB4F4FDD1ABDBD3BC61A3D0A65F47C0'; Length=24221 },
    @{ Name='AC_39-10.pdf'; Sha256='2A0000DF9FBD338DC6D403BD63C36659FF5542FE4B924FDE3B28C02D12B3A6C1'; Length=397778 }
)

function Test-PathUnderRoot([string]$Path, [string]$Root) {
    $fullPath = [IO.Path]::GetFullPath($Path).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    $fullRoot = [IO.Path]::GetFullPath($Root).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    if ($fullPath.Equals($fullRoot, [StringComparison]::OrdinalIgnoreCase)) { return $true }
    $rootPrefix = $fullRoot + [IO.Path]::DirectorySeparatorChar
    return $fullPath.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase)
}

function Get-Sha256([string]$Path) {
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToUpperInvariant()
}

$checks = [ordered]@{
    transfer_root_present = Test-Path -LiteralPath $TransferRoot -PathType Container
    output_root_present = $false
    package_present = Test-Path -LiteralPath $Package -PathType Leaf
    frozen_evidence_zip_present = Test-Path -LiteralPath $EvidenceZip -PathType Leaf
    frozen_evidence_zip_sha256_match = $false
    extraction_confined = $false
    expected_pdf_count = $false
    expected_pdf_hashes_match = $false
    expected_pdf_lengths_match = $false
    no_r001_material_supplied = $true
    tgcv_repo_not_supplied = $true
    network_not_requested = $true
    r002_not_performed = $true
}

if (-not $checks.transfer_root_present) { throw "Transfer root missing: $TransferRoot" }
if (-not (Test-PathUnderRoot $OutputRoot 'C:\')) { throw 'Invalid output root.' }
New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null
$checks.output_root_present = Test-Path -LiteralPath $OutputRoot -PathType Container

if (-not $checks.package_present) { throw "Controlled package missing: $Package" }
if (-not $checks.frozen_evidence_zip_present) { throw "Frozen evidence ZIP missing: $EvidenceZip" }

$checks.frozen_evidence_zip_sha256_match = ((Get-Sha256 $EvidenceZip) -eq $ExpectedZipSha256)
if (-not $checks.frozen_evidence_zip_sha256_match) { throw 'Frozen evidence ZIP SHA-256 mismatch.' }

if (Test-Path $OutputEvidence) { Remove-Item -Recurse -Force $OutputEvidence }
New-Item -ItemType Directory -Force -Path $OutputEvidence | Out-Null

Expand-Archive -LiteralPath $EvidenceZip -DestinationPath $OutputEvidence -Force
$files = @(Get-ChildItem -LiteralPath $OutputEvidence -Recurse -File)
$checks.expected_pdf_count = ($files.Count -eq $ExpectedFiles.Count)
if (-not $checks.expected_pdf_count) { throw "Frozen evidence extraction contains $($files.Count) files; expected $($ExpectedFiles.Count)." }

$actual = @{}
foreach ($f in $files) {
    if (-not (Test-PathUnderRoot $f.FullName $OutputEvidence)) { throw "Extraction escaped evidence root: $($f.FullName)" }
    $actual[$f.Name] = @{ Sha256=(Get-Sha256 $f.FullName); Length=$f.Length; FullName=$f.FullName }
}
$checks.extraction_confined = $true

$hashOk = $true
$lengthOk = $true
foreach ($expected in $ExpectedFiles) {
    if (-not $actual.ContainsKey($expected.Name)) { $hashOk = $false; $lengthOk = $false; continue }
    if ($actual[$expected.Name].Sha256 -ne $expected.Sha256) { $hashOk = $false }
    if ([int64]$actual[$expected.Name].Length -ne [int64]$expected.Length) { $lengthOk = $false }
}
$checks.expected_pdf_hashes_match = $hashOk
$checks.expected_pdf_lengths_match = $lengthOk

$failedChecks = @($checks.Values | Where-Object { $_ -eq $false })
$manifest = [ordered]@{
    PACKAGE_ID = 'IT-METH-I-AMOC-BLIND-EXEC-001'
    CASE_ID = 'IT-G1-I-AMOC-US-91-12-10-7K0-18-00734'
    MODE = 'R002_FROZEN_PDF_INTAKE_ONLY'
    STATUS = if ($failedChecks.Count -eq 0) { 'PASS' } else { 'FAIL' }
    CHECKS = $checks
    TRANSFER_ROOT = $TransferRoot
    OUTPUT_ROOT = $OutputRoot
    EVIDENCE_ZIP_SHA256 = Get-Sha256 $EvidenceZip
    EXTRACTED_FILES = @($ExpectedFiles | ForEach-Object {
        if ($actual.ContainsKey($_.Name)) {
            [ordered]@{ Name=$_.Name; Length=$actual[$_.Name].Length; SHA256=$actual[$_.Name].Sha256 }
        }
    })
    R002_STATUS = 'NOT_EXECUTED'
    EXECUTOR_2_INDEPENDENCE = 'NOT_ESTABLISHED_BY_INTAKE'
    AUTHORIZATION = 'INHERITED_FROM_IT-G5-002; NOT_REISSUED_BY_INTAKE'
    PURPOSE = 'Verify and expose only the frozen evidence files to a subsequent independent R002 executor; this script performs no reconstruction or interpretation.'
}

$manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $ManifestPath -Encoding UTF8

$manifest | ConvertTo-Json -Depth 8
