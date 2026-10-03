#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

SOURCE_REV="eb68158a3d74581f69ccb8bc4f47673b12abdf85"
TARGET_BLOB_SHA="7481dee30f1ae07d7dd9212d7891dc336f1e96ae"
OBSERVER_MANIFEST="observer/META-INF/MANIFEST.MF"

echo "== Repository structure =="
test -f pom.xml
test -f target-definition/pom.xml
test -f target-definition/org.eclipse.viatra.examples.cps.target.target
test -f "$OBSERVER_MANIFEST"
test -f observer/pom.xml

echo "== Historical CPS bundle materialization =="
for bundle in \
  org.eclipse.viatra.examples.cps.model \
  org.eclipse.viatra.examples.cps.deployment \
  org.eclipse.viatra.examples.cps.traceability
do
  b="cps-models/$bundle"
  test -f "$b/pom.xml"
  test -f "$b/META-INF/MANIFEST.MF"
  test -f "$b/build.properties"
  test -f "$b/plugin.xml"
  test -f "$b/plugin.properties"
  test -d "$b/model"
  test -d "$b/src"
  test -n "$(find "$b/model" -type f -print -quit)"
  test -n "$(find "$b/src" -type f -print -quit)"
  grep -Fq "Bundle-SymbolicName: $bundle;singleton:=true" "$b/META-INF/MANIFEST.MF"
  grep -Fq "Bundle-Version: 2.1.0.qualifier" "$b/META-INF/MANIFEST.MF"
  grep -Fq "Bundle-RequiredExecutionEnvironment: JavaSE-1.8" "$b/META-INF/MANIFEST.MF"
  grep -Fq "model/" "$b/build.properties"
  grep -Fq "source.. = src/" "$b/build.properties"
  grep -Fq "<packaging>eclipse-plugin</packaging>" "$b/pom.xml"
  grep -Fq "<artifactId>$bundle</artifactId>" "$b/pom.xml"
  grep -Fq "<artifactId>tgcv-viatra-v002-cps-models</artifactId>" "$b/pom.xml"
done

echo "== Historical source revision provenance =="
grep -Fq "$SOURCE_REV" materialize-historical-cps-models.sh

echo "== Reactor wiring =="
grep -Fq '<module>target-definition</module>' pom.xml
grep -Fq '<module>cps-models</module>' pom.xml
grep -Fq '<module>observer</module>' pom.xml
grep -Fq '<module>org.eclipse.viatra.examples.cps.model</module>' cps-models/pom.xml
grep -Fq '<module>org.eclipse.viatra.examples.cps.deployment</module>' cps-models/pom.xml
grep -Fq '<module>org.eclipse.viatra.examples.cps.traceability</module>' cps-models/pom.xml

echo "== Observer dependency closure =="
for dep in \
  org.eclipse.emf.common \
  org.eclipse.emf.ecore \
  org.eclipse.emf.ecore.xmi \
  org.eclipse.viatra.examples.cps.model \
  org.eclipse.viatra.examples.cps.deployment \
  org.eclipse.viatra.examples.cps.traceability
do
  grep -Fq "$dep" "$OBSERVER_MANIFEST"
done

echo "== OSGi version compatibility =="
grep -Fq 'org.eclipse.viatra.examples.cps.model;bundle-version="0.1.0"' "$OBSERVER_MANIFEST"
grep -Fq 'org.eclipse.viatra.examples.cps.deployment;bundle-version="0.1.0"' "$OBSERVER_MANIFEST"
grep -Fq 'org.eclipse.viatra.examples.cps.traceability;bundle-version="0.1.0"' "$OBSERVER_MANIFEST"
grep -Fq 'Bundle-Version: 2.1.0.qualifier' cps-models/org.eclipse.viatra.examples.cps.model/META-INF/MANIFEST.MF
grep -Fq 'Bundle-Version: 2.1.0.qualifier' cps-models/org.eclipse.viatra.examples.cps.deployment/META-INF/MANIFEST.MF
grep -Fq 'Bundle-Version: 2.1.0.qualifier' cps-models/org.eclipse.viatra.examples.cps.traceability/META-INF/MANIFEST.MF

echo "== Historical model-bundle dependency closure =="
for bundle in \
  org.eclipse.viatra.examples.cps.model \
  org.eclipse.viatra.examples.cps.deployment
do
  grep -Fq 'org.eclipse.core.runtime' "cps-models/$bundle/META-INF/MANIFEST.MF"
  grep -Fq 'org.eclipse.emf.ecore;visibility:=reexport' "cps-models/$bundle/META-INF/MANIFEST.MF"
done
grep -Fq 'org.eclipse.viatra.examples.cps.model;bundle-version="0.1.0";visibility:=reexport' cps-models/org.eclipse.viatra.examples.cps.traceability/META-INF/MANIFEST.MF
grep -Fq 'org.eclipse.viatra.examples.cps.deployment;bundle-version="0.1.0";visibility:=reexport' cps-models/org.eclipse.viatra.examples.cps.traceability/META-INF/MANIFEST.MF
grep -Fq 'org.eclipse.emf.ecore;visibility:=reexport' cps-models/org.eclipse.viatra.examples.cps.traceability/META-INF/MANIFEST.MF

echo "== Target immutability =="
test "$(git hash-object target-definition/org.eclipse.viatra.examples.cps.target.target)" = "$TARGET_BLOB_SHA"

echo "BUILD_READINESS_PREFLIGHT=PASS"
