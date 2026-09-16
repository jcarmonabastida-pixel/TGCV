# TGCV MT4-5 — Candidate P_tau Rule Auditor 001
# Analytical diagnostic only; not a gate decision.
$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip="$env:USERPROFILE\Downloads\TGCV_MT4_energy_public-dataset_v2.zip"
$out="$env:USERPROFILE\Downloads\TGCV_MT4_5_PTAU_CANDIDATE_RULE_AUDIT_001.txt"
$required='Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate','Resource'
$h=@{}
$z=[IO.Compression.ZipFile]::OpenRead($zip)
try{foreach($e in $z.Entries){if($e.FullName -notmatch '/Technologies/.*\.csv$'){continue};$r=[IO.StreamReader]::new($e.Open());try{$null=$r.ReadLine();while(($l=$r.ReadLine())-ne$null){$x=$l -split ',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)',10;if($x.Count-lt 10){continue};$p=$x[2].Trim();if($required-notcontains$p){continue};$k="$($x[0].Trim())|$($x[1].Trim())|$($x[3].Trim())";if(!$h[$k]){$h[$k]=@{}};$h[$k][$p]=$x[5].Trim().Trim('"')}}finally{$r.Dispose()}}}finally{$z.Dispose()}
$n=$h.Count;$complete=0;$badLF=0;$badNum=0
foreach($c in $h.Values){$ok=$true;foreach($p in $required){if(!$c.ContainsKey($p)-or[string]::IsNullOrWhiteSpace($c[$p])){$ok=$false}};if($ok){$complete++};[double]$a=0;[double]$b=0;if([double]::TryParse($c['LF_min'],[ref]$a)-and[double]::TryParse($c['LF_max'],[ref]$b)-and$a-gt$b){$badLF++};foreach($p in 'Fuel_efficiency','LF_min','LF_max','Peak_contr','Ramp_rate'){[double]$v=0;if($c.ContainsKey($p)-and![double]::TryParse($c[$p],[ref]$v)){$badNum++}}}
$pct=[math]::Round(100*$complete/$n,2)
@"
TGCV MT4-5 — CANDIDATE P_tau RULE AUDIT 001
ZIP=$zip
CORE6_CELLS=$n
CORE6_COMPLETE=$complete
CORE6_COVERAGE_PCT=$pct
LF_MIN_GT_LF_MAX=$badLF
NUMERIC_PARSE_ANOMALIES=$badNum

RULE CLASSIFICATION
Resource compatibility = DIRECT
LF_min <= LF_max = DERIVED
Numeric parseability = DERIVED
Fuel_efficiency positive = NOT YET ADOPTED (threshold/hypothesis)
Ramp_rate non-negative = NOT YET ADOPTED (threshold/hypothesis)
Peak_contr non-negative = NOT YET ADOPTED (threshold/hypothesis)
Full socio-political/legal accessibility = UNSUPPORTED

P_TAU_TECHNICAL=PARTIALLY_FORMALIZED
P_TAU_FULL=UNDETERMINED
STATUS=ANALYTICAL DIAGNOSTIC — NOT A FINAL MT4-5 GATE DECISION
"@|Set-Content $out -Encoding UTF8
Get-Content $out
