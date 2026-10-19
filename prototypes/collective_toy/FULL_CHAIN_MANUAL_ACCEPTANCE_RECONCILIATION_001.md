# Full Chain — Manual Acceptance Reconciliation 001

- **Date:** 2026-10-19
- **Status:** `ACCEPTED — MANUAL SYNTHETIC WALKTHROUGH`
- **Base:** `main` at `a92e3070aa75588c5b4c2ead7829f7bfe4c72dae`
- **Implementation under test:** Full Chain browser demonstrator, temporal prerequisite graph profile (profile 3).
- **Scope:** manual browser acceptance of the synthetic software demonstrator only. This record does not establish TGCV scientific validity, empirical causality, value creation, or real-system validity.
- **Evidence class:** user-reported observations from the guided browser walkthrough on 2026-10-19. The exported JSON remained on the user's machine; its bytes and hashes were not independently collected in this record.

## Acceptance rule

The end-to-end chain is accepted when valid ordered execution, separate outcome and contextual assessment, package export/import, and contract-declared replay work. UI display details are assessed against the existing contract and tests; they are not promoted into new requirements without an explicit design decision. No requirement is added for one dedicated test per predicate; grouped contract and adversarial coverage remains acceptable.

## Manual results

| ID | Result | Evidence / qualification |
|---|---|---|
| FC-GUIA-01 | PASS (user-reported) | Example model loaded and model/state/transition data inspected in the earlier walkthrough. |
| FC-GUIA-02 | PASS (user-reported) | Scenario exploration and accessible trajectories/results inspected in the earlier walkthrough. |
| FC-GUIA-03 | PASS (user-reported) | Accessible trajectory alternatives inspected in the earlier walkthrough. |
| FC-GUIA-04 | PASS (user-reported) | Graph and visual controls inspected in the earlier walkthrough. |
| FC-GUIA-05 | PASS (user-reported) | Baseline path A→B→D selected using `t_ab`, `t_bd`. |
| FC-GUIA-06 | PASS (user-reported) | Ordered execution completed at D with status `COMPLETED`. |
| FC-GUIA-07 | PASS — contract-conformant behavior | Adversarial sequence `t_ac, t_cd` was blocked at state C because a prerequisite was missing; it did not falsely complete. The primary UI intentionally presents a user-readable blocking explanation rather than internal transition IDs. The existing automated contract explicitly requires IDs and machine reason codes to remain in the audit package, not the primary view. The blocked trace retains `transition_id`, `required_transition_ids`, and `reason`. |
| FC-GUIA-08 | PASS (user-reported) | Trace/model/scenario provenance check reported complete in the earlier walkthrough; no independent byte-level inspection was retained here. |
| FC-GUIA-09 | PASS (user-reported) | Outcome treated as synthetic and linked to the functional execution, not as empirical measurement. |
| FC-GUIA-10 | PASS (user-reported) | Explicit illustrative outcome fields were entered in the earlier walkthrough. |
| FC-GUIA-11 | PASS (user-reported) | Observer, context, criterion, valuation rule and rationale were entered in the earlier walkthrough. |
| FC-GUIA-12 | PASS (user-reported) | Score entered and assessment reached `ASSESSED`. |
| FC-GUIA-13 | PASS | Comparison of executions A and B showed the warning that valuation contexts differed. |
| FC-GUIA-14 | PASS | Export completed to `toy-diamond-001-run.json`; user confirmed it was execution B. |
| FC-GUIA-15 | PASS | User inspected the exported file and confirmed `package_version=collective-toy-browser-run-002`, `package_stage=ASSESSMENT`, trace status `COMPLETED`, assessment status `ASSESSED`, outcome and integrity field `package_sha256`. The file itself was not uploaded or independently hashed in this record. |
| FC-GUIA-16 | PASS | Import/package validation displayed: `replay-verified: Integridad verificada y reproducción independiente coincidente bajo el contrato declarado.` |
| FC-GUIA-17 | PASS — contract-reported independent replay | No separate replay button is expected: the import validation action performs integrity/semantic checks and independent replay when the package and engine are supported. The UI reported `replay-verified`; the existing browser test likewise asserts that validating a freshly exported artifact reaches `replay-verified` and reports a matching independently recomputed result. A step-by-step replay display is not required by the current contract. |

## Reconciliation and disposition

1. The manual walkthrough exercised the chain through concrete execution, outcome, observer/contextual valuation, export, package validation, and independent replay.
2. FC-GUIA-07's generic user-facing diagnostic is **not a demonstrated functional gap**. The engine and trace record the blocked transition, missing prerequisite IDs, and machine reason; the primary view intentionally keeps those internal identifiers out of the concise explanation.
3. FC-GUIA-17 is satisfied by the package validation action's contract-declared independent replay. The absence of a separate replay button or a step-by-step replay display is not a failure under the existing contract.
4. The package's actual bytes, digest, and individual replayed steps were not independently retrieved; this record does not invent those values.
5. Overall disposition: `ACCEPTED — MANUAL SYNTHETIC WALKTHROUGH`, based on the user-reported manual results and the referenced existing UI contract tests. This is not scientific validation.

## Follow-up decision

No UI code correction is justified by these observations alone. The historical contract and existing tests intentionally keep internal blocked-transition identifiers out of the primary view, and package validation already performs independent replay. A more detailed replay viewer could be considered only as a separately agreed UX enhancement, with a defined requirement and acceptance criteria; it is not a current blocker.

This record does not authorize a change to `main`, a scientific execution, or a TGCV Core change.
