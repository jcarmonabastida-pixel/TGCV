$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip=Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$out=Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_5_CORE6_DISCRIMINATION_SUMMARY_001.txt'
if(!(Test-Path -LiteralPath $zip)){throw "Frozen ZIP not found: $zip"}
$sha256=(Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash.ToUpperInvariant()
$md5=(Get-FileHash -LiteralPath $zip -Algorithm MD5).Hash.ToUpperInvariant()
$core=@('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
function Parse([string]$l){$l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10}
function Clean([string]$s){if($null-eq$s){return ''};$s.Trim().Trim('"')}
$cells=@{}
$a=[IO.Compression.ZipFile]::OpenRead($zip)
try{foreach($e in $a.Entries){if($e.FullName -notmatch '/Technologies/[^/]+\.csv$'){continue};$p=$e.FullName -split '/';$country=$p[$p.Count-2];$tf=[IO.Path]::GetFileNameWithoutExtension($p[$p.Count-1]);$tech=$tf -replace '^'+[regex]::Escape($country)+'_','';$r=New-Object IO.StreamReader($e.Open());try{$h=$null;while(!$r.EndOfStream){$l=$r.ReadLine();if($l-and !$l.StartsWith('#')){$h=Parse $l;break}};if($null-eq$h){continue};$ix=@{};for($i=0;$i-lt$h.Count;$i++){$ix[(Clean $h[$i])]=$i};while(!$r.EndOfStream){$l=$r.ReadLine();if([string]::IsNullOrWhiteSpace($l)){continue};$x=Parse $l;if($x.Count-lt 5){continue};$par=Clean $x[$ix['Parameter']];if($core-notcontains$par){continue};$yr=Clean $x[$ix['Year']];if($yr-notmatch '^\d{4}$'){continue};$v=Clean $x[$ix['Value']];$k="$country|$tech|$yr";if(!$cells.ContainsKey($k)){$cells[$k]=@{}};$cells[$k][$par]=$v}}finally{$r.Dispose()}}}finally{$a.Dispose()}
$groups=@{};$complete=0;$incomplete=0
foreach($k in $cells.Keys){$c=$cells[$k];$ok=$true;foreach($p in $core){if(!$c.ContainsKey($p)-or[string]::IsNullOrWhiteSpace($c[$p])){$ok=$false;break}};if(!$ok){$incomplete++;continue};$complete++;$q=$k-split '\|';$g="$($q[0])|$($q[2])";if(!$groups.ContainsKey($g)){$groups[$g]=@()};$sig=(($core|%{Clean $c[$_]})-join '||');$groups[$g]+=[pscustomobject]@{Technology=$q[1];Signature=$sig}}
$g2=0;$g2d=0;$gd=0;$slots=0;$dups=0;$maxn=0;$maxu=0;$freq=@{}
foreach($g in $groups.Keys){$rows=$groups[$g];$n=$rows.Count;$u=@($rows|Select-Object -ExpandProperty Signature -Unique).Count;$slots+=$n;if($n-ge 2){$g2++};if($u-ge 2){$g2d++};if($u-lt$n){$gd++;$dups+=($n-$u)};if($n-gt$maxn){$maxn=$n};if($u-gt$maxu){$maxu=$u};foreach($z in $rows){if(!$freq.ContainsKey($z.Signature)){$freq[$z.Signature]=0};$freq[$z.Signature]++}}
$lines=New-Object Collections.Generic.List[string]
@("TGCV MT4-5 - CORE_6 DISCRIMINATION AUDIT 001","STATUS=ANALYTICAL DIAGNOSTIC - NOT A FINAL MT4-5 GATE DECISION","ZIP=$zip","SHA256=$sha256","MD5=$md5",'',"TOTAL_TECHNOLOGY_YEAR_CELLS=$($cells.Count)","COMPLETE_CORE6_CELLS=$complete","INCOMPLETE_CORE6_CELLS=$incomplete",'',"COUNTRY_YEAR_GROUPS=$($groups.Count)","GROUPS_WITH_2PLUS_COMPLETE_TECHNOLOGIES=$g2","GROUPS_WITH_2PLUS_DISTINCT_CORE6_SIGNATURES=$g2d","GROUPS_WITH_CORE6_DUPLICATE_SIGNATURES=$gd","TOTAL_COMPLETE_TECHNOLOGY_SLOTS=$slots","TOTAL_DUPLICATE_TECHNOLOGY_SLOTS_WITHIN_GROUPS=$dups","MAX_COMPLETE_TECHNOLOGIES_IN_COUNTRY_YEAR=$maxn","MAX_DISTINCT_CORE6_SIGNATURES_IN_COUNTRY_YEAR=$maxu","GLOBAL_UNIQUE_CORE6_SIGNATURES=$($freq.Count)",'',"SUFFICIENT_FOR_P_tau=UNDETERMINED","DECISION=DIAGNOSTIC ONLY")|%{$lines.Add($_)}
[IO.File]::WriteAllLines($out,$lines)
Write-Output "OUTPUT=$out"
Write-Output "SHA256=$sha256"
Write-Output "MD5=$md5"
Write-Output "COMPLETE_CORE6_CELLS=$complete"
Write-Output "COUNTRY_YEAR_GROUPS=$($groups.Count)"
Write-Output "GROUPS_2PLUS_TECH=$g2"
Write-Output "GROUPS_2PLUS_DISTINCT_SIGNATURES=$g2d"
Write-Output "GROUPS_WITH_DUPLICATE_SIGNATURES=$gd"
Write-Output "GLOBAL_UNIQUE_SIGNATURES=$($freq.Count)"
Write-Output 'SUFFICIENT_FOR_P_tau=UNDETERMINED'
Write-Output 'STATUS=ANALYTICAL DIAGNOSTIC - NOT A FINAL MT4-5 GATE DECISION'