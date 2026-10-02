# TGCV VIATRA V002 Fixture Byte Hash Manifest

**Status:** VERIFIED — exact UTF-8 bytes independently recalculated and hashes confirmed  
**Date:** 2026-10-03  
**Fixture:** `TGCV_VIATRA_MINIMAL_FIXTURE_v002`  
**Scope:** byte integrity / provenance only

## 1. Purpose

Record the independently recalculated SHA-256 digests of the five canonical VIATRA V002 fixture artefacts.

The digests below are SHA-256 values calculated over the exact UTF-8 byte sequences. Git blob SHAs are not used as substitutes.

## 2. Canonical hash inventory

| Artifact | SHA-256 | Exact UTF-8 bytes |
|---|---|---:|
| CPS | `8d432da0d3fd49ba88f809611f222614ef588809691e66bcc954a4cd509f66bb` | 316 |
| Deployment INITIAL | `fea5bc84929e99145ebe07f4eabeb1d04eaceb805b3e35d7975aff793bd9af8e` | 187 |
| Deployment EXPECTED | `92addffad49e828a8c3c7f0ca7b00c870f00e9c419415c3b997e06cc36b0e966` | 240 |
| Traceability INITIAL | `1ce4c0c69f324e43d87b41dee2561a55668d06c815294919011a2d5c3d1d88c1` | 500 |
| Traceability EXPECTED | `29ebb291e72ff061618aa809af2e16527464f2475e21bfe558de00bd36de33e3` | 720 |

## 3. Verification statement

The five SHA-256 values were independently recalculated over the exact UTF-8 bytes and coincide with the previously recorded values.

Therefore:

- byte content: **VERIFIED**;
- UTF-8 byte sizes: **VERIFIED**;
- SHA-256 digests: **VERIFIED**;
- no hash substitution by Git blob SHA: **CONFIRMED**.

## 4. Boundary

This manifest records byte-level provenance only.

It does not:

- modify the fixture bytes;
- establish runtime equivalence;
- authorize implementation;
- authorize scientific execution;
- imply any new scientific result.

Any subsequent change to a fixture artefact requires a new immutable manifest revision.
