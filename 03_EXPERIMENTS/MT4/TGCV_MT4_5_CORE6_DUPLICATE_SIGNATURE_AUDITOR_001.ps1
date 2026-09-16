$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip=Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$out=Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_5_CORE6_DUPLICATE_SIGNATURE_SUMMARY_001.txt'
$core=@('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
function Parse([string]$l){$l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10}
function Clean([string]$s){if($null-eq$s){return ''};$s.Trim().Trim('"')}
$cells=@{}
$z=[IO.Compression.ZipFile]::OpenRead($zip)
try{foreach($e in $z.Entries){if($e.FullName -notmatch '/Technologies/.*\.csv$'){continue};$r=[IO.StreamReader]::new($e.Open());try{while(($l=$r.ReadLine())-ne$null){if([string]::IsNullOrWhiteSpace($l)){continue};$x=Parse $l;if($x.Count-lt 10){continue};$country=Clean $x[0];$tech=Clean $x[1];$par=Clean $x[2];$yr=Clean $x[3];$v=Clean $x[5];if($core-notcontains$par){continue};if($yr-notmatch '^\d{4}$'){continue};if([string]::IsNullOrWhiteSpace($country)-or[string]::IsNullOrWhiteSpace($tech)){continue};$k="$country|$tech|$yr";if(!$cells.ContainsKey($k)){$cells[$k]=@{}};$cells[$k][$par]=$v}}finally{$r.Dispose()}}}finally{$z.Dispose()}
$groups=@{}
foreach($k in $cells.Keys){$c=$cells[$k];$ok=$true;foreach($p in $core){if(!$c.ContainsKey($p)-or[string]::IsNullOrWhiteSpace($c[$p])){$ok=$false;break}};if(!$ok){continue};$q=$k-split '\|';$g="$($q[0])|$($q[2])";if(!$groups.ContainsKey($g)){$groups[$g]=@()};$sig=(($core|%{Clean $c[$_]})-join '||');$groups[$g]+=[pscustomobject]@{Technology=$q[1];Signature=$sig;Values=($core|%{"$_=$(Clean $c[$_])"}) -join ';'}}
$dups=@()
foreach($g in $groups.Keys){$rows=$groups[$g];$by=@{};foreach($r in $rows){if(!$by.ContainsKey($r.Signature)){$by[$r.Signature]=@()};$by[$r.Signature]+=$r};foreach($sig in $by.Keys){$rs=$by[$sig];if($rs.Count-gt 1){$dups+=[pscustomobject]@{CountryYear=$g;TechnologyCount=$rs.Count;Technologies=($rs.Technology-join ',');Signature=$sig;Values=$rs[0].Values}}}}
$sha=(Get-FileHash $zip -Algorithm SHA256).Hash.ToUpperInvariant();$md5=(Get-FileHash $zip -Algorithm MD5).Hash.ToUpperInvariant()
$lines=New-Object Collections.Generic.List[string]
$lines.Add('TGCV MT4-5 - CORE_6 DUPLICATE SIGNATURE AUDIT 001');$lines.Add('STATUS=ANALYTICAL DIAGNOSTIC - NOT A FINAL MT4-5 GATE DECISION');$lines.Add("ZIP=$zip");$lines.Add("SHA256=$sha");$lines.Add("MD5=$md5");$lines.Add("DUPLICATE_SIGNATURE_GROUPS=$($dups.Count)");$lines.Add('')
foreach($d in $dups){$lines.Add("COUNTRY_YEAR=$($d.CountryYear)");$lines.Add("TECHNOLOGY_COUNT=$($d.TechnologyCount)");$lines.Add("TECHNOLOGIES=$($d.Technologies)");$lines.Add("CORE6_SIGNATURE=$($d.Signature)");$lines.Add("CORE6_VALUES=$($d.Values)");$lines.Add('')}
$lines.Add('INTERPRETATION=Requires semantic inspection of the named technologies; duplicate CORE6 signatures do not by themselves refute or establish P_tau sufficiency.');$lines.Add('SUFFICIENT_FOR_P_tau=UNDETERMINED')
[IO.File]::WriteAllLines($out,$lines)
Write-Output "OUTPUT=$out";Write-Output "SHA256=$sha";Write-Output "MD5=$md5";Write-Output "DUPLICATE_SIGNATURE_GROUPS=$($dups.Count)";foreach($d in $dups){Write-Output "COUNTRY_YEAR=$($d.CountryYear)";Write-Output "TECHNOLOGIES=$($d.Technologies)";Write-Output "CORE6_VALUES=$($d.Values)"};Write-Output 'SUFFICIENT_FOR_P_tau=UNDETERMINED';Write-Output 'STATUS=ANALYTICAL DIAGNOSTIC - NOT A FINAL MT4-5 GATE DECISION'