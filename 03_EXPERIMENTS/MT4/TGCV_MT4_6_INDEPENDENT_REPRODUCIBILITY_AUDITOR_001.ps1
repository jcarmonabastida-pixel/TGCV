$ErrorActionPreference='Stop'
$Zip='C:\Users\pedri\Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$Expected='691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30'
$Out='C:\Users\pedri\Downloads\TGCV_MT4_6_INDEPENDENT_REPRODUCIBILITY_SUMMARY_001.txt'
$sha=(Get-FileHash -Algorithm SHA256 $Zip).Hash.ToUpper(); if($sha -ne $Expected){throw "SOURCE_HASH_MISMATCH: $sha"}
Add-Type -AssemblyName System.IO.Compression.FileSystem
$z=[IO.Compression.ZipFile]::OpenRead($Zip)
try{
 $cells=@{}; $miss=@{Fuel_efficiency=0;LF_min=0;LF_max=0;Peak_contr=0;Ramp_rate=0;Resource=0}; $total=0
 foreach($e in $z.Entries){
  if($e.FullName -notmatch '/Technologies/[^/]+\.csv$'){continue}
  $sr=New-Object IO.StreamReader($e.Open()); try{
   $h=$sr.ReadLine(); while(($l=$sr.ReadLine()) -ne $null){
    $x=$l -split ',(?=(?:[^"]*"[^"]*")*[^"]*$)',10; if($x.Count -lt 10){continue}
    $country=$x[0];$tech=$x[1];$param=$x[2];$year=$x[3]; if($year -notmatch '^\d{4}$'){continue}
    if($param -notin $miss.Keys){continue}; $k="$country|$tech|$year"; if(-not $cells.ContainsKey($k)){$cells[$k]=@{}}
    if(-not $cells[$k].ContainsKey($param)){$cells[$k][$param]=$x[5]}
   }
  }finally{$sr.Dispose()}
 }
 $total=$cells.Count; foreach($k in $cells.Keys){foreach($p in $miss.Keys){if(-not $cells[$k].ContainsKey($p) -or [string]::IsNullOrWhiteSpace($cells[$k][$p])){$miss[$p]++}}}
 $complete=$cells.Keys | Where-Object { $ok=$true; foreach($p in $miss.Keys){if(-not $cells[$_].ContainsKey($p) -or [string]::IsNullOrWhiteSpace($cells[$_][$p])){$ok=$false;break}}; $ok }
 $groups=@{}; foreach($k in $complete){$a=$k.Split('|');$g="$($a[0])|$($a[2])";if(-not $groups.ContainsKey($g)){$groups[$g]=@()};$groups[$g]+=$k}
 $groups2=$groups.Keys|Where-Object{$groups[$_].Count -ge 2};$distinct=0;$dups=0
 foreach($g in $groups2){$s=@{};foreach($k in $groups[$g]){$v=foreach($p in $miss.Keys){$cells[$k][$p]};$s[(($v -join '|'))]=1};if($s.Count -ge 2){$distinct++};if($s.Count -lt $groups[$g].Count){$dups++}}
 $coverage=[math]::Round(100*$complete.Count/$total,2)
 $lines=@("AUDIT=TGCV_MT4_6_INDEPENDENT_REPRODUCIBILITY_AUDITOR_001","SOURCE_SHA256=$sha","TOTAL_COUNTRY_TECHNOLOGY_YEAR_CELLS=$total","COMPLETE_CORE6_CELLS=$($complete.Count)","INCOMPLETE_CORE6_CELLS=$($total-$complete.Count)","CORE6_COVERAGE_PCT=$coverage")
 foreach($p in $miss.Keys){$lines+="MISSING_$p=$($miss[$p])"};$lines+="COUNTRY_YEAR_GROUPS_2PLUS_TECH=$($groups2.Count)","GROUPS_2PLUS_DISTINCT_SIGNATURES=$distinct","GROUPS_WITH_DUPLICATE_SIGNATURES=$dups","STATUS=INDEPENDENT REPRODUCIBILITY RESULT — NOT YET RECONCILED"
 Set-Content $Out $lines -Encoding UTF8;$lines;"OUTPUT=$Out"
}finally{$z.Dispose()}
