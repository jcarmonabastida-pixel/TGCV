# TR-131 PLADAPT External Dependency Reconstruction Record

**Status:** REACH BUILD PASS — JAVA 8 COMPATIBILITY VERIFIED
**Date:** 2026-09-23
**Purpose:** Record the externally sourced PLADAPT dependency and the local reconstruction boundary before Rainbow runtime integration.

## External source
- Repository: https://github.com/cps-sei/pladapt.git
- Pinned revision: `6d594bd8e16299f0bb8d0a403088c5638aff9e6f`
- Revision message observed during checkout: `change SWIG version to specific required version`
- Local checkout: `TR131_RAINBOW_SRC/pladapt`
- Checkout state: detached HEAD at the pinned revision.

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

Compilation initially failed because the active compiler did not support source/target 7.

## Build attempt 002 — 2026-09-23
The same pinned PLADAPT build was rerun under the already validated Java 8 environment:

    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

The downloads were already present. The `ln` step reported that `reach/lib/yamlbeans.jar` already existed; Ant then compiled all 10 source files successfully.

Result:

    [javac] Compiling 10 source files to .../pladapt/reach/bin
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 1.7
    BUILD SUCCESSFUL

The single compiler warning is a Java 8 compatibility warning associated with the legacy source level; compilation completed successfully.

## Interpretation
PLADAPT Reach compilation is now **PASS at the infrastructure/build level** under Java 8, with the source tree and build definition unchanged. The earlier JDK compatibility block is resolved by selecting the validated Java 8 toolchain rather than modifying PLADAPT.

## Execution boundary
No Rainbow source has been modified. No scientific execution has been authorized. This PASS establishes only that the pinned PLADAPT Reach component can be built under the validated Java 8 environment. Runtime invocation and integration remain separate gates.

## Canonicality
This record belongs to the TGCV TR-131 experimental evidence/governance tree. The external PLADAPT repository remains the source of truth for PLADAPT itself; this file records provenance, build observations, reproducibility state, and the TR-131 integration boundary.