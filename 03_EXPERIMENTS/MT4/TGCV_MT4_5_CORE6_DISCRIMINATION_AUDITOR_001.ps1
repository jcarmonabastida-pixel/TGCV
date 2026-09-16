$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$zip = Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$out = Join-Path $env:USERPROFILE 'Downloads\TGCV_MT4_5_CORE6_DISCRIMINATION_SUMMARY_001.txt'

if (-not (Test-Path -LiteralPath $zip)) { throw "Frozen ZIP not found: $zip" }

$sha256 = (Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash.ToUpperInvariant()
$md5 = (Get-FileHash -LiteralPath $zip -Algorithm MD5).Hash.ToUpperInvariant()

$core = @('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
$required = @{}
foreach ($p in $core) { $required[$p] = $true }

function Parse-CsvLine([string]$line) {
    return $line -split ',(?=(?:[^"]*"[^"]*")*[^"]*$)', 10
}

function Clean([string]$s) {
    if ($null -eq $s) { return '' }
    return $s.Trim().Trim('"')
}

# key = country|technology|year ; value = parameter/value map
$cells = @{}

$archive = [System.IO.Compression.ZipFile]::OpenRead($zip)
try {
    foreach ($entry in $archive.Entries) {
        if ($entry.FullName -notmatch '/Technologies/[^/]+\.csv$') { continue }

        $parts = $entry.FullName -split '/'
        if ($parts.Count -lt 3) { continue }
        $country = $parts[$parts.Count-2]
        $technologyFile = [System.IO.Path]::GetFileNameWithoutExtension($parts[$parts.Count-1])
        $technology = $technologyFile -replace '^'+[regex]::Escape($country)+'_',''

        $sr = New-Object System.IO.StreamReader($entry.Open())
        try {
            $header = $null
            while (-not $sr.EndOfStream) {
                $l = $sr.ReadLine()
                if ($l -and -not $l.StartsWith('#')) { $header = Parse-CsvLine $l; break }
            }
            if ($null -eq $header) { continue }
            $idx = @{}
            for ($i=0; $i -lt $header.Count; $i++) { $idx[(Clean $header[$i])] = $i }
            foreach ($h in @('Country','Entity','Parameter','Year','Value')) { if (-not $idx.ContainsKey($h)) { continue } }

            while (-not $sr.EndOfStream) {
                $l = $sr.ReadLine()
                if ([string]::IsNullOrWhiteSpace($l)) { continue }
                $x = Parse-CsvLine $l
                if ($x.Count -lt 5) { continue }
                $parameter = Clean $x[$idx['Parameter']]
                if (-not $required.ContainsKey($parameter)) { continue }
                $year = Clean $x[$idx['Year']]
                if ($year -notmatch '^\d{4}$') { continue }
                $value = Clean $x[$idx['Value']]
                $key = "$country|$technology|$year"
                if (-not $cells.ContainsKey($key)) { $cells[$key] = @{} }
                $cells[$key][$parameter] = $value
            }
        }
        finally { $sr.Dispose() }
    }
}
finally { $archive.Dispose() }

# Build within-country-year discrimination statistics.
$groups = @{}
$completeCells = 0
$incompleteCells = 0
foreach ($key in $cells.Keys) {
    $c = $cells[$key]
    $complete = $true
    foreach ($p in $core) {
        if (-not $c.ContainsKey($p) -or [string]::IsNullOrWhiteSpace($c[$p])) { $complete = $false; break }
    }
    if (-not $complete) { $incompleteCells++; continue }
    $completeCells++
    $parts = $key -split '\|'
    $groupKey = "$($parts[0])|$($parts[2])"
    if (-not $groups.ContainsKey($groupKey)) { $groups[$groupKey] = @() }
    $signature = (($core | ForEach-Object { Clean $c[$_] }) -join '||')
    $groups[$groupKey] += [pscustomobject]@{ Technology=$parts[1]; Signature=$signature }
}

$totalGroups = $groups.Count
$groupsWith2Plus = 0
$groupsWithUniqueSignatures = 0
$groupsWithDuplicates = 0
$totalCompleteTechnologySlots = 0
$totalDistinctSignatures = 0
$totalDuplicateTechnologySlots = 0
$maxTechnologies = 0
$maxDistinctSignatures = 0

$signatureFreq = @{}
foreach ($gk in $groups.Keys) {
    $rows = $groups[$gk]
    $n = $rows.Count
    $u = @($rows | Select-Object -ExpandProperty Signature -Unique).Count
    $totalCompleteTechnologySlots += $n
    $totalDistinctSignatures += $u
    if ($n -ge 2) { $groupsWith2Plus++ }
    if ($u -ge 2) { $groupsWithUniqueSignatures++ }
    if ($u -lt $n) { $groupsWithDuplicates++; $totalDuplicateTechnologySlots += ($n-$u) }
    if ($n -gt $maxTechnologies) { $maxTechnologies=$n }
    if ($u -gt $maxDistinctSignatures) { $maxDistinctSignatures=$u }
    foreach ($r in $rows) {
        if (-not $signatureFreq.ContainsKey($r.Signature)) { $signatureFreq[$r.Signature]=0 }
        $signatureFreq[$r.Signature]++
    }
}

$globalUniqueSignatures = $signatureFreq.Count
$globalRepeatedSignatures = @($signatureFreq.Values | Where-Object { $_ -gt 1 }).Count
$globalRepeatedSlots = (($signatureFreq.Values | Where-Object { $_ -gt 1 }) | Measure-Object -Sum).Sum
if ($null -eq $globalRepeatedSlots) { $globalRepeatedSlots = 0 }

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add('TGCV MT4-5 — CORE_6 DISCRIMINATION AUDIT 001')
$lines.Add('STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION')
$lines.Add("ZIP=$zip")
$lines.Add("SHA256=$sha256")
$lines.Add("MD5=$md5")
$lines.Add('')
$lines.Add('OBJECTIVE')
$lines.Add('Test whether CORE_6 values can discriminate multiple technological profiles within the same country-year, without defining those profiles as T_acc or P_tau.')
$lines.Add('')
$lines.Add('CELL COUNTS')
$lines.Add("TOTAL_TECHNOLOGY_YEAR_CELLS=$($cells.Count)")
$lines.Add("COMPLETE_CORE6_CELLS=$completeCells")
$lines.Add("INCOMPLETE_CORE6_CELLS=$incompleteCells")
$lines.Add('')
$lines.Add('WITHIN-COUNTRY-YEAR DISCRIMINATION')
$lines.Add("COUNTRY_YEAR_GROUPS=$totalGroups")
$lines.Add("GROUPS_WITH_2PLUS_COMPLETE_TECHNOLOGIES=$groupsWith2Plus")
$lines.Add("GROUPS_WITH_2PLUS_DISTINCT_CORE6_SIGNATURES=$groupsWithUniqueSignatures")
$lines.Add("GROUPS_WITH_CORE6_DUPLICATE_SIGNATURES=$groupsWithDuplicates")
$lines.Add("TOTAL_COMPLETE_TECHNOLOGY_SLOTS=$totalCompleteTechnologySlots")
$lines.Add("TOTAL_DISTINCT_CORE6_SIGNATURES_WITHIN_GROUPS=$totalDistinctSignatures")
$lines.Add("TOTAL_DUPLICATE_TECHNOLOGY_SLOTS_WITHIN_GROUPS=$totalDuplicateTechnologySlots")
$lines.Add("MAX_COMPLETE_TECHNOLOGIES_IN_COUNTRY_YEAR=$maxTechnologies")
$lines.Add("MAX_DISTINCT_CORE6_SIGNATURES_IN_COUNTRY_YEAR=$maxDistinctSignatures")
$lines.Add('')
$lines.Add('GLOBAL SIGNATURE REPETITION')
$lines.Add("GLOBAL_UNIQUE_CORE6_SIGNATURES=$globalUniqueSignatures")
$lines.Add("GLOBAL_SIGNATURES_REPEATED_ACROSS_CELLS=$globalRepeatedSignatures")
$lines.Add("GLOBAL_SLOTS_BELONGING_TO_REPEATED_SIGNATURES=$globalRepeatedSlots")
$lines.Add('')
$lines.Add('INTERPRETATION')
$lines.Add('1. Distinct CORE_6 signatures within the same country-year show that the variables can distinguish technological profiles under a common country-year context.')
$lines.Add('2. Duplicate signatures show that CORE_6 is not uniquely identifying every technology; non-identification does not imply failure of P_tau.')
$lines.Add('3. This audit does not establish that a CORE_6 signature is a transformation, an accessible transformation, or a sufficient admissibility rule.')
$lines.Add('4. Country-year grouping is used only as a diagnostic control for contextual comparability; no causal or accessibility claim is made.')
$lines.Add('')
$lines.Add('SUFFICIENT_FOR_P_tau=UNDETERMINED')
$lines.Add('DECISION=DIAGNOSTIC ONLY')

[System.IO.File]::WriteAllLines($out, $lines)

Write-Output "OUTPUT=$out"
Write-Output "SHA256=$sha256"
Write-Output "MD5=$md5"
Write-Output "COMPLETE_CORE6_CELLS=$completeCells"
Write-Output "COUNTRY_YEAR_GROUPS=$totalGroups"
Write-Output "GROUPS_2PLUS_TECH=$groupsWith2Plus"
Write-Output "GROUPS_2PLUS_DISTINCT_SIGNATURES=$groupsWithUniqueSignatures"
Write-Output "GROUPS_WITH_DUPLICATE_SIGNATURES=$groupsWithDuplicates"
Write-Output "GLOBAL_UNIQUE_SIGNATURES=$globalUniqueSignatures"
Write-Output "SUFFICIENT_FOR_P_tau=UNDETERMINED"
Write-Output "STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION"
