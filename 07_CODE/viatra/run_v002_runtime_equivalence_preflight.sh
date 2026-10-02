#!/usr/bin/env bash
set -euo pipefail

CORE_REVISION="${1:?core revision required}"
EXAMPLES_REVISION="${2:?examples revision required}"
FIXTURE_DIR="${3:?fixture directory required}"
RESULT="${4:?result path required}"

EXPECTED_CORE="6f7d2d7860ed901c33029700387d3535bd2553f1"
EXPECTED_EXAMPLES="15f269dbf74000eac7b97cf7f92e256b8fb1fc1c"

test "$CORE_REVISION" = "$EXPECTED_CORE"
test "$EXAMPLES_REVISION" = "$EXPECTED_EXAMPLES"

EXAMPLES_DIR="${GITHUB_WORKSPACE}/_viatra-examples"
HARNESS_DIR="$EXAMPLES_DIR/cps/tests/org.eclipse.viatra.examples.cps.xform.m2m.tgcv.preflight"
HARNESS_SRC="$HARNESS_DIR/src/org/eclipse/viatra/examples/cps/xform/m2m/tgcv"
HARNESS_CLASS="$HARNESS_SRC/TGCVV002RuntimeEquivalencePreflightTest.java"
HARNESS_POM="$HARNESS_DIR/pom.xml"
HARNESS_MANIFEST="$HARNESS_DIR/META-INF/MANIFEST.MF"
HARNESS_BUILD="$HARNESS_DIR/build.properties"

mkdir -p "$HARNESS_SRC" "$HARNESS_DIR/META-INF"
cp "$(dirname "$0")/TGCVV002RuntimeEquivalencePreflightTest.java" "$HARNESS_CLASS"

cat > "$HARNESS_POM" <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>org.eclipse.viatra.examples.cps</groupId>
    <artifactId>org.eclipse.viatra.examples.cps.parent</artifactId>
    <version>2.9.0-SNAPSHOT</version>
    <relativePath>../../pom.xml</relativePath>
  </parent>
  <artifactId>org.eclipse.viatra.examples.cps.xform.m2m.tgcv.preflight</artifactId>
  <packaging>eclipse-test-plugin</packaging>
</project>
EOF

cat > "$HARNESS_MANIFEST" <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: TGCV VIATRA V002 Runtime Equivalence Preflight
Bundle-SymbolicName: org.eclipse.viatra.examples.cps.xform.m2m.tgcv.preflight
Bundle-Version: 1.0.0.qualifier
Require-Bundle: org.junit,
 org.eclipse.emf.ecore.xmi,
 org.eclipse.viatra.examples.cps.model,
 org.eclipse.viatra.examples.cps.deployment,
 org.eclipse.viatra.examples.cps.traceability,
 org.eclipse.viatra.examples.cps.xform.m2m.incr.expl,
 org.eclipse.viatra.query.runtime,
 org.eclipse.viatra.query.runtime.emf
Bundle-RequiredExecutionEnvironment: JavaSE-11
EOF

cat > "$HARNESS_BUILD" <<'EOF'
source.. = src/
output.. = bin/
bin.includes = META-INF/,               .
EOF

python3 - <<'PY'
from pathlib import Path
p = Path("cps/pom.xml")
s = p.read_text()
module = "tests/org.eclipse.viatra.examples.cps.xform.m2m.tgcv.preflight"
if module not in s:
    s = s.replace("\t\t<module>tests/org.eclipse.viatra.examples.cps.xform.m2m.tests</module>",
                  "\t\t<module>tests/org.eclipse.viatra.examples.cps.xform.m2m.tests</module>\n\t\t<module>"+module+"</module>")
    p.write_text(s)
PY

export TGCV_VIATRA_FIXTURE_DIR="$FIXTURE_DIR"
export TGCV_VIATRA_RESULT="$GITHUB_WORKSPACE/$RESULT"
export TGCV_VIATRA_CORE_REVISION="$CORE_REVISION"
export TGCV_VIATRA_EXAMPLES_REVISION="$EXAMPLES_REVISION"

cleanup() {
  rm -rf "$HARNESS_DIR"
  git -C "$EXAMPLES_DIR" checkout -- cps/pom.xml >/dev/null 2>&1 || true
}
trap cleanup EXIT

cd "$EXAMPLES_DIR"

mvn -B -f cps/pom.xml \
  -pl tests/org.eclipse.viatra.examples.cps.xform.m2m.tgcv.preflight \
  -am verify \
  -Dtest=TGCVV002RuntimeEquivalencePreflightTest
