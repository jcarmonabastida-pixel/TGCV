#!/usr/bin/env bash
set -euo pipefail

SOURCE_REPO="https://github.com/eclipse-viatra/org.eclipse.viatra.examples.git"
SOURCE_REV="eb68158a3d74581f69ccb8bc4f47673b12abdf85"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEST_ROOT="$SCRIPT_DIR/cps-models"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

git clone --no-checkout --filter=blob:none "$SOURCE_REPO" "$TMP_DIR/source"
git -C "$TMP_DIR/source" sparse-checkout init --cone
git -C "$TMP_DIR/source" sparse-checkout set \
  cps/domains/org.eclipse.viatra.examples.cps.model \
  cps/domains/org.eclipse.viatra.examples.cps.deployment \
  cps/domains/org.eclipse.viatra.examples.cps.traceability
git -C "$TMP_DIR/source" checkout --detach "$SOURCE_REV"

test "$(git -C "$TMP_DIR/source" rev-parse HEAD)" = "$SOURCE_REV"

for bundle in \
  org.eclipse.viatra.examples.cps.model \
  org.eclipse.viatra.examples.cps.deployment \
  org.eclipse.viatra.examples.cps.traceability
do
  src="$TMP_DIR/source/cps/domains/$bundle"
  dst="$DEST_ROOT/$bundle"

  test -d "$src/META-INF"
  test -f "$src/META-INF/MANIFEST.MF"
  test -f "$src/build.properties"
  test -d "$src/model"
  test -d "$src/src"
  test -f "$src/plugin.xml"
  test -f "$src/plugin.properties"

  rm -rf "$dst/META-INF" "$dst/model" "$dst/src" "$dst/plugin.xml" "$dst/plugin.properties" "$dst/build.properties"
  mkdir -p "$dst"

  cp -R "$src/META-INF" "$dst/META-INF"
  cp -R "$src/model" "$dst/model"
  cp -R "$src/src" "$dst/src"
  cp "$src/plugin.xml" "$dst/plugin.xml"
  cp "$src/plugin.properties" "$dst/plugin.properties"
  cp "$src/build.properties" "$dst/build.properties"
done
