# TGCV MT4-5 — CORE_6 Missingness Auditor 001
# Purpose: decompose the 989 incomplete CORE_6 country-technology-year cells.
# Diagnostic only; no P_tau sufficiency or gate decision.
$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zipPath="$env:USERPROFILE\Downloads\TGCV_MT4_energy_public-dataset_v2.zip"
$outPath="$env:USERPROFILE\Downloads\TGCV_MT4_5_CORE6_MISSINGNESS_SUMMARY_001.txt"
$core=@('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
$all=@{}
$z=[IO.Compression.ZipFile]::OpenRead($zipPath)
try {
 foreach($e in $z.Entries){
  if($e.FullName -notmatch '/Technologies/.*\.csv$'){continue}
  $sr=[IO.StreamReader]::new($e.Open())
  try {
   while(($l=$sr.ReadLine()) -ne $null){
    $x=$l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10
    if($x.Count -lt 10){continue}
    $p=$x[2].Trim();if($core -notcontains $p){continue}
    $country=$x[0].Trim();$tech=$x[1].Trim();$year=$x[3].Trim();$value=$x[5].Trim().Trim('"')
    if([string]::IsNullOrWhiteSpace($country)-or[string]::IsNullOrWhiteSpace($tech)-or[string]::IsNullOrWhiteSpace($year)){continue}
    $key="$country|$tech|$year"
    if(-not $all.ContainsKey($key)){$all[$key]=@{}}
    $all[$key][$p]=(-not [string]::IsNullOrWhiteSpace($value))
   }
  } finally {$sr.Dispose()}
 }
} finally {$z.Dispose()}

$pattern=@{}
$missingByParam=@{}
$incomplete=@{}
foreach($key in $all.Keys){
 $h=$all[$key];$miss=@($core|Where-Object {-not $h.ContainsKey($_) -or -not $h[$_]})
 if($miss.Count -gt 0){
  $incomplete[$key]=$miss
  $sig=$miss -join '+'
  if(-not $pattern.ContainsKey($sig)){$pattern[$sig]=0};$pattern[$sig]++
  foreach($p in $miss){if(-not $missingByParam.ContainsKey($p)){$missingByParam[$p]=0};$missingByParam[$p]++}
 }
}
$country=@{};$tech=@{}
foreach($key in $incomplete.Keys){$parts=$key -split '\|',3;$c=$parts[0];$t=$parts[1];if(-not $country.ContainsKey($c)){$country[$c]=0};$country[$c]++;if(-not $tech.ContainsKey($t)){$tech[$t]=0};$tech[$t]++}
$sha=(Get-FileHash $zipPath -Algorithm SHA256).Hash;$md5=(Get-FileHash $zipPath -Algorithm MD5).Hash
$o=@()
$o+='TGCV MT4-5 — CORE_6 MISSINGNESS AUDIT 001'
$o+='============================================='
$o+="ZIP=$zipPath";$o+="MD5=$md5";$o+="SHA256=$sha";$o+="TOTAL_CORE6_CELLS=$($all.Count)";$o+="INCOMPLETE_CORE6_CELLS=$($incomplete.Count)";$o+=''
$o+='MISSING_BY_PARAMETER';foreach($p in $core){$o+="$p=$($missingByParam[$p])"};$o+=''
$o+='MISSINGNESS_PATTERNS';foreach($k in ($pattern.Keys|Sort-Object {[int]$pattern[$_]} -Descending)){$o+="$k=$($pattern[$k])"};$o+=''
$o+='TOP_25_COUNTRIES_BY_INCOMPLETE_CELLS';foreach($k in ($country.Keys|Sort-Object {[int]$country[$_]} -Descending|Select-Object -First 25)){$o+="$k=$($country[$k])"};$o+=''
$o+='TOP_25_TECHNOLOGIES_BY_INCOMPLETE_CELLS';foreach($k in ($tech.Keys|Sort-Object {[int]$tech[$_]} -Descending|Select-Object -First 25)){$o+="$k=$($tech[$k])"};$o+=''
$o+='INTERPRETATION=Missingness decomposition only; no inference that missing cells invalidate or validate P_tau.';$o+='SUFFICIENT_FOR_P_tau=UNDETERMINED';$o+='STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION'
$o|Set-Content $outPath -Encoding UTF8
Write-Output "OUTPUT=$outPath";Write-Output "TOTAL_CORE6_CELLS=$($all.Count)";Write-Output "INCOMPLETE_CORE6_CELLS=$($incomplete.Count)";Write-Output "SHA256=$sha";Write-Output "MD5=$md5"
