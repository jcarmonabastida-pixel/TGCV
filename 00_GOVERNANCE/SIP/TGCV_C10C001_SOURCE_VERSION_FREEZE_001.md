# TGCV C10-C — C10C-001 Source Version Freeze 001

## Status

`FROZEN — SOURCE VERSION, ARCHIVE INTEGRITY, AND MEMBER INVENTORY VERIFIED`

## Exact source

Harvard Dataverse dataset:

- Persistent identifier: `doi:10.7910/DVN/QOGMVI`
- Dataset ID: `3348774`
- Released version: `v1`
- Dataset version ID: `192190`
- Internal version: `3`
- Minor version: `2`
- Publication date: `2019-01-29`
- Last update/release recorded: `2020-04-01T15:34:19Z`
- License: `CC0 1.0`

Dataset title: **Replication Data for: Exporting and Firm Performance: Evidence from a Randomized Experiment**.

## Exact admitted archive

The released version exposes one replication archive:

- filename: `JPAL_3813.zip`
- Dataverse file ID: `3348775`
- persistent file ID: `doi:10.7910/DVN/QOGMVI/R6SZN9`
- content type: `application/zip`
- size: `895831` bytes
- MD5 reported by Dataverse: `d34d30d45bbabcb5bd21eec31c89a613`
- description: contains data, do files, and a readme file.

## Controlled local acquisition integrity record

The archive was downloaded to:

`C:\Users\pedri\Downloads\TGCV_C10C001\JPAL_3813.zip`

Observed integrity:

- byte size: `895831` — **PASS**
- MD5: `D34D30D45BBABCB5BD21EEC31C89A613` — **PASS**, exact match to Dataverse metadata
- SHA-256: `B528F933BD72022AD16F320C55FEB20DB8B410AB2C5816137D0DAD7061A73AB5` — **FROZEN**

## Frozen ZIP member inventory

The ZIP index was inspected without extraction. It contains 14 non-directory members: 10 Stata data files, 3 Stata do-files, and 1 PDF README.

| Member | Size (bytes) | SHA-256 |
|---|---:|---|
| `JPAL_3813/data/analysis.dta` | 4587846 | `7C24424D63C3032F6D16394EF3F641FD8F5031715CCF423244EC755669346361` |
| `JPAL_3813/data/attrition.dta` | 37344 | `D56B8AE27D3DDE4FE7C5609F3E92B73688AAF91BD8AF477E93ED31AB60EB867F` |
| `JPAL_3813/data/cumu_hours.dta` | 50674 | `902C004ACA7D19C9C084B8BB4F0CB73F9AF44FFC3534F0ACBB1B50B7FD911D34` |
| `JPAL_3813/data/distance_all.dta` | 26166 | `017656DAB18259993BF7B1BF8BB9A970E1FAC5F7FC201B312093289DEBCF7965` |
| `JPAL_3813/data/Info_by_metrics.dta` | 35074 | `FAE86F06AF5E56FC3CAE2DE4F37FA390C3FF7AD8420DC3C611677B2E8DF98680` |
| `JPAL_3813/data/Rug_Surveys.dta` | 484185 | `E2911EA2D516E4A5C3041BC0340868BA7CEBBC5F9546713E15C35C98DFF82E95` |
| `JPAL_3813/data/takeup.dta` | 67782 | `4ABB3C583E2C8196E8ABCB97CBA2E5A4D31A3BECC8C61BBE6AA71C92F5B4D832` |
| `JPAL_3813/data/takeup_lab.dta` | 1373 | `6613C5BE840F7836967266279C7AF76794851E37E72E8E0B74846CC48A90C638` |
| `JPAL_3813/data/technique.dta` | 35423 | `A72803F9876C470FEE316FC93DEB7240BF9DAA63A4998B56AF04E7BC740483D3` |
| `JPAL_3813/data/Training_Survey.dta` | 15521 | `CEF2A52F4121C41EE601F74A6BA90426E56D1534CA562D5C754B47FCBC4060A8` |
| `JPAL_3813/dofile/Common_Variables.do` | 3923 | `0D1B3A3F84EDBD0BC9C05F2DA168602EEB89A1A2505F59D0DFA7D11C268204F3` |
| `JPAL_3813/dofile/Replication_File.do` | 88798 | `5560FC650BE1AB033104FB33B98D64869FC91562FAC9E390AC5498CE4F94C342` |
| `JPAL_3813/dofile/Replication_File_Appendix.do` | 40432 | `0C2A4F7E1412605D962E08092FCBBD193187E7A17CB6DE19DD0D25214B690CB4` |
| `JPAL_3813/README.pdf` | 110554 | `6C8A1C25884BB5F1EC8D4F62FD43AF93A8AA1936C940A99B651485E6616D0E67` |

Directory entries were also present for `JPAL_3813/data/` and `JPAL_3813/dofile/`; these contain no data bytes and are not included in the member hash table.

## Controlled inspection boundary

Archive and member integrity are now frozen. The next operation is controlled extraction of the frozen archive to a separate local inspection directory, followed by non-executing inspection of the README and replication scripts. No `.do` file is to be executed at this stage.

No causal estimation, replication of published estimates, outcome-informed variable selection, transformation construction, or claim upgrade is authorized by this record.
