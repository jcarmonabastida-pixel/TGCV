# TGCV MT4-5 — Structural Ex Ante Coverage Auditor 001
# Purpose: test whether a candidate ex-ante admissibility information set is jointly
# available for country-technology-year cells, without treating availability as proof
# of semantic sufficiency. Analytical diagnostic only; not a gate decision.

$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zipPath="$env:USERPROFILE\Downloads\TGCV_MT4_energy_public-dataset_v2.zip"
$outPath="$env:USERPROFILE\Downloads\TGCV_MT4_5_STRUCTURAL_COVERAGE_SUMMARY_001.txt"

# Minimal technical candidate set. These variables are not realization outcomes.
$sets=[ordered]@{
 'CORE_6'=@('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
 'CORE_6_PLUS_LIFETIME'=@('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource','Lifetime')
 'CORE_6_PLUS_POTENTIAL_INSTALLED'=@('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource','Potential_installed')
}

# We require a nonblank Value field for presence. Actual_* are deliberately excluded.
$all=New-Object 'System.Collections.Generic.HashSet[string]'
$presence=@{}
$z=[IO.Compression.ZipFile]::OpenRead($zipPath)
try {
 foreach($e in $z.Entries){
  if($e.FullName -notmatch '/Technologies/.*\.csv$'){continue}
  $sr=[IO.StreamReader]::new($e.Open())
  try {
   while(($l=$sr.ReadLine()) -ne $null){
    if($l -notmatch ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)'){continue}
    $x=$l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10
    if($x.Count -lt 10){continue}
    $p=$x[2].Trim()
    $wanted=$false
    foreach($s in $sets.Values){if($s -contains $p){$wanted=$true;break}}
    if(-not $wanted){continue}
    $country=$x[0].Trim();$tech=$x[1].Trim();$year=$x[3].Trim();$value=$x[5].Trim().Trim('"')
    if([string]::IsNullOrWhiteSpace($country)-or[string]::IsNullOrWhiteSpace($tech)-or[string]::IsNullOrWhiteSpace($year)){continue}
    $key="$country|$tech|$year"
    $all.Add($key)|Out-Null
    if(-not $presence.ContainsKey($key)){$presence[$key]=@{}}
    if(-not [string]::IsNullOrWhiteSpace($value)){$presence[$key][$p]=$true}
   }
  } finally {$sr.Dispose()}
 }
} finally {$z.Dispose()}

$lines=New-Object System.Collections.Generic.List[string]
$lines.Add('TGCV MT4-5 — STRUCTURAL EX ANTE COVERAGE AUDIT 001')
$lines.Add('====================================================')
$lines.Add("ZIP=$zipPath")
$lines.Add("MD5=$((Get-FileHash $zipPath -Algorithm MD5).Hash)")
$lines.Add("SHA256=$((Get-FileHash $zipPath -Algorithm SHA256).Hash)")
$lines.Add("UNIQUE_COUNTRY_TECHNOLOGY_YEAR_CELLS=$($all.Count)")
$lines.Add('')
$lines.Add('SET COVERAGE')
$lines.Add('Set`tRequiredParameters`tCompleteCells`tIncompleteCells`tCoveragePct')
foreach($name in $sets.Keys){
 $req=$sets[$name];$complete=0
 foreach($k in $all){$h=$presence[$k];$ok=$true;foreach($p in $req){if(-not $h.ContainsKey($p)){$ok=$false;break}};if($ok){$complete++}}
 $incomplete=$all.Count-$complete;$pct=if($all.Count){[math]::Round(100*$complete/$all.Count,2)}else{0}
 $lines.Add(('{0}`t{1}`t{2}`t{3}`t{4}'-f $name,($req -join '+'),$complete,$incomplete,$pct))
}
$lines.Add('')
$lines.Add('INTERPRETATION')
$lines.Add('1. Complete cell coverage means only that the required variables have nonblank values in the same country-technology-year cell.')
$lines.Add('2. It does not establish that the variables are sufficient to define P_tau or that their values were point-in-time admissible.')
$lines.Add('3. Potential_installed is reported as an optional extension because its semantics remain heterogeneous and date-sensitive.')
$lines.Add('4. Potential_annual and Buildrates are excluded from the minimum candidate set because prior temporal audit identified substantial retrospective/future dependencies.')
$lines.Add('SUFFICIENT_FOR_P_tau=UNDETERMINED')
$lines.Add('STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION')
$lines | Set-Content $outPath -Encoding utf8
Get-Content $outPath
