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
test -f target-definition/tgcv-viatra-v002-target.target
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
  grep -Fq "<version>2.1.0-SNAPSHOT</version>" "$b/pom.xml"
  grep -Fq "<artifactId>tgcv-viatra-v002-cps-models</artifactId>" "$b/pom.xml"
done

echo "== Historical source revision provenance =="
grep -Fq "$SOURCE_REV" materialize-historical-cps-models.sh

echo "== Target-platform configuration placement =="
grep -Fq '<artifactId>tycho-maven-plugin</artifactId>' pom.xml
! grep -Fq '<artifactId>target-platform-configuration</artifactId>' pom.xml
grep -Fq '<artifactId>target-platform-configuration</artifactId>' cps-models/pom.xml
grep -Fq '<version>${parent.version}</version>' cps-models/pom.xml
grep -Fq '<artifactId>target-platform-configuration</artifactId>' observer/pom.xml
! grep -Fq '<relativePath>target-definition/pom.xml</relativePath>' cps-models/pom.xml
! grep -Fq '<relativePath>target-definition/pom.xml</relativePath>' observer/pom.xml

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


echo "== Build closure audit =="

ROOT_GROUP_ID="$(sed -n 's:.*<groupId>\\([^<]*\\)</groupId>.*:\\1:p' pom.xml | head -n1)"
ROOT_ARTIFACT_ID="$(sed -n 's:.*<artifactId>\\([^<]*\\)</artifactId>.*:\\1:p' pom.xml | head -n1)"
ROOT_VERSION="$(sed -n 's:.*<version>\\([^<]*\\)</version>.*:\\1:p' pom.xml | head -n1)"

TARGET_GROUP_ID="$(grep -B20 -A20 '<artifactId>tgcv-viatra-v002-target</artifactId>' target-definition/pom.xml | sed -n 's:.*<groupId>\\([^<]*\\)</groupId>.*:\\1:p' | tail -n1)"
TARGET_ARTIFACT_ID="$(grep -B20 -A20 '<artifactId>tgcv-viatra-v002-target</artifactId>' target-definition/pom.xml | sed -n 's:.*<artifactId>\\([^<]*\\)</artifactId>.*:\\1:p' | tail -n1)"
TARGET_VERSION="$(grep -B20 -A20 '<artifactId>tgcv-viatra-v002-target</artifactId>' target-definition/pom.xml | sed -n 's:.*<version>\\([^<]*\\)</version>.*:\\1:p' | tail -n1)"

test "$ROOT_GROUP_ID" = "org.tgcv"
test "$ROOT_ARTIFACT_ID" = "viatra-v002-observer-host"
test "$ROOT_VERSION" = "0.1.0-SNAPSHOT"
test "$TARGET_GROUP_ID" = "$ROOT_GROUP_ID"
test "$TARGET_ARTIFACT_ID" = "tgcv-viatra-v002-target"
test "$TARGET_VERSION" = "$ROOT_VERSION"

for consumer in cps-models observer
do
  grep -Fq '<groupId>org.tgcv</groupId>' "$consumer/pom.xml"
  grep -Fq '<artifactId>tgcv-viatra-v002-target</artifactId>' "$consumer/pom.xml"
  grep -Fq '<version>${parent.version}</version>' "$consumer/pom.xml"
  ! grep -Fq '<version>${project.version}</version>' "$consumer/pom.xml"
done

test "$(grep -Fc '<artifactId>tgcv-viatra-v002-target</artifactId>' cps-models/pom.xml)" = "1"
test "$(grep -Fc '<artifactId>tgcv-viatra-v002-target</artifactId>' observer/pom.xml)" = "1"

for bundle in   org.eclipse.viatra.examples.cps.model   org.eclipse.viatra.examples.cps.deployment   org.eclipse.viatra.examples.cps.traceability
do
  grep -Fq '<version>2.1.0-SNAPSHOT</version>' "cps-models/$bundle/pom.xml"
  grep -Fq 'Bundle-Version: 2.1.0.qualifier' "cps-models/$bundle/META-INF/MANIFEST.MF"
done

echo "== Reactor artifact identity closure =="

for bundle in   org.eclipse.viatra.examples.cps.model   org.eclipse.viatra.examples.cps.deployment   org.eclipse.viatra.examples.cps.traceability
do
  test "$(grep -Fc "<artifactId>$bundle</artifactId>" "cps-models/$bundle/pom.xml")" = "1"
  test "$(grep -Fc "<module>$bundle</module>" cps-models/pom.xml)" = "1"
done

echo "== Target filename/artifact identity closure =="

test -f "target-definition/$TARGET_ARTIFACT_ID.target"
test "$(find target-definition -maxdepth 1 -type f -name '*.target' | wc -l)" = "1"

echo "== No unresolved target-coordinate interpolation =="

! grep -R -Fq '<version>${project.version}</version>' cps-models observer
grep -R -Fq '<version>${parent.version}</version>' cps-models observer

echo "== Target immutability =="
test "$(git hash-object target-definition/tgcv-viatra-v002-target.target)" = "$TARGET_BLOB_SHA"

echo "BUILD_READINESS_PREFLIGHT=PASS"
