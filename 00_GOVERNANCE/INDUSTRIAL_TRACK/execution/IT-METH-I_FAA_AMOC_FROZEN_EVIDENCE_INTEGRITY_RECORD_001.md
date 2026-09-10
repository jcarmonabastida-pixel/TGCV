# IT-METH-I FAA AMOC — Frozen Evidence Integrity Record 001

## Status

`CLOSED — FROZEN EVIDENCE BYTE INTEGRITY ESTABLISHED`

## Purpose

Record the exact local byte-level integrity anchors for the frozen documentary evidence set to be used by the controlled IT-METH-I FAA AMOC execution process.

This record establishes documentary input integrity only. It does **not** authorize Reconstruction 002, establish Executor-2 independence, modify Package 002, or supersede/complement the operative IT-G5 execution-block decision.

## Case

- Case ID: `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`
- Package ID: `IT-METH-I-AMOC-BLIND-EXEC-001`
- Frozen evidence container: `IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_001.zip`
- Local container path: `C:\Users\pedri\Downloads\IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_001.zip`
- Retrieval/assembly date recorded by operator: `2026-09-10`

## Frozen evidence boundary

The byte-level frozen documentary set consists of exactly three PDF documents:

1. FAA AMOC approval letter, reference `7K0-18-00734`, concerning AD `91-12-10`.
2. AD `US-91-12-10`.
3. FAA AC 39-10, `Alternative Methods of Compliance`, issued `2016-09-14`.

The case-specific 2018 approval-process context admitted at IT-G1–IT-G4 remains a governance/context element and is not represented here as a fourth independent PDF byte object.

## File-level integrity anchors

| Frozen role | ZIP member | Size (bytes) | SHA-256 |
|---|---|---:|---|
| FAA AMOC approval letter 7K0-18-00734 | `EASA_AD_US-91-12-10_1.pdf` | 1,308,719 | `136C9458701AD63402C966694CB30A773D53E2A4C3FF7FA5CDE101B90379FFFE` |
| AD US-91-12-10 | `EASA_AD_US-91-12-10_2.pdf` | 24,221 | `1C7D810B9CC905EBE0FF456A0515E3B86EB4F4FDD1ABDBD3BC61A3D0A65F47C0` |
| FAA AC 39-10 | `AC_39-10.pdf` | 397,778 | `2A0000DF9FBD338DC6D403BD63C36659FF5542FE4B924FDE3B28C02D12B3A6C1` |

## Frozen container integrity anchor

- Container: `IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_001.zip`
- Size: `1,366,829` bytes
- SHA-256: `829A301215FB13EC619EE478DA45FDE4DABF0A3206B7D14F8ECADBF1660EDCBA`

## Source identity verification

The operator visually verified the two EASA members before this record was established:

- `EASA_AD_US-91-12-10_1.pdf` = FAA AMOC approval letter `7K0-18-00734`.
- `EASA_AD_US-91-12-10_2.pdf` = AD `US-91-12-10`.

The EASA public record identifies US-91-12-10 and its two attachments, including AMOC reference `7K0-18-00734`. The FAA identifies AC 39-10 as active and issued `2016-09-14`.

## Integrity interpretation

The three individual SHA-256 values identify the exact local PDF byte sequences used to construct the frozen container. The container SHA-256 identifies the exact ZIP byte sequence held locally at the recorded path.

The ZIP is therefore suitable as a reproducible local frozen-input container, subject to the separate execution-control and authorization gates.

## Governance boundary

This record does not:

- authorize transfer into Windows Sandbox;
- authorize Reconstruction 002;
- release or expose Reconstruction 001;
- establish Executor-2 distinctness by itself;
- establish independence by itself;
- alter the frozen IT-G5 review;
- modify the canonical Package 002;
- establish any utility, comparative, causal, safety, cost, or value result.

The operative IT-G5 status remains `EXECUTION BLOCKED` until its stated pre-execution control conditions are satisfied and a new explicit authorization decision is recorded through the applicable governance process.

## External source identity references

- EASA Safety Publications Tool: `https://ad.easa.europa.eu/ad/US-91-12-10`
- FAA AC 39-10 document page: `https://www.faa.gov/airports/resources/advisory_circulars/index.cfm/go/document.information/documentNumber/39-10`
- FAA AC 39-10 PDF: `https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_39-10.pdf`

## Record disposition

`FROZEN_EVIDENCE_BYTE_INTEGRITY = ESTABLISHED`

`R002_EXECUTION = NOT_AUTHORIZED`

`R002_EXECUTION = NOT_EXECUTED`

`IT-G5_AUTHORIZATION = BLOCKED / NOT_GRANTED`
