param(
    [string]$ZipPath = "$env:USERPROFILE\Downloads\TGCV_MT4_energy_public-dataset_v2.zip",
    [string]$OutputDir = "$env:USERPROFILE\Downloads"
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem

$AuditPath = Join-Path $OutputDir 'TGCV_MT4_MT5_TEMPORAL_AUDIT_001.txt'
$SummaryPath = Join-Path $OutputDir 'TGCV_MT4_MT5_TEMPORAL_SUMMARY_001.txt'
$ExceptionsPath = Join-Path $OutputDir 'TGCV_MT4_MT5_TEMPORAL_EXCEPTIONS_001.txt'

function Parse-Csv10([string]$Line) {
    return ($Line -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10)
}

function Classify-Note([int]$Year,[string]$Parameter,[string]$Note) {
    $n = $Note.Trim()
    if ([string]::IsNullOrWhiteSpace($n)) { return 'CLEAN / NOT FLAGGED' }
    if ($n -match '(?i)estimate for\s+20\d{2}|estimate.*\b20\d{2}\b|\b20\d{2}\b.*estimate') { return 'FUTURE INFORMATION / EXPLICIT LEAKAGE' }
    if ($n -match '(?i)based on\s+20\d{2}\s+estimate') { return 'RETROSPECTIVE / HISTORICAL DEPENDENCY' }
    if ($n -match '(?i)maximum historical|historical buildrate|historical value|historical generation|historical capacity') { return 'RETROSPECTIVE / HISTORICAL DEPENDENCY' }
    if ($n -match '(?i)master plan|planned plants|legally possible|resolution|referend|act on nuclear|policy|ban on new|replace older|foreseeable') { return 'PLANNING_OR_LEGAL_REQUIRES_DATE_CHECK' }
    if ($n -match '(?i)assumption|scenario|potential|technical-social') { return 'UNKNOWN / REQUIRES REVIEW' }
    return 'UNKNOWN / REQUIRES REVIEW'
}

if (-not (Test-Path -LiteralPath $ZipPath)) { throw "Frozen ZIP not found: $ZipPath" }
$sha256 = (Get-FileHash -LiteralPath $ZipPath -Algorithm SHA256).Hash
$md5 = (Get-FileHash -LiteralPath $ZipPath -Algorithm MD5).Hash

$rows = [System.Collections.Generic.List[object]]::new()
$zip = [IO.Compression.ZipFile]::OpenRead($ZipPath)
try {
    foreach ($entry in $zip.Entries) {
        if ($entry.FullName -notmatch '/Technologies/[^/]+\.csv$') { continue }
        $sr = [IO.StreamReader]::new($entry.Open())
        try {
            while (($line = $sr.ReadLine()) -ne $null) {
                if ($line -notmatch ',(Buildrates|Potential_annual|Potential_installed),') { continue }
                $x = Parse-Csv10 $line
                if ($x.Count -lt 10) { continue }
                $parameter = $x[2].Trim()
                $year = 0
                if (-not [int]::TryParse($x[3].Trim(), [ref]$year)) { continue }
                $note = $x[9].Trim().Trim('"')
                $class = Classify-Note $year $parameter $note
                $technology = $x[1].Trim()
                $country = $x[0].Trim()
                $rows.Add([pscustomobject]@{Country=$country;Technology=$technology;Parameter=$parameter;Year=$year;Class=$class;Note=$note;Source=$entry.FullName})
            }
        } finally { $sr.Dispose() }
    }
} finally { $zip.Dispose() }

$rows | Sort-Object Parameter,Year,Country,Technology | ForEach-Object {
    "{0}`t{1}`t{2}`t{3}`t{4}`t{5}`t{6}" -f $_.Country,$_.Technology,$_.Parameter,$_.Year,$_.Class,$_.Note,$_.Source
} | Set-Content -LiteralPath $AuditPath -Encoding UTF8

$summary = [System.Collections.Generic.List[string]]::new()
$summary.Add('TGCV MT4-5 TEMPORAL AUDIT 001')
$summary.Add('================================')
$summary.Add("ZIP=$ZipPath")
$summary.Add("MD5=$md5")
$summary.Add("SHA256=$sha256")
$summary.Add("TOTAL_RECORDS=$($rows.Count)")
$summary.Add('')
$summary.Add('BY_PARAMETER')
$summary.Add('Parameter`tN`tMinYear`tMaxYear')
foreach ($g in ($rows | Group-Object Parameter | Sort-Object Name)) {
    $ys = @($g.Group.Year)
    $summary.Add("$($g.Name)`t$($g.Count)`t$($ys | Measure-Object -Minimum | Select-Object -ExpandProperty Minimum)`t$($ys | Measure-Object -Maximum | Select-Object -ExpandProperty Maximum)")
}
$summary.Add('')
$summary.Add('BY_PARAMETER_AND_CLASS')
$summary.Add('Parameter`tClass`tN`tMinYear`tMaxYear')
foreach ($g in ($rows | Group-Object Parameter,Class | Sort-Object Name)) {
    $ys = @($g.Group.Year)
    $summary.Add("$($g.Group[0].Parameter)`t$($g.Group[0].Class)`t$($g.Count)`t$($ys | Measure-Object -Minimum | Select-Object -ExpandProperty Minimum)`t$($ys | Measure-Object -Maximum | Select-Object -ExpandProperty Maximum)")
}
$summary.Add('')
$summary.Add('FUTURE_LEAKAGE_EXAMPLES')
$future = @($rows | Where-Object Class -eq 'FUTURE INFORMATION / EXPLICIT LEAKAGE' | Sort-Object Year | Select-Object -First 20)
if ($future.Count -eq 0) { $summary.Add('NONE') } else { foreach ($r in $future) { $summary.Add("$($r.Country)`t$($r.Technology)`t$($r.Parameter)`t$($r.Year)`t$($r.Note)") } }
$summary.Add('')
$summary.Add('PRELIMINARY_STATUS')
$futureN = @($rows | Where-Object Class -eq 'FUTURE INFORMATION / EXPLICIT LEAKAGE').Count
$retroN = @($rows | Where-Object Class -eq 'RETROSPECTIVE / HISTORICAL DEPENDENCY').Count
$reviewN = @($rows | Where-Object Class -eq 'PLANNING_OR_LEGAL_REQUIRES_DATE_CHECK').Count + @($rows | Where-Object Class -eq 'UNKNOWN / REQUIRES REVIEW').Count
$summary.Add("FUTURE_LEAKAGE_RECORDS=$futureN")
$summary.Add("RETROSPECTIVE_RECORDS=$retroN")
$summary.Add("REVIEW_REQUIRED_RECORDS=$reviewN")
$summary.Add('STATUS=ANALYTICAL PRELIMINARY — NOT A FINAL MT4-5 GATE DECISION')
$summary | Set-Content -LiteralPath $SummaryPath -Encoding UTF8

$exceptions = $rows | Where-Object { $_.Class -ne 'CLEAN / NOT FLAGGED' } | Group-Object Parameter,Class | Sort-Object Name | ForEach-Object {
    $ys = @($_.Group.Year)
    [pscustomobject]@{Parameter=$_.Group[0].Parameter;Class=$_.Group[0].Class;N=$_.Count;MinYear=($ys|Measure-Object -Minimum).Minimum;MaxYear=($ys|Measure-Object -Maximum).Maximum}
}
$exceptions | Format-Table -AutoSize | Out-File -LiteralPath $ExceptionsPath -Encoding UTF8

Write-Host "AUDIT=$AuditPath"
Write-Host "SUMMARY=$SummaryPath"
Write-Host "EXCEPTIONS=$ExceptionsPath"
Write-Host "TOTAL_RECORDS=$($rows.Count)"
Write-Host "FUTURE_LEAKAGE_RECORDS=$futureN"
Write-Host "RETROSPECTIVE_RECORDS=$retroN"
Write-Host "REVIEW_REQUIRED_RECORDS=$reviewN"
