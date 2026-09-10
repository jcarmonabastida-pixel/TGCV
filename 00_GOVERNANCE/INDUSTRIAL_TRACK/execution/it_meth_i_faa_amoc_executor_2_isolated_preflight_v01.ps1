# IT-METH-I FAA AMOC — Executor-2 isolated preflight v0.2
# PRE-R002 PREFLIGHT ONLY
# Technical boundary check for Windows Sandbox; does NOT execute Reconstruction 002.
# Inputs remain under the read-only transfer mount; preflight output is written to a separate writable sandbox root.

param(
    [string]$TransferRoot = 'C:\R002_TRANSFER',
    [string]$OutputRoot = 'C:\R002_OUTPUT'
)

$ErrorActionPreference = 'Stop'
$package = Join-Path $TransferRoot 'IT-METH-I_FAA_AMOC_BLIND_EXECUTION_PACKAGE_001.md'
$evidence = Join-Path $TransferRoot 'IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_001.zip'
$runtime = Join-Path $TransferRoot 'it_meth_i_faa_amoc_executor_2_isolated_runtime_v01.py'

New-Item -ItemType Directory -Path $OutputRoot -Force | Out-Null
$output = Join-Path $OutputRoot 'executor_2_isolation_preflight.json'

$expectedPackageSha256 = '352F56F5EBF1E5CB43B02D56B38B6A02BCBE3F8DC9B6058AFED8A495550E7A69'
$expectedEvidenceSha256 = '829A301215FB13EC619EE478DA45FDE4DABF0A3206B7D14F8ECADBF1660EDCBA'
$expectedRuntimeSha256 = '2B559B39FD00E7E152D290AE754733AAA1469392900E77917F4CC200143C2B26'

function Test-PathUnderRoot([string]$Path, [string]$Root) {
    $fullPath = [IO.Path]::GetFullPath($Path)
    $fullRoot = ([IO.Path]::GetFullPath($Root)).TrimEnd('\\') + '\\'
    return $fullPath.StartsWith($fullRoot, [StringComparison]::OrdinalIgnoreCase)
}

$checks = [ordered]@{}
$checks.transfer_root_present = Test-Path -LiteralPath $TransferRoot -PathType Container
$checks.output_root_present = Test-Path -LiteralPath $OutputRoot -PathType Container
$checks.package_present = Test-Path -LiteralPath $package -PathType Leaf
$checks.frozen_evidence_present = Test-Path -LiteralPath $evidence -PathType Leaf
$checks.runtime_present = Test-Path -LiteralPath $runtime -PathType Leaf

if ($checks.package_present) { $checks.package_sha256_match = ((Get-FileHash $package -Algorithm SHA256).Hash -eq $expectedPackageSha256) } else { $checks.package_sha256_match = $false }
if ($checks.frozen_evidence_present) { $checks.frozen_evidence_sha256_match = ((Get-FileHash $evidence -Algorithm SHA256).Hash -eq $expectedEvidenceSha256) } else { $checks.frozen_evidence_sha256_match = $false }
if ($checks.runtime_present) { $checks.runtime_sha256_match = ((Get-FileHash $runtime -Algorithm SHA256).Hash -eq $expectedRuntimeSha256) } else { $checks.runtime_sha256_match = $false }

$checks.r001_not_supplied = -not (Test-Path -LiteralPath (Join-Path $TransferRoot 'R001') -PathType Any)
$checks.tgcv_repo_not_supplied = -not (Test-Path -LiteralPath (Join-Path $TransferRoot 'TGCV') -PathType Any)
$checks.output_confined = Test-PathUnderRoot $output $OutputRoot
$checks.network_not_requested = $true
$checks.r002_not_performed = $true

$technicalPass = @($checks.Values | Where-Object { $_ -ne $true }).Count -eq 0

$result = [ordered]@{
    PACKAGE_ID = 'IT-METH-I-AMOC-BLIND-EXEC-001'
    CASE_ID = 'IT-G1-I-AMOC-US-91-12-10-7K0-18-00734'
    MODE = 'PRE_R002_ISOLATION_PREFLIGHT'
    TECHNICAL_ISOLATION_PREFLIGHT = if ($technicalPass) { 'PASS' } else { 'FAIL' }
    CHECKS = $checks
    TRANSFER_ROOT = $TransferRoot
    OUTPUT_ROOT = $OutputRoot
    R002_STATUS = 'NOT_EXECUTED'
    EXECUTOR_2_INDEPENDENCE = 'NOT_ESTABLISHED_BY_RUNTIME'
    AUTHORIZATION = 'INHERITED_FROM_IT-G5-002; NOT_REISSUED_BY_RUNTIME'
}

$result | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $output -Encoding UTF8
$result | ConvertTo-Json -Depth 6
