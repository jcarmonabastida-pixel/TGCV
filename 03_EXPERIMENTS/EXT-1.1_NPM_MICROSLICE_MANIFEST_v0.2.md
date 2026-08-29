# EXT-1.1 NPM Micro-slice Manifest v0.2

Date: 2026-08-29

## Change from v0.1

The package `express` is replaced by `webpack` because the uploaded historical download responses for express contain 90/90 zero-download observations in all three windows. This is treated as an acquisition/data-quality failure, not as a scientific result.

The package `lodash` and `semver` inputs already acquired remain valid for the structural portion of the gate.

## Packages

- lodash
- semver
- webpack

## Structural cutoffs

- T1 = 2019-01-01
- T2 = 2019-07-01
- T3 = 2020-01-01

## New files required

### Packument
`https://registry.npmjs.org/webpack`

Save as: `webpack.packument.json`

### Downloads T1
`https://api.npmjs.org/downloads/range/2019-01-02:2019-04-01/webpack`

Save as: `webpack.downloads.T1.json`

### Downloads T2
`https://api.npmjs.org/downloads/range/2019-07-02:2019-09-29/webpack`

Save as: `webpack.downloads.T2.json`

### Downloads T3
`https://api.npmjs.org/downloads/range/2020-01-02:2020-03-31/webpack`

Save as: `webpack.downloads.T3.json`

## Existing files retained

The uploaded archive already contains valid structural packuments and download windows for lodash and semver. Keep them unchanged.

## Gate rationale

Webpack has a long historical release series and non-trivial dependency metadata; npm's public package page currently documents hundreds of versions and active download volume, making it a more useful third package for the microexperiment than an outcome series that is identically zero.

The new four files are the only additional acquisition requested. Do not redownload the other eight files and do not download npm-follower.

## Acceptance checks

The replacement webpack download series must contain 90 daily records with non-zero aggregate activity. If it is also all-zero or otherwise malformed, stop and report acquisition failure rather than replacing packages again automatically.
