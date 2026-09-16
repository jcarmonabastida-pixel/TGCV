# TGCV MT4-5 — CORE_6 Variation Auditor 001
# Purpose: characterize variation/information content of the six CORE_6 candidate parameters.
# Diagnostic only; no P_tau sufficiency or gate decision.
$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zipPath="$env:USERPROFILE\Downloads\TGCV_MT4_energy_public-dataset_v2.zip"
$outPath="$env:USERPROFILE\Downloads\TGCV_MT4_5_CORE6_VARIATION_SUMMARY_001.txt"
$core=@('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
$stats=@{};foreach($p in $core){$stats[$p]=@{N=0;NonBlank=0;Numeric=0;NonNumeric=0;Values=@{};Min=$null;Max=$null}}
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
    $s=$stats[$p];$s.N++
    $v=$x[5].Trim().Trim('"')
    if([string]::IsNullOrWhiteSpace($v)){continue}
    $s.NonBlank++
    if(-not $s.Values.ContainsKey($v)){$s.Values[$v]=0};$s.Values[$v]++
    $d=0.0
    if([double]::TryParse($v,[Globalization.NumberStyles]::Float,[Globalization.CultureInfo]::InvariantCulture,[ref]$d)){
      $s.Numeric++
      if($null -eq $s.Min -or $d -lt $s.Min){$s.Min=$d};if($null -eq $s.Max -or $d -gt $s.Max){$s.Max=$d}
    } else {$s.NonNumeric++}
   }
  } finally {$sr.Dispose()}
 }
} finally {$z.Dispose()}
$sha=(Get-FileHash $zipPath -Algorithm SHA256).Hash;$md5=(Get-FileHash $zipPath -Algorithm MD5).Hash
$o=@('TGCV MT4-5 — CORE_6 VARIATION AUDIT 001','============================================','ZIP='+$zipPath,'MD5='+$md5,'SHA256='+$sha,'')
foreach($p in $core){$s=$stats[$p];$o+="PARAMETER=$p";$o+="RECORDS=$($s.N)";$o+="NONBLANK=$($s.NonBlank)";$o+="UNIQUE_VALUES=$($s.Values.Count)";$o+="NUMERIC=$($s.Numeric)";$o+="NONNUMERIC=$($s.NonNumeric)";if($null -ne $s.Min){$o+="MIN=$($s.Min.ToString('G17',[Globalization.CultureInfo]::InvariantCulture))";$o+="MAX=$($s.Max.ToString('G17',[Globalization.CultureInfo]::InvariantCulture))"}else{$o+='MIN=N/A';$o+='MAX=N/A'};if($s.Values.Count -le 20){$o+='VALUES='+ (($s.Values.Keys|Sort-Object) -join ' | ')}else{$o+='TOP_VALUES='+ (($s.Values.GetEnumerator()|Sort-Object Value -Descending|Select-Object -First 10|ForEach-Object {"$($_.Key)($($_.Value))"}) -join ' | ')};$o+=''}
$o+='INTERPRETATION=Variation/information-content diagnostic only; distinct values and ranges do not establish semantic sufficiency for P_tau.';$o+='SUFFICIENT_FOR_P_tau=UNDETERMINED';$o+='STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION'
$o|Set-Content $outPath -Encoding UTF8
Write-Output "OUTPUT=$outPath";Write-Output "SHA256=$sha";Write-Output "MD5=$md5";foreach($p in $core){$s=$stats[$p];Write-Output "$p`tn=$($s.N)`tnonblank=$($s.NonBlank)`tunique=$($s.Values.Count)`tnumeric=$($s.Numeric)"}
