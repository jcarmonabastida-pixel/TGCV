$ErrorActionPreference = 'Stop'
$Zip = 'C:\Users\pedri\Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$ExpectedSha256 = '691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30'
$Out = 'C:\Users\pedri\Downloads\TGCV_MT4_5_PTAU_POTENTIAL_ANNUAL_TARGETED_SUMMARY_001.txt'

$sha = (Get-FileHash -Algorithm SHA256 $Zip).Hash.ToUpper()
if ($sha -ne $ExpectedSha256) { throw "FROZEN_SOURCE_HASH_MISMATCH: $sha" }

Add-Type -AssemblyName System.IO.Compression.FileSystem
$z = [System.IO.Compression.ZipFile]::OpenRead($Zip)
try {
  $targets = @(
    'EST/Technologies/EST_HydroRoR.csv',
    'EST/Technologies/EST_HydroDam.csv'
  )
  $rows = @{}
  foreach ($p in $targets) {
    $e = $z.GetEntry($p)
    if (-not $e) { throw "MISSING_TARGET_ENTRY: $p" }
    $sr = New-Object System.IO.StreamReader($e.Open())
    try {
      $header = $sr.ReadLine()
      while (($line = $sr.ReadLine()) -ne $null) {
        if ($line -notmatch '^EST,[^,]+,([^,]+),1990,') { continue }
        $x = $line -split ',(?=(?:[^"]*"[^"]*")*[^"]*$)',10
        if ($x.Count -lt 10) { continue }
        $param = $x[2]
        if ($param -in @('Potential_annual','Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource','Actual_capacity','Actual_generation','Actual_new_capacity','Actual_retired_capacity')) {
          if (-not $rows.ContainsKey($p)) { $rows[$p] = @{} }
          $rows[$p][$param] = [pscustomobject]@{ Value=$x[5]; Unit=$x[6]; Reference=$x[7]; Priority=$x[8]; Note=$x[9] }
        }
      }
    } finally { $sr.Dispose() }
  }

  $outLines = @()
  $outLines += 'AUDIT=TGCV_MT4_5_PTAU_POTENTIAL_ANNUAL_TARGETED_AUDITOR_001'
  $outLines += "ZIP_SHA256=$sha"
  $outLines += 'TARGET=EST|1990|HydroRoR vs HydroDam'
  $outLines += 'PURPOSE=Assess whether Potential_annual supplies an independently admissibility-relevant and temporally valid ex-ante dimension for the sole CORE6 collision.'
  $outLines += 'RULE=Do not promote Potential_annual to P_tau automatically; observed realization/outcome variables are not admissibility variables.'
  $outLines += ''

  foreach ($p in $targets) {
    $tech = [IO.Path]::GetFileNameWithoutExtension($p) -replace '^EST_',''
    $outLines += "TECHNOLOGY=$tech"
    foreach ($k in @('Potential_annual','Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource','Actual_capacity','Actual_generation','Actual_new_capacity','Actual_retired_capacity')) {
      if ($rows[$p].ContainsKey($k)) {
        $r = $rows[$p][$k]
        $outLines += "$k|Value=$($r.Value)|Unit=$($r.Unit)|Reference=$($r.Reference)|Priority=$($r.Priority)|Note=$($r.Note)"
      } else { $outLines += "$k|MISSING" }
    }
    $outLines += ''
  }

  $r1=$rows[$targets[0]]['Potential_annual']; $r2=$rows[$targets[1]]['Potential_annual']
  $outLines += 'COMPARISON'
  $outLines += "POTENTIAL_ANNUAL_HYDRO_ROR=$($r1.Value)"
  $outLines += "POTENTIAL_ANNUAL_HYDRO_DAM=$($r2.Value)"
  $outLines += "POTENTIAL_ANNUAL_DIFFERENCE=$([double]$r1.Value - [double]$r2.Value)"
  $txt = (($r1.Reference + ' ' + $r1.Note + ' ' + $r2.Reference + ' ' + $r2.Note)).ToLowerInvariant()
  $futurePattern = '2010|2020|based on|estimate|historical|retrospective|corrected|adjusted|maximum historical|planned|future'
  $temporalFlag = [regex]::IsMatch($txt,$futurePattern)
  $outLines += "TEMPORAL_REVIEW_REQUIRED=$temporalFlag"
  $outLines += 'SEMANTIC_STATUS=Potential_annual is a candidate technical/potential constraint, but this targeted inspection alone cannot establish that it is sufficient or point-in-time admissibility-valid for P_tau.'
  $outLines += 'SUFFICIENT_FOR_P_tau=UNDETERMINED'
  $outLines += 'STATUS=ANALYTICAL DIAGNOSTIC - TARGETED COLLISION INSPECTION'

  Set-Content -Path $Out -Value $outLines -Encoding UTF8
  $outLines | Where-Object { $_ -match '^(AUDIT|ZIP_SHA256|TARGET|TECHNOLOGY|Potential_annual\||POTENTIAL_ANNUAL_|TEMPORAL_REVIEW_REQUIRED|SEMANTIC_STATUS|SUFFICIENT_FOR_P_tau|STATUS)' }
  "OUTPUT=$Out"
} finally { $z.Dispose() }
