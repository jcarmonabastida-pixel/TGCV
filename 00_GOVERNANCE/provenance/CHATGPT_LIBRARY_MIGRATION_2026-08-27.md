# TGCV — ChatGPT Library migration register

**Date:** 2026-08-27

This register records which Library artefacts have been recovered and migrated into the canonical GitHub continuity layer, and which remain external/working material.

## Migrated canonical/research records

- `TGCV_RMA_v0.1.md` → `00_GOVERNANCE/rma/TGCV_RMA_v0.1.md`
- `TGCV_RMA_traceability_v0.1.csv` → `00_GOVERNANCE/rma/TGCV_RMA_traceability_v0.1.csv`
- `TGCV-EXT-TCP-001_v0.1.md` → external asset archive
- `TGCV-EXT-TCP-001_v0.2.md` → external asset archive
- `TGCV-EXT-VP-001_v0.1.md` → external asset archive
- `TGCV — Paquete maestro de transferencia y continuidad tras TR-140.md` → governance/provenance continuity archive
- `TGCV_EMPIRICAL_STATUS_2026-08-26.md` → EXT-1.1 empirical status
- `Experimental_Protocol_v1_1.json` → EXT-1.1 frozen protocol
- `TEST_SEAL.json` → EXT-1.1 test seal
- `CONFIRMATORY_RESULTS.json` → EXT-1.1 results
- `STRUCTURAL_INTERVENTION_RESULTS.json` → EXT-1.1 intervention results
- `FINAL_REPORT.md` → EXT-1.0 final report
- `DATASET_MANIFEST_PRECHECK.txt` → EXT-1.0 manifest
- MVE reproducibility archives are retained in the ChatGPT Library and should be migrated as raw archives only when the repository's binary-file policy/path is explicitly established.

## Not migrated as canonical TGCV science

- generic literature PDFs: retained in the Library/literature corpus, not duplicated into the Git repository by default;
- personal CV/photo/application identity files: not part of the scientific core and should not be copied into the public TGCV repository;
- older IE packs: retained as application history unless a specific version is designated canonical;
- unsupported/ambiguous UAM or Orange artefacts: not invented or reconstructed merely from filenames.

## Migration principle

GitHub receives the canonical scientific and programme records, not an indiscriminate dump of the ChatGPT Library. Every migrated artefact must have a clear repository role, provenance and epistemic status.
