# EXT-1.1 C3 — self-contained crate bundle

## Purpose
Preserve the exact crate tarballs resolved by the historical C3 Cargo.lock.

## Resolved packages
cfg-if 1.0.0
getrandom 0.2.2
libc 0.2.94
ppv-lite86 0.2.10
rand 0.8.0
rand_chacha 0.3.0
rand_core 0.6.2
rand_hc 0.3.0
wasi 0.10.2+wasi-snapshot-preview1

## Verification
All 9 crate SHA-256 values match the checksums recorded in project/Cargo.lock.

## Qualification
This bundle contains the exact crate artifacts and project lockfiles. The historical registry index is not yet reduced to a self-contained portable index subset.

## Historical index fragments

The files under bundle/index/ are retained locally as provenance artifacts derived from the historical Cargo registry index used for the offline C3 resolution. They contain historical package-version metadata (dependencies, checksums, features, and yanked status) beyond the exact versions required by the frozen Cargo.lock.

They are intentionally excluded from version control and are not part of the minimal versioned C3 bundle. Their retention does not imply that the bundle has been demonstrated to be independently portable to a clean machine.
