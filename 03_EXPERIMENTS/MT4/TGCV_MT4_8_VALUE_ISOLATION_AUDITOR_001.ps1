$ErrorActionPreference = 'Stop'
$zipPath = 'C:\Users\pedri\Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$expectedSha = '691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30'
$outPath = 'C:\Users\pedri\Downloads\TGCV_MT4_8_VALUE_ISOLATION_SUMMARY_001.txt'

$sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $zipPath).Hash.ToUpperInvariant()
if ($sha -ne $expectedSha) { throw "SOURCE_SHA256_MISMATCH: $sha" }

Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
try {
  $candidate = @('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
  $valueVars = @('Inv','Fixed_OM_annual','Variable_OM')
  $actual = @('Actual_capacity','Actual_generation','Actual_new_capacity','Actual_retired_capacity')
  $counts = @{}
  foreach ($p in ($candidate + $valueVars + $actual)) { $counts[$p] = 0 }
  $yearMin = @{}
  $yearMax = @{}
  $rows = 0
  $overlap = New-Object System.Collections.Generic.List[string]

  foreach ($entry in $zip.Entries) {
    if ($entry.FullName -notmatch '/Technologies/([^/]+)\.csv$') { continue }
    $reader = New-Object System.IO.StreamReader($entry.Open())
    try {
      [void]$reader.ReadLine()
      while (($line = $reader.ReadLine()) -ne $null) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $x = $line -split ',(?=(?:[^"]*"[^"]*")*[^"]*$)',10
        if ($x.Count -lt 10) { continue }
        $param = $x[2].Trim('"').Trim()
        $yearText = $x[3].Trim('"').Trim()
        $rows++
        if ($counts.ContainsKey($param)) {
          $counts[$param]++
          if ($yearText -match '^\d{4}$') {
            if (-not $yearMin.ContainsKey($param) -or [int]$yearText -lt $yearMin[$param]) { $yearMin[$param] = [int]$yearText }
            if (-not $yearMax.ContainsKey($param) -or [int]$yearText -gt $yearMax[$param]) { $yearMax[$param] = [int]$yearText }
          }
          if (($candidate -contains $param) -and ($valueVars -contains $param)) { $overlap.Add("OVERLAP:$param") }
        }
      }
    } finally { $reader.Dispose() }
  }

  $core6Rows = (($candidate | ForEach-Object { $counts[$_] }) | Measure-Object -Sum).Sum
  $actualRows = (($actual | ForEach-Object { $counts[$_] }) | Measure-Object -Sum).Sum
  $lines = @(
    'AUDIT=TGCV_MT4_8_VALUE_ISOLATION_AUDITOR_001',
    "SOURCE_SHA256=$sha",
    "TECHNOLOGY_PARAMETER_ROWS=$rows",
    "CORE6_ROWS=$core6Rows",
    "INV_ROWS=$($counts['Inv'])",
    "FIXED_OM_ANNUAL_ROWS=$($counts['Fixed_OM_annual'])",
    "VARIABLE_OM_ROWS=$($counts['Variable_OM'])",
    "ACTUAL_ROWS=$actualRows",
    "CORE6_VALUE_OVERLAP_VIOLATIONS=$($overlap.Count)",
    "VALUE_PARAMETER_YEAR_RANGES=Inv:$($yearMin['Inv'])-$($yearMax['Inv']);Fixed_OM_annual:$($yearMin['Fixed_OM_annual'])-$($yearMax['Fixed_OM_annual']);Variable_OM:$($yearMin['Variable_OM'])-$($yearMax['Variable_OM'])",
    'VALUE_VARIABLES=Inv|Fixed_OM_annual|Variable_OM',
    'CORE6=Fuel_efficiency|LF_min|LF_max|Peak_contr|Ramp_rate|Resource',
    'VALUE_ENDPOINT_STATUS=NOT_ESTABLISHED_AS_TGCV_DELTA_V',
    'TEMPORAL_DOWNSTREAM_STATUS=REQUIRES_SEPARATE_SEMANTIC_AND_TEMPORAL_RECONCILIATION',
    'CAUSAL_EFFECT_STATUS=NOT_TESTED',
    'STATUS=VALUE_ISOLATION_STRUCTURAL_AUDIT - NOT YET RECONCILED',
    "OUTPUT=$outPath"
  )
  $lines | Set-Content -LiteralPath $outPath -Encoding UTF8
  $lines
} finally { $zip.Dispose() }
