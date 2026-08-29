# EXT-1.1 — Dataset acquisition note — 2026-08-29

## Finding

The canonical Figshare landing/share resource has been independently identified as:

`https://figshare.com/s/93158d03416765444650`

It is the dataset/code resource cited by Schueller et al. (2022) and later work using the same anonymized Rust ecosystem dataset.

The authors' public reconstruction repository is:

`https://github.com/wschuell/repo_datasets`

The published data descriptor confirms that the dataset contains, among other tables, `package_dependencies`, `package_version_downloads`, `package_versions`, and `packages`. It also states that the data are available in multiple formats and that the compressed data do not exceed approximately 6 GB in the 2022 data release.

## Acquisition status

**CANONICAL RESOURCE IDENTIFIED — BINARY ACQUISITION STILL OPEN.**

The web research layer can verify the canonical share resource and its provenance, but it cannot provide the binary artifact bytes needed for an EXT-1.1 integrity freeze in this execution path.

Therefore:

- no SHA-256 is asserted;
- no byte size is asserted for a downloaded artifact;
- no local schema inspection is asserted;
- no dataset freeze is declared.

## Reproducibility route

If direct artifact acquisition is unavailable, the authors' reconstruction code provides a secondary reproducibility route. This route must not silently replace the canonical replication artifact: it would constitute a separately reconstructed dataset and would require its own provenance, version pinning, acquisition log, hashes and validation.

## Decision consequence

EXT-1.1 remains **BLOCKED only at physical acquisition/integrity verification**, not at conceptual dataset suitability. No further modification of DR-013 is required on the basis of this finding.
