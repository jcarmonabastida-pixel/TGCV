# TGCV MT-4 — Source Freeze Manifest 001

**Status:** FROZEN — SOURCE IDENTITY VERIFIED  
**Date:** 2026-09-16  
**Protocol:** `TGCV_MT4_DOMAIN_TRANSFER_TEST_PROTOCOL_001.md`  
**Candidate domain:** Historical national electricity-system transitions / energy-system technology change  

## 1. Frozen source identity

- **Source:** Jaxa-Rozen, Wen & Trutnevyte, *Historic data of the national electricity system transitions in Europe in 1990–2019 for retrospective evaluation of models*
- **Repository:** Zenodo
- **Record:** 6696776
- **Version:** v2
- **DOI:** 10.5281/zenodo.6696776
- **Frozen file:** `public-dataset.zip`
- **Declared Zenodo MD5:** `920548154EB918A202AB6ACB6BF37746`
- **Observed MD5:** `920548154EB918A202AB6ACB6BF37746`
- **Observed SHA-256:** `691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`
- **Local acquisition path:** `C:\Users\pedri\Downloads\TGCV_MT4_energy_public-dataset_v2.zip`
- **Acquisition status:** completed locally
- **Integrity check:** PASS — observed MD5 exactly matches the MD5 declared by the source record

## 2. Freeze decision

MT4-2 **FROZEN EVIDENCE: PASS**.

The exact source package has been acquired locally and its observed MD5 matches the source-declared MD5. The observed SHA-256 is recorded as the local cryptographic identity for subsequent execution and audit.

No variable inspection, semantic mapping, construction of `Uτ`, `Pτ`, `T_acc`, or `ΔT_acc` is represented by this manifest. Those operations remain downstream MT-4 activities and must not retroactively alter the frozen source identity.

## 3. Boundary and integrity rule

The source package is now treated as immutable input for MT-4. Any later transformation, extraction, filtering, variable selection, or derived dataset must retain a traceable relationship to this frozen package and must not replace the frozen source with a modified or outcome-conditioned version.

## 4. Current MT-4 gate state

- MT4-0 protocol freeze: PASS
- MT4-1 domain novelty: provisional PASS
- MT4-2 frozen evidence: **PASS — CLOSED**
- MT4-3 independent semantic mapping: NOT STARTED
- MT4-4 semantic non-substitution: NOT STARTED
- MT4-5 temporal non-leakage: NOT STARTED
- MT4-6 independent reproducibility: NOT STARTED
- MT4-7 downstream separation: NOT STARTED
- MT4-8 value isolation: NOT STARTED

**Scientific execution status:** NOT YET STARTED.  
**Next authorized operation:** inspect the frozen package only to establish its documented structure/provenance and identify candidate pre-decisional observables; do not assign TGCV roles or construct `T_acc`/`ΔT_acc` from observed outcomes or adoption measures.
