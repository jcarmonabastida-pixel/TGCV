$ErrorActionPreference = "Stop"
$repo = (git rev-parse --show-toplevel)
$commit = (git rev-parse HEAD).Trim()
$py = (py -3 --version).Trim()
$os = (Get-CimInstance Win32_OperatingSystem).Caption
$build = (Get-CimInstance Win32_OperatingSystem).BuildNumber
$files = @(
"00_GOVERNANCE/SIP/VSL_EXP_A_EXECUTABLE_BUNDLE_001/EXECUTION_SPEC.md",
"00_GOVERNANCE/SIP/VSL_EXP_A_EXECUTABLE_BUNDLE_001/execute.py",
"00_GOVERNANCE/SIP/VSL_EXP_A_EXECUTABLE_BUNDLE_001/EXECUTOR_2_RECONSTRUCTION_SPEC.md",
"00_GOVERNANCE/SIP/VSL_EXP_B_EXECUTABLE_BUNDLE_001/EXECUTION_SPEC.md",
"00_GOVERNANCE/SIP/VSL_EXP_B_EXECUTABLE_BUNDLE_001/execute.py",
"00_GOVERNANCE/SIP/VSL_EXP_B_EXECUTABLE_BUNDLE_001/EXECUTOR_2_RECONSTRUCTION_SPEC.md"
)
$result = [ordered]@{
  generated_utc = (Get-Date).ToUniversalTime().ToString("o")
  repository = $repo
  commit = $commit
  python = $py
  os = $os
  build = $build
  network_access = "PROHIBITED"
  files = @()
}
foreach ($f in $files) {
  $h = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $repo $f)).Hash
  $result.files += [ordered]@{ path=$f; sha256=$h }
}
$result | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 (Join-Path $repo "00_GOVERNANCE/SIP/VSL_TECHNICAL_FREEZE_CAPTURE_RESULT_001.json")
Write-Host "FREEZE CAPTURE WRITTEN"
