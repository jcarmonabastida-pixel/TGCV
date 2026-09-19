# TGCV TR-131 — Audit Worksheet v0.1

**Status:** CANDIDATE — NOT FROZEN  
**Scientific execution:** NOT AUTHORIZED

## A. Package identity
- Protocol: `TGCV_TR-131_PROTOCOL_v0.1`
- Package: `EXECUTOR_2_PACKAGE_MANIFEST_v02.json`
- Bundle: `TR-131_SCIENTIFIC_OPERATIONAL_BUNDLE_SPEC_v0.1.md`
- Runner: `tr131_scientific_runner_v02.py`
- Environment: `ENVIRONMENT_SPEC_v01.json`

## B. Integrity checks
Record and independently verify SHA-256 for every artifact listed in the Package Manifest and Integrity Manifest.
- [ ] Protocol hash matches
- [ ] Runner hash matches
- [ ] Policy definitions hash matches
- [ ] Scientific configuration hash matches
- [ ] Bundle Spec hash matches
- [ ] Environment hash matches
- [ ] Reconstruction Instructions hash matches
- [ ] G8 schema hash matches
- [ ] Scientific output schema hash matches
- [ ] Integrity Manifest inventory is internally consistent
- [ ] Package Manifest contains the complete allowed-input set

## C. Scientific design invariants
- [ ] S0 is identical across A/B
- [ ] C is identical across A/B
- [ ] T_acc is identical across A/B
- [ ] Transformation definitions are identical across A/B
- [ ] Admissibility rules are identical across A/B
- [ ] Transition function is identical across A/B
- [ ] X is declared before realization
- [ ] X_A and X_B are distinct
- [ ] X does not derive from H, O, V or T_real
- [ ] No post-hoc modification is permitted
- [ ] Realized transformations are admissible
- [ ] H is deterministically derived from the realized trajectory

## D. Executor-2 independence
- [ ] Executor-1 results are absent
- [ ] Executor-1 interpretation is absent
- [ ] Expected outcomes/coaching are absent
- [ ] Post-execution modifications are absent
- [ ] Executor-2 receives only the frozen package
- [ ] Reconstruction is independently reproducible from the package

## E. Freeze / authorization boundary
- [ ] Package status is CANDIDATE before freeze
- [ ] No scientific execution authorization is present
- [ ] Freeze audit is PASS
- [ ] Executor-2 reconstruction is PASS
- [ ] G8 authorization record is valid and hash-bound
- [ ] Only after all preceding checks may scientific execution be authorized

## F. Disposition
**C4 cannot be marked PASS until all applicable checks above are evidenced.**

Auditor:
Date:
Commit:
Disposition:
