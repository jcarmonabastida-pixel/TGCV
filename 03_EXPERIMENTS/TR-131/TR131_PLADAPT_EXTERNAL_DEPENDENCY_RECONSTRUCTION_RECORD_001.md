# TR-131 PLADAPT External Dependency Reconstruction Record

**Status:** CANONICAL PROVENANCE RECORDED — BUILD NOT YET EXECUTED
**Date:** 2026-09-23
**Purpose:** Record the externally sourced PLADAPT dependency required by the Rainbow SWIM PLA-SDP runtime before any local build or runtime modification.

## External source
- Repository: https://github.com/cps-sei/pladapt.git
- Pinned revision: `6d594bd8e16299f0bb8d0a403088c5638aff9e6f`
- Revision message observed during checkout: `change SWIG version to specific required version`
- Local checkout: `TR131_RAINBOW_SRC/pladapt`
- Checkout state: detached HEAD at the pinned revision; working tree clean at checkout.

## Provenance established

The pinned PLADAPT revision contains `reach/reach.sh`, `reach/build.sh`, `reach/build.xml`, and Java reachability sources under `reach/src`.

The PLADAPT README specifies that PLA-SDP requires the reachability-function generator and instructs execution of `cd $PLADAPT` followed by `reach/build.sh`.

The pinned `reach/build.sh` creates `reach/lib`, downloads `alloy4.2.jar` and `yamlbeans-1.11.jar`, creates the `yamlbeans.jar` symlink, and runs Ant against `reach/build.xml`.

The pinned `reach/build.xml` compiles `reach/src` into `reach/bin` using Alloy 4.2 and yamlbeans.

The pinned `reach/reach.sh` invokes `reach.Reach` using `reach/bin` and `reach/lib/*`, and extracts the Alloy AMD64 SAT solver libraries from `alloy4.2.jar` on first use.

## Rainbow relevance

The Rainbow SWIM configuration resolves:

    rainbow.adaptation.plasdp.reachPath = ${PLADAPT}/reach/reach.sh
    rainbow.adaptation.plasdp.reachModel = ${PLADAPT}/reach/model/reachAddSvrDimmer

The reconstructed Rainbow runtime contains the PLADAPT Java wrapper artifacts, but the complete PLADAPT tree providing `reach/reach.sh` and `reach/model/reachAddSvrDimmer` was absent. This caused `ADAPTATION_MANAGER: Environment variable PLADAPT is not defined` and prevented the PLA-SDP Reach invocation from resolving its external dependency.

## Execution boundary

No PLADAPT build has been executed as part of this record. No Rainbow source has been modified. No scientific execution has been authorized. The next operational step is to execute the pinned revision's own `reach/build.sh` locally and inspect the resulting artifacts before wiring them into the Rainbow runtime.

## Canonicality

This record belongs to the TGCV TR-131 experimental evidence/governance tree. The external PLADAPT repository remains the source of truth for PLADAPT itself; this file records only the provenance, pinned revision, reproducibility procedure, and TR-131 integration boundary.