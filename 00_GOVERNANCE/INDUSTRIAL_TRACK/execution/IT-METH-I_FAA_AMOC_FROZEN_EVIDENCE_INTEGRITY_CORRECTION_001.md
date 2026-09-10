# IT-METH-I FAA AMOC — Frozen Evidence Integrity Correction 001

## Status

`CLOSED — CORRECTION VERIFIED / NO EVIDENCE BYTES CHANGED`

## Purpose

Record and correct a transcription error in the file-level SHA-256 anchor recorded by `IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_INTEGRITY_RECORD_001.md` for the second frozen PDF.

This correction does not alter the frozen ZIP, any PDF byte sequence, the evidence boundary, the controlled package, authorization, Executor-2 independence, or Reconstruction 002 status.

## Case

- Case ID: `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`
- Package ID: `IT-METH-I-AMOC-BLIND-EXEC-001`
- Frozen container: `IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_001.zip`

## Affected evidence member

`EASA_AD_US-91-12-10_2.pdf`

Recorded in Integrity Record 001:

`1C7D810B9CC905EB0FF456A0515E3B86EB4F4FDD1ABDBD3BC61A3D0A65F47C0`

Independently verified SHA-256 from the exact PDF extracted from the frozen ZIP:

`1C7D810B9CC905EBE0FF456A0515E3B86EB4F4FDD1ABDBD3BC61A3D0A65F47C0`

The discrepancy is a metadata/transcription error in the recorded hash. The independent host extraction and the Sandbox extraction both derive the corrected value from the same frozen ZIP, whose container SHA-256 remains:

`829A301215FB13EC619EE478DA45FDE4DABF0A3206B7D14F8ECADBF1660EDCBA`

## Verification

The corrected PDF hash was independently recomputed on the host from the frozen ZIP on 2026-09-10. The Sandbox intake subsequently recomputed the same PDF hash from the same frozen ZIP.

The other two PDF SHA-256 values and all three recorded lengths match their frozen anchors.

## Operational anchor

For subsequent controlled intake and execution records, the canonical file-level SHA-256 for `EASA_AD_US-91-12-10_2.pdf` is:

`1C7D810B9CC905EBE0FF456A0515E3B86EB4F4FDD1ABDBD3BC61A3D0A65F47C0`

The original Integrity Record 001 remains immutable historical evidence of the value that was recorded at that time. This correction record is the controlled clarification to be used for subsequent verification.

## Governance boundary

- `R002_EXECUTION = NOT_EXECUTED`
- `EXECUTOR_2_INDEPENDENCE = NOT_ESTABLISHED_BY_THIS_CORRECTION`
- `IT-G5-002 AUTHORIZATION = UNCHANGED`
- No R001 material was released.
- No comparison was performed.
- No evidence byte was changed.
- No reconstruction result was produced.

## Disposition

`PDF_2_HASH_CORRECTION = VERIFIED`

`FROZEN_ZIP_HASH = UNCHANGED`

`FROZEN_EVIDENCE_BYTES = UNCHANGED`

`R002_EXECUTION = NOT_EXECUTED`
