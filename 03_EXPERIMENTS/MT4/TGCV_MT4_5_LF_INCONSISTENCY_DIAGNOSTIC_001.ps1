$ErrorActionPreference='Stop'
$zip='C:\Users\pedri\Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$out='C:\Users\pedri\Downloads\TGCV_MT4_5_LF_INCONSISTENCY_DIAGNOSTIC_001.txt'
if(!(Test-Path $zip)){throw "ZIP_NOT_FOUND=$zip"}
Add-Type -AssemblyName System.IO.Compression.FileSystem
$sha=(Get-FileHash $zip -Algorithm SHA256).Hash
$md5=(Get-FileHash $zip -Algorithm MD5).Hash
$z=[IO.Compression.ZipFile]::OpenRead($zip)
try{
 $rows=@()
 foreach($e in $z.Entries){
  if($e.FullName -notmatch '/Technologies/[^/]+\.csv$'){continue}
  $sr=New-Object IO.StreamReader($e.Open())
  try{$txt=$sr.ReadToEnd()}finally{$sr.Dispose()}
  $lines=$txt -split "`r?`n"
  if($lines.Count -lt 2){continue}
  $h=$lines[0].Split(',')
  $idx=@{}; for($i=0;$i -lt $h.Count;$i++){$idx[$h[$i].Trim()]=$i}
  foreach($ln in $lines[1..($lines.Count-1)]){
   if([string]::IsNullOrWhiteSpace($ln)){continue}
   $f=$ln.Split(',')
   if(!$idx.ContainsKey('Parameter') -or $f[$idx['Parameter']] -notin @('LF_min','LF_max')){continue}
   $rows += [pscustomobject]@{File=$e.FullName;Country=$f[$idx['Country']];Entity=$f[$idx['Entity']];Parameter=$f[$idx['Parameter']];Year=$f[$idx['Year']];Value=$f[$idx['Value']];Unit=$f[$idx['Unit']];Reference=$f[$idx['Reference']];Note=$f[$idx['Note']]}
  }
 }
 $cells=@{}
 foreach($r in $rows){$k="$($r.Country)|$($r.Entity)|$($r.Year)";if(!$cells.ContainsKey($k)){$cells[$k]=@{}};$cells[$k][$r.Parameter]=$r}
 $bad=@(); $classes=@{}
 foreach($k in $cells.Keys){$c=$cells[$k];if(!$c.ContainsKey('LF_min') -or !$c.ContainsKey('LF_max')){continue};$a=0.0;$b=0.0;$ok1=[double]::TryParse($c['LF_min'].Value,[Globalization.NumberStyles]::Float,[Globalization.CultureInfo]::InvariantCulture,[ref]$a);$ok2=[double]::TryParse($c['LF_max'].Value,[Globalization.NumberStyles]::Float,[Globalization.CultureInfo]::InvariantCulture,[ref]$b);if($ok1 -and $ok2 -and $a -gt $b){$gap=$a-$b;$ref="$($c['LF_min'].Reference)|$($c['LF_max'].Reference)";$note="$($c['LF_min'].Note)|$($c['LF_max'].Note)";$bad += [pscustomobject]@{Country=$c['LF_min'].Country;Entity=$c['LF_min'].Entity;Year=$c['LF_min'].Year;LF_min=$a;LF_max=$b;Gap=$gap;Reference=$ref;Note=$note}}}
 $byYear=$bad|Group-Object Year|Sort-Object Name
 $byEntity=$bad|Group-Object Entity|Sort-Object Count -Descending
 $byCountry=$bad|Group-Object Country|Sort-Object Count -Descending
 $gapBins=@{'>0-0.05'=0;'>0.05-0.10'=0;'>0.10-0.25'=0;'>0.25-0.50'=0;'>0.50-1.00'=0;'>1.00'=0};foreach($x in $bad){if($x.Gap -le .05){$gapBins['>0-0.05']++}elseif($x.Gap -le .1){$gapBins['>0.05-0.10']++}elseif($x.Gap -le .25){$gapBins['>0.10-0.25']++}elseif($x.Gap -le .5){$gapBins['>0.25-0.50']++}elseif($x.Gap -le 1){$gapBins['>0.50-1.00']++}else{$gapBins['>1.00']++}}
 $notes=$bad|Where-Object {$_.Note -or $_.Reference}|ForEach-Object {($_.Note+' '+$_.Reference).Trim()}|Group-Object|Sort-Object Count -Descending
 $o=@();$o+='TGCV MT4-5 — LF INCONSISTENCY DIAGNOSTIC 001';$o+='ZIP='+$zip;$o+='MD5='+$md5;$o+='SHA256='+$sha;$o+='LF_INCONSISTENCY_CELLS='+$bad.Count;$o+='';$o+='GAP BINS';foreach($k in $gapBins.Keys|Sort-Object){$o+="$k=$($gapBins[$k])"};$o+='';$o+='BY YEAR';foreach($g in $byYear){$o+="$($g.Name)=$($g.Count)"};$o+='';$o+='TOP ENTITIES';foreach($g in ($byEntity|Select-Object -First 25)){$o+="$($g.Name)=$($g.Count)"};$o+='';$o+='TOP COUNTRIES';foreach($g in ($byCountry|Select-Object -First 25)){$o+="$($g.Name)=$($g.Count)"};$o+='';$o+='TOP NOTE/REFERENCE PATTERNS';foreach($g in ($notes|Select-Object -First 25)){$s=($g.Name -replace '\s+',' ');if($s.Length -gt 220){$s=$s.Substring(0,220)};$o+="$($g.Count)=$s"};$o+='';$o+='INTERPRETATION_BOUNDARY=This diagnostic identifies internal LF_min/LF_max inconsistencies only. It does not repair, impute, redefine, or exclude records and does not establish P_tau sufficiency.';$o+='STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION';$o|Set-Content -Encoding UTF8 $out;Write-Output "OUTPUT=$out";Write-Output "LF_INCONSISTENCY_CELLS=$($bad.Count)";Write-Output "SHA256=$sha";Write-Output "MD5=$md5"
}finally{$z.Dispose()}