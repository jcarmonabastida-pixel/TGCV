$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip=Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$out=Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_5_EST_HYDRO_CORE6_COLLISION_INSPECTION_001.txt'
function Parse([string]$l){$l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10}
function Clean([string]$s){if($null-eq$s){return ''};$s.Trim().Trim('"')}
$rows=@{}
$z=[IO.Compression.ZipFile]::OpenRead($zip)
try{foreach($e in $z.Entries){if($e.FullName -notmatch '/Technologies/(HydroRoR|HydroDam)\.csv$'){continue};$r=[IO.StreamReader]::new($e.Open());try{while(($l=$r.ReadLine())-ne$null){$x=Parse $l;if($x.Count-lt 10){continue};$country=Clean $x[0];$tech=Clean $x[1];$par=Clean $x[2];$year=Clean $x[3];$value=Clean $x[5];if($country-ne'EST'-or$year-ne'1990'){continue};if(!$rows.ContainsKey($tech)){$rows[$tech]=@{}};$rows[$tech][$par]=$value}}finally{$r.Dispose()}}}finally{$z.Dispose()}
$sha=(Get-FileHash $zip -Algorithm SHA256).Hash.ToUpperInvariant();$md5=(Get-FileHash $zip -Algorithm MD5).Hash.ToUpperInvariant()
$lines=New-Object Collections.Generic.List[string];$lines.Add('TGCV MT4-5 - EST 1990 HYDRO CORE6 COLLISION INSPECTION 001');$lines.Add('STATUS=ANALYTICAL DIAGNOSTIC - NOT A FINAL MT4-5 GATE DECISION');$lines.Add("SHA256=$sha");$lines.Add("MD5=$md5");$lines.Add('')
foreach($tech in @('HydroRoR','HydroDam')){$lines.Add("TECHNOLOGY=$tech");foreach($p in ($rows[$tech].Keys|Sort-Object)){$lines.Add("$p=$($rows[$tech][$p])")};$lines.Add('')}
$lines.Add('CORE6_COLLISION=HydroRoR and HydroDam share the same CORE6 signature in EST 1990.');$lines.Add('PURPOSE=Inspect non-CORE6 parameters to determine whether the collision is a harmless representational equivalence or evidence that CORE6 omits relevant distinctions.');$lines.Add('SUFFICIENT_FOR_P_tau=UNDETERMINED');[IO.File]::WriteAllLines($out,$lines)
Write-Output "OUTPUT=$out";Write-Output "SHA256=$sha";Write-Output "MD5=$md5";Write-Output 'TECHNOLOGIES=HydroRoR,HydroDam';foreach($tech in @('HydroRoR','HydroDam')){Write-Output "TECHNOLOGY=$tech";foreach($p in ($rows[$tech].Keys|Sort-Object)){Write-Output "$p=$($rows[$tech][$p])"}};Write-Output 'SUFFICIENT_FOR_P_tau=UNDETERMINED';Write-Output 'STATUS=ANALYTICAL DIAGNOSTIC - NOT A FINAL MT4-5 GATE DECISION'