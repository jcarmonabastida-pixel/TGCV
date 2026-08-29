# EXT-1.1 NPM Micro-slice Manifest v0.1

Date: 2026-08-29

## Purpose

Define the exact minimal raw inputs for the empirical npm gate. No full npm-follower archive is required.

## Packages

- lodash
- semver
- express

Rationale: mature, heavily used packages with long publication histories and substantial dependency metadata, reducing the chance that the gate outcome is driven by a trivial package.

## Historical structural cutoffs

Use three cutoffs common to all packages:

- T1 = 2019-01-01
- T2 = 2019-07-01
- T3 = 2020-01-01

For each package, reconstruct the package state using only versions whose npm publication timestamp is <= the cutoff.

## Raw metadata URLs

- https://registry.npmjs.org/lodash
- https://registry.npmjs.org/semver
- https://registry.npmjs.org/express

Save the responses unchanged as:

- `raw/npm/lodash.packument.json`
- `raw/npm/semver.packument.json`
- `raw/npm/express.packument.json`

## Outcome windows

For each cutoff use a 90-day strictly subsequent window:

- after T1: 2019-01-02 through 2019-04-01
- after T2: 2019-07-02 through 2019-09-29
- after T3: 2020-01-02 through 2020-03-31

Raw outcome URLs use the npm downloads range endpoint:

- https://api.npmjs.org/downloads/range/2019-01-02:2019-04-01/lodash
- https://api.npmjs.org/downloads/range/2019-01-02:2019-04-01/semver
- https://api.npmjs.org/downloads/range/2019-01-02:2019-04-01/express
- https://api.npmjs.org/downloads/range/2019-07-02:2019-09-29/lodash
- https://api.npmjs.org/downloads/range/2019-07-02:2019-09-29/semver
- https://api.npmjs.org/downloads/range/2019-07-02:2019-09-29/express
- https://api.npmjs.org/downloads/range/2020-01-02:2020-03-31/lodash
- https://api.npmjs.org/downloads/range/2020-01-02:2020-03-31/semver
- https://api.npmjs.org/downloads/range/2020-01-02:2020-03-31/express

## Important limitation

The manifest defines the acquisition slice; it does not claim that `T_acc` has already been computed. The resolver semantics must be pinned before the raw data are transformed. The experiment must not use current package metadata to infer historical dependency resolution beyond what is explicitly supported by the archived/published version data.

## User action

No download is required until the acquisition path is confirmed. If direct API retrieval is unavailable in the execution environment, download the 12 URLs above and upload the resulting JSON files together. Do not download npm-follower's full archive.
