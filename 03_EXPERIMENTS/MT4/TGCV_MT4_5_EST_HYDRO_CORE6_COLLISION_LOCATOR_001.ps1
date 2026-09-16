$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip=Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$out=Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_5_EST_HYDRO_CORE6_COLLISION_LOCATOR_001.txt'
$z=[IO.Compression.ZipFile]::OpenRead($zip)
try{$hits=@($z.Entries|Where-Object{$_.FullName -match 'Hydro(RoR|Dam).*\.csv$' -or $_.FullName -match '(HydroRoR|HydroDam)'}|Select-Object -ExpandProperty FullName)}finally{$z.Dispose()}
$sha=(Get-FileHash $zip -Algorithm SHA256).Hash.ToUpperInvariant();$md5=(Get-FileHash $zip -Algorithm MD5).Hash.ToUpperInvariant()
$lines=@("SHA256=$sha","MD5=$md5","HIT_COUNT=$($hits.Count)");$lines+=$hits;[IO.File]::WriteAllLines($out,$lines)
Write-Output "OUTPUT=$out";Write-Output "SHA256=$sha";Write-Output "MD5=$md5";Write-Output "HIT_COUNT=$($hits.Count)";foreach($h in $hits){Write-Output $h};Write-Output 'STATUS=DIAGNOSTIC - NO MT4-5 GATE DECISION'