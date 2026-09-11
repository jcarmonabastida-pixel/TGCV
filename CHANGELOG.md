# Changelog

## 2026-09-11 — EXT-UPD-4.8 O3 accessibility-closure reassessment closure and propagation

- Executed the authorized bounded corrective assessment for `IUT-A-01 / O3` with execution integrity `PASS`.
- Confirmed RF-AC01 through RF-AC04 `PASS`.
- Closed O3 accessibility as `INDETERMINATE / H-B` with hard stop `HS-AC01` because MC02 (alternative tooling T-C availability/accessibility at decision time) and MC03 (required setup within the decision-time boundary) remained unresolved.
- Preserved the distinction between native candidate identification and decision-time accessibility closure; the decisive accessibility rule remains `ANALYST-INTERPRETATION`.
- Recorded the execution result and governance closure as immutable evidence records.
- Propagated the material methodological boundary to Evidence→Claim Matrix v1.1, RMA v3.32, RMA traceability and STATUS.
- Kept C01–C16 unchanged; no Core modification, utility, superiority, causal, value or transversal claim was introduced.
- No additional constructive attempt, comparative IUT or reopening of EXT-UPD-4.7 is authorized by this closure.
- Standing industrial execution authorization remains `NONE`.

## 2026-09-11 — Material evidence propagation rule, IUT-A-01 and IT-NOSD-010

- Identified and corrected an overly aggressive governance rule that treated absence of scientific claim upgrade as sufficient reason to omit material experimental evidence from the Evidence→Claim Matrix.
- Established the operative rule: material experimental evidence is propagated when it adds, removes, qualifies, bounds or otherwise changes the evidentiary basis or interpretation of a claim, even when no claim status/level changes; claim upgrade remains a separate decision.
- Propagated IUT-A-01 U2 FULL_PILOT 001 to Evidence→Claim Matrix v1.0 as bounded comparative methodological evidence: M1 PASS (+40 pp) and M2 FAIL, final `U2-NULL`; C12 and all other C01–C16 statuses remain unchanged.
- Propagated IT-NOSD-010 G0/G1/G2 to Evidence→Claim Matrix v1.0 as bounded methodological evidence for reconstruction and downstream separation; no C01–C16 status upgraded.
- Created RMA v3.31 and propagated the material-evidence rule and both evidence records without changing the scientific Core.
- Updated RMA traceability to v3.31 and current pointers; historical versions remain immutable.
- Updated `CANONICAL_STATE.json` to RMA v3.31, Evidence→Claim Matrix v1.0 and traceability v3.31.
- Updated STATUS with the evidence-propagation boundary and current bounded evidence state.
- Updated the canonical current-state validator so it verifies current-version alignment and requires the current matrix to explicitly declare the distinction between material evidence propagation and claim upgrade.
- The validator remains a validator: it does not infer scientific upgrades or mutate the matrix automatically.
- Standing industrial execution authorization remains `NONE`.

## 2026-09-11 — IT-NOSD-010 TR-132 IT-G2 closure propagation

- Closed IT-NOSD-010 IT-G2 as `CLOSED — BOUNDED DOWNSTREAM-SEPARATION PASS` for the same frozen public 5G-to-5G handover event admitted through G0 and G1.
- Independent IT-G2 executor v0.1 returned `PASS`; G2-01 through G2-10 all passed.
- Verified frozen events/spectrum MD5s, candidate continuity, pre-state continuity, post-state observability, transition identity, accessibility isolation, outcome separation, temporal closure, evidence integrity and deterministic reconstruction.
- Confirmed accessibility was not reused as outcome and outcome was not used to define post-state.
- Confirmed complete ex-ante enumeration of `T_acc` was not required.
- Recorded bounded downstream reconstruction only; no utility, causality, value, superiority, normative 3GPP compliance or scientific validation claim was introduced.
- Propagated the closure to RMA v3.30, current RMA pointer, RMA traceability and current-state governance records.
- Standing industrial execution authorization remains `NONE`.
- Historical records remain immutable.
