$ErrorActionPreference = 'Stop'
$zip = "$env:USERPROFILE\Downloads\TGCV_MT4_energy_public-dataset_v2.zip"
$out = "$env:USERPROFILE\Downloads\TGCV_MT4_5_LF_INCONSISTENCY_DIAGNOSTIC_001.txt"
Add-Type -AssemblyName System.IO.Compression.FileSystem

$z = [IO.Compression.ZipFile]::OpenRead($zip)
try {
    $cells = @{}
    foreach ($e in $z.Entries) {
        if ($e.FullName -notmatch '/Technologies/.*\.csv$') { continue }
        $r = [IO.StreamReader]::new($e.Open())
        try {
            $null = $r.ReadLine()
            while (($l = $r.ReadLine()) -ne $null) {
                if ($l -notmatch ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)') { continue }
                $x = $l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', 10
                if ($x.Count -lt 10) { continue }
                $p = $x[2].Trim()
                if ($p -notin @('LF_min','LF_max')) { continue }
                $k = "$($x[0].Trim())|$($x[1].Trim())|$($x[3].Trim())"
                if (-not $cells.ContainsKey($k)) { $cells[$k] = @{} }
                $cells[$k][$p] = $x[5].Trim().Trim('"')
            }
        }
        finally { $r.Dispose() }
    }

    $badDefault = @()
    $badInvariant = @()
    $parseDefault = 0
    $parseInvariant = 0
    $both = 0

    foreach ($key in $cells.Keys) {
        $c = $cells[$key]
        if (-not $c.ContainsKey('LF_min') -or -not $c.ContainsKey('LF_max')) { continue }
        $both++

        [double]$ad = 0
        [double]$bd = 0
        $d1 = [double]::TryParse($c['LF_min'], [ref]$ad)
        $d2 = [double]::TryParse($c['LF_max'], [ref]$bd)
        if ($d1 -and $d2) {
            if ($ad -gt $bd) {
                $badDefault += [pscustomobject]@{Key=$key; Min=$c['LF_min']; Max=$c['LF_max']; Gap=$ad-$bd}
            }
        }
        else { $parseDefault++ }

        [double]$ai = 0
        [double]$bi = 0
        $i1 = [double]::TryParse($c['LF_min'], [Globalization.NumberStyles]::Float, [Globalization.CultureInfo]::InvariantCulture, [ref]$ai)
        $i2 = [double]::TryParse($c['LF_max'], [Globalization.NumberStyles]::Float, [Globalization.CultureInfo]::InvariantCulture, [ref]$bi)
        if ($i1 -and $i2) {
            if ($ai -gt $bi) {
                $badInvariant += [pscustomobject]@{Key=$key; Min=$c['LF_min']; Max=$c['LF_max']; Gap=$ai-$bi}
            }
        }
        else { $parseInvariant++ }
    }

    $sha = (Get-FileHash $zip -Algorithm SHA256).Hash
    $md5 = (Get-FileHash $zip -Algorithm MD5).Hash
    $o = @()
    $o += 'TGCV MT4-5 — LF INCONSISTENCY DIAGNOSTIC 003'
    $o += "ZIP=$zip"
    $o += "MD5=$md5"
    $o += "SHA256=$sha"
    $o += "LF_CELLS_WITH_BOTH=$both"
    $o += "DEFAULT_CULTURE_INCONSISTENCIES=$($badDefault.Count)"
    $o += "INVARIANT_CULTURE_INCONSISTENCIES=$($badInvariant.Count)"
    $o += "DEFAULT_PARSE_FAILURE_CELLS=$parseDefault"
    $o += "INVARIANT_PARSE_FAILURE_CELLS=$parseInvariant"
    $o += ''
    $o += 'DEFAULT_CULTURE_TOP_25'
    foreach ($x in ($badDefault | Select-Object -First 25)) {
        $o += "$($x.Key)|MIN=$($x.Min)|MAX=$($x.Max)|GAP=$($x.Gap)"
    }
    $o += ''
    $o += 'INVARIANT_CULTURE_TOP_25'
    foreach ($x in ($badInvariant | Select-Object -First 25)) {
        $o += "$($x.Key)|MIN=$($x.Min)|MAX=$($x.Max)|GAP=$($x.Gap)"
    }
    $o += ''
    $o += 'BOUNDARY=Compare both parsing modes because prior auditor reported 802 while invariant diagnostic reported 0. No repair/exclusion/P_tau decision.'
    $o += 'STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION'
    $o | Set-Content $out -Encoding UTF8
    Write-Output "OUTPUT=$out"
    Write-Output "LF_CELLS_WITH_BOTH=$both"
    Write-Output "DEFAULT_CULTURE_INCONSISTENCIES=$($badDefault.Count)"
    Write-Output "INVARIANT_CULTURE_INCONSISTENCIES=$($badInvariant.Count)"
    Write-Output "SHA256=$sha"
    Write-Output "MD5=$md5"
}
finally { $z.Dispose() }