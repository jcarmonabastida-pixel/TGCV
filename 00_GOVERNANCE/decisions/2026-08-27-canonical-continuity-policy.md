# Decision — GitHub as canonical TGCV continuity layer

**Date:** 2026-08-27
**Status:** ADOPTED

## Decision

GitHub repository `jcarmonabastida-pixel/TGCV` is the canonical continuity point for the entire TGCV programme.

## Canonical contents

The repository is the authoritative versioned index and storage location for:

- research-state decisions and freezes;
- Core architecture and ontology;
- RMA and traceability;
- literature/evidence records and SLR work;
- experimental protocols, code and reproducibility manifests;
- datasets' identities, provenance and hashes (not sensitive/raw datasets);
- external scientific assets;
- industrial/application adaptations;
- methodological assets and programme-management records.

## Continuity rule

Every substantive state change must be represented in GitHub by a versioned commit. Frozen states are immutable snapshots. Superseding work creates a new version and preserves the predecessor.

Conversation context, local working files and other storage locations may be working sources, but are not authoritative when they conflict with the repository's canonical record.

## Provenance rule

Recovered historical material is added with its provenance and epistemic status. Unknown or unsupported details must remain explicitly unknown rather than being promoted to canonical facts.

## Experimental integrity

No experimental result is considered canonical merely because it appears in a conversation. The protocol, data identity/provenance, configuration, execution and result record must be traceable.

## Recovery rule

If continuity is interrupted, the recovery procedure is:

1. read `STATUS.md`;
2. inspect `00_GOVERNANCE/decisions/` and `00_GOVERNANCE/freezes/`;
3. identify the latest valid freeze/state;
4. follow RMA dependencies;
5. resume from the recorded next operation.
