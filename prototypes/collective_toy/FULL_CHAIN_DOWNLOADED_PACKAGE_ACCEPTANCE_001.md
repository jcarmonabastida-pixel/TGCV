# Full Chain — Downloaded Executable Package Acceptance 001

- **Date:** 2026-10-20
- **Status:** `ACCEPTED — USER-REPORTED LOCAL FUNCTIONAL WALKTHROUGH`
- **Repository base:** `main` at the time the audit branch was created; this record is maintained on a separate audit branch until reviewed.
- **Build workflow:** [Run 39299724496](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39299724496)
- **Build source commit:** `8476a2d810610ea38156678eb83a31a4ff7d38a4` (distribution artifact name); workflow run head SHA: `95a7e30f1fe312e9932695de04d7ff48447f0e02`.
- **Scope:** User-reported manual test of the downloaded standalone browser distribution on the user's Windows environment. This is software/package acceptance only, not scientific validation of TGCV.
- **Provenance limitation:** The downloaded ZIP's local bytes and SHA-256 were not supplied to the audit process, so this record does not assert byte-for-byte identity between the user's download and the CI artifact.

## CI artifact provenance

The workflow run completed successfully. Its `browser-cross-runtime` job reported success for browser/Python concordance, standalone distribution preparation, artifact uploads, and replay of the browser/Python suite from a clean source archive.

Published artifacts recorded by GitHub Actions:

| Artifact | GitHub artifact SHA-256 | Qualification |
|---|---|---|
| `tgcv-full-chain-executable-8476a2d810610ea38156678eb83a31a4ff7d38a4` | `892f71be731d20a13f9b535f8c33c402afe0324054ae8a74f671d51e181c2a89` | CI artifact digest; not measured from the user's local download. |
| `tgcv-full-chain-acceptance-8476a2d810610ea38156678eb83a31a4ff7d38a4` | `f6b61271d82c0a5433028c715d10eddfe140582f4113319721b68a04554440d0` | CI artifact digest; not measured from the user's local download. |

## Manual acceptance results

Results below are based on the user's direct confirmations during the guided local walkthrough on 2026-10-20.

| ID | Result | Observation |
|---|---|---|
| PKG-LOCAL-01 | PASS (user-reported) | `index.html` opened successfully in Google Chrome. Initial failure was caused by Windows associating `.html` files with AVG; opening with Chrome worked. |
| PKG-LOCAL-02 | PASS (user-reported) | The synthetic example included in the downloaded package loaded successfully. |
| PKG-LOCAL-03 | PASS (user-reported) | Accessible transformations could be explored and trajectories displayed. |
| PKG-LOCAL-04 | PASS (user-reported) | A selected trajectory executed sequentially and reached its final state. |
| PKG-LOCAL-05 | PASS (user-reported) | The user entered an outcome and completed contextual assessment. |
| PKG-LOCAL-06 | PASS (user-reported) | Export and subsequent import of the execution package completed. |
| PKG-LOCAL-07 | PASS (user-reported) | Import validation reported integrity verified and independent replay coincident with the declared contract. |

## Disposition

The downloaded distribution has passed the guided, user-reported local functional walkthrough listed above. The observed AVG file association was an environment/open-with issue: the same `index.html` opened in Chrome, and no repository or package change was required to proceed.

The combined evidence supports acceptance of the package's basic local functionality, qualified by user-reported observations and the lack of a local artifact digest. It does not independently prove that the local ZIP bytes match the CI artifact digest, nor does it validate scientific claims, empirical causality, or TGCV value construction.

No changes to `main`, demonstrator code, or TGCV Core are made by this record.
