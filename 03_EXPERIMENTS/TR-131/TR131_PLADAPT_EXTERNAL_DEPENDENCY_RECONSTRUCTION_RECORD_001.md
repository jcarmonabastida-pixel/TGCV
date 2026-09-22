# TR-131 PLADAPT External Dependency Reconstruction Record

**Status:** BUILD BLOCKED — JDK SOURCE/TARGET COMPATIBILITY
**Date:** 2026-09-23
**Purpose:** Record the externally sourced PLADAPT dependency and the local reconstruction boundary before Rainbow runtime integration.

## External source
- Repository: https://github.com/cps-sei/pladapt.git
- Pinned revision: `6d594bd8e16299f0bb8d0a403088c5638aff9e6f`
- Revision message observed during checkout: `change SWIG version to specific required version`
- Local checkout: `TR131_RAINBOW_SRC/pladapt`
- Checkout state: detached HEAD at the pinned revision; working tree clean at checkout.

## Provenance established
The pinned revision contains `reach/reach.sh`, `reach/build.sh`, `reach/build.xml`, and Java reachability sources under `reach/src`.

The README specifies that PLA-SDP requires the reachability-function generator and instructs `cd $PLADAPT` followed by `reach/build.sh`.

The pinned `reach/build.sh` creates `reach/lib`, downloads Alloy 4.2 and yamlbeans 1.11, creates the `yamlbeans.jar` symlink, and invokes Ant.

The pinned `reach/build.xml` declares Java source/target level 1.7 and compiles the reachability sources into `reach/bin`.

The pinned `reach/reach.sh` invokes `reach.Reach` using `reach/bin` and `reach/lib/*`, extracting the Alloy AMD64 SAT solver libraries on first use.

## Rainbow relevance
The Rainbow SWIM configuration resolves `rainbow.adaptation.plasdp.reachPath = ${PLADAPT}/reach/reach.sh` and `rainbow.adaptation.plasdp.reachModel = ${PLADAPT}/reach/model/reachAddSvrDimmer`.

The reconstructed Rainbow runtime contains PLADAPT Java wrapper artifacts, but the complete PLADAPT tree was absent. This caused `ADAPTATION_MANAGER: Environment variable PLADAPT is not defined` and prevented the PLA-SDP Reach invocation from resolving its external dependency.

## Build attempt 001 — 2026-09-23 01:41:57
The pinned `reach/build.sh` successfully downloaded `alloy4.2.jar` (13,317,090 bytes) and `yamlbeans-1.11.jar` (137,630 bytes), then created `reach/bin` and invoked Ant.

Compilation failed before producing the reachability classes because the active Java compiler no longer supports source/target 7:

    [javac] error: Source option 7 is no longer supported. Use 8 or later.
    [javac] error: Target option 7 is no longer supported. Use 8 or later.

This is an infrastructure/toolchain compatibility failure. It is not a PLADAPT source failure and does not justify changing the pinned PLADAPT source or its build.xml.

## Execution boundary
No Rainbow source has been modified. No scientific execution has been authorized. The next step is to rerun the pinned build under the already validated Java 8 environment used for Rainbow, then inspect the resulting artifacts before runtime integration.

## Canonicality
This record belongs to the TGCV TR-131 experimental evidence/governance tree. The external PLADAPT repository remains the source of truth for PLADAPT itself; this file records provenance, build observations, reproducibility state, and the TR-131 integration boundary.