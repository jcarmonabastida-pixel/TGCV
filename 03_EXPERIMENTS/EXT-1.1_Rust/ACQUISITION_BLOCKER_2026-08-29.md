# EXT-1.1 — Acquisition blocker — 2026-08-29

## Result of acquisition attempt

The canonical Figshare resource was verified through the published data descriptor and independent web search. The dataset is explicitly hosted on Figshare and the authors state that the database/code are included in the Figshare upload. The resource supports multiple database formats and the compressed data are documented as <=6 GB.

A direct binary retrieval was attempted from the execution environment but failed because outbound DNS/network access from the container is unavailable. This is an infrastructure limitation, not evidence that the dataset is inaccessible to the user.

## Required user-side action

If direct acquisition is still blocked from the assistant environment, download the dataset from the canonical Figshare resource and upload the resulting artifact here. Do not rename or modify the artifact before upload if possible.

Canonical resource:
`https://figshare.com/s/93158d03416765444650`

Version DOI:
`10.6084/m9.figshare.c.5983534.v1`

## Upon receipt

Immediately perform:

1. SHA-256 hashing;
2. archive/file inventory;
3. decompression if applicable while retaining original;
4. schema extraction;
5. temporal coverage audit;
6. cardinality checks;
7. DR-013 field mapping;
8. leakage/censoring checks;
9. reproducible acquisition record;
10. dataset FREEZE if all gates pass.

## Status

`DATASET SUITABILITY = PASS`
`CANONICAL RESOURCE = VERIFIED`
`PHYSICAL ARTIFACT = NOT YET ACQUIRED`
`INTEGRITY = OPEN`
`FREEZE = BLOCKED`
