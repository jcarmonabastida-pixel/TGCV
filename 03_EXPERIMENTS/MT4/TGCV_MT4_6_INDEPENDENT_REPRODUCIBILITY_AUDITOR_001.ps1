$ErrorActionPreference = 'Stop'
$Zip = 'C:\Users\pedri\Downloads\TGCV_MT4_energy_public-dataset_v2.zip'
$Expected = '691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30'
$Out = 'C:\Users\pedri\Downloads\TGCV_MT4_6_INDEPENDENT_REPRODUCIBILITY_SUMMARY_001.txt'

$sha = (Get-FileHash -Algorithm SHA256 $Zip).Hash.ToUpper()
if ($sha -ne $Expected) { throw "SOURCE_HASH_MISMATCH: $sha" }

Add-Type -AssemblyName System.IO.Compression.FileSystem
$z = [IO.Compression.ZipFile]::OpenRead($Zip)
try {
    $cells = @{}
    $params = @('Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource')
    $missing = @{}
    foreach ($p in $params) { $missing[$p] = 0 }

    foreach ($e in $z.Entries) {
        if ($e.FullName -notmatch '/Technologies/[^/]+\.csv$') { continue }
        $sr = New-Object IO.StreamReader($e.Open())
        try {
            $null = $sr.ReadLine()
            while (($line = $sr.ReadLine()) -ne $null) {
                $x = $line -split ',(?=(?:[^"]*"[^"]*")*[^"]*$)', 10
                if ($x.Count -lt 10) { continue }
                $country = $x[0]
                $tech = $x[1]
                $param = $x[2]
                $year = $x[3]
                if ($year -notmatch '^\d{4}$') { continue }
                if ($param -notin $params) { continue }
                $key = "$country|$tech|$year"
                if (-not $cells.ContainsKey($key)) { $cells[$key] = @{} }
                if (-not $cells[$key].ContainsKey($param)) { $cells[$key][$param] = $x[5] }
            }
        }
        finally { $sr.Dispose() }
    }

    $total = $cells.Count
    foreach ($key in $cells.Keys) {
        foreach ($p in $params) {
            if (-not $cells[$key].ContainsKey($p) -or [string]::IsNullOrWhiteSpace($cells[$key][$p])) {
                $missing[$p]++
            }
        }
    }

    $complete = @($cells.Keys | Where-Object {
        $ok = $true
        foreach ($p in $params) {
            if (-not $cells[$_].ContainsKey($p) -or [string]::IsNullOrWhiteSpace($cells[$_][$p])) {
                $ok = $false
                break
            }
        }
        $ok
    })

    $groups = @{}
    foreach ($key in $complete) {
        $a = $key.Split('|')
        $group = "$($a[0])|$($a[2])"
        if (-not $groups.ContainsKey($group)) { $groups[$group] = @() }
        $groups[$group] += $key
    }

    $groups2 = @($groups.Keys | Where-Object { $groups[$_].Count -ge 2 })
    $distinct = 0
    $dups = 0
    foreach ($group in $groups2) {
        $signatures = @{}
        foreach ($key in $groups[$group]) {
            $values = foreach ($p in $params) { $cells[$key][$p] }
            $signature = ($values -join '|')
            $signatures[$signature] = 1
        }
        if ($signatures.Count -ge 2) { $distinct++ }
        if ($signatures.Count -lt $groups[$group].Count) { $dups++ }
    }

    $coverage = [math]::Round(100 * $complete.Count / $total, 2)

    $lines = @()
    $lines += 'AUDIT=TGCV_MT4_6_INDEPENDENT_REPRODUCIBILITY_AUDITOR_001'
    $lines += "SOURCE_SHA256=$sha"
    $lines += "TOTAL_COUNTRY_TECHNOLOGY_YEAR_CELLS=$total"
    $lines += "COMPLETE_CORE6_CELLS=$($complete.Count)"
    $lines += "INCOMPLETE_CORE6_CELLS=$($total - $complete.Count)"
    $lines += "CORE6_COVERAGE_PCT=$coverage"
    foreach ($p in $params) { $lines += "MISSING_$p=$($missing[$p])" }
    $lines += "COUNTRY_YEAR_GROUPS_2PLUS_TECH=$($groups2.Count)"
    $lines += "GROUPS_2PLUS_DISTINCT_SIGNATURES=$distinct"
    $lines += "GROUPS_WITH_DUPLICATE_SIGNATURES=$dups"
    $lines += 'STATUS=INDEPENDENT REPRODUCIBILITY RESULT - NOT YET RECONCILED'

    Set-Content -Path $Out -Value $lines -Encoding UTF8
    $lines
    "OUTPUT=$Out"
}
finally {
    $z.Dispose()
}
