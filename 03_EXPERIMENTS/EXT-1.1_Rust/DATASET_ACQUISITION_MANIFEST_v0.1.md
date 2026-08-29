# EXT-1.1 — Dataset acquisition manifest v0.1

**Status:** IDENTIFIED / ACQUISITION OPEN

## Canonical source

Schueller, W., Wachs, J., Servedio, V. D. P., Thurner, S. & Loreto, V. (2022). *Replication Data for Evolving collaboration, dependencies, and use in the Rust Open Source Software ecosystem*. Figshare.

DOI: `10.6084/m9.figshare.c.5983534.v1`

Source publication DOI: `10.1038/s41597-022-01819-z`

## Dataset suitability audit

The publication documents the presence of:

- package identities and creation dates;
- package versions;
- version-level dependency relations with semver constraints;
- daily downloads for package versions;
- package-level and repository-level temporal information.

The documented data model therefore supports the EXT-1.1 observational unit and the provisional DR-013 outcome specification at the conceptual/schema level.

## Acquisition gate

The exact downloadable artifact/version is **not yet frozen**. Before computational use, record:

1. exact Figshare artifact identifier;
2. download URL;
3. file name(s);
4. byte size;
5. SHA-256 hash(es);
6. schema/version metadata;
7. temporal coverage;
8. row/cardinality checks for the tables used by EXT-1.1;
9. local acquisition timestamp;
10. any transformation performed before analysis.

## Required tables / fields

Minimum expected evidence for the confirmatory pipeline:

- `packages`: package identity;
- `package_versions`: package version identity and release timestamp;
- `package_dependencies`: version-to-package dependency relations;
- `package_version_downloads`: date-level download observations by package version.

The exact column names and types must be verified from the acquired artifact rather than inferred from the publication.

## Freeze rule

No EXT-1.1 dataset freeze may be declared until the acquired artifact is hashed and its schema and temporal coverage have been independently checked against DR-013.

## Provenance note

The source publication states that the dataset is hosted on Figshare, that the accompanying code can rebuild the database, and that the data are distributed in PostgreSQL/SQLite-compatible forms. The publication also describes pseudonymisation of developer-identifying information.
