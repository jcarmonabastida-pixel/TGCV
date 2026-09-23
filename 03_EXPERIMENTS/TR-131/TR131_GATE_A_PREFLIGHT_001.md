# TR-131 — Gate A Preflight Record 001

**Status:** PREFLIGHT BLOCKED — EXTERNAL FIXTURE NOT YET FROZEN  
**Date:** 2026-09-23  
**Candidate:** Healthcare treatment process / CPN process execution  
**Gate:** A — Cross-domain operationalisation

## 1. Purpose

This preflight verifies the public source metadata before any scientific execution or operational mapping is frozen.

## 2. Source verification

The 4TU.ResearchData record for **Mozafari Mehr, Azadeh (2023), Healthcare treatment process (logs and CPN model)** was independently checked through the publisher/repository record.

Verified:

- Version: **1**
- Versioned DOI: **10.4121/8683fc1a-aca1-447b-aba4-8d7806a9977f.v1**
- Publisher: **4TU.ResearchData**
- Original publication date: **2023-03-28**
- Licence: **CC0**
- Format: **RAR**
- Dataset description: simulated healthcare treatment process using a Colored Petri Net (CPN) model
- Event logs include activities such as patient admission, doctor visits and test orders
- Data logs record data-access events
- Published experiment archives: **9**
- Total uncompressed size reported by repository: **25,833,041 bytes**

Repository-reported MD5 values:

| File | Size | MD5 |
|---|---:|---|
| Experiment0.rar | 2,875,209 | 7ca4a5583405a8e91db2be30fafa1330 |
| Experiment1.rar | 2,870,112 | a2c2dcbbb01abe7aba9a7c1991d971f4 |
| Experiment2.rar | 2,871,632 | 2b0e82a0c4278611d3d039650b1e3339 |
| Experiment3.rar | 2,882,379 | 05913dcf233c24d6e96b71eedc4e7c69 |
| Experiment4.rar | 2,868,909 | f37b369fd955706c549040a75acf2b90 |
| Experiment5.rar | 2,879,782 | 8f55579982e4185e7c37b44cb1c618ae |
| Experiment6.rar | 2,867,793 | 9ee1c8b85ec763fffa75f149c7e7cb2a |
| Experiment7.rar | 2,856,585 | 368594d2df1963fb112705f8f99c5d50 |
| Experiment8.rar | 2,860,640 | 862a6863d4483d25323aedd83e63c94c7 |

## 3. Current preflight result

**BLOCKED — FIXTURE NOT FROZEN**

The repository metadata is sufficiently identified, but the actual archive contents have not yet been incorporated into the experimental fixture.

Therefore the following remain **UNVERIFIED**:

- exact CPN model file;
- exact experiment/log files to use;
- internal file names and versions;
- model semantics;
- state representation;
- enabled-transition semantics;
- data-dependent guards;
- event-to-transition mapping;
- state-update rule;
- case/trajectory identity;
- executable/replay mechanism.

No Gate A scientific execution is authorized.

## 4. Required next action

Download the version-1 dataset from the repository and place the original archive(s) into the local experimental workspace without modification.

Then:

1. verify repository MD5 values;
2. enumerate archive contents;
3. identify the CPN model artifact;
4. identify the candidate experiment/log artifact;
5. hash every selected fixture file;
6. freeze the fixture manifest;
7. only then define the operational mapping.

The operational definitions must not be adapted after inspecting scientific results.

## 5. Scientific boundary

This preflight establishes only source/fixture readiness.

It does not establish:

- Gate A PASS;
- cross-domain validity;
- cross-domain usefulness;
- Transformational Intelligence;
- outcome linkage;
- value linkage;
- causal delta-Tacc to delta-Value;
- ontological consequences.

## 6. Decision

**Gate A remains OPEN but execution is BLOCKED pending fixture freezing.**

The candidate remains valid as a selected domain because the public source provides a formal CPN-based healthcare process and versioned reproducible provenance. Its suitability for the actual TGCV operationalisation remains to be tested from the artifact contents.
