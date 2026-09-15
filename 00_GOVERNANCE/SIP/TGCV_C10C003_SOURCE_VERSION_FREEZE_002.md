# TGCV C10-C — C10C-003 India Source Version Freeze 002

## Status

`FROZEN — DATAVERSE DATASET VERSION IDENTIFIED; BYTE-LEVEL SHA-256 PENDING LOCAL ACQUISITION`

## Canonical source

- Persistent DOI: `10.7910/DVN/QXKPHH`
- Harvard Dataverse dataset ID: `3015346`
- Dataset identifier: `DVN/QXKPHH`
- Published dataset date: `2017-05-01`
- Latest released version: `2`
- Internal version: `2`
- Minor version: `1`
- Dataset version ID: `126497`
- Version state: `RELEASED`
- Release time: `2017-05-19T06:28:25Z`
- Last update time: `2017-05-19T06:28:25Z`
- Dataverse UNF: `UNF:6:VDTiBHmFm1sPgTzhwPO2uQ==`
- License: `CC0-1.0`

## Frozen file inventory

| File | Dataverse file ID | Size | MD5 |
|---|---:|---:|---|
| `ReadMe.txt` | 3018284 | 2,705 | `b43a4c62e47038cbf7fb23e2b54f974f` |
| `ReplicationCensusIndiaData.dta` | 3018285 | 30,692,844 | `1c177ecfb8a2df6a31e5e806f3a08fec` |
| `ReplicationCensusUPData.dta` | 3018286 | 10,443,132 | `d84319bab6d1d56d9448061524f4c41c` |
| `ReplicationDataFinal.tab` | 3018290 | 1,220,136 | `b8745018a9fe1882cf798949db1ca07f` |
| `ReplicationDataRaw.tab` | 3018291 | 596,003 | `cec810434894f46f7e880c0760496fc5` |
| `ReplicationExternalValidity.do` | 3018292 | 22,952 | `dbc9d9b4fa0a6d6a515c5095106ebfdb` |
| `ReplicationImpactEvaluationAnalysis.do` | 3018293 | 86,571 | `0779191711d0163dbc83a5c7d0b056a2` |
| `ReplicationImpactEvaluationCoding.do` | 3018294 | 11,786 | `10584a3e6f825f3af4a507c77f0dccda` |
| `ReplicationPlacebo.do` | 3018295 | 12,291 | `0a2dc1c638b04a0c34f695df6985c84d` |

Total frozen payload size: `45,088,420` bytes.

## Tabular-file provenance

`ReplicationDataFinal.tab`:
- original file format: `application/x-stata`
- original filename: `ReplicationDataFinal.dta`
- original file size: `1,779,669` bytes
- Dataverse UNF: `UNF:6:NjkfUcMLjwqwwaBG+L557w==`

`ReplicationDataRaw.tab`:
- original file format: `application/x-stata`
- original filename: `ReplicationDataRaw.dta`
- original file size: `1,158,964` bytes
- Dataverse UNF: `UNF:6:Kf+PzK9ElaL1Be6bVxl3+A==`

## Freeze interpretation

This is now an exact **Dataverse-version freeze**: version `2`, dataset version ID `126497`, released 2017-05-19, with the complete nine-file inventory and Dataverse-provided MD5 checksums.

A local SHA-256 is still required before declaring the byte-level archive freeze. Because Dataverse exposes the components as individual files in this released version, the canonical local acquisition should preserve those nine files and hash each one. No substitute re-packaged ZIP should be treated as the canonical source unless its contents are independently reconciled to this inventory.

## Execution boundary

Downloading and hashing the files is authorized. Reading text/code for inspection is authorized. **Executing any `.do` file is not authorized.** No causal estimation, outcome-informed variable selection, replication of published estimates as scientific evidence, value inference, or TGCV Core modification is authorized.

## Next inspection target

After local acquisition and SHA-256 verification, inspect `ReadMe.txt` and the `.do` files as static text only, then inspect the data dictionaries/variable metadata needed to determine whether a non-circular `U_tau` and `P_tau(S,C,L)` and reconstructable `T_acc,0`, `T_acc,1`, `Delta T_acc` can be established.
