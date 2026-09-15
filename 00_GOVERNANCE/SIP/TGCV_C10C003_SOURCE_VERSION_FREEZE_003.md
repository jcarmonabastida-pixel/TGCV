# TGCV C10-C — C10C-003 India Source Version Freeze 003

## Status

`FROZEN — BYTE-LEVEL VERIFIED LOCAL ACQUISITION`

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
- Local acquisition directory: `C:\Users\pedri\Downloads\C10C003_India_v2`

## Byte-level verified inventory

| File | Dataverse file ID | Size (bytes) | Dataverse MD5 | Local SHA-256 |
|---|---:|---:|---|---|
| `ReadMe.txt` | 3018284 | 2,705 | `b43a4c62e47038cbf7fb23e2b54f974f` | `A7FDA0052B8CA063FA1F2BB9CA31737B9ED852E3CD7FBB40BF8A019045E2396D` |
| `ReplicationCensusIndiaData.dta` | 3018285 | 30,692,844 | `1c177ecfb8a2df6a31e5e806f3a08fec` | `AFC0DC13EA83EF0FAE63A039C58D63CD5121D843AC5C514B5F4DFB5CB8065D52` |
| `ReplicationCensusUPData.dta` | 3018286 | 10,443,132 | `d84319bab6d1d56d9448061524f4c41c` | `77FE8D42320A098512B44703ED3FB1C7295A41997CB19F49D75708CDF7C8529B` |
| `ReplicationDataFinal.tab` | 3018290 | 1,220,136 | `b8745018a9fe1882cf798949db1ca07f` | `ADE2BBEF7FF951A9D78B53219DABA540F783415F822C09BEFA6C6B310763A280` |
| `ReplicationDataRaw.tab` | 3018291 | 596,003 | `cec810434894f46f7e880c0760496fc5` | `0DD41E8A9C23899080D16CB4EE94EE393C213A8ED67B722C61E98E0323A8A5BD` |
| `ReplicationExternalValidity.do` | 3018292 | 22,952 | `dbc9d9b4fa0a6d6a515c5095106ebfdb` | `6A5EE38E17EBB370A229D1AB453F5408AB52BD5E8B9EE809CBA0EFEE6C23A67D` |
| `ReplicationImpactEvaluationAnalysis.do` | 3018293 | 86,571 | `0779191711d0163dbc83a5c7d0b056a2` | `73B06E3C41D991D09F632AFED6143A6E9F7CCB86DAC195E12996029C24B63F99` |
| `ReplicationImpactEvaluationCoding.do` | 3018294 | 11,786 | `10584a3e6f825f3af4a507c77f0dccda` | `31A8F9C198916560879534D32419333FEF110ACC4254E8AA86C97D1CF2904928` |
| `ReplicationPlacebo.do` | 3018295 | 12,291 | `0a2dc1c638b04a0c34f695df6985c84d` | `7A5042DAA02261A1CEDBB0856AA0565FDADEBE143F6F40DF5F6219B3D8081DE7` |

Total payload size: `45,088,420` bytes.

## Verification statement

The nine locally acquired files correspond to the nine files in the frozen Dataverse version `2` / dataset version ID `126497`. The local SHA-256 values above were calculated from the acquired files supplied from the Dataverse API. Dataverse-provided MD5 values and file sizes are retained as the source-side integrity metadata.

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

## Execution boundary remains unchanged

This freeze authorizes static inspection only. **No `.do` file may be executed.** No causal estimation, outcome-informed variable selection, replication of published estimates as scientific evidence, value inference, or TGCV Core modification is authorized.

## Next controlled operation

Static inspection of `ReadMe.txt` and all `.do` files, followed by data-level inspection of variable metadata, with the sole purpose of determining whether a closed, independent `U_tau`, a non-circular `P_tau(S,C,L)`, and reconstructable `T_acc,0`, `T_acc,1`, and `Delta T_acc` can be established.
