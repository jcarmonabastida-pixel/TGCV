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

## New failure recorded — 2026-09-23: test compilation still reaches typelib

The first execution of the reconstructed temporary-script workaround failed in the typelib module during Maven testCompile with missing JUnit classes:

- package org.junit does not exist
- class file for org.junit.Assert not found
- cascaded @Test / @Before symbol failures
- failing goal: org.apache.maven.plugins:maven-compiler-plugin:3.0:testCompile
- project: typelib

This establishes that the previous sed workaround was too narrow: it altered the jcctarget invocation but did not prevent test compilation for all subsequent module Maven invocations. The error is therefore a build-script propagation problem, not evidence that typelib production sources are broken.

### Rule added from this failure

Do not repeat the narrow jcctarget-only substitution. Before the next package-build attempt, inspect build.sh for all Maven invocations that can reach module testCompile and determine where -DskipTests is introduced. The required invariant for this legacy package build is that every relevant Maven invocation used by the package build carries -Dmaven.test.skip=true, not merely the JavaCC/parsec invocation.

Do not modify module POMs to solve this unless the build-script route is proven insufficient. In particular, keep libs/parsec/pom.xml untouched.

**Current status:** this failure is persisted as a known blocker; the next command should inspect the actual build.sh Maven call sites before another build is launched.

## Build-script inspection result — 2026-09-23

Inspection of the canonical Rainbow `build.sh` showed 12 Maven invocations. The script defines `SKIPTESTS="-DskipTests"` (line 72), while multiple invocations hard-code `-DskipTests` (lines 113, 121, 127, 131, 135) and others use `$SKIPTESTS` (105, 109, 117, 144, 149, 155). Line 139 invokes Maven without either flag.

This confirms the previous workaround was incomplete: replacing only the JavaCC invocation cannot prevent downstream `testCompile` phases. The next repair must operate on the build-script flag propagation as a whole. The intended temporary build-script invariant is to replace the effective test-skipping mode with `-Dmaven.test.skip=true` for the package build, while preserving the original `build.sh` unchanged.

No new build has been launched from this inspection. POMs remain untouched.

## build.sh control-flow inspection — 2026-09-23

Inspection of lines 65–145 confirms the relevant control flow. Option `-s` only sets `SKIPTESTS="-DskipTests"` (lines 71–73). The build then executes Maven sequentially in `libs/auxtestlib`, `libs/incubator`, `libs/parsec`, `libs/typelib`, `libs/eseblib`, followed by Rainbow modules. Several calls hard-code `-DskipTests`, while line 139 (`rainbow-utility-model`) invokes `mvn $target` without any test-skip flag. Therefore the robust temporary repair is to construct a copy of the script in which `-s` selects `-Dmaven.test.skip=true` and all hard-coded `-DskipTests` calls are replaced by `-Dmaven.test.skip=true`; the unguarded utility-model invocation must also receive the same property. The original `build.sh` remains unchanged.

This is now a sufficiently specified workaround to test. It is still a proposed build workaround until a complete package build succeeds; no scientific conclusion is attached to it.

## Full Rainbow package build — 2026-09-23

The temporary build-script workaround was executed successfully with JDK 8 and `-s -d rainbow-swim`. The Rainbow package compiled and was generated successfully. This validates the build workaround for the current source tree.

Validated sequence: preserve original `build.sh`; create a temporary copy; change `SKIPTESTS` to `-Dmaven.test.skip=true`; replace hard-coded `-DskipTests`; ensure the previously unguarded `rainbow-utility-model` invocation receives the same skip property; execute the temporary script with Java 8 and `rainbow-swim` target.

The validation concerns compilation/package generation only. It does not constitute scientific execution or TR-131 evidence by itself.

## Launcher discovery gate — 2026-09-23

The generated SWIM target package was inspected and does not itself contain a Rainbow runtime launcher. The runtime artifacts are under `deployments/rainbow-swim/target`; the generated `Rainbow-*/targets/swim` tree contains target configuration/model/system assets rather than the Rainbow process entry point.

Operational rule: launcher discovery is a separate gate after successful package generation. Because this path has previously required iteration, once the correct Rainbow launcher/entry point is identified and verified, its exact path, invocation, required working directory/properties, and observed startup markers must be recorded in this runbook before proceeding. Do not execute target utility scripts such as `system/util/swimcmd.sh` as a substitute for the Rainbow launcher.

Current status: launcher not yet identified; no runtime execution performed in this step.
