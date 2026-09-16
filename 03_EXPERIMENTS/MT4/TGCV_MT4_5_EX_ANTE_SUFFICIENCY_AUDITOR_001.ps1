# TGCV MT4-5 — Ex Ante Sufficiency Auditor 001
# Purpose: determine whether a temporally clean candidate information subset exists
# for constructing U_tau and P_tau without using realized outcomes or future information.
# This is an analytical diagnostic, not a gate decision.

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zipPath = "$env:USERPROFILE\Downloads\TGCV_MT4_energy_public-dataset_v2.zip"
$summaryPath = "$env:USERPROFILE\Downloads\TGCV_MT4_5_EX_ANTE_SUFFICIENCY_SUMMARY_001.txt"
$detailPath = "$env:USERPROFILE\Downloads\TGCV_MT4_5_EX_ANTE_SUFFICIENCY_DETAIL_001.txt"

$knownTechParams = @(
 'Actual_capacity','Actual_generation','Actual_new_capacity','Actual_retired_capacity',
 'Buildrates','Fixed_OM_annual','Fuel_efficiency','Heat_to_electricity',
 'Initial_retired_capacity','Inv','Learning_rate','LF_max','LF_min','Lifetime',
 'Own_use','Peak_contr','Potential_annual','Potential_installed','Ramp_rate',
 'Resource','Variable_OM'
)

# Parameters that are analytically eligible for candidate admissibility components,
# subject to temporal/provenance verification. Observed Actual_* variables are excluded
# because they describe realization rather than admissibility.
$candidateParams = @('Fuel_efficiency','LF_max','LF_min','Lifetime','Peak_contr','Ramp_rate','Resource','Potential_annual','Potential_installed','Buildrates')

$futurePatterns = '2010 estimate|2030|estimate for 2030|Adjusted to 110% of historical value'
$retroPatterns = 'maximum historical|historical buildrate|historical value|historical peak'
$planningPatterns = 'master plan|planned plants|legally possible|Act on|resolution|referenda|foreseeable future|scenario'

$z=[IO.Compression.ZipFile]::OpenRead($zipPath)
$rows = New-Object System.Collections.Generic.List[object]
try {
 foreach($e in $z.Entries) {
  if($e.FullName -notmatch '/Technologies/.*\.csv$'){ continue }
  $sr=[IO.StreamReader]::new($e.Open())
  try {
   while(($l=$sr.ReadLine()) -ne $null) {
    if($l -notmatch ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)'){ continue }
    $x=$l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10
    if($x.Count -lt 10){ continue }
    $param=$x[2].Trim()
    if($knownTechParams -notcontains $param){ continue }
    $year=0; [int]::TryParse($x[3].Trim(),[ref]$year) | Out-Null
    $note=$x[9].Trim().Trim('"')
    $class='CLEAN / NOT FLAGGED'
    if($param -eq 'Actual_capacity' -or $param -eq 'Actual_generation' -or $param -eq 'Actual_new_capacity' -or $param -eq 'Actual_retired_capacity' -or $param -eq 'Initial_retired_capacity'){$class='REALIZATION / STATE — NOT ADMISSIBILITY'}
    elseif($note -match $futurePatterns){$class='FUTURE / EXPLICIT LEAKAGE'}
    elseif($note -match $retroPatterns){$class='RETROSPECTIVE / HISTORICAL DEPENDENCY'}
    elseif($note -match $planningPatterns){$class='PLANNING / LEGAL — DATE CHECK'}
    elseif($candidateParams -contains $param){$class='CANDIDATE — REQUIRES TEMPORAL/SEMANTIC VALIDATION'}
    else{$class='TECHNICAL/ECONOMIC — NOT SUFFICIENT ALONE'}
    $rows.Add([pscustomobject]@{Parameter=$param;Country=$x[0].Trim();Technology=$x[1].Trim();Year=$year;Class=$class;Note=$note})
   }
  } finally {$sr.Dispose()}
 }
} finally {$z.Dispose()}

$lines=New-Object System.Collections.Generic.List[string]
$lines.Add('TGCV MT4-5 — EX ANTE SUFFICIENCY AUDIT 001')
$lines.Add('================================================')
$lines.Add("ZIP=$zipPath")
$md5=(Get-FileHash $zipPath -Algorithm MD5).Hash
$sha=(Get-FileHash $zipPath -Algorithm SHA256).Hash
$lines.Add("MD5=$md5")
$lines.Add("SHA256=$sha")
$lines.Add("TECHNOLOGY_PARAMETER_RECORDS=$($rows.Count)")
$lines.Add('')
$lines.Add('PARAMETER SUMMARY')
$lines.Add('Parameter`tN`tRealization/State`tFuture`tRetrospective`tPlanning/Legal`tCandidateValidated`tTechnicalEconomic')
foreach($p in $knownTechParams){
 $q=@($rows|Where-Object Parameter -eq $p)
 if($q.Count -eq 0){continue}
 $lines.Add(('{0}`t{1}`t{2}`t{3}`t{4}`t{5}`t{6}`t{7}' -f $p,$q.Count,@($q|Where-Object Class -like 'REALIZATION*').Count,@($q|Where-Object Class -eq 'FUTURE / EXPLICIT LEAKAGE').Count,@($q|Where-Object Class -eq 'RETROSPECTIVE / HISTORICAL DEPENDENCY').Count,@($q|Where-Object Class -eq 'PLANNING / LEGAL — DATE CHECK').Count,@($q|Where-Object Class -like 'CANDIDATE*').Count,@($q|Where-Object Class -eq 'TECHNICAL/ECONOMIC — NOT SUFFICIENT ALONE').Count))
}
$lines.Add('')
$lines.Add('CANDIDATE PARAMETER COVERAGE')
$candidates=@($rows|Where-Object Parameter -in $candidateParams)
$lines.Add("CANDIDATE_RECORDS=$($candidates.Count)")
$lines.Add("CANDIDATE_FUTURE=$(@($candidates|Where-Object Class -eq 'FUTURE / EXPLICIT LEAKAGE').Count)")
$lines.Add("CANDIDATE_RETROSPECTIVE=$(@($candidates|Where-Object Class -eq 'RETROSPECTIVE / HISTORICAL DEPENDENCY').Count)")
$lines.Add("CANDIDATE_PLANNING_LEGAL=$(@($candidates|Where-Object Class -eq 'PLANNING / LEGAL — DATE CHECK').Count)")
$lines.Add("CANDIDATE_UNFLAGGED=$(@($candidates|Where-Object Class -eq 'CANDIDATE — REQUIRES TEMPORAL/SEMANTIC VALIDATION').Count)")
$lines.Add('')
$lines.Add('PRELIMINARY SUFFICIENCY')
$lines.Add('SUFFICIENT_FOR_U_tau=UNDETERMINED')
$lines.Add('SUFFICIENT_FOR_P_tau=UNDETERMINED')
$lines.Add('REASON=Temporal cleanliness alone does not establish semantic sufficiency; candidate subset requires rule-level construction and independent admissibility test.')
$lines.Add('STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION')

$lines | Set-Content $summaryPath -Encoding utf8
$rows | Sort-Object Parameter,Country,Technology,Year | Format-Table -AutoSize | Out-File $detailPath -Encoding utf8
Get-Content $summaryPath
