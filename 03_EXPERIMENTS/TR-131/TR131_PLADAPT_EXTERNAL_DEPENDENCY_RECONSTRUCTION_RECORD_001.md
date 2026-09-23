# TR-131 PLADAPT External Dependency Reconstruction Record

**Status:** REACH EXECUTION PASS — RAINBOW PLA-SDP INVOCATION REPRODUCED
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

The reconstructed Rainbow runtime contains PLADAPT Java wrapper artifacts, but the complete PLADAPT tree was initially absent. This caused `ADAPTATION_MANAGER: Environment variable PLADAPT is not defined` and prevented the PLA-SDP Reach invocation from resolving its external dependency.

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

## Reach execution attempt 001 — 2026-09-23
An initial `./reach/reach.sh -h` invocation was not a valid help/smoke command for this program. It entered `reach.Reach` processing and was terminated after process inspection showed sustained CPU use. No scientific inference was made from this attempt.

## Reach execution attempt 002 — 2026-09-23
The valid Reach invocation was then reconstructed from the program's own usage syntax and the exact invocation observed in Rainbow logs.

Command shape:

    ./reach/reach.sh -i ./reach/model/reachAddSvrDimmer.als "./reach-i-reachAddSvrDimmer-S=3 TAP#=2 D=5.yaml" S=3 TAP#=2 D=5

The first attempt at this invocation passed `S=3 TAP#=2 D=5` as one shell argument and failed with:

    NumberFormatException: For input string: "3 TAP#"

This was a command-argument construction error, not a PLADAPT failure.

The corrected invocation passed `S=3`, `TAP#=2`, and `D=5` as separate arguments. Reach then completed and returned:

    ****Command: Run show for exactly 3 S, exactly 3 TAP, 5 D, 3 C, 3 CP, 3 TraceElement

The process exited and subsequent process inspection showed no remaining `reach.Reach` or `reach.sh` process.

## Interpretation
PLADAPT Reach is now **PASS at both build and isolated execution level** for the specific PLA-SDP model/invocation required by Rainbow SWIM. The pinned source tree, Java 8 toolchain, Alloy/yamlbeans dependencies, Reach classes, model, and executable path have all been exercised without modifying PLADAPT source.

This does **not** constitute scientific evidence and does not authorize TR-131 scientific execution. It closes an infrastructure/dependency gate only.

## Next integration gate
Before the next Rainbow runtime launch, the environment variable must be defined in the same shell context:

    export PLADAPT=/mnt/c/Users/pedri/TGCV/TR131_RAINBOW_SRC/pladapt

Rainbow should then be relaunched without source modification. The next observed failure, if any, is the next runtime integration blocker to diagnose.

## Execution boundary
No Rainbow source has been modified by the PLADAPT reconstruction. No scientific execution has been authorized.

## Canonicality
This record belongs to the TGCV TR-131 experimental evidence/governance tree. The external PLADAPT repository remains the source of truth for PLADAPT itself; this file records provenance, build observations, reproducibility state, and the TR-131 integration boundary.
