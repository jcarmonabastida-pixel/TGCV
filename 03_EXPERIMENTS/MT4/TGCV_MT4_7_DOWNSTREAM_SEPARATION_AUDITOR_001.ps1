$ErrorActionPreference = 'Stop'
$zipPath = 'C:\Users\pedri\Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$expectedSha = '691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30'
$outPath = 'C:\Users\pedri\Downloads\TGCV_MT4_7_DOWNSTREAM_SEPARATION_SUMMARY_001.txt'

$sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $zipPath).Hash.ToUpperInvariant()
if ($sha -ne $expectedSha) { throw "SOURCE_SHA256_MISMATCH: $sha" }

Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
try {
  $counts = @{
    CandidateTechnical = 0
    RealizedTransformation = 0
    StateTrajectory = 0
    EconomicValueRelated = 0
    Other = 0
  }
  $actualNames = @('Actual_capacity','Actual_generation','Actual_new_capacity','Actual_retired_capacity')
  $candidateNames = @('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
  $economicNames = @('Inv','Fixed_OM_annual','Variable_OM')
  $allTechRows = 0
  $violations = New-Object System.Collections.Generic.List[string]

  foreach ($entry in $zip.Entries) {
    if ($entry.FullName -notmatch '/Technologies/[^/]+\.csv$') { continue }
    $reader = New-Object System.IO.StreamReader($entry.Open())
    try {
      $header = $reader.ReadLine()
      while (($line = $reader.ReadLine()) -ne $null) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $x = $line -split ',(?=(?:[^"]*"[^"]*")*[^"]*$)',10
        if ($x.Count -lt 10) { continue }
        $param = $x[2].Trim('"').Trim()
        $allTechRows++
        if ($candidateNames -contains $param) { $counts.CandidateTechnical++ }
        elseif ($param -eq 'Actual_new_capacity' -or $param -eq 'Actual_retired_capacity') { $counts.RealizedTransformation++ }
        elseif ($param -eq 'Actual_capacity' -or $param -eq 'Actual_generation') { $counts.StateTrajectory++ }
        elseif ($economicNames -contains $param) { $counts.EconomicValueRelated++ }
        else { $counts.Other++ }
        if (($actualNames -contains $param) -and ($candidateNames -contains $param)) { $violations.Add("OVERLAP:$param") }
      }
    } finally { $reader.Dispose() }
  }

  $lines = @(
    'AUDIT=TGCV_MT4_7_DOWNSTREAM_SEPARATION_AUDITOR_001',
    "SOURCE_SHA256=$sha",
    "TECHNOLOGY_PARAMETER_ROWS=$allTechRows",
    "CANDIDATE_TECHNICAL_ROWS=$($counts.CandidateTechnical)",
    "REALIZED_TRANSFORMATION_ROWS=$($counts.RealizedTransformation)",
    "STATE_TRAJECTORY_ROWS=$($counts.StateTrajectory)",
    "ECONOMIC_VALUE_RELATED_ROWS=$($counts.EconomicValueRelated)",
    "OTHER_ROWS=$($counts.Other)",
    "CANDIDATE_RULE_ACTUAL_OVERLAP_VIOLATIONS=$($violations.Count)",
    'CANDIDATE_TECHNICAL=Fuel_efficiency|LF_min|LF_max|Peak_contr|Ramp_rate|Resource',
    'REALIZED_TRANSFORMATION=Actual_new_capacity|Actual_retired_capacity',
    'STATE_TRAJECTORY=Actual_capacity|Actual_generation',
    'ECONOMIC_VALUE_RELATED=Inv|Fixed_OM_annual|Variable_OM',
    'OUTCOME_LAYER=NOT_ESTABLISHED_BY_THIS_STRUCTURAL_AUDIT',
    'VALUE_LAYER=NOT_ESTABLISHED_AS_TGCV_DELTA_V',
    'STATUS=STRUCTURAL_DOWNSTREAM_SEPARATION_AUDIT - NOT YET RECONCILED'
  )
  $lines | Set-Content -LiteralPath $outPath -Encoding UTF8
  $lines
} finally { $zip.Dispose() }
