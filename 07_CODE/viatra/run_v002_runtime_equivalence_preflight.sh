#!/usr/bin/env bash
set -euo pipefail

CORE_REVISION="${1:?core revision required}"
EXAMPLES_REVISION="${2:?examples revision required}"
FIXTURE_DIR="${3:?fixture directory required}"
RESULT="${4:?result path required}"

EXPECTED_CORE="ffa111dbb160c0bc55e89ea16430e97a38908662"
EXPECTED_EXAMPLES="15f269dbf74000eac7b97cf7f92e256b8fb1fc1c"

test "$CORE_REVISION" = "$EXPECTED_CORE"
test "$EXAMPLES_REVISION" = "$EXPECTED_EXAMPLES"

EXAMPLES_DIR="${GITHUB_WORKSPACE}/_viatra-examples"
TEST_SRC="$EXAMPLES_DIR/cps/tests/org.eclipse.viatra.examples.cps.xform.m2m.tests/src/org/eclipse/viatra/examples/cps/xform/m2m/tests/tgcv"
TEST_CLASS="$TEST_SRC/TGCVV002RuntimeEquivalencePreflightTest.java"

mkdir -p "$TEST_SRC"
cp "$(dirname "$0")/TGCVV002RuntimeEquivalencePreflightTest.java" "$TEST_CLASS"

export TGCV_VIATRA_FIXTURE_DIR="$FIXTURE_DIR"
export TGCV_VIATRA_RESULT="$GITHUB_WORKSPACE/$RESULT"

cleanup() {
  rm -f "$TEST_CLASS"
}
trap cleanup EXIT

cd "$EXAMPLES_DIR"

mvn -B -pl cps/tests/org.eclipse.viatra.examples.cps.xform.m2m.tests \
  -am test \
  -Dtest=TGCVV002RuntimeEquivalencePreflightTest \
  -DfailIfNoTests=false
