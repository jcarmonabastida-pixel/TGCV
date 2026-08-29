# EXT-1.1 NPM Microexperiment Status v0.1

Date: 2026-08-29

## Status

**NOT EXECUTED / GATE OPEN**

The public-source audit confirms that npm package metadata exposes package identity, published versions, publication timestamps, and version-level dependency ranges. The public downloads API exposes historical package-level daily download counts and documented historical range limits.

However, the present execution environment could retrieve the npm registry documentation and package metadata endpoint but did not successfully retrieve the historical downloads-range endpoint as machine-readable data. Therefore no 3-package × 3-cutoff empirical result is claimed here.

## Important correction

Previous planning language saying the microexperiment was about to be executed must not be interpreted as an empirical execution. This file records the distinction between **source-level feasibility** and **executed evidence**.

## Verified source properties

1. npm package metadata endpoint: `GET /:package`.
2. Full packument contains `time`, mapping versions to publication timestamps.
3. Version objects contain `name`, `version`, `dependencies`, and `dist`.
4. Public downloads API provides range/point endpoints for package-level historical downloads; published documentation reports a maximum 18-month range per request and historical coverage from January 2015.

## Required execution

Select three packages with sufficient release history and low metadata complexity. For each package use three historical cutoffs, reconstruct `S_t`, compute `T_acc,t`, compare adjacent `T_acc`, then collect a strictly subsequent package-download outcome window.

The execution must persist raw packuments, raw download responses, resolver configuration, cutoff definitions, and hashes before calculating any outcome association.

## Acquisition rule

No full npm-follower archive is required for this gate. Prefer direct public npm sources for the microexperiment. If direct acquisition remains technically unavailable, obtain the minimum raw JSON files through a user download only after providing exact URLs and filenames.

## Decision rule

- PASS: all seven reproducibility/leakage checks succeed on all three packages and all three cutoffs.
- FAIL: any package/cutoff cannot be reconstructed deterministically or the outcome window cannot be separated temporally.
- INCONCLUSIVE: source is valid but execution cannot be reproduced due to acquisition/tooling limitations.

Current classification: **INCONCLUSIVE — acquisition/tooling limitation, not scientific failure.**
