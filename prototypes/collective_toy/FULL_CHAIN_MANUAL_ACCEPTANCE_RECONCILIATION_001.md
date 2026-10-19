# Full Chain — Manual Acceptance Reconciliation 001

- **Date:** 2026-10-19
- **Status:** `ACCEPTED_WITH_SECONDARY_OBSERVATIONS`
- **Base:** `main` at `a92e3070aa75588c5b4c2ead7829f7bfe4c72dae`
- **Implementation under test:** Full Chain browser demonstrator, temporal prerequisite graph profile (profile 3).
- **Scope:** manual browser acceptance of the synthetic software demonstrator only. This record does not establish TGCV scientific validity, empirical causality, value creation, or real-system validity.
- **Evidence class:** user-reported observations from the guided browser walkthrough in the conversation on 2026-10-19. The exported JSON remained on the user's machine; its bytes and hashes were not independently collected in this record.

## Acceptance rule

The end-to-end chain is accepted when valid ordered execution, separate outcome and contextual assessment, package export/import, and contract-declared replay work. Secondary diagnostic and display limitations are recorded explicitly and do not silently become scientific claims. No requirement is added for one dedicated test per predicate; grouped contract and adversarial coverage remains acceptable.

## Manual results

| ID | Result | Evidence / qualification |
|---|---|---|
| FC-GUIA-01 | PASS (user-reported) | Example model loaded and model/state/transition data inspected in the earlier walkthrough. |
| FC-GUIA-02 | PASS (user-reported) | Scenario exploration and accessible trajectories/results inspected in the earlier walkthrough. |
| FC-GUIA-03 | PASS (user-reported) | Accessible trajectory alternatives inspected in the earlier walkthrough. |
| FC-GUIA-04 | PASS (user-reported) | Graph and visual controls inspected in the earlier walkthrough. |
| FC-GUIA-05 | PASS (user-reported) | Baseline path A→B→D selected using `t_ab`, `t_bd`. |
| FC-GUIA-06 | PASS (user-reported) | Ordered execution completed at D with status `COMPLETED`. |
| FC-GUIA-07 | PARTIAL | Adversarial sequence `t_ac, t_cd` was blocked at state C because a prerequisite was missing; it did not falsely complete. UI diagnostic did not identify the blocked transition `t_cd` and missing prerequisite `t_ab` explicitly. |
| FC-GUIA-08 | PASS (user-reported) | Trace/model/scenario provenance check reported complete in the earlier walkthrough; no independent byte-level inspection was retained here. |
| FC-GUIA-09 | PASS (user-reported) | Outcome treated as synthetic and linked to the functional execution, not as empirical measurement. |
| FC-GUIA-10 | PASS (user-reported) | Explicit illustrative outcome fields were entered in the earlier walkthrough. |
| FC-GUIA-11 | PASS (user-reported) | Observer, context, criterion, valuation rule and rationale were entered in the earlier walkthrough. |
| FC-GUIA-12 | PASS (user-reported) | Score entered and assessment reached `ASSESSED`. |
| FC-GUIA-13 | PASS | Comparison of executions A and B showed the warning that valuation contexts differed. |
| FC-GUIA-14 | PASS | Export completed to `toy-diamond-001-run.json`; user confirmed it was execution B. |
| FC-GUIA-15 | PASS | User inspected the exported file and confirmed `package_version=collective-toy-browser-run-002`, `package_stage=ASSESSMENT`, trace status `COMPLETED`, assessment status `ASSESSED`, outcome and integrity field `package_sha256`. The file itself was not uploaded or independently hashed in this record. |
| FC-GUIA-16 | PASS | Import/package validation displayed: `replay-verified: Integridad verificada y reproducción independiente coincidente bajo el contrato declarado.` |
| FC-GUIA-17 | PASS — limited UI evidence | The importer reported contract-declared independent replay verification. No separate replay button was pressed, and the UI showed only the recommended workflow below the message, without a visible step-by-step replay trace. The contract-level message is recorded; visual inspection of the replayed transition sequence is not claimed. |

## Reconciliation and disposition

1. The core demonstrator chain was exercised through execution, outcome, observer/contextual valuation, export, package validation and a reported independent replay.
2. FC-GUIA-07 remains a **diagnostic-specificity limitation**: the blocking behavior worked, but the message did not name the exact blocked transition and prerequisite.
3. FC-GUIA-17 remains **contract-reported replay with limited UI observability**: the application reported replay verification, but the user-facing screen did not expose the replayed sequence for direct visual comparison.
4. The package's actual bytes, digest, and individual replayed steps were not independently retrieved; this record does not invent those values.
5. Overall disposition: `ACCEPTED_WITH_SECONDARY_OBSERVATIONS` for the manual synthetic walkthrough, subject to the above limitations. Do not represent this as scientific validation.

## Follow-up candidate (not implemented by this record)

Consider one grouped, separately validated UX correction on a development branch:
- on prerequisite-blocked execution, expose the blocked transition ID and missing prerequisite ID;
- in package import/replay results, expose a concise replay summary (execution ID, ordered transition IDs, final state/status, and links/digests for trace and outcome/assessment where present).

This record does not authorize a change to `main`, a scientific execution, or a TGCV Core change. Any correction must be implemented and validated in a separate branch/PR before promotion.
