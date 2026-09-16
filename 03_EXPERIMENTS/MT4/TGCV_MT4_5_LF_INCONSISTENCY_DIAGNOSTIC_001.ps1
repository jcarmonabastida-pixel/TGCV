$ErrorActionPreference='Stop'
$zip="$env:USERPROFILE\Downloads\TGCV_MT4_energy_public-dataset_v2.zip"
$out="$env:USERPROFILE\Downloads\TGCV_MT4_5_LF_INCONSISTENCY_DIAGNOSTIC_001.txt"
Add-Type -AssemblyName System.IO.Compression.FileSystem
$z=[IO.Compression.ZipFile]::OpenRead($zip)
try{
 $cells=@{}
 foreach($e in $z.Entries){
  if($e.FullName -notmatch '/Technologies/.*\.csv$'){continue}
  $sr=[IO.StreamReader]::new($e.Open())
  try{
   while(($l=$sr.ReadLine()) -ne $null){
    if($l -notmatch ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)'){continue}
    $x=$l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10
    if($x.Count -lt 10){continue}
    $p=$x[2].Trim();if($p -notin @('LF_min','LF_max')){continue}
    $key="$($x[0].Trim())|$($x[1].Trim())|$($x[3].Trim())"
    if(!$cells.ContainsKey($key)){$cells[$key]=@{}}
    $cells[$key][$p]=[pscustomobject]@{Country=$x[0].Trim();Entity=$x[1].Trim();Year=$x[3].Trim();Value=$x[5].Trim().Trim('"');Reference=$x[7].Trim().Trim('"');Note=$x[9].Trim().Trim('"')}
   }
  }finally{$sr.Dispose()}
 }
 $bad=@()
 foreach($key in $cells.Keys){$c=$cells[$key];if(!$c.ContainsKey('LF_min') -or !$c.ContainsKey('LF_max')){continue};$a=0.0;$b=0.0;$ok1=[double]::TryParse($c.LF_min.Value,[Globalization.NumberStyles]::Float,[Globalization.CultureInfo]::InvariantCulture,[ref]$a);$ok2=[double]::TryParse($c.LF_max.Value,[Globalization.NumberStyles]::Float,[Globalization.CultureInfo]::InvariantCulture,[ref]$b);if($ok1 -and $ok2 -and $a -gt $b){$bad += [pscustomobject]@{Country=$c.LF_min.Country;Entity=$c.LF_min.Entity;Year=$c.LF_min.Year;LF_min=$a;LF_max=$b;Gap=$a-$b;Reference=$c.LF_min.Reference;Note=$c.LF_min.Note}}}
 $o=@();$o+='TGCV MT4-5 — LF INCONSISTENCY DIAGNOSTIC 002';$o+='ZIP='+$zip;$o+='MD5='+((Get-FileHash $zip -Algorithm MD5).Hash);$o+='SHA256='+((Get-FileHash $zip -Algorithm SHA256).Hash);$o+='LF_INCONSISTENCY_CELLS='+$bad.Count;$o+='';$o+='BY YEAR';foreach($g in ($bad|Group-Object Year|Sort-Object Name)){$o+="$($g.Name)=$($g.Count)"};$o+='';$o+='TOP ENTITIES';foreach($g in ($bad|Group-Object Entity|Sort-Object Count -Descending|Select-Object -First 25)){$o+="$($g.Name)=$($g.Count)"};$o+='';$o+='TOP COUNTRIES';foreach($g in ($bad|Group-Object Country|Sort-Object Count -Descending|Select-Object -First 25)){$o+="$($g.Name)=$($g.Count)"};$o+='';$o+='INTERPRETATION_BOUNDARY=Diagnostic only; no repair, imputation, exclusion, or P_tau sufficiency claim.';$o+='STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION';$o|Set-Content $out -Encoding UTF8;Write-Output "OUTPUT=$out";Write-Output "LF_INCONSISTENCY_CELLS=$($bad.Count)";Write-Output "SHA256=$((Get-FileHash $zip -Algorithm SHA256).Hash)";Write-Output "MD5=$((Get-FileHash $zip -Algorithm MD5).Hash)"
}finally{$z.Dispose()}