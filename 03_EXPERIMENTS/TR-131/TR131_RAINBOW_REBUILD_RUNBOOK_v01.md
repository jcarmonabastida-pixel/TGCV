# TR-131 Rainbow — Rebuild Runbook v0.1

## Purpose

This document preserves the recovered build procedure and the evidence status for the TR-131 Rainbow experimental package. Its purpose is to prevent repetition of the long compilation/debugging sequence already performed.

Rainbow is an experimental instrument for unlocking TR-131 and for observing transformation-space dynamics. This is not a Rainbow maintenance project.

## Canonical source / execution boundary

- TGCV GitHub repository: `jcarmonabastida-pixel/TGCV`
- Rainbow working tree used for execution: `TR131_RAINBOW_SRC`
- GitHub is the canonical source for TGCV governance and runbooks.
- Compilation and generated execution artifacts remain local unless explicitly incorporated into TGCV.

## Environment

Validated Java runtime for this package:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH="$JAVA_HOME/bin:$PATH"
```

JDK 21 is not suitable for the legacy source/target configuration used by this package.

## Important Maven structure

The SWIM deployment is:

```text
deployments/rainbow-swim/pom.xml
```

It is NOT:

```text
rainbow/rainbow-swim
```

Therefore do not use `-pl rainbow/rainbow-swim`.

## Recovered build history

### 1. JavaCC / parsec generation

The reactor initially failed because JavaCC-generated parser sources were absent.

The POM in `libs/parsec/pom.xml` was inspected and was deliberately NOT modified. The following command successfully generated/installed parsec:

```bash
cd libs/parsec
mvn -Dmaven.test.skip=true javacc:javacc install
```

This step reached `BUILD SUCCESS`.

This is the confirmed reusable prerequisite.

### 2. Why `-DskipTests` was insufficient

The normal `build.sh` path uses a Maven target equivalent to:

```text
javacc:javacc install
```

and subsequent invocations encountered `parsec:testCompile`.

The observed failure was caused by missing JUnit classes during test compilation:

- `package org.junit does not exist`
- `class file for org.junit.Assert not found`
- cascaded failures involving `assertEquals`, `@Test`, `@Before`, etc.

Therefore `-DskipTests` is insufficient for this legacy build: it skips test execution but does not prevent test compilation.

The required Maven property for bypassing test compilation is:

```text
-Dmaven.test.skip=true
```

### 3. Previously used build.sh target

The Rainbow package build target previously used was:

```bash
./build.sh -s -d rainbow-swim -t swim
```

A later invocation also used:

```bash
./build.sh -d rainbow-swim -s
```

These commands are recorded as the intended package-build path.

IMPORTANT EVIDENCE STATUS: the recovered history does NOT establish a verified full-package `BUILD SUCCESS` for these commands. They subsequently failed in `parsec:testCompile` because of missing JUnit. Do not describe the full package build as previously proven successful.

### 4. Recovered workaround for the parsec test-compile problem

A non-invasive workaround was proposed that creates a temporary copy of `build.sh` and changes only the Maven invocation so that test compilation is skipped:

```bash
sed 's/mvn -DskipTests \\$jcctarget/mvn -Dmaven.test.skip=true -DskipTests $jcctarget/' build.sh > /tmp/build-tr131-rainbow.sh && bash /tmp/build-tr131-rainbow.sh -s -d rainbow-swim
```

This leaves the repository `build.sh` unchanged.

IMPORTANT EVIDENCE STATUS: the recovered history does NOT establish a full-package `BUILD SUCCESS` for this temporary-script variant. It is the reconstructed next build procedure, not a historically proven result.

## Known failed command — do not repeat

Do NOT use:

```bash
mvn -pl rainbow/rainbow-swim -am ...
```

The path is wrong.

A direct root-reactor attempt against:

```bash
mvn -pl deployments/rainbow-swim -am package -Dmaven.test.skip=true
```

was also recorded as failing because the deployment is not included in the root reactor in the way required by that `-pl` invocation.

## Rebuild protocol

When a full rebuild is required, first establish Java 8:

```bash
cd /mnt/c/Users/pedri/TGCV/TR131_RAINBOW_SRC
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH="$JAVA_HOME/bin:$PATH"
```

Then ensure the known-good parsec prerequisite is installed:

```bash
cd libs/parsec
mvn -Dmaven.test.skip=true javacc:javacc install
```

Then return to the Rainbow root and use the non-invasive temporary build-script workaround:

```bash
cd ..
sed 's/mvn -DskipTests \\$jcctarget/mvn -Dmaven.test.skip=true -DskipTests $jcctarget/' build.sh > /tmp/build-tr131-rainbow.sh
bash /tmp/build-tr131-rainbow.sh -s -d rainbow-swim
```

The result of this final step must be recorded as either PASS or FAIL. Until a real `BUILD SUCCESS` and the expected package artifacts are observed, the full-package procedure remains UNVERIFIED.

## Diagnostic patch continuity

The Rainbow diagnostic patch was made idempotent and committed as:

```text
5d13dad375ed53d4d16052a1098890c1ab6f562a
```

The patch produced exactly eight diagnostic markers (before/after pairs around the relevant connection/heartbeat operations) with no duplicates or legacy markers.

An isolated Java 8 compilation of `RainbowMaster.java` also passed; this was a diagnostic/instrumentation fallback and is NOT equivalent to a complete Rainbow package rebuild.

## Scientific boundary

The purpose of recompiling Rainbow is to unblock TR-131 and obtain experimental evidence about transformation-space dynamics. The current TGCV direction is not a test of a simple causal relation `Delta_Tacc -> Delta_Value`. Any further Rainbow work must be justified by its contribution to TR-131 / transformation-space dynamics.

## Status at persistence

- Java 8 environment: VERIFIED.
- JavaCC generation/install for parsec with test compilation disabled: VERIFIED.
- parsec POM modification: NOT required / must remain untouched.
- Correct SWIM deployment path: VERIFIED as `deployments/rainbow-swim`.
- Standard `build.sh` path: historically attempted, but full success NOT VERIFIED.
- Temporary `maven.test.skip=true` build-script workaround: reconstructed, full success NOT VERIFIED.
- Full Rainbow package reproducible build: **NOT YET PROVEN**.
