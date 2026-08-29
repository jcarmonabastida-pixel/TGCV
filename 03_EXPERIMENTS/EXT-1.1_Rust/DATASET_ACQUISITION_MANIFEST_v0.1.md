# EXT-1.1 — Dataset acquisition manifest v0.1

**Status:** IDENTIFIED / SUITABILITY AUDITED / PHYSICAL ACQUISITION OPEN

## Canonical source

Schueller, W., Wachs, J., Servedio, V. D. P., Thurner, S. & Loreto, V. (2022). *Replication Data for Evolving collaboration, dependencies, and use in the Rust Open Source Software ecosystem*. Figshare.

DOI: `10.6084/m9.figshare.c.5983534.v1`

Source publication DOI: `10.1038/s41597-022-01819-z`

## Dataset suitability audit — PASS

The published data descriptor confirms that the dataset integrates Cargo package metadata, versions, semantic-versioned dependencies and daily downloads per package version. It also provides temporal data on dependencies, use and success and documents the database schema. The named tables include `packages`, `package_versions`, `package_dependencies` and `package_version_downloads`.

This is sufficient to establish **conceptual/schema-level suitability** for the EXT-1.1 observational unit and the provisional DR-013 outcome specification.

Evidence: Schueller et al. (2022), Scientific Data 9:703, Data Sources and Data Records sections.

## Important distinction

The suitability audit is **not** an acquisition or integrity audit. We have not yet obtained the exact binary/database artifact in this execution environment, so no hash, byte size, local file inventory or empirical schema check is claimed.

## Acquisition gate

Before computational use, record:

1. exact Figshare artifact identifier;
2. download URL;
3. file name(s);
4. byte size;
5. SHA-256 hash(es);
6. schema/version metadata;
7. temporal coverage;
8. row/cardinality checks for the tables used by EXT-1.1;
9. acquisition timestamp;
10. any transformation performed before analysis.

## Required evidence for confirmatory pipeline

- `packages`: package identity;
- `package_versions`: package version identity and release timestamp;
- `package_dependencies`: version-to-package dependency relations;
- `package_version_downloads`: date-level download observations by package version.

The exact column names, types and constraints must be verified from the acquired artifact rather than inferred from the publication.

## Acquisition attempt — 2026-08-29

The canonical Figshare DOI and publication were independently located and verified. The web-access layer confirms the dataset and its documented structure, but this execution environment could not retrieve the Figshare binary/API artifact directly. Therefore the physical acquisition gate remains OPEN rather than being falsely marked PASS.

## Freeze rule

No EXT-1.1 dataset freeze may be declared until the acquired artifact is hashed and its schema and temporal coverage have been independently checked against DR-013.

## Provenance note

The publication states that the data are hosted on Figshare, that the accompanying code can recreate the database, and that the database can be created in PostgreSQL or SQLite formats. It also documents pseudonymisation of direct developer-identifying information.
